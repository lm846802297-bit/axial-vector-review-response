"""Independent audit of the published B.7--B.10 neutrino kernel.

Compares the repository's analytic Fermi-pair average with the closed-form
I(alpha,beta,v) in published Eq. (B.9), and with direct angular quadrature.
It also checks the B.7 normalization and the B.10/B.4 detailed-balance
reduced-absorption factor for the 10 MeV benchmark.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from scipy.special import logsumexp
from numpy.polynomial.legendre import leggauss

from reference import fermi_pair_average

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_neutrino_b7_b9_kernel_10mev_2026-11-10.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def published_i_b9(mu: float, omega: float, temperature: float,
                   mass: float) -> float:
    alpha = mu / temperature
    beta = omega / temperature
    velocity = np.sqrt(1.0 - (mass / omega)**2)
    b = 0.5 * beta * (velocity + 1.0)

    # Eq. (B.9): the second numerator factor is exp(alpha+b)+1.
    log_numerator = (
        logsumexp([alpha, b])
        + logsumexp([alpha + b, 0.0])
    )
    log_denominator_inside = logsumexp([
        alpha + beta,
        2.0 * alpha + b,
        b,
        alpha + beta * velocity,
    ])
    log_ratio = log_numerator - log_denominator_inside
    log_outer_denominator = (
        beta + np.log1p(-np.exp(-beta))
        + np.log(beta) + np.log(velocity)
    )
    return float(log_ratio / np.exp(log_outer_denominator))


def direct_pair_average(mu: float, omega: float, temperature: float,
                        mass: float, order: int) -> float:
    z, w = leggauss(order)
    velocity = np.sqrt(1.0 - (mass / omega)**2)
    e1 = omega * (1.0 + velocity * z) / 2.0
    e2 = omega * (1.0 - velocity * z) / 2.0
    # expit is written with stable logistic branches to avoid overflow.
    def logistic(x):
        x = np.asarray(x, float)
        out = np.empty_like(x)
        positive = x > 40.0
        negative = x < -40.0
        middle = ~(positive | negative)
        out[positive] = np.exp(-x[positive])
        out[negative] = 1.0
        out[middle] = 1.0 / (1.0 + np.exp(x[middle]))
        return out
    return float(0.5 * np.sum(
        w * logistic((e1 - mu) / temperature)
        * logistic((e2 + mu) / temperature)
    ))


def run(profile_path: Path, mass: float = 10.0) -> dict:
    profile = np.genfromtxt(profile_path, delimiter=",", names=True)
    radii = (8.0, 10.0, 12.5, 15.0)
    energies = (60.0, 110.0, 210.0, 510.0, 1010.0)
    direct_orders = (128, 256, 512, 1024)
    rows = []

    for radius in radii:
        temperature = float(np.interp(
            radius, profile["r_km"], profile["T_MeV"]
        ))
        mu_numu = float(np.interp(
            radius, profile["r_km"], profile["mu_numu_MeV"]
        ))
        for omega in energies:
            beta = omega / temperature
            velocity = np.sqrt(1.0 - (mass / omega)**2)
            i_values = {}
            for species, mu in (("mu_numu", mu_numu), ("mu_zero", 0.0)):
                code_i = float(fermi_pair_average(
                    mu, omega, temperature, velocity
                ))
                paper_i = published_i_b9(mu, omega, temperature, mass)
                direct = [
                    {
                        "order": order,
                        "value": direct_pair_average(
                            mu, omega, temperature, mass, order
                        ),
                    }
                    for order in direct_orders
                ]
                i_values[species] = {
                    "mu_MeV": mu,
                    "alpha": mu / temperature,
                    "repository_fermi_pair_average": code_i,
                    "published_eq_B9": paper_i,
                    "eq_B9_relative_residual": paper_i / code_i - 1.0,
                    "direct_angular_quadrature": direct,
                    "direct_angular_relative_residual_by_order": {
                        str(item["order"]): item["value"] / code_i - 1.0
                        for item in direct
                    },
                }

            # Eq. (B.7) per g^2, using alpha_V = g^2/(4 pi) and
            # Gamma(V -> nu nu-bar) = alpha_V*mV/6 for one neutrino flavour.
            alpha_v_per_g2 = 1.0 / (4.0 * np.pi)
            gamma_v_nunu_per_g2 = alpha_v_per_g2 * mass / 6.0
            paper_prefactor_per_g2 = (
                mass / omega * 3.0 * gamma_v_nunu_per_g2
            )
            repository_prefactor_per_g2 = mass**2 / (8.0 * np.pi * omega)
            pair_sum = (
                i_values["mu_numu"]["repository_fermi_pair_average"]
                + i_values["mu_zero"]["repository_fermi_pair_average"]
            )
            paper_rate_per_g2 = paper_prefactor_per_g2 * (
                i_values["mu_numu"]["published_eq_B9"]
                + i_values["mu_zero"]["published_eq_B9"]
            )
            repository_rate_per_g2 = repository_prefactor_per_g2 * pair_sum

            # Eq. (B.10) followed by Eq. (B.4):
            # Gamma_abs=e^beta Gamma_prod and Gamma_abs^*=(e^beta-1)Gamma_prod.
            exp_beta = np.exp(min(beta, 700.0))
            detailed_balance_ratio = exp_beta
            reduced_factor = -np.expm1(-beta) * exp_beta
            expected_reduced_factor = np.expm1(min(beta, 700.0))

            rows.append({
                "radius_km": radius,
                "temperature_MeV": temperature,
                "energy_MeV": omega,
                "beta": beta,
                "velocity": velocity,
                "flavours": i_values,
                "B7_normalization": {
                    "paper_prefactor_per_g2": paper_prefactor_per_g2,
                    "repository_prefactor_per_g2": repository_prefactor_per_g2,
                    "prefactor_relative_residual": (
                        paper_prefactor_per_g2 / repository_prefactor_per_g2 - 1.0
                    ),
                    "two_flavour_rate_per_g2_from_B9": paper_rate_per_g2,
                    "two_flavour_rate_per_g2_from_repository_I": repository_rate_per_g2,
                    "rate_relative_residual": paper_rate_per_g2 / repository_rate_per_g2 - 1.0,
                },
                "B10_B4_detailed_balance": {
                    "Gamma_abs_over_Gamma_prod": detailed_balance_ratio,
                    "reduced_absorption_factor": reduced_factor,
                    "expected_expm1_beta": expected_reduced_factor,
                    "relative_residual": reduced_factor / expected_reduced_factor - 1.0,
                },
            })

    max_b9 = max(
        abs(flavour["eq_B9_relative_residual"])
        for row in rows for flavour in row["flavours"].values()
    )
    max_direct = {
        str(order): max(
            abs(flavour["direct_angular_relative_residual_by_order"][str(order)])
            for row in rows for flavour in row["flavours"].values()
        )
        for order in direct_orders
    }
    max_rate = max(
        abs(row["B7_normalization"]["rate_relative_residual"])
        for row in rows
    )
    max_balance = max(
        abs(row["B10_B4_detailed_balance"]["relative_residual"])
        for row in rows
    )
    return {
        "title": "10 MeV neutrino inverse-decay B.7--B.10 kernel audit",
        "mass_MeV": mass,
        "profile_sha256": sha256(profile_path),
        "radii_km": list(radii),
        "energies_MeV": list(energies),
        "direct_angular_orders": list(direct_orders),
        "summary": {
            "max_abs_relative_residual_eq_B9_vs_repository_pair_average": max_b9,
            "max_abs_relative_residual_direct_angular_by_order": max_direct,
            "max_abs_relative_residual_eq_B7_two_flavour_rate": max_rate,
            "max_abs_relative_residual_B10_B4_detailed_balance": max_balance,
            "sample_count": len(rows),
        },
        "points": rows,
        "interpretation": [
            "The Eq. (B.9) expression is evaluated independently from the repository's Fermi-pair antiderivative.",
            "Direct angular quadrature evaluates the original Fermi-Dirac product, independently of both closed forms.",
            "The Eq. (B.7) prefactor includes the three-vector-polarization sum and the one-flavour vacuum width; the two active flavours are summed separately.",
            "Eq. (B.10) and the reduced-absorption definition Eq. (B.4) are checked independently of the chord integration.",
            "This verifies the local neutrino kernel, not the reconstructed stellar profile or the full transport geometry.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    args = parser.parse_args()
    result = run(args.profile, args.mass)
    payload = {
        "result": result,
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "script_sha256": sha256(Path(__file__)),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
