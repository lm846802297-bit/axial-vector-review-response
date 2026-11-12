"""Independent-grid B.16 quadrature convergence around the archived high-order baseline.

The published Fig. 7 baseline is the fixed-omega B.14--B.19 prescription.
The B.1 source grid and B.2 opacity interpolation grid remain independent.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

try:
    from .audit_b16_global_redshift import (
        DEFAULT_FIG7,
        DEFAULT_PROFILE,
        run_mass,
        sha256,
    )
except ImportError:
    from audit_b16_global_redshift import (
        DEFAULT_FIG7,
        DEFAULT_PROFILE,
        run_mass,
        sha256,
    )


HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE / "outputs"

# Each variation changes only the named quadrature family. The final row is
# a joint stress test; the B.1 and B.2 radial grids stay fixed in every case.
CONFIGS = {
    "energy_300": (200, 300, 32, 64, 640),
    "angular_48": (200, 200, 48, 64, 640),
    "path_96": (200, 200, 32, 96, 640),
    "combined_300_48_96": (200, 300, 48, 96, 640),
}


def mass_tag(mass: float) -> str:
    return f"{float(mass):g}"


def source_total(result: dict) -> float:
    return float(sum(
        item["thin_source_erg_s_per_g2"]
        for item in result["source_channel_fractions"].values()
    ))


def compare_rows(reference_rows: list[dict], current_rows: list[dict]) -> dict:
    if len(reference_rows) != len(current_rows):
        raise ArithmeticError("Coupling-grid length changed between quadrature runs")
    rows = []
    for ref, cur in zip(reference_rows, current_rows):
        if not math.isclose(ref["g"], cur["g"], rel_tol=0.0, abs_tol=1e-24):
            raise ArithmeticError("Coupling-grid values changed between quadrature runs")
        ratio = cur["calculated_luminosity_erg_s"] / ref["calculated_luminosity_erg_s"]
        rows.append({
            "g": cur["g"],
            "relative_change_vs_high_order_baseline": float(ratio - 1.0),
        })
    changes = [x["relative_change_vs_high_order_baseline"] for x in rows]
    return {
        "mean_absolute_relative_change": float(np.mean(np.abs(changes))),
        "maximum_absolute_relative_change": float(np.max(np.abs(changes))),
        "maximum_change_g": rows[int(np.argmax(np.abs(changes))) ]["g"],
        "points": rows,
    }


def run(profile_path: Path, fig7_path: Path, baseline_path: Path, mass: float) -> dict:
    baseline_payload = json.loads(baseline_path.read_text(encoding="utf-8"))
    baseline = baseline_payload["result"]
    baseline_config = baseline["configuration"]

    expected_baseline = {
        "radial_order": 200,
        "opacity_order": 640,
        "energy_order": 200,
        "angular_order": 32,
        "path_order": 64,
        "source_grid_mode": "independent",
    }
    for key, expected in expected_baseline.items():
        if baseline_config.get(key) != expected:
            raise ArithmeticError(
                f"Archived baseline {key}={baseline_config.get(key)!r}, expected {expected!r}"
            )
    if not math.isclose(baseline["mass_MeV"], mass, rel_tol=0.0, abs_tol=1e-12):
        raise ArithmeticError("Archived baseline mass does not match requested mass")
    if sha256(profile_path) != baseline["profile"]["sha256"]:
        raise ArithmeticError("Profile hash differs from the archived high-order baseline")
    if sha256(fig7_path) != baseline["fig7_reference"]["sha256"]:
        raise ArithmeticError("Fig. 7 digitization hash differs from the archived baseline")

    baseline_source_total = source_total(baseline)
    results = {}
    for name, (nr, ne, na, ns, no) in CONFIGS.items():
        current = run_mass(
            mass,
            profile_path,
            fig7_path,
            radial_order=nr,
            energy_order=ne,
            angular_order=na,
            path_order=ns,
            radius_km=25.0,
            energy_offset=1000.0,
            opacity_order=no,
            separate_source_grid=True,
        )
        config = current["configuration"]

        # Source and opacity grids are held fixed; only the intended
        # quadrature family is allowed to change.
        if config["source_grid_mode"] != "independent":
            raise ArithmeticError(f"{name}: source grid is not independent")
        if config["source_grid_sha256"] != baseline_config["source_grid_sha256"]:
            raise ArithmeticError(f"{name}: B.1 source grid changed")
        if config["opacity_grid_sha256"] != baseline_config["opacity_grid_sha256"]:
            raise ArithmeticError(f"{name}: B.2 opacity grid changed")
        if config["opacity_order"] != 640:
            raise ArithmeticError(f"{name}: opacity interpolation order changed")
        if config["radial_order"] != 200:
            raise ArithmeticError(f"{name}: source radial order changed")

        fixed = compare_rows(
            baseline["eq_b2_fixed_omega_baseline"]["points"],
            current["eq_b2_fixed_omega_baseline"]["points"],
        )
        redshift = compare_rows(
            baseline["path_redshift_only_diagnostic"]["points"],
            current["path_redshift_only_diagnostic"]["points"],
        )
        current_source_total = source_total(current)
        results[name] = {
            "configuration": config,
            "grid_identity": {
                "source_grid_sha256": config["source_grid_sha256"],
                "opacity_grid_sha256": config["opacity_grid_sha256"],
                "energy_grid_sha256": config["energy_grid_sha256"],
                "source_radial_node_count": config["source_radial_node_count"],
                "opacity_radial_node_count": config["opacity_radial_node_count"],
                "energy_node_count": config["energy_node_count"],
            },
            "source_integral": {
                "thin_source_erg_s_per_g2": current_source_total,
                "relative_change_vs_high_order_baseline": (
                    current_source_total / baseline_source_total - 1.0
                ),
            },
            "fixed_omega": {
                "curve_metrics_vs_fig7": current["eq_b2_fixed_omega_baseline"]["curve_metrics"],
                "luminosity_change_vs_high_order_baseline": fixed,
            },
            "path_redshift_diagnostic": {
                "curve_metrics_vs_fig7": current["path_redshift_only_diagnostic"]["curve_metrics"],
                "luminosity_change_vs_high_order_baseline": redshift,
            },
        }

    return {
        "title": "Independent-grid B.16 quadrature convergence",
        "paper_reference": "Blinov et al., JHEP 06 (2026) 155, Appendix B, Eqs. (B.14)--(B.19)",
        "mass_MeV": float(mass),
        "baseline": {
            "path": str(baseline_path),
            "configuration": baseline_config,
            "profile_sha256": baseline["profile"]["sha256"],
            "fig7_reference_sha256": baseline["fig7_reference"]["sha256"],
            "fixed_omega_metrics_vs_fig7": baseline["eq_b2_fixed_omega_baseline"]["curve_metrics"],
            "path_redshift_metrics_vs_fig7": baseline["path_redshift_only_diagnostic"]["curve_metrics"],
            "thin_source_erg_s_per_g2": baseline_source_total,
        },
        "fixed_grid_policy": {
            "source_radial_order": 200,
            "opacity_order": 640,
            "source_and_opacity_grids_are_independent": True,
            "energy_offset_MeV": 1000.0,
            "radius_km": 25.0,
        },
        "variations": results,
        "interpretation_guard": (
            "Workflow success validates execution, grid isolation, and finite outputs. "
            "Numerical convergence is assessed from the reported changes and is not "
            "automatically declared by a green workflow."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mass", type=float, required=True)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payload = run(args.profile, args.fig7, args.baseline, args.mass)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "mass_MeV": payload["mass_MeV"],
        "baseline": payload["baseline"]["configuration"],
        "variations": {
            name: {
                "fixed_omega_max_change": item["fixed_omega"]["luminosity_change_vs_high_order_baseline"]["maximum_absolute_relative_change"],
                "redshift_max_change": item["path_redshift_diagnostic"]["luminosity_change_vs_high_order_baseline"]["maximum_absolute_relative_change"],
                "source_integral_change": item["source_integral"]["relative_change_vs_high_order_baseline"],
            }
            for name, item in payload["variations"].items()
        },
        "output": str(args.output),
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
