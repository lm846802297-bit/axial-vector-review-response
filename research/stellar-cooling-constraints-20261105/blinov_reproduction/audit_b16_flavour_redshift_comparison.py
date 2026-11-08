"""Compare flavor-resolved neutrino opacity under fixed-omega and path-redshift prescriptions.

The fixed-omega calculation is the literal Appendix-B Eq. (B.2) benchmark.
The path-redshift calculation is a separately labeled diagnostic:
omega_loc(s)=omega_source*N(source)/N(path), with the same Euclidean chord
measure. The B.1 source and all profile inputs are held fixed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, scalar_optical_depths, redshifted_scalar_optical_depths,
        decay_production, compton_production,
        negative_muon_density_and_degeneracy, fermi_pair_average,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_neutrino_flavour_opacity import flavour_rate_arrays
    from .audit_b16_shell_luminosity_sensitivity import (
        shell_columns_by_channel, log_escaped_integral, removal_diagnostic,
        SHELL_EDGES_KM,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, scalar_optical_depths, redshifted_scalar_optical_depths,
        decay_production, compton_production,
        negative_muon_density_and_degeneracy, fermi_pair_average,
    )
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_neutrino_flavour_opacity import flavour_rate_arrays
    from audit_b16_shell_luminosity_sensitivity import (
        shell_columns_by_channel, log_escaped_integral, removal_diagnostic,
        SHELL_EDGES_KM,
    )

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_flavour_fixed_vs_redshift_10mev_2026-11-08.json"
CHANNELS = ("nu_mu", "nu_tau", "compton", "dimuon")


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _single_channel_rates(production, temperature, energies, channel):
    """Package one production component for the common shell integrator."""
    zeros = np.zeros_like(production)
    result = {
        "neutrino_production": zeros,
        "compton_production": zeros,
        "dimuon_production": zeros,
    }
    result[{
        "nu_mu": "neutrino_production",
        "nu_tau": "neutrino_production",
        "compton": "compton_production",
        "dimuon": "dimuon_production",
    }[channel]] = production
    x = np.asarray(energies, float)[None, :]/np.asarray(temperature, float)[:, None]
    result["reduced_absorption"] = np.expm1(np.minimum(x, 700.0))*production
    return result


def _source_weighted_mean_tau(source, angle_weights, columns):
    angle_average = np.einsum("rae,a->re", columns, angle_weights)
    denominator = float(np.sum(source))
    return float(np.sum(source*angle_average)/denominator) if denominator else 0.0


def _shell_summary(source, angle_weights, channel_shell_columns, labels):
    channel_summary = {}
    for channel, shell_columns in channel_shell_columns.items():
        per_shell = []
        for i, label in enumerate(labels):
            per_shell.append({
                "shell": label,
                "mean_tau": _source_weighted_mean_tau(
                    source, angle_weights, shell_columns[i]
                ),
            })
        channel_summary[channel] = {
            "mean_tau": float(sum(x["mean_tau"] for x in per_shell)),
            "shells": per_shell,
        }

    total_shells = []
    for i, label in enumerate(labels):
        shell_total = sum(
            values[i] for values in channel_shell_columns.values()
        )
        total_shells.append({
            "shell": label,
            "mean_tau": _source_weighted_mean_tau(
                source, angle_weights, shell_total
            ),
        })
    total_mean = float(sum(x["mean_tau"] for x in total_shells))
    outer_mean = float(sum(
        x["mean_tau"] for x in total_shells
        if float(x["shell"].split("-")[0]) >= 15.0
    ))
    return {
        "channels": channel_summary,
        "total_by_shell": total_shells,
        "total_mean_tau": total_mean,
        "outer_r_ge_15km_mean_tau": outer_mean,
        "outer_fraction_of_total_mean_tau": (
            outer_mean/total_mean if total_mean else 0.0
        ),
    }


def _fixed_omega_shell_columns(
    source_radii, radial_grid, profile, mass, energies,
    radius_km, angular_order, path_order,
):
    rates = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    nu_mu_prod, nu_tau_prod = flavour_rate_arrays(mass, energies, profile)
    productions = {
        "nu_mu": nu_mu_prod,
        "nu_tau": nu_tau_prod,
        "compton": rates["compton_production"],
        "dimuon": rates["dimuon_production"],
    }
    output = {}
    angle_weights = None
    for channel, production in productions.items():
        packed = _single_channel_rates(
            production, profile["T"], energies, channel
        )
        result = shell_columns_by_channel(
            source_radii, radial_grid, profile["T"], packed,
            mass, energies, radius_km, angular_order, path_order
        )
        output[channel] = result["columns_by_channel"][
            "compton" if channel == "compton" else
            "dimuon" if channel == "dimuon" else "neutrino"
        ]
        angle_weights = result["angle_weights"]
    return output, angle_weights, rates


def redshifted_shell_columns_by_flavour(
    source_radii, radial_grid, profile, mass, source_energies,
    radius_km=25.0, angular_order=16, path_order=32,
):
    """Return per-flavor/per-channel shell columns with local redshifted energy."""
    source_radii = np.asarray(source_radii, float)
    radial_grid = np.asarray(radial_grid, float)
    source_energies = np.asarray(source_energies, float)
    r = source_radii[:, None]

    angles, angle_weights = np.polynomial.legendre.leggauss(angular_order)
    path_x, path_w = np.polynomial.legendre.leggauss(path_order)
    path_w = path_w/2.0

    source_indices = np.searchsorted(radial_grid, source_radii)
    source_lapse = profile["lapse"][source_indices]

    n_mu_grid, fdeg_grid = negative_muon_density_and_degeneracy(
        profile["T"], profile["mu_mu"]
    )
    chi_grid = n_mu_grid*fdeg_grid

    labels = [
        f"{lo:g}-{hi:g} km"
        for lo, hi in zip(SHELL_EDGES_KM[:-1], SHELL_EDGES_KM[1:])
        if hi <= radius_km
    ]
    edges = [x for x in SHELL_EDGES_KM if x <= radius_km]
    if edges[-1] < radius_km:
        edges.append(radius_km)
    labels = [f"{lo:g}-{hi:g} km" for lo, hi in zip(edges[:-1], edges[1:])]
    n_source, n_energy = len(source_radii), len(source_energies)
    shell_columns = {
        channel: np.zeros((len(labels), n_source, angular_order, n_energy))
        for channel in CHANNELS
    }

    min_ratio = np.inf
    max_ratio = 0.0
    min_velocity = 1.0
    eligible_all = source_lapse[:, None]*source_energies[None, :] > mass*(1.0+1e-12)

    for ia, cosine in enumerate(angles):
        smax = -cosine*r + np.sqrt(
            radius_km**2-r**2+r**2*cosine**2
        )
        s = smax*(1.0+path_x[None, :])/2.0
        position = np.sqrt(np.maximum(
            r**2+s**2+2.0*r*s*cosine, 0.0
        ))
        path_weights = smax*path_w[None, :]
        flat = position.ravel()

        def interp(field):
            return np.interp(flat, radial_grid, profile[field]).reshape(position.shape)

        t_path = interp("T")
        mu_mu_path = interp("mu_mu")
        mu_numu_path = interp("mu_numu")
        lapse_path = interp("lapse")
        chi_path = np.interp(flat, radial_grid, chi_grid).reshape(position.shape)

        # E_infinity=N(source)*omega_source is conserved on the diagnostic ray.
        omega_local = (
            source_energies[None, None, :]*source_lapse[:, None, None]
            / lapse_path[:, :, None]
        )
        ratio = omega_local/source_energies[None, None, :]
        min_ratio = min(min_ratio, float(np.min(ratio)))
        max_ratio = max(max_ratio, float(np.max(ratio)))

        eligible = eligible_all[:, None, :]
        omega_eval = np.where(
            eligible, omega_local, mass*(1.0+1e-9)
        )
        velocity = np.sqrt(np.maximum(1.0-(mass/omega_eval)**2, 0.0))
        if np.any((velocity <= 0.0) & eligible):
            raise FloatingPointError("Eligible redshifted ray reached zero speed")
        if np.any(eligible):
            min_velocity = min(min_velocity, float(np.min(velocity[eligible])))

        prefactor = mass**2/(8.0*np.pi*omega_eval)
        beta = omega_eval/t_path[:, :, None]
        i_mu = fermi_pair_average(
            mu_numu_path[:, :, None], omega_eval,
            t_path[:, :, None], velocity
        )
        i_tau = fermi_pair_average(
            np.zeros_like(omega_eval), omega_eval,
            t_path[:, :, None], velocity
        )
        nu_mu_prod = prefactor*i_mu
        nu_tau_prod = prefactor*i_tau

        _, dimuon_prod = decay_production(
            mass, omega_eval, t_path[:, :, None],
            mu_numu_path[:, :, None], mu_mu_path[:, :, None]
        )
        compton_prod = compton_production(
            mass, omega_eval, t_path[:, :, None],
            chi_path[:, :, None], np.ones_like(chi_path[:, :, None])
        )
        productions = {
            "nu_mu": nu_mu_prod,
            "nu_tau": nu_tau_prod,
            "compton": compton_prod,
            "dimuon": dimuon_prod,
        }
        inverse_velocity = np.divide(
            1.0, velocity, out=np.zeros_like(velocity), where=velocity > 0.0
        )
        reduced_absorption = {
            name: np.expm1(np.minimum(beta, 700.0))*production
            for name, production in productions.items()
        }

        shell_masks = [
            (position >= lo) &
            (position < hi if hi < radius_km else position <= hi)
            for lo, hi in zip(edges[:-1], edges[1:])
        ]
        for channel, reduced in reduced_absorption.items():
            for ish, mask in enumerate(shell_masks):
                shell_columns[channel][ish, :, ia, :] = (
                    np.sum(
                        path_weights[:, :, None]*mask[:, :, None]
                        * reduced*inverse_velocity,
                        axis=1
                    )*KM_TO_MEV_INV
                )

    # Non-escaping modes have infinite total optical depth in the global
    # redshift audit. Their channel-resolved opacity columns are set to zero
    # so removing one flavor never performs inf-inf; the infinite barrier
    # remains in the total baseline column.
    for channel in CHANNELS:
        shell_columns[channel] = np.where(
            eligible_all[None, :, None, :],
            shell_columns[channel], 0.0
        )
    return {
        "labels": labels,
        "angle_weights": angle_weights/2.0,
        "shell_columns_by_channel": shell_columns,
        "channel_columns": {
            channel: np.sum(values, axis=0)
            for channel, values in shell_columns.items()
        },
        "minimum_local_over_source_energy_ratio": float(min_ratio),
        "maximum_local_over_source_energy_ratio": float(max_ratio),
        "minimum_local_vector_speed": float(min_velocity),
        "eligible_source_energy_mask": eligible_all,
    }


def _removal_for_prescription(
    source, angle_weights, total_columns, channel_columns,
    shell_columns, labels, couplings, reference_luminosities, name,
):
    log_escape = np.asarray([
        log_escaped_integral(source, angle_weights, total_columns, g)
        for g in couplings
    ])
    log_luminosity = 2.0*np.log(couplings)+log_escape
    peak_idx = int(np.argmax(log_luminosity))
    indices = {
        "weak_coupling": 0,
        f"{name}_luminosity_peak": peak_idx,
        "strong_absorption_endpoint": len(couplings)-1,
    }
    outer_indices = [
        i for i, label in enumerate(labels)
        if float(label.split("-")[0]) >= 15.0
    ]
    outer_columns = {
        channel: np.sum(shell_columns[channel][outer_indices], axis=0)
        for channel in CHANNELS
    }
    points = []
    for idx in sorted(set(indices.values())):
        g = float(couplings[idx])
        points.append({
            "index": idx,
            "g": g,
            "reference_luminosity_erg_s": float(reference_luminosities[idx]),
            "baseline_log10_luminosity_erg_s": float(log_luminosity[idx]/np.log(10.0)),
            "remove_all_nu_mu": removal_diagnostic(
                source, angle_weights, total_columns, channel_columns["nu_mu"], g
            ),
            "remove_all_nu_tau": removal_diagnostic(
                source, angle_weights, total_columns, channel_columns["nu_tau"], g
            ),
            "remove_outer_nu_mu": removal_diagnostic(
                source, angle_weights, total_columns, outer_columns["nu_mu"], g
            ),
            "remove_outer_nu_tau": removal_diagnostic(
                source, angle_weights, total_columns, outer_columns["nu_tau"], g
            ),
            "remove_both_outer_neutrino_flavours": removal_diagnostic(
                source, angle_weights, total_columns,
                outer_columns["nu_mu"]+outer_columns["nu_tau"], g
            ),
        })
    return {"peak_index": peak_idx, "points": points}


def run_audit(
    profile_path=DEFAULT_PROFILE, fig7_path=DEFAULT_FIG7,
    mass=10.0, radial_order=40, energy_order=100,
    angular_order=16, path_order=32, radius_km=25.0, energy_offset=1000.0,
):
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
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
    source_index = np.searchsorted(radial_grid, r)
    source, source_measure = eq_b1_source_measure(
        r, rw, energies, profile["lapse"][source_index], mass,
        rates["production"][source_index]
    )

    fixed_shells, fixed_angles, fixed_rates = _fixed_omega_shell_columns(
        r, radial_grid, profile, mass, energies, radius_km,
        angular_order, path_order
    )
    redshift = redshifted_shell_columns_by_flavour(
        r, radial_grid, profile, mass, energies, radius_km,
        angular_order, path_order
    )
    if np.max(np.abs(fixed_angles-redshift["angle_weights"])) > 1.0e-14:
        raise ArithmeticError("Fixed and redshifted angle weights differ")

    total_fixed, total_fixed_angles = scalar_optical_depths(
        r, radial_grid, fixed_rates["reduced_absorption"],
        mass, energies, radius_km, angular_order, path_order
    )
    total_redshift, total_redshift_angles, redshift_info = (
        redshifted_scalar_optical_depths(
            r, radial_grid, profile, mass, energies, radius_km,
            angular_order, path_order
        )
    )
    if np.max(np.abs(total_fixed_angles-fixed_angles)) > 1.0e-14:
        raise ArithmeticError("Fixed total and shell angle weights differ")
    if np.max(np.abs(total_redshift_angles-redshift["angle_weights"])) > 1.0e-14:
        raise ArithmeticError("Redshift total and shell angle weights differ")

    fixed_channel_columns = {
        channel: np.sum(values, axis=0)
        for channel, values in fixed_shells.items()
    }
    redshift_channel_columns = redshift["channel_columns"]
    fixed_sum = sum(fixed_channel_columns.values())
    redshift_sum = sum(redshift_channel_columns.values())
    eligible = redshift["eligible_source_energy_mask"]
    fixed_closure = float(np.max(
        np.abs(fixed_sum-total_fixed)
        / np.maximum(np.abs(total_fixed), 1.0e-300)
    ))
    eligible_3d = np.broadcast_to(eligible[:, None, :], total_redshift.shape)
    redshift_relative_residual = (
        np.abs(redshift_sum-total_redshift)
        / np.maximum(np.abs(total_redshift), 1.0e-300)
    )
    redshift_closure = float(np.max(redshift_relative_residual[eligible_3d]))
    # Flavor sum is separately checked against the direct neutrino component.
    fixed_nu_mu, fixed_nu_tau = flavour_rate_arrays(mass, energies, profile)
    fixed_nu_total = fixed_rates["neutrino_production"]
    fixed_flavour_rate_residual = float(np.max(
        np.abs(fixed_nu_mu+fixed_nu_tau-fixed_nu_total)
        / np.maximum(np.abs(fixed_nu_total), 1.0e-300)
    ))

    labels = redshift["labels"]
    fixed_summary = _shell_summary(
        source, fixed_angles, fixed_shells, labels
    )
    redshift_summary = _shell_summary(
        source, redshift["angle_weights"],
        redshift["shell_columns_by_channel"], labels
    )
    redshift_summary["minimum_local_over_source_energy_ratio"] = (
        redshift["minimum_local_over_source_energy_ratio"]
    )
    redshift_summary["maximum_local_over_source_energy_ratio"] = (
        redshift["maximum_local_over_source_energy_ratio"]
    )
    redshift_summary["minimum_local_vector_speed"] = (
        redshift["minimum_local_vector_speed"]
    )

    fixed_removal = _removal_for_prescription(
        source, fixed_angles, total_fixed, fixed_channel_columns,
        fixed_shells, labels, couplings, reference_lum, "fixed_omega"
    )
    redshift_removal = _removal_for_prescription(
        source, redshift["angle_weights"], total_redshift,
        redshift_channel_columns, redshift["shell_columns_by_channel"],
        labels, couplings, reference_lum, "path_redshift"
    )

    # Compare per-shell and total flavor contributions between the two
    # prescriptions. This is the central diagnostic, with no rescaling.
    fixed_by_channel = fixed_summary["channels"]
    redshift_by_channel = redshift_summary["channels"]
    comparisons = {}
    for channel in CHANNELS:
        f = fixed_by_channel[channel]
        z = redshift_by_channel[channel]
        comparisons[channel] = {
            "fixed_omega_mean_tau": f["mean_tau"],
            "path_redshift_mean_tau": z["mean_tau"],
            "path_redshift_over_fixed": (
                z["mean_tau"]/f["mean_tau"] if f["mean_tau"] else None
            ),
            "shell_ratios": [
                {
                    "shell": fs["shell"],
                    "fixed_omega_mean_tau": fs["mean_tau"],
                    "path_redshift_mean_tau": zs["mean_tau"],
                    "path_redshift_over_fixed": (
                        zs["mean_tau"]/fs["mean_tau"]
                        if fs["mean_tau"] else None
                    ),
                }
                for fs, zs in zip(f["shells"], z["shells"])
            ],
        }

    return {
        "title": "B.16 flavor-resolved radial opacity: fixed omega versus path-redshift diagnostic",
        "mass_MeV": mass,
        "scope": [
            "Pure-vector B.14--B.16 benchmark at m_V=10 MeV.",
            "Fixed omega is the literal published Eq. (B.2) baseline.",
            "Path redshift changes omega_loc(s)=omega_source*N(source)/N(path) and local v_V(s), but retains the Euclidean straight-chord ds; it is not a full GR ray trace.",
            "The Eq. (B.1) source, source energy variable, coupling grid, profile, radial/angular/path quadrature, and production rates at the source are held fixed.",
            "No rescaling of rates, couplings, or luminosities.",
        ],
        "configuration": {
            "radial_order": radial_order,
            "energy_order": energy_order,
            "angular_order": angular_order,
            "path_order": path_order,
            "radius_km": radius_km,
            "energy_offset_MeV": energy_offset,
            "shell_edges_km": labels,
        },
        "provenance": {
            "profile_path": str(profile_path),
            "profile_sha256": sha256(profile_path),
            "profile_identity": "digitized public-figure SFHo-18.8, t_pb=1 s; not original Garching simulation table",
            "fig7_path": str(fig7_path),
            "fig7_sha256": sha256(fig7_path),
            "reference_pdf_sha256": fig7.get("pdf_sha256"),
            "source_reference": "Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B",
        },
        "eq_b1_source_measure": source_measure,
        "column_closure": {
            "fixed_omega_all_channel_shell_sum_max_relative_residual": fixed_closure,
            "fixed_omega_flavour_rate_sum_max_relative_residual": fixed_flavour_rate_residual,
            "path_redshift_all_channel_shell_sum_max_relative_residual_on_escaping_bins": redshift_closure,
            "path_redshift_total_column_infinite_source_weight_fraction": float(
                np.sum(source*(~eligible))/np.sum(source)
            ),
        },
        "fixed_omega": {
            "prescription": "Gamma_abs_star(r'(s), omega_source)/v_V(omega_source)",
            "shell_summary": fixed_summary,
            "luminosity_removal": fixed_removal,
        },
        "path_redshift_only": {
            "prescription": "omega_local(s)=omega_source*N(source)/N(path); update local rates and v_V(s), same Euclidean ds",
            "kinematic_range": redshift_info,
            "shell_summary": redshift_summary,
            "luminosity_removal": redshift_removal,
        },
        "fixed_vs_redshift_flavour_comparison": comparisons,
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
        "closure": result["column_closure"],
        "fixed_shell_summary": result["fixed_omega"]["shell_summary"],
        "redshift_shell_summary": result["path_redshift_only"]["shell_summary"],
        "channel_comparisons": result["fixed_vs_redshift_flavour_comparison"],
        "fixed_luminosity_removal": result["fixed_omega"]["luminosity_removal"],
        "redshift_luminosity_removal": result["path_redshift_only"]["luminosity_removal"],
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
