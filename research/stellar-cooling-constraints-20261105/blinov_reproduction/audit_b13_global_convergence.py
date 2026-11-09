"""Angular/path and combined-grid convergence audit for global B.13 transport."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_PATH = HERE / "audit_b13_global_transport.py"
SPEC = importlib.util.spec_from_file_location("audit_b13_global_transport", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Could not load audit_b13_global_transport.py")
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)

from blinov_reproduction.reference import DEFAULT_PROFILE  # noqa: E402
from blinov_reproduction.audit_b16_global_redshift import (  # noqa: E402
    DEFAULT_FIG7, run_mass as run_b16_mass,
)

DEFAULT_REFERENCE = HERE / "outputs" / "b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b13_global_convergence_vertex_preserving_10mev_2026-11-09.json"


def shift_summary(points, baseline_points, field):
    import numpy as np
    values = np.asarray([p[field] for p in points], float)
    baseline = np.asarray([p[field] for p in baseline_points], float)
    if values.shape != baseline.shape:
        raise ValueError(f"Different Fig. 7 point count for {field}")
    rel = values / baseline - 1.0
    peak = int(np.argmax([p["reference_luminosity_erg_s"] for p in baseline_points]))
    return {
        "mean_absolute_relative_shift": float(np.mean(np.abs(rel))),
        "maximum_absolute_relative_shift": float(np.max(np.abs(rel))),
        "weak_endpoint_relative_shift": float(rel[0]),
        "reference_peak_relative_shift": float(rel[peak]),
        "strong_endpoint_relative_shift": float(rel[-1]),
    }


def compact_run(result, label, orders, reference_variants):
    variants = result["variant_results"]
    selected = {}
    for key in (
        "B13_mu_minus_consistent_source_and_opacity",
        "B13_both_charges_consistent_source_and_opacity",
    ):
        item = variants[key]
        base = reference_variants[key]
        selected[key] = {
            "metrics_vs_fig7": item["metrics_vs_fig7"],
            "thin_luminosity_ratio_vs_B16": item["thin_luminosity_ratio_vs_B16"],
            "luminosity_shift_vs_original_40x100x16x32": shift_summary(
                item["points"], base["points"], "calculated_luminosity_erg_s"
            ),
            "escape_fraction_shift_vs_original_40x100x16x32": shift_summary(
                item["points"], base["points"], "escape_fraction"
            ),
            "thin_luminosity_erg_s": [p["optically_thin_luminosity_erg_s"] for p in item["points"]],
            "escape_fraction": [p["escape_fraction"] for p in item["points"]],
            "luminosity_erg_s": [p["calculated_luminosity_erg_s"] for p in item["points"]],
        }
    return {
        "label": label,
        "quadrature": orders,
        "configuration": result["configuration"],
        "B16_baseline_reproduction_residual": result["archived_B16_baseline"]["max_relative_reproduction_residual"],
        "numerical_validation": result["B13_numerical_validation"],
        "source_channel_fractions": result["source_channel_fractions"],
        "radial_source_diagnostics": result["radial_source_diagnostics"],
        "opacity_weighted_diagnostics": result["opacity_weighted_diagnostics"],
        "variants": selected,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    reference = json.loads(args.reference.read_text(encoding="utf-8"))
    ref_variants = reference["variant_results"]
    ref_profile = reference["profile"]["sha256"]
    scans = [
        ("angular_only_24x32", 40, 100, 24, 32),
        ("path_only_16x48", 40, 100, 16, 48),
        ("joint_ray_24x48", 40, 100, 24, 48),
        ("combined_60x140_24x48", 60, 140, 24, 48),
    ]
    results = []
    with tempfile.TemporaryDirectory(prefix="b13-convergence-") as tmp:
        tmp = Path(tmp)
        for label, nr, ne, na, ns in scans:
            orders = {
                "radial_order": nr,
                "energy_order": ne,
                "angular_order": na,
                "path_order": ns,
                "local_kernel_base_orders": [12, 8, 8, 8],
                "local_kernel_refined_orders": [16, 10, 10, 10],
            }
            # The B.16 reference must be regenerated on the identical grid.
            b16 = run_b16_mass(
                10.0, args.profile, args.fig7, nr, ne, na, ns, 25.0, 1000.0
            )
            baseline_path = tmp / f"{label}_b16_baseline.json"
            baseline_path.write_text(
                json.dumps({"results": [b16]}, indent=2) + "\n",
                encoding="utf-8",
            )
            output_path = tmp / f"{label}_b13_full.json"
            result = AUDIT.run(
                profile_path=args.profile,
                fig7_path=args.fig7,
                baseline_path=baseline_path,
                output_path=output_path,
                mass=10.0,
                radial_order=nr,
                energy_order=ne,
                angular_order=na,
                path_order=ns,
                radius_km=25.0,
                energy_offset=1000.0,
                base_orders=(12, 8, 8, 8),
                refined_orders=(16, 10, 10, 10),
                active_opacity_fraction_threshold=1.0e-8,
            )
            if result["profile"]["sha256"] != ref_profile:
                raise RuntimeError(f"{label}: profile fingerprint changed")
            compact = compact_run(result, label, orders, ref_variants)
            results.append(compact)
            print(json.dumps({
                "label": label,
                "quadrature": orders,
                "B16_baseline_reproduction_residual": compact["B16_baseline_reproduction_residual"],
                "variants": {
                    key: {
                        "luminosity_shift": val["luminosity_shift_vs_original_40x100x16x32"],
                        "escape_shift": val["escape_fraction_shift_vs_original_40x100x16x32"],
                        "metrics_vs_fig7": val["metrics_vs_fig7"],
                    } for key, val in compact["variants"].items()
                },
                "wall_time_seconds": result["configuration"]["wall_time_seconds"],
            }, indent=2), flush=True)

    output = {
        "title": "Global B.13 quadrature convergence audit at 10 MeV",
        "scope": "Angular/path convergence and combined radial-energy-angular-path refinement only. The physical kernels, profile, interaction channels, and fixed-omega B.2 convention are unchanged.",
        "reference": {
            "summary_path": str(args.reference),
            "profile_sha256": ref_profile,
            "original_configuration": reference["configuration"],
        },
        "scans": results,
        "acceptance_targets": {
            "optically_thin_source_relative_change": 0.01,
            "peak_luminosity_relative_change": 0.01,
            "strong_endpoint_luminosity_relative_change": 0.02,
            "note": "Project numerical acceptance targets, not literature-derived physical uncertainty bounds. Compare the refined grids against the original 40x100x16x32 result.",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "scan_count": len(results)}, indent=2), flush=True)


if __name__ == "__main__":
    main()
