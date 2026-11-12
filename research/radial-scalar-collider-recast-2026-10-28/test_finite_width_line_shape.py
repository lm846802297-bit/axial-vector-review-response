import unittest
import numpy as np

from finite_width_line_shape import (
    crystal_ball_pdf,
    two_crystal_ball_mixture_pdf,
    fourmu_observable_mass,
    tautau_observable_mass,
    convolve_fourmu,
    convolve_tautau,
    load_response_table,
)


def response_table(lo, hi):
    x = np.linspace(lo, hi, 5)
    return {
        "mass_GeV": x,
        "fraction_1": np.full_like(x, 0.65),
        "mean_bias_GeV": np.zeros_like(x),
        "sigma_fit_GeV": np.full_like(x, 0.002),
        "sigma_1_GeV": np.full_like(x, 0.0018),
        "alpha_1": np.full_like(x, 2.0),
        "n_1": np.full_like(x, 3.0),
        "sigma_2_GeV": np.full_like(x, 0.0025),
        "alpha_2": np.full_like(x, 1.8),
        "n_2": np.full_like(x, 4.0),
        "tail_side_1": "left",
        "tail_side_2": "right",
    }


class FiniteWidthLineShapeTests(unittest.TestCase):
    def test_single_crystal_ball_normalization(self):
        x = np.linspace(-0.2, 0.2, 20001)
        p = crystal_ball_pdf(x, 0.0, 0.002, 1.8, 3.0, "left")
        self.assertAlmostEqual(float(np.trapezoid(p, x)), 1.0, delta=0.002)

    def test_two_component_mixture_normalization(self):
        x = np.linspace(-0.2, 0.2, 20001)
        p = two_crystal_ball_mixture_pdf(
            x, 0.0, 0.6, 0.002, 2.0, 3.0, "left",
            0.003, 1.8, 4.0, "right"
        )
        self.assertAlmostEqual(float(np.trapezoid(p, x)), 1.0, delta=0.002)

    def test_fourmu_reduced_mass_transform(self):
        q = np.array([0.22, 0.3, 1.0])
        mr = fourmu_observable_mass(q)
        self.assertTrue(np.all(mr < q))
        with self.assertRaises(ValueError):
            fourmu_observable_mass(np.array([2*0.1056583755]))

    def test_tautau_observable_is_recoil_mass(self):
        q = np.array([3.6, 6.0, 9.0])
        np.testing.assert_allclose(tautau_observable_mass(q), q)

    def test_fourmu_convolution_returns_normalized_shape(self):
        q = np.linspace(0.30, 0.50, 401)
        mr = fourmu_observable_mass(q)
        resp = response_table(float(mr.min()), float(mr.max()))
        gt = np.full_like(q, 0.001)
        gf = gt.copy()
        pe = np.ones_like(q)
        rec = np.linspace(float(mr.min()-0.07), float(mr.max()+0.07), 2001)
        out = convolve_fourmu(
            pole_mass_GeV=0.4, true_mass_grid_GeV=q,
            gamma_total_GeV=gt, gamma_final_GeV=gf,
            production_times_efficiency=pe,
            reconstructed_mass_grid_GeV=rec,
            response_table=resp,
        )
        grid_fraction = float(np.trapezoid(out["normalized_spectrum_per_GeV"], rec))
        self.assertAlmostEqual(grid_fraction, 1.0, delta=1e-4)
        self.assertGreater(out["fit_window_fraction"], 0.95)
        self.assertEqual(out["status"], "shape_only_no_CLs_reinterpretation")

    def test_tau_convolution_uses_40_sigma_total_fit_window(self):
        q = np.linspace(3.7, 4.3, 401)
        resp = response_table(float(q.min()), float(q.max()))
        gt = np.full_like(q, 0.001)
        gf = gt.copy()
        pe = np.ones_like(q)
        rec = np.linspace(3.0, 5.0, 3001)
        out = convolve_tautau(
            pole_mass_GeV=4.0, true_mass_grid_GeV=q,
            gamma_total_GeV=gt, gamma_final_GeV=gf,
            production_times_efficiency=pe,
            reconstructed_mass_grid_GeV=rec,
            response_table=resp,
        )
        lo, hi = out["fit_window"]
        self.assertAlmostEqual(hi-lo, 0.08, places=6)

    def test_missing_crystal_ball_parameters_are_rejected(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/"bad.csv"
            p.write_text("mass_GeV,sigma_GeV\n4,0.01\n5,0.01\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_response_table(p)


if __name__ == "__main__":
    unittest.main(verbosity=2)
