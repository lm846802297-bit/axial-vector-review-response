#!/usr/bin/env python3
"""High-order local quadrature convergence audit for the exact B.13 moving-muon kernel.

This is a local collision-kernel diagnostic only. It does not modify the production
rate implementation, replace the B.14--B.16 Fig. 7 reference baseline, perform a
B.2 path integral, or generate an axial-vector cooling curve.

Quadrature orders are (muon kinetic-energy, cos(theta_mu), cos(theta_gamma),
relative photon azimuth). Production and absorption are retained independently
from the kernel output and checked mode by mode for detailed balance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "finite_mixing") not in sys.path:
    sys.path.insert(0, str(ROOT / "finite_mixing"))

from blinov_reproduction.reference import DEFAULT_PROFILE, load_profile
from moving_muon_compton import moving_muon_compton_rates

MASS_MEV = 10.0
SAMPLE_POINTS = ((8.0, 15.0), (12.5, 20.0), (15.0, 30.0))
ORDER_LADDER = (
    (12, 8, 8, 8),
    (16, 10, 10, 10),
    (20, 12, 12, 12),
    (24, 14, 14, 14),
)
DIMENSION_BASE = (20, 12, 12, 12)
DIMENSION_VARIANTS = {
    "kinetic_energy_only": (24, 12, 12, 12),
    "muon_polar_angle_only": (20, 14, 12, 12),
    "photon_polar_angle_only": (20, 12, 14, 12),
    "relative_photon_azimuth_only": (20, 12, 12, 14),
    "all_dimensions_together": (24, 14, 14, 14),
}
CHARGES = ("mu_minus", "mu_plus")
MODES = ("L", "+", "-")


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def relative_change(a, b) -> float:
    aa, bb = np.asarray(a, float), np.asarray(b, float)
    return float(np.max(np.abs(aa - bb) / np.maximum(np.abs(bb), 1.0e-300)))


def extract_species(result, species: str, omega: float, temperature: float):
    item = result["charge_resolved"][species]
    production = np.asarray(item["production"], float)
    absorption = np.asarray(item["absorption"], float)
    reduced = (1.0 - math.exp(-omega / temperature)) * absorption
    balance = relative_change(production, math.exp(-omega / temperature) * absorption)
    return {
        "production_modes_MeV": production.tolist(),
        "absorption_modes_MeV": absorption.tolist(),
        "reduced_absorption_modes_MeV": reduced.tolist(),
        "production_sum_MeV": float(np.sum(production)),
        "absorption_sum_MeV": float(np.sum(absorption)),
        "reduced_absorption_sum_MeV": float(np.sum(reduced)),
        "mode_detailed_balance_max_relative_residual": balance,
        "minimum_matrix_element_before_roundoff_clip": float(
            item["minimum_matrix_element_before_roundoff_clip"]
        ),
        "maximum_matrix_element": float(item["maximum_matrix_element"]),
    }


def compare_species(a: dict, b: dict):
    fields = (
        "production_modes_MeV",
        "absorption_modes_MeV",
        "reduced_absorption_modes_MeV",
    )
    return {
        field: relative_change(a[field], b[field])
        for field in fields
    } | {
        "maximum_over_production_absorption_and_reduced_absorption": max(
            relative_change(a[field], b[field]) for field in fields
        )
    }


def run(profile_path: Path, output_path: Path, mass_mev: float = MASS_MEV):
    cache = {}
    def evaluate(radius: float, omega: float, orders: tuple[int, int, int, int]):
        key = (radius, omega, tuple(orders))
        if key in cache:
            return cache[key]
        local = load_profile(profile_path, np.asarray([radius], float))
        temperature = float(local["T"][0])
        mu_mu = float(local["mu_mu"][0])
        result = moving_muon_compton_rates(
            mass_mev, omega, temperature, mu_mu,
            g_vector=1.0, g_axial=0.0, orders=tuple(orders)
        )
        row = {
            "radius_km": radius,
            "omega_MeV": omega,
            "temperature_MeV": temperature,
            "mu_minus_chemical_potential_MeV": mu_mu,
            "orders": list(orders),
            "x_max": result["diagnostics"]["x_max"],
            "final_muon_shell_relative_error": result["diagnostics"][
                "final_muon_shell_relative_error"
            ],
            "charges": {
                charge: extract_species(result, charge, omega, temperature)
                for charge in CHARGES
            },
        }
        cache[key] = row
        return row

    point_results = []
    maximum_shell_error = 0.0
    maximum_balance_error = 0.0
    maximum_20_to_24_change = 0.0
    maximum_16_to_20_change = 0.0

    for radius, omega in SAMPLE_POINTS:
        ladder = [evaluate(radius, omega, order) for order in ORDER_LADDER]
        comparisons = []
        for i in range(1, len(ladder)):
            per_charge = {
                charge: compare_species(
                    ladder[i]["charges"][charge], ladder[i - 1]["charges"][charge]
                )
                for charge in CHARGES
            }
            comparisons.append({
                "from_orders": ladder[i - 1]["orders"],
                "to_orders": ladder[i]["orders"],
                "per_charge": per_charge,
                "maximum_relative_change": max(
                    per_charge[c]["maximum_over_production_absorption_and_reduced_absorption"]
                    for c in CHARGES
                ),
            })
        high_vs_fine = comparisons[-1]["maximum_relative_change"]
        mid_vs_low = comparisons[-2]["maximum_relative_change"]
        maximum_20_to_24_change = max(maximum_20_to_24_change, high_vs_fine)
        maximum_16_to_20_change = max(maximum_16_to_20_change, mid_vs_low)
        for item in ladder:
            maximum_shell_error = max(
                maximum_shell_error, item["final_muon_shell_relative_error"]
            )
            maximum_balance_error = max(
                maximum_balance_error,
                *(item["charges"][c]["mode_detailed_balance_max_relative_residual"]
                  for c in CHARGES)
            )
        point_results.append({
            "radius_km": radius,
            "omega_MeV": omega,
            "temperature_MeV": ladder[-1]["temperature_MeV"],
            "mu_minus_chemical_potential_MeV": ladder[-1][
                "mu_minus_chemical_potential_MeV"
            ],
            "order_ladder": ladder,
            "successive_refinement": comparisons,
            "highest_order_assessment": {
                "orders_20x12x12x12_to_24x14x14x14_max_relative_change": high_vs_fine,
                "orders_16x10x10x10_to_20x12x12x12_max_relative_change": mid_vs_low,
            },
        })

    # Isolate the four integration dimensions at the most demanding sampled point.
    worst_radius, worst_omega = SAMPLE_POINTS[0]
    dimension_base = evaluate(worst_radius, worst_omega, DIMENSION_BASE)
    dimension_rows = []
    for label, orders in DIMENSION_VARIANTS.items():
        varied = evaluate(worst_radius, worst_omega, orders)
        per_charge = {
            charge: compare_species(
                varied["charges"][charge], dimension_base["charges"][charge]
            )
            for charge in CHARGES
        }
        dimension_rows.append({
            "variation": label,
            "base_orders": list(DIMENSION_BASE),
            "varied_orders": list(orders),
            "per_charge": per_charge,
            "maximum_relative_change": max(
                per_charge[c]["maximum_over_production_absorption_and_reduced_absorption"]
                for c in CHARGES
            ),
            "final_muon_shell_relative_error": varied[
                "final_muon_shell_relative_error"
            ],
        })

    # The current profile identity is a fixed input, not a fit parameter.
    profile_hash = sha256(profile_path)
    expected_profile_hash = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
    result = {
        "title": "B.13 exact moving-muon local collision-kernel quadrature convergence",
        "status": "diagnostic_run_completed_no_predeclared_local_tolerance",
        "mass_MeV": float(mass_mev),
        "current": "pure vector, g_V=1, g_A=0, rates per g_X^2",
        "profile": {
            "path": str(profile_path),
            "sha256": profile_hash,
            "expected_vertex_preserving_sha256": expected_profile_hash,
            "identity": "1687-row vertex-preserving reconstruction of public-figure SFHo-18.8 profile; not raw Garching simulation data",
            "matches_expected_profile": profile_hash == expected_profile_hash,
        },
        "quadrature_definition": [
            "muon kinetic-energy variable x=(E_mu-m_mu)/T with t=sqrt(x)",
            "cos(theta_mu), the angle of the initial muon relative to the mediator",
            "cos(theta_gamma), the photon polar angle",
            "relative photon azimuth phi_gamma in [0,2pi]",
        ],
        "configuration": {
            "sample_points_r_km_omega_MeV": [list(x) for x in SAMPLE_POINTS],
            "order_ladder": [list(x) for x in ORDER_LADDER],
            "dimension_isolation_point_r_km_omega_MeV": [worst_radius, worst_omega],
            "dimension_isolation_base_orders": list(DIMENSION_BASE),
            "dimension_isolation_variants": {
                key: list(value) for key, value in DIMENSION_VARIANTS.items()
            },
            "charge_species": list(CHARGES),
            "polarization_modes": list(MODES),
        },
        "pointwise_results": point_results,
        "dimension_isolation": dimension_rows,
        "summary": {
            "maximum_final_muon_shell_relative_error": maximum_shell_error,
            "maximum_mode_detailed_balance_relative_residual": maximum_balance_error,
            "maximum_16_to_20_refinement_change": maximum_16_to_20_change,
            "maximum_20_to_24_refinement_change": maximum_20_to_24_change,
            "local_kernel_convergence_screening_target": 1.0e-3,
            "screening_target_is_project_diagnostic_not_literature_bound": True,
            "screening_target_passed": maximum_20_to_24_change < 1.0e-3,
            "local_kernel_convergence_certified": maximum_20_to_24_change < 1.0e-3,
            "note": (
                "A 0.1% local screening target is adopted explicitly for this audit. "
                "If the highest-order ladder fails it, increase the relevant "
                "quadrature dimensions before treating the local kernel as converged."
            ),
        },
        "scope": [
            "Local B.13 collision-kernel quadrature only; no global B.1/B.2 integration.",
            "Production and absorption are computed independently from the same exact phase-space kernel and retained by charge and polarization.",
            "The mu-minus and mu-plus contributions are evaluated separately.",
            "No density, source, opacity, coupling, luminosity, or rate rescaling.",
            "The published B.14--B.16 vector reference baseline is not modified.",
            "No production axial-vector output or constraint curve is changed.",
        ],
        "source_sha256": {
            "moving_muon_compton_py": sha256(ROOT / "finite_mixing" / "moving_muon_compton.py"),
            "rates_py": sha256(ROOT / "rates.py"),
            "reference_py": sha256(HERE / "reference.py"),
            "audit_script": sha256(Path(__file__)),
        },
    }
    if not result["profile"]["matches_expected_profile"]:
        raise RuntimeError(
            f"Profile hash mismatch: expected {expected_profile_hash}, got {profile_hash}"
        )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2, sort_keys=True))
    print(f"Saved {output_path}")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument(
        "--output", type=Path,
        default=HERE / "outputs" / "b13_local_kernel_quadrature_convergence_10mev_2026-11-09.json"
    )
    parser.add_argument("--mass", type=float, default=MASS_MEV)
    args = parser.parse_args()
    run(args.profile, args.output, args.mass)


if __name__ == "__main__":
    main()
