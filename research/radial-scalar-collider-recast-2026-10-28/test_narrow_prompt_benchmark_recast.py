import gzip
import tempfile
import unittest
from pathlib import Path

import numpy as np

from narrow_prompt_benchmark_recast import (
    _open_scan,
    evaluate_row,
    tau_reference_branching_fraction,
)


def limits(obs, exp=None):
    if exp is None:
        exp = obs
    x = np.array([0.2, 10.0])
    return ((x, np.array([obs, obs])), (x, np.array([exp, exp])))


def scan_row(**overrides):
    row = {
        "ms_GeV": "1.0",
        "mA_GeV": "2.0",
        "gX": "0.01",
        "vs_GeV": "100.0",
        "lambdaS": "0.005",
        "passes_lambdaS_le_4pi": "True",
        "passes_scalar_yukawas_le_sqrt4pi": "True",
        "y_smu": "0.01",
        "y_stau": "0.17",
        "width_regime": "two_virtual_A_four_body_bounded",
        "branching_fractions_bounded_under_declared_benchmark": "True",
        "branching_fractions_exact_under_declared_benchmark": "False",
        "BR_mu_mu_min": "0.70",
        "BR_mu_mu_max": "0.90",
        "BR_tau_tau_min": "0.70",
        "BR_tau_tau_max": "0.90",
        "fourmu_Gamma_over_sigma_lower_bound": "0.02",
        "fourmu_Gamma_over_sigma_upper_bound": "0.04",
        "tau_Gamma_over_sigma_lower_bound": "0.02",
        "tau_Gamma_over_sigma_upper_bound": "0.04",
        "scalar_mean_lab_flight_max_lower_m": "0.0001",
        "scalar_mean_lab_flight_max_upper_m": "0.0002",
    }
    row.update({k: str(v) for k, v in overrides.items()})
    return row


class BoundedWidthRecastTests(unittest.TestCase):
    def test_fourmu_exclusion_uses_conservative_minimum_branching_fraction(self):
        row = scan_row(y_smu="0.02", BR_mu_mu_min="0.60", BR_mu_mu_max="0.90")
        out = evaluate_row(row, "fourmu", limits(0.01))
        self.assertEqual(out["classification"],
                         "excluded_under_published_narrow_prompt_benchmark_conditional")
        self.assertAlmostEqual(out["signal_strength_ratio_observed_min"], 2.4)
        self.assertAlmostEqual(out["signal_strength_ratio_observed_max"], 3.6)

    def test_branching_interval_straddling_limit_is_not_called_excluded(self):
        row = scan_row(y_smu=str(0.01 * np.sqrt(1.25)),
                       BR_mu_mu_min="0.70", BR_mu_mu_max="0.90")
        out = evaluate_row(row, "fourmu", limits(0.01))
        self.assertEqual(out["classification"],
                         "unclassified_branching_interval_straddles_observed_limit")
        self.assertLess(out["signal_strength_ratio_observed_min"], 1.0)
        self.assertGreater(out["signal_strength_ratio_observed_max"], 1.0)

    def test_upper_width_bound_controls_narrow_proxy(self):
        row = scan_row(fourmu_Gamma_over_sigma_lower_bound="0.02",
                       fourmu_Gamma_over_sigma_upper_bound="0.15")
        out = evaluate_row(row, "fourmu", limits(0.01))
        self.assertEqual(out["classification"],
                         "width_interval_straddles_narrow_threshold")

    def test_flight_interval_controls_prompt_proxy(self):
        row = scan_row(scalar_mean_lab_flight_max_lower_m="0.001",
                       scalar_mean_lab_flight_max_upper_m="0.008")
        out = evaluate_row(row, "fourmu", limits(0.01))
        self.assertEqual(out["classification"],
                         "flight_interval_straddles_5mm_proxy")

    def test_nonperturbative_scalar_yukawa_is_not_experimentally_classified(self):
        row = scan_row(passes_scalar_yukawas_le_sqrt4pi="False")
        out = evaluate_row(row, "fourmu", limits(0.01))
        self.assertEqual(out["classification"],
                         "theoretically_inconsistent_scalar_yukawa")

    def test_tau_reference_branching_fraction_includes_e_mu_tau(self):
        br = tau_reference_branching_fraction(4.0)
        self.assertGreater(br, 0.0)
        self.assertLess(br, 1.0)
        self.assertAlmostEqual(br, 0.9649, places=3)

    def test_gzip_scan_reader(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scan.csv.gz"
            with gzip.open(path, "wt", encoding="utf-8") as f:
                f.write("ms_GeV\n1.0\n")
            with _open_scan(path) as f:
                self.assertEqual(f.read(), "ms_GeV\n1.0\n")


if __name__ == "__main__":
    unittest.main()
