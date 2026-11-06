import tempfile
import unittest
from pathlib import Path
import numpy as np
from diagnose_muon_profile_sensitivity import contour_crossings, write_ferreira_mu_profile


class MuonProfileSensitivityTests(unittest.TestCase):
    def test_alternate_profile_changes_only_muon_chemical_potential(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp)/"source.csv", Path(tmp)/"alternate.csv"
            src.write_text(
                "r_km,T_MeV,mu_mu_MeV,mu_numu_MeV,lapse,mu_mu_Ferreira_MeV\n"
                "0,20,40,-10,0.7,150\n1,15,20,-5,0.8,\n", encoding="utf-8")
            meta = write_ferreira_mu_profile(src, dst)
            data = np.genfromtxt(dst, delimiter=",", names=True)
            np.testing.assert_allclose(data["T_MeV"], [20, 15])
            np.testing.assert_allclose(data["mu_numu_MeV"], [-10, -5])
            np.testing.assert_allclose(data["lapse"], [0.7, 0.8])
            np.testing.assert_allclose(data["mu_mu_MeV"], [150, 0])
            self.assertIn("mu_mu_Ferreira_MeV", meta["changed_column"])

    def test_log_log_contour_crossings(self):
        points = [
            {"g": 1., "calculated_luminosity_erg_s": 1e52},
            {"g": 10., "calculated_luminosity_erg_s": 1e54},
            {"g": 100., "calculated_luminosity_erg_s": 1e52},
        ]
        np.testing.assert_allclose(
            contour_crossings(points, 1e53), [np.sqrt(10), np.sqrt(1000)],
            rtol=1e-12, atol=1e-12)

    def test_no_crossing(self):
        points = [
            {"g": 1., "calculated_luminosity_erg_s": 1e54},
            {"g": 10., "calculated_luminosity_erg_s": 2e54},
        ]
        self.assertEqual(contour_crossings(points, 1e52), [])


if __name__ == "__main__":
    unittest.main()
