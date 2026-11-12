import json
import unittest

import numpy as np

import rates
from finite_mixing.thermal_integrals.audit_vector_semicompton_polarization import (
    build_audit,
    exact_production_cross_sections,
    json_native,
)


class VectorSemiComptonPolarizationAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = build_audit(0.001, 0.1)

    def test_audit_payload_is_json_serializable(self):
        encoded = json.dumps(json_native(self.audit))
        self.assertIsInstance(encoded, str)
        self.assertIn('"acceptance"', encoded)

    def test_exact_cross_sections_are_nonnegative_for_all_modes(self):
        mass = 0.001
        photon_energy = 0.1
        e_vector = photon_energy - mass * mass / (2.0 * rates.M_MU)
        cosines = np.array([-0.999, -0.7, 0.0, 0.7, 0.999])
        _, matrix_elements = rates.compton_matrix_elements(
            mass, [e_vector], cosines, current="vector"
        )
        _, kernels = rates.compton_kernels(
            mass, [e_vector], order=128, current="vector"
        )
        self.assertGreaterEqual(float(np.min(matrix_elements)), -1e-11)
        self.assertGreaterEqual(float(np.min(kernels)), -1e-14)
        self.assertTrue(self.audit["positivity"]["direct_exact_mode_cross_sections_nonnegative"])
        self.assertTrue(self.audit["positivity"]["direct_exact_differential_cross_sections_nonnegative"])

    def test_thomson_limit_is_transverse_and_vector_longitudinal_is_suppressed(self):
        acceptance = self.audit["acceptance"]
        self.assertTrue(acceptance["thomson_transverse_limit_pass"])
        self.assertTrue(acceptance["conserved_vector_longitudinal_suppression_pass"])
        ratios = self.audit["ratios_to_thomson"]
        self.assertAlmostEqual(ratios["direct_exact_T_sum"], 1.0, delta=5e-3)
        self.assertLess(ratios["direct_exact_L"], 1e-3)

    def test_paper_eq5_9_mode_assignment_and_coefficient_are_flagged_not_relabelled(self):
        comparison = self.audit["printed_Eq5_9_comparison"]
        # The printed unsuppressed expression tracks the exact transverse sum,
        # while the printed suppressed expression has the opposite mode label.
        self.assertAlmostEqual(
            comparison["paper_L_over_exact_T_sum"], 1.0, delta=5e-3
        )
        # The residual suppressed coefficient remains a separate discrepancy.
        self.assertGreater(comparison["paper_T_over_exact_L"], 1.35)
        self.assertLess(comparison["paper_T_over_exact_L"], 1.65)
        self.assertLess(comparison["exact_L_over_exact_T_sum"], 1e-3)

    def test_mode_projectors_are_orthogonal_and_complete_in_medium_frame(self):
        self.assertTrue(self.audit["acceptance"]["medium_frame_projectors_pass"])

    def test_photon_and_vector_mediator_ward_identities(self):
        self.assertTrue(self.audit["acceptance"]["photon_ward_pass"])
        self.assertTrue(self.audit["acceptance"]["vector_mediator_ward_pass"])

    def test_direct_spinor_and_crossed_trace_calculations_agree(self):
        self.assertTrue(self.audit["acceptance"]["direct_spinor_vs_crossed_trace_pass"])

    def test_printed_eqb6_differential_formulas_are_flagged_for_negativity(self):
        diagnostic = self.audit["printed_EqB6_differential_comparison"]
        self.assertGreater(diagnostic["EqB6a_printed_T_negative_fraction"], 0.4)
        self.assertGreater(diagnostic["EqB6b_printed_L_negative_fraction"], 0.0)
        self.assertGreaterEqual(diagnostic["exact_T_minimum_over_angular_grid_MeV_minus2"], 0.0)
        self.assertGreaterEqual(diagnostic["exact_L_minimum_over_angular_grid_MeV_minus2"], 0.0)
        flags = self.audit["interpretation_flags"]
        self.assertTrue(
            flags["EqB6b_is_closer_to_exact_T_than_EqB6a_but_not_accurate"]
        )
        self.assertTrue(flags["EqB6_differential_shapes_fail_the_low_energy_reference"])

    def test_appendix_B_matrix_element_traces_match_direct_spinor_sum(self):
        audit = self.audit["appendix_B_trace_audit"]
        self.assertEqual(len(audit["cases"]), 6)
        self.assertTrue(all(audit["acceptance"].values()))
        self.assertLess(audit["max_abs_B2_T_relative_residual"], 5e-5)
        self.assertLess(audit["max_abs_B4_total_relative_residual"], 5e-5)
        self.assertLess(audit["max_abs_B3_L_relative_residual"], 0.015)

    def test_eqb6_angular_shapes_fail_while_exact_shapes_recover_thomson_limit(self):
        angular = self.audit["low_energy_angular_shape_audit"]
        self.assertTrue(
            angular["acceptance"]["exact_T_matches_leading_Thomson_shape"]
        )
        self.assertTrue(
            angular["acceptance"]["exact_L_matches_leading_suppressed_shape"]
        )
        self.assertTrue(
            angular["acceptance"]["printed_EqB6a_fails_exact_L_angular_shape"]
        )
        self.assertTrue(
            angular["acceptance"]["printed_EqB6b_fails_exact_T_angular_shape"]
        )
        self.assertGreater(
            angular["printed_EqB6b_vs_exact_T_max_abs_over_exact_T_peak"], 0.5
        )

    def test_eq5_9_hierarchy_and_longitudinal_coefficient_persist_across_low_energy_scan(self):
        scan = self.audit["low_energy_parameter_scan"]
        self.assertTrue(all(scan["acceptance"].values()))
        self.assertEqual(len(scan["cases"]), 6)
        self.assertGreater(
            scan["max_abs_deviation_Eq5_9a_over_exact_L_from_three_halves"], 0.0
        )

    def test_paper_eq5_9_mode_hierarchy_is_opposite_to_conserved_vector_limit(self):
        self.assertTrue(
            self.audit["interpretation_flags"][
                "integrated_Eq5_9_TL_hierarchy_opposite_to_conserved_vector_limit"
            ]
        )

    def test_angular_quadrature_is_converged(self):
        self.assertTrue(self.audit["acceptance"]["quadrature_convergence_pass"])


if __name__ == "__main__":
    unittest.main()
