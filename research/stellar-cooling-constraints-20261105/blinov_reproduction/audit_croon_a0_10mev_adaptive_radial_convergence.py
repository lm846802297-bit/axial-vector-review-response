#!/usr/bin/env python3
"""A0 10 MeV adaptive radial-grid convergence audit.

The accepted 103-node A0 adaptive result is compared with an independent
153-node calculation at identical energy, angular, susceptibility, and
coupling resolution. The B.7 source is also compared against C1 on the same
153-node grid to verify that the neutrino channel is unchanged.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np

from croon_a0_uv_axial_transport import DEFAULT_OUTPUT, compute_a0
from croon_c1_b13_vector_transport import DEFAULT_PROFILE

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE / "outputs"
BASELINE = OUTPUTS / "croon_a0_uv_axial_transport_10mev_2026-11-20.json"
C1_FINE = OUTPUTS / "croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_2026-11-20.json"
RESULT_STEM = "croon_a0_uv_axial_transport_10mev_153nodes_adaptive_2026-11-20"
SUMMARY = OUTPUTS / "A0_10MEV_ADAPTIVE_RADIAL_CONVERGENCE_2026-11-20.json"
MODES = ("L", "+", "-")
CURVE_LABELS = (
    "Rfar_Rnu_adaptive_quad",
    "Rfar_100km_vacuum_nu_tail_adaptive_quad",
)
TARGET = 1.0e-2


def _relative(reference, varied):
    return abs(float(varied) - float(reference)) / max(abs(float(reference)), 1.0e-300)


def _curve_change(reference, varied, key):
    a = np.asarray([row[key] for row in reference], dtype=float)
    b = np.asarray([row[key] for row in varied], dtype=float)
    peak = max(float(np.max(np.abs(a))), 1.0e-300)
    relevant = np.abs(a) > 1.0e-8 * peak
    return {
        "max_absolute_difference_over_reference_peak": float(np.max(np.abs(b-a))/peak),
        "max_pointwise_relative_difference_above_1e-8_peak": (
            float(np.max(np.abs(b[relevant]-a[relevant])/np.abs(a[relevant])))
            if np.any(relevant) else 0.0
        ),
        "at_g_X_max_absolute_difference": float(reference[int(np.argmax(np.abs(b-a))) ]["g_X"]),
    }


def _mode_change(reference, varied, total_key, mode):
    key = total_key + "_by_mode_erg_s"
    a = np.asarray([row[key][mode] for row in reference], dtype=float)
    b = np.asarray([row[key][mode] for row in varied], dtype=float)
    peak = max(float(np.max(np.abs(a))), 1.0e-300)
    relevant = np.abs(a) > 1.0e-8 * peak
    return {
        "max_absolute_difference_over_reference_peak": float(np.max(np.abs(b-a))/peak),
        "max_pointwise_relative_difference_above_1e-8_peak": (
            float(np.max(np.abs(b[relevant]-a[relevant])/np.abs(a[relevant])))
            if np.any(relevant) else 0.0
        ),
        "at_g_X_max_absolute_difference": float(reference[int(np.argmax(np.abs(b-a))) ]["g_X"]),
    }


def main():
    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    c1 = json.loads(C1_FINE.read_text(encoding="utf-8"))
    base_item = base["masses"]["10"]
    base_curve = base_item["coupling_curve"]
    if base_item["radial_points"] != 103 or base_item["energy_points"] != 32:
        raise ValueError("A0 baseline must be the 103-node, energy-32 result")
    if not base_item["adaptive_radial_enabled"]:
        raise ValueError("A0 baseline must use adaptive radial integration")
    c1_item = c1["masses"]["10"]
    if c1_item["radial_points"] != 153 or c1_item["energy_points"] != 32:
        raise ValueError("C1 comparison must be the 153-node, energy-32 result")

    payload = compute_a0(
        profile_path=DEFAULT_PROFILE,
        masses=(10.0,),
        radial_points=151,
        energy_order=32,
        inner_orders=(12, 8, 8, 8),
        neutrino_order=128,
        susceptibility_order=192,
        coupling_count=121,
        theta_mu_r=1.0e-2,
        include_adaptive_radial=True,
    )
    item = payload["masses"]["10"]
    curve = item["coupling_curve"]
    if item["radial_points"] != 153 or item["energy_points"] != 32:
        raise ValueError("Unexpected A0 refined grid")
    if not item["adaptive_radial_enabled"]:
        raise ValueError("Refined A0 result did not use adaptive radial integration")
    if len(curve) != len(base_curve) or any(
        a["g_X"] != b["g_X"] for a, b in zip(base_curve, curve)
    ):
        raise ValueError("A0 coupling grids do not match")

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    json_path = OUTPUTS / f"{RESULT_STEM}.json"
    csv_path = OUTPUTS / f"{RESULT_STEM}.csv"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        rows = payload["local_profile_rows"]
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    total_changes = {
        key: _curve_change(base_curve, curve, key) for key in CURVE_LABELS
    }
    mode_changes = {
        key: {
            mode: _mode_change(base_curve, curve, key, mode) for mode in MODES
        }
        for key in CURVE_LABELS
    }
    source_total_changes = {
        channel: _relative(
            base_item["thin_source_per_g2_erg_s"][channel],
            item["thin_source_per_g2_erg_s"][channel],
        )
        for channel in base_item["thin_source_per_g2_erg_s"]
    }
    source_mode_changes = {
        channel: {
            mode: _relative(
                base_item["thin_source_by_mode_per_g2_erg_s"][channel][mode],
                item["thin_source_by_mode_per_g2_erg_s"][channel][mode],
            )
            for mode in MODES
        }
        for channel in base_item["thin_source_by_mode_per_g2_erg_s"]
    }

    b7_total = _relative(
        c1_item["thin_source_per_g2_erg_s"]["B7_nu_mu_plus_nu_tau"],
        item["thin_source_per_g2_erg_s"]["B7_nu_mu_plus_nu_tau"],
    )
    b7_modes = {
        mode: _relative(
            c1_item["thin_source_by_mode_per_g2_erg_s"]["B7_nu_mu_plus_nu_tau"][mode],
            item["thin_source_by_mode_per_g2_erg_s"]["B7_nu_mu_plus_nu_tau"][mode],
        )
        for mode in MODES
    }

    surface = item["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"]
    high = curve[-1]["Rfar_Rnu_adaptive_quad_by_mode_erg_s"]
    surface_residuals = {
        mode: _relative(surface[mode], high[mode]) for mode in MODES
    }

    metrics = []
    for change in total_changes.values():
        metrics.extend([
            change["max_absolute_difference_over_reference_peak"],
            change["max_pointwise_relative_difference_above_1e-8_peak"],
        ])
    for label in mode_changes.values():
        for change in label.values():
            metrics.extend([
                change["max_absolute_difference_over_reference_peak"],
                change["max_pointwise_relative_difference_above_1e-8_peak"],
            ])
    metrics.extend(source_total_changes.values())
    metrics.extend(value for channel in source_mode_changes.values() for value in channel.values())
    max_radial_metric = max(metrics)

    max_quad_error = 0.0
    max_mode_closure = 0.0
    for row in curve:
        for label in ("Rfar_Rnu", "Rfar_100km_vacuum_nu_tail"):
            total_key = label + "_adaptive_quad"
            modes_key = total_key + "_by_mode_erg_s"
            error_key = total_key + "_relative_error_estimate"
            mode_error_key = total_key + "_relative_error_estimate_by_mode"
            total = float(row[total_key])
            modes = row[modes_key]
            if not np.isfinite(total) or total < 0.0:
                raise ValueError((total_key, total))
            closure = abs(sum(modes.values())-total)/max(abs(total),1.0e-300)
            max_mode_closure = max(max_mode_closure, closure)
            if closure >= 1.0e-12:
                raise ValueError((modes_key, closure))
            max_quad_error = max(
                max_quad_error,
                float(row[error_key]),
                *[float(v) for v in row[mode_error_key].values()],
            )

    status = (
        "PASS"
        if max_radial_metric < TARGET
        and b7_total < 1.0e-12
        and max(b7_modes.values()) < 1.0e-12
        and max_quad_error < 1.0e-6
        and max_mode_closure < 1.0e-12
        and max(surface_residuals.values()) < 1.0e-6
        else "REFINE"
    )
    report = {
        "title": "A0 10 MeV adaptive radial-grid convergence",
        "status": status,
        "baseline": {
            "path": str(BASELINE.relative_to(HERE)),
            "sha256": hashlib.sha256(BASELINE.read_bytes()).hexdigest(),
            "radial_points": base_item["radial_points"],
            "energy_order": base_item["energy_points"],
        },
        "refined": {
            "json_path": str(json_path.relative_to(HERE)),
            "csv_path": str(csv_path.relative_to(HERE)),
            "sha256_json": hashlib.sha256(json_path.read_bytes()).hexdigest(),
            "sha256_csv": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
            "radial_points": item["radial_points"],
            "energy_order": item["energy_points"],
        },
        "fixed_parameters": {
            "profile_sha256": payload["source_profile"]["sha256"],
            "theta_mu_R": payload["model"]["theta_mu_R"],
            "gV_mu_over_gX": payload["model"]["gV_mu_over_gX"],
            "gA_mu_over_gX": payload["model"]["gA_mu_over_gX"],
            "neutrino_couplings_over_gX": payload["model"]["neutrino_couplings_over_gX"],
            "neutrino_angular_order": payload["numerics"]["neutrino_angular_order"],
            "susceptibility_order": payload["numerics"]["susceptibility_order"],
            "inner_orders": payload["numerics"]["inner_orders"],
            "coupling_count": payload["numerics"]["coupling_count"],
            "adaptive_radial": payload["numerics"]["adaptive_radial_enabled"],
        },
        "target": TARGET,
        "maximum_radial_change_metric": max_radial_metric,
        "total_curve_changes": total_changes,
        "mode_curve_changes": mode_changes,
        "thin_source_total_relative_changes": source_total_changes,
        "thin_source_mode_relative_changes": source_mode_changes,
        "B7_unchanged_against_C1_153node": {
            "total_relative_difference": b7_total,
            "per_mode_relative_differences": b7_modes,
        },
        "surface_asymptote_high_g_relative_residuals": surface_residuals,
        "max_quadpack_relative_error_estimate": max_quad_error,
        "max_mode_sum_relative_residual": max_mode_closure,
        "detailed_balance": {
            "max_B7_mode_residual": item["maximum_B7_mode_detailed_balance_residual"],
            "max_B13_charge_mode_residual": item["maximum_B13_charge_mode_detailed_balance_residual"],
            "max_final_muon_shell_relative_error": item["maximum_final_muon_shell_relative_error"],
        },
        "scope": (
            "A0 10 MeV adaptive radial convergence on the reconstructed "
            "SFHo-18.8 interior profile. Outer 25--100 km semi-Compton opacity "
            "is omitted; this is not an SN1987A exclusion curve."
        ),
    }
    SUMMARY.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
