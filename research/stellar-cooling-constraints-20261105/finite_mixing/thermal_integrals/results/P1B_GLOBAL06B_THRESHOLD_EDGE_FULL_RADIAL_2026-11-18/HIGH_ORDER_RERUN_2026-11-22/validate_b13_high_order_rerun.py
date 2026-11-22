from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = Path(path).read_bytes()
    payload = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    return hashlib.sha1(payload).hexdigest()


def finite_tree(value, path="$"):
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return
    if isinstance(value, (int, float)):
        if not math.isfinite(float(value)):
            raise AssertionError(f"Non-finite value at {path}: {value!r}")
        return
    if isinstance(value, list):
        for i, item in enumerate(value):
            finite_tree(item, f"{path}[{i}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            finite_tree(item, f"{path}.{key}")
        return
    raise AssertionError(f"Unsupported JSON type at {path}: {type(value).__name__}")


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1.0e-300)


def close(a, b, *, rel_tol=1.0e-8, abs_tol=1.0e-12):
    return math.isclose(float(a), float(b), rel_tol=rel_tol, abs_tol=abs_tol)


def main():
    parser = argparse.ArgumentParser(description="Independent B.13 431-point high-order result validator")
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--local-summary", type=Path, required=True)
    parser.add_argument("--source-identity", type=Path, required=True)
    args = parser.parse_args()

    source = args.source_root.resolve()
    results = args.results_dir.resolve()
    local = json.loads(args.local_summary.read_text(encoding="utf-8"))
    identity = json.loads(args.source_identity.read_text(encoding="utf-8"))

    if identity["source_commit"] != local["source_commit"]:
        raise AssertionError("Source identity commit differs from the local run record")

    source_file_checks = {}
    for relpath, expected in identity["files"].items():
        path = source / relpath
        if not path.is_file():
            raise AssertionError(f"Missing source file: {relpath}")
        got_sha = sha256(path)
        got_blob = git_blob_sha1(path)
        if got_sha != expected["sha256"]:
            raise AssertionError(f"Source SHA-256 mismatch: {relpath}")
        if got_blob != expected["git_blob_sha1"]:
            raise AssertionError(f"Git blob SHA-1 mismatch: {relpath}")
        source_file_checks[relpath] = {"sha256": got_sha, "git_blob_sha1": got_blob}

    target_path = source / "finite_mixing/thermal_integrals/results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_TARGETS_INPUT.json"
    profile_path = source / "data/sfho188_digitized.csv"
    driver_path = source / "finite_mixing/thermal_integrals/run_p1b_global06b_threshold_edge_high_order_targets.py"
    raw_path = results / "HIGH_ORDER_TARGETED_POINTS.json"
    summary_path = results / "HIGH_ORDER_ACCEPTANCE_SUMMARY.json"

    targets = json.loads(target_path.read_text(encoding="utf-8"))
    profile = np.genfromtxt(profile_path, delimiter=",", names=True)
    radii = np.asarray(profile["r_km"], dtype=float)
    xgrid = np.asarray(targets["x_grid"], dtype=float)
    xval = np.asarray(targets["x_validation"], dtype=float)
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    finite_tree(raw, "$.raw")
    finite_tree(summary, "$.summary")

    if sha256(target_path) != local["inputs"]["targets_sha256"]:
        raise AssertionError("Target input SHA-256 differs from the local run")
    if sha256(profile_path) != local["inputs"]["profile_sha256"]:
        raise AssertionError("Profile SHA-256 differs from the local run")
    if sha256(driver_path) != local["inputs"]["driver_sha256"]:
        raise AssertionError("Driver SHA-256 differs from the local run")

    radial_keys = set()
    energy_keys = set()
    task_map = {}

    def add_task(target, radius, x):
        key = (round(float(radius), 12), round(float(x), 14))
        target.add(key)
        task_map[key] = (float(radius), float(x))

    for item in targets["radial_top10"]:
        i = int(item["left_index"])
        r0 = float(radii[i])
        r1 = float(radii[i + 1])
        rm = 0.5 * (r0 + r1)
        for radius in (r0, rm, r1):
            for x in xgrid:
                add_task(radial_keys, radius, x)

    for item in targets["energy_worst10"]:
        radius = float(item["r_km"])
        for x in np.r_[xgrid, xval]:
            add_task(energy_keys, radius, x)

    expected_keys = radial_keys | energy_keys
    actual_keys = [(round(float(p["r_km"]), 12), round(float(p["x"]), 14)) for p in raw]
    if len(raw) != len(actual_keys) or len(set(actual_keys)) != len(actual_keys):
        raise AssertionError("Raw result contains duplicate (r,x) points")
    if set(actual_keys) != expected_keys:
        raise AssertionError("Raw result task set differs from independently reconstructed target set")
    if len(raw) != 431 or len(expected_keys) != 431:
        raise AssertionError("Expected exactly 431 unique (r,x) points")
    if len(radii) != 1687 or len(xgrid) != 9 or len(xval) != 8:
        raise AssertionError("Profile or energy-grid node count differs from the local run")
    if len(targets["radial_top10"]) != 10 or len(targets["energy_worst10"]) != 10:
        raise AssertionError("Target selection must contain ten radial and ten energy targets")

    expected_ladder = local["numerics"]["order_ladder"]
    bykey = {(round(float(p["r_km"]), 12), round(float(p["x"]), 14)): p for p in raw}
    ordered_evaluations = 0
    for key, point in bykey.items():
        if point["orders"] != expected_ladder:
            raise AssertionError(f"Unexpected quadrature ladder at {key}")
        ordered_evaluations += len(point["orders"])
        if len(point["successive_changes"]) != 4:
            raise AssertionError(f"Unexpected successive-change sequence at {key}")
        if not close(point["final_change"], point["successive_changes"][-1], rel_tol=1e-13, abs_tol=1e-16):
            raise AssertionError(f"Final convergence change mismatch at {key}")
        if not point["quadrature_pass"] or float(point["final_change"]) >= 1.0e-3:
            raise AssertionError(f"Quadrature convergence failed at {key}")
        if not point["finite_nonnegative"]:
            raise AssertionError(f"Finite/nonnegative result flag failed at {key}")
        payload = point["final_payload"]
        if payload["orders"] != expected_ladder[-1]:
            raise AssertionError(f"Final payload order mismatch at {key}")
        if not payload["all_rates_finite_and_nonnegative"]:
            raise AssertionError(f"Final rate validation failed at {key}")
        if payload["mode_order"] != ["L", "+", "-"]:
            raise AssertionError(f"Mode ordering mismatch at {key}")
        for charge in ("mu_minus", "mu_plus"):
            for field in ("production", "absorption", "reduced_absorption", "spectral_source"):
                values = payload["charge_resolved"][charge][field]
                if len(values) != 3 or any((not math.isfinite(float(v)) or float(v) < 0.0) for v in values):
                    raise AssertionError(f"Invalid {charge}.{field} at {key}")

    if ordered_evaluations != 2155 or summary["nominal_ordered_evaluations"] != 2155:
        raise AssertionError(f"Expected 2,155 ordered evaluations, got {ordered_evaluations}")
    if summary["unique_r_x_points"] != 431:
        raise AssertionError("Summary unique point count mismatch")

    radial_errors = []
    for item in targets["radial_top10"]:
        i = int(item["left_index"])
        r0 = float(radii[i])
        r1 = float(radii[i + 1])
        rm = 0.5 * (r0 + r1)
        for x in xgrid:
            left = bykey[(round(r0, 12), round(float(x), 14))]["final_payload"]
            middle = bykey[(round(rm, 12), round(float(x), 14))]["final_payload"]
            right = bykey[(round(r1, 12), round(float(x), 14))]["final_payload"]
            for charge in ("mu_minus", "mu_plus"):
                for mode_index in range(3):
                    a = float(left["charge_resolved"][charge]["absorption"][mode_index])
                    b = float(right["charge_resolved"][charge]["absorption"][mode_index])
                    prediction = math.exp(0.5 * (math.log(a) + math.log(b))) if a > 0 and b > 0 else 0.5 * (a + b)
                    truth = float(middle["charge_resolved"][charge]["absorption"][mode_index])
                    radial_errors.append(rel(prediction, truth))
    max_radial = max(radial_errors)

    energy_errors = []
    for item in targets["energy_worst10"]:
        radius = float(item["r_km"])
        x = float(item["x_validation"])
        grid_payloads = [bykey[(round(radius, 12), round(float(xx), 14))]["final_payload"] for xx in xgrid]
        direct = bykey[(round(radius, 12), round(x, 14))]["final_payload"]
        for charge in ("mu_minus", "mu_plus"):
            for mode_index in range(3):
                values = np.asarray([p["charge_resolved"][charge]["absorption"][mode_index] for p in grid_payloads], dtype=float)
                truth = float(direct["charge_resolved"][charge]["absorption"][mode_index])
                if np.all(values > 0.0):
                    prediction = float(np.exp(PchipInterpolator(np.sqrt(xgrid), np.log(values))(math.sqrt(x))))
                else:
                    prediction = max(float(PchipInterpolator(np.sqrt(xgrid), values)(math.sqrt(x))), 0.0)
                energy_errors.append(rel(prediction, truth))
    max_energy = max(energy_errors)

    max_final = max(float(p["final_change"]) for p in raw)
    max_db = max(float(p["detailed_balance_max"]) for p in raw)
    max_shell = max(float(p["mass_shell_max"]) for p in raw)
    acceptance = summary["acceptance"]
    computed = {
        "unique_r_x_points": len(raw),
        "nominal_ordered_evaluations": ordered_evaluations,
        "maximum_final_successive_order_change": max_final,
        "maximum_high_order_radial_midpoint_interpolation_error": max_radial,
        "maximum_high_order_energy_pchip_error": max_energy,
        "maximum_detailed_balance_residual": max_db,
        "maximum_mass_shell_residual": max_shell,
    }
    for key in (
        "maximum_final_successive_order_change",
        "maximum_high_order_radial_midpoint_interpolation_error",
        "maximum_high_order_energy_pchip_error",
        "maximum_detailed_balance_residual",
        "maximum_mass_shell_residual",
    ):
        if not close(computed[key], acceptance[key], rel_tol=1e-11, abs_tol=1e-15):
            raise AssertionError(f"Recomputed {key} differs from stored summary")
        local_value = local["numerics"][key]
        if not close(computed[key], local_value, rel_tol=1e-7, abs_tol=1e-12):
            raise AssertionError(f"Independent reproduction differs from local {key}")

    if not acceptance["all_targeted_quadrature_pass"]:
        raise AssertionError("Summary says targeted quadrature did not pass")
    if not acceptance["all_rates_finite_nonnegative"]:
        raise AssertionError("Summary says rates are not finite/nonnegative")
    if acceptance["full_global_high_order_acceptance"] is not False:
        raise AssertionError("The targeted calculation must not claim full-global acceptance")

    raw_sha = sha256(raw_path)
    summary_sha = sha256(summary_path)
    local_raw_sha = local["hashes"]["raw_results_sha256"]
    report = {
        "status": "PASS",
        "source_commit": identity["source_commit"],
        "source_file_checks": len(source_file_checks),
        "profile_radial_rows": len(radii),
        "radial_unique_r_x_points": len(radial_keys),
        "energy_unique_r_x_points": len(energy_keys),
        "intersection_points": len(radial_keys & energy_keys),
        "unique_r_x_points": len(raw),
        "nominal_ordered_evaluations": ordered_evaluations,
        "actual_orders_per_point": 5,
        "all_targeted_quadrature_pass": True,
        "all_rates_finite_nonnegative": True,
        "maximum_final_successive_order_change": max_final,
        "maximum_high_order_radial_midpoint_interpolation_error": max_radial,
        "maximum_high_order_energy_pchip_error": max_energy,
        "maximum_detailed_balance_residual": max_db,
        "maximum_mass_shell_residual": max_shell,
        "local_raw_results_sha256": local_raw_sha,
        "independent_rerun_raw_results_sha256": raw_sha,
        "byte_identical_to_local_raw_results": raw_sha == local_raw_sha,
        "local_summary_sha256": local["hashes"]["local_summary_sha256"],
        "independent_rerun_summary_sha256": summary_sha,
        "full_global_high_order_acceptance": False,
        "scope": local["scope"]
    }
    (results / "INDEPENDENT_VALIDATION_REPORT.json").write_text(
        json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
