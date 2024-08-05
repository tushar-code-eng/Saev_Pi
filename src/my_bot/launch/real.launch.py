import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro


def generate_launch_description():

    
    diff_drive_spawner = Node(package='controller_manager', executable='spawner.py',
                        arguments=["diff_cont"],)

   delayed_diff_drive_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[diff_drive_spawner],
        )
    )
    joint_broad_spawner = Node(package='controller_manager', executable='spawner.py',
                        arguments=["joint_broad"],)
    delayed_joint_broad_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[joint_broad_spawner],
        )
    )

    return LaunchDescription([
        diff_drive_spawner,
        joint_broad_spawner
    ])