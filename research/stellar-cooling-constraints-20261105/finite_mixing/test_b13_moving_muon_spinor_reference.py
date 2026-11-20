import unittest

import numpy as np

from finite_mixing.thermal_integrals.audit_b13_moving_muon_spinor_reference import (
    CURRENT_CASES,
    KINEMATIC_POINTS,
    explicit_spinor_kernel,
    run_audit,
)
from finite_mixing.moving_muon_compton import moving_muon_point_kernel


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

    def test_low_mass_longitudinal_mode_matches_independent_explicit_spinors(self):
        # At m_A'=0.1 eV, the physical longitudinal polarization is nearly
        # q^mu/m_A'. The old covariant -g photon trace suffers catastrophic
        # cancellation at this point; the positive physical-photon spin sum
        # must remain finite and agree with the independent spinor reference.
        point = (
            1.0e-7,
            5.332961631033191e-4,
            640.1416278200652,
            0.525532409916329,
            0.9602898564975362,
            2.5653157283115897,
        )
        for label, g_vector, g_axial, charge_sign in CURRENT_CASES:
            with self.subTest(current=label):
                stable = moving_muon_point_kernel(
                    *point, g_vector, g_axial, charge_sign
                )
                reference = explicit_spinor_kernel(
                    *point, g_vector, g_axial, charge_sign
                )
                np.testing.assert_allclose(
                    stable["matrix_element_squared_by_mode"],
                    reference["matrix_element_squared_by_mode"],
                    rtol=5.0e-8,
                    atol=1.0e-12,
                )
                self.assertTrue(
                    all(x >= 0.0 for x in stable["matrix_element_squared_by_mode"])
                )
                self.assertLess(
                    max(stable["photon_ward_relative_residual_by_mode"]),
                    1.0e-8,
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
