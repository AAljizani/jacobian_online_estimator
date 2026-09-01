"""Bridges the arm's serial-bus servo protocol into ROS 2.

Phase 2 (hardware bring-up) work item.

Responsibilities:
- Command joint angles to the arm's servos.
- Read back actual joint angles (position feedback) and publish as
  sensor_msgs/JointState.

TODO: implement once the arm purchase is finalized (Hiwonder xArm 2.0 vs.
SO-101/SO-ARM100) -- the serial protocol differs between the two.
"""
import rclpy
from rclpy.node import Node


class JointInterfaceNode(Node):
    def __init__(self):
        super().__init__('joint_interface_node')
        self.get_logger().info('joint_interface_node started (stub - Phase 2)')
        # TODO: open serial connection to servo bus
        # TODO: publish sensor_msgs/JointState on a timer
        # TODO: subscribe to joint command topic, write to servos


def main(args=None):
    rclpy.init(args=args)
    node = JointInterfaceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
