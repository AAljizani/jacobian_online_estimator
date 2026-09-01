"""Kalman-filter-based online Jacobian estimation.

Reference: Piepmeier et al., dynamic quasi-Newton / Kalman-filter Jacobian
estimation for uncalibrated visual servoing.

TODO: this is a stub. Real implementation needs the state to be the
(vectorized) Jacobian, process noise Q and measurement noise R tuned
against real hardware/camera noise (Phase 2/3), not just simulation
defaults.
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
        # TODO: implement the full predict/update cycle. Left as a stub
        # until Phase 2 hardware noise characteristics are known -- tuning
        # Q/R against simulation defaults alone risks a filter that
        # diverges on real sensor noise.
        raise NotImplementedError(
            "KalmanJacobianEstimator.update: implement during Phase 1-2, "
            "tune against real hardware noise in Phase 2-3."
        )
