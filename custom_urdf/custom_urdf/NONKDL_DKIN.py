import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState
from quaternion import *


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

        # self.declare_parameter('received_timestamp', [])
        # self.declare_parameter('received_joint_state_elbow_pos', '')
        # self.declare_parameter('received_joint_state_shoulder_pos', '')
        # self.declare_parameter('received_joint_state_wrist_connector_pos', '')
        
        # self.declare_parameter('calculated_timestamp', [])
        # self.declare_parameter('calculated__id_arm', ['arm', 'forearm'])
        # self.declare_parameter('calculated_pose_arm', [])
        # self.declare_parameter('calculated__id_body', ['body', 'arm'])
        # self.declare_parameter('calculated_pose_body', [])
        # self.declare_parameter('calculated__id_connector', ['connector', 'hand'])
        # self.declare_parameter('calculated_pose_connector', [])




    def listener_callback(self, msg):
        #angle of shoulder: 
        shoulder_pos = msg.position[0]
        #angle of elbow:
        elbow_pos = msg.position[1]
        #position of wrist connector
        wrist_connector_pos = msg.position[2]

        q_shoulder = Quaternion()
        q_shoulder.calculate(0.0, 0.0, shoulder_pos)

        #create PoseStamped message
        self.posestamped_msg = PoseStamped()
        self.posestamped_msg.header.frame_id = 'body'
        self.posestamped_msg.header.stamp = self.get_clock().now().to_msg()

        #origin position of the shoulder, must be read from urdf:
        self.posestamped_msg.pose.position.x = self.get_parameter('joint_shoulder').value[0]
        self.posestamped_msg.pose.position.y = self.get_parameter('joint_shoulder').value[1]
        self.posestamped_msg.pose.position.z = self.get_parameter('joint_shoulder').value[2]

        #set orientation values
        self.posestamped_msg.pose.orientation.x = q_shoulder.x
        self.posestamped_msg.pose.orientation.y = q_shoulder.y
        self.posestamped_msg.pose.orientation.z = q_shoulder.z
        self.posestamped_msg.pose.orientation.w = q_shoulder.w

        self.nonkdl_pose_publisher.publish(self.posestamped_msg)


    

def main(args=None):
    global node
    rclpy.init(args=args)
    node = NONKDL_DKIN()

    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()
    rate = node.create_rate(10)
    try:
        while rclpy.ok():
            print("NONKDL_DKN node is working")
            rate.sleep()
    except KeyboardInterrupt:
        pass
        rclpy.spin(node)
    rclpy.shutdown()
    thread.join()