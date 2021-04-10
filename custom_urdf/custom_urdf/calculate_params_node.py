import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading

from DHtoURDF import my_main

class CalculateParamsNode(Node):
    def __init__(self):
        super().__init__('calculate_params_node')
        
        
        self.declare_parameter("joint_0")
        self.declare_parameter("jonit_1")
        self.declare_parameter("jonit_2")
        self.declare_parameter("jonit_3")
        self.declare_parameter("jonit_4")




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
        
def main(args=None):
    global node
    rclpy.init(args=args)
    node = CalculateParamsNode()
            
    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()
    rate = node.create_rate(10)
    try:
        while rclpy.ok():
            # default_parameters = get_nodes_parameters(node)
            # print(f"Default keys for controlling: {default_parameters[0]}, {default_parameters[1]}, {default_parameters[2]}, {default_parameters[3]}")
            # print("Do you want to change them?(y/n)")
            # user_choice = process_user_choice(get_key())
            # if user_choice == True:
            #     new_params = get_new_parameters()
            #     change_parameters(node, new_params)
            #     print(f"New keys for controlling: {new_params[0]}, {new_params[1]}, {new_params[2]}, {new_params[3]}")
            # print("Press the key to move the turtle")
            # movement_choice(node) 
            print('CalculateParamsNode is working')
            my_main()
            rate.sleep()
    except KeyboardInterrupt:
        pass
        rclpy.spin(node)
    rclpy.shutdown()
    thread.join()

if __name__ == '__main__':
    main()