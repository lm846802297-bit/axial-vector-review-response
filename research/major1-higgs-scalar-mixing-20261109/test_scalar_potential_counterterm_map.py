import unittest

from scalar_potential_counterterm_map import (
    fixed_vev_bookkeeping_basis,
    linearized_mass_counterterm,
    linearized_tadpole_counterterms_per_vev,
    potential_mass_matrix,
    potential_tadpole_brackets,
)


class ScalarPotentialCountertermMapTests(unittest.TestCase):
    def test_tree_mass_matrix_matches_potential_second_derivatives(self):
        vh, vs = 246.22, 70.886458
        mu_h2, mu_s2 = 7800.0, 1200.0
        lh, ls, lhs = 0.129, 0.2, 0.03
        matrix = potential_mass_matrix(vh, vs, mu_h2, mu_s2, lh, ls, lhs)
        self.assertAlmostEqual(matrix[0][1], lhs * vh * vs, places=10)
        self.assertAlmostEqual(matrix[1][0], matrix[0][1], places=12)

    def test_fixed_vev_basis_reconstructs_all_three_pole_entries(self):
        examples = (
            ([[ -13374386.09800963, 4.33770200548787e-05],
              [4.33770200548787e-05, -63902155.30209779]], 70.886458),
            ([[-13374386.09800963, 9.761407305064081e-06],
              [9.761407305064081e-06, -3236092.6837118976]], 315.0),
        )
        for matrix, vs in examples:
            result = fixed_vev_bookkeeping_basis(matrix, 246.22, vs)
            self.assertLess(result["max_reconstruction_residual_GeV2"], 2e-8)
            self.assertAlmostEqual(
                result["delta_lambda_HS"],
                matrix[0][1] / (246.22 * vs),
                places=18,
            )

    def test_counterterm_and_tadpole_maps_obey_stationary_point_identity(self):
        vh, vs = 246.22, 70.886458
        lh, ls, lhs = 0.129, 0.22, 0.04
        params = dict(
            vh=vh, vs=vs, lam_h=lh, lam_s=ls, lam_hs=lhs,
            dmu_h2=1.3, dmu_s2=-2.1, dlam_h=0.004,
            dlam_s=-0.003, dlam_hs=0.002, dvh=0.01, dvs=-0.02,
        )
        dm = linearized_mass_counterterm(**params)
        dt_h, dt_s = linearized_tadpole_counterterms_per_vev(**params)
        self.assertAlmostEqual(
            dm[0][0] - dt_h,
            2 * vh**2 * params["dlam_h"] + 4 * lh * vh * params["dvh"],
            places=8,
        )
        self.assertAlmostEqual(
            dm[1][1] - dt_s,
            2 * vs**2 * params["dlam_s"] + 4 * ls * vs * params["dvs"],
            places=8,
        )

    def test_tadpole_stationarity_reference(self):
        vh, vs, lh, ls, lhs = 246.22, 70.886458, 0.129, 0.22, 0.04
        mu_h2 = lh * vh**2 + 0.5 * lhs * vs**2
        mu_s2 = ls * vs**2 + 0.5 * lhs * vh**2
        th, ts = potential_tadpole_brackets(vh, vs, mu_h2, mu_s2, lh, ls, lhs)
        self.assertAlmostEqual(th, 0.0, places=10)
        self.assertAlmostEqual(ts, 0.0, places=10)


if __name__ == "__main__":
    unittest.main()
