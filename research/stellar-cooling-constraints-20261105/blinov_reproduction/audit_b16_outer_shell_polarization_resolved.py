"""Polarization-resolved 22--25 km inverse-decay opacity diagnostic.

The literal scalar B.2 baseline is retained. This audit separately propagates
L,+,- modes through the outer shell, using the mode-resolved B.6/B.10 rates.
It reports (i) neutrino-production-weighted mode transport and (ii) an
unpolarized Compton-source split as an explicit diagnostic assumption.

No production axial code, scalar reference, coupling, or luminosity is changed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

try:
    from .reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_inner_path_channel_directional import (
        direction_binned_radial_columns,
    )
    from .audit_b16_neutrino_inverse_decay_direct import direct_flavour_integrals
    import rates as production_rates
except ImportError:
    from reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_inner_path_channel_directional import (
        direction_binned_radial_columns,
    )
    from audit_b16_neutrino_inverse_decay_direct import direct_flavour_integrals
    import rates as production_rates

DEFAULT_OUTPUT = HERE / "outputs" / "b16_outer_shell_polarization_resolved_10mev_2026-11-09.json"
MASS_DEFAULT = 10.0
RADIUS_INNER = 22.0
RADIUS_OUTER = 25.0
SOURCE_RANGE = (8.0, 15.0)
ANGLE_BINS = ((-1.0, -0.5), (-0.5, 0.0), (0.0, 0.5), (0.5, 1.0))
COUPLINGS = {
    "fig7_peak": 1.1341108687336194e-8,
    "strong_endpoint": 4.171689650228597e-8,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def mode_neutrino_rates(mass, energies, temperature, mu_numu, order=48):
    """Return total nu_mu+nu_tau production and absorption for L,+,-."""
    omega = np.asarray(energies, float)[None, :]
    temp = np.asarray(temperature, float)[:, None]
    mu = np.asarray(mu_numu, float)[:, None]
    p_mu, a_mu = production_rates.neutrino_rates(
        mass, omega, temp, mu, order=order
    )
    p_tau, a_tau = production_rates.neutrino_rates(
        mass, omega, temp, np.zeros_like(mu), order=order
    )
    return p_mu + p_tau, a_mu + a_tau


def _source_measure(radius, radial_weights, energies, lapse, mass, production):
    return eq_b1_source_measure(
        radius, radial_weights, energies, lapse, mass, production
    )[0]


def _escape_scalar(source, columns, angle_weights, coupling, angle_mask=None):
    if angle_mask is None:
        angle_mask = np.ones(len(angle_weights), dtype=bool)
    weights = source[:, None, :] * angle_weights[None, angle_mask, None]
    selected = columns[:, angle_mask, :]
    denominator = float(np.sum(weights))
    if denominator <= 0.0:
        return None
    return float(np.sum(weights * np.exp(-coupling * coupling * selected)) / denominator)


def _escape_modes(source_modes, columns_modes, angle_weights, coupling,
                  angle_mask=None, denominator_source=None):
    if angle_mask is None:
        angle_mask = np.ones(len(angle_weights), dtype=bool)
    weights = angle_weights[None, angle_mask, None]
    numerator = 0.0
    for mode in range(3):
        numerator += float(np.sum(
            source_modes[mode][:, None, :] * weights
            * np.exp(-coupling * coupling * columns_modes[mode][:, angle_mask, :])
        ))
    if denominator_source is None:
        denominator_source = np.sum(source_modes)
    denominator = float(denominator_source)
    return float(numerator / denominator) if denominator > 0.0 else None


def run(profile_path=DEFAULT_PROFILE, mass=MASS_DEFAULT, radial_order=40,
        energy_order=100, energy_offset=1000.0, angular_order_per_bin=32,
        rate_order=48, direct_order=512):
    raw = np.genfromtxt(profile_path, delimiter=",", names=True)
    raw_r = np.asarray(raw["r_km"], float)
    outer_mask = (raw_r >= RADIUS_INNER) & (raw_r <= RADIUS_OUTER)
    outer_r = raw_r[outer_mask]
    if len(outer_r) < 20 or not np.isclose(outer_r[0], RADIUS_INNER) or not np.isclose(outer_r[-1], RADIUS_OUTER):
        raise ValueError("Expected the archived 0.05 km profile to cover 22--25 km")

    # Build the same B.1 source quadrature as the scalar reference.
    source_r, source_rw = radial_rule(RADIUS_OUTER, radial_order)
    source_profile = load_profile(profile_path, source_r)
    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass / source_profile["lapse"], 12.0, 20.0, 50.0])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()

    source_rates = local_rates(
        mass, energies[None, :],
        source_profile["T"][:, None],
        source_profile["mu_numu"][:, None],
        source_profile["mu_mu"][:, None],
    )
    source_prod_modes, _ = mode_neutrino_rates(
        mass, energies, source_profile["T"], source_profile["mu_numu"],
        order=rate_order,
    )
    source_modes = np.stack([
        _source_measure(
            source_r, source_rw, energies, source_profile["lapse"], mass,
            source_prod_modes[:, :, mode],
        )
        for mode in range(3)
    ])
    source_nu = _source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        source_rates["neutrino_production"],
    )
    source_compton = _source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        source_rates["compton_production"],
    )
    source_total = _source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        source_rates["production"],
    )
    source_mode_sum_residual = float(
        np.max(np.abs(np.sum(source_modes, axis=0) - source_nu)
               / np.maximum(np.abs(source_nu), 1.0e-300))
    )
    source_channel_sum_residual = float(
        np.max(np.abs(source_nu + source_compton - source_total)
               / np.maximum(np.abs(source_total), 1.0e-300))
    )

    selected = (source_r >= SOURCE_RANGE[0]) & (source_r <= SOURCE_RANGE[1])
    selected_r = source_r[selected]
    selected_total = source_total[selected]
    selected_nu = source_nu[selected]
    selected_compton = source_compton[selected]
    selected_modes = source_modes[:, selected, :]
    total_source_weight = float(np.sum(selected_total))
    neutrino_source_weight = float(np.sum(selected_nu))
    if total_source_weight <= 0.0 or neutrino_source_weight <= 0.0:
        raise ValueError("Selected 8--15 km source weight is zero")

    # Re-evaluate the local opacity on the original 0.05 km outer-shell nodes.
    outer_T = np.asarray(raw["T_MeV"][outer_mask], float)
    outer_mu_numu = np.asarray(raw["mu_numu_MeV"][outer_mask], float)
    outer_mu_mu = np.asarray(raw["mu_mu_MeV"][outer_mask], float)
    outer_rates = local_rates(
        mass, energies[None, :], outer_T[:, None],
        outer_mu_numu[:, None], outer_mu_mu[:, None],
    )
    outer_prod_modes, outer_abs_modes = mode_neutrino_rates(
        mass, energies, outer_T, outer_mu_numu, order=rate_order
    )
    x = energies[None, :] / outer_T[:, None]
    reduced_modes = -np.expm1(-x)[..., None] * outer_abs_modes
    reduced_compton = np.expm1(np.minimum(x, 700.0)) * outer_rates["compton_production"]
    reduced_scalar = np.asarray(outer_rates["reduced_absorption"], float)
    reduced_scalar_nu = np.expm1(np.minimum(x, 700.0)) * outer_rates["neutrino_production"]

    mode_prod_sum = np.sum(outer_prod_modes, axis=-1)
    mode_reduced_sum = np.sum(reduced_modes, axis=-1)
    scalar_rate_residual = float(np.max(
        np.abs(mode_prod_sum - outer_rates["neutrino_production"])
        / np.maximum(np.abs(outer_rates["neutrino_production"]), 1.0e-300)
    ))
    reduced_rate_residual = float(np.max(
        np.abs(mode_reduced_sum - reduced_scalar_nu)
        / np.maximum(np.abs(reduced_scalar_nu), 1.0e-300)
    ))
    scalar_channel_residual = float(np.max(
        np.abs(reduced_scalar_nu + reduced_compton - reduced_scalar)
        / np.maximum(np.abs(reduced_scalar), 1.0e-300)
    ))
    detailed_balance_residual = float(np.max(
        np.abs(outer_prod_modes - np.exp(-x)[..., None] * outer_abs_modes)
        / np.maximum(np.abs(outer_prod_modes), 1.0e-300)
    ))

    # Keep the outer-shell primitive profile at its native 0.05 km spacing.
    # The zero-opacity prefix is discarded by selecting only the final shell.
    opacity_grid = np.r_[0.0, outer_r]
    def prepend_zero(values):
        result = np.zeros((len(opacity_grid), len(energies)), dtype=float)
        result[1:, :] = values
        return result

    reduced_by_mode = {
        "L": prepend_zero(reduced_modes[:, :, 0]),
        "plus": prepend_zero(reduced_modes[:, :, 1]),
        "minus": prepend_zero(reduced_modes[:, :, 2]),
    }
    mode_path, angles, angle_weights, bin_ids = direction_binned_radial_columns(
        selected_r, opacity_grid, reduced_by_mode, mass, energies,
        RADIUS_OUTER, per_bin_order=angular_order_per_bin,
    )
    mode_columns = np.asarray(mode_path[:, -1, :, :, :], float)

    compton_path, _, _, _ = direction_binned_radial_columns(
        selected_r, opacity_grid, {"compton": prepend_zero(reduced_compton)},
        mass, energies, RADIUS_OUTER, per_bin_order=angular_order_per_bin,
    )
    compton_columns = np.asarray(compton_path[0, -1, :, :, :], float)

    scalar_path, _, _, _ = direction_binned_radial_columns(
        selected_r, opacity_grid, {"scalar": prepend_zero(reduced_scalar)},
        mass, energies, RADIUS_OUTER, per_bin_order=angular_order_per_bin,
    )
    scalar_columns = np.asarray(scalar_path[0, -1, :, :, :], float)
    mode_plus_compton_columns = np.sum(mode_columns, axis=0) + compton_columns
    column_sum_residual = float(np.max(
        np.abs(mode_plus_compton_columns - scalar_columns)
        / np.maximum(np.abs(scalar_columns), 1.0e-300)
    ))

    # A common equal-mode split for the scalar Compton source/opacity is only
    # a diagnostic convention; the exact B.14--B.19 mode decomposition is not
    # supplied by the scalar approximation.
    mode_columns_with_compton = mode_columns + compton_columns[None, :, :, :] / 3.0
    mode_source_with_compton = (
        selected_modes + selected_compton[None, :, :] / 3.0
    )
    equal_mode_source = np.broadcast_to(
        selected_total[None, :, :] / 3.0, mode_source_with_compton.shape
    ).copy()

    # Mode-resolved production fractions for the neutrino source alone.
    mode_source_fractions = [
        float(np.sum(selected_modes[mode]) / neutrino_source_weight)
        for mode in range(3)
    ]
    compton_source_fraction = float(np.sum(selected_compton) / total_source_weight)
    neutrino_source_fraction = float(np.sum(selected_nu) / total_source_weight)

    coupling_results = {}
    for label, coupling in COUPLINGS.items():
        scalar_escape = _escape_scalar(
            selected_total, scalar_columns, angle_weights, coupling
        )
        avg_opacity_columns = np.mean(mode_columns_with_compton, axis=0)
        avg_opacity_escape = _escape_scalar(
            selected_total, avg_opacity_columns, angle_weights, coupling
        )
        equal_mode_escape = _escape_modes(
            equal_mode_source, mode_columns_with_compton, angle_weights,
            coupling, denominator_source=total_source_weight,
        )
        production_weighted_escape = _escape_modes(
            mode_source_with_compton, mode_columns_with_compton, angle_weights,
            coupling, denominator_source=total_source_weight,
        )
        neutrino_only_mode_escape = _escape_modes(
            selected_modes, mode_columns, angle_weights, coupling,
            denominator_source=neutrino_source_weight,
        )

        direction_rows = []
        for ib, (lo, hi) in enumerate(ANGLE_BINS):
            mask = bin_ids == ib
            scalar_bin = _escape_scalar(
                selected_total, scalar_columns, angle_weights, coupling, mask
            )
            average_bin = _escape_scalar(
                selected_total, avg_opacity_columns, angle_weights, coupling, mask
            )
            equal_bin = _escape_modes(
                equal_mode_source, mode_columns_with_compton, angle_weights,
                coupling, mask, denominator_source=total_source_weight / 4.0,
            )
            production_bin = _escape_modes(
                mode_source_with_compton, mode_columns_with_compton, angle_weights,
                coupling, mask, denominator_source=total_source_weight / 4.0,
            )
            direction_rows.append({
                "cos_theta_bin": [lo, hi],
                "unattenuated_source_fraction": float(
                    np.sum(selected_total[:, None, :] * angle_weights[None, mask, None])
                    / total_source_weight
                ),
                "literal_scalar_escape_factor": scalar_bin,
                "polarization_average_opacity_escape_factor": average_bin,
                "equal_mode_source_escape_factor": equal_bin,
                "neutrino_production_weighted_mode_escape_factor": production_bin,
            })

        coupling_results[label] = {
            "g": coupling,
            "literal_scalar_sum_opacity_escape_factor": scalar_escape,
            "mode_average_opacity_escape_factor": avg_opacity_escape,
            "equal_mode_source_mode_resolved_escape_factor": equal_mode_escape,
            "production_weighted_mode_resolved_escape_factor": production_weighted_escape,
            "neutrino_only_production_weighted_mode_escape_factor": neutrino_only_mode_escape,
            "mode_resolved_over_literal_scalar_ratio": (
                production_weighted_escape / scalar_escape
                if scalar_escape and production_weighted_escape is not None else None
            ),
            "direction_bins": direction_rows,
        }

    # Local longitudinal/transverse opacity comparison at representative radii.
    local_rows = []
    for radius in (22.0, 23.0, 24.0, 25.0):
        ir = int(np.argmin(np.abs(outer_r - radius)))
        for omega in (12.0, 15.0, 20.0, 30.0, 50.0, 100.0):
            ie = int(np.argmin(np.abs(energies - omega)))
            mode_values = reduced_modes[ir, ie, :]
            transverse = 0.5 * (mode_values[1] + mode_values[2])
            local_rows.append({
                "r_km": float(outer_r[ir]),
                "omega_grid_MeV": float(energies[ie]),
                "omega_target_MeV": omega,
                "omega_over_T": float(energies[ie] / outer_T[ir]),
                "mu_numu_MeV": float(outer_mu_numu[ir]),
                "reduced_absorption_modes_per_g2": mode_values.tolist(),
                "longitudinal_over_transverse": float(mode_values[0] / transverse),
                "max_mode_over_min_mode": float(np.max(mode_values) / np.min(mode_values)),
            })

    # Independent 512-point check at selected outer-shell points.
    direct_rows = []
    direct_max_production = 0.0
    direct_max_absorption = 0.0
    for radius in (22.0, 23.5, 25.0):
        ir = int(np.argmin(np.abs(outer_r - radius)))
        for omega in (12.0, 20.0, 50.0):
            T = float(outer_T[ir])
            mu = float(outer_mu_numu[ir])
            p_mu, a_mu = direct_flavour_integrals(mass, omega, T, mu, direct_order)
            p_tau, a_tau = direct_flavour_integrals(mass, omega, T, 0.0, direct_order)
            p_direct, a_direct = p_mu + p_tau, a_mu + a_tau
            ie = int(np.argmin(np.abs(energies - omega)))
            p_code, a_code = outer_prod_modes[ir, ie, :], outer_abs_modes[ir, ie, :]
            prod_err = float(np.max(
                np.abs(p_code - p_direct) / np.maximum(np.abs(p_direct), 1.0e-300)
            ))
            abs_err = float(np.max(
                np.abs(a_code - a_direct) / np.maximum(np.abs(a_direct), 1.0e-300)
            ))
            direct_max_production = max(direct_max_production, prod_err)
            direct_max_absorption = max(direct_max_absorption, abs_err)
            direct_rows.append({
                "r_km": float(outer_r[ir]),
                "omega_MeV": omega,
                "max_mode_production_relative_residual": prod_err,
                "max_mode_absorption_relative_residual": abs_err,
            })

    return {
        "title": "B.2 outer-shell polarization-resolved inverse-decay transport diagnostic",
        "mass_MeV": mass,
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(Path(profile_path)),
            "identity": "public-figure SFHo-18.8 reconstruction; not raw Garching simulation data",
            "outer_radial_nodes": int(len(outer_r)),
            "outer_radial_spacing_km": float(np.min(np.diff(outer_r))),
        },
        "configuration": {
            "radial_source_order": radial_order,
            "energy_grid_size": int(len(energies)),
            "energy_offset_MeV": energy_offset,
            "mode_rate_quadrature_order": rate_order,
            "independent_direct_quadrature_order": direct_order,
            "angular_order_per_direction_bin": angular_order_per_bin,
            "outer_shell_km": [RADIUS_INNER, RADIUS_OUTER],
            "source_region_km": list(SOURCE_RANGE),
            "fixed_omega": True,
        },
        "normalization_and_closure": {
            "source_mode_sum_max_relative_residual": source_mode_sum_residual,
            "source_neutrino_plus_compton_max_relative_residual": source_channel_sum_residual,
            "outer_mode_production_sum_vs_scalar_neutrino_max_relative_residual": scalar_rate_residual,
            "outer_mode_reduced_absorption_sum_vs_scalar_neutrino_max_relative_residual": reduced_rate_residual,
            "outer_scalar_channel_sum_max_relative_residual": scalar_channel_residual,
            "outer_B10_detailed_balance_max_relative_residual": detailed_balance_residual,
            "outer_path_mode_sum_plus_compton_vs_scalar_column_max_relative_residual": column_sum_residual,
            "direct_512_max_mode_production_relative_residual": direct_max_production,
            "direct_512_max_mode_absorption_relative_residual": direct_max_absorption,
        },
        "source": {
            "global_B1_source_fraction_from_8_15km": float(
                total_source_weight / np.sum(source_total)
            ),
            "selected_source_neutrino_fraction": neutrino_source_fraction,
            "selected_source_compton_fraction": compton_source_fraction,
            "neutrino_source_mode_fractions_L_plus_minus": mode_source_fractions,
            "Compton_source_mode_assumption": "split equally among L,+,- only for the full-source mode-resolved diagnostic",
        },
        "local_outer_mode_samples": local_rows,
        "direct_phase_space_samples": direct_rows,
        "coupling_results": coupling_results,
        "interpretation": {
            "literal_scalar": "Uses the sum of L,+,- inverse-decay opacities in the B.2 exponent, matching the repository's literal scalar reference implementation.",
            "mode_resolved": "Propagates each mode with its own inverse-decay opacity and weights it with the corresponding neutrino production mode. The scalar Compton source is split equally among modes only as a stated diagnostic assumption.",
            "average_opacity": "Uses one third of the mode-summed opacity in the exponent; this is a comparison convention, not a replacement for the literal paper baseline.",
            "scope": "Only the 22--25 km path segment is attenuated. The B.1 source is held fixed, and all opacity inside 22 km is omitted from these escape factors.",
            "no_rescaling": "No empirical rescaling, production axial update, or Fig. 7 curve modification is performed.",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=MASS_DEFAULT)
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    parser.add_argument("--angle-order", type=int, default=24)
    parser.add_argument("--rate-order", type=int, default=48)
    parser.add_argument("--direct-order", type=int, default=512)
    args = parser.parse_args()
    result = run(
        args.profile, args.mass, args.nr, args.ne, args.energy_offset,
        args.angle_order, args.rate_order, args.direct_order,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "normalization_and_closure": result["normalization_and_closure"],
        "source": result["source"],
        "coupling_results": result["coupling_results"],
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
