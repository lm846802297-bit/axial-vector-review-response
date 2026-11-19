import unittest
from pathlib import Path

import numpy as np

try:
    from .croon_c0_luminosity import (
        DEFAULT_PROFILE,
        MEV_INV_PER_KM,
        build_croon_optical_depth,
        outer_vacuum_neutrino_tau_per_g2,
        run_c0_luminosity,
        vectorized_muon_susceptibility,
        muon_density_and_susceptibility,
    )
except ImportError:
    from croon_c0_luminosity import (
        DEFAULT_PROFILE,
        MEV_INV_PER_KM,
        build_croon_optical_depth,
        outer_vacuum_neutrino_tau_per_g2,
        run_c0_luminosity,
        vectorized_muon_susceptibility,
        muon_density_and_susceptibility,
    )


class CroonC0LuminosityTests(unittest.TestCase):
    def test_vectorized_nmu_fdeg_matches_bollig_single_muon_component(self):
        temperatures = np.array([19.265221107965, 39.2496793414134,
                                  23.881959149249, 3.03377069226813])
        chemical_potentials = np.array([46.6743284468278, 87.638,
                                        90.2165853124713, 0.0])
        vectorized = vectorized_muon_susceptibility(
            temperatures, chemical_potentials, order=128
        )
        reference = np.array([
            muon_density_and_susceptibility(float(t), float(mu), order=128)[
                "n_mu_Fdeg_total_MeV3"
            ]
            for t, mu in zip(temperatures, chemical_potentials)
        ])
        np.testing.assert_allclose(vectorized, reference, rtol=2e-13, atol=0.0)

    def test_outer_vacuum_tail_matches_croon_profile_audit(self):
        omega = np.array([10.0, 12.0, 20.0, 50.0])
        tau = outer_vacuum_neutrino_tau_per_g2(
            10.0, omega, 25.151168281622343, 100.0
        )
        expected = np.array([
            1.00616090e17, 8.38467418e16,
            5.03080451e16, 2.01232180e16
        ])
        np.testing.assert_allclose(tau, expected, rtol=2e-8, atol=0.0)

    def test_croon_absorption_integral_has_vacuum_tail_at_Rnu(self):
        mass = 10.0
        omega = np.array([10.0, 12.0, 50.0])
        r_nu = 25.151168281622343
        tau = build_croon_optical_depth(
            mass_MeV=mass,
            r_km=np.array([0.0, r_nu]),
            temperature_MeV=np.array([3.0, 3.0]),
            chi_mu_MeV3=np.array([0.0, 0.0]),
            omega_grid_MeV=omega,
            r_far_km=100.0,
            outer_temperature_envelope_MeV=0.0,
        )
        expected_outer = outer_vacuum_neutrino_tau_per_g2(
            mass, omega, r_nu, 100.0
        )
        np.testing.assert_allclose(tau[:, -1], expected_outer, rtol=2e-14)
        beta = omega / 3.0
        fB = 1.0 / np.expm1(beta)
        kappa_inside = mass**2/(12.0*np.pi*omega)*(1.0+fB)
        expected_center = expected_outer + kappa_inside*r_nu*MEV_INV_PER_KM
        np.testing.assert_allclose(tau[:, 0], expected_center, rtol=2e-14)

    def test_full_c0_adapter_reproduces_free_neutrino_channel_and_attenuates(self):
        result = run_c0_luminosity(
            Path(DEFAULT_PROFILE),
            mass_MeV=10.0,
            couplings=np.array([1e-11, 1e-9]),
            energy_order=32,
            tau_grid_points=81,
            susceptibility_order=64,
        )
        free = result["free_streaming_channel_luminosity_per_g2_erg_s"]
        self.assertAlmostEqual(result["R_nu_km"], 25.1511683, places=5)
        self.assertAlmostEqual(
            free["nu_coalescence"]/3.05793824e70, 1.0, delta=2e-3
        )
        low, high = result["coupling_curve"]
        for record in (low, high):
            self.assertGreater(record["vacuum_tail"]["L_total_erg_s"], 0.0)
            self.assertGreater(record["T3_outer_envelope"]["L_total_erg_s"], 0.0)
            self.assertLessEqual(
                record["T3_outer_envelope"]["L_total_erg_s"],
                record["vacuum_tail"]["L_total_erg_s"]*1.001
            )
        self.assertLess(
            high["vacuum_tail"]["L_total_erg_s"]/high["g_X"]**2,
            free["total"]*1.01
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
