import unittest

from audit_croon_outer_muon_opacity_envelope import (
    DEFAULT_PROFILE,
    run_outer_muon_opacity_envelope,
)


class CroonOuterMuonOpacityEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_outer_muon_opacity_envelope(
            profile_path=DEFAULT_PROFILE,
            couplings=[3.0e-6, 3.0e-2],
            energy_order=64,
            tau_grid_points=301,
            susceptibility_order=128,
        )

    def test_uses_current_vertex_preserving_profile_b(self):
        self.assertEqual(
            self.result["profile"]["sha256"],
            "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c",
        )
        self.assertEqual(self.result["profile"]["rows"], 1687)
        self.assertAlmostEqual(self.result["profile"]["R_nu_km"], 25.1511682816, places=8)

    def test_resolved_edge_susceptibility_is_reproduced(self):
        edge = self.result["profile"]["last_resolved_muon_sample"]
        self.assertAlmostEqual(edge["r_km"], 22.1918936570, places=8)
        self.assertAlmostEqual(edge["T_MeV"], 3.5152434568, places=8)
        self.assertAlmostEqual(edge["mu_mu_MeV"], 0.9999998342, places=8)
        self.assertAlmostEqual(edge["chi_mu_MeV3"], 1.13518337e-10, delta=2e-16)

    def test_source_weighted_outer_envelopes_suppress_but_do_not_close_fig2_gap(self):
        low, high = self.result["luminosity_comparison"]
        self.assertGreater(low["vacuum_over_T3_envelope_luminosity_ratio"], 1.0)
        self.assertGreater(high["vacuum_over_T3_envelope_luminosity_ratio"], 1.015)
        self.assertLess(high["vacuum_over_T3_envelope_luminosity_ratio"], 1.020)
        self.assertGreater(
            high["vacuum_over_Tedge_envelope_luminosity_ratio"],
            high["vacuum_over_T3_envelope_luminosity_ratio"],
        )
        self.assertLess(high["vacuum_over_Tedge_envelope_luminosity_ratio"], 1.025)
        self.assertGreater(
            self.result["paper_reference"]["median_solid_over_dashed_luminosity_ratio"],
            3.0,
        )

    def test_constant_outer_susceptibility_equivalent_is_not_the_edge_profile(self):
        low, high = self.result["effective_constant_outer_susceptibility"]
        self.assertAlmostEqual(low["achieved_ratio"], 3.38190, places=9)
        self.assertAlmostEqual(high["achieved_ratio"], 3.38190, places=9)
        self.assertGreater(low["chi_required_MeV3"], 0.5)
        self.assertGreater(high["chi_required_MeV3"], 6.0e-9)
        self.assertLess(high["chi_required_MeV3"], 1.0e-8)
        self.assertGreater(low["chi_required_MeV3"] / high["chi_required_MeV3"], 1.0e7)
        self.assertGreater(high["chi_required_over_resolved_edge"], 50.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
