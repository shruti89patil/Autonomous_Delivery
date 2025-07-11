from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('slam_launch'),
        'config',
        'slam_params.yaml'
    )

    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[config],
        )
    ])


# from launch import LaunchDescription
# from launch_ros.actions import Node
# import os

# def generate_launch_description():
#     return LaunchDescription([
#         Node(
#             package='slam_toolbox',
#             executable='async_slam_toolbox_node',
#             name='slam_toolbox',
#             output='screen',
#             parameters=[os.path.join(
#                 '/home/pi/Autonomous_Delivery_Robot/src/slam_launch/config',  # Update path
#                 'slam_params.yaml'  # This file must exist
#             )]
#         )
#     ])
