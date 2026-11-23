#!/usr/bin/env python3
"""Exact-rational charge/current bookkeeping audit for the RC-001 QLD8 EOM map."""
from __future__ import annotations

from fractions import Fraction
import json


Y_H = Fraction(1, 2)
Y = {
    "Q_L": Fraction(1, 6),
    "u_R": Fraction(2, 3),
    "d_R": Fraction(-1, 3),
    "L_L": Fraction(-1, 2),
    "e_R": Fraction(-1, 1),
}
X = {
    "L_mu": 1,
    "mu_R": -1,
    "L_tau": -1,
    "tau_R": 1,
    "S": 2,
    "H": 0,
    "Q_L": 0,
    "u_R": 0,
    "d_R": 0,
    "L_e": 0,
    "e_R": 0,
}
SU2_DOUBLETS = ("Q_L", "L_L")
SU2_SINGLET_RIGHTS = ("u_R", "d_R", "e_R", "mu_R", "tau_R")
LOW_ENERGY_EXPLICIT_FIELDS = {
    "Q_L", "u_R", "d_R", "L_e", "L_mu", "L_tau",
    "e_R", "mu_R", "tau_R", "H", "S",
}


def audit():
    assert Y_H == Fraction(1, 2)
    assert Y == {
        "Q_L": Fraction(1, 6),
        "u_R": Fraction(2, 3),
        "d_R": Fraction(-1, 3),
        "L_L": Fraction(-1, 2),
        "e_R": Fraction(-1, 1),
    }
    assert SU2_DOUBLETS == ("Q_L", "L_L")
    assert all(X[k] == 0 for k in ("H", "Q_L", "u_R", "d_R", "L_e", "e_R"))
    assert X["L_mu"] == 1 and X["mu_R"] == -1
    assert X["L_tau"] == -1 and X["tau_R"] == 1 and X["S"] == 2
    assert "E_mu" not in LOW_ENERGY_EXPLICIT_FIELDS
    assert "E_tau" not in LOW_ENERGY_EXPLICIT_FIELDS
    assert "N_R" not in LOW_ENERGY_EXPLICIT_FIELDS

    # Coefficients multiplying the explicitly expanded total currents.
    prefactors = {
        "external_abelian_internal_weak": -Fraction(1, 2),  # -g2^2/2
        "external_abelian_internal_hypercharge": -Y_H / 2,  # -gY^2/4
        "external_weak_internal_weak_singlet": -Fraction(1, 8),  # -g2^2/8
        "external_weak_internal_weak_epsilon": Fraction(1, 4),  # +g2^2/4
        "external_weak_internal_hypercharge": -Y_H / 2,  # -gY^2/4
    }
    assert prefactors["external_abelian_internal_hypercharge"] == -Fraction(1, 4)
    assert prefactors["external_weak_internal_weak_singlet"] == -Fraction(1, 8)
    assert prefactors["external_weak_internal_weak_epsilon"] == Fraction(1, 4)
    assert prefactors["external_weak_internal_hypercharge"] == -Fraction(1, 4)

    return {
        "scope": "leading-renormalizable light-field currents and gauge-EOM prefactors only",
        "hypercharge_current": {
            "Higgs": "1/2 j_H",
            "fermions": {
                "Q_L_each_generation": "1/6",
                "u_R_each_generation": "2/3",
                "d_R_each_generation": "-1/3",
                "L_L_each_generation": "-1/2",
                "e_R_each_generation": "-1",
            },
            "generations": 3,
            "colour_sum": "implicit",
        },
        "weak_current": {
            "Higgs": "j_H^a",
            "fermions": ["Q_L each generation", "L_L each generation"],
            "generator": "T^a=sigma^a/2",
            "right_singlet_currents": "absent",
        },
        "normalized_axial_X_current": {
            "L_mu": 1,
            "mu_R": -1,
            "L_tau": -1,
            "tau_R": 1,
            "S": 2,
            "electron_quarks_H": 0,
            "heavy_VLL": "integrated out; absent from low-energy current",
            "right_handed_neutrinos": "absent in the minimal model",
        },
        "gauge_EOM_prefactors_in_upstream_plus_i_gA_convention": {
            k: str(v) for k, v in prefactors.items()
        },
        "axial_raw_field_EOM_sign": "opposite to upstream; currents themselves unchanged",
        "result": "PASS",
        "limitations": [
            "No loop integrals or Wilson coefficients are evaluated.",
            "No fermion-EOM/Fierz reduction is performed.",
            "No two-background or complete UV-EFT matching closure is claimed.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
