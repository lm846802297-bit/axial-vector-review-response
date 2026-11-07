#!/usr/bin/env python3
"""Independent direct forward/reverse collision-integral audit.

P0 scope:
  * neutrino coalescence / inverse decay: independent adaptive angular
    quadrature of f f and (1-f)(1-f), mode by mode and flavor by flavor;
  * semi-Compton: independent direct Bose-factor thermal integrals in the
    published B.14--B.19 non-recoil approximation, mode by mode.

This is a validation script, not a replacement production rate solver.
The Compton calculation here deliberately uses E_gamma ~= omega and the
B.14 Thomson/no-recoil kernel. It is NOT the full moving-muon B.13 thermal
phase-space integral. The separate exact-recoil fixed-target B.19
collision-integrand regression remains in test_stage1_detailed_balance.py.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import expit

import rates

HERE = Path(__file__).resolve().parent


def _fermi(energy: float, chemical: float, temperature: float) -> float:
    return float(expit((chemical - energy) / temperature))


def direct_neutrino_rates(mass: float, energy: float, temperature: float,
                          mu_numu: float, epsrel: float = 3e-12):
    """Direct adaptive integrals for nu_mu and nu_tau, separately.

    Returns arrays (flavor, mode) for production and absorption. The two
    collision terms are integrated independently; neither is obtained from
    the other by a Boltzmann factor.
    """
    if mass <= 0 or energy < mass or temperature <= 0:
        raise ValueError("Require mass>0, energy>=mass, temperature>0")
    k = np.sqrt(max(energy * energy - mass * mass, 0.0))
    mode_weights = (
        lambda z: 3.0 * (1.0 - z*z) / 4.0,
        lambda z: 3.0 * (1.0 + z)**2 / 8.0,
        lambda z: 3.0 * (1.0 - z)**2 / 8.0,
    )
    production = np.zeros((2, 3))
    absorption = np.zeros((2, 3))
    for iflavor, chemical in enumerate((mu_numu, 0.0)):
        def occupations(z):
            e1 = 0.5 * (energy + k*z)
            e2 = 0.5 * (energy - k*z)
            f1 = _fermi(e1, chemical, temperature)
            f2 = _fermi(e2, -chemical, temperature)
            return f1, f2
        for h, weight in enumerate(mode_weights):
            def prod_integrand(z):
                f1, f2 = occupations(z)
                return weight(z) * f1 * f2
            def abs_integrand(z):
                f1, f2 = occupations(z)
                return weight(z) * (1.0-f1) * (1.0-f2)
            production[iflavor, h] = quad(
                prod_integrand, -1.0, 1.0, epsabs=1e-300,
                epsrel=epsrel, limit=250
            )[0]
            absorption[iflavor, h] = quad(
                abs_integrand, -1.0, 1.0, epsabs=1e-14,
                epsrel=epsrel, limit=250
            )[0]
    prefactor = mass*mass / (24.0*np.pi*energy)
    return prefactor*production, prefactor*absorption


def direct_muon_susceptibility(temperature: float, mu_mu: float):
    """Independent adaptive integral of both charge susceptibilities.

    n_eff = 2 int d^3p/(2 pi)^3 [f_-(1-f_-) + f_+(1-f_+)].
    The two spin states are included; units are MeV^3.
    """
    if temperature <= 0:
        raise ValueError("temperature must be positive")
    result = []
    for chemical in (mu_mu, -mu_mu):
        def integrand(momentum):
            energy = np.hypot(momentum, rates.M_MU)
            f = _fermi(energy, chemical, temperature)
            return momentum*momentum*f*(1.0-f)
        value = quad(integrand, 0.0, np.inf, epsabs=1e-12,
                     epsrel=2e-11, limit=400)[0] / np.pi**2
        result.append(value)
    return tuple(float(x) for x in result)


def direct_b14_compton_rates(mass: float, energy: float, temperature: float,
                             n_mu_eff: float):
    """Direct B.14--B.19 no-recoil thermal integrals, for L,+,-.

    The inverse rate is integrated with (1+f_gamma); the forward rate is
    integrated independently with f_gamma. In this approximation
    E_gamma=omega and v*sigma_abs,h = 2 alpha/(3 m_mu^2) *
    (m_V^2/omega^2, 1, 1). No detailed-balance relation is used to construct
    either rate.
    """
    if mass <= 0 or energy <= mass or temperature <= 0 or n_mu_eff < 0:
        raise ValueError("Require mass>0, energy>mass, T>0, n_mu_eff>=0")
    x = energy/temperature
    bose = 1.0/np.expm1(x)
    v_sigma = (2.0*rates.ALPHA/(3.0*rates.M_MU**2)
               * np.array([(mass/energy)**2, 1.0, 1.0]))
    production = n_mu_eff * v_sigma * bose
    absorption = n_mu_eff * v_sigma * (1.0 + bose)

    # Independent spin-summed B.14/B.16 normalization at unit g_X:
    # alpha_V=g_X^2/(4 pi)=1/(4 pi), and the photon degeneracy gives 2.
    alpha_v = 1.0/(4.0*np.pi)
    sigma_prod_over_v = (
        8.0*np.pi*rates.ALPHA*alpha_v/(3.0*rates.M_MU**2)
        * (1.0 + mass*mass/(2.0*energy*energy))
    )
    production_b14_sum = 2.0*n_mu_eff*sigma_prod_over_v*bose
    return production, absorption, float(production_b14_sum)


def _relative_error(actual, reference):
    a, b = np.asarray(actual, float), np.asarray(reference, float)
    return float(np.max(np.abs(a-b)/np.maximum(np.abs(b), 1e-300)))


def run_audit(profile_path: Path):
    profile = np.genfromtxt(profile_path, delimiter=",", names=True)
    radii = (0.0, 5.0, 8.0, 10.0, 15.0)
    masses = (1.0, 10.0, 100.0, 200.0)
    energy_factors = (1.05, 1.5, 3.0)
    neutrino_rows = []
    compton_rows = []
    max_neutrino_prod_error = 0.0
    max_neutrino_abs_error = 0.0
    max_neutrino_balance_error = 0.0
    max_compton_balance_error = 0.0
    max_compton_b14_sum_error = 0.0

    for radius in radii:
        t = float(np.interp(radius, profile["r_km"], profile["T_MeV"]))
        mu_nu = float(np.interp(radius, profile["r_km"], profile["mu_numu_MeV"]))
        mu_mu = float(np.interp(radius, profile["r_km"], profile["mu_mu_MeV"]))
        nminus, nplus = direct_muon_susceptibility(t, mu_mu)
        nmu = nminus+nplus
        for mass in masses:
            for factor in energy_factors:
                energy = mass*factor
                p_flavor, a_flavor = direct_neutrino_rates(
                    mass, energy, t, mu_nu
                )
                p_direct, a_direct = p_flavor.sum(axis=0), a_flavor.sum(axis=0)
                p_code, a_code = rates.neutrino_rates(
                    mass, np.array([energy]), t, mu_nu, order=96
                )
                p_code, a_code = p_code[0], a_code[0]
                p_error = _relative_error(p_code, p_direct)
                a_error = _relative_error(a_code, a_direct)
                ratios = a_direct/p_direct
                expected = np.full(3, np.exp(energy/t))
                balance_error = _relative_error(ratios, expected)
                max_neutrino_prod_error = max(max_neutrino_prod_error, p_error)
                max_neutrino_abs_error = max(max_neutrino_abs_error, a_error)
                max_neutrino_balance_error = max(max_neutrino_balance_error, balance_error)
                neutrino_rows.append({
                    "r_km": radius, "mass_MeV": mass, "omega_MeV": energy,
                    "T_MeV": t, "mu_numu_MeV": mu_nu,
                    "production_by_flavor_mode": p_flavor.tolist(),
                    "absorption_by_flavor_mode": a_flavor.tolist(),
                    "production_total_by_mode": p_direct.tolist(),
                    "absorption_total_by_mode": a_direct.tolist(),
                    "absorption_over_production_by_mode": ratios.tolist(),
                    "expected_exp_omega_over_T": float(np.exp(energy/t)),
                    "max_direct_vs_rates_production_relative_error": p_error,
                    "max_direct_vs_rates_absorption_relative_error": a_error,
                    "max_mode_detailed_balance_relative_error": balance_error,
                })

                p_compton, a_compton, p_b14 = direct_b14_compton_rates(
                    mass, energy, t, nmu
                )
                c_balance = _relative_error(a_compton/p_compton, expected)
                c_sum = float(np.sum(p_compton))
                c_sum_error = abs(c_sum-p_b14)/max(abs(p_b14), 1e-300)
                max_compton_balance_error = max(max_compton_balance_error, c_balance)
                max_compton_b14_sum_error = max(max_compton_b14_sum_error, c_sum_error)
                compton_rows.append({
                    "r_km": radius, "mass_MeV": mass, "omega_MeV": energy,
                    "T_MeV": t, "mu_mu_MeV": mu_mu,
                    "n_mu_minus_eff_MeV3": nminus,
                    "n_mu_plus_eff_MeV3": nplus,
                    "n_mu_total_eff_MeV3": nmu,
                    "positive_muon_fraction": nplus/nmu if nmu else 0.0,
                    "production_direct_by_mode": p_compton.tolist(),
                    "absorption_direct_by_mode": a_compton.tolist(),
                    "absorption_over_production_by_mode":
                        (a_compton/p_compton).tolist(),
                    "expected_exp_omega_over_T": float(np.exp(energy/t)),
                    "production_sum_B14_B16": p_b14,
                    "production_sum_from_modes": c_sum,
                    "B14_spin_sum_relative_error": c_sum_error,
                    "mode_detailed_balance_relative_error": c_balance,
                })

    return {
        "title": "Independent direct forward/reverse collision-integral audit",
        "scope": (
            "Neutrino rates: independent adaptive angular integration of both "
            "ff and (1-f)(1-f), per flavor and polarization. Compton: direct "
            "B.14-B.19 Bose-factor thermal integrals in the published "
            "non-recoil approximation, per polarization."
        ),
        "limitations": [
            "Compton B.14 integral uses E_gamma=omega and the analytic no-recoil kernel.",
            "It is not the full moving-muon thermal phase-space integral of B.13.",
            "The exact-recoil fixed-target collision-integrand identity is separately tested in test_stage1_detailed_balance.py.",
            "The current profile's n_mu_eff includes both mu- and mu+ susceptibilities; the source's charge-conjugate convention remains separately documented as an ambiguity.",
            "These local rate tests do not by themselves validate the stellar transport or the complete Fig. 7 curve."
        ],
        "configuration": {
            "radii_km": list(radii), "masses_MeV": list(masses),
            "omega_over_mass": list(energy_factors),
            "neutrino_adaptive_epsrel": 3e-12,
            "neutrino_code_gauss_legendre_order": 96,
            "muon_susceptibility_adaptive_epsrel": 2e-11,
        },
        "summary": {
            "neutrino_cases": len(neutrino_rows),
            "compton_cases": len(compton_rows),
            "max_neutrino_production_vs_code_relative_error": max_neutrino_prod_error,
            "max_neutrino_absorption_vs_code_relative_error": max_neutrino_abs_error,
            "max_neutrino_mode_balance_relative_error": max_neutrino_balance_error,
            "max_compton_mode_balance_relative_error": max_compton_balance_error,
            "max_compton_B14_spin_sum_relative_error": max_compton_b14_sum_error,
        },
        "neutrino": neutrino_rows,
        "compton_B14_direct_thermal_integrals": compton_rows,
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "sha256": {
            "script": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "rates_py": hashlib.sha256((HERE/"rates.py").read_bytes()).hexdigest(),
            "profile": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=HERE/"data"/"sfho188_digitized.csv")
    parser.add_argument("--output", type=Path,
                        default=HERE/"outputs"/"direct_collision_integrals_2026-11-07.json")
    args = parser.parse_args()
    result = run_audit(args.profile)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
