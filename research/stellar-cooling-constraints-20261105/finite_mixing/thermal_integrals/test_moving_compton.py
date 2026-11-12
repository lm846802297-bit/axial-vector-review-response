import unittest

import numpy as np

import rates
from finite_mixing.thermal_integrals.moving_compton import (
    _muon_radial_rule,
    moving_compton_matrix_elements,
    moving_muon_compton_rates,
)


_METRIC = np.diag([1.0, -1.0, -1.0, -1.0])


def _boost_four_vector(vector, beta):
    beta = np.asarray(beta, dtype=float)
    beta2 = float(np.dot(beta, beta))
    if beta2 == 0.0:
        return np.asarray(vector, dtype=float).copy()
    gamma = 1.0 / np.sqrt(1.0 - beta2)
    bp = float(np.dot(beta, vector[1:]))
    energy = gamma * (vector[0] - bp)
    spatial = vector[1:] + (((gamma - 1.0) * bp / beta2) - gamma * vector[0]) * beta
    return np.concatenate(([energy], spatial))


def _medium_longitudinal_polarization(q, u, mass):
    q_dot_u = float(q @ _METRIC @ u)
    return (q_dot_u * q - mass * mass * u) / (
        mass * np.sqrt(q_dot_u * q_dot_u - mass * mass)
    )


def _boost_four_vector(vector, beta):
    beta = np.asarray(beta, dtype=float)
    beta2 = float(np.dot(beta, beta))
    if beta2 == 0.0:
        return np.asarray(vector, dtype=complex).copy()
    gamma = 1.0 / np.sqrt(1.0-beta2)
    bp = float(np.dot(beta, np.asarray(vector)[1:]))
    energy = gamma*(vector[0]-bp)
    spatial = np.asarray(vector)[1:] + (
        ((gamma-1.0)*bp/beta2)-gamma*vector[0]
    )*beta
    return np.concatenate(([energy], spatial))


def _minkowski_dot(a, b):
    return float(np.asarray(a) @ rates._METRIC @ np.asarray(b))


def _spin_summed_axial_matrix_element(p_in, k_gamma, p_out, q_vector,
                                       photon_polarizations,
                                       vector_polarization):
    """Covariant spin trace for one fixed outgoing-vector polarization."""
    mass = rates.M_MU
    den_s = 2.0*_minkowski_dot(p_in, k_gamma)
    den_u = -2.0*_minkowski_dot(p_in, q_vector)
    prop_s = (
        rates._slash(p_in+k_gamma)+mass*rates._I4
    )/den_s
    prop_u = (
        rates._slash(p_in-q_vector)+mass*rates._I4
    )/den_u
    spin_out = rates._slash(p_out)+mass*rates._I4
    spin_in = rates._slash(p_in)+mass*rates._I4
    gamma_x = rates._slash(vector_polarization) @ rates._G5
    gamma0 = rates._GAMMA[0]
    total = 0.0
    for eps_gamma in photon_polarizations:
        gamma_gamma = rates._slash(eps_gamma)
        amplitude = (
            gamma_x @ prop_s @ gamma_gamma
            + gamma_gamma @ prop_u @ gamma_x
        )
        conjugate = gamma0 @ rates._dagger(amplitude) @ gamma0
        trace = np.trace(
            spin_out @ amplitude @ spin_in @ conjugate
        )
        total += float(trace.real/2.0)
    return total


class MovingComptonMatrixElementTests(unittest.TestCase):
    def test_axial_TL_matrix_elements_are_lorentz_covariant(self):
        mass, omega = 20.0, 45.0
        p_magnitude, cos_mu, cos_gamma, phi_gamma = 80.0, 0.4, -0.3, 1.2
        q_energy, e_initial_muon, _ = moving_compton_matrix_elements(
            mass, omega, np.array([p_magnitude]), np.array([cos_mu]),
            np.array([cos_gamma]), np.array([phi_gamma]), 0.0, 1.0
        )
        q_energy = float(q_energy[0])
        k_magnitude = np.sqrt(omega*omega-mass*mass)
        p_vector = np.array([
            p_magnitude*np.sqrt(1.0-cos_mu*cos_mu), 0.0,
            p_magnitude*cos_mu
        ])
        n_gamma = np.array([
            np.sqrt(1.0-cos_gamma*cos_gamma)*np.cos(phi_gamma),
            np.sqrt(1.0-cos_gamma*cos_gamma)*np.sin(phi_gamma),
            cos_gamma
        ])
        p_out = np.r_[np.hypot(rates.M_MU,p_magnitude),p_vector]
        q_vector = np.array([omega,0.0,0.0,k_magnitude])
        k_gamma = np.r_[q_energy,q_energy*n_gamma]
        p_in = np.r_[float(e_initial_muon[0]),p_vector+q_vector[1:]-k_gamma[1:]]

        # Two real photon polarizations, built orthogonally to the incoming
        # photon momentum. The initial photon is summed, not averaged.
        eps1 = np.cross(np.array([0.0,0.0,1.0]),n_gamma)
        eps1 /= np.linalg.norm(eps1)
        eps2 = np.cross(n_gamma,eps1)
        photon_pols = (np.r_[0.0,eps1],np.r_[0.0,eps2])

        eps_l = np.array([k_magnitude/mass,0.0,0.0,omega/mass])
        eps_t1 = np.array([0.0,1.0,0.0,0.0])
        eps_t2 = np.array([0.0,0.0,1.0,0.0])
        vector_pols = (eps_l,eps_t1,eps_t2)
        original = np.array([
            _spin_summed_axial_matrix_element(
                p_in,k_gamma,p_out,q_vector,photon_pols,eps
            ) for eps in vector_pols
        ])

        beta = np.array([0.31,-0.17,0.22])
        boosted = [
            _boost_four_vector(v,beta)
            for v in (p_in,k_gamma,p_out,q_vector)
        ]
        p_in_b,k_gamma_b,p_out_b,q_vector_b = boosted
        photon_pols_b = tuple(_boost_four_vector(e,beta) for e in photon_pols)
        vector_pols_b = tuple(_boost_four_vector(e,beta) for e in vector_pols)
        transformed = np.array([
            _spin_summed_axial_matrix_element(
                p_in_b,k_gamma_b,p_out_b,q_vector_b,
                photon_pols_b,eps
            ) for eps in vector_pols_b
        ])
        np.testing.assert_allclose(transformed,original,rtol=3e-11,atol=3e-10)
        self.assertGreater(original[0],0.0)
        self.assertGreater(original[1]+original[2],0.0)

    def test_fixed_energy_argument_is_q_dot_u_after_a_frame_boost(self):
        mass, omega, temperature, mu_mu = 10.0, 25.0, 20.0, 45.0
        k = np.sqrt(omega*omega-mass*mass)
        q = np.array([omega,0.0,0.0,k])
        u = np.array([1.0,0.0,0.0,0.0])
        beta = np.array([0.31,-0.17,0.22])
        q_b = _boost_four_vector(q,beta)
        u_b = _boost_four_vector(u,beta)
        omega_medium = _minkowski_dot(q_b,u_b)
        self.assertAlmostEqual(omega_medium,omega,delta=2e-13)
        self.assertGreater(abs(float(q_b[0])-omega),1e-3)

        rest = moving_muon_compton_rates(
            mass,omega,temperature,mu_mu,0.0,-1.0,orders=(4,4,4,4)
        )
        boosted_frame_reconstructed = moving_muon_compton_rates(
            mass,omega_medium,temperature,mu_mu,0.0,-1.0,orders=(4,4,4,4)
        )
        np.testing.assert_allclose(
            boosted_frame_reconstructed["production"],rest["production"],
            rtol=2e-13,atol=1e-300
        )
        np.testing.assert_allclose(
            boosted_frame_reconstructed["absorption"],rest["absorption"],
            rtol=2e-13,atol=1e-300
        )

    def test_medium_frame_projectors_are_boost_covariant(self):
        mass, omega = 0.7, 3.2
        momentum = np.sqrt(omega * omega - mass * mass)
        q = np.array([omega, 0.0, 0.0, momentum])
        u = np.array([1.0, 0.0, 0.0, 0.0])
        eps_l = _medium_longitudinal_polarization(q, u, mass)
        eps_x = np.array([0.0, 1.0, 0.0, 0.0])
        eps_y = np.array([0.0, 0.0, 1.0, 0.0])

        beta = np.array([0.31, -0.17, 0.22])
        q_boosted = _boost_four_vector(q, beta)
        u_boosted = _boost_four_vector(u, beta)
        eps_l_boosted = _boost_four_vector(eps_l, beta)
        eps_x_boosted = _boost_four_vector(eps_x, beta)
        eps_y_boosted = _boost_four_vector(eps_y, beta)
        eps_l_covariant = _medium_longitudinal_polarization(
            q_boosted, u_boosted, mass
        )

        np.testing.assert_allclose(
            eps_l_covariant, eps_l_boosted, rtol=2e-13, atol=2e-13
        )
        total = -_METRIC + np.outer(q_boosted, q_boosted) / (mass * mass)
        p_t_covariant = total - np.outer(eps_l_covariant, eps_l_covariant)
        p_t_boosted = (
            np.outer(eps_x_boosted, eps_x_boosted)
            + np.outer(eps_y_boosted, eps_y_boosted)
        )
        np.testing.assert_allclose(
            p_t_covariant, p_t_boosted, rtol=2e-12, atol=2e-12
        )
        self.assertAlmostEqual(
            float(q_boosted @ _METRIC @ eps_l_covariant), 0.0, delta=2e-13
        )
        self.assertAlmostEqual(
            float(eps_l_covariant @ _METRIC @ eps_l_covariant),
            -1.0, delta=2e-13
        )
        self.assertLess(
            float(np.max(np.abs(q_boosted @ _METRIC @ p_t_covariant))),
            2e-12,
        )
        self.assertLess(
            float(np.max(np.abs(u_boosted @ _METRIC @ p_t_covariant))),
            2e-12,
        )

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

    def test_unpolarized_normalization_matches_paper_eq_5_12(self):
        out = self._run(0.15, -0.85, mu_mu=45.0)
        normalization = out["unpolarized_normalization"]
        self.assertEqual(normalization["initial_photon_polarization_average"], 2)
        self.assertEqual(normalization["initial_vector_polarization_average"], 3)
        self.assertAlmostEqual(
            normalization["Gamma_abs_over_Gamma_prod"],
            normalization["Eq_5_12_expected_ratio"],
            delta=3e-10,
        )
        self.assertLess(normalization["Eq_5_12_relative_residual"], 3e-10)

    def test_pure_axial_mode_resolved_rates_are_positive_and_balance(self):
        out = self._run(0.0, -1.0, mu_mu=45.0)
        expected = np.exp(-25.0/20.0)*out["Gamma_abs_by_mode"]
        np.testing.assert_allclose(out["Gamma_prod_by_mode"], expected,
                                   rtol=3e-10, atol=1e-300)
        self.assertTrue(np.all(out["Gamma_abs_by_mode"] > 0.0))
        self.assertTrue(np.all(out["Gamma_prod_by_mode"] > 0.0))
        self.assertGreater(float(out["Gamma_abs_by_mode"][0]), 0.0)
        self.assertGreater(float(np.sum(out["Gamma_abs_by_mode"][1:])), 0.0)
        self.assertLess(out["max_detailed_balance_relative_residual"], 3e-10)

    def test_cold_dilute_inverse_rate_uses_log_space_without_overflow(self):
        temperature = 1.0e-3
        mu_mu = rates.M_MU-5.0*temperature
        out = moving_muon_compton_rates(
            10.0,15.0,temperature,mu_mu,0.0,-1.0,orders=(4,4,4,4)
        )
        normalization = out["unpolarized_normalization"]
        self.assertGreater(normalization["Eq_5_12_expected_log_ratio"],700.0)
        self.assertIsNone(normalization["Eq_5_12_expected_ratio"])
        self.assertTrue(normalization["Eq_5_12_underflow_limited"])
        self.assertIsNone(normalization["Eq_5_12_relative_residual"])
        self.assertTrue(np.isfinite(out["max_detailed_balance_relative_residual"]))

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
