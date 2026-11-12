#!/usr/bin/env python3
"""C4-C1: exact outgoing-neutrino energy support and E' completeness."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel import (
    INCIDENT_ENERGY,
    COS_THETA,
    HBARC,
    MASS,
    N0,
    TAIL_T,
    differential_rate_eos,
    legacy,
    pmax_eos,
)

HERE = Path(__file__).resolve().parent
EXPECTED_C2_GIT_BLOB_SHA = "c472040a4551e68ffadbf7addf9402663f99e7e3"
PROFILE_INDICES = (0, 96, 196, 300)
SPECIES = ("n", "p")
ANTINU_VALUES = (False, True)
EPRIME_ORDERS = (32, 48, 72)
MOMENTUM_ORDER = 48
AZIMUTH_ORDER = 16
SUPPORT_SCAN_POINTS = 2001
LOCAL_WINDOW_HALF_WIDTH = 60.0
COLD_BARYON_DENSITY_OVER_N0 = 1e-10
COLD_PROTON_FRACTION = 0.10
COLD_TEMPERATURE = 1e-3


def load_c2_reference(path: Path) -> list[dict[str, float]]:
    data = path.read_bytes()
    digest = hashlib.sha1(f"blob {len(data)}\0".encode("ascii")+data).hexdigest()
    if digest != EXPECTED_C2_GIT_BLOB_SHA:
        raise ValueError(f"C2 occupation CSV Git blob SHA mismatch: {digest}")
    with path.open("r", newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 301:
        raise ValueError(f"expected 301 C2 rows, found {len(rows)}")
    return [{key: float(value) for key, value in row.items()} for row in rows]


def support_function(
    outgoing_energy: float,
    incident_energy: float,
    cos_theta: float,
    mstar: float,
    pmax: float,
) -> float:
    if outgoing_energy <= 0.0:
        return math.inf
    q0 = incident_energy-outgoing_energy
    q2 = (
        incident_energy*incident_energy
        +outgoing_energy*outgoing_energy
        -2.0*incident_energy*outgoing_energy*cos_theta
    )
    q = math.sqrt(max(q2, 0.0))
    if q <= abs(q0) or q <= 0.0:
        return math.inf
    pmin = legacy.pmin_rel(q0, q, mstar)
    return pmin-pmax


def exact_outgoing_energy_support(
    incident_energy: float,
    cos_theta: float,
    mstar: float,
    temperature: float,
    nu: float,
    *,
    scan_points: int = SUPPORT_SCAN_POINTS,
) -> tuple[float, float, float, float]:
    """Solve p_min(E')=p_max at both support boundaries.

    p_max is defined by a 45 T kinetic-energy tail. The returned interval is
    the complete E' support under that explicitly stated numerical cutoff.
    """
    pmax = pmax_eos(mstar, nu, temperature)
    kinetic_cut = max(nu, 0.0)+TAIL_T*temperature
    upper_energy = incident_energy+kinetic_cut
    grid = np.linspace(1e-7, upper_energy, scan_points)
    values = np.asarray([
        support_function(float(ep), incident_energy, cos_theta, mstar, pmax)
        for ep in grid
    ])
    finite = np.isfinite(values)
    if not np.any(finite & (values < 0.0)):
        raise ArithmeticError("no outgoing-energy support found")
    crossings = []
    for index in range(len(grid)-1):
        left, right = values[index], values[index+1]
        if not (math.isfinite(left) and math.isfinite(right)):
            continue
        if left == 0.0:
            crossings.append(float(grid[index]))
        elif left*right < 0.0:
            root = brentq(
                lambda ep: support_function(
                    ep, incident_energy, cos_theta, mstar, pmax
                ),
                float(grid[index]), float(grid[index+1]),
                xtol=2e-12, rtol=2e-13,
            )
            crossings.append(float(root))
    if len(crossings) != 2:
        raise ArithmeticError(
            f"expected one connected E' support interval, found {len(crossings)} roots"
        )
    lower, upper = crossings
    if not (0.0 < lower < upper <= upper_energy*(1.0+1e-12)):
        raise ArithmeticError(f"invalid E' support [{lower}, {upper}]")
    midpoint = 0.5*(lower+upper)
    if support_function(midpoint, incident_energy, cos_theta, mstar, pmax) >= 0.0:
        raise ArithmeticError("the interval between support roots is not allowed")
    residuals = (
        abs(support_function(lower, incident_energy, cos_theta, mstar, pmax))/pmax,
        abs(support_function(upper, incident_energy, cos_theta, mstar, pmax))/pmax,
    )
    return lower, upper, pmax, max(residuals)


def integrate_outgoing_energy(
    lower: float,
    upper: float,
    incident_energy: float,
    cos_theta: float,
    target: str,
    antinu: bool,
    temperature: float,
    nu: float,
    mstar: float,
    *,
    order_ep: int,
    order_p: int = MOMENTUM_ORDER,
    order_phi: int = AZIMUTH_ORDER,
) -> float:
    if upper <= lower:
        return 0.0
    x, w = leggauss(order_ep)
    outgoing = 0.5*(upper-lower)*(x+1.0)+lower
    weights = 0.5*(upper-lower)*w
    values = [
        differential_rate_eos(
            incident_energy, float(ep), cos_theta, target, antinu,
            temperature, nu, mstar,
            order_p=order_p, order_phi=order_phi,
        )
        for ep in outgoing
    ]
    return float(np.dot(weights, values))


def _local_cases(
    profile: list[dict[str, float]],
    c2: list[dict[str, float]],
) -> tuple[list[dict], list[dict]]:
    local_records, support_records = [], []
    for index in PROFILE_INDICES:
        row, occupation = profile[index], c2[index]
        if abs(row["r_km"]-occupation["r_km"]) > 1e-12:
            raise ValueError("C1/C2 radial mismatch")
        for target in SPECIES:
            mstar = row[f"mstar_{target}_MeV"]
            temperature = row["T_MeV"]
            nu = occupation[f"nu_{target}_EOS_MeV"]
            nprime_fm3 = occupation[f"nprime_{target}_fm3"]
            xi = row["xi_SPP"]
            lower, upper, pmax, root_residual = exact_outgoing_energy_support(
                INCIDENT_ENERGY, COS_THETA, mstar, temperature, nu
            )
            stationary_center = (
                INCIDENT_ENERGY
                /(1.0+INCIDENT_ENERGY/mstar*(1.0-COS_THETA))
            )
            window_lower = max(lower, stationary_center-LOCAL_WINDOW_HALF_WIDTH)
            window_upper = min(upper, stationary_center+LOCAL_WINDOW_HALF_WIDTH)
            if window_upper <= window_lower:
                raise ArithmeticError("the legacy 60 MeV window misses the allowed support")
            support_records.append({
                "r_km": row["r_km"],
                "species": target,
                "mstar_MeV": mstar,
                "T_MeV": temperature,
                "nu_MeV": nu,
                "pmax_MeV": pmax,
                "Eprime_support_min_MeV": lower,
                "Eprime_support_max_MeV": upper,
                "Eprime_support_width_MeV": upper-lower,
                "support_root_max_relative_residual": root_residual,
            })
            nprime_mev3 = nprime_fm3*HBARC**3
            for antinu in ANTINU_VALUES:
                full_rates = {
                    order: integrate_outgoing_energy(
                        lower, upper, INCIDENT_ENERGY, COS_THETA,
                        target, antinu, temperature, nu, mstar,
                        order_ep=order,
                    )
                    for order in EPRIME_ORDERS
                }
                window_rate = integrate_outgoing_energy(
                    window_lower, window_upper, INCIDENT_ENERGY, COS_THETA,
                    target, antinu, temperature, nu, mstar,
                    order_ep=EPRIME_ORDERS[-1],
                )
                full = full_rates[EPRIME_ORDERS[-1]]
                if full <= 0.0:
                    raise ArithmeticError("non-positive full-support local rate")
                local_records.append({
                    "r_km": row["r_km"],
                    "species": target,
                    "antinu": antinu,
                    "E_MeV": INCIDENT_ENERGY,
                    "cos_theta": COS_THETA,
                    "T_MeV": temperature,
                    "mstar_MeV": mstar,
                    "nu_MeV": nu,
                    "eta_nu_over_T": nu/temperature,
                    "theta_T_over_mstar": temperature/mstar,
                    "X_free": row[f"X_{target}"],
                    "xi_SPP": xi,
                    "nprime_fm3": nprime_fm3,
                    "Eprime_support_min_MeV": lower,
                    "Eprime_support_max_MeV": upper,
                    "Eprime_support_width_MeV": upper-lower,
                    "Eprime_window_min_MeV": window_lower,
                    "Eprime_window_max_MeV": window_upper,
                    "gamma_full_order32": full_rates[32],
                    "gamma_full_order48": full_rates[48],
                    "gamma_full_order72": full,
                    "relative_convergence_32_to_72": abs(full/full_rates[32]-1.0),
                    "relative_convergence_48_to_72": abs(full/full_rates[48]-1.0),
                    "gamma_legacy_60MeV_window": window_rate,
                    "legacy_window_fraction_of_full_support": window_rate/full,
                    "sigma_full_support_per_target_MeV_minus2": full/nprime_mev3,
                    "xi_times_gamma_full_support": xi*full,
                })
    return local_records, support_records

def _cold_horowitz_cases() -> list[dict]:
    records = []
    for target in SPECIES:
        for antinu in ANTINU_VALUES:
            n_b = COLD_BARYON_DENSITY_OVER_N0*N0
            fraction = (
                1.0-COLD_PROTON_FRACTION
                if target == "n" else COLD_PROTON_FRACTION
            )
            n_species = fraction*n_b
            mass = MASS[target]
            mu = legacy.solve_mu(n_species, mass, COLD_TEMPERATURE)
            nu = mu-mass
            lower, upper, pmax, root_residual = exact_outgoing_energy_support(
                INCIDENT_ENERGY, COS_THETA, mass, COLD_TEMPERATURE, nu
            )
            full = integrate_outgoing_energy(
                lower, upper, INCIDENT_ENERGY, COS_THETA,
                target, antinu, COLD_TEMPERATURE, nu, mass,
                order_ep=96, order_p=48, order_phi=16,
            )
            stationary = legacy.kernel.evaluate(
                INCIDENT_ENERGY, COS_THETA, target, antinu
            )["dsdo"]
            ratio = full/(n_species*HBARC**3)/stationary
            records.append({
                "species": target,
                "antinu": antinu,
                "nB_over_n0": COLD_BARYON_DENSITY_OVER_N0,
                "T_MeV": COLD_TEMPERATURE,
                "Eprime_support_min_MeV": lower,
                "Eprime_support_max_MeV": upper,
                "Eprime_support_width_MeV": upper-lower,
                "pmax_MeV": pmax,
                "support_root_max_relative_residual": root_residual,
                "ratio_to_Horowitz_dsigma_dOmega": ratio,
                "relative_Horowitz_residual": ratio-1.0,
            })
    return records


def analyze(
    profile: list[dict[str, float]],
    c2: list[dict[str, float]],
) -> tuple[list[dict], list[dict], list[dict], dict]:
    if len(profile) != 301 or len(c2) != 301:
        raise ValueError("C4-C1 requires the 301-point C1/C2 profile")
    local, support = _local_cases(profile, c2)
    cold = _cold_horowitz_cases()
    max_root = max(row["support_root_max_relative_residual"] for row in support+cold)
    max_horowitz = max(abs(row["relative_Horowitz_residual"]) for row in cold)
    max_convergence_48 = max(row["relative_convergence_48_to_72"] for row in local)
    max_convergence_32 = max(row["relative_convergence_32_to_72"] for row in local)
    min_window_fraction = min(row["legacy_window_fraction_of_full_support"] for row in local)
    max_window_fraction = max(row["legacy_window_fraction_of_full_support"] for row in local)
    acceptance = {
        "sixteen_local_EOS_cases": bool(len(local) == 16),
        "eight_unique_support_intervals": bool(len(support) == 8),
        "four_cold_Horowitz_cases": bool(len(cold) == 4),
        "support_roots_relative_residual_below_1e_7": bool(max_root < 1e-7),
        "cold_dilute_full_support_Horowitz_below_1e_3": bool(max_horowitz < 1e-3),
        "full_Eprime_quadrature_48_to_72_below_1_percent": bool(max_convergence_48 < 1e-2),
        "full_Eprime_quadrature_32_to_72_below_2_percent": bool(max_convergence_32 < 2e-2),
        "window_fraction_in_unit_interval": bool(
            min_window_fraction >= 0.0 and max_window_fraction <= 1.0+1e-8
        ),
        "all_full_support_rates_positive": bool(
            all(row["gamma_full_order72"] > 0.0 for row in local)
        ),
    }
    summary = {
        "title": "P1-IIIe-C4C1 exact outgoing-neutrino energy support",
        "date": "2026-11-11",
        "status": "PASS: exact pmin/pmax support, full Eprime quadrature, and cold Horowitz limit",
        "scope": (
            "Local EOS differential-in-angle collision kernel at four selected radii; "
            "full outgoing-energy support at fixed E=100 MeV and cos(theta)=-0.5; "
            "not integrated over outgoing angle or radius."
        ),
        "provenance": {
            "selected_profile_indices_zero_based": list(PROFILE_INDICES),
            "selected_radii_km": [profile[i]["r_km"] for i in PROFILE_INDICES],
            "species": list(SPECIES),
            "neutrino_antineutrino": ["nu", "antinu"],
            "incident_energy_MeV": INCIDENT_ENERGY,
            "cos_theta": COS_THETA,
            "local_cases": len(local),
            "cold_Horowitz_cases": len(cold),
            "C2_occupation_git_blob_sha": EXPECTED_C2_GIT_BLOB_SHA,
        },
        "support_definition": {
            "condition": "p_min(q0(Eprime),q(Eprime);mstar) <= p_max(mstar,nu,T)",
            "pmax_kinetic_tail": f"max(nu,0)+{TAIL_T}*T",
            "root_method": "bracket all sign changes on 2001-point Eprime scan; refine with Brent",
            "support_note": "complete support with the explicitly stated 45T numerical occupation tail",
        },
        "numerical_method": {
            "Eprime_orders": list(EPRIME_ORDERS),
            "initial_momentum_order": MOMENTUM_ORDER,
            "azimuth_order": AZIMUTH_ORDER,
            "support_scan_points": SUPPORT_SCAN_POINTS,
            "legacy_window_half_width_MeV": LOCAL_WINDOW_HALF_WIDTH,
        },
        "maxima": {
            "support_root_relative_residual": float(max_root),
            "cold_dilute_Horowitz_relative_residual": float(max_horowitz),
            "Eprime_48_to_72_relative_difference": float(max_convergence_48),
            "Eprime_32_to_72_relative_difference": float(max_convergence_32),
        },
        "legacy_60MeV_window_fraction": {
            "minimum": float(min_window_fraction),
            "maximum": float(max_window_fraction),
        },
        "acceptance": acceptance,
        "overall_pass": bool(all(acceptance.values())),
        "interpretation": [
            "The Eprime support is determined by the exact local pmin condition and the same 45T pmax tail used by C4-B2.",
            "The old fixed 60 MeV half-window is compared against the complete support rather than assumed to be complete.",
            "The cold/dilute full-support integral recovers the stationary Horowitz differential cross section.",
            "The output remains differential in outgoing angle; no total cross section, radial opacity, or transport is inferred.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C4-C1 acceptance failed: {acceptance}")
    return local, support, cold, summary


def _write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError("cannot write empty C4-C1 output")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--c2-reference", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-local-csv", type=Path, required=True)
    parser.add_argument("--output-support-csv", type=Path, required=True)
    parser.add_argument("--output-cold-csv", type=Path, required=True)
    args = parser.parse_args()
    profile = load_profile(args.profile)
    c2 = load_c2_reference(args.c2_reference)
    local, support, cold, summary = analyze(profile, c2)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(summary, indent=2, allow_nan=False)+"\n", encoding="utf-8"
    )
    for path, rows in (
        (args.output_local_csv, local),
        (args.output_support_csv, support),
        (args.output_cold_csv, cold),
    ):
        _write_csv(path, rows)
    print(json.dumps({
        "overall_pass": summary["overall_pass"],
        "maxima": summary["maxima"],
        "legacy_60MeV_window_fraction": summary["legacy_60MeV_window_fraction"],
        "acceptance": summary["acceptance"],
    }, indent=2))


if __name__ == "__main__":
    main()
