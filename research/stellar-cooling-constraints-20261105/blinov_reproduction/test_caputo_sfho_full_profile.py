import unittest

import numpy as np

from build_caputo_sfho_full_profile import build_profile_rows
from map_caputo_sfho_eos_full_profile import axis_domain, bracket


class TestBuildFullCaputoProfile(unittest.TestCase):
    def setUp(self):
        self.temperature = [
            {"r_km": "0.0", "value": "10.0"},
            {"r_km": "1.0", "value": "20.0"},
        ]
        self.composition = [
            {
                "r_km": f"{r:.2f}",
                "nB_over_n0": "1.0",
                "Yn": "0.8",
                "Yp": "0.2",
                "Ye_plus_Ymu": "0.2",
                "Xcluster": "0.0",
                "Ycluster_charge": "0.0",
            }
            for r in (0.20, 0.25, 0.30)
        ]

    def test_interpolates_temperature_and_builds_separate_densities(self):
        rows = build_profile_rows(self.temperature, self.composition, 0.05)
        self.assertEqual(len(rows), 3)
        self.assertAlmostEqual(rows[0]["T_MeV"], 12.0)
        self.assertAlmostEqual(rows[1]["T_MeV"], 12.5)
        self.assertAlmostEqual(rows[2]["T_MeV"], 13.0)
        self.assertAlmostEqual(rows[0]["nB_fm3"], 0.181)
        self.assertAlmostEqual(rows[0]["n_n_free_fm3"], 0.8 * 0.181)
        self.assertAlmostEqual(rows[0]["n_p_free_fm3"], 0.2 * 0.181)
        self.assertAlmostEqual(rows[0]["n_cluster_baryon_fm3"], 0.0)
        self.assertAlmostEqual(
            rows[0]["n_n_free_fm3"] + rows[0]["n_p_free_fm3"]
            + rows[0]["n_cluster_baryon_fm3"],
            rows[0]["nB_fm3"],
        )

    def test_rejects_temperature_extrapolation(self):
        temperature = [
            {"r_km": "0.25", "value": "10.0"},
            {"r_km": "1.0", "value": "20.0"},
        ]
        with self.assertRaisesRegex(ValueError, "would extrapolate"):
            build_profile_rows(temperature, self.composition, 0.05)

    def test_rejects_nonuniform_composition_grid(self):
        composition = [dict(row) for row in self.composition]
        composition[2]["r_km"] = "0.31"
        with self.assertRaisesRegex(ValueError, "uniform radial grid"):
            build_profile_rows(self.temperature, composition, 0.05)

    def test_rejects_nonclosing_cluster_charge(self):
        composition = [dict(row) for row in self.composition]
        composition[1]["Ye_plus_Ymu"] = "0.21"
        with self.assertRaisesRegex(ValueError, "cluster charge"):
            build_profile_rows(self.temperature, composition, 0.05)

    def test_rejects_wrong_or_invalid_total_proton_fraction(self):
        composition = [dict(row) for row in self.composition]
        composition[1]["Ye_plus_Ymu"] = "0.19"
        with self.assertRaisesRegex(ValueError, "cluster charge"):
            build_profile_rows(self.temperature, composition, 0.05)

    def test_rejects_nonpositive_density(self):
        composition = [dict(row) for row in self.composition]
        composition[1]["nB_over_n0"] = "0"
        with self.assertRaisesRegex(ValueError, "non-positive"):
            build_profile_rows(self.temperature, composition, 0.05)


class TestEOSInterpolationBounds(unittest.TestCase):
    def test_bracket_returns_correct_linear_weight(self):
        axis = np.asarray([0.0, 1.0, 2.0, 3.0])
        self.assertEqual(bracket(axis, 0.0), (0, 1, 0.0))
        self.assertEqual(bracket(axis, 1.5), (1, 2, 0.5))
        self.assertEqual(bracket(axis, 3.0), (2, 3, 1.0))

    def test_bracket_rejects_extrapolation(self):
        axis = np.asarray([0.0, 1.0, 2.0])
        with self.assertRaises(ValueError):
            bracket(axis, -1e-4)
        with self.assertRaises(ValueError):
            bracket(axis, 2.0001)

    def test_axis_domain_reports_nonnegative_boundary_margins(self):
        result = axis_domain(
            np.asarray([0.0, 1.0, 2.0]),
            np.asarray([0.2, 1.5]),
        )
        self.assertTrue(result["within_bounds"])
        self.assertAlmostEqual(result["lower_margin"], 0.2)
        self.assertAlmostEqual(result["upper_margin"], 0.5)

    def test_axis_domain_detects_out_of_range_profile(self):
        result = axis_domain(
            np.asarray([0.0, 1.0, 2.0]),
            np.asarray([-0.01, 1.5]),
        )
        self.assertFalse(result["within_bounds"])
        self.assertLess(result["lower_margin"], 0.0)


if __name__ == "__main__":
    unittest.main()
