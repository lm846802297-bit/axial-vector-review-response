#!/usr/bin/env python3
"""Grid-convergence audit of fixed-omega versus path-redshift B.2 transport.

The fixed-omega prescription is the literal printed Eq. (B.2). The alternative
uses E_infinity=N(source)*omega_source and omega_local(path)=E_infinity/N(path),
while keeping the Euclidean chord and ds unchanged. This is a redshift-only
sensitivity diagnostic, not a complete GR ray-tracing calculation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from blinov_reproduction.audit_b16_global_redshift import (
    DEFAULT_FIG7,
    DEFAULT_PROFILE,
    run_mass,
)

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "outputs" / "b2_path_energy_convergence_2026-11-09.json"
PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"

CONFIGS = (
    ("baseline", 40, 100, 16, 32),
    ("radial60", 60, 100, 16, 32),
    ("radial80", 80, 100, 16, 32),
    ("energy150", 40, 150, 16, 32),
    ("energy200", 40, 200, 16, 32),
    ("angle24", 40, 100, 24, 32),
    ("angle32", 40, 100, 32, 32),
    ("path48", 40, 100, 16, 48),
    ("path64", 40, 100, 16, 64),
    ("combined_60x140x24x48", 60, 140, 24, 48),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def summarize_run(result: dict, label: str) -> dict:
    fixed = result["eq_b2_fixed_omega_baseline"]
    shifted = result["path_redshift_only_diagnostic"]
    fixed_points = fixed["points"]
    shifted_points = shifted["points"]
    if len(fixed_points) != len(shifted_points):
        raise ValueError(f"{label}: fixed and redshifted coupling grids differ")

    ref = np.asarray([p["reference_luminosity_erg_s"] for p in fixed_points], float)
    lf = np.asarray([p["calculated_luminosity_erg_s"] for p in fixed_points], float)
    lr = np.asarray([p["calculated_luminosity_erg_s"] for p in shifted_points], float)
    delta = lr / lf - 1.0
    peak = int(np.argmax(ref))

    return {
        "label": label,
        "configuration": result["configuration"],
        "profile": result["profile"],
        "fig7_reference": result["fig7_reference"],
        "fixed_omega_metrics_vs_fig7": fixed["curve_metrics"],
        "path_redshift_metrics_vs_fig7": shifted["curve_metrics"],
        "redshift_shift_vs_fixed": {
            "mean_absolute_relative_shift": float(np.mean(np.abs(delta))),
            "maximum_absolute_relative_shift": float(np.max(np.abs(delta))),
            "weak_endpoint_relative_shift": float(delta[0]),
            "reference_peak_relative_shift": float(delta[peak]),
            "strong_endpoint_relative_shift": float(delta[-1]),
            "relative_shift_by_coupling": delta.tolist(),
        },
        "kinematics": shifted["kinematic_range"],
        "source_radial_distribution": result["source_radial_distribution"],
        "source_channel_fractions": result["source_channel_fractions"],
        "path_absorption_radial_decomposition": result["path_absorption_radial_decomposition"],
        "outer_mu_numu_branch_opacity_sensitivity": {
            key: value for key, value in result["outer_mu_numu_branch_opacity_sensitivity"].items()
            if key != "points"
        },
        "fixed_luminosity_erg_s": lf.tolist(),
        "redshifted_luminosity_erg_s": lr.tolist(),
        "optically_thin_luminosity_erg_s": [
            float(p["optically_thin_luminosity_erg_s"]) for p in fixed_points
        ],
        "couplings_g": [float(p["g"]) for p in fixed_points],
        "reference_luminosity_erg_s": ref.tolist(),
    }


def compare_pair(coarse: dict, fine: dict) -> dict:
    if coarse["couplings_g"] != fine["couplings_g"]:
        raise ValueError("B.2 convergence comparison has mismatched coupling grids")
    lf0 = np.asarray(coarse["fixed_luminosity_erg_s"], float)
    lf1 = np.asarray(fine["fixed_luminosity_erg_s"], float)
    lr0 = np.asarray(coarse["redshifted_luminosity_erg_s"], float)
    lr1 = np.asarray(fine["redshifted_luminosity_erg_s"], float)
    d0 = np.asarray(coarse["redshift_shift_vs_fixed"]["relative_shift_by_coupling"], float)
    d1 = np.asarray(fine["redshift_shift_vs_fixed"]["relative_shift_by_coupling"], float)
    peak = int(np.argmax(np.asarray(coarse["reference_luminosity_erg_s"], float)))

    def metrics(a, b):
        rel = b / a - 1.0
        return {
            "maximum_absolute_relative_change": float(np.max(np.abs(rel))),
            "mean_absolute_relative_change": float(np.mean(np.abs(rel))),
            "weak_endpoint_relative_change": float(rel[0]),
            "reference_peak_relative_change": float(rel[peak]),
            "strong_endpoint_relative_change": float(rel[-1]),
        }

    delta = d1 - d0
    return {
        "fixed_omega_luminosity": metrics(lf0, lf1),
        "path_redshift_luminosity": metrics(lr0, lr1),
        "redshift_shift_absolute_change": {
            "maximum_percentage_point_change": float(100.0 * np.max(np.abs(delta))),
            "mean_percentage_point_change": float(100.0 * np.mean(np.abs(delta))),
            "weak_endpoint_percentage_point_change": float(100.0 * delta[0]),
            "reference_peak_percentage_point_change": float(100.0 * delta[peak]),
            "strong_endpoint_percentage_point_change": float(100.0 * delta[-1]),
        },
    }


def run_mass_audit(mass: float, profile_path: Path, fig7_path: Path) -> dict:
    results = {}
    for label, nr, ne, na, ns in CONFIGS:
        raw = run_mass(
            mass, profile_path, fig7_path,
            radial_order=nr, energy_order=ne,
            angular_order=na, path_order=ns,
            radius_km=25.0, energy_offset=1000.0,
        )
        if raw["profile"]["sha256"] != PROFILE_SHA256:
            raise RuntimeError(f"{label}: unexpected reconstructed-profile fingerprint")
        results[label] = summarize_run(raw, label)
        print(json.dumps({
            "mass_MeV": mass,
            "case": label,
            "quadrature": [nr, ne, na, ns],
            "mean_redshift_shift": results[label]["redshift_shift_vs_fixed"]["mean_absolute_relative_shift"],
            "max_redshift_shift": results[label]["redshift_shift_vs_fixed"]["maximum_absolute_relative_shift"],
            "peak_redshift_shift": results[label]["redshift_shift_vs_fixed"]["reference_peak_relative_shift"],
            "strong_redshift_shift": results[label]["redshift_shift_vs_fixed"]["strong_endpoint_relative_shift"],
        }, indent=2), flush=True)

    pairs = {
        "radial_60_to_80": compare_pair(results["radial60"], results["radial80"]),
        "energy_150_to_200": compare_pair(results["energy150"], results["energy200"]),
        "angular_24_to_32": compare_pair(results["angle24"], results["angle32"]),
        "path_48_to_64": compare_pair(results["path48"], results["path64"]),
        "combined_to_finest_available": compare_pair(
            results["combined_60x140x24x48"], results["radial80"]
        ),
    }

    acceptance = {}
    for dimension, item in pairs.items():
        fixed_ok = item["fixed_omega_luminosity"]["maximum_absolute_relative_change"] < 0.01
        redshift_ok = item["path_redshift_luminosity"]["maximum_absolute_relative_change"] < 0.01
        delta_ok = item["redshift_shift_absolute_change"]["maximum_percentage_point_change"] < 0.5
        acceptance[dimension] = {
            "fixed_luminosity_max_change_below_1pct": fixed_ok,
            "redshifted_luminosity_max_change_below_1pct": redshift_ok,
            "redshift_effect_max_change_below_0p5_percentage_point": delta_ok,
            "passed": fixed_ok and redshift_ok and delta_ok,
        }

    baseline = results["baseline"]
    return {
        "mass_MeV": float(mass),
        "profile_sha256": baseline["profile"]["sha256"],
        "fig7_reference_sha256": baseline["fig7_reference"].get("pdf_sha256"),
        "fixed_physics": {
            "current": "pure vector, g_V=1, g_A=0; B.14--B.16 collision rates",
            "published_B2_baseline": "fixed omega_source along the Euclidean chord",
            "alternative": "omega_local(s)=omega_source*N(source)/N(path)",
            "conserved_quantity": "E_infinity=N(source)*omega_source=N(path)*omega_local(path)",
            "path_measure": "same Euclidean chord ds in both prescriptions",
            "not_claimed": "The path-redshift variant is not a complete GR ray-tracing calculation.",
            "profile_provenance": "1687-row vertex-preserving reconstruction from public figures; not raw Garching simulation output",
        },
        "configurations": results,
        "pairwise_convergence": pairs,
        "acceptance": acceptance,
        "overall_passed": all(item["passed"] for item in acceptance.values()),
        "acceptance_targets": {
            "fixed_and_redshifted_luminosity_max_change": 0.01,
            "redshift_effect_absolute_change_percentage_points": 0.5,
            "note": "Project numerical screening targets, not physical uncertainty bounds.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--masses", default="0.1,1,10")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if sha256(args.profile) != PROFILE_SHA256:
        raise RuntimeError("Unexpected SFHo-18.8 reconstructed-profile fingerprint")

    results = [
        run_mass_audit(float(token.strip()), args.profile, args.fig7)
        for token in args.masses.split(",") if token.strip()
    ]
    payload = {
        "title": "B.2 fixed-omega versus path-redshift transport convergence audit",
        "date": "2026-11-09",
        "profile_sha256": sha256(args.profile),
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "mass_results": {
            str(item["mass_MeV"]): {
                "overall_passed": item["overall_passed"],
                "acceptance": item["acceptance"],
                "baseline_redshift_shift": item["configurations"]["baseline"]["redshift_shift_vs_fixed"],
            } for item in results
        },
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
