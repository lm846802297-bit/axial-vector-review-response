from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import numpy as np

SCRIPT = Path(__file__).with_name("audit_croon_fig2_energy_threshold_convergence.py")
SPEC = importlib.util.spec_from_file_location("audit_croon_fig2_energy_threshold_convergence", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class CroonFig2EnergyThresholdAuditTests(unittest.TestCase):
    def test_relative_change_is_symmetric_and_zero_safe(self):
        previous = np.asarray([0.0, 1.0, 2.0])
        current = np.asarray([0.0, 1.01, 1.98])
        got = MODULE.relative_change(previous, current)
        self.assertEqual(got[0], 0.0)
        self.assertAlmostEqual(got[1], 0.01 / 1.01, places=12)
        self.assertAlmostEqual(got[2], 0.02 / 2.0, places=12)

    def test_audit_targets_light_masses_and_outer_boundary(self):
        self.assertEqual(MODULE.MASS_LABELS, ("0.1 eV", "1 eV", "10 eV"))
        self.assertIn(2560, MODULE.ORDERS)
        self.assertIn(1.0, MODULE.COUPLINGS)
        self.assertIn(7.5e-4, MODULE.COUPLINGS)


if __name__ == "__main__":
    unittest.main()
