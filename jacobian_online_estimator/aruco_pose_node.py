"""Finds the ArUco marker in the camera image and gets its pose.

We need this in Phase 1 and 2. It publishes the pose of the marker on the
end of the arm, as seen by the fixed camera, so the estimator can use it.

TODO: calibrate the camera first (with a checkerboard) and load that
calibration, otherwise the poses from here can't be trusted.
TODO: hand-eye calibration (where the camera is compared to the arm base)
is a separate step we only do once, see DECISIONS.md. This node publishes
the marker pose in the camera frame, and the change to the base frame
happens later (or through tf2 once hand-eye calibration is done).
"""
import rclpy
from rclpy.node import Node


class ArucoPoseNode(Node):
    def __init__(self):
        super().__init__('aruco_pose_node')
        self.get_logger().info('aruco_pose_node started (stub - Phase 1/2)')
        # TODO: open the camera with OpenCV and load the calibration
        # TODO: find the ArUco marker and get its pose (rvec and tvec)
        # TODO: publish the pose as geometry_msgs/PoseStamped


def main(args=None):
    rclpy.init(args=args)
    node = ArucoPoseNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
