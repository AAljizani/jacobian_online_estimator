"""Runs the selected Jacobian estimator (Broyden or Kalman) online.

Subscribes to joint state + end-effector pose, computes dq/dy between
updates, feeds them to the active estimator, and publishes the current
Jacobian estimate.

TODO: parameterize estimator choice (broyden|kalman) via config/params.yaml
so both can run side-by-side for the Broyden-vs-Kalman comparison
(Stretch 1).
"""
import rclpy
from rclpy.node import Node


class JacobianEstimatorNode(Node):
    def __init__(self):
        super().__init__('jacobian_estimator_node')
        self.get_logger().info('jacobian_estimator_node started (stub - Phase 1)')
        # TODO: subscribe to JointState and end-effector PoseStamped
        # TODO: instantiate BroydenEstimator and/or KalmanJacobianEstimator
        # TODO: publish estimated Jacobian (custom msg or Float64MultiArray)


def main(args=None):
    rclpy.init(args=args)
    node = JacobianEstimatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
