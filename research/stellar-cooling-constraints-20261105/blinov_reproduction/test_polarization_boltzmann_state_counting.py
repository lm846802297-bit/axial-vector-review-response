import math
import unittest

from polarization_boltzmann_state_counting import (
    effective_absorption_rate,
    mode_collision_terms,
    mode_escape_luminosity,
    reduced_absorption_rates,
    scalar_escape_average_opacity,
    scalar_escape_sum_opacity,
    unpolarized_total_collision,
)


class PolarizationBoltzmannStateCountingTests(unittest.TestCase):
    def test_mode_by_mode_detailed_balance_gives_equilibrium(self):
        omega_over_T = 12.0
        f_eq = 1.0 / math.expm1(omega_over_T)
        gamma_abs = (0.8, 1.1, 1.3)
        gamma_prod = tuple(math.exp(-omega_over_T) * x for x in gamma_abs)
        collision = mode_collision_terms(
            gamma_prod, gamma_abs, (f_eq, f_eq, f_eq)
        )
        for value in collision:
            self.assertAlmostEqual(value, 0.0, delta=2e-15)

    def test_sum_of_modes_matches_equal_occupation_total_equation(self):
        gamma_prod = (0.21, 0.17, 0.13)
        gamma_abs = (0.81, 1.02, 1.24)
        total_occupation = 0.81
        f_each = total_occupation / 3.0
        direct = sum(mode_collision_terms(
            gamma_prod, gamma_abs, (f_each, f_each, f_each)
        ))
        scalar = unpolarized_total_collision(
            gamma_prod, gamma_abs, total_occupation
        )
        self.assertAlmostEqual(direct, scalar, places=15)

    def test_effective_absorption_is_occupancy_weighted(self):
        gamma_abs = (2.0, 4.0, 6.0)
        occupations = (1.0, 2.0, 3.0)
        self.assertAlmostEqual(
            effective_absorption_rate(gamma_abs, occupations), 5.0
        )
        equal_occupations = (1.0, 1.0, 1.0)
        self.assertAlmostEqual(
            effective_absorption_rate(gamma_abs, equal_occupations), 4.0
        )
        self.assertAlmostEqual(sum(gamma_abs) / 3.0, 4.0)

    def test_reduced_absorption_preserves_mode_sum(self):
        gamma_abs = (0.8, 1.1, 1.3)
        x = 3.7
        reduced = reduced_absorption_rates(gamma_abs, x)
        expected = (1.0 - math.exp(-x)) * sum(gamma_abs)
        self.assertAlmostEqual(sum(reduced), expected, places=14)

    def test_equal_mode_opacities_make_average_closure_exact(self):
        source = (0.24, 0.37, 0.39)
        tau = (2.0, 2.0, 2.0)
        mode = mode_escape_luminosity(source, tau)
        average = scalar_escape_average_opacity(source, tau)
        self.assertAlmostEqual(mode, average, places=15)

    def test_sum_opacity_is_not_single_mode_attenuation(self):
        source = (0.24, 0.37, 0.39)
        tau = (2.0, 2.0, 2.0)
        mode = mode_escape_luminosity(source, tau)
        summed = scalar_escape_sum_opacity(source, tau)
        self.assertAlmostEqual(mode / summed, math.exp(4.0), places=13)

    def test_mode_sum_is_not_generically_equal_to_average_opacity(self):
        source = (0.24, 0.37, 0.39)
        tau = (0.2, 0.5, 1.0)
        mode = mode_escape_luminosity(source, tau)
        average = scalar_escape_average_opacity(source, tau)
        self.assertGreater(abs(mode - average), 1e-3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
