"""Radial/energy convergence scan for the global B.13 transport result.

The scan reuses the same exact B.13 kernel and builds a matching B.16 baseline
for each grid, so every B.13/B.16 comparison is internally like-for-like.
Only compact convergence summaries are retained; full local-rate grids from
the three test runs live in the temporary runner directory.
"""
from __future__ import annotations

import argparse
import json
import tempfile
import time
from pathlib import Path

import numpy as np

from blinov_reproduction.reference import DEFAULT_PROFILE
from blinov_reproduction.audit_b16_global_redshift import (
    DEFAULT_FIG7, run_mass as run_b16_mass,
)
from blinov_reproduction.audit_b13_global_transport import run as run_b13_global

HERE = Path(__file__).resolve().parent
DEFAULT_BASELINE_SUMMARY = HERE / "outputs" / "b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b13_global_grid_convergence_2026-11-09.json"

CONFIGS = (
    {"name": "radial_60_energy_100", "radial_order": 60, "energy_order": 100},
    {"name": "radial_40_energy_140", "radial_order": 40, "energy_order": 140},
    {"name": "radial_60_energy_140", "radial_order": 60, "energy_order": 140},
)


def compare_points(points, baseline_points):
    values = np.asarray([p["calculated_luminosity_erg_s"] for p in points], float)
    baseline = np.asarray(
        [p["calculated_luminosity_erg_s"] for p in baseline_points], float
    )
    if values.shape != baseline.shape:
        raise ValueError("Convergence grid has a different number of Fig. 7 coupling points")
    rel = values / baseline - 1.0
    peak = int(np.argmax([p["reference_luminosity_erg_s"] for p in baseline_points]))
    return {
        "mean_absolute_relative_shift_vs_40x100": float(np.mean(np.abs(rel))),
        "maximum_absolute_relative_shift_vs_40x100": float(np.max(np.abs(rel))),
        "weak_endpoint_relative_shift_vs_40x100": float(rel[0]),
        "reference_peak_relative_shift_vs_40x100": float(rel[peak]),
        "strong_endpoint_relative_shift_vs_40x100": float(rel[-1]),
    }


def run_scan(
    profile_path=DEFAULT_PROFILE,
    fig7_path=DEFAULT_FIG7,
    baseline_summary_path=DEFAULT_BASELINE_SUMMARY,
    output_path=DEFAULT_OUTPUT,
    mass=10.0,
    angular_order=16,
    path_order=32,
    radius_km=25.0,
    energy_offset=1000.0,
    base_orders=(12, 8, 8, 8),
    refined_orders=(16, 10, 10, 10),
    active_threshold=1.0e-8,
):
    baseline_summary = json.loads(
        Path(baseline_summary_path).read_text(encoding="utf-8")
    )
    baseline_variant = baseline_summary["variant_results"][
        "B13_mu_minus_consistent_source_and_opacity"
    ]
    baseline_points = baseline_variant["points"]
    results = []

    with tempfile.TemporaryDirectory(prefix="b13-grid-convergence-") as tmp:
        tmp = Path(tmp)
        for config in CONFIGS:
            started = time.time()
            nr = config["radial_order"]
            ne = config["energy_order"]

            # Build the matching B.16 baseline on this exact grid. The global
            # B.13 runner then verifies its pre-replacement B.16 closure.
            b16_result = run_b16_mass(
                mass, profile_path, fig7_path,
                nr, ne, angular_order, path_order,
                radius_km, energy_offset,
            )
            baseline_path = tmp / f"{config['name']}_b16_baseline.json"
            baseline_path.write_text(
                json.dumps({"results": [b16_result]}, indent=2) + "\n",
                encoding="utf-8",
            )

            full_output_path = tmp / f"{config['name']}_b13_full.json"
            result = run_b13_global(
                profile_path, fig7_path, baseline_path, full_output_path,
                mass, nr, ne, angular_order, path_order,
                radius_km, energy_offset, tuple(base_orders),
                tuple(refined_orders), active_threshold,
            )

            b13_minus = result["variant_results"][
                "B13_mu_minus_consistent_source_and_opacity"
            ]
            b13_both = result["variant_results"][
                "B13_both_charges_consistent_source_and_opacity"
            ]
            b16 = result["variant_results"]["B16_reference"]

            results.append({
                "configuration": config,
                "active_radial_node_count": result["configuration"]["active_radial_node_count"],
                "active_energy_node_count": result["configuration"]["active_energy_node_count"],
                "exact_B13_kernel_evaluations": result["configuration"]["exact_B13_kernel_evaluations"],
                "B16_baseline_closure_residual": result["archived_B16_baseline"]["max_relative_reproduction_residual"],
                "B13_mu_minus_shift_vs_40x100": compare_points(
                    b13_minus["points"], baseline_points
                ),
                "B13_both_charge_shift_vs_40x100": compare_points(
                    b13_both["points"], baseline_summary["variant_results"][
                        "B13_both_charges_consistent_source_and_opacity"
                    ]["points"]
                ),
                "B13_mu_minus_metrics_vs_fig7": b13_minus["metrics_vs_fig7"],
                "B13_both_charge_metrics_vs_fig7": b13_both["metrics_vs_fig7"],
                "B16_metrics_vs_fig7": b16["metrics_vs_fig7"],
                "B13_mu_minus_thin_source_ratio_vs_B16": b13_minus["thin_luminosity_ratio_vs_B16"],
                "B13_mu_minus_strong_escape_fraction": b13_minus["strong_endpoint_escape_fraction"],
                "B13_numerical_validation": result["B13_numerical_validation"],
                "wall_time_seconds": float(time.time() - started),
            })
            print(json.dumps({
                "configuration": config,
                "B13_mu_minus_shift_vs_40x100": results[-1]["B13_mu_minus_shift_vs_40x100"],
                "B13_mu_minus_metrics_vs_fig7": b13_minus["metrics_vs_fig7"],
                "exact_kernel_evaluations": results[-1]["exact_B13_kernel_evaluations"],
                "wall_time_seconds": results[-1]["wall_time_seconds"],
            }, indent=2), flush=True)
            del result

    max_shift = max(
        item["B13_mu_minus_shift_vs_40x100"]["maximum_absolute_relative_shift_vs_40x100"]
        for item in results
    )
    combined = results[-1]
    combined_shift = combined["B13_mu_minus_shift_vs_40x100"][
        "maximum_absolute_relative_shift_vs_40x100"
    ]
    output = {
        "title": "Radial and energy grid convergence scan for global B.13 exact Compton transport",
        "mass_MeV": float(mass),
        "profile_sha256": baseline_summary["profile"]["sha256"],
        "baseline_configuration": {
            "radial_order": 40,
            "energy_order": 100,
            "source": str(baseline_summary_path),
        },
        "fixed_configuration": {
            "angular_order": int(angular_order),
            "path_order": int(path_order),
            "energy_offset_MeV": float(energy_offset),
            "B13_kernel_orders": list(base_orders),
            "active_opacity_fraction_threshold": float(active_threshold),
        },
        "convergence_criterion": {
            "target_maximum_relative_luminosity_shift": 0.01,
            "combined_60x140_maximum_relative_shift": combined_shift,
            "combined_grid_meets_one_percent_target": bool(combined_shift < 0.01),
        },
        "grid_results": results,
        "decision": (
            "The 60x140 combined grid meets the 1% luminosity-stability target."
            if combined_shift < 0.01 else
            "The 60x140 combined grid does not yet meet the 1% target; increase the radial and/or energy resolution before treating the B.13 global result as converged."
        ),
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(output["convergence_criterion"], indent=2), flush=True)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--baseline-summary", type=Path, default=DEFAULT_BASELINE_SUMMARY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--na", type=int, default=16)
    parser.add_argument("--ns", type=int, default=32)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()
    run_scan(
        args.profile, args.fig7, args.baseline_summary, args.output,
        args.mass, args.na, args.ns, args.radius, args.energy_offset,
    )


if __name__ == "__main__":
    main()
