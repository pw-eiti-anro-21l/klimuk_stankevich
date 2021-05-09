import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading
from std_msgs.msg import String
# from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState
from my_robot_interfaces.srv import InterPol
from math import *
from time import sleep

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

import matplotlib.pyplot as plt
import numpy as np

global shoulder_velocities
global elbow_velocities
global wrist_velocities
global time_line
global plot_flag
plot_flag = False

class jint(Node):
	def __init__(self):
		super().__init__('jint')
		namespace = ""
		self.srv = self.create_service(InterPol, 'interpol', self.interpol_callback)
		self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)

		self.declare_parameter("actual_shoulder", 0.0)
		self.declare_parameter("actual_elbow", 0.0)
		self.declare_parameter("actual_wrist", 0.0)

	def interpol_callback(self, request, response):
		global shoulder_velocities
		global elbow_velocities
		global wrist_velocities
		global time_line, plot_flag
		response.description = ''
		if abs(request.shoulder) > 1.57:
			response.description += 'Requested shoulder position is out of range. '
		if abs(request.elbow) > 1.57:
			response.description += 'Requested elbow position is out of range. '
		if  request.wrist < 0.00 or request.wrist > 0.50:
			response.description += 'Requested wrist position is out of range. '
		if  request.time <= 0:
			response.description += 'Requested time must be postive number. '
		if response.description:
			response.success = False
			return response
		else:
			actual_shoulder = self.get_parameter("actual_shoulder").value
			actual_elbow = self.get_parameter("actual_elbow").value
			actual_wrist = self.get_parameter("actual_wrist").value

			shoulder_distance = request.shoulder - actual_shoulder
			elbow_distance = request.elbow - actual_elbow
			wrist_distance = request.wrist - actual_wrist

			num_of_moves = int(request.time*100)

			lin_shoulder_step = shoulder_distance/num_of_moves
			lin_elbow_step = elbow_distance/num_of_moves
			lin_wrist_step = wrist_distance/num_of_moves

			shoulder_step = 0.0
			elbow_step = 0.0
			wrist_step = 0.0

			shoulder_velocities = []
			elbow_velocities = []
			wrist_velocities = []


			for i in range(0,num_of_moves):
				if request.velocity == 'linear':
					shoulder_velocities.append(abs(lin_shoulder_step*100))
					elbow_velocities.append(abs(lin_elbow_step*100))
					wrist_velocities.append(abs(lin_wrist_step*100))
					actual_shoulder += lin_shoulder_step
					actual_elbow += lin_elbow_step
					actual_wrist += lin_wrist_step
				else:
					shoulder_velocities.append(abs(shoulder_step*100))
					elbow_velocities.append(abs(elbow_step*100))
					wrist_velocities.append(abs(wrist_step*100))
					if request.velocity == 'triangle':
						shoulder_step_incr = (lin_shoulder_step*2)/int(num_of_moves/2)
						elbow_step_incr = (lin_elbow_step*2)/int(num_of_moves/2)
						wrist_step_incr = (lin_wrist_step*2)/int(num_of_moves/2)
						if i in range(0, int(num_of_moves/2)):
							shoulder_step += shoulder_step_incr
							elbow_step += elbow_step_incr
							wrist_step += wrist_step_incr
						elif i in range(int(num_of_moves/2), num_of_moves):
							shoulder_step -= shoulder_step_incr
							elbow_step -= elbow_step_incr
							wrist_step -= wrist_step_incr
					elif request.velocity == 'trapezoid':
						shoulder_step_incr = (lin_shoulder_step*1.5)/int(num_of_moves/3)
						elbow_step_incr = (lin_elbow_step*1.5)/int(num_of_moves/3)
						wrist_step_incr = (lin_wrist_step*1.5)/int(num_of_moves/3)
						if i in range(0, int(num_of_moves/3)):
							shoulder_step += shoulder_step_incr
							elbow_step += elbow_step_incr
							wrist_step += wrist_step_incr
						elif i in range(int(num_of_moves*(2/3)), num_of_moves):
							shoulder_step -= shoulder_step_incr
							elbow_step -= elbow_step_incr
							wrist_step -= wrist_step_incr


					actual_shoulder += shoulder_step
					actual_elbow += elbow_step
					actual_wrist += wrist_step


				new_shoulder = Parameter('actual_shoulder', Parameter.Type.DOUBLE, actual_shoulder)
				new_elbow = Parameter('actual_elbow', Parameter.Type.DOUBLE, actual_elbow)
				new_wrist = Parameter('actual_wrist', Parameter.Type.DOUBLE, actual_wrist)


				self.set_parameters([new_shoulder, new_elbow, new_wrist])
				self.post_actual_parameters()
				sleep_time = 0.007
				sleep(sleep_time)
			

			response.success = True
			response.description = "Interpolation completed."
			time_line = np.arange(0,request.time,0.01)
			plot_flag = True
			return response
			
	def post_actual_parameters(self):
		joint_state_msg = JointState()

		joint_state_msg.header.stamp = self.get_clock().now().to_msg()
		joint_state_msg.header.frame_id = ''
		joint_state_msg.name = ['shoulder', 'elbow', 'wrist_connector']

		joint_state_msg.position = [self.get_parameter("actual_shoulder").value, self.get_parameter("actual_elbow").value, self.get_parameter("actual_wrist").value]

		joint_state_msg.velocity = []
		joint_state_msg.effort = []

		self.publisher_.publish(joint_state_msg)

def plot_velocity(shoulder_velocities, elbow_velocities, wrist_velocities, time_line):
	global plot_flag
	plt.plot(time_line, shoulder_velocities)
	plt.plot(time_line, elbow_velocities)
	plt.plot(time_line, wrist_velocities)

	plt.xlabel('Time')

	plt.ylabel('Velocities')

	plt.title('Velocity compare')

	plt.legend(['Shoulder','Elbow','Wrist'])

	plot_flag = False

	plt.show()


def main(args=None):
	global shoulder_velocities
	global elbow_velocities
	global wrist_velocities
	global time_line, plot_flag
	print("Jint node is working")
	rclpy.init(args=args)
	node = jint()
	thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
	thread.start()
	rate = node.create_rate(100)
	try:
		while rclpy.ok():
			node.post_actual_parameters()
			if plot_flag == True:
				plot_velocity(shoulder_velocities, elbow_velocities, wrist_velocities, time_line)
			rate.sleep()
	except KeyboardInterrupt:
	    pass
	    rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()