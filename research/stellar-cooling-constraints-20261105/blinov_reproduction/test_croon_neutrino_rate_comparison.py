import unittest
from pathlib import Path

import numpy as np

try:
    from .croon_neutrino_rate_comparison import (
        b7_one_flavour_rate_per_g2,
        blinov_b7_two_flavour_rate_per_g2,
        croon_eq46_rate_per_g2,
        fermi_pair_average,
        lai_eq10_mb_rate_per_g2,
        rate_ratios,
    )
    from .reference import DEFAULT_PROFILE, fermi_pair_average as reference_pair_average
except ImportError:
    from croon_neutrino_rate_comparison import (
        b7_one_flavour_rate_per_g2,
        blinov_b7_two_flavour_rate_per_g2,
        croon_eq46_rate_per_g2,
        fermi_pair_average,
        lai_eq10_mb_rate_per_g2,
        rate_ratios,
    )
    from reference import DEFAULT_PROFILE, fermi_pair_average as reference_pair_average


class CroonNeutrinoRateComparisonTests(unittest.TestCase):
    def test_direct_B6_angular_integral_matches_reference_antiderivative(self):
        cases = (
            (-58.6137567217484, 12.0, 19.265221107965),
            (-20.4279370538693, 50.0, 38.847171184805),
            (-2.59165549916519, 100.0, 23.881959149249),
            (0.0, 210.0, 13.2314158304208),
        )
        for mu, omega, temperature in cases:
            velocity = np.sqrt(1.0 - (10.0 / omega) ** 2)
            direct = fermi_pair_average(mu, omega, temperature, velocity, order=384)
            reference = float(reference_pair_average(mu, omega, temperature, velocity))
            self.assertAlmostEqual(direct / reference, 1.0, delta=3e-12)

    def test_B7_prefactor_includes_three_polarization_sum(self):
        mass, omega, pair_average = 10.0, 30.0, 0.123
        rate = b7_one_flavour_rate_per_g2(mass, omega, pair_average)
        expected = (mass / omega) * 3.0 * (mass / (24.0 * np.pi)) * pair_average
        self.assertAlmostEqual(rate / expected, 1.0, places=14)

    def test_two_flavour_MB_limit_matches_Lai_and_is_three_times_Croon(self):
        mass, omega, temperature = 99.0, 100.0, 2.0
        velocity = np.sqrt(1.0 - (mass / omega) ** 2)
        b7 = blinov_b7_two_flavour_rate_per_g2(
            mass, omega, temperature, 0.0, 0.0, order=256
        )["rate_total_per_g2_MeV"]
        lai = lai_eq10_mb_rate_per_g2(mass, omega, temperature)
        croon = croon_eq46_rate_per_g2(mass, omega, temperature)
        self.assertAlmostEqual(b7 / lai, 1.0, delta=2e-9)
        self.assertAlmostEqual(b7 / croon, 3.0, delta=2e-9)

    def test_actual_SFHo_rate_ratio_is_not_a_constant(self):
        low = rate_ratios(
            10.0, 12.0, 38.847171184805, -20.4279370538693, 0.0, order=512
        )["B7_two_flavour_over_Croon"]
        high = rate_ratios(
            10.0, 210.0, 38.847171184805, -20.4279370538693, 0.0, order=512
        )["B7_two_flavour_over_Croon"]
        self.assertLess(low, 0.3)
        self.assertGreater(high, 2.0)
        self.assertGreater(high, low)

    def test_profile_benchmark_has_expected_profile_provenance(self):
        self.assertTrue(Path(DEFAULT_PROFILE).exists())
        result = rate_ratios(
            10.0, 50.0, 23.881959149249, -2.59165549916519, 0.0, order=256
        )
        self.assertTrue(np.isfinite(result["B7_two_flavour_over_Croon"]))
        self.assertGreater(result["rate_total_per_g2_MeV"], 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
