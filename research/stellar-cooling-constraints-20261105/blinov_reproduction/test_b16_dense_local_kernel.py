import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from blinov_reproduction.audit_b16_dense_local_kernel import (
    direct_neutrino_pair_rates,
    direct_compton_rates,
)


class DenseLocalKernelTests(unittest.TestCase):
    def test_neutrino_pair_rate_is_even_in_chemical_potential(self):
        omega = np.linspace(10.5, 80.0, 40)
        plus, _ = direct_neutrino_pair_rates(10.0, omega, 25.0, 12.0, 512)
        minus, _ = direct_neutrino_pair_rates(10.0, omega, 25.0, -12.0, 512)
        np.testing.assert_allclose(plus, minus, rtol=2.0e-13, atol=1.0e-300)

    def test_neutrino_direct_integral_satisfies_detailed_balance(self):
        omega = np.linspace(10.5, 80.0, 40)
        prod, absorption = direct_neutrino_pair_rates(10.0, omega, 25.0, -7.0, 512)
        np.testing.assert_allclose(
            prod, np.exp(-omega/25.0)*absorption, rtol=2.0e-13, atol=1.0e-300
        )

    def test_compton_velocity_cancellation(self):
        omega = np.linspace(10.5, 80.0, 40)
        result = direct_compton_rates(10.0, omega, 25.0, 2.0e-5)
        np.testing.assert_allclose(
            result["reduced_absorption"], result["reduced_closed"],
            rtol=2.0e-13, atol=1.0e-300
        )

    def test_compton_detailed_balance(self):
        omega = np.linspace(10.5, 80.0, 40)
        result = direct_compton_rates(10.0, omega, 25.0, 2.0e-5)
        np.testing.assert_allclose(
            result["absorption"], np.exp(omega/25.0)*result["production"],
            rtol=2.0e-13, atol=1.0e-300
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
