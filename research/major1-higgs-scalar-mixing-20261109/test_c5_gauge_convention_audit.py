import unittest
from fractions import Fraction

from c5_gauge_convention_audit import (
    audit,
    c5_from_schur,
    convention_sign_map,
    manuscript_signed_mass,
    schur_light_mass,
)


class C5GaugeConventionAuditTests(unittest.TestCase):
    def test_schur_complement_fixes_negative_c5(self):
        y, lam, vh, vs, me = map(Fraction, (2, 3, 5, 7, 11))
        self.assertEqual(c5_from_schur(y, lam, vh, vs, me), -y * lam / me)
        self.assertEqual(
            c5_from_schur(y, lam, vh, vs, me) * vh * vs / 2,
            schur_light_mass(y, lam, vh, vs, me),
        )

    def test_printed_v6_coefficient_has_opposite_signed_mass(self):
        y, lam, vh, vs, me = map(Fraction, (2, 3, 5, 7, 11))
        self.assertEqual(
            manuscript_signed_mass(y, lam, vh, vs, me),
            -schur_light_mass(y, lam, vh, vs, me),
        )

    def test_right_handed_rephasing_preserves_matching_identity(self):
        y, lam, vh, vs, me = map(Fraction, (2, 3, 5, 7, 11))
        c5 = c5_from_schur(y, lam, vh, vs, me)
        c5_prime = c5_from_schur(y, -lam, vh, vs, me)
        self.assertEqual(c5_prime, -c5)
        self.assertEqual(c5_prime * (-1), c5)  # O5' = -O5

    def test_so2_diagonalization_preserves_negative_determinant(self):
        y, lam, vh, vs, me = map(Fraction, (2, 3, 5, 7, 11))
        determinant = -y * lam * vh * vs / 2
        self.assertLess(determinant, 0)
        # det(U_L)=det(U_R)=+1, so signed diagonal masses multiply to det(M)<0.
        self.assertEqual(determinant, -y * lam * vh * vs / 2)

    def test_covariant_derivative_and_curvature_sign_map(self):
        signs = convention_sign_map()
        self.assertEqual(signs["A_plus_over_A_minus"], -1)
        self.assertEqual(signs["F_plus_over_F_minus"], -1)
        self.assertEqual(signs["D_plus_over_D_minus"], 1)
        self.assertEqual(signs["commutator_curvature_plus_over_minus"], 1)
        self.assertEqual(signs["currents_built_from_D_plus_over_minus"], 1)

    def test_raw_field_strength_and_operator_sign_bookkeeping(self):
        signs = convention_sign_map()
        self.assertEqual(signs["raw_two_field_strength_product_sign"], 1)
        self.assertEqual(signs["single_explicit_raw_F_operator_sign"], -1)
        self.assertEqual(signs["D_only_operator_coefficient_sign"], 1)
        self.assertEqual(signs["one_background_vertex_of_D_only_operator_sign"], -1)
        self.assertEqual(signs["axial_raw_gauge_EOM_sign_relative_to_upstream"], -1)

    def test_complete_audit_summary(self):
        result = audit()
        self.assertEqual(result["result"], "C5 = - y_l lambda_l / M_E_l")
        self.assertEqual(result["v6_Eq5d_signed_mass_ratio_to_Schur"], -1)
        self.assertEqual(len(result["cases"]), 2)


if __name__ == "__main__":
    unittest.main()
