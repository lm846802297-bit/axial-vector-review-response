#!/usr/bin/env python3
"""A0 10 MeV adaptive-radial energy-order convergence audit.

Compare the accepted 153-node, energy-order-32 A0 result with an independent
153-node, energy-order-48 calculation. The actual UV V-A current, charge-
resolved muon targets, B.7 neutrino channel, and all three physical modes are
kept unchanged. C1 energy-48 is used only to verify that A0's B.7 channel is
identical to the pure-vector neutrino reference.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np

from croon_a0_uv_axial_transport import DEFAULT_PROFILE, compute_a0

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE / "outputs"
BASELINE = OUTPUTS / (
    "croon_a0_uv_axial_transport_10mev_153nodes_adaptive_2026-11-20.json"
)
C1_FINE = OUTPUTS / (
    "croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_energy48_2026-11-20.json"
)
RESULT_STEM = (
    "croon_a0_uv_axial_transport_10mev_153nodes_adaptive_energy48_2026-11-20"
)
SUMMARY = OUTPUTS / "A0_10MEV_ADAPTIVE_ENERGY_CONVERGENCE_2026-11-20.json"
MODES = ("L", "+", "-")
CURVE_LABELS = (
    "Rfar_Rnu_adaptive_quad",
    "Rfar_100km_vacuum_nu_tail_adaptive_quad",
)
TARGET_NORMALIZED = 1.0e-4


def _relative_change(reference: float, varied: float) -> float:
    reference = float(reference)
    varied = float(varied)
    if not np.isfinite(reference) or not np.isfinite(varied):
        raise ValueError(("non-finite comparison input", reference, varied))
    return abs(varied - reference) / max(abs(reference), 1.0e-300)


def _curve_change(reference, varied, key):
    ref = np.asarray([row[key] for row in reference], dtype=float)
    val = np.asarray([row[key] for row in varied], dtype=float)
    if not np.all(np.isfinite(ref)) or not np.all(np.isfinite(val)):
        raise ValueError((key, "non-finite luminosity curve"))
    if not np.all(np.isfinite(ref)) or not np.all(np.isfinite(val)):
        raise ValueError((key, mode, "non-finite mode-resolved luminosity curve"))
    peak = max(float(np.max(np.abs(ref))), 1.0e-300)
    relevant = np.abs(ref) > 1.0e-8 * peak
    index = int(np.argmax(np.abs(val - ref)))
    return {
        "max_absolute_difference_over_reference_peak": float(
            np.max(np.abs(val - ref)) / peak
        ),
        "max_pointwise_relative_difference_above_1e-8_peak": (
            float(np.max(np.abs(val[relevant] - ref[relevant]) / np.abs(ref[relevant])))
            if np.any(relevant) else 0.0
        ),
        "at_g_X_max_absolute_difference": float(reference[index]["g_X"]),
    }


def _mode_change(reference, varied, total_key, mode):
    key = total_key + "_by_mode_erg_s"
    ref = np.asarray([row[key][mode] for row in reference], dtype=float)
    val = np.asarray([row[key][mode] for row in varied], dtype=float)
    peak = max(float(np.max(np.abs(ref))), 1.0e-300)
    relevant = np.abs(ref) > 1.0e-8 * peak
    index = int(np.argmax(np.abs(val - ref)))
    return {
        "max_absolute_difference_over_reference_peak": float(
            np.max(np.abs(val - ref)) / peak
        ),
        "max_pointwise_relative_difference_above_1e-8_peak": (
            float(np.max(np.abs(val[relevant] - ref[relevant]) / np.abs(ref[relevant])))
            if np.any(relevant) else 0.0
        ),
        "at_g_X_max_absolute_difference": float(reference[index]["g_X"]),
    }


def _write_payload(payload):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    json_path = OUTPUTS / f"{RESULT_STEM}.json"
    csv_path = OUTPUTS / f"{RESULT_STEM}.csv"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    rows = payload["local_profile_rows"]
    if not rows:
        raise ValueError("A0 energy-48 calculation returned no local-profile rows")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)
    return json_path, csv_path


def main():
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    c1_fine = json.loads(C1_FINE.read_text(encoding="utf-8"))
    base_item = baseline["masses"]["10"]
    base_curve = base_item["coupling_curve"]
    if base_item["radial_points"] != 153 or base_item["energy_points"] != 32:
        raise ValueError("A0 reference must be the accepted 153-node, energy-32 result")
    if not base_item["adaptive_radial_enabled"]:
        raise ValueError("A0 energy reference must use adaptive radial integration")

    c1_item = c1_fine["masses"]["10"]
    if c1_item["radial_points"] != 153 or c1_item["energy_points"] != 48:
        raise ValueError("C1 cross-check must be the 153-node, energy-48 result")

    payload = compute_a0(
        profile_path=DEFAULT_PROFILE,
        masses=(10.0,),
        radial_points=151,
        energy_order=48,
        inner_orders=(12, 8, 8, 8),
        neutrino_order=128,
        susceptibility_order=192,
        coupling_count=121,
        theta_mu_r=1.0e-2,
        include_adaptive_radial=True,
    )
    item = payload["masses"]["10"]
    curve = item["coupling_curve"]
    if item["radial_points"] != 153 or item["energy_points"] != 48:
        raise ValueError("Unexpected A0 refined radial or energy grid")
    if item["polarization_modes"] != list(MODES):
        raise ValueError("Unexpected A0 polarization basis")
    if len(curve) != len(base_curve) or any(
        a["g_X"] != b["g_X"] for a, b in zip(base_curve, curve)
    ):
        raise ValueError("A0 coupling grids do not match")

    json_path, csv_path = _write_payload(payload)

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
        channel: _relative_change(
            reference, item["thin_source_per_g2_erg_s"][channel]
        )
        for channel, reference in base_item["thin_source_per_g2_erg_s"].items()
    }
    source_mode_changes = {
        channel: {
            mode: _relative_change(
                reference_modes[mode],
                item["thin_source_by_mode_per_g2_erg_s"][channel][mode],
            )
            for mode in MODES
        }
        for channel, reference_modes in
        base_item["thin_source_by_mode_per_g2_erg_s"].items()
    }

    surface32 = base_item["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"]
    surface48 = item["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"]
    surface_changes = {
        mode: _relative_change(surface32[mode], surface48[mode]) for mode in MODES
    }

    # B.7 is independent of the charged-muon current. It must match the
    # same-grid C1 energy-48 neutrino source, including each polarization.
    b7_total = _relative_change(
        c1_item["thin_source_per_g2_erg_s"]["B7_nu_mu_plus_nu_tau"],
        item["thin_source_per_g2_erg_s"]["B7_nu_mu_plus_nu_tau"],
    )
    b7_modes = {
        mode: _relative_change(
            c1_item["thin_source_by_mode_per_g2_erg_s"]["B7_nu_mu_plus_nu_tau"][mode],
            item["thin_source_by_mode_per_g2_erg_s"]["B7_nu_mu_plus_nu_tau"][mode],
        )
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
    if not all(np.isfinite(value) for value in all_metrics):
        raise ValueError(("non-finite convergence metric", all_metrics))
    maximum_metric = max(all_metrics)

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
            if set(modes) != set(MODES):
                raise ValueError((modes_key, modes))
            if any(not np.isfinite(float(v)) or float(v) < 0.0 for v in modes.values()):
                raise ValueError((modes_key, modes))
            closure = abs(sum(modes.values()) - total) / max(abs(total), 1.0e-300)
            max_mode_closure = max(max_mode_closure, closure)
            if closure >= 1.0e-12:
                raise ValueError((modes_key, closure))
            quad_error = float(row[error_key])
            mode_errors = [float(v) for v in row[mode_error_key].values()]
            if (
                not np.isfinite(quad_error) or quad_error < 0.0
                or any(not np.isfinite(v) or v < 0.0 for v in mode_errors)
            ):
                raise ValueError((error_key, quad_error, mode_errors))
            max_quad_error = max(max_quad_error, quad_error, *mode_errors)

    high = curve[-1]["Rfar_Rnu_adaptive_quad_by_mode_erg_s"]
    surface_residuals = {
        mode: _relative_change(surface48[mode], high[mode]) for mode in MODES
    }

    db = {
        "max_B7_mode_residual": float(item["maximum_B7_mode_detailed_balance_residual"]),
        "max_B13_charge_mode_residual": float(item["maximum_B13_charge_mode_detailed_balance_residual"]),
        "max_final_muon_shell_relative_error": float(item["maximum_final_muon_shell_relative_error"]),
    }
    if any(not np.isfinite(value) or value < 0.0 for value in db.values()):
        raise ValueError(("non-finite detailed-balance or shell residual", db))

    status = (
        "PASS"
        if maximum_metric < TARGET_NORMALIZED
        and b7_total < 1.0e-12
        and max(b7_modes.values()) < 1.0e-12
        and max_quad_error < 1.0e-6
        and max_mode_closure < 1.0e-12
        and max(surface_residuals.values()) < 1.0e-6
        and db["max_B7_mode_residual"] < 1.0e-10
        and db["max_B13_charge_mode_residual"] < 1.0e-10
        and db["max_final_muon_shell_relative_error"] < 2.0e-10
        else "REFINE"
    )

    report = {
        "title": "A0 10 MeV adaptive-radial energy-order convergence",
        "status": status,
        "reference": {
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
            "polarizations": item["polarization_modes"],
            "adaptive_radial": payload["numerics"]["adaptive_radial_enabled"],
        },
        "comparison_definition": (
            "The full 121-point coupling curves are compared for both outer "
            "boundaries and separately for L,+,-. The report also compares "
            "thin-source totals and modes, surface asymptotes, and the B.7 "
            "source against C1 on the identical 153-node, energy-48 grid. "
            "Pointwise relative differences are evaluated only above 1e-8 "
            "of the reference curve peak; normalized absolute differences "
            "are reported over the full curve."
        ),
        "target": TARGET_NORMALIZED,
        "maximum_over_all_reported_metrics": maximum_metric,
        "total_curve_changes": total_changes,
        "mode_curve_changes": mode_changes,
        "thin_source_total_relative_changes": source_total_changes,
        "thin_source_mode_relative_changes": source_mode_changes,
        "surface_asymptote_mode_relative_changes": surface_changes,
        "surface_asymptote_high_g_relative_residuals": surface_residuals,
        "B7_unchanged_against_C1_153node_energy48": {
            "total_relative_difference": b7_total,
            "per_mode_relative_differences": b7_modes,
        },
        "max_quadpack_relative_error_estimate": max_quad_error,
        "max_mode_sum_relative_residual": max_mode_closure,
        "detailed_balance": db,
        "scope": (
            "A0 10 MeV energy-order convergence on the reconstructed "
            "SFHo-18.8 interior profile. Outer 25--100 km semi-Compton opacity "
            "is omitted; this is not an SN1987A exclusion curve."
        ),
    }
    SUMMARY.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
