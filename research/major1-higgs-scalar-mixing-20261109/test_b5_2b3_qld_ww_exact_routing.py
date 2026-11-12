#!/usr/bin/env python3
import unittest
import sympy as sp

from b5_2b3_qld_ww_exact_routing import (
    exact_pair_kernels,
    weighted_triplet_sum,
    retain_epsilon_times_uv_pole,
    eps, DeltaUV, L, M2, d,
)


class TestB52B3ExactWWRouting(unittest.TestCase):
    def setUp(self):
        self.k = exact_pair_kernels()
        self.J = (DeltaUV+1-L)/M2
        self.K = -1/M2

    def test_pair01_FF_kernel(self):
        expected = 2*(d-2)/d*self.K
        self.assertEqual(sp.simplify(self.k["LD-W-01"]-expected), 0)

    def test_pair02_FS_kernel(self):
        expected = -self.J+2/d*self.K
        self.assertEqual(sp.simplify(self.k["LD-W-02"]-expected), 0)

    def test_pair05_FS_kernel_is_distinct(self):
        expected = (1+2/d)*self.J
        self.assertEqual(sp.simplify(self.k["LD-W-05"]-expected), 0)
        self.assertNotEqual(
            sp.simplify(self.k["LD-W-05"]-self.k["LD-W-02"]), 0
        )

    def test_pair06_SS_kernel(self):
        expected = -4/d*self.J
        self.assertEqual(sp.simplify(self.k["LD-W-06"]-expected), 0)

    def test_exact_weak_tensor_weighted_sum(self):
        expected = (6/d*self.J-2*(d-3)/d*self.K)/4
        self.assertEqual(sp.simplify(weighted_triplet_sum(self.k)-expected), 0)

    def test_epsilon_times_uv_pole_retained(self):
        expected = (sp.Rational(3,8)*DeltaUV-sp.Rational(3,8)*L+sp.Rational(11,16))/M2
        self.assertEqual(sp.simplify(retain_epsilon_times_uv_pole(weighted_triplet_sum(self.k))-expected), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
