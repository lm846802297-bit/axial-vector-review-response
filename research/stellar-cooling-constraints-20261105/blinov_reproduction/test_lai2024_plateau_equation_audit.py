import unittest

import numpy as np

from lai2024_plateau_equation_audit import (
    croon_generic_neutrino_coalescence_coefficient,
    croon_lmutau_neutrino_coalescence_coefficient,
    croon_semicompton_absorption_length_coefficient,
    full_angle_surface_geometry_factor,
    geometry_factor_ratio_two_ray_to_full_angle,
    lai_over_croon_lmutau_neutrino_ratio,
    lai_over_croon_semicompton_opacity_ratio,
    lai_semicompton_inverse_mfp_coefficient,
    lai_two_flavour_neutrino_coalescence_coefficient,
    plateau_luminosity_at_coupling,
    plateau_luminosity_natural_units,
    two_ray_surface_geometry_factor,
)


class Lai2024PlateauEquationAuditTests(unittest.TestCase):
    def test_lai_semicompton_absorption_ratio_is_two_thirds_over_velocity(self):
        omega = np.array([12.0, 20.0, 50.0, 100.0])
        mass = 10.0
        ratio = lai_over_croon_semicompton_opacity_ratio(omega, mass)
        velocity = np.sqrt(1.0 - (mass / omega) ** 2)
        np.testing.assert_allclose(ratio, 2.0 / (3.0 * velocity), rtol=2e-15)
        self.assertAlmostEqual(
            lai_semicompton_inverse_mfp_coefficient(omega, 5.0, mass, 2.0)[0]
            / croon_semicompton_absorption_length_coefficient(omega, 5.0, mass, 2.0)[0],
            ratio[0],
            places=14,
        )

    def test_two_neutrino_flavour_and_bose_convention_are_explicit(self):
        omega = np.array([3.0, 10.0, 30.0])
        mass = 2.0
        temp = 3.0
        generic = croon_generic_neutrino_coalescence_coefficient(omega, mass, temp)
        lmutau = croon_lmutau_neutrino_coalescence_coefficient(omega, mass, temp)
        lai = lai_two_flavour_neutrino_coalescence_coefficient(omega, mass, temp)
        np.testing.assert_allclose(lmutau, 2.0 * generic, rtol=0.0, atol=0.0)
        expected_ratio = 1.5 * (1.0 - np.exp(-omega / temp))
        np.testing.assert_allclose(lai / lmutau, expected_ratio, rtol=2e-15)
        np.testing.assert_allclose(
            lai_over_croon_lmutau_neutrino_ratio(omega, mass, temp),
            expected_ratio,
            rtol=2e-15,
        )

    def test_lai_neutrino_rate_matches_B7_in_MB_two_flavour_limit(self):
        omega = np.array([5.0, 15.0, 40.0])
        mass = 2.0
        temperature = 8.0
        b7_mb = mass**2/(8.0*np.pi*omega) * (
            2.0*np.exp(-omega/temperature)
        )
        lai = lai_two_flavour_neutrino_coalescence_coefficient(
            omega, mass, temperature
        )
        np.testing.assert_allclose(lai, b7_mb, rtol=2e-15)

    def test_plateau_formula_is_independent_of_coupling(self):
        omega = np.linspace(1.0, 50.0, 200)
        emissivity = np.exp(-omega / 10.0) * omega**3
        opacity = 0.2 + 0.03 * omega
        rnu = 1.2e19
        reference = plateau_luminosity_natural_units(rnu, omega, emissivity, opacity)
        for coupling in (1e-9, 1e-6, 1e-3, 0.1):
            value = plateau_luminosity_at_coupling(
                coupling, rnu, omega, emissivity, opacity
            )
            self.assertAlmostEqual(value / reference, 1.0, delta=2e-15)

    def test_full_angle_and_two_ray_geometry_differ_by_factor_two(self):
        self.assertAlmostEqual(full_angle_surface_geometry_factor(), 0.25, places=15)
        self.assertAlmostEqual(two_ray_surface_geometry_factor(), 0.5, places=15)
        self.assertAlmostEqual(geometry_factor_ratio_two_ray_to_full_angle(), 2.0, places=15)

    def test_lai_neutrino_only_plateau_reaches_massless_limit(self):
        from lai2024_plateau_equation_audit import lai_neutrino_only_plateau

        result = lai_neutrino_only_plateau(
            mass_MeV=2.0e-6,
            temperature_MeV=3.0,
            neutrinosphere_radius_km=25.151168281622343,
            energy_order=256,
        )
        self.assertAlmostEqual(result["relative_to_massless_limit"], 1.0, delta=2e-8)
        self.assertAlmostEqual(
            result["L_nu_only_plateau_erg_s"], 9.1762591e51, delta=2e-5*9.1762591e51
        )
        self.assertIn("omits semi-Compton", result["scope"])

    def test_lai_neutrino_only_plateau_is_mass_suppressed(self):
        from lai2024_plateau_equation_audit import lai_neutrino_only_plateau

        light = lai_neutrino_only_plateau(2.0e-6, 3.0, 25.151168281622343)
        heavy = lai_neutrino_only_plateau(10.0, 3.0, 25.151168281622343)
        self.assertLess(heavy["L_nu_only_plateau_erg_s"], light["L_nu_only_plateau_erg_s"])

    def test_plateau_integral_rejects_nonphysical_opacity_and_grid(self):
        omega = np.array([1.0, 2.0, 3.0])
        emissivity = np.ones(3)
        with self.assertRaises(ValueError):
            plateau_luminosity_natural_units(1.0, omega, emissivity, np.array([1.0, 0.0, 1.0]))
        with self.assertRaises(ValueError):
            plateau_luminosity_natural_units(1.0, omega[::-1], emissivity, np.ones(3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
