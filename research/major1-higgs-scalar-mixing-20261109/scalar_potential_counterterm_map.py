#!/usr/bin/env python3
"""Map the fermion-sector local UV pole matrix onto scalar-potential parameters.

The output is an algebraic counterterm ledger, not a choice of tadpole or VEV
renormalization scheme. It displays the general parameter map and one
fixed-VEV bookkeeping basis that reconstructs the three local matrix poles.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

VH = 246.22
BENCHMARK_VS = {"A_open_AA": 70.886458, "B_closed_AA": 315.0}


def potential_mass_matrix(
    vh: float, vs: float, mu_h2: float, mu_s2: float,
    lam_h: float, lam_s: float, lam_hs: float,
) -> list[list[float]]:
    """H0=(vh+h)/sqrt(2), S=(vs+s)/sqrt(2), L contains -V."""
    return [
        [
            -mu_h2 + 3.0 * lam_h * vh**2 + 0.5 * lam_hs * vs**2,
            lam_hs * vh * vs,
        ],
        [
            lam_hs * vh * vs,
            -mu_s2 + 3.0 * lam_s * vs**2 + 0.5 * lam_hs * vh**2,
        ],
    ]


def potential_tadpole_brackets(
    vh: float, vs: float, mu_h2: float, mu_s2: float,
    lam_h: float, lam_s: float, lam_hs: float,
) -> tuple[float, float]:
    """Tree tadpoles divided by their VEVs."""
    return (
        -mu_h2 + lam_h * vh**2 + 0.5 * lam_hs * vs**2,
        -mu_s2 + lam_s * vs**2 + 0.5 * lam_hs * vh**2,
    )


def linearized_mass_counterterm(
    vh: float, vs: float, lam_h: float, lam_s: float, lam_hs: float,
    dmu_h2: float, dmu_s2: float,
    dlam_h: float, dlam_s: float, dlam_hs: float,
    dvh: float = 0.0, dvs: float = 0.0,
) -> list[list[float]]:
    """First-order variation of the tree scalar mass matrix."""
    dhh = (
        -dmu_h2 + 3.0 * vh**2 * dlam_h + 6.0 * lam_h * vh * dvh
        + 0.5 * vs**2 * dlam_hs + lam_hs * vs * dvs
    )
    dss = (
        -dmu_s2 + 3.0 * vs**2 * dlam_s + 6.0 * lam_s * vs * dvs
        + 0.5 * vh**2 * dlam_hs + lam_hs * vh * dvh
    )
    dhs = vh * vs * dlam_hs + lam_hs * (vs * dvh + vh * dvs)
    return [[dhh, dhs], [dhs, dss]]


def linearized_tadpole_counterterms_per_vev(
    vh: float, vs: float, lam_h: float, lam_s: float, lam_hs: float,
    dmu_h2: float, dmu_s2: float,
    dlam_h: float, dlam_s: float, dlam_hs: float,
    dvh: float = 0.0, dvs: float = 0.0,
) -> tuple[float, float]:
    """Parameter-induced delta T_h/vh and delta T_s/vs at a tree stationary point."""
    dh = (
        -dmu_h2 + vh**2 * dlam_h + 2.0 * lam_h * vh * dvh
        + 0.5 * vs**2 * dlam_hs + lam_hs * vs * dvs
    )
    ds = (
        -dmu_s2 + vs**2 * dlam_s + 2.0 * lam_s * vs * dvs
        + 0.5 * vh**2 * dlam_hs + lam_hs * vh * dvh
    )
    return dh, ds


def fixed_vev_bookkeeping_basis(
    delta_matrix: list[list[float]], vh: float, vs: float,
) -> dict:
    """One exact algebraic decomposition; not a selected renormalization scheme.

    Set delta-lambda_H=delta-lambda_S=delta-vh=delta-vs=0. The off-diagonal
    entry fixes delta-lambda_HS, and the two diagonal entries are absorbed
    into the quadratic potential parameters mu_H^2 and mu_S^2.
    """
    dhh = float(delta_matrix[0][0])
    dhs = float(delta_matrix[0][1])
    dss = float(delta_matrix[1][1])
    dlam_hs = dhs / (vh * vs)
    dmu_h2 = -dhh + 0.5 * vs**2 * dlam_hs
    dmu_s2 = -dss + 0.5 * vh**2 * dlam_hs
    reconstructed = linearized_mass_counterterm(
        vh, vs, lam_h=0.0, lam_s=0.0, lam_hs=0.0,
        dmu_h2=dmu_h2, dmu_s2=dmu_s2,
        dlam_h=0.0, dlam_s=0.0, dlam_hs=dlam_hs,
    )
    residual = max(
        abs(reconstructed[0][0] - dhh),
        abs(reconstructed[0][1] - dhs),
        abs(reconstructed[1][1] - dss),
    )
    return {
        "basis_label": "fixed_vev_quadratic_diagonal_plus_portal_offdiagonal",
        "delta_lambda_H": 0.0,
        "delta_lambda_S": 0.0,
        "delta_lambda_HS": dlam_hs,
        "delta_mu_H2_GeV2": dmu_h2,
        "delta_mu_S2_GeV2": dmu_s2,
        "delta_vh_GeV": 0.0,
        "delta_vs_GeV": 0.0,
        "reconstructed_mass_matrix_counterterm_GeV2": reconstructed,
        "max_reconstruction_residual_GeV2": residual,
        "warning": (
            "This is one bookkeeping decomposition of the two-point UV pole. "
            "It does not fix the tadpole counterterms or define a VEV scheme."
        ),
    }


def run_mapping(independent_json: Path) -> dict:
    independent = json.loads(independent_json.read_text(encoding="utf-8"))
    benchmarks = {}
    for label, vs in BENCHMARK_VS.items():
        data = independent["benchmarks"][label]
        matrix = [
            [
                data["hh"]["MS_mass_counterterm_pole_coefficient_full_minus_light_GeV2"],
                data["hs"]["MS_mass_counterterm_pole_coefficient_full_minus_light_GeV2"],
            ],
            [
                data["hs"]["MS_mass_counterterm_pole_coefficient_full_minus_light_GeV2"],
                data["ss"]["MS_mass_counterterm_pole_coefficient_full_minus_light_GeV2"],
            ],
        ]
        basis = fixed_vev_bookkeeping_basis(matrix, VH, vs)
        benchmarks[label] = {
            "vs_GeV": vs,
            "mass_matrix_counterterm_pole_coefficient_GeV2": matrix,
            "fixed_vev_bookkeeping_basis": basis,
            "tadpole_and_vev_scheme_status": "not_fixed_by_the_two_point_subcalculation",
        }

    return {
        "status": "PASS",
        "potential_convention": (
            "V=-mu_H2 HdaggerH-mu_S2 SdaggerS+lambda_H(HdaggerH)^2"
            "+lambda_S(SdaggerS)^2+lambda_HS(HdaggerH)(SdaggerS); "
            "H0=(vh+h)/sqrt(2), S=(vs+s)/sqrt(2), L contains -V"
        ),
        "tree_mass_matrix": {
            "hh": "-mu_H2 + 3 lambda_H vh^2 + (lambda_HS/2) vs^2",
            "ss": "-mu_S2 + 3 lambda_S vs^2 + (lambda_HS/2) vh^2",
            "hs": "lambda_HS vh vs",
        },
        "general_counterterm_map": {
            "hh": "-dmu_H2 + 3 vh^2 dlambda_H + 6 lambda_H vh dvh + (vs^2/2) dlambda_HS + lambda_HS vs dvs",
            "ss": "-dmu_S2 + 3 vs^2 dlambda_S + 6 lambda_S vs dvs + (vh^2/2) dlambda_HS + lambda_HS vh dvh",
            "hs": "vh vs dlambda_HS + lambda_HS (vs dvh + vh dvs)",
        },
        "tadpole_map_at_tree_stationarity": {
            "delta_T_h_over_vh": "-dmu_H2 + vh^2 dlambda_H + 2 lambda_H vh dvh + (vs^2/2) dlambda_HS + lambda_HS vs dvs",
            "delta_T_s_over_vs": "-dmu_S2 + vs^2 dlambda_S + 2 lambda_S vs dvs + (vh^2/2) dlambda_HS + lambda_HS vh dvh",
            "identity_hh": "delta_M_hh^2 - delta_T_h/vh = 2 vh^2 dlambda_H + 4 lambda_H vh dvh",
            "identity_ss": "delta_M_ss^2 - delta_T_s/vs = 2 vs^2 dlambda_S + 4 lambda_S vs dvs",
        },
        "non_uniqueness": (
            "The three two-point matrix entries do not determine all quadratic, "
            "quartic, VEV, and tadpole counterterms. A tadpole/VEV prescription "
            "and the corresponding one-point functions are required before "
            "assigning unique renormalized potential-parameter counterterms."
        ),
        "benchmarks": benchmarks,
        "scope": [
            "The matrix entries are UV-pole counterterm coefficients proportional to Delta_UV, not finite mass shifts.",
            "The fixed-VEV decomposition is an algebraic example only, not a claim that this is the chosen MS-bar tadpole or VEV scheme.",
            "No tadpole diagrams, VEV renormalization, complete scalar-potential beta functions, or gauge-complete self-energies are included.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--independent-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run_mapping(args.independent_json)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        k: {
            "mass_matrix_counterterm_pole_coefficient_GeV2": v["mass_matrix_counterterm_pole_coefficient_GeV2"],
            "fixed_vev_bookkeeping_basis": v["fixed_vev_bookkeeping_basis"],
        } for k, v in result["benchmarks"].items()
    }, indent=2))


if __name__ == "__main__":
    main()
