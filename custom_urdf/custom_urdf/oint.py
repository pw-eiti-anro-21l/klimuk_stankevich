import rclpy
from rclpy.node import Node
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

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

class oint(Node):
	def __init__(self):
		super().__init__('oint')
		namespace = ""

		self.srv = self.create_service(InterPol2, 'interpol2', self.interpol2_callback)
		self.publisher_ = self.create_publisher(PoseStamped, '/oint_position', 10)
		self.marker_publisher = self.create_publisher(MarkerArray, '/marker_topic_oint', 1)
		self.markers = MarkerArray()

		self.declare_parameter("actual_posx", 0.0)
		self.declare_parameter("actual_posy", 0.0)
		self.declare_parameter("actual_posz", 0.0)

		self.declare_parameter("actual_orx", 0.0)
		self.declare_parameter("actual_ory", 0.0)
		self.declare_parameter("actual_orz", 0.0)
		self.declare_parameter("actual_orw", 1.0)



	def interpol2_callback(self, request, response):
		response.description = ''
		if  request.time <= 0:
			response.description += 'Requested time must be postive number. '
		if response.description:
			response.success = False
			return response
		else:
			actual_posx = self.get_parameter("actual_posx").value
			actual_posy = self.get_parameter("actual_posy").value
			actual_posz = self.get_parameter("actual_posz").value

			actual_orx = self.get_parameter("actual_orx").value
			actual_ory = self.get_parameter("actual_ory").value
			actual_orz = self.get_parameter("actual_orz").value			
			actual_orw = self.get_parameter("actual_orw").value

			posx_distance = request.posx - actual_posx
			posy_distance = request.posy - actual_posy
			posz_distance = request.posz - actual_posz

			request_orientation = Quaternion()
			request_orientation.calculate(request.r,request.p,request.y)

			orx_distance = request_orientation.x - actual_orx
			ory_distance = request_orientation.y - actual_ory
			orz_distance = request_orientation.z - actual_orz
			orw_distance = request_orientation.w - actual_orw

			num_of_moves = int(request.time*100)

			posx_step = posx_distance/num_of_moves
			posy_step = posy_distance/num_of_moves
			posz_step = posz_distance/num_of_moves

			orx_step = orx_distance/num_of_moves
			ory_step = ory_distance/num_of_moves
			orz_step = orz_distance/num_of_moves
			orw_step = orw_distance/num_of_moves

			for i in range(0,num_of_moves):
				actual_posx += posx_step
				actual_posy += posy_step
				actual_posz += posz_step

				actual_orx += orx_step
				actual_ory += ory_step
				actual_orz += orz_step
				actual_orw += orw_step

				new_posx = Parameter('actual_posx', Parameter.Type.DOUBLE, actual_posx)
				new_posy = Parameter('actual_posy', Parameter.Type.DOUBLE, actual_posy)
				new_posz = Parameter('actual_posz', Parameter.Type.DOUBLE, actual_posz)

				new_orx = Parameter('actual_orx', Parameter.Type.DOUBLE, actual_orx)
				new_ory = Parameter('actual_ory', Parameter.Type.DOUBLE, actual_ory)
				new_orz = Parameter('actual_orz', Parameter.Type.DOUBLE, actual_orz)
				new_orw = Parameter('actual_orw', Parameter.Type.DOUBLE, actual_orw)

				self.set_parameters([new_posx, new_posy, new_posz, new_orx, new_ory, new_orz, new_orw])
				self.post_actual_parameters()
				sleep_time = 0.00000001
				sleep(sleep_time)


			



			response.success = True
			response.description = "Interpolation completed."
			return response



	def post_actual_parameters(self):
		#create PoseStamped message
		self.posestamped_msg = PoseStamped()
		self.posestamped_msg.header.frame_id = 'map'
		self.posestamped_msg.header.stamp = self.get_clock().now().to_msg()

		#origin position of the shoulder, must be read from urdf:
		self.posestamped_msg.pose.position.x = self.get_parameter("actual_posx").value
		self.posestamped_msg.pose.position.y = self.get_parameter("actual_posy").value
		self.posestamped_msg.pose.position.z = self.get_parameter("actual_posz").value

		#set orientation values
		self.posestamped_msg.pose.orientation.x = self.get_parameter("actual_orx").value
		self.posestamped_msg.pose.orientation.y = self.get_parameter("actual_ory").value
		self.posestamped_msg.pose.orientation.z = self.get_parameter("actual_orz").value
		self.posestamped_msg.pose.orientation.w = self.get_parameter("actual_orw").value

		point = Point()
		point.x = self.get_parameter("actual_posx").value
		point.y = self.get_parameter("actual_posy").value
		point.z = self.get_parameter("actual_posz").value
		pose = Pose()
		pose.position = point
		pose.orientation.x = self.get_parameter("actual_orx").value
		pose.orientation.y = self.get_parameter("actual_ory").value
		pose.orientation.z = self.get_parameter("actual_orz").value
		pose.orientation.w = self.get_parameter("actual_orw").value

		marker = Marker()
		marker.header.stamp = self.get_clock().now().to_msg()
		marker.header.frame_id = "/map"
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


		self.publisher_.publish(self.posestamped_msg)

def main(args=None):
	print("Oint node is working")
	rclpy.init(args=args)
	node = oint()
	thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
	thread.start()
	rate = node.create_rate(100)
	try:
		while rclpy.ok():
			node.post_actual_parameters()
			rate.sleep()
	except KeyboardInterrupt:
		pass
		rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()