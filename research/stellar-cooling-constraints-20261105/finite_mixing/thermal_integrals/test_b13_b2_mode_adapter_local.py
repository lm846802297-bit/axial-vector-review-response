#!/usr/bin/env python3
"""Local pointwise adapter check: exact B.13 Compton + mode-resolved neutrino rates."""
from __future__ import annotations
import json
import math
import sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from blinov_reproduction.reference import load_profile, decay_production
from finite_mixing.moving_muon_compton import moving_muon_compton_rates
from rates import neutrino_rates

PROFILE = ROOT / "data" / "sfho188_digitized.csv"
MASS = 10.0
RADIUS = 8.24821831451522
ORDERS = (26, 14, 14, 14)
X_VALUES = (0.0, 0.015, 0.05)


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def mode_ratio(values):
    return float(values[0] / (0.5 * (values[1] + values[2])))


def main():
    bg = load_profile(PROFILE, np.array([RADIUS]))
    temperature = float(bg["T"][0])
    mu_mu = float(bg["mu_mu"][0])
    mu_numu = float(bg["mu_numu"][0])
    output = {
        "profile": PROFILE.name,
        "radius_km": RADIUS,
        "T_MeV": temperature,
        "mu_mu_MeV": mu_mu,
        "mu_numu_MeV": mu_numu,
        "orders": list(ORDERS),
        "points": [],
    }

    for x in X_VALUES:
        omega = MASS + x * temperature
        compton = moving_muon_compton_rates(
            MASS, omega, temperature, mu_mu,
            g_vector=1.0, g_axial=0.0, orders=ORDERS,
        )
        nu_prod, nu_abs = neutrino_rates(
            MASS, omega, temperature, mu_numu, order=64
        )

        mu_minus_prod = np.asarray(
            compton["charge_resolved"]["mu_minus"]["production"], float
        )
        mu_minus_abs = np.asarray(
            compton["charge_resolved"]["mu_minus"]["absorption"], float
        )
        mu_plus_prod = np.asarray(
            compton["charge_resolved"]["mu_plus"]["production"], float
        )
        mu_plus_abs = np.asarray(
            compton["charge_resolved"]["mu_plus"]["absorption"], float
        )
        charge_sum_prod = mu_minus_prod + mu_plus_prod
        charge_sum_abs = mu_minus_abs + mu_plus_abs

        boltzmann = math.exp(-omega / temperature)
        compton_db = max(
            rel(
                float(compton["charge_resolved"][charge]["production"][mode]),
                boltzmann * float(compton["charge_resolved"][charge]["absorption"][mode]),
            )
            for charge in ("mu_minus", "mu_plus")
            for mode in range(3)
        )
        neutrino_db = max(
            rel(float(nu_prod[mode]), boltzmann * float(nu_abs[mode]))
            for mode in range(3)
        )
        nu_scalar, _ = decay_production(
            MASS, omega, temperature, mu_numu, mu_mu
        )
        neutrino_closure = rel(float(np.sum(nu_prod)), float(nu_scalar))
        charge_closure = max(
            rel(float(compton["production"][mode]), float(charge_sum_prod[mode]))
            for mode in range(3)
        )
        charge_closure = max(
            charge_closure,
            max(
                rel(float(compton["absorption"][mode]), float(charge_sum_abs[mode]))
                for mode in range(3)
            ),
        )

        total_prod_minus = mu_minus_prod + nu_prod
        total_abs_minus = mu_minus_abs + nu_abs
        total_prod_sum = charge_sum_prod + nu_prod
        total_abs_sum = charge_sum_abs + nu_abs
        reduced_nu = (1.0 - boltzmann) * nu_abs
        reduced_total_minus = (1.0 - boltzmann) * total_abs_minus
        reduced_total_sum = (1.0 - boltzmann) * total_abs_sum

        output["points"].append({
            "x": x,
            "omega_local_MeV": omega,
            "compton_absorption_mu_minus": mu_minus_abs.tolist(),
            "compton_absorption_mu_plus": mu_plus_abs.tolist(),
            "compton_absorption_charge_sum": charge_sum_abs.tolist(),
            "neutrino_absorption_modes": nu_abs.tolist(),
            "total_absorption_modes_mu_minus_lane": total_abs_minus.tolist(),
            "total_absorption_modes_charge_sum_lane": total_abs_sum.tolist(),
            "compton_L_over_T_mu_minus": mode_ratio(mu_minus_abs),
            "compton_L_over_T_mu_plus": mode_ratio(mu_plus_abs),
            "compton_L_over_T_charge_sum": mode_ratio(charge_sum_abs),
            "neutrino_L_over_T": mode_ratio(nu_abs),
            "total_L_over_T_mu_minus_lane": mode_ratio(total_abs_minus),
            "total_L_over_T_charge_sum_lane": mode_ratio(total_abs_sum),
            "compton_fraction_of_total_absorption_mu_minus_lane":
                float(np.sum(mu_minus_abs) / np.sum(total_abs_minus)),
            "compton_fraction_of_total_absorption_charge_sum_lane":
                float(np.sum(charge_sum_abs) / np.sum(total_abs_sum)),
            "compton_fraction_by_mode_mu_minus_lane":
                (mu_minus_abs / total_abs_minus).tolist(),
            "compton_fraction_by_mode_charge_sum_lane":
                (charge_sum_abs / total_abs_sum).tolist(),
            "total_production_modes_mu_minus_lane": total_prod_minus.tolist(),
            "total_production_modes_charge_sum_lane": total_prod_sum.tolist(),
            "total_reduced_absorption_modes_mu_minus_lane":
                reduced_total_minus.tolist(),
            "total_reduced_absorption_modes_charge_sum_lane":
                reduced_total_sum.tolist(),
            "neutrino_reduced_absorption_modes": reduced_nu.tolist(),
            "charge_sum_closure_residual": charge_closure,
            "neutrino_sum_closure_residual": neutrino_closure,
            "compton_detailed_balance_residual": compton_db,
            "neutrino_detailed_balance_residual": neutrino_db,
            "transverse_plus_minus_relative_difference_mu_minus":
                rel(mu_minus_abs[1], mu_minus_abs[2]),
            "transverse_plus_minus_relative_difference_mu_plus":
                rel(mu_plus_abs[1], mu_plus_abs[2]),
        })

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
