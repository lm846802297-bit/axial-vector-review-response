"""Quantify how individual radial shells suppress the B.16 vector luminosity.

This is a diagnostic removal test, not a physical alternate supernova model:
the B.1 source is held fixed while selected B.2 opacity contributions are
removed from the escape exponent. It uses the published fixed-omega path
prescription and the same reconstructed SFHo-18.8 profile as the baseline.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import logsumexp

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, scalar_optical_depths,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, scalar_optical_depths,
    )
    from audit_b16_global_redshift import eq_b1_source_measure

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_shell_luminosity_sensitivity_10mev_2026-11-08.json"
SHELL_EDGES_KM = [0.0, 5.0, 8.0, 10.0, 12.0, 15.0, 16.5, 18.5, 20.0, 22.0, 25.0]


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def shell_columns_by_channel(
    source_radii, radial_grid, temperature, rates, mass, energies,
    radius_km=25.0, angular_order=16, path_order=32,
):
    """Return optical-depth columns indexed by channel and radial shell."""
    source_radii = np.asarray(source_radii, float)
    radial_grid = np.asarray(radial_grid, float)
    temperature = np.asarray(temperature, float)
    energies = np.asarray(energies, float)

    x = energies[None, :]/temperature[:, None]
    detailed_balance = np.expm1(np.minimum(x, 700.0))
    channel_keys = {
        "neutrino": "neutrino_production",
        "compton": "compton_production",
        "dimuon": "dimuon_production",
    }
    reduced = {
        name: detailed_balance*np.asarray(rates[key], float)
        for name, key in channel_keys.items()
    }
    reduced_sum = sum(reduced.values())
    total_reference = np.asarray(rates["reduced_absorption"], float)
    residual = float(np.max(
        np.abs(reduced_sum-total_reference)
        / np.maximum(np.abs(total_reference), 1.0e-300)
    ))

    labels = [
        f"{lo:g}-{hi:g} km"
        for lo, hi in zip(SHELL_EDGES_KM[:-1], SHELL_EDGES_KM[1:])
    ]
    n_source, n_energy = len(source_radii), len(energies)
    angles, angle_weights = leggauss(angular_order)
    angle_weights = angle_weights/2.0
    path_x, path_w = leggauss(path_order)
    path_w = path_w/2.0
    r = source_radii[:, None]

    columns = {
        channel: np.zeros((len(labels), n_source, angular_order, n_energy))
        for channel in channel_keys
    }

    for ia, cosine in enumerate(angles):
        smax = -cosine*r + np.sqrt(
            radius_km**2-r**2+r**2*cosine**2
        )
        s = smax*(1.0+path_x[None, :])/2.0
        position = np.sqrt(np.maximum(
            r**2+s**2+2.0*r*s*cosine, 0.0
        ))
        path_weights = smax*path_w[None, :]
        masks = [
            (position >= lo) &
            (position < hi if hi < radius_km else position <= hi)
            for lo, hi in zip(SHELL_EDGES_KM[:-1], SHELL_EDGES_KM[1:])
        ]
        flat_position = position.ravel()

        for ie, omega in enumerate(energies):
            velocity = float(np.sqrt(max(1.0-(mass/omega)**2, 0.0)))
            if velocity <= 0.0:
                continue
            for channel, reduced_grid in reduced.items():
                path_rate = np.interp(
                    flat_position, radial_grid, reduced_grid[:, ie]
                ).reshape(position.shape)
                for ish, mask in enumerate(masks):
                    columns[channel][ish, :, ia, ie] = (
                        np.sum(path_weights*path_rate*mask, axis=1)
                        * KM_TO_MEV_INV/velocity
                    )

    total_by_shell = sum(columns.values())
    total_columns = np.sum(total_by_shell, axis=0)
    direct_columns, direct_angles = scalar_optical_depths(
        source_radii, radial_grid, total_reference, mass, energies,
        radius_km, angular_order, path_order
    )
    angle_residual = float(np.max(np.abs(direct_angles-angle_weights)))
    column_residual = float(np.max(
        np.abs(total_columns-direct_columns)
        / np.maximum(np.abs(direct_columns), 1.0e-300)
    ))
    return {
        "shell_labels": labels,
        "angle_weights": angle_weights,
        "columns_by_channel": columns,
        "columns_by_shell": total_by_shell,
        "columns_total": total_columns,
        "direct_columns": direct_columns,
        "detailed_balance_channel_sum_relative_residual": residual,
        "angular_weight_relative_residual": angle_residual,
        "shell_sum_to_direct_column_max_relative_residual": column_residual,
    }


def log_escaped_integral(source, angle_weights, columns, coupling):
    """Return log of integral(source * angle_average(exp(-g^2 tau)))."""
    source = np.asarray(source, float)
    columns = np.asarray(columns, float)
    log_source = np.where(source > 0.0, np.log(source), -np.inf)
    log_angle = np.log(np.asarray(angle_weights, float))
    terms = (
        log_source[:, None, :]
        + log_angle[None, :, None]
        - coupling**2*columns
    )
    return float(logsumexp(terms))


def removal_diagnostic(source, angle_weights, total_columns, removed_columns, coupling):
    base = log_escaped_integral(source, angle_weights, total_columns, coupling)
    alternative = log_escaped_integral(
        source, angle_weights,
        np.maximum(total_columns-removed_columns, 0.0), coupling
    )
    delta = alternative-base
    return {
        "log10_luminosity_enhancement": float(delta/np.log(10.0)),
        "relative_luminosity_enhancement": (
            float(np.expm1(delta)) if delta < 700.0 else None
        ),
    }


def run_audit(
    profile_path, fig7_path, mass=10.0, radial_order=40, energy_order=100,
    angular_order=16, path_order=32, radius_km=25.0, energy_offset=1000.0,
):
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    key = str(float(mass))
    vertices = fig7["reference_vertices"][key]
    couplings = np.asarray(vertices["g"], float)
    reference_lum = np.asarray(vertices["luminosity_erg_s"], float)

    r, rw = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
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
    source_indices = np.searchsorted(radial_grid, r)
    source, source_measure = eq_b1_source_measure(
        r, rw, energies, profile["lapse"][source_indices], mass,
        rates["production"][source_indices]
    )

    shell_data = shell_columns_by_channel(
        r, radial_grid, profile["T"], rates, mass, energies,
        radius_km, angular_order, path_order
    )
    columns = shell_data["columns_total"]
    channel_columns = shell_data["columns_by_channel"]
    shell_columns = shell_data["columns_by_shell"]
    labels = shell_data["shell_labels"]
    angle_weights = shell_data["angle_weights"]

    source_log_norm = float(logsumexp(np.where(source > 0.0, np.log(source), -np.inf)))
    shell_mean_tau = {}
    for i, label in enumerate(labels):
        tau = np.einsum("rae,a->re", shell_columns[i], angle_weights)
        shell_mean_tau[label] = float(np.sum(source*tau)/np.exp(source_log_norm))

    channel_mean_tau = {}
    for channel, values in channel_columns.items():
        summed = np.sum(values, axis=0)
        tau = np.einsum("rae,a->re", summed, angle_weights)
        channel_mean_tau[channel] = float(np.sum(source*tau)/np.exp(source_log_norm))

    outer_indices = [
        i for i, label in enumerate(labels)
        if float(label.split("-")[0]) >= 15.0
    ]
    inner_indices = [i for i in range(len(labels)) if i not in outer_indices]
    outer_columns = np.sum(shell_columns[outer_indices], axis=0)
    inner_columns = np.sum(shell_columns[inner_indices], axis=0)
    outer_neutrino_columns = np.sum(
        channel_columns["neutrino"][outer_indices], axis=0
    )
    outer_compton_columns = np.sum(
        channel_columns["compton"][outer_indices], axis=0
    )
    all_neutrino_columns = np.sum(channel_columns["neutrino"], axis=0)
    all_compton_columns = np.sum(channel_columns["compton"], axis=0)

    # Pick representative couplings by reference peak, calculated peak,
    # weak-coupling endpoint, and strong-absorption endpoint.
    log_base = np.asarray([
        log_escaped_integral(source, angle_weights, columns, g)
        for g in couplings
    ])
    log_luminosity = 2.0*np.log(couplings)+log_base
    calculated_lum = np.exp(np.clip(log_luminosity, -745.0, 700.0))
    indices = {
        "weak_coupling": 0,
        "reference_luminosity_peak": int(np.argmax(reference_lum)),
        "calculated_luminosity_peak": int(np.argmax(log_luminosity)),
        "strong_absorption_endpoint": len(couplings)-1,
    }
    selected_indices = sorted(set(indices.values()))
    selected = []
    for idx in selected_indices:
        g = float(couplings[idx])
        row = {
            "index": int(idx),
            "g": g,
            "reference_luminosity_erg_s": float(reference_lum[idx]),
            "baseline_log10_luminosity_erg_s": float(
                (2.0*np.log(g)+log_base[idx])/np.log(10.0)
            ),
            "baseline_luminosity_erg_s": float(calculated_lum[idx]),
            "baseline_relative_difference_vs_fig7": float(
                calculated_lum[idx]/reference_lum[idx]-1.0
            ),
            "remove_each_shell": {},
        }
        for ish, label in enumerate(labels):
            row["remove_each_shell"][label] = removal_diagnostic(
                source, angle_weights, columns, shell_columns[ish], g
            )
        row["remove_outer_r_ge_15km"] = removal_diagnostic(
            source, angle_weights, columns, outer_columns, g
        )
        row["remove_inner_r_lt_15km"] = removal_diagnostic(
            source, angle_weights, columns, inner_columns, g
        )
        row["remove_all_neutrino_opacity"] = removal_diagnostic(
            source, angle_weights, columns, all_neutrino_columns, g
        )
        row["remove_all_compton_opacity"] = removal_diagnostic(
            source, angle_weights, columns, all_compton_columns, g
        )
        row["remove_outer_neutrino_opacity"] = removal_diagnostic(
            source, angle_weights, columns, outer_neutrino_columns, g
        )
        row["remove_outer_compton_opacity"] = removal_diagnostic(
            source, angle_weights, columns, outer_compton_columns, g
        )
        selected.append(row)

    return {
        "title": "B.16 fixed-omega radial-shell opacity removal sensitivity",
        "mass_MeV": mass,
        "scope": [
            "Pure-vector B.14--B.16 benchmark at m=10 MeV.",
            "The B.1 source term is held fixed; only selected B.2 opacity terms are removed from the escape exponent.",
            "This is a diagnostic attribution, not a physical alternate supernova model or a new exclusion curve.",
            "No coupling, source, opacity, or final luminosity rescaling.",
        ],
        "configuration": {
            "radial_order": radial_order,
            "energy_order": energy_order,
            "angular_order": angular_order,
            "path_order": path_order,
            "radius_km": radius_km,
            "energy_offset_MeV": energy_offset,
            "shell_edges_km": SHELL_EDGES_KM,
        },
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "identity": "reconstructed public-figure SFHo-18.8, t_pb=1 s profile; not original raw Garching table",
        },
        "fig7_reference": {
            "path": str(fig7_path),
            "sha256": sha256(fig7_path),
            "pdf_sha256": fig7.get("pdf_sha256"),
            "points": len(couplings),
        },
        "eq_b1_source_measure": source_measure,
        "mean_optical_depth_by_shell": shell_mean_tau,
        "mean_optical_depth_by_channel": channel_mean_tau,
        "outer_r_ge_15km_fraction_of_source_weighted_mean_tau": (
            sum(shell_mean_tau[labels[i]] for i in outer_indices)
            / sum(shell_mean_tau.values())
        ),
        "column_closure": {
            "detailed_balance_channel_sum_max_relative_residual": (
                shell_data["detailed_balance_channel_sum_relative_residual"]
            ),
            "angular_weight_max_residual": shell_data["angular_weight_relative_residual"],
            "radial_shell_sum_to_direct_column_max_relative_residual": (
                shell_data["shell_sum_to_direct_column_max_relative_residual"]
            ),
        },
        "representative_coupling_indices": indices,
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
    parser.add_argument("--na", type=int, default=16)
    parser.add_argument("--ns", type=int, default=32)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()
    result = run_audit(
        args.profile, args.fig7, args.mass, args.nr, args.ne,
        args.na, args.ns, args.radius, args.energy_offset
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "mean_optical_depth_by_shell": result["mean_optical_depth_by_shell"],
        "mean_optical_depth_by_channel": result["mean_optical_depth_by_channel"],
        "outer_tau_fraction": result["outer_r_ge_15km_fraction_of_source_weighted_mean_tau"],
        "column_closure": result["column_closure"],
        "representative_couplings": result["representative_couplings"],
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
