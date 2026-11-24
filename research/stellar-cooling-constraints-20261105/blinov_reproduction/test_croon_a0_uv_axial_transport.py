#!/usr/bin/env python3
"""Regression tests for the original-UV A0 finite-mixing transport driver."""
import math
import unittest

import numpy as np

from croon_a0_uv_axial_transport import compute_a0
from croon_c1_b13_vector_transport import M_MU
from finite_mixing.model import muon_couplings, neutrino_couplings
from finite_mixing.moving_muon_compton import moving_muon_compton_rates


class A0UVCouplingMapTests(unittest.TestCase):
    def test_actual_uv_mass_basis_couplings(self):
        theta = 1.0e-2
        point = muon_couplings(1.0, theta)
        self.assertAlmostEqual(point.g_vector, math.sin(theta) ** 2, places=15)
        self.assertAlmostEqual(point.g_axial, -math.cos(theta) ** 2, places=15)
        self.assertAlmostEqual(point.g_left, 1.0, places=15)
        self.assertAlmostEqual(point.g_right, -math.cos(2.0 * theta), places=15)

    def test_vector_and_axial_endpoints(self):
        axial = muon_couplings(1.0, 0.0)
        vector = muon_couplings(1.0, math.pi / 2.0)
        self.assertEqual((axial.g_vector, axial.g_axial), (0.0, -1.0))
        self.assertEqual((vector.g_vector, vector.g_axial), (1.0, 0.0))

    def test_active_neutrino_couplings_do_not_follow_muon_mixing(self):
        self.assertEqual(neutrino_couplings(1.0), (1.0, -1.0))
        self.assertEqual(neutrino_couplings(0.37), (0.37, -0.37))

    def test_finite_mixing_goldstone_current_identity(self):
        # Single-VEV model: m_A'=2*g_X*v_s.  The Ward identity fixes
        # y_Gμμ = 2*|g_A^mu|*m_mu/m_A' = cos(theta_muR)^2*m_mu/v_s.
        gx, vs, theta = 0.07, 120.0, 1.0e-2
        point = muon_couplings(gx, theta)
        m_a = 2.0 * gx * vs
        y_goldstone_from_phase = math.cos(theta) ** 2 * M_MU / vs
        y_goldstone_from_current = (
            2.0 * abs(point.g_axial) * M_MU / m_a
        )
        self.assertAlmostEqual(
            y_goldstone_from_phase, y_goldstone_from_current, places=15
        )


class A0MovingMuonKernelTests(unittest.TestCase):
    def test_uv_mixed_kernel_detailed_balance_by_charge_and_mode(self):
        point = muon_couplings(1.0, 1.0e-2)
        energy, temperature = 15.0, 25.0
        result = moving_muon_compton_rates(
            10.0, energy, temperature, 46.67432845,
            g_vector=point.g_vector,
            g_axial=point.g_axial,
            orders=(8, 6, 6, 6),
        )
        expected_factor = math.exp(-energy / temperature)
        self.assertEqual(result["mode_order"], ["L", "+", "-"])
        self.assertTrue(np.all(np.asarray(result["production"]) > 0.0))
        self.assertTrue(np.all(np.asarray(result["absorption"]) > 0.0))
        np.testing.assert_allclose(
            result["production"],
            expected_factor * result["absorption"],
            rtol=5.0e-11,
            atol=1.0e-14,
        )
        for charge in ("mu_minus", "mu_plus"):
            item = result["charge_resolved"][charge]
            np.testing.assert_allclose(
                item["production"],
                expected_factor * item["absorption"],
                rtol=5.0e-11,
                atol=1.0e-14,
            )

    def test_a0_engine_rejects_masses_with_omitted_dimuon_channel(self):
        with self.assertRaisesRegex(ValueError, "dimuon inverse decay"):
            compute_a0(masses=(2.0 * M_MU + 1.0,))


if __name__ == "__main__":
    unittest.main(verbosity=2)
