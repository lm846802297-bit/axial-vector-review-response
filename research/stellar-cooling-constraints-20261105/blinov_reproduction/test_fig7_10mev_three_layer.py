import unittest
import numpy as np
from diagnose_fig7_10mev_three_layer import channel_reduced_absorptions, weighted_quantile, weighted_tau_summary

class ThreeLayerDiagnosticTests(unittest.TestCase):
    def test_channel_reduced_opacity_additivity(self):
        x=np.array([[0.5,1.0,2.0]])
        production={
            "neutrino":np.array([[2.0,3.0,4.0]]),
            "compton":np.array([[5.0,6.0,7.0]]),
            "dimuon":np.array([[0.0,1.0,2.0]]),
        }
        reduced=channel_reduced_absorptions(production,x,np.ones_like(x))
        expected=-np.expm1(-x)*np.exp(x)*sum(production.values())
        np.testing.assert_allclose(sum(reduced.values()),expected,rtol=2e-15,atol=0.0)

    def test_weighted_quantile(self):
        values=np.array([1.0,2.0,3.0])
        weights=np.array([1.0,2.0,1.0])
        self.assertEqual(weighted_quantile(values,weights,0.0),1.0)
        self.assertEqual(weighted_quantile(values,weights,0.5),2.0)
        self.assertEqual(weighted_quantile(values,weights,1.0),3.0)

    def test_tau_channel_sums_and_fraction(self):
        weights=np.ones((2,2))
        tau={"neutrino":np.full((2,2),2.0),"compton":np.full((2,2),1.0),"dimuon":np.zeros((2,2))}
        result=weighted_tau_summary(tau,weights)
        self.assertEqual(result["total"]["weighted_mean"],3.0)
        self.assertAlmostEqual(result["neutrino"]["fraction_of_mean_total"],2.0/3.0)
        self.assertAlmostEqual(result["compton"]["fraction_of_mean_total"],1.0/3.0)

if __name__=="__main__":
    unittest.main(verbosity=2)
