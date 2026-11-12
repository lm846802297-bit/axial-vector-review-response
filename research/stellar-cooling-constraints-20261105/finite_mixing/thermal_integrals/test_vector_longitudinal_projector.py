"""Regression tests for the direct vector-current P_L projection."""
import unittest

from .audit_vector_longitudinal_projector import M_MU, build_audit


class DirectLongitudinalProjectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = build_audit()
        cls.summary = cls.audit["summary"]

    def test_physical_projector_and_ward_representative_agree(self):
        self.assertLess(self.summary["max_physical_vs_Ward_rel"], 1e-5)
        self.assertLess(self.summary["max_trace_vs_spinor_rel"], 1e-8)

    def test_vector_ward_identity_and_printed_u_channel_order(self):
        self.assertLess(self.summary["max_correct_qWard_rel_amplitude"], 1e-10)
        self.assertGreater(
            self.summary["min_literal_B1b_wrong_u_qWard_rel_amplitude"], 1e-2
        )

    def test_direct_longitudinal_response_is_positive_and_has_expected_shape(self):
        self.assertTrue(self.summary["all_direct_longitudinal_rates_positive"])
        self.assertLess(
            self.summary["max_L_over_T_x2_shape_error_E_le_0p1_x_le_0p01"],
            1e-2,
        )

    def test_small_x_recoil_residual_laws(self):
        selected = [
            r for r in self.audit["cases"]
            if r["x"] == 0.001 and r["Egamma_MeV"] <= 0.1
        ]
        for r in selected:
            c = r["cos_theta"]
            recoil = r["Egamma_MeV"] / M_MU
            b2_leading = 2.0 * r["x"]**2 * recoil / (1.0 + c**2)
            b3_leading = -2.0 * recoil / (1.0 - c**2)
            self.assertLess(abs(r["B2_relative_residual"] / b2_leading - 1.0), 0.002)
            self.assertLess(abs(r["B3_relative_residual"] / b3_leading - 1.0), 0.002)


if __name__ == "__main__":
    unittest.main()
