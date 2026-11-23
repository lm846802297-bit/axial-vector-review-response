#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-nonexceptional-hard-expansion.py"
SPEC = importlib.util.spec_from_file_location("rc001_ww_nonexceptional_hard", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestNonexceptionalHardExpansion(unittest.TestCase):
    def test_exceptional_pair_kernels_match_previous_result(self):
        expected = {
            "01": (0, 2*(MOD.d-2)/MOD.d),
            "02": (-1, 2/MOD.d),
            "05": (2*(1-1/MOD.d), -2/MOD.d),
            "06": (-1, 2/MOD.d),
        }
        got = MOD.exceptional_kernels()
        for pair in expected:
            self.assertEqual(sp.simplify(got[pair][0]-expected[pair][0]), 0)
            self.assertEqual(sp.simplify(got[pair][1]-expected[pair][1]), 0)

    def test_weighted_J_kernel(self):
        got, _ = MOD.triplet_weighted_kernels()
        expected, _ = MOD.expected_triplet_kernels()
        self.assertEqual(sp.simplify(got-expected), 0)

    def test_weighted_K_kernel(self):
        _, got = MOD.triplet_weighted_kernels()
        _, expected = MOD.expected_triplet_kernels()
        self.assertEqual(sp.simplify(got-expected), 0)

    def test_nonexceptional_pole_matches_soft_residue(self):
        pole, _, _ = MOD.hard_amplitude_expansion()
        self.assertEqual(sp.simplify(pole-MOD.soft_uv_residue()), 0)

    def test_soft_pole_cancels_hard_pole(self):
        pole, _, _ = MOD.hard_amplitude_expansion()
        eft_soft_pole = -MOD.soft_uv_residue()
        self.assertEqual(sp.simplify(pole+eft_soft_pole), 0)

    def test_msbar_finite_local_polynomial(self):
        _, finite, _ = MOD.hard_amplitude_expansion()
        finite = sp.factor(finite.subs(MOD.cbar, 0))
        expected = (
            sp.Rational(1, 2)*(1-MOD.L)*MOD.p1
            + (sp.Rational(11, 16)-sp.Rational(3, 8)*MOD.L)*MOD.p2
            + (sp.Rational(1, 4)-sp.Rational(3, 4)*MOD.L)*MOD.p3
        )
        self.assertEqual(sp.simplify(finite-expected), 0)

    def test_matching_scale_mu_equals_ME(self):
        _, finite, _ = MOD.hard_amplitude_expansion()
        finite = sp.factor(finite.subs({MOD.cbar: 0, MOD.L: 0}))
        expected = (
            sp.Rational(1, 2)*MOD.p1
            + sp.Rational(11, 16)*MOD.p2
            + sp.Rational(1, 4)*MOD.p3
        )
        self.assertEqual(sp.simplify(finite-expected), 0)

    def test_exceptional_limit_reproduces_11_over_16(self):
        _, finite, _ = MOD.hard_amplitude_expansion()
        finite = sp.factor(finite.subs(MOD.cbar, 0))
        exceptional = sp.simplify(finite.subs({
            MOD.p1: 0, MOD.p2: 1, MOD.p3: 0
        }))
        expected = sp.Rational(11, 16)-sp.Rational(3, 8)*MOD.L
        self.assertEqual(sp.simplify(exceptional-expected), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
