import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState
from quaternion import *
from PyKDL import *

class KDL_DKIN(Node):
    def __init__(self):
        super().__init__('KDL_DKIN')
        namespace=""
        
        self.kdl_joint_state_subscription = self.create_subscription(JointState,'/joint_states', self.listener_callback, 10)
        self.kdl_pose_publisher = self.create_publisher(PoseStamped, '/kdl_pose_topic', 10)
        self.kdl_joint_state_subscription
        
        self.declare_parameter("joint_fixed", None)
        self.declare_parameter("joint_shoulder", None)
        self.declare_parameter("joint_elbow", None)
        self.declare_parameter("joint_wrist", None)
        self.declare_parameter("joint_fixed_end", None)
        self.declare_parameter("joint_wrist_connector", None)

        self.declare_parameter("table_row_1", None)
        self.declare_parameter("table_row_2", None)
        self.declare_parameter("table_row_3", None)

    def listener_callback(self, msg):
        #angle of shoulder: 
        shoulder_pos = msg.position[0]
        #angle of elbow:
        elbow_pos = msg.position[1]
        #position of wrist connector
        wrist_connector_pos = msg.position[2]
        init_pos = Vector(0.0, 0.0, 0.0)
        init_rot = Rotation(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
        frame = Frame(init_rot, init_pos)

        #angle of shoulder: 
        shoulder_pos = msg.position[0]
        #angle of elbow:
        elbow_pos = msg.position[1]
        #position of wrist connector
        wrist_connector_pos = msg.position[2]
        init_pos = Vector(0,0,0)
        init_rot = Rotation(1,0,0,0,1,0,0,0,1)
        frame = Frame(init_rot, init_pos)

        #1 step
        frame.p += Vector(self.get_parameter('joint_shoulder').value[0],self.get_parameter('joint_shoulder').value[1],self.get_parameter('joint_shoulder').value[2])
        #2 step
        frame.M.DoRotZ(shoulder_pos)
        #3 step
        #frame.p += Vector(self.get_parameter('joint_elbow').value[0],self.get_parameter('joint_elbow').value[1],self.get_parameter('joint_elbow').value[2])

        #4 step
        rotmat = Rotation()
        rotmat.DoRotZ(shoulder_pos)
        #newFrameP = rotmat*frame.p
        #frame.p = newFrameP

        #5 step
        frame.M.DoRotZ(elbow_pos)
        #6 step
        #frame.p += Vector(self.get_parameter('joint_wrist').value[0],self.get_parameter('joint_wrist').value[1],self.get_parameter('joint_wrist').value[2])

        #7 step
        rotmat2 = Rotation()
        rotmat2.DoRotZ(elbow_pos)
        #newFrameP = rotmat*Vector(1,0,1.5)
        p1 = Vector(self.get_parameter('joint_elbow').value[0]*cos(elbow_pos),self.get_parameter('joint_elbow').value[0]*sin(elbow_pos),self.get_parameter('joint_shoulder').value[2])
        d = Vector(self.get_parameter('joint_wrist').value[0]*cos(shoulder_pos),self.get_parameter('joint_wrist').value[0]*sin(shoulder_pos),0)
        frame.p = rotmat*p1 + d

        q = frame.M.GetQuaternion()

        #create PoseStamped message
        self.posestamped_msg = PoseStamped()
        self.posestamped_msg.header.frame_id = 'world'
        self.posestamped_msg.header.stamp = self.get_clock().now().to_msg()

        #origin position of the shoulder, must be read from urdf:
        self.posestamped_msg.pose.position.x = frame.p.x()
        self.posestamped_msg.pose.position.y = frame.p.y()
        self.posestamped_msg.pose.position.z = frame.p.z()

        #set orientation values
        self.posestamped_msg.pose.orientation.x = q[0]
        self.posestamped_msg.pose.orientation.y = q[1]
        self.posestamped_msg.pose.orientation.z = q[2]
        self.posestamped_msg.pose.orientation.w = q[3]

        self.kdl_pose_publisher.publish(self.posestamped_msg)

        # print(frame.p.x())


def main(args=None):
    global node
    rclpy.init(args=args)
    node = KDL_DKIN()
    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()
    rate = node.create_rate(10)
    print("KDL_DKN node is working")
    try:
        while rclpy.ok():
            rate.sleep()
    except KeyboardInterrupt:
        pass
        rclpy.spin(node)
    rclpy.shutdown()
    thread.join()