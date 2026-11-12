import unittest

import numpy as np

import audit_b16_p1iii_eos_c4c4_radial_energy_dependence as c4c4


class C4C4BRadialEnergyDependenceTests(unittest.TestCase):
    def test_energy_and_case_grid(self):
        self.assertEqual(len(c4c4.expected_rate_keys()), 7224)
        self.assertEqual(len(c4c4.expected_quad_keys()), 340)
        self.assertEqual(c4c4.ENERGY_GRID_MEV, (10.0, 20.0, 40.0, 60.0, 100.0, 150.0))

    def test_radial_shards_partition_all_301_nodes(self):
        shards = [list(c4c4.shard_indices(i, 5)) for i in range(5)]
        merged = [index for shard in shards for index in shard]
        self.assertEqual(merged, list(range(301)))
        self.assertEqual([len(shard) for shard in shards], [60, 60, 60, 60, 61])

    def test_high_order_sample_contains_anchor_and_opacity_peak_nodes(self):
        sample = set(c4c4.QUAD_SAMPLE_INDICES)
        self.assertTrue({0, 96, 142, 143, 196, 300}.issubset(sample))
        self.assertEqual(len(sample), 17)

    def test_relative_difference_is_symmetric_and_positive(self):
        self.assertAlmostEqual(c4c4.relative_difference(1.001, 1.0), 1e-3)
        with self.assertRaises(ValueError):
            c4c4.relative_difference(0.0, 1.0)

    def test_tau_for_constant_opacity(self):
        r = np.asarray([0.0, 0.5, 1.0])
        k = np.asarray([2.0, 2.0, 2.0])
        tau = c4c4.tau_from_kappa(r, k)
        self.assertAlmostEqual(tau[0] / (2.0 * c4c4.KM_TO_MEV_INV), 1.0, places=14)
        self.assertAlmostEqual(tau[1] / c4c4.KM_TO_MEV_INV, 1.0, places=14)
        self.assertEqual(tau[2], 0.0)
        self.assertTrue(np.all(np.diff(tau) <= 0.0))

    def test_tau_rejects_nonmonotone_radius_and_negative_opacity(self):
        with self.assertRaises(ValueError):
            c4c4.tau_from_kappa(np.asarray([0.0, 1.0, 0.5]), np.ones(3))
        with self.assertRaises(ValueError):
            c4c4.tau_from_kappa(np.asarray([0.0, 1.0]), np.asarray([1.0, -1.0]))

    def test_full_radial_products_have_expected_shape_and_grid_convergence(self):
        profile = [
            {"r_km": 0.2 + 0.05 * i, "T_MeV": 20.0 - 0.01 * i, "nB_fm3": 0.3, "xi_SPP": 1.0}
            for i in range(301)
        ]
        rows = []
        for energy in c4c4.ENERGY_GRID_MEV:
            for index in range(301):
                for species in ("n", "p"):
                    for anti in ("False", "True"):
                        gamma = energy * (1.0 if species == "n" else 0.5) * (1.0 if anti == "False" else 0.8)
                        rows.append({
                            "E_MeV": energy, "profile_index": index, "species": species,
                            "antinu": anti, "kappa_sc_MeV": gamma * 1e-13,
                        })
        radial, channels, convergence, checks = c4c4.build_radial_products(rows, profile)
        self.assertEqual(len(radial), 6 * 301)
        self.assertEqual(len(channels), 6 * 301)
        self.assertEqual(len(convergence), 6 * 6 * 2)
        self.assertTrue(checks["radial_grid_convergence_pass"])
        self.assertTrue(checks["acceptance"]["all_tau_nonnegative_and_radially_monotone"])

    def test_quad_validation_reconstructs_all_340_differences(self):
        rows = []
        for energy in c4c4.NEW_ENERGIES_MEV:
            for index in c4c4.QUAD_SAMPLE_INDICES:
                for species in ("n", "p"):
                    for anti in ("False", "True"):
                        rows.append({
                            "E_MeV": energy, "profile_index": index, "species": species,
                            "antinu": anti, "gamma_base_MeV": 1.0,
                            "gamma_high_MeV": 1.0001, "relative_difference": 1e-4,
                            "support_root_max_relative_residual": 1e-12,
                        })
        result = c4c4.validate_quadrature_rows(rows)
        self.assertEqual(len(rows), 340)
        self.assertTrue(result["quadrature_convergence_pass"])
        self.assertAlmostEqual(result["max_relative_difference"], 1e-4)

    def test_rate_grid_validation_requires_all_7224_keys(self):
        profile = [{"r_km": 0.2 + 0.05 * i} for i in range(301)]
        rows = []
        for energy in c4c4.ENERGY_GRID_MEV:
            for index in range(301):
                for species in ("n", "p"):
                    for anti in ("False", "True"):
                        gamma = 1.0e-13
                        xi = 0.9
                        rows.append({
                            "E_MeV": energy, "profile_index": index, "species": species,
                            "antinu": anti, "gamma_available_volume_MeV": gamma,
                            "sigma_per_target_MeV_minus2": 1.0e-19,
                            "kappa_sc_MeV": xi * gamma, "lambda_sc_km": 1.0,
                            "xi_SPP": xi, "density_closure_relative_residual": 1e-4,
                            "support_root_max_relative_residual": 1e-12,
                        })
        result = c4c4.validate_rate_rows(rows, profile)
        self.assertTrue(result["numerical_integrity_pass"])
        self.assertEqual(result["case_counts_by_energy"]["100.0"], 1204)


if __name__ == "__main__":
    unittest.main()
