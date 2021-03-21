from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='package_lab1',
            executable='sterowanie_zolwiem',
            name='sterowanie_zolwiem',
            prefix='gnome-terminal --'
        )
    ])