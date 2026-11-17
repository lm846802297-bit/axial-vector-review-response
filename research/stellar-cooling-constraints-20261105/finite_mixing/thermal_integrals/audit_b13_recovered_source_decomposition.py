#!/usr/bin/env python3
"""Decompose the recovered direct-midpoint B.13 source by radius, charge and mode.

This is a local-source diagnostic only. It does not calculate B.2 escape,
optical depth, neutrino inverse decay, or Fig. 7 luminosity.
"""
from __future__ import annotations
import argparse, csv, json, math
from bisect import bisect_right
from collections import defaultdict
from pathlib import Path

MASS_MEV = 10.0

def bracket(nodes, x, transform=lambda q: q):
    values = [transform(v) for v in nodes]
    xx = transform(x)
    i = max(0, min(bisect_right(values, xx) - 1, len(nodes) - 2))
    return nodes[i], nodes[i + 1]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    with args.csv.open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    grid = [r for r in rows if r["point_type"] == "grid_node"]
    mids = [r for r in rows if r["point_type"] == "cell_midpoint"]
    radii = sorted({float(r["radius_km"]) for r in grid})
    energies = sorted({float(r["omega_local_MeV"]) for r in grid})

    total = 0.0
    lapse_total = 0.0
    by_charge_mode = defaultdict(float)
    by_shell = defaultdict(float)
    by_shell_charge_mode = defaultdict(float)
    for row in mids:
        radius = float(row["radius_km"])
        omega = float(row["omega_local_MeV"])
        r0, r1 = bracket(radii, radius)
        e0, e1 = bracket(energies, omega,
                         lambda q: math.sqrt(max(q - MASS_MEV, 0.0)))
        measure = 4.0 * math.pi * radius**2 * (r1-r0) * (e1-e0)
        source = float(row["spectral_source_MeV5"])
        weight = measure * source
        key = (row["charge"], row["mode"])
        shell = f"{int(radius // 2)*2}-{int(radius // 2)*2+2} km"
        by_charge_mode[key] += weight
        by_shell[shell] += weight
        by_shell_charge_mode[(shell, *key)] += weight
        total += weight
        lapse_total += float(row["lapse"]) * weight

    result = {
        "status": "LOCAL_B13_SOURCE_DECOMPOSITION_ONLY_NOT_B2",
        "input_rows": len(rows),
        "grid_nodes": len(grid),
        "direct_midpoints": len(mids),
        "mass_MeV": MASS_MEV,
        "measure": "4*pi*r^2*Delta_r*Delta_omega times direct midpoint spectral_source",
        "direct_midpoint_source_integral_internal_units": total,
        "lapse_weighted_source_integral_internal_units": lapse_total,
        "lapse_weighted_over_unweighted": lapse_total / total,
        "charge_mode_contributions": {
            f"{q}/{mode}": {
                "integral": value, "fraction": value/total
            } for (q, mode), value in sorted(by_charge_mode.items())
        },
        "charge_contributions": {
            q: {
                "integral": sum(v for (qq, _), v in by_charge_mode.items() if qq == q),
                "fraction": sum(v for (qq, _), v in by_charge_mode.items() if qq == q)/total
            } for q in ("mu_minus", "mu_plus")
        },
        "mode_contributions": {
            mode: {
                "integral": sum(v for (_, mm), v in by_charge_mode.items() if mm == mode),
                "fraction": sum(v for (_, mm), v in by_charge_mode.items() if mm == mode)/total
            } for mode in ("L", "+", "-")
        },
        "radial_shell_contributions": {
            shell: {"integral": value, "fraction": value/total}
            for shell, value in sorted(by_shell.items(),
                key=lambda item: int(item[0].split("-")[0]))
        },
        "radial_shell_charge_mode_contributions": {
            f"{shell}/{q}/{mode}": {"integral": value, "fraction": value/total}
            for (shell, q, mode), value in sorted(by_shell_charge_mode.items())
        },
        "interpretation": [
            "The integral uses direct archived cell-midpoint spectral-source values, not interpolated values.",
            "The mu_minus/mu_plus and L,+,- channels are retained separately.",
            "This is a local B.13 semi-Compton source diagnostic; it excludes neutrino inverse decay, ray geometry, attenuation, and the complete GR transport measure.",
            "The mode fractions are source fractions, not escaped-luminosity fractions."
        ]
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
