#!/usr/bin/env python3
"""Global-06: full 1687-radius low-x B.13 table and interpolation screen.

This driver is a low-order global screen, not a high-order acceptance run.
It preserves the exact-recoil B.13 kernel, both muon charges, and L,+,- modes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROFILE = ROOT / "data" / "sfho188_digitized.csv"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
MASS_MEV = 10.0
ORDER = (10, 6, 6, 6)
BASE_X = np.asarray([0.05, 0.1, 0.2, 0.35, 0.5], dtype=float)
X_GRID = np.sort(np.concatenate([
    BASE_X,
    ((np.sqrt(BASE_X[:-1]) + np.sqrt(BASE_X[1:])) / 2.0) ** 2,
]))
X_VALIDATION = (
    (np.sqrt(X_GRID[:-1]) + np.sqrt(X_GRID[1:])) / 2.0
) ** 2
CHARGES = ("mu_minus", "mu_plus")
FIELDS = ("absorption", "production")
MODES = ("L", "+", "-")
N_RADIAL_CHUNK = 48
TOP_RADIAL_INTERVALS = 60
ENERGY_INTERPOLATION_TOL = 1.0e-2
RADIAL_INTERPOLATION_TOL = 1.0e-2
DB_TOL = 2.0e-10
SHELL_TOL = 2.0e-10


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def relative_error(a, b):
    aa = np.asarray(a, dtype=float)
    bb = np.asarray(b, dtype=float)
    den = np.maximum(np.maximum(np.abs(aa), np.abs(bb)), 1.0e-300)
    return float(np.max(np.abs(aa - bb) / den))


def pack_point(result, radial_index, radius, x):
    return {
        "radial_index": int(radial_index),
        "r_km": float(radius),
        "T_MeV": float(result["temperature_MeV"]),
        "mu_mu_MeV": float(result["mu_minus_chemical_potential_MeV"]),
        "lapse": float(result["lapse"]),
        "x": float(x),
        "omega_local_MeV": float(result["omega_local_MeV"]),
        "orders": list(result["orders"]),
        "absorption": {
            q: list(result["charge_resolved"][q]["absorption"]) for q in CHARGES
        },
        "production": {
            q: list(result["charge_resolved"][q]["production"]) for q in CHARGES
        },
        "reduced_absorption": {
            q: list(result["charge_resolved"][q]["reduced_absorption"]) for q in CHARGES
        },
        "spectral_source": {
            q: list(result["charge_resolved"][q]["spectral_source"]) for q in CHARGES
        },
        "detailed_balance_residual": float(
            result["maximum_mode_detailed_balance_relative_residual"]
        ),
        "mass_shell_residual": float(result["final_muon_shell_relative_error"]),
        "charge_sum_closure_residual": float(result["charge_sum_closure_relative_residual"]),
        "finite_nonnegative": bool(result["all_rates_finite_and_nonnegative"]),
    }


def interpolate_positive(x_nodes, y_nodes, x_eval):
    x_nodes = np.asarray(x_nodes, dtype=float)
    y_nodes = np.asarray(y_nodes, dtype=float)
    if np.all(y_nodes > 0.0):
        value = float(np.exp(PchipInterpolator(np.sqrt(x_nodes), np.log(y_nodes))(math.sqrt(x_eval))))
    else:
        value = float(PchipInterpolator(np.sqrt(x_nodes), y_nodes)(math.sqrt(x_eval)))
    return max(value, 0.0)


def interpolate_radial(a, b):
    aa = float(a)
    bb = float(b)
    if aa > 0.0 and bb > 0.0:
        return math.exp(0.5 * (math.log(aa) + math.log(bb)))
    return 0.5 * (aa + bb)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--output", type=Path, default=HERE / "results" / "P1B_GLOBAL06_LOW_X_FULL_RADIAL_2026-11-14")
    args = parser.parse_args()
    started = time.time()
    profile_path = args.profile
    profile_sha = file_sha256(profile_path)
    if profile_sha != EXPECTED_PROFILE_SHA256:
        raise RuntimeError(f"profile SHA mismatch: {profile_sha}")

    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as audit

    table = np.genfromtxt(profile_path, delimiter=",", names=True)
    radii = np.asarray(table["r_km"], dtype=float)
    temperatures = np.asarray(table["T_MeV"], dtype=float)

    def fast_load(_path, requested_radii):
        rr = np.asarray(requested_radii, dtype=float)
        return {
            name: np.interp(rr, radii, np.asarray(table[column], dtype=float))
            for name, column in {
                "T": "T_MeV",
                "mu_mu": "mu_mu_MeV",
                "mu_numu": "mu_numu_MeV",
                "lapse": "lapse",
            }.items()
        }

    audit.load_profile = fast_load
    cache = {}
    node_data = []
    db_max = 0.0
    shell_max = 0.0
    all_positive = True
    outdir = args.output
    outdir.mkdir(parents=True, exist_ok=True)

    # Full 1687-node radial layer: nine interpolation knots plus eight
    # independent sqrt(x)-midpoint validation knots at every radius.
    all_x = np.sort(np.concatenate([X_GRID, X_VALIDATION]))
    for start in range(0, len(radii), N_RADIAL_CHUNK):
        stop = min(start + N_RADIAL_CHUNK, len(radii))
        chunk = []
        for i in range(start, stop):
            r = float(radii[i])
            temp = float(temperatures[i])
            points = []
            for x in all_x:
                omega = MASS_MEV + float(x) * temp
                raw = audit.evaluate_point(profile_path, r, omega, ORDER, cache)
                item = pack_point(raw, i, r, float(x))
                points.append(item)
                db_max = max(db_max, item["detailed_balance_residual"])
                shell_max = max(shell_max, item["mass_shell_residual"])
                all_positive = all_positive and item["finite_nonnegative"]
            node = {"radial_index": i, "r_km": r, "T_MeV": temp, "points": points}
            node_data.append(node)
            chunk.append(node)
        target = outdir / f"LOW_X_RADIAL_NODES_{start:04d}_{stop-1:04d}.json"
        target.write_text(json.dumps(chunk, separators=(",", ":")) + "\n", encoding="utf-8")
        print(f"radial nodes {start}-{stop-1}/{len(radii)-1} complete; cache={len(cache)}", flush=True)

    # Energy interpolation validation at every radial node and all eight
    # independent points between the nine formal sqrt(x)-PCHIP knots.
    energy_checks = []
    for node in node_data:
        by_x = {round(p["x"], 14): p for p in node["points"]}
        formal = [by_x[round(float(x), 14)] for x in X_GRID]
        for xv in X_VALIDATION:
            direct = by_x[round(float(xv), 14)]
            channel_errors = {}
            for q in CHARGES:
                channel_errors[q] = {}
                for mode_index, mode in enumerate(MODES):
                    y = [p["absorption"][q][mode_index] for p in formal]
                    pred = interpolate_positive(X_GRID, y, float(xv))
                    truth = direct["absorption"][q][mode_index]
                    channel_errors[q][mode] = relative_error([pred], [truth])
            maximum = max(v for q in CHARGES for v in channel_errors[q].values())
            energy_checks.append({
                "radial_index": node["radial_index"],
                "r_km": node["r_km"],
                "x_validation": float(xv),
                "maximum_channel_relative_error": maximum,
                "channel_errors": channel_errors,
            })

    # Rank every adjacent radial interval using symmetric relative changes
    # in charge-resolved production and absorption at all nine formal x knots.
    radial_rank = []
    node_by_i = {n["radial_index"]: n for n in node_data}
    for i in range(len(radii) - 1):
        left = node_by_i[i]
        right = node_by_i[i + 1]
        lp = {round(p["x"], 14): p for p in left["points"]}
        rp = {round(p["x"], 14): p for p in right["points"]}
        worst = 0.0
        worst_channel = None
        for x in X_GRID:
            a = lp[round(float(x), 14)]
            b = rp[round(float(x), 14)]
            for q in CHARGES:
                for field in FIELDS:
                    for imode, mode in enumerate(MODES):
                        err = relative_error(
                            [a[field][q][imode]], [b[field][q][imode]]
                        )
                        if err > worst:
                            worst = err
                            worst_channel = {
                                "x": float(x), "charge": q, "field": field, "mode": mode
                            }
        radial_rank.append({
            "left_index": i,
            "right_index": i + 1,
            "r_left_km": left["r_km"],
            "r_right_km": right["r_km"],
            "dr_km": right["r_km"] - left["r_km"],
            "maximum_neighbor_change": worst,
            "worst_channel": worst_channel,
        })
    radial_rank.sort(key=lambda z: z["maximum_neighbor_change"], reverse=True)
    top = radial_rank[:TOP_RADIAL_INTERVALS]

    # Direct midpoint checks at all nine formal low-x knots for the top 60
    # intervals. Interpolate endpoint absorption in log-radius at fixed x;
    # reconstruct production/reduced absorption by exact local detailed balance.
    midpoint_checks = []
    for rank, interval in enumerate(top, start=1):
        i0 = interval["left_index"]
        i1 = interval["right_index"]
        rmid = 0.5 * (float(radii[i0]) + float(radii[i1]))
        tmid = float(np.interp(rmid, radii, temperatures))
        for x in X_GRID:
            omega = MASS_MEV + float(x) * tmid
            direct_raw = audit.evaluate_point(profile_path, rmid, omega, ORDER, cache)
            direct = pack_point(direct_raw, -1, rmid, float(x))
            left = {round(p["x"], 14): p for p in node_by_i[i0]["points"]}[round(float(x), 14)]
            right = {round(p["x"], 14): p for p in node_by_i[i1]["points"]}[round(float(x), 14)]
            channel_errors = {}
            for q in CHARGES:
                channel_errors[q] = {}
                for imode, mode in enumerate(MODES):
                    pred = interpolate_radial(
                        left["absorption"][q][imode], right["absorption"][q][imode]
                    )
                    truth = direct["absorption"][q][imode]
                    channel_errors[q][mode] = relative_error([pred], [truth])
            maximum = max(v for q in CHARGES for v in channel_errors[q].values())
            midpoint_checks.append({
                "rank": rank,
                "interval_index": i0,
                "r_mid_km": rmid,
                "x": float(x),
                "maximum_channel_relative_error": maximum,
                "channel_errors": channel_errors,
                "detailed_balance_residual": direct["detailed_balance_residual"],
                "mass_shell_residual": direct["mass_shell_residual"],
                "finite_nonnegative": direct["finite_nonnegative"],
            })
        print(f"radial midpoint rank {rank}/{len(top)} complete", flush=True)

    max_energy_error = max(x["maximum_channel_relative_error"] for x in energy_checks)
    max_radial_midpoint_error = max(x["maximum_channel_relative_error"] for x in midpoint_checks)
    summary = {
        "run": "P1B-GLOBAL-06-LOW-X-FULL-RADIAL",
        "profile_sha256": profile_sha,
        "profile_radial_nodes": int(len(radii)),
        "base_x_knots": BASE_X.tolist(),
        "formal_x_grid": X_GRID.tolist(),
        "independent_validation_x": X_VALIDATION.tolist(),
        "energy_coordinates_per_radius": int(len(all_x)),
        "direct_radial_node_evaluations": int(len(radii) * len(all_x)),
        "radial_intervals": int(len(radii) - 1),
        "top_radial_intervals_midpoint_checked": int(len(top)),
        "direct_radial_midpoint_evaluations": int(len(top) * len(X_GRID)),
        "quadrature_order": list(ORDER),
        "energy_interpolation": {
            "method": "PCHIP(log absorption) in sqrt(x); exact detailed-balance reconstruction for production and reduced absorption",
            "validation_points": int(len(energy_checks)),
            "maximum_relative_error": max_energy_error,
            "pass_1pct": bool(max_energy_error < ENERGY_INTERPOLATION_TOL),
            "worst": max(energy_checks, key=lambda x: x["maximum_channel_relative_error"]),
        },
        "radial_neighbor_screen": {
            "ranked_intervals": len(radial_rank),
            "maximum_neighbor_change": radial_rank[0]["maximum_neighbor_change"],
            "worst_interval": radial_rank[0],
        },
        "radial_midpoint_interpolation": {
            "checked_intervals": len(top),
            "direct_evaluations": len(midpoint_checks),
            "maximum_relative_error": max_radial_midpoint_error,
            "pass_1pct": bool(max_radial_midpoint_error < RADIAL_INTERPOLATION_TOL),
            "worst": max(midpoint_checks, key=lambda x: x["maximum_channel_relative_error"]),
        },
        "micro_consistency": {
            "maximum_detailed_balance_residual": db_max,
            "maximum_mass_shell_residual": shell_max,
            "all_rates_finite_nonnegative": bool(all_positive),
            "detailed_balance_pass": bool(db_max < DB_TOL),
            "mass_shell_pass": bool(shell_max < SHELL_TOL),
        },
        "acceptance_boundary": {
            "full_1687_radial_low_x_screen_complete": True,
            "low_order_energy_interpolation_pass": bool(max_energy_error < ENERGY_INTERPOLATION_TOL),
            "top60_radial_midpoint_screen_pass": bool(max_radial_midpoint_error < RADIAL_INTERPOLATION_TOL),
            "global_high_order_quadrature_acceptance": False,
            "full_band_B1_B2_transport": False,
            "x_below_0p05_covered": False,
            "SN1987A_or_axial_limit_updated": False,
        },
        "runtime_seconds": time.time() - started,
        "scope": "Low-order full-radial low-x B.13 screen plus top-60 radial midpoint checks. High-order quadrature, x<0.05, full-band B.1/B.2, and luminosity are not claimed.",
    }
    (outdir / "RADIAL_NEIGHBOR_RANKING_TOP60.json").write_text(
        json.dumps(top, indent=2) + "\n", encoding="utf-8"
    )
    (outdir / "RADIAL_MIDPOINT_CHECKS_TOP60.json").write_text(
        json.dumps(midpoint_checks, indent=2) + "\n", encoding="utf-8"
    )
    (outdir / "ENERGY_INTERPOLATION_CHECKS.json").write_text(
        json.dumps(energy_checks, separators=(",", ":")) + "\n", encoding="utf-8"
    )
    (outdir / "GLOBAL06_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print("\nGlobal-06 summary:")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return summary


if __name__ == "__main__":
    main()
