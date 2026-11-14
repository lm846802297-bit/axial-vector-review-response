"""Dense radial-energy and quadrature convergence audit for the exact B.13 kernel.

This is a pure-vector, 10 MeV local-kernel audit on the reconstructed
SFHo-18.8, t_pb=1 s profile. It retains both muon charges and L,+,- modes,
and never changes the scalar B.2 or production axial-vector results.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
FINITE_MIXING = HERE.parent
ROOT = FINITE_MIXING.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from blinov_reproduction.reference import DEFAULT_PROFILE, load_profile
from finite_mixing.moving_muon_compton import (
    moving_muon_compton_rates,
    thermal_compton_emissivity,
)

MASS_MEV = 10.0
G_VECTOR = 1.0
G_AXIAL = 0.0
EXPECTED_PROFILE_SHA256 = (
    "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
)
BASE_RADII_KM = (
    0.0, 5.0, 8.0, 8.4821412022467, 10.0, 12.5, 15.0, 18.66, 22.0, 24.0,
)
BASE_ENERGIES_MEV = (
    10.0, 10.5, 12.0, 15.0, 20.0, 30.0,
    50.0, 80.0, 120.0, 200.0, 300.0, 510.0, 720.0, 1500.0,
)


def _bisect_radial_grid(nodes):
    midpoints = [0.5 * (a + b) for a, b in zip(nodes, nodes[1:])]
    return tuple(sorted(set(nodes).union(midpoints)))


def _bisect_energy_grid(nodes):
    midpoints = []
    for a, b in zip(nodes, nodes[1:]):
        ya = math.sqrt(max(a - MASS_MEV, 0.0))
        yb = math.sqrt(max(b - MASS_MEV, 0.0))
        midpoints.append(MASS_MEV + (0.5 * (ya + yb)) ** 2)
    return tuple(sorted(set(nodes).union(midpoints)))


# One systematic bisection of the original radial and sqrt(omega-m) grids.
RADII_KM = _bisect_radial_grid(BASE_RADII_KM)
ENERGIES_MEV = _bisect_energy_grid(BASE_ENERGIES_MEV)
GRID_ORDERS = (
    (16, 10, 10, 10),
    (20, 12, 12, 12),
)
REFINEMENT_ORDERS = (
    (24, 14, 14, 14),
    (28, 16, 16, 16),
)
MIDPOINT_ORDERS = (
    (16, 10, 10, 10),
    (20, 12, 12, 12),
)
ENERGY_INTEGRAL_RADII_KM = (
    0.0, 5.0, 8.0, 8.4821412022467, 10.0, 12.5, 15.0, 18.66, 22.0, 24.0,
)
ENERGY_INTEGRAL_ORDERS = (8, 12, 16, 20)
ENERGY_INTEGRAL_REFINEMENTS = (24, 28)
ENERGY_INTEGRAL_INNER_ORDERS = (20, 12, 12, 12)
ENERGY_INTEGRAL_X_MAX = 36.0
MODES = ("L", "+", "-")
CHARGES = ("mu_minus", "mu_plus")
RATE_FIELDS = ("production", "absorption", "reduced_absorption", "spectral_source")
QUADRATURE_TOLERANCE = 1.0e-3
INTERPOLATION_TOLERANCE = 1.0e-2
DB_TOLERANCE = 2.0e-10
SHELL_TOLERANCE = 2.0e-10


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _as_float_list(values):
    return [float(x) for x in np.asarray(values, dtype=float)]


def _max_relative_difference(a, b):
    aa = np.asarray(a, dtype=float)
    bb = np.asarray(b, dtype=float)
    denom = np.maximum(np.maximum(np.abs(aa), np.abs(bb)), 1.0e-300)
    return float(np.max(np.abs(aa - bb) / denom))


def _channel_payload(raw, omega, temperature):
    """Convert a local kernel result to charge/mode-resolved audit channels."""
    factor_reduced = -math.expm1(-omega / temperature)
    k_a = math.sqrt(max(omega * omega - MASS_MEV * MASS_MEV, 0.0))
    spectral_prefactor = omega * omega * k_a / (2.0 * math.pi**2)
    result = {}
    max_db = 0.0
    min_m2 = math.inf
    max_m2 = 0.0
    all_finite_nonnegative = True
    for charge in CHARGES:
        item = raw["charge_resolved"][charge]
        production = np.asarray(item["production"], dtype=float)
        absorption = np.asarray(item["absorption"], dtype=float)
        reduced_absorption = factor_reduced * absorption
        spectral_source = spectral_prefactor * production
        expected_production = math.exp(-omega / temperature) * absorption
        db = np.abs(production - expected_production) / np.maximum(
            np.maximum(np.abs(production), np.abs(expected_production)), 1.0e-300
        )
        max_db = max(max_db, float(np.max(db)))
        min_m2 = min(
            min_m2, float(item["minimum_matrix_element_before_roundoff_clip"])
        )
        max_m2 = max(max_m2, float(item["maximum_matrix_element"]))
        all_finite_nonnegative = all_finite_nonnegative and all(
            np.all(np.isfinite(x)) and np.all(x >= 0.0)
            for x in (production, absorption, reduced_absorption, spectral_source)
        )
        result[charge] = {
            "production": _as_float_list(production),
            "absorption": _as_float_list(absorption),
            "reduced_absorption": _as_float_list(reduced_absorption),
            "spectral_source": _as_float_list(spectral_source),
            "mode_detailed_balance_relative_residual": _as_float_list(db),
            "minimum_matrix_element_before_roundoff_clip": float(
                item["minimum_matrix_element_before_roundoff_clip"]
            ),
            "maximum_matrix_element": float(item["maximum_matrix_element"]),
        }

    total_prod = np.asarray(raw["production"], dtype=float)
    total_abs = np.asarray(raw["absorption"], dtype=float)
    charge_prod = sum(
        np.asarray(raw["charge_resolved"][c]["production"], dtype=float)
        for c in CHARGES
    )
    charge_abs = sum(
        np.asarray(raw["charge_resolved"][c]["absorption"], dtype=float)
        for c in CHARGES
    )
    sum_closure = max(
        _max_relative_difference(total_prod, charge_prod),
        _max_relative_difference(total_abs, charge_abs),
    )
    return {
        "charge_resolved": result,
        "maximum_mode_detailed_balance_relative_residual": max_db,
        "minimum_matrix_element_before_roundoff_clip": min_m2,
        "maximum_matrix_element": max_m2,
        "all_rates_finite_and_nonnegative": bool(all_finite_nonnegative),
        "charge_sum_closure_relative_residual": sum_closure,
        "total_production_by_mode": _as_float_list(total_prod),
        "total_absorption_by_mode": _as_float_list(total_abs),
        "total_reduced_absorption_by_mode": _as_float_list(
            factor_reduced * total_abs
        ),
        "total_spectral_source_by_mode": _as_float_list(
            spectral_prefactor * total_prod
        ),
    }


def evaluate_point(profile_path, radius, omega, orders, cache):
    key = (float(radius), float(omega), tuple(int(x) for x in orders))
    if key in cache:
        return cache[key]
    background = load_profile(profile_path, np.asarray([radius], dtype=float))
    temperature = float(background["T"][0])
    mu_mu = float(background["mu_mu"][0])
    lapse = float(background["lapse"][0])
    raw = moving_muon_compton_rates(
        MASS_MEV,
        float(omega),
        temperature,
        mu_mu,
        g_vector=G_VECTOR,
        g_axial=G_AXIAL,
        orders=tuple(orders),
    )
    channels = _channel_payload(raw, float(omega), temperature)
    result = {
        "radius_km": float(radius),
        "omega_local_MeV": float(omega),
        "temperature_MeV": temperature,
        "mu_minus_chemical_potential_MeV": mu_mu,
        "lapse": lapse,
        "orders": list(orders),
        "mode_order": list(MODES),
        "charge_resolved": channels["charge_resolved"],
        "maximum_mode_detailed_balance_relative_residual": channels[
            "maximum_mode_detailed_balance_relative_residual"
        ],
        "minimum_matrix_element_before_roundoff_clip": channels[
            "minimum_matrix_element_before_roundoff_clip"
        ],
        "maximum_matrix_element": channels["maximum_matrix_element"],
        "all_rates_finite_and_nonnegative": channels[
            "all_rates_finite_and_nonnegative"
        ],
        "charge_sum_closure_relative_residual": channels[
            "charge_sum_closure_relative_residual"
        ],
        "total_production_by_mode": channels["total_production_by_mode"],
        "total_absorption_by_mode": channels["total_absorption_by_mode"],
        "total_reduced_absorption_by_mode": channels[
            "total_reduced_absorption_by_mode"
        ],
        "total_spectral_source_by_mode": channels[
            "total_spectral_source_by_mode"
        ],
        "final_muon_shell_relative_error": float(
            raw["diagnostics"]["final_muon_shell_relative_error"]
        ),
        "x_max": float(raw["diagnostics"]["x_max"]),
    }
    cache[key] = result
    return result


def compare_points(a, b):
    """Compare every charge, mode, source, opacity, and reduced-opacity channel."""
    details = {}
    maximum = 0.0
    for charge in CHARGES:
        details[charge] = {}
        for field in RATE_FIELDS:
            change = _max_relative_difference(
                a["charge_resolved"][charge][field],
                b["charge_resolved"][charge][field],
            )
            details[charge][field] = change
            maximum = max(maximum, change)
    return {
        "per_charge_and_field_max_relative_change": details,
        "maximum_relative_change": maximum,
    }


def _bilinear_log_value(corners, t_r=0.5, t_e=0.5):
    """Bilinear interpolation in log(rate); fall back to linear for zero corners."""
    weights = (
        (1.0 - t_r) * (1.0 - t_e),
        (1.0 - t_r) * t_e,
        t_r * (1.0 - t_e),
        t_r * t_e,
    )
    values = np.asarray(corners, dtype=float)
    if np.all(values > 0.0):
        return float(np.exp(np.dot(weights, np.log(values))))
    return float(np.dot(weights, values))


def _interpolate_pair(a, b, fraction=0.5):
    """Log-linear interpolation for positive rates, linear at a true zero."""
    a, b = float(a), float(b)
    if a > 0.0 and b > 0.0:
        return float(np.exp((1.0 - fraction) * np.log(a) + fraction * np.log(b)))
    return float((1.0 - fraction) * a + fraction * b)


def interpolate_cell(c00, c01, c10, c11, omega_mid, temperature_mid):
    """Interpolate absorption, then reconstruct other rates by detailed balance.

    Detailed balance is an exact local identity. Reconstructing production and
    reduced absorption with the midpoint temperature avoids interpolating the
    steep exp(-omega/T) factor as if it were an independent smooth table entry.
    The spectral source then receives its exact midpoint phase-space factor.
    """
    prediction = {}
    boltzmann = math.exp(-omega_mid / temperature_mid)
    reduced_factor = -math.expm1(-omega_mid / temperature_mid)
    k_mid = math.sqrt(max(omega_mid * omega_mid - MASS_MEV * MASS_MEV, 0.0))
    spectral_prefactor = omega_mid * omega_mid * k_mid / (2.0 * math.pi**2)
    for charge in CHARGES:
        arrays = [
            np.asarray(item["charge_resolved"][charge]["absorption"], dtype=float)
            for item in (c00, c01, c10, c11)
        ]
        bottom = [
            _interpolate_pair(arrays[0][mode], arrays[1][mode])
            for mode in range(3)
        ]
        top = [
            _interpolate_pair(arrays[2][mode], arrays[3][mode])
            for mode in range(3)
        ]
        absorption = [
            _interpolate_pair(bottom[mode], top[mode])
            for mode in range(3)
        ]
        production = [boltzmann * value for value in absorption]
        reduced_absorption = [reduced_factor * value for value in absorption]
        prediction[charge] = {
            "absorption": absorption,
            "production": production,
            "reduced_absorption": reduced_absorption,
            "spectral_source": [
                spectral_prefactor * value for value in production
            ],
        }
    return prediction

def compare_midpoint_to_interpolation(direct, prediction):
    details = {}
    maximum = 0.0
    for charge in CHARGES:
        details[charge] = {}
        for field in RATE_FIELDS:
            direct_values = np.asarray(
                direct["charge_resolved"][charge][field], dtype=float
            )
            predicted_values = np.asarray(prediction[charge][field], dtype=float)
            changes = np.abs(direct_values - predicted_values) / np.maximum(
                np.maximum(np.abs(direct_values), np.abs(predicted_values)),
                1.0e-300,
            )
            details[charge][field] = _as_float_list(changes)
            maximum = max(maximum, float(np.max(changes)))
    return {
        "per_charge_field_mode_relative_error": details,
        "maximum_relative_error": maximum,
    }


def _compare_emissivity_results(a, b):
    details = {}
    maximum = 0.0
    for charge in CHARGES:
        aa = a["emissivity_by_charge_and_mode_MeV5"][charge]
        bb = b["emissivity_by_charge_and_mode_MeV5"][charge]
        change = _max_relative_difference(aa, bb)
        details[charge] = change
        maximum = max(maximum, change)
    total_change = _max_relative_difference(
        a["emissivity_by_mode_MeV5"], b["emissivity_by_mode_MeV5"]
    )
    maximum = max(maximum, total_change)
    return {
        "per_charge_max_relative_change": details,
        "total_mode_max_relative_change": total_change,
        "maximum_relative_change": maximum,
    }


def evaluate_energy_integral(profile_path, radius, energy_order):
    background = load_profile(profile_path, np.asarray([radius], dtype=float))
    temperature = float(background["T"][0])
    mu_mu = float(background["mu_mu"][0])
    result = thermal_compton_emissivity(
        MASS_MEV,
        temperature,
        mu_mu,
        g_vector=G_VECTOR,
        g_axial=G_AXIAL,
        energy_order=int(energy_order),
        orders=ENERGY_INTEGRAL_INNER_ORDERS,
        x_max=ENERGY_INTEGRAL_X_MAX,
    )
    return {
        "radius_km": float(radius),
        "temperature_MeV": temperature,
        "mu_minus_chemical_potential_MeV": mu_mu,
        "energy_order": int(energy_order),
        "inner_orders": list(ENERGY_INTEGRAL_INNER_ORDERS),
        "x_max": ENERGY_INTEGRAL_X_MAX,
        "omega_max_local_MeV": MASS_MEV + ENERGY_INTEGRAL_X_MAX * temperature,
        "emissivity_by_mode_MeV5": result["emissivity_by_mode_MeV5"],
        "emissivity_by_charge_and_mode_MeV5": (
            result["emissivity_by_charge_and_mode_MeV5"]
        ),
        "emissivity_total_MeV5": result["emissivity_total_MeV5"],
        "max_detailed_balance_relative_error": (
            result["max_detailed_balance_relative_error"]
        ),
        "max_final_muon_shell_relative_error": (
            result["max_final_muon_shell_relative_error"]
        ),
    }


def run_energy_integral_audit(profile_path):
    """Converge the actual local emissivity energy integral at anchor radii."""
    results = []
    maximum_change = 0.0
    maximum_db = 0.0
    maximum_shell = 0.0
    all_nonnegative = True
    for radius in ENERGY_INTEGRAL_RADII_KM:
        ladder = [
            evaluate_energy_integral(profile_path, radius, order)
            for order in ENERGY_INTEGRAL_ORDERS
        ]
        comparisons = []
        for i in range(1, len(ladder)):
            comparisons.append({
                "from_energy_order": ladder[i - 1]["energy_order"],
                "to_energy_order": ladder[i]["energy_order"],
                **_compare_emissivity_results(ladder[i - 1], ladder[i]),
            })
        while comparisons[-1]["maximum_relative_change"] >= QUADRATURE_TOLERANCE:
            last_order = ladder[-1]["energy_order"]
            if last_order == ENERGY_INTEGRAL_ORDERS[-1]:
                next_order = ENERGY_INTEGRAL_REFINEMENTS[0]
            elif last_order == ENERGY_INTEGRAL_REFINEMENTS[0]:
                next_order = ENERGY_INTEGRAL_REFINEMENTS[1]
            else:
                break
            next_result = evaluate_energy_integral(profile_path, radius, next_order)
            comparisons.append({
                "from_energy_order": ladder[-1]["energy_order"],
                "to_energy_order": next_result["energy_order"],
                **_compare_emissivity_results(ladder[-1], next_result),
            })
            ladder.append(next_result)
        final_change = comparisons[-1]["maximum_relative_change"]
        maximum_change = max(maximum_change, final_change)
        maximum_db = max(
            maximum_db,
            *(x["max_detailed_balance_relative_error"] for x in ladder),
        )
        maximum_shell = max(
            maximum_shell,
            *(x["max_final_muon_shell_relative_error"] for x in ladder),
        )
        all_nonnegative = all_nonnegative and all(
            x["emissivity_total_MeV5"] >= 0.0
            and np.all(np.asarray(x["emissivity_by_mode_MeV5"]) >= 0.0)
            for x in ladder
        )
        results.append({
            "radius_km": radius,
            "order_ladder": ladder,
            "successive_refinement": comparisons,
            "final_energy_order": ladder[-1]["energy_order"],
            "final_refinement_relative_change": final_change,
            "energy_quadrature_pass": final_change < QUADRATURE_TOLERANCE,
        })
        print(
            f"Local emissivity energy integral at r={radius:6.2f} km complete "
            f"(final order={ladder[-1]['energy_order']})",
            flush=True,
        )
    return {
        "radii_km": list(ENERGY_INTEGRAL_RADII_KM),
        "energy_order_ladder": list(ENERGY_INTEGRAL_ORDERS),
        "adaptive_energy_orders": list(ENERGY_INTEGRAL_REFINEMENTS),
        "inner_local_kernel_orders": list(ENERGY_INTEGRAL_INNER_ORDERS),
        "x_max": ENERGY_INTEGRAL_X_MAX,
        "results": results,
        "acceptance": {
            "relative_tolerance": QUADRATURE_TOLERANCE,
            "pass": maximum_change < QUADRATURE_TOLERANCE,
            "maximum_successive_energy_order_change": maximum_change,
            "maximum_detailed_balance_residual": maximum_db,
            "maximum_final_muon_shell_residual": maximum_shell,
            "all_emissivities_nonnegative": all_nonnegative,
        },
    }


def _refine_if_needed(profile_path, radius, omega, ladder, cache, tolerance):
    """Adaptively add 24- or 28-order rules if the last refinement exceeds 0.1%."""
    comparisons = []
    for i in range(1, len(ladder)):
        comparisons.append({
            "from_orders": ladder[i - 1]["orders"],
            "to_orders": ladder[i]["orders"],
            **compare_points(ladder[i - 1], ladder[i]),
        })
    while comparisons[-1]["maximum_relative_change"] >= tolerance:
        last_orders = tuple(ladder[-1]["orders"])
        if last_orders == GRID_ORDERS[-1]:
            next_orders = REFINEMENT_ORDERS[0]
        elif last_orders == REFINEMENT_ORDERS[0]:
            next_orders = REFINEMENT_ORDERS[1]
        else:
            break
        next_result = evaluate_point(
            profile_path, radius, omega, next_orders, cache
        )
        comparisons.append({
            "from_orders": ladder[-1]["orders"],
            "to_orders": next_result["orders"],
            **compare_points(ladder[-1], next_result),
        })
        ladder.append(next_result)
    return ladder, comparisons


def run_audit(profile_path=DEFAULT_PROFILE, output_path=None):
    started = time.time()
    profile_path = Path(profile_path)
    if not profile_path.exists():
        raise FileNotFoundError(profile_path)
    profile_hash = sha256(profile_path)
    if profile_hash != EXPECTED_PROFILE_SHA256:
        raise RuntimeError(
            "Profile SHA-256 mismatch: "
            f"expected {EXPECTED_PROFILE_SHA256}, got {profile_hash}"
        )

    profile_table = np.genfromtxt(profile_path, delimiter=",", names=True)
    profile_temperature = np.asarray(profile_table["T_MeV"], dtype=float)
    peak_index = int(np.nanargmax(profile_temperature))
    maximum_temperature = float(profile_temperature[peak_index])
    maximum_temperature_radius = float(profile_table["r_km"][peak_index])
    required_maximum_energy = MASS_MEV + ENERGY_INTEGRAL_X_MAX * maximum_temperature
    if not any(
        abs(radius - maximum_temperature_radius) < 1.0e-8
        for radius in RADII_KM
    ):
        raise RuntimeError(
            "Radial grid does not include the maximum-temperature shell: "
            f"r_peak={maximum_temperature_radius:.9f} km"
        )
    if not any(
        abs(radius - maximum_temperature_radius) < 1.0e-8
        for radius in ENERGY_INTEGRAL_RADII_KM
    ):
        raise RuntimeError(
            "Local emissivity energy-integral audit omits the maximum-temperature shell"
        )
    if ENERGIES_MEV[-1] < required_maximum_energy:
        raise RuntimeError(
            "Radial-energy grid does not cover the full local emissivity cutoff: "
            f"grid maximum={ENERGIES_MEV[-1]:.6f} MeV, "
            f"required maximum={required_maximum_energy:.6f} MeV"
        )

    cache = {}
    grid_points = []
    grid_final = {}
    grid_comparison_max = 0.0
    grid_shell_max = 0.0
    grid_db_max = 0.0
    grid_all_positive = True

    print(
        f"Starting 10 MeV B.13 grid: {len(RADII_KM)} radii x "
        f"{len(ENERGIES_MEV)} energies; profile sha256={profile_hash}",
        flush=True,
    )

    # Perform the base-to-fine order ladder at every requested grid node.
    for ir, radius in enumerate(RADII_KM):
        for omega in ENERGIES_MEV:
            ladder = [
                evaluate_point(profile_path, radius, omega, orders, cache)
                for orders in GRID_ORDERS
            ]
            ladder, comparisons = _refine_if_needed(
                profile_path, radius, omega, ladder, cache,
                QUADRATURE_TOLERANCE,
            )
            final = ladder[-1]
            grid_final[(radius, omega)] = final
            local_change = comparisons[-1]["maximum_relative_change"]
            grid_comparison_max = max(grid_comparison_max, local_change)
            grid_shell_max = max(
                grid_shell_max, *(x["final_muon_shell_relative_error"] for x in ladder)
            )
            grid_db_max = max(
                grid_db_max,
                *(x["maximum_mode_detailed_balance_relative_residual"] for x in ladder),
            )
            grid_all_positive = grid_all_positive and all(
                x["all_rates_finite_and_nonnegative"] for x in ladder
            )
            grid_points.append({
                "radius_km": radius,
                "omega_local_MeV": omega,
                "order_ladder": ladder,
                "successive_refinement": comparisons,
                "final_order": final["orders"],
                "final_refinement_relative_change": local_change,
                "quadrature_pass": local_change < QUADRATURE_TOLERANCE,
            })
        print(
            f"Grid radius {radius:6.2f} km complete "
            f"({(ir + 1) * len(ENERGIES_MEV)}/{len(RADII_KM) * len(ENERGIES_MEV)} nodes; "
            f"cache={len(cache)})",
            flush=True,
        )

    # Directly evaluate every radial-energy cell center. Energy midpoints are
    # centered in sqrt(omega-m), matching the threshold variable used by the
    # local emissivity integral.
    midpoint_points = []
    midpoint_final = {}
    midpoint_comparison_max = 0.0
    interpolation_max = 0.0
    midpoint_shell_max = 0.0
    midpoint_db_max = 0.0
    midpoint_all_positive = True

    for ir in range(len(RADII_KM) - 1):
        r0, r1 = RADII_KM[ir], RADII_KM[ir + 1]
        rmid = 0.5 * (r0 + r1)
        for ie in range(len(ENERGIES_MEV) - 1):
            w0, w1 = ENERGIES_MEV[ie], ENERGIES_MEV[ie + 1]
            y0 = math.sqrt(max(w0 - MASS_MEV, 0.0))
            y1 = math.sqrt(max(w1 - MASS_MEV, 0.0))
            omega_mid = MASS_MEV + (0.5 * (y0 + y1)) ** 2
            ladder = [
                evaluate_point(profile_path, rmid, omega_mid, orders, cache)
                for orders in MIDPOINT_ORDERS
            ]
            ladder, comparisons = _refine_if_needed(
                profile_path, rmid, omega_mid, ladder, cache,
                QUADRATURE_TOLERANCE,
            )
            direct = ladder[-1]
            c00 = grid_final[(r0, w0)]
            c01 = grid_final[(r0, w1)]
            c10 = grid_final[(r1, w0)]
            c11 = grid_final[(r1, w1)]
            prediction = interpolate_cell(
                c00, c01, c10, c11, omega_mid, direct["temperature_MeV"]
            )
            interpolation = compare_midpoint_to_interpolation(
                direct, prediction
            )
            midpoint_final[(rmid, omega_mid)] = direct
            midpoint_comparison_max = max(
                midpoint_comparison_max,
                comparisons[-1]["maximum_relative_change"],
            )
            interpolation_max = max(
                interpolation_max, interpolation["maximum_relative_error"]
            )
            midpoint_shell_max = max(
                midpoint_shell_max,
                *(x["final_muon_shell_relative_error"] for x in ladder),
            )
            midpoint_db_max = max(
                midpoint_db_max,
                *(x["maximum_mode_detailed_balance_relative_residual"] for x in ladder),
            )
            midpoint_all_positive = midpoint_all_positive and all(
                x["all_rates_finite_and_nonnegative"] for x in ladder
            )
            midpoint_points.append({
                "radius_midpoint_km": rmid,
                "omega_midpoint_MeV": omega_mid,
                "energy_midpoint_coordinate": "sqrt(omega-mass)",
            "maximum_profile_temperature_MeV": maximum_temperature,
            "maximum_profile_temperature_radius_km": maximum_temperature_radius,
            "required_energy_coverage_from_x_max_MeV": required_maximum_energy,
            "energy_coverage_pass": bool(ENERGIES_MEV[-1] >= required_maximum_energy),
                "order_ladder": ladder,
                "successive_refinement": comparisons,
                "final_order": direct["orders"],
                "final_refinement_relative_change": comparisons[-1][
                    "maximum_relative_change"
                ],
                "sequential_log_interpolation": prediction,
                "direct_vs_interpolated": interpolation,
                "quadrature_pass": comparisons[-1][
                    "maximum_relative_change"
                ] < QUADRATURE_TOLERANCE,
                "interpolation_pass": interpolation["maximum_relative_error"]
                < INTERPOLATION_TOLERANCE,
            })
        print(
            f"Midpoint radial cell {r0:6.2f}-{r1:6.2f} km complete "
            f"({(ir + 1) * (len(ENERGIES_MEV) - 1)}/"
            f"{(len(RADII_KM) - 1) * (len(ENERGIES_MEV) - 1)} cells; "
            f"cache={len(cache)})",
            flush=True,
        )

    # Independently converge the complete local emissivity integral over omega.
    energy_integral_audit = run_energy_integral_audit(profile_path)

    # Isolate the integration dimensions at the worst grid point, rather than
    # changing all four orders together and guessing which angle controls it.
    worst_grid = max(
        grid_points, key=lambda x: x["final_refinement_relative_change"]
    )
    worst_radius = float(worst_grid["radius_km"])
    worst_omega = float(worst_grid["omega_local_MeV"])
    base_orders = (20, 12, 12, 12)
    dimension_variants = {
        "kinetic_energy_only": (24, 12, 12, 12),
        "muon_polar_angle_only": (20, 14, 12, 12),
        "photon_polar_angle_only": (20, 12, 14, 12),
        "relative_photon_azimuth_only": (20, 12, 12, 14),
        "all_dimensions_together": (24, 14, 14, 14),
    }
    dimension_base = evaluate_point(
        profile_path, worst_radius, worst_omega, base_orders, cache
    )
    dimension_isolation = []
    for label, orders in dimension_variants.items():
        varied = evaluate_point(
            profile_path, worst_radius, worst_omega, orders, cache
        )
        dimension_isolation.append({
            "variation": label,
            "base_orders": list(base_orders),
            "varied_orders": list(orders),
            **compare_points(dimension_base, varied),
        })

    # Aggregate only the directly sampled midpoint errors; this is an
    # interpolation screen, not a claimed global interpolation error bound.
    worst_midpoints = sorted(
        midpoint_points,
        key=lambda x: x["direct_vs_interpolated"]["maximum_relative_error"],
        reverse=True,
    )[:10]

    all_quadrature_pass = (
        grid_comparison_max < QUADRATURE_TOLERANCE
        and midpoint_comparison_max < QUADRATURE_TOLERANCE
    )
    all_detailed_balance_pass = (
        max(grid_db_max, midpoint_db_max) < DB_TOLERANCE
    )
    all_shell_pass = max(grid_shell_max, midpoint_shell_max) < SHELL_TOLERANCE
    all_positive = grid_all_positive and midpoint_all_positive
    interpolation_pass = interpolation_max < INTERPOLATION_TOLERANCE
    energy_integral_pass = energy_integral_audit["acceptance"]["pass"]

    result = {
        "title": "P1-B dense radial-energy convergence audit of exact B.13 local Compton kernel",
        "date": "2026-11-13",
        "status": "completed_numerical_audit",
        "physics_scope": {
            "mediator_mass_MeV": MASS_MEV,
            "current": "pure vector endpoint",
            "g_vector_over_gX": G_VECTOR,
            "g_axial_over_gX": G_AXIAL,
            "process": "muon + photon <-> muon + A'",
            "profile_identity": (
                "Reconstructed SFHo-18.8, t_pb=1 s, 1687-row vertex-preserving "
                "digitization; not raw Garching simulation data"
            ),
            "profile_sha256": profile_hash,
            "polarization_basis": "medium rest frame, A' momentum along +z",
            "mode_order": list(MODES),
            "charge_species": list(CHARGES),
            "rates": "local-frame coefficients per g_X^2",
        },
        "grid": {
            "base_radii_km": list(BASE_RADII_KM),
            "base_omega_local_MeV": list(BASE_ENERGIES_MEV),
            "refinement_depth": 1,
            "radii_km": list(RADII_KM),
            "omega_local_MeV": list(ENERGIES_MEV),
            "radial_nodes": len(RADII_KM),
            "energy_nodes": len(ENERGIES_MEV),
            "grid_node_count": len(grid_points),
            "radial_energy_cell_midpoint_count": len(midpoint_points),
            "quadrature_order_ladder": [list(x) for x in GRID_ORDERS],
            "midpoint_order_ladder": [list(x) for x in MIDPOINT_ORDERS],
            "adaptive_refinements": [list(x) for x in REFINEMENT_ORDERS],
            "quadrature_order_definition": [
                "muon kinetic-energy variable x=(E_mu-m_mu)/T with t=sqrt(x)",
                "cos(theta_mu)",
                "cos(theta_gamma)",
                "relative photon azimuth",
            ],
            "energy_midpoint_coordinate": "sqrt(omega-mass)",
        },
        "acceptance": {
            "quadrature_relative_tolerance": QUADRATURE_TOLERANCE,
            "quadrature_pass": bool(all_quadrature_pass),
            "maximum_grid_node_final_refinement_change": grid_comparison_max,
            "maximum_cell_midpoint_final_refinement_change": midpoint_comparison_max,
            "interpolation_relative_tolerance": INTERPOLATION_TOLERANCE,
            "interpolation_pass": bool(interpolation_pass),
            "local_emissivity_energy_integral_pass": bool(energy_integral_pass),
            "maximum_local_emissivity_energy_order_change": energy_integral_audit[
                "acceptance"
            ]["maximum_successive_energy_order_change"],
            "maximum_direct_midpoint_vs_sequential_log_interpolation_error": interpolation_max,
            "detailed_balance_tolerance": DB_TOLERANCE,
            "detailed_balance_pass": bool(all_detailed_balance_pass),
            "maximum_mode_detailed_balance_relative_residual": max(
                grid_db_max, midpoint_db_max
            ),
            "mass_shell_tolerance": SHELL_TOLERANCE,
            "mass_shell_pass": bool(all_shell_pass),
            "maximum_final_muon_mass_shell_relative_error": max(
                grid_shell_max, midpoint_shell_max
            ),
            "finite_nonnegative_rates_pass": bool(all_positive),
            "overall_p1b_pass": bool(
                all_quadrature_pass
                and interpolation_pass
                and energy_integral_pass
                and all_detailed_balance_pass
                and all_shell_pass
                and all_positive
            ),
            "screening_thresholds_are_project_numerical_criteria_not_literature_bounds": True,
        },
        "worst_grid_point": {
            "radius_km": worst_radius,
            "omega_local_MeV": worst_omega,
            "final_refinement_relative_change": worst_grid[
                "final_refinement_relative_change"
            ],
        },
        "quadrature_dimension_isolation_at_worst_grid_point": dimension_isolation,
        "local_emissivity_energy_integral_audit": energy_integral_audit,
        "ten_worst_interpolation_cells": worst_midpoints,
        "grid_node_results": grid_points,
        "radial_energy_midpoint_results": midpoint_points,
        "source_sha256": {
            "moving_muon_compton_py": sha256(
                FINITE_MIXING / "moving_muon_compton.py"
            ),
            "rates_py": sha256(ROOT / "rates.py"),
            "reference_py": sha256(ROOT / "blinov_reproduction" / "reference.py"),
            "audit_script": sha256(Path(__file__)),
            "profile_provenance_json": sha256(
                ROOT / "data" / "profile_provenance.json"
            ),
        },
        "runtime_seconds": time.time() - started,
        "interpretation_boundary": [
            "This audit validates local collision-kernel quadrature and sampled radial-energy interpolation only.",
            "It does not perform the global B.1 source integral, B.2 path optical-depth integral, or independent-mode transport.",
            "It does not modify the scalar B.2 baseline, vector Fig. 7 reference, production axial-vector scan, or any exclusion curve.",
            "The 0.1% quadrature and 1% interpolation criteria are project screening targets, not published physical uncertainties.",
            "The local emissivity energy integral uses omega=m_Aprime+T*y^2 with y in [0,6], matching x_max=36 of the existing local-emissivity routine.",
        ],
    }

    if output_path is None:
        output_path = (
            HERE / "outputs"
            / "p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.json"
        )
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("\nP1-B acceptance summary:")
    print(json.dumps(result["acceptance"], indent=2, sort_keys=True))
    print(f"Saved {output_path}")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "outputs"
        / "p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.json",
    )
    args = parser.parse_args()
    run_audit(args.profile, args.output)


if __name__ == "__main__":
    main()
