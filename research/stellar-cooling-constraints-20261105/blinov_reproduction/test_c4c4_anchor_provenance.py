"""Check that C4-C4 runners use the archived byte-pinned anchor."""
import unittest
from pathlib import Path

import audit_b16_p1iii_eos_c4c4_quadrature_convergence as aq
import audit_b16_p1iii_eos_c4c4_radial_energy_dependence as radial


class AnchorProvenanceTests(unittest.TestCase):
    def test_historical_anchor_loads_with_expected_blob(self):
        self.assertEqual(len(aq.load_base_scan()), 96)
        self.assertEqual(radial.require_blob_sha(radial.C4C4A_PATH, radial.EXPECTED_C4C4A_GIT_BLOB, 'anchor'), aq.EXPECTED_BASE_SCAN_GIT_BLOB)
        self.assertEqual(aq.BASE_SCAN_PATH, radial.C4C4A_PATH)

    def test_current_table_is_not_silently_used_as_exact_snapshot(self):
        current = Path(__file__).parent / 'outputs/c4c4_energy_dependence_2026-11-12/local_rates_96.csv'
        with self.assertRaisesRegex(ValueError, 'SHA mismatch'):
            radial.require_blob_sha(current, radial.EXPECTED_C4C4A_GIT_BLOB, 'current table')


if __name__ == '__main__':
    unittest.main()
