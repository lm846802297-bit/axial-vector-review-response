import unittest
from math import exp, log

import numpy as np

from weighted import tangents


class ChannelDerivativeTests(unittest.TestCase):
    def test_one_ray_one_open_channel(self):
        p = tangents({"neutrino":np.array([[2.]]), "semi_compton":np.array([[0.]])},
                     {"neutrino":np.array([[[3.]]]), "semi_compton":np.array([[[0.]]])},
                     np.array([1.]), 0.5)
        nu = p["channel_tangents"]["neutrino"]
        self.assertAlmostEqual(p["luminosity_erg_s"], 0.5*exp(-0.75))
        self.assertAlmostEqual(p["dlnL_dlng"], 0.5)
        self.assertAlmostEqual(nu["source_only_dlnL_dln_channel_rate"], 1.)
        self.assertAlmostEqual(nu["opacity_only_dlnL_dln_channel_rate"], -.75)
        self.assertAlmostEqual(nu["same_channel_source_opacity_matched_dlnL_dln_channel_rate"], .25)

    def test_exact_derivative_against_two_ray_hand_coded_central_difference(self):
        a = np.array([.25,.75])
        sources = dict(neutrino=np.array([[2.]]), semi_compton=np.array([[3.]]))
        columns = dict(neutrino=np.array([[[1.],[6.]]]),semi_compton=np.array([[[4.],[1.]]]))
        p = tangents(sources,columns,a,1.)
        h = 1.e-5
        def log_l(scale):
            return log((2.*scale+3.)*(.25*exp(-scale-4.)+.75*exp(-6.*scale-1.)))
        numerical = (log_l(exp(h))-log_l(exp(-h)))/(2*h)
        analytic = p["channel_tangents"]["neutrino"][
            "same_channel_source_opacity_matched_dlnL_dln_channel_rate"]
        self.assertAlmostEqual(analytic,numerical,places=9)

if __name__ == "__main__":
    unittest.main()
