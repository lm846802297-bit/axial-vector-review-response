import unittest
import numpy as np
import rates
from finite_mixing.response_scan import compton_scan,dimuon_scan
class ResponseScanTests(unittest.TestCase):
 def test_compton_grid_and_modes(self):
  r=compton_scan(); self.assertEqual(len(r["differential"]),25); self.assertEqual(len(r["angular_integrated"]),25)
  for row in r["angular_integrated"]:
   self.assertEqual(set(row["integrated_ratio_A_over_V_by_mode"]),{"L","+","-"})
   self.assertTrue(np.isfinite(row["integrated_ratio_polarization_sum"])); self.assertGreater(row["integrated_ratio_polarization_sum"],0)
 def test_compton_ratio_not_constant(self):
  vals=[x["integrated_ratio_polarization_sum"] for x in compton_scan()["angular_integrated"]]
  self.assertGreater(max(vals)/min(vals),1.01)
 def test_finite_mixing_compton_and_raw_angle_data(self):
  result=compton_scan()
  self.assertEqual(len(result["finite_mixing_integrated"]),25)
  for row in result["differential"]:
   self.assertEqual(len(row["cosines"]),19)
   for mode in ("L","+","-"):
    self.assertEqual(len(row["differential_ratio_A_over_V_raw_by_mode"][mode]),19)
    self.assertEqual(len(row["mixed_interference_fraction_raw_by_mode"][mode]),19)
  for row in result["finite_mixing_integrated"]:
   self.assertEqual(set(row["mixed_over_vector_by_mode"]),{"L","+","-"})
   self.assertTrue(np.isfinite(row["mixed_over_vector_polarization_sum"]))
 def test_interference_retained(self):
  rows=compton_scan()["differential"]; vals=[abs(x["max"]) for r in rows for x in r["mixed_interference_fraction_by_mode"].values() if x["max"] is not None]
  self.assertTrue(vals); self.assertGreater(max(vals),0)
 def test_dimuon_threshold_scan(self):
  rows=dimuon_scan()["rows"]; self.assertEqual(len(rows),9)
  self.assertLess(rows[0]["vacuum_width_ratio_A_over_V"],1e-3); self.assertGreater(rows[-1]["vacuum_width_ratio_A_over_V"],rows[0]["vacuum_width_ratio_A_over_V"])
  for row in rows:
   self.assertEqual(set(row["thermal_production_ratio_A_over_V_by_mode"]),{"L","+","-"})
   self.assertEqual(set(row["thermal_absorption_ratio_A_over_V_by_mode"]),{"L","+","-"})
   self.assertEqual(set(row["finite_mixing_production_over_vector_by_mode"]),{"L","+","-"})
   self.assertEqual(set(row["finite_mixing_absorption_over_vector_by_mode"]),{"L","+","-"})
   self.assertEqual(set(row["interference_fraction_in_production_by_mode"]),{"L","+","-"})
   self.assertEqual(set(row["interference_fraction_in_absorption_by_mode"]),{"L","+","-"})
 def test_width_formula(self):
  for row in dimuon_scan()["rows"]:
   m=row["mass_MeV"]; beta=np.sqrt(1-(2*rates.M_MU/m)**2)
   self.assertAlmostEqual(row["vacuum_width_ratio_A_over_V"],beta**2/(1+2*rates.M_MU**2/m**2),places=13)
if __name__=="__main__":unittest.main(verbosity=2)
