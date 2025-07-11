# from launch import LaunchDescription
# from launch_ros.actions import Node
# import os
# from ament_index_python.packages import get_package_share_directory
# from launch.substitutions import Command

# def generate_launch_description():
#     urdf_file = os.path.join(
#         get_package_share_directory('my_robot_description'),
#         'urdf',
#         'my_robot.urdf.xacro'
#     )

#     return LaunchDescription([
#         Node(
#             package='joint_state_publisher_gui',
#             executable='joint_state_publisher_gui',
#         ),
#         Node(
#             package='robot_state_publisher',
#             executable='robot_state_publisher',
#             # parameters=[{'robot_description': open(urdf_file).read()}],
#             parameters=[{
#                 'robot_description': Command(['xacro ', urdf_file])
#             }],
#         ),

        
#         Node(
#             package='tf2_ros',
#             executable='static_transform_publisher',
#             arguments=['0', '0', '0', '0', '0', '0', '1', 'odom', 'base_link'],
#         ),
#         Node(
#             package='slam_toolbox',
#             executable='sync_slam_toolbox_node',
#             name='slam_toolbox',
#             output='screen',
#             parameters=[{'use_sim_time': False}],
#         ),
#         Node(
#             package='rviz2',
#             executable='rviz2',
#             arguments=['-d', os.path.join(
#                 get_package_share_directory('my_robot_description'),
#                 'rviz',
#                 'view.rviz')],
#             output='screen',
#         ),
#         Node(
#             package='ydlidar_ros2_driver',
#             executable='ydlidar_ros2_driver_node',
#             name='ydlidar',
#             output='screen',
#             parameters=[os.path.join(
#                 get_package_share_directory('ydlidar_ros2_driver'),
#                 'params',
#                 'ydlidar.yaml')]
# ),

#     ])

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'odom_frame': 'odom',
                'map_frame': 'map',
                'base_frame': 'base_link',
                'scan_topic': 'scan'
            }]
        )
    ])
