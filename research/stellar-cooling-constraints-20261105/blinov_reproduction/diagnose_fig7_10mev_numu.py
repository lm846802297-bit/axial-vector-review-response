"""One-factor diagnostic for the unresolved 10 MeV Blinov Fig. 7 tail.

Scales only the reconstructed muon-neutrino chemical-potential profile. For each
scale, the same modified profile is used consistently in production and inverse
absorption through detailed balance. This is a sensitivity diagnostic, not a
proposal to replace the baseline profile or tune it to the figure.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import tempfile
from pathlib import Path

import numpy as np

try:
    from .reference import evaluate_mass
except ImportError:  # direct script execution from this directory
    from reference import evaluate_mass

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "fig7_10mev_numu_sensitivity.json"


def read_profile(path: Path):
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.reader(stream)
        header = next(reader)
        rows = np.asarray([[float(x) for x in row] for row in reader], dtype=float)
    if "mu_numu_MeV" not in header:
        raise ValueError("Profile is missing mu_numu_MeV")
    return header, rows


def write_scaled_profile(source: Path, destination: Path, scale: float):
    """Write a temporary profile changing only mu_numu_MeV by scale."""
    if scale < 0:
        raise ValueError("Scale must be non-negative")
    header, rows = read_profile(source)
    column = header.index("mu_numu_MeV")
    rows[:, column] *= scale
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(header)
        writer.writerows([[f"{x:.12g}" for x in row] for row in rows])


def run(profile: Path, fig7_path: Path, scales=(0.0, 0.5, 1.0, 1.5),
        radial_order=40, energy_order=100, angular_order=16, path_order=32):
    fig7 = json.loads(fig7_path.read_text(encoding="utf-8"))
    points = fig7["reference_vertices"]["10.0"]
    couplings = np.asarray(points["g"], dtype=float)
    reference_luminosity = np.asarray(points["luminosity_erg_s"], dtype=float)

    output = {
        "purpose": "diagnose 10 MeV Fig. 7 residual sensitivity to reconstructed mu_numu profile",
        "baseline_is_scale_1": True,
        "interpretation": (
            "Each scale changes the same mu_numu(r) input in both neutrino-pair "
            "production and inverse-decay absorption. This is not a physical "
            "profile uncertainty distribution and no scale is selected by fit."
        ),
        "mass_MeV": 10.0,
        "threshold_erg_s": 4.4e52,
        "quadrature": {
            "radial_order": radial_order, "energy_order": energy_order,
            "angular_order": angular_order, "path_order": path_order,
        },
        "profile_sha256": hashlib.sha256(profile.read_bytes()).hexdigest(),
        "fig7_source_sha256": hashlib.sha256(fig7_path.read_bytes()).hexdigest(),
        "fig7_pdf_sha256": fig7.get("pdf_sha256"),
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "scales": [],
    }

    with tempfile.TemporaryDirectory(prefix="blinov_numu_") as temp:
        for scale in scales:
            varied_profile = Path(temp) / f"profile_numu_scale_{scale:g}.csv"
            write_scaled_profile(profile, varied_profile, float(scale))
            scan = evaluate_mass(
                10.0, varied_profile, couplings,
                radial_order, energy_order, angular_order, path_order,
                25.0, 1000.0,
            )
            calculated = np.asarray(scan["luminosity_erg_s"], dtype=float)
            relative = calculated / reference_luminosity - 1.0
            output["scales"].append({
                "mu_numu_scale": float(scale),
                "thin_luminosity_erg_s": scan["thin_luminosity_erg_s"],
                "max_abs_relative_difference": float(np.max(np.abs(relative))),
                "mean_abs_relative_difference": float(np.mean(np.abs(relative))),
                "relative_difference_low_coupling": float(relative[0]),
                "relative_difference_peak_reference": float(relative[int(np.argmax(reference_luminosity))]),
                "relative_difference_high_coupling": float(relative[-1]),
                "points": [
                    {"g": float(g), "reference_erg_s": float(ref),
                     "calculated_erg_s": float(calc), "relative_difference": float(delta)}
                    for g, ref, calc, delta in zip(
                        couplings, reference_luminosity, calculated, relative)
                ],
            })
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--scales", default="0,0.5,1,1.5")
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--na", type=int, default=16)
    parser.add_argument("--ns", type=int, default=32)
    args = parser.parse_args()
    scales = tuple(float(x) for x in args.scales.split(","))
    result = run(args.profile, args.fig7, scales, args.nr, args.ne, args.na, args.ns)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([
        {k: row[k] for k in (
            "mu_numu_scale", "thin_luminosity_erg_s",
            "max_abs_relative_difference", "mean_abs_relative_difference",
            "relative_difference_low_coupling",
            "relative_difference_peak_reference",
            "relative_difference_high_coupling",
        )}
        for row in result["scales"]
    ], indent=2))


if __name__ == "__main__":
    main()
