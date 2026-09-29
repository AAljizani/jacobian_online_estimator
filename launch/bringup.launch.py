"""Starts everything: the joint interface, ArUco pose, estimator, and
controller.

TODO: once we have the arm, split this into bringup_sim.launch.py (Gazebo)
and bringup_hardware.launch.py, since they will at least need different
settings for joint_interface_node.
"""
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='jacobian_online_estimator',
            executable='joint_interface_node',
            name='joint_interface_node',
        ),
        Node(
            package='jacobian_online_estimator',
            executable='aruco_pose_node',
            name='aruco_pose_node',
        ),
        Node(
            package='jacobian_online_estimator',
            executable='jacobian_estimator_node',
            name='jacobian_estimator_node',
        ),
        Node(
            package='jacobian_online_estimator',
            executable='visual_servo_controller_node',
            name='visual_servo_controller_node',
        ),
    ])
