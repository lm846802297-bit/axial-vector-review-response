#!/usr/bin/env python3
"""Horowitz exact free-nucleon recoil/weak-magnetism transport moments.

This computes free-space neutral-current nu-N scattering for an initially
stationary proton or neutron. It is a local collision-kernel baseline, not a
medium opacity or a B.2 radial transport result.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

GF_MEV = 1.1663787e-11
HBARC_MEV_CM = 1.973269804e-11
MEV2_TO_CM2 = HBARC_MEV_CM**2
MASS = {"n": 939.56542052, "p": 938.27208816}
SIN2W = 0.2325
GA = 1.260
LAMBDA_P = 1.793
LAMBDA_N = -1.913
F2_POINT = {"p": 1.019, "n": -0.963}
ENERGIES = (50.0, 100.0, 150.0, 255.0, 500.0)
OUTER_T_MEV = 3.03


def point_couplings(target: str):
    if target == "p":
        return 0.5 - 2.0 * SIN2W, GA / 2.0, F2_POINT["p"]
    return -0.5, -GA / 2.0, F2_POINT["n"]


def horowitz_form_factors(q2: np.ndarray, target: str, mass: float):
    tau = q2 / (4.0 * mass * mass)
    eta_em = 1.0 / (1.0 + 5.6 * tau)
    g_dipole = (1.0 + 4.97 * tau) ** -2
    f1p = (1.0 + tau * (1.0 + LAMBDA_P)) * g_dipole / (1.0 + tau)
    f2p = LAMBDA_P * g_dipole / (1.0 + tau)
    f1n = tau * LAMBDA_N * (1.0 - eta_em) * g_dipole / (1.0 + tau)
    f2n = LAMBDA_N * (1.0 + tau * eta_em) * g_dipole / (1.0 + tau)

    if target == "p":
        cv = (0.5 - 2.0 * SIN2W) * f1p - 0.5 * f1n
        ca = +GA / 2.0 * (1.0 + 3.53 * tau) ** -2
        f2z = (0.5 - 2.0 * SIN2W) * f2p - 0.5 * f2n
    else:
        cv = (0.5 - 2.0 * SIN2W) * f1n - 0.5 * f1p
        ca = -GA / 2.0 * (1.0 + 3.53 * tau) ** -2
        f2z = (0.5 - 2.0 * SIN2W) * f2n - 0.5 * f2p
    return cv, ca, f2z


def cross_sections(
    energy: float,
    target: str,
    antinu: bool,
    use_form_factors: bool = True,
    order: int = 600,
):
    mass = MASS[target]
    e = energy / mass
    x, w = leggauss(order)
    eta = 1.0 / (1.0 + e * (1.0 - x))
    q2 = 2.0 * energy**2 * eta * (1.0 - x)

    if use_form_factors:
        cv, ca, f2 = horowitz_form_factors(q2, target, mass)
    else:
        cv, ca, f2 = point_couplings(target)

    sign = -1.0 if antinu else 1.0
    brace = (
        cv**2 * (1.0 + eta**2 - eta * (1.0 - x))
        + ca**2 * (1.0 + eta**2 + eta * (1.0 - x))
        + sign * 2.0 * ca * (cv + f2) * (1.0 - eta**2)
        + eta**2 * e**2 / 2.0 * (1.0 - x)
        * (f2**2 * (3.0 - x) + 4.0 * cv * f2 * (1.0 - x))
    )
    dsdo = GF_MEV**2 * energy**2 / (4.0 * math.pi**2) * eta**2 * brace
    dsdx = 2.0 * math.pi * dsdo

    total = float(np.sum(w * dsdx) * MEV2_TO_CM2)
    angular_transport = float(np.sum(w * dsdx * (1.0 - x)) * MEV2_TO_CM2)
    momentum_transfer = float(np.sum(w * dsdx * (1.0 - eta * x)) * MEV2_TO_CM2)
    energy_loss = float(np.sum(w * dsdx * (1.0 - eta)) * MEV2_TO_CM2)

    return {
        "sigma_total_cm2": total,
        "sigma_angular_transport_cm2": angular_transport,
        "sigma_momentum_transfer_cm2": momentum_transfer,
        "sigma_energy_loss_cm2": energy_loss,
        "mean_fractional_energy_loss": energy_loss / total,
        "sigma_energy_over_momentum": energy_loss / momentum_transfer,
        "momentum_over_angular_transport": momentum_transfer / angular_transport,
        "max_Q2_GeV2": float(np.max(q2) / 1.0e6),
    }


def sigma0_transport(energy: float, target: str):
    cv, ca, _ = point_couplings(target)
    value = GF_MEV**2 * energy**2 / math.pi * (2.0 / 3.0) * (cv**2 + 5.0 * ca**2)
    return value * MEV2_TO_CM2


def horowitz_analytic_rt(energy: float, target: str, antinu: bool):
    """Horowitz (2002), Eqs. (37)-(42), pointlike form factors."""
    mass = MASS[target]
    e = energy / mass
    cv, ca, f2 = point_couplings(target)
    log = math.log(1.0 + 2.0 * e)
    term_cv = cv**2 * (
        (e - 1.0) / (2.0 * e**3) * log
        + (3.0 + 12.0*e + 9.0*e**2 - 10.0*e**3)
        / (3.0 * e**2 * (1.0 + 2.0*e)**3)
    )
    term_ca = ca**2 * (
        (1.0 + e) / (2.0 * e**3) * log
        - (10.0*e**3 + 27.0*e**2 + 18.0*e + 3.0)
        / (3.0 * e**2 * (1.0 + 2.0*e)**3)
    )
    sign = -1.0 if antinu else 1.0
    term_interference = sign * (cv + f2) * ca * (
        log / e**2
        - (2.0 + 10.0*e + (28.0/3.0)*e**2)
        / (e * (1.0 + 2.0*e)**3)
    )
    term_cv_f2 = cv * f2 * (
        log / e**2
        - (2.0/3.0) * (3.0 + 15.0*e + 22.0*e**2)
        / (e * (1.0 + 2.0*e)**3)
    )
    term_f2 = f2**2 * (
        log / (4.0 * e**2)
        + (8.0*e**3 - 22.0*e**2 - 15.0*e - 3.0)
        / (6.0 * e * (1.0 + 2.0*e)**3)
    )
    return (
        term_cv + term_ca + term_interference + term_cv_f2 + term_f2
    ) / ((2.0/3.0) * (cv**2 + 5.0*ca**2))


def build_payload():
    results = []
    raw = {}
    for energy in ENERGIES:
        raw[energy] = {}
        for target in ("n", "p"):
            raw[energy][target] = {}
            for antinu in (False, True):
                label = "antinu" if antinu else "nu"
                ff = cross_sections(energy, target, antinu, True)
                point = cross_sections(energy, target, antinu, False)
                raw[energy][target][label] = {
                    **ff,
                    "form_factor_ratio": (
                        ff["sigma_angular_transport_cm2"]
                        / point["sigma_angular_transport_cm2"]
                    ),
                    "pointlike_Rt_direct": (
                        point["sigma_angular_transport_cm2"]
                        / sigma0_transport(energy, target)
                    ),
                    "pointlike_Rt_analytic": horowitz_analytic_rt(energy, target, antinu),
                }

    for energy in ENERGIES:
        for target in ("n", "p"):
            base_nu = raw[100.0][target]["nu"]["sigma_angular_transport_cm2"]
            base_anti = raw[100.0][target]["antinu"]["sigma_angular_transport_cm2"]
            nu = raw[energy][target]["nu"]
            anti = raw[energy][target]["antinu"]
            anti_over_nu = (
                anti["sigma_angular_transport_cm2"]
                / nu["sigma_angular_transport_cm2"]
            )
            for label, item, base in (
                ("nu", nu, base_nu),
                ("antinu", anti, base_anti),
            ):
                results.append({
                    "E_MeV": energy,
                    "target": target,
                    "species": label,
                    "sigma_tr_1e-40_cm2": item["sigma_angular_transport_cm2"] / 1.0e-40,
                    "mean_energy_loss_fraction": item["mean_fractional_energy_loss"],
                    "form_factor_ratio": item["form_factor_ratio"],
                    "relative_to_E2_scaling": (
                        item["sigma_angular_transport_cm2"]
                        / (base * (energy / 100.0)**2)
                    ),
                    "antinu_over_nu": anti_over_nu,
                    "sigma_energy_over_momentum": item["sigma_energy_over_momentum"],
                    "momentum_over_angular_transport": item["momentum_over_angular_transport"],
                    "max_Q2_GeV2": item["max_Q2_GeV2"],
                })

    mj_comparison = []
    for energy in (100.0, 150.0, 255.0, 500.0):
        alpha_mj = abs(energy - 3.0 * OUTER_T_MEV) / MASS["n"]
        channels = {}
        for target in ("n", "p"):
            for label in ("nu", "antinu"):
                exact = raw[energy][target][label]["mean_fractional_energy_loss"]
                channels[f"{label}_{target}"] = {
                    "exact_stationary_target_mean_loss": exact,
                    "MJ_over_exact": alpha_mj / exact,
                }
        mj_comparison.append({
            "E_MeV": energy,
            "T_outer_MeV": OUTER_T_MEV,
            "alpha_MJ_A31": alpha_mj,
            "channels": channels,
        })

    max_rt_residual = 0.0
    max_identity_residual = 0.0
    all_positive = True
    for energy in ENERGIES:
        for target in ("n", "p"):
            for antinu in (False, True):
                point = cross_sections(energy, target, antinu, False)
                direct_rt = point["sigma_angular_transport_cm2"] / sigma0_transport(energy, target)
                analytic_rt = horowitz_analytic_rt(energy, target, antinu)
                max_rt_residual = max(max_rt_residual, abs(direct_rt / analytic_rt - 1.0))
                ff = raw[energy][target]["antinu" if antinu else "nu"]
                exact_ratio = energy / (MASS[target] + energy)
                max_identity_residual = max(
                    max_identity_residual,
                    abs(ff["sigma_energy_over_momentum"] / exact_ratio - 1.0),
                )
                all_positive = all_positive and (
                    ff["sigma_total_cm2"] > 0.0
                    and ff["sigma_angular_transport_cm2"] > 0.0
                    and ff["sigma_energy_loss_cm2"] >= 0.0
                )

    convergence = {}
    for energy, target, antinu in (
        (100.0, "n", False),
        (255.0, "n", True),
        (500.0, "n", False),
        (500.0, "n", True),
        (500.0, "p", True),
    ):
        key = f"{energy:g}MeV_{target}_{'antinu' if antinu else 'nu'}"
        reference = cross_sections(energy, target, antinu, True, 1024)[
            "sigma_angular_transport_cm2"
        ]
        convergence[key] = {}
        for order in (64, 128, 256, 512, 1024):
            value = cross_sections(energy, target, antinu, True, order)[
                "sigma_angular_transport_cm2"
            ]
            convergence[key][str(order)] = value / reference - 1.0

    return {
        "title": "Horowitz exact free-nucleon recoil/weak-magnetism moment summary",
        "date": "2026-11-10",
        "reference": "Horowitz, PRD 65, 043001 (2002), Eqs. (12)-(17), (30)-(43), Table I, Appendix II",
        "cross_section_units": "10^-40 cm^2 for sigma_tr_1e-40_cm2",
        "target_masses_MeV": MASS,
        "T_outer_MeV": OUTER_T_MEV,
        "rows": results,
        "muller_janka_A31_comparison": mj_comparison,
        "analytic_identity": (
            "sigma_energy_loss/sigma_momentum_transfer = E/(M+E) "
            "for a stationary target"
        ),
        "validation": {
            "Horowitz_pointlike_Rt_vs_Eqs_37_42_max_relative_residual": max_rt_residual,
            "energy_momentum_identity_max_relative_residual": max_identity_residual,
            "all_cross_sections_positive": all_positive,
            "quadrature_convergence_relative_to_order_1024": convergence,
        },
        "limitations": [
            "Free nucleon initially at rest; no nucleon thermal motion, Pauli blocking, mean fields, RPA correlations, or nucleon-nucleon correlations.",
            "No strange axial form factor; Horowitz discusses it separately.",
            "The form-factor model is the Horowitz 2002 dipole parameterization and should be varied as a nuclear-input uncertainty at Q2 approaching 0.5 GeV2.",
            "The angular transport moment integral (1-cos(theta)) is the Horowitz convention; at high E/M the momentum-transfer moment (1-eta*cos(theta)) is also reported.",
            "These are local free-space cross-section moments, not a radial optical-depth integration and not an updated B.2 result.",
        ],
    }


def main():
    full = build_payload()

    rows = []
    for row in full["rows"]:
        rows.append({
            "E_MeV": row["E_MeV"],
            "target": row["target"],
            "species": row["species"],
            "sigma_tr_1e-40_cm2": round(row["sigma_tr_1e-40_cm2"], 6),
            "mean_energy_loss_fraction": round(row["mean_energy_loss_fraction"], 6),
            "form_factor_ratio": round(row["form_factor_ratio"], 6),
            "relative_to_E2_scaling": round(row["relative_to_E2_scaling"], 6),
            "antinu_over_nu": round(row["antinu_over_nu"], 6),
        })

    mj_comparison = []
    for row in full["muller_janka_A31_comparison"]:
        exact_mean_loss = {
            channel: round(values["exact_stationary_target_mean_loss"], 6)
            for channel, values in row["channels"].items()
        }
        mj_comparison.append({
            "E_MeV": row["E_MeV"],
            "T_outer_MeV": row["T_outer_MeV"],
            "alpha_MJ_A31": round(row["alpha_MJ_A31"], 6),
            "exact_mean_loss": exact_mean_loss,
        })

    quadrature_max = max(
        abs(delta)
        for values in full["validation"]["quadrature_convergence_relative_to_order_1024"].values()
        for delta in values.values()
    )
    summary = {
        "title": "Horowitz exact free-nucleon recoil/weak-magnetism moment summary",
        "date": "2026-11-10",
        "reference": "Horowitz, PRD 65, 043001 (2002), Eqs. (12)-(17), (30)-(43), Table I, Appendix II",
        "cross_section_units": "10^-40 cm^2 for sigma_tr_1e-40_cm2",
        "target_masses_MeV": MASS,
        "T_outer_MeV": OUTER_T_MEV,
        "rows": rows,
        "muller_janka_A31_comparison": mj_comparison,
        "analytic_identity": "sigma_energy_loss/sigma_momentum_transfer = E/(M+E) for a stationary target",
        "validation": {
            "Horowitz_pointlike_Rt_vs_Eqs_37_42_max_relative_residual": float(
                f"{full['validation']['Horowitz_pointlike_Rt_vs_Eqs_37_42_max_relative_residual']:.3g}"
            ),
            "energy_momentum_identity_max_relative_residual": float(
                f"{full['validation']['energy_momentum_identity_max_relative_residual']:.3g}"
            ),
            "quadrature_convergence_max_relative_difference_at_64_to_1024_nodes": float(
                f"{quadrature_max:.3g}"
            ),
        },
        "limitations": full["limitations"],
    }

    output = (
        Path(__file__).resolve().parent
        / "outputs"
        / "p1i_horowitz_transport_summary_2026-11-10.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output),
        "validation": summary["validation"],
        "sample_500MeV_neutron": [
            row for row in summary["rows"]
            if row["E_MeV"] == 500.0 and row["target"] == "n"
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
