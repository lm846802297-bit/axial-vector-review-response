import pathlib
import sys
import unittest

import numpy as np
import sympy as sp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import b5_1b_sm_threshold_and_uv_rge as production
from b5_1d_independent_rge_audit import (
    gauge_spectrum_sums, scalar_quartic_tensor_coefficients,
    yukawa_matrix_coefficients, gauge_casimirs, gauge_quartic_sources,
    fermion_box_coefficients, independent_beta_vector, model_yukawa_charge_sums,
)


class IndependentB5OneLoopRGETests(unittest.TestCase):
    def test_complete_gauge_spectrum(self):
        g = gauge_spectrum_sums()
        self.assertEqual((g["bY"],g["b2"],g["b3"],g["bX"],g["TrYX"]),
                         (sp.Rational(19,2),-sp.Rational(19,6),-7,8,0))

    def test_scalar_tensor_portal_multiplicity(self):
        lH,lS,lHS=sp.symbols("lambda_H lambda_S lambda_HS")
        b=scalar_quartic_tensor_coefficients()
        self.assertEqual(sp.simplify(b["betaH_scalar"]-(24*lH**2+lHS**2)),0)
        self.assertEqual(sp.simplify(b["betaS_scalar"]-(20*lS**2+2*lHS**2)),0)
        self.assertEqual(sp.simplify(b["betaHS_scalar"]-lHS*(12*lH+8*lS+4*lHS)),0)

    def test_singlet_and_higgs_yukawa_matrices(self):
        lm,lt=sp.symbols("lambda_mu lambda_tau",real=True)
        ym,yt=sp.symbols("y_mu y_tau",real=True)
        b=yukawa_matrix_coefficients()
        self.assertEqual(sp.simplify(b["beta_lambda_mu_Y"]-lm*(2*lm**2+lt**2)),0)
        self.assertEqual(sp.simplify(b["beta_lambda_tau_Y"]-lt*(2*lt**2+lm**2)),0)
        self.assertEqual(sp.simplify(b["beta_y_mu_VLL"]-ym*(sp.Rational(5,2)*ym**2+yt**2)),0)
        self.assertEqual(sp.simplify(b["beta_y_tau_VLL"]-yt*(sp.Rational(5,2)*yt**2+ym**2)),0)

    def test_all_gauge_casimir_coefficients(self):
        self.assertEqual(gauge_casimirs(),{
            "yt_gY":-sp.Rational(17,12),"yt_g2":-sp.Rational(9,4),"yt_g3":-8,
            "yVLL_gY":-sp.Rational(15,4),"yVLL_g2":-sp.Rational(9,4),
            "yVLL_gX":-6,"lambdaVLL_gY":-6,"lambdaVLL_gX":-6,
            "lambdaH_g2":-9,"lambdaH_gY":-3,"lambdaS_gX":-48,
            "lambdaHS_g2":-sp.Rational(9,2),"lambdaHS_gY":-sp.Rational(3,2),
            "lambdaHS_gX":-24})

    def test_gauge_quartic_sources(self):
        g2,gY,gX=sp.symbols("g2 gY gX",real=True)
        q=gauge_quartic_sources()
        self.assertEqual(sp.simplify(q["betaH_gauge4"]-
            (sp.Rational(9,8)*g2**4+sp.Rational(3,4)*g2**2*gY**2+
             sp.Rational(3,8)*gY**4)),0)
        self.assertEqual(sp.simplify(q["betaS_gauge4"]-96*gX**4),0)
        self.assertEqual(q["betaHS_gauge4"],0)

    def test_pyrate3_model_yukawa_charge_invariance(self):
        sums=model_yukawa_charge_sums()
        self.assertEqual(len(sums),7)
        self.assertTrue(all(pair==(0,0) for pair in sums.values()))

    def test_vll_mixed_fermion_box_vanishes(self):
        b=fermion_box_coefficients()
        self.assertEqual(b["mixed_h2s2"],0)
        self.assertNotEqual(b["pure_h4"],0)
        self.assertNotEqual(b["pure_s4"],0)

    def _compare_production_rhs(self, state):
        expected=np.asarray(independent_beta_vector(state),dtype=float).reshape(-1)
        actual=production.uv_rhs(0.0,np.asarray(state,dtype=float))
        np.testing.assert_allclose(actual,expected,rtol=2e-12,atol=2e-14)

    def test_full_vector_matches_production_at_benchmarks(self):
        sm=production.run_sm_to_threshold()
        for name in ("A","B"):
            p=production.initial_uv(name,100.0,sm)
            self._compare_production_rhs([p[k] for k in production.KEYS])

    def test_full_vector_matches_production_at_generic_point(self):
        self._compare_production_rhs([
            0.371,0.617,0.941,0.083,0.754,0.91,0.62,
            0.13,0.71,0.057,0.094,0.017
        ])

    def test_decomposition_closes_to_full_quartic_beta(self):
        sm=production.run_sm_to_threshold()
        p=production.initial_uv("B",100.0,sm)
        b_hs,b_h,b_s=production.beta_decomposition(p)
        rhs=production.uv_rhs(0.0,np.asarray([p[k] for k in production.KEYS]))
        self.assertAlmostEqual(sum(b_h.values()),rhs[9],places=14)
        self.assertAlmostEqual(sum(b_s.values()),rhs[10],places=14)
        self.assertAlmostEqual(sum(b_hs.values()),rhs[11],places=14)


if __name__=="__main__":
    unittest.main()
