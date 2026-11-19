import unittest
from pathlib import Path

import numpy as np

try:
    from .croon_blinov_neutrino_emissivity import (
        DEFAULT_PROFILE,
        local_rate_spectra,
        load_profile,
        free_streaming_volume_integral,
        MEV_INV_PER_KM,
        MEV2_TO_ERG_PER_SECOND,
    )
    from .reference import fermi_pair_average as reference_pair_average
except ImportError:
    from croon_blinov_neutrino_emissivity import (
        DEFAULT_PROFILE,
        local_rate_spectra,
        load_profile,
        free_streaming_volume_integral,
        MEV_INV_PER_KM,
        MEV2_TO_ERG_PER_SECOND,
    )
    from reference import fermi_pair_average as reference_pair_average


class CroonBlinovNeutrinoEmissivityTests(unittest.TestCase):
    def test_profile_provenance_and_full_radial_coverage(self):
        rows = load_profile(Path(DEFAULT_PROFILE))
        self.assertEqual(len(rows), 1687)
        self.assertAlmostEqual(float(rows["r_km"][0]), 0.0, places=12)
        self.assertAlmostEqual(float(rows["r_km"][-1]), 25.0, places=12)
        self.assertIn("mu_numu_MeV", rows.dtype.names)

    def test_zero_degeneracy_MB_limit_gives_factor_three(self):
        result = local_rate_spectra(
            mass=99.0, temperature=2.0, mu_numu=0.0, mu_nutau=0.0,
            energy_order=48, angular_order=96
        )
        self.assertAlmostEqual(result["Q_B7_over_Q_Croon"], 3.0, delta=1e-8)

    def test_FD_chemical_potential_suppresses_low_energy_rate_vs_Croon(self):
        result = local_rate_spectra(
            mass=10.0, temperature=19.265221107965,
            mu_numu=-58.6137567217484, mu_nutau=0.0,
            energy_order=64, angular_order=192
        )
        self.assertGreater(result["Q_B7_two_flavour_per_g2_MeV5"], 0.0)
        self.assertGreater(result["Q_Croon_Eq46_per_g2_MeV5"], 0.0)
        self.assertLess(result["Q_B7_over_Q_Croon"], 3.0)

    def test_direct_B6_angular_average_matches_B9_reference(self):
        mass, temperature, mu_nu, omega = 10.0, 23.881959149249, -2.59165549916519, 50.0
        velocity = np.sqrt(1.0-(mass/omega)**2)
        reference = float(reference_pair_average(mu_nu, omega, temperature, velocity))
        # Extract the B.7 angular average from its per-flavour rate.
        result = local_rate_spectra(
            mass, temperature, mu_nu, 0.0, energy_order=64, angular_order=256
        )
        idx = int(np.argmin(np.abs(np.asarray(result["omega_MeV"])-omega)))
        sampled_omega = result["omega_MeV"][idx]
        sampled_v = np.sqrt(1.0-(mass/sampled_omega)**2)
        sampled_ref = float(reference_pair_average(
            mu_nu, sampled_omega, temperature, sampled_v
        ))
        extracted = (
            result["B7_two_flavour_rate_per_g2_MeV"][idx]
            * 8.0*np.pi*sampled_omega/(mass*mass)
            - float(result["I_nutau"][idx])
        )
        self.assertAlmostEqual(extracted/sampled_ref, 1.0, delta=3e-12)

    def test_piecewise_linear_spherical_volume_integral_and_units(self):
        result = free_streaming_volume_integral(
            r_km=np.array([0.0, 1.0]),
            temperature_MeV=np.array([5.0, 4.0]),
            q_b7_MeV5=np.array([2.0, 2.0]),
            q_croon_MeV5=np.array([1.0, 1.0]),
            neutrinosphere_temperature_MeV=3.0,
        )
        self.assertAlmostEqual(result["neutrinosphere_radius_km"], 2.0, places=13)
        self.assertAlmostEqual(
            result["Q_B7_over_Q_Croon_free_streaming_luminosity"], 2.0, places=13
        )
        expected = (
            4.0*np.pi*2.0*(2.0**3)/3.0
            * MEV_INV_PER_KM**3 * MEV2_TO_ERG_PER_SECOND
        )
        self.assertAlmostEqual(
            result["Q_B7_free_streaming_luminosity_per_g2_erg_s"]/expected,
            1.0, delta=2e-13
        )

    def test_selected_energy_angular_quadrature_converges(self):
        coarse = local_rate_spectra(
            10.0, 23.881959149249, -2.59165549916519, 0.0, 64, 128
        )
        fine = local_rate_spectra(
            10.0, 23.881959149249, -2.59165549916519, 0.0, 96, 256
        )
        self.assertLess(
            abs(fine["Q_B7_two_flavour_per_g2_MeV5"]
                / coarse["Q_B7_two_flavour_per_g2_MeV5"] - 1.0),
            1e-3
        )
        self.assertLess(
            abs(fine["Q_Croon_Eq46_per_g2_MeV5"]
                / coarse["Q_Croon_Eq46_per_g2_MeV5"] - 1.0),
            1e-3
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
