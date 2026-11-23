import unittest
import numpy as np
from shape import shape, scale_free_window, native_data

class NecessaryLaplaceChecks(unittest.TestCase):
 def test_positive_mixture(self):
  x=np.array([.02,.1,.4,.7,1.])
  y=np.log(.3*np.exp(-x)+.7*np.exp(-12*x))
  a=shape(x,y)
  self.assertEqual(a['n_monotonicity_violations'],0)
  self.assertEqual(a['n_convexity_violations'],0)
  self.assertAlmostEqual(a['min_vertical_log_envelope_for_shape_feasibility'],0.)
 def test_nonconvex_peak_fails_exact_but_fits_perturbation(self):
  out=shape(np.array([0.,.5,1.]),np.array([0.,-.3,-1.]))
  self.assertEqual(out['n_convexity_violations'],1)
  self.assertAlmostEqual(out['max_positive_log_convexity_excess'],.2)
  self.assertAlmostEqual(out['min_vertical_log_envelope_for_shape_feasibility'],.1)
 def test_normalization_free(self):
  x=np.array([.1,.2,1.0]);ref=np.array([1.,-.1,-2.]);baseline=np.array([1.5,.7,-.9])
  a=scale_free_window(x,baseline,ref,0,2);b=scale_free_window(x,baseline+7.5,ref-1.2,0,2)
  self.assertAlmostEqual(a['log_ratio_change'],b['log_ratio_change'])
 def test_pinned_figure_crosscheck(self):
  u=native_data()
  self.assertEqual(len(u['g']),25)
  self.assertLess(u['geometry_crosscheck_max_rel'],2e-13)
