import rclpy
from rclpy.node import Node
from geometry_msgs.msg  import Twist
from curtsies import Input
from rcl_interfaces.msg import ParameterDescriptor

class CustomControlNode(Node):
    def __init__(self):
        super().__init__('custom_control_node')
        self.velocity_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        

        # mf__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
        #                                               description='Key you press for moving forward')
        
        self.declare_parameter("moving_forward", 'i', mf__descriptor)
        
        # mb__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
        #                                               description='Key you press for moving moving_backwards')

        self.declare_parameter("moving_backwards", 'k', mb__descriptor)
        
        # rcckw__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
        #                                               description='Key you press for rotating counterclockwise')
        
        self.declare_parameter("rotating_cckw", 'i')

        # rckw__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
        #                                               description='Key you press for rotating_clockwise')

        self.declare_parameter("rotating_ckw", 'l')
	

    def move_in_circle(self):
        vel_msg = Twist()
        vel_msg.linear.x = 2.0
        vel_msg.angular.z = -1.8
        self.velocity_publisher.publish(vel_msg)
        print("I am moving")

def get_input_character():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            return e

def check_if_key_is_pressed(key):
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == key:
                print("You are pressing the right key")
            else:
                print("You are pressing the WRONG key")

def check_if_key_is_pressed(key):
    global node
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == key:
                print("You are pressing the right key")
                node.move_in_circle()
    	
def main(args=None):
    global node
    print("Node is working")
    rclpy.init(args=args)
    node = CustomControlNode()
    # for i in range(500):
    #     node.move()
    #     i += 1

    print("Press the key:")
    pressed_character = get_input_character()
    print(f"Your key is: {pressed_character}")
    check_if_key_is_pressed(pressed_character)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
