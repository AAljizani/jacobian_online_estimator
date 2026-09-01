"""Closes the loop by turning the marker error into joint commands.

For the minimum version we use a simple proportional controller (see
DECISIONS.md). We aren't doing any trajectory planning, since the
estimator is the main part of the project, not the controller.

We take the error between the target pose and the current pose, multiply
it by a gain, and turn it into joint changes using the pseudo-inverse of
the estimated Jacobian:

    dq = pinv(J) @ (K_p * (target_pose - current_pose))
"""
import rclpy
from rclpy.node import Node


class VisualServoControllerNode(Node):
    def __init__(self):
        super().__init__('visual_servo_controller_node')
        self.get_logger().info('visual_servo_controller_node started (stub - Phase 3)')
        # TODO: subscribe to the current Jacobian estimate and the marker pose
        # TODO: get the target pose (from a topic or just keep a fixed one)
        # TODO: work out dq with the pseudo-inverse and publish the joint command


def main(args=None):
    rclpy.init(args=args)
    node = VisualServoControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
