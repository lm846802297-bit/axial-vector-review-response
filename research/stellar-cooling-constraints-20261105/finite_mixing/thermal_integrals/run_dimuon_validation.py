"""Reproducible quadrature and threshold validation for dimuon emissivity."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT))

import rates
from finite_mixing.thermal_integrals.dimuon import dimuon_thermal_integral


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def max_relative_difference(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.max(np.abs(a - b) / np.maximum(np.abs(b), 1e-300)))


def run_benchmark(mass, temperature, mu_mu, g_vector, g_axial):
    results = {}
    q_values = {}
    balance_residuals = {}
    for order in (64, 128, 192):
        out = dimuon_thermal_integral(
            mass, temperature, mu_mu, g_vector, g_axial, order=order
        )
        q = out["Q_by_mode"]
        omega = out["energy"]
        production = out["production_spectrum"]
        absorption = out["absorption_spectrum"]
        balance_rhs = np.exp(-omega / temperature)[:, None] * absorption
        balance = max_relative_difference(production, balance_rhs)
        q_values[order] = q
        balance_residuals[order] = balance
        results[str(order)] = {
            "Q_by_mode_MeV5": [float(x) for x in q],
            "Q_total_MeV5": float(np.sum(q)),
            "max_pointwise_detailed_balance_relative_residual": balance,
        }
    results["relative_difference_Q_64_vs_128"] = max_relative_difference(
        q_values[64], q_values[128]
    )
    results["relative_difference_Q_128_vs_192"] = max_relative_difference(
        q_values[128], q_values[192]
    )
    results["max_detailed_balance_relative_residual"] = max(balance_residuals.values())
    return results


def run_threshold_scan():
    rows = {}
    for delta in (1e-4, 1e-8, 1e-12):
        mass = 2.0 * rates.M_MU * (1.0 + delta)
        vector = dimuon_thermal_integral(
            mass, 30.0, 80.0, 1.0, 0.0, order=128
        )
        axial = dimuon_thermal_integral(
            mass, 30.0, 80.0, 0.0, 1.0, order=128
        )
        beta2 = 1.0 - 4.0 * rates.M_MU**2 / mass**2
        analytic = beta2 / (1.0 + 2.0 * rates.M_MU**2 / mass**2)
        observed = float(np.sum(axial["Q_by_mode"]) / np.sum(vector["Q_by_mode"]))
        deviation = abs(observed / analytic - 1.0)
        rows[f"{delta:g}"] = {
            "mass_MeV": float(mass),
            "beta": float(np.sqrt(beta2)),
            "Q_vector_total_MeV5": float(np.sum(vector["Q_by_mode"])),
            "Q_axial_total_MeV5": float(np.sum(axial["Q_by_mode"])),
            "observed_QA_over_QV": observed,
            "analytic_GammaA_over_GammaV": float(analytic),
            "relative_deviation": float(deviation),
        }
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "outputs" / "dimuon_thermal_integral_validation.json",
    )
    args = parser.parse_args()

    benchmarks = {
        "m300_T30_mu80_pure_axial": run_benchmark(300.0, 30.0, 80.0, 0.0, 1.0),
        "m500_T35_mu75_mixed": run_benchmark(500.0, 35.0, 75.0, 1e-4, 1.0),
        "m3000_T10_mu0_pure_axial": run_benchmark(3000.0, 10.0, 0.0, 0.0, 1.0),
    }
    threshold = run_threshold_scan()

    max_quad = max(
        max(v["relative_difference_Q_64_vs_128"],
            v["relative_difference_Q_128_vs_192"])
        for v in benchmarks.values()
    )
    max_balance = max(v["max_detailed_balance_relative_residual"]
                      for v in benchmarks.values())
    max_threshold = max(v["relative_deviation"] for v in threshold.values())

    payload = {
        "title": "Dimuon thermal emissivity integral: numerical validation",
        "units": {
            "mass_temperature_momentum": "MeV",
            "differential_rates": "MeV",
            "energy_emissivity": "MeV^5",
        },
        "method": {
            "momentum_map": "k = scale*x/(1-x), x in (0,1)",
            "quadrature": "Gauss-Legendre on the mapped finite interval",
            "default_scale": "max(T, sqrt(m_Aprime*T))",
            "absorption": "retained differentially in mediator energy and polarization; not phase-space integrated",
            "scope": "local microphysical rate only; no stellar profile or transport",
        },
        "source_sha256": {
            "rates.py": sha256(ROOT / "rates.py"),
            "dimuon.py": sha256(HERE / "dimuon.py"),
            "test_dimuon.py": sha256(HERE / "test_dimuon.py"),
            "run_dimuon_validation.py": sha256(HERE / "run_dimuon_validation.py"),
            "moving_compton.py": sha256(HERE / "moving_compton.py"),
            "test_moving_compton.py": sha256(HERE / "test_moving_compton.py"),
            "moving_compton_derivation.md": sha256(
                HERE.parent / "MOVING_MUON_SEMI_COMPTON_DERIVATION_2026-11-07.md"
            ),
        },
        "benchmarks": benchmarks,
        "threshold_scan": threshold,
        "acceptance": {
            "quadrature_relative_difference_max": max_quad,
            "detailed_balance_relative_residual_max": max_balance,
            "threshold_width_ratio_relative_deviation_max": max_threshold,
            "quadrature_pass": max_quad < 1e-10,
            "detailed_balance_pass": max_balance < 1e-10,
            "threshold_scaling_pass": max_threshold < 1e-8,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload["acceptance"], indent=2))
    if not all(payload["acceptance"][key] for key in (
        "quadrature_pass", "detailed_balance_pass", "threshold_scaling_pass"
    )):
        raise SystemExit("Dimuon thermal-integral validation failed")


if __name__ == "__main__":
    main()
