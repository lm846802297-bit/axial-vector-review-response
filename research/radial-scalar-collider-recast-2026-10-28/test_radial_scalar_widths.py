"""Tests for the original paper one-VEV radial-scalar width scaffold."""

import math
import unittest

from radial_scalar_widths import (
    M_MU_GEV,
    evaluate_point,
    fermion_pair_width,
    leptophilic_scalar_xi_from_vs,
    rescale_coupling_limit_for_branching_fraction,
    vector_pair_width,
)


class RadialScalarWidthsTests(unittest.TestCase):
    def test_fermion_threshold_and_formula(self):
        self.assertEqual(fermion_pair_width(2.0 * M_MU_GEV, 0.1, M_MU_GEV), 0.0)
        ms, y, mf = 1.0, 0.02, M_MU_GEV
        expected = y**2 * ms / (8.0 * math.pi) * (1.0 - 4.0 * mf**2 / ms**2) ** 1.5
        self.assertAlmostEqual(fermion_pair_width(ms, y, mf), expected, places=15)

    def test_vector_threshold(self):
        self.assertEqual(vector_pair_width(1.0, 0.6, 2.0), 0.0)
        self.assertGreater(vector_pair_width(1.3, 0.6, 2.0), 0.0)

    def test_vev_and_lambda_relation(self):
        point = evaluate_point(1.0, 0.2, 0.1)
        self.assertAlmostEqual(point["vs_GeV"], 1.0)
        self.assertAlmostEqual(point["lambdaS"], 0.5)
        self.assertAlmostEqual(point["y_smu"], M_MU_GEV)

    def test_fractions_are_only_among_included_channels_by_default(self):
        point = evaluate_point(1.0, 0.6, 0.1)
        fractions = point["fractions_among_included_channels"]
        self.assertTrue(fractions)
        self.assertAlmostEqual(sum(fractions.values()), 1.0)
        self.assertFalse(point["branching_fractions_complete"])
        self.assertIsNone(point["ctau_m"])
        self.assertIn("partial_widths_only", point["status"])

    def test_lifetime_only_returned_after_explicit_completeness_assertion(self):
        point = evaluate_point(
            1.0,
            0.6,
            0.1,
            additional_widths_GeV={"other_open_channels": 1.0e-10},
            all_channels_included=True,
        )
        self.assertTrue(point["branching_fractions_complete"])
        self.assertGreater(point["ctau_m"], 0.0)

    def test_negative_extra_width_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_point(1.0, 0.6, 0.1, additional_widths_GeV={"bad": -1.0})

    def test_belle_ii_leptophilic_xi_normalization(self):
        self.assertAlmostEqual(leptophilic_scalar_xi_from_vs(246.0), 1.0)
        self.assertAlmostEqual(leptophilic_scalar_xi_from_vs(123.0), 2.0)
        with self.assertRaises(ValueError):
            leptophilic_scalar_xi_from_vs(0.0)

    def test_branching_fraction_limit_rescaling(self):
        # Same production normalization: halving the UV BR weakens the
        # coupling limit by sqrt(2).
        result = rescale_coupling_limit_for_branching_fraction(
            coupling_limit_benchmark=0.01,
            br_benchmark=1.0,
            br_uv=0.5,
        )
        self.assertAlmostEqual(result, 0.01 * math.sqrt(2.0), places=14)
        with self.assertRaises(ValueError):
            rescale_coupling_limit_for_branching_fraction(0.01, 1.1, 0.5)
        with self.assertRaises(ValueError):
            rescale_coupling_limit_for_branching_fraction(0.01, 0.5, 0.0)

    def test_tau_threshold_changes_uv_dimuon_and_tautau_fractions(self):
        # Choose mA well above ms/2 so that s -> A'A' is closed.
        near_threshold = evaluate_point(3.6, 10.0, 0.1)
        above_threshold = evaluate_point(4.0, 10.0, 0.1)
        br_tau_36 = near_threshold["fractions_among_included_channels"]["tau_tau"]
        br_tau_40 = above_threshold["fractions_among_included_channels"]["tau_tau"]
        self.assertAlmostEqual(br_tau_36, 0.5372, places=3)
        self.assertAlmostEqual(br_tau_40, 0.9649, places=3)
        self.assertGreater(br_tau_40, br_tau_36)

    def test_open_vector_pair_can_suppress_tau_branching(self):
        point = evaluate_point(4.0, 0.5, 0.1)
        widths = point["partial_widths_GeV"]
        self.assertGreater(widths["Aprime_Aprime"], widths["tau_tau"])


if __name__ == "__main__":
    unittest.main()
