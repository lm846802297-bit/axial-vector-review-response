import unittest

from compare_croon_fig2_digitized_curves import compare_curves


class CroonFig2DigitizedComparisonTests(unittest.TestCase):
    def setUp(self):
        self.model = {
            "status": "synthetic-test",
            "profile": {"sha256": "profile-test"},
            "curves": {
                "10 MeV": {
                    "mass_mev": 10.0,
                    "g": [1e-10, 1e-9, 1e-8, 1e-7],
                    "L_erg_s": [1e50, 1e52, 1e54, 1e52],
                },
                "0.1 eV (Rfar=Rnu)": {
                    "mass_mev": 1e-7,
                    "g": [1e-10, 1e-9, 1e-8],
                    "L_erg_s": [2e50, 2e52, 2e54],
                },
            },
        }
        self.digitized = {
            "source_pdf_sha256": "pdf-test",
            "source_page_index": 11,
            "axis_calibration": {"x_tick_fit_max_abs_residual_dex": 1e-7},
            "curves": {
                "10 MeV": {
                    "source_path_index": 123,
                    "points": [
                        {"g": 1e-10, "L_erg_s": 1e50},
                        {"g": 1e-9, "L_erg_s": 1e52},
                        {"g": 1e-8, "L_erg_s": 1e54},
                        {"g": 1e-7, "L_erg_s": 1e52},
                    ],
                },
                "0.1 eV (Rfar=Rnu)": {
                    "source_path_index": 124,
                    "points": [
                        {"g": 1e-10, "L_erg_s": 2e50},
                        {"g": 1e-9, "L_erg_s": 2e52},
                        {"g": 1e-8, "L_erg_s": 2e54},
                    ],
                },
            },
        }

    def test_exact_model_digitization_has_zero_residual(self):
        result = compare_curves(self.model, self.digitized)
        for curve in result["curve_results"].values():
            self.assertEqual(curve["all_points"]["point_count"], 4 if curve["mass_MeV"] == 10 else 3)
            self.assertLess(curve["all_points"]["maximum_absolute_residual_dex"], 2e-14)
            self.assertAlmostEqual(curve["all_points"]["median_model_over_digitized"], 1.0, places=13)

    def test_residual_sign_and_branch_split_are_explicit(self):
        digitized = {
            "source_pdf_sha256": "pdf-test",
            "curves": {
                "10 MeV": {
                    "source_path_index": 123,
                    "points": [
                        {"g": 1e-10, "L_erg_s": 1e49},
                        {"g": 1e-9, "L_erg_s": 1e51},
                        {"g": 1e-8, "L_erg_s": 1e53},
                        {"g": 1e-7, "L_erg_s": 1e51},
                    ],
                }
            },
        }
        result = compare_curves(self.model, digitized)["curve_results"]["10 MeV"]
        self.assertAlmostEqual(result["all_points"]["median_residual_dex_model_minus_digitized"], 1.0, places=13)
        self.assertEqual(result["low_g_branch"]["point_count"], 3)
        self.assertEqual(result["high_g_branch"]["point_count"], 1)

    def test_digitized_points_outside_model_range_are_reported(self):
        digitized = {
            "source_pdf_sha256": "pdf-test",
            "curves": {
                "10 MeV": {
                    "source_path_index": 123,
                    "points": [
                        {"g": 1e-12, "L_erg_s": 1e40},
                        {"g": 1e-9, "L_erg_s": 1e52},
                        {"g": 1e-6, "L_erg_s": 1e40},
                    ],
                }
            },
        }
        result = compare_curves(self.model, digitized)["curve_results"]["10 MeV"]
        self.assertEqual(result["used_point_count"], 1)
        self.assertEqual(result["excluded_outside_model_range_count"], 2)

    def test_missing_model_counterpart_is_rejected(self):
        digitized = {"curves": {"missing": {"points": []}}}
        with self.assertRaisesRegex(ValueError, "no model counterpart"):
            compare_curves(self.model, digitized)

    def test_nonpositive_model_luminosities_are_not_log_interpolated(self):
        model = {
            "curves": {
                "10 MeV": {
                    "mass_mev": 10.0,
                    "g": [1e-10, 1e-9, 1e-8],
                    "L_erg_s": [1e50, 0.0, 1e54],
                }
            }
        }
        digitized = {
            "curves": {
                "10 MeV": {
                    "points": [{"g": 1e-9, "L_erg_s": 1e52}],
                }
            }
        }
        with self.assertRaisesRegex(ValueError, "no digitized points overlap"):
            compare_curves(model, digitized)


if __name__ == "__main__":
    unittest.main(verbosity=2)
