import unittest

from audit_croon_fig2_outer_opacity_gap import analyze_outer_opacity_gap


class CroonOuterOpacityGapTests(unittest.TestCase):
    def setUp(self):
        g = [1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2]
        model_solid = [1, 10, 100, 100, 50, 20, 10]
        model_dashed = [1, 10, 100, 100, 50, 20, 10]
        paper_solid = [1, 10, 25, 25, 12.5, 5, 2.5]
        paper_dashed = [1, 10, 100, 100, 50, 20, 10]
        self.model = {
            "status": "synthetic",
            "profile": {"sha256": "profile"},
            "curves": {
                "0.1 eV": {"mass_mev": 1e-7, "g": g, "L_erg_s": model_solid},
                "0.1 eV (Rfar=Rnu)": {"mass_mev": 1e-7, "g": g, "L_erg_s": model_dashed},
            },
        }
        self.digitized = {
            "source_pdf_sha256": "pdf",
            "curves": {
                "0.1 eV": {"points": [{"g": x, "L_erg_s": y} for x, y in zip(g, paper_solid)]},
                "0.1 eV (Rfar=Rnu)": {"points": [{"g": x, "L_erg_s": y} for x, y in zip(g, paper_dashed)]},
            },
        }

    def test_recovers_missing_outer_suppression_and_log_ratio(self):
        result = analyze_outer_opacity_gap(
            self.model, self.digitized,
            plateau_g_range=(1e-6, 1e-2), low_g_range=(1e-8, 1e-7)
        )
        plateau = result["strong_coupling_plateau"]
        self.assertEqual(plateau["additional_missing_luminosity_suppression"]["count"], 5)
        self.assertAlmostEqual(
            plateau["additional_missing_luminosity_suppression"]["median"], 4.0,
            places=12
        )
        self.assertAlmostEqual(
            plateau["effective_log_suppression_ln_ratio"]["median"], 1.38629436112,
            places=10
        )

    def test_weak_branch_does_not_claim_missing_opacity(self):
        result = analyze_outer_opacity_gap(
            self.model, self.digitized,
            plateau_g_range=(1e-6, 1e-2), low_g_range=(1e-8, 1e-7)
        )
        weak = result["weak_branch"]
        self.assertEqual(weak["additional_missing_luminosity_suppression"]["median"], 1.0)

    def test_rejects_extrapolation_and_missing_curve(self):
        bad = {"curves": {"0.1 eV": self.model["curves"]["0.1 eV"]}}
        with self.assertRaisesRegex(ValueError, "Missing required"):
            analyze_outer_opacity_gap(bad, self.digitized)


if __name__ == "__main__":
    unittest.main(verbosity=2)
