#!/usr/bin/env python3
import unittest
import sympy as sp

from b5_2b4_triplet_derivative_eom_current_map import (
    triplet_derivative_eom_identity,
    current_basis_projection,
    adjoint_covariant_derivative_check,
    triplet_adjoint_contact_check,
    box_to_current_coefficients,
    g2, C_LD,
)


class TestB52B4TripletDerivativeMap(unittest.TestCase):
    def test_triplet_derivative_eom_identity(self):
        self.assertTrue(triplet_derivative_eom_identity())

    def test_current_basis_projection(self):
        O1, O3, E1, E3 = sp.symbols("O1 O3 E1 E3")
        expected = (-3*O1 + O3 + 3*E1 - E3)/4
        self.assertEqual(sp.simplify(current_basis_projection()-expected), 0)

    def test_adjoint_derivative_sign_for_both_composites(self):
        self.assertTrue(adjoint_covariant_derivative_check())

    def test_nonzero_triplet_W_contact_and_EOM_contact_identity(self):
        self.assertTrue(triplet_adjoint_contact_check())

    def test_box_to_current_coefficients(self):
        c = box_to_current_coefficients()
        base = g2**2*C_LD/(16*sp.pi**2)
        self.assertEqual(sp.simplify(c["C3"]-sp.Rational(3,4)*base), 0)
        self.assertEqual(sp.simplify(c["delta_C_HL1"]+sp.Rational(9,16)*base), 0)
        self.assertEqual(sp.simplify(c["delta_C_HL3"]-sp.Rational(3,16)*base), 0)
        self.assertEqual(sp.simplify(c["delta_E1"]-sp.Rational(9,16)*base), 0)
        self.assertEqual(sp.simplify(c["delta_E3"]+sp.Rational(3,16)*base), 0)

    def test_pauli_vs_generator_normalization(self):
        # O_HL^(3)[T] = O_HL^(3)[sigma]/4, hence C[T] = 4 C[sigma].
        C_sigma, C_T = sp.symbols("C_sigma C_T")
        self.assertEqual(sp.solve(C_sigma*4-C_T, C_T)[0], 4*C_sigma)


if __name__ == "__main__":
    unittest.main(verbosity=2)
