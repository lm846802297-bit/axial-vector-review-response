"""Post-process archived vector luminosity curves with a coupling-axis rescaling.

This audit reads existing JSON outputs only. It does not import or execute the
thermal-rate, Compton-kernel, optical-depth, or luminosity-integration code.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = ROOT / "research" / "stellar-cooling-constraints-20261105"
INPUTS = {
    "literal_scan": BASE / "blinov_reproduction" / "outputs" / "blinov_literal_scan.json",
    "literal_comparison": BASE / "blinov_reproduction" / "outputs" / "fig4_fig7_comparison.json",
    "vector_comparison": BASE / "outputs" / "vector_audit" / "luminosity_comparison.json",
}
KAPPA_MIN, KAPPA_MAX, GRID_POINTS = 0.90, 1.10, 801

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate_curve(x_values, y_values):
    x = np.asarray(x_values, dtype=float)
    y = np.asarray(y_values, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or len(x) != len(y) or len(x) < 2:
        raise ValueError("A curve requires matching one-dimensional arrays with at least two points")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("Curve coordinates must be finite")
    # Archived high-coupling luminosities can underflow to exact zero. Trim
    # only a trailing zero tail; an interior zero would make log interpolation
    # ambiguous and is therefore rejected.
    positive = np.flatnonzero(y > 0.0)
    if positive.size == 0:
        raise ValueError("Curve contains no positive luminosity samples")
    last_positive = int(positive[-1])
    if np.any(y[:last_positive + 1] <= 0.0):
        raise ValueError("Nonpositive luminosity occurs inside the sampled curve")
    x, y = x[:last_positive + 1], y[:last_positive + 1]
    if np.any(x <= 0.0) or np.any(np.diff(x) <= 0.0):
        raise ValueError("Log interpolation requires positive x and strictly increasing x")
    return x, y

def log_interpolate(x_value, x_values, y_values):
    """Interpolate y(x) linearly in log(y)-log(x), without extrapolation."""
    x, y = validate_curve(x_values, y_values)
    x_value = float(x_value)
    if x_value < x[0] or x_value > x[-1]:
        return None
    return float(np.exp(np.interp(np.log(x_value), np.log(x), np.log(y))))

def residual_metrics(log_residuals):
    residuals = np.asarray(log_residuals, dtype=float)
    if residuals.size == 0 or not np.all(np.isfinite(residuals)):
        raise ValueError("Cannot summarize an empty or non-finite residual array")
    relative = np.expm1(residuals)
    return {
        "n_points": int(residuals.size),
        "rms_log_residual_pct": float(100.0 * np.sqrt(np.mean(residuals**2))),
        "mean_abs_log_residual_pct": float(100.0 * np.mean(np.abs(residuals))),
        "max_abs_log_residual_pct": float(100.0 * np.max(np.abs(residuals))),
        "mean_abs_relative_residual_pct": float(100.0 * np.mean(np.abs(relative))),
        "max_abs_relative_residual_pct": float(100.0 * np.max(np.abs(relative))),
    }

def curve_residuals(points, x_values, y_values, kappa):
    residuals = []
    for point in points:
        predicted = log_interpolate(kappa * point["g"], x_values, y_values)
        if predicted is not None:
            residuals.append(float(np.log(predicted / point["reference_erg_s"])))
    return residuals

def fixed_fit_points(points, x_values):
    """Use one fixed point set for every trial kappa to prevent endpoint-loss bias."""
    x, _ = validate_curve(x_values, np.ones(len(x_values)))
    return [
        point for point in points
        if point["g"] * KAPPA_MIN >= x[0] * (1.0 - 1e-12)
        and point["g"] * KAPPA_MAX <= x[-1] * (1.0 + 1e-12)
    ]

def fit_one_scale(datasets):
    grid = np.linspace(KAPPA_MIN, KAPPA_MAX, GRID_POINTS)
    best = None
    for index, kappa in enumerate(grid):
        residuals = []
        for dataset in datasets:
            residuals.extend(curve_residuals(
                dataset["fit_points"], dataset["x"], dataset["y"], float(kappa)
            ))
        metrics = residual_metrics(residuals)
        if best is None or metrics["rms_log_residual_pct"] < best["metrics"]["rms_log_residual_pct"]:
            best = {
                "kappa": float(kappa),
                "grid_index": int(index),
                "fit_at_search_boundary": bool(index in (0, GRID_POINTS - 1)),
                "metrics": metrics,
            }
    return best

def summarize_datasets(datasets):
    prepared, per_mass = [], {}
    for dataset in datasets:
        x, y = validate_curve(dataset["x"], dataset["y"])
        points = dataset["points"]
        fit_points = fixed_fit_points(points, x)
        if len(fit_points) < 3:
            raise ValueError(f"Insufficient fixed-overlap points at mass {dataset['mass_MeV']} MeV")
        baseline_all = residual_metrics(curve_residuals(points, x, y, 1.0))
        baseline_fit = residual_metrics(curve_residuals(fit_points, x, y, 1.0))
        prepared.append({"fit_points": fit_points, "x": x, "y": y})
        per_mass[str(int(round(float(dataset["mass_MeV"]))))] = {
            "mass_MeV": float(dataset["mass_MeV"]),
            "n_reference_points": len(points),
            "n_fixed_fit_points": len(fit_points),
            "baseline_all_points": baseline_all,
            "baseline_fixed_fit_subset": baseline_fit,
            "best_fit": fit_one_scale([{"fit_points": fit_points, "x": x, "y": y}]),
        }
    global_fit = fit_one_scale(prepared)
    return {
        "per_mass": per_mass,
        "global_fit": global_fit,
        "fixed_fit_point_counts": {key: value["n_fixed_fit_points"] for key, value in per_mass.items()},
    }

def build_literal_datasets(scan, comparison, vector_data):
    scan_by_mass = {float(row["mass_MeV"]): row for row in scan["results"]}
    datasets = []
    for entry in comparison["fig7"]:
        mass = float(entry["mass_MeV"])
        reference = vector_data["reference_vertices"][str(mass)]
        row = scan_by_mass[mass]
        points = [
            {"g": float(g), "reference_erg_s": float(lum)}
            for g, lum in zip(reference["g"], reference["luminosity_erg_s"])
        ]
        datasets.append({
            "mass_MeV": mass, "points": points,
            "x": row["couplings"], "y": row["luminosity_erg_s"],
        })
    return datasets

def build_mode_resolved_datasets(vector_data):
    datasets = []
    for mass in (1.0, 10.0, 200.0):
        rows = sorted(
            (row for row in vector_data["comparison"]
             if float(row["mass_MeV"]) == mass and row["variant"] == "exact_modes"),
            key=lambda row: float(row["g"]),
        )
        datasets.append({
            "mass_MeV": mass,
            "points": [
                {"g": float(row["g"]), "reference_erg_s": float(row["reference_erg_s"])}
                for row in rows
            ],
            "x": [float(row["g"]) for row in rows],
            "y": [float(row["calculated_erg_s"]) for row in rows],
        })
    return datasets

def fig4_boundary_audit(comparison, literal_summary):
    global_kappa = literal_summary["global_fit"]["kappa"]
    per_mass = literal_summary["per_mass"]
    rows = []
    for entry in comparison["fig4"]:
        mass = float(entry["mass_MeV"])
        key = str(int(round(mass)))
        reference = entry["reference_crossings"]
        calc_lower, calc_upper = float(entry["calculated_lower"]), float(entry["calculated_upper"])
        def deviations(kappa):
            return {
                "lower_pct": float(100.0 * (calc_lower / kappa / reference[0] - 1.0)),
                "upper_pct": float(100.0 * (calc_upper / kappa / reference[-1] - 1.0)),
            }
        mass_fit = per_mass.get(key)
        rows.append({
            "mass_MeV": mass,
            "reference_lower": float(reference[0]),
            "reference_upper": float(reference[-1]),
            "unscaled_boundary_deviation_pct": {
                "lower": float(100.0 * entry["relative_lower"]),
                "upper": float(100.0 * entry["relative_upper"]),
            },
            "global_rescaling_kappa": global_kappa,
            "global_rescaled_boundary_deviation_pct": deviations(global_kappa),
            "masswise_fig7_kappa": None if mass_fit is None else mass_fit["best_fit"]["kappa"],
            "masswise_rescaled_boundary_deviation_pct": (
                None if mass_fit is None else deviations(mass_fit["best_fit"]["kappa"])
            ),
        })
    return rows

def run_audit():
    scan = read_json(INPUTS["literal_scan"])
    comparison = read_json(INPUTS["literal_comparison"])
    vector_data = read_json(INPUTS["vector_comparison"])
    literal = summarize_datasets(build_literal_datasets(scan, comparison, vector_data))
    mode_resolved = summarize_datasets(build_mode_resolved_datasets(vector_data))
    input_hashes = {
        name: hashlib.sha256(path.read_bytes()).hexdigest()
        for name, path in INPUTS.items()
    }
    return {
        "audit_date": "2026-11-07",
        "title": "Coupling-axis rescaling audit of archived vector luminosity curves",
        "scope": (
            "Post-processing only. Reads archived JSON curves and digitized reference points; "
            "does not rerun B.13 thermal phase-space integrals, matrix elements, opacity integrals, "
            "or stellar luminosity scans."
        ),
        "definition": "L_calc(kappa * g_ref) is compared with L_ref(g_ref).",
        "method": {
            "kappa_search_interval": [KAPPA_MIN, KAPPA_MAX],
            "grid_points": GRID_POINTS,
            "grid_step": float((KAPPA_MAX - KAPPA_MIN) / (GRID_POINTS - 1)),
            "interpolation": "piecewise-linear in log(L) versus log(g); no extrapolation",
            "objective": "minimize the RMS of log(L_calc(kappa*g_ref)/L_ref)",
            "fit_coverage": (
                "The same reference points are retained for every trial kappa: each scaled "
                "coupling must remain inside the calculated curve's sampled range."
            ),
            "reported_residuals": "Both log-residual and ordinary relative-residual percentages are reported.",
        },
        "input_sha256": input_hashes,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "literal_blinov_scalar": literal,
        "production_mode_resolved_vector_control": mode_resolved,
        "fig4_boundary_cross_check": fig4_boundary_audit(comparison, literal),
        "interpretation": {
            "literal_reference": (
                "A mass-specific kappa improves the 10 MeV Fig. 7 pointwise curve, but the fitted "
                "10 MeV kappa worsens the already-close Fig. 4 contour boundaries. This is not a "
                "single coupling-normalization correction."
            ),
            "global_scale": (
                "One common near-unity kappa does not reconcile all Fig. 7 masses; the remaining "
                "10 MeV high-coupling tail dominates the residual."
            ),
            "mode_resolved_control": (
                "The exact_modes output is not a like-for-like scalar-opacity implementation of "
                "the literal Blinov Appendix-B prescription. Its rescaling failure is recorded as "
                "a diagnostic only, not as a stand-alone proof of a production-code error."
            ),
            "disposition": (
                "Do not apply fitted kappas to production scans or constraint figures. Keep PR #56 "
                "Draft until the physical origin of the 10 MeV shape mismatch is understood."
            ),
        },
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "outputs" / "rescaling_audit.json")
    args = parser.parse_args()
    report = run_audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "literal_global_kappa": report["literal_blinov_scalar"]["global_fit"]["kappa"],
        "literal_global_fit": report["literal_blinov_scalar"]["global_fit"]["metrics"],
        "literal_per_mass": {
            mass: data["best_fit"]
            for mass, data in report["literal_blinov_scalar"]["per_mass"].items()
        },
        "mode_resolved_global_fit": report["production_mode_resolved_vector_control"]["global_fit"],
        "fig4_boundary_cross_check": report["fig4_boundary_cross_check"],
        "output": str(args.output),
    }
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
