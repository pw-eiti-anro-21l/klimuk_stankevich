import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Pose, Point
from sensor_msgs.msg import JointState
from quaternion import *
from PyKDL import *
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray



class Trajectory_poster(Node):
    def __init__(self):
        super().__init__('Trajectory_poster')
        namespace=""
        
        self.trajectory_poster_subscription = self.create_subscription(JointState,'/joint_states', self.listener_callback, 10)
        self.trajectory_poster_subscription
        self.marker_publisher = self.create_publisher(MarkerArray, '/marker_topic_jint', 1)
        self.markers = MarkerArray()

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
        global previous_point
        #angle of shoulder: 
        shoulder_pos = msg.position[0]
        #angle of elbow:
        elbow_pos = msg.position[1]
        #position of wrist connector
        wrist_connector_pos = msg.position[2]
        init_pos = Vector(0,0,0)
        init_rot = Rotation(1,0,0,0,1,0,0,0,1)
        frame = Frame(init_rot, init_pos)

        #Position calculation:
        frame.p += Vector(self.get_parameter('joint_shoulder').value[0],self.get_parameter('joint_shoulder').value[1],self.get_parameter('joint_shoulder').value[2])

        rotmat = Rotation()
        rotmat.DoRotZ(shoulder_pos)

        rotmat2 = Rotation()
        rotmat2.DoRotZ(elbow_pos)

        p1 = rotmat2*Vector(self.get_parameter('joint_wrist').value[0],0,self.get_parameter('joint_shoulder').value[2])
        d = rotmat*Vector(self.get_parameter('joint_elbow').value[0],self.get_parameter('joint_elbow').value[1],self.get_parameter('joint_elbow').value[2])
        frame.p = rotmat*p1 + d + Vector(0,0,self.get_parameter('joint_fixed_end').value[0]) + Vector(0,0,wrist_connector_pos)

        #Orientation calculation:
        frame.M.DoRotZ(shoulder_pos)
        frame.M.DoRotZ(elbow_pos)

        q = frame.M.GetQuaternion()

        point = Point()
        point.x = frame.p.x()
        point.y = frame.p.y()
        point.z = frame.p.z()
        pose = Pose()
        pose.position = point
        pose.orientation.x = q[0]
        pose.orientation.y = q[1]
        pose.orientation.z = q[2]
        pose.orientation.w = q[3]

        marker = Marker()
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.header.frame_id = "/world"
        marker.type = 2
        marker.pose = pose
        marker.id = len(self.markers.markers) + 1
        marker.action = Marker.ADD
        marker.type = Marker.SPHERE
        marker.scale.x = 0.03
        marker.scale.y = 0.03
        marker.scale.z = 0.03
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 1.0

        self.markers.markers.append(marker)
        self.marker_publisher.publish(self.markers)

def main(args=None):
    global node
    rclpy.init(args=args)
    node = Trajectory_poster()
    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()
    rate = node.create_rate(10)
    print("Trajectory_poster node is working")
    try:
        while rclpy.ok():
            rate.sleep()
    except KeyboardInterrupt:
        pass
        rclpy.spin(node)
    rclpy.shutdown()
    thread.join()