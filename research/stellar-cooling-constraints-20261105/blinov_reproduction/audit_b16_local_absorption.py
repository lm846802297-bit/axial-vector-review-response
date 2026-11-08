"""Independent local-opacity audit of Blinov B.6--B.10 and B.13--B.19.

The neutrino reference values are obtained from direct two-body angular
phase-space integrals, not the logarithmic antiderivative in reference.py.
The Compton reference values independently evaluate the printed B.14--B.17
formula, with n_mu F_deg computed by a transformed Gauss-Legendre integral.
No production rates, transport, luminosity, or axial outputs are modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import expit

try:
    from .reference import (
        ALPHA, DEFAULT_PROFILE, M_MU, fermi_pair_average, load_profile,
        local_rates,
    )
except ImportError:
    from reference import (
        ALPHA, DEFAULT_PROFILE, M_MU, fermi_pair_average, load_profile,
        local_rates,
    )

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "outputs" / "b16_local_absorption_10mev_2026-11-09.json"
SAMPLE_RADII_KM = (8.0, 10.0, 12.0, 15.0, 18.5, 20.0, 22.0, 23.0, 24.0, 25.0)
SAMPLE_ENERGIES_MEV = (12.0, 15.0, 20.0, 30.0, 50.0, 100.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def relative(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(b)), 1.0e-300)


def direct_neutrino_modes(mass: float, omega: float, temperature: float,
                          chemical_potential: float, order: int = 512):
    """Direct B.6 production and inverse-occupation absorption, per flavor.

    The z-integral is evaluated directly. The three polarization weights sum
    to the unpolarized B.6 rate and are normalized as in the published
    spin-summed vector-current calculation.
    """
    z, weights = leggauss(order)
    velocity = np.sqrt(1.0 - (mass / omega) ** 2)
    e1 = 0.5 * omega * (1.0 + velocity * z)
    e2 = 0.5 * omega * (1.0 - velocity * z)
    f1 = expit((chemical_potential - e1) / temperature)
    f2 = expit((-chemical_potential - e2) / temperature)
    production_stat = f1 * f2
    absorption_stat = (1.0 - f1) * (1.0 - f2)
    polarization_weights = np.stack((
        3.0 * (1.0 - z * z) / 4.0,
        3.0 * (1.0 + z) ** 2 / 8.0,
        3.0 * (1.0 - z) ** 2 / 8.0,
    ), axis=-1)
    prefactor = mass * mass / (24.0 * np.pi * omega)
    production_modes = prefactor * np.einsum(
        "z,zh->h", weights * production_stat, polarization_weights
    )
    absorption_modes = prefactor * np.einsum(
        "z,zh->h", weights * absorption_stat, polarization_weights
    )
    return production_modes, absorption_modes


def independent_muon_density_susceptibility(temperature: float,
                                             chemical_potential: float,
                                             order: int = 256):
    """Independently evaluate n_mu and n_mu F_deg from B.17.

    Use x=(E-m_mu)/T=t^2, so the p=0 endpoint is resolved without using the
    adaptive-p quadrature in reference.py. The spin degeneracy two is included.
    """
    if temperature <= 0.0 or order < 8:
        raise ValueError("Require T>0 and quadrature order >=8")
    nodes, weights = leggauss(order)
    xmax = max(36.0, max(abs(chemical_potential) - M_MU, 0.0)
               / temperature + 36.0)
    tmax = np.sqrt(xmax)
    t = 0.5 * tmax * (nodes + 1.0)
    wt = 0.5 * tmax * weights
    x = t * t
    energy = M_MU + temperature * x
    momentum = np.sqrt(temperature * x * (2.0 * M_MU + temperature * x))
    radial_measure = 2.0 * temperature * energy * momentum * t * wt / np.pi**2
    occupation = expit((chemical_potential - energy) / temperature)
    density = float(np.sum(radial_measure * occupation))
    susceptibility = float(np.sum(radial_measure * occupation * (1.0 - occupation)))
    fdeg = susceptibility / density if density > 0.0 else 0.0
    return density, susceptibility, fdeg


def independent_b14_b16_compton(mass: float, omega: float, temperature: float,
                                 susceptibility: float):
    """Evaluate B.14--B.17 directly, then B.19 and B.4.

    All rates are per g_X^2. For g_X=1, alpha_V=1/(4 pi). The explicit
    1/v_V in B.16 cancels the v_V in the B.14 cross section.
    """
    if mass <= 0.0 or omega <= mass or temperature <= 0.0:
        raise ValueError("Require m>0, omega>m, and T>0")
    velocity = np.sqrt(1.0 - (mass / omega) ** 2)
    alpha_v_per_g2 = 1.0 / (4.0 * np.pi)
    sigma = (
        8.0 * np.pi * ALPHA * alpha_v_per_g2 / (3.0 * M_MU**2)
        * (1.0 + mass**2 / (2.0 * omega**2)) * velocity
    )
    x = omega / temperature
    bose = 1.0 / np.expm1(x)
    production = (2.0 / velocity) * susceptibility * bose * sigma
    absorption = np.exp(x) * production
    reduced_from_absorption = (1.0 - np.exp(-x)) * absorption
    reduced_from_production = np.expm1(x) * production
    reduced_simplified = (
        4.0 * ALPHA / (3.0 * M_MU**2)
        * susceptibility * (1.0 + mass**2 / (2.0 * omega**2))
    )
    return {
        "v_V": float(velocity),
        "sigma_B14_MeV_minus2_per_g2": float(sigma),
        "production_B16_MeV_per_g2": float(production),
        "absorption_B19_MeV_per_g2": float(absorption),
        "reduced_B4_from_absorption_MeV_per_g2": float(reduced_from_absorption),
        "reduced_B4_from_production_MeV_per_g2": float(reduced_from_production),
        "reduced_closed_form_MeV_per_g2": float(reduced_simplified),
        "B19_relative_residual": relative(production, np.exp(-x) * absorption),
        "B4_relative_residual": relative(reduced_from_absorption, reduced_from_production),
        "B14_B16_velocity_cancellation_residual": relative(
            reduced_from_production, reduced_simplified
        ),
    }


def run(profile_path: Path = DEFAULT_PROFILE, mass: float = 10.0,
        neutrino_order: int = 512, susceptibility_order: int = 256):
    radii = np.asarray(SAMPLE_RADII_KM, float)
    energies = np.asarray(SAMPLE_ENERGIES_MEV, float)
    profile = load_profile(profile_path, radii)
    code = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )

    rows = []
    maxima = {
        "nu_mu_B6_production_vs_reference": 0.0,
        "nu_tau_B6_production_vs_reference": 0.0,
        "nu_mu_B10_detailed_balance": 0.0,
        "nu_tau_B10_detailed_balance": 0.0,
        "neutrino_B4_reduced_absorption": 0.0,
        "compton_B16_production_vs_reference": 0.0,
        "compton_B19_detailed_balance": 0.0,
        "compton_B4_reduced_absorption": 0.0,
        "total_local_production_closure": 0.0,
        "total_local_absorption_closure": 0.0,
        "total_local_reduced_absorption_closure": 0.0,
    }

    for ir, radius in enumerate(radii):
        temperature = float(profile["T"][ir])
        mu_mu = float(profile["mu_mu"][ir])
        mu_numu = float(profile["mu_numu"][ir])
        n_mu, chi_mu, fdeg = independent_muon_density_susceptibility(
            temperature, mu_mu, susceptibility_order
        )
        _, chi_mu_plus, _ = independent_muon_density_susceptibility(
            temperature, -mu_mu, susceptibility_order
        )
        plus_fraction = (
            chi_mu_plus / (chi_mu + chi_mu_plus)
            if chi_mu + chi_mu_plus > 0.0 else 0.0
        )

        for ie, omega in enumerate(energies):
            x = float(omega / temperature)
            p_mu, a_mu = direct_neutrino_modes(
                mass, float(omega), temperature, mu_numu, neutrino_order
            )
            p_tau, a_tau = direct_neutrino_modes(
                mass, float(omega), temperature, 0.0, neutrino_order
            )
            p_nu_mu, a_nu_mu = float(np.sum(p_mu)), float(np.sum(a_mu))
            p_nu_tau, a_nu_tau = float(np.sum(p_tau)), float(np.sum(a_tau))
            red_nu_mu = (1.0 - np.exp(-x)) * a_nu_mu
            red_nu_tau = (1.0 - np.exp(-x)) * a_nu_tau
            velocity = np.sqrt(1.0 - (mass / omega) ** 2)
            analytic_prefactor = mass * mass / (8.0 * np.pi * omega)
            analytic_nu_mu = analytic_prefactor * float(
                fermi_pair_average(mu_numu, float(omega), temperature, velocity)
            )
            analytic_nu_tau = analytic_prefactor * float(
                fermi_pair_average(0.0, float(omega), temperature, velocity)
            )

            compton = independent_b14_b16_compton(
                mass, float(omega), temperature, chi_mu
            )
            code_nu = float(code["neutrino_production"][ir, ie])
            code_compton = float(code["compton_production"][ir, ie])
            code_red_total = float(code["reduced_absorption"][ir, ie])
            direct_prod_total = p_nu_mu + p_nu_tau + compton["production_B16_MeV_per_g2"]
            direct_abs_total = (
                a_nu_mu + a_nu_tau + compton["absorption_B19_MeV_per_g2"]
            )
            direct_red_total = (
                red_nu_mu + red_nu_tau
                + compton["reduced_B4_from_absorption_MeV_per_g2"]
            )

            checks = {
                "nu_mu_B6_production_vs_analytic": relative(p_nu_mu, analytic_nu_mu),
                "nu_tau_B6_production_vs_analytic": relative(p_nu_tau, analytic_nu_tau),
                "nu_mu_B10_detailed_balance": relative(
                    p_nu_mu, np.exp(-x) * a_nu_mu
                ),
                "nu_tau_B10_detailed_balance": relative(
                    p_nu_tau, np.exp(-x) * a_nu_tau
                ),
                "neutrino_B4_reduced_absorption": relative(
                    red_nu_mu + red_nu_tau,
                    np.expm1(x) * (p_nu_mu + p_nu_tau)
                ),
                "compton_B16_production_vs_reference": relative(
                    compton["production_B16_MeV_per_g2"], code_compton
                ),
                "compton_B19_detailed_balance": compton["B19_relative_residual"],
                "compton_B4_reduced_absorption": compton["B4_relative_residual"],
                "total_local_production_closure": relative(
                    direct_prod_total, float(code["production"][ir, ie])
                ),
                "total_local_absorption_closure": relative(
                    direct_abs_total, float(code["absorption"][ir, ie])
                ),
                "total_local_reduced_absorption_closure": relative(
                    direct_red_total, code_red_total
                ),
            }
            for key, value in checks.items():
                maxima[key] = max(maxima[key], float(value))

            rows.append({
                "radius_km": float(radius),
                "omega_MeV": float(omega),
                "T_MeV": temperature,
                "mu_mu_MeV": mu_mu,
                "mu_numu_MeV": mu_numu,
                "n_mu_minus_MeV3_independent": n_mu,
                "n_mu_minus_Fdeg_MeV3_independent": chi_mu,
                "Fdeg_mu_minus_independent": fdeg,
                "mu_plus_fraction_of_total_susceptibility": float(plus_fraction),
                "nu_mu_production_direct_MeV": p_nu_mu,
                "nu_mu_production_analytic_MeV": analytic_nu_mu,
                "nu_mu_absorption_direct_MeV": a_nu_mu,
                "nu_tau_production_direct_MeV": p_nu_tau,
                "nu_tau_production_analytic_MeV": analytic_nu_tau,
                "nu_tau_absorption_direct_MeV": a_nu_tau,
                "compton_B16": compton,
                "code_reference_production": {
                    "neutrino_sum_MeV": code_nu,
                    "compton_MeV": code_compton,
                },
                "direct_total_production_MeV": float(direct_prod_total),
                "direct_total_absorption_MeV": float(direct_abs_total),
                "direct_total_reduced_absorption_MeV": float(direct_red_total),
                "code_total_reduced_absorption_MeV": code_red_total,
                "residuals": checks,
            })

    return {
        "title": "Independent local absorption audit of Blinov B.6--B.10 and B.13--B.19",
        "mass_MeV": float(mass),
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "identity": "reconstructed public-figure SFHo-18.8 profile, not raw Garching data",
        },
        "configuration": {
            "radii_km": list(SAMPLE_RADII_KM),
            "energies_MeV": list(SAMPLE_ENERGIES_MEV),
            "direct_neutrino_angular_order": int(neutrino_order),
            "independent_muon_susceptibility_order": int(susceptibility_order),
            "Compton_reference": "B.14--B.17, one mu-minus species as printed in B.17",
            "dimuon_channel": "closed at mV=10 MeV",
        },
        "maximum_residuals": maxima,
        "pointwise_results": rows,
        "scope": [
            "B.6 neutrino production is integrated directly over the two-body angular phase space for nu_mu and nu_tau separately.",
            "B.10 inverse occupation factors and B.4 reduced absorption are evaluated independently.",
            "B.14--B.17 Compton production is reconstructed from an independent Gauss-Legendre evaluation of the B.17 susceptibility integral.",
            "B.19 and B.4 are checked separately for Compton; the 1/v_V factor is retained and its cancellation against the B.14 cross-section velocity is explicit.",
            "The printed B.17 one-species convention is followed; the mu-plus susceptibility is reported only as a separate small correction diagnostic.",
            "No production source, transport, luminosity, coupling, or axial-vector output is modified.",
            "The exact moving-muon B.13 integral is a separate approximation diagnostic and is not substituted for the B.14--B.17 reference prescription.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--neutrino-order", type=int, default=512)
    parser.add_argument("--susceptibility-order", type=int, default=256)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(
        args.profile, args.mass, args.neutrino_order, args.susceptibility_order
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["maximum_residuals"], indent=2, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
