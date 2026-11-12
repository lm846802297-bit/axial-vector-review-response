import math
import unittest

from radial_scalar_widths import (
    M_MU_GEV, M_TAU_GEV, evaluate_point, fermion_pair_width,
    leptophilic_scalar_xi_from_vs, photon_pair_width_lepton_loops,
    rescale_coupling_limit_for_branching_fraction, vector_pair_width,
)


class RadialScalarWidthsTests(unittest.TestCase):
    def test_fermion_threshold_and_formula(self):
        self.assertEqual(fermion_pair_width(2*M_MU_GEV, 0.1, M_MU_GEV), 0.0)
        ms, y, mf = 1.0, 0.02, M_MU_GEV
        expected = y*y*ms/(8*math.pi)*(1-4*mf*mf/ms**2)**1.5
        self.assertAlmostEqual(fermion_pair_width(ms,y,mf),expected,places=15)

    def test_tau_threshold(self):
        self.assertEqual(fermion_pair_width(2*M_TAU_GEV,0.2,M_TAU_GEV),0.0)
        self.assertGreater(fermion_pair_width(3.6,0.2,M_TAU_GEV),0.0)

    def test_vector_pair_threshold_and_original_normalization(self):
        self.assertEqual(vector_pair_width(1.0,0.5,2.0),0.0)
        ms,mA,vs=4.0,0.5,2.0
        r=(mA/ms)**2
        expected=ms**3/(32*math.pi*vs**2)*math.sqrt(1-4*r)*(1-4*r+12*r*r)
        self.assertAlmostEqual(vector_pair_width(ms,mA,vs),expected,places=15)

    def test_gamma_gamma_loop_width_is_finite_and_positive(self):
        for ms in (0.212,0.3,1.0,3.6,10.0):
            width=photon_pair_width_lepton_loops(ms,100.0)
            self.assertTrue(math.isfinite(width))
            self.assertGreater(width,0.0)

    def test_gamma_gamma_near_muon_threshold_is_small_but_nonzero(self):
        ms=0.212; vs=1.0
        gg=photon_pair_width_lepton_loops(ms,vs)
        mm=fermion_pair_width(ms,M_MU_GEV/vs,M_MU_GEV)
        self.assertGreater(gg,0.0)
        self.assertLess(gg/mm,0.02)

    def test_vev_lambda_and_yukawa_relations(self):
        point=evaluate_point(1.0,0.2,0.1)
        self.assertAlmostEqual(point["vs_GeV"],1.0)
        self.assertAlmostEqual(point["lambdaS"],0.5)
        self.assertAlmostEqual(point["y_smu"],M_MU_GEV)
        self.assertAlmostEqual(point["y_stau"],M_TAU_GEV)

    def test_branching_fractions_are_gX_independent(self):
        a=evaluate_point(4.0,0.5,1e-3)
        b=evaluate_point(4.0,0.5,1e-2)
        for channel in a["fractions_among_included_channels"]:
            self.assertAlmostEqual(a["fractions_among_included_channels"][channel],
                                   b["fractions_among_included_channels"][channel],places=13)

    def test_all_included_widths_scale_as_gX_squared(self):
        a=evaluate_point(4.0,0.5,1e-3)
        b=evaluate_point(4.0,0.5,1e-2)
        self.assertAlmostEqual(b["sum_of_included_widths_GeV"]/a["sum_of_included_widths_GeV"],100.0,places=10)

    def test_fractions_are_not_claimed_complete_by_default(self):
        point=evaluate_point(4.0,0.5,0.1)
        self.assertAlmostEqual(sum(point["fractions_among_included_channels"].values()),1.0)
        self.assertFalse(point["branching_fractions_complete"])
        self.assertIsNone(point["ctau_m"])
        self.assertIsNotNone(point["ctau_upper_bound_from_included_widths_m"])
        self.assertFalse(point["off_shell_AAprime_channels_included"])

    def test_negative_additional_width_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_point(1.0,0.5,0.1,additional_widths_GeV={"bad":-1.0})

    def test_lifetime_only_asserted_complete_on_explicit_flag(self):
        point=evaluate_point(1.0,0.6,0.1,all_channels_included=True)
        self.assertTrue(point["branching_fractions_complete"])
        self.assertGreater(point["ctau_m"],0.0)

    def test_belle_ii_xi_normalization(self):
        self.assertAlmostEqual(leptophilic_scalar_xi_from_vs(246.0),1.0)
        self.assertAlmostEqual(leptophilic_scalar_xi_from_vs(123.0),2.0)
        with self.assertRaises(ValueError):
            leptophilic_scalar_xi_from_vs(0.0)

    def test_branching_fraction_limit_rescaling(self):
        result=rescale_coupling_limit_for_branching_fraction(0.01,1.0,0.5)
        self.assertAlmostEqual(result,0.01*math.sqrt(2),places=14)
        with self.assertRaises(ValueError):
            rescale_coupling_limit_for_branching_fraction(0.01,1.1,0.5)

    def test_tau_threshold_changes_branching_fractions(self):
        near=evaluate_point(3.6,10.0,0.1)
        above=evaluate_point(4.0,10.0,0.1)
        br36=near["fractions_among_included_channels"]["tau_tau"]
        br40=above["fractions_among_included_channels"]["tau_tau"]
        self.assertAlmostEqual(br36,0.537,places=2)
        self.assertAlmostEqual(br40,0.965,places=2)
        self.assertGreater(br40,br36)

    def test_open_AAprime_can_dominate(self):
        point=evaluate_point(4.0,0.5,0.1)
        widths=point["partial_widths_GeV"]
        self.assertGreater(widths["Aprime_Aprime"],widths["tau_tau"])


if __name__ == "__main__":
    unittest.main()
