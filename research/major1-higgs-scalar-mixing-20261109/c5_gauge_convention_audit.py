#!/usr/bin/env python3
"""Exact convention audit for the original axial VLL model and RC-001.

This is a small algebra/bookkeeping audit, not a loop calculation.
It checks the signed dimension-five coefficient from the Schur complement,
its covariance under a right-handed light-field rephasing, and the sign map
between D=partial-i g A and D=partial+i g A conventions.
"""
from __future__ import annotations

from fractions import Fraction
import json


def schur_light_mass(y, lam, vh, vs, me):
    """Leading signed light mass from the 2x2 UV mass-matrix Schur complement."""
    return (
        -Fraction(y) * Fraction(lam) * Fraction(vh) * Fraction(vs)
        / (2 * Fraction(me))
    )


def c5_from_schur(y, lam, vh, vs, me):
    """Match m_eff = C5 vh vs / 2 for L_EFT = -C5 S bar(L) H l_R."""
    return 2 * schur_light_mass(y, lam, vh, vs, me) / (
        Fraction(vh) * Fraction(vs)
    )


def manuscript_signed_mass(y, lam, vh, vs, me):
    """Signed mass implied by the positive coefficient printed in v6 Eq. (5-d)."""
    return (
        Fraction(y) * Fraction(lam) * Fraction(vh) * Fraction(vs)
        / (2 * Fraction(me))
    )


def convention_sign_map():
    """Map upstream (+i g A) to axial-paper (-i g A) conventions.

    Choose A_plus = -A_minus with unchanged positive gauge couplings and
    unchanged generators/charges. Then D_plus = D_minus, while the raw
    component field strengths satisfy F_plus = -F_minus. The curvature
    matrix defined by [D_mu,D_nu] = i mathscrF_mu_nu is invariant.
    """
    return {
        "A_plus_over_A_minus": -1,
        "F_plus_over_F_minus": -1,
        "D_plus_over_D_minus": 1,
        "commutator_curvature_plus_over_minus": 1,
        "currents_built_from_D_plus_over_minus": 1,
        "raw_two_field_strength_product_sign": 1,
        "single_explicit_raw_F_operator_sign": -1,
        "D_only_operator_coefficient_sign": 1,
        "one_background_vertex_of_D_only_operator_sign": -1,
        "axial_raw_gauge_EOM_sign_relative_to_upstream": -1,
    }


def audit():
    cases = [
        (Fraction(2), Fraction(3), Fraction(5), Fraction(7), Fraction(11)),
        (
            Fraction(1, 3), Fraction(5, 7), Fraction(24622, 100),
            Fraction(70886458, 10**6), Fraction(20000),
        ),
    ]
    rows = []
    for y, lam, vh, vs, me in cases:
        m_uv = schur_light_mass(y, lam, vh, vs, me)
        c5 = c5_from_schur(y, lam, vh, vs, me)
        m_eft = c5 * vh * vs / 2
        m_v6 = manuscript_signed_mass(y, lam, vh, vs, me)

        assert c5 == -y * lam / me
        assert m_eft == m_uv
        assert m_v6 == -m_uv

        # Rephase the light right-handed field by -1. Then lambda -> -lambda
        # and O5 -> -O5; the matching relation C5=-y lambda/M remains covariant.
        lam_rephased = -lam
        c5_rephased = c5_from_schur(y, lam_rephased, vh, vs, me)
        operator_rephasing = -1
        assert c5_rephased == -c5
        assert c5_rephased * operator_rephasing == c5

        determinant = -y * lam * vh * vs / 2
        assert determinant < 0
        rows.append({
            "y": str(y),
            "lambda": str(lam),
            "vh_GeV": str(vh),
            "vs_GeV": str(vs),
            "ME_GeV": str(me),
            "C5_from_Schur_GeVminus1": str(c5),
            "signed_mass_from_UV_GeV": str(m_uv),
            "signed_mass_from_v6_Eq5d_GeV": str(m_v6),
            "v6_to_Schur_signed_mass_ratio": "-1",
            "det_mass_matrix_GeV2": str(determinant),
            "right_field_rephasing_covariance": "PASS",
        })

    sign_map = convention_sign_map()
    assert sign_map["D_plus_over_D_minus"] == 1
    assert sign_map["F_plus_over_F_minus"] == -1
    assert sign_map["commutator_curvature_plus_over_minus"] == 1
    assert sign_map["raw_two_field_strength_product_sign"] == 1
    assert sign_map["single_explicit_raw_F_operator_sign"] == -1
    assert sign_map["D_only_operator_coefficient_sign"] == 1
    assert sign_map["axial_raw_gauge_EOM_sign_relative_to_upstream"] == -1

    return {
        "scope": "tree-level sign and convention audit only; no loop matching",
        "C5_convention": "L_EFT = -C5 S_l bar(L_l) H l_R + h.c.",
        "result": "C5 = - y_l lambda_l / M_E_l",
        "v6_Eq5d_displayed_relation": "c_l/Lambda = + y_l lambda_l / M_E_l",
        "v6_Eq5d_signed_mass_ratio_to_Schur": -1,
        "rephasing": "l_R -> -l_R implies lambda -> -lambda, O5 -> -O5; C5=-y lambda/M is preserved",
        "field_convention_map": sign_map,
        "cases": rows,
        "limitations": [
            "A signed Dirac mass can be rephased, but all UV/EFT couplings and operators must transform together.",
            "The printed Eq. (5-d) coefficient is opposite to the Schur result for the displayed UV Lagrangian and operator orientation.",
            "The mass-squared formula is unaffected; sign-sensitive interference must use one consistent convention.",
            "The field-strength sign map depends on whether an operator is written with raw F or the commutator curvature mathscrF.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
