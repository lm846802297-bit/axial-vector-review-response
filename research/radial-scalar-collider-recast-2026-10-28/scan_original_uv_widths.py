#!/usr/bin/env python3
"""Grid scan of the original one-VEV radial-scalar widths.

Scope: original S + VLL model only; no extra scalar, VEV, or RH neutrinos.
Benchmark: negligible Higgs portal and decoupled VLLs. This is a width and
lifetime study, not a Belle II recast.

Regimes:
  mA < ms/2: on-shell A'A' two-body channel;
  ms/2 <= mA < ms: one-on-shell/one-virtual A' three-body cascades;
  mA >= ms: double-virtual A' four-body contribution plus a conservative
            identical-pair exchange upper bound.

The double-virtual result is factorized. Identical-flavor exchange is bounded
rather than explicitly integrated. Its upper bound is retained in the total
width and direct-branching-fraction intervals. No arbitrary Gamma/m cut is
used as an experimental narrow-resonance criterion.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
from functools import lru_cache
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
from off_shell_four_body import fourbody_spectral_widths
from belleii_resolution_promptness import (
    TRACK_DCA_TRANSVERSE_M, TRACK_DCA_LONGITUDINAL_M,
    scalar_beta_gamma_lab_max, aprime_beta_gamma_lab_max,
    fourmu_width_resolution_ratios, tau_width_resolution_ratios,
)


FOURBODY_REFERENCE_GX = 0.1


def log_grid(lo: float, hi: float, n: int) -> np.ndarray:
    if lo <= 0 or hi <= lo or n < 2:
        raise ValueError("log grid requires 0 < lo < hi and n >= 2")
    return np.geomspace(lo, hi, n)


@lru_cache(maxsize=2048)
def _fourbody_reference(ms: float, mA: float, order: int,
                        theta_mu_R: float, theta_tau_R: float) -> tuple[float, float, float]:
    """Cache gX=0.1 double-virtual result; off-shell widths scale as gX^6."""
    r = fourbody_spectral_widths(
        ms, mA, FOURBODY_REFERENCE_GX, quadrature_order=order,
        theta_mu_R=theta_mu_R, theta_tau_R=theta_tau_R,
    )
    return (
        r["total_diagonal_pairing_GeV"],
        r["same_species_diagonal_GeV"],
        r["identical_exchange_cauchy_upper_bound_GeV"],
    )


def evaluate_scan_point(
    ms: float, mA: float, gX: float,
    theta_mu_R: float = 1.0e-2,
    theta_tau_R: float = 1.0e-2,
    threebody_quadrature_order: int = 192,
    fourbody_quadrature_order: int = 128,
) -> dict:
    vs = mA / (2.0 * gX)
    lam = ms * ms / (2.0 * vs * vs)
    ymu, ytau = M_MU_GEV / vs, M_TAU_GEV / vs

    widths = {
        "mu_mu": fermion_pair_width(ms, ymu, M_MU_GEV),
        "tau_tau": fermion_pair_width(ms, ytau, M_TAU_GEV),
        "A_A_on_shell": vector_pair_width(ms, mA, vs),
        "gamma_gamma_mu_tau_loops": photon_pair_width_lepton_loops(ms, vs),
        "A_nu_nu_mu_mu_tau_tau_three_body": 0.0,
        "Astar_Astar_four_fermion_diagonal": 0.0,
    }
    fourbody_same_species = 0.0
    fourbody_upper = 0.0
    fourbody_status = "not_kinematically_open"
    exact_widths_under_benchmark = True

    if mA < 0.5 * ms:
        regime = "on_shell_AA"
    elif mA < ms:
        regime = "one_on_shell_one_virtual_A_three_body"
        cascade = off_shell_aprime_three_body_width(
            ms, mA, gX, theta_mu_R=theta_mu_R,
            theta_tau_R=theta_tau_R,
            quadrature_order=threebody_quadrature_order,
        )
        widths["A_nu_nu_mu_mu_tau_tau_three_body"] = cascade["total"]
    else:
        regime = "two_virtual_A_four_body_bounded"
        ref_diag, ref_same, ref_upper = _fourbody_reference(
            float(ms), float(mA), int(fourbody_quadrature_order),
            float(theta_mu_R), float(theta_tau_R),
        )
        scale = (gX / FOURBODY_REFERENCE_GX)**6
        widths["Astar_Astar_four_fermion_diagonal"] = ref_diag * scale
        fourbody_same_species = ref_same * scale
        fourbody_upper = ref_upper * scale
        fourbody_status = "diagonal_factorization_with_Cauchy_exchange_upper_bound"
        exact_widths_under_benchmark = False

    aprime = aprime_decay_widths(
        mA, gX, theta_mu_R=theta_mu_R, theta_tau_R=theta_tau_R
    )

    total_diagonal = sum(widths.values())
    direct_total = total_diagonal - widths["Astar_Astar_four_fermion_diagonal"]
    total_upper = direct_total + fourbody_upper
    gamma_over_mass = total_diagonal / ms
    gamma_over_mass_lower = direct_total / ms
    gamma_over_mass_upper = total_upper / ms

    fractions_diagonal = {
        name: width / total_diagonal if total_diagonal > 0 else 0.0
        for name, width in widths.items()
    }
    direct_channel_intervals = {}
    for name, width in widths.items():
        if name == "Astar_Astar_four_fermion_diagonal":
            continue
        direct_channel_intervals[f"BR_{name}_min"] = (
            width / total_upper if total_upper > 0 else 0.0
        )
        direct_channel_intervals[f"BR_{name}_max"] = (
            width / direct_total if direct_total > 0 else 0.0
        )

    beta_gamma_s_max = scalar_beta_gamma_lab_max(ms)
    scalar_flight_min = beta_gamma_s_max * HBAR_C_GEV_M / total_upper if total_upper > 0 else math.inf
    scalar_flight_max = beta_gamma_s_max * HBAR_C_GEV_M / direct_total if direct_total > 0 else math.inf
    beta_gamma_A_max = aprime_beta_gamma_lab_max(ms, mA)
    A_flight_max = beta_gamma_A_max * aprime["ctau_m"] if beta_gamma_A_max is not None else None

    fourmu_lower = fourmu_width_resolution_ratios(ms, direct_total)
    fourmu_upper = fourmu_width_resolution_ratios(ms, total_upper)
    fourmu_resolution = {}
    if fourmu_lower is not None and fourmu_upper is not None:
        fourmu_resolution = {
            "fourmu_Gamma_MR_lower_GeV": fourmu_lower["Gamma_MR_GeV"],
            "fourmu_Gamma_MR_upper_GeV": fourmu_upper["Gamma_MR_GeV"],
            "fourmu_sigma_MR_min_GeV": fourmu_lower["sigma_MR_min_GeV"],
            "fourmu_sigma_MR_max_GeV": fourmu_lower["sigma_MR_max_GeV"],
            "fourmu_Gamma_over_sigma_lower_bound": fourmu_lower["Gamma_over_sigma_upper_resolution"],
            "fourmu_Gamma_over_sigma_upper_bound": fourmu_upper["Gamma_over_sigma_lower_resolution"],
            "fourmu_mass_in_published_scan": not (3.07 <= ms <= 3.12),
        }
    else:
        fourmu_resolution = {
            "fourmu_Gamma_MR_lower_GeV": None,
            "fourmu_Gamma_MR_upper_GeV": None,
            "fourmu_sigma_MR_min_GeV": None,
            "fourmu_sigma_MR_max_GeV": None,
            "fourmu_Gamma_over_sigma_lower_bound": None,
            "fourmu_Gamma_over_sigma_upper_bound": None,
            "fourmu_mass_in_published_scan": False,
        }

    tau_lower = tau_width_resolution_ratios(ms, direct_total)
    tau_upper = tau_width_resolution_ratios(ms, total_upper)
    if tau_lower is not None and tau_upper is not None:
        tau_resolution = {
            "tau_sigma_recoil_min_GeV": tau_lower["sigma_recoil_min_GeV"],
            "tau_sigma_recoil_max_GeV": tau_lower["sigma_recoil_max_GeV"],
            "tau_Gamma_over_sigma_lower_bound": tau_lower["Gamma_over_sigma_lower_resolution"],
            "tau_Gamma_over_sigma_upper_bound": tau_upper["Gamma_over_sigma_upper_resolution"],
            "tau_mass_in_published_scan": True,
        }
    else:
        tau_resolution = {
            "tau_sigma_recoil_min_GeV": None,
            "tau_sigma_recoil_max_GeV": None,
            "tau_Gamma_over_sigma_lower_bound": None,
            "tau_Gamma_over_sigma_upper_bound": None,
            "tau_mass_in_published_scan": False,
        }

    return {
        "ms_GeV": ms, "mA_GeV": mA, "gX": gX, "vs_GeV": vs,
        "lambdaS": lam, "passes_lambdaS_le_4pi": lam <= 4.0 * math.pi,
        "y_smu": ymu, "y_stau": ytau,
        **{f"Gamma_{k}_GeV": v for k, v in widths.items()},
        "Gamma_4f_same_species_diagonal_GeV": fourbody_same_species,
        "Gamma_4f_identical_exchange_upper_GeV": fourbody_upper,
        "fourbody_status": fourbody_status,
        "fourbody_identical_exchange_explicitly_integrated": False,
        "fourbody_upper_over_direct_widths": (
            fourbody_upper / direct_total if direct_total > 0 else 0.0
        ),
        "Gamma_s_factorized_diagonal_GeV": total_diagonal,
        "Gamma_s_upper_bound_GeV": total_upper,
        "Gamma_s_over_ms_factorized_diagonal": gamma_over_mass,
        "Gamma_s_over_ms_lower_bound": gamma_over_mass_lower,
        "Gamma_s_over_ms_upper_bound": gamma_over_mass_upper,
        "ctau_s_factorized_diagonal_m": (
            HBAR_C_GEV_M / total_diagonal if total_diagonal > 0 else math.inf
        ),
        "ctau_s_lower_bound_m": (
            HBAR_C_GEV_M / total_upper if total_upper > 0 else math.inf
        ),
        "ctau_s_upper_bound_m": (
            HBAR_C_GEV_M / direct_total if direct_total > 0 else math.inf
        ),
        "beta_gamma_s_lab_kinematic_max": beta_gamma_s_max,
        "scalar_mean_lab_flight_max_lower_m": scalar_flight_min,
        "scalar_mean_lab_flight_max_upper_m": scalar_flight_max,
        "scalar_flight_upper_over_track_DCA_transverse": scalar_flight_max / TRACK_DCA_TRANSVERSE_M,
        "scalar_flight_upper_over_track_DCA_longitudinal": scalar_flight_max / TRACK_DCA_LONGITUDINAL_M,
        "beta_gamma_A_lab_kinematic_max": beta_gamma_A_max,
        "A_mean_lab_flight_max_m": A_flight_max,
        **fourmu_resolution,
        **tau_resolution,
        "branching_fractions_exact_under_declared_benchmark": exact_widths_under_benchmark,
        "branching_fractions_bounded_under_declared_benchmark": True,
        "width_regime": regime,
        **{f"fraction_diagonal_{k}": v for k, v in fractions_diagonal.items()},
        **direct_channel_intervals,
        "A_width_GeV": aprime["total_width_GeV"],
        "A_ctau_m": aprime["ctau_m"],
        "A_BR_nunu": aprime["branching_fractions"]["nu_nu"],
        "A_BR_mumu": aprime["branching_fractions"]["mu_mu"],
        "A_BR_tautau": aprime["branching_fractions"]["tau_tau"],
        "portal_width_included": False,
        "VLL_loop_width_included": False,
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
    p.add_argument("--threebody-quadrature-order", type=int, default=192)
    p.add_argument("--fourbody-quadrature-order", type=int, default=128)
    args = p.parse_args()

    ms_grid = log_grid(args.ms_min, args.ms_max, args.ms_points)
    mA_grid = log_grid(args.mA_min, args.mA_max, args.mA_points)
    gX_grid = log_grid(args.gX_min, args.gX_max, args.gX_points)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_dir / "original_uv_width_scan.csv"
    summary_path = args.output_dir / "original_uv_width_scan_summary.json"

    counts = {}
    n_total = n_pert = n_exact = n_bounded = 0
    max_fourbody_ratio = 0.0
    min_gamma_ratio = math.inf
    max_gamma_ratio = 0.0

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = None
        for ms, mA, gX in itertools.product(ms_grid, mA_grid, gX_grid):
            row = evaluate_scan_point(
                float(ms), float(mA), float(gX),
                args.theta_mu_R, args.theta_tau_R,
                args.threebody_quadrature_order,
                args.fourbody_quadrature_order,
            )
            if writer is None:
                writer = csv.DictWriter(f, fieldnames=list(row))
                writer.writeheader()
            writer.writerow(row)
            n_total += 1
            n_pert += int(row["passes_lambdaS_le_4pi"])
            n_exact += int(row["branching_fractions_exact_under_declared_benchmark"])
            n_bounded += int(row["branching_fractions_bounded_under_declared_benchmark"])
            max_fourbody_ratio = max(max_fourbody_ratio, row["fourbody_upper_over_direct_widths"])
            min_gamma_ratio = min(min_gamma_ratio, row["Gamma_s_over_ms_lower_bound"])
            max_gamma_ratio = max(max_gamma_ratio, row["Gamma_s_over_ms_upper_bound"])
            counts[row["width_regime"]] = counts.get(row["width_regime"], 0) + 1

    summary = {
        "scope": "original single-VEV S+VLL field content; zero-portal and decoupled-VLL benchmark",
        "scan": {
            "ms_GeV": [args.ms_min, args.ms_max, args.ms_points],
            "mA_GeV": [args.mA_min, args.mA_max, args.mA_points],
            "gX": [args.gX_min, args.gX_max, args.gX_points],
            "theta_mu_R": args.theta_mu_R,
            "theta_tau_R": args.theta_tau_R,
            "threebody_quadrature_order": args.threebody_quadrature_order,
            "fourbody_quadrature_order": args.fourbody_quadrature_order,
        },
        "counts": {
            "total_points": n_total,
            "lambdaS_le_4pi_points": n_pert,
            "exact_primary_width_points_under_declared_benchmark": n_exact,
            "points_with_bounded_branching_fractions": n_bounded,
            "by_width_regime": counts,
        },
        "max_fourbody_identical_exchange_upper_over_direct_widths": max_fourbody_ratio,
        "Gamma_s_over_ms_lower_bound_min": min_gamma_ratio,
        "Gamma_s_over_ms_upper_bound_max": max_gamma_ratio,
        "interpretation": [
            "The mA >= ms four-body contribution is a double-spectral diagonal-pairing result; identical-flavor exchange is bounded but not explicitly integrated.",
            "For mA >= ms, the four-body width scales as gX^6 when the off-shell absorptive term is neglected; its effect on direct branching fractions is enclosed by the reported intervals.",
            "The portal is set to zero and VLLs are decoupled by benchmark; these are assumptions, not symmetry-enforced results.",
            "No Belle II detector-level recast or experimental exclusion is produced by this scan.",
        ],
        "output_csv": csv_path.name,
    }
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
