"""Radial fixed-energy comparison of exact B.13 and approximate B.14--B.16 opacity.

This is a local diagnostic only. It does not replace the published-reference
B.14--B.16 baseline, integrate B.2 paths, or generate/update any cooling curve.
The exact moving-muon B.13 kernel is evaluated charge by charge so that the
mu-minus result can be compared like-for-like with the one-species B.17
reference convention.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from blinov_reproduction.reference import DEFAULT_PROFILE, load_profile, local_rates
from finite_mixing.moving_muon_compton import moving_muon_compton_rates

DEFAULT_OUTPUT = HERE / "outputs" / "b13_exact_compton_opacity_radial_10mev_2026-11-09.json"
MASS_MEV = 10.0
RADII_KM = (8.0, 10.0, 12.5, 15.0, 18.5, 20.0, 22.0)
ENERGIES_MEV = (12.0, 15.0, 20.0, 30.0, 50.0, 80.0)
BASE_ORDERS = (12, 8, 8, 8)
REFINED_ORDERS = (16, 10, 10, 10)
REFINEMENT_POINTS = ((8.0, 15.0), (12.5, 20.0), (15.0, 30.0))


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rel(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(b)), 1.0e-300)


def _species_rates(result, species: str):
    item = result["charge_resolved"][species]
    production = np.asarray(item["production"], float)
    absorption = np.asarray(item["absorption"], float)
    return float(np.sum(production)), float(np.sum(absorption)), production, absorption


def run(profile_path: Path = DEFAULT_PROFILE, mass: float = MASS_MEV,
        base_orders=BASE_ORDERS, refined_orders=REFINED_ORDERS):
    radii = np.asarray(RADII_KM, float)
    energies = np.asarray(ENERGIES_MEV, float)
    profile = load_profile(profile_path, radii)
    reference = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )

    rows = []
    maxima = {
        "B13_mu_minus_mode_detailed_balance": 0.0,
        "B13_mu_plus_mode_detailed_balance": 0.0,
        "B13_mu_minus_absorption_vs_production": 0.0,
        "B13_mu_plus_absorption_vs_production": 0.0,
    }

    for ir, radius in enumerate(radii):
        temperature = float(profile["T"][ir])
        mu_mu = float(profile["mu_mu"][ir])
        for ie, omega in enumerate(energies):
            exact = moving_muon_compton_rates(
                mass, float(omega), temperature, mu_mu,
                1.0, 0.0, orders=tuple(base_orders)
            )
            p_minus, a_minus, pm_modes, am_modes = _species_rates(exact, "mu_minus")
            p_plus, a_plus, pp_modes, ap_modes = _species_rates(exact, "mu_plus")
            x = float(omega / temperature)
            boltzmann = np.exp(-x)
            reduced_factor = 1.0 - boltzmann

            db_minus = float(np.max(
                np.abs(pm_modes - boltzmann * am_modes)
                / np.maximum(np.abs(pm_modes), 1.0e-300)
            ))
            db_plus = float(np.max(
                np.abs(pp_modes - boltzmann * ap_modes)
                / np.maximum(np.abs(pp_modes), 1.0e-300)
            ))
            maxima["B13_mu_minus_mode_detailed_balance"] = max(
                maxima["B13_mu_minus_mode_detailed_balance"], db_minus
            )
            maxima["B13_mu_plus_mode_detailed_balance"] = max(
                maxima["B13_mu_plus_mode_detailed_balance"], db_plus
            )
            maxima["B13_mu_minus_absorption_vs_production"] = max(
                maxima["B13_mu_minus_absorption_vs_production"],
                rel(p_minus, boltzmann * a_minus)
            )
            maxima["B13_mu_plus_absorption_vs_production"] = max(
                maxima["B13_mu_plus_absorption_vs_production"],
                rel(p_plus, boltzmann * a_plus)
            )

            b16_production = float(reference["compton_production"][ir, ie])
            b16_reduced = float(np.expm1(x) * b16_production)
            b13_minus_reduced = float(reduced_factor * a_minus)
            b13_plus_reduced = float(reduced_factor * a_plus)
            b13_both_reduced = b13_minus_reduced + b13_plus_reduced
            neutrino_reduced = float(
                np.expm1(x) * reference["neutrino_production"][ir, ie]
            )
            baseline_total = neutrino_reduced + b16_reduced
            exact_minus_total = neutrino_reduced + b13_minus_reduced
            exact_both_total = neutrino_reduced + b13_both_reduced

            rows.append({
                "radius_km": float(radius),
                "omega_MeV": float(omega),
                "T_MeV": temperature,
                "mu_mu_MeV": mu_mu,
                "B16_reference_mu_minus_production_MeV": b16_production,
                "B16_reference_mu_minus_reduced_absorption_MeV": b16_reduced,
                "B13_exact_mu_minus_production_MeV": p_minus,
                "B13_exact_mu_minus_absorption_MeV": a_minus,
                "B13_exact_mu_minus_reduced_absorption_MeV": b13_minus_reduced,
                "B13_exact_mu_plus_production_MeV": p_plus,
                "B13_exact_mu_plus_absorption_MeV": a_plus,
                "B13_exact_mu_plus_reduced_absorption_MeV": b13_plus_reduced,
                "B13_exact_both_charges_reduced_absorption_MeV": b13_both_reduced,
                "B13_over_B16_mu_minus_production": (
                    p_minus / b16_production if b16_production > 0.0 else None
                ),
                "B13_over_B16_mu_minus_reduced_absorption": (
                    b13_minus_reduced / b16_reduced if b16_reduced > 0.0 else None
                ),
                "mu_plus_fraction_of_B13_Compton_reduced_absorption": (
                    b13_plus_reduced / b13_both_reduced
                    if b13_both_reduced > 0.0 else 0.0
                ),
                "neutrino_reduced_absorption_MeV": neutrino_reduced,
                "B16_total_local_reduced_absorption_MeV": baseline_total,
                "B13_mu_minus_total_local_reduced_absorption_MeV": exact_minus_total,
                "B13_both_charge_total_local_reduced_absorption_MeV": exact_both_total,
                "B16_Compton_fraction_of_total_opacity": (
                    b16_reduced / baseline_total if baseline_total > 0.0 else 0.0
                ),
                "B13_mu_minus_Compton_fraction_of_total_opacity": (
                    b13_minus_reduced / exact_minus_total
                    if exact_minus_total > 0.0 else 0.0
                ),
                "B13_mu_minus_change_in_total_local_opacity": (
                    exact_minus_total / baseline_total - 1.0
                    if baseline_total > 0.0 else None
                ),
                "B13_mode_detailed_balance_residuals": {
                    "mu_minus": db_minus,
                    "mu_plus": db_plus,
                },
                "B13_final_muon_shell_relative_error": (
                    exact["diagnostics"]["final_muon_shell_relative_error"]
                ),
            })

    refinement = []
    for radius, omega in REFINEMENT_POINTS:
        ir = int(np.argmin(np.abs(radii - radius)))
        temperature = float(profile["T"][ir])
        mu_mu = float(profile["mu_mu"][ir])
        base = moving_muon_compton_rates(
            mass, omega, temperature, mu_mu, 1.0, 0.0,
            orders=tuple(base_orders)
        )
        fine = moving_muon_compton_rates(
            mass, omega, temperature, mu_mu, 1.0, 0.0,
            orders=tuple(refined_orders)
        )
        base_minus = float(np.sum(base["charge_resolved"]["mu_minus"]["production"]))
        fine_minus = float(np.sum(fine["charge_resolved"]["mu_minus"]["production"]))
        base_plus = float(np.sum(base["charge_resolved"]["mu_plus"]["production"]))
        fine_plus = float(np.sum(fine["charge_resolved"]["mu_plus"]["production"]))
        refinement.append({
            "radius_km": float(radius),
            "omega_MeV": float(omega),
            "base_orders": list(base_orders),
            "refined_orders": list(refined_orders),
            "mu_minus_relative_change": rel(fine_minus, base_minus),
            "mu_plus_relative_change": rel(fine_plus, base_plus),
            "base_final_muon_shell_relative_error": (
                base["diagnostics"]["final_muon_shell_relative_error"]
            ),
            "refined_final_muon_shell_relative_error": (
                fine["diagnostics"]["final_muon_shell_relative_error"]
            ),
        })

    return {
        "title": "Radial fixed-energy comparison of exact B.13 and approximate B.14--B.16 Compton opacity",
        "mass_MeV": float(mass),
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "identity": "reconstructed public-figure SFHo-18.8 profile, not raw Garching simulation data",
        },
        "configuration": {
            "radii_km": list(RADII_KM),
            "energies_MeV": list(ENERGIES_MEV),
            "B13_base_orders": list(base_orders),
            "B13_refined_orders": list(refined_orders),
            "current": "pure vector, g_V=1, g_A=0, rates per g_X^2",
            "comparison_convention": "B13 mu-minus-only is compared with the one-species B.17 B16 reference; mu-plus is reported separately",
        },
        "maximum_residuals": maxima,
        "refinement_checks": refinement,
        "pointwise_results": rows,
        "scope": [
            "This is a local fixed-energy opacity diagnostic, not a B.2 path integration.",
            "B.13 exact moving-muon rates are not substituted into the published-reference B.14--B.16 baseline.",
            "No source, coupling, opacity, luminosity, or axial-vector rescaling is applied.",
            "No axial-vector cooling curve is generated or updated.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--mass", type=float, default=MASS_MEV)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.profile, args.mass)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "configuration": result["configuration"],
        "maximum_residuals": result["maximum_residuals"],
        "refinement_checks": result["refinement_checks"],
        "number_of_points": len(result["pointwise_results"]),
    }, indent=2, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
