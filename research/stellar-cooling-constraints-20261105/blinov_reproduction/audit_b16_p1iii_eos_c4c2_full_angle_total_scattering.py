#!/usr/bin/env python3
"""C4-C2: full outgoing-angle and outgoing-energy EOS scattering integral."""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel import (
    HBARC,
    INCIDENT_ENERGY,
    MASS,
    N0,
    differential_rate_eos,
    legacy,
)
from audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support import (
    COLD_BARYON_DENSITY_OVER_N0,
    COLD_PROTON_FRACTION,
    COLD_TEMPERATURE,
    EPRIME_ORDERS,
    PROFILE_INDICES,
    SPECIES,
    exact_outgoing_energy_support,
    integrate_outgoing_energy,
    load_c2_reference,
)

HERE = Path(__file__).resolve().parent
LOCAL_COS_ORDER = 8
ANGLE_CONVERGENCE_ORDERS = (8, 12)
COLD_COS_ORDER = 16
HOROWITZ_COS_ORDERS = (16, 32)
LOCAL_EPRIME_ORDER = 48
LOCAL_P_ORDER = 36
LOCAL_PHI_ORDER = 12
COLD_EPRIME_ORDER = 72
COLD_P_ORDER = 48
COLD_PHI_ORDER = 16
LOCAL_SUPPORT_SCAN = 10001
COLD_SUPPORT_SCAN = 40001
ANTINU_VALUES = (False, True)


def integrate_total_rate(
    incident_energy: float,
    target: str,
    antinu: bool,
    temperature: float,
    nu: float,
    mstar: float,
    *,
    n_cos: int,
    order_ep: int,
    order_p: int,
    order_phi: int,
    support_scan_points: int,
) -> tuple[float, float]:
    """Return 2pi int dcos int dE' dGamma/(dE' dOmega') and max root residual."""
    x, w = leggauss(n_cos)
    angular_sum = 0.0
    max_root_residual = 0.0
    for costh, weight in zip(x, w):
        lower, upper, _, root_residual = exact_outgoing_energy_support(
            incident_energy, float(costh), mstar, temperature, nu,
            scan_points=support_scan_points,
        )
        max_root_residual = max(max_root_residual, root_residual)
        differential_angle = integrate_outgoing_energy(
            lower, upper, incident_energy, float(costh),
            target, antinu, temperature, nu, mstar,
            order_ep=order_ep, order_p=order_p, order_phi=order_phi,
        )
        angular_sum += float(weight)*differential_angle
    return 2.0*math.pi*angular_sum, max_root_residual


def horowitz_total_cross_section(
    target: str,
    antinu: bool,
    *,
    n_cos: int,
) -> float:
    x, w = leggauss(n_cos)
    return float(
        2.0*math.pi*sum(
            float(weight)*legacy.kernel.evaluate(
                INCIDENT_ENERGY, float(costh), target, antinu
            )["dsdo"]
            for costh, weight in zip(x, w)
        )
    )


def _local_cases(
    profile: list[dict[str, float]],
    c2: list[dict[str, float]],
) -> tuple[list[dict], list[dict], list[dict]]:
    local_records, angle_records, kernel_records = [], [], []
    for index in PROFILE_INDICES:
        row, occupation = profile[index], c2[index]
        if abs(row["r_km"]-occupation["r_km"]) > 1e-12:
            raise ValueError("C1/C2 radial mismatch")
        for target in SPECIES:
            mstar = row[f"mstar_{target}_MeV"]
            temperature = row["T_MeV"]
            nu = occupation[f"nu_{target}_EOS_MeV"]
            nprime_fm3 = occupation[f"nprime_{target}_fm3"]
            nprime_mev3 = nprime_fm3*HBARC**3
            xi = row["xi_SPP"]
            for antinu in ANTINU_VALUES:
                gamma, root_residual = integrate_total_rate(
                    INCIDENT_ENERGY, target, antinu, temperature, nu, mstar,
                    n_cos=LOCAL_COS_ORDER,
                    order_ep=LOCAL_EPRIME_ORDER,
                    order_p=LOCAL_P_ORDER,
                    order_phi=LOCAL_PHI_ORDER,
                    support_scan_points=LOCAL_SUPPORT_SCAN,
                )
                if gamma <= 0.0:
                    raise ArithmeticError("non-positive EOS total scattering rate")
                local_records.append({
                    "r_km": row["r_km"],
                    "species": target,
                    "antinu": antinu,
                    "E_MeV": INCIDENT_ENERGY,
                    "T_MeV": temperature,
                    "mstar_MeV": mstar,
                    "nu_MeV": nu,
                    "eta_nu_over_T": nu/temperature,
                    "theta_T_over_mstar": temperature/mstar,
                    "X_free": row[f"X_{target}"],
                    "xi_SPP": xi,
                    "nprime_fm3": nprime_fm3,
                    "gamma_total_available_volume_MeV": gamma,
                    "sigma_total_per_target_MeV_minus2": gamma/nprime_mev3,
                    "xi_times_gamma_total_MeV": xi*gamma,
                    "cosine_quadrature_order": LOCAL_COS_ORDER,
                    "Eprime_quadrature_order": LOCAL_EPRIME_ORDER,
                    "initial_momentum_order": LOCAL_P_ORDER,
                    "azimuth_order": LOCAL_PHI_ORDER,
                    "support_root_max_relative_residual": root_residual,
                })

                if index == PROFILE_INDICES[0]:
                    gamma12, root12 = integrate_total_rate(
                        INCIDENT_ENERGY, target, antinu, temperature, nu, mstar,
                        n_cos=12,
                        order_ep=LOCAL_EPRIME_ORDER,
                        order_p=LOCAL_P_ORDER,
                        order_phi=LOCAL_PHI_ORDER,
                        support_scan_points=LOCAL_SUPPORT_SCAN,
                    )
                    angle_records.append({
                        "r_km": row["r_km"],
                        "species": target,
                        "antinu": antinu,
                        "gamma_cos8": gamma,
                        "gamma_cos12": gamma12,
                        "relative_cos8_to_cos12_difference": abs(gamma12/gamma-1.0),
                        "max_support_root_residual": max(root_residual, root12),
                    })

                    if (target == "n" and not antinu) or (target == "p" and antinu):
                        gamma_high, root_high = integrate_total_rate(
                            INCIDENT_ENERGY, target, antinu, temperature, nu, mstar,
                            n_cos=LOCAL_COS_ORDER,
                            order_ep=LOCAL_EPRIME_ORDER,
                            order_p=48,
                            order_phi=16,
                            support_scan_points=LOCAL_SUPPORT_SCAN,
                        )
                        kernel_records.append({
                            "r_km": row["r_km"],
                            "species": target,
                            "antinu": antinu,
                            "gamma_p36_phi12": gamma,
                            "gamma_p48_phi16": gamma_high,
                            "relative_kernel_order_difference": abs(gamma_high/gamma-1.0),
                            "max_support_root_residual": max(root_residual, root_high),
                        })
    return local_records, angle_records, kernel_records


def _cold_horowitz_cases() -> tuple[list[dict], list[dict]]:
    records, angle_records = [], []
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
            gamma, root_residual = integrate_total_rate(
                INCIDENT_ENERGY, target, antinu,
                COLD_TEMPERATURE, nu, mass,
                n_cos=COLD_COS_ORDER,
                order_ep=COLD_EPRIME_ORDER,
                order_p=COLD_P_ORDER,
                order_phi=COLD_PHI_ORDER,
                support_scan_points=COLD_SUPPORT_SCAN,
            )
            sigma_dynamic = gamma/(n_species*HBARC**3)
            sigma_horowitz = horowitz_total_cross_section(
                target, antinu, n_cos=HOROWITZ_COS_ORDERS[-1]
            )
            sigma_horowitz_low = horowitz_total_cross_section(
                target, antinu, n_cos=HOROWITZ_COS_ORDERS[0]
            )
            records.append({
                "species": target,
                "antinu": antinu,
                "nB_over_n0": COLD_BARYON_DENSITY_OVER_N0,
                "T_MeV": COLD_TEMPERATURE,
                "E_MeV": INCIDENT_ENERGY,
                "gamma_total_MeV": gamma,
                "sigma_dynamic_total_MeV_minus2": sigma_dynamic,
                "sigma_Horowitz_total_MeV_minus2": sigma_horowitz,
                "relative_total_Horowitz_residual": sigma_dynamic/sigma_horowitz-1.0,
                "Horowitz_cos16_to_cos32_relative_difference": abs(
                    sigma_horowitz/sigma_horowitz_low-1.0
                ),
                "support_root_max_relative_residual": root_residual,
            })
            angle_records.append({
                "species": target,
                "antinu": antinu,
                "sigma_Horowitz_cos16": sigma_horowitz_low,
                "sigma_Horowitz_cos32": sigma_horowitz,
                "relative_cos16_to_cos32_difference": abs(
                    sigma_horowitz/sigma_horowitz_low-1.0
                ),
            })
    return records, angle_records


def analyze(
    profile: list[dict[str, float]],
    c2: list[dict[str, float]],
) -> tuple[list[dict], list[dict], list[dict], list[dict], list[dict], dict]:
    if len(profile) != 301 or len(c2) != 301:
        raise ValueError("C4-C2 requires the 301-point C1/C2 profile")
    local, angle_local, kernel_order = _local_cases(profile, c2)
    cold, angle_cold = _cold_horowitz_cases()

    max_cold_horowitz = max(
        abs(row["relative_total_Horowitz_residual"]) for row in cold
    )
    max_horowitz_angle = max(
        row["Horowitz_cos16_to_cos32_relative_difference"] for row in cold
    )
    max_local_angle = max(
        row["relative_cos8_to_cos12_difference"] for row in angle_local
    )
    max_kernel_order = max(
        row["relative_kernel_order_difference"] for row in kernel_order
    )
    max_root = max(
        [row["support_root_max_relative_residual"] for row in local]
        +[row["support_root_max_relative_residual"] for row in cold]
        +[row["max_support_root_residual"] for row in angle_local]
        +[row["max_support_root_residual"] for row in kernel_order]
    )

    acceptance = {
        "sixteen_full_angle_EOS_cases": bool(len(local) == 16),
        "four_cold_Horowitz_total_cases": bool(len(cold) == 4),
        "four_core_angle_convergence_cases": bool(len(angle_local) == 4),
        "two_core_kernel_order_cases": bool(len(kernel_order) == 2),
        "cold_full_angle_Horowitz_below_1e_3": bool(max_cold_horowitz < 1e-3),
        "Horowitz_angle_quadrature_below_1e_4": bool(max_horowitz_angle < 1e-4),
        "EOS_local_angle_quadrature_below_1_percent": bool(max_local_angle < 1e-2),
        "EOS_kernel_order_difference_below_1_percent": bool(max_kernel_order < 1e-2),
        "support_root_residual_below_1e_7": bool(max_root < 1e-7),
        "all_local_total_rates_positive": bool(
            all(row["gamma_total_available_volume_MeV"] > 0.0 for row in local)
        ),
    }
    summary = {
        "title": "P1-IIIe-C4C2 full outgoing-angle and outgoing-energy scattering integral",
        "date": "2026-11-11",
        "status": "PASS: full Eprime support, outgoing-angle convergence, and cold total Horowitz limit",
        "scope": (
            "Local EOS total neutral-current scattering rate at four selected radii; "
            "full outgoing energy and angle at fixed E=100 MeV; no radial transport."
        ),
        "provenance": {
            "selected_profile_indices_zero_based": list(PROFILE_INDICES),
            "selected_radii_km": [profile[i]["r_km"] for i in PROFILE_INDICES],
            "species": list(SPECIES),
            "neutrino_antineutrino": ["nu", "antinu"],
            "incident_energy_MeV": INCIDENT_ENERGY,
            "local_cosine_order": LOCAL_COS_ORDER,
            "local_Eprime_order": LOCAL_EPRIME_ORDER,
            "local_initial_momentum_order": LOCAL_P_ORDER,
            "local_azimuth_order": LOCAL_PHI_ORDER,
            "cold_cosine_order": COLD_COS_ORDER,
            "cold_Eprime_order": COLD_EPRIME_ORDER,
            "cold_initial_momentum_order": COLD_P_ORDER,
            "cold_azimuth_order": COLD_PHI_ORDER,
        },
        "maxima": {
            "cold_total_Horowitz_relative_residual": float(max_cold_horowitz),
            "Horowitz_cos16_to_cos32_relative_difference": float(max_horowitz_angle),
            "EOS_local_cos8_to_cos12_relative_difference": float(max_local_angle),
            "EOS_kernel_p36phi12_to_p48phi16_relative_difference": float(max_kernel_order),
            "support_root_relative_residual": float(max_root),
        },
        "acceptance": acceptance,
        "overall_pass": bool(all(acceptance.values())),
        "interpretation": [
            "The full outgoing-energy support is integrated at every outgoing-angle node.",
            "The factor 2pi converts the azimuth-symmetric differential-in-angle rate to a total rate.",
            "The cold/dilute total cross section is compared with the independently angle-integrated Horowitz stationary-target result.",
            "The local EOS rate is per available volume; xi_SPP is restored only in xi_times_gamma_total.",
            "The output is a local total scattering rate, not yet a radial optical depth or transport solution.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C4-C2 acceptance failed: {acceptance}")
    return local, cold, angle_local, kernel_order, angle_cold, summary


def _write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError("cannot write empty C4-C2 output")
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
    parser.add_argument("--output-cold-csv", type=Path, required=True)
    parser.add_argument("--output-angle-csv", type=Path, required=True)
    parser.add_argument("--output-kernel-order-csv", type=Path, required=True)
    args = parser.parse_args()
    profile = load_profile(args.profile)
    c2 = load_c2_reference(args.c2_reference)
    local, cold, angle_local, kernel_order, angle_cold, summary = analyze(profile, c2)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(summary, indent=2, allow_nan=False)+"\n", encoding="utf-8"
    )
    _write_csv(args.output_local_csv, local)
    _write_csv(args.output_cold_csv, cold)

    angle_columns = (
        "kind", "r_km", "species", "antinu", "n_cos_low", "n_cos_high",
        "rate_or_sigma_low", "rate_or_sigma_high", "relative_difference",
    )
    angle_rows = []
    for row in angle_local:
        angle_rows.append({
            "kind": "EOS_local",
            "r_km": row["r_km"],
            "species": row["species"],
            "antinu": row["antinu"],
            "n_cos_low": 8,
            "n_cos_high": 12,
            "rate_or_sigma_low": row["gamma_cos8"],
            "rate_or_sigma_high": row["gamma_cos12"],
            "relative_difference": row["relative_cos8_to_cos12_difference"],
        })
    for row in angle_cold:
        angle_rows.append({
            "kind": "Horowitz",
            "r_km": "",
            "species": row["species"],
            "antinu": row["antinu"],
            "n_cos_low": 16,
            "n_cos_high": 32,
            "rate_or_sigma_low": row["sigma_Horowitz_cos16"],
            "rate_or_sigma_high": row["sigma_Horowitz_cos32"],
            "relative_difference": row["relative_cos16_to_cos32_difference"],
        })
    args.output_angle_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_angle_csv.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=angle_columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(angle_rows)
    _write_csv(args.output_kernel_order_csv, kernel_order)

    print(json.dumps({
        "overall_pass": summary["overall_pass"],
        "maxima": summary["maxima"],
        "acceptance": summary["acceptance"],
    }, indent=2))

if __name__ == "__main__":
    main()
