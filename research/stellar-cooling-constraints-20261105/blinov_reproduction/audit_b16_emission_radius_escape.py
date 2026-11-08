"""Map the B.1 source radius to B.2 escape probability and path-opacity shells.

The calculation is the fixed-omega scalar Appendix-B baseline at m_V=10 MeV.
It distinguishes (i) where the vector is produced, (ii) where its optical depth
accumulates along the outgoing chord, and (iii) which emission radii survive
the angular/energy-averaged escape factor. No source or opacity rescaling.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

try:
    from .reference import (
        DEFAULT_PROFILE, radial_rule, load_profile, local_rates,
        scalar_optical_depths,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_neutrino_flavour_opacity import flavour_rate_arrays
    from .audit_b16_shell_luminosity_sensitivity import (
        shell_columns_by_channel, SHELL_EDGES_KM,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE, radial_rule, load_profile, local_rates,
        scalar_optical_depths,
    )
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_neutrino_flavour_opacity import flavour_rate_arrays
    from audit_b16_shell_luminosity_sensitivity import (
        shell_columns_by_channel, SHELL_EDGES_KM,
    )

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_emission_radius_escape_10mev_2026-11-08.json"
CHANNELS = ("nu_mu", "nu_tau", "compton", "dimuon")


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def shell_labels(edges):
    return [f"{lo:g}-{hi:g} km" for lo, hi in zip(edges[:-1], edges[1:])]


def shell_masks(radius, edges):
    radius = np.asarray(radius, float)
    masks = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        masks.append(
            (radius >= lo) &
            (radius < hi if hi < edges[-1] else radius <= hi)
        )
    return masks


def weighted_quantile(values, weights, quantile):
    values, weights = np.asarray(values, float), np.asarray(weights, float)
    valid = np.isfinite(values) & np.isfinite(weights) & (weights > 0.0)
    if not np.any(valid):
        return None
    values, weights = values[valid], weights[valid]
    order = np.argsort(values)
    values, weights = values[order], weights[order]
    cumulative = np.cumsum(weights)
    index = min(
        int(np.searchsorted(cumulative, quantile*cumulative[-1])),
        len(values)-1
    )
    return float(values[index])


def source_radial_summary(radius, source, edges, labels=None):
    """Return source fractions and radial moments; source already includes dr."""
    radius = np.asarray(radius, float)
    source = np.asarray(source, float)
    radial_weight = np.sum(source, axis=1)
    total = float(np.sum(radial_weight))
    if total <= 0.0:
        raise ValueError("Source measure must be positive")
    labels = labels or shell_labels(edges)
    masks = shell_masks(radius, edges)
    shells = []
    for label, mask in zip(labels, masks):
        weight = float(np.sum(radial_weight[mask]))
        shells.append({
            "shell": label,
            "source_weight": weight,
            "source_fraction": weight/total,
        })
    return {
        "total_source_weight": total,
        "mean_emission_radius_km": float(np.sum(radius*radial_weight)/total),
        "median_emission_radius_km": weighted_quantile(radius, radial_weight, 0.5),
        "p90_emission_radius_km": weighted_quantile(radius, radial_weight, 0.9),
        "shells": shells,
    }


def emission_shell_escape_summary(radius, source, escape_average, edges, labels=None):
    """Source-weighted P_escape and emergent luminosity fraction by emission shell."""
    radius = np.asarray(radius, float)
    source = np.asarray(source, float)
    escape_average = np.asarray(escape_average, float)
    if source.shape != escape_average.shape:
        raise ValueError("source and escape_average must have identical shape")
    if np.any((escape_average < -1e-13) | (escape_average > 1.0+1e-13)):
        raise ValueError("Escape probabilities must lie in [0,1]")
    labels = labels or shell_labels(edges)
    masks = shell_masks(radius, edges)
    total_source = float(np.sum(source))
    total_escaped = float(np.sum(source*escape_average))
    rows = []
    for label, mask in zip(labels, masks):
        thin = float(np.sum(source[mask]))
        escaped = float(np.sum(source[mask]*escape_average[mask]))
        rows.append({
            "emission_shell": label,
            "thin_source_fraction": thin/total_source if total_source else 0.0,
            "mean_escape_probability": escaped/thin if thin else None,
            "escaped_luminosity_fraction": (
                escaped/total_escaped if total_escaped else 0.0
            ),
        })
    return rows


def emission_absorption_tau_matrix(
    radius, source, angle_weights, columns_by_absorption_shell, edges, labels=None
):
    """Source-weighted mean tau matrix: rows=emission shells, columns=path shells."""
    radius = np.asarray(radius, float)
    source = np.asarray(source, float)
    angle_weights = np.asarray(angle_weights, float)
    columns = np.asarray(columns_by_absorption_shell, float)
    if columns.ndim != 4:
        raise ValueError("columns must have shape (abs_shell, source_r, angle, energy)")
    if columns.shape[1] != source.shape[0] or columns.shape[2] != len(angle_weights):
        raise ValueError("columns shape is inconsistent with source/angle weights")
    if columns.shape[3] != source.shape[1]:
        raise ValueError("columns energy dimension does not match source")
    labels = labels or shell_labels(edges)
    masks = shell_masks(radius, edges)
    angle_average = np.einsum("srae,a->sre", columns, angle_weights)
    matrix = []
    for emission_label, emission_mask in zip(labels, masks):
        source_weight = float(np.sum(source[emission_mask]))
        absorption = []
        for absorption_index, absorption_label in enumerate(labels):
            numerator = float(np.sum(
                source[emission_mask]*angle_average[
                    absorption_index, emission_mask, :
                ]
            ))
            absorption.append({
                "absorption_shell": absorption_label,
                "mean_tau_per_g2": numerator/source_weight if source_weight else None,
            })
        matrix.append({
            "emission_shell": emission_label,
            "source_weight": source_weight,
            "mean_tau_by_absorption_shell": absorption,
            "mean_total_tau_per_g2": float(sum(
                x["mean_tau_per_g2"] or 0.0 for x in absorption
            )),
        })
    return matrix


def _make_source_by_channel(radius, radial_weights, energies, profile, mass, rates):
    source_indices = np.searchsorted(
        np.unique(np.r_[0.0, radius, 25.0]), radius
    )
    # The caller passes the already interpolated source-profile arrays below;
    # this helper is retained for direct tests and requires no hidden state.
    raise NotImplementedError("Use build_source_channels with the supplied radial grid")


def build_source_channels(
    radius, radial_weights, energies, lapse_at_source, source_productions, mass
):
    """Apply the identical Eq. (B.1) measure to each source production channel."""
    result = {}
    for channel, production in source_productions.items():
        source, _ = eq_b1_source_measure(
            radius, radial_weights, energies, lapse_at_source, mass, production
        )
        result[channel] = source
    return result


def run_audit(
    profile_path=DEFAULT_PROFILE, fig7_path=DEFAULT_FIG7,
    mass=10.0, radial_order=40, energy_order=100,
    angular_order=16, path_order=32, radius_km=25.0, energy_offset=1000.0,
):
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
    couplings = np.asarray(vertices["g"], float)
    reference_luminosities = np.asarray(vertices["luminosity_erg_s"], float)

    radius, radial_weights = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, radius, radius_km])
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
    lapse_source = profile["lapse"][source_indices]
    source_total, source_measure = eq_b1_source_measure(
        radius, radial_weights, energies, lapse_source, mass,
        rates["production"][source_indices]
    )

    nu_mu_prod, nu_tau_prod = flavour_rate_arrays(mass, energies, profile)
    source_productions = {
        "nu_mu": nu_mu_prod[source_indices],
        "nu_tau": nu_tau_prod[source_indices],
        "compton": rates["compton_production"][source_indices],
        "dimuon": rates["dimuon_production"][source_indices],
    }
    source_by_channel = build_source_channels(
        radius, radial_weights, energies, lapse_source,
        source_productions, mass
    )
    source_channel_sum = sum(source_by_channel.values())
    source_closure = float(np.max(
        np.abs(source_channel_sum-source_total)
        / np.maximum(np.abs(source_total), 1e-300)
    ))

    shell_data = shell_columns_by_channel(
        radius, radial_grid, profile["T"], rates, mass, energies,
        radius_km, angular_order, path_order
    )
    angle_weights = shell_data["angle_weights"]
    total_columns = shell_data["columns_total"]
    direct_columns, direct_angles = scalar_optical_depths(
        radius, radial_grid, rates["reduced_absorption"], mass,
        energies, radius_km, angular_order, path_order
    )
    column_closure = float(np.max(
        np.abs(total_columns-direct_columns)
        / np.maximum(np.abs(direct_columns), 1e-300)
    ))
    angle_closure = float(np.max(np.abs(angle_weights-direct_angles)))

    # Sum channel opacity contributions within each traversed radial shell.
    columns_by_absorption_shell = sum(
        shell_data["columns_by_channel"].values()
    )
    total_shell_sum = np.sum(columns_by_absorption_shell, axis=0)
    shell_column_closure = float(np.max(
        np.abs(total_shell_sum-total_columns)
        / np.maximum(np.abs(total_columns), 1e-300)
    ))

    edges = [x for x in SHELL_EDGES_KM if x <= radius_km]
    if edges[-1] < radius_km:
        edges.append(radius_km)
    labels = shell_labels(edges)
    source_radial = source_radial_summary(radius, source_total, edges, labels)
    source_by_channel_radial = {
        channel: source_radial_summary(radius, source, edges, labels)
        for channel, source in source_by_channel.items()
    }

    # Source-weighted mean tau as a function of both emission and absorption shell.
    tau_matrix_total = emission_absorption_tau_matrix(
        radius, source_total, angle_weights,
        columns_by_absorption_shell, edges, labels
    )
    tau_matrix_by_channel = {}
    for channel, channel_columns in shell_data["columns_by_channel"].items():
        tau_matrix_by_channel[channel] = emission_absorption_tau_matrix(
            radius, source_total, angle_weights,
            channel_columns, edges, labels
        )

    log_luminosities = []
    for g in couplings:
        escape = np.exp(-g*g*total_columns)
        escape_average = np.einsum("rae,a->re", escape, angle_weights)
        log_luminosities.append(
            np.log(g*g)+np.log(np.sum(source_total*escape_average))
        )
    peak_index = int(np.argmax(log_luminosities))
    reference_peak_index = int(np.argmax(reference_luminosities))
    selected_indices = {
        "weak_coupling": 0,
        "calculated_luminosity_peak": peak_index,
        "reference_luminosity_peak": reference_peak_index,
        "strong_absorption_endpoint": len(couplings)-1,
    }

    selected = []
    for idx in sorted(set(selected_indices.values())):
        g = float(couplings[idx])
        escape = np.exp(-g*g*total_columns)
        escape_average = np.einsum("rae,a->re", escape, angle_weights)
        escaped_source = source_total*escape_average
        thin_luminosity = float(g*g*np.sum(source_total))
        escaped_luminosity = float(g*g*np.sum(escaped_source))
        by_emission_shell = emission_shell_escape_summary(
            radius, source_total, escape_average, edges, labels
        )

        by_channel = {}
        for channel, channel_source in source_by_channel.items():
            thin = float(g*g*np.sum(channel_source))
            escaped = float(g*g*np.sum(channel_source*escape_average))
            by_channel[channel] = {
                "thin_source_luminosity_erg_s": thin,
                "escaped_luminosity_erg_s": escaped,
                "escape_fraction": escaped/thin if thin else 0.0,
                "fraction_of_total_thin_source": (
                    thin/thin_luminosity if thin_luminosity else 0.0
                ),
                "fraction_of_total_escaped_luminosity": (
                    escaped/escaped_luminosity if escaped_luminosity else 0.0
                ),
                "emission_shells": emission_shell_escape_summary(
                    radius, channel_source, escape_average, edges, labels
                ),
            }

        mean_tau_by_emission_shell = []
        angle_average_total_tau = np.einsum(
            "rae,a->re", total_columns, angle_weights
        )
        for label, mask in zip(labels, shell_masks(radius, edges)):
            w = float(np.sum(source_total[mask]))
            mean_tau = float(
                np.sum(source_total[mask]*angle_average_total_tau[mask])/w
            ) if w else None
            mean_tau_by_emission_shell.append({
                "emission_shell": label,
                "source_fraction": (
                    float(np.sum(source_total[mask])/np.sum(source_total))
                ),
                "mean_total_tau_per_g2": mean_tau,
            })

        selected.append({
            "index": idx,
            "g": g,
            "reference_luminosity_erg_s": float(reference_luminosities[idx]),
            "calculated_luminosity_erg_s": escaped_luminosity,
            "relative_difference_vs_fig7": (
                escaped_luminosity/reference_luminosities[idx]-1.0
            ),
            "optically_thin_luminosity_erg_s": thin_luminosity,
            "global_escape_fraction": (
                escaped_luminosity/thin_luminosity if thin_luminosity else 0.0
            ),
            "source_weighted_mean_escape_probability": (
                escaped_luminosity/thin_luminosity if thin_luminosity else 0.0
            ),
            "emission_shell_escape": by_emission_shell,
            "mean_tau_by_emission_shell": mean_tau_by_emission_shell,
            "source_channels": by_channel,
        })

    # Verify the source-weighted mean of the emission/absorption matrix
    # reconstructs the direct source-weighted mean tau.
    source_total_weight = float(np.sum(source_total))
    matrix_weighted_mean_tau = float(sum(
        row["source_weight"]*row["mean_total_tau_per_g2"]
        for row in tau_matrix_total
    )/source_total_weight)
    direct_mean_tau = float(np.sum(
        source_total*np.einsum("rae,a->re", total_columns, angle_weights)
    )/source_total_weight)

    return {
        "title": "B.1 source-emission radius and B.2 escape/absorption radial weights",
        "mass_MeV": mass,
        "scope": [
            "Literal fixed-omega scalar Appendix-B B.1/B.2 benchmark.",
            "The source distribution includes the B.1 lapse-squared factor and local escape-energy lower bound.",
            "The escape probability is angle averaged after exponentiating the full chord optical depth.",
            "The opacity matrix separates the shell where a vector is emitted from the shell where it accumulates optical depth.",
            "No fitted scaling, modified background, source feedback, or axial-production replacement.",
        ],
        "configuration": {
            "radial_order": radial_order,
            "energy_order": energy_order,
            "angular_order": angular_order,
            "path_order": path_order,
            "radius_km": radius_km,
            "energy_offset_MeV": energy_offset,
            "emission_and_absorption_shells_km": labels,
        },
        "provenance": {
            "profile_path": str(profile_path),
            "profile_sha256": sha256(profile_path),
            "fig7_reference_path": str(fig7_path),
            "fig7_reference_sha256": sha256(fig7_path),
            "fig7_source_pdf_sha256": fig7.get("pdf_sha256"),
        },
        "eq_b1_source_measure": source_measure,
        "internal_closure": {
            "source_channel_sum_max_relative_residual": source_closure,
            "shell_columns_vs_direct_chord_max_relative_residual": column_closure,
            "angle_weight_max_absolute_residual": angle_closure,
            "absorption_shell_sum_vs_total_column_max_relative_residual": shell_column_closure,
            "emission_absorption_matrix_weighted_mean_tau": matrix_weighted_mean_tau,
            "direct_source_weighted_mean_tau": direct_mean_tau,
            "mean_tau_matrix_relative_residual": (
                matrix_weighted_mean_tau/direct_mean_tau-1.0
            ),
        },
        "optically_thin_source_radial_distribution": source_radial,
        "optically_thin_source_radial_distribution_by_channel": source_by_channel_radial,
        "source_weighted_mean_tau_by_emission_and_absorption_shell": {
            "total": tau_matrix_total,
            "neutrino": tau_matrix_by_channel["neutrino"],
            "compton": tau_matrix_by_channel["compton"],
            "dimuon": tau_matrix_by_channel["dimuon"],
        },
        "representative_coupling_indices": selected_indices,
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
        "closure": result["internal_closure"],
        "source_radial": result["optically_thin_source_radial_distribution"],
        "source_radial_by_channel": result["optically_thin_source_radial_distribution_by_channel"],
        "tau_matrix": result["source_weighted_mean_tau_by_emission_and_absorption_shell"]["total"],
        "selected": result["representative_couplings"],
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
