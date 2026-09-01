"""Broyden rank-1 update for estimating the Jacobian while the arm runs.

Reference: Hosoda and Asada (1994), "Versatile visual servoing without
knowledge of true Jacobian."

J_{k+1} = J_k + ((dy - J_k @ dq) @ dq.T) / (dq.T @ dq)

dq is how much the joints moved and dy is how much the marker moved.
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
            return self.J  # skip tiny moves so we don't divide by almost zero
        residual = dy - self.J @ dq
        self.J = self.J + (residual @ dq.T) / denom
        return self.J
