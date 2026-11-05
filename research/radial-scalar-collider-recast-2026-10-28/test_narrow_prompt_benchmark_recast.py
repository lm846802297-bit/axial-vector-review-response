import unittest

import narrow_prompt_benchmark_recast as recast


class NarrowPromptRecastTests(unittest.TestCase):
    def test_tau_reference_branching_fraction_threshold(self):
        self.assertAlmostEqual(recast.tau_reference_branching_fraction(3.6), 0.5372, places=4)

    def test_tau_reference_electron_effect_is_tiny(self):
        mass = 6.6
        br_ref = recast.tau_reference_branching_fraction(mass)
        weights_uv = [
            recast._partial_weight(mass, recast.M_MU_GEV),
            recast._partial_weight(mass, recast.M_TAU_GEV),
        ]
        br_uv = weights_uv[1] / sum(weights_uv)
        self.assertLess(abs(br_ref / br_uv - 1.0), 1.2e-5)

    def test_fourmu_benchmark_coupling_mapping(self):
        row = {
            "ms_GeV": "1.0", "mA_GeV": "2.0", "gX": "0.01", "vs_GeV": "100",
            "lambdaS": "0.00005", "passes_lambdaS_le_4pi": "True",
            "width_regime": "two_body", "branching_fractions_complete": "True",
            "Gamma_s_included_GeV": "1e-8", "ctau_s_from_included_widths_m": "1e-8",
            "fraction_mu_mu": "0.5", "fraction_tau_tau": "0",
            "y_smu": str(recast.M_MU_GEV / 100),
        }
        limits = (([0.2, 2.0], [0.001, 0.002]), ([0.2, 2.0], [0.001, 0.002]))
        result = recast.evaluate_row(row, "fourmu", limits)
        limit = recast._log_interp(1.0, [0.2, 2.0], [0.001, 0.002])
        expected = (recast.M_MU_GEV / 100 / limit)**2 * 0.5
        self.assertAlmostEqual(result["signal_strength_ratio_observed"], expected, places=8)
        self.assertAlmostEqual(
            result["UV_coupling_limit_observed_BR_corrected"],
            limit / (0.5**0.5), places=8
        )

    def test_tau_reference_branching_fraction_enters_mapping(self):
        row = {
            "ms_GeV": "4.0", "mA_GeV": "5.0", "gX": "0.01", "vs_GeV": "100",
            "lambdaS": "0.0032", "passes_lambdaS_le_4pi": "True",
            "width_regime": "two_body", "branching_fractions_complete": "True",
            "Gamma_s_included_GeV": "1e-8", "ctau_s_from_included_widths_m": "1e-8",
            "fraction_mu_mu": "0.02", "fraction_tau_tau": "0.98",
            "y_smu": str(recast.M_MU_GEV / 100),
        }
        limits = (([3.6, 10.0], [100.0, 200.0]), ([3.6, 10.0], [100.0, 200.0]))
        result = recast.evaluate_row(row, "tautau", limits)
        self.assertAlmostEqual(
            result["BR_benchmark_signal"],
            recast.tau_reference_branching_fraction(4.0)
        )
        xi_lim = recast._log_interp(4.0, [3.6, 10.0], [100.0, 200.0])
        expected = (2.46 / xi_lim)**2 * 0.98 / result["BR_benchmark_signal"]
        self.assertAlmostEqual(result["signal_strength_ratio_observed"], expected, places=8)

    def test_incomplete_double_virtual_width_is_unclassified(self):
        row = {
            "ms_GeV": "4.0", "mA_GeV": "5.0", "gX": "0.01", "vs_GeV": "250",
            "lambdaS": "0.000512", "passes_lambdaS_le_4pi": "True",
            "width_regime": "two_virtual_A_four_body_missing",
            "branching_fractions_complete": "False",
            "Gamma_s_included_GeV": "1e-8", "ctau_s_from_included_widths_m": "1e-8",
            "fraction_mu_mu": "0.5", "fraction_tau_tau": "0.5",
            "y_smu": str(recast.M_MU_GEV / 250),
        }
        limits = (([0.2, 9.0], [0.001, 0.01]), ([0.2, 9.0], [0.001, 0.01]))
        self.assertEqual(
            recast.evaluate_row(row, "fourmu", limits)["classification"],
            "unclassified_incomplete_width_sum"
        )

    def test_fourmu_jpsi_veto(self):
        row = {
            "ms_GeV": "3.1", "mA_GeV": "5.0", "gX": "0.01", "vs_GeV": "250",
            "lambdaS": "0.000512", "passes_lambdaS_le_4pi": "True",
            "width_regime": "two_body", "branching_fractions_complete": "True",
            "Gamma_s_included_GeV": "1e-8", "ctau_s_from_included_widths_m": "1e-8",
            "fraction_mu_mu": "0.5", "fraction_tau_tau": "0.5",
            "y_smu": str(recast.M_MU_GEV / 250),
        }
        limits = (([0.2, 9.0], [0.001, 0.01]), ([0.2, 9.0], [0.001, 0.01]))
        self.assertEqual(
            recast.evaluate_row(row, "fourmu", limits)["classification"],
            "unclassified_experimental_Jpsi_veto"
        )

    def test_no_extrapolation_beyond_limit_grid(self):
        row = {
            "ms_GeV": "10.0", "mA_GeV": "20.0", "gX": "0.01", "vs_GeV": "1000",
            "lambdaS": "0.0002", "passes_lambdaS_le_4pi": "True",
            "width_regime": "two_body", "branching_fractions_complete": "True",
            "Gamma_s_included_GeV": "1e-8", "ctau_s_from_included_widths_m": "1e-8",
            "fraction_mu_mu": "0.01", "fraction_tau_tau": "0.99",
            "y_smu": str(recast.M_MU_GEV / 1000),
        }
        limits = (([3.6, 9.99943], [50.0, 200.0]), ([3.6, 9.99943], [50.0, 200.0]))
        self.assertEqual(
            recast.evaluate_row(row, "tautau", limits)["classification"],
            "unclassified_outside_numerical_limit_grid"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
