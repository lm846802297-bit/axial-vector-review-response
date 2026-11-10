import sympy as sp
import unittest

from b5_1b_complex_singlet_yukawa_beta_audit import (
    derive_yukawa_beta,
    derive_higgs_doublet_vll_yukawa_beta,
)


class ComplexSingletYukawaBetaTests(unittest.TestCase):
    def test_muon_beta_has_two_self_and_one_tau(self):
        lm, lt, beta_mu, beta_tau = derive_yukawa_beta()
        self.assertEqual(sp.simplify(beta_mu-lm*(2*lm**2+lt**2)), 0)

    def test_tau_beta_has_two_self_and_one_muon(self):
        lm, lt, beta_mu, beta_tau = derive_yukawa_beta()
        self.assertEqual(sp.simplify(beta_tau-lt*(2*lt**2+lm**2)), 0)

    def test_single_flavor_limit_is_two_lambda_cubed(self):
        lm, lt, beta_mu, beta_tau = derive_yukawa_beta()
        self.assertEqual(sp.simplify(beta_mu.subs(lt, 0)-2*lm**3), 0)
        self.assertEqual(sp.simplify(beta_tau.subs(lm, 0)-2*lt**3), 0)


    def test_higgs_muon_beta_has_sm_doublet_self_coefficient(self):
        ym, yt, beta_mu, beta_tau = derive_higgs_doublet_vll_yukawa_beta()
        expected = ym*(sp.Rational(5, 2)*ym**2+yt**2)
        self.assertEqual(sp.simplify(beta_mu-expected), 0)

    def test_higgs_tau_beta_has_sm_doublet_self_coefficient(self):
        ym, yt, beta_mu, beta_tau = derive_higgs_doublet_vll_yukawa_beta()
        expected = yt*(sp.Rational(5, 2)*yt**2+ym**2)
        self.assertEqual(sp.simplify(beta_tau-expected), 0)

    def test_flavor_exchange_symmetry(self):
        lm, lt, beta_mu, beta_tau = derive_yukawa_beta()
        self.assertEqual(sp.simplify(beta_mu.subs({lm: lt, lt: lm}, simultaneous=True)-beta_tau), 0)


if __name__ == "__main__":
    unittest.main()
