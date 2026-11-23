"""Reconstruct and compare the B.16 high-order energy-grid identities.

2026-11-23 exact-head refresh after strict phase-space re-run.

This is a read-only diagnostic. It does not evaluate production rates, opacity,
luminosity, or alter any physics input. It reproduces the energy-grid
construction used by the archived high-order run and the B.16 phase-space
post-processor, then compares both with the archived baseline fingerprint.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path

import numpy as np
import scipy

try:
    from .reference import DEFAULT_PROFILE, radial_rule, load_profile
    from .audit_b16_global_redshift import sha256
    from .energy_grid_identity import (
        DEFAULT_ENERGY_GRID_REFERENCE, compare_energy_grid,
        float_array_sha256, load_energy_grid_reference,
    )
except ImportError:
    from reference import DEFAULT_PROFILE, radial_rule, load_profile
    from audit_b16_global_redshift import sha256
    from energy_grid_identity import (
        DEFAULT_ENERGY_GRID_REFERENCE, compare_energy_grid,
        float_array_sha256, load_energy_grid_reference,
    )

HERE = Path(__file__).resolve().parent
DEFAULT_BASELINE = (
    HERE / "outputs" / "b16_global_high_order_independent_grid_10mev_2026-11-09.json"
)
DEFAULT_OUTPUT = HERE / "outputs" / "b16_energy_grid_identity_diagnostic_2026-11-17.json"
HISTORICAL_FAILED_HASH = (
    "db6f613c7c76c3a80b07f20b6b44feb9520b031e78237685dacd60575c964639"
)


def build_energy_grid(mass: float, energy_order: int, energy_offset: float,
                      lapse: np.ndarray) -> tuple[np.ndarray, dict]:
    """Copy the exact energy-grid construction used by both B.16 drivers."""
    seed = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    thresholds = mass / np.asarray(lapse, dtype=float)
    merged = np.unique(np.r_[seed, thresholds])
    filtered = merged[merged > mass * (1.0 + 1.0e-10)]
    filtered.sort()
    return filtered, {
        "seed_node_count": int(len(seed)),
        "lapse_threshold_node_count": int(len(thresholds)),
        "merged_unique_node_count": int(len(merged)),
        "filtered_node_count": int(len(filtered)),
        "duplicates_removed": int(len(seed) + len(thresholds) - len(merged)),
        "threshold_min_MeV": float(np.min(thresholds)),
        "threshold_max_MeV": float(np.max(thresholds)),
        "energy_min_MeV": float(np.min(filtered)),
        "energy_max_MeV": float(np.max(filtered)),
    }


def _profile_lapse_direct(profile_path: Path, opacity_grid: np.ndarray) -> np.ndarray:
    """Independent CSV read/interpolation, avoiding reference.load_profile."""
    data = np.genfromtxt(profile_path, delimiter=",", names=True)
    required = ("r_km", "lapse")
    if any(name not in data.dtype.names for name in required):
        raise ValueError(f"Profile must contain columns {required}")
    return np.interp(opacity_grid, data["r_km"], data["lapse"])


def run(profile_path: Path, baseline_path: Path, mass: float,
        radial_order: int, opacity_order: int, energy_order: int,
        energy_offset: float, grid_reference_path: Path = DEFAULT_ENERGY_GRID_REFERENCE) -> dict:
    baseline_payload = json.loads(baseline_path.read_text(encoding="utf-8"))
    baseline = baseline_payload["result"]
    baseline_config = baseline["configuration"]

    source_r, _ = radial_rule(25.0, radial_order)
    opacity_r, _ = radial_rule(25.0, opacity_order)
    opacity_grid = np.unique(np.r_[0.0, opacity_r, 25.0])

    # Path A: reproduce the high-order run_mass() setup:
    # radial_grid = unique([0, opacity_r, radius]); p = load_profile(...).
    high_order_profile = load_profile(profile_path, opacity_grid)
    energy_high_order, details_high_order = build_energy_grid(
        mass, energy_order, energy_offset, high_order_profile["lapse"]
    )

    # Path B: reproduce the phase-space script setup:
    # opacity_grid is built independently; opacity_profile is loaded there.
    phase_profile = load_profile(profile_path, opacity_grid)
    energy_phase, details_phase = build_energy_grid(
        mass, energy_order, energy_offset, phase_profile["lapse"]
    )

    # Path C: independently read/interpolate the CSV lapse column.
    direct_lapse = _profile_lapse_direct(profile_path, opacity_grid)
    energy_direct, details_direct = build_energy_grid(
        mass, energy_order, energy_offset, direct_lapse
    )

    high_hash = float_array_sha256(energy_high_order)
    phase_hash = float_array_sha256(energy_phase)
    direct_hash = float_array_sha256(energy_direct)
    expected_hash = baseline_config["energy_grid_sha256"]
    grid_reference = load_energy_grid_reference(grid_reference_path, expected_hash)
    grid_comparison = compare_energy_grid(energy_high_order, grid_reference)
    profile_hash = sha256(profile_path)

    current_code_hashes = {
        "audit_b16_global_redshift.py": sha256(HERE / "audit_b16_global_redshift.py"),
        "reference.py": sha256(HERE / "reference.py"),
        "audit_b16_escape_phase_space.py": sha256(HERE / "audit_b16_escape_phase_space.py"),
    }
    baseline_code_hashes = baseline.get("code_sha256", {})

    paths_equal = (
        np.array_equal(energy_high_order, energy_phase)
        and np.array_equal(energy_high_order, energy_direct)
    )
    lapse_equal = (
        np.array_equal(high_order_profile["lapse"], phase_profile["lapse"])
        and np.array_equal(high_order_profile["lapse"], direct_lapse)
    )
    baseline_hash_match = high_hash == expected_hash
    baseline_match = grid_comparison["matches"]
    profile_match = profile_hash == baseline["profile"]["sha256"]

    return {
        "title": "B.16 energy-grid identity diagnostic",
        "status": (
            "baseline_reproduced"
            if paths_equal and baseline_match and profile_match
            else "revision_required"
        ),
        "scope": (
            "Read-only grid reconstruction only; no local rates, opacity, "
            "escape probability, luminosity, or axial-vector output is computed."
        ),
        "inputs": {
            "mass_MeV": float(mass),
            "radius_km": 25.0,
            "source_radial_order": int(radial_order),
            "opacity_order": int(opacity_order),
            "energy_order": int(energy_order),
            "energy_offset_MeV": float(energy_offset),
            "profile_path": str(profile_path),
            "profile_sha256": profile_hash,
            "baseline_profile_sha256": baseline["profile"]["sha256"],
            "profile_matches_baseline": bool(profile_match),
            "baseline_run_commit_sha": baseline_payload.get("run_commit_sha"),
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "platform": platform.platform(),
            "byteorder": sys.byteorder,
            "hash_encoding": "little-endian float64 bytes",
        },
        "grid_identity": {
            "source_node_count": int(len(source_r)),
            "source_grid_sha256": float_array_sha256(source_r),
            "opacity_node_count": int(len(opacity_grid)),
            "opacity_grid_sha256": float_array_sha256(opacity_grid),
            "expected_baseline_energy_node_count": int(baseline_config["energy_node_count"]),
            "actual_energy_node_count": int(len(energy_high_order)),
            "expected_baseline_energy_grid_sha256": expected_hash,
            "high_order_driver_energy_grid_sha256": high_hash,
            "phase_space_driver_energy_grid_sha256": phase_hash,
            "direct_csv_energy_grid_sha256": direct_hash,
            "historical_failed_run_energy_grid_sha256": HISTORICAL_FAILED_HASH,
            "energy_grid_reference_file_sha256": grid_reference["_file_sha256"],
        },
        "construction_details": {
            "high_order_driver": details_high_order,
            "phase_space_driver": details_phase,
            "direct_csv_interpolation": details_direct,
        },
        "comparisons": {
            "high_order_vs_phase_array_equal": bool(np.array_equal(energy_high_order, energy_phase)),
            "high_order_vs_direct_csv_array_equal": bool(np.array_equal(energy_high_order, energy_direct)),
            "lapse_arrays_equal": bool(lapse_equal),
            "max_abs_lapse_difference": float(max(
                np.max(np.abs(high_order_profile["lapse"] - phase_profile["lapse"])),
                np.max(np.abs(high_order_profile["lapse"] - direct_lapse)),
            )),
            "high_order_vs_baseline_hash_match": bool(baseline_hash_match),
            "high_order_vs_baseline_nodes_match": bool(baseline_match),
            "energy_grid_reference_comparison": grid_comparison,
            "profile_hash_matches_baseline": bool(profile_match),
            "current_code_sha256": current_code_hashes,
            "baseline_code_sha256": baseline_code_hashes,
        },
        "energy_grid_edges_MeV": {
            "first_12": energy_high_order[:12].tolist(),
            "last_12": energy_high_order[-12:].tolist(),
        },
        "energy_grid_nodes_MeV": energy_high_order.tolist(),
        "energy_grid_seed_nodes_MeV": (
            mass + np.geomspace(
                max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
            )
        ).tolist(),
        "energy_grid_lapse_threshold_nodes_MeV": (
            mass / high_order_profile["lapse"]
        ).tolist(),
        "interpretation": (
            "A matching current grid with a historical failed-run mismatch means "
            "the old failure is not reproducible from the current main inputs. "
            "A current mismatch requires inspecting the saved grid arrays and "
            "code/input fingerprints before changing any baseline."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--nr", type=int, default=200)
    parser.add_argument("--opacity-order", type=int, default=640)
    parser.add_argument("--ne", type=int, default=200)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    parser.add_argument("--strict-baseline", action="store_true")
    parser.add_argument("--grid-reference", type=Path, default=DEFAULT_ENERGY_GRID_REFERENCE)
    args = parser.parse_args()

    result = run(
        args.profile, args.baseline, args.mass, args.nr,
        args.opacity_order, args.ne, args.energy_offset, args.grid_reference
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)

    if not result["comparisons"]["high_order_vs_phase_array_equal"]:
        return 2
    if not result["comparisons"]["high_order_vs_direct_csv_array_equal"]:
        return 3
    if args.strict_baseline and result["status"] != "baseline_reproduced":
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
