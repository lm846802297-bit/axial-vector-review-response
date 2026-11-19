#!/usr/bin/env python3
"""C1 10 MeV radial, energy, and B.7 angular convergence audit.

The archived mode-resolved 101 x 32 C1 result is the reference. This script
computes independent radial, energy, combined-grid, and neutrino-angular
refinements, retaining all three polarizations and their closure diagnostics.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np

from croon_c1_b13_vector_transport import (
    DEFAULT_PROFILE,
    compute_c1,
)

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE / "outputs"
BASELINE = OUTPUTS / "croon_c1_b13_vector_transport_10mev_mode_resolved_2026-11-20.json"
SUMMARY = OUTPUTS / "croon_c1_10mev_grid_convergence_summary_2026-11-20.json"
MODES = ("L", "+", "-")
CURVE_LABELS = ("Rfar_Rnu", "Rfar_100km_vacuum_nu_tail")
TARGET_RELATIVE = 1.0e-2

CONFIGS = (
    {
        "name": "radial151_energy32",
        "radial_points": 151,
        "energy_order": 32,
        "neutrino_order": 128,
    },
    {
        "name": "radial101_energy48",
        "radial_points": 101,
        "energy_order": 48,
        "neutrino_order": 128,
    },
    {
        "name": "radial151_energy48",
        "radial_points": 151,
        "energy_order": 48,
        "neutrino_order": 128,
    },
    {
        "name": "radial101_energy32_nu192",
        "radial_points": 101,
        "energy_order": 32,
        "neutrino_order": 192,
    },
)


def _max_relative_curve_change(reference, varied, label):
    ref = np.asarray([row[label] for row in reference], float)
    val = np.asarray([row[label] for row in varied], float)
    scale = max(float(np.max(np.abs(ref))), 1.0e-300)
    return float(np.max(np.abs(val - ref)) / scale)


def _mode_curve_change(reference, varied, label, mode):
    key = label + "_by_mode_erg_s"
    ref = np.asarray([row[key][mode] for row in reference], float)
    val = np.asarray([row[key][mode] for row in varied], float)
    scale = max(float(np.max(np.abs(ref))), 1.0e-300)
    return float(np.max(np.abs(val - ref)) / scale)


def _thin_source_changes(reference, varied):
    totals = {}
    modes = {}
    for channel, ref_value in reference["thin_source_per_g2_erg_s"].items():
        value = varied["thin_source_per_g2_erg_s"][channel]
        totals[channel] = abs(value - ref_value) / max(abs(ref_value), 1.0e-300)
    for channel, ref_modes in reference["thin_source_by_mode_per_g2_erg_s"].items():
        modes[channel] = {}
        for mode in MODES:
            ref_value = ref_modes[mode]
            value = varied["thin_source_by_mode_per_g2_erg_s"][channel][mode]
            modes[channel][mode] = abs(value - ref_value) / max(abs(ref_value), 1.0e-300)
    return totals, modes


def _write_result(payload, stem):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    json_path = OUTPUTS / f"{stem}.json"
    csv_path = OUTPUTS / f"{stem}.csv"
    rows = payload["local_profile_rows"]
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
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
    results = []

    for config in CONFIGS:
        payload = compute_c1(
            profile_path=DEFAULT_PROFILE,
            masses=(10.0,),
            radial_points=config["radial_points"],
            energy_order=config["energy_order"],
            inner_orders=(12, 8, 8, 8),
            neutrino_order=config["neutrino_order"],
            susceptibility_order=192,
            coupling_count=121,
        )
        item = payload["masses"]["10"]
        stem = "croon_c1_10mev_grid_" + config["name"] + "_2026-11-20"
        json_path, csv_path = _write_result(payload, stem)

        total_curve_changes = {
            label: _max_relative_curve_change(
                base_curve, item["coupling_curve"], label
            )
            for label in CURVE_LABELS
        }
        mode_curve_changes = {
            label: {
                mode: _mode_curve_change(
                    base_curve, item["coupling_curve"], label, mode
                )
                for mode in MODES
            }
            for label in CURVE_LABELS
        }
        thin_total_changes, thin_mode_changes = _thin_source_changes(
            base_item, item
        )
        maximum_shape_change = max(
            list(total_curve_changes.values())
            + [
                value
                for channel in mode_curve_changes.values()
                for value in channel.values()
            ]
        )
        maximum_thin_source_change = max(
            list(thin_total_changes.values())
            + [
                value
                for channel in thin_mode_changes.values()
                for value in channel.values()
            ]
        )
        maximum_change = max(maximum_shape_change, maximum_thin_source_change)
        results.append({
            "configuration": config,
            "actual_radial_points": item["radial_points"],
            "energy_points": item["energy_points"],
            "polarization_modes": item["polarization_modes"],
            "max_B7_detailed_balance_residual": item[
                "maximum_B7_mode_detailed_balance_residual"
            ],
            "max_B13_detailed_balance_residual": item[
                "maximum_B13_charge_mode_detailed_balance_residual"
            ],
            "max_final_muon_shell_relative_error": item[
                "maximum_final_muon_shell_relative_error"
            ],
            "total_curve_max_normalized_changes": total_curve_changes,
            "mode_curve_max_normalized_changes": mode_curve_changes,
            "thin_source_total_relative_changes": thin_total_changes,
            "thin_source_mode_relative_changes": thin_mode_changes,
            "maximum_curve_or_source_change": maximum_change,
            "target_relative": TARGET_RELATIVE,
            "status": "PASS" if maximum_change < TARGET_RELATIVE else "REFINE",
            "json_path": str(json_path.relative_to(HERE)),
            "csv_path": str(csv_path.relative_to(HERE)),
            "json_sha256": hashlib.sha256(json_path.read_bytes()).hexdigest(),
            "csv_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        })

    summary = {
        "title": "C1 10 MeV radial-energy-angular convergence audit",
        "baseline": {
            "path": str(BASELINE.relative_to(HERE)),
            "sha256": hashlib.sha256(BASELINE.read_bytes()).hexdigest(),
            "radial_points": base_item["radial_points"],
            "energy_points": base_item["energy_points"],
            "inner_orders": base_item["inner_orders"],
            "neutrino_angular_order": base_item["neutrino_angular_order"],
            "susceptibility_order": baseline["numerics"]["susceptibility_order"],
            "coupling_points": len(base_curve),
        },
        "comparison_definition": (
            "Maximum absolute curve difference normalized to the reference "
            "curve's peak, separately for total and each polarization; thin "
            "source relative changes are checked channel by channel."
        ),
        "acceptance_target": TARGET_RELATIVE,
        "configurations": results,
        "overall_status": (
            "PASS" if all(item["status"] == "PASS" for item in results)
            else "REFINE"
        ),
        "scope": (
            "This is a C1 interior-profile grid-convergence audit. It does not "
            "add the unavailable outer 25--100 km semi-Compton opacity."
        ),
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
