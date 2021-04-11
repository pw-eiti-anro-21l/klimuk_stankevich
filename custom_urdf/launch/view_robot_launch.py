import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node


def generate_launch_description():
    # Get the launch directory
    bringup_dir = get_package_share_directory('custom_urdf')
    launch_dir = os.path.join(bringup_dir, 'launch')
    config = os.path.join(bringup_dir, 'params.yaml')

    # Launch configuration variables specific to simulation
    rviz_config_file = LaunchConfiguration('rviz_config_file')
    use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
    use_joint_state_pub = LaunchConfiguration('use_joint_state_pub')
    use_rviz = LaunchConfiguration('use_rviz')
    urdf_file= LaunchConfiguration('urdf_file')
    # use_calc_params = LaunchConfiguration('use_calc_params')
    
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
        'rviz_config_file',
        default_value=os.path.join(bringup_dir, 'view.rviz'),
        description='Full path to the RVIZ config file to use')  
    declare_use_robot_state_pub_cmd = DeclareLaunchArgument(
        'use_robot_state_pub',
        default_value='True',
        description='Whether to start the robot state publisher')
    declare_use_joint_state_pub_cmd = DeclareLaunchArgument(
        'use_joint_state_pub',
        default_value='True',
        description='Whether to start the joint state publisher')
    declare_use_rviz_cmd = DeclareLaunchArgument(
        'use_rviz',
        default_value='True',
        description='Whether to start RVIZ')

    declare_urdf_cmd = DeclareLaunchArgument(
        'urdf_file',
        default_value=os.path.join(bringup_dir, 'custom.urdf'),
        description='Whether to start RVIZ')


    # declare_use_calc_params_cmd = DeclareLaunchArgument(
    #     'use_calc_params',
    #     default_value=os.path.join(bringup_dir, 'custom_urdf', 'calculate_params.py'),
    #     description='123')


    start_robot_state_publisher_cmd = Node(
        condition=IfCondition(use_robot_state_pub),
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        #parameters=[{'use_sim_time': use_sim_time}],
        arguments=[urdf_file])
    
    start_joint_state_publisher_cmd = Node(
        condition=IfCondition(use_joint_state_pub),
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen',
        arguments=[urdf_file])
    
    rviz_cmd = Node(
        condition=IfCondition(use_rviz),
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen')

    start_calc_params_cmd = Node(
            package='custom_urdf',
            prefix='gnome-terminal --',
            executable='calc_params',
            name='calc_params',
            parameters= [config])
                
  
    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_rviz_config_file_cmd)
    ld.add_action(declare_urdf_cmd)
    ld.add_action(declare_use_robot_state_pub_cmd)
    ld.add_action(declare_use_joint_state_pub_cmd)
    ld.add_action(declare_use_rviz_cmd)
    # ld.add_action(declare_use_calc_params_cmd)


    # Add any conditioned actions
    ld.add_action(start_joint_state_publisher_cmd)
    ld.add_action(start_robot_state_publisher_cmd)
    ld.add_action(rviz_cmd)
    ld.add_action(start_calc_params_cmd)

    return ld   
    




# def generate_launch_description():
#     # Get the launch directory
#     bringup_dir = get_package_share_directory('custom_urdf')
#     launch_dir = os.path.join(bringup_dir, 'launch')
#     config = os.path.join(bringup_dir, 'params.yaml')

#     start_calc_params_cmd = Node(
#                 package='custom_urdf',
#                 prefix='gnome-terminal --',
#                 executable='calc_params',
#                 name='calc_params',
#                 parameters= [config])

#     # start_calc_params_cmd = Node(
#     #             package='custom_urdf',
#     #             prefix='gnome-terminal --',
#     #             executable='calc_params',
#     #             name='calc_params')

#     ld = LaunchDescription()
#     ld.add_action(start_calc_params_cmd)
    
#     return ld 