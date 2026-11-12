import unittest
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_full_radial_degeneracy_radial_diagnostics import (
    analyze,
    load_c2_reference,
)

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_REFERENCE = HERE / "outputs" / "p1iii_eos_full_radial_occupation_2026-11-11.csv"


class TestFullRadialDegeneracyRadialDiagnostics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records, cls.summary = analyze(
            load_profile(PROFILE),
            load_c2_reference(C2_REFERENCE),
        )

    def test_all_301_radii_and_both_species_are_present(self):
        self.assertEqual(len(self.records), 602)
        self.assertEqual(
            [(row["r_km"], row["species"]) for row in self.records[:4]],
            [(0.2, "n"), (0.2, "p"), (0.25, "n"), (0.25, "p")],
        )

    def test_relativistic_baseline_reproduces_c2(self):
        self.assertLess(
            max(
                self.summary["species"]["n"]["max_abs_C2_reproduction_difference"],
                self.summary["species"]["p"]["max_abs_C2_reproduction_difference"],
            ),
            5e-12,
        )

    def test_nonrelativistic_comparisons_are_density_consistent(self):
        for species in ("n", "p"):
            result = self.summary["species"][species]["nonrelativistic_density_matched"]
            self.assertLess(result["max_abs_density_match_residual"], 1e-8)
            self.assertTrue(result["all_points_nonrel_below_rel"])
        self.assertTrue(all(
            row["NR_fixed_nu_relative_shift"] < 0.0
            and row["NR_density_matched_relative_shift"] < 0.0
            for row in self.records
        ))

    def test_dimensionless_eta_dominates_radial_monotonicity(self):
        for species in ("n", "p"):
            corr = self.summary["species"][species]["correlations"]["Fdeg_vs_eta"]
            self.assertLess(corr["spearman_rho"], -0.999)
            self.assertGreater(
                self.summary["species"][species]["linear_regression_R2"]["eta_only"],
                0.95,
            )

    def test_composition_closure_and_all_acceptance_criteria(self):
        self.assertLess(self.summary["composition_closure_max_abs"], 1e-8)
        self.assertTrue(self.summary["overall_pass"])
        self.assertTrue(all(self.summary["acceptance"].values()))


if __name__ == "__main__":
    unittest.main()
