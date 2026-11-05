#!/usr/bin/env python3
"""Unit tests for the original paper's single-VEV axial/Goldstone mapping."""
import unittest

from single_vev_axial_mapping import SingleVEVPoint, eaten_goldstone


class SingleVEVMappingTests(unittest.TestCase):
    def test_exact_gauge_mass_relation(self):
        p = SingleVEVPoint(v_s=100.0, g_x=0.02)
        self.assertAlmostEqual(p.m_a, 2.0 * abs(p.g_x) * p.v_s)

    def test_goldstone_current_identity(self):
        p = SingleVEVPoint(v_s=100.0, g_x=0.02)
        for m_l in (0.1056583755, 1.77686):
            self.assertAlmostEqual(
                p.goldstone_lepton_yukawa(m_l),
                p.longitudinal_current_yukawa(m_l),
                places=14,
            )

    def test_single_phase_is_fully_eaten(self):
        p = SingleVEVPoint(v_s=100.0, g_x=0.02)
        self.assertEqual(p.goldstone_s_projection, 1.0)
        self.assertAlmostEqual(eaten_goldstone(0.37), 0.37)

    def test_inverse_mapping(self):
        original = SingleVEVPoint(v_s=100.0, g_x=0.02)
        restored = SingleVEVPoint.from_mediator_inputs(original.m_a, original.g_x)
        self.assertAlmostEqual(restored.v_s, original.v_s)
        self.assertAlmostEqual(restored.g_x, original.g_x)

    def test_goldstone_coupling_scales_with_lepton_mass(self):
        p = SingleVEVPoint(v_s=200.0, g_x=0.03)
        y_mu = p.goldstone_lepton_yukawa(0.1056583755)
        y_tau = p.goldstone_lepton_yukawa(1.77686)
        self.assertAlmostEqual(y_tau / y_mu, 1.77686 / 0.1056583755)

    def test_invalid_inputs(self):
        for args in ((0.0, 0.1), (1.0, 0.0), (float("nan"), 0.1)):
            with self.assertRaises(ValueError):
                SingleVEVPoint(*args)
        with self.assertRaises(ValueError):
            SingleVEVPoint.from_mediator_inputs(1.0, 0.0)
        with self.assertRaises(ValueError):
            eaten_goldstone(float("inf"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
