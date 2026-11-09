#!/usr/bin/env python3
"""Compare Caputo and Ferreira SFHo-18.8 muon chemical-potential reconstructions.

This is a profile-provenance audit only. It does not modify rates, transport,
luminosity, or the production axial-vector output.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "outputs" / "caputo_ferreira_mu_mu_5_15km_2026-11-10.json"
M_MU_MEV = 105.6583755
SAMPLE_RADII_KM = (0, 5, 8, 10, 12, 12.5, 13, 14, 15, 20)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def interpolate(rows, key: str, radius: float) -> float:
    x = [row["r_km"] for row in rows]
    if radius <= x[0]:
        return rows[0][key]
    if radius >= x[-1]:
        return rows[-1][key]
    lo, hi = 0, len(rows) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if x[mid] <= radius:
            lo = mid
        else:
            hi = mid
    fraction = (radius - x[lo]) / (x[hi] - x[lo])
    return rows[lo][key] * (1.0 - fraction) + rows[hi][key] * fraction


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    with args.input.open(newline="", encoding="utf-8") as stream:
        rows = [{key: float(value) for key, value in row.items()}
                for row in csv.DictReader(stream)]

    window = [row for row in rows if 5.0 <= row["r_km"] <= 15.0]
    relative_eta = []
    eta_ratios = []
    relative_temperature = []
    for row in window:
        eta_caputo = row["mu_mu_MeV"] / row["T_MeV"]
        eta_ferreira = row["mu_mu_Ferreira_MeV"] / row["T_Ferreira_MeV"]
        relative_eta.append(abs(eta_ferreira / eta_caputo - 1.0))
        eta_ratios.append(eta_ferreira / eta_caputo)
        relative_temperature.append(abs(row["T_Ferreira_MeV"] / row["T_MeV"] - 1.0))

    samples = []
    for radius in SAMPLE_RADII_KM:
        tc = interpolate(rows, "T_MeV", radius)
        tf = interpolate(rows, "T_Ferreira_MeV", radius)
        mc = interpolate(rows, "mu_mu_MeV", radius)
        mf = interpolate(rows, "mu_mu_Ferreira_MeV", radius)
        samples.append({
            "r_km": radius,
            "T_caputo_MeV": tc,
            "T_ferreira_MeV": tf,
            "mu_mu_caputo_MeV": mc,
            "mu_mu_ferreira_MeV": mf,
            "eta_caputo": mc / tc,
            "eta_ferreira": mf / tf,
            "eta_ratio_ferreira_over_caputo": (mf / tf) / (mc / tc),
            "delta_mu_MeV": mf - mc,
            "delta_mu_after_subtracting_mmu_MeV": mf - mc - M_MU_MEV,
        })

    result = {
        "title": "Caputo versus Ferreira SFHo-18.8 muon chemical-potential profile comparison",
        "status": "profile_provenance_diagnostic_only",
        "input_csv": str(args.input.resolve().relative_to(ROOT.parent.parent.resolve())) if args.input.resolve().is_relative_to(ROOT.parent.parent.resolve()) else str(args.input),
        "input_sha256": sha256(args.input),
        "radial_window_km": [5.0, 15.0],
        "n_profile_nodes_inclusive": len(window),
        "statistics": {
            "eta_relative_difference_mean": sum(relative_eta) / len(relative_eta),
            "eta_relative_difference_median": median(relative_eta),
            "eta_relative_difference_max": max(relative_eta),
            "eta_ratio_min": min(eta_ratios),
            "eta_ratio_max": max(eta_ratios),
            "temperature_relative_difference_mean": sum(relative_temperature) / len(relative_temperature),
            "temperature_relative_difference_max": max(relative_temperature),
        },
        "samples": samples,
        "interpretation": [
            "The temperature profiles agree closely; the large discrepancy is specific to mu_mu.",
            "The mu_mu difference is radius-dependent and is not a constant additive rest-mass shift.",
            "This compares the two published reconstructions; it is not a direct full-5-to-15-km vector residual against Bollig Fig. 4.",
            "No source, opacity, transport, luminosity, or axial-vector output is changed.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
