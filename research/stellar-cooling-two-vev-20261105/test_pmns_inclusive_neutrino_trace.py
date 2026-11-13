#!/usr/bin/env python3
"""Unitary-PMNS invariance of the inclusive active-neutrino charge trace."""
import math
import unittest

import numpy as np


def representative_pmns(
    theta12_deg: float = 33.44,
    theta23_deg: float = 49.2,
    theta13_deg: float = 8.57,
    delta_cp_deg: float = 197.0,
) -> np.ndarray:
    """Standard three-angle/one-Dirac-phase unitary PMNS parameterization."""
    t12, t23, t13, delta = map(
        math.radians,
        (theta12_deg, theta23_deg, theta13_deg, delta_cp_deg),
    )
    s12, c12 = math.sin(t12), math.cos(t12)
    s23, c23 = math.sin(t23), math.cos(t23)
    s13, c13 = math.sin(t13), math.cos(t13)
    em = np.exp(-1j * delta)
    ep = np.exp(1j * delta)
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * em],
            [
                -s12 * c23 - c12 * s23 * s13 * ep,
                c12 * c23 - s12 * s23 * s13 * ep,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * ep,
                -c12 * s23 - s12 * c23 * s13 * ep,
                c23 * c13,
            ],
        ],
        dtype=complex,
    )


class InclusiveNeutrinoTraceTests(unittest.TestCase):
    def test_pmns_rotation_preserves_inclusive_charge_trace(self):
        q_nu = np.diag([0.0, 1.0, -1.0]).astype(complex)
        u = representative_pmns()
        g_nu = u.conj().T @ q_nu @ u

        np.testing.assert_allclose(u.conj().T @ u, np.eye(3), atol=2e-15)
        self.assertAlmostEqual(
            float(np.real(np.trace(g_nu.conj().T @ g_nu))),
            2.0,
            places=13,
        )

    def test_nontrivial_pmns_generates_flavour_offdiagonal_couplings(self):
        q_nu = np.diag([0.0, 1.0, -1.0]).astype(complex)
        g_nu = representative_pmns().conj().T @ q_nu @ representative_pmns()
        off_diagonal = g_nu - np.diag(np.diag(g_nu))
        self.assertGreater(float(np.linalg.norm(off_diagonal)), 0.1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
