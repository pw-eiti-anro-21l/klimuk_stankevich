from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),
        Node(
            package='custom_control',
            prefix='gnome-terminal --',
            executable='custom_controller',
            name='custom_controller'
        )
    ])
