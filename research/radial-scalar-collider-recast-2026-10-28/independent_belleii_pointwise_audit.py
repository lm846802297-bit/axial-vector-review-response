#!/usr/bin/env python3
"""Independent full-grid check of the Belle II scalar pointwise mapping.

This intentionally does not import the production recast module. It reads the
archived UV width scan and the raw Belle II limit tables, reconstructs the
published-limit interpolation and UV/reference rate ratios, and compares every
relevant grid row with the archived pointwise output.
"""
from __future__ import annotations

import argparse
import bisect
import csv
import gzip
import json
import math
from collections import Counter
from pathlib import Path

M_E = 0.00051099895
M_MU = 0.1056583755
M_TAU = 1.77686
V_H = 246.0
NARROW_CEILING = 0.10
FLIGHT_CEILING_M = 0.005
FOURMU_COUNTS = {
    "evaluated_not_excluded_by_this_channel_conditional": 39534,
    "finite_width_sensitive": 8673,
    "theoretically_inconsistent_scalar_yukawa": 1734,
    "theoretically_inconsistent_scalar_quartic": 4948,
    "width_interval_straddles_narrow_threshold": 933,
    "lifetime_sensitive": 12088,
    "excluded_under_published_narrow_prompt_benchmark_conditional": 2746,
}
TAUTAU_COUNTS = {
    "evaluated_not_excluded_by_this_channel_conditional": 11337,
    "width_interval_straddles_narrow_threshold": 891,
    "finite_width_sensitive": 3286,
    "theoretically_inconsistent_scalar_quartic": 2414,
    "lifetime_sensitive": 721,
    "unclassified_outside_numerical_limit_grid": 1319,
}


def as_bool(value: str | None) -> bool:
    return str(value).strip().lower() in ("true", "1", "yes")


def number(row: dict, key: str) -> float:
    value = row.get(key)
    if value in (None, "", "None"):
        raise ValueError(f"missing required value {key}")
    out = float(value)
    if not math.isfinite(out):
        raise ValueError(f"non-finite value {key}")
    return out


def partial_weight(mass: float, fermion_mass: float) -> float:
    if mass <= 2.0 * fermion_mass:
        return 0.0
    beta2 = 1.0 - 4.0 * fermion_mass**2 / mass**2
    return fermion_mass**2 * beta2**1.5


def tau_reference_branching(mass: float) -> float:
    weights = [partial_weight(mass, m) for m in (M_E, M_MU, M_TAU)]
    total = sum(weights)
    return weights[2] / total if total > 0.0 else 0.0


def load_fourmu_limits(path: Path) -> tuple[list[float], list[float], list[float], dict]:
    masses, observed, expected = [], [], []
    with path.open(encoding="utf-8") as stream:
        next(stream)
        for line in stream:
            fields = line.split()
            if not fields:
                continue
            if len(fields) != 15:
                raise ValueError(f"four-muon row has {len(fields)} columns, expected 15")
            masses.append(float(fields[0]))
            observed.append(float(fields[7]))
            expected.append(float(fields[8]))
    order = sorted(range(len(masses)), key=masses.__getitem__)
    masses = [masses[i] for i in order]
    observed = [observed[i] for i in order]
    expected = [expected[i] for i in order]
    if len(set(masses)) != len(masses):
        raise ValueError("four-muon mass table unexpectedly contains duplicate masses")
    return masses, observed, expected, {
        "raw_rows": len(masses), "unique_masses": len(set(masses)),
        "mass_min_GeV": min(masses), "mass_max_GeV": max(masses),
    }


def load_tau_limits(path: Path) -> tuple[list[float], list[float], list[float], dict]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))
    masses = [float(row["m [GeV/c^2]"]) for row in rows]
    observed = [float(row["xi_UL_obs"]) for row in rows]
    expected = [float(row["xi_UL_exp"]) for row in rows]
    triples = sorted(zip(masses, observed, expected))
    unique = []
    for item in triples:
        if not unique or item[0] != unique[-1][0]:
            unique.append(item)
        elif item[1:] != unique[-1][1:]:
            raise ValueError("duplicate tau mass has inconsistent limit values")
    return ([x[0] for x in unique], [x[1] for x in unique],
            [x[2] for x in unique], {
                "raw_rows": len(rows), "unique_masses": len(unique),
                "duplicate_rows": len(rows) - len(unique),
                "mass_min_GeV": min(masses), "mass_max_GeV": max(masses),
            })


def loglog_interpolate(x: float, xs: list[float], ys: list[float]) -> float | None:
    if x < xs[0] or x > xs[-1]:
        return None
    i = bisect.bisect_left(xs, x)
    if i < len(xs) and xs[i] == x:
        return ys[i]
    if i == 0 or i == len(xs):
        return None
    x0, x1 = math.log(xs[i - 1]), math.log(xs[i])
    y0, y1 = math.log(ys[i - 1]), math.log(ys[i])
    t = (math.log(x) - x0) / (x1 - x0)
    return math.exp(y0 + t * (y1 - y0))


def width_status(row: dict, channel: str) -> dict:
    prefix = "fourmu" if channel == "fourmu" else "tau"
    lo = number(row, f"{prefix}_Gamma_over_sigma_lower_bound")
    hi = number(row, f"{prefix}_Gamma_over_sigma_upper_bound")
    flight_lo = number(row, "scalar_mean_lab_flight_max_lower_m")
    flight_hi = number(row, "scalar_mean_lab_flight_max_upper_m")
    if lo < 0.0 or hi < lo or flight_lo < 0.0 or flight_hi < flight_lo:
        raise ValueError("invalid width or flight interval")
    if hi >= NARROW_CEILING:
        width = ("finite_width_sensitive" if lo >= NARROW_CEILING
                 else "width_interval_straddles_narrow_threshold")
    else:
        width = "narrow_proxy_pass"
    if flight_hi >= FLIGHT_CEILING_M:
        flight = ("lifetime_sensitive" if flight_lo >= FLIGHT_CEILING_M
                  else "flight_interval_straddles_5mm_proxy")
    else:
        flight = "prompt_geometry_proxy_pass"
    return {
        "width_ratio_min": lo, "width_ratio_max": hi,
        "flight_length_proxy_min_m": flight_lo,
        "flight_length_proxy_max_m": flight_hi,
        "width_status": width, "flight_status": flight,
    }


def independently_classify(row: dict, channel: str, limits: tuple) -> dict:
    mass = number(row, "ms_GeV")
    mA = number(row, "mA_GeV")
    gx = number(row, "gX")
    vs = number(row, "vs_GeV")
    if not as_bool(row.get("passes_lambdaS_le_4pi", "false")):
        return {"classification": "theoretically_inconsistent_scalar_quartic"}
    if not as_bool(row.get("passes_scalar_yukawas_le_sqrt4pi", "false")):
        return {"classification": "theoretically_inconsistent_scalar_yukawa"}
    if channel == "fourmu" and 3.07 <= mass <= 3.12:
        return {"classification": "unclassified_experimental_Jpsi_veto"}

    xs, obs, exp = limits
    lim_obs = loglog_interpolate(mass, xs, obs)
    lim_exp = loglog_interpolate(mass, xs, exp)
    if lim_obs is None or lim_exp is None:
        return {"classification": "unclassified_outside_numerical_limit_grid"}
    if not as_bool(row.get("branching_fractions_bounded_under_declared_benchmark", "false")):
        return {"classification": "unclassified_branching_fraction_not_bounded"}

    if channel == "fourmu":
        br_lo = number(row, "BR_mu_mu_min")
        br_hi = number(row, "BR_mu_mu_max")
        uv_coupling = M_MU / vs
        reference_br = 1.0
    elif channel == "tautau":
        br_lo = number(row, "BR_tau_tau_min")
        br_hi = number(row, "BR_tau_tau_max")
        reference_br = tau_reference_branching(mass)
        if reference_br <= 0.0:
            return {"classification": "unclassified_zero_reference_tau_branching_fraction"}
        uv_coupling = V_H / vs
    else:
        raise ValueError(channel)

    if br_lo < 0.0 or br_hi < br_lo or br_hi > 1.0 + 1e-10:
        raise ValueError("invalid UV branching-fraction interval")
    if br_hi <= 0.0:
        return {"classification": f"unclassified_zero_{channel}_branching_fraction"}

    ratio_scale_obs = (uv_coupling / lim_obs)**2 / reference_br
    ratio_scale_exp = (uv_coupling / lim_exp)**2 / reference_br
    r_obs_lo, r_obs_hi = ratio_scale_obs * br_lo, ratio_scale_obs * br_hi
    r_exp_lo, r_exp_hi = ratio_scale_exp * br_lo, ratio_scale_exp * br_hi
    widths = width_status(row, channel)

    if widths["width_status"] != "narrow_proxy_pass":
        classification = widths["width_status"]
    elif widths["flight_status"] != "prompt_geometry_proxy_pass":
        classification = widths["flight_status"]
    elif r_obs_lo > 1.0:
        classification = "excluded_under_published_narrow_prompt_benchmark_conditional"
    elif r_obs_hi <= 1.0:
        classification = "evaluated_not_excluded_by_this_channel_conditional"
    else:
        classification = "unclassified_branching_interval_straddles_observed_limit"

    return {
        "classification": classification,
        "published_coupling_limit_observed": lim_obs,
        "published_coupling_limit_expected": lim_exp,
        "UV_coupling": uv_coupling,
        "BR_benchmark_signal": reference_br,
        "BR_UV_signal_min": br_lo,
        "BR_UV_signal_max": br_hi,
        "signal_strength_ratio_observed_min": r_obs_lo,
        "signal_strength_ratio_observed_max": r_obs_hi,
        "signal_strength_ratio_expected_min": r_exp_lo,
        "signal_strength_ratio_expected_max": r_exp_hi,
        **widths,
    }


def close_enough(actual: str, expected: float, *, atol: float = 2e-12) -> bool:
    value = float(actual)
    return abs(value - expected) <= max(atol, 2e-10 * max(abs(value), abs(expected)))


def read_rows(path: Path) -> dict[tuple[float, float, float], dict]:
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    keyed = {}
    for row in rows:
        key = (float(row["ms_GeV"]), float(row["mA_GeV"]), float(row["gX"]))
        if key in keyed:
            raise ValueError(f"duplicate recast point {key}")
        keyed[key] = row
    return keyed


def sample_record(row: dict, calc: dict) -> dict:
    return {
        "ms_GeV": number(row, "ms_GeV"),
        "mA_GeV": number(row, "mA_GeV"),
        "gX": number(row, "gX"),
        "classification": calc["classification"],
        "R_obs_min": calc.get("signal_strength_ratio_observed_min"),
        "width_ratio_upper": calc.get("width_ratio_max"),
        "flight_length_upper_m": calc.get("flight_length_proxy_max_m"),
    }


def run_audit(scan_path: Path, fourmu_limits_path: Path, tau_limits_path: Path,
              fourmu_output_path: Path, tau_output_path: Path) -> dict:
    four_limits = load_fourmu_limits(fourmu_limits_path)
    tau_limits = load_tau_limits(tau_limits_path)
    output_maps = {
        "fourmu": read_rows(fourmu_output_path),
        "tautau": read_rows(tau_output_path),
    }
    limits_by_channel = {
        "fourmu": (four_limits[0], four_limits[1], four_limits[2]),
        "tautau": (tau_limits[0], tau_limits[1], tau_limits[2]),
    }
    counts = {"fourmu": Counter(), "tautau": Counter()}
    samples = {"fourmu": [], "tautau": []}
    comparisons = {"fourmu": 0, "tautau": 0}
    masses_seen = set()

    opener = gzip.open if str(scan_path).endswith(".gz") else open
    with opener(scan_path, "rt", newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            mass = number(row, "ms_GeV")
            masses_seen.add(mass)
            key = (mass, number(row, "mA_GeV"), number(row, "gX"))
            for channel, lo, hi in (("fourmu", 0.212, 9.0), ("tautau", 3.6, 10.0)):
                if not lo <= mass <= hi:
                    continue
                archived = output_maps[channel].get(key)
                if archived is None:
                    raise AssertionError(f"{channel}: missing archived output row {key}")
                calc = independently_classify(row, channel, limits_by_channel[channel])
                counts[channel][calc["classification"]] += 1
                comparisons[channel] += 1
                if calc["classification"] != archived["classification"]:
                    raise AssertionError(
                        f"{channel} classification mismatch at {key}: "
                        f"{calc['classification']} != {archived['classification']}"
                    )
                for field in (
                    "published_coupling_limit_observed", "published_coupling_limit_expected",
                    "UV_coupling", "BR_benchmark_signal", "BR_UV_signal_min",
                    "BR_UV_signal_max", "signal_strength_ratio_observed_min",
                    "signal_strength_ratio_observed_max", "signal_strength_ratio_expected_min",
                    "signal_strength_ratio_expected_max", "width_ratio_min", "width_ratio_max",
                    "flight_length_proxy_min_m", "flight_length_proxy_max_m",
                ):
                    if field in calc and not close_enough(archived[field], calc[field]):
                        raise AssertionError(
                            f"{channel} {field} mismatch at {key}: "
                            f"{calc[field]} != {archived[field]}"
                        )
                samples[channel].append((row, calc))

    if len(masses_seen) != 48:
        raise AssertionError(f"expected 48 scalar-mass grid values, found {len(masses_seen)}")
    for channel in ("fourmu", "tautau"):
        if comparisons[channel] != len(output_maps[channel]):
            raise AssertionError(
                f"{channel}: compared {comparisons[channel]} rows but archived "
                f"{len(output_maps[channel])}"
            )

    expected_counts = {"fourmu": FOURMU_COUNTS, "tautau": TAUTAU_COUNTS}
    for channel, expected in expected_counts.items():
        actual = dict(counts[channel])
        if actual != expected:
            raise AssertionError(f"{channel} classification counts changed: {actual} != {expected}")

    four_rows = samples["fourmu"]
    tau_rows = samples["tautau"]
    near_limit = [x for x in four_rows
                  if x[1].get("signal_strength_ratio_observed_min") is not None
                  and x[1]["classification"] == "evaluated_not_excluded_by_this_channel_conditional"]
    width_candidates = [x for x in four_rows if "width_ratio_max" in x[1]]
    flight_candidates = [x for x in four_rows if "flight_length_proxy_max_m" in x[1]]
    tau_in_grid = [x for x in tau_rows if "signal_strength_ratio_observed_min" in x[1]]

    def nearest(candidates, metric, target):
        row, calc = min(candidates, key=lambda pair: abs(metric(pair[1]) - target))
        return sample_record(row, calc)

    def closest_mass(candidates, target):
        row, calc = min(candidates, key=lambda pair: abs(number(pair[0], "ms_GeV") - target))
        return sample_record(row, calc)

    first_mu = closest_mass(four_rows, 2.0 * M_MU)
    tau_first = closest_mass(tau_in_grid, 2.0 * M_TAU)
    tau_six = closest_mass(tau_in_grid, 6.0)
    tau_upper = max(tau_in_grid, key=lambda pair: number(pair[0], "ms_GeV"))
    tau_upper_sample = sample_record(*tau_upper)

    return {
        "status": "PASS",
        "method": "independent standard-library pointwise reconstruction; no production recast imports",
        "scan_mass_grid_values": len(masses_seen),
        "scan_min_mass_GeV": min(masses_seen),
        "muon_pair_threshold_GeV": 2.0 * M_MU,
        "tau_pair_threshold_GeV": 2.0 * M_TAU,
        "grid_has_mass_below_muon_threshold": min(masses_seen) < 2.0 * M_MU,
        "grid_has_mass_inside_Jpsi_veto": any(3.07 <= m <= 3.12 for m in masses_seen),
        "fourmu_limit_table": four_limits[3],
        "tau_limit_table": tau_limits[3],
        "row_comparisons": comparisons,
        "classification_counts": {k: dict(v) for k, v in counts.items()},
        "samples": {
            "fourmu_nearest_muon_threshold_grid_point": first_mu,
            "fourmu_nearest_Robs_to_one_from_not_excluded_subset": sample_record(
                *max(near_limit, key=lambda pair: pair[1]["signal_strength_ratio_observed_min"])
            ),
            "fourmu_nearest_narrow_width_boundary": nearest(
                width_candidates, lambda x: x["width_ratio_max"], NARROW_CEILING
            ),
            "fourmu_nearest_5mm_prompt_proxy_boundary": nearest(
                flight_candidates, lambda x: x["flight_length_proxy_max_m"], FLIGHT_CEILING_M
            ),
            "tau_nearest_threshold_grid_point": tau_first,
            "tau_nearest_6GeV_grid_point": tau_six,
            "tau_highest_mass_with_published_limit": tau_upper_sample,
        },
        "boundary_tests": {
            "muon_channel_below_threshold_weight": partial_weight(2.0 * M_MU - 1e-8, M_MU),
            "muon_channel_above_threshold_weight": partial_weight(2.0 * M_MU + 1e-8, M_MU),
            "tau_reference_BR_at_threshold": tau_reference_branching(2.0 * M_TAU),
            "tau_reference_BR_just_above_threshold": tau_reference_branching(2.0 * M_TAU + 1e-8),
            "Jpsi_veto_at_3p095_GeV": 3.07 <= 3.095 <= 3.12,
            "Jpsi_veto_just_below": 3.07 <= 3.069999 <= 3.12,
            "Jpsi_veto_just_above": 3.07 <= 3.120001 <= 3.12,
        },
        "interpretation": [
            "The archived 2,746 four-muon points are reproduced as conditional narrow/prompt pointwise exclusions.",
            "No grid point lies below the muon threshold or inside the J/psi veto; those boundaries are checked analytically, while the nearest available grid points are reported.",
            "The 0.10 width and 5 mm flight-length values remain internal conservative proxies, not Belle II selection cuts.",
            "Finite-width and lifetime-sensitive points remain unclassified; no detector-level CLs result is inferred.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", type=Path, required=True)
    parser.add_argument("--fourmu-limits", type=Path, required=True)
    parser.add_argument("--tau-limits", type=Path, required=True)
    parser.add_argument("--fourmu-output", type=Path, required=True)
    parser.add_argument("--tau-output", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_audit(args.scan, args.fourmu_limits, args.tau_limits,
                       args.fourmu_output, args.tau_output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
