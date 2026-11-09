import unittest

from belleii_resolution_promptness import (
    aprime_beta_gamma_lab_max,
    fourmu_sigma_MR_envelope_GeV,
    fourmu_width_resolution_ratios,
    scalar_beta_gamma_lab_max,
    tau_sigma_recoil_envelope_GeV,
    tau_width_resolution_ratios,
)


class BelleIIPromptnessTests(unittest.TestCase):
    def test_scalar_kinematic_lab_boost_is_finite(self):
        self.assertGreater(scalar_beta_gamma_lab_max(0.212), 1.0)
        self.assertGreater(scalar_beta_gamma_lab_max(6.6), 0.0)

    def test_aprime_boost_only_when_on_shell_channel_is_open(self):
        self.assertIsNone(aprime_beta_gamma_lab_max(4.0, 4.0))
        self.assertGreater(aprime_beta_gamma_lab_max(4.0, 0.5), 0.0)
        self.assertGreater(aprime_beta_gamma_lab_max(4.0, 2.1), 0.0)

    def test_fourmu_resolution_uses_reduced_mass(self):
        sig = fourmu_sigma_MR_envelope_GeV(0.212)
        self.assertEqual(sig, (0.002, 0.0025))
        r = fourmu_width_resolution_ratios(0.212, 1e-6)
        self.assertGreater(r["Gamma_MR_GeV"], 1e-6)

    def test_tau_resolution_anchors(self):
        self.assertEqual(tau_sigma_recoil_envelope_GeV(3.6), (0.010, 0.030))
        self.assertEqual(tau_sigma_recoil_envelope_GeV(6.6), (0.010, 0.010))
        self.assertEqual(tau_sigma_recoil_envelope_GeV(10.0), (0.001, 0.010))
        r = tau_width_resolution_ratios(6.6, 1e-3)
        self.assertAlmostEqual(r["Gamma_over_sigma_lower_resolution"], 0.1)

    def test_outside_published_mass_ranges_has_no_resolution(self):
        self.assertIsNone(fourmu_sigma_MR_envelope_GeV(9.1))
        self.assertIsNone(fourmu_width_resolution_ratios(9.1, 1e-6))
        self.assertIsNone(tau_sigma_recoil_envelope_GeV(3.5))


if __name__ == "__main__":
    unittest.main()
