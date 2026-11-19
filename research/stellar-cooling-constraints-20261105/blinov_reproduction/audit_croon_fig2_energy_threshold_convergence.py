#!/usr/bin/env python3
"""Audit low-energy quadrature convergence in the Croon Fig. 2 transport integral.

The 0.1 eV--10 eV curves are particularly sensitive to the outer vacuum-decay
opacity because tau_out is proportional to m_V^2/omega.  This audit compares
the same two-flavour L_mu-L_tau calculation at successively higher Gauss
orders, separately for R_far=100 km and R_far=R_nu.  It does not tune any
normalization to the published plot.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from croon_fig2_literal_transport import (
    DEFAULT_PROFILE,
    R_FAR_KM,
    CROON_MASSES_MEV,
    load_and_sample_profile,
    luminosity_curve,
    muon_susceptibility,
)

ORDERS = (160, 320, 640, 1280, 2560)
MASS_LABELS = ("0.1 eV", "1 eV", "10 eV")
COUPLINGS = np.asarray(
    (1.0e-4, 3.0e-4, 6.0e-4, 7.5e-4, 1.0e-3,
     3.0e-3, 1.0e-2, 3.0e-2, 1.0e-1, 3.0e-1, 1.0),
    dtype=float,
)


def relative_change(previous: np.ndarray, current: np.ndarray) -> np.ndarray:
    """Symmetric relative change, robust when a luminosity underflows to zero."""
    previous = np.asarray(previous, dtype=float)
    current = np.asarray(current, dtype=float)
    scale = np.maximum(np.maximum(np.abs(previous), np.abs(current)), 1.0e-300)
    result = np.abs(current - previous) / scale
    result[(previous == 0.0) & (current == 0.0)] = 0.0
    return result


def run_audit(
    profile_path: str | Path = DEFAULT_PROFILE,
    radial_step_km: float = 0.05,
    orders: tuple[int, ...] = ORDERS,
) -> dict:
    profile = load_and_sample_profile(profile_path, radial_step_km)
    profile["muon_susceptibility_mev3"] = muon_susceptibility(
        profile["temperature_mev"],
        profile["muon_chemical_potential_mev"],
        order=256,
    )
    rnu = float(profile["rnu_km"])
    rfar_cases = {"R_far_100_km": R_FAR_KM, "R_far_Rnu": rnu}

    curves: dict[str, dict] = {}
    rows: list[dict] = []
    convergence: dict[str, dict] = {}

    for label in MASS_LABELS:
        mass = float(CROON_MASSES_MEV[label])
        curves[label] = {}
        convergence[label] = {}
        for rfar_label, rfar in rfar_cases.items():
            curves[label][rfar_label] = {}
            convergence[label][rfar_label] = {}
            previous = None
            for order in orders:
                luminosity = luminosity_curve(
                    mass, COUPLINGS, profile,
                    rfar_km=float(rfar), energy_order=int(order)
                )
                curves[label][rfar_label][str(order)] = luminosity.tolist()
                for coupling, value in zip(COUPLINGS, luminosity):
                    rows.append({
                        "mass_label": label,
                        "mass_mev": mass,
                        "R_far_case": rfar_label,
                        "R_far_km": float(rfar),
                        "energy_order": int(order),
                        "g_X": float(coupling),
                        "L_erg_s": float(value),
                    })
                if previous is not None:
                    delta = relative_change(previous, luminosity)
                    convergence[label][rfar_label][f"{orders[orders.index(order)-1]}->{order}"] = {
                        "max_relative_change": float(np.max(delta)),
                        "median_relative_change": float(np.median(delta)),
                        "max_relative_change_percent": float(100.0*np.max(delta)),
                    }
                previous = luminosity

    final_order_pair = f"{orders[-2]}->{orders[-1]}"
    final_max = max(
        convergence[mass][case][final_order_pair]["max_relative_change"]
        for mass in MASS_LABELS for case in rfar_cases
    )
    return {
        "status": "energy_threshold_convergence_audit",
        "source_paper": "Croon et al., JHEP 01 (2021) 107, arXiv:2006.13942",
        "model": "gauged U(1)_{L_mu-L_tau}; two neutrino flavours in source and opacity",
        "profile": {
            "path": profile["profile_path"],
            "sha256": profile["profile_sha256"],
            "source_rows": int(profile["profile_source_rows"]),
            "radial_grid_points": int(len(profile["r_km"])),
            "radial_step_km": float(profile["radial_step_km"]),
            "R_nu_km": rnu,
        },
        "numerics": {
            "energy_orders": list(map(int, orders)),
            "momentum_order": 256,
            "couplings": COUPLINGS.tolist(),
            "R_far_cases_km": {key: float(value) for key, value in rfar_cases.items()},
            "energy_map": "omega = m + Tmax*y^2, y in [0,6]",
            "convergence_threshold": 1.0e-3,
            "final_pair": final_order_pair,
            "final_pair_max_relative_change": float(final_max),
            "final_pair_converged_below_0p1_percent": bool(final_max < 1.0e-3),
        },
        "convergence": convergence,
        "curves": curves,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--radial-step-km", type=float, default=0.05)
    parser.add_argument("--orders", type=int, nargs="+", default=list(ORDERS))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/croon_fig2_energy_threshold_convergence"))
    args = parser.parse_args()

    result = run_audit(args.profile, args.radial_step_km, tuple(args.orders))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "croon_fig2_energy_threshold_convergence.json"
    csv_path = args.output_dir / "croon_fig2_energy_threshold_convergence.csv"
    json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(result["rows"][0]))
        writer.writeheader()
        writer.writerows(result["rows"])
    print(json.dumps({
        "json": str(json_path),
        "csv": str(csv_path),
        "final_pair": result["numerics"]["final_pair"],
        "final_pair_max_relative_change": result["numerics"]["final_pair_max_relative_change"],
        "converged_below_0p1_percent": result["numerics"]["final_pair_converged_below_0p1_percent"],
    }, indent=2))


if __name__ == "__main__":
    main()
