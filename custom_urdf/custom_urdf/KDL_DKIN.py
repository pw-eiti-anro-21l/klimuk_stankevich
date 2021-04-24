import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState
from quaternion import *

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