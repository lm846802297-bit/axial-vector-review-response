"""Compare the independent Blinov scalar scan with digitized Fig. 4 and Fig. 7.

Inputs are archived figure-path extractions; they are not author numerical tables.
This script does not import the production solver.
"""
import argparse
import csv
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_SCAN = HERE / "outputs" / "blinov_literal_scan.json"
DEFAULT_FIG4 = ROOT / "data" / "vector_reference" / "blinov_cooling_vertices.csv"
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"


def load_vertices(path):
    with Path(path).open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    return np.array([[float(row["mass_MeV"]), float(row["coupling"])]
                     for row in rows], dtype=float)


def contour_crossings(vertices, mass):
    """Log-log polyline intersections at fixed mass, without extrapolation."""
    x = np.log(vertices[:, 0])
    y = np.log(vertices[:, 1])
    target = np.log(mass)
    found = []
    for i in range(len(x) - 1):
        if min(x[i], x[i + 1]) <= target <= max(x[i], x[i + 1]) and x[i] != x[i + 1]:
            found.append(float(np.exp(y[i] + (target - x[i])
                                      * (y[i + 1] - y[i]) / (x[i + 1] - x[i]))))
    unique = []
    for value in sorted(found):
        if not unique or not np.isclose(value, unique[-1], rtol=1e-8, atol=0.0):
            unique.append(value)
    return unique


def cooling_intervals(couplings, luminosities, threshold):
    g = np.asarray(couplings, float)
    l = np.asarray(luminosities, float)
    x = np.log(g)
    y = np.log(np.maximum(l, 1e-300) / threshold)
    crossings = []
    for i in range(len(g) - 1):
        if y[i] * y[i + 1] < 0:
            crossings.append(float(np.exp(
                x[i] - y[i] * (x[i + 1] - x[i]) / (y[i + 1] - y[i]))))
    bounds = [float(g[0])] + crossings + [float(g[-1])]
    intervals = []
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        mid = np.sqrt(lo * hi)
        if np.interp(np.log(mid), x, y) > 0:
            intervals.append([lo, hi])
    return intervals


def log_interpolate(x, y, xnew):
    x, y, xnew = np.asarray(x), np.asarray(y), np.asarray(xnew)
    valid = np.isfinite(x) & np.isfinite(y) & (x > 0.0) & (y > 0.0)
    if np.count_nonzero(valid) < 2:
        raise ValueError("Need at least two positive finite scan samples for log interpolation")
    order = np.argsort(x[valid])
    return np.exp(np.interp(np.log(xnew), np.log(x[valid][order]),
                            np.log(y[valid][order])))


def compare(scan_path, fig4_path, fig7_path, threshold=4.4e52):
    scan = json.loads(Path(scan_path).read_text(encoding="utf-8"))
    fig4 = load_vertices(fig4_path)
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    fig7_points = fig7["reference_vertices"]
    results = {"threshold_erg_s": threshold, "fig4": [], "fig7": []}

    for row in scan["results"]:
        mass = float(row["mass_MeV"])
        calc = cooling_intervals(row["couplings"], row["luminosity_erg_s"], threshold)
        ref = contour_crossings(fig4, mass)
        entry = {"mass_MeV": mass, "reference_crossings": ref,
                 "calculated_intervals": calc}
        if len(ref) >= 2 and calc:
            calc_lower = min(interval[0] for interval in calc)
            calc_upper = max(interval[1] for interval in calc)
            entry.update({
                "calculated_lower": calc_lower,
                "calculated_upper": calc_upper,
                "relative_lower": calc_lower / ref[0] - 1.0,
                "relative_upper": calc_upper / ref[-1] - 1.0,
            })
        else:
            entry["comparison_status"] = "not enough contour crossings in scan window"
        results["fig4"].append(entry)

        key = str(float(mass))
        if key in fig7_points:
            points = fig7_points[key]
            calculated = log_interpolate(
                row["couplings"], row["luminosity_erg_s"], points["g"])
            relative = calculated / np.asarray(points["luminosity_erg_s"]) - 1.0
            results["fig7"].append({
                "mass_MeV": mass,
                "reference_points": len(relative),
                "max_abs_relative_difference": float(np.max(np.abs(relative))),
                "mean_abs_relative_difference": float(np.mean(np.abs(relative))),
                "points": [
                    {"g": float(g), "reference_erg_s": float(ref_l),
                     "calculated_erg_s": float(calc_l), "relative_difference": float(delta)}
                    for g, ref_l, calc_l, delta in zip(
                        points["g"], points["luminosity_erg_s"], calculated, relative)
                ],
            })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan", type=Path, default=DEFAULT_SCAN)
    parser.add_argument("--fig4", type=Path, default=DEFAULT_FIG4)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--threshold", type=float, default=4.4e52)
    parser.add_argument("--output", type=Path,
                        default=HERE / "outputs" / "fig4_fig7_comparison.json")
    args = parser.parse_args()
    result = compare(args.scan, args.fig4, args.fig7, args.threshold)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "fig4": result["fig4"],
        "fig7_summary": [
            {k: v for k, v in row.items() if k != "points"}
            for row in result["fig7"]
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
