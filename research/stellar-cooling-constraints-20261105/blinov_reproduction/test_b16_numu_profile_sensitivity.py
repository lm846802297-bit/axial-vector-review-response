import sys
import tempfile
import unittest
from pathlib import Path
import csv

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))

from blinov_reproduction.audit_b16_numu_profile_sensitivity import write_scaled_profile
from blinov_reproduction.reference import DEFAULT_PROFILE


class B16NumuProfileSensitivityTests(unittest.TestCase):
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
                    self.assertAlmostEqual(float(a[key]),float(b[key]),places=10)

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
                        self.assertAlmostEqual(float(a[key]),float(b[key]),places=10)


if __name__=="__main__":
    unittest.main(verbosity=2)
