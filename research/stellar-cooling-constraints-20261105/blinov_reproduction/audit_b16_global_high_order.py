"""High-order, independently gridded B.16 reproduction of published Fig. 7.

The Compton kernel is the published non-relativistic-muon/no-recoil
prescription, Eqs. (B.14)--(B.19). The B.1 source radial grid is evaluated
separately from the fixed B.2 opacity interpolation grid.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

try:
    from .audit_b16_global_redshift import (
        DEFAULT_FIG7, DEFAULT_PROFILE, run_mass, sha256,
    )
except ImportError:
    from audit_b16_global_redshift import (
        DEFAULT_FIG7, DEFAULT_PROFILE, run_mass, sha256,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mass", type=float, required=True)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--nr", type=int, default=200)
    parser.add_argument("--ne", type=int, default=200)
    parser.add_argument("--na", type=int, default=32)
    parser.add_argument("--ns", type=int, default=64)
    parser.add_argument("--opacity-order", type=int, default=640)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()

    result = run_mass(
        args.mass, args.profile, args.fig7,
        args.nr, args.ne, args.na, args.ns,
        args.radius, args.energy_offset,
        opacity_order=args.opacity_order,
        separate_source_grid=True,
    )
    config = result["configuration"]
    if config["source_grid_mode"] != "independent":
        raise ArithmeticError("B.1 source grid is not independent of B.2 opacity grid")
    if config["radial_order"] != args.nr:
        raise ArithmeticError("Unexpected source radial order")
    if config["opacity_order"] != args.opacity_order:
        raise ArithmeticError("Unexpected opacity order")
    if config["opacity_radial_node_count"] != args.opacity_order + 2:
        raise ArithmeticError("Opacity grid node count does not match fixed order plus endpoints")
    if config["energy_order"] != args.ne:
        raise ArithmeticError("Unexpected base energy order")
    if config["angular_order"] != args.na or config["path_order"] != args.ns:
        raise ArithmeticError("Unexpected angular/path quadrature orders")

    payload = {
        "title": "High-order independently gridded B.16 global vector luminosity",
        "paper_reference": {
            "citation": "Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619",
            "doi": "10.1007/JHEP06(2026)155",
            "figure": "Fig. 7",
            "compton_method": "Non-relativistic-muon/no-recoil Eqs. (B.14)--(B.19)",
            "transport_method": "Eq. (B.1) source integral and fixed-omega Eq. (B.2) baseline",
        },
        "profile_provenance_warning": (
            "The radial profile is reconstructed from public figure paths; "
            "it is not the original s18.8-SFHo-MUONS simulation table."
        ),
        "quadratures": {
            "source_radial_order": args.nr,
            "opacity_order": args.opacity_order,
            "base_energy_order": args.ne,
            "angular_order": args.na,
            "path_order": args.ns,
            "radius_km": args.radius,
            "energy_offset_MeV": args.energy_offset,
        },
        "grid_identity": {
            "source_grid_mode": config["source_grid_mode"],
            "source_radial_node_count": config["source_radial_node_count"],
            "source_grid_sha256": config["source_grid_sha256"],
            "opacity_radial_node_count": config["opacity_radial_node_count"],
            "opacity_grid_sha256": config["opacity_grid_sha256"],
            "energy_node_count": config["energy_node_count"],
            "energy_grid_sha256": config["energy_grid_sha256"],
        },
        "profile_sha256": sha256(args.profile),
        "fig7_digitization_sha256": sha256(args.fig7),
        "result": result,
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print(json.dumps({
        "mass_MeV": result["mass_MeV"],
        "profile_sha256": payload["profile_sha256"],
        "grid_identity": payload["grid_identity"],
        "fixed_omega_metrics": result["eq_b2_fixed_omega_baseline"]["curve_metrics"],
        "path_redshift_metrics": result["path_redshift_only_diagnostic"]["curve_metrics"],
        "mean_abs_path_redshift_shift": result["path_redshift_only_diagnostic"]["mean_absolute_luminosity_shift_vs_fixed"],
        "max_abs_path_redshift_shift": result["path_redshift_only_diagnostic"]["maximum_absolute_luminosity_shift_vs_fixed"],
        "output": str(args.output),
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
