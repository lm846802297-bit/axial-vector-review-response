"""Regression tests for the 10 MeV local polarization sample package."""
from __future__ import annotations

import json
import math
import unittest
from pathlib import Path

import numpy as np

import audit_b16_local_rate_polarization_samples as samples
import audit_b16_local_absorption as local

HERE = Path(__file__).resolve().parent
PROFILE = HERE.parent / "data" / "sfho188_digitized.csv"
LEGACY_LOCAL_JSON = HERE / "outputs" / "b16_local_absorption_vertex_preserving_10mev_2026-11-09.json"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"

# Anchors from the supplied 54-point reference table. They cover the inner
# source, the 12 km shell, the 15 km edge, and the high-energy outer tail.
REFERENCE_SAMPLES = {
    (8.0, 12.0): {
        "n_mu_minus_MeV3": 35810.87760782956,
        "n_mu_plus_MeV3": 369.86064998810974,
        "nu_mu_prod_L_MeV_per_g2": 0.0219833297731016,
        "nu_mu_prod_plus_MeV_per_g2": 0.0217373087017323,
        "nu_mu_prod_minus_MeV_per_g2": 0.0222165559488136,
        "nu_tau_prod_L_MeV_per_g2": 0.0235274841973123,
        "compton_prod_scalar_MeV_per_g2": 0.1012242961781512,
        "compton_w_L": 0.2577319587628866,
        "compton_w_plus": 0.3711340206185566,
        "total_prod_L_MeV_per_g2": 0.0715995500988034,
        "total_prod_plus_MeV_per_g2": 0.082824054855224,
        "total_prod_minus_MeV_per_g2": 0.0833033021023053,
    },
    (12.0, 30.0): {
        "n_mu_minus_MeV3": 14934.282807386817,
        "n_mu_plus_MeV3": 12.791320980597906,
        "nu_mu_prod_L_MeV_per_g2": 0.005604464514791,
        "nu_mu_prod_plus_MeV_per_g2": 0.0054189692131822,
        "nu_mu_prod_minus_MeV_per_g2": 0.0056431453224701,
        "nu_tau_prod_L_MeV_per_g2": 0.0056387886963789,
        "compton_prod_scalar_MeV_per_g2": 0.0055118801893726,
        "compton_w_L": 0.0526315789473684,
        "compton_w_plus": 0.4736842105263157,
        "total_prod_L_MeV_per_g2": 0.0115333521685053,
        "total_prod_plus_MeV_per_g2": 0.013593495817048,
        "total_prod_minus_MeV_per_g2": 0.0138176719263359,
    },
    (15.0, 100.0): {
        "n_mu_minus_MeV3": 308.3814828262899,
        "n_mu_plus_MeV3": 0.0254454070179342,
        "nu_mu_prod_L_MeV_per_g2": 6.082922734989068e-06,
        "nu_mu_prod_plus_MeV_per_g2": 5.461506282538999e-06,
        "nu_mu_prod_minus_MeV_per_g2": 5.461506282538998e-06,
        "nu_tau_prod_L_MeV_per_g2": 6.082922734989068e-06,
        "compton_prod_scalar_MeV_per_g2": 1.394403061128045e-07,
        "compton_w_L": 0.0049751243781094,
        "compton_w_plus": 0.4975124378109453,
        "total_prod_L_MeV_per_g2": 1.2166539202844368e-05,
        "total_prod_plus_MeV_per_g2": 1.0992385851701284e-05,
        "total_prod_minus_MeV_per_g2": 1.0992385851701282e-05,
    },
    (20.0, 200.0): {
        "n_mu_minus_MeV3": 5.233673683499569e-07,
        "n_mu_plus_MeV3": 4.6471634967205344e-10,
        "nu_mu_prod_L_MeV_per_g2": 1.4484550065564452e-23,
        "nu_mu_prod_plus_MeV_per_g2": 1.3950285975562337e-23,
        "nu_mu_prod_minus_MeV_per_g2": 1.3950285975562334e-23,
        "nu_tau_prod_L_MeV_per_g2": 1.4484550065564452e-23,
        "compton_prod_scalar_MeV_per_g2": 1.0016401261144452e-33,
        "compton_w_L": 0.0012484394506866,
        "compton_w_plus": 0.4993757802746567,
        "total_prod_L_MeV_per_g2": 2.8969100131130155e-23,
        "total_prod_plus_MeV_per_g2": 2.790057195162487e-23,
        "total_prod_minus_MeV_per_g2": 2.7900571951624864e-23,
    },
    (22.0, 300.0): {
        "n_mu_minus_MeV3": 5.576259992070647e-10,
        "n_mu_plus_MeV3": 2.4904722437766412e-11,
        "nu_mu_prod_L_MeV_per_g2": 9.085642334029555e-40,
        "nu_mu_prod_plus_MeV_per_g2": 8.883382519489328e-40,
        "nu_mu_prod_minus_MeV_per_g2": 8.88338251948932e-40,
        "nu_tau_prod_L_MeV_per_g2": 9.085642334029555e-40,
        "compton_prod_scalar_MeV_per_g2": 1.000675065007581e-52,
        "compton_w_L": 0.0005552470849528,
        "compton_w_plus": 0.4997223764575235,
        "total_prod_L_MeV_per_g2": 1.8171284668059117e-39,
        "total_prod_plus_MeV_per_g2": 1.7766765038979155e-39,
        "total_prod_minus_MeV_per_g2": 1.776676503897914e-39,
    },
    (25.0, 500.0): {
        "n_mu_minus_MeV3": 5.758208344715423e-13,
        "n_mu_plus_MeV3": 5.758208344715423e-13,
        "nu_mu_prod_L_MeV_per_g2": 7.028019512574342e-75,
        "nu_mu_prod_plus_MeV_per_g2": 6.944077890941606e-75,
        "nu_mu_prod_minus_MeV_per_g2": 6.9440778909416e-75,
        "nu_tau_prod_L_MeV_per_g2": 7.028019512574342e-75,
        "compton_prod_scalar_MeV_per_g2": 1.3304181237103119e-90,
        "compton_w_L": 0.0001999600079984,
        "compton_w_plus": 0.4999000199960008,
        "total_prod_L_MeV_per_g2": 1.4056039025148684e-74,
        "total_prod_plus_MeV_per_g2": 1.3888155781883213e-74,
        "total_prod_minus_MeV_per_g2": 1.38881557818832e-74,
    },
}


class LocalRatePolarizationSampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.maxima = samples.build_rows(
            PROFILE, neutrino_order=512, susceptibility_order=256
        )
        cls.by_key = {(r["radius_km"], r["omega_MeV"]): r for r in cls.rows}

    def test_profile_fingerprint_and_54_point_grid(self):
        self.assertEqual(samples.sha256(PROFILE), EXPECTED_PROFILE_SHA256)
        self.assertEqual(len(self.rows), 54)
        self.assertEqual(sorted({r["radius_km"] for r in self.rows}), list(samples.RADII_KM))
        self.assertEqual(sorted({r["omega_MeV"] for r in self.rows}), list(samples.ENERGIES_MEV))

    def test_all_mode_sums_and_detailed_balance_close(self):
        for name, value in self.maxima.items():
            self.assertLess(value, 1.0e-12, (name, value))

    def test_reference_table_anchors(self):
        for key, expected in REFERENCE_SAMPLES.items():
            row = self.by_key[key]
            for field, target in expected.items():
                self.assertTrue(
                    np.isclose(row[field], target, rtol=2.0e-10, atol=1.0e-300),
                    (key, field, row[field], target),
                )

    def test_overlap_with_archived_independent_local_audit(self):
        archive = json.loads(LEGACY_LOCAL_JSON.read_text(encoding="utf-8"))
        legacy = {
            (float(r["radius_km"]), float(r["omega_MeV"])): r
            for r in archive["pointwise_results"]
        }
        common = 0
        for key, row in self.by_key.items():
            if key not in legacy:
                continue
            old = legacy[key]
            self.assertTrue(np.isclose(
                row["nu_mu_prod_L_MeV_per_g2"] + row["nu_mu_prod_plus_MeV_per_g2"] + row["nu_mu_prod_minus_MeV_per_g2"],
                old["nu_mu_production_direct_MeV"], rtol=2.0e-11, atol=1.0e-300
            ))
            self.assertTrue(np.isclose(
                row["nu_tau_prod_L_MeV_per_g2"] + row["nu_tau_prod_plus_MeV_per_g2"] + row["nu_tau_prod_minus_MeV_per_g2"],
                old["nu_tau_production_direct_MeV"], rtol=2.0e-11, atol=1.0e-300
            ))
            self.assertTrue(np.isclose(
                row["compton_prod_scalar_MeV_per_g2"],
                old["compton_B16"]["production_B16_MeV_per_g2"], rtol=2.0e-11, atol=1.0e-300
            ))
            self.assertTrue(np.isclose(
                row["total_prod_scalar_MeV_per_g2"],
                old["direct_total_production_MeV"], rtol=2.0e-11, atol=1.0e-300
            ))
            self.assertTrue(np.isclose(
                row["total_abs_scalar_MeV_per_g2"],
                old["direct_total_absorption_MeV"], rtol=2.0e-11, atol=1.0e-300
            ))
            self.assertTrue(np.isclose(
                row["total_red_abs_scalar_MeV_per_g2"],
                old["direct_total_reduced_absorption_MeV"], rtol=2.0e-11, atol=1.0e-300
            ))
            common += 1
        self.assertEqual(common, 36)

    def test_b14_weights_and_separate_mu_plus_diagnostic(self):
        for row in self.rows:
            weights = [row["compton_w_" + m] for m in samples.MODES]
            self.assertTrue(all(w > 0.0 for w in weights))
            self.assertLess(abs(sum(weights) - 1.0), 1.0e-14)
            self.assertGreaterEqual(row["n_mu_plus_MeV3"], 0.0)
            self.assertGreaterEqual(row["chi_mu_plus_MeV3"], 0.0)
            self.assertGreaterEqual(row["mu_plus_susceptibility_fraction"], 0.0)
            self.assertLessEqual(row["mu_plus_susceptibility_fraction"], 1.0)
        # The B.17 Compton kernel is intentionally built from chi_mu_minus only.
        row = self.by_key[(8.0, 12.0)]
        expected = local.independent_b14_b16_compton(
            10.0, 12.0, row["T_MeV"], row["chi_mu_minus_MeV3"]
        )["production_B16_MeV_per_g2"]
        self.assertTrue(math.isclose(
            row["compton_prod_scalar_MeV_per_g2"], expected, rel_tol=1.0e-14
        ))


if __name__ == "__main__":
    unittest.main()
