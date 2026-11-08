import sys
import unittest
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))

from blinov_reproduction.audit_b16_outer_profile_inputs import radial_shell_columns
from blinov_reproduction.audit_b16_directional_escape_8_15 import weighted_mean,weighted_quantile


class B16DirectionalEscapeTests(unittest.TestCase):
    def test_outer_shell_tau_is_symmetric_under_cos_theta_sign(self):
        radii=np.array([8.0,10.0,12.0,15.0])
        energies=np.array([10.5,12.0,20.0,50.0])
        radial=np.array([22.0,22.5,23.0,23.5,24.0,24.5,25.0])
        rate=np.tile(np.linspace(0.1,0.5,len(radial))[:,None],(1,len(energies)))
        columns,angles,weights=radial_shell_columns(
            radii,energies,radial,rate,10.0,angular_order=32,radial_order=64
        )
        np.testing.assert_allclose(columns,columns[:,::-1,:],rtol=2e-14,atol=1e-300)
        self.assertAlmostEqual(float(np.sum(weights)),1.0,places=14)

    def test_directional_weighted_statistics(self):
        values=np.array([1.0,2.0,3.0,4.0])
        weights=np.ones(4)
        self.assertAlmostEqual(weighted_mean(values,weights),2.5)
        self.assertAlmostEqual(weighted_quantile(values,weights,0.5),3.0)

    def test_outer_shell_path_length_has_correct_impact_parameter_dependence(self):
        r0=12.0
        cosine=np.array([1.0,0.0,-1.0])
        impact=r0*np.sqrt(1.0-cosine**2)
        lengths=np.sqrt(25.0**2-impact**2)-np.sqrt(22.0**2-impact**2)
        self.assertAlmostEqual(lengths[0],3.0,places=12)
        self.assertAlmostEqual(lengths[1],lengths[2],places=12)
        self.assertGreater(lengths[1],lengths[0])


if __name__=="__main__":
    unittest.main(verbosity=2)
