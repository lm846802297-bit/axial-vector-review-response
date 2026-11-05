#!/usr/bin/env python3
"""Conditional narrow-width/prompt benchmark reinterpretation of Belle II scalar limits.

Scope: original paper's single-VEV S+VLL model only:
    mA = 2 gX vs, ms^2 = 2 lambdaS vs^2, y_sll = ml/vs.

This does NOT rerun Belle II CLs fits or detector simulation. It maps published
scalar coupling limits onto UV points only when the archived width table marks
the branching-fraction sum complete, the point passes lambdaS<=4pi, and
conservative narrow-width / flight-scale diagnostics are satisfied.

Rows marked branching_fractions_complete=False remain unclassified. In
particular, an older scan artifact may predate the double-virtual four-body
width update; this script never fills such missing branching fractions by
renormalizing an incomplete partial-width sum.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np

M_E_GEV = 0.00051099895
M_MU_GEV = 0.1056583755
M_TAU_GEV = 1.77686
V_EW_GEV = 246.0
SQRT_S_GEV = 10.58
BETA_GAMMA_CM = 0.28
GAMMA_CM = math.sqrt(1.0 + BETA_GAMMA_CM**2)
BETA_CM = BETA_GAMMA_CM / GAMMA_CM
TRACK_DCA_TRANSVERSE_M = 0.005
NARROW_WIDTH_RATIO_TOLERANCE = 0.10  # internal diagnostic, not a Belle II cut


def _unique_sorted(x, *ys):
    order = np.argsort(x, kind="mergesort")
    x = np.asarray(x)[order]
    ys = [np.asarray(y)[order] for y in ys]
    keep = np.r_[True, np.diff(x) > 1e-10]
    return (x[keep], *(y[keep] for y in ys))


def _read_fourmu_limits(path: Path):
    raw = np.loadtxt(path, skiprows=1)
    if raw.ndim != 2 or raw.shape[1] != 15:
        raise ValueError(f"expected 15 numeric columns in {path}, got {raw.shape}")
    x, y_obs, y_exp = _unique_sorted(raw[:, 0], raw[:, 7], raw[:, 8])
    return ((x, y_obs), (x, y_exp)), {
        "rows_raw": int(raw.shape[0]),
        "rows_unique": int(len(x)),
        "mass_min_GeV": float(raw[:, 0].min()),
        "mass_max_GeV": float(raw[:, 0].max()),
    }


def _read_tau_limits(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    rows = [{k.strip(): v for k, v in r.items()} for r in rows]
    if not rows:
        raise ValueError(f"empty tau-pair limit table: {path}")
    mass = np.array([float(r["m [GeV/c^2]"]) for r in rows])
    xi_obs = np.array([float(r["xi_UL_obs"]) for r in rows])
    xi_exp = np.array([float(r["xi_UL_exp"]) for r in rows])
    x, y_obs, y_exp = _unique_sorted(mass, xi_obs, xi_exp)
    return ((x, y_obs), (x, y_exp)), {
        "rows_raw": len(rows),
        "rows_unique": int(len(x)),
        "mass_min_GeV": float(mass.min()),
        "mass_max_GeV": float(mass.max()),
    }


def _log_interp(x, xp, yp):
    if x < xp[0] or x > xp[-1]:
        raise ValueError(f"mass {x} outside limit table [{xp[0]}, {xp[-1]}]")
    return math.exp(float(np.interp(math.log(x), np.log(xp), np.log(yp))))


def _partial_weight(mass, ml):
    if mass <= 2.0 * ml:
        return 0.0
    beta2 = 1.0 - 4.0 * ml * ml / (mass * mass)
    return ml * ml * beta2**1.5


def tau_reference_branching_fraction(mass):
    """Belle mass-proportional scalar BR(tau tau), with e, mu, tau channels."""
    weights = [_partial_weight(mass, ml)
               for ml in (M_E_GEV, M_MU_GEV, M_TAU_GEV)]
    total = sum(weights)
    return weights[2] / total if total > 0 else 0.0


def scalar_beta_gamma_lab_max(mass):
    """Kinematic maximum for ee -> mu mu s, dimuon recoil at threshold."""
    s = SQRT_S_GEV**2
    energy_cm = (s + mass**2 - 4.0 * M_MU_GEV**2) / (2.0 * SQRT_S_GEV)
    momentum_cm = math.sqrt(max(0.0, energy_cm**2 - mass**2))
    return GAMMA_CM * (momentum_cm + BETA_CM * energy_cm) / mass


def fourmu_resolution_envelope(mass):
    """Published reduced-mass resolution envelope, GeV."""
    if mass < 1.0:
        return 0.0020, 0.0025
    # Published text: smooth rise to ~5 MeV near 5 GeV, fall to 2.5 MeV at 9.
    # Use the conservative envelope until mass-dependent response parameters exist.
    return 0.0025, 0.0050


def tau_resolution_envelope(mass):
    """Anchor-based published recoil-mass resolution envelope, GeV."""
    if mass < 6.0:
        return 0.010, 0.030
    if mass <= 6.6:
        return 0.010, 0.010
    if mass < 10.0:
        return 0.001, 0.010
    return 0.001, 0.001


def _bool(value):
    return str(value).strip().lower() in ("true", "1", "yes")


def _base_classification(row, channel):
    mass = float(row["ms_GeV"])
    if not _bool(row["passes_lambdaS_le_4pi"]):
        return "theoretically_inconsistent_lambdaS"
    if channel == "fourmu" and 3.07 <= mass <= 3.12:
        return "unclassified_experimental_Jpsi_veto"
    if not _bool(row["branching_fractions_complete"]):
        return "unclassified_incomplete_width_sum"
    return None


def evaluate_row(row, channel, limits):
    mass = float(row["ms_GeV"])
    result = {
        "channel": channel,
        "ms_GeV": mass,
        "mA_GeV": float(row["mA_GeV"]),
        "gX": float(row["gX"]),
        "vs_GeV": float(row["vs_GeV"]),
        "lambdaS": float(row["lambdaS"]),
        "passes_lambdaS_le_4pi": _bool(row["passes_lambdaS_le_4pi"]),
        "width_regime": row["width_regime"],
        "branching_fractions_complete": _bool(row["branching_fractions_complete"]),
        "Gamma_s_GeV": float(row["Gamma_s_included_GeV"]),
        "ctau_s_m": float(row["ctau_s_from_included_widths_m"]),
    }
    base = _base_classification(row, channel)
    if base:
        result["classification"] = base
        return result
    limit_mass_max = float(limits[0][0][-1])
    if mass > limit_mass_max:
        result["classification"] = "unclassified_outside_numerical_limit_grid"
        return result

    gamma = result["Gamma_s_GeV"]
    beta_gamma_max = scalar_beta_gamma_lab_max(mass)
    flight_max = beta_gamma_max * result["ctau_s_m"]
    result["beta_gamma_scalar_kinematic_max"] = beta_gamma_max
    result["mean_lab_flight_max_m"] = flight_max
    result["flight_max_over_transverse_DCA"] = flight_max / TRACK_DCA_TRANSVERSE_M
    # This is a geometry-scale screen only, not a detector efficiency calculation.
    prompt_proxy = flight_max < TRACK_DCA_TRANSVERSE_M
    result["mean_flight_below_5mm_proxy"] = prompt_proxy

    if channel == "fourmu":
        br_uv = float(row["fraction_mu_mu"])
        if br_uv <= 0.0:
            result["classification"] = "unclassified_zero_muon_branching_fraction"
            return result
        reduced_mass = math.sqrt(max(mass * mass - 4.0 * M_MU_GEV**2, 1e-300))
        gamma_fit = gamma * mass / reduced_mass
        sigma_min, sigma_max = fourmu_resolution_envelope(mass)
        lim_obs = _log_interp(mass, *limits[0])
        lim_exp = _log_interp(mass, *limits[1])
        coupling_uv = float(row["y_smu"])
        ratio_over_sigma_min = gamma_fit / sigma_min
        ratio_over_sigma_max = gamma_fit / sigma_max
        strength_obs = (coupling_uv / lim_obs)**2 * br_uv
        strength_exp = (coupling_uv / lim_exp)**2 * br_uv
        result.update({
            "BR_UV_signal": br_uv,
            "BR_benchmark_signal": 1.0,
            "UV_coupling": coupling_uv,
            "published_coupling_limit_observed": lim_obs,
            "published_coupling_limit_expected": lim_exp,
            "UV_coupling_limit_observed_BR_corrected": lim_obs / math.sqrt(br_uv),
            "UV_coupling_limit_expected_BR_corrected": lim_exp / math.sqrt(br_uv),
            "Gamma_fit_variable_GeV": gamma_fit,
            "sigma_resolution_min_GeV": sigma_min,
            "sigma_resolution_max_GeV": sigma_max,
            "Gamma_over_sigma_min_resolution": ratio_over_sigma_min,
            "Gamma_over_sigma_max_resolution": ratio_over_sigma_max,
            "signal_strength_ratio_observed": strength_obs,
            "signal_strength_ratio_expected": strength_exp,
        })
    else:
        br_uv = float(row["fraction_tau_tau"])
        br_ref = tau_reference_branching_fraction(mass)
        if br_uv <= 0.0 or br_ref <= 0.0:
            result["classification"] = "unclassified_zero_tau_branching_fraction"
            return result
        sigma_min, sigma_max = tau_resolution_envelope(mass)
        lim_obs = _log_interp(mass, *limits[0])
        lim_exp = _log_interp(mass, *limits[1])
        coupling_uv = V_EW_GEV / result["vs_GeV"]
        ratio_over_sigma_min = gamma / sigma_min
        ratio_over_sigma_max = gamma / sigma_max
        strength_obs = (coupling_uv / lim_obs)**2 * (br_uv / br_ref)
        strength_exp = (coupling_uv / lim_exp)**2 * (br_uv / br_ref)
        result.update({
            "BR_UV_signal": br_uv,
            "BR_benchmark_signal": br_ref,
            "UV_coupling": coupling_uv,
            "published_coupling_limit_observed": lim_obs,
            "published_coupling_limit_expected": lim_exp,
            "UV_coupling_limit_observed_BR_corrected": lim_obs * math.sqrt(br_ref / br_uv),
            "UV_coupling_limit_expected_BR_corrected": lim_exp * math.sqrt(br_ref / br_uv),
            "Gamma_fit_variable_GeV": gamma,
            "sigma_resolution_min_GeV": sigma_min,
            "sigma_resolution_max_GeV": sigma_max,
            "Gamma_over_sigma_min_resolution": ratio_over_sigma_min,
            "Gamma_over_sigma_max_resolution": ratio_over_sigma_max,
            "signal_strength_ratio_observed": strength_obs,
            "signal_strength_ratio_expected": strength_exp,
        })

    # Require Gamma/sigma_min < 0.1 across the full resolution envelope.
    # This is an internal tolerance, not a Belle II selection or published cut.
    narrow_proxy = result["Gamma_over_sigma_min_resolution"] < NARROW_WIDTH_RATIO_TOLERANCE
    result["narrow_template_proxy_pass"] = narrow_proxy
    if not narrow_proxy:
        result["classification"] = "finite_width_sensitive"
    elif not prompt_proxy:
        result["classification"] = "lifetime_sensitive"
    elif strength_obs > 1.0:
        result["classification"] = "excluded_under_published_narrow_prompt_benchmark_conditional"
    else:
        result["classification"] = "evaluated_not_excluded_by_this_channel_conditional"
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scan", type=Path, required=True)
    p.add_argument("--fourmu-limits", type=Path, required=True)
    p.add_argument("--tau-limits", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    args = p.parse_args()

    fourmu_limits, fourmu_meta = _read_fourmu_limits(args.fourmu_limits)
    tau_limits, tau_meta = _read_tau_limits(args.tau_limits)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_paths = {
        "fourmu": args.output_dir / "belleii_4mu_narrow_prompt_uv_recast.csv",
        "tautau": args.output_dir / "belleii_tautau_narrow_prompt_uv_recast.csv",
    }
    counts = {ch: Counter() for ch in output_paths}
    input_rows = 0

    with args.scan.open(newline="", encoding="utf-8") as sf:
        reader = csv.DictReader(sf)
        with output_paths["fourmu"].open("w", newline="", encoding="utf-8") as f4, \
             output_paths["tautau"].open("w", newline="", encoding="utf-8") as ft:
            writers = {"fourmu": None, "tautau": None}
            for row in reader:
                input_rows += 1
                mass = float(row["ms_GeV"])
                if 0.212 <= mass <= 9.0:
                    rec = evaluate_row(row, "fourmu", fourmu_limits)
                    counts["fourmu"][rec["classification"]] += 1
                    if writers["fourmu"] is None:
                        writers["fourmu"] = csv.DictWriter(f4, fieldnames=list(rec))
                        writers["fourmu"].writeheader()
                    writers["fourmu"].writerow(rec)
                if 3.6 <= mass <= 10.0:
                    rec = evaluate_row(row, "tautau", tau_limits)
                    counts["tautau"][rec["classification"]] += 1
                    if writers["tautau"] is None:
                        writers["tautau"] = csv.DictWriter(ft, fieldnames=list(rec))
                        writers["tautau"].writeheader()
                    writers["tautau"].writerow(rec)

    summary = {
        "scope": "original one-VEV S+VLL model; no neutrino-sector extension",
        "scan_rows": input_rows,
        "fourmu_limit_data": fourmu_meta,
        "tau_limit_data": tau_meta,
        "mass_interpolation": "linear interpolation in log(coupling limit) versus log(mass); no extrapolation",
        "narrow_width_tolerance": NARROW_WIDTH_RATIO_TOLERANCE,
        "narrow_width_tolerance_note": "internal conservative diagnostic, not a Belle II cut",
        "promptness_note": "maximum-kinematic mean lab flight length compared with 5 mm transverse DCA scale; geometry proxy only, not detector efficiency or proof of prompt acceptance",
        "fourmu_resolution_note": "published reduced-mass resolution envelope; exact mass-dependent Crystal Ball parameters are not public in the archived source",
        "tau_resolution_note": "anchor-based conservative recoil-mass resolution envelope, not a reconstructed pointwise response",
        "coupling_mappings": {
            "fourmu": "y_smu = m_mu/v_s; compare y_smu^2 * BR_UV(mumu) with gS_UL^2; benchmark BR_ref=1",
            "tautau": "xi_UV = v/v_s; compare xi_UV^2 * BR_UV(tautau)/BR_ref(tautau) with xi_UL^2; BR_ref includes e,mu,tau",
        },
        "classification_counts": {ch: dict(c) for ch, c in counts.items()},
        "limitations": [
            "Rows with branching_fractions_complete=False remain unclassified. In the currently archived 33-column scan CSV these are the double-virtual A' points; that artifact predates the later four-body bounded-width code update.",
            "The 5 mm flight-length comparison is a geometry proxy, not a lifetime-dependent detector efficiency.",
            "No finite-width convolution or event-level CLs fit is performed.",
            "No independent MadGraph production recalculation is performed; coupling scaling assumes the same spin-0 muon-FSR matrix element as the Belle benchmark.",
            "These are conditional reinterpretations of published scalar coupling limits, not new Belle II CLs results.",
        ],
        "outputs": {k: v.name for k, v in output_paths.items()},
    }
    (args.output_dir / "narrow_prompt_recast_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
