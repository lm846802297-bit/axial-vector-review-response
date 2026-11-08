"""Audit the reconstructed 22--25 km profile and its B.2 opacity interpolation.

The audit holds the B.1 source fixed and compares:
  (i) the existing 40-node composite radial interpolation,
  (ii) direct interpolation of the archived 0.05 km public-figure profile.
It evaluates the outer-shell optical depth with the same fixed-omega B.2
prescription and isolates the effect on the source-weighted escape factor.

This is a profile/interpolation diagnostic, not a replacement SN model.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, fermi_pair_average,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, fermi_pair_average,
    )
    from audit_b16_global_redshift import eq_b1_source_measure

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "outputs" / "b16_outer_profile_inputs_10mev_2026-11-08.json"
SHELL_INNER_KM = 22.0
SHELL_OUTER_KM = 25.0


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def weighted_quantile(values, weights, quantile):
    values = np.asarray(values, float).ravel()
    weights = np.asarray(weights, float).ravel()
    valid = np.isfinite(values) & np.isfinite(weights) & (weights > 0.0)
    if not np.any(valid):
        return None
    values, weights = values[valid], weights[valid]
    order = np.argsort(values)
    values, weights = values[order], weights[order]
    cumulative = np.cumsum(weights)
    index = min(int(np.searchsorted(cumulative, quantile*cumulative[-1])), len(values)-1)
    return float(values[index])


def interpolation_summary(raw_r, raw_values, coarse_r, coarse_values, sample_r):
    truth = np.interp(sample_r, raw_r, raw_values)
    approx = np.interp(sample_r, coarse_r, coarse_values)
    delta = approx-truth
    scale = np.maximum(np.abs(truth), 1.0e-30)
    positive = np.abs(truth) > 1.0e-12
    return {
        "max_absolute_error": float(np.max(np.abs(delta))),
        "rms_absolute_error": float(np.sqrt(np.mean(delta**2))),
        "max_relative_error_where_abs_truth_gt_1e-12": (
            float(np.max(np.abs(delta[positive])/scale[positive]))
            if np.any(positive) else None
        ),
        "max_absolute_error_radius_km": float(sample_r[int(np.argmax(np.abs(delta)))]),
        "truth_min": float(np.min(truth)),
        "truth_max": float(np.max(truth)),
    }


def radial_shell_columns(
    source_radii, energies, radial_grid, reduced_rate_grid,
    angular_order=64, radial_order=64,
    shell_inner=SHELL_INNER_KM, shell_outer=SHELL_OUTER_KM,
):
    """Integrate B.2 optical-depth columns over one radial shell.

    For source radii below shell_inner, the path crosses the full shell once.
    Using r as the integration variable avoids a discontinuous shell mask in s.
    """
    source_radii = np.asarray(source_radii, float)
    energies = np.asarray(energies, float)
    radial_grid = np.asarray(radial_grid, float)
    reduced_rate_grid = np.asarray(reduced_rate_grid, float)
    if np.any(source_radii >= shell_inner):
        raise ValueError("This shell routine expects all source radii below 22 km")

    angles, angle_weights = leggauss(angular_order)
    angle_weights = angle_weights/2.0
    x, w = leggauss(radial_order)
    path_r = (shell_inner+shell_outer)/2.0 + (shell_outer-shell_inner)*x/2.0
    path_w = (shell_outer-shell_inner)*w/2.0

    # Interpolate the local reduced absorption rate at the radial quadrature nodes.
    path_rate = np.column_stack([
        np.interp(path_r, radial_grid, reduced_rate_grid[:, ie])
        for ie in range(len(energies))
    ])
    velocity = np.sqrt(np.maximum(1.0-(10.0/energies)**2, 0.0))
    columns = np.zeros((len(source_radii), len(angles), len(energies)))

    for ir, r0 in enumerate(source_radii):
        for ia, cosine in enumerate(angles):
            impact = r0*np.sqrt(max(1.0-cosine*cosine, 0.0))
            ds_dr = path_r/np.sqrt(path_r**2-impact**2)
            columns[ir, ia, :] = (
                np.sum(path_w[:, None]*ds_dr[:, None]*path_rate, axis=0)
                * KM_TO_MEV_INV/velocity
            )
    return columns, angles, angle_weights


def escape_factor(source, angle_weights, columns, coupling):
    weights = source[:, None, :]*angle_weights[None, :, None]
    denominator = float(np.sum(weights))
    numerator = float(np.sum(weights*np.exp(-coupling**2*columns)))
    return numerator/denominator if denominator > 0.0 else 0.0


def run(
    profile_path=DEFAULT_PROFILE, mass=10.0, radial_order=40,
    energy_order=100, energy_offset=1000.0, angular_order=64,
    radial_path_order=64,
):
    raw = np.genfromtxt(profile_path, delimiter=",", names=True)
    raw_r = np.asarray(raw["r_km"], float)
    outer_mask = (raw_r >= SHELL_INNER_KM) & (raw_r <= SHELL_OUTER_KM)
    outer = {name: np.asarray(raw[name][outer_mask], float)
             for name in ("r_km", "T_MeV", "mu_mu_MeV", "mu_numu_MeV", "lapse")}
    sample_r = outer["r_km"]
    if len(sample_r) < 20 or not np.isclose(sample_r[0], SHELL_INNER_KM) or not np.isclose(sample_r[-1], SHELL_OUTER_KM):
        raise ValueError("Expected the archived 0.05 km profile to cover 22--25 km")

    radius, radial_weights = radial_rule(SHELL_OUTER_KM, radial_order)
    radial_grid = np.unique(np.r_[0.0, radius, SHELL_OUTER_KM])
    profile = load_profile(profile_path, radial_grid)

    energies = mass+np.geomspace(
        max(mass*1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass/profile["lapse"]])
    energies = energies[energies > mass*(1.0+1.0e-10)]
    energies.sort()

    rates = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    source_indices = np.searchsorted(radial_grid, radius)
    source, source_meta = eq_b1_source_measure(
        radius, radial_weights, energies, profile["lapse"][source_indices],
        mass, rates["production"][source_indices]
    )

    # Recompute local rates on the original 0.05 km nodes in the outer shell.
    dense_rates = local_rates(
        mass, energies[None, :], outer["T_MeV"][:, None],
        outer["mu_numu_MeV"][:, None], outer["mu_mu_MeV"][:, None]
    )

    # Compare raw profile values with the profile reconstructed on the current
    # composite Gauss grid and then linearly interpolated along a path.
    profile_fields = {}
    for field, raw_key, profile_key in (
        ("temperature", "T_MeV", "T"),
        ("muon_chemical_potential", "mu_mu_MeV", "mu_mu"),
        ("muon_neutrino_chemical_potential", "mu_numu_MeV", "mu_numu"),
        ("lapse", "lapse", "lapse"),
    ):
        profile_fields[field] = interpolation_summary(
            outer["r_km"], outer[raw_key],
            radial_grid, profile[profile_key], sample_r
        )

    # Compare the nonlinear local opacity after rate evaluation, not just the
    # primitive thermodynamic variables.
    coarse_reduced = np.asarray(rates["reduced_absorption"], float)
    dense_reduced = np.asarray(dense_rates["reduced_absorption"], float)
    coarse_nu = np.asarray(rates["neutrino_production"], float)
    dense_nu = np.asarray(dense_rates["neutrino_production"], float)
    coarse_compton = np.asarray(rates["compton_production"], float)
    dense_compton = np.asarray(dense_rates["compton_production"], float)
    x_coarse = energies[None, :]/profile["T"][:, None]
    x_dense = energies[None, :]/outer["T_MeV"][:, None]
    coarse_reduced_nu = np.expm1(np.minimum(x_coarse, 700.0))*coarse_nu
    dense_reduced_nu = np.expm1(np.minimum(x_dense, 700.0))*dense_nu
    coarse_reduced_compton = np.expm1(np.minimum(x_coarse, 700.0))*coarse_compton
    dense_reduced_compton = np.expm1(np.minimum(x_dense, 700.0))*dense_compton

    path_r = np.linspace(SHELL_INNER_KM, SHELL_OUTER_KM, 3001)
    def compare_rate(coarse, dense):
        dense_at_sample = np.column_stack([
            np.interp(path_r, outer["r_km"], dense[:, ie])
            for ie in range(len(energies))
        ])
        coarse_at_sample = np.column_stack([
            np.interp(path_r, radial_grid, coarse[:, ie])
            for ie in range(len(energies))
        ])
        valid = dense_at_sample > np.max(dense_at_sample)*1.0e-12
        rel = np.zeros_like(dense_at_sample)
        rel[valid] = np.abs(coarse_at_sample[valid]-dense_at_sample[valid])/dense_at_sample[valid]
        return {
            "max_relative_error_above_1e-12_of_peak": float(np.max(rel)),
            "rms_relative_error_above_1e-12_of_peak": float(np.sqrt(np.mean(rel[valid]**2))) if np.any(valid) else None,
            "peak_dense_rate": float(np.max(dense_at_sample)),
            "peak_radius_km": float(path_r[np.unravel_index(np.argmax(dense_at_sample), dense_at_sample.shape)[0]]),
        }

    rate_interpolation = {
        "total_reduced_absorption": compare_rate(coarse_reduced, dense_reduced),
        "neutrino_reduced_absorption": compare_rate(coarse_reduced_nu, dense_reduced_nu),
        "compton_reduced_absorption": compare_rate(coarse_reduced_compton, dense_reduced_compton),
        "compton_to_neutrino_peak_rate_ratio": float(
            np.max(dense_reduced_compton)/np.max(dense_reduced_nu)
        ),
    }

    # The B.1 source weights are held fixed. Only the opacity profile in 22--25
    # km changes. Use source points from the dominant 8--15 km production region.
    source_mask = (radius >= 8.0) & (radius <= 15.0)
    selected_r = radius[source_mask]
    selected_source = source[source_mask]
    coarse_outer_columns, angles, angle_weights = radial_shell_columns(
        selected_r, energies, radial_grid, coarse_reduced,
        angular_order, radial_path_order
    )
    dense_outer_columns, _, _ = radial_shell_columns(
        selected_r, energies, outer["r_km"], dense_reduced,
        angular_order, radial_path_order
    )
    rel_columns = np.abs(dense_outer_columns-coarse_outer_columns)/np.maximum(
        dense_outer_columns, 1.0e-300
    )
    opacity_weights = selected_source[:, None, :]*angle_weights[None, :, None]
    mean_tau_coarse = float(np.sum(opacity_weights*coarse_outer_columns)/np.sum(opacity_weights))
    mean_tau_dense = float(np.sum(opacity_weights*dense_outer_columns)/np.sum(opacity_weights))
    weighted_rel_mean = float(np.sum(opacity_weights*rel_columns)/np.sum(opacity_weights))

    shell_summaries = []
    for lo, hi in ((8.0,10.0),(10.0,12.0),(12.0,15.0)):
        mask = (selected_r >= lo) & (selected_r < hi if hi < 15.0 else selected_r <= hi)
        wgt = opacity_weights[mask]
        shell_summaries.append({
            "emission_shell_km": [lo,hi],
            "source_fraction_within_selected_8_15km": float(np.sum(selected_source[mask])/np.sum(selected_source)),
            "coarse_source_weighted_mean_tau_per_g2": float(np.sum(wgt*coarse_outer_columns[mask])/np.sum(wgt)),
            "dense_source_weighted_mean_tau_per_g2": float(np.sum(wgt*dense_outer_columns[mask])/np.sum(wgt)),
            "relative_change_in_mean_tau": float(
                np.sum(wgt*dense_outer_columns[mask])/np.sum(wgt*coarse_outer_columns[mask])-1.0
            ),
            "weighted_95th_percentile_abs_pointwise_tau_change": weighted_quantile(
                rel_columns[mask], wgt, 0.95
            ),
        })

    couplings = {
        "fig7_peak": 1.1341108687336194e-8,
        "strong_endpoint": 4.171689650228597e-8,
    }
    escape_comparison = {}
    for label, coupling in couplings.items():
        p_coarse = escape_factor(selected_source, angle_weights, coarse_outer_columns, coupling)
        p_dense = escape_factor(selected_source, angle_weights, dense_outer_columns, coupling)
        escape_comparison[label] = {
            "g": coupling,
            "outer_shell_escape_factor_coarse_profile": p_coarse,
            "outer_shell_escape_factor_dense_profile": p_dense,
            "relative_change_dense_vs_coarse": p_dense/p_coarse-1.0,
        }

    # Bound the figure-floor convention mu_nu_mu=0 outside the plotted branch:
    # test |mu_nu_mu|=1 MeV throughout 22--25 km, keeping all other inputs fixed.
    omega = energies[None, :]
    temp = outer["T_MeV"][:, None]
    v = np.sqrt(np.maximum(1.0-(mass/energies)**2, 0.0))[None, :]
    i_tau = fermi_pair_average(np.zeros_like(temp), omega, temp, v)
    i_mu_floor = fermi_pair_average(np.ones_like(temp), omega, temp, v)
    nu_floor_prod = mass**2/(8.0*np.pi*omega)*(i_mu_floor+i_tau)
    floor_reduced = (
        np.expm1(np.minimum(omega/temp,700.0))*nu_floor_prod
        + dense_reduced_compton
    )
    floor_columns, _, _ = radial_shell_columns(
        selected_r, energies, outer["r_km"], floor_reduced,
        angular_order, radial_path_order
    )
    floor_sensitivity = {}
    for label, coupling in couplings.items():
        p_zero = escape_factor(selected_source, angle_weights, dense_outer_columns, coupling)
        p_floor = escape_factor(selected_source, angle_weights, floor_columns, coupling)
        floor_sensitivity[label] = {
            "g": coupling,
            "escape_factor_mu_numu_zero": p_zero,
            "escape_factor_abs_mu_numu_1MeV": p_floor,
            "relative_change": p_floor/p_zero-1.0,
        }

    # B.1 source fraction in the outermost region and the lapse's role.
    source_fraction_by_radius = {
        "r_ge_22km": float(np.sum(source[radius >= 22.0])/np.sum(source)),
        "r_ge_24km": float(np.sum(source[radius >= 24.0])/np.sum(source)),
        "r_8_to_15km": float(np.sum(source[source_mask])/np.sum(source)),
    }
    outer_nodes = radial_grid[radial_grid >= SHELL_INNER_KM]
    return {
        "title": "B.16 outer-profile input and interpolation audit",
        "mass_MeV": mass,
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "raw_radial_spacing_km": float(np.min(np.diff(raw_r))),
            "raw_outer_node_count": int(len(sample_r)),
            "raw_outer_radius_range_km": [float(sample_r[0]),float(sample_r[-1])],
            "radial_order": radial_order,
            "composite_opacity_grid_outer_nodes_km": outer_nodes.tolist(),
            "composite_opacity_grid_outer_node_count": int(len(outer_nodes)),
            "composite_outer_max_spacing_km": float(np.max(np.diff(outer_nodes))),
            "field_interpolation_errors": profile_fields,
            "mu_mu_max_outer_MeV": float(np.max(outer["mu_mu_MeV"])),
            "mu_numu_max_abs_outer_MeV": float(np.max(np.abs(outer["mu_numu_MeV"]))),
            "temperature_range_outer_MeV": [float(np.min(outer["T_MeV"])),float(np.max(outer["T_MeV"]))],
            "lapse_range_outer": [float(np.min(outer["lapse"])),float(np.max(outer["lapse"]))],
            "lapse_source": "Ferreira figure through r=23.9998 km; matched Schwarzschild continuation from there to 25 km.",
            "temperature_source": "Caputo public-figure polyline, including encoded vertices beyond the visible plotting frame.",
            "mu_numu_source": "Caputo public-figure branches; zero where |mu_numu| is below the plotted 1 MeV floor or outside the plotted branches.",
            "mu_tau_assumption": "mu_nu_tau=0, as stated in the published Blinov et al. Appendix B because the SN simulations do not provide this profile.",
        },
        "equation_roles": {
            "B2_fixed_omega": "The opacity integral uses T(r') and chemical potentials at r', with omega held fixed along the path.",
            "lapse": "The lapse does not appear in the fixed-omega B.2 path opacity. It enters the B.1 source weight at the emission radius and the local escape-energy lower bound.",
            "outer_boundary": "The path ends at R_max=R_nu=25 km; no opacity beyond 25 km is included.",
        },
        "source_fraction_by_radius": source_fraction_by_radius,
        "local_reduced_absorption_interpolation": rate_interpolation,
        "outer_shell_tau_for_8_15km_sources": {
            "integration": "r-coordinate integral over 22--25 km with ds/dr=r/sqrt(r^2-b^2), 64-point Gauss rule; fixed omega.",
            "angular_order": angular_order,
            "radial_path_order": radial_path_order,
            "source_weighted_mean_tau_per_g2_coarse": mean_tau_coarse,
            "source_weighted_mean_tau_per_g2_dense": mean_tau_dense,
            "relative_change_source_weighted_mean_tau": mean_tau_dense/mean_tau_coarse-1.0,
            "source_weighted_mean_absolute_pointwise_relative_tau_change": weighted_rel_mean,
            "weighted_95th_percentile_abs_pointwise_tau_change": weighted_quantile(rel_columns,opacity_weights,0.95),
            "max_abs_pointwise_relative_tau_change": float(np.max(rel_columns)),
            "by_emission_shell": shell_summaries,
            "outer_shell_escape_factor": escape_comparison,
        },
        "mu_numu_plot_floor_sensitivity": {
            "test": "Set |mu_nu_mu|=1 MeV throughout 22--25 km, versus the baseline zero continuation; keep mu_nu_tau=0.",
            "by_coupling": floor_sensitivity,
        },
        "eq_b1_source_measure": source_meta,
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    parser.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    parser.add_argument("--mass",type=float,default=10.0)
    parser.add_argument("--nr",type=int,default=40)
    parser.add_argument("--ne",type=int,default=100)
    parser.add_argument("--energy-offset",type=float,default=1000.0)
    parser.add_argument("--angular-order",type=int,default=64)
    parser.add_argument("--radial-path-order",type=int,default=64)
    args=parser.parse_args()
    result=run(
        args.profile,args.mass,args.nr,args.ne,args.energy_offset,
        args.angular_order,args.radial_path_order
    )
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({
        "profile":result["profile"],
        "source_fraction_by_radius":result["source_fraction_by_radius"],
        "local_reduced_absorption_interpolation":result["local_reduced_absorption_interpolation"],
        "outer_shell_tau_for_8_15km_sources":result["outer_shell_tau_for_8_15km_sources"],
        "mu_numu_plot_floor_sensitivity":result["mu_numu_plot_floor_sensitivity"],
    },indent=2))
    print(f"Saved {args.output}")


if __name__=="__main__":
    main()
