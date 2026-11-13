#!/usr/bin/env python3
"""P1-B E1 energy interpolation audit at a requested SFHo radial anchor.

Evaluates the nine-knot one-bisection sqrt(x) energy interpolant and checks
all eight intervening energy midpoints directly with exact-recoil B.13.
The order-24 scan is a screening layer; selected worst points require the
separate high-order ladder. This script does not claim global radial acceptance.

Run from the repository or extracted package root:
  python finite_mixing/thermal_integrals/run_p1b_e1_energy_anchor.py --radius 14.575 --tag g2_worst
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
import audit_b13_local_kernel_radial_energy_10mev as audit

PROFILE = ROOT / "data" / "sfho188_digitized.csv"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
MASS_MEV = 10.0
ORDERS = (24, 14, 14, 14)
BASE_X = np.asarray([0.5, 2.0, 6.0, 18.0, 36.0], dtype=float)
INTERP_TOL = 1.0e-2


def bisect_sqrt_x(nodes):
    return np.asarray(sorted(set(nodes.tolist() + [
        (0.5 * (math.sqrt(a) + math.sqrt(b))) ** 2
        for a, b in zip(nodes[:-1], nodes[1:])
    ])), dtype=float)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--radius", type=float, required=True, help="radial anchor in km")
    ap.add_argument("--tag", required=True, help="short identifier for output/checkpoint names")
    ap.add_argument("--output-dir", type=Path, default=HERE / "results" / "P1B_E1_ANCHORS_2026-11-14")
    args = ap.parse_args()
    if not args.tag.replace("_", "").replace("-", "").isalnum():
        raise ValueError("tag must contain only letters, digits, underscore, or hyphen")
    profile_sha = hashlib.sha256(PROFILE.read_bytes()).hexdigest()
    if profile_sha != EXPECTED_PROFILE_SHA256:
        raise RuntimeError(f"SFHo profile SHA mismatch: {profile_sha}")
    bg = audit.load_profile(PROFILE, np.asarray([args.radius], dtype=float))
    temperature = float(bg["T"][0])
    mu_mu = float(bg["mu_mu"][0])
    coarse_x = bisect_sqrt_x(BASE_X)
    validation_grid = bisect_sqrt_x(coarse_x)
    midpoint_x = np.asarray([
        x for x in validation_grid
        if not np.any(np.isclose(x, coarse_x, rtol=0.0, atol=1.0e-13))
    ])
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / f"{args.tag}.json"
    checkpoint = args.output_dir / f"{args.tag}.checkpoint.json"
    values = {}
    if checkpoint.exists():
        saved = json.loads(checkpoint.read_text())
        if saved.get("profile_sha256") != profile_sha or saved.get("radius_km") != args.radius:
            raise RuntimeError("checkpoint provenance/radius mismatch")
        values = saved.get("values", {})
    cache = {}
    started = time.time()
    for x in validation_grid:
        key = f"{float(x):.14g}"
        if key in values:
            continue
        result = audit.evaluate_point(
            PROFILE, args.radius, MASS_MEV + float(x) * temperature, ORDERS, cache
        )
        values[key] = {
            "x": float(x),
            "omega_local_MeV": MASS_MEV + float(x) * temperature,
            "rates": result,
        }
        checkpoint.write_text(json.dumps({
            "run": "P1B-E1-ENERGY-ANCHOR-CHECKPOINT",
            "profile_sha256": profile_sha,
            "radius_km": args.radius,
            "temperature_MeV": temperature,
            "mu_mu_MeV": mu_mu,
            "coarse_x": coarse_x.tolist(),
            "validation_grid_x": validation_grid.tolist(),
            "orders": list(ORDERS),
            "values": values,
        }, separators=(",", ":")) + "\n")
        print(f"{args.tag}: evaluated x={float(x):.9g}", flush=True)

    errors = []
    for charge in audit.CHARGES:
        coarse_rates = np.asarray([
            values[f"{float(x):.14g}"]["rates"]["charge_resolved"][charge]["absorption"]
            for x in coarse_x
        ], dtype=float)
        for x in midpoint_x:
            direct = np.asarray(
                values[f"{float(x):.14g}"]["rates"]["charge_resolved"][charge]["absorption"],
                dtype=float,
            )
            for mode_index, mode in enumerate(audit.MODES):
                interpolant = PchipInterpolator(
                    np.sqrt(coarse_x),
                    np.log(np.maximum(coarse_rates[:, mode_index], 1.0e-300)),
                )
                predicted = float(np.exp(interpolant(math.sqrt(float(x)))))
                observed = float(direct[mode_index])
                error = abs(observed - predicted) / max(abs(observed), abs(predicted), 1.0e-300)
                errors.append({
                    "x_mid": float(x), "charge": charge, "mode": mode,
                    "direct_absorption": observed, "PCHIP_absorption": predicted,
                    "relative_error": error,
                })
    worst = max(errors, key=lambda z: z["relative_error"])
    max_db = max(v["rates"]["maximum_mode_detailed_balance_relative_residual"] for v in values.values())
    max_shell = max(v["rates"]["final_muon_shell_relative_error"] for v in values.values())
    all_nonnegative = all(v["rates"]["all_rates_finite_and_nonnegative"] for v in values.values())
    summary = {
        "run": "P1B-E1-ENERGY-ANCHOR-PCHIP",
        "profile_sha256": profile_sha,
        "profile_rows": 1687,
        "radius_km": args.radius,
        "temperature_MeV": temperature,
        "mu_mu_MeV": mu_mu,
        "mass_MeV": MASS_MEV,
        "couplings": {"gV_over_gX": 1.0, "gA_over_gX": 0.0},
        "interpolation_knots_x": coarse_x.tolist(),
        "direct_validation_midpoints_x": midpoint_x.tolist(),
        "quadrature_orders": list(ORDERS),
        "interpolant": "PCHIP(log absorption) in sqrt(x); production/reduced absorption reconstructed by detailed balance",
        "maximum_PCHIP_interpolation_error": worst["relative_error"],
        "worst": worst,
        "maximum_detailed_balance_residual": max_db,
        "maximum_final_muon_mass_shell_residual": max_shell,
        "all_rates_finite_nonnegative": all_nonnegative,
        "interpolation_pass_at_anchor": bool(worst["relative_error"] < INTERP_TOL),
        "runtime_seconds_this_invocation": time.time() - started,
        "scope": "Single radial anchor only; not full 1687-knot radial acceptance or full-star transport.",
    }
    output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
