#!/usr/bin/env python3
"""C4-C2 supplementary audit: outgoing-energy convergence inside the full-angle integral."""
from __future__ import annotations

import argparse
import csv
import json
import math
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel import INCIDENT_ENERGY
from audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support import (
    exact_outgoing_energy_support,
    integrate_outgoing_energy,
    load_c2_reference,
)

HERE = Path(__file__).resolve().parent
PROFILE_INDICES = (0, 96, 196, 300)
TARGETS = ("n", "p")
ANTINU_VALUES = (False, True)
COSINE_ORDER = 8
INITIAL_MOMENTUM_ORDER = 36
AZIMUTH_ORDER = 12
EPRIME_ORDERS = (48, 72)
SUPPORT_SCAN_POINTS = 10001


def integrate_full_angle_eprime_orders(
    target: str,
    antinu: bool,
    temperature: float,
    nu: float,
    mstar: float,
    *,
    support_scan_points: int = SUPPORT_SCAN_POINTS,
) -> tuple[dict[int, float], float]:
    """Integrate 2pi dcos(theta) dE' at two E' orders using identical exact supports."""
    cos_nodes, cos_weights = leggauss(COSINE_ORDER)
    totals = {order: 0.0 for order in EPRIME_ORDERS}
    max_root_residual = 0.0
    for costh, weight in zip(cos_nodes, cos_weights):
        lower, upper, _, root_residual = exact_outgoing_energy_support(
            INCIDENT_ENERGY,
            float(costh),
            mstar,
            temperature,
            nu,
            scan_points=support_scan_points,
        )
        max_root_residual = max(max_root_residual, root_residual)
        for order in EPRIME_ORDERS:
            value = integrate_outgoing_energy(
                lower,
                upper,
                INCIDENT_ENERGY,
                float(costh),
                target,
                antinu,
                temperature,
                nu,
                mstar,
                order_ep=order,
                order_p=INITIAL_MOMENTUM_ORDER,
                order_phi=AZIMUTH_ORDER,
            )
            totals[order] += float(weight) * value
    for order in EPRIME_ORDERS:
        totals[order] *= 2.0 * math.pi
    return totals, max_root_residual


def analyze(profile: list[dict[str, float]], c2: list[dict[str, float]], source_commit: str) -> tuple[list[dict], dict]:
    if len(profile) != 301 or len(c2) != 301:
        raise ValueError("C4-C2 Eprime convergence requires the exact 301-point C1/C2 profiles")
    rows = []
    for index in PROFILE_INDICES:
        state, occupation = profile[index], c2[index]
        if abs(state["r_km"] - occupation["r_km"]) > 1e-12:
            raise ValueError("C1/C2 radial mismatch")
        for target in TARGETS:
            for antinu in ANTINU_VALUES:
                totals, root_residual = integrate_full_angle_eprime_orders(
                    target,
                    antinu,
                    state["T_MeV"],
                    occupation[f"nu_{target}_EOS_MeV"],
                    state[f"mstar_{target}_MeV"],
                )
                rate48, rate72 = totals[48], totals[72]
                if not (rate48 > 0.0 and rate72 > 0.0):
                    raise ArithmeticError("non-positive full-angle EOS rate")
                rows.append({
                    "profile_index": index,
                    "r_km": state["r_km"],
                    "species": target,
                    "antinu": antinu,
                    "E_MeV": INCIDENT_ENERGY,
                    "T_MeV": state["T_MeV"],
                    "mstar_MeV": state[f"mstar_{target}_MeV"],
                    "nu_MeV": occupation[f"nu_{target}_EOS_MeV"],
                    "n_cos": COSINE_ORDER,
                    "n_p": INITIAL_MOMENTUM_ORDER,
                    "n_phi": AZIMUTH_ORDER,
                    "n_Eprime_48": 48,
                    "n_Eprime_72": 72,
                    "gamma_full_angle_Eprime48_MeV": rate48,
                    "gamma_full_angle_Eprime72_MeV": rate72,
                    "relative_48_to_72_difference": abs(rate72 / rate48 - 1.0),
                    "support_root_max_relative_residual": root_residual,
                })
    rows.sort(key=lambda row: (row["profile_index"], row["species"], row["antinu"]))
    max_difference = max(row["relative_48_to_72_difference"] for row in rows)
    max_root = max(row["support_root_max_relative_residual"] for row in rows)
    acceptance = {
        "all_16_radius_species_sign_cases_present": len(rows) == 16,
        "all_full_angle_rates_positive": all(
            row["gamma_full_angle_Eprime48_MeV"] > 0.0
            and row["gamma_full_angle_Eprime72_MeV"] > 0.0
            for row in rows
        ),
        "Eprime_48_to_72_below_1_percent": max_difference < 1e-2,
        "support_root_below_1e_7": max_root < 1e-7,
    }
    summary = {
        "title": "C4-C2 full-angle outgoing-energy quadrature convergence",
        "source_commit": source_commit,
        "input_profile_git_blob_sha": "9ff7818b0679992c0a9ba402330ec7f0d1f3041b",
        "input_c2_git_blob_sha": "c472040a4551e68ffadbf7addf9402663f99e7e3",
        "profile_indices": list(PROFILE_INDICES),
        "radii_km": [profile[index]["r_km"] for index in PROFILE_INDICES],
        "cases": len(rows),
        "incident_energy_MeV": INCIDENT_ENERGY,
        "quadrature": {
            "cosine": COSINE_ORDER,
            "initial_momentum": INITIAL_MOMENTUM_ORDER,
            "azimuth": AZIMUTH_ORDER,
            "outgoing_energy_orders": list(EPRIME_ORDERS),
            "support_scan_points": SUPPORT_SCAN_POINTS,
        },
        "maxima": {
            "full_angle_Eprime_48_to_72_relative_difference": max_difference,
            "support_root_relative_residual": max_root,
        },
        "acceptance": acceptance,
        "overall_pass": all(acceptance.values()),
        "interpretation": (
            "The 48-versus-72 outgoing-energy comparison is performed inside the full "
            "outgoing-angle integral. At each angular node the exact kinematic support "
            "roots are solved once and reused for both energy orders. The existing "
            "C4-C2 collision kernel and C1/C2 EOS inputs are reused unchanged."
        ),
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C4-C2 full-angle Eprime convergence failed: {acceptance}")
    return rows, summary


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=HERE / "outputs" / "caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv")
    parser.add_argument("--c2-reference", type=Path, default=HERE / "outputs" / "p1iii_eos_full_radial_occupation_2026-11-11.csv")
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    parser.add_argument("--source-commit", default=os.environ.get("GITHUB_SHA", "local"))
    args = parser.parse_args()
    profile = load_profile(args.profile)
    c2 = load_c2_reference(args.c2_reference)
    rows, summary = analyze(profile, c2, args.source_commit)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    write_csv(args.output_csv, rows)
    print(json.dumps({"overall_pass": summary["overall_pass"], "maxima": summary["maxima"], "acceptance": summary["acceptance"]}, indent=2))


if __name__ == "__main__":
    main()
