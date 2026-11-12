import unittest

from independent_fermion_tadpole_uv_audit import (
    BENCHMARKS,
    M_LEPTON,
    VH,
    derivatives,
    trace_m4_closed_form,
    trace_m4_from_svd,
    verify_symbolic_derivatives,
)


class IndependentFermionTadpoleUVTests(unittest.TestCase):
    def test_trace_invariant_matches_independent_svd_spectrum(self):
        for vs in (70.886458, 315.0):
            for ml in M_LEPTON.values():
                from independent_fermion_tadpole_uv_audit import yukawas
                y, lam = yukawas(vs, ml)
                for h, s in ((VH, vs), (0.97*VH, 1.03*vs), (1.02*VH, 0.91*vs)):
                    direct = trace_m4_from_svd(h, s, y, lam)
                    closed = trace_m4_closed_form(h, s, y, lam)
                    self.assertLess(abs(direct-closed)/closed, 2e-14)

    def test_analytic_derivatives_match_50_digit_mpmath(self):
        for benchmark in BENCHMARKS.values():
            result = verify_symbolic_derivatives(benchmark["vs_GeV"])
            self.assertEqual(result["derivative_components_checked"], 10)
            self.assertLess(result["max_relative_difference"], 1e-35)

    def test_mixed_hs_local_uv_pole_vanishes(self):
        for vs in (70.886458, 315.0):
            result = derivatives(vs)
            self.assertEqual(result["sum"]["F_hs"], 0.0)

    def test_diagonal_second_derivatives_are_positive(self):
        for vs in (70.886458, 315.0):
            result = derivatives(vs)["sum"]
            self.assertGreater(result["F_hh"], 0.0)
            self.assertGreater(result["F_ss"], 0.0)


if __name__ == "__main__":
    unittest.main()
