import csv
import gzip
import tempfile
import unittest
from pathlib import Path
from audit_scan_archive_versions_2026_11_14 import compare_archives


class ArchiveComparisonTests(unittest.TestCase):
    def write_csv(self, path, rows):
        with gzip.open(path, 'wt', newline='', encoding='utf-8') as stream:
            writer = csv.writer(stream)
            writer.writerow(['mass', 'fourmu_Gamma_over_sigma_lower_bound', 'fourmu_Gamma_over_sigma_upper_bound'])
            writer.writerows(rows)

    def test_detects_swapped_bounds_and_tracks_other_columns(self):
        with tempfile.TemporaryDirectory() as d:
            old, new = Path(d)/'old.gz', Path(d)/'new.gz'
            self.write_csv(old, [['1','4','2'], ['2','nan','nan']])
            self.write_csv(new, [['1','2','4'], ['3','nan','nan']])
            result = compare_archives(old, new)
            self.assertEqual(result.get('rows'), 2)
            self.assertEqual(result.get('different_rows'), 2)
            self.assertEqual(result.get('changed_columns'), {'mass': 1, 'fourmu_Gamma_over_sigma_lower_bound': 1, 'fourmu_Gamma_over_sigma_upper_bound': 1})
            self.assertEqual(result.get('old_lower_greater_count'), 1)
            self.assertEqual(result.get('current_lower_greater_count'), 0)
            self.assertEqual(result.get('exact_swapped_pairs'), 1)
            self.assertEqual(result.get('nonfinite_bound_rows'), 1)

    def test_rejects_different_row_counts(self):
        with tempfile.TemporaryDirectory() as d:
            old, new = Path(d)/'old.gz', Path(d)/'new.gz'
            self.write_csv(old, [['1','4','2']])
            self.write_csv(new, [])
            with self.assertRaises(ValueError):
                compare_archives(old, new)

if __name__ == '__main__':
    unittest.main()
