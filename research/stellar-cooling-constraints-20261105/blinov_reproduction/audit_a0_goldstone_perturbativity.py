#!/usr/bin/env python3
"""Perturbative-domain audit for the A0 finite-mixing Goldstone coupling.

The A0 current has g_A^mu/g_X = -cos(theta_mu_R)^2 and
m_A' = 2 g_X v_s. The Goldstone-equivalence relation therefore gives
y_Gμμ = 2 |g_A^mu| m_mu / m_A'.

This audit uses y_G^2/(4 pi) <= 1 as a conservative perturbativity
criterion. It is a theory-validity mask for the A0 scan, not an additional
supernova constraint.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE / "outputs"
M_MU_MEV = 105.6583755
THETA_MU_R = 1.0e-2
G_MIN = 1.0e-11
G_MAX = 1.0
N_G = 121
MASS_BENCHMARKS_MEV = {
    "0.1 eV": 1.0e-7,
    "1 eV": 1.0e-6,
    "10 eV": 1.0e-5,
    "0.1 MeV": 0.1,
    "10 MeV": 10.0,
    "200 MeV": 200.0,
}


def goldstone_yukawa(g_x: float, mass_mev: float, theta_mu_r: float = THETA_MU_R) -> float:
    if g_x < 0.0 or mass_mev <= 0.0:
        raise ValueError("Require g_X >= 0 and m_A' > 0")
    return 2.0 * g_x * math.cos(theta_mu_r) ** 2 * M_MU_MEV / mass_mev


def perturbative_gx_max(mass_mev: float, theta_mu_r: float = THETA_MU_R) -> float:
    """Solve y_Gμμ^2/(4 pi) = 1 for the maximum perturbative g_X."""
    if mass_mev <= 0.0:
        raise ValueError("m_A' must be positive")
    return (
        math.sqrt(4.0 * math.pi) * mass_mev
        / (2.0 * M_MU_MEV * math.cos(theta_mu_r) ** 2)
    )


def run_audit() -> dict:
    g_grid = np.logspace(math.log10(G_MIN), math.log10(G_MAX), N_G)
    rows = []
    for label, mass in MASS_BENCHMARKS_MEV.items():
        g_limit = perturbative_gx_max(mass)
        mask = g_grid <= g_limit
        valid = g_grid[mask]
        rows.append({
            "mass_label": label,
            "m_A_MeV": mass,
            "g_X_perturbative_max": g_limit,
            "g_X_scan_min": G_MIN,
            "g_X_scan_max": G_MAX,
            "scan_points": N_G,
            "perturbative_points": int(np.count_nonzero(mask)),
            "perturbative_fraction_of_scan": float(np.mean(mask)),
            "largest_perturbative_scan_point": float(valid[-1]) if len(valid) else None,
            "goldstone_yukawa_at_gX_1": goldstone_yukawa(1.0, mass),
            "alpha_G_at_gX_1": goldstone_yukawa(1.0, mass) ** 2 / (4.0 * math.pi),
            "goldstone_yukawa_at_perturbative_boundary": goldstone_yukawa(g_limit, mass),
        })
    return {
        "title": "A0 Goldstone-Yukawa perturbativity window",
        "status": "computed",
        "criterion": "y_Gμμ^2/(4 pi) <= 1",
        "theta_mu_R": THETA_MU_R,
        "coupling_map": {
            "g_A_mu_over_g_X": "-cos(theta_mu_R)^2",
            "m_A_prime": "2 g_X v_s",
            "y_G_mumu": "2 |g_A_mu| m_mu / m_A_prime = cos(theta_mu_R)^2 m_mu / v_s",
        },
        "scan": {"g_X_min": G_MIN, "g_X_max": G_MAX, "points": N_G},
        "masses": rows,
        "interpretation": (
            "The full transport scan may be retained for numerical diagnostics, "
            "but only points satisfying the stated Goldstone-Yukawa criterion "
            "belong to this conservative perturbative A0 domain."
        ),
    }


def main() -> None:
    payload = run_audit()
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    json_path = OUTPUTS / "A0_GOLDSTONE_PERTURBATIVITY_WINDOW_2026-11-20.json"
    csv_path = OUTPUTS / "A0_GOLDSTONE_PERTURBATIVITY_WINDOW_2026-11-20.csv"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(payload["masses"][0]))
        writer.writeheader()
        writer.writerows(payload["masses"])
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
