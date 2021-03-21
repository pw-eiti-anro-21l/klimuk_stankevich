import rclpy
from rclpy.node import Node
from curtsies import Input
from geometry_msgs.msg  import Twist
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType


class SterowanieZolwiem(Node):

    def __init__(self):
        super().__init__('sterowanie_zolwiem')
        self.publisher_ = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.new_velocity = Twist()
        self.declare_parameter('forward','w')
        self.declare_parameter('backwards','s')
        self.declare_parameter('left','a')
        self.declare_parameter('right','d')
        
    def move_forward(self):
    	self.new_velocity.linear.x = 1.0
    	self.new_velocity.angular.z = 0.0
    	self.publisher_.publish(self.new_velocity)

    def move_backwards(self):
    	self.new_velocity.linear.x = -1.0
    	self.new_velocity.angular.z = 0.0
    	self.publisher_.publish(self.new_velocity)

    def turn_left(self):
    	self.new_velocity.angular.z = 1.0
    	self.new_velocity.linear.x = 0.0
    	self.publisher_.publish(self.new_velocity)

    def turn_right(self):
    	self.new_velocity.angular.z = -1.0
    	self.new_velocity.linear.x = 0.0
    	self.publisher_.publish(self.new_velocity)

    def stop(self):
    	self.new_velocity.angular.z = 0.0
    	self.new_velocity.linear.x = 0.0
    	self.publisher_.publish(self.new_velocity)

    def get_key(self):
    	with Input(keynames='curtsies') as input_generator:
    		for e in Input():
    			return e

    def move_control(self):
    	key = self.get_key()
    	if key == self.get_parameter('forward').get_parameter_value().string_value:
    		self.move_forward()
    	elif key == self.get_parameter('backwards').get_parameter_value().string_value:
    		self.move_backwards()
    	elif key == self.get_parameter('left').get_parameter_value().string_value:
    		self.turn_left()
    	elif key == self.get_parameter('right').get_parameter_value().string_value:
    		self.turn_right()







    


def main(args=None):
    rclpy.init(args=args)

    sterowanie_zolwiem = SterowanieZolwiem()

    while(True):
        sterowanie_zolwiem.move_control()


    rclpy.spin(sterowanie_zolwiem)

    rclpy.shutdown()


if __name__ == '__main__':
    main()