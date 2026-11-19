import unittest

import numpy as np

from croon_c0_luminosity import ALPHA_EM, M_MU, T_NU_MEV
from lai2024_plateau_equation_audit import (
    lai_neutrino_inverse_mfp_coefficient,
    lai_semicompton_inverse_mfp_coefficient,
    lai_semicompton_production_coefficient,
    lai_semicompton_to_neutrino_opacity_ratio,
    lai_semicompton_to_neutrino_production_ratio,
)
from run_lai2024_surface_semicompton_check import (
    DEFAULT_PROFILE,
    run_surface_semicompton_check,
)


class Lai2024SurfaceSemiComptonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_surface_semicompton_check(
            profile_path=DEFAULT_PROFILE,
            susceptibility_order=128,
        )

    def test_lai_inverse_decay_and_semicompton_coefficients_match_printed_equations(self):
        omega = np.array([6.0, 9.0, 12.0, 15.0])
        mass = 2.0e-6
        chi = 1.1351833714357841e-10
        temperature = 3.0
        velocity = np.sqrt(1.0 - (mass / omega) ** 2)
        expected_nu = mass**2 / (12.0 * np.pi * omega * velocity)
        expected_sc = (
            4.0 * ALPHA_EM / (9.0 * M_MU**2)
            * chi * (1.0 + 1.0 / np.expm1(omega / temperature))
        )
        np.testing.assert_allclose(
            lai_neutrino_inverse_mfp_coefficient(omega, mass),
            expected_nu,
            rtol=2e-15,
        )
        np.testing.assert_allclose(
            lai_semicompton_inverse_mfp_coefficient(omega, temperature, mass, chi),
            expected_sc,
            rtol=2e-15,
        )

    def test_semicompton_opacity_to_production_ratio_has_exact_factor_two(self):
        omega = np.array([6.0, 9.0, 12.0, 15.0])
        ratio_opacity = lai_semicompton_to_neutrino_opacity_ratio(
            omega, 3.0, 2.0e-6, 1.1351833714357841e-10
        )
        ratio_production = lai_semicompton_to_neutrino_production_ratio(
            omega, 3.0, 2.0e-6, 1.1351833714357841e-10
        )
        np.testing.assert_allclose(ratio_opacity, 2.0 * ratio_production, rtol=3e-15)

    def test_public_profile_surface_susceptibility_and_digitized_edge_are_pinned(self):
        profile = self.result["profile"]
        self.assertEqual(
            profile["sha256"],
            "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c",
        )
        self.assertEqual(profile["rows"], 1687)
        self.assertAlmostEqual(profile["R_nu_km"], 25.1511682816, places=8)
        self.assertAlmostEqual(
            profile["chi_mu_Rnu_extrapolated_MeV3"],
            3.82364561e-13,
            delta=5e-16,
        )
        edge = profile["last_nonzero_digitized_sample"]
        self.assertAlmostEqual(edge["r_km"], 22.1918936570, places=8)
        self.assertAlmostEqual(edge["chi_mu_MeV3"], 1.13518337e-10, delta=2e-16)

    def test_lai_two_ev_surface_semicompton_opacity_is_subpercent_even_at_edge_envelope(self):
        rows = self.result["summary"]
        edge_2ev = next(
            x for x in rows
            if x["mass_label"] == "2 eV"
            and x["susceptibility_case"] == "conditional_last_nonzero_edge_envelope"
        )
        surface_2ev = next(
            x for x in rows
            if x["mass_label"] == "2 eV"
            and x["susceptibility_case"] == "public_profile_Rnu_extrapolation"
        )
        self.assertLess(
            edge_2ev["max_kappa_sC_over_kappa_nu_over_omega_over_T_2_to_8"],
            8.0e-3,
        )
        self.assertLess(
            surface_2ev["max_kappa_sC_over_kappa_nu_over_omega_over_T_2_to_8"],
            3.0e-5,
        )

    def test_point_one_ev_outer_edge_envelope_can_make_semicompton_opacity_competitive(self):
        rows = self.result["summary"]
        edge_01ev = next(
            x for x in rows
            if x["mass_label"] == "0.1 eV"
            and x["susceptibility_case"] == "conditional_last_nonzero_edge_envelope"
        )
        surface_01ev = next(
            x for x in rows
            if x["mass_label"] == "0.1 eV"
            and x["susceptibility_case"] == "public_profile_Rnu_extrapolation"
        )
        self.assertGreater(
            edge_01ev["max_kappa_sC_over_kappa_nu_over_omega_over_T_2_to_8"],
            2.9,
        )
        self.assertLess(
            surface_01ev["max_kappa_sC_over_kappa_nu_over_omega_over_T_2_to_8"],
            1.1e-2,
        )

    def test_semicompton_source_coefficient_matches_lai_eq11(self):
        omega = np.array([6.0, 9.0, 12.0])
        mass = 2.0e-6
        chi = 1.1351833714357841e-10
        temp = 3.0
        velocity = np.sqrt(1.0 - (mass / omega) ** 2)
        expected = (
            2.0 * ALPHA_EM / (3.0 * M_MU**2)
            * chi * velocity / np.expm1(omega / temp)
        )
        np.testing.assert_allclose(
            lai_semicompton_production_coefficient(omega, temp, mass, chi),
            expected,
            rtol=2e-15,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
