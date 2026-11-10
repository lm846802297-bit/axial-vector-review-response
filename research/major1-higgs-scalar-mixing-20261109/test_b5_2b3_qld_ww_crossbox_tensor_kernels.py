#!/usr/bin/env python3
import unittest
import sympy as sp

from b5_2b3_qld_ww_crossbox_tensor_kernels import (
    canonical_lorentz_kernels,
    weak_tensor_weighted_oriented_sum,
    DeltaUV, L, M2,
)


class TestB52B3QLDWWKernels(unittest.TestCase):
    def setUp(self):
        self.k = canonical_lorentz_kernels()

    def test_FF_hard_kernel(self):
        expected = (DeltaUV-L-sp.Rational(3,2))/M2
        self.assertEqual(sp.simplify(self.k["A_FF"]-expected), 0)

    def test_FS_hard_kernel(self):
        expected = (DeltaUV-L+sp.Rational(3,2))/M2
        self.assertEqual(sp.simplify(self.k["A_FS"]-expected), 0)

    def test_SS_equals_FS_for_declared_numerator(self):
        self.assertEqual(sp.simplify(self.k["A_SS"]-self.k["A_FS"]), 0)

    def test_all_cross_box_UV_poles_cancel_after_oriented_sum(self):
        _, pole = weak_tensor_weighted_oriented_sum(self.k)
        self.assertEqual(pole, 0)

    def test_oriented_finite_T3_coefficient(self):
        coeff, _ = weak_tensor_weighted_conditional_sum(self.k)
        self.assertEqual(sp.simplify(coeff-sp.Rational(3,4)/M2), 0)

    def test_FF_Oepsilon_term_changes_finite_part(self):
        naive = (DeltaUV+1-L)/M2 - 1/M2
        self.assertEqual(sp.simplify(self.k["A_FF"]-naive+sp.Rational(3,2)/M2), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
