from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    config_path = os.path.join(
        os.getenv('HOME'),
        'Autonomous_Delivery_Robot',
        'src',
        'imu_lidar_localization',
        'config',
        'ekf.yaml'
    )

    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[config_path]
        )
    ])
