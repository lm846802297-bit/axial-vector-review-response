#!/usr/bin/env python3
import unittest
import sympy as sp

from b5_2b_gauge_current_subblock import (
    gauge_parameter_poles,
    weak_current_eom_identity,
    conjugate_singlet_current_identity,
    tree_current_coefficients,
    gY, g2, gX, Q,
)


class TestB52BGaugeCurrentSubblock(unittest.TestCase):
    def test_C5_parameter_pole(self):
        r = gauge_parameter_poles()
        expected = -(sp.Rational(15,8)*gY**2
                     + sp.Rational(9,8)*g2**2 + 3*Q**2*gX**2)
        self.assertEqual(sp.simplify(r["pole_C5"]-expected), 0)

    def test_C5_direct_EFT_casimir_agreement(self):
        r = gauge_parameter_poles()
        self.assertEqual(
            sp.simplify(r["beta_C5_16pi2"]-r["direct_EFT_C5_16pi2"]), 0
        )

    def test_CLD_parameter_pole(self):
        r = gauge_parameter_poles()
        expected = sp.Rational(9,4)*gY**2-sp.Rational(9,4)*g2**2
        self.assertEqual(sp.simplify(r["pole_CLD"]-expected), 0)

    def test_CRD_parameter_pole_cancels(self):
        r = gauge_parameter_poles()
        self.assertEqual(sp.simplify(r["pole_CRD"]), 0)
        self.assertEqual(sp.simplify(r["beta_CRD_16pi2"]), 0)

    def test_weak_singlet_triplet_decomposition(self):
        self.assertTrue(weak_current_eom_identity())

    def test_conjugate_singlet_current_flips(self):
        self.assertTrue(conjugate_singlet_current_identity())

    def test_tree_current_coefficients_common_S_basis(self):
        a = tree_current_coefficients(3.299007795034e-9, 3.141592656728e-8, -1)
        self.assertAlmostEqual(a["C_HL_1_Pauli"], -8.247519487585e-10, places=21)
        self.assertAlmostEqual(a["C_HL_3_Pauli"], -8.247519487585e-10, places=21)
        self.assertAlmostEqual(a["C_Se_commonS_tree"], -1.570796328364e-8, places=20)
        b = tree_current_coefficients(3.299007795034e-9, 5.625443342554e-12, +1)
        self.assertAlmostEqual(b["C_Se_commonS_tree"], +2.812721671277e-12, places=23)


if __name__ == "__main__":
    unittest.main(verbosity=2)
