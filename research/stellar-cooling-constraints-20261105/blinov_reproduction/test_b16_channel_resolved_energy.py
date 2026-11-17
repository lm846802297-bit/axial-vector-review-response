import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.reference import fermi_pair_average
from blinov_reproduction.audit_b16_channel_resolved_energy import (
    direct_pair_average as channel_direct_pair_average,
)
from blinov_reproduction.audit_b16_neutrino_b7_b9_kernel import (
    direct_pair_average as b9_direct_pair_average,
    published_i_b9,
)


class B16ChannelResolvedPairAverageTests(unittest.TestCase):
    SAMPLES = (
        (-58.0, 60.0, 10.0),
        (-1.0, 110.0, 3.5),
        (0.0, 210.0, 20.0),
        (1.0, 510.0, 3.4),
        (50.0, 1010.0, 18.0),
        (0.0, 60.0, 10.0),
        (20.0, 210.0, 10.0),
        (-20.0, 510.0, 10.0),
    )

    def test_channel_direct_angular_average_matches_closed_form(self):
        mass = 10.0
        for mu, omega, temperature in self.SAMPLES:
            velocity = np.sqrt(1.0 - (mass / omega) ** 2)
            expected = float(fermi_pair_average(mu, omega, temperature, velocity))
            actual = channel_direct_pair_average(
                mu, omega, temperature, mass, order=256
            )
            np.testing.assert_allclose(
                actual, expected, rtol=3.0e-12, atol=1.0e-300
            )

    def test_channel_and_b9_direct_angular_integrals_agree(self):
        mass = 10.0
        for mu, omega, temperature in self.SAMPLES:
            channel = channel_direct_pair_average(
                mu, omega, temperature, mass, order=256
            )
            b9 = b9_direct_pair_average(
                mu, omega, temperature, mass, order=256
            )
            np.testing.assert_allclose(
                channel, b9, rtol=3.0e-13, atol=1.0e-300
            )

    def test_published_b9_closed_form_matches_repository_pair_average(self):
        mass = 10.0
        for mu, omega, temperature in self.SAMPLES:
            velocity = np.sqrt(1.0 - (mass / omega) ** 2)
            expected = float(fermi_pair_average(mu, omega, temperature, velocity))
            actual = published_i_b9(mu, omega, temperature, mass)
            np.testing.assert_allclose(
                actual, expected, rtol=3.0e-12, atol=1.0e-300
            )

    def test_high_energy_pair_average_is_occupancy_suppressed(self):
        actual = channel_direct_pair_average(
            mu=0.0, omega=60.0, temperature=10.0, mass=10.0, order=512
        )
        self.assertGreater(actual, 0.0)
        self.assertLess(actual, 1.0e-2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
