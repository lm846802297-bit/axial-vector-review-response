#!/usr/bin/env python3
"""Archive the existing A0 10 MeV radial/energy results; never rerun physics."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from archive_croon_c1_10mev import (
    ck, digest, dump, filehash, flatten, gitshow, load, now, record, rel,
    status, unit_curve, unit_profile, verify_sums, write_curve,
)

RADIAL_RUN_ID = 44671688630
RADIAL_COMMIT = "066039c8ca24f5fa747b88ad4bd6bcbc9e4c6393"
RADIAL_START = "2026-11-20T04:02:16Z"
RADIAL_END = "2026-11-20T04:17:03Z"
BASELINE_RUN_ID = 44656918116
BASELINE_COMMIT = "a76c6714f25140cbedc9792cd5c10a5254218a71"
ENERGY_RUN_ID = 44673753335
ENERGY_COMMIT = "770d64926d9981328e9cc082bdb2e8e34d2ca287"
ENERGY_START = "2026-11-20T04:20:33Z"
ENERGY_END = None  # Filled from the completed workflow record before final archive.
PROFILE_SHA = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
PROFILE_BYTES = 182716
BASE = "research/stellar-cooling-constraints-20261105"
HERE_REL = f"{BASE}/blinov_reproduction"
P = {
    "profile": f"{BASE}/data/sfho188_digitized.csv",
    "radial_audit": f"{HERE_REL}/audit_croon_a0_10mev_adaptive_radial_convergence.py",
    "energy_audit": f"{HERE_REL}/audit_croon_a0_10mev_adaptive_energy_convergence.py",
    "a0_core": f"{HERE_REL}/croon_a0_uv_axial_transport.py",
    "c1_core": f"{HERE_REL}/croon_c1_b13_vector_transport.py",
    "adaptive": f"{HERE_REL}/adaptive_radial_transport.py",
    "finite_model": f"{BASE}/finite_mixing/model.py",
    "radial_workflow": ".github/workflows/croon-a0-10mev-adaptive-radial-convergence.yml",
    "energy_workflow": ".github/workflows/croon-a0-10mev-adaptive-energy-convergence.yml",
    "a0_103_json": f"{HERE_REL}/outputs/croon_a0_uv_axial_transport_10mev_2026-11-20.json",
    "a0_103_csv": f"{HERE_REL}/outputs/croon_a0_uv_axial_transport_10mev_2026-11-20.csv",
    "a0_153_32_json": f"{HERE_REL}/outputs/croon_a0_uv_axial_transport_10mev_153nodes_adaptive_2026-11-20.json",
    "a0_153_32_csv": f"{HERE_REL}/outputs/croon_a0_uv_axial_transport_10mev_153nodes_adaptive_2026-11-20.csv",
    "c1_153_32_json": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_2026-11-20.json",
    "radial_report": f"{HERE_REL}/outputs/A0_10MEV_ADAPTIVE_RADIAL_CONVERGENCE_2026-11-20.json",
    "radial_sums": f"{HERE_REL}/outputs/SHA256SUMS_croon_a0_adaptive_radial_convergence_2026-11-20.txt",
    "a0_153_48_json": f"{HERE_REL}/outputs/croon_a0_uv_axial_transport_10mev_153nodes_adaptive_energy48_2026-11-20.json",
    "a0_153_48_csv": f"{HERE_REL}/outputs/croon_a0_uv_axial_transport_10mev_153nodes_adaptive_energy48_2026-11-20.csv",
    "c1_153_48_json": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_energy48_2026-11-20.json",
    "energy_report": f"{HERE_REL}/outputs/A0_10MEV_ADAPTIVE_ENERGY_CONVERGENCE_2026-11-20.json",
    "energy_sums": f"{HERE_REL}/outputs/SHA256SUMS_croon_a0_adaptive_energy_convergence_2026-11-20.txt",
}

def _source_hashes(root: Path, commit: str, keys: tuple[str, ...]) -> dict[str, str]:
    hashes = {}
    for key in keys:
        path = P[key]
        blob = gitshow(root, commit, path)
        current = (root / path).read_bytes()
        if current != blob:
            raise ValueError(f"source file differs from recorded commit {commit}: {path}")
        hashes[path] = digest(blob)
    return hashes

def _input(root: Path, archived_path: Path, original_path: str, name: str,
           source: str, version: str, commit: str) -> dict:
    sha = filehash(archived_path)
    return {
        "name": name, "source": source, "version": version,
        "path": rel(root, archived_path),
        "uri": f"https://github.com/lm846802297-bit/axial-vector-review-response/blob/{commit}/{original_path}",
        "format": "csv" if archived_path.suffix.lower() == ".csv" else "json",
        "bytes": archived_path.stat().st_size, "sha256": sha,
        "access": "byte-for-byte archive snapshot; original source URI retained",
        "transformation": "copied without numerical or content transformation",
    }

def build(root: Path, out: Path) -> Path:
    root, out = root.resolve(), out.resolve()
    out.relative_to(root)
    raw = {key: root / value for key, value in P.items()}
    radial = load(raw["radial_report"])
    base103 = load(raw["a0_103_json"])
    fine32 = load(raw["a0_153_32_json"])
    c1_32 = load(raw["c1_153_32_json"])
    a0_103_item = base103["masses"]["10"]
    a0_32_item = fine32["masses"]["10"]
    if radial["status"] != "PASS":
        raise ValueError("A0 radial 103/153-node convergence report is not PASS")
    if radial["baseline"]["sha256"] != filehash(raw["a0_103_json"]):
        raise ValueError("A0 103-node baseline JSON hash mismatch")
    if radial["refined"]["sha256_json"] != filehash(raw["a0_153_32_json"]):
        raise ValueError("A0 153-node energy-32 JSON hash mismatch")
    if radial["refined"]["sha256_csv"] != filehash(raw["a0_153_32_csv"]):
        raise ValueError("A0 153-node energy-32 CSV hash mismatch")
    if fine32["source_profile"]["sha256"] != PROFILE_SHA:
        raise ValueError("A0 profile SHA-256 mismatch")
    if a0_103_item["radial_points"] != 103 or a0_32_item["radial_points"] != 153:
        raise ValueError("unexpected A0 radial grid")
    if a0_32_item["energy_points"] != 32 or a0_32_item["polarization_modes"] != ["L", "+", "-"]:
        raise ValueError("unexpected A0 153-node reference resolution or polarization basis")
    if radial["B7_unchanged_against_C1_153node"]["total_relative_difference"] >= 1.0e-12:
        raise ValueError("A0 B.7 source does not match the C1 same-grid reference")
    if max(radial["B7_unchanged_against_C1_153node"]["per_mode_relative_differences"].values()) >= 1.0e-12:
        raise ValueError("A0 B.7 mode-resolved source does not match C1")

    profile_ok = raw["profile"].is_file() and filehash(raw["profile"]) == PROFILE_SHA
    if not profile_ok:
        raise ValueError("SFHo-18.8 profile is missing or its SHA-256 changed")
    radial_checksums = verify_sums(raw["radial_sums"], root / HERE_REL)

    energy_available = all(raw[key].is_file() for key in (
        "a0_153_48_json", "a0_153_48_csv", "c1_153_48_json",
        "energy_report", "energy_sums",
    ))
    energy = None
    energy_checksums = []
    if energy_available:
        energy = load(raw["energy_report"])
        fine48 = load(raw["a0_153_48_json"])
        c1_48 = load(raw["c1_153_48_json"])
        if energy["status"] != "PASS":
            raise ValueError("A0 energy-32/48 convergence report is not PASS")
        if energy["baseline"]["sha256_json"] != filehash(raw["a0_153_32_json"]):
            raise ValueError("A0 energy-32 baseline hash mismatch")
        if energy["refined"]["sha256_json"] != filehash(raw["a0_153_48_json"]):
            raise ValueError("A0 energy-48 JSON hash mismatch")
        if energy["refined"]["sha256_csv"] != filehash(raw["a0_153_48_csv"]):
            raise ValueError("A0 energy-48 CSV hash mismatch")
        if fine48["masses"]["10"]["radial_points"] != 153 or fine48["masses"]["10"]["energy_points"] != 48:
            raise ValueError("unexpected A0 energy-48 grid")
        energy_checksums = verify_sums(raw["energy_sums"], root / HERE_REL)
        final_json = raw["a0_153_48_json"]
        final_csv = raw["a0_153_48_csv"]
        final_item = fine48["masses"]["10"]
        run_id = f"A0-10MeV-153R-48E-20261120-{ENERGY_RUN_ID}"
        primary_commit = ENERGY_COMMIT
        primary_audit = P["energy_audit"]
        primary_workflow = P["energy_workflow"]
        primary_run = ENERGY_RUN_ID
        primary_start = ENERGY_START
        primary_end = ENERGY_END
    else:
        final_json = raw["a0_153_32_json"]
        final_csv = raw["a0_153_32_csv"]
        final_item = a0_32_item
        run_id = f"A0-10MeV-153R-32E-20261120-{RADIAL_RUN_ID}"
        primary_commit = RADIAL_COMMIT
        primary_audit = P["radial_audit"]
        primary_workflow = P["radial_workflow"]
        primary_run = RADIAL_RUN_ID
        primary_start = RADIAL_START
        primary_end = RADIAL_END

    radial_sources = ("radial_audit", "a0_core", "c1_core", "adaptive",
                      "finite_model", "radial_workflow", "profile")
    radial_source_hashes = _source_hashes(root, RADIAL_COMMIT, radial_sources)
    energy_source_hashes = {}
    if energy_available:
        energy_sources = ("energy_audit", "a0_core", "c1_core", "adaptive",
                          "finite_model", "energy_workflow", "profile")
        energy_source_hashes = _source_hashes(root, ENERGY_COMMIT, energy_sources)

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    snapshots = {
        "profile": (P["profile"], "sfho188_digitized.csv"),
        "a0_103_json": (P["a0_103_json"], "radial_103_nodes.json"),
        "a0_103_csv": (P["a0_103_csv"], "radial_103_nodes.csv"),
        "a0_153_32_json": (P["a0_153_32_json"], "radial_153_nodes_energy32.json"),
        "a0_153_32_csv": (P["a0_153_32_csv"], "radial_153_nodes_energy32.csv"),
        "c1_153_32_json": (P["c1_153_32_json"], "c1_153_nodes_B7_reference.json"),
        "radial_report": (P["radial_report"], "radial_convergence_report.json"),
        "radial_sums": (P["radial_sums"], "radial_native_SHA256SUMS.txt"),
    }
    if energy_available:
        snapshots.update({
            "a0_153_48_json": (P["a0_153_48_json"], "radial_153_nodes_energy48.json"),
            "a0_153_48_csv": (P["a0_153_48_csv"], "radial_153_nodes_energy48.csv"),
            "c1_153_48_json": (P["c1_153_48_json"], "c1_153_nodes_energy48_B7_reference.json"),
            "energy_report": (P["energy_report"], "energy_convergence_report.json"),
            "energy_sums": (P["energy_sums"], "energy_native_SHA256SUMS.txt"),
        })
    archived = {}
    for key, (source_rel, name) in snapshots.items():
        target = out / name
        shutil.copyfile(root / source_rel, target)
        if filehash(target) != filehash(root / source_rel):
            raise ValueError(f"archive copy changed bytes: {source_rel}")
        archived[key] = target

    curve_path = out / "coupling_curve.csv"
    curve_columns, curve_units, curve_rows = write_curve(curve_path, final_item["coupling_curve"])
    radial_max = float(radial["maximum_radial_change_metric"])
    radial_target = float(radial["target"])
    radial_rnu = float(radial["total_curve_changes"]["Rfar_Rnu_adaptive_quad"]["max_pointwise_relative_difference_above_1e-8_peak"])
    radial_100 = float(radial["total_curve_changes"]["Rfar_100km_vacuum_nu_tail_adaptive_quad"]["max_pointwise_relative_difference_above_1e-8_peak"])
    b7_diff = float(radial["B7_unchanged_against_C1_153node"]["total_relative_difference"])
    qmax = float(radial["max_quadpack_relative_error_estimate"])
    closure = float(radial["max_mode_sum_relative_residual"])
    db7 = float(radial["detailed_balance"]["max_B7_mode_residual"])
    db13 = float(radial["detailed_balance"]["max_B13_charge_mode_residual"])
    shell = float(radial["detailed_balance"]["max_final_muon_shell_relative_error"])
    surface = sum(float(x) for x in final_item["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"].values())
    energy_max = float(energy["maximum_over_all_reported_metrics"]) if energy_available else None
    energy_target = float(energy["target"]) if energy_available else 1.0e-4

    convergence = {
        "schema_version": "1.0.0",
        "report_type": "supernova_transport_convergence",
        "run_id": run_id,
        "created_at": now(),
        "status": "PASS" if energy_available else "PARTIAL",
        "radial_grid": {
            "workflow_run_id": RADIAL_RUN_ID,
            "workflow_source_commit": RADIAL_COMMIT,
            "workflow_started_at": RADIAL_START,
            "workflow_finished_at": RADIAL_END,
            "coarse_radial_points": radial["baseline"]["radial_points"],
            "fine_radial_points": radial["refined"]["radial_points"],
            "energy_order_fixed": radial["refined"]["energy_order"],
            "coupling_points": radial["fixed_parameters"]["coupling_count"],
            "maximum_radial_change_metric": radial_max,
            "acceptance_threshold": radial_target,
            "Rfar_Rnu_max_pointwise_relative_change": radial_rnu,
            "Rfar_100km_max_pointwise_relative_change": radial_100,
            "maximum_QUADPACK_relative_error_estimate": qmax,
            "maximum_three_mode_closure_residual": closure,
            "B7_unchanged_against_C1_153node": radial["B7_unchanged_against_C1_153node"],
            "detailed_balance": radial["detailed_balance"],
        },
        "energy_order": {
            "status": "PASS" if energy_available else "not_run",
            "workflow_run_id": ENERGY_RUN_ID if energy_available else None,
            "workflow_source_commit": ENERGY_COMMIT if energy_available else None,
            "workflow_started_at": ENERGY_START if energy_available else None,
            "workflow_finished_at": ENERGY_END if energy_available else None,
            "reference_energy_order": 32,
            "refined_energy_order": 48 if energy_available else None,
            "radial_points_fixed": 153,
            "maximum_over_all_reported_metrics": energy_max,
            "acceptance_threshold": energy_target,
            "reason_not_run": None if energy_available else "The independent 153-node, energy-48 A0 run has not yet produced committed outputs.",
        },
        "scope": (
            "A0 finite-mixing axial-vector 10 MeV interior-profile transport. "
            "Outer 25-100 km B.13 semi-Compton opacity is omitted; this is not an SN1987A exclusion curve."
        ),
    }
    convergence_path = out / "convergence_report.json"
    dump(convergence_path, convergence)

    source_total = final_item["thin_source_per_g2_erg_s"]
    source_ratios = final_item["thin_source_ratios"]
    peak_rnu = max(final_item["coupling_curve"], key=lambda row: row["Rfar_Rnu_adaptive_quad"])
    peak_100 = max(final_item["coupling_curve"], key=lambda row: row["Rfar_100km_vacuum_nu_tail_adaptive_quad"])
    summary = {
        "schema_version": "1.0.0",
        "record_type": "result_summary",
        "run_id": run_id,
        "created_at": now(),
        "project": {
            "repository": "lm846802297-bit/axial-vector-review-response",
            "project_id": "axial-vector-supernova-cooling",
            "workstream_id": "A0-10MeV",
        },
        "calculation": "A0 finite-mixing axial-vector B.7 plus charge-resolved exact-recoil B.13 interior-profile transport",
        "scope": {
            "included": [
                "B.7 unchanged two-flavour neutrino coalescence/inverse decay",
                "B.13 moving-muon semi-Compton production and inverse absorption with exact final-muon recoil",
                "mu_minus and mu_plus targets separately",
                "three massive-vector polarization modes L, +, -",
                "adaptive radial integration and 121-point g_X coupling scan",
                "103/153 radial comparison" + (", 32/48 energy-order comparison" if energy_available else ""),
            ],
            "excluded": [
                "outer 25-100 km B.13 semi-Compton opacity",
                "angular escape average",
                "lapse/redshift correction in the Croon Sec. 3 comparison convention",
                "final SN1987A exclusion curve",
            ],
            "assumptions": [
                "reconstructed SFHo-18.8 1 s interior profile",
                "theta_mu_R=0.01 with mass-basis gV/gX and gA/gX",
                "B.7 two-flavour vacuum neutrino tail to R_far=100 km",
            ],
        },
        "benchmark": {
            "mediator_mass": {"value": 10.0, "unit": "MeV"},
            "theta_mu_R": 0.01,
            "muon_couplings": {
                "gV_over_gX": final_item["model"]["gV_mu_over_gX"] if "model" in final_item else base103["model"]["gV_mu_over_gX"],
                "gA_over_gX": final_item["model"]["gA_mu_over_gX"] if "model" in final_item else base103["model"]["gA_mu_over_gX"],
            },
            "neutrino_couplings_over_gX": {"nu_mu": 1.0, "nu_tau": -1.0},
            "muon_targets": ["mu_minus", "mu_plus"],
            "polarizations": ["L", "+", "-"],
            "radial_points": final_item["radial_points"],
            "energy_order": final_item["energy_points"],
            "inner_orders": final_item["inner_orders"],
            "neutrino_angular_order": final_item["neutrino_angular_order"],
            "susceptibility_order": final_item["susceptibility_order"],
            "coupling_scan": {"minimum": 1.0e-11, "maximum": 1.0, "points": 121},
            "R_nu": {"value": final_item["R_nu_km"], "unit": "km"},
        },
        "observables": [
            {"name": "thin_source_B7_per_gX2", "value": source_total["B7_nu_mu_plus_nu_tau"], "unit": "erg s^-1", "status": "computed"},
            {"name": "thin_source_B13_mu_minus_per_gX2", "value": source_total["B13_mu_minus"], "unit": "erg s^-1", "status": "computed"},
            {"name": "thin_source_B13_mu_plus_per_gX2", "value": source_total["B13_mu_plus"], "unit": "erg s^-1", "status": "computed"},
            {"name": "thin_source_B13_mu_pm_per_gX2", "value": source_total["B13_mu_pm"], "unit": "erg s^-1", "status": "computed"},
            {"name": "thin_source_B7_plus_B13_per_gX2", "value": source_total["B7_plus_B13"], "unit": "erg s^-1", "status": "computed"},
            {"name": "thin_source_B13_mu_pm_over_Croon_Eq47", "value": source_ratios["B13_mu_pm_over_Croon_Eq47"], "unit": "1", "status": "computed"},
            {"name": "radial_grid_maximum_change_metric", "value": radial_max, "unit": "1", "status": "computed"},
            {"name": "radial_Rnu_max_pointwise_relative_change", "value": radial_rnu, "unit": "1", "status": "computed"},
            {"name": "radial_100km_max_pointwise_relative_change", "value": radial_100, "unit": "1", "status": "computed"},
            {"name": "B7_source_relative_difference_vs_C1_same_grid", "value": b7_diff, "unit": "1", "status": "computed"},
            {"name": "maximum_B7_detailed_balance_residual", "value": db7, "unit": "1", "status": "computed"},
            {"name": "maximum_B13_charge_mode_detailed_balance_residual", "value": db13, "unit": "1", "status": "computed"},
            {"name": "maximum_final_muon_shell_relative_error", "value": shell, "unit": "1", "status": "computed"},
            {"name": "maximum_QUADPACK_relative_error_estimate", "value": qmax, "unit": "1", "status": "computed"},
            {"name": "maximum_three_mode_sum_relative_residual", "value": closure, "unit": "1", "status": "computed"},
            {"name": "Rnu_high_coupling_surface_asymptote", "value": surface, "unit": "erg s^-1", "status": "computed"},
            {"name": "Rnu_adaptive_luminosity_peak", "value": peak_rnu["Rfar_Rnu_adaptive_quad"], "unit": "erg s^-1", "status": "computed", "dimensions": {"g_X_at_peak": peak_rnu["g_X"]}},
            {"name": "R100km_vacuum_nu_tail_luminosity_peak", "value": peak_100["Rfar_100km_vacuum_nu_tail_adaptive_quad"], "unit": "erg s^-1", "status": "computed", "dimensions": {"g_X_at_peak": peak_100["g_X"]}},
            {"name": "energy_order_32_48_maximum_relative_change", "value": energy_max, "unit": "1", "status": "computed" if energy_available else "not_computed"},
        ],
        "data_files": [],
        "scientific_status": "provisional",
        "interpretation": (
            "A0 10 MeV radial convergence is accepted at 103/153 nodes. "
            + ("The 32/48 energy-order comparison is also accepted. " if energy_available else "The 32/48 energy-order comparison remains not_run. ")
            + "Outer 25-100 km B.13 semi-Compton opacity is omitted; this is not a final SN1987A exclusion curve."
        ),
        "extensions": {"supernova_transport": {
            "model": fine32["model"],
            "transport": fine32["transport"],
            "outer_opacity": "B.7 two-flavour vacuum decay per mode from Rnu to 100 km; B.13 outer semi-Compton opacity omitted",
            "coupling_curve_csv": rel(root, curve_path),
            "convergence_report": rel(root, convergence_path),
        }},
    }
    summary_path = out / "result_summary.json"
    dump(summary_path, summary)

    checks = [
        ck("A0-PROFILE-INTEGRITY", "SFHo-18.8 profile integrity", "integrity",
           "passed" if profile_ok else "failed", "Compare profile SHA-256 with the hash embedded in the A0 transport outputs.",
           filehash(raw["profile"]), PROFILE_SHA, "sha256", rel(root, archived["profile"])),
        ck("A0-BASELINE-INTEGRITY", "A0 103-node baseline integrity", "integrity",
           "passed" if radial["baseline"]["sha256"] == filehash(raw["a0_103_json"]) else "failed",
           "Compare baseline JSON SHA-256 with the radial convergence report.",
           filehash(raw["a0_103_json"]), radial["baseline"]["sha256"], "sha256", rel(root, archived["a0_103_json"])),
        ck("A0-RADIAL-103-153", "A0 adaptive radial convergence", "convergence",
           "passed" if radial_max <= radial_target else "failed",
           "Compare the complete 121-point curves for both R_far boundaries and all three polarization modes.",
           radial_max, radial_target, "1", rel(root, archived["radial_report"])),
        ck("A0-RADIAL-RNU-POINTWISE", "R_far=R_nu pointwise radial convergence", "convergence",
           "passed" if radial_rnu <= 1.0e-2 else "failed",
           "Maximum pointwise relative change above 1e-8 of the reference-curve peak.",
           radial_rnu, 1.0e-2, "1", rel(root, archived["radial_report"])),
        ck("A0-RADIAL-100KM-POINTWISE", "R_far=100 km pointwise radial convergence", "convergence",
           "passed" if radial_100 <= 1.0e-2 else "failed",
           "Maximum pointwise relative change above 1e-8 of the reference-curve peak.",
           radial_100, 1.0e-2, "1", rel(root, archived["radial_report"])),
        ck("A0-B7-UNCHANGED", "B.7 neutrino source unchanged against C1", "analytic",
           "passed" if b7_diff < 1.0e-12 else "failed",
           "Compare total and per-mode B.7 thin-source coefficients on the same 153-node grid.",
           b7_diff, 1.0e-12, "1", rel(root, archived["radial_report"])),
        ck("A0-B7-DB", "B.7 mode detailed balance", "analytic", "passed" if db7 < 1.0e-10 else "failed",
           "Maximum B.7 mode detailed-balance residual.", db7, 1.0e-10, "1", rel(root, archived["a0_153_32_json"])),
        ck("A0-B13-DB", "B.13 charge/mode detailed balance", "analytic", "passed" if db13 < 1.0e-10 else "failed",
           "Maximum B.13 charge- and polarization-resolved detailed-balance residual.", db13, 1.0e-10, "1", rel(root, archived["a0_153_32_json"])),
        ck("A0-MUON-SHELL", "Final-muon on-shell closure", "analytic", "passed" if shell < 2.0e-10 else "failed",
           "Maximum final-muon mass-shell residual.", shell, 2.0e-10, "1", rel(root, archived["a0_153_32_json"])),
        ck("A0-QUADPACK", "Adaptive radial QUADPACK error estimate", "convergence", "passed" if qmax < 1.0e-6 else "failed",
           "Maximum QUADPACK relative error estimate from the radial convergence report.", qmax, 1.0e-6, "1", rel(root, archived["radial_report"])),
        ck("A0-MODE-CLOSURE", "Three-polarization sum closure", "analytic", "passed" if closure < 1.0e-12 else "failed",
           "Maximum L+T++T- mode-sum residual.", closure, 1.0e-12, "1", rel(root, archived["a0_153_32_json"])),
        ck("A0-RADIAL-CHECKSUMS", "A0 radial output checksum manifest", "integrity", "passed",
           "Verify all entries in the original radial workflow SHA-256 manifest.",
           len(radial_checksums), "all listed files match", "files", rel(root, archived["radial_sums"])),
    ]
    if energy_available:
        checks.extend([
            ck("A0-ENERGY-32-48", "A0 adaptive energy-order convergence", "convergence",
               "passed" if energy_max < energy_target else "failed",
               "Compare the full 121-point 153-node curves, thin-source integrals, surface asymptotes and mode-resolved outputs.",
               energy_max, energy_target, "1", rel(root, archived["energy_report"])),
            ck("A0-B7-ENERGY48-UNCHANGED", "B.7 source unchanged against C1 energy-48", "analytic",
               "passed" if energy["B7_unchanged_against_C1_153node_energy48"]["total_relative_difference"] < 1.0e-12 else "failed",
               "Compare B.7 total and each polarization at fixed 153 radial nodes and energy order 48.",
               energy["B7_unchanged_against_C1_153node_energy48"]["total_relative_difference"], 1.0e-12, "1",
               rel(root, archived["energy_report"])),
            ck("A0-ENERGY-CHECKSUMS", "A0 energy output checksum manifest", "integrity", "passed",
               "Verify all entries in the original energy workflow SHA-256 manifest.",
               len(energy_checksums), "all listed files match", "files", rel(root, archived["energy_sums"])),
        ])
    else:
        checks.append(
            ck("A0-ENERGY-32-48", "A0 adaptive energy-order convergence", "convergence", "not_run",
               "The independent 153-node, energy-48 output/report pair is not present in the repository snapshot.",
               None, 1.0e-4, "1", P["energy_report"])
        )
    checks.extend([
        ck("A0-OUTER-B13-OPACITY", "Outer 25-100 km B.13 semi-Compton opacity", "physical", "partial",
           "Inspect the transport scope metadata.", "omitted", "validated outer opacity included", "scope",
           rel(root, archived["a0_153_32_json"]), "No validated outer muon-susceptibility profile is included."),
        ck("A0-SN1987A-LIMIT", "Final SN1987A exclusion curve", "physical", "not_run",
           "Not evaluated by this interior-profile benchmark.", None,
           "requires full outer transport and mass scan", "scope", rel(root, archived["a0_153_32_json"])),
    ])
    vstatus = status(checks)
    validation = {
        "schema_version": "1.0.0", "record_type": "validation_report",
        "run_id": run_id, "created_at": now(), "status": vstatus, "checks": checks,
        "convergence": {
            "radial_grid": convergence["radial_grid"],
            "energy_order": convergence["energy_order"],
            "numerical_acceptance": "PASS" if energy_available else "PARTIAL",
            "overall_physical_scope": "PARTIAL",
        },
        "extensions": {"supernova_transport": {
            "radial_grid_accepted": True,
            "energy_order_32_48": "PASS" if energy_available else "not_run",
            "outer_semicompton_25_100_km": "not included",
            "final_SN1987A_exclusion": "not computed",
        }},
    }
    validation_path = out / "validation_report.json"
    dump(validation_path, validation)

    readme = out / "README.md"
    readme.write_text(
        f"# A0 10 MeV structured result archive\n\n"
        f"- Run ID: {run_id}\n"
        f"- Radial workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/{RADIAL_RUN_ID}\n"
        + (f"- Energy workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/{ENERGY_RUN_ID}\n" if energy_available else "- Energy workflow: not_run\n")
        + f"- Grid: 153 actual radial nodes, energy order {final_item['energy_points']}, 121 coupling points, L/T+/T-.\n"
        + f"- Radial convergence metric: {radial_max:.9g} (threshold {radial_target:.9g}).\n"
        + (f"- Energy convergence metric: {energy_max:.9g} (threshold {energy_target:.9g}).\n" if energy_available else "- Energy-order 32/48 convergence remains not_run.\n")
        + "- Numerical status: radial PASS; physical scope PARTIAL.\n\n"
        + "The archive contains the 103-node baseline, 153-node A0 transport, C1 same-grid B.7 reference, radial/energy convergence evidence, local production-rate profile, 121-point coupling/luminosity curve and original SHA-256 manifests. The original physics outputs are copied byte-for-byte.\n\n"
        + "Outer 25-100 km B.13 semi-Compton opacity is omitted. This is not a final SN1987A exclusion curve. The archive generator packages existing outputs only and does not rerun the physics calculation.\n",
        encoding="utf-8",
    )

    roles = [
        ("profile", "reconstructed SFHo-18.8 profile input snapshot"),
        ("a0_103_json", "103-node A0 adaptive transport baseline JSON"),
        ("a0_103_csv", "103-node A0 local production-rate CSV"),
        ("a0_153_32_json", "153-node A0 energy-32 transport JSON"),
        ("a0_153_32_csv", "153-node A0 energy-32 local production-rate CSV"),
        ("c1_153_32_json", "C1 153-node B.7 unchanged-reference JSON"),
        ("radial_report", "A0 103/153 radial convergence report"),
        ("radial_sums", "original A0 radial SHA-256 manifest"),
    ]
    if energy_available:
        roles += [
            ("a0_153_48_json", "153-node A0 energy-48 transport JSON"),
            ("a0_153_48_csv", "153-node A0 energy-48 local production-rate CSV"),
            ("c1_153_48_json", "C1 153-node energy-48 B.7 reference JSON"),
            ("energy_report", "A0 32/48 energy convergence report"),
            ("energy_sums", "original A0 energy SHA-256 manifest"),
        ]
    output_records = []
    for key, role in roles:
        target = archived[key]
        if key == "profile":
            continue  # Input snapshot is described in run_manifest.inputs.
        units = unit_profile if target.suffix.lower() == ".csv" else None
        output_records.append(record(root, rel(root, target), role, units))
    output_records.append(record(root, rel(root, curve_path), "121-point adaptive coupling/luminosity curve CSV", curve_units))
    output_records += [
        record(root, rel(root, convergence_path), "combined radial/energy convergence report"),
        record(root, rel(root, summary_path), "structured result summary"),
        record(root, rel(root, validation_path), "structured validation report"),
        record(root, rel(root, readme), "archive guide"),
    ]

    summary["data_files"] = [item for item in output_records if item["format"] in {"csv", "json"}]
    dump(summary_path, summary)

    checksum_paths = [archived["profile"]] + [
        root / item["path"] for item in output_records
    ] + [summary_path, validation_path, readme]
    sums_path = out / "SHA256SUMS.txt"
    sums_path.write_text("".join(
        f"{filehash(item)}  {item.relative_to(out).as_posix()}\n"
        for item in sorted(checksum_paths, key=lambda x: x.as_posix())
    ), encoding="utf-8")
    output_records.append(record(root, rel(root, sums_path), "combined SHA-256 archive manifest"))

    if energy_available:
        validation_workflows = {
            "radial": {"run_id": RADIAL_RUN_ID, "source_commit": RADIAL_COMMIT,
                       "started_at": RADIAL_START, "finished_at": RADIAL_END, "conclusion": "success"},
            "energy": {"run_id": ENERGY_RUN_ID, "source_commit": ENERGY_COMMIT,
                       "started_at": ENERGY_START, "finished_at": ENERGY_END, "conclusion": "success"},
        }
    else:
        validation_workflows = {
            "radial": {"run_id": RADIAL_RUN_ID, "source_commit": RADIAL_COMMIT,
                       "started_at": RADIAL_START, "finished_at": RADIAL_END, "conclusion": "success"},
            "energy": {"run_id": ENERGY_RUN_ID, "source_commit": ENERGY_COMMIT,
                       "started_at": ENERGY_START, "finished_at": None, "conclusion": "not_run"},
        }

    primary_source_hashes = energy_source_hashes if energy_available else radial_source_hashes
    source_script_sha = primary_source_hashes[primary_audit]
    inputs = [
        _input(root, archived["profile"], P["profile"], "SFHo-18.8 reconstructed 1 s profile",
               "reviewed supernova profile input", f"git:{RADIAL_COMMIT}", RADIAL_COMMIT),
        _input(root, archived["a0_103_json"], P["a0_103_json"], "A0 103-node energy-32 baseline",
               f"A0 baseline workflow #{BASELINE_RUN_ID}", f"workflow:{BASELINE_RUN_ID};git:{BASELINE_COMMIT}", BASELINE_COMMIT),
        _input(root, archived["c1_153_32_json"], P["c1_153_32_json"], "C1 153-node energy-32 B.7 reference",
               f"C1 radial workflow #44650913407", "workflow:44650913407", RADIAL_COMMIT),
    ]
    if energy_available:
        inputs += [
            _input(root, archived["a0_153_32_json"], P["a0_153_32_json"], "A0 153-node energy-32 reference",
                   f"A0 radial workflow #{RADIAL_RUN_ID}", f"workflow:{RADIAL_RUN_ID};git:{RADIAL_COMMIT}", RADIAL_COMMIT),
            _input(root, archived["c1_153_48_json"], P["c1_153_48_json"], "C1 153-node energy-48 B.7 reference",
                   "C1 accepted 153x48 energy-order benchmark", "workflow:44656225572", RADIAL_COMMIT),
        ]

    manifest = {
        "schema_version": "1.0.0", "record_type": "run_manifest",
        "run_id": run_id, "created_at": now(),
        "project": {"repository": "lm846802297-bit/axial-vector-review-response",
                    "project_id": "axial-vector-supernova-cooling", "workstream_id": "A0-10MeV"},
        "source": {
            "commit_sha": primary_commit,
            "branch": "research/croon-vector-benchmark-and-rate-corrections-20261119",
            "script_path": primary_audit,
            "script_sha256": source_script_sha,
            "workflow_path": primary_workflow,
            "workflow_run_id": primary_run,
        },
        "inputs": inputs,
        "configuration": {
            "physics": {
                "mediator_mass_MeV": 10.0, "theta_mu_R": 0.01,
                "gV_mu_over_gX": fine32["model"]["gV_mu_over_gX"],
                "gA_mu_over_gX": fine32["model"]["gA_mu_over_gX"],
                "neutrino_couplings_over_gX": fine32["model"]["neutrino_couplings_over_gX"],
                "muon_targets": ["mu_minus", "mu_plus"], "polarizations": ["L", "+", "-"],
                "channels": ["B.7", "B.13"],
            },
            "numerics": {
                "radial_points_requested": final_item["radial_points"],
                "radial_points_actual": final_item["radial_points"],
                "energy_order": final_item["energy_points"],
                "inner_orders": final_item["inner_orders"],
                "neutrino_angular_order": final_item["neutrino_angular_order"],
                "susceptibility_order": final_item["susceptibility_order"],
                "coupling_count": 121, "coupling_range_gX": [1.0e-11, 1.0],
                "adaptive_radial": True,
            },
            "conventions": {
                "volume_element": fine32["transport"]["volume_element"],
                "optical_depth": fine32["transport"]["optical_depth"],
                "outer_neutrino_opacity": fine32["transport"]["outer_neutrino_opacity"],
                "outer_semicompton_opacity": fine32["transport"]["outer_semicompton_opacity"],
                "angular_escape_average": fine32["transport"]["angular_escape_average"],
                "lapse_redshift": fine32["transport"]["lapse_redshift"],
                "R_far_values_km": fine32["transport"]["R_far_values_km"],
            },
        },
        "environment": {
            "platform": "GitHub-hosted ubuntu-latest",
            "runtime": {"python": "3.13"},
            "dependencies": {"numpy": "2.5.5", "scipy": "1.18.1"},
            "hardware": {"runner": "ubuntu-latest", "machine_model": "not recorded"},
        },
        "execution": {
            "status": "succeeded",
            "command": (
                "python audit_croon_a0_10mev_adaptive_radial_convergence.py"
                + ("; python audit_croon_a0_10mev_adaptive_energy_convergence.py" if energy_available else "")
            ),
            "started_at": RADIAL_START,
            "finished_at": ENERGY_END if energy_available else RADIAL_END,
            "exit_code": 0,
        },
        "outputs": output_records,
        "validation": {"status": vstatus, "checks": checks, "report_path": rel(root, validation_path)},
        "archive": {"status": "local_only"},
        "extensions": {
            "source_files": {"radial_commit": radial_source_hashes, "energy_commit": energy_source_hashes},
            "supernova_transport": {
                "numerical_baseline_accepted": True,
                "radial_workflow_run_id": RADIAL_RUN_ID,
                "energy_workflow_run_id": ENERGY_RUN_ID if energy_available else None,
                "outer_semicompton_25_100_km": "not included",
                "final_SN1987A_exclusion": "not computed",
                "energy_order_32_48": "PASS" if energy_available else "not_run",
            },
            "archive_generation": {
                "generator_path": f"{HERE_REL}/archive_croon_a0_10mev.py",
                "generator_sha256": filehash(Path(__file__).resolve()),
                "generated_at": now(),
                "archive_workflow_run_id": None,
            },
            "source_outputs": {
                "original_repository_paths": {
                    key: {"path": P[key], "sha256": filehash(raw[key]), "bytes": raw[key].stat().st_size}
                    for key in (
                        "a0_103_json", "a0_103_csv", "a0_153_32_json", "a0_153_32_csv",
                        "c1_153_32_json", "radial_report", "radial_sums",
                    ) + (("a0_153_48_json", "a0_153_48_csv", "c1_153_48_json", "energy_report", "energy_sums") if energy_available else ())
                },
            },
            "validation_workflows": validation_workflows,
            "source_checksum_verification": {"radial": radial_checksums, "energy": energy_checksums},
        },
    }
    manifest_path = out / "run_manifest.json"
    dump(manifest_path, manifest)
    return manifest_path

def finalize(manifest_path: Path, pr_url: str) -> None:
    manifest = load(manifest_path)
    manifest["archive"] = {"status": "committed_to_pr_branch", "pr_url": pr_url}
    manifest.setdefault("extensions", {}).setdefault("archive_generation", {})["finalized_at"] = now()
    dump(manifest_path, manifest)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "outputs" / "a0_10mev_structured_archive_2026-11-20")
    parser.add_argument("--finalize", action="store_true")
    parser.add_argument("--pr-url")
    args = parser.parse_args()
    root = args.repo_root.resolve()
    out = args.output_dir if args.output_dir.is_absolute() else root / args.output_dir
    if args.finalize:
        if not args.pr_url:
            parser.error("--finalize requires --pr-url")
        finalize(out / "run_manifest.json", args.pr_url)
        print(out / "run_manifest.json")
        return 0
    manifest_path = build(root, out)
    print(manifest_path)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
