"""Camera calibration + ArUco marker pose estimation.

Phase 1/2 work item. Publishes the end-effector's pose (as seen by the
fixed eye-to-hand camera) for the Jacobian estimator to consume.

TODO: camera intrinsic calibration (checkerboard) must be done and loaded
before any pose here can be trusted.
TODO: hand-eye calibration (camera-to-base transform) is a separate,
one-time step -- see DECISIONS.md. This node publishes marker pose in the
camera frame; the transform to base frame is applied downstream (or via
tf2, once hand-eye calibration is complete).
"""
import rclpy
from rclpy.node import Node


class ArucoPoseNode(Node):
    def __init__(self):
        super().__init__('aruco_pose_node')
        self.get_logger().info('aruco_pose_node started (stub - Phase 1/2)')
        # TODO: open camera (OpenCV VideoCapture), load calibration
        # TODO: detect ArUco marker, estimate pose (rvec/tvec)
        # TODO: publish geometry_msgs/PoseStamped


def main(args=None):
    rclpy.init(args=args)
    node = ArucoPoseNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
