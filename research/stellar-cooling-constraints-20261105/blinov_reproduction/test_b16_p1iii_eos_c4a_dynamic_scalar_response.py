import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4a_dynamic_scalar_response import (
    analyze,
    load_c2_reference,
)

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_REFERENCE = HERE / "outputs" / "p1iii_eos_full_radial_occupation_2026-11-11.csv"


class TestC4AEOSDynamicScalarResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.response, cls.sumrules, cls.summary = analyze(
            load_profile(PROFILE),
            load_c2_reference(C2_REFERENCE),
        )

    def test_selected_radii_and_response_grid_shape(self):
        self.assertEqual(len(self.sumrules), 56)
        self.assertEqual(len(self.response), 13440)
        self.assertEqual(
            self.summary["provenance"]["selected_radii_km"],
            [0.2, 5.0, 10.0, 15.2],
        )

    def test_dynamic_static_sum_rule(self):
        for row in self.sumrules:
            self.assertLess(abs(row["sum_rule_relative_residual"]), 1e-8)
            self.assertGreater(row["I_dynamic_MeV3"], 0.0)
            self.assertGreater(row["I_static_MeV3"], 0.0)

    def test_detailed_balance(self):
        for species in ("n", "p"):
            self.assertLess(
                self.summary["species"][species][
                    "max_abs_detailed_balance_relative_residual"
                ],
                1e-8,
            )

    def test_q_zero_susceptibility_limit(self):
        for species in ("n", "p"):
            result = self.summary["species"][species]
            self.assertLess(result["max_abs_q1_static_vs_q0_blocked"], 1e-4)
            self.assertLess(result["max_abs_q3_static_vs_q0_blocked"], 1e-3)

    def test_response_nonnegative_and_all_acceptance_criteria(self):
        self.assertTrue(all(row["S_MeV2"] >= 0.0 for row in self.response))
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))


if __name__ == "__main__":
    unittest.main()
