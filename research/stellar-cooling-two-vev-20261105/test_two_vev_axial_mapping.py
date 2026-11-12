#!/usr/bin/env python3
"""Unit tests for the exact two-VEV axial/Goldstone mapping."""
import math
import unittest

from two_vev_axial_mapping import TwoVEVPoint, eaten_goldstone, physical_pseudoscalar


class TwoVEVMappingTests(unittest.TestCase):
    def test_exact_gauge_mass_relation(self):
        p = TwoVEVPoint(v_s=100.0, v_sigma=60.0, g_x=0.02)
        self.assertAlmostEqual(p.m_a**2, p.g_x**2 * (4*p.v_s**2 + p.v_sigma**2))

    def test_goldstone_current_identity(self):
        p = TwoVEVPoint(v_s=100.0, v_sigma=60.0, g_x=0.02)
        for m_l in (0.1056583755, 1.77686):
            self.assertAlmostEqual(p.goldstone_lepton_yukawa(m_l),
                                   p.longitudinal_current_yukawa(m_l), places=14)

    def test_single_vev_limit(self):
        p = TwoVEVPoint(v_s=100.0, v_sigma=0.0, g_x=0.02)
        self.assertAlmostEqual(p.m_a, 2.0 * abs(p.g_x) * p.v_s)
        self.assertAlmostEqual(p.goldstone_s_projection, 1.0)
        self.assertAlmostEqual(p.goldstone_lepton_yukawa(0.105), 0.105/100.0)

    def test_inverse_mapping(self):
        original = TwoVEVPoint(v_s=100.0, v_sigma=60.0, g_x=0.02)
        restored = TwoVEVPoint.from_mediator_inputs(original.m_a, original.g_x,
                                                    original.r_sigma)
        self.assertAlmostEqual(restored.v_s, original.v_s)
        self.assertAlmostEqual(restored.v_sigma, original.v_sigma)

    def test_goldstone_and_physical_pseudoscalar_are_orthonormal(self):
        vs, vq = 100.0, 60.0
        gs, ps = (2*vs, vq), (vq, -2*vs)
        norm, pnorm = math.hypot(*gs), math.hypot(*ps)
        self.assertAlmostEqual((gs[0]*ps[0] + gs[1]*ps[1])/(norm*pnorm), 0.0)
        self.assertAlmostEqual(eaten_goldstone(vs, vq, 1.0, 0.0)**2
                               + physical_pseudoscalar(vs, vq, 1.0, 0.0)**2, 1.0)

    def test_invalid_inputs(self):
        for args in ((0.0, 1.0, 0.1), (1.0, -1.0, 0.1), (1.0, 0.0, 0.0)):
            with self.assertRaises(ValueError):
                TwoVEVPoint(*args)
        with self.assertRaises(ValueError):
            TwoVEVPoint.from_mediator_inputs(1.0, 0.1, -0.1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
