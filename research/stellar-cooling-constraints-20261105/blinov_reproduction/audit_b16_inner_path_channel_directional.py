"""Direction- and channel-resolved B.2 opacity audit with exact radial path integration.

The path integral is evaluated analytically on each piecewise-linear radial
opacity segment. Inward rays traverse b<r<r_em twice and r>r_em once.
This independently checks the global-s quadrature used by the legacy shell
audit. The B.1 source and published fixed-omega B.2 convention are unchanged.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from scipy.special import logsumexp

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, scalar_optical_depths,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_neutrino_flavour_opacity import flavour_rate_arrays
    from .audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, scalar_optical_depths,
    )
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_neutrino_flavour_opacity import flavour_rate_arrays
    from audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_inner_path_channel_directional_10mev_2026-11-09.json"
SHELL_EDGES_KM = np.array([0.0, 5.0, 8.0, 10.0, 12.0, 15.0, 16.5, 18.5, 20.0, 22.0, 25.0])
CHANNELS = ("nu_mu", "nu_tau", "compton", "dimuon")
ANGLE_BINS = ((-1.0, -0.5), (-0.5, 0.0), (0.0, 0.5), (0.5, 1.0))


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _f1_primitive(radius, impact):
    """Primitive of r^2/sqrt(r^2-b^2) with its b-dependent constant removed."""
    radius = float(radius)
    y = np.sqrt(max(radius * radius - impact * impact, 0.0))
    if impact < 1.0e-12:
        return 0.5 * radius * radius
    return 0.5 * (radius * y + impact * impact * np.log((radius + y) / impact))


def analytic_ray_shell_columns(
    source_radius, cosine, radial_grid, reduced_by_channel,
    mass, energies, radius_km=25.0, shell_edges=SHELL_EDGES_KM,
):
    """Return [channel, path-shell, energy] tau/g^2 for one emission ray.

    Each local opacity is linearly interpolated in radius between radial_grid
    nodes. The integral of (a+b*r) ds is analytic because
    ds/dr = r/sqrt(r^2-b^2). For cosine<0, b<r<r_source is traversed twice.
    """
    radial_grid = np.asarray(radial_grid, float)
    energies = np.asarray(energies, float)
    shell_edges = np.asarray(shell_edges, float)
    names = tuple(reduced_by_channel)
    reduced = np.stack([np.asarray(reduced_by_channel[name], float) for name in names])
    if reduced.ndim != 3 or reduced.shape[1] != len(radial_grid):
        raise ValueError("reduced_by_channel arrays must have shape (n_radius,n_energy)")
    if reduced.shape[2] != len(energies):
        raise ValueError("energy dimension does not match energies")
    if np.any(np.diff(radial_grid) <= 0.0) or np.any(np.diff(shell_edges) <= 0.0):
        raise ValueError("radial and shell grids must be strictly increasing")
    if radial_grid[0] > 0.0 or radial_grid[-1] < radius_km:
        raise ValueError("radial_grid must cover the complete path")
    if shell_edges[0] > 0.0 or shell_edges[-1] < radius_km:
        raise ValueError("shell_edges must cover the complete path")
    if source_radius < 0.0 or source_radius > radius_km or abs(cosine) > 1.0:
        raise ValueError("invalid source radius or direction")

    n_channel = len(names)
    n_shell = len(shell_edges) - 1
    n_energy = len(energies)
    result = np.zeros((n_channel, n_shell, n_energy))
    if source_radius >= radius_km:
        return result

    impact = source_radius * np.sqrt(max(1.0 - cosine * cosine, 0.0))
    r_min = impact if cosine < 0.0 else source_radius
    if r_min >= radius_km:
        return result

    breaks = [r_min, radius_km]
    breaks.extend(radial_grid[(radial_grid > r_min) & (radial_grid < radius_km)])
    breaks.extend(shell_edges[(shell_edges > r_min) & (shell_edges < radius_km)])
    if cosine < 0.0 and r_min < source_radius < radius_km:
        breaks.append(source_radius)
    breaks = np.unique(np.asarray(breaks, float))

    velocity = np.sqrt(np.maximum(1.0 - (mass / energies) ** 2, 0.0))
    if np.any(velocity <= 0.0):
        raise ValueError("all energies must be above the mediator mass")

    for r_a, r_b in zip(breaks[:-1], breaks[1:]):
        if r_b <= r_a:
            continue
        r_mid = 0.5 * (r_a + r_b)
        ir = int(np.searchsorted(radial_grid, r_mid, side="right") - 1)
        ir = min(max(ir, 0), len(radial_grid) - 2)
        slope = (reduced[:, ir + 1, :] - reduced[:, ir, :]) / (
            radial_grid[ir + 1] - radial_grid[ir]
        )
        intercept = reduced[:, ir, :] - slope * radial_grid[ir]

        y_a = np.sqrt(max(r_a * r_a - impact * impact, 0.0))
        y_b = np.sqrt(max(r_b * r_b - impact * impact, 0.0))
        delta_y = y_b - y_a
        delta_f1 = _f1_primitive(r_b, impact) - _f1_primitive(r_a, impact)
        multiplicity = 2.0 if cosine < 0.0 and r_mid < source_radius else 1.0
        shell = int(np.searchsorted(shell_edges, r_mid, side="right") - 1)
        shell = min(max(shell, 0), n_shell - 1)

        integral = multiplicity * (
            intercept * delta_y + slope * delta_f1
        )
        scale = max(float(np.max(np.abs(integral))), 1.0)
        if float(np.min(integral)) < -2.0e-11 * scale:
            raise ArithmeticError("piecewise-linear positive opacity produced a negative path integral")
        result[:, shell, :] += np.maximum(integral, 0.0) * KM_TO_MEV_INV / velocity[None, :]
    return result


def segmented_radial_columns(
    source_radii, radial_grid, reduced_by_channel, mass, energies,
    radius_km=25.0, angular_order=32, shell_edges=SHELL_EDGES_KM,
):
    """Return [channel,shell,source,angle,energy] analytic B.2 columns."""
    angles, angle_weights = np.polynomial.legendre.leggauss(angular_order)
    angle_weights = angle_weights / 2.0
    names = tuple(reduced_by_channel)
    columns = np.zeros((
        len(names), len(shell_edges) - 1, len(source_radii),
        len(angles), len(energies)
    ))
    for ia, cosine in enumerate(angles):
        for ir, r0 in enumerate(source_radii):
            columns[:, :, ir, ia, :] = analytic_ray_shell_columns(
                r0, cosine, radial_grid, reduced_by_channel,
                mass, energies, radius_km, shell_edges
            )
    return columns, angles, angle_weights


def direction_binned_radial_columns(
    source_radii, radial_grid, reduced_by_channel, mass, energies,
    radius_km=25.0, per_bin_order=32, shell_edges=SHELL_EDGES_KM,
):
    """Integrate each equal-width direction bin with its own Gauss rule.

    This avoids masking global Gauss-Legendre nodes with discontinuous bin
    indicators. The returned weights already include the 1/2 angular-average
    factor, so all four bins together sum to unity.
    """
    nodes, weights = np.polynomial.legendre.leggauss(per_bin_order)
    angle_blocks = []
    weight_blocks = []
    bin_blocks = []
    for ib, (lo, hi) in enumerate(ANGLE_BINS):
        half = 0.5 * (hi - lo)
        midpoint = 0.5 * (hi + lo)
        angle_blocks.append(midpoint + half * nodes)
        weight_blocks.append(0.5 * half * weights)
        bin_blocks.append(np.full(per_bin_order, ib, dtype=int))
    angles = np.concatenate(angle_blocks)
    angle_weights = np.concatenate(weight_blocks)
    bin_ids = np.concatenate(bin_blocks)

    names = tuple(reduced_by_channel)
    columns = np.zeros((
        len(names), len(shell_edges) - 1, len(source_radii),
        len(angles), len(energies)
    ))
    for ia, cosine in enumerate(angles):
        for ir, r0 in enumerate(source_radii):
            columns[:, :, ir, ia, :] = analytic_ray_shell_columns(
                r0, cosine, radial_grid, reduced_by_channel,
                mass, energies, radius_km, shell_edges
            )
    return columns, angles, angle_weights, bin_ids


def reduced_absorption_channels(mass, energies, profile, rates):
    """Build B.4 reduced opacity separately for nu_mu, nu_tau, Compton, dimuon."""
    omega = np.asarray(energies, float)[None, :]
    temperature = np.asarray(profile["T"], float)[:, None]
    detailed_balance = np.expm1(np.minimum(omega / temperature, 700.0))
    nu_mu, nu_tau = flavour_rate_arrays(mass, energies, profile)
    production = {
        "nu_mu": nu_mu,
        "nu_tau": nu_tau,
        "compton": np.asarray(rates["compton_production"], float),
        "dimuon": np.asarray(rates["dimuon_production"], float),
    }
    reduced = {name: detailed_balance * value for name, value in production.items()}
    production_sum = sum(production.values())
    reduced_sum = sum(reduced.values())
    production_residual = float(np.max(
        np.abs(production_sum - rates["production"])
        / np.maximum(np.abs(rates["production"]), 1.0e-300)
    ))
    reduced_residual = float(np.max(
        np.abs(reduced_sum - rates["reduced_absorption"])
        / np.maximum(np.abs(rates["reduced_absorption"]), 1.0e-300)
    ))
    return production, reduced, {
        "production_channel_sum_max_relative_residual": production_residual,
        "reduced_absorption_channel_sum_max_relative_residual": reduced_residual,
    }


def _weighted_mean(values, weights):
    denominator = float(np.sum(weights))
    return float(np.sum(values * weights) / denominator) if denominator > 0.0 else None


def _log_escaped_integral(source, angle_weights, total_columns, coupling, source_mask):
    selected = np.asarray(source[source_mask], float)
    log_source = np.where(selected > 0.0, np.log(selected), -np.inf)[:, None, :]
    return float(logsumexp(
        log_source + np.log(angle_weights)[None, :, None]
        - coupling * coupling * total_columns[source_mask]
    ))


def _channel_shell_rows(columns, channel_names, shell_labels, source_weights, escaped_weights):
    rows = []
    for ic, channel in enumerate(channel_names):
        for ish, shell in enumerate(shell_labels):
            tau = columns[ic, ish]
            mean_source = _weighted_mean(tau, source_weights)
            mean_escaped = _weighted_mean(tau, escaped_weights)
            rows.append({
                "channel": channel,
                "path_shell": shell,
                "mean_tau_source_weighted_per_g2": mean_source,
                "mean_tau_escaped_population_weighted_per_g2": mean_escaped,
            })
    return rows


def _region_summary(
    label, source_mask, source, columns, total_columns, channel_names,
    shell_labels, shell_edges, radii, angles, angle_weights, coupling,
    direction_data,
):
    source_region = source[source_mask]
    base_weights = source_region[:, None, :] * angle_weights[None, :, None]
    base_norm = float(np.sum(base_weights))
    survival = np.exp(-coupling * coupling * total_columns[source_mask])
    escaped_weights = base_weights * survival
    escaped_norm = float(np.sum(escaped_weights))
    mean_escape = escaped_norm / base_norm if base_norm > 0.0 else None

    direction_columns, direction_angles, direction_weights, direction_bin_ids = direction_data
    direction_total_columns = np.sum(direction_columns, axis=(0, 1))
    direction_base_weights = source_region[:, None, :] * direction_weights[None, :, None]
    direction_survival = np.exp(
        -coupling * coupling * direction_total_columns[source_mask]
    )
    direction_escaped_weights = direction_base_weights * direction_survival
    direction_base_norm = float(np.sum(direction_base_weights))
    direction_escaped_norm = float(np.sum(direction_escaped_weights))

    channel_shell = _channel_shell_rows(
        columns[:, :, source_mask, :, :], channel_names, shell_labels,
        base_weights, escaped_weights
    )
    direction_rows = []
    for ib, (lo, hi) in enumerate(ANGLE_BINS):
        angle_mask = direction_bin_ids == ib
        w0 = direction_base_weights[:, angle_mask, :]
        we = direction_escaped_weights[:, angle_mask, :]
        tau_total = direction_total_columns[source_mask][:, angle_mask, :]
        selected_direction_columns = direction_columns[:, :, source_mask, :, :][:, :, :, angle_mask, :]
        channel_shell_rows = _channel_shell_rows(
            selected_direction_columns, channel_names, shell_labels, w0, we
        )
        direction_rows.append({
            "cos_theta_bin": [lo, hi],
            "thin_source_fraction": (
                float(np.sum(w0) / direction_base_norm) if direction_base_norm else 0.0
            ),
            "escaped_luminosity_fraction": (
                float(np.sum(we) / direction_escaped_norm) if direction_escaped_norm else 0.0
            ),
            "mean_escape_probability": (
                float(np.sum(we) / np.sum(w0)) if np.sum(w0) else None
            ),
            "mean_total_tau_source_weighted_per_g2": _weighted_mean(tau_total, w0),
            "mean_total_tau_escaped_population_weighted_per_g2": _weighted_mean(tau_total, we),
            "channel_shell_tau": channel_shell_rows,
        })

    grouped_shells = {
        "core_0_8km": (0.0, 8.0),
        "target_inner_8_22km": (8.0, 22.0),
        "outer_reference_22_25km": (22.0, 25.0),
    }
    group_rows = []
    for group_name, (lo, hi) in grouped_shells.items():
        selected_shells = [
            i for i, (a, b) in enumerate(zip(shell_edges[:-1], shell_edges[1:]))
            if a >= lo - 1.0e-12 and b <= hi + 1.0e-12
        ]
        for ic, channel in enumerate(channel_names):
            tau = np.sum(columns[ic, selected_shells, :, :, :], axis=0)[source_mask, :, :]
            group_rows.append({
                "path_group": group_name,
                "channel": channel,
                "mean_tau_source_weighted_per_g2": _weighted_mean(tau, base_weights),
                "mean_tau_escaped_population_weighted_per_g2": _weighted_mean(tau, escaped_weights),
            })

    emission_rows = []
    for lo, hi in zip(shell_edges[:-1], shell_edges[1:]):
        emission_mask = source_mask & (radii >= lo) & (
            (radii < hi) if hi < shell_edges[-1] else (radii <= hi)
        )
        if not np.any(emission_mask):
            continue
        w0 = source[emission_mask, None, :] * angle_weights[None, :, None]
        we = w0 * np.exp(-coupling * coupling * total_columns[emission_mask])
        thin = float(np.sum(w0))
        escaped = float(np.sum(we))
        emission_rows.append({
            "emission_shell": f"{lo:g}-{hi:g}km",
            "thin_source_fraction": thin / base_norm if base_norm else 0.0,
            "escaped_luminosity_fraction": escaped / escaped_norm if escaped_norm else 0.0,
            "mean_escape_probability": escaped / thin if thin else None,
        })

    base_log = _log_escaped_integral(source, angle_weights, total_columns, coupling, source_mask)
    leave_one_out = []
    for ic, channel in enumerate(channel_names):
        for ish, shell in enumerate(shell_labels):
            removed = columns[ic, ish]
            alternative = np.maximum(total_columns - removed, 0.0)
            alt_log = _log_escaped_integral(
                source, angle_weights, alternative, coupling, source_mask
            )
            delta = alt_log - base_log
            leave_one_out.append({
                "channel": channel,
                "path_shell": shell,
                "log10_luminosity_enhancement": float(delta / np.log(10.0)),
                "relative_luminosity_enhancement": (
                    float(np.expm1(delta)) if delta < 700.0 else None
                ),
            })

    combined_sensitivity = []

    def append_combined_sensitivity(name, removed, removed_channels, removed_shells, kind):
        alternative = np.maximum(total_columns - removed, 0.0)
        alt_log = _log_escaped_integral(
            source, angle_weights, alternative, coupling, source_mask
        )
        delta = alt_log - base_log
        combined_sensitivity.append({
            "name": name,
            "kind": kind,
            "removed_channels": list(removed_channels),
            "removed_path_shells": list(removed_shells),
            "log10_luminosity_enhancement": float(delta / np.log(10.0)),
            "relative_luminosity_enhancement": (
                float(np.expm1(delta)) if delta < 700.0 else None
            ),
        })

    shell_index = {name: i for i, name in enumerate(shell_labels)}
    channel_index = {name: i for i, name in enumerate(channel_names)}

    # Remove all channels in one path shell at a time.
    for ish, shell in enumerate(shell_labels):
        append_combined_sensitivity(
            f"all_channels_in_{shell}",
            np.sum(columns[:, ish], axis=0),
            channel_names, [shell], "all_channels_in_one_shell"
        )

    # Remove one complete channel across the full path.
    for ic, channel in enumerate(channel_names):
        append_combined_sensitivity(
            f"{channel}_all_path_shells",
            np.sum(columns[ic], axis=0),
            [channel], shell_labels, "one_channel_across_all_shells"
        )

    # Nonlinear combined removals that distinguish the inner and outer paths.
    group_shells = {
        "inner_8_22km": [
            "8-10km", "10-12km", "12-15km", "15-16.5km",
            "16.5-18.5km", "18.5-20km", "20-22km"
        ],
        "outer_22_25km": ["22-25km"],
        "full_8_25km": [
            "8-10km", "10-12km", "12-15km", "15-16.5km",
            "16.5-18.5km", "18.5-20km", "20-22km", "22-25km"
        ],
    }
    neutrino_channels = [
        channel_index[name] for name in ("nu_mu", "nu_tau")
        if name in channel_index
    ]
    compton_channels = [channel_index["compton"]] if "compton" in channel_index else []

    for group_name, group_labels in group_shells.items():
        indices = [shell_index[name] for name in group_labels if name in shell_index]
        if not indices:
            continue
        append_combined_sensitivity(
            f"all_channels_{group_name}",
            np.sum(columns[:, indices], axis=(0, 1)),
            channel_names, group_labels, "all_channels_in_radial_group"
        )
        if neutrino_channels:
            append_combined_sensitivity(
                f"neutrino_channels_{group_name}",
                np.sum(columns[neutrino_channels][:, indices], axis=(0, 1)),
                [channel_names[i] for i in neutrino_channels],
                group_labels, "neutrino_channels_in_radial_group"
            )
        if compton_channels:
            append_combined_sensitivity(
                f"compton_{group_name}",
                np.sum(columns[compton_channels][:, indices], axis=(0, 1)),
                [channel_names[i] for i in compton_channels],
                group_labels, "compton_in_radial_group"
            )

    return {
        "region": label,
        "source_fraction_of_total_B1": (
            float(np.sum(source_region) / np.sum(source)) if np.sum(source) else 0.0
        ),
        "source_weighted_escape_probability": mean_escape,
        "direction_bin_quadrature_escape_probability": (
            direction_escaped_norm / direction_base_norm if direction_base_norm else None
        ),
        "direction_bins": direction_rows,
        "channel_shell_tau": channel_shell,
        "path_group_tau": group_rows,
        "emission_shells": emission_rows,
        "leave_one_channel_shell_out": leave_one_out,
        "combined_leave_one_out": combined_sensitivity,
    }


def _local_rate_samples(mass, profile, radial_grid, radii=(8, 10, 12, 15, 18.5, 20, 22), energies=(15, 20, 30)):
    rows = []
    energies = np.asarray(energies, float)
    for radius in radii:
        sample = {
            key: np.array([np.interp(radius, radial_grid, profile[key])])
            for key in ("T", "mu_mu", "mu_numu")
        }
        local = local_rates(
            mass, energies[None, :], sample["T"][:, None],
            sample["mu_numu"][:, None], sample["mu_mu"][:, None]
        )
        production, reduced, _ = reduced_absorption_channels(mass, energies, sample, local)
        for ie, omega in enumerate(energies):
            rows.append({
                "radius_km": float(radius),
                "omega_local_MeV": float(omega),
                "T_MeV": float(sample["T"][0]),
                "mu_mu_MeV": float(sample["mu_mu"][0]),
                "mu_numu_MeV": float(sample["mu_numu"][0]),
                "reduced_absorption_per_g2_MeV": {
                    name: float(reduced[name][0, ie]) for name in CHANNELS
                },
                "production_per_g2_MeV": {
                    name: float(production[name][0, ie]) for name in CHANNELS
                },
            })
    return rows


def _legacy_shell_comparison(
    source, source_mask, columns, channel_names, radial_grid, radii,
    profile, rates, mass, energies, radius_km, angular_order, base_path_order,
):
    """Convergence audit of the legacy global-s shell mask against analytic columns."""
    path_orders = sorted(set((
        max(8, base_path_order // 2),
        base_path_order,
        base_path_order * 2,
        base_path_order * 4,
        base_path_order * 8,
    )))
    analytic_map = {
        "neutrino": columns[channel_names.index("nu_mu")] + columns[channel_names.index("nu_tau")],
        "compton": columns[channel_names.index("compton")],
        "dimuon": columns[channel_names.index("dimuon")],
    }
    rows_by_order = []
    for path_order in path_orders:
        legacy = shell_columns_by_channel(
            radii, radial_grid, profile["T"], rates, mass, energies,
            radius_km, angular_order, path_order
        )
        source_weights = source[source_mask, None, :] * legacy["angle_weights"][None, :, None]
        comparisons = []
        angle_masks = [("all", np.ones(len(legacy["angle_weights"]), dtype=bool))]
        for lo, hi in ANGLE_BINS:
            mask = (legacy["angle_weights"] > 0.0)
            # The angle nodes are reconstructed from the same Gauss-Legendre rule.
            angle_nodes, _ = np.polynomial.legendre.leggauss(angular_order)
            mask = (angle_nodes >= lo) & (
                (angle_nodes < hi) if hi < 1.0 else (angle_nodes <= hi)
            )
            angle_masks.append((f"{lo:g} to {hi:g}", mask))
        for old_name, new_values in analytic_map.items():
            old_values = legacy["columns_by_channel"][old_name]
            for ish, shell in enumerate(legacy["shell_labels"]):
                for angle_label, angle_mask in angle_masks:
                    weights = source_weights[:, angle_mask, :]
                    old = old_values[ish, source_mask, :, :][:, angle_mask, :]
                    new = new_values[ish, source_mask, :, :][:, angle_mask, :]
                    numerator = float(np.sum(weights * np.abs(old - new)))
                    denominator = float(np.sum(weights * new))
                    comparisons.append({
                        "legacy_channel": old_name,
                        "path_shell": shell,
                        "direction_bin": angle_label,
                        "source_weighted_L1_relative_difference": (
                            numerator / denominator if denominator > 0.0 else 0.0
                        ),
                    })
        rows_by_order.append({
            "path_order": path_order,
            "legacy_shell_sum_to_legacy_direct_max_relative_residual": legacy[
                "shell_sum_to_direct_column_max_relative_residual"
            ],
            "source_weighted_shell_comparisons_for_8_15km_emission": comparisons,
        })
    return {
        "base_path_order": base_path_order,
        "path_order_scan": path_orders,
        "convergence_by_path_order": rows_by_order,
    }


def _angular_order_convergence(
    source, radii, radial_grid, reduced, mass, energies, couplings,
    selected_indices, radius_km, base_order, base_columns,
):
    """Check the full-angle integral at n_mu/2, n_mu, and 2*n_mu."""
    orders = sorted(set((max(8, base_order // 2), base_order, base_order * 2)))
    source_regions = {
        "all_emission_radii": np.ones(len(radii), dtype=bool),
        "dominant_8_15km_emission": (radii >= 8.0) & (radii < 15.0),
    }
    results = []
    for order in orders:
        if order == base_order:
            columns = base_columns
            angle_weights = np.polynomial.legendre.leggauss(order)[1] / 2.0
        else:
            columns, _, angle_weights = segmented_radial_columns(
                radii, radial_grid, reduced, mass, energies,
                radius_km, order, SHELL_EDGES_KM
            )
        total_columns = np.sum(columns, axis=(0, 1))
        coupling_rows = []
        for label, index in selected_indices.items():
            g = float(couplings[index])
            region_rows = []
            for region_name, source_mask in source_regions.items():
                w0 = source[source_mask, None, :] * angle_weights[None, :, None]
                we = w0 * np.exp(-g * g * total_columns[source_mask])
                region_rows.append({
                    "region": region_name,
                    "source_weighted_escape_probability": (
                        float(np.sum(we) / np.sum(w0)) if np.sum(w0) else None
                    ),
                })
            coupling_rows.append({"label": label, "g": g, "regions": region_rows})
        results.append({"angular_order": order, "representative_couplings": coupling_rows})

    reference = results[-1]
    reference_lookup = {
        (c["label"], r["region"]): r["source_weighted_escape_probability"]
        for c in reference["representative_couplings"] for r in c["regions"]
    }
    for item in results:
        for coupling_row in item["representative_couplings"]:
            for region_row in coupling_row["regions"]:
                ref = reference_lookup[(coupling_row["label"], region_row["region"])]
                value = region_row["source_weighted_escape_probability"]
                region_row["relative_difference_vs_highest_angular_order"] = (
                    abs(value - ref) / abs(ref) if ref not in (None, 0.0) else None
                )
    return {"orders": orders, "reference_order": orders[-1], "results": results}


def _direction_bin_quadrature_convergence(
    source, radii, radial_grid, reduced, mass, energies, couplings,
    selected_indices, radius_km, per_bin_orders=(8, 16, 32),
):
    """Converge each direction bin using a separate mapped Gauss rule."""
    source_regions = {
        "all_emission_radii": np.ones(len(radii), dtype=bool),
        "dominant_8_15km_emission": (radii >= 8.0) & (radii < 15.0),
    }
    results = []
    reference_data = None
    for per_bin_order in per_bin_orders:
        columns, angles, weights, bin_ids = direction_binned_radial_columns(
            radii, radial_grid, reduced, mass, energies,
            radius_km, per_bin_order, SHELL_EDGES_KM
        )
        if per_bin_order == per_bin_orders[-1]:
            reference_data = (columns, angles, weights, bin_ids)
        total_columns = np.sum(columns, axis=(0, 1))
        coupling_rows = []
        for label, index in selected_indices.items():
            g = float(couplings[index])
            region_rows = []
            for region_name, source_mask in source_regions.items():
                w0 = source[source_mask, None, :] * weights[None, :, None]
                we = w0 * np.exp(-g * g * total_columns[source_mask])
                base_norm = float(np.sum(w0))
                escaped_norm = float(np.sum(we))
                bins = []
                for ib, (lo, hi) in enumerate(ANGLE_BINS):
                    angle_mask = bin_ids == ib
                    w0_bin = w0[:, angle_mask, :]
                    we_bin = we[:, angle_mask, :]
                    bins.append({
                        "cos_theta_bin": [lo, hi],
                        "thin_source_fraction": (
                            float(np.sum(w0_bin) / base_norm) if base_norm else 0.0
                        ),
                        "escaped_luminosity_fraction": (
                            float(np.sum(we_bin) / escaped_norm) if escaped_norm else 0.0
                        ),
                        "mean_escape_probability": (
                            float(np.sum(we_bin) / np.sum(w0_bin))
                            if np.sum(w0_bin) else None
                        ),
                    })
                region_rows.append({
                    "region": region_name,
                    "source_weighted_escape_probability": (
                        escaped_norm / base_norm if base_norm else None
                    ),
                    "direction_bins": bins,
                })
            coupling_rows.append({"label": label, "g": g, "regions": region_rows})
        results.append({
            "per_bin_order": per_bin_order,
            "representative_couplings": coupling_rows,
        })

    reference = results[-1]
    reference_lookup = {}
    for c in reference["representative_couplings"]:
        for r in c["regions"]:
            reference_lookup[(c["label"], r["region"])] = r
    for item in results:
        for c in item["representative_couplings"]:
            for r in c["regions"]:
                ref = reference_lookup[(c["label"], r["region"])]
                ref_escape = ref["source_weighted_escape_probability"]
                value = r["source_weighted_escape_probability"]
                r["relative_difference_escape_vs_reference_order"] = (
                    abs(value - ref_escape) / abs(ref_escape)
                    if ref_escape not in (None, 0.0) else None
                )
                for bin_row, ref_bin in zip(r["direction_bins"], ref["direction_bins"]):
                    ref_fraction = ref_bin["escaped_luminosity_fraction"]
                    value_fraction = bin_row["escaped_luminosity_fraction"]
                    bin_row["relative_difference_escaped_fraction_vs_reference_order"] = (
                        abs(value_fraction - ref_fraction) / abs(ref_fraction)
                        if ref_fraction not in (None, 0.0) else None
                    )
    return {
        "per_bin_orders": list(per_bin_orders),
        "reference_order": per_bin_orders[-1],
        "results": results,
    }, reference_data


def run_audit(
    profile_path=DEFAULT_PROFILE, fig7_path=DEFAULT_FIG7, mass=10.0,
    radial_order=40, energy_order=100, angular_order=32,
    legacy_path_order=32, direct_path_order=256,
    radius_km=25.0, energy_offset=1000.0,
):
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
    couplings = np.asarray(vertices["g"], float)
    reference_luminosities = np.asarray(vertices["luminosity_erg_s"], float)

    radii, radial_weights = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, radii, radius_km])
    profile = load_profile(profile_path, radial_grid)
    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass / profile["lapse"]])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()

    rates = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    production, reduced, channel_closure = reduced_absorption_channels(
        mass, energies, profile, rates
    )
    columns, angles, angle_weights = segmented_radial_columns(
        radii, radial_grid, reduced, mass, energies,
        radius_km, angular_order, SHELL_EDGES_KM
    )
    channel_names = list(reduced)
    shell_labels = [
        f"{lo:g}-{hi:g}km"
        for lo, hi in zip(SHELL_EDGES_KM[:-1], SHELL_EDGES_KM[1:])
    ]
    total_columns = np.sum(columns, axis=(0, 1))

    source_indices = np.searchsorted(radial_grid, radii)
    source, source_meta = eq_b1_source_measure(
        radii, radial_weights, energies, profile["lapse"][source_indices],
        mass, rates["production"][source_indices]
    )
    source_8_15 = (radii >= 8.0) & (radii < 15.0)

    direct_columns, direct_angles = scalar_optical_depths(
        radii, radial_grid, rates["reduced_absorption"], mass, energies,
        radius_km, angular_order, direct_path_order
    )
    direct_residual = float(np.max(
        np.abs(total_columns - direct_columns)
        / np.maximum(np.abs(direct_columns), 1.0e-300)
    ))
    direct_source_weighted_residual = float(
        np.sum(source[source_8_15, None, :] *
               np.abs(total_columns[source_8_15] - direct_columns[source_8_15]) *
               angle_weights[None, :, None])
        / max(float(np.sum(source[source_8_15, None, :] *
                           direct_columns[source_8_15] *
                           angle_weights[None, :, None])), 1.0e-300)
    )

    legacy_comparison = _legacy_shell_comparison(
        source, source_8_15, columns, channel_names, radial_grid,
        radii, profile, rates, mass, energies, radius_km,
        angular_order, legacy_path_order
    )

    selected_indices = {
        "weak_endpoint": 0,
        "reference_luminosity_peak": int(np.argmax(reference_luminosities)),
        "strong_endpoint": len(couplings) - 1,
    }
    direction_convergence, direction_data = _direction_bin_quadrature_convergence(
        source, radii, radial_grid, reduced, mass, energies, couplings,
        selected_indices, radius_km, (8, 16, 32)
    )
    selected = []
    for label, index in selected_indices.items():
        g = float(couplings[index])
        regions = [
            _region_summary(
                "all_emission_radii", np.ones(len(radii), dtype=bool),
                source, columns, total_columns, channel_names, shell_labels,
                SHELL_EDGES_KM, radii, angles, angle_weights, g,
                direction_data
            ),
            _region_summary(
                "dominant_8_15km_emission", source_8_15,
                source, columns, total_columns, channel_names, shell_labels,
                SHELL_EDGES_KM, radii, angles, angle_weights, g,
                direction_data
            ),
        ]
        selected.append({
            "label": label,
            "coupling_index": int(index),
            "g": g,
            "reference_luminosity_erg_s": float(reference_luminosities[index]),
            "regions": regions,
        })

    angular_convergence = _angular_order_convergence(
        source, radii, radial_grid, reduced, mass, energies, couplings,
        selected_indices, radius_km, angular_order, columns
    )

    return {
        "title": "B.2 inner-path opacity: channel x radial shell x emission direction",
        "mass_MeV": float(mass),
        "scope": [
            "Pure-vector Blinov B.14-B.19 transport baseline at fixed omega.",
            "B.1 source, reconstructed SFHo-18.8 profile, Rmax=25 km, and all coupling values are held fixed.",
            "Opacity channels are nu_mu inverse decay, nu_tau inverse decay, Compton, and dimuon.",
            "The 10 MeV dimuon channel is kinematically closed and is retained as an explicit zero channel.",
            "The exact moving-muon B.13 local kernel is not substituted into the B.14-B.19 transport baseline.",
            "No source, coupling, opacity, or luminosity rescaling; no axial-vector curve is generated.",
        ],
        "configuration": {
            "radial_order": radial_order,
            "energy_order": energy_order,
            "angular_order": angular_order,
            "angular_order_scan": sorted(set((max(8, angular_order // 2), angular_order, angular_order * 2))),
            "direction_bin_per_interval_order": 32,
            "direction_bin_per_interval_order_scan": [8, 16, 32],
            "legacy_path_order": legacy_path_order,
            "direct_path_order": direct_path_order,
            "radius_km": radius_km,
            "energy_offset_MeV": energy_offset,
            "path_energy_convention": "fixed omega along the B.2 path",
            "shell_edges_km": SHELL_EDGES_KM.tolist(),
            "direction_bins": [list(x) for x in ANGLE_BINS],
        },
        "provenance": {
            "profile_path": str(profile_path),
            "profile_sha256": sha256(profile_path),
            "fig7_reference_path": str(fig7_path),
            "fig7_reference_sha256": sha256(fig7_path),
            "fig7_source_pdf_sha256": fig7.get("pdf_sha256"),
            "run_commit_sha": os.environ.get("GITHUB_SHA"),
        },
        "eq_b1_source_measure": source_meta,
        "source_fraction_8_15km_of_total_B1": float(
            np.sum(source[source_8_15]) / np.sum(source)
        ),
        "local_rate_samples": _local_rate_samples(
            mass, profile, radial_grid
        ),
        "internal_closure": {
            **channel_closure,
            "angular_weight_sum_residual": float(abs(np.sum(angle_weights) - 1.0)),
            "analytic_total_vs_global_s_quadrature_max_relative_residual": direct_residual,
            "analytic_total_vs_global_s_quadrature_source_weighted_L1_relative_residual_8_15km": direct_source_weighted_residual,
        },
        "legacy_masked_shell_vs_analytic_radial_integration": legacy_comparison,
        "angular_order_convergence": angular_convergence,
        "direction_bin_quadrature_convergence": direction_convergence,
        "representative_couplings": selected,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--na", type=int, default=32)
    parser.add_argument("--legacy-path-order", type=int, default=32)
    parser.add_argument("--direct-path-order", type=int, default=256)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()
    result = run_audit(
        args.profile, args.fig7, args.mass, args.nr, args.ne, args.na,
        args.legacy_path_order, args.direct_path_order, 25.0,
        args.energy_offset
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "source_fraction_8_15km": result["source_fraction_8_15km_of_total_B1"],
        "internal_closure": result["internal_closure"],
        "legacy_shell_max_L1_by_path_order": [
            {
                "path_order": item["path_order"],
                "max_L1_by_channel": {
                    channel: max(
                        (row["source_weighted_L1_relative_difference"]
                         for row in item["source_weighted_shell_comparisons_for_8_15km_emission"]
                         if row["legacy_channel"] == channel),
                        default=0.0
                    )
                    for channel in ("neutrino", "compton", "dimuon")
                },
            }
            for item in result["legacy_masked_shell_vs_analytic_radial_integration"]["convergence_by_path_order"]
        ],
        "angular_convergence_strong_8_15km": [
            {
                "angular_order": item["angular_order"],
                "escape_probability": next(
                    region["source_weighted_escape_probability"]
                    for coupling in item["representative_couplings"]
                    if coupling["label"] == "strong_endpoint"
                    for region in coupling["regions"]
                    if region["region"] == "dominant_8_15km_emission"
                ),
                "relative_difference_vs_64": next(
                    region["relative_difference_vs_highest_angular_order"]
                    for coupling in item["representative_couplings"]
                    if coupling["label"] == "strong_endpoint"
                    for region in coupling["regions"]
                    if region["region"] == "dominant_8_15km_emission"
                ),
            }
            for item in result["angular_order_convergence"]["results"]
        ],
        "direction_bin_convergence_strong_8_15km": [
            {
                "per_bin_order": item["per_bin_order"],
                "escape_probability": next(
                    region["source_weighted_escape_probability"]
                    for coupling in item["representative_couplings"]
                    if coupling["label"] == "strong_endpoint"
                    for region in coupling["regions"]
                    if region["region"] == "dominant_8_15km_emission"
                ),
                "direction_bins": next(
                    region["direction_bins"]
                    for coupling in item["representative_couplings"]
                    if coupling["label"] == "strong_endpoint"
                    for region in coupling["regions"]
                    if region["region"] == "dominant_8_15km_emission"
                ),
            }
            for item in result["direction_bin_quadrature_convergence"]["results"]
        ],
        "selected": [
            {
                "label": row["label"], "g": row["g"],
                "regions": [
                    {
                        "region": region["region"],
                        "escape": region["source_weighted_escape_probability"],
                        "direction_bins": [
                            {
                                "cos_theta_bin": item["cos_theta_bin"],
                                "escaped_fraction": item["escaped_luminosity_fraction"],
                                "mean_tau_escape_weighted": item[
                                    "mean_total_tau_escaped_population_weighted_per_g2"
                                ],
                            } for item in region["direction_bins"]
                        ],
                    } for region in row["regions"]
                ],
            } for row in result["representative_couplings"]
        ],
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
