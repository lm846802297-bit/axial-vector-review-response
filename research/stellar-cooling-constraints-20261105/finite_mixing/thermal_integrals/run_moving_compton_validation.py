"""Reproducible local validation for the moving-muon semi-Compton kernel."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT))

import rates
from finite_mixing.thermal_integrals.moving_compton import (
    moving_compton_matrix_elements,
    moving_muon_compton_rates,
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def max_rel(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.max(np.abs(a-b)/np.maximum(np.abs(b), 1e-300)))


def matrix_element_checks():
    mass, omega = 10.0, 30.0
    cosines = np.array([-0.7, 0.1, 0.8])
    zeros = np.zeros_like(cosines)
    endpoint = {}
    for current, gv, ga in (("vector", 1.0, 0.0), ("axial", 0.0, 1.0)):
        _, _, value = moving_compton_matrix_elements(
            mass, omega, zeros, zeros, cosines, zeros, gv, ga
        )
        _, reference = rates.compton_matrix_elements(
            mass, [omega], cosines, current=current
        )
        endpoint[current] = max_rel(value, reference[0])

    args = (
        20.0, 45.0, np.array([25.0, 80.0]), np.array([0.2, -0.4]),
        np.array([-0.3, 0.7]), np.array([0.5, 2.1]), 0.2, -0.8,
    )
    photon_ward = 0.0
    for charge in ("mu_minus", "mu_plus"):
        _, _, ward = moving_compton_matrix_elements(
            *args, charge=charge, photon_ward=True
        )
        photon_ward = max(photon_ward, float(np.max(np.abs(ward))))
    _, _, vector_ward = moving_compton_matrix_elements(
        20.0, 45.0, np.array([25.0, 80.0]),
        np.array([0.2, -0.4]), np.array([-0.3, 0.7]),
        np.array([0.5, 2.1]), 1.0, 0.0,
        vector_mediator_ward=True,
    )
    _, _, plus = moving_compton_matrix_elements(*args, charge="mu_plus")
    flipped = args[:-1] + (-args[-1],)
    _, _, minus_flip = moving_compton_matrix_elements(
        *flipped, charge="mu_minus"
    )
    return {
        "stationary_endpoint_relative_residual": endpoint,
        "photon_ward_max_abs": photon_ward,
        "vector_mediator_ward_max_abs": float(np.max(np.abs(vector_ward[:, 0]))),
        "charge_conjugation_relative_residual": max_rel(plus, minus_flip),
    }


def interference_checks():
    settings = dict(
        mass=10.0, omega=25.0, temperature=20.0,
        radial_order=8, angular_order=4, azimuth_order=4, chunk_size=512,
    )

    def run(gv, ga, mu):
        return moving_muon_compton_rates(
            **settings, mu_mu=mu, g_vector=gv, g_axial=ga
        )["Gamma_abs_by_mode"]

    gv, ga = 0.2, -0.8
    mixed_zero = run(gv, ga, 0.0)
    vector_zero = run(1.0, 0.0, 0.0)
    axial_zero = run(0.0, 1.0, 0.0)
    incoherent_zero = gv*gv*vector_zero + ga*ga*axial_zero
    cancellation = max_rel(mixed_zero, incoherent_zero)

    mixed_asymmetric = run(gv, ga, 45.0)
    vector_asymmetric = run(1.0, 0.0, 45.0)
    axial_asymmetric = run(0.0, 1.0, 45.0)
    incoherent_asymmetric = gv*gv*vector_asymmetric + ga*ga*axial_asymmetric
    interference_size = float(np.max(np.abs(mixed_asymmetric-incoherent_asymmetric)))
    return {
        "zero_mu_charge_sum_interference_cancellation_relative_residual": cancellation,
        "nonzero_mu_interference_abs_max": interference_size,
    }


def thermal_convergence_case(label, temperature, mu_mu):
    common = dict(
        mass=10.0, omega=25.0, temperature=temperature, mu_mu=mu_mu,
        g_vector=0.15, g_axial=-0.85, chunk_size=8192,
    )
    coarse = moving_muon_compton_rates(
        **common, radial_order=24, angular_order=12, azimuth_order=20
    )
    fine = moving_muon_compton_rates(
        **common, radial_order=48, angular_order=16, azimuth_order=24
    )
    return {
        "temperature_MeV": temperature,
        "muon_chemical_potential_MeV": mu_mu,
        "coarse_absorption_by_mode": [float(x) for x in coarse["Gamma_abs_by_mode"]],
        "fine_absorption_by_mode": [float(x) for x in fine["Gamma_abs_by_mode"]],
        "relative_difference_absorption": max_rel(
            coarse["Gamma_abs_by_mode"], fine["Gamma_abs_by_mode"]
        ),
        "coarse_detailed_balance_residual": coarse["max_detailed_balance_relative_residual"],
        "fine_detailed_balance_residual": fine["max_detailed_balance_relative_residual"],
        "mu_minus_fraction_by_mode": [
            float(x) for x in (
                fine["charge_contributions"]["mu_minus"]["Gamma_abs_by_mode"]
                / fine["Gamma_abs_by_mode"]
            )
        ],
        "total_quadrature_points_all_charges_fine": fine["total_quadrature_points_all_charges"],
    }


def main():
    checks = matrix_element_checks()
    interference = interference_checks()
    convergence = {
        "nondegenerate_muon_gas": thermal_convergence_case(
            "nondegenerate", 20.0, 45.0
        ),
        "degenerate_core_like_gas": thermal_convergence_case(
            "degenerate", 19.3, 254.9
        ),
    }
    max_quad = max(x["relative_difference_absorption"] for x in convergence.values())
    max_balance = max(
        max(x["coarse_detailed_balance_residual"], x["fine_detailed_balance_residual"])
        for x in convergence.values()
    )
    max_endpoint = max(checks["stationary_endpoint_relative_residual"].values())
    acceptance = {
        "stationary_endpoint_pass": max_endpoint < 2e-12,
        "photon_ward_pass": checks["photon_ward_max_abs"] < 2e-9,
        "vector_mediator_ward_pass": checks["vector_mediator_ward_max_abs"] < 2e-9,
        "charge_conjugation_pass": checks["charge_conjugation_relative_residual"] < 2e-13,
        "zero_mu_interference_cancellation_pass": (
            interference["zero_mu_charge_sum_interference_cancellation_relative_residual"] < 3e-10
        ),
        "nonzero_mu_interference_retained": interference["nonzero_mu_interference_abs_max"] > 1e-12,
        "quadrature_convergence_pass": max_quad < 5e-4,
        "detailed_balance_pass": max_balance < 1e-10,
        "max_stationary_endpoint_relative_residual": max_endpoint,
        "max_thermal_quadrature_relative_difference": max_quad,
        "max_detailed_balance_relative_residual": max_balance,
    }
    payload = {
        "title": "Moving-muon semi-Compton local-rate validation",
        "scope": "Fixed mediator energy local rates only; no stellar luminosity or transport.",
        "units": {"energy_momentum_temperature": "MeV", "rates": "MeV"},
        "method": {
            "phase_space": "Exact 2<->2 collision integral with final-state delta eliminated analytically",
            "angular_quadrature": "Gauss-Legendre in cos(theta_p), cos(theta_gamma); periodic trapezoid in relative azimuth",
            "charge_species": "mu- and mu+ integrated separately with chemical potentials +mu_mu and -mu_mu",
            "current": "Coherent vector-axial amplitude; charge-conjugate interference sign retained",
            "production_absorption": "Independent Fermi/Bose statistical factors on common invariant phase space",
        },
        "source_sha256": {
            "rates.py": sha256(ROOT / "rates.py"),
            "moving_compton.py": sha256(HERE / "moving_compton.py"),
            "test_moving_compton.py": sha256(HERE / "test_moving_compton.py"),
            "derivation.md": sha256(HERE.parent / "MOVING_MUON_SEMI_COMPTON_DERIVATION_2026-11-07.md"),
        },
        "matrix_element_checks": checks,
        "interference_checks": interference,
        "thermal_convergence": convergence,
        "acceptance": acceptance,
    }
    output = HERE / "outputs" / "moving_compton_validation.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(acceptance, indent=2))
    if not all(value for key, value in acceptance.items() if key.endswith("_pass") or key.endswith("_retained")):
        raise SystemExit("Moving-muon semi-Compton validation failed")


if __name__ == "__main__":
    main()
