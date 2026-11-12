#!/usr/bin/env python3
import math
import unittest

from b5_2a_c5_squared_operator_block import calculate, symbolic_checks


class TestB52ACurrentOrientation(unittest.TestCase):
    def test_flavor_scalar_orientation(self):
        _, _, _, a, _, _ = calculate("A", 100.0)
        self.assertEqual(a["mu"]["eta"], +1)
        self.assertEqual(a["tau"]["eta"], -1)
        self.assertLess(a["mu"]["currents"]["CLS_commonS"], 0.0)
        self.assertGreater(a["tau"]["currents"]["CLS_commonS"], 0.0)
        self.assertGreater(a["mu"]["currents"]["CSe_commonS"], 0.0)
        self.assertLess(a["tau"]["currents"]["CSe_commonS"], 0.0)

    def test_benchmark_A_common_S_sums(self):
        _, _, _, a, _, _ = calculate("A", 100.0)
        cls = sum(v["currents"]["CLS_commonS"] for v in a.values())
        che = sum(v["currents"]["CHe"] for v in a.values())
        cse = sum(v["currents"]["CSe_commonS"] for v in a.values())
        self.assertTrue(math.isclose(cls, 9.809941046989e-11, rel_tol=2e-12))
        self.assertTrue(math.isclose(che, 9.879561393123e-11, rel_tol=2e-12))
        self.assertTrue(math.isclose(cse, -1.961988209398e-10, rel_tol=2e-12))

    def test_benchmark_B_common_S_sums(self):
        _, _, _, b, _, _ = calculate("B", 100.0)
        cls = sum(v["currents"]["CLS_commonS"] for v in b.values())
        che = sum(v["currents"]["CHe"] for v in b.values())
        cse = sum(v["currents"]["CSe_commonS"] for v in b.values())
        self.assertTrue(math.isclose(cls, 4.967888532040e-12, rel_tol=2e-12))
        self.assertTrue(math.isclose(che, 5.003145229048e-12, rel_tol=2e-12))
        self.assertTrue(math.isclose(cse, -9.935777064080e-12, rel_tol=2e-12))

    def test_scalar_bubble_and_4f_coefficients_are_orientation_even(self):
        _, _, _, a, beta_c, delta_portal = calculate("A", 100.0)
        ksum = sum(v["kappa"] for v in a.values())
        self.assertTrue(math.isclose(beta_c, -400_000_000.0*ksum, rel_tol=2e-14))
        self.assertTrue(math.isclose(beta_c, delta_portal/2.0, rel_tol=2e-14))
        c4s = sum(v["currents"]["C4f_scalar"] for v in a.values())
        c4v = sum(v["currents"]["C4f_vector"] for v in a.values())
        self.assertTrue(math.isclose(c4s, -2.0*ksum, rel_tol=2e-14))
        self.assertTrue(math.isclose(c4v, +ksum, rel_tol=2e-14))

    def test_exact_current_and_log_derivative_identities(self):
        deriv = symbolic_checks()
        self.assertEqual(set(deriv), {
            "CLS_commonS", "CHe", "CSe_commonS", "C4fS", "C4fV"
        })


if __name__ == "__main__":
    unittest.main(verbosity=2)
