#!/usr/bin/env python3
import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "RC-001-dim6-WW-fivepoint-momentum-dependent-scalar-current-audit.py"
SPEC = importlib.util.spec_from_file_location("rc001_scalar_current_route_audit", SOURCE)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestRC001MomentumDependentScalarCurrentAudit(unittest.TestCase):
    def test_a_b_s_current_shifts_are_exactly_q(self):
        self.assertEqual(MOD.verify_exact_scalar_current_shifts(), 12)

    def test_all_six_scalar_endpoint_substitutions_are_nonzero(self):
        results, denominators = MOD.audit_actual_scalar_endpoint_rfg_differences()
        self.assertEqual(
            tuple(results),
            (
                "LD-W-02:B",
                "LD-W-05:A",
                "LD-W-06:A-current",
                "LD-W-06:B-current",
                "LD-W-03:S",
                "LD-W-04:S",
            ),
        )
        self.assertTrue(all(MOD.nonzero_entries(m) > 0 for m in results.values()))
        self.assertTrue(all(
            value != 0
            for values in denominators.values()
            for value in values
        ))

    def test_pair_06_two_scalar_endpoints_are_kept_separate(self):
        results, _ = MOD.audit_actual_scalar_endpoint_rfg_differences()
        self.assertGreater(MOD.nonzero_entries(results["LD-W-06:A-current"]), 0)
        self.assertGreater(MOD.nonzero_entries(results["LD-W-06:B-current"]), 0)


    def test_three_w_internal_leg_exchange_preserves_full_vertex(self):
        self.assertEqual(
            MOD.verify_three_w_internal_leg_exchange(),
            (64, 27, 1728),
        )


    def test_actual_line_seagull_three_w_denominator_factors(self):
        self.assertEqual(MOD.verify_actual_denominator_route_factors(), 7)

    def test_main_reports_no_physical_non_cancellation_claim(self):
        import contextlib
        import io
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            MOD.main()
        captured = output.getvalue()
        self.assertIn("12/12 vector components", captured)
        self.assertIn("64/64", captured)
        self.assertIn("27/27", captured)
        self.assertIn("1728/1728", captured)
        self.assertIn("7/7 exact identities", captured)
        self.assertIn("LD-W-06:A-current", captured)
        self.assertIn("LD-W-06:B-current", captured)
        self.assertIn("no physical non-cancellation is claimed", captured)


if __name__ == "__main__":
    unittest.main(verbosity=2)
