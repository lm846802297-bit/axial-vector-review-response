"""Compare Croon Eq. (4.6) with Blinov B.7--B.9 for two L_mu-L_tau flavours.

The B.7 rate is polarization-summed and retains the Fermi-Dirac pair average.
Croon Eq. (4.6) is evaluated literally with its Bose factor and printed
coefficient. All returned rates are per g_X^2, in MeV.

This is a local production-rate comparison only; it is not a luminosity or
transport calculation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

M_MU_MEV = 105.6583755
HERE = Path(__file__).resolve().parent
DEFAULT_PROFILE = HERE.parent / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "croon_blinov_neutrino_rate_comparison_2026-11-19.json"


def _fermi(x: np.ndarray) -> np.ndarray:
    """Stable Fermi-Dirac occupation."""
    return np.exp(-np.logaddexp(0.0, np.asarray(x, dtype=float)))


def _validate(mass: float, omega: float, temperature: float, mu_nu: float) -> None:
    values = np.asarray([mass, omega, temperature, mu_nu], dtype=float)
    if not np.all(np.isfinite(values)):
        raise ValueError("All inputs must be finite")
    if mass <= 0.0 or omega <= mass or temperature <= 0.0:
        raise ValueError("Require mass>0, omega>mass, and temperature>0")


def vector_speed(mass: float, omega: float) -> float:
    if mass <= 0.0 or omega <= mass:
        raise ValueError("Require 0 < mass < omega")
    return float(np.sqrt(1.0 - (mass / omega) ** 2))


def bose_occupation(omega: float, temperature: float) -> float:
    if omega <= 0.0 or temperature <= 0.0:
        raise ValueError("Require omega>0 and temperature>0")
    beta = omega / temperature
    if beta > 700.0:
        return float(np.exp(-beta))
    return float(1.0 / np.expm1(beta))


def fermi_pair_average(
    mu_nu: float,
    omega: float,
    temperature: float,
    velocity: float,
    order: int = 256,
) -> float:
    """Direct B.6 angular average of fbar(E1;-mu_nu) fnu(E2;mu_nu).

    E1,2 = omega/2 (1 +/- velocity*cos(theta)); weights are normalized
    to (1/2) integral_{-1}^{+1} d cos(theta).
    """
    if temperature <= 0.0 or omega <= 0.0 or not 0.0 <= velocity < 1.0:
        raise ValueError("Require T>0, omega>0, and 0<=velocity<1")
    if order < 8:
        raise ValueError("Gauss-Legendre order must be at least 8")
    cosine, weights = leggauss(order)
    weights = weights / 2.0
    e_bar = omega * (1.0 + velocity * cosine) / 2.0
    e_nu = omega * (1.0 - velocity * cosine) / 2.0
    f_bar = _fermi((e_bar + mu_nu) / temperature)
    f_nu = _fermi((e_nu - mu_nu) / temperature)
    return float(np.dot(weights, f_bar * f_nu))


def b7_one_flavour_rate_per_g2(
    mass: float, omega: float, pair_average: float
) -> float:
    """B.7: (m/omega)*3*Gamma_decay with Gamma_decay/g^2=m/(24 pi)."""
    if mass <= 0.0 or omega < mass or pair_average < 0.0:
        raise ValueError("Invalid B.7 arguments")
    return float(mass * mass / (8.0 * np.pi * omega) * pair_average)


def blinov_b7_two_flavour_rate_per_g2(
    mass: float,
    omega: float,
    temperature: float,
    mu_numu: float,
    mu_nutau: float = 0.0,
    order: int = 256,
) -> dict:
    """B.7 total for nu_mu and nu_tau, each evaluated with its own chemical potential."""
    _validate(mass, omega, temperature, mu_numu)
    if not np.isfinite(mu_nutau):
        raise ValueError("mu_nutau must be finite")
    velocity = vector_speed(mass, omega)
    i_numu = fermi_pair_average(mu_numu, omega, temperature, velocity, order)
    i_nutau = fermi_pair_average(mu_nutau, omega, temperature, velocity, order)
    rate_numu = b7_one_flavour_rate_per_g2(mass, omega, i_numu)
    rate_nutau = b7_one_flavour_rate_per_g2(mass, omega, i_nutau)
    return {
        "I_numu": i_numu,
        "I_nutau": i_nutau,
        "rate_numu_per_g2_MeV": rate_numu,
        "rate_nutau_per_g2_MeV": rate_nutau,
        "rate_total_per_g2_MeV": rate_numu + rate_nutau,
        "vector_speed": velocity,
    }


def croon_eq46_rate_per_g2(mass: float, omega: float, temperature: float) -> float:
    """Croon Eq. (4.6), literal printed coefficient and Bose occupation."""
    _validate(mass, omega, temperature, 0.0)
    return float(mass * mass / (12.0 * np.pi * omega)
                 * bose_occupation(omega, temperature))


def lai_eq10_mb_rate_per_g2(mass: float, omega: float, temperature: float) -> float:
    """Lai et al. Eq. (10), two-flavour Maxwell-Boltzmann benchmark."""
    _validate(mass, omega, temperature, 0.0)
    return float(mass * mass / (4.0 * np.pi * omega)
                 * np.exp(-omega / temperature))


def rate_ratios(
    mass: float,
    omega: float,
    temperature: float,
    mu_numu: float,
    mu_nutau: float = 0.0,
    order: int = 256,
) -> dict:
    b7 = blinov_b7_two_flavour_rate_per_g2(
        mass, omega, temperature, mu_numu, mu_nutau, order
    )
    croon = croon_eq46_rate_per_g2(mass, omega, temperature)
    lai_mb = lai_eq10_mb_rate_per_g2(mass, omega, temperature)
    return {
        **b7,
        "croon_eq46_per_g2_MeV": croon,
        "lai_eq10_mb_per_g2_MeV": lai_mb,
        "B7_two_flavour_over_Croon": b7["rate_total_per_g2_MeV"] / croon,
        "B7_two_flavour_over_Lai_MB": b7["rate_total_per_g2_MeV"] / lai_mb,
        "omega_over_T": omega / temperature,
        "bose_occupation": bose_occupation(omega, temperature),
    }


def load_profile_point(profile_path: Path, radius_km: float) -> dict:
    data = np.genfromtxt(profile_path, delimiter=",", names=True)
    required = ("r_km", "T_MeV", "mu_numu_MeV")
    if any(name not in data.dtype.names for name in required):
        raise ValueError(f"Profile must contain columns {required}")
    return {
        "radius_km": float(radius_km),
        "temperature_MeV": float(np.interp(radius_km, data["r_km"], data["T_MeV"])),
        "mu_numu_MeV": float(np.interp(radius_km, data["r_km"], data["mu_numu_MeV"])),
        "mu_nutau_MeV": 0.0,
    }


def run_benchmark(
    profile_path: Path = DEFAULT_PROFILE,
    mass: float = 10.0,
    radii_km=(0.0, 8.0, 12.5, 15.0),
    energies_MeV=(10.25, 12.0, 20.0, 30.0, 50.0, 100.0, 210.0),
    order: int = 512,
) -> dict:
    if not profile_path.exists():
        raise FileNotFoundError(profile_path)
    points = []
    for radius in radii_km:
        profile = load_profile_point(profile_path, float(radius))
        for omega in energies_MeV:
            if omega <= mass:
                continue
            result = rate_ratios(
                mass, float(omega), profile["temperature_MeV"],
                profile["mu_numu_MeV"], profile["mu_nutau_MeV"], order
            )
            points.append({**profile, "omega_MeV": float(omega), **result})
    return {
        "title": "Croon Eq. (4.6) versus Blinov Eqs. (B.7)-(B.9)",
        "mass_MeV": float(mass),
        "profile_file": profile_path.name,
        "profile_sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
        "angular_legendre_order": int(order),
        "flavour_assumptions": {
            "nu_mu": "profile mu_numu_MeV",
            "nu_tau": "zero; same assumption used in the published Blinov SFHo-profile calculation",
        },
        "normalization": {
            "Blinov_B8_one_flavour_width_per_g2_MeV": "mV/(24*pi)",
            "Blinov_B7_prefactor_per_flavour_per_g2": "mV^2/(8*pi*omega), including the factor 3 for the vector-polarization sum",
            "Croon_Eq46_per_g2": "mV^2/(12*pi*omega) * 1/(exp(omega/T)-1)",
            "Lai_Eq10_MB_per_g2": "mV^2/(4*pi*omega) * exp(-omega/T), both nu_mu and nu_tau",
            "exact_ratio": "Gamma_B7(two flavours)/Gamma_Croon = (3/2)*(I_numu+I_nutau)/f_B",
            "MB_zero_degeneracy_limit": "Gamma_B7(two flavours)/Gamma_Lai_MB -> 1; Gamma_B7(two flavours)/Gamma_Croon -> 3",
        },
        "points": points,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--order", type=int, default=512)
    args = parser.parse_args()
    result = run_benchmark(args.profile, args.mass, order=args.order)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    ratios = [p["B7_two_flavour_over_Croon"] for p in result["points"]]
    print(json.dumps({
        "profile_sha256": result["profile_sha256"],
        "point_count": len(ratios),
        "minimum_B7_over_Croon": min(ratios),
        "maximum_B7_over_Croon": max(ratios),
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
