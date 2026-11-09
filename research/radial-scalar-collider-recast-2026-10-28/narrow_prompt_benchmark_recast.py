#!/usr/bin/env python3
"""Conservative Belle II reinterpretation using the regenerated bounded-width scan.

The scan supplies intervals for direct scalar branching fractions and for the
total scalar width in the double-virtual A' region. This program propagates
those intervals through the published scalar coupling limits. It does not
perform detector simulation, finite-width convolution, or a new CLs fit.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np

M_E_GEV = 0.00051099895
M_MU_GEV = 0.1056583755
M_TAU_GEV = 1.77686
V_EW_GEV = 246.0
NARROW_WIDTH_RATIO_TOLERANCE = 0.10
TRANSVERSE_DCA_PROXY_M = 0.005


def _unique_sorted(x, *ys):
    order = np.argsort(x, kind="mergesort")
    x = np.asarray(x, dtype=float)[order]
    ys = [np.asarray(y, dtype=float)[order] for y in ys]
    keep = np.r_[True, np.diff(x) > 1.0e-10]
    return (x[keep], *(y[keep] for y in ys))


def _read_fourmu_limits(path: Path):
    raw = np.loadtxt(path, skiprows=1)
    if raw.ndim != 2 or raw.shape[1] != 15:
        raise ValueError(f"expected 15 numeric columns in {path}, got {raw.shape}")
    x, y_obs, y_exp = _unique_sorted(raw[:, 0], raw[:, 7], raw[:, 8])
    if np.any(y_obs <= 0.0) or np.any(y_exp <= 0.0):
        raise ValueError("four-muon scalar coupling limits must be positive")
    return ((x, y_obs), (x, y_exp)), {
        "rows_raw": int(raw.shape[0]),
        "rows_unique": int(len(x)),
        "mass_min_GeV": float(raw[:, 0].min()),
        "mass_max_GeV": float(raw[:, 0].max()),
    }


def _read_tau_limits(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    rows = [{k.strip(): v.strip() for k, v in r.items()} for r in rows]
    if not rows:
        raise ValueError(f"empty tau-pair limit table: {path}")
    mass = np.array([float(r["m [GeV/c^2]"]) for r in rows])
    xi_obs = np.array([float(r["xi_UL_obs"]) for r in rows])
    xi_exp = np.array([float(r["xi_UL_exp"]) for r in rows])
    x, y_obs, y_exp = _unique_sorted(mass, xi_obs, xi_exp)
    if np.any(y_obs <= 0.0) or np.any(y_exp <= 0.0):
        raise ValueError("tau-pair scalar coupling limits must be positive")
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
    """Belle mass-proportional scalar BR(tau tau), including e, mu and tau."""
    weights = [_partial_weight(mass, ml)
               for ml in (M_E_GEV, M_MU_GEV, M_TAU_GEV)]
    total = sum(weights)
    return weights[2] / total if total > 0.0 else 0.0


def _as_bool(value):
    return str(value).strip().lower() in ("true", "1", "yes")


def _number(row, key):
    value = row.get(key)
    if value in (None, "", "None"):
        raise ValueError(f"missing required scan value {key}")
    out = float(value)
    if not math.isfinite(out):
        raise ValueError(f"non-finite scan value {key}")
    return out


def _limit_interval(mass, limits):
    lo = float(limits[0][0][0])
    hi = float(limits[0][0][-1])
    if mass < lo or mass > hi:
        return None
    return (_log_interp(mass, *limits[0]), _log_interp(mass, *limits[1]))


def _base_classification(row, channel, limit_interval):
    mass = _number(row, "ms_GeV")
    if not _as_bool(row.get("passes_lambdaS_le_4pi", "false")):
        return "theoretically_inconsistent_scalar_quartic"
    if not _as_bool(row.get("passes_scalar_yukawas_le_sqrt4pi", "false")):
        return "theoretically_inconsistent_scalar_yukawa"
    if channel == "fourmu" and 3.07 <= mass <= 3.12:
        return "unclassified_experimental_Jpsi_veto"
    if limit_interval is None:
        return "unclassified_outside_numerical_limit_grid"
    if not _as_bool(row.get("branching_fractions_bounded_under_declared_benchmark", "false")):
        return "unclassified_branching_fraction_not_bounded"
    return None


def _width_and_lifetime_status(row, channel):
    if channel == "fourmu":
        width_lo_key = "fourmu_Gamma_over_sigma_lower_bound"
        width_hi_key = "fourmu_Gamma_over_sigma_upper_bound"
    else:
        width_lo_key = "tau_Gamma_over_sigma_lower_bound"
        width_hi_key = "tau_Gamma_over_sigma_upper_bound"
    width_lo = _number(row, width_lo_key)
    width_hi = _number(row, width_hi_key)
    if width_lo < 0.0 or width_hi < width_lo:
        raise ValueError("invalid width/resolution interval")

    flight_lo = _number(row, "scalar_mean_lab_flight_max_lower_m")
    flight_hi = _number(row, "scalar_mean_lab_flight_max_upper_m")
    if flight_lo < 0.0 or flight_hi < flight_lo:
        raise ValueError("invalid scalar flight-length interval")

    if width_hi >= NARROW_WIDTH_RATIO_TOLERANCE:
        width_status = (
            "finite_width_sensitive"
            if width_lo >= NARROW_WIDTH_RATIO_TOLERANCE
            else "width_interval_straddles_narrow_threshold"
        )
    else:
        width_status = "narrow_proxy_pass"
    if flight_hi >= TRANSVERSE_DCA_PROXY_M:
        flight_status = (
            "lifetime_sensitive"
            if flight_lo >= TRANSVERSE_DCA_PROXY_M
            else "flight_interval_straddles_5mm_proxy"
        )
    else:
        flight_status = "prompt_geometry_proxy_pass"
    return {
        "width_ratio_min": width_lo,
        "width_ratio_max": width_hi,
        "flight_length_proxy_min_m": flight_lo,
        "flight_length_proxy_max_m": flight_hi,
        "narrow_width_proxy_pass": width_status == "narrow_proxy_pass",
        "prompt_geometry_proxy_pass": flight_status == "prompt_geometry_proxy_pass",
        "width_status": width_status,
        "flight_status": flight_status,
    }


def _record_classification_details(details, rec):
    """Accumulate mass coverage and conservative diagnostic extrema by class."""
    name = rec["classification"]
    bucket = details.setdefault(name, {
        "count": 0,
        "masses_GeV": [],
        "max_signal_strength_ratio_observed_min": None,
        "max_signal_strength_ratio_observed_max": None,
        "max_width_ratio_upper": None,
        "max_flight_length_proxy_upper_m": None,
    })
    bucket["count"] += 1
    bucket["masses_GeV"].append(float(rec["ms_GeV"]))
    for source, target in (
        ("signal_strength_ratio_observed_min", "max_signal_strength_ratio_observed_min"),
        ("signal_strength_ratio_observed_max", "max_signal_strength_ratio_observed_max"),
        ("width_ratio_max", "max_width_ratio_upper"),
        ("flight_length_proxy_max_m", "max_flight_length_proxy_upper_m"),
    ):
        value = rec.get(source)
        if value is not None:
            bucket[target] = value if bucket[target] is None else max(bucket[target], value)


def _finalize_classification_details(details):
    finalized = {}
    for name, bucket in details.items():
        masses = bucket.pop("masses_GeV")
        finalized[name] = {
            **bucket,
            "unique_mass_points": len(set(masses)),
            "mass_min_GeV": min(masses),
            "mass_max_GeV": max(masses),
        }
    return finalized


def evaluate_row(row, channel, limits):
    mass = _number(row, "ms_GeV")
    limit_interval = _limit_interval(mass, limits)
    result = {
        "channel": channel,
        "ms_GeV": mass,
        "mA_GeV": _number(row, "mA_GeV"),
        "gX": _number(row, "gX"),
        "vs_GeV": _number(row, "vs_GeV"),
        "lambdaS": _number(row, "lambdaS"),
        "passes_lambdaS_le_4pi": _as_bool(row.get("passes_lambdaS_le_4pi", "false")),
        "passes_scalar_yukawas_le_sqrt4pi": _as_bool(row.get("passes_scalar_yukawas_le_sqrt4pi", "false")),
        "width_regime": row.get("width_regime", "unknown"),
        "branching_fractions_bounded": _as_bool(
            row.get("branching_fractions_bounded_under_declared_benchmark", "false")
        ),
    }
    base = _base_classification(row, channel, limit_interval)
    if base:
        result["classification"] = base
        return result

    if channel == "fourmu":
        br_lo = _number(row, "BR_mu_mu_min")
        br_hi = _number(row, "BR_mu_mu_max")
        coupling_uv = _number(row, "y_smu")
        br_ref = 1.0
        limit_obs, limit_exp = limit_interval
        scale_obs = (coupling_uv / limit_obs) ** 2
        scale_exp = (coupling_uv / limit_exp) ** 2
        width = _width_and_lifetime_status(row, "fourmu")
    elif channel == "tautau":
        br_lo = _number(row, "BR_tau_tau_min")
        br_hi = _number(row, "BR_tau_tau_max")
        br_ref = tau_reference_branching_fraction(mass)
        if br_ref <= 0.0:
            result["classification"] = "unclassified_zero_reference_tau_branching_fraction"
            return result
        coupling_uv = V_EW_GEV / result["vs_GeV"]
        limit_obs, limit_exp = limit_interval
        scale_obs = (coupling_uv / limit_obs) ** 2 / br_ref
        scale_exp = (coupling_uv / limit_exp) ** 2 / br_ref
        width = _width_and_lifetime_status(row, "tautau")
    else:
        raise ValueError(f"unknown channel {channel!r}")

    if br_lo < 0.0 or br_hi < br_lo or br_hi > 1.0 + 1.0e-10:
        raise ValueError(f"invalid {channel} branching-fraction interval [{br_lo}, {br_hi}]")
    if br_hi <= 0.0:
        result["classification"] = f"unclassified_zero_{channel}_branching_fraction"
        return result

    strength_obs_lo, strength_obs_hi = scale_obs * br_lo, scale_obs * br_hi
    strength_exp_lo, strength_exp_hi = scale_exp * br_lo, scale_exp * br_hi
    result.update({
        "BR_UV_signal_min": br_lo,
        "BR_UV_signal_max": br_hi,
        "BR_benchmark_signal": br_ref,
        "UV_coupling": coupling_uv,
        "published_coupling_limit_observed": limit_obs,
        "published_coupling_limit_expected": limit_exp,
        "signal_strength_ratio_observed_min": strength_obs_lo,
        "signal_strength_ratio_observed_max": strength_obs_hi,
        "signal_strength_ratio_expected_min": strength_exp_lo,
        "signal_strength_ratio_expected_max": strength_exp_hi,
        **width,
    })

    if width["width_status"] != "narrow_proxy_pass":
        result["classification"] = width["width_status"]
    elif width["flight_status"] != "prompt_geometry_proxy_pass":
        result["classification"] = width["flight_status"]
    elif strength_obs_lo > 1.0:
        result["classification"] = "excluded_under_published_narrow_prompt_benchmark_conditional"
    elif strength_obs_hi <= 1.0:
        result["classification"] = "evaluated_not_excluded_by_this_channel_conditional"
    else:
        result["classification"] = "unclassified_branching_interval_straddles_observed_limit"
    return result


def _open_scan(path: Path):
    if path.name.endswith(".gz"):
        return gzip.open(path, "rt", newline="", encoding="utf-8")
    return path.open(newline="", encoding="utf-8")


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
        "fourmu": args.output_dir / "belleii_4mu_bounded_width_uv_recast.csv",
        "tautau": args.output_dir / "belleii_tautau_bounded_width_uv_recast.csv",
    }
    counts = {ch: Counter() for ch in output_paths}
    classification_details = {ch: {} for ch in output_paths}
    input_rows = 0
    with _open_scan(args.scan) as sf:
        reader = csv.DictReader(sf)
        with output_paths["fourmu"].open("w", newline="", encoding="utf-8") as f4, \
             output_paths["tautau"].open("w", newline="", encoding="utf-8") as ft:
            writers = {"fourmu": None, "tautau": None}
            for row in reader:
                input_rows += 1
                mass = _number(row, "ms_GeV")
                if 0.212 <= mass <= 9.0:
                    rec = evaluate_row(row, "fourmu", fourmu_limits)
                    counts["fourmu"][rec["classification"]] += 1
                    _record_classification_details(classification_details["fourmu"], rec)
                    if writers["fourmu"] is None:
                        writers["fourmu"] = csv.DictWriter(f4, fieldnames=list(rec))
                        writers["fourmu"].writeheader()
                    writers["fourmu"].writerow(rec)
                if 3.6 <= mass <= 10.0:
                    rec = evaluate_row(row, "tautau", tau_limits)
                    counts["tautau"][rec["classification"]] += 1
                    _record_classification_details(classification_details["tautau"], rec)
                    if writers["tautau"] is None:
                        writers["tautau"] = csv.DictWriter(ft, fieldnames=list(rec))
                        writers["tautau"].writeheader()
                    writers["tautau"].writerow(rec)

    summary = {
        "scope": "original one-VEV S+VLL model; zero-portal and decoupled-VLL collider benchmark",
        "scan_rows": input_rows,
        "fourmu_limit_data": fourmu_meta,
        "tau_limit_data": tau_meta,
        "mass_interpolation": "log-log interpolation of observed/expected scalar coupling limits; no extrapolation",
        "branching_fraction_treatment": "propagate scan-provided min/max intervals; do not renormalize incomplete partial widths",
        "narrow_width_tolerance": NARROW_WIDTH_RATIO_TOLERANCE,
        "narrow_width_tolerance_note": "internal conservative diagnostic, not a Belle II cut",
        "promptness_note": "maximum-kinematic scalar mean-flight interval compared with 5 mm transverse DCA scale; geometry proxy only, not detector efficiency or a literal decay-radius cut",
        "fourmu_resolution_note": "published reduced-mass resolution envelope used by the width scan",
        "tau_resolution_note": "anchor-based conservative recoil-mass resolution interval used by the width scan",
        "coupling_mappings": {
            "fourmu": "y_smu^2 * BR_UV(mumu) / gS_UL^2; Belle muonphilic scalar reference BR=1",
            "tautau": "xi_UV^2 * BR_UV(tautau) / (xi_UL^2 * BR_Belle(tautau)); xi_UV=246 GeV/vs",
        },
        "classification_counts": {ch: dict(c) for ch, c in counts.items()},
        "classification_details": {
            ch: _finalize_classification_details(details)
            for ch, details in classification_details.items()
        },
        "limitations": [
            "The double-virtual four-body contribution uses a diagonal-pairing spectral calculation and a Cauchy-Schwarz upper bound on identical-flavour exchange; it is not an exact exclusive four-body calculation.",
            "A point is excluded only if the lower signal-strength endpoint exceeds the observed published limit and the entire width/flight intervals pass the narrow/prompt proxies.",
            "The 5 mm flight-length comparison is a geometry proxy, not a lifetime-dependent detector efficiency.",
            "No finite-width convolution or event-level CLs fit is performed.",
            "No independent MadGraph production recalculation is performed; the mapping uses the same spin-zero muon-FSR coupling normalization as the published scalar benchmark.",
            "These are conditional reinterpretations of published scalar coupling limits, not new Belle II CLs results.",
        ],
        "outputs": {k: v.name for k, v in output_paths.items()},
    }
    (args.output_dir / "bounded_width_recast_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
