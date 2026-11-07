#!/usr/bin/env python3
"""Compare baseline/high-resolution scalar scans and the independent vector audit."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def load(path):
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8"))


def interp_log(x, y, xnew):
    x, y, xnew = map(lambda a: np.asarray(a, float), (x, y, xnew))
    valid = (x > 0) & (y > 0) & np.isfinite(x) & np.isfinite(y)
    order = np.argsort(x[valid])
    return np.exp(np.interp(np.log(xnew), np.log(x[valid][order]),
                            np.log(y[valid][order])))


def compare(base_path, high_path, vector_path):
    base, high, vector = map(load, (base_path, high_path, vector_path))
    base_by_mass = {float(x["mass_MeV"]): x for x in base["results"]}
    high_by_mass = {float(x["mass_MeV"]): x for x in high["results"]}
    results = []
    for mass, hi in high_by_mass.items():
        lo = base_by_mass[mass]
        g_lo, g_hi = np.asarray(lo["couplings"]), np.asarray(hi["couplings"])
        if not np.array_equal(g_lo, g_hi):
            raise ValueError(f"Coupling grids differ at m={mass:g} MeV")
        l_lo = np.asarray(lo["luminosity_erg_s"])
        l_hi = np.asarray(hi["luminosity_erg_s"])
        delta = l_hi/l_lo - 1.0
        results.append({
            "mass_MeV": mass,
            "mean_abs_resolution_change": float(np.mean(np.abs(delta))),
            "max_abs_resolution_change": float(np.max(np.abs(delta))),
            "peak_coupling_baseline": float(g_lo[np.argmax(l_lo)]),
            "peak_coupling_high": float(g_hi[np.argmax(l_hi)]),
            "peak_luminosity_baseline": float(np.max(l_lo)),
            "peak_luminosity_high": float(np.max(l_hi)),
        })

    vector_rows = []
    for mass in high_by_mass:
        hi = high_by_mass[mass]
        rows = [x for x in vector["comparison"]
                if float(x["mass_MeV"]) == mass
                and x["variant"] == "blinov_literal"]
        if not rows:
            continue
        g = np.array([x["g"] for x in rows])
        ref_vector = np.array([x["calculated_erg_s"] for x in rows])
        high_at_points = interp_log(hi["couplings"], hi["luminosity_erg_s"], g)
        delta = high_at_points/ref_vector - 1.0
        vector_rows.append({
            "mass_MeV": mass,
            "mean_abs_reference_implementation_difference": float(np.mean(np.abs(delta))),
            "max_abs_reference_implementation_difference": float(np.max(np.abs(delta))),
        })

    return {
        "baseline_scan_sha256": hashlib.sha256(Path(base_path).read_bytes()).hexdigest(),
        "high_resolution_scan_sha256": hashlib.sha256(Path(high_path).read_bytes()).hexdigest(),
        "vector_audit_sha256": hashlib.sha256(Path(vector_path).read_bytes()).hexdigest(),
        "baseline_configuration": base["results"][0]["config"],
        "high_resolution_configuration": high["results"][0]["config"],
        "resolution_convergence": results,
        "independent_implementation_crosscheck": vector_rows,
        "interpretation": (
            "A convergence pass requires small changes between the two scalar "
            "resolutions. Agreement between the two scalar implementations is "
            "a separate check; neither result is promoted to a literature pass "
            "until the full Fig. 7 residual criteria are met."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--high", type=Path, required=True)
    parser.add_argument("--vector", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = compare(args.baseline, args.high, args.vector)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({
        "resolution_convergence": result["resolution_convergence"],
        "independent_implementation_crosscheck": result["independent_implementation_crosscheck"],
    }, indent=2))


if __name__ == "__main__":
    main()
