"""Independent quadrature-convergence audit for the 10 MeV global B.13 run.

Only numerical quadrature orders are varied. Physics kernels, profile, channels,
fixed-omega B.2 convention, and local B.13 kernel orders remain unchanged.
"""
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

DEFAULT_REFERENCE = HERE / "outputs" / "b13_global_transport_summary_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b13_global_convergence_vertex_preserving_10mev_2026-11-09.json"


def compact_run(result: dict, label: str, orders: dict) -> dict:
    variants = result["variant_results"]
    selected = {}
    for key in ("B13_mu_minus_consistent", "B13_mu_minus_plus_mu_plus_consistent"):
        if key not in variants:
            raise KeyError(f"Missing expected result variant: {key}")
        item = variants[key]
        points = item["points"]
        selected[key] = {
            "metrics_vs_fig7": item["metrics_vs_fig7"],
            "thin_luminosity_ratio_vs_B16": item["thin_luminosity_ratio_vs_B16"],
            "weak_endpoint_luminosity_erg_s": points[0]["calculated_luminosity_erg_s"],
            "peak_point_luminosity_erg_s": points[max(range(len(points)), key=lambda i: points[i]["reference_luminosity_erg_s"])]["calculated_luminosity_erg_s"],
            "strong_endpoint_luminosity_erg_s": points[-1]["calculated_luminosity_erg_s"],
            "weak_endpoint_escape_fraction": points[0]["escape_fraction"],
            "peak_point_escape_fraction": points[max(range(len(points)), key=lambda i: points[i]["reference_luminosity_erg_s"])]["escape_fraction"],
            "strong_endpoint_escape_fraction": points[-1]["escape_fraction"],
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
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    reference = json.loads(args.reference.read_text(encoding="utf-8"))
    ref_variants = reference["variant_results"]
    ref_config = reference["configuration"]
    ref_profile = reference["profile"]["sha256"]

    # Orthogonal scans isolate radial, energy, and ray-integration sensitivity.
    # A combined refinement then checks whether the separate trends persist.
    scans = [
        ("radial_60", 60, 100, 16, 32),
        ("energy_160", 40, 160, 16, 32),
        ("ray_24x48", 40, 100, 24, 48),
        ("combined_60_160_24x48", 60, 160, 24, 48),
    ]
    results = []
    with tempfile.TemporaryDirectory(prefix="b13-convergence-") as tmp:
        for label, nr, ne, na, ns in scans:
            orders = {
                "radial_order": nr,
                "energy_order": ne,
                "angular_order": na,
                "path_order": ns,
                "local_kernel_base_orders": [12, 8, 8, 8],
                "local_kernel_refined_orders": [16, 10, 10, 10],
            }
            output_path = Path(tmp) / f"{label}.json"
            result = AUDIT.run(
                profile_path=AUDIT.DEFAULT_PROFILE,
                fig7_path=AUDIT.DEFAULT_FIG7,
                baseline_path=AUDIT.DEFAULT_BASELINE,
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
            results.append(compact_run(result, label, orders))

    baseline = {}
    for key in ("B13_mu_minus_consistent", "B13_mu_minus_plus_mu_plus_consistent"):
        baseline[key] = {
            "metrics_vs_fig7": ref_variants[key]["metrics_vs_fig7"],
            "thin_luminosity_ratio_vs_B16": ref_variants[key]["thin_luminosity_ratio_vs_B16"],
            "weak_endpoint_luminosity_erg_s": ref_variants[key]["points"][0]["calculated_luminosity_erg_s"],
            "peak_point_luminosity_erg_s": ref_variants[key]["points"][max(range(len(ref_variants[key]["points"])), key=lambda i: ref_variants[key]["points"][i]["reference_luminosity_erg_s"])]["calculated_luminosity_erg_s"],
            "strong_endpoint_luminosity_erg_s": ref_variants[key]["points"][-1]["calculated_luminosity_erg_s"],
            "weak_endpoint_escape_fraction": ref_variants[key]["points"][0]["escape_fraction"],
            "peak_point_escape_fraction": ref_variants[key]["points"][max(range(len(ref_variants[key]["points"])), key=lambda i: ref_variants[key]["points"][i]["reference_luminosity_erg_s"])]["escape_fraction"],
            "strong_endpoint_escape_fraction": ref_variants[key]["points"][-1]["escape_fraction"],
        }

    output = {
        "title": "Global B.13 quadrature-convergence audit at 10 MeV",
        "scope": "Numerical convergence only; no physics kernel, profile, interaction channel, or axial-vector result is changed.",
        "reference": {
            "summary_path": str(args.reference),
            "profile_sha256": ref_profile,
            "original_configuration": ref_config,
            "baseline_variants": baseline,
        },
        "scans": results,
        "acceptance_targets": {
            "thin_source_relative_change": 0.01,
            "peak_luminosity_relative_change": 0.01,
            "strong_endpoint_luminosity_relative_change": 0.02,
            "note": "Project numerical acceptance targets, not literature-derived physical uncertainty bounds. Compare against the original 40/100/16/32 result and also inspect the combined-refinement result.",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "profile_sha256": ref_profile,
        "scans": [{
            "label": item["label"],
            "quadrature": item["quadrature"],
            "B16_baseline_reproduction_residual": item["B16_baseline_reproduction_residual"],
            "variants": {
                key: {
                    "mean_abs_diff": val["metrics_vs_fig7"]["mean_absolute_relative_difference"],
                    "weak_diff": val["metrics_vs_fig7"]["weak_endpoint_relative_difference"],
                    "peak_diff": val["metrics_vs_fig7"]["reference_peak_relative_difference"],
                    "strong_diff": val["metrics_vs_fig7"]["strong_endpoint_relative_difference"],
                    "thin_ratio": val["thin_luminosity_ratio_vs_B16"],
                    "strong_escape": val["strong_endpoint_escape_fraction"],
                } for key, val in item["variants"].items()
            },
        } for item in results],
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
