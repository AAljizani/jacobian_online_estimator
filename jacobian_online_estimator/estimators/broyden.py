"""Broyden rank-1 update for online Jacobian estimation.

Reference: Hosoda & Asada (1994), "Versatile visual servoing without
knowledge of true Jacobian."

J_{k+1} = J_k + ((dy - J_k @ dq) @ dq.T) / (dq.T @ dq)

where dq is the joint-space displacement and dy is the observed
end-effector displacement.
"""
import numpy as np


class BroydenEstimator:
    def __init__(self, initial_jacobian: np.ndarray):
        self.J = initial_jacobian.copy()

    def update(self, dq: np.ndarray, dy: np.ndarray) -> np.ndarray:
        dq = dq.reshape(-1, 1)
        dy = dy.reshape(-1, 1)
        denom = float(dq.T @ dq)
        if denom < 1e-9:
            return self.J  # avoid divide-by-near-zero on tiny motions
        residual = dy - self.J @ dq
        self.J = self.J + (residual @ dq.T) / denom
        return self.J
