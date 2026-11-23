#!/usr/bin/env python3
import importlib.util
import pathlib
import sympy as sp
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-nonexceptional-kinematics.py"
SPEC = importlib.util.spec_from_file_location("rc001_nonexceptional", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestNonexceptionalKinematics(unittest.TestCase):
    def test_momentum_conservation_and_p4_norm(self):
        self.assertEqual(MOD.checks()["p4_on_shell_offshell_norm"], 0)

    def test_all_p4_pairwise_products(self):
        self.assertTrue(all(x == 0 for x in MOD.checks()["p4_pairwise_dot"]))

    def test_gram_determinant(self):
        self.assertEqual(MOD.checks()["determinant"], 0)

    def test_two_particle_channels_nonzero(self):
        self.assertEqual(
            MOD.checks()["two_particle_channel"],
            sp.Rational(4,3)*MOD.mu2
        )

    def test_gram_rank_three(self):
        self.assertEqual(MOD.G3.det(), sp.Rational(16,27)*MOD.mu2**3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
