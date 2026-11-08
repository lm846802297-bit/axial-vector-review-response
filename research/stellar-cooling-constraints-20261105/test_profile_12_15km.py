import unittest
from pathlib import Path

import numpy as np

from audit_profile_12_15km import (
    density_and_susceptibility, interp_curve, read_curve, resampling_error,
)
from blinov_reproduction.reference import fermi_pair_average

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"


class Profile12To15KmTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.csv = np.genfromtxt(DATA / "sfho188_digitized.csv",
                                delimiter=",", names=True)
        cls.region = ((cls.csv["r_km"] >= 12.0)
                      & (cls.csv["r_km"] <= 15.0))

    def test_profile_contains_all_required_columns(self):
        required = {
            "r_km", "T_MeV", "mu_mu_MeV", "mu_numu_MeV", "lapse",
            "T_Ferreira_MeV", "mu_mu_Ferreira_MeV",
        }
        self.assertTrue(required.issubset(set(self.csv.dtype.names)))
        self.assertEqual(len(self.csv), 501)

    def test_caputo_and_ferreira_temperature_profiles_agree(self):
        rel = np.abs(
            (self.csv["T_Ferreira_MeV"][self.region]
             - self.csv["T_MeV"][self.region])
            / self.csv["T_MeV"][self.region]
        )
        self.assertLess(float(np.max(rel)), 0.002)

    def test_caputo_muon_density_matches_independent_plotted_density(self):
        curve = read_curve(DATA / "n_mu_over_n0_caputo_vertices.csv")
        for radius in (12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0):
            row = self.csv[int(round(radius / 0.05))]
            density = density_and_susceptibility(
                float(row["T_MeV"]), float(row["mu_mu_MeV"])
            )["n_mu_fm3"]
            plotted = interp_curve(curve, radius) * 0.181
            self.assertLess(abs(density / plotted - 1.0), 0.02)

    def test_caputo_and_ferreira_muon_curves_are_not_silently_identified(self):
        rel = (
            self.csv["mu_mu_Ferreira_MeV"][self.region]
            / self.csv["mu_mu_MeV"][self.region] - 1.0
        )
        self.assertGreater(float(np.mean(rel)), 0.08)
        self.assertLess(float(np.mean(rel)), 0.20)

    def test_neutrino_muon_chemical_potential_floor_is_numerically_small(self):
        max_zeroing_change = 0.0
        max_hidden_floor_change = 0.0
        for radius in (12.0, 12.5, 13.0, 13.1, 13.15, 13.5, 14.0, 14.5, 15.0):
            row = self.csv[int(round(radius / 0.05))]
            T = float(row["T_MeV"])
            mu = float(row["mu_numu_MeV"])
            if radius <= 13.1:
                mu_alt = 0.0
                baseline_mu = mu
            else:
                mu_alt = 1.0
                baseline_mu = 0.0
            omega, mass = 12.0, 10.0
            v = np.sqrt(1.0 - (mass / omega) ** 2)
            base = (fermi_pair_average(baseline_mu, omega, T, v)
                    + fermi_pair_average(0.0, omega, T, v))
            alt = (fermi_pair_average(mu_alt, omega, T, v)
                   + fermi_pair_average(0.0, omega, T, v))
            change = abs(float(alt / base - 1.0))
            if radius <= 13.1:
                max_zeroing_change = max(max_zeroing_change, change)
            else:
                max_hidden_floor_change = max(max_hidden_floor_change, change)
        self.assertLess(max_zeroing_change, 0.004)
        self.assertLess(max_hidden_floor_change, 0.001)

    def test_lapse_is_monotonic_in_the_audited_region(self):
        values = self.csv["lapse"][self.region]
        self.assertTrue(np.all(np.diff(values) > 0.0))
        self.assertTrue(np.all((values > 0.0) & (values < 1.0)))

    def test_resampling_tracks_the_raw_pdf_polyline(self):
        specs = (
            ("T_caputo_vertices.csv", "T_MeV", 1.0),
            ("mu_mu_caputo_vertices.csv", "mu_mu_MeV", 1.0),
            ("minus_mu_numu_caputo_vertices.csv", "mu_numu_MeV", -1.0),
            ("T_ferreira_vertices.csv", "T_Ferreira_MeV", 1.0),
            ("mu_mu_ferreira_vertices.csv", "mu_mu_Ferreira_MeV", 1.0),
            ("lapse_ferreira_vertices.csv", "lapse", 1.0),
        )
        for filename, column, sign in specs:
            raw = read_curve(DATA / filename)
            result = resampling_error(
                np.column_stack((raw["r_km"], raw["value"])),
                self.csv["r_km"], self.csv[column], sign=sign
            )
            self.assertLess(result["max_relative_error"], 2e-8, filename)


if __name__ == "__main__":
    unittest.main(verbosity=2)
