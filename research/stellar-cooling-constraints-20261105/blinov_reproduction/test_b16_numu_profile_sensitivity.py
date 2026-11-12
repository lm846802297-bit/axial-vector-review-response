import sys
import tempfile
import unittest
from pathlib import Path
import csv
import math

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))

from blinov_reproduction.audit_b16_numu_profile_sensitivity import write_scaled_profile
from blinov_reproduction.reference import DEFAULT_PROFILE


class B16NumuProfileSensitivityTests(unittest.TestCase):
    def assert_float_same(self, a, b):
        av, bv = float(a), float(b)
        if math.isnan(av) or math.isnan(bv):
            self.assertTrue(math.isnan(av) and math.isnan(bv))
        else:
            self.assertAlmostEqual(av, bv, places=10)

    def read_rows(self,path):
        with Path(path).open(newline="",encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def test_scale_one_preserves_all_profile_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/"same.csv"
            write_scaled_profile(DEFAULT_PROFILE,out,1.0)
            original=self.read_rows(DEFAULT_PROFILE)
            copied=self.read_rows(out)
            self.assertEqual(len(original),len(copied))
            for a,b in zip(original,copied):
                for key in a:
                    self.assert_float_same(a[key],b[key])

    def test_zero_scale_only_zeros_muon_neutrino_chemical_potential(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/"zero.csv"
            write_scaled_profile(DEFAULT_PROFILE,out,0.0)
            original=self.read_rows(DEFAULT_PROFILE)
            copied=self.read_rows(out)
            for a,b in zip(original,copied):
                self.assertEqual(float(b["mu_numu_MeV"]),0.0)
                for key in a:
                    if key!="mu_numu_MeV":
                        self.assert_float_same(a[key],b[key])


if __name__=="__main__":
    unittest.main(verbosity=2)
