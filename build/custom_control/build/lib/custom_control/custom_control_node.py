# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg  import Twist
# from curtsies import Input
# from rcl_interfaces.msg import ParameterType, ParameterDescriptor
# from rclpy.parameter import Parameter

# class CustomControlNode(Node):
#     def __init__(self):
#         super().__init__('custom_control_node')
#         self.velocity_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        

#         mf__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
#                                                       description='Key you press for moving forward')
        
#         self.declare_parameter("moving_forward", 'i', mf__descriptor)
        
#         mb__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
#                                                       description='Key you press for moving moving_backwards')

#         self.declare_parameter("moving_backwards", 'k', mb__descriptor)
        
#         rcckw__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
#                                                       description='Key you press for rotating counterclockwise')
        
#         self.declare_parameter("rotating_cckw", 'j', rcckw__descriptor)

#         rckw__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
#                                                       description='Key you press for rotating_clockwise')

#         self.declare_parameter("rotating_ckw", 'l', rckw__descriptor)


#     def move_forward(self):
#         vel_msg = Twist()
#         vel_msg.linear.x = 2.0
#         vel_msg.angular.z = 0.0
#         self.velocity_publisher.publish(vel_msg)

#     def move_backwards(self):
#         vel_msg = Twist()
#         vel_msg.linear.x = -2.0
#         vel_msg.angular.z = 0.0
#         self.velocity_publisher.publish(vel_msg)

#     def rotate_clockwise(self):
#         vel_msg = Twist()
#         vel_msg.linear.x = 0.0
#         vel_msg.angular.z = -2.0
#         self.velocity_publisher.publish(vel_msg)

#     def rotate_counterclockwise(self):
#         vel_msg = Twist()
#         vel_msg.linear.x = 0.0
#         vel_msg.angular.z = 2.0
#         self.velocity_publisher.publish(vel_msg)


# def get_key():
#     with Input(keynames='curses') as input_generator:
#         for e in input_generator:
#             return e

# def movement_choice(forward_key, backwards_key, counterclockwise_key, clockwise_key):
#     global node
#     with Input(keynames='curses') as input_generator:
#         for e in input_generator:
#             if e == forward_key:
#                 node.move_forward()
#             elif e == backwards_key:
#                 node.move_backwards()
#             elif e == counterclockwise_key:
#                 node.rotate_counterclockwise()
#             elif e == clockwise_key:
#                 node.rotate_clockwise()

# def process_user_choice(pressed_key):
#     pressed_key = pressed_key.lower()
#     if pressed_key == "y":
#         return True
#     elif pressed_key == "n":
#         return False

# def get_new_parameters():
#     print("Enter new keys:\nMoving forward:")
#     new_mf = get_key()
#     print(new_mf)
#     print("Moving backwards:")
#     new_mb = get_key()
#     print(new_mb)
#     print("Rotating Counterclockwise:")
#     new_rcckw = get_key()
#     print(new_rcckw)
#     print("Rotating Clockwise:")
#     new_rckw = get_key()
#     print(new_rckw)
#     return new_mf, new_mb, new_rcckw, new_rckw

# def change_parameters(node, new_param_list):
#     param_mf = Parameter('moving_forward', Parameter.Type.STRING, new_param_list[0])
#     param_mb = Parameter('moving_backwards', Parameter.Type.STRING, new_param_list[1])
#     param_rcckw = Parameter('rotating_cckw', Parameter.Type.STRING, new_param_list[2])
#     param_rckw = Parameter('rotating_ckw', Parameter.Type.STRING, new_param_list[3])
#     node.set_parameters([param_mf, param_mb, param_rcckw, param_rckw])

# def get_nodes_parameters(node):
#     mf_key = node.get_parameter('moving_forward').value 
#     mb_key = node.get_parameter('moving_backwards').value
#     rcckw_key = node.get_parameter('rotating_cckw').value
#     rckw_key = node.get_parameter('rotating_ckw').value
#     return mf_key, mb_key, rcckw_key, rckw_key
    	
# def main(args=None):
#     global node
#     rclpy.init(args=args)
#     node = CustomControlNode()
#     default_parameters = get_nodes_parameters(node)
#     print(f"Default keys for controlling: {default_parameters[0]}, {default_parameters[1]}, {default_parameters[2]}, {default_parameters[3]}")
#     print("Do you want to change them?(y/n)")
#     user_choice = process_user_choice(get_key())
#     if user_choice == True:
#         new_params = get_new_parameters()
#         change_parameters(node, new_params)
#         print(f"New keys for controlling: {new_params[0]}, {new_params[1]}, {new_params[2]}, {new_params[3]}")    
#     nodes_parameters = get_nodes_parameters(node)
#     print("Press the key to move the turtle")
#     movement_choice(nodes_parameters[0], nodes_parameters[1], nodes_parameters[2], nodes_parameters[3]) 
#     print("finished")
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()











import rclpy
from rclpy.node import Node
from geometry_msgs.msg  import Twist
from curtsies import Input
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading

class CustomControlNode(Node):
    def __init__(self):
        super().__init__('custom_control_node')
        self.velocity_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        

        mf__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
                                                      description='Key you press for moving forward')
        
        self.declare_parameter("moving_forward", 'i', mf__descriptor)
        
        mb__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
                                                      description='Key you press for moving moving_backwards')

        self.declare_parameter("moving_backwards", 'k', mb__descriptor)
        
        rcckw__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
                                                      description='Key you press for rotating counterclockwise')
        
        self.declare_parameter("rotating_cckw", 'j', rcckw__descriptor)

        rckw__descriptor = ParameterDescriptor(type=ParameterType.PARAMETER_STRING,
                                                      description='Key you press for rotating_clockwise')

        self.declare_parameter("rotating_ckw", 'l', rckw__descriptor)


    def move_forward(self):
        vel_msg = Twist()
        vel_msg.linear.x = 2.0
        vel_msg.angular.z = 0.0
        self.velocity_publisher.publish(vel_msg)

    def move_backwards(self):
        vel_msg = Twist()
        vel_msg.linear.x = -2.0
        vel_msg.angular.z = 0.0
        self.velocity_publisher.publish(vel_msg)

    def rotate_clockwise(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = -2.0
        self.velocity_publisher.publish(vel_msg)

    def rotate_counterclockwise(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 2.0
        self.velocity_publisher.publish(vel_msg)


def get_key():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            return e

def movement_choice(node):
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            nodes_keys = get_nodes_parameters(node)
            forward_key = nodes_keys[0]
            backwards_key = nodes_keys[1]
            counterclockwise_key = nodes_keys[2]
            clockwise_key = nodes_keys[3]
            if e == forward_key:
                node.move_forward()
            elif e == backwards_key:
                node.move_backwards()
            elif e == counterclockwise_key:
                node.rotate_counterclockwise()
            elif e == clockwise_key:
                node.rotate_clockwise()

def process_user_choice(pressed_key):
    pressed_key = pressed_key.lower()
    if pressed_key == "y":
        return True
    elif pressed_key == "n":
        return False

def get_new_parameters():
    print("Enter new keys:\nMoving forward:")
    new_mf = get_key()
    print(new_mf)
    print("Moving backwards:")
    new_mb = get_key()
    print(new_mb)
    print("Rotating Counterclockwise:")
    new_rcckw = get_key()
    print(new_rcckw)
    print("Rotating Clockwise:")
    new_rckw = get_key()
    print(new_rckw)
    return new_mf, new_mb, new_rcckw, new_rckw

def change_parameters(node, new_param_list):
    param_mf = Parameter('moving_forward', Parameter.Type.STRING, new_param_list[0])
    param_mb = Parameter('moving_backwards', Parameter.Type.STRING, new_param_list[1])
    param_rcckw = Parameter('rotating_cckw', Parameter.Type.STRING, new_param_list[2])
    param_rckw = Parameter('rotating_ckw', Parameter.Type.STRING, new_param_list[3])
    node.set_parameters([param_mf, param_mb, param_rcckw, param_rckw])

def get_nodes_parameters(node):
    mf_key = node.get_parameter('moving_forward').value 
    mb_key = node.get_parameter('moving_backwards').value
    rcckw_key = node.get_parameter('rotating_cckw').value
    rckw_key = node.get_parameter('rotating_ckw').value
    return mf_key, mb_key, rcckw_key, rckw_key
        
def main(args=None):
    global node
    rclpy.init(args=args)
    node = CustomControlNode()
            
    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()
    rate = node.create_rate(10)
    try:
        while rclpy.ok():
            default_parameters = get_nodes_parameters(node)
            print(f"Default keys for controlling: {default_parameters[0]}, {default_parameters[1]}, {default_parameters[2]}, {default_parameters[3]}")
            print("Do you want to change them?(y/n)")
            user_choice = process_user_choice(get_key())
            if user_choice == True:
                new_params = get_new_parameters()
                change_parameters(node, new_params)
                print(f"New keys for controlling: {new_params[0]}, {new_params[1]}, {new_params[2]}, {new_params[3]}")
            print("Press the key to move the turtle")
            movement_choice(node) 
            rate.sleep()
    except KeyboardInterrupt:
        pass
        rclpy.spin(node)
    rclpy.shutdown()
    thread.join()

if __name__ == '__main__':
    main()
