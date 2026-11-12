"""Low-mass B.13/B.14--B.16 vector benchmark scan.

New masses are evaluated with the exact moving-muon B.13 kernel, the
stationary-muon exact-recoil kernel, and the spin-summed B.14--B.16
approximation. The existing 10 MeV result is imported as a provenance-tagged
reference rather than recomputed. This is a local-rate audit, not transport.
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
from b13_b16_comparison import (
    BASE_ENERGY_ORDER,
    BASE_INNER_ORDERS,
    REFINED_ENERGY_ORDER,
    b13_fixed_energy,
    b13_thermal_case,
    b14_b16_emissivity,
    b14_b16_rate,
    energy_grid,
    muon_density_and_susceptibility,
    profile_at_radius,
    stationary_target_exact_emissivity,
)

NEW_MASSES_MEV = (0.1, 0.3, 1.0, 3.0)
REFERENCE_MASS_MEV = 10.0
RADIUS_POINTS_KM = (0.0, 12.5)
FIXED_OMEGA_POINTS_MEV = (15.0, 30.0, 50.0)
INNER_REFINED_ORDERS = (16, 10, 10, 10)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def muon_kinematic_diagnostics(
    temperature: float, mu_mu: float, order: int = 192
) -> dict:
    """B.17-susceptibility-weighted muon velocity and kinetic-energy moments.

    The weights are f(1-f), not f alone, because this is the distribution
    entering n_mu F_deg in Eq. (B.17). The p/m cut fractions are diagnostics,
    not a claim that a sharp cutoff defines the nonrelativistic regime.
    """
    if temperature <= 0.0 or order < 8:
        raise ValueError("Require T>0 and quadrature order >=8")
    z, weights = leggauss(order)
    x_max = max(36.0, max(abs(mu_mu) - rates.M_MU, 0.0) / temperature + 36.0)
    t_max = math.sqrt(x_max)
    t = 0.5 * t_max * (z + 1.0)
    wt = 0.5 * t_max * weights
    x = t * t
    momentum = np.sqrt(
        temperature * x * (2.0 * rates.M_MU + temperature * x)
    )
    energy = rates.M_MU + temperature * x
    radial = 2.0 * temperature * momentum * energy * t * wt / math.pi**2
    velocity = momentum / energy
    p_over_m = momentum / rates.M_MU
    kinetic_over_m = (energy - rates.M_MU) / rates.M_MU

    species = {}
    all_weights = []
    for name, chemical in (("mu_minus", mu_mu), ("mu_plus", -mu_mu)):
        f = np.exp(-np.logaddexp(0.0, (energy - chemical) / temperature))
        susceptibility_weight = radial * f * (1.0 - f)
        norm = float(np.sum(susceptibility_weight))
        if norm <= 0.0:
            raise ArithmeticError(f"Zero B.17 susceptibility for {name}")
        all_weights.append(susceptibility_weight)
        species[name] = {
            "B17_susceptibility_MeV3": norm,
            "mean_p_over_m": float(np.sum(susceptibility_weight*p_over_m)/norm),
            "rms_velocity": float(
                math.sqrt(np.sum(susceptibility_weight*velocity**2)/norm)
            ),
            "mean_velocity": float(
                np.sum(susceptibility_weight*velocity)/norm
            ),
            "mean_kinetic_energy_over_m": float(
                np.sum(susceptibility_weight*kinetic_over_m)/norm
            ),
            "fraction_p_over_m_below_0p3": float(
                np.sum(susceptibility_weight[p_over_m < 0.3])/norm
            ),
            "fraction_p_over_m_below_0p5": float(
                np.sum(susceptibility_weight[p_over_m < 0.5])/norm
            ),
        }
    total_weight = all_weights[0] + all_weights[1]
    total_norm = float(np.sum(total_weight))
    species["combined"] = {
        "B17_susceptibility_MeV3": total_norm,
        "mean_p_over_m": float(np.sum(total_weight*p_over_m)/total_norm),
        "rms_velocity": float(
            math.sqrt(np.sum(total_weight*velocity**2)/total_norm)
        ),
        "mean_velocity": float(np.sum(total_weight*velocity)/total_norm),
        "mean_kinetic_energy_over_m": float(
            np.sum(total_weight*kinetic_over_m)/total_norm
        ),
        "fraction_p_over_m_below_0p3": float(
            np.sum(total_weight[p_over_m < 0.3])/total_norm
        ),
        "fraction_p_over_m_below_0p5": float(
            np.sum(total_weight[p_over_m < 0.5])/total_norm
        ),
    }
    return {
        "weighting": "B.17 susceptibility f_mu(1-f_mu), summed over mu- and mu+",
        "quadrature_order": int(order),
        "species": species,
    }


def build_fixed_energy_comparison(
    mass: float, point: dict, susceptibility: float
) -> dict:
    result = {}
    for omega in FIXED_OMEGA_POINTS_MEV:
        if omega <= mass:
            continue
        b13 = b13_fixed_energy(
            mass, point, omega, "vector", orders=BASE_INNER_ORDERS
        )
        b16 = b14_b16_rate(
            mass, omega, point["temperature_MeV"], susceptibility, True
        )
        b16_no = b14_b16_rate(
            mass, omega, point["temperature_MeV"], susceptibility, False
        )
        result[str(omega)] = {
            "B13_vector": b13,
            "B16_B14_with_mass_correction": b16,
            "B16_B14_without_parenthesis_correction": b16_no,
            "B13_vector_over_B16_corrected": (
                b13["production_total_MeV"]
                / b16["B16_total_with_mass_correction_MeV"]
            ),
            "B13_vector_over_B16_without_parenthesis_correction": (
                b13["production_total_MeV"]
                / b16_no["B16_total_without_parenthesis_correction_MeV"]
            ),
        }
    return result


def run_new_mass_radius_case(
    profile_path: Path, radius_km: float, mass: float
) -> dict:
    point = profile_at_radius(profile_path, radius_km)
    thermo_coarse = muon_density_and_susceptibility(
        point["temperature_MeV"], point["mu_mu_MeV"], order=128
    )
    thermo = muon_density_and_susceptibility(
        point["temperature_MeV"], point["mu_mu_MeV"], order=192
    )
    chi = thermo["n_mu_Fdeg_total_MeV3"]

    b13 = b13_thermal_case(
        mass, point, "vector", BASE_ENERGY_ORDER, BASE_INNER_ORDERS
    )
    b13_energy_refined = b13_thermal_case(
        mass, point, "vector", REFINED_ENERGY_ORDER, BASE_INNER_ORDERS
    )
    b13_inner_refined = b13_thermal_case(
        mass, point, "vector", BASE_ENERGY_ORDER, INNER_REFINED_ORDERS
    )

    b16 = b14_b16_emissivity(mass, point, chi, energy_order=96)
    b16_coarse = b14_b16_emissivity(mass, point, chi, energy_order=64)

    stationary = stationary_target_exact_emissivity(
        mass, point, chi, "vector", energy_order=16, angular_order=128
    )
    stationary_coarse = stationary_target_exact_emissivity(
        mass, point, chi, "vector", energy_order=16, angular_order=64
    )

    fixed_energy = build_fixed_energy_comparison(mass, point, chi)
    return {
        "mass_MeV": float(mass),
        "recomputed": True,
        "local_thermodynamics": point,
        "muon_density_and_B17_degeneracy": thermo,
        "muon_susceptibility_order_128_to_192_relative_change": (
            chi / thermo_coarse["n_mu_Fdeg_total_MeV3"] - 1.0
        ),
        "muon_nonrelativistic_diagnostics": muon_kinematic_diagnostics(
            point["temperature_MeV"], point["mu_mu_MeV"], order=192
        ),
        "B13_exact_moving_muon_vector": b13,
        "stationary_muon_exact_recoil_vector": stationary,
        "B14_B16_vector_no_recoil": {
            **b16,
            "energy_order_64_comparison": b16_coarse,
            "energy_order_64_to_96_relative_change": (
                b16["Q_B16_with_mass_correction_MeV5"]
                / b16_coarse["Q_B16_with_mass_correction_MeV5"] - 1.0
            ),
        },
        "fixed_energy_rate_comparison": fixed_energy,
        "relative_differences": {
            "B13_vector_vs_B16_corrected_fraction": (
                b13["Q_total_MeV5"]
                / b16["Q_B16_with_mass_correction_MeV5"] - 1.0
            ),
            "B13_vector_vs_B16_without_parenthesis_correction_fraction": (
                b13["Q_total_MeV5"]
                / b16["Q_B16_without_parenthesis_correction_MeV5"] - 1.0
            ),
            "B13_vector_vs_stationary_exact_recoil_fraction": (
                b13["Q_total_MeV5"]
                / stationary["Q_total_MeV5"] - 1.0
            ),
            "stationary_exact_recoil_vs_B16_corrected_fraction": (
                stationary["Q_total_MeV5"]
                / b16["Q_B16_with_mass_correction_MeV5"] - 1.0
            ),
            "moving_muon_and_B16_approximation_factorization_residual": (
                (b13["Q_total_MeV5"]/stationary["Q_total_MeV5"])
                *(stationary["Q_total_MeV5"]/b16["Q_B16_with_mass_correction_MeV5"])
                - b13["Q_total_MeV5"]/b16["Q_B16_with_mass_correction_MeV5"]
            ),
            "B16_integrated_mass_correction_fraction": (
                b16["relative_mass_correction_to_no_parenthesis"]
            ),
        },
        "quadrature_convergence": {
            "B13_energy_order_12_to_16_relative_change": (
                b13_energy_refined["Q_total_MeV5"]
                / b13["Q_total_MeV5"] - 1.0
            ),
            "B13_inner_orders_12_8_8_8_to_16_10_10_10_relative_change": (
                b13_inner_refined["Q_total_MeV5"]
                / b13["Q_total_MeV5"] - 1.0
            ),
            "B16_energy_order_64_to_96_relative_change": (
                b16["Q_B16_with_mass_correction_MeV5"]
                / b16_coarse["Q_B16_with_mass_correction_MeV5"] - 1.0
            ),
            "stationary_exact_angular_order_64_to_128_relative_change": (
                stationary["Q_total_MeV5"]
                / stationary_coarse["Q_total_MeV5"] - 1.0
            ),
            "B13_max_detailed_balance_relative_error": (
                b13["max_detailed_balance_relative_error"]
            ),
            "B13_max_final_muon_shell_relative_error": (
                b13["max_final_muon_shell_relative_error"]
            ),
        },
    }


def reuse_existing_10MeV_case(
    reference_output_path: Path, radius_km: float
) -> dict:
    reference = json.loads(reference_output_path.read_text())
    key = str(radius_km)
    source = reference["cases"][key]
    point = source["local_thermodynamics"]
    return {
        "mass_MeV": REFERENCE_MASS_MEV,
        "recomputed": False,
        "reuse_note": (
            "Reused from the previously validated 10 MeV B.13/B.14--B.16 "
            "comparison; no collision integral was recomputed in this scan."
        ),
        "source_run_commit_sha": reference.get("run_commit_sha"),
        "source_script_sha256": reference.get("code_sha256", {}).get("script"),
        "local_thermodynamics": point,
        "muon_density_and_B17_degeneracy": source[
            "muon_density_and_B17_degeneracy"
        ],
        "muon_nonrelativistic_diagnostics": muon_kinematic_diagnostics(
            point["temperature_MeV"], point["mu_mu_MeV"], order=192
        ),
        "B13_exact_moving_muon_vector": source[
            "B13_exact_moving_muon"
        ]["vector"],
        "stationary_muon_exact_recoil_vector": source[
            "existing_stationary_muon_exact_recoil"
        ]["vector"],
        "B14_B16_vector_no_recoil": source["B14_B16_vector_no_recoil"],
        "fixed_energy_rate_comparison": source["fixed_energy_rate_comparison"],
        "relative_differences": {
            "B13_vector_vs_B16_corrected_fraction": source[
                "relative_differences"
            ]["B13_vector_vs_B16_corrected_fraction"],
            "B13_vector_vs_B16_without_parenthesis_correction_fraction": source[
                "relative_differences"
            ]["B13_vector_vs_B16_without_parenthesis_correction_fraction"],
            "B13_vector_vs_stationary_exact_recoil_fraction": source[
                "relative_differences"
            ]["B13_vector_vs_existing_stationary_exact_fraction"],
            "B16_integrated_mass_correction_fraction": source[
                "B14_B16_vector_no_recoil"
            ]["relative_mass_correction_to_no_parenthesis"],
        },
        "quadrature_convergence": {
            "B13_energy_order_12_to_16_relative_change": source[
                "B13_quadrature_convergence"
            ]["energy_order_12_to_16_relative_change"],
            "B13_inner_orders_12_8_8_8_to_16_10_10_10_relative_change": source[
                "B13_quadrature_convergence"
            ]["inner_order_12_8_8_8_to_16_10_10_10_relative_change"],
            "B16_energy_order_64_to_96_relative_change": source[
                "B14_B16_vector_no_recoil"
            ]["energy_order_64_to_96_relative_change"],
            "stationary_exact_angular_order_64_to_128_relative_change": source[
                "existing_stationary_muon_exact_recoil"
            ]["vector_angular_order_64_to_128_relative_change"],
            "B13_max_detailed_balance_relative_error": source[
                "B13_exact_moving_muon"
            ]["vector"]["max_detailed_balance_relative_error"],
            "B13_max_final_muon_shell_relative_error": source[
                "B13_exact_moving_muon"
            ]["vector"]["max_final_muon_shell_relative_error"],
        },
    }


def run_mass_scan(
    profile_path: Path, reference_output_path: Path,
    masses: tuple[float, ...] = NEW_MASSES_MEV
) -> dict:
    mass_cases = {}
    for mass in masses:
        mass_key = f"{mass:g}"
        mass_cases[mass_key] = {}
        for radius in RADIUS_POINTS_KM:
            mass_cases[mass_key][str(radius)] = run_new_mass_radius_case(
                profile_path, radius, mass
            )

    # Keep the previous 10 MeV benchmark in the comparison table, but retain
    # its original run/code provenance and do not spend CI time recomputing it.
    mass_cases[f"{REFERENCE_MASS_MEV:g}"] = {
        str(radius): reuse_existing_10MeV_case(reference_output_path, radius)
        for radius in RADIUS_POINTS_KM
    }

    return {
        "title": "Low-mass exact moving-muon B.13 vs stationary exact recoil and B.14--B.16 vector scan",
        "paper_reference": {
            "citation": "N. Blinov et al., arXiv:2511.09619v2, JHEP 06 (2026) 155",
            "equations": "Appendix B, Eqs. (B.13)--(B.19)",
            "quoted_mass_regime": (
                "The O(m_V^2/omega^2) term in the B.14 parenthesis is "
                "typically dropped for m_V less than or of order MeV."
            ),
            "important_distinction": (
                "The low-mass condition controls the explicit m_V^2/omega^2 "
                "correction; it does not by itself establish the separate "
                "nonrelativistic-muon and negligible-recoil assumptions. "
                "The B.17-weighted muon kinematic diagnostics and direct "
                "B.13/B.16 comparison test those assumptions independently."
            ),
        },
        "configuration": {
            "new_masses_MeV": list(masses),
            "reused_reference_mass_MeV": REFERENCE_MASS_MEV,
            "radii_km": list(RADIUS_POINTS_KM),
            "fixed_omega_points_MeV": list(FIXED_OMEGA_POINTS_MEV),
            "B13_base_energy_order": BASE_ENERGY_ORDER,
            "B13_base_inner_orders_p_cosmu_cosgamma_phi": list(BASE_INNER_ORDERS),
            "B13_refined_energy_order": REFINED_ENERGY_ORDER,
            "B13_refined_inner_orders": list(INNER_REFINED_ORDERS),
            "B16_energy_orders": [64, 96],
            "stationary_exact_angular_orders": [64, 128],
            "B17_susceptibility_order": 192,
            "rate_normalization": "per g_X^2, with g_X=1",
            "current": "pure vector only; B.14--B.16 is not applied to axial currents",
        },
        "profile": {
            "path": str(profile_path),
            "sha256": file_sha256(profile_path),
            "source": "reconstructed SFHo-18.8 t_pb=1s digitized profile",
        },
        "mass_cases": mass_cases,
        "scope_limits": [
            "Local source-rate comparison at r=0 and 12.5 km only.",
            "No radial luminosity integral, escape probability, opacity, or transport calculation.",
            "B.14-B.16 is the published nonrelativistic-muon, negligible-recoil Thomson-limit approximation; its difference from exact B.13 is decomposed using the stationary exact-recoil kernel.",
            "The 10 MeV result is reused from its previously validated output and is not recomputed.",
            "No coupling, production, absorption, opacity, or stellar-profile rescaling.",
            "The B.14 low-mass statement concerns dropping O(m_V^2/omega^2); nonrelativistic muon and negligible-recoil assumptions are tested separately.",
            "No axial exclusion curve is produced; this scan is a pure-vector literature benchmark.",
        ],
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": {
            "mass_scan_script": file_sha256(Path(__file__)),
            "comparison_kernel_script": file_sha256(HERE / "b13_b16_comparison.py"),
            "moving_muon_compton.py": file_sha256(HERE / "moving_muon_compton.py"),
            "rates.py": file_sha256(ROOT / "rates.py"),
            "profile": file_sha256(profile_path),
            "reused_10MeV_output": file_sha256(reference_output_path),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile", type=Path, default=ROOT / "data" / "sfho188_digitized.csv"
    )
    parser.add_argument(
        "--reference-output", type=Path,
        default=HERE / "outputs" / "b13_b16_comparison_2026-11-08.json"
    )
    parser.add_argument(
        "--output", type=Path,
        default=HERE / "outputs" / "b13_b16_low_mass_scan_2026-11-08.json"
    )
    parser.add_argument(
        "--masses", type=str, default=",".join(str(x) for x in NEW_MASSES_MEV),
        help="comma-separated new masses in MeV; the existing 10 MeV case is added automatically",
    )
    args = parser.parse_args()
    masses = tuple(float(x.strip()) for x in args.masses.split(",") if x.strip())
    if not masses or any(x <= 0.0 or x >= REFERENCE_MASS_MEV for x in masses):
        raise ValueError("New masses must be positive and below the 10 MeV reference")
    result = run_mass_scan(args.profile, args.reference_output, masses)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    for mass, radii in result["mass_cases"].items():
        for radius, case in radii.items():
            rel = case["relative_differences"]
            print(json.dumps({
                "mass_MeV": mass,
                "r_km": radius,
                "recomputed": case["recomputed"],
                "B13_over_B16_minus_1": rel[
                    "B13_vector_vs_B16_corrected_fraction"
                ],
                "B13_over_stationary_exact_minus_1": rel[
                    "B13_vector_vs_stationary_exact_recoil_fraction"
                ],
                "B16_mass_correction": rel[
                    "B16_integrated_mass_correction_fraction"
                ],
                "muon_rms_velocity": case[
                    "muon_nonrelativistic_diagnostics"
                ]["species"]["combined"]["rms_velocity"],
            }, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
