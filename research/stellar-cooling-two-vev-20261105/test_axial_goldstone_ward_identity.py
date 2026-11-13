#!/usr/bin/env python3
"""Direct axial-current / Goldstone Ward-identity regression tests."""
import unittest

from stellar_semi_compton_axial_matrix_element import (
    axial_goldstone_ward_identity_residual,
)


class AxialGoldstoneWardIdentityTests(unittest.TestCase):
    def test_q_contract_equals_twice_mass_times_pseudoscalar_amplitude(self):
        benchmarks = (
            (10.0, 2.0, 0.3),
            (1.0, 0.1, -0.5),
            (200.0, 50.0, 0.8),
            (1.0, 0.5, 0.1),
            (30.0, 10.0, -0.9),
        )
        for point in benchmarks:
            with self.subTest(photon_energy=point[0], vector_mass=point[1]):
                self.assertLess(
                    axial_goldstone_ward_identity_residual(*point),
                    1.0e-10,
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
