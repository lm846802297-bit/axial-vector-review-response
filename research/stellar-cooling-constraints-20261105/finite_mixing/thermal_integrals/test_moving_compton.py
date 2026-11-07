import unittest

import numpy as np

import rates
from finite_mixing.thermal_integrals.moving_compton import (
    _muon_radial_rule,
    moving_compton_matrix_elements,
    moving_muon_compton_rates,
)


class MovingComptonMatrixElementTests(unittest.TestCase):
    def test_stationary_muon_endpoint_matches_existing_vector_and_axial_kernels(self):
        mass, omega = 10.0, 30.0
        cosines = np.array([-0.7, 0.1, 0.8])
        zeros = np.zeros_like(cosines)

        _, _, vector = moving_compton_matrix_elements(
            mass, omega, zeros, zeros, cosines, zeros, 1.0, 0.0
        )
        _, vector_ref = rates.compton_matrix_elements(
            mass, [omega], cosines, current="vector"
        )
        np.testing.assert_allclose(vector, vector_ref[0], rtol=2e-12, atol=2e-12)

        _, _, axial = moving_compton_matrix_elements(
            mass, omega, zeros, zeros, cosines, zeros, 0.0, 1.0
        )
        _, axial_ref = rates.compton_matrix_elements(
            mass, [omega], cosines, current="axial"
        )
        np.testing.assert_allclose(axial, axial_ref[0], rtol=2e-12, atol=2e-12)

    def test_stationary_target_phase_space_weight_matches_existing_kernel(self):
        mass, omega, order = 10.0, 30.0, 32
        cosines, weights = rates.quadrature(order)
        zeros = np.zeros_like(cosines)
        q, _, msq = moving_compton_matrix_elements(
            mass, omega, zeros, zeros, cosines, zeros, 1.0, 0.0
        )
        k = np.sqrt(omega*omega-mass*mass)
        denominator = rates.M_MU+omega-k*cosines
        differential_vsigma = (
            q/(64.0*np.pi**2*rates.M_MU*omega*denominator)
        )[:, None]*msq
        integrated = differential_vsigma*(2.0*np.pi*weights)[:, None]
        _, reference = rates.compton_kernels(
            mass, [omega], order=order, current="vector"
        )
        np.testing.assert_allclose(integrated, reference[0],
                                   rtol=2e-12, atol=2e-12)

    def test_photon_ward_identity_for_both_charge_species(self):
        args = (20.0, 45.0, np.array([25.0, 80.0]),
                np.array([0.2, -0.4]), np.array([-0.3, 0.7]),
                np.array([0.5, 2.1]), 0.2, -0.8)
        for charge in ("mu_minus", "mu_plus"):
            _, _, ward = moving_compton_matrix_elements(
                *args, charge=charge, photon_ward=True
            )
            self.assertLess(float(np.max(np.abs(ward))), 2e-9)

    def test_vector_mediator_ward_identity(self):
        _, _, ward = moving_compton_matrix_elements(
            20.0, 45.0, np.array([25.0, 80.0]),
            np.array([0.2, -0.4]), np.array([-0.3, 0.7]),
            np.array([0.5, 2.1]), 1.0, 0.0,
            vector_mediator_ward=True,
        )
        self.assertLess(float(np.max(np.abs(ward[:, 0]))), 2e-9)

    def test_charge_conjugation_reverses_only_relative_axial_sign(self):
        args = (20.0, 45.0, np.array([25.0, 80.0]),
                np.array([0.2, -0.4]), np.array([-0.3, 0.7]),
                np.array([0.5, 2.1]), 0.2, -0.8)
        _, _, plus = moving_compton_matrix_elements(*args, charge="mu_plus")
        flipped = (args[:-1] + (-args[-1],))
        _, _, minus_with_flipped_axial = moving_compton_matrix_elements(
            *flipped, charge="mu_minus"
        )
        np.testing.assert_allclose(plus, minus_with_flipped_axial,
                                   rtol=2e-13, atol=2e-13)

    def test_negative_chemical_potential_does_not_create_fake_fermi_surface(self):
        temperature = 20.0
        omega = 25.0
        p_negative, _ = _muon_radial_rule(temperature, -300.0, omega, 16)
        p_zero, _ = _muon_radial_rule(temperature, 0.0, omega, 16)
        p_positive, _ = _muon_radial_rule(temperature, +300.0, omega, 16)
        np.testing.assert_array_equal(p_negative, p_zero)
        self.assertGreater(float(np.max(p_positive)), float(np.max(p_negative)))


class MovingComptonThermalRateTests(unittest.TestCase):
    def _run(self, g_vector, g_axial, mu_mu=0.0):
        return moving_muon_compton_rates(
            mass=10.0, omega=25.0, temperature=20.0, mu_mu=mu_mu,
            g_vector=g_vector, g_axial=g_axial,
            radial_order=8, angular_order=4, azimuth_order=4,
            chunk_size=512,
        )

    def test_production_and_absorption_are_integrated_independently_and_balance(self):
        out = self._run(0.15, -0.85, mu_mu=45.0)
        expected = np.exp(-25.0/20.0)*out["Gamma_abs_by_mode"]
        np.testing.assert_allclose(out["Gamma_prod_by_mode"], expected,
                                   rtol=3e-10, atol=1e-300)
        self.assertLess(out["max_detailed_balance_relative_residual"], 3e-10)
        self.assertTrue(np.all(out["Gamma_prod_by_mode"] > 0.0))
        self.assertTrue(np.all(out["Gamma_abs_by_mode"] > 0.0))
        self.assertTrue(np.all(
            out["charge_contributions"]["mu_minus"]["Gamma_abs_by_mode"] > 0.0
        ))
        self.assertTrue(np.all(
            out["charge_contributions"]["mu_plus"]["Gamma_abs_by_mode"] > 0.0
        ))

    def test_charge_summed_interference_cancels_at_zero_muon_chemical_potential(self):
        gv, ga = 0.2, -0.8
        mixed = self._run(gv, ga, mu_mu=0.0)["Gamma_abs_by_mode"]
        vector = self._run(1.0, 0.0, mu_mu=0.0)["Gamma_abs_by_mode"]
        axial = self._run(0.0, 1.0, mu_mu=0.0)["Gamma_abs_by_mode"]
        incoherent = gv*gv*vector + ga*ga*axial
        np.testing.assert_allclose(mixed, incoherent, rtol=3e-10, atol=1e-300)

    def test_charge_asymmetric_medium_retains_interference(self):
        gv, ga = 0.2, -0.8
        mixed = self._run(gv, ga, mu_mu=45.0)["Gamma_abs_by_mode"]
        vector = self._run(1.0, 0.0, mu_mu=45.0)["Gamma_abs_by_mode"]
        axial = self._run(0.0, 1.0, mu_mu=45.0)["Gamma_abs_by_mode"]
        incoherent = gv*gv*vector + ga*ga*axial
        self.assertGreater(float(np.max(np.abs(mixed-incoherent))), 1e-12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
