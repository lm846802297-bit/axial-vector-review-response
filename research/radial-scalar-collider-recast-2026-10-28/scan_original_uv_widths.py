#!/usr/bin/env python3
"""Grid scan of the original one-VEV radial scalar widths.

Scope: original S + VLL model only; no sigma, extra VEV, or RH neutrinos.
The benchmark sets the Higgs portal to zero and decouples VLLs (ME > 10 TeV).
This is a width/lifetime diagnostic, not a Belle II recast.

The scan distinguishes:
  * mA < ms/2: on-shell A'A' is included;
  * ms/2 <= mA < ms: one-on-shell/one-virtual A' three-body cascades are included;
  * mA >= ms: two-virtual-A' four-body cascades are not yet included, so the
    total width and branching fractions are explicitly marked incomplete.

The narrow-width ratio is reported continuously. The optional threshold used
for a diagnostic label is a user-set bookkeeping convention, not a Belle II
published detector-resolution criterion.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
from pathlib import Path

import numpy as np

from radial_scalar_widths import (
    HBAR_C_GEV_M, M_MU_GEV, M_TAU_GEV,
    fermion_pair_width, photon_pair_width_lepton_loops,
    vector_pair_width,
)
from off_shell_cascades import (
    aprime_decay_widths, off_shell_aprime_three_body_width,
)


def log_grid(lo: float, hi: float, n: int) -> np.ndarray:
    if lo <= 0 or hi <= lo or n < 2:
        raise ValueError("log grid requires 0 < lo < hi and n >= 2")
    return np.geomspace(lo, hi, n)


def evaluate_scan_point(ms: float, mA: float, gX: float,
                         theta_mu_R: float, theta_tau_R: float,
                         quadrature_order: int, narrow_ratio: float) -> dict:
    vs = mA / (2.0 * gX)
    lam = ms * ms / (2.0 * vs * vs)
    ymu, ytau = M_MU_GEV / vs, M_TAU_GEV / vs

    widths = {
        "mu_mu": fermion_pair_width(ms, ymu, M_MU_GEV),
        "tau_tau": fermion_pair_width(ms, ytau, M_TAU_GEV),
        "A_A_on_shell": vector_pair_width(ms, mA, vs),
        "gamma_gamma_mu_tau_loops": photon_pair_width_lepton_loops(ms, vs),
        "A_nu_nu_mu_mu_tau_tau_three_body": 0.0,
    }
    if mA < 0.5 * ms:
        regime = "on_shell_AA"
        complete_at_declared_tree_level = True
    elif mA < ms:
        regime = "one_on_shell_one_virtual_A_three_body"
        cascade = off_shell_aprime_three_body_width(
            ms, mA, gX, theta_mu_R=theta_mu_R,
            theta_tau_R=theta_tau_R, quadrature_order=quadrature_order,
        )
        widths["A_nu_nu_mu_mu_tau_tau_three_body"] = cascade["total"]
        complete_at_declared_tree_level = True
    else:
        regime = "two_virtual_A_four_body_missing"
        complete_at_declared_tree_level = False

    # The on-shell A' decay pattern is part of the cascade topology. No
    # electron coupling is introduced; only nu_mu, nu_tau, mu, tau are used.
    aprime = aprime_decay_widths(
        mA, gX, theta_mu_R=theta_mu_R, theta_tau_R=theta_tau_R
    )

    total_included = sum(widths.values())
    gamma_over_mass = total_included / ms
    fractions = {
        name: width / total_included if total_included > 0 else 0.0
        for name, width in widths.items()
    }
    return {
        "ms_GeV": ms, "mA_GeV": mA, "gX": gX, "vs_GeV": vs,
        "lambdaS": lam, "passes_lambdaS_le_4pi": lam <= 4.0 * math.pi,
        "y_smu": ymu, "y_stau": ytau,
        **{f"Gamma_{k}_GeV": v for k, v in widths.items()},
        "Gamma_s_included_GeV": total_included,
        "Gamma_s_over_ms": gamma_over_mass,
        "ctau_s_from_included_widths_m": (
            HBAR_C_GEV_M / total_included if total_included > 0 else math.inf
        ),
        "narrow_ratio_below_user_threshold": gamma_over_mass < narrow_ratio,
        "narrow_ratio_threshold_used": narrow_ratio,
        "branching_fractions_complete": complete_at_declared_tree_level,
        "width_regime": regime,
        **{f"fraction_{k}": v for k, v in fractions.items()},
        "A_width_GeV": aprime["total_width_GeV"],
        "A_ctau_m": aprime["ctau_m"],
        "A_BR_nunu": aprime["branching_fractions"]["nu_nu"],
        "A_BR_mumu": aprime["branching_fractions"]["mu_mu"],
        "A_BR_tautau": aprime["branching_fractions"]["tau_tau"],
        "portal_width_included": False,
        "VLL_loop_width_included": False,
        "four_body_A_virtual_cascade_included": False,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--ms-min", type=float, default=0.212)
    p.add_argument("--ms-max", type=float, default=10.0)
    p.add_argument("--ms-points", type=int, default=48)
    p.add_argument("--mA-min", type=float, default=1.0e-3)
    p.add_argument("--mA-max", type=float, default=100.0)
    p.add_argument("--mA-points", type=int, default=48)
    p.add_argument("--gX-min", type=float, default=1.0e-6)
    p.add_argument("--gX-max", type=float, default=1.0e-1)
    p.add_argument("--gX-points", type=int, default=32)
    p.add_argument("--theta-mu-R", type=float, default=1.0e-2)
    p.add_argument("--theta-tau-R", type=float, default=1.0e-2)
    p.add_argument("--quadrature-order", type=int, default=192)
    p.add_argument("--narrow-ratio", type=float, default=1.0e-2,
                   help="diagnostic Gamma/m threshold only; not a Belle II resolution")
    args = p.parse_args()

    ms_grid = log_grid(args.ms_min, args.ms_max, args.ms_points)
    mA_grid = log_grid(args.mA_min, args.mA_max, args.mA_points)
    gX_grid = log_grid(args.gX_min, args.gX_max, args.gX_points)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_dir / "original_uv_width_scan.csv"
    summary_path = args.output_dir / "original_uv_width_scan_summary.json"

    counts = {}
    n_total = 0
    n_pert = 0
    n_complete = 0
    n_narrow = 0
    min_ratio = math.inf
    max_ratio = 0.0
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = None
        for ms, mA, gX in itertools.product(ms_grid, mA_grid, gX_grid):
            row = evaluate_scan_point(
                float(ms), float(mA), float(gX),
                args.theta_mu_R, args.theta_tau_R,
                args.quadrature_order, args.narrow_ratio,
            )
            if writer is None:
                writer = csv.DictWriter(f, fieldnames=list(row))
                writer.writeheader()
            writer.writerow(row)
            n_total += 1
            n_pert += int(row["passes_lambdaS_le_4pi"])
            n_complete += int(row["branching_fractions_complete"])
            n_narrow += int(row["narrow_ratio_below_user_threshold"])
            min_ratio = min(min_ratio, row["Gamma_s_over_ms"])
            max_ratio = max(max_ratio, row["Gamma_s_over_ms"])
            counts[row["width_regime"]] = counts.get(row["width_regime"], 0) + 1

    summary = {
        "scope": "original single-VEV S+VLL field content; zero-portal and decoupled-VLL benchmark",
        "scan": {
            "ms_GeV": [args.ms_min, args.ms_max, args.ms_points],
            "mA_GeV": [args.mA_min, args.mA_max, args.mA_points],
            "gX": [args.gX_min, args.gX_max, args.gX_points],
            "theta_mu_R": args.theta_mu_R,
            "theta_tau_R": args.theta_tau_R,
            "quadrature_order": args.quadrature_order,
        },
        "counts": {
            "total_points": n_total,
            "lambdaS_le_4pi_points": n_pert,
            "width_complete_at_declared_tree_level_points": n_complete,
            "points_below_user_Gamma_over_mass_threshold": n_narrow,
            "by_width_regime": counts,
        },
        "Gamma_over_ms_included_min": min_ratio,
        "Gamma_over_ms_included_max": max_ratio,
        "interpretation": [
            "Gamma_s/m_s is reported as a continuous diagnostic; 1e-2 is a user-configurable bookkeeping threshold, not an experimentally established Belle II resolution criterion.",
            "Points with mA >= ms omit two-virtual-A' four-body cascades and are flagged incomplete.",
            "Portal-mediated widths and non-decoupled VLL effects are not included in this benchmark.",
            "Where the width is incomplete, the reported lifetime is an upper bound from included widths, not a physical lifetime prediction.",
            "No detector-level recast or experimental exclusion is produced by this scan."
        ],
        "output_csv": csv_path.name,
    }
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
