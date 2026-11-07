#!/usr/bin/env python3
"""Independent geometric and quadrature audit of Blinov Appendix-B Eq. (B.2).

The local collision rates and reconstructed profile are frozen to the existing
literal-reference inputs. This module independently evaluates the path integral
using an impact-parameter/longitudinal-coordinate representation. For the
piecewise-linear radial opacity interpolant used by reference.py, the line
integral is analytic on each radial cell. The angular average is recomputed at
higher Gauss-Legendre orders and checked at selected points by adaptive
quadrature.

No chemical potential, local rate, opacity normalization, or coupling is fit.
This is a scalar, polarization-summed Blinov reference-path audit only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        energy_weights, fermi_pair_average, load_profile, local_rates,
        radial_rule, scalar_optical_depths,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        energy_weights, fermi_pair_average, load_profile, local_rates,
        radial_rule, scalar_optical_depths,
    )

HERE = Path(__file__).resolve().parent
MASS_MEV = 10.0
RMAX_KM = 25.0
G_HIGH = 4.171689650228597e-8
SOURCE_BINS = ((0.0, 5.0), (5.0, 10.0), (10.0, 15.0),
               (15.0, 20.0), (20.0, 25.0))
DIRECTION_COSINES = (-0.9, -0.5, 0.0, 0.5, 0.9)
SOURCE_RADII = (0.0, 5.0, 10.0, 15.0, 17.0, 20.0, 22.0, 24.0)
ENERGY_TARGETS = (10.1, 20.0, 50.0, 100.0)
ANGLE_ORDERS = (16, 64, 128, 256)
THREE_LAYER_JSON = HERE / "outputs" / "fig7_10mev_three_layer.json"


def sqrt_radius_primitive(impact_km: float, z_km: float) -> float:
    """Primitive F'(z)=sqrt(b^2+z^2), with a stable b=0 limit."""
    if impact_km <= 1.0e-14:
        return 0.5 * z_km * abs(z_km)
    radius = np.hypot(impact_km, z_km)
    return 0.5 * (
        z_km * radius
        + impact_km**2 * np.arcsinh(z_km / impact_km)
    )


def ray_breakpoints(source_radius_km: float, cosine: float,
                    radial_grid: np.ndarray, radius_km: float,
                    extra_edges=()) -> tuple[float, ...]:
    """Return all z locations where a straight ray crosses a radial cell edge.

    The ray is parameterized by impact parameter b and longitudinal coordinate
    z. At production, z0=r*cos(theta); at the outer sphere, z1=sqrt(R^2-b^2).
    This representation includes inward-going rays through the center.
    """
    r = float(source_radius_km)
    mu = float(np.clip(cosine, -1.0, 1.0))
    b = r * np.sqrt(max(0.0, 1.0 - mu * mu))
    z0 = r * mu
    z1 = np.sqrt(max(radius_km * radius_km - b * b, 0.0))
    if z1 <= z0:
        return (z0, z1)

    cuts = [z0, z1]
    knots = np.unique(np.r_[np.asarray(radial_grid, float),
                            np.asarray(tuple(extra_edges), float)])
    for rk in knots:
        if rk < b - 1.0e-12:
            continue
        zabs = np.sqrt(max(rk * rk - b * b, 0.0))
        for zcross in (-zabs, zabs):
            if z0 + 1.0e-12 < zcross < z1 - 1.0e-12:
                cuts.append(float(zcross))
    return tuple(sorted(set(cuts)))


def exact_piecewise_linear_ray_column(
    source_radius_km: float,
    cosine: float,
    radial_grid: np.ndarray,
    reduced_absorption: np.ndarray,
    mass_mev: float,
    energies_mev: np.ndarray,
    radius_km: float = RMAX_KM,
    absorber_range: tuple[float, float] | None = None,
) -> np.ndarray:
    """Evaluate integral ds Gamma_abs^*(r(s),omega)/v exactly for np.interp.

    reduced_absorption has shape (n_radius,n_energy), is the unit-g^2 local
    reduced absorption rate in MeV, and is linearly interpolated in radius.
    The returned column is the unit-coupling optical depth. Restricting
    absorber_range integrates only that radial shell; shell edges are inserted
    as exact geometric breakpoints, not smeared across a grid cell.
    """
    grid = np.asarray(radial_grid, float)
    opacity = np.asarray(reduced_absorption, float)
    energies = np.asarray(energies_mev, float)
    if opacity.ndim != 2 or opacity.shape != (grid.size, energies.size):
        raise ValueError("Opacity must have shape (len(radial_grid), len(energies))")
    if np.any(np.diff(grid) <= 0.0):
        raise ValueError("radial_grid must be strictly increasing")
    if source_radius_km < 0.0 or source_radius_km > radius_km:
        raise ValueError("Source radius lies outside the transport sphere")
    if absorber_range is not None:
        lo, hi = map(float, absorber_range)
        if lo < 0.0 or hi <= lo or hi > radius_km:
            raise ValueError("Invalid absorber radial interval")
        extra_edges = (lo, hi)
    else:
        lo, hi = None, None
        extra_edges = ()

    r = float(source_radius_km)
    mu = float(np.clip(cosine, -1.0, 1.0))
    b = r * np.sqrt(max(0.0, 1.0 - mu * mu))
    cuts = ray_breakpoints(r, mu, grid, radius_km, extra_edges)
    if len(cuts) < 2 or cuts[-1] <= cuts[0]:
        return np.zeros(energies.size, dtype=float)

    integral = np.zeros(energies.size, dtype=float)
    for za, zb in zip(cuts[:-1], cuts[1:]):
        if zb <= za:
            continue
        zm = 0.5 * (za + zb)
        rm = np.hypot(b, zm)
        if absorber_range is not None and not (lo <= rm <= hi):
            continue

        cell = int(np.searchsorted(grid, rm, side="right") - 1)
        cell = min(max(cell, 0), grid.size - 2)
        dr = grid[cell + 1] - grid[cell]
        slope = (opacity[cell + 1] - opacity[cell]) / dr
        intercept = opacity[cell] - slope * grid[cell]
        dz = zb - za
        dprimitive = (
            sqrt_radius_primitive(b, zb)
            - sqrt_radius_primitive(b, za)
        )
        integral += intercept * dz + slope * dprimitive

    velocity = np.sqrt(np.maximum(1.0 - (mass_mev / energies)**2, 0.0))
    if np.any(velocity <= 0.0):
        raise ValueError("All transport energies must be strictly above the mass")
    return integral * KM_TO_MEV_INV / velocity


def exact_columns(source_radii: np.ndarray, angle_cosines: np.ndarray,
                  radial_grid: np.ndarray, reduced_absorption: np.ndarray,
                  mass_mev: float, energies_mev: np.ndarray,
                  radius_km: float = RMAX_KM,
                  absorber_range: tuple[float, float] | None = None) -> np.ndarray:
    """Build unit-coupling columns with independent ray geometry."""
    radii = np.asarray(source_radii, float)
    angles = np.asarray(angle_cosines, float)
    out = np.empty((radii.size, angles.size, len(energies_mev)), dtype=float)
    for ir, radius in enumerate(radii):
        for ia, cosine in enumerate(angles):
            out[ir, ia] = exact_piecewise_linear_ray_column(
                radius, cosine, radial_grid, reduced_absorption,
                mass_mev, energies_mev, radius_km, absorber_range,
            )
    return out


def escape_average(columns: np.ndarray, angle_weights: np.ndarray,
                   coupling: float) -> np.ndarray:
    """1/2 integral dcos(theta) exp(-g^2 tau), for normalized weights."""
    return np.einsum(
        "rae,a->re", np.exp(-coupling * coupling * columns),
        np.asarray(angle_weights, float), optimize=True,
    )


def adaptive_escape_probability(source_radius_km: float, energy_index: int,
                                 radial_grid: np.ndarray,
                                 reduced_absorption: np.ndarray,
                                 mass_mev: float, energies_mev: np.ndarray,
                                 coupling: float, radius_km: float = RMAX_KM
                                 ) -> float:
    """Independent adaptive angular integral using the analytic ray column."""
    def integrand(cosine):
        column = exact_piecewise_linear_ray_column(
            source_radius_km, cosine, radial_grid, reduced_absorption,
            mass_mev, energies_mev, radius_km,
        )[energy_index]
        return np.exp(-coupling * coupling * column)

    value = quad(
        integrand, -1.0, 1.0, points=[0.0],
        epsabs=2.0e-12, epsrel=2.0e-9, limit=200,
    )[0]
    return 0.5 * value


def build_frozen_state(profile_path: Path, radial_order: int = 40,
                       energy_order: int = 100,
                       energy_offset_mev: float = 1000.0) -> dict:
    """Rebuild the exact profile/rate/source inputs used by reference.py."""
    source_radii, radial_weights = radial_rule(RMAX_KM, radial_order)
    radial_grid = np.unique(np.r_[0.0, source_radii, RMAX_KM])
    profile = load_profile(profile_path, radial_grid)

    energies = MASS_MEV + np.geomspace(
        max(MASS_MEV * 1.0e-6, 1.0e-6), energy_offset_mev, energy_order
    )
    energies = np.unique(np.r_[energies, MASS_MEV / profile["lapse"]])
    energies = energies[energies > MASS_MEV * (1.0 + 1.0e-10)]
    energies.sort()

    rates = local_rates(
        MASS_MEV, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None],
    )
    x = energies[None, :] / profile["T"][:, None]
    bose_inverse_factor = np.expm1(x)
    nu_mu_production = (
        MASS_MEV**2 / (8.0 * np.pi * energies[None, :])
        * fermi_pair_average(
            profile["mu_numu"][:, None], energies[None, :],
            profile["T"][:, None],
            np.sqrt(1.0 - (MASS_MEV / energies[None, :])**2),
        )
    )
    nu_tau_production = (
        MASS_MEV**2 / (8.0 * np.pi * energies[None, :])
        * fermi_pair_average(
            np.zeros_like(profile["mu_numu"][:, None]),
            energies[None, :], profile["T"][:, None],
            np.sqrt(1.0 - (MASS_MEV / energies[None, :])**2),
        )
    )
    nu_mu_reduced = nu_mu_production * bose_inverse_factor
    nu_tau_reduced = nu_tau_production * bose_inverse_factor
    nu_reduced = nu_mu_reduced + nu_tau_reduced
    total_reduced = rates["reduced_absorption"]

    rate_split_residual = float(np.max(
        np.abs(nu_reduced - rates["neutrino_production"] * bose_inverse_factor)
        / np.maximum(np.abs(nu_reduced), 1.0e-300)
    ))
    if rate_split_residual > 2.0e-11:
        raise AssertionError(f"Flavor split does not reproduce local neutrino rate: {rate_split_residual}")

    lower = MASS_MEV / profile["lapse"]
    eweights = energy_weights(energies, lower)
    momentum = np.sqrt(np.maximum(energies**2 - MASS_MEV**2, 0.0))
    geometry = (
        4.0 * np.pi * (source_radii * KM_TO_MEV_INV)**2
        * radial_weights * KM_TO_MEV_INV * profile["lapse"]**2
    )
    phase_space = momentum * energies**2 / (2.0 * np.pi**2)
    source = (
        geometry[:, None] * eweights * phase_space[None, :]
        * rates["production"] * MEV2_TO_ERG_S
    )

    return {
        "source_radii": source_radii,
        "radial_weights": radial_weights,
        "radial_grid": radial_grid,
        "profile": profile,
        "energies": energies,
        "rates": rates,
        "nu_mu_reduced": nu_mu_reduced,
        "nu_tau_reduced": nu_tau_reduced,
        "nu_reduced": nu_reduced,
        "total_reduced": total_reduced,
        "source": source,
        "rate_split_max_relative_residual": rate_split_residual,
    }


def load_fig7_points(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    points = payload.get("all_25_curve_points")
    if not points or len(points) != 25:
        raise ValueError("Expected the archived 25-point 10 MeV Fig. 7 comparison")
    return points


def luminosity_for_columns(source: np.ndarray, columns: np.ndarray,
                           angle_weights: np.ndarray,
                           couplings: np.ndarray) -> np.ndarray:
    result = []
    for coupling in couplings:
        escape = escape_average(columns, angle_weights, float(coupling))
        result.append(float(coupling**2 * np.sum(source * escape)))
    return np.asarray(result, float)


def curve_metrics(calculated: np.ndarray, reference: np.ndarray) -> dict:
    residual = calculated / reference - 1.0
    return {
        "mean_absolute_relative_residual": float(np.mean(np.abs(residual))),
        "maximum_absolute_relative_residual": float(np.max(np.abs(residual))),
        "weak_coupling_relative_residual": float(residual[0]),
        "peak_relative_residual": float(residual[int(np.argmax(reference))]),
        "high_coupling_relative_residual": float(residual[-1]),
    }


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.sum(values * weights) / max(float(np.sum(weights)), 1.0e-300))


def run_audit(profile_path: Path, output_path: Path) -> dict:
    state = build_frozen_state(profile_path)
    r = state["source_radii"]
    grid = state["radial_grid"]
    energies = state["energies"]
    source = state["source"]
    rates = state["rates"]
    nu_mu = state["nu_mu_reduced"]
    nu_tau = state["nu_tau_reduced"]
    nu_total = state["nu_reduced"]
    total = state["total_reduced"]

    fig7_points = load_fig7_points(THREE_LAYER_JSON)
    couplings = np.asarray([p["g"] for p in fig7_points], float)
    fig7_reference = np.asarray(
        [p["reference_luminosity_erg_s"] for p in fig7_points], float
    )
    archived_reference_path = np.asarray(
        [p["calculated_luminosity_erg_s"] for p in fig7_points], float
    )

    # Existing implementation: 16-point angle and 32-point path quadrature.
    reference_columns, reference_angle_weights = scalar_optical_depths(
        r, grid, total, MASS_MEV, energies, RMAX_KM,
        angular_order=16, path_order=32,
    )
    reference_angle_nodes, reference_angle_weights_check = leggauss(16)
    reference_angle_weights_check = reference_angle_weights_check / 2.0
    if not np.allclose(reference_angle_weights, reference_angle_weights_check,
                       rtol=0.0, atol=2.0e-15):
        raise AssertionError("Reference angular weights are inconsistent")

    # Independent exact path columns at the same 16 directions isolate the
    # path quadrature from the angular quadrature.
    exact_16_columns = exact_columns(
        r, reference_angle_nodes, grid, total, MASS_MEV, energies, RMAX_KM
    )
    path_difference = exact_16_columns - reference_columns
    path_scale = np.maximum(np.abs(reference_columns), 1.0e-300)
    path_mask = np.abs(reference_columns) > (
        1.0e-10 * float(np.max(np.abs(reference_columns)))
    )
    path_relative = np.abs(path_difference[path_mask] / path_scale[path_mask])
    path_comparison = {
        "max_absolute_column_difference_unit_g2": float(np.max(np.abs(path_difference))),
        "max_relative_column_difference_above_1e-10_of_global_peak": float(
            np.max(path_relative) if path_relative.size else 0.0
        ),
        "rms_relative_column_difference_above_1e-10_of_global_peak": float(
            np.sqrt(np.mean(path_relative**2)) if path_relative.size else 0.0
        ),
    }

    exact_16_luminosity = luminosity_for_columns(
        source, exact_16_columns, reference_angle_weights, couplings
    )
    reference_path_luminosity = luminosity_for_columns(
        source, reference_columns, reference_angle_weights, couplings
    )
    baseline_archive_residual = (
        reference_path_luminosity / archived_reference_path - 1.0
    )

    angle_results = {}
    high_order_columns = None
    high_order_weights = None
    for order in ANGLE_ORDERS:
        mu_nodes, mu_weights = leggauss(order)
        mu_weights = mu_weights / 2.0
        if order == 16:
            columns = exact_16_columns
        else:
            columns = exact_columns(
                r, mu_nodes, grid, total, MASS_MEV, energies, RMAX_KM
            )
        lum = luminosity_for_columns(source, columns, mu_weights, couplings)
        angle_results[str(order)] = {
            "luminosity_erg_s": lum.tolist(),
            "fig7_residual_metrics": curve_metrics(lum, fig7_reference),
        }
        if order == max(ANGLE_ORDERS):
            high_order_columns = columns
            high_order_weights = mu_weights

    if high_order_columns is None or high_order_weights is None:
        raise AssertionError("Highest-order angular columns were not generated")

    # Independent adaptive angular quadrature at representative source radii
    # and energies, compared with the highest-order Gauss-Legendre result.
    adaptive_checks = []
    for radius in (5.0, 15.0, 20.0, 24.0):
        for target_energy in (10.1, 20.0, 50.0):
            ie = int(np.argmin(np.abs(energies - target_energy)))
            adaptive = adaptive_escape_probability(
                radius, ie, grid, total, MASS_MEV, energies, G_HIGH, RMAX_KM
            )
            mu_nodes, mu_weights = leggauss(max(ANGLE_ORDERS))
            mu_weights = mu_weights / 2.0
            cols = exact_columns(
                np.asarray([radius]), mu_nodes, grid, total,
                MASS_MEV, energies, RMAX_KM,
            )[0]
            gauss = float(np.dot(
                mu_weights, np.exp(-G_HIGH**2 * cols[:, ie])
            ))
            adaptive_checks.append({
                "source_radius_km": radius,
                "energy_MeV": float(energies[ie]),
                "adaptive_escape_probability": adaptive,
                "gauss_legendre_escape_probability": gauss,
                "relative_difference": gauss / adaptive - 1.0,
            })

    # Resolve the neutrino opacity by flavor and absorber shell using the
    # independent path integral. Exact shell boundaries are included.
    mu_nodes, mu_weights = leggauss(max(ANGLE_ORDERS))
    mu_weights = mu_weights / 2.0
    nu_mu_columns = exact_columns(
        r, mu_nodes, grid, nu_mu, MASS_MEV, energies, RMAX_KM
    )
    nu_tau_columns = exact_columns(
        r, mu_nodes, grid, nu_tau, MASS_MEV, energies, RMAX_KM
    )
    nu_total_columns = exact_columns(
        r, mu_nodes, grid, nu_total, MASS_MEV, energies, RMAX_KM
    )
    nu_15_20_columns = exact_columns(
        r, mu_nodes, grid, nu_total, MASS_MEV, energies, RMAX_KM,
        absorber_range=(15.0, 20.0),
    )
    nu_20_25_columns = exact_columns(
        r, mu_nodes, grid, nu_total, MASS_MEV, energies, RMAX_KM,
        absorber_range=(20.0, 25.0),
    )
    nu_outer_columns = nu_15_20_columns + nu_20_25_columns
    shell_additivity = float(np.max(
        np.abs(nu_outer_columns - exact_columns(
            r, mu_nodes, grid, nu_total, MASS_MEV, energies, RMAX_KM,
            absorber_range=(15.0, 25.0),
        ))
        / np.maximum(np.abs(nu_outer_columns), 1.0e-300)
    ))
    flavor_sum_residual = float(np.max(
        np.abs(nu_mu_columns + nu_tau_columns - nu_total_columns)
        / np.maximum(np.abs(nu_total_columns), 1.0e-300)
    ))

    weights = source[:, None, :] * mu_weights[None, :, None]
    high_g2 = G_HIGH**2
    shell_means = {
        "nu_mu_total": weighted_mean(high_g2 * nu_mu_columns, weights),
        "nu_tau_total": weighted_mean(high_g2 * nu_tau_columns, weights),
        "nu_total_total": weighted_mean(high_g2 * nu_total_columns, weights),
        "nu_mu_15_25": weighted_mean(high_g2 * (
            exact_columns(r, mu_nodes, grid, nu_mu, MASS_MEV, energies,
                          RMAX_KM, absorber_range=(15.0, 25.0))
        ), weights),
        "nu_tau_15_25": weighted_mean(high_g2 * (
            exact_columns(r, mu_nodes, grid, nu_tau, MASS_MEV, energies,
                          RMAX_KM, absorber_range=(15.0, 25.0))
        ), weights),
        "nu_total_15_20": weighted_mean(high_g2 * nu_15_20_columns, weights),
        "nu_total_20_25": weighted_mean(high_g2 * nu_20_25_columns, weights),
        "nu_total_15_25": weighted_mean(high_g2 * nu_outer_columns, weights),
    }
    shell_means["nu_total_15_25_fraction_of_nu_total"] = (
        shell_means["nu_total_15_25"] / shell_means["nu_total_total"]
    )

    by_production_bin = []
    for lo, hi in SOURCE_BINS:
        mask = ((r >= lo) & ((r < hi) if hi < RMAX_KM else (r <= hi)))
        w_bin = weights[mask]
        row = {"production_shell_km": [lo, hi], "source_weight_sum": float(np.sum(w_bin))}
        for label, columns in (
            ("nu_mu_total", nu_mu_columns),
            ("nu_tau_total", nu_tau_columns),
            ("nu_total_total", nu_total_columns),
            ("nu_total_15_25", nu_outer_columns),
        ):
            row[label] = weighted_mean(high_g2 * columns[mask], w_bin)
        row["nu_total_15_25_fraction_of_nu_total"] = (
            row["nu_total_15_25"] / row["nu_total_total"]
            if row["nu_total_total"] > 0.0 else None
        )
        by_production_bin.append(row)

    # Escape luminosity by production shell, using the independent high-order
    # angular average and the full (neutrino + Compton) reduced opacity.
    escape_high = np.exp(-high_g2 * high_order_columns)
    escaped_source = high_g2 * source[:, None, :] * escape_high
    escaped_by_production_bin = []
    for lo, hi in SOURCE_BINS:
        mask = ((r >= lo) & ((r < hi) if hi < RMAX_KM else (r <= hi)))
        value = float(np.sum(escaped_source[mask] * high_order_weights[None, :, None]))
        escaped_by_production_bin.append({
            "production_shell_km": [lo, hi],
            "escaped_luminosity_erg_s": value,
        })

    # Direction-resolved probabilities at the high-absorption benchmark.
    direction_table = []
    for radius in SOURCE_RADII:
        for cosine in DIRECTION_COSINES:
            total_col = exact_piecewise_linear_ray_column(
                radius, cosine, grid, total, MASS_MEV, energies, RMAX_KM
            )
            nu_col = exact_piecewise_linear_ray_column(
                radius, cosine, grid, nu_total, MASS_MEV, energies, RMAX_KM
            )
            outer_col = exact_piecewise_linear_ray_column(
                radius, cosine, grid, nu_total, MASS_MEV, energies, RMAX_KM,
                absorber_range=(15.0, 25.0),
            )
            for target_energy in ENERGY_TARGETS:
                ie = int(np.argmin(np.abs(energies - target_energy)))
                tau_total = high_g2 * total_col[ie]
                tau_nu = high_g2 * nu_col[ie]
                tau_outer = high_g2 * outer_col[ie]
                direction_table.append({
                    "source_radius_km": radius,
                    "cos_theta": cosine,
                    "energy_MeV": float(energies[ie]),
                    "tau_total": float(tau_total),
                    "tau_neutrino": float(tau_nu),
                    "tau_neutrino_outer_15_25": float(tau_outer),
                    "escape_probability_total": float(np.exp(-tau_total)),
                    "escape_probability_neutrino_only": float(np.exp(-tau_nu)),
                    "outer_fraction_of_neutrino_tau": (
                        float(tau_outer / tau_nu) if tau_nu > 0.0 else None
                    ),
                })

    order_luminosities = {
        order: np.asarray(angle_results[str(order)]["luminosity_erg_s"], float)
        for order in ANGLE_ORDERS
    }
    convergence = {}
    for low, high in zip(ANGLE_ORDERS[:-1], ANGLE_ORDERS[1:]):
        delta = order_luminosities[high] / order_luminosities[low] - 1.0
        convergence[f"{low}_to_{high}"] = {
            "max_absolute_relative_luminosity_change": float(np.max(np.abs(delta))),
            "high_coupling_relative_change": float(delta[-1]),
        }

    result = {
        "title": "Independent Blinov Eq. (B.2) path and angular integration audit",
        "status": "independent_transport_integral_complete_local_rates_frozen",
        "source": "Blinov et al., arXiv:2511.09619v2, Appendix B, Eqs. (B.1)-(B.5)",
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "profile_sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
        "fig7_three_layer_input_sha256": hashlib.sha256(
            THREE_LAYER_JSON.read_bytes()
        ).hexdigest(),
        "frozen_inputs": {
            "mass_MeV": MASS_MEV,
            "radius_km": RMAX_KM,
            "mu_numu": "Caputo digitized profile, unchanged",
            "mu_nutau": "zero baseline, unchanged",
            "mu_mu": "Caputo digitized profile, unchanged",
            "energy_along_path": "fixed omega as written in Eq. (B.2)",
            "local_reduced_absorption": "reference.local_rates output, unchanged",
            "coupling_scaling": "unit-g^2 opacity multiplied by g^2 only in exp(-g^2 tau)",
            "radial_order": 40,
            "energy_order": 100,
            "energy_offset_MeV": 1000.0,
        },
        "quadrature": {
            "reference_path": {"angular_order": 16, "path_order": 32},
            "independent_path": "analytic integration of the piecewise-linear radial opacity in impact-parameter coordinates",
            "independent_angle_orders": list(ANGLE_ORDERS),
            "highest_order": max(ANGLE_ORDERS),
        },
        "local_rate_freeze_check": {
            "flavor_split_max_relative_residual": state["rate_split_max_relative_residual"],
            "note": "The same frozen local rates are used in both path implementations; no local rate is recalibrated.",
        },
        "reference_path_vs_independent_path": {
            "path_column_comparison_at_identical_16_angles": path_comparison,
            "luminosity_reproduction_of_archived_three_layer_baseline": {
                "max_absolute_relative_difference": float(np.max(np.abs(baseline_archive_residual))),
                "mean_absolute_relative_difference": float(np.mean(np.abs(baseline_archive_residual))),
            },
            "luminosity_at_same_16_angles": {
                "reference_path_quadrature": reference_path_luminosity.tolist(),
                "independent_analytic_path": exact_16_luminosity.tolist(),
                "max_absolute_relative_difference": float(np.max(np.abs(
                    exact_16_luminosity / reference_path_luminosity - 1.0
                ))),
            },
        },
        "fig7_full_curve": {
            "couplings": couplings.tolist(),
            "reference_luminosity_erg_s": fig7_reference.tolist(),
            "reference_path_16x32_luminosity_erg_s": reference_path_luminosity.tolist(),
            "independent_angle_order_results": angle_results,
            "angle_convergence": convergence,
        },
        "outer_neutrino_path_decomposition": {
            "source_weighted_mean_optical_depth_at_high_coupling": shell_means,
            "by_production_radius_shell": by_production_bin,
            "shell_additivity_max_relative_residual": shell_additivity,
            "flavor_sum_max_relative_residual": flavor_sum_residual,
            "escaped_luminosity_by_production_radius_shell": escaped_by_production_bin,
        },
        "adaptive_angle_cross_checks": adaptive_checks,
        "direction_resolved_escape_probabilities": direction_table,
        "interpretation": [
            "The path integral is evaluated in an independent impact-parameter/longitudinal-coordinate representation; inward rays pass through the closest-approach point and exit the opposite side of the sphere.",
            "For the same piecewise-linear radial opacity interpolant, the path integral is analytic on each radial cell. This isolates path quadrature from local-rate interpolation.",
            "The full Eq. (B.2) angular average is recomputed at 16, 64, 128 and 256 Gauss-Legendre nodes; selected points are also checked with adaptive angular quadrature.",
            "The full escape probability uses the unchanged total reduced opacity. Neutrino-only and 15-25 km shell optical depths are reported separately to identify the outer contribution.",
            "The energy omega is held fixed along each ray, following the literal argument shown in Eq. (B.2); gravitational redshift in the production luminosity remains as in Eq. (B.1).",
            "This audit does not change the muon or neutrino chemical potentials, local collision rates, opacity normalization, production source, or coupling axis.",
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n",
                            encoding="utf-8")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument(
        "--output", type=Path,
        default=HERE / "outputs" / "eq_b2_independent_path_integral_2026-11-08.json",
    )
    args = parser.parse_args()
    result = run_audit(args.profile, args.output)
    print(json.dumps({
        "status": result["status"],
        "path_comparison": result["reference_path_vs_independent_path"],
        "angle_convergence": result["fig7_full_curve"]["angle_convergence"],
        "outer_neutrino": result["outer_neutrino_path_decomposition"][
            "source_weighted_mean_optical_depth_at_high_coupling"
        ],
        "adaptive_angle_max_relative_difference": max(
            abs(row["relative_difference"])
            for row in result["adaptive_angle_cross_checks"]
        ),
        "fig7_residuals": {
            order: values["fig7_residual_metrics"]
            for order, values in result["fig7_full_curve"][
                "independent_angle_order_results"
            ].items()
        },
    }, indent=2))


if __name__ == "__main__":
    main()
