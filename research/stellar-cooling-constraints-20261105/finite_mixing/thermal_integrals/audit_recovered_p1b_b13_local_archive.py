#!/usr/bin/env python3
"""Independent, inexpensive audit of the recovered P1-B B.13 CSV archive.

This is post-processing only. It does not rerun the collision integral or B.2 transport.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math
from collections import defaultdict
from pathlib import Path

EXPECTED_PROFILE_BLOB = "e41df78c8035540760fbcb7ef592cd830171822e"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def relerr(a: float, b: float) -> float:
    return abs(a-b) / max(abs(a), abs(b), 1e-300)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--current-profile-blob", default=EXPECTED_PROFILE_BLOB)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    manifest = json.loads((args.archive / "MANIFEST.json").read_text())
    csv_path = args.archive / "p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.csv"
    actual_csv_sha = sha256(csv_path)
    assert actual_csv_sha == manifest["outputs"][csv_path.name]
    assert args.current_profile_blob == EXPECTED_PROFILE_BLOB
    assert manifest["profile_sha256"] == "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"

    with csv_path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == manifest["csv_rows"] == 5886
    groups = defaultdict(list)
    for row in rows:
        groups[(row["point_type"], float(row["radius_km"]),
                float(row["omega_local_MeV"]))].append(row)
        for field in ("production_MeV", "absorption_MeV",
                      "reduced_absorption_MeV", "spectral_source_MeV5"):
            assert math.isfinite(float(row[field])) and float(row[field]) >= 0
    assert len(groups) == 981
    assert all(len(v) == 6 for v in groups.values())

    grid = [r for r in rows if r["point_type"] == "grid_node"]
    mids = [r for r in rows if r["point_type"] == "cell_midpoint"]
    assert len(grid) == 3078 and len(mids) == 2808
    assert {r["charge"] for r in rows} == {"mu_minus", "mu_plus"}
    assert {r["mode"] for r in rows} == {"L", "+", "-"}

    max_db = max(float(r["detailed_balance_relative_residual"]) for r in rows)
    max_shell = max(float(r["final_muon_shell_relative_error"]) for r in rows)
    max_refine_row = max(grid, key=lambda r: float(r["quadrature_refinement_relative_change"]))
    max_interp_row = max(mids, key=lambda r: float(r["direct_vs_interpolated_relative_error"]))
    interp = [float(r["direct_vs_interpolated_relative_error"]) for r in mids]
    grid_refine = [float(r["quadrature_refinement_relative_change"]) for r in grid]

    # Verify the transverse degeneracy and compare longitudinal to transverse.
    by_point = defaultdict(dict)
    for r in grid:
        by_point[(float(r["radius_km"]), float(r["omega_local_MeV"]), r["charge"])][r["mode"]] = float(r["absorption_MeV"])
    transverse_max = max(relerr(v["+"], v["-"]) for v in by_point.values())
    longitudinal_max = max(relerr(v["L"], v["+"]) for v in by_point.values())

    # 8--15 km local 10 MeV shell means, preserving charge and mode.
    shell = [r for r in grid if 8 <= float(r["radius_km"]) <= 15
             and math.isclose(float(r["omega_local_MeV"]), 10.0, rel_tol=0, abs_tol=1e-12)]
    shell_summary = {}
    for charge in ("mu_minus", "mu_plus"):
        for mode in ("L", "+", "-"):
            selected = [r for r in shell if r["charge"] == charge and r["mode"] == mode]
            shell_summary[f"{charge}/{mode}"] = {
                "n_radial_nodes": len(selected),
                "production_mean_MeV": sum(float(r["production_MeV"]) for r in selected)/len(selected),
                "production_max_MeV": max(float(r["production_MeV"]) for r in selected),
                "absorption_mean_MeV": sum(float(r["absorption_MeV"]) for r in selected)/len(selected),
                "absorption_max_MeV": max(float(r["absorption_MeV"]) for r in selected),
            }

    result = {
      "status": "LOCAL_POSTPROCESSING_AUDIT_COMPLETE__P1B_ACCEPTANCE_STILL_FAILED",
      "scope": "Recovered local B.13 rates only; no B.2 optical depth or Fig. 7 transport rerun",
      "identity": {
        "source_run_id": manifest["source_run_id"],
        "source_artifact_id": manifest["source_artifact_id"],
        "source_json_sha256": manifest["input_json_sha256"],
        "csv_sha256_verified": actual_csv_sha,
        "archived_profile_sha256": manifest["profile_sha256"],
        "current_profile_git_blob_sha1": args.current_profile_blob,
        "source_snapshot_profile_git_blob_sha1": EXPECTED_PROFILE_BLOB,
        "profile_blob_identity_match": True
      },
      "coverage": {
        "grid_nodes": manifest["grid_nodes"], "cell_midpoints": manifest["cell_midpoints"],
        "csv_rows": len(rows), "unique_radius_energy_points": len(groups),
        "charges": ["mu_minus", "mu_plus"], "modes": ["L", "+", "-"],
        "grid_radius_km": [min(float(r["radius_km"]) for r in grid), max(float(r["radius_km"]) for r in grid)],
        "grid_local_energy_MeV": [min(float(r["omega_local_MeV"]) for r in grid), max(float(r["omega_local_MeV"]) for r in grid)],
        "midpoint_radius_km": [min(float(r["radius_km"]) for r in mids), max(float(r["radius_km"]) for r in mids)],
        "midpoint_local_energy_MeV": [min(float(r["omega_local_MeV"]) for r in mids), max(float(r["omega_local_MeV"]) for r in mids)]
      },
      "local_rate_checks": {
        "all_rates_finite_nonnegative": True,
        "max_detailed_balance_relative_residual": max_db,
        "detailed_balance_tolerance": manifest["acceptance"]["detailed_balance_tolerance"],
        "max_final_muon_shell_relative_error": max_shell,
        "mass_shell_tolerance": manifest["acceptance"]["mass_shell_tolerance"],
        "transverse_plus_minus_max_relative_difference": transverse_max,
        "longitudinal_vs_plus_max_relative_difference": longitudinal_max,
        "ten_MeV_8_15_km_shell": shell_summary
      },
      "quadrature": {
        "maximum_grid_node_refinement_change": max(grid_refine),
        "maximum_grid_node_location": {k: max_refine_row[k] for k in ("radius_km","omega_local_MeV","charge","mode")},
        "project_tolerance": manifest["acceptance"]["quadrature_relative_tolerance"],
        "fraction_grid_rows_above_tolerance": sum(x > manifest["acceptance"]["quadrature_relative_tolerance"] for x in grid_refine)/len(grid_refine)
      },
      "interpolation": {
        "maximum_direct_midpoint_vs_sequential_log_interpolation_error": max(interp),
        "maximum_error_location": {k: max_interp_row[k] for k in ("radius_km","omega_local_MeV","charge","mode")},
        "median_relative_error": sorted(interp)[len(interp)//2],
        "fraction_midpoint_rows_above_1pct": sum(x > .01 for x in interp)/len(interp),
        "fraction_midpoint_rows_above_10pct": sum(x > .10 for x in interp)/len(interp),
        "project_tolerance": manifest["acceptance"]["interpolation_relative_tolerance"]
      },
      "acceptance": {
        "detailed_balance": "PASS",
        "mass_shell": "PASS",
        "local_emissivity_energy_integral": "PASS",
        "quadrature": "FAIL",
        "interpolation": "FAIL",
        "overall_p1b": "FAIL"
      },
      "interpretation": [
        "Current profile B and the historical source-snapshot profile have the same Git blob SHA; this establishes profile-file identity, not independent validation of the reconstructed astrophysical profile.",
        "The archived local rates pass detailed-balance and final-muon mass-shell checks.",
        "The archived grid-node quadrature does not meet the project 0.1% criterion.",
        "Direct midpoint versus sequential log interpolation fails the project 1% criterion substantially; do not feed these interpolated rates into B.2 as if accepted.",
        "The local audit does not establish scalar or mode-resolved optical depths, global transport, or Fig. 7 reproduction."
      ]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
