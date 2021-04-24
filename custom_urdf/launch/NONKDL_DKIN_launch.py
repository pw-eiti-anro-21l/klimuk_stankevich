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
    config = os.path.join(bringup_dir, 'nonkdl_params.yaml')
    urdf_file= LaunchConfiguration('urdf_file')

    declare_urdf_cmd = DeclareLaunchArgument(
        'urdf_file',
        default_value=os.path.join(bringup_dir, 'custom.urdf'),
        description='Whether to start RVIZ')

    start_NONKDL_DKIN_cmd = Node(
                package='custom_urdf',
                prefix='gnome-terminal --',
                executable='NONKDL_DKIN',
                name='NONKDL_DKIN',
                output='screen',
                arguments=[urdf_file],
                parameters= [config])

    ld = LaunchDescription()

    ld.add_action(declare_urdf_cmd)

    ld.add_action(start_NONKDL_DKIN_cmd)
    
    return ld 