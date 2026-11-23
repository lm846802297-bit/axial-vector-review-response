#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-nonexceptional-soft-pole.py"
SPEC = importlib.util.spec_from_file_location("rc001_ww_nonexceptional_soft", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestNonexceptionalWWSoftPole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 40
        cls.data = MOD.compute_audit()

    def test_symmetric_point_and_momentum_conservation(self):
        p1, p2, p3, p4 = MOD.symmetric_momenta()
        self.assertEqual(MOD.vadd(p1, p2, p3, p4), [0, 0, 0, 0])
        for p in (p1, p2, p3, p4):
            self.assertEqual(MOD.vdot(p, p), 1)
        for i, p in enumerate((p1, p2, p3, p4)):
            for q in (p1, p2, p3, p4)[i+1:]:
                self.assertEqual(MOD.vdot(p, q), -sp.Rational(1, 3))

    def test_all_four_triangle_invariants(self):
        expected = (1, 1, sp.Rational(4, 3))
        for pair in MOD.PAIRS:
            self.assertEqual(self.data["triangle_invariants"][pair], expected)

    def test_uv_soft_expansion_equals_eft_insertion_numerator(self):
        momenta = MOD.symmetric_momenta()
        for pair in MOD.PAIRS:
            uv_numerator, _, _ = MOD.routing(pair, momenta)
            eft_numerator = MOD.eft_soft_numerator(pair, momenta)
            self.assertEqual(sp.simplify(uv_numerator - eft_numerator), sp.zeros(4), pair)

    def test_pairwise_soft_uv_residues(self):
        self.assertEqual(
            self.data["pair_coefficients"],
            self.data["expected_pairs"],
        )

    def test_weighted_triplet_soft_uv_residue(self):
        self.assertEqual(
            self.data["weighted_coefficients"],
            [sp.Rational(1, 2), sp.Rational(3, 8), sp.Rational(3, 4)],
        )
        self.assertEqual(self.data["weighted_residual"], sp.zeros(4))

    def test_exceptional_limit_reproduces_old_three_eighths(self):
        self.assertEqual(
            self.data["exceptional_coefficients"],
            [sp.Rational(3, 8), 0, 0, 0],
        )

    def test_epsilon_form_factor_polynomial(self):
        self.assertEqual(
            sp.simplify(
                self.data["epsilon_polynomial"]
                - sp.sqrt(3) * (MOD.Y + 3 * MOD.Z - 2) / 9
            ),
            0,
        )
        self.assertEqual(
            sp.simplify(
                self.data["epsilon_symmetrized"]
                + 2 * sp.sqrt(3) * (1 - MOD.Y - MOD.Z) / 9
            ),
            0,
        )

    def test_scalar_triangle_master(self):
        value = MOD.scalar_triangle_parameter(mp.mpf(4) / 3)
        expected = mp.mpf("2.1240339480038191550754515898884732174783")
        self.assertLess(abs(value - expected), mp.mpf("1e-35"))

    def test_epsilon_moment(self):
        value = MOD.epsilon_moment(mp.mpf(4) / 3)
        expected = mp.mpf("0.7467700413397904843482771519674888779972")
        self.assertLess(abs(value - expected), mp.mpf("1e-35"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
