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
        self.declare_parameter("joint_wrist_connector", None)

    def spin(self):
        while rclpy.ok():
            rclpy.spin_once(self)
            print('CalculateParamsNode is working')
            my_main()


def get_joints_parameters(node):
    fixed = node.get_parameter('joint_fixed').value
    shoulder = node.get_parameter('joint_shoulder').value
    elbow = node.get_parameter('joint_elbow').value
    wrist = node.get_parameter('joint_wrist').value
    fixed_end = node.get_parameter('joint_fixed_end').value
    wrist_conn = node.get_parameter('joint_wrist_connector').value
    return fixed, shoulder, elbow, wrist, fixed_end, wrist_conn

        
def main(args=None):
    global node

    rclpy.init(args=args)
    node = CalculateParamsNode()
    print('CalculateParamsNode is working')

    t1_row = node.get_parameter('table_row_1').value
    t2_row = node.get_parameter('table_row_2').value
    t3_row = node.get_parameter('table_row_3').value
    rows_strings_table = [t1_row, t2_row, t3_row]
    result_table = calculate_joints_coordinates(rows_strings_table)
    
    
    shoulder_param = Parameter('joint_shoulder', Parameter.Type.DOUBLE_ARRAY, result_table[0])
    elbow_param = Parameter('joint_elbow', Parameter.Type.DOUBLE_ARRAY, result_table[1])
    wrist_param = Parameter('joint_wrist', Parameter.Type.DOUBLE_ARRAY, result_table[2])
    fixed_end_param = Parameter('joint_fixed_end', Parameter.Type.DOUBLE_ARRAY, result_table[3])
    const_wrist_conn_array = [0.0, 0.0, 0.0, 0.0, 1.578, 0.0, 0.0, 0.0, 0.0]
    wrist_conn_param = Parameter('joint_wrist_connector', Parameter.Type.DOUBLE_ARRAY, const_wrist_conn_array)
    node.set_parameters([shoulder_param, elbow_param, wrist_param, fixed_end_param, wrist_conn_param])

    joints_params_list = get_joints_parameters(node)

    write_params_to_yaml(joints_params_list, "./custom_urdf/config/joints_params.yaml", "calc_params")
    write_params_to_yaml(joints_params_list, "./custom_urdf/config/nonkdl_params.yaml", "NONKDL_DKIN")
    write_params_to_yaml(joints_params_list, "./custom_urdf/config/kdl_params.yaml", "KDL_DKIN")
    
    print("Joints parameters has been written to yaml file")
    print("You can now launch view_robot_launch.py")

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()