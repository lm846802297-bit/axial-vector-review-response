#!/usr/bin/env python3
"""Source/absorber radial-weight decomposition for the 10 MeV Fig. 7 tail.

This is a spatial bookkeeping audit, not a fit. It uses the frozen Caputo
reconstructed profile, unchanged local production/absorption rates, the
independently validated analytic Eq. (B.2) ray integral, and the same 25 km
transport boundary. It reports the joint distribution of production radius
and absorber radius, plus the production-shell escape weighting at weak,
peak, and high-absorption Fig. 7 points.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .audit_eq_b2_path_integral import (
        MASS_MEV, RMAX_KM, build_frozen_state, exact_columns,
        load_fig7_points,
    )
except ImportError:
    from audit_eq_b2_path_integral import (
        MASS_MEV, RMAX_KM, build_frozen_state, exact_columns,
        load_fig7_points,
    )

HERE = Path(__file__).resolve().parent
PROFILE_DEFAULT = HERE.parent / "data" / "sfho188_digitized.csv"
FIG7_DEFAULT = HERE / "outputs" / "fig7_10mev_three_layer.json"
OUTPUT_DEFAULT = HERE / "outputs" / "fig7_spatial_weight_matrix_2026-11-08.json"

RADIAL_BINS = (
    (0.0, 5.0), (5.0, 10.0), (10.0, 15.0),
    (15.0, 20.0), (20.0, 25.0),
)
ANGLE_ORDER = 128
RADIAL_ORDER = 40
ENERGY_ORDER = 100
ENERGY_OFFSET_MEV = 1000.0


def radial_bin_mask(radii: np.ndarray, interval: tuple[float, float],
                    final_edge: float = RMAX_KM) -> np.ndarray:
    """Half-open radial bins, with the final outer boundary included."""
    lo, hi = map(float, interval)
    r = np.asarray(radii, float)
    return (r >= lo) & ((r < hi) if hi < final_edge else (r <= hi))


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    values = np.asarray(values, float)
    weights = np.asarray(weights, float)
    denominator = float(np.sum(weights))
    if denominator <= 0.0:
        raise ValueError("A spatial bin has zero source weight")
    return float(np.sum(values * weights) / denominator)


def build_channel_opacities(state: dict) -> dict:
    """Recover channel-resolved reduced opacities from frozen detailed balance."""
    energies = state["energies"]
    temperature = state["profile"]["T"][:, None]
    x = energies[None, :] / temperature
    stimulated_factor = np.expm1(x)

    # The 10 MeV dimuon channel is kinematically closed. The flavor split is
    # evaluated independently with the same Fermi-pair function used by the
    # frozen local-rate implementation.
    try:
        from .reference import fermi_pair_average
    except ImportError:
        from reference import fermi_pair_average
    mu_numu = state["profile"]["mu_numu"][:, None]
    velocity = np.sqrt(1.0 - (MASS_MEV / energies[None, :])**2)
    nu_mu_production = (
        MASS_MEV**2 / (8.0 * np.pi * energies[None, :])
        * fermi_pair_average(mu_numu, energies[None, :], temperature, velocity)
    )
    nu_tau_production = (
        MASS_MEV**2 / (8.0 * np.pi * energies[None, :])
        * fermi_pair_average(np.zeros_like(mu_numu), energies[None, :],
                             temperature, velocity)
    )
    compton_production = state["rates"]["compton_production"]

    result = {
        "nu_mu": nu_mu_production * stimulated_factor,
        "nu_tau": nu_tau_production * stimulated_factor,
        "compton": compton_production * stimulated_factor,
    }
    result["neutrino"] = result["nu_mu"] + result["nu_tau"]
    result["total"] = result["neutrino"] + result["compton"]

    reference_total = state["total_reduced"]
    result["local_channel_closure_max_relative_residual"] = float(np.max(
        np.abs(result["total"] - reference_total)
        / np.maximum(np.abs(reference_total), 1.0e-300)
    ))
    return result


def representative_points(fig7_path: Path) -> dict:
    points = load_fig7_points(fig7_path)
    weak = points[0]
    peak = max(points, key=lambda item: item["reference_luminosity_erg_s"])
    high = points[-1]
    return {
        "weak": {
            "g": float(weak["g"]),
            "reference_luminosity_erg_s": float(weak["reference_luminosity_erg_s"]),
        },
        "reference_peak": {
            "g": float(peak["g"]),
            "reference_luminosity_erg_s": float(peak["reference_luminosity_erg_s"]),
        },
        "high_absorption": {
            "g": float(high["g"]),
            "reference_luminosity_erg_s": float(high["reference_luminosity_erg_s"]),
        },
    }


def run_audit(profile_path: Path, fig7_path: Path, output_path: Path) -> dict:
    state = build_frozen_state(
        profile_path,
        radial_order=RADIAL_ORDER,
        energy_order=ENERGY_ORDER,
        energy_offset_mev=ENERGY_OFFSET_MEV,
    )
    radii = state["source_radii"]
    radial_grid = state["radial_grid"]
    energies = state["energies"]
    source = state["source"]
    channels = build_channel_opacities(state)

    if channels["local_channel_closure_max_relative_residual"] > 2.0e-11:
        raise AssertionError("Channel-resolved opacity does not close to frozen total rate")

    angle_nodes, angle_weights = leggauss(ANGLE_ORDER)
    angle_weights = angle_weights / 2.0
    source_angle_energy_weights = (
        source[:, None, :] * angle_weights[None, :, None]
    )

    # Independently integrate each absorber shell. The shell edges are exact
    # geometric breakpoints in the path integrator, not radial masks on a
    # coarse path quadrature.
    shell_columns = {}
    for shell in RADIAL_BINS:
        key = f"{shell[0]:g}-{shell[1]:g}"
        shell_columns[key] = {}
        for channel in ("nu_mu", "nu_tau", "compton"):
            shell_columns[key][channel] = exact_columns(
                radii, angle_nodes, radial_grid, channels[channel],
                MASS_MEV, energies, RMAX_KM, absorber_range=shell,
            )

    # A direct full-path calculation provides an independent closure target.
    full_columns = {
        channel: exact_columns(
            radii, angle_nodes, radial_grid, channels[channel],
            MASS_MEV, energies, RMAX_KM,
        )
        for channel in ("nu_mu", "nu_tau", "compton")
    }

    shell_sum_residuals = {}
    for channel in ("nu_mu", "nu_tau", "compton"):
        summed = sum(shell_columns[
            f"{lo:g}-{hi:g}"
        ][channel] for lo, hi in RADIAL_BINS)
        denominator = np.maximum(np.abs(full_columns[channel]), 1.0e-300)
        shell_sum_residuals[channel] = float(np.max(
            np.abs(summed - full_columns[channel]) / denominator
        ))

    neutrino_full = full_columns["nu_mu"] + full_columns["nu_tau"]
    total_full = neutrino_full + full_columns["compton"]
    frozen_total = exact_columns(
        radii, angle_nodes, radial_grid, state["total_reduced"],
        MASS_MEV, energies, RMAX_KM,
    )
    total_closure = float(np.max(
        np.abs(total_full - frozen_total)
        / np.maximum(np.abs(frozen_total), 1.0e-300)
    ))

    points = representative_points(fig7_path)
    high_g = points["high_absorption"]["g"]

    # Joint matrix: each cell is the source-weighted mean optical depth
    # contributed by one absorber shell, conditional on production in one
    # source-radius shell. This is not an absorbed-luminosity fraction.
    joint_matrix = []
    by_production_shell = []
    for production_shell in RADIAL_BINS:
        source_mask = radial_bin_mask(radii, production_shell)
        weights = source_angle_energy_weights[source_mask]
        row = {
            "production_radius_km": list(production_shell),
            "source_weight_fraction": float(
                np.sum(source[source_mask]) / np.sum(source)
            ),
            "absorber_shell_contributions": [],
        }
        mean_tau_nu_sum = 0.0
        mean_tau_compton_sum = 0.0
        for absorber_shell in RADIAL_BINS:
            key = f"{absorber_shell[0]:g}-{absorber_shell[1]:g}"
            nu_cols = (
                shell_columns[key]["nu_mu"][source_mask]
                + shell_columns[key]["nu_tau"][source_mask]
            )
            compton_cols = shell_columns[key]["compton"][source_mask]
            tau_nu = weighted_mean(high_g**2 * nu_cols, weights)
            tau_compton = weighted_mean(high_g**2 * compton_cols, weights)
            mean_tau_nu_sum += tau_nu
            mean_tau_compton_sum += tau_compton
            row["absorber_shell_contributions"].append({
                "absorber_radius_km": list(absorber_shell),
                "mean_neutrino_tau": tau_nu,
                "mean_compton_tau": tau_compton,
                "mean_total_tau": tau_nu + tau_compton,
            })
        row["mean_neutrino_tau_all_radii"] = mean_tau_nu_sum
        row["mean_compton_tau_all_radii"] = mean_tau_compton_sum
        row["mean_total_tau_all_radii"] = mean_tau_nu_sum + mean_tau_compton_sum
        joint_matrix.append(row)

    # Source-shell production and escape weights at three Fig. 7 points.
    escape_decomposition = {}
    total_columns = total_full
    for label, point in points.items():
        g = point["g"]
        escape = np.exp(-g*g*total_columns)
        total_thin = float(g*g*np.sum(source))
        total_escaped = float(
            g*g*np.sum(source_angle_energy_weights * escape)
        )
        rows = []
        for production_shell in RADIAL_BINS:
            mask = radial_bin_mask(radii, production_shell)
            thin = float(g*g*np.sum(source[mask]))
            escaped = float(
                g*g*np.sum(source_angle_energy_weights[mask] * escape[mask])
            )
            rows.append({
                "production_radius_km": list(production_shell),
                "thin_luminosity_erg_s": thin,
                "thin_source_fraction": thin / total_thin,
                "escaped_luminosity_erg_s": escaped,
                "escaped_luminosity_fraction": escaped / total_escaped,
                "source_weighted_escape_probability": escaped / thin if thin > 0.0 else None,
            })
        escape_decomposition[label] = {
            "g": g,
            "reference_luminosity_erg_s": point["reference_luminosity_erg_s"],
            "calculated_luminosity_erg_s": total_escaped,
            "calculated_over_reference_minus_one": (
                total_escaped / point["reference_luminosity_erg_s"] - 1.0
            ),
            "overall_escape_fraction": total_escaped / total_thin,
            "production_shells": rows,
        }

    profile_samples = []
    for radius in (0.0, 5.0, 10.0, 15.0, 20.0, 25.0):
        sample = {"r_km": radius}
        for name in ("T", "mu_mu", "mu_numu", "lapse"):
            sample[name] = float(np.interp(radius, radial_grid, state["profile"][name]))
        # Show the local 10.1 MeV opacity split without changing the energy grid.
        target = 10.1
        ir = int(np.argmin(np.abs(radial_grid - radius)))
        nu_rate = channels["neutrino"][ir]
        comp_rate = channels["compton"][ir]
        sample["nearest_profile_node_km"] = float(radial_grid[ir])
        sample["reduced_neutrino_opacity_at_10p1_MeV_MeV"] = float(
            np.interp(target, energies, nu_rate)
        )
        sample["reduced_compton_opacity_at_10p1_MeV_MeV"] = float(
            np.interp(target, energies, comp_rate)
        )
        profile_samples.append(sample)

    result = {
        "title": "Blinov Fig. 7 10 MeV joint production/absorption spatial-weight audit",
        "status": "PASS_FROZEN_PROFILE_SPATIAL_DECOMPOSITION",
        "source": "Blinov et al., arXiv:2511.09619v2, Appendix B, Eqs. (B.1)-(B.5)",
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "profile_sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
        "fig7_input_sha256": hashlib.sha256(fig7_path.read_bytes()).hexdigest(),
        "frozen_inputs": {
            "mass_MeV": MASS_MEV,
            "R_max_km": RMAX_KM,
            "profile": "existing Caputo-digitized reconstructed SFHo-18.8 profile",
            "mu_nu_tau": "zero baseline",
            "path_energy": "fixed omega, literal Eq. (B.2)",
            "local_rates": "unchanged reference.local_rates output",
            "radial_order": RADIAL_ORDER,
            "energy_order": ENERGY_ORDER,
            "energy_offset_MeV": ENERGY_OFFSET_MEV,
            "angular_order": ANGLE_ORDER,
        },
        "representative_fig7_points": points,
        "profile_samples": profile_samples,
        "local_rate_closure": {
            "channel_sum_max_relative_residual": channels[
                "local_channel_closure_max_relative_residual"
            ],
            "path_shell_additivity_max_relative_residual": shell_sum_residuals,
            "total_channel_vs_frozen_total_path_max_relative_residual": total_closure,
        },
        "joint_production_absorber_matrix_at_high_coupling": {
            "definition": (
                "Each cell is g^2 times the source-weighted mean optical-depth "
                "contribution from the absorber shell, conditional on production "
                "in the listed source-radius shell. It is not an absorbed-luminosity fraction."
            ),
            "rows": joint_matrix,
        },
        "source_and_escape_decomposition": escape_decomposition,
        "interpretation": [
            "The profile and all local rates are frozen; this audit does not fit or rescale any input.",
            "The joint matrix separates production radius from absorber radius, avoiding the ambiguity between where V is produced and where it is absorbed.",
            "The source-weighted mean optical depth is a diagnostic average; it is not equal to the logarithm of the luminosity-weighted escape fraction.",
            "The escape decomposition reports both the optically thin source distribution and the surviving luminosity distribution at weak, peak, and high-absorption points.",
            "The calculation uses the reconstructed Caputo profile, not the original author simulation tables. A direct radial-profile comparison with Blinov's private s18.8-SFHo-MUONS data is not possible from the plotted Fig. 7 curve alone.",
            "The digitized Fig. 7 curve supplies integrated luminosities only; it does not determine the authors' internal source-radius or absorber-radius weights.",
        ],
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n",
                            encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=PROFILE_DEFAULT)
    parser.add_argument("--fig7", type=Path, default=FIG7_DEFAULT)
    parser.add_argument("--output", type=Path, default=OUTPUT_DEFAULT)
    args = parser.parse_args()
    result = run_audit(args.profile, args.fig7, args.output)
    print(json.dumps({
        "status": result["status"],
        "closure": result["local_rate_closure"],
        "joint_matrix": result["joint_production_absorber_matrix_at_high_coupling"],
        "escape_decomposition": result["source_and_escape_decomposition"],
    }, indent=2))


if __name__ == "__main__":
    main()
