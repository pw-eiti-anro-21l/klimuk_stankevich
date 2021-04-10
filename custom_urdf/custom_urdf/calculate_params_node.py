import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterDescriptor
from rclpy.parameter import Parameter
import threading

from DHtoURDF import *

class CalculateParamsNode(Node):
    def __init__(self):
        super().__init__('calculate_params_node')
        namespace = ""
        
        self.declare_parameter("table_row_1", None)
        self.declare_parameter("table_row_2", None)
        self.declare_parameter("table_row_3", None)

        self.declare_parameter("joint_fixed", None)
        self.declare_parameter("joint_shoulder", None)
        self.declare_parameter("joint_elbow", None)
        self.declare_parameter("joint_wrist", None)
        self.declare_parameter("joint_fixed_end", None)


    def spin(self):
        while rclpy.ok():
            rclpy.spin_once(self)
            print('CalculateParamsNode is working')
            my_main()

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
    # global node
    # rclpy.init(args=args)
    # node = CalculateParamsNode()
            
    # thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    # thread.start()
    # rate = node.create_rate(10)
    # try:
    #     while rclpy.ok():
    #         print(node.get_parameter('table_row_1').value)
    #         print(node.get_parameter('table_row_2').value)
    #         print(node.get_parameter('table_row_3').value)
    #         print('CalculateParamsNode is working')
    #         # my_main()
    #         rate.sleep()
    # except KeyboardInterrupt:
    #     pass
    #     rclpy.spin(node)
    # rclpy.shutdown()
    # thread.join()

    rclpy.init(args=args)
    node = CalculateParamsNode()
    print('CalculateParamsNode is working')

    t1_row = node.get_parameter('table_row_1').value
    t2_row = node.get_parameter('table_row_2').value
    t3_row = node.get_parameter('table_row_3').value
    rows_strings_table = [t1_row, t2_row, t3_row]
    result_table = calculate_joints_coordinates(rows_strings_table)
    
    print(result_table)
    
    shoulder_param = Parameter('joint_shoulder', Parameter.Type.DOUBLE_ARRAY, result_table[0])
    elbow_param = Parameter('joint_elbow', Parameter.Type.DOUBLE_ARRAY, result_table[1])
    wrist_param = Parameter('joint_wrist', Parameter.Type.DOUBLE_ARRAY, result_table[2])
    fixed_end_param = Parameter('joint_fixed_end', Parameter.Type.DOUBLE_ARRAY, result_table[3])
    node.set_parameters([shoulder_param, elbow_param, wrist_param, fixed_end_param])

    print(node.get_parameter('joint_shoulder').value)
    print(node.get_parameter('joint_elbow').value)
    print(node.get_parameter('joint_wrist').value)
    print(node.get_parameter('joint_fixed_end').value)


    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()