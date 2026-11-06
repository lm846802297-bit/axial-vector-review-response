import csv
import tempfile
import unittest
from pathlib import Path

import numpy as np

try:
    from .diagnose_fig7_10mev_numu import read_profile, write_scaled_profile
except ImportError:  # direct unittest discovery with this directory as top-level
    from diagnose_fig7_10mev_numu import read_profile, write_scaled_profile


class Fig7MuonNeutrinoSensitivityTests(unittest.TestCase):
    def test_scale_changes_only_muon_neutrino_chemical_potential(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.csv"
            target = Path(temp) / "scaled.csv"
            source.write_text(
                "r_km,T_MeV,mu_mu_MeV,mu_numu_MeV,lapse\n"
                "0,20,45,-50,0.7\n"
                "5,25,55,-30,0.8\n",
                encoding="utf-8",
            )
            write_scaled_profile(source, target, 0.5)
            header0, original = read_profile(source)
            header1, scaled = read_profile(target)
            self.assertEqual(header0, header1)
            col = header0.index("mu_numu_MeV")
            np.testing.assert_allclose(scaled[:, col], 0.5 * original[:, col])
            keep = [i for i in range(len(header0)) if i != col]
            np.testing.assert_allclose(scaled[:, keep], original[:, keep])

    def test_zero_scale_sets_only_muon_neutrino_chemical_potential_to_zero(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.csv"
            target = Path(temp) / "scaled.csv"
            source.write_text(
                "r_km,T_MeV,mu_mu_MeV,mu_numu_MeV,lapse\n"
                "0,20,45,-50,0.7\n",
                encoding="utf-8",
            )
            write_scaled_profile(source, target, 0.0)
            header, rows = read_profile(target)
            self.assertTrue(np.all(rows[:, header.index("mu_numu_MeV")] == 0.0))
            self.assertEqual(rows[0, header.index("T_MeV")], 20.0)
            self.assertEqual(rows[0, header.index("mu_mu_MeV")], 45.0)

    def test_negative_scale_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.csv"
            target = Path(temp) / "scaled.csv"
            source.write_text(
                "r_km,T_MeV,mu_mu_MeV,mu_numu_MeV,lapse\n"
                "0,20,45,-50,0.7\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                write_scaled_profile(source, target, -1.0)


if __name__ == "__main__":
    unittest.main()
