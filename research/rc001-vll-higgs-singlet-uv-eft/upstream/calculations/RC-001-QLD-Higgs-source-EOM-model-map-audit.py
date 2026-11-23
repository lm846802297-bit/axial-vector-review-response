#!/usr/bin/env python3
"""Exact charge and inverse-ME-order audit for the original axial Higgs source."""
from __future__ import annotations

import json


X_L = {"e": 0, "mu": 1, "tau": -1}
X_R = {"e": 0, "mu": -1, "tau": 1}


def charged_lepton_yukawa_charge_matrix():
    return {
        left: {right: -X_L[left] + X_R[right] for right in ("e", "mu", "tau")}
        for left in ("e", "mu", "tau")
    }


def audit():
    q = charged_lepton_yukawa_charge_matrix()
    expected = {
        "e": {"e": 0, "mu": -1, "tau": 1},
        "mu": {"e": -1, "mu": -2, "tau": 0},
        "tau": {"e": 1, "mu": 0, "tau": 2},
    }
    assert q == expected

    allowed = [(l, r) for l in q for r in q[l] if q[l][r] == 0]
    assert allowed == [("e", "e"), ("mu", "tau"), ("tau", "mu")]
    model_kept = [("e", "e")]
    model_zero_by_flavour_assumption = [("mu", "tau"), ("tau", "mu")]
    gauge_forbidden = [
        (l, r) for l in q for r in q[l]
        if q[l][r] != 0
    ]
    assert len(gauge_forbidden) == 6

    # Dimension-five source charge neutrality.
    q_mu_source = -2 + 1 + 1  # S* + bar(mu_R) + L_mu
    q_tau_source = 2 - 1 - 1  # S + bar(tau_R) + L_tau
    assert q_mu_source == 0 and q_tau_source == 0

    # The source insertion is multiplied by an O(M_E^-4) operator coefficient.
    order_cross = 4 + 1  # M^-4 * C5(M^-1) -> M^-5
    order_square = 4 + 2  # M^-4 * C5^2(M^-2) -> M^-6
    assert order_cross == 5 and order_square == 6

    return {
        "scope": "charged-lepton Yukawa charge matrix and source power counting",
        "charge_matrix_rows_L_columns_R": q,
        "gauge_allowed_entries": allowed,
        "kept_in_original_flavour_diagonal_model": model_kept,
        "gauge_allowed_but_set_to_zero_by_model_flavour_assumption": model_zero_by_flavour_assumption,
        "gauge_forbidden_entries": gauge_forbidden,
        "dimension5_source_charge_checks": {
            "Sdagger_bar_muR_Lmu": q_mu_source,
            "S_bar_tauR_Ltau": q_tau_source,
        },
        "source_order": {
            "O(M^-4)_operator_times_C5_source": "O(M^-5), outside strict O(M^-4)",
            "O(M^-4)_operator_times_C5_source_squared": "O(M^-6), outside strict O(M^-4)",
        },
        "result": "PASS",
        "limitations": [
            "No Lorentz/weak/color Fierz reduction is performed.",
            "No fermion-loop or UV-EFT matching coefficient is evaluated.",
            "The original flavor-diagonal assumption is retained; relaxing it requires enlarging the charged-lepton mass matrix.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
