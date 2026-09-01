"""Closes the visual servoing loop: end-effector error -> joint command.

MVP control law: basic proportional control (see DECISIONS.md -- no
trajectory optimization; the estimator is the contribution, not the
controller).

    dq = pinv(J_estimated) @ (K_p * (target_pose - current_pose))
"""
import rclpy
from rclpy.node import Node


class VisualServoControllerNode(Node):
    def __init__(self):
        super().__init__('visual_servo_controller_node')
        self.get_logger().info('visual_servo_controller_node started (stub - Phase 3)')
        # TODO: subscribe to current Jacobian estimate + end-effector pose
        # TODO: subscribe to (or hold) target pose
        # TODO: compute dq via pseudo-inverse, publish joint command


def main(args=None):
    rclpy.init(args=args)
    node = VisualServoControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
