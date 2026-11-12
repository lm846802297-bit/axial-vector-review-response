#!/usr/bin/env python3
import unittest
import sympy as sp

from b5_2b2_eft_contact_vertex_audit import (
    composite_charges,
    eft_contact_coefficients,
    weak_singlet_covariant_derivative_check,
    gY, gX, Q,
)


class TestB52B2ContactVertices(unittest.TestCase):
    def test_mu_composite_charges(self):
        l, r = composite_charges(+1)
        self.assertEqual(l[0], -1)
        self.assertEqual(r[0], -1)
        self.assertEqual(sp.simplify(l[1]-Q), 0)
        self.assertEqual(sp.simplify(r[1]-Q), 0)
        self.assertEqual(l[2], "singlet")
        self.assertEqual(r[2], "singlet")

    def test_tau_composite_charges(self):
        l, r = composite_charges(-1)
        self.assertEqual(l[0], -1)
        self.assertEqual(r[0], -1)
        self.assertEqual(sp.simplify(l[1]+Q), 0)
        self.assertEqual(sp.simplify(r[1]+Q), 0)
        self.assertEqual(l[2], "singlet")
        self.assertEqual(r[2], "singlet")

    def test_B_contact_same_for_both_flavors(self):
        mu = eft_contact_coefficients(+1)
        tau = eft_contact_coefficients(-1)
        self.assertEqual(mu["B"], -gY)
        self.assertEqual(tau["B"], -gY)

    def test_Aprime_contact_flips_with_eta(self):
        mu = eft_contact_coefficients(+1)
        tau = eft_contact_coefficients(-1)
        self.assertEqual(sp.simplify(mu["A_prime"]-Q*gX), 0)
        self.assertEqual(sp.simplify(tau["A_prime"]+Q*gX), 0)

    def test_no_direct_W_contact(self):
        self.assertEqual(eft_contact_coefficients(+1)["W"], 0)
        self.assertEqual(eft_contact_coefficients(-1)["W"], 0)
        self.assertTrue(weak_singlet_covariant_derivative_check())


if __name__ == "__main__":
    unittest.main(verbosity=2)
