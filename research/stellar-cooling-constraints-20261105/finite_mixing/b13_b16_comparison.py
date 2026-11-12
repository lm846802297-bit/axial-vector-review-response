"""Like-for-like local comparison of exact moving-muon B.13 and B.14--B.16.

The published B.14--B.16 formula is the conventional vector-current,
spin-summed, nonrelativistic/no-recoil approximation.  It is compared only
with the pure-vector B.13 result.  Axial and UV mixed-current B.13 results
are recorded separately; no vector B.14 formula is assigned to them.

All rates are normalized per g_X^2.  The two muon charge species are
integrated separately and then summed, matching the moving-muon kernel.
This is a local source comparison, not a stellar transport calculation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys

import numpy as np
from numpy.polynomial.legendre import leggauss

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import rates
from moving_muon_compton import moving_muon_compton_rates, thermal_compton_emissivity


MASS_V = 10.0
RADIUS_POINTS = (0.0, 12.5)
OMEGA_POINTS = (12.0, 15.0, 20.0, 30.0, 50.0, 80.0)
BASE_ENERGY_ORDER = 12
BASE_INNER_ORDERS = (12, 8, 8, 8)
REFINED_ENERGY_ORDER = 16
REFINED_INNER_ORDERS = (12, 8, 8, 8)


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def profile_at_radius(profile_path: Path, radius_km: float) -> dict:
    rows = np.genfromtxt(profile_path, delimiter=",", names=True)
    index = int(np.argmin(np.abs(rows["r_km"] - radius_km)))
    row = rows[index]
    return {
        "r_km": float(row["r_km"]),
        "temperature_MeV": float(row["T_MeV"]),
        "mu_mu_MeV": float(row["mu_mu_MeV"]),
        "mu_numu_MeV": float(row["mu_numu_MeV"]),
        "lapse": float(row["lapse"]),
    }


def muon_density_and_susceptibility(
    temperature: float, mu_mu: float, order: int = 192
) -> dict:
    """Return n_q, chi_q=int 2 d^3p/(2pi)^3 f_q(1-f_q), and Fdeg_q.

    The kinetic-energy substitution x=(E-m_mu)/T=t^2 resolves the p=0
    endpoint.  The two spin states are included.  mu+ has chemical
    potential -mu_mu.  Thus n_q*Fdeg_q=chi_q exactly by definition.
    """
    if temperature <= 0 or order < 8:
        raise ValueError("Require T>0 and susceptibility order >=8")
    z, weights = leggauss(order)
    x_max = max(36.0, max(abs(mu_mu) - rates.M_MU, 0.0) / temperature + 36.0)
    t_max = math.sqrt(x_max)
    t = 0.5 * t_max * (z + 1.0)
    wt = 0.5 * t_max * weights
    x = t * t
    momentum = np.sqrt(temperature * x * (2.0 * rates.M_MU + temperature * x))
    energy = rates.M_MU + temperature * x
    radial = 2.0 * temperature * momentum * energy * t * wt / math.pi**2

    species = {}
    for name, chemical in (("mu_minus", mu_mu), ("mu_plus", -mu_mu)):
        f = np.exp(-np.logaddexp(0.0, (energy - chemical) / temperature))
        density = float(np.sum(radial * f))
        susceptibility = float(np.sum(radial * f * (1.0 - f)))
        species[name] = {
            "chemical_potential_MeV": float(chemical),
            "number_density_MeV3": density,
            "susceptibility_nFdeg_MeV3": susceptibility,
            "Fdeg": susceptibility / density if density > 0.0 else 0.0,
        }
    n_total = sum(v["number_density_MeV3"] for v in species.values())
    chi_total = sum(v["susceptibility_nFdeg_MeV3"] for v in species.values())
    return {
        "species": species,
        "n_mu_total_MeV3": n_total,
        "n_mu_Fdeg_total_MeV3": chi_total,
        "Fdeg_total": chi_total / n_total if n_total > 0.0 else 0.0,
        "positive_muon_fraction_of_susceptibility": (
            species["mu_plus"]["susceptibility_nFdeg_MeV3"] / chi_total
            if chi_total > 0.0 else 0.0
        ),
        "quadrature_order": int(order),
        "x_max": float(x_max),
    }


def b14_b16_rate(
    mass: float, omega: float, temperature: float, n_mu_fdeg: float,
    include_mass_correction: bool = True
) -> dict:
    """Spin-summed B.14--B.16 production rate and its Thomson-limit split.

    sigma(mu gamma -> mu V) = 8 pi alpha alpha_V/(3 m_mu^2)
        * (1 + m_V^2/(2 omega^2)) * v_V.
    Eq. (B.16) supplies 2/v_V, so v_V cancels in Gamma_prod.
    The no-parenthesis-correction limit retains only the two transverse
    modes; the O(m_V^2/omega^2) longitudinal contribution is omitted.
    """
    if mass <= 0 or omega <= mass or temperature <= 0 or n_mu_fdeg < 0:
        raise ValueError("Require m>0, omega>m, T>0, and n_mu*Fdeg>=0")
    velocity = math.sqrt(1.0 - mass * mass / (omega * omega))
    alpha_v = 1.0 / (4.0 * math.pi)  # g_X=1
    bose = 1.0 / math.expm1(omega / temperature)
    sigma_prefactor = (
        8.0 * math.pi * rates.ALPHA * alpha_v
        / (3.0 * rates.M_MU**2)
    )
    correction = 1.0 + mass * mass / (2.0 * omega * omega)
    sigma_corrected = sigma_prefactor * correction * velocity
    sigma_no_parenthesis = sigma_prefactor * velocity

    transverse_prefactor = (
        n_mu_fdeg * 2.0 * rates.ALPHA / (3.0 * rates.M_MU**2) * bose
    )
    mode_rates_corrected = transverse_prefactor * np.array(
        [(mass / omega)**2, 1.0, 1.0]
    )
    mode_rates_no_correction = transverse_prefactor * np.array([0.0, 1.0, 1.0])
    total_from_b16 = (
        2.0 * n_mu_fdeg * sigma_corrected / velocity * bose
    )
    total_no_parenthesis = (
        2.0 * n_mu_fdeg * sigma_no_parenthesis / velocity * bose
    )
    return {
        "v_V": velocity,
        "sigma_B14_with_mass_correction_MeV_minus2": sigma_corrected,
        "sigma_B14_without_parenthesis_correction_MeV_minus2": sigma_no_parenthesis,
        "B16_mode_rates_with_mass_correction_MeV": mode_rates_corrected.tolist(),
        "B16_total_with_mass_correction_MeV": float(total_from_b16),
        "B16_mode_rates_without_parenthesis_correction_MeV": mode_rates_no_correction.tolist(),
        "B16_total_without_parenthesis_correction_MeV": float(total_no_parenthesis),
        "B16_sum_of_modes_relative_residual": float(
            abs(np.sum(mode_rates_corrected) - total_from_b16)
            / max(abs(total_from_b16), 1e-300)
        ),
        "mass_correction_factor": correction,
        "longitudinal_fraction_of_corrected_B16_rate": (
            float(mode_rates_corrected[0] / np.sum(mode_rates_corrected))
        ),
    }


def energy_grid(mass: float, temperature: float, order: int, x_max: float = 36.0):
    z, w = leggauss(order)
    y_max = math.sqrt(x_max)
    y = 0.5 * y_max * (z + 1.0)
    wy = 0.5 * y_max * w
    omega = mass + temperature * y * y
    domega_weights = 2.0 * temperature * y * wy
    momentum = np.sqrt(np.maximum((omega - mass) * (omega + mass), 0.0))
    phase_weights = domega_weights * omega**2 * momentum / (2.0 * math.pi**2)
    return omega, phase_weights


def b14_b16_emissivity(
    mass: float, point: dict, susceptibility: float, energy_order: int = 96
) -> dict:
    omega, phase = energy_grid(mass, point["temperature_MeV"], energy_order)
    rates_corrected = np.empty_like(omega)
    rates_no_correction = np.empty_like(omega)
    for i, energy in enumerate(omega):
        value = b14_b16_rate(
            mass, float(energy), point["temperature_MeV"], susceptibility, True
        )
        rates_corrected[i] = value["B16_total_with_mass_correction_MeV"]
        rates_no_correction[i] = value["B16_total_without_parenthesis_correction_MeV"]
    q_corrected = float(np.sum(phase * rates_corrected))
    q_no_correction = float(np.sum(phase * rates_no_correction))
    return {
        "Q_B16_with_mass_correction_MeV5": q_corrected,
        "Q_B16_without_parenthesis_correction_MeV5": q_no_correction,
        "relative_mass_correction_to_no_parenthesis": (
            q_corrected / q_no_correction - 1.0
        ),
        "energy_order": int(energy_order),
    }


def stationary_target_exact_emissivity(
    mass: float, point: dict, susceptibility: float,
    current: str, energy_order: int = 16, angular_order: int = 128
) -> dict:
    """Existing muon-at-rest exact-recoil kernel with the same B.17 chi."""
    omega, phase = energy_grid(mass, point["temperature_MeV"], energy_order)
    if current == "vector":
        eg, kernels = rates.compton_kernels(
            mass, omega, order=angular_order, current="vector"
        )
    elif current == "axial":
        eg, kernels = rates.compton_kernels(
            mass, omega, order=angular_order, current="axial"
        )
    elif current == "uv_theta_1e-2":
        theta = 1.0e-2
        eg, kernels = rates.compton_mixed_kernels(
            mass, omega, math.sin(theta)**2, -math.cos(theta)**2,
            order=angular_order
        )
    else:
        raise ValueError(f"Unknown current {current}")
    gamma_abs = rates.compton_absorption(
        (eg, kernels), point["temperature_MeV"], susceptibility
    )
    gamma_prod = np.exp(-omega / point["temperature_MeV"])[:, None] * gamma_abs
    q_mode = np.einsum("i,ih->h", phase, gamma_prod)
    return {
        "Q_by_mode_MeV5": q_mode.tolist(),
        "Q_total_MeV5": float(np.sum(q_mode)),
        "energy_order": int(energy_order),
        "angular_order": int(angular_order),
    }


def neutrino_emissivity(
    mass: float, point: dict, energy_order: int = 96, angular_order: int = 96
) -> dict:
    """Local nu_mu+nu_tau coalescence source, with unchanged neutrino currents."""
    omega, phase = energy_grid(mass, point["temperature_MeV"], energy_order)
    production, absorption = rates.neutrino_rates(
        mass, omega, point["temperature_MeV"], point["mu_numu_MeV"],
        order=angular_order
    )
    q_mode = np.einsum("i,ih->h", phase, production)
    return {
        "Q_by_mode_MeV5": q_mode.tolist(),
        "Q_total_MeV5": float(np.sum(q_mode)),
        "max_mode_balance_residual": float(np.max(
            np.abs(production-np.exp(-omega/point["temperature_MeV"])[:,None]*absorption)
            / np.maximum(np.abs(production),1e-300)
        )),
        "energy_order": int(energy_order),
        "angular_order": int(angular_order),
    }


def local_source_budget(q_compton_exact: float, q_compton_stationary: float,
                        q_neutrino: float) -> dict:
    """Compare local thin sources without introducing a global radial weight."""
    stationary_total = q_compton_stationary + q_neutrino
    exact_total = q_compton_exact + q_neutrino
    return {
        "Q_neutrino_MeV5": q_neutrino,
        "Q_compton_stationary_exact_recoil_MeV5": q_compton_stationary,
        "Q_compton_moving_muon_B13_MeV5": q_compton_exact,
        "Q_total_stationary_source_MeV5": stationary_total,
        "Q_total_moving_muon_source_MeV5": exact_total,
        "stationary_compton_fraction": (
            q_compton_stationary/stationary_total if stationary_total else 0.0
        ),
        "moving_muon_compton_fraction": (
            q_compton_exact/exact_total if exact_total else 0.0
        ),
        "compton_rate_shift_fraction": (
            q_compton_exact/q_compton_stationary-1.0
            if q_compton_stationary else None
        ),
        "total_local_thin_source_shift_fraction": (
            exact_total/stationary_total-1.0 if stationary_total else None
        ),
    }


def b13_fixed_energy(
    mass: float, point: dict, omega: float, current: str,
    orders: tuple[int, int, int, int] = BASE_INNER_ORDERS
) -> dict:
    if current == "vector":
        gv, ga = 1.0, 0.0
    elif current == "axial":
        gv, ga = 0.0, -1.0
    elif current == "uv_theta_1e-2":
        theta = 1.0e-2
        gv, ga = math.sin(theta)**2, -math.cos(theta)**2
    else:
        raise ValueError(f"Unknown current {current}")
    result = moving_muon_compton_rates(
        mass, omega, point["temperature_MeV"], point["mu_mu_MeV"],
        gv, ga, orders=orders
    )
    production = np.asarray(result["production"], float)
    return {
        "production_by_mode_MeV": production.tolist(),
        "production_total_MeV": float(np.sum(production)),
        "charge_resolved_production_by_mode_MeV": {
            name: np.asarray(value["production"], float).tolist()
            for name, value in result["charge_resolved"].items()
        },
        "max_final_muon_shell_relative_error": (
            result["diagnostics"]["final_muon_shell_relative_error"]
        ),
        "orders": list(orders),
    }


def b13_thermal_case(
    mass: float, point: dict, current: str,
    energy_order: int, inner_orders: tuple[int, int, int, int]
) -> dict:
    if current == "vector":
        gv, ga = 1.0, 0.0
    elif current == "axial":
        gv, ga = 0.0, -1.0
    elif current == "uv_theta_1e-2":
        theta = 1.0e-2
        gv, ga = math.sin(theta)**2, -math.cos(theta)**2
    else:
        raise ValueError(f"Unknown current {current}")
    result = thermal_compton_emissivity(
        mass, point["temperature_MeV"], point["mu_mu_MeV"],
        gv, ga, energy_order=energy_order, orders=inner_orders
    )
    return {
        "Q_by_mode_MeV5": result["emissivity_by_mode_MeV5"],
        "Q_total_MeV5": result["emissivity_total_MeV5"],
        "Q_by_charge_and_mode_MeV5": result["emissivity_by_charge_and_mode_MeV5"],
        "max_detailed_balance_relative_error": result["max_detailed_balance_relative_error"],
        "max_final_muon_shell_relative_error": result["max_final_muon_shell_relative_error"],
        "energy_order": int(energy_order),
        "inner_orders": list(inner_orders),
    }


def run_case(profile_path: Path, radius: float) -> dict:
    point = profile_at_radius(profile_path, radius)
    thermo_coarse = muon_density_and_susceptibility(
        point["temperature_MeV"], point["mu_mu_MeV"], order=128
    )
    thermo = muon_density_and_susceptibility(
        point["temperature_MeV"], point["mu_mu_MeV"], order=192
    )
    chi = thermo["n_mu_Fdeg_total_MeV3"]
    chi_minus = thermo["species"]["mu_minus"]["susceptibility_nFdeg_MeV3"]
    chi_plus = thermo["species"]["mu_plus"]["susceptibility_nFdeg_MeV3"]

    b13_vector = b13_thermal_case(
        MASS_V, point, "vector", BASE_ENERGY_ORDER, BASE_INNER_ORDERS
    )
    b13_axial = b13_thermal_case(
        MASS_V, point, "axial", BASE_ENERGY_ORDER, BASE_INNER_ORDERS
    )
    b13_uv = b13_thermal_case(
        MASS_V, point, "uv_theta_1e-2", BASE_ENERGY_ORDER, BASE_INNER_ORDERS
    )
    b16 = b14_b16_emissivity(MASS_V, point, chi, energy_order=96)
    b16_coarse = b14_b16_emissivity(MASS_V, point, chi, energy_order=64)
    b16_minus = b14_b16_emissivity(MASS_V, point, chi_minus, energy_order=96)
    b16_plus = b14_b16_emissivity(MASS_V, point, chi_plus, energy_order=96)

    stationary_vector = stationary_target_exact_emissivity(
        MASS_V, point, chi, "vector", energy_order=16, angular_order=128
    )
    stationary_axial = stationary_target_exact_emissivity(
        MASS_V, point, chi, "axial", energy_order=16, angular_order=128
    )
    stationary_uv = stationary_target_exact_emissivity(
        MASS_V, point, chi, "uv_theta_1e-2", energy_order=16, angular_order=128
    )
    stationary_vector_coarse = stationary_target_exact_emissivity(
        MASS_V, point, chi, "vector", energy_order=16, angular_order=64
    )
    neutrino = neutrino_emissivity(
        MASS_V, point, energy_order=96, angular_order=96
    )
    neutrino_coarse = neutrino_emissivity(
        MASS_V, point, energy_order=64, angular_order=96
    )

    energy_refined = b13_thermal_case(
        MASS_V, point, "vector", REFINED_ENERGY_ORDER, REFINED_INNER_ORDERS
    )
    inner_refined = b13_thermal_case(
        MASS_V, point, "vector", BASE_ENERGY_ORDER, (16, 10, 10, 10)
    )

    fixed_energy = {}
    for omega in OMEGA_POINTS:
        if omega <= MASS_V:
            continue
        b13v = b13_fixed_energy(MASS_V, point, omega, "vector")
        b13a = b13_fixed_energy(MASS_V, point, omega, "axial")
        b13uv = b13_fixed_energy(MASS_V, point, omega, "uv_theta_1e-2")
        b16omega = b14_b16_rate(MASS_V, omega, point["temperature_MeV"], chi, True)
        b16no = b14_b16_rate(MASS_V, omega, point["temperature_MeV"], chi, False)
        b16minus = b14_b16_rate(MASS_V, omega, point["temperature_MeV"], chi_minus, True)
        b16plus = b14_b16_rate(MASS_V, omega, point["temperature_MeV"], chi_plus, True)
        fixed_energy[str(omega)] = {
            "B13_vector": b13v,
            "B13_axial": b13a,
            "B13_UV_theta_muR_1e-2": b13uv,
            "B13_vector_over_B16_corrected": (
                b13v["production_total_MeV"] /
                b16omega["B16_total_with_mass_correction_MeV"]
            ),
            "B13_vector_over_B16_without_parenthesis_correction": (
                b13v["production_total_MeV"] /
                b16no["B16_total_without_parenthesis_correction_MeV"]
            ),
            "B16_B14_with_mass_correction": b16omega,
            "B16_B14_without_parenthesis_correction": b16no,
            "B16_B14_charge_resolved_with_mass_correction": {
                "mu_minus": b16minus["B16_total_with_mass_correction_MeV"],
                "mu_plus": b16plus["B16_total_with_mass_correction_MeV"],
                "sum": (
                    b16minus["B16_total_with_mass_correction_MeV"]
                    + b16plus["B16_total_with_mass_correction_MeV"]
                ),
            },
        }

    vector_vs_b16 = (
        b13_vector["Q_total_MeV5"] / b16["Q_B16_with_mass_correction_MeV5"] - 1.0
    )
    vector_vs_b16_no = (
        b13_vector["Q_total_MeV5"] / b16["Q_B16_without_parenthesis_correction_MeV5"] - 1.0
    )
    vector_vs_stationary = (
        b13_vector["Q_total_MeV5"] / stationary_vector["Q_total_MeV5"] - 1.0
    )
    stationary_vs_b16 = (
        stationary_vector["Q_total_MeV5"]
        / b16["Q_B16_with_mass_correction_MeV5"] - 1.0
    )
    approximation_factorization_residual = (
        (1.0+vector_vs_stationary)*(1.0+stationary_vs_b16)
        - (1.0+vector_vs_b16)
    )
    axial_vs_stationary = (
        b13_axial["Q_total_MeV5"] / stationary_axial["Q_total_MeV5"] - 1.0
    )
    uv_vs_stationary = (
        b13_uv["Q_total_MeV5"] / stationary_uv["Q_total_MeV5"] - 1.0
    )
    local_budgets = {
        "vector": local_source_budget(
            b13_vector["Q_total_MeV5"], stationary_vector["Q_total_MeV5"],
            neutrino["Q_total_MeV5"]
        ),
        "axial": local_source_budget(
            b13_axial["Q_total_MeV5"], stationary_axial["Q_total_MeV5"],
            neutrino["Q_total_MeV5"]
        ),
        "UV_theta_muR_1e-2": local_source_budget(
            b13_uv["Q_total_MeV5"], stationary_uv["Q_total_MeV5"],
            neutrino["Q_total_MeV5"]
        ),
    }

    return {
        "local_thermodynamics": point,
        "muon_density_and_B17_degeneracy": thermo,
        "B13_exact_moving_muon": {
            "vector": b13_vector,
            "axial": b13_axial,
            "UV_theta_muR_1e-2": b13_uv,
        },
        "B14_B16_vector_no_recoil": {
            **b16,
            "energy_order_64_comparison": b16_coarse,
            "mu_minus_only_Q": b16_minus,
            "mu_plus_only_Q": b16_plus,
            "charge_resolved_Q_sum_relative_residual": (
                (b16_minus["Q_B16_with_mass_correction_MeV5"]
                 + b16_plus["Q_B16_with_mass_correction_MeV5"])
                / b16["Q_B16_with_mass_correction_MeV5"] - 1.0
            ),
            "energy_order_64_to_96_relative_change": (
                b16["Q_B16_with_mass_correction_MeV5"] /
                b16_coarse["Q_B16_with_mass_correction_MeV5"] - 1.0
            ),
            "susceptibility_order_128_comparison": thermo_coarse,
            "susceptibility_order_128_to_192_relative_change": (
                chi / thermo_coarse["n_mu_Fdeg_total_MeV3"] - 1.0
            ),
            "susceptibility_order": thermo["quadrature_order"],
        },
        "existing_stationary_muon_exact_recoil": {
            "vector": stationary_vector,
            "axial": stationary_axial,
            "UV_theta_muR_1e-2": stationary_uv,
            "vector_angular_order_64_comparison": stationary_vector_coarse,
            "vector_angular_order_64_to_128_relative_change": (
                stationary_vector["Q_total_MeV5"] /
                stationary_vector_coarse["Q_total_MeV5"] - 1.0
            ),
        },
        "local_neutrino_source": {
            "production": neutrino,
            "energy_order_64_comparison": neutrino_coarse,
            "energy_order_64_to_96_relative_change": (
                neutrino["Q_total_MeV5"]/neutrino_coarse["Q_total_MeV5"]-1.0
            ),
            "local_thin_source_budgets": local_budgets,
            "scope": (
                "These are local two-channel source budgets at r=0 and 12.5 km; "
                "they are not a radial integration of the global weak-coupling luminosity."
            ),
        },
        "relative_differences": {
            "B13_vector_vs_B16_corrected_fraction": vector_vs_b16,
            "B13_vector_vs_B16_without_parenthesis_correction_fraction": vector_vs_b16_no,
            "B13_vector_vs_existing_stationary_exact_fraction": vector_vs_stationary,
            "stationary_exact_recoil_vs_B16_corrected_fraction": stationary_vs_b16,
            "moving_muon_and_B16_approximation_factorization_residual": (
                approximation_factorization_residual
            ),
            "B13_axial_vs_existing_stationary_exact_fraction": axial_vs_stationary,
            "B13_UV_vs_existing_stationary_exact_fraction": uv_vs_stationary,
        },
        "fixed_energy_rate_comparison": fixed_energy,
        "B13_quadrature_convergence": {
            "base": b13_vector,
            "energy_refined": energy_refined,
            "inner_refined": inner_refined,
            "energy_order_12_to_16_relative_change": (
                energy_refined["Q_total_MeV5"] / b13_vector["Q_total_MeV5"] - 1.0
            ),
            "inner_order_12_8_8_8_to_16_10_10_10_relative_change": (
                inner_refined["Q_total_MeV5"] / b13_vector["Q_total_MeV5"] - 1.0
            ),
            "fixed_energy_one_at_a_time_inner_refinement_at_30MeV": {},
        },
    }


def run(profile_path: Path) -> dict:
    results = {}
    for radius in RADIUS_POINTS:
        results[str(radius)] = run_case(profile_path, radius)

    # One-at-a-time convergence at fixed omega=30 MeV isolates all four
    # inner integrations independently, for each requested radius.
    for radius in RADIUS_POINTS:
        case = results[str(radius)]
        point = case["local_thermodynamics"]
        baseline = b13_fixed_energy(MASS_V, point, 30.0, "vector", BASE_INNER_ORDERS)
        variants = {
            "p_order_16": (16, 8, 8, 8),
            "cos_mu_order_12": (12, 12, 8, 8),
            "cos_gamma_order_12": (12, 8, 12, 8),
            "phi_order_12": (12, 8, 8, 12),
            "all_inner_refined": (16, 12, 12, 12),
        }
        summary = {}
        for name, orders in variants.items():
            value = b13_fixed_energy(MASS_V, point, 30.0, "vector", orders)
            summary[name] = {
                "orders": list(orders),
                "production_by_mode_MeV": value["production_by_mode_MeV"],
                "production_total_MeV": value["production_total_MeV"],
                "relative_change_vs_base": (
                    value["production_total_MeV"] / baseline["production_total_MeV"] - 1.0
                ),
            }
        case["B13_quadrature_convergence"][
            "fixed_energy_one_at_a_time_inner_refinement_at_30MeV"
        ] = {
            "omega_MeV": 30.0,
            "base_orders": list(BASE_INNER_ORDERS),
            "base_by_mode_MeV": baseline["production_by_mode_MeV"],
            "base_total_MeV": baseline["production_total_MeV"],
            "refinements": summary,
        }

    return {
        "title": "B.13 exact moving-muon vs B.14-B.16 no-recoil semi-Compton comparison",
        "paper_reference": {
            "citation": "N. Blinov et al., arXiv:2511.09619v2, JHEP 06 (2026) 155",
            "equations": "Appendix B, Eqs. (B.13)-(B.19)",
            "B13": "Full moving-muon 2->2 collision integral with Fermi blocking and Bose occupation.",
            "B14_B16": (
                "Spin-summed vector-current nonrelativistic/no-recoil approximation. "
                "The factor (1+m_V^2/(2 omega^2)) is retained or dropped as two "
                "separate comparisons; the 1/v_V in B.16 cancels the v_V in B.14."
            ),
        },
        "configuration": {
            "mediator_mass_MeV": MASS_V,
            "radii_km_requested": list(RADIUS_POINTS),
            "fixed_omega_points_MeV": list(OMEGA_POINTS),
            "base_energy_order": BASE_ENERGY_ORDER,
            "base_inner_orders_p_cosmu_cosgamma_phi": list(BASE_INNER_ORDERS),
            "refined_energy_order": REFINED_ENERGY_ORDER,
            "refined_inner_orders": list(REFINED_INNER_ORDERS),
            "B17_susceptibility_order": 192,
            "B16_energy_orders": [64, 96],
            "stationary_exact_angular_orders": [64, 128],
            "rate_normalization": "per g_X^2, set g_X=1",
            "muon_charges": "mu- chemical potential +mu_mu; mu+ chemical potential -mu_mu; both summed",
            "B14_current": "pure vector only",
        },
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "source": "reconstructed SFHo-18.8 t_pb=1s digitized profile",
        },
        "cases": results,
        "scope_limits": [
            "Local source-rate comparison only; no radial integration or escape probability.",
            "B.14-B.16 is the published nonrelativistic-muon, negligible-recoil Thomson-limit approximation; its difference from the exact B.13 kernel is retained as a physical approximation diagnostic.",
            "B.14-B.16 is compared only to the pure-vector B.13 rate.",
            "No B.14 vector formula is assigned to the axial or UV mixed-current rates.",
            "No coupling, production, absorption, opacity, or profile rescaling is performed.",
            "The full pure-vector Fig. 7 validation gate remains separate and is not passed by this local comparison.",
        ],
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": {
            "script": sha256(Path(__file__)),
            "moving_muon_compton.py": sha256(HERE / "moving_muon_compton.py"),
            "rates.py": sha256(ROOT / "rates.py"),
            "profile": sha256(profile_path),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile", type=Path, default=ROOT / "data" / "sfho188_digitized.csv"
    )
    parser.add_argument(
        "--output", type=Path,
        default=HERE / "outputs" / "b13_b16_comparison_2026-11-08.json"
    )
    args = parser.parse_args()
    result = run(args.profile)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    for radius, case in result["cases"].items():
        print(json.dumps({
            "r_km": radius,
            "Q_B13_vector": case["B13_exact_moving_muon"]["vector"]["Q_total_MeV5"],
            "Q_B16_corrected": case["B14_B16_vector_no_recoil"]["Q_B16_with_mass_correction_MeV5"],
            "B13_over_B16_minus_1": case["relative_differences"]["B13_vector_vs_B16_corrected_fraction"],
            "B13_over_stationary_exact_minus_1": case["relative_differences"]["B13_vector_vs_existing_stationary_exact_fraction"],
        }, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
