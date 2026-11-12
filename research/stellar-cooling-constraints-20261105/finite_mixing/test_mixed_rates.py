import math
import unittest

import numpy as np

import rates
from finite_mixing.model import muon_couplings


class MixedComptonKernelTests(unittest.TestCase):
    def setUp(self):
        self.mass = 10.0
        self.energies = np.array([11.0, 20.0, 100.0])
        self.cosines = np.array([-0.7, 0.1, 0.8])

    def test_pure_vector_endpoint_matches_existing_kernel(self):
        _, mixed = rates.compton_mixed_matrix_elements(
            self.mass, self.energies, self.cosines, 1.0, 0.0
        )
        _, vector = rates.compton_matrix_elements(
            self.mass, self.energies, self.cosines, current="vector"
        )
        np.testing.assert_allclose(mixed, vector, rtol=2e-13, atol=1e-13)

    def test_pure_axial_endpoint_matches_existing_kernel(self):
        _, mixed = rates.compton_mixed_matrix_elements(
            self.mass, self.energies, self.cosines, 0.0, -1.0
        )
        _, axial = rates.compton_matrix_elements(
            self.mass, self.energies, self.cosines, current="axial"
        )
        np.testing.assert_allclose(mixed, axial, rtol=2e-13, atol=1e-13)

    def test_uv_benchmark_keeps_amplitude_level_interference(self):
        c = muon_couplings(1.0, 1.0e-2)
        _, mixed = rates.compton_mixed_matrix_elements(
            self.mass, self.energies, self.cosines,
            c.g_vector, c.g_axial
        )
        _, vector = rates.compton_matrix_elements(
            self.mass, self.energies, self.cosines, current="vector"
        )
        _, axial = rates.compton_matrix_elements(
            self.mass, self.energies, self.cosines, current="axial"
        )
        incoherent = c.g_vector**2*vector+c.code_axial_minus_gamma5_coefficient**2*axial
        self.assertGreater(float(np.max(np.abs(mixed-incoherent))), 1e-8)

    def test_mixed_photon_ward_identity(self):
        c = muon_couplings(1.0, 1.0e-2)
        _, ward = rates.compton_mixed_matrix_elements(
            self.mass, self.energies, self.cosines,
            c.g_vector, c.g_axial, photon_ward=True
        )
        self.assertLess(float(np.max(np.abs(ward))), 1e-8)

    def test_integrated_kernels_recover_both_endpoints(self):
        _, vector = rates.compton_mixed_kernels(
            self.mass, self.energies, 1.0, 0.0, order=24
        )
        _, vector_ref = rates.compton_kernels(
            self.mass, self.energies, order=24, current="vector"
        )
        _, axial = rates.compton_mixed_kernels(
            self.mass, self.energies, 0.0, -1.0, order=24
        )
        _, axial_ref = rates.compton_kernels(
            self.mass, self.energies, order=24, current="axial"
        )
        np.testing.assert_allclose(vector, vector_ref, rtol=2e-13, atol=1e-13)
        np.testing.assert_allclose(axial, axial_ref, rtol=2e-13, atol=1e-13)


class MixedDimuonKernelTests(unittest.TestCase):
    def setUp(self):
        self.mass = 300.0
        self.energy = np.array([310.0, 400.0])
        self.temperature = np.array([30.0, 40.0])
        self.mu_mu = np.array([80.0, 90.0])

    def test_pure_vector_endpoint_matches_existing_rates(self):
        prod, absorp = rates.charged_muon_decay_rates_mixed(
            self.mass, self.energy, self.temperature, self.mu_mu, 1.0, 0.0
        )
        ref_prod, ref_absorp = rates.charged_muon_decay_rates(
            self.mass, self.energy, self.temperature, self.mu_mu, current="vector"
        )
        np.testing.assert_allclose(prod, ref_prod, rtol=2e-12, atol=1e-14)
        np.testing.assert_allclose(absorp, ref_absorp, rtol=2e-12, atol=1e-14)

    def test_pure_axial_endpoint_matches_existing_rates(self):
        prod, absorp = rates.charged_muon_decay_rates_mixed(
            self.mass, self.energy, self.temperature, self.mu_mu, 0.0, -1.0
        )
        ref_prod, ref_absorp = rates.charged_muon_decay_rates(
            self.mass, self.energy, self.temperature, self.mu_mu, current="axial"
        )
        np.testing.assert_allclose(prod, ref_prod, rtol=2e-12, atol=1e-14)
        np.testing.assert_allclose(absorp, ref_absorp, rtol=2e-12, atol=1e-14)

    def test_mode_by_mode_detailed_balance(self):
        c = muon_couplings(1.0, 1.0e-2)
        prod, absorp = rates.charged_muon_decay_rates_mixed(
            self.mass, self.energy, self.temperature, self.mu_mu,
            c.g_vector, c.g_axial
        )
        np.testing.assert_allclose(
            prod, np.exp(-self.energy[:, None]/self.temperature[:, None])*absorp,
            rtol=2e-12, atol=1e-15
        )

    def test_mixed_interference_splits_circular_modes_in_asymmetric_medium(self):
        c = muon_couplings(1.0, 1.0e-2)
        prod, _ = rates.charged_muon_decay_rates_mixed(
            self.mass, self.energy[:1], self.temperature[:1], self.mu_mu[:1],
            c.g_vector, c.g_axial
        )
        relative_asymmetry = abs(prod[0, 1]-prod[0, 2])/max(prod[0, 1], prod[0, 2])
        self.assertGreater(float(relative_asymmetry), 1e-6)

    def test_circular_modes_are_equal_at_zero_muon_chemical_potential(self):
        c = muon_couplings(1.0, 1.0e-2)
        prod, _ = rates.charged_muon_decay_rates_mixed(
            self.mass, self.energy[:1], self.temperature[:1], np.array([0.0]),
            c.g_vector, c.g_axial
        )
        self.assertAlmostEqual(float(prod[0, 1]), float(prod[0, 2]), places=14)

    def test_each_mixed_mode_angular_weight_is_normalized(self):
        c = muon_couplings(1.0, 1.0e-2)
        z, weights, angular = rates.dimuon_mixed_angular_weights(
            self.mass, c.g_vector, c.g_axial, order=64
        )
        np.testing.assert_allclose(np.einsum("z,zh->h", weights, angular),
                                   np.ones(3), rtol=2e-13, atol=2e-13)


if __name__ == "__main__":
    unittest.main()
