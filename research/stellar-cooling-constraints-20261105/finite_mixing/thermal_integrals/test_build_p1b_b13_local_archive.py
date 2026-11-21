from __future__ import annotations
import csv,json,os,pathlib,unittest
OUT=pathlib.Path(os.environ["P1B_ARCHIVE_DIR"])
class TestP1BLocalArchive(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.m=json.loads((OUT/"MANIFEST.json").read_text())
  with (OUT/"p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.csv").open(newline="") as f: cls.rows=list(csv.DictReader(f))
 def test_counts(self):
  self.assertEqual((self.m["grid_nodes"],self.m["cell_midpoints"],len(self.rows)),(513,468,5886))
  groups={(r["point_type"],r["radius_km"],r["omega_local_MeV"]) for r in self.rows}
  self.assertEqual(len(groups),981)
  self.assertTrue(all(sum(1 for x in self.rows if (x["point_type"],x["radius_km"],x["omega_local_MeV"])==g)==6 for g in groups))
 def test_charges_modes_and_closures(self):
  self.assertEqual({r["charge"] for r in self.rows},{"mu_minus","mu_plus"});self.assertEqual({r["mode"] for r in self.rows},{"L","+","-"})
  for r in self.rows:
   for k in ("production_MeV","absorption_MeV","reduced_absorption_MeV","spectral_source_MeV5"):self.assertGreaterEqual(float(r[k]),0)
   self.assertLessEqual(float(r["detailed_balance_relative_residual"]),2e-10);self.assertLessEqual(float(r["final_muon_shell_relative_error"]),2e-10)
 def test_failed_acceptance_preserved(self):
  a=self.m["acceptance"];self.assertEqual(self.m["status"],"ARCHIVED_EVIDENCE_ONLY_NUMERICAL_ACCEPTANCE_FAILED")
  self.assertFalse(a["overall_p1b_pass"]);self.assertFalse(a["quadrature_pass"]);self.assertFalse(a["interpolation_pass"])
  self.assertGreater(a["maximum_grid_node_final_refinement_change"],a["quadrature_relative_tolerance"])
  self.assertGreater(a["maximum_direct_midpoint_vs_sequential_log_interpolation_error"],a["interpolation_relative_tolerance"])
 def test_visuals_and_manifest(self):
  for n in ("README.md","grid_node_quadrature_refinement.svg","cell_midpoint_interpolation_error.svg"):self.assertGreater((OUT/n).stat().st_size,1000)
  self.assertEqual(self.m["profile_sha256"],"9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c")
  self.assertEqual(self.m["source_run_id"],43376779901);self.assertEqual(self.m["source_artifact_id"],14015517843)
if __name__=="__main__":unittest.main(verbosity=2)
