import unittest

from belleii_resolution_promptness import (
    aprime_beta_gamma_lab_max,
    fourmu_sigma_MR_envelope_GeV,
    fourmu_width_resolution_ratios,
    scalar_beta_gamma_lab_max,
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

    def test_fourmu_outside_published_mass_range_has_no_resolution(self):
        self.assertIsNone(fourmu_sigma_MR_envelope_GeV(9.1))
        self.assertIsNone(fourmu_width_resolution_ratios(9.1, 1e-6))


if __name__ == "__main__":
    unittest.main()
