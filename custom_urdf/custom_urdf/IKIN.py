import rclpy
from rclpy.node import Node


# from sensor_msgs.msg import JointState
# from geometry_msgs.msg import PoseStamped
# import math
# from math import *

from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Pose, Point
from sensor_msgs.msg import JointState
from my_robot_interfaces.srv import InterPol, InterPol2
from quaternion import *
from matrix import *
from math import *
from time import sleep

global arm
arm = None
global forearm
forearm = None
global body
body = None
global wrist
wrist = None

class IKIN(Node):
    global arm, forearm, body, wrist

    def __init__(self):
        super().__init__('IKIN')
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        self.subscription_ = self.create_subscription(PoseStamped, '/oint_position', self.IKIN_callback, 10)
        self.subscription_

        self.declare_parameter("joint_fixed", None)
        self.declare_parameter("joint_shoulder", None)
        self.declare_parameter("joint_elbow", None)
        self.declare_parameter("joint_wrist", None)
        self.declare_parameter("joint_fixed_end", None)
        self.declare_parameter("joint_wrist_connector", None)
        self.declare_parameter('arm', None);
        self.declare_parameter('forearm', None);
        self.declare_parameter('body', None);
        self.declare_parameter('wrist', None);

    def IKIN_callback(self, msg):
        global arm, forearm, body, wrist     
        x = msg.pose.position.x
        y = msg.pose.position.y
        z = msg.pose.position.z

        elbow = acos(round(( x**2 + y**2 - arm**2 - forearm**2 )/(2*arm*forearm), 5))
        shoulder = atan(round((y/x),5)) - asin(round(forearm*sin(elbow)/sqrt(x**2 + y**2), 5))

        wrist_connector = z - body + wrist

        if x <= 0:
            shoulder += pi
            if shoulder > pi:
                shoulder -= 2*pi

        js_msg = JointState()

        js_msg.header.stamp = self.get_clock().now().to_msg()
        js_msg.header.frame_id = ''

        js_msg.name = ['shoulder', 'elbow', 'wrist_connector']

        js_msg.position = [shoulder, elbow, wrist_connector]

        js_msg.velocity = []
        js_msg.effort = []

        self.publisher_.publish(js_msg)



def main(args=None):
    global arm, forearm, body, wrist
    print("IKIN node is working")
    rclpy.init(args=args)
    node = IKIN()
    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()
    rate = node.create_rate(100)
    try:
        while rclpy.ok():
            if arm == None and forearm == None and body == None and wrist == None:
                arm = node.get_parameter('joint_elbow').value[0]
                forearm = node.get_parameter('joint_wrist').value[0]
                body = node.get_parameter('joint_shoulder').value[2]
                wrist = abs(node.get_parameter('joint_fixed_end').value[0])
            rate.sleep()
    except KeyboardInterrupt:
        pass
        rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
