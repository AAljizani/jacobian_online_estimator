"""Kalman filter for estimating the Jacobian while the arm runs.

Reference: Piepmeier et al., dynamic quasi-Newton and Kalman filter
Jacobian estimation for uncalibrated visual servoing.

TODO: this is still a placeholder. The state is the Jacobian flattened into
a vector. The process noise Q and the measurement noise R need to be tuned
on the real arm and camera, not just left at sim values.
"""
import numpy as np


class KalmanJacobianEstimator:
    def __init__(self, initial_jacobian: np.ndarray, process_noise: float = 1e-3,
                 measurement_noise: float = 1e-2):
        self.J = initial_jacobian.copy()
        n, m = self.J.shape
        self.P = np.eye(n * m) * 1.0
        self.Q = np.eye(n * m) * process_noise
        self.R = np.eye(n) * measurement_noise

    def update(self, dq: np.ndarray, dy: np.ndarray) -> np.ndarray:
        # TODO: write the full predict and update steps. We left this for
        # now because we need to know how noisy the real hardware is first.
        # If we only tune Q and R in the sim, the filter could go wrong
        # once it sees real sensor noise.
        raise NotImplementedError(
            "KalmanJacobianEstimator.update: implement during Phase 1-2, "
            "tune against real hardware noise in Phase 2-3."
        )
