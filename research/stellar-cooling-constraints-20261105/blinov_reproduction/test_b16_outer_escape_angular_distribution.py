import sys
import unittest
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))

from blinov_reproduction.reference import KM_TO_MEV_INV
from blinov_reproduction.audit_b16_outer_profile_inputs import radial_shell_columns
from blinov_reproduction.audit_b16_outer_escape_angular_distribution import (
    summarize_distribution, escape_probability
)

class B16OuterEscapeAngularTests(unittest.TestCase):
    def test_constant_opacity_shell_matches_analytic_chord_length(self):
        source=np.array([8.0,12.0,15.0])
        energy=np.array([20.0])
        grid=np.linspace(0.0,25.0,501)
        rate=np.full((len(grid),1),0.37)
        mass=10.0
        columns,angles,weights=radial_shell_columns(
            source,energy,grid,rate,mass,angular_order=12,radial_order=96,
            shell_inner=22.0,shell_outer=25.0
        )
        velocity=np.sqrt(1.0-(mass/energy[0])**2)
        impact=source[:,None]*np.sqrt(1.0-angles[None,:]**2)
        length=np.sqrt(25.0**2-impact**2)-np.sqrt(22.0**2-impact**2)
        expected=0.37*length*KM_TO_MEV_INV/velocity
        np.testing.assert_allclose(columns[:,:,0],expected,rtol=2e-12,atol=1e-14)
        self.assertAlmostEqual(float(np.sum(weights)),1.0,places=14)

    def test_weighted_distribution_and_escape_probability(self):
        values=np.array([0.0,1.0,2.0,3.0])
        weights=np.ones_like(values)
        summary=summarize_distribution(values,weights)
        self.assertAlmostEqual(summary["mean"],1.5)
        self.assertEqual(summary["q50"],1.0)
        cols=values.reshape(2,2,1)
        w=weights.reshape(2,2,1)
        p1=escape_probability(cols,w,0.5)
        p2=escape_probability(cols,w,1.0)
        self.assertGreaterEqual(p1, p2)
        self.assertTrue(0.0<=p2<=1.0)

if __name__=="__main__":
    unittest.main(verbosity=2)
