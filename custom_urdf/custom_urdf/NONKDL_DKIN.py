import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState
from quaternion import *
from matrix import *


class NONKDL_DKIN(Node):
    def __init__(self):
        super().__init__('NONKDL_DKIN')
        namespace=""
        
        self.nonkdl_joint_state_subscription = self.create_subscription(JointState,'/joint_states', self.listener_callback, 10)
        self.nonkdl_pose_publisher = self.create_publisher(PoseStamped, '/nonkdl_pose_topic', 10)
        self.nonkdl_joint_state_subscription
        
        self.declare_parameter("joint_fixed", None)
        self.declare_parameter("joint_shoulder", None)
        self.declare_parameter("joint_elbow", None)
        self.declare_parameter("joint_wrist", None)
        self.declare_parameter("joint_fixed_end", None)
        self.declare_parameter("joint_wrist_connector", None)



    def listener_callback(self, msg):
        #angle of shoulder: 
        shoulder_pos = msg.position[0]
        #angle of elbow:
        elbow_pos = msg.position[1]
        #position of wrist connector
        wrist_connector_pos = msg.position[2]


        T0 = Translation()
        T0.set_matrix_z(self.get_parameter('joint_shoulder').value[2])
        T1 = Translation()
        T1.set_matrix_yawl(shoulder_pos)
        T2 = Translation()
        T2.set_matrix_x(self.get_parameter('joint_elbow').value[0])
        T3 = Translation()
        T3.set_matrix_yawl(elbow_pos)
        T4 = Translation()
        T4.set_matrix_x(self.get_parameter('joint_wrist').value[0])
        T5 = Translation()
        T5.set_matrix_z(self.get_parameter('joint_fixed_end').value[0])
        T6 = Translation()
        T6.set_matrix_z(wrist_connector_pos)


        T01 = T0 * T1
        T02 = T01 * T2 
        T03 = T02 * T3
        T04 = T03 * T4
        T05 = T04 * T5
        T06 = T05 * T6

        q_shoulder = Quaternion()
        q_shoulder.calculate(T01.calculate_roll(),T01.calculate_pitch(), T01.calculate_yawl())

        q_elbow = Quaternion()
        q_elbow.calculate(T03.calculate_roll(),T03.calculate_pitch(),T03.calculate_yawl())

        q_wrist = Quaternion()
        q_wrist.calculate(T04.calculate_roll(),T04.calculate_pitch(),T04.calculate_yawl())

        q_hand = Quaternion()
        q_hand.calculate(T06.calculate_roll(),T06.calculate_pitch(),T06.calculate_yawl())

        #create PoseStamped message
        self.posestamped_msg = PoseStamped()
        self.posestamped_msg.header.frame_id = 'world'
        self.posestamped_msg.header.stamp = self.get_clock().now().to_msg()

        #origin position of the shoulder, must be read from urdf:
        self.posestamped_msg.pose.position.x = T06.matrix[0][3]
        self.posestamped_msg.pose.position.y = T06.matrix[1][3]
        self.posestamped_msg.pose.position.z = T06.matrix[2][3]

        #set orientation values
        self.posestamped_msg.pose.orientation.x = q_hand.x
        self.posestamped_msg.pose.orientation.y = q_hand.y
        self.posestamped_msg.pose.orientation.z = q_hand.z
        self.posestamped_msg.pose.orientation.w = q_hand.w

        self.nonkdl_pose_publisher.publish(self.posestamped_msg)


    

def main(args=None):
    global node
    rclpy.init(args=args)
    node = NONKDL_DKIN()

    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()
    rate = node.create_rate(10)
    print("NONKDL_DKN node is working")
    try:
        while rclpy.ok():
            rate.sleep()
    except KeyboardInterrupt:
        pass
        rclpy.spin(node)
    rclpy.shutdown()
    thread.join()