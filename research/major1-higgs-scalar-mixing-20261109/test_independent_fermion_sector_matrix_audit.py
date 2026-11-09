import math
import unittest

import numpy as np

from independent_fermion_sector_matrix_audit import (
    ME,
    MU_R,
    b0_feynman_parameter,
)


class IndependentFermionMatrixAuditTests(unittest.TestCase):
    def test_zero_momentum_equal_mass_b0_closed_form(self):
        mass = 1.7
        expected = -math.log(mass * mass / (MU_R * MU_R))
        actual = b0_feynman_parameter(0.0, mass, mass)
        self.assertAlmostEqual(actual.real, expected, places=12)
        self.assertAlmostEqual(actual.imag, 0.0, places=12)

    def test_heavy_equal_mass_b0_is_real_below_threshold(self):
        actual = b0_feynman_parameter(125.25**2, ME, ME)
        self.assertAlmostEqual(actual.imag, 0.0, places=14)
        self.assertTrue(math.isfinite(actual.real))

    def test_light_pair_b0_has_positive_absorptive_part_above_threshold(self):
        actual = b0_feynman_parameter(125.25**2, 0.1056583755, 0.1056583755)
        self.assertGreater(actual.imag, 0.0)
        self.assertAlmostEqual(actual.imag, math.pi * (1.0 - math.sqrt(1.0 - 4.0 * 0.1056583755**2 / 125.25**2)), places=10)

    def test_chiral_coefficients_reproduce_explicit_dirac_trace(self):
        identity = np.eye(2, dtype=complex)
        zero = np.zeros((2, 2), dtype=complex)
        sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
        sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
        sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)
        gamma = [
            np.block([[identity, zero], [zero, -identity]]),
            np.block([[zero, sigma1], [-sigma1, zero]]),
            np.block([[zero, sigma2], [-sigma2, zero]]),
            np.block([[zero, sigma3], [-sigma3, zero]]),
        ]
        gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
        projector_r = (np.eye(4) + gamma5) / 2.0
        projector_l = (np.eye(4) - gamma5) / 2.0

        def slash(q):
            return gamma[0] * q[0] - sum(gamma[i + 1] * q[i + 1] for i in range(3))

        ga_ij = 0.2 + 0.1j
        ga_ji = 0.3 - 0.05j
        gb_ij = 0.4 + 0.2j
        gb_ji = 0.1 - 0.3j
        mi, mj = 2.3, 1.2
        k = np.array([3.1, 0.2, 0.4, 0.5])
        p = np.array([1.1, -0.3, 0.1, 0.2])
        vertex_a = ga_ij * projector_r + np.conj(ga_ji) * projector_l
        vertex_b = gb_ji * projector_r + np.conj(gb_ij) * projector_l
        trace = np.trace(
            vertex_a @ (slash(k) + mj * np.eye(4))
            @ vertex_b @ (slash(k + p) + mi * np.eye(4))
        )
        c_kinetic = ga_ij * np.conj(gb_ij) + np.conj(ga_ji) * gb_ji
        c_mass = ga_ij * gb_ji + np.conj(ga_ji) * np.conj(gb_ij)
        k_dot_kp = k[0] * (k[0] + p[0]) - np.dot(k[1:], k[1:] + p[1:])
        reduced = 2.0 * c_kinetic * k_dot_kp + 2.0 * mi * mj * c_mass
        self.assertAlmostEqual(abs(trace - reduced), 0.0, places=12)


if __name__ == "__main__":
    unittest.main()
