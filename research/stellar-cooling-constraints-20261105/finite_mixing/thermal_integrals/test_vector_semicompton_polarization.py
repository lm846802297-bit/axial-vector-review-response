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

    def test_paper_eq58_mode_assignment_and_coefficient_are_flagged_not_relabelled(self):
        comparison = self.audit["printed_Eq58_comparison"]
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

    def test_printed_eq106_differential_formulas_are_flagged_for_negativity(self):
        diagnostic = self.audit["printed_Eq106_differential_comparison"]
        self.assertGreater(diagnostic["Eq106a_printed_T_negative_fraction"], 0.4)
        self.assertGreater(diagnostic["Eq106b_printed_L_negative_fraction"], 0.0)
        self.assertGreaterEqual(diagnostic["exact_T_minimum_over_angular_grid_MeV_minus2"], 0.0)
        self.assertGreaterEqual(diagnostic["exact_L_minimum_over_angular_grid_MeV_minus2"], 0.0)
        self.assertTrue(
            self.audit["interpretation_flags"]["Eq106b_shape_tracks_exact_transverse_mode"]
        )

    def test_paper_eq58_mode_hierarchy_is_opposite_to_conserved_vector_limit(self):
        self.assertTrue(
            self.audit["interpretation_flags"][
                "integrated_Eq58_TL_hierarchy_opposite_to_conserved_vector_limit"
            ]
        )

    def test_angular_quadrature_is_converged(self):
        self.assertTrue(self.audit["acceptance"]["quadrature_convergence_pass"])


if __name__ == "__main__":
    unittest.main()
