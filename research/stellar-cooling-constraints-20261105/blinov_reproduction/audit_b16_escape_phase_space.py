"""High-order 10 MeV B.16 escape distribution over emission radius, energy and direction.

This is a post-processing diagnostic of the literal fixed-omega B.2 baseline.
It repeats the high-order source/opacity construction and verifies exact grid
identity and luminosity closure against the archived high-order result before
reporting source-weighted and escape-weighted phase-space bins.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates, scalar_optical_depths
    from .audit_b16_global_redshift import (
        DEFAULT_FIG7, eq_b1_source_measure, float_array_sha256, weighted_quantile,
    )
except ImportError:
    from reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates, scalar_optical_depths
    from audit_b16_global_redshift import (
        DEFAULT_FIG7, eq_b1_source_measure, float_array_sha256, weighted_quantile,
    )

HERE = Path(__file__).resolve().parent
DEFAULT_BASELINE = HERE / "outputs" / "b16_global_high_order_independent_grid_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_escape_phase_space_10mev_2026-11-10.json"
SHELL_EDGES = np.array([0.0, 5.0, 8.0, 10.0, 12.0, 15.0, 16.5, 18.5, 20.0, 22.0, 25.0])
DIRECTION_EDGES_4 = np.linspace(-1.0, 1.0, 5)
DIRECTION_EDGES_8 = np.linspace(-1.0, 1.0, 9)


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def label(lo: float, hi: float, unit: str) -> str:
    return f"{lo:g}-{hi:g} {unit}"


def _bin_record(base, escaped, tau, total_thin, total_escaped,
                region_thin, region_escaped, global_luminosity, g):
    thin = float(np.sum(base))
    esc = float(np.sum(escaped))
    mean_tau_source = float(np.sum(base * tau) / thin) if thin > 0.0 else None
    mean_tau_escaped = float(np.sum(escaped * tau) / esc) if esc > 0.0 else None
    return {
        "thin_source_erg_s_per_g2": thin,
        "escaped_luminosity_erg_s": g * g * esc,
        "thin_source_fraction_of_global": thin / total_thin if total_thin else 0.0,
        "thin_source_fraction_within_region": thin / region_thin if region_thin else 0.0,
        "escaped_luminosity_fraction_of_global": esc / total_escaped if total_escaped else 0.0,
        "escaped_luminosity_fraction_within_region": esc / region_escaped if region_escaped else 0.0,
        "mean_escape_probability": esc / thin if thin else None,
        "mean_tau_source_weighted": mean_tau_source,
        "mean_tau_escape_weighted": mean_tau_escaped,
    }


def _axis_bins(axis, edges, names, region_mask, r, energies, angles,
               base, escaped, tau, total_thin, total_escaped,
               region_thin, region_escaped, g):
    rows = []
    if axis == "emission_radius":
        values = r
        for i, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
            mask = region_mask & (values >= lo) & (
                values < hi if i < len(edges) - 2 else values <= hi
            )
            if not np.any(mask):
                continue
            b, e, t = base[mask, :, :], escaped[mask, :, :], tau[mask, :, :]
            rows.append({"bin": names[i], **_bin_record(
                b, e, t, total_thin, total_escaped, region_thin,
                region_escaped, total_escaped, g
            )})
    elif axis == "energy":
        values = energies
        for i, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
            mask = (values >= lo) & (values < hi if i < len(edges) - 2 else values <= hi)
            if not np.any(mask):
                continue
            b, e, t = (base[region_mask][:, :, mask],
                        escaped[region_mask][:, :, mask],
                        tau[region_mask][:, :, mask])
            rows.append({"bin": names[i], **_bin_record(
                b, e, t, total_thin, total_escaped, region_thin,
                region_escaped, total_escaped, g
            )})
    elif axis == "direction":
        values = angles
        for i, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
            mask = (values >= lo) & (values < hi if i < len(edges) - 2 else values <= hi)
            if not np.any(mask):
                continue
            b, e, t = (base[region_mask][:, mask, :],
                        escaped[region_mask][:, mask, :],
                        tau[region_mask][:, mask, :])
            rows.append({"bin": names[i], **_bin_record(
                b, e, t, total_thin, total_escaped, region_thin,
                region_escaped, total_escaped, g
            )})
    else:
        raise ValueError(f"Unknown bin axis {axis}")
    return rows


def region_summary(name, region_mask, r, energies, angles, angle_weights,
                   source, columns, g, shell_edges, energy_edges,
                   direction_edges_4, direction_edges_8, global_thin,
                   global_escaped):
    base = source[:, None, :] * angle_weights[None, :, None]
    tau = g * g * columns
    survival = np.exp(-tau)
    escaped = base * survival
    region_base = base[region_mask, :, :]
    region_escaped_weights = escaped[region_mask, :, :]
    region_tau = tau[region_mask, :, :]
    region_thin = float(np.sum(region_base))
    region_escaped = float(np.sum(region_escaped_weights))
    if region_thin <= 0.0 or region_escaped <= 0.0:
        raise ArithmeticError(f"Empty source or escaped phase space for region {name}")

    shell_names = [
        label(float(lo), float(hi), "km")
        for lo, hi in zip(shell_edges[:-1], shell_edges[1:])
    ]
    energy_names = [
        label(float(lo), float(hi), "MeV")
        for lo, hi in zip(energy_edges[:-1], energy_edges[1:])
    ]
    direction_names_4 = [
        label(float(lo), float(hi), "cos(theta)")
        for lo, hi in zip(direction_edges_4[:-1], direction_edges_4[1:])
    ]
    direction_names_8 = [
        label(float(lo), float(hi), "cos(theta)")
        for lo, hi in zip(direction_edges_8[:-1], direction_edges_8[1:])
    ]

    radial_bins = _axis_bins(
        "emission_radius", shell_edges, shell_names, region_mask, r,
        energies, angles, base, escaped, tau, global_thin, global_escaped,
        region_thin, region_escaped, g
    )
    energy_bins = _axis_bins(
        "energy", energy_edges, energy_names, region_mask, r,
        energies, angles, base, escaped, tau, global_thin, global_escaped,
        region_thin, region_escaped, g
    )
    direction_bins_4 = _axis_bins(
        "direction", direction_edges_4, direction_names_4, region_mask, r,
        energies, angles, base, escaped, tau, global_thin, global_escaped,
        region_thin, region_escaped, g
    )
    direction_bins_8 = _axis_bins(
        "direction", direction_edges_8, direction_names_8, region_mask, r,
        energies, angles, base, escaped, tau, global_thin, global_escaped,
        region_thin, region_escaped, g
    )

    # Full radius x energy x direction joint distribution. Each cell is
    # aggregated from the same B.1 source weights and B.2 survival factor.
    joint = []
    shell_indices = np.digitize(r, shell_edges[1:-1], right=False)
    energy_indices = np.digitize(energies, energy_edges[1:-1], right=False)
    direction_indices_4 = np.digitize(angles, direction_edges_4[1:-1], right=False)
    for ir, shell_name in enumerate(shell_names):
        rmask = region_mask & (shell_indices == ir)
        if not np.any(rmask):
            continue
        rids = np.flatnonzero(rmask)
        for ie, energy_name in enumerate(energy_names):
            eids = np.flatnonzero(energy_indices == ie)
            if not len(eids):
                continue
            for ia, direction_name in enumerate(direction_names_4):
                aids = np.flatnonzero(direction_indices_4 == ia)
                if not len(aids):
                    continue
                b = base[np.ix_(rids, aids, eids)]
                e = escaped[np.ix_(rids, aids, eids)]
                t = tau[np.ix_(rids, aids, eids)]
                record = _bin_record(
                    b, e, t, global_thin, global_escaped,
                    region_thin, region_escaped, global_escaped, g
                )
                if record["thin_source_erg_s_per_g2"] > 0.0:
                    joint.append({
                        "emission_shell": shell_name,
                        "energy_bin": energy_name,
                        "direction_bin": direction_name,
                        **record,
                    })
    joint.sort(key=lambda row: row["escaped_luminosity_fraction_within_region"], reverse=True)

    quantiles = {}
    for q in (0.1, 0.5, 0.9, 0.99):
        quantiles[f"p{int(q*100):02d}"] = {
            "source_weighted_tau": weighted_quantile(
                region_tau, region_base, q
            ),
            "escape_weighted_tau": weighted_quantile(
                region_tau, region_escaped_weights, q
            ),
        }

    return {
        "region": name,
        "source_fraction_of_global_B1": region_thin / global_thin,
        "escaped_luminosity_fraction_of_global": region_escaped / global_escaped,
        "source_weighted_escape_probability": region_escaped / region_thin,
        "thin_source_erg_s_per_g2": region_thin,
        "escaped_luminosity_erg_s": g * g * region_escaped,
        "optically_thin_luminosity_erg_s": g * g * region_thin,
        "tau_quantiles": quantiles,
        "emission_radius_bins": radial_bins,
        "energy_bins": energy_bins,
        "direction_bins_4": direction_bins_4,
        "direction_bins_8": direction_bins_8,
        "top_joint_radius_energy_direction_bins": joint[:80],
        "joint_bin_count_nonempty": len(joint),
    }


def run(profile_path=DEFAULT_PROFILE, fig7_path=DEFAULT_FIG7,
        baseline_path=DEFAULT_BASELINE, mass=10.0,
        radial_order=200, opacity_order=640, energy_order=200,
        angular_order=32, path_order=64, energy_offset=1000.0):
    if float(mass) != 10.0:
        raise ValueError("This targeted audit is deliberately restricted to m=10 MeV")
    baseline_payload = json.loads(Path(baseline_path).read_text(encoding="utf-8"))
    baseline = baseline_payload["result"]
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
    couplings = np.asarray(vertices["g"], float)
    reference_luminosities = np.asarray(vertices["luminosity_erg_s"], float)
    g = float(couplings[-1])
    reference_luminosity = float(reference_luminosities[-1])

    source_r, source_rw = radial_rule(25.0, radial_order)
    opacity_r, _ = radial_rule(25.0, opacity_order)
    opacity_grid = np.unique(np.r_[0.0, opacity_r, 25.0])
    source_profile = load_profile(profile_path, source_r)
    opacity_profile = load_profile(profile_path, opacity_grid)

    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass / opacity_profile["lapse"]])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()

    opacity_rates = local_rates(
        mass, energies[None, :], opacity_profile["T"][:, None],
        opacity_profile["mu_numu"][:, None], opacity_profile["mu_mu"][:, None]
    )
    source_rates = local_rates(
        mass, energies[None, :], source_profile["T"][:, None],
        source_profile["mu_numu"][:, None], source_profile["mu_mu"][:, None]
    )
    source, source_meta = eq_b1_source_measure(
        source_r, source_rw, energies, source_profile["lapse"],
        mass, source_rates["production"]
    )
    columns, angle_weights = scalar_optical_depths(
        source_r, opacity_grid, opacity_rates["reduced_absorption"],
        mass, energies, 25.0, angular_order, path_order
    )
    angles, raw_angle_weights = leggauss(angular_order)
    angle_weights_expected = raw_angle_weights / 2.0
    angle_weight_residual = float(np.max(np.abs(angle_weights-angle_weights_expected)))
    if angle_weight_residual > 1.0e-15:
        raise ArithmeticError("Direction nodes/weights do not match the B.2 Gauss rule")

    source_grid_hash = float_array_sha256(source_r)
    opacity_grid_hash = float_array_sha256(opacity_grid)
    energy_grid_hash = float_array_sha256(energies)
    current_profile_hash = sha256(profile_path)
    current_fig7_hash = sha256(fig7_path)

    baseline_config = baseline["configuration"]
    expected_hashes = {
        "source_grid_sha256": baseline_config["source_grid_sha256"],
        "opacity_grid_sha256": baseline_config["opacity_grid_sha256"],
        "energy_grid_sha256": baseline_config["energy_grid_sha256"],
    }
    actual_hashes = {
        "source_grid_sha256": source_grid_hash,
        "opacity_grid_sha256": opacity_grid_hash,
        "energy_grid_sha256": energy_grid_hash,
    }
    if actual_hashes != expected_hashes:
        raise ArithmeticError(
            "Phase-space grids differ from the archived high-order B.16 baseline: "
            + json.dumps({"expected": expected_hashes, "actual": actual_hashes})
        )
    if current_profile_hash != baseline["profile"]["sha256"]:
        raise ArithmeticError("Profile fingerprint differs from the archived high-order baseline")
    if current_fig7_hash != baseline["fig7_reference"]["sha256"]:
        raise ArithmeticError("Fig. 7 digitization fingerprint differs from the archived baseline")

    total_thin = float(np.sum(source))
    base = source[:, None, :] * angle_weights[None, :, None]
    survival = np.exp(-g * g * columns)
    escaped = base * survival
    total_escaped = float(np.sum(escaped))
    thin_luminosity = g * g * total_thin
    luminosity = g * g * total_escaped
    escape_probability = total_escaped / total_thin
    baseline_point = baseline["eq_b2_fixed_omega_baseline"]["points"][-1]
    closure = {
        "luminosity_relative_residual_vs_high_order_baseline": (
            luminosity / baseline_point["calculated_luminosity_erg_s"] - 1.0
        ),
        "thin_luminosity_relative_residual_vs_high_order_baseline": (
            thin_luminosity / baseline_point["optically_thin_luminosity_erg_s"] - 1.0
        ),
        "escape_probability_absolute_residual_vs_high_order_baseline": (
            escape_probability - baseline_point["escape_fraction"]
        ),
    }
    if abs(closure["luminosity_relative_residual_vs_high_order_baseline"]) > 2.0e-10:
        raise ArithmeticError("Recomputed strong-end luminosity does not close to the archived baseline")
    if abs(closure["thin_luminosity_relative_residual_vs_high_order_baseline"]) > 2.0e-10:
        raise ArithmeticError("Recomputed thin luminosity does not close to the archived baseline")

    energy_edges = np.array([
        mass, mass+1.0, mass+2.0, mass+3.0, mass+5.0, mass+7.5,
        mass+10.0, mass+15.0, mass+20.0, mass+30.0, mass+50.0,
        mass+100.0, mass+200.0, mass+500.0, energies[-1]*(1.0+1.0e-12)
    ])
    if np.any(np.diff(energy_edges) <= 0.0):
        raise ArithmeticError("Energy-bin edges are not strictly increasing")
    all_region = np.ones(len(source_r), dtype=bool)
    core_region = (source_r >= 8.0) & (source_r < 15.0)
    summaries = [
        region_summary(
            "all_emission_radii", all_region, source_r, energies, angles,
            angle_weights, source, columns, g, SHELL_EDGES, energy_edges,
            DIRECTION_EDGES_4, DIRECTION_EDGES_8, total_thin, total_escaped
        ),
        region_summary(
            "dominant_8_15km_emission", core_region, source_r, energies,
            angles, angle_weights, source, columns, g, SHELL_EDGES,
            energy_edges, DIRECTION_EDGES_4, DIRECTION_EDGES_8,
            total_thin, total_escaped
        ),
    ]

    result = {
        "title": "High-order B.16 10 MeV escaping phase-space decomposition",
        "mass_MeV": mass,
        "coupling": g,
        "reference_luminosity_erg_s": reference_luminosity,
        "calculated_luminosity_erg_s": luminosity,
        "optically_thin_luminosity_erg_s": thin_luminosity,
        "escape_probability": escape_probability,
        "relative_difference_vs_fig7": luminosity / reference_luminosity - 1.0,
        "profile": {"sha256": current_profile_hash, "identity": baseline["profile"]["identity"]},
        "fig7_reference_sha256": current_fig7_hash,
        "baseline_json_sha256": sha256(baseline_path),
        "configuration": {
            "source_radial_order": radial_order,
            "source_radial_node_count": len(source_r),
            "source_grid_sha256": source_grid_hash,
            "opacity_order": opacity_order,
            "opacity_radial_node_count": len(opacity_grid),
            "opacity_grid_sha256": opacity_grid_hash,
            "energy_order": energy_order,
            "energy_node_count": len(energies),
            "energy_grid_sha256": energy_grid_hash,
            "angular_order": angular_order,
            "path_order": path_order,
            "direction_weight_sum": float(np.sum(angle_weights)),
            "direction_weight_closure_residual": angle_weight_residual,
            "path_energy_convention": "fixed omega along the full Eq. (B.2) chord",
            "energy_bin_edges_MeV": energy_edges.tolist(),
            "emission_shell_edges_km": SHELL_EDGES.tolist(),
            "direction_edges_4": DIRECTION_EDGES_4.tolist(),
            "direction_edges_8": DIRECTION_EDGES_8.tolist(),
        },
        "source_channel_fractions": {
            "neutrino": float(np.sum(source_rates["neutrino_production"] * 0.0)
                              + np.sum(eq_b1_source_measure(
                                  source_r, source_rw, energies, source_profile["lapse"],
                                  mass, source_rates["neutrino_production"]
                              )[0]) / total_thin),
            "compton": float(np.sum(eq_b1_source_measure(
                source_r, source_rw, energies, source_profile["lapse"],
                mass, source_rates["compton_production"]
            )[0]) / total_thin),
        },
        "source_measure_metadata": {
            "radial_node_count": len(source_meta["radial_measure_MeVminus3"]),
            "energy_node_count": len(source_meta["spectral_measure_MeV3"]),
        },
        "closure": closure,
        "regions": summaries,
        "interpretation_limits": [
            "The result uses the literal fixed-omega Eq. (B.2) baseline and the archived public-figure reconstructed SFHo-18.8 profile.",
            "This is an escape-distribution decomposition, not a correction or rescaling of the published curve.",
            "The phase-space bins are post-processing partitions of the same high-order source and opacity arrays; no new physical approximation is introduced.",
            "The energy bins are reporting bins only and do not alter the underlying quadrature.",
            "No axial-vector output or constraint curve is changed."
        ],
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--nr", type=int, default=200)
    parser.add_argument("--opacity-order", type=int, default=640)
    parser.add_argument("--ne", type=int, default=200)
    parser.add_argument("--na", type=int, default=32)
    parser.add_argument("--ns", type=int, default=64)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()
    result = run(
        args.profile, args.fig7, args.baseline, args.mass,
        args.nr, args.opacity_order, args.ne, args.na, args.ns,
        args.energy_offset
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "mass_MeV": result["mass_MeV"],
        "coupling": result["coupling"],
        "calculated_luminosity_erg_s": result["calculated_luminosity_erg_s"],
        "reference_luminosity_erg_s": result["reference_luminosity_erg_s"],
        "relative_difference_vs_fig7": result["relative_difference_vs_fig7"],
        "escape_probability": result["escape_probability"],
        "closure": result["closure"],
        "configuration": result["configuration"],
        "regions": [
            {
                "region": x["region"],
                "source_fraction_of_global_B1": x["source_fraction_of_global_B1"],
                "escaped_luminosity_fraction_of_global": x["escaped_luminosity_fraction_of_global"],
                "source_weighted_escape_probability": x["source_weighted_escape_probability"],
                "top_joint_bins": x["top_joint_radius_energy_direction_bins"][:12],
            } for x in result["regions"]
        ],
        "output": str(args.output),
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
