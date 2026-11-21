#!/usr/bin/env python3
"""Adaptive-radial C1 10 MeV energy-order convergence audit.

The accepted 153-node, energy-order-32 adaptive result is the reference.
This audit recomputes the identical radial/coupling/polarization setup at
energy order 48 and compares the full luminosity curves and source integrals.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np

from croon_c1_b13_vector_transport import DEFAULT_PROFILE, compute_c1

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE / "outputs"
BASELINE = OUTPUTS / (
    "croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_2026-11-20.json"
)
RESULT_STEM = "croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_energy48_2026-11-20"
SUMMARY = OUTPUTS / "C1_RNU_10MEV_ADAPTIVE_ENERGY_CONVERGENCE_2026-11-20.json"
MODES = ("L", "+", "-")
CURVE_LABELS = (
    "Rfar_Rnu_adaptive_quad",
    "Rfar_100km_vacuum_nu_tail_adaptive_quad",
)
TARGET_NORMALIZED = 1.0e-4


def _relative_change(reference: float, varied: float) -> float:
    return abs(varied - reference) / max(abs(reference), 1.0e-300)


def _max_curve_changes(reference, varied, key):
    ref = np.asarray([row[key] for row in reference], dtype=float)
    val = np.asarray([row[key] for row in varied], dtype=float)
    peak = max(float(np.max(np.abs(ref))), 1.0e-300)
    absolute_normalized = float(np.max(np.abs(val - ref)) / peak)
    relevant = np.abs(ref) > 1.0e-8 * peak
    pointwise_relative = (
        float(np.max(np.abs(val[relevant] - ref[relevant]) / np.abs(ref[relevant])))
        if np.any(relevant) else 0.0
    )
    index = int(np.argmax(np.abs(val - ref)))
    return {
        "max_absolute_difference_over_reference_peak": absolute_normalized,
        "max_pointwise_relative_difference_above_1e-8_peak": pointwise_relative,
        "at_g_X_max_absolute_difference": float(reference[index]["g_X"]),
    }


def _mode_changes(reference, varied, total_key, mode):
    key = total_key + "_by_mode_erg_s"
    ref = np.asarray([row[key][mode] for row in reference], dtype=float)
    val = np.asarray([row[key][mode] for row in varied], dtype=float)
    peak = max(float(np.max(np.abs(ref))), 1.0e-300)
    absolute_normalized = float(np.max(np.abs(val - ref)) / peak)
    relevant = np.abs(ref) > 1.0e-8 * peak
    pointwise_relative = (
        float(np.max(np.abs(val[relevant] - ref[relevant]) / np.abs(ref[relevant])))
        if np.any(relevant) else 0.0
    )
    index = int(np.argmax(np.abs(val - ref)))
    return {
        "max_absolute_difference_over_reference_peak": absolute_normalized,
        "max_pointwise_relative_difference_above_1e-8_peak": pointwise_relative,
        "at_g_X_max_absolute_difference": float(reference[index]["g_X"]),
    }


def _write_payload(payload):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    json_path = OUTPUTS / f"{RESULT_STEM}.json"
    csv_path = OUTPUTS / f"{RESULT_STEM}.csv"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    rows = payload["local_profile_rows"]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)
    return json_path, csv_path


def main():
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    base_item = baseline["masses"]["10"]
    base_curve = base_item["coupling_curve"]
    if base_item["radial_points"] != 153 or base_item["energy_points"] != 32:
        raise ValueError("The archived adaptive reference is not 153 nodes x energy 32")
    if not baseline["numerics"]["adaptive_radial_enabled"]:
        raise ValueError("The reference must use the surface-centered adaptive integral")

    payload = compute_c1(
        profile_path=DEFAULT_PROFILE,
        masses=(10.0,),
        radial_points=151,
        energy_order=48,
        inner_orders=(12, 8, 8, 8),
        neutrino_order=128,
        susceptibility_order=192,
        coupling_count=121,
        include_adaptive_radial=True,
    )
    item = payload["masses"]["10"]
    curve = item["coupling_curve"]
    if item["radial_points"] != 153 or item["energy_points"] != 48:
        raise ValueError("Unexpected actual radial or energy grid")
    if item["polarization_modes"] != ["L", "+", "-"]:
        raise ValueError("Unexpected polarization basis")
    if len(curve) != len(base_curve) or any(
        a["g_X"] != b["g_X"] for a, b in zip(base_curve, curve)
    ):
        raise ValueError("The coupling grids do not match")

    json_path, csv_path = _write_payload(payload)

    total_changes = {
        key: _max_curve_changes(base_curve, curve, key)
        for key in CURVE_LABELS
    }
    mode_changes = {
        key: {
            mode: _mode_changes(base_curve, curve, key, mode)
            for mode in MODES
        }
        for key in CURVE_LABELS
    }

    source_total_changes = {}
    for channel, reference in base_item["thin_source_per_g2_erg_s"].items():
        value = item["thin_source_per_g2_erg_s"][channel]
        source_total_changes[channel] = _relative_change(reference, value)
    source_mode_changes = {}
    for channel, reference_modes in base_item["thin_source_by_mode_per_g2_erg_s"].items():
        source_mode_changes[channel] = {
            mode: _relative_change(
                reference_modes[mode],
                item["thin_source_by_mode_per_g2_erg_s"][channel][mode],
            )
            for mode in MODES
        }

    surface32 = base_item["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"]
    surface48 = item["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"]
    surface_changes = {
        mode: _relative_change(surface32[mode], surface48[mode])
        for mode in MODES
    }

    all_metrics = []
    for values in total_changes.values():
        all_metrics.extend([
            values["max_absolute_difference_over_reference_peak"],
            values["max_pointwise_relative_difference_above_1e-8_peak"],
        ])
    for label in mode_changes.values():
        for values in label.values():
            all_metrics.extend([
                values["max_absolute_difference_over_reference_peak"],
                values["max_pointwise_relative_difference_above_1e-8_peak"],
            ])
    all_metrics.extend(source_total_changes.values())
    all_metrics.extend(
        value for channel in source_mode_changes.values()
        for value in channel.values()
    )
    all_metrics.extend(surface_changes.values())
    maximum_metric = max(all_metrics)

    max_quad_error = 0.0
    max_mode_closure = 0.0
    for row in curve:
        for key in (
            "Rfar_Rnu_adaptive_quad",
            "Rfar_100km_vacuum_nu_tail_adaptive_quad",
            "Rfar_Rnu_adaptive_quad_relative_error_estimate",
            "Rfar_100km_vacuum_nu_tail_adaptive_quad_relative_error_estimate",
        ):
            value = float(row[key])
            if not np.isfinite(value) or value < 0.0:
                raise ValueError((key, value))
        for label in ("Rfar_Rnu", "Rfar_100km_vacuum_nu_tail"):
            total_key = label + "_adaptive_quad"
            modes_key = total_key + "_by_mode_erg_s"
            errors_key = total_key + "_relative_error_estimate_by_mode"
            modes = row[modes_key]
            if set(modes) != set(MODES):
                raise ValueError((modes_key, modes))
            closure = abs(sum(modes.values()) - row[total_key]) / max(
                abs(row[total_key]), 1.0e-300
            )
            max_mode_closure = max(max_mode_closure, closure)
            if closure >= 1.0e-12:
                raise ValueError((modes_key, closure))
            if max(row[errors_key].values()) >= 1.0e-6:
                raise ValueError((errors_key, row[errors_key]))
        max_quad_error = max(
            max_quad_error,
            row["Rfar_Rnu_adaptive_quad_relative_error_estimate"],
            row["Rfar_100km_vacuum_nu_tail_adaptive_quad_relative_error_estimate"],
            *row["Rfar_Rnu_adaptive_quad_relative_error_estimate_by_mode"].values(),
            *row["Rfar_100km_vacuum_nu_tail_adaptive_quad_relative_error_estimate_by_mode"].values(),
        )

    report = {
        "title": "C1 10 MeV adaptive radial energy-order convergence",
        "status": "PASS" if maximum_metric < TARGET_NORMALIZED else "REFINE",
        "reference": {
            "path": str(BASELINE.relative_to(HERE)),
            "radial_points": base_item["radial_points"],
            "energy_order": base_item["energy_points"],
            "sha256": hashlib.sha256(BASELINE.read_bytes()).hexdigest(),
        },
        "refined": {
            "json_path": str(json_path.relative_to(HERE)),
            "csv_path": str(csv_path.relative_to(HERE)),
            "radial_points": item["radial_points"],
            "energy_order": item["energy_points"],
            "sha256_json": hashlib.sha256(json_path.read_bytes()).hexdigest(),
            "sha256_csv": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        },
        "fixed_parameters": {
            "profile_sha256": payload["source_profile"]["sha256"],
            "neutrino_angular_order": payload["numerics"]["neutrino_angular_order"],
            "susceptibility_order": payload["numerics"]["susceptibility_order"],
            "inner_orders": payload["numerics"]["inner_orders"],
            "coupling_count": payload["numerics"]["coupling_count"],
            "coupling_range": payload["numerics"]["coupling_range"],
            "polarizations": item["polarization_modes"],
            "adaptive_radial": payload["numerics"]["adaptive_radial_enabled"],
        },
        "comparison_definition": (
            "Full 121-point curves are compared pointwise. Both the maximum "
            "absolute difference divided by the reference curve peak and the "
            "maximum pointwise relative difference where the reference exceeds "
            "1e-8 of its peak are reported. Thin-source channel/mode integrals "
            "and surface asymptotes are compared separately."
        ),
        "target": TARGET_NORMALIZED,
        "maximum_over_all_reported_metrics": maximum_metric,
        "total_curve_changes": total_changes,
        "mode_curve_changes": mode_changes,
        "thin_source_total_relative_changes": source_total_changes,
        "thin_source_mode_relative_changes": source_mode_changes,
        "surface_asymptote_mode_relative_changes": surface_changes,
        "max_quadpack_relative_error_estimate": max_quad_error,
        "max_mode_sum_relative_residual": max_mode_closure,
        "detailed_balance": {
            "max_B7_mode_residual": item["maximum_B7_mode_detailed_balance_residual"],
            "max_B13_charge_mode_residual": item["maximum_B13_charge_mode_detailed_balance_residual"],
            "max_final_muon_shell_relative_error": item["maximum_final_muon_shell_relative_error"],
        },
        "scope": (
            "10 MeV C1 interior-profile energy convergence for the adaptive "
            "radial integral. It does not add the unavailable outer 25--100 km "
            "semi-Compton opacity and is not an SN1987A exclusion curve."
        ),
    }
    SUMMARY.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
