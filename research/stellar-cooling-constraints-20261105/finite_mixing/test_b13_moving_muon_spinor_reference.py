import unittest

from finite_mixing.thermal_integrals.audit_b13_moving_muon_spinor_reference import (
    CURRENT_CASES,
    KINEMATIC_POINTS,
    run_audit,
)


class B13MovingMuonExplicitSpinorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_audit()

    def test_all_modes_match_independent_explicit_spinor_sum(self):
        summary = self.result["summary"]
        self.assertLess(
            summary["maximum_explicit_spinor_vs_dirac_trace_relative_residual"],
            1.0e-10,
        )
        self.assertEqual(
            self.result["total_point_current_cases"],
            len(KINEMATIC_POINTS) * len(CURRENT_CASES),
        )

    def test_photon_ward_identity_for_both_charges_and_mixed_current(self):
        self.assertLess(
            self.result["summary"]["maximum_explicit_photon_ward_amplitude_residual"],
            1.0e-10,
        )

    def test_final_muon_mass_shell(self):
        self.assertLess(
            self.result["summary"]["maximum_final_muon_shell_relative_error"],
            1.0e-10,
        )

    def test_vector_longitudinal_ward_shift_is_exact(self):
        self.assertLess(
            self.result["summary"]["maximum_vector_longitudinal_ward_shift_relative_residual"],
            1.0e-10,
        )

    def test_all_explicit_mode_matrix_elements_are_nonnegative(self):
        self.assertTrue(
            self.result["summary"]["all_mode_matrix_elements_nonnegative"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
