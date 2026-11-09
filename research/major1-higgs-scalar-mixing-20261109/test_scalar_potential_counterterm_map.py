import unittest

from scalar_potential_counterterm_map import (
    LOOP,
    finite_heavy_potential_matching,
    finite_potential_hs_mass_contributions,
    leading_eft5_derivatives,
    potential_mass_counterterm,
    potential_tadpoles_per_vev,
    solve_potential_counterterms,
    plan_c_scale_dependence,
)


class ScalarPotentialCountertermMapTests(unittest.TestCase):
    def test_full_theory_potential_counterterms_cancel_tadpoles_and_local_poles(self):
        cases = (
            (70.886458, 519912273576.47626, 715204443204.932,
             2111998398.3185194, 0.0, 10091023891.362673),
            (315.0, 519912273576.47626, 160947014998.92,
             2111998398.3185194, 0.0, 511023273.49714106),
        )
        for vs, fh, fs, fhh, fhs, fss in cases:
            result = solve_potential_counterterms(246.22, vs, fh, fs, fhh, fhs, fss)
            self.assertLess(max(abs(x) for x in result["tadpole_cancellation_residual_GeV2"]), 2e-6)
            mass_res = result["mass_cancellation_residual_GeV2"]
            self.assertLess(max(abs(x) for row in mass_res for x in row), 2e-8)
            self.assertAlmostEqual(result["delta_lambda_HS"], 0.0, places=20)

    def test_counterterm_potential_derivatives_reconstruct_target_matrix(self):
        result = solve_potential_counterterms(
            246.22, 70.886458,
            519912273576.47626, 715204443204.932,
            2111998398.3185194, 0.0, 10091023891.362673,
        )
        p = result
        tad = potential_tadpoles_per_vev(
            246.22, 70.886458,
            p["delta_mu_H2_GeV2"], p["delta_mu_S2_GeV2"],
            p["delta_lambda_H"], p["delta_lambda_S"], p["delta_lambda_HS"],
        )
        mass = potential_mass_counterterm(
            246.22, 70.886458,
            p["delta_mu_H2_GeV2"], p["delta_mu_S2_GeV2"],
            p["delta_lambda_H"], p["delta_lambda_S"], p["delta_lambda_HS"],
        )
        self.assertAlmostEqual(tad[0], p["loop_1PI_tadpole_pole_coefficients_GeV3"][0]/246.22, places=7)
        self.assertAlmostEqual(tad[1], p["loop_1PI_tadpole_pole_coefficients_GeV3"][1]/70.886458, places=7)
        self.assertAlmostEqual(mass[0][0], p["loop_Pi_RC_local_pole_coefficients_GeV2"][0][0], places=7)
        self.assertAlmostEqual(mass[1][1], p["loop_Pi_RC_local_pole_coefficients_GeV2"][1][1], places=7)

    def test_leading_eft5_contact_completes_mixed_two_point_uv_pole(self):
        by_flavour = {
            "mu": {"y": 1.14873979560807, "lambda": 0.2107927407099522, "ml_GeV": 0.1056583755},
            "tau": {"y": 1.14873979560807, "lambda": 3.544907703581773, "ml_GeV": 1.77686},
        }
        result = leading_eft5_derivatives(246.22, 70.886458, by_flavour)
        total = result["sum_derivatives_GeV"]
        bubble = result["bubble_local_UV_coefficients_GeV2"]
        contact = result["dimension5_contact_local_UV_coefficients_GeV2"]
        complete = result["complete_leading_EFT5_local_UV_coefficients_GeV2"]
        self.assertAlmostEqual(complete["hh"], total["F_hh"], places=14)
        self.assertAlmostEqual(complete["hs"], total["F_hs"], places=14)
        self.assertAlmostEqual(complete["ss"], total["F_ss"], places=14)
        self.assertAlmostEqual(contact["hs"], 4*total["F"]/(246.22*70.886458), places=18)
        self.assertGreater(contact["hs"], 0.0)
        self.assertEqual(contact["hh"], 0.0)
        self.assertEqual(contact["ss"], 0.0)

    def test_c5_normalization_reproduces_seesaw_masses(self):
        by_flavour = {
            "mu": {"y": 1.14873979560807, "lambda": 0.2107927407099522, "ml_GeV": 0.1056583755},
            "tau": {"y": 1.14873979560807, "lambda": 3.544907703581773, "ml_GeV": 1.77686},
        }
        result = leading_eft5_derivatives(246.22, 70.886458, by_flavour)
        for item in result["flavours"].values():
            self.assertLess(item["C5_GeVminus1"], 0.0)
            self.assertLess(item["kappa_neutral_mass_operator_GeVminus1"], 0.0)
            self.assertAlmostEqual(
                item["m_EFT5_mass_parameter_at_vev_GeV"],
                -item["input_light_mass_GeV"], places=14,
            )
            self.assertAlmostEqual(
                item["m_EFT5_at_vev_GeV"],
                item["input_light_mass_GeV"], places=14,
            )
            self.assertLess(item["mass_relative_difference"], 2e-15)

    def test_plan_c_scale_residual_is_twice_eft5_mixed_uv_pole(self):
        cases = (
            (70.886458, {
                "mu": {"ml_GeV": 0.1056583755, "y": 1.14873979560807, "lambda": 0.2107927407099522},
                "tau": {"ml_GeV": 1.77686, "y": 1.14873979560807, "lambda": 3.544907703581773},
            }),
            (315.0, {
                "mu": {"ml_GeV": 0.1056583755, "y": 1.14873979560807, "lambda": 0.04743603416203466},
                "tau": {"ml_GeV": 1.77686, "y": 1.14873979560807, "lambda": 0.7977331779169075},
            }),
        )
        for vs, by_flavour in cases:
            result = plan_c_scale_dependence(
                246.22, vs, 125.25**2, by_flavour,
                mu_reference=20000.0, mu_low=125.25,
            )
            self.assertLess(result["relative_identity_residual"], 1e-13)
            self.assertLess(result["relative_finite_difference_residual"], 2e-7)
            self.assertAlmostEqual(
                result["total_d_dlnmu_GeV2"],
                2.0*result["leading_EFT5_PiB_hs_local_UV_coefficient_GeV2"],
                places=15,
            )
            running = result["dimension8_running"]
            self.assertLess(running["relative_residual_after_O8_running"], 2e-8)
            self.assertAlmostEqual(
                running["delta_PiB_from_O8_running_GeV2"],
                -running["delta_PiB_soft_plus_hard_GeV2"][0],
                places=14,
            )
            self.assertEqual(running["finite_matching_value_c8_at_M_E"], "not determined")

    def test_finite_heavy_cw_matching_coefficients_and_c8_running(self):
        by_flavour = {
            "mu": {"y": 1.14873979560807, "lambda": 0.21079274070995216},
            "tau": {"y": 1.14873979560807, "lambda": 3.5449077035817727},
        }
        result = finite_heavy_potential_matching(by_flavour)
        coeff = result["finite_potential_wilson_coefficients_at_mu_ME"]
        c8 = result["O8_matching_and_running"]
        c5_fourth = result["dimensionless_coupling_invariants"]["c5_fourth"]
        self.assertAlmostEqual(coeff["delta_lambda_HS_finite_at_mu_ME"],
                               -2.0*LOOP*sum(
                                   abs(v["y"])**2*abs(v["lambda"])**2
                                   for v in by_flavour.values()), places=15)
        self.assertAlmostEqual(c8["UV_pole_residue_GeVminus4"],
                               -LOOP*c5_fourth, places=30)
        self.assertAlmostEqual(c8["finite_matching_coefficient_c8_at_mu_ME_GeVminus4"],
                               -3.5*LOOP*c5_fourth, places=30)
        self.assertAlmostEqual(c8["loop_induced_beta_c8_GeVminus4"],
                               -2.0*LOOP*c5_fourth, places=30)
        self.assertAlmostEqual(
            coeff["c_(HdagH)^2(SdagS)^2_GeVminus4"],
            c8["finite_matching_coefficient_c8_at_mu_ME_GeVminus4"], places=30
        )
        self.assertGreater(coeff["c_(HdagH)^2(SdagS)_GeVminus2"], 0.0)
        self.assertGreater(coeff["c_(HdagH)(SdagS)^2_GeVminus2"], 0.0)
        self.assertLess(coeff["c_(HdagH)^3(SdagS)_GeVminus4"], 0.0)
        self.assertLess(coeff["c_(HdagH)(SdagS)^3_GeVminus4"], 0.0)

    def test_finite_potential_hs_curvature_matches_exact_heavy_cw(self):
        import mpmath as mp
        mp.mp.dps = 60
        cases = (
            (mp.mpf("70.886458"), {
                "mu": {"y": 1.14873979560807, "lambda": 0.21079274070995216},
                "tau": {"y": 1.14873979560807, "lambda": 3.5449077035817727},
            }, 246.22, -3677.9466276134013, 0.65693383515755),
            (mp.mpf("315.0"), {
                "mu": {"y": 1.14873979560807, "lambda": 0.04743603416203465},
                "tau": {"y": 1.14873979560807, "lambda": 0.7977331779169073},
            }, 246.22, -827.6717750620922, 0.147834008618015),
        )
        me = mp.mpf("20000")
        loop = 1/(16*mp.pi**2)
        for vs, flavs, vh, expected_total, expected_higher in cases:
            match = finite_heavy_potential_matching(flavs)
            coeff = match["finite_potential_wilson_coefficients_at_mu_ME"]
            local = finite_potential_hs_mass_contributions(coeff, vh, float(vs))
            self.assertLess(
                abs(local["total_including_portal_GeV2"]-expected_total)/abs(expected_total),
                1e-9,
            )
            self.assertLess(
                abs(local["higher_dimensional_sum_GeV2"]-expected_higher)/abs(expected_higher),
                1e-9,
            )

            def exact_heavy_potential(h, s):
                value = mp.mpf("0")
                for item in flavs.values():
                    y = mp.mpf(str(item["y"]))
                    lam = mp.mpf(str(item["lambda"]))
                    x = y**2*h**2/2
                    yy = lam**2*s**2/2
                    total = me**2+x+yy
                    zplus = (total+mp.sqrt(total**2-4*x*yy))/2
                    value += -loop*zplus**2*(mp.log(zplus/me**2)-mp.mpf(3)/2)
                return value

            exact_mixed = mp.diff(lambda h: mp.diff(lambda s: exact_heavy_potential(h,s), vs), mp.mpf(str(vh)))
            self.assertLess(abs(exact_mixed-mp.mpf(str(local["total_including_portal_GeV2"])))/abs(exact_mixed), mp.mpf("1e-9"))

    def test_exact_heavy_eigenvalue_cw_matches_dimension8_background_expansion(self):
        import mpmath as mp
        mp.mp.dps = 70

        def exact_heavy_cw(x, y):
            total = 1 + x + y
            heavy = (total + mp.sqrt(total**2 - 4*x*y))/2
            return heavy**2*(mp.log(heavy)-mp.mpf(3)/2)

        def truncated_expansion(x, y):
            u = x+y
            p = x*y
            return (
                -mp.mpf(3)/2 - 2*u + 2*p
                + (u**3/3 - 2*p*u)
                + (-u**4/12 + p*u**2 + 2*p**2)
            )

        x0, y0 = mp.mpf("0.4"), mp.mpf("0.6")
        scale_large, scale_small = mp.mpf("0.04"), mp.mpf("0.02")
        err_large = abs(
            exact_heavy_cw(scale_large*x0, scale_large*y0)
            - truncated_expansion(scale_large*x0, scale_large*y0)
        )
        err_small = abs(
            exact_heavy_cw(scale_small*x0, scale_small*y0)
            - truncated_expansion(scale_small*x0, scale_small*y0)
        )
        # The first omitted terms have total degree five in X,Y.
        self.assertLess(err_small/err_large, mp.mpf("0.04"))
        self.assertGreater(err_small/err_large, mp.mpf("0.02"))

    def test_dimension8_coefficient_has_correct_mass_dimension_and_scaling(self):
        by_a = {
            "mu": {"y": 1.14873979560807, "lambda": 0.2107927407099522, "ml_GeV": 0.1056583755},
            "tau": {"y": 1.14873979560807, "lambda": 3.544907703581773, "ml_GeV": 1.77686},
        }
        by_b = {
            "mu": {"y": 1.14873979560807, "lambda": 0.04743603416203466, "ml_GeV": 0.1056583755},
            "tau": {"y": 1.14873979560807, "lambda": 0.7977331779169075, "ml_GeV": 1.77686},
        }
        a = leading_eft5_derivatives(246.22, 70.886458, by_a)
        b = leading_eft5_derivatives(246.22, 315.0, by_b)
        self.assertLess(a["dimension8_potential_counterterm_coefficient_GeVminus4"], 0.0)
        self.assertLess(b["dimension8_potential_counterterm_coefficient_GeVminus4"], 0.0)
        self.assertLess(abs(a["dimension8_potential_counterterm_coefficient_GeVminus4"]), 1e-15)
        self.assertLess(abs(b["dimension8_potential_counterterm_coefficient_GeVminus4"]), 1e-18)


if __name__ == "__main__":
    unittest.main()
