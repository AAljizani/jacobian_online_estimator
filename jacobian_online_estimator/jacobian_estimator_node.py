"""Runs the Jacobian estimator (Broyden or Kalman) while the arm is moving.

It listens to the joint states and the marker pose, works out how much the
joints and the marker moved between updates, gives those to the estimator,
and publishes the current Jacobian estimate.

TODO: let config/params.yaml pick which estimator to use (broyden or
kalman) so we can run both for the comparison.
"""
import rclpy
from rclpy.node import Node


class JacobianEstimatorNode(Node):
    def __init__(self):
        super().__init__('jacobian_estimator_node')
        self.get_logger().info('jacobian_estimator_node started (stub - Phase 1)')
        # TODO: subscribe to JointState and the marker PoseStamped
        # TODO: create the BroydenEstimator and/or KalmanJacobianEstimator
        # TODO: publish the Jacobian estimate (custom message or Float64MultiArray)


def main(args=None):
    rclpy.init(args=args)
    node = JacobianEstimatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
