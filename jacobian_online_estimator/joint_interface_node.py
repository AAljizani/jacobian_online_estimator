"""Connects the arm's servos to ROS 2.

We need this in Phase 2 (hardware setup).

What it does:
- Sends joint angles to the servos.
- Reads back the actual joint angles from the servos and publishes them
  as sensor_msgs/JointState.

Arm: SO-101 follower (5-DOF plus gripper) with 12V STS3215 servos.
TODO: decide if this node uses the so_arm_100_hardware ros2_control package
or talks to the servos directly. Either way, the estimator has to get the
measured joint angles, not the commanded ones (see DECISIONS.md, 2026-09-08).
"""
import rclpy
from rclpy.node import Node


class JointInterfaceNode(Node):
    def __init__(self):
        super().__init__('joint_interface_node')
        self.get_logger().info('joint_interface_node started (stub - Phase 2)')
        # TODO: open the serial connection to the servo bus
        # TODO: publish sensor_msgs/JointState on a timer
        # TODO: listen for joint commands and send them to the servos


def main(args=None):
    rclpy.init(args=args)
    node = JointInterfaceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
