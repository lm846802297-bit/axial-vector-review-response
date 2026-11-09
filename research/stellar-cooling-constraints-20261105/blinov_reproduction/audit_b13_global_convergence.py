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

def mass_token(mass):
    value = float(mass)
    if abs(value - 0.1) < 1e-12:
        return "0p1"
    if abs(value - 1.0) < 1e-12:
        return "1"
    if abs(value - 10.0) < 1e-12:
        return "10"
    return f"{value:g}".replace(".", "p")


def default_reference(mass):
    token = mass_token(mass)
    return HERE / "outputs" / f"b13_global_transport_summary_vertex_preserving_{token}mev_2026-11-09.json"


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
            "thin_luminosity_shift_vs_original_40x100x16x32": shift_summary(
                item["points"], base["points"], "optically_thin_luminosity_erg_s"
            ),
            "thin_luminosity_erg_s": [p["optically_thin_luminosity_erg_s"] for p in item["points"]],
            "escape_fraction": [p["escape_fraction"] for p in item["points"]],
            "luminosity_erg_s": [p["calculated_luminosity_erg_s"] for p in item["points"]],
            "reference_luminosity_erg_s": [p["reference_luminosity_erg_s"] for p in item["points"]],
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


def pairwise_shift(coarse, fine, variant, peak_index):
    import numpy as np
    fields = {
        "Lthin": "thin_luminosity_erg_s",
        "Pesc": "escape_fraction",
        "Ltotal": "luminosity_erg_s",
    }
    result = {}
    for label, field in fields.items():
        a = np.asarray(coarse["variants"][variant][field], float)
        b = np.asarray(fine["variants"][variant][field], float)
        rel = b / a - 1.0
        result[label] = {
            "max_abs_relative_change": float(np.max(np.abs(rel))),
            "mean_abs_relative_change": float(np.mean(np.abs(rel))),
            "weak_endpoint_relative_change": float(rel[0]),
            "reference_peak_relative_change": float(rel[peak_index]),
            "strong_endpoint_relative_change": float(rel[-1]),
        }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--reference", type=Path, default=None)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--kernel-orders", default="12,8,8,8")
    parser.add_argument("--refined-orders", default="16,10,10,10")
    parser.add_argument("--active-threshold", type=float, default=1.0e-8)
    args = parser.parse_args()

    reference_path = args.reference or default_reference(args.mass)
    output_path = args.output or (
        HERE / "outputs" /
        f"b13_global_convergence_vertex_preserving_{mass_token(args.mass)}mev_2026-11-09.json"
    )
    base_orders = tuple(int(x) for x in args.kernel_orders.split(","))
    refined_orders = tuple(int(x) for x in args.refined_orders.split(","))
    if len(base_orders) != 4 or len(refined_orders) != 4:
        raise ValueError("Kernel orders must contain four comma-separated integers")

    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    ref_variants = reference["variant_results"]
    ref_profile = reference["profile"]["sha256"]
    scans = [
        ("radial60", 60, 100, 16, 32),
        ("radial80", 80, 100, 16, 32),
        ("energy150", 40, 150, 16, 32),
        ("energy200", 40, 200, 16, 32),
        ("angle24", 40, 100, 24, 32),
        ("angle32", 40, 100, 32, 32),
        ("path48", 40, 100, 16, 48),
        ("path64", 40, 100, 16, 64),
        ("combined_60x140_24x48", 60, 140, 24, 48),
    ]
    results = []
    by_label = {}
    with tempfile.TemporaryDirectory(prefix="b13-convergence-") as tmp:
        tmp = Path(tmp)
        for label, nr, ne, na, ns in scans:
            orders = {
                "radial_order": nr,
                "energy_order": ne,
                "angular_order": na,
                "path_order": ns,
                "local_kernel_base_orders": list(base_orders),
                "local_kernel_refined_orders": list(refined_orders),
            }
            b16 = run_b16_mass(
                args.mass, args.profile, args.fig7, nr, ne, na, ns, 25.0, 1000.0
            )
            baseline_path = tmp / f"{label}_b16_baseline.json"
            baseline_path.write_text(
                json.dumps({"results": [b16]}, indent=2) + "\n",
                encoding="utf-8",
            )
            output_path_full = tmp / f"{label}_b13_full.json"
            result = AUDIT.run(
                profile_path=args.profile,
                fig7_path=args.fig7,
                baseline_path=baseline_path,
                output_path=output_path_full,
                mass=args.mass,
                radial_order=nr,
                energy_order=ne,
                angular_order=na,
                path_order=ns,
                radius_km=25.0,
                energy_offset=1000.0,
                base_orders=base_orders,
                refined_orders=refined_orders,
                active_opacity_fraction_threshold=args.active_threshold,
            )
            if result["profile"]["sha256"] != ref_profile:
                raise RuntimeError(f"{label}: profile fingerprint changed")
            if result["archived_B16_baseline"]["max_relative_reproduction_residual"] > 2.0e-10:
                raise ArithmeticError(f"{label}: same-grid B.16 closure failed")
            compact = compact_run(result, label, orders, ref_variants)
            results.append(compact)
            by_label[label] = compact
            print(json.dumps({
                "mass_MeV": args.mass,
                "label": label,
                "quadrature": orders,
                "B16_baseline_reproduction_residual": compact["B16_baseline_reproduction_residual"],
                "B13_mu_minus_shift_vs_original": compact["variants"]["B13_mu_minus_consistent_source_and_opacity"]["luminosity_shift_vs_original_40x100x16x32"],
                "wall_time_seconds": result["configuration"]["wall_time_seconds"],
            }, indent=2), flush=True)

        # A full-grid local-kernel order check separates collision-kernel
        # quadrature error from radial/energy/ray integration error.
        b16_baseline = run_b16_mass(
            args.mass, args.profile, args.fig7, 40, 100, 16, 32, 25.0, 1000.0
        )
        baseline_path = tmp / "kernel_order_b16_baseline.json"
        baseline_path.write_text(
            json.dumps({"results": [b16_baseline]}, indent=2) + "\n",
            encoding="utf-8",
        )
        kernel_order_result = AUDIT.run(
            profile_path=args.profile,
            fig7_path=args.fig7,
            baseline_path=baseline_path,
            output_path=tmp / "kernel_order_b13_full.json",
            mass=args.mass,
            radial_order=40,
            energy_order=100,
            angular_order=16,
            path_order=32,
            radius_km=25.0,
            energy_offset=1000.0,
            base_orders=(16, 10, 10, 10),
            refined_orders=(20, 12, 12, 12),
            active_opacity_fraction_threshold=args.active_threshold,
        )
        if kernel_order_result["archived_B16_baseline"]["max_relative_reproduction_residual"] > 2.0e-10:
            raise ArithmeticError("Kernel-order run: same-grid B.16 closure failed")
        kernel_order_compact = compact_run(
            kernel_order_result,
            "kernel_16x10x10x10",
            {
                "radial_order": 40, "energy_order": 100,
                "angular_order": 16, "path_order": 32,
                "local_kernel_base_orders": [16, 10, 10, 10],
                "local_kernel_refined_orders": [20, 12, 12, 12],
            },
            ref_variants,
        )

    variant = "B13_mu_minus_consistent_source_and_opacity"
    peak_index = max(
        range(len(ref_variants[variant]["points"])),
        key=lambda i: float(ref_variants[variant]["points"][i]["reference_luminosity_erg_s"])
    )
    pair_specs = {
        "radial_60_to_80": ("radial60", "radial80"),
        "energy_150_to_200": ("energy150", "energy200"),
        "angular_24_to_32": ("angle24", "angle32"),
        "path_48_to_64": ("path48", "path64"),
    }
    pairwise = {
        name: pairwise_shift(by_label[coarse], by_label[fine], variant, peak_index)
        for name, (coarse, fine) in pair_specs.items()
    }
    acceptance = {}
    for dimension, shifts in pairwise.items():
        thin_ok = shifts["Lthin"]["max_abs_relative_change"] < 0.01
        peak_ok = abs(shifts["Ltotal"]["reference_peak_relative_change"]) < 0.01
        strong_ok = abs(shifts["Ltotal"]["strong_endpoint_relative_change"]) < 0.02
        escape_ok = shifts["Pesc"]["max_abs_relative_change"] < 0.01
        acceptance[dimension] = {
            "Lthin_max_change_below_1pct": thin_ok,
            "Pesc_max_change_below_1pct": escape_ok,
            "peak_Ltotal_change_below_1pct": peak_ok,
            "strong_endpoint_Ltotal_change_below_2pct": strong_ok,
            "passed": thin_ok and escape_ok and peak_ok and strong_ok,
        }

    kernel_variant = kernel_order_compact["variants"][variant]
    kernel_shift = kernel_variant["luminosity_shift_vs_original_40x100x16x32"]
    kernel_thin_shift = kernel_variant["thin_luminosity_shift_vs_original_40x100x16x32"]
    kernel_escape_shift = kernel_variant["escape_fraction_shift_vs_original_40x100x16x32"]
    kernel_acceptance = {
        "Lthin_max_change_below_1pct": kernel_thin_shift["maximum_absolute_relative_shift"] < 0.01,
        "Pesc_max_change_below_1pct": kernel_escape_shift["maximum_absolute_relative_shift"] < 0.01,
        "peak_Ltotal_change_below_1pct": abs(kernel_shift["reference_peak_relative_shift"]) < 0.01,
        "strong_endpoint_Ltotal_change_below_2pct": abs(kernel_shift["strong_endpoint_relative_shift"]) < 0.02,
    }
    kernel_acceptance["passed"] = all(kernel_acceptance.values())

    output = {
        "title": f"Global B.13 quadrature convergence audit at {args.mass:g} MeV",
        "mass_MeV": float(args.mass),
        "scope": (
            "One-factor radial, energy, angular, and path convergence, a combined "
            "higher grid, and a full-grid local collision-kernel order check. "
            "The profile, physical channels, fixed-omega B.2 convention, and "
            "coupling normalization are held fixed."
        ),
        "reference": {
            "summary_path": str(reference_path),
            "profile_sha256": ref_profile,
            "original_configuration": reference["configuration"],
        },
        "scans": results,
        "pairwise_convergence": pairwise,
        "acceptance": acceptance,
        "overall_grid_passed": all(x["passed"] for x in acceptance.values()),
        "kernel_order_scan": kernel_order_compact,
        "kernel_order_acceptance": kernel_acceptance,
        "overall_passed": all(x["passed"] for x in acceptance.values()) and kernel_acceptance["passed"],
        "acceptance_targets": {
            "optically_thin_source_relative_change": 0.01,
            "escape_fraction_max_relative_change": 0.01,
            "peak_luminosity_relative_change": 0.01,
            "strong_endpoint_luminosity_relative_change": 0.02,
            "note": "Project numerical acceptance targets, not literature-derived physical uncertainty bounds. The full-grid local-kernel order check is separate from the global radial/energy/ray quadrature checks.",
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output_path),
        "mass_MeV": args.mass,
        "overall_grid_passed": output["overall_grid_passed"],
        "kernel_order_acceptance": kernel_acceptance,
        "overall_passed": output["overall_passed"],
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
