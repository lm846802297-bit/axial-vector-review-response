import unittest
from off_shell_cascades import off_shell_aprime_three_body_width, aprime_decay_widths


class OffShellCascadeTests(unittest.TestCase):
    def test_no_double_count_when_on_shell_pair_open(self):
        r=off_shell_aprime_three_body_width(4.0,1.9,0.1)
        self.assertEqual(r["total"],0.0)
        self.assertIn("do_not_add_three_body",r["status"])

    def test_both_virtual_four_body_region_is_flagged(self):
        r=off_shell_aprime_three_body_width(4.0,4.0,0.1)
        self.assertEqual(r["total"],0.0)
        self.assertIn("four_body_modes_not_included",r["status"])

    def test_one_on_shell_one_virtual_three_body_is_positive(self):
        r=off_shell_aprime_three_body_width(4.0,2.1,0.1)
        self.assertGreater(r["nu_nu"],0.0)
        self.assertGreater(r["mu_mu"],0.0)
        self.assertEqual(r["tau_tau"],0.0)
        self.assertAlmostEqual(r["total"],r["nu_nu"]+r["mu_mu"]+r["tau_tau"],places=18)

    def test_tau_virtual_channel_opens_when_available(self):
        r=off_shell_aprime_three_body_width(10.0,5.1,0.1)
        self.assertGreater(r["tau_tau"],0.0)

    def test_finite_at_exact_two_body_threshold_with_running_width(self):
        r=off_shell_aprime_three_body_width(4.0,2.0,0.1,quadrature_order=512)
        self.assertGreater(r["total"],0.0)

    def test_on_shell_Aprime_below_dimuon_threshold_is_invisible(self):
        r=aprime_decay_widths(0.1,0.1)
        self.assertEqual(r["branching_fractions"]["mu_mu"],0.0)
        self.assertEqual(r["branching_fractions"]["tau_tau"],0.0)
        self.assertAlmostEqual(r["branching_fractions"]["nu_nu"],1.0)

    def test_on_shell_Aprime_muon_and_tau_thresholds(self):
        below_tau=aprime_decay_widths(1.8,0.1)
        above_tau=aprime_decay_widths(4.0,0.1)
        self.assertGreater(below_tau["branching_fractions"]["mu_mu"],0.0)
        self.assertEqual(below_tau["branching_fractions"]["tau_tau"],0.0)
        self.assertGreater(above_tau["branching_fractions"]["tau_tau"],0.0)

    def test_on_shell_Aprime_width_scales_as_gX_squared(self):
        a=aprime_decay_widths(1.8,0.01)["total_width_GeV"]
        b=aprime_decay_widths(1.8,0.1)["total_width_GeV"]
        self.assertAlmostEqual(b/a,100.0,places=10)

    def test_far_off_shell_three_body_scales_as_gX_fourth_power(self):
        a=off_shell_aprime_three_body_width(4.0,2.1,0.001)["total"]
        b=off_shell_aprime_three_body_width(4.0,2.1,0.01)["total"]
        self.assertAlmostEqual(b/a,1.0e4,delta=2.0)


if __name__=="__main__":
    unittest.main()
