import sys
import unittest
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))

from blinov_reproduction.reference import KM_TO_MEV_INV, radial_rule
from blinov_reproduction.audit_b16_outer_profile_inputs import radial_shell_columns


class B16OuterProfileInputTests(unittest.TestCase):
    def test_outer_radial_grid_resolves_both_22_24_and_24_25_intervals(self):
        r,_=radial_rule(25.0,40)
        grid=np.unique(np.r_[0.0,r,25.0])
        outer=grid[grid>=22.0]
        self.assertEqual(len(outer),9)
        self.assertAlmostEqual(outer[0],22.138863688405948,places=10)
        self.assertAlmostEqual(outer[-1],25.0,places=12)
        self.assertLess(float(np.max(np.diff(outer))),0.7)

    def test_radial_coordinate_shell_integral_matches_analytic_chord_length(self):
        mass=10.0
        energies=np.array([12.0,20.0,50.0])
        grid=np.array([0.0,22.0,23.0,24.0,25.0])
        constant_rate=2.5e-4
        rate=np.full((len(grid),len(energies)),constant_rate)
        source_radii=np.array([8.0,12.0,15.0])
        columns,angles,weights=radial_shell_columns(
            source_radii,energies,grid,rate,mass,angular_order=12,radial_order=64
        )
        velocity=np.sqrt(1.0-(mass/energies)**2)
        for ir,r0 in enumerate(source_radii):
            for ia,cosine in enumerate(angles):
                impact=r0*np.sqrt(1.0-cosine*cosine)
                length=np.sqrt(25.0**2-impact**2)-np.sqrt(22.0**2-impact**2)
                expected=constant_rate*length*KM_TO_MEV_INV/velocity
                np.testing.assert_allclose(columns[ir,ia],expected,rtol=2e-13,atol=0.0)
        self.assertAlmostEqual(float(np.sum(weights)),1.0,places=14)

    def test_shell_integral_rejects_sources_inside_the_shell(self):
        with self.assertRaises(ValueError):
            radial_shell_columns(
                np.array([22.5]),np.array([12.0]),
                np.array([22.0,25.0]),np.ones((2,1)),10.0
            )


if __name__=="__main__":
    unittest.main(verbosity=2)
