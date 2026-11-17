#!/usr/bin/env python3
"""Regression tests for the heavy-light endpoint quadrature repair."""
import math, unittest, warnings, importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "exact_momentum_fermion_pole_audit.py"
spec = importlib.util.spec_from_file_location("exact_momentum_driver_test", SOURCE)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot import {SOURCE}")
driver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver)

class TestExactMomentumPoleQuadrature(unittest.TestCase):
    def setUp(self):
        driver.B0_GL_ORDER = 64
        driver.b0bar_cached.cache_clear()

    def test_b0bar_is_symmetric_under_internal_mass_exchange(self):
        s = 15687.56259940277 - 0.510105269611901j
        light, heavy = 0.10565307823687947, 20001.002765505546
        a = driver.b0bar(s, light, heavy, True)
        b = driver.b0bar(s, heavy, light, True)
        self.assertLess(abs(a - b), 2e-13)

    def test_endpoint_layer_integral_matches_high_precision_reference(self):
        import mpmath as mp
        mp.mp.dps = 80
        s_re, s_im = 15687.56259940277, -0.510105269611901
        mi, mj = 20001.002765505546, 0.10565307823687947
        smp = mp.mpc(repr(s_re), repr(s_im))
        mip, mjp, mup = mp.mpf(repr(mi)), mp.mpf(repr(mj)), mp.mpf(repr(driver.MU))
        def f(x):
            den = x*mip**2 + (1-x)*mjp**2 - x*(1-x)*smp
            return -mp.log(den/mup**2)
        delta = (mjp/mip)**2
        points = [mp.mpf("0"), mp.mpf("1")]
        for k in range(-1, 15):
            x = delta*mp.power(10,k)
            if 0 < x < mp.mpf("0.1"):
                points.append(x)
        points = sorted(set(points))
        ref = sum(mp.quad(f,[a,b],method="tanh-sinh",maxdegree=8) for a,b in zip(points[:-1],points[1:]))
        got = driver.b0bar(complex(s_re,s_im),mi,mj,True)
        self.assertLess(abs(got-complex(ref)),1e-12)

    def test_production_integrator_emits_no_warnings(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            for _name,vs,ma in (("A",70.886458,10.0),("B",315.0,63.0)):
                for ms in (100.0,125.25,150.0):
                    driver.b0bar_cached.cache_clear()
                    driver.poles_and_residues(ms,vs,ma)

    def test_hard_momentum_reference_coefficients(self):
        refs = {"A": (70.886458, 0.024030443985870786),
                "B": (315.0, 0.005407723994710553)}
        for name,(vs,ref) in refs.items():
            with self.subTest(benchmark=name):
                driver.b0bar_cached.cache_clear()
                got = driver.hard_momentum(vs,driver.MH**2,False)
                self.assertLess(abs(got.real-ref),2e-12)
                self.assertLess(abs(got.imag),2e-12)

    def test_all_six_pole_pairs_and_residue_closure(self):
        for name,vs,ma in (("A",70.886458,10.0),("B",315.0,63.0)):
            for ms in (100.0,125.25,150.0):
                with self.subTest(benchmark=name,ms=ms):
                    driver.b0bar_cached.cache_clear()
                    rows=driver.poles_and_residues(ms,vs,ma)
                    self.assertEqual(len(rows),2)
                    self.assertLess(max(r["residual"] for r in rows),1e-7)
                    self.assertLess(abs(sum(r["R_hh"] for r in rows)-1.0),3e-5)
                    for row in rows:
                        self.assertTrue(math.isfinite(row["mass"]))
                        self.assertTrue(math.isfinite(row["width"]))

if __name__ == "__main__":
    unittest.main(verbosity=2)
