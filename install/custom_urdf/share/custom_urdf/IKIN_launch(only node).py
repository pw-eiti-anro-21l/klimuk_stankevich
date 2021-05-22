import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Get the launch directory
    bringup_dir = get_package_share_directory('custom_urdf')
    launch_dir = os.path.join(bringup_dir, 'launch')
    config = os.path.join(bringup_dir, 'ikin_params.yaml')

    start_IKIN_cmd = Node(
                package='custom_urdf',
                executable='IKIN',
                name='IKIN',
                output='screen',
                parameters= [config])

    ld = LaunchDescription()

    ld.add_action(start_IKIN_cmd)
    
    return ld 