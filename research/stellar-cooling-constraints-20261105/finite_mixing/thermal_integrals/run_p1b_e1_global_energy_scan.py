#!/usr/bin/env python3
"""P1-B E1 global energy interpolation screening on every SFHo radial knot.

Computes the 17-point validation set (9 one-bisection interpolation knots plus
8 direct midpoints) at every original 1687-row SFHo-18.8 radius, using the
exact-recoil moving-muon B.13 kernel. The low-order scan is only a screening
layer; worst points must subsequently pass the independent high-order ladder.

Default run (one radial node per immutable checkpoint):
  python finite_mixing/thermal_integrals/run_p1b_e1_global_energy_scan.py

Resume a subset/range:
  python .../run_p1b_e1_global_energy_scan.py --start-chunk 500 --end-chunk 600
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys, time
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import audit_b13_local_kernel_radial_energy_10mev as audit

PROFILE = ROOT / "data" / "sfho188_digitized.csv"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
MASS_MEV = 10.0
ORDERS = (10, 6, 6, 6)
BASE_X = np.asarray([0.5, 2.0, 6.0, 18.0, 36.0], dtype=float)
INTERP_TOL = 1.0e-2


def bisect_sqrt_x(nodes):
    return np.asarray(sorted(set(nodes.tolist() + [
        (0.5 * (math.sqrt(a) + math.sqrt(b))) ** 2
        for a, b in zip(nodes[:-1], nodes[1:])
    ])), dtype=float)


def compact_record(value):
    return {
        "radius_km": value["radius_km"],
        "omega_local_MeV": value["omega_local_MeV"],
        "temperature_MeV": value["temperature_MeV"],
        "mu_minus_chemical_potential_MeV": value["mu_minus_chemical_potential_MeV"],
        "lapse": value["lapse"],
        "x_max": value["x_max"],
        "orders": value["orders"],
        "charge_resolved": {
            q: {
                "production": value["charge_resolved"][q]["production"],
                "absorption": value["charge_resolved"][q]["absorption"],
                "reduced_absorption": value["charge_resolved"][q]["reduced_absorption"],
                "spectral_source": value["charge_resolved"][q]["spectral_source"],
            } for q in audit.CHARGES
        },
        "maximum_mode_detailed_balance_relative_residual": value["maximum_mode_detailed_balance_relative_residual"],
        "final_muon_shell_relative_error": value["final_muon_shell_relative_error"],
        "charge_sum_closure_relative_residual": value["charge_sum_closure_relative_residual"],
        "all_rates_finite_and_nonnegative": value["all_rates_finite_and_nonnegative"],
    }


def interpolation_for_radius(point_values, coarse_x, new_x):
    errors = []
    for charge in audit.CHARGES:
        coarse_rates = np.asarray([
            point_values[float(x)]["charge_resolved"][charge]["absorption"]
            for x in coarse_x
        ], dtype=float)
        for x in new_x:
            direct = np.asarray(point_values[float(x)]["charge_resolved"][charge]["absorption"], dtype=float)
            for mode_index, mode in enumerate(audit.MODES):
                interpolant = PchipInterpolator(
                    np.sqrt(coarse_x), np.log(np.maximum(coarse_rates[:, mode_index], 1.0e-300))
                )
                predicted = float(np.exp(interpolant(math.sqrt(float(x)))))
                observed = float(direct[mode_index])
                rel = abs(observed - predicted) / max(abs(observed), abs(predicted), 1.0e-300)
                errors.append({
                    "x_mid": float(x), "charge": charge, "mode": mode,
                    "direct_absorption": observed, "PCHIP_absorption": predicted,
                    "relative_error": rel,
                })
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", type=Path, default=HERE / "results" / "P1B_E1_GLOBAL_2026-11-14")
    ap.add_argument("--chunk-size", type=int, default=1,
                    help="default 1 writes a checkpoint after each radial knot")
    ap.add_argument("--start-chunk", type=int, default=0)
    ap.add_argument("--end-chunk", type=int, default=None, help="exclusive chunk index")
    args = ap.parse_args()
    profile_sha = hashlib.sha256(PROFILE.read_bytes()).hexdigest()
    if profile_sha != EXPECTED_PROFILE_SHA256:
        raise RuntimeError(f"SFHo profile SHA mismatch: {profile_sha}")
    table = np.genfromtxt(PROFILE, delimiter=",", names=True)
    radii = np.asarray(table["r_km"], dtype=float)
    if len(radii) != 1687:
        raise RuntimeError(f"Expected 1687 radial knots, got {len(radii)}")
    coarse_x = bisect_sqrt_x(BASE_X)
    validation_grid = bisect_sqrt_x(coarse_x)
    new_x = np.asarray([
        x for x in validation_grid
        if not np.any(np.isclose(x, coarse_x, rtol=0.0, atol=1.0e-13))
    ])
    chunk_size = max(1, int(args.chunk_size))
    n_chunks = math.ceil(len(radii) / chunk_size)
    end_chunk = n_chunks if args.end_chunk is None else min(n_chunks, args.end_chunk)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    started_all = time.time()

    for chunk_index in range(args.start_chunk, end_chunk):
        lo = chunk_index * chunk_size
        hi = min(len(radii), lo + chunk_size)
        out_path = args.output_dir / f"chunk_{chunk_index:04d}.json"
        if out_path.exists():
            old = json.loads(out_path.read_text())
            if old.get("profile_sha256") == profile_sha and old.get("source_sha256") == source_sha:
                print(f"skip verified chunk {chunk_index+1}/{n_chunks} ({lo}:{hi})", flush=True)
                continue
            raise RuntimeError(f"Existing chunk has mismatched provenance: {out_path}")
        chunk_records = []
        chunk_errors = []
        max_db = 0.0
        max_shell = 0.0
        all_nonnegative = True
        t0 = time.time()
        for radial_index in range(lo, hi):
            radius = float(radii[radial_index])
            point_values = {}
            cache = {}
            temperature = float(table["T_MeV"][radial_index])
            for x in validation_grid:
                omega = MASS_MEV + float(x) * temperature
                value = audit.evaluate_point(PROFILE, radius, omega, ORDERS, cache)
                point_values[float(x)] = value
                max_db = max(max_db, value["maximum_mode_detailed_balance_relative_residual"])
                max_shell = max(max_shell, value["final_muon_shell_relative_error"])
                all_nonnegative = all_nonnegative and value["all_rates_finite_and_nonnegative"]
                chunk_records.append({
                    "radial_index": radial_index,
                    "x": float(x),
                    **compact_record(value),
                })
            errs = interpolation_for_radius(point_values, coarse_x, new_x)
            worst = max(errs, key=lambda z: z["relative_error"])
            chunk_errors.append({
                "radial_index": radial_index,
                "radius_km": radius,
                "maximum_interpolation_error": worst["relative_error"],
                "worst_x_mid": worst["x_mid"],
                "worst_charge": worst["charge"],
                "worst_mode": worst["mode"],
                "all_channel_errors": errs,
            })
        payload = {
            "run": "P1B-E1-GLOBAL-ALL-RADIAL-KNOTS",
            "chunk_index": chunk_index,
            "radial_index_range_inclusive": [lo, hi - 1],
            "profile_sha256": profile_sha,
            "source_sha256": source_sha,
            "profile_rows": int(len(radii)),
            "mass_MeV": MASS_MEV,
            "couplings": {"gV_over_gX": 1.0, "gA_over_gX": 0.0},
            "orders": list(ORDERS),
            "base_x": BASE_X.tolist(),
            "coarse_x": coarse_x.tolist(),
            "validation_grid_x": validation_grid.tolist(),
            "new_midpoint_x": new_x.tolist(),
            "records": chunk_records,
            "radial_interpolation_summaries": chunk_errors,
            "acceptance": {
                "all_finite_nonnegative": bool(all_nonnegative),
                "maximum_detailed_balance_residual": max_db,
                "maximum_final_muon_shell_residual": max_shell,
                "maximum_energy_interpolation_error": max(x["maximum_interpolation_error"] for x in chunk_errors),
                "interpolation_tolerance": INTERP_TOL,
                "interpolation_pass_in_chunk": all(x["maximum_interpolation_error"] < INTERP_TOL for x in chunk_errors),
            },
            "runtime_seconds": time.time() - t0,
        }
        tmp = out_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(payload, separators=(",", ":")) + "\n")
        tmp.replace(out_path)
        print(f"completed chunk {chunk_index+1}/{n_chunks}: {hi-lo} radii, {len(chunk_records)} B.13 points, maxE={payload['acceptance']['maximum_energy_interpolation_error']:.4%}, {payload['runtime_seconds']:.1f}s", flush=True)

    files = sorted(args.output_dir.glob("chunk_*.json"))
    all_summaries = []
    completed = []
    for file in files:
        data = json.loads(file.read_text())
        if data.get("profile_sha256") != profile_sha or data.get("source_sha256") != source_sha:
            continue
        completed.append(data["chunk_index"])
        all_summaries.extend(data["radial_interpolation_summaries"])
    if all_summaries:
        worst = max(all_summaries, key=lambda z: z["maximum_interpolation_error"])
        errs = np.asarray([z["maximum_interpolation_error"] for z in all_summaries])
        summary = {
            "run": "P1B-E1-GLOBAL-ALL-RADIAL-KNOTS",
            "profile_sha256": profile_sha,
            "source_sha256": source_sha,
            "profile_rows": int(len(radii)),
            "completed_chunks": sorted(completed),
            "total_chunks": n_chunks,
            "completed_radial_nodes": len(all_summaries),
            "maximum_energy_interpolation_error": float(errs.max()),
            "median_radial_node_maximum_error": float(np.median(errs)),
            "p95_radial_node_maximum_error": float(np.quantile(errs, 0.95)),
            "fraction_radial_nodes_over_1pct": float(np.mean(errs >= INTERP_TOL)),
            "worst_location": worst,
            "global_low_order_interpolation_screen_pass": bool(len(all_summaries) == len(radii) and errs.max() < INTERP_TOL),
            "quadrature_acceptance": "not tested by this low-order global screening run",
            "full_star_transport_claimed": False,
            "scope": "Low-order global energy-interpolation screening. Not quadrature acceptance; worst points require high-order B.13 re-evaluation.",
            "runtime_seconds_this_invocation": time.time() - started_all,
        }
        (args.output_dir / "GLOBAL_SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n")
        print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
