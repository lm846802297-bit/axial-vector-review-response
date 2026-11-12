#!/usr/bin/env python3
"""Audit the long-wavelength support of H&R's q=0 NN response for V->nu nu daughters.

This is a kinematic validity diagnostic, not a neutrino collision-rate calculation.
The H&R angular kernel (3-cos(theta)) is used only to define a transparent
angular measure. The elastic E'=E limit maximizes the phase space available
at small momentum transfer for a fixed incident daughter energy.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

M_V_MEV = 10.0
M_PI_MEV = 134.98
OMEGA_NODES_MEV = (210.0, 300.0, 510.0)
Q_FRACTIONS_OF_MPI = (1.0, 0.5, 0.25)
MODES = {
    "L": lambda z: 0.75 * (1.0 - z * z),
    "plus": lambda z: 0.375 * (1.0 + z) ** 2,
    "minus": lambda z: 0.375 * (1.0 - z) ** 2,
}
QUADRATURE_ORDER = 400


def angular_fraction_below_q(energy: np.ndarray, q_max: float) -> np.ndarray:
    """Fraction of (3-cos theta) angular weight with Q<q_max for E'=E."""
    energy = np.asarray(energy, dtype=float)
    if np.any(energy <= 0.0):
        raise ValueError("Incident daughter energies must be positive")
    c_min = 1.0 - q_max**2 / (2.0 * energy**2)
    return np.where(
        c_min <= -1.0,
        1.0,
        np.where(
            c_min >= 1.0,
            0.0,
            ((3.0 - 0.5) - (3.0 * c_min - 0.5 * c_min**2)) / 6.0,
        ),
    )


def mode_energy_weighted_fraction(
    omega: float, mode: str, q_max: float, nodes: np.ndarray, weights: np.ndarray
) -> float:
    beta = np.sqrt(1.0 - (M_V_MEV / omega) ** 2)
    z = nodes
    e1 = 0.5 * omega * (1.0 + beta * z)
    e2 = 0.5 * omega * (1.0 - beta * z)
    f1 = angular_fraction_below_q(e1, q_max)
    f2 = angular_fraction_below_q(e2, q_max)
    integrand = MODES[mode](z) * (e1 * f1 + e2 * f2) / omega
    return float(np.sum(weights * integrand))


def build_result() -> dict:
    nodes, weights = leggauss(QUADRATURE_ORDER)
    mode_norms = {
        mode: float(np.sum(weights * weight_fn(nodes)))
        for mode, weight_fn in MODES.items()
    }
    if any(abs(value - 1.0) > 1.0e-12 for value in mode_norms.values()):
        raise AssertionError(f"Polarization weights are not normalized: {mode_norms}")

    results = []
    for omega in OMEGA_NODES_MEV:
        beta = float(np.sqrt(1.0 - (M_V_MEV / omega) ** 2))
        threshold_results = {}
        for fraction in Q_FRACTIONS_OF_MPI:
            q_max = fraction * M_PI_MEV
            by_mode = {
                mode: mode_energy_weighted_fraction(
                    omega, mode, q_max, nodes, weights
                )
                for mode in MODES
            }
            threshold_results[str(fraction)] = {
                "q_max_MeV": q_max,
                "mode_energy_weighted_fraction": by_mode,
                "equal_mode_average": float(np.mean(list(by_mode.values()))),
            }
        results.append(
            {
                "omega_MeV": omega,
                "beta": beta,
                "thresholds": threshold_results,
            }
        )

    return {
        "title": "Long-wavelength angular-support diagnostic for high-energy vector-decay neutrino daughters",
        "date": "2026-11-10",
        "benchmark": {
            "mV_MeV": M_V_MEV,
            "omega_nodes_MeV": list(OMEGA_NODES_MEV),
            "mpi_MeV": M_PI_MEV,
        },
        "method": {
            "daughter_energies": "E1,2=omega/2*(1 +/- beta*z), beta=sqrt(1-mV^2/omega^2)",
            "scattering_transfer": "Q=|k-k'|; elastic limit E'=E gives Q=2E*sin(theta/2)",
            "angular_weight": "3-cos(theta), from Hannestad & Raffelt (1998), Eqs. (23) and (32)",
            "angular_fraction": "integral_{Q<qmax} dcos(theta)*(3-cos(theta)) / integral_{-1}^{1} dcos(theta)*(3-cos(theta))",
            "pair_energy_weight": "(1/omega)*integral dz W_h(z)*(E1*F(E1)+E2*F(E2))",
            "polarization_weights": {
                "L": "3/4*(1-z^2)",
                "plus": "3/8*(1+z)^2",
                "minus": "3/8*(1-z)^2",
            },
            "quadrature": {"method": "Gauss-Legendre", "order": QUADRATURE_ORDER},
            "mode_norms": mode_norms,
        },
        "results": results,
        "interpretation": {
            "q_lt_mpi": "A deliberately generous scale diagnostic, not the formal validity condition.",
            "q_lt_half_mpi": "A stricter but still not asymptotically small-transfer criterion.",
            "q_lt_quarter_mpi": "A more conservative small-transfer indicator.",
            "important": (
                "The H&R long-wavelength kernel neglects neutrino momentum transfer "
                "in the nuclear response. These fractions are computed in the elastic "
                "E'=E limit; finite energy transfer gives Q_min=|E-E'| and can reduce "
                "the supported fraction. They are not collision probabilities or "
                "corrections to the H&R rate."
            ),
        },
    }


def main() -> None:
    result = build_result()
    output = Path(__file__).resolve().parent / "outputs" / "p1i_long_wavelength_support_2026-11-10.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    summary = {
        str(item["omega_MeV"]): {
            key: round(value["equal_mode_average"], 6)
            for key, value in item["thresholds"].items()
        }
        for item in result["results"]
    }
    print(json.dumps({"output": str(output), "equal_mode_average": summary}, indent=2))


if __name__ == "__main__":
    main()
