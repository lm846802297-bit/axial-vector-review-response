"""Independent adaptive-quadrature tests for direct forward/reverse rates."""
import math
import unittest
from pathlib import Path

import numpy as np
from numpy.testing import assert_allclose

import rates
from audit_direct_collision_integrals import (
    direct_b14_compton_rates,
    direct_muon_susceptibility,
    direct_neutrino_rates,
)


class DirectNeutrinoCollisionIntegralTests(unittest.TestCase):
    def test_both_collision_terms_match_independent_adaptive_integrals(self):
        cases = [
            (1.0, 1.05, 19.265, -58.614),
            (10.0, 15.0, 24.0, -25.0),
            (100.0, 150.0, 27.0, 12.0),
            (200.0, 300.0, 20.0, 25.0),
        ]
        for mass, energy, temperature, chemical in cases:
            with self.subTest(mass=mass, energy=energy):
                p_flavor, a_flavor = direct_neutrino_rates(
                    mass, energy, temperature, chemical
                )
                p_direct, a_direct = p_flavor.sum(axis=0), a_flavor.sum(axis=0)
                p_code, a_code = rates.neutrino_rates(
                    mass, np.array([energy]), temperature, chemical, order=96
                )
                assert_allclose(p_code[0], p_direct, rtol=2e-9, atol=1e-300)
                assert_allclose(a_code[0], a_direct, rtol=2e-9, atol=1e-14)

    def test_detailed_balance_holds_for_each_flavor_and_mode(self):
        cases = [
            (1.0, 1.3, 19.265, -58.614),
            (10.0, 20.0, 24.0, -25.0),
            (100.0, 175.0, 27.0, 12.0),
            (200.0, 400.0, 20.0, 25.0),
        ]
        for mass, energy, temperature, chemical in cases:
            with self.subTest(mass=mass, energy=energy):
                p, a = direct_neutrino_rates(mass, energy, temperature, chemical)
                assert_allclose(a/p, np.full((2, 3), math.exp(energy/temperature)),
                                rtol=3e-10, atol=0.0)

    def test_charge_conjugation_swaps_neutrino_helicity_rates(self):
        p1, a1 = direct_neutrino_rates(10.0, 25.0, 24.0, 30.0)
        p2, a2 = direct_neutrino_rates(10.0, 25.0, 24.0, -30.0)
        assert_allclose(p1[:, [0, 2, 1]], p2, rtol=3e-11)
        assert_allclose(a1[:, [0, 2, 1]], a2, rtol=3e-11)


class DirectComptonThermalIntegralTests(unittest.TestCase):
    def test_b14_forward_and_inverse_thermal_integrals_are_independent(self):
        cases = [
            (1.0, 1.2, 19.265, 46.674),
            (10.0, 15.0, 24.0, 55.0),
            (100.0, 150.0, 27.0, 90.0),
            (200.0, 300.0, 20.0, 120.0),
        ]
        for mass, energy, temperature, mu_mu in cases:
            with self.subTest(mass=mass, energy=energy):
                n_minus, n_plus = direct_muon_susceptibility(temperature, mu_mu)
                p, a, p_b14 = direct_b14_compton_rates(
                    mass, energy, temperature, n_minus+n_plus
                )
                assert_allclose(a/p, np.full(3, math.exp(energy/temperature)),
                                rtol=3e-13)
                self.assertAlmostEqual(float(np.sum(p))/p_b14, 1.0, delta=3e-13)
                self.assertTrue(np.all(p > 0.0))
                self.assertTrue(np.all(a > p))

    def test_muon_charge_conjugation_swaps_susceptibilities(self):
        t, mu = 19.26522111, 46.67432845
        minus, plus = direct_muon_susceptibility(t, mu)
        plus2, minus2 = direct_muon_susceptibility(t, -mu)
        assert_allclose([minus, plus], [minus2, plus2], rtol=2e-11)
        self.assertGreater(minus, plus)
        self.assertGreater(plus, 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
