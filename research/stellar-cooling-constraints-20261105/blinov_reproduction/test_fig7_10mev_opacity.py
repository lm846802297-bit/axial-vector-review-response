import unittest
from pathlib import Path

import numpy as np

try:
    from .reference import DEFAULT_PROFILE, evaluate_mass
    from .diagnose_fig7_10mev_opacity import evaluate_with_opacity_scales
except ImportError:  # direct unittest discovery with this directory as top-level
    from reference import DEFAULT_PROFILE, evaluate_mass
    from diagnose_fig7_10mev_opacity import evaluate_with_opacity_scales


class Fig7OpacitySensitivityTests(unittest.TestCase):
    def test_unit_opacity_scales_reproduce_literal_reference(self):
        couplings = np.array([8e-10, 2e-9])
        baseline, thin = evaluate_with_opacity_scales(
            10.0, DEFAULT_PROFILE, couplings,
            {"neutrino": 1.0, "compton": 1.0, "dimuon": 1.0},
            radial_order=12, energy_order=24, angular_order=8, path_order=8)
        reference = evaluate_mass(
            10.0, DEFAULT_PROFILE, couplings,
            radial_order=12, energy_order=24, angular_order=8, path_order=8)
        np.testing.assert_allclose(
            baseline, reference["luminosity_erg_s"], rtol=2e-13, atol=0.0)
        self.assertAlmostEqual(thin, reference["thin_luminosity_erg_s"], places=10)

    def test_opacity_rescaling_keeps_production_source_fixed(self):
        couplings = np.array([1e-9])
        baseline, thin0 = evaluate_with_opacity_scales(
            10.0, DEFAULT_PROFILE, couplings,
            {"neutrino": 1.0, "compton": 1.0, "dimuon": 1.0},
            radial_order=12, energy_order=24, angular_order=8, path_order=8)
        varied, thin1 = evaluate_with_opacity_scales(
            10.0, DEFAULT_PROFILE, couplings,
            {"neutrino": 2.0, "compton": 0.5, "dimuon": 1.0},
            radial_order=12, energy_order=24, angular_order=8, path_order=8)
        self.assertEqual(thin0, thin1)
        self.assertNotEqual(baseline[0], varied[0])


if __name__ == "__main__":
    unittest.main()
