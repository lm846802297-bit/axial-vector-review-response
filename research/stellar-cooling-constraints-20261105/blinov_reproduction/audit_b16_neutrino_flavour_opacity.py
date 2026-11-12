"""Split B.16 neutrino opacity into nu_mu and nu_tau contributions.

The production kernel in reference.py sums I(mu_nu_mu)+I(0): the first term
is the muon-neutrino flavor and the second is the tau-neutrino flavor, for
which the Blinov analysis sets mu_nu_tau=0. This audit checks their separate
radial optical depths and luminosity-removal sensitivities.
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
        local_rates, scalar_optical_depths, fermi_pair_average,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_shell_luminosity_sensitivity import (
        shell_columns_by_channel, log_escaped_integral, removal_diagnostic,
        SHELL_EDGES_KM,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, radial_rule, load_profile,
        local_rates, scalar_optical_depths, fermi_pair_average,
    )
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_shell_luminosity_sensitivity import (
        shell_columns_by_channel, log_escaped_integral, removal_diagnostic,
        SHELL_EDGES_KM,
    )

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_neutrino_flavour_opacity_10mev_2026-11-08.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def flavour_rate_arrays(mass, energies, profile):
    """Return nu_mu and nu_tau production rates per g^2 from Eq. (23)."""
    omega = np.asarray(energies, float)[None, :]
    temperature = np.asarray(profile["T"], float)[:, None]
    mu_numu = np.asarray(profile["mu_numu"], float)[:, None]
    velocity = np.sqrt(np.maximum(1.0-(mass/omega)**2, 0.0))
    prefactor = mass**2/(8.0*np.pi*omega)
    i_mu = fermi_pair_average(mu_numu, omega, temperature, velocity)
    i_tau = fermi_pair_average(np.zeros_like(mu_numu), omega, temperature, velocity)
    return prefactor*i_mu, prefactor*i_tau


def fake_flavour_rates(production, temperature, energies):
    x = np.asarray(energies, float)[None, :]/np.asarray(temperature, float)[:, None]
    reduced = np.expm1(np.minimum(x, 700.0))*production
    zeros = np.zeros_like(production)
    return {
        "neutrino_production": production,
        "compton_production": zeros,
        "dimuon_production": zeros,
        "reduced_absorption": reduced,
    }


def source_weighted_mean_tau(source, angle_weights, columns):
    avg = np.einsum("rae,a->re", columns, angle_weights)
    return float(np.sum(source*avg)/np.sum(source))


def run_audit(
    profile_path, fig7_path, mass=10.0, radial_order=40, energy_order=100,
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
    nu_mu, nu_tau = flavour_rate_arrays(mass, energies, profile)
    nu_sum = nu_mu+nu_tau
    rate_sum_residual = float(np.max(
        np.abs(nu_sum-rates["neutrino_production"])
        / np.maximum(np.abs(rates["neutrino_production"]), 1.0e-300)
    ))

    mu_rates = fake_flavour_rates(nu_mu, profile["T"], energies)
    tau_rates = fake_flavour_rates(nu_tau, profile["T"], energies)
    mu_data = shell_columns_by_channel(
        r, radial_grid, profile["T"], mu_rates, mass, energies,
        radius_km, angular_order, path_order
    )
    tau_data = shell_columns_by_channel(
        r, radial_grid, profile["T"], tau_rates, mass, energies,
        radius_km, angular_order, path_order
    )
    mu_columns = mu_data["columns_total"]
    tau_columns = tau_data["columns_total"]
    neutrino_columns = mu_columns+tau_columns

    x = energies[None, :]/profile["T"][:, None]
    reduced_nu_total = np.expm1(np.minimum(x, 700.0))*rates["neutrino_production"]
    direct_nu_columns, angle_weights = scalar_optical_depths(
        r, radial_grid, reduced_nu_total, mass, energies,
        radius_km, angular_order, path_order
    )
    flavour_column_residual = float(np.max(
        np.abs(neutrino_columns-direct_nu_columns)
        / np.maximum(np.abs(direct_nu_columns), 1.0e-300)
    ))

    source_indices = np.searchsorted(radial_grid, r)
    source, source_measure = eq_b1_source_measure(
        r, rw, energies, profile["lapse"][source_indices],
        mass, rates["production"][source_indices]
    )
    total_columns, total_angles = scalar_optical_depths(
        r, radial_grid, rates["reduced_absorption"], mass, energies,
        radius_km, angular_order, path_order
    )
    angle_residual = float(np.max(np.abs(total_angles-angle_weights)))
    compton_columns = np.maximum(total_columns-neutrino_columns, 0.0)

    shell_labels = mu_data["shell_labels"]
    shell_mu = mu_data["columns_by_shell"]
    shell_tau = tau_data["columns_by_shell"]
    shell_outer_indices = [
        i for i, label in enumerate(shell_labels)
        if float(label.split("-")[0]) >= 15.0
    ]
    mu_outer = np.sum(shell_mu[shell_outer_indices], axis=0)
    tau_outer = np.sum(shell_tau[shell_outer_indices], axis=0)
    nu_outer = mu_outer+tau_outer

    mean_tau_mu = source_weighted_mean_tau(source, angle_weights, mu_columns)
    mean_tau_tau = source_weighted_mean_tau(source, angle_weights, tau_columns)
    mean_tau_nu = source_weighted_mean_tau(source, angle_weights, neutrino_columns)
    mean_tau_total = source_weighted_mean_tau(source, angle_weights, total_columns)
    mean_tau_mu_outer = source_weighted_mean_tau(source, angle_weights, mu_outer)
    mean_tau_tau_outer = source_weighted_mean_tau(source, angle_weights, tau_outer)
    mean_tau_nu_outer = mean_tau_mu_outer+mean_tau_tau_outer

    # Local detailed-balance diagnostic. In the MB/low-T limit,
    # (e^(omega/T)-1) I(0,omega/T,v) -> 1, so Gamma_abs* approaches
    # the time-dilated vacuum-decay scale 3m^2/(8 pi omega) per g^2.
    sample_radii = [8.0, 10.0, 12.0, 15.0, 18.5, 20.0, 22.0, 25.0]
    sample_energies = [15.0, 20.0, 30.0]
    local_rows = []
    for radius in sample_radii:
        t = float(np.interp(radius, radial_grid, profile["T"]))
        mu = float(np.interp(radius, radial_grid, profile["mu_numu"]))
        for omega in sample_energies:
            v = float(np.sqrt(1.0-(mass/omega)**2))
            i_mu = float(fermi_pair_average(mu, omega, t, v))
            i_tau = float(fermi_pair_average(0.0, omega, t, v))
            factor = float(np.expm1(omega/t))
            vacuum_scale = mass**2/(8.0*np.pi*omega)
            local_rows.append({
                "r_km": radius,
                "omega_local_MeV": omega,
                "T_MeV": t,
                "mu_numu_MeV": mu,
                "mu_numu_over_T": mu/t,
                "omega_over_T": omega/t,
                "muon_neutrino_I": i_mu,
                "tau_neutrino_I": i_tau,
                "muon_neutrino_reduced_absorption_per_g2": factor*vacuum_scale*i_mu,
                "tau_neutrino_reduced_absorption_per_g2": factor*vacuum_scale*i_tau,
                "muon_neutrino_reduced_absorption_over_vacuum_scale": factor*i_mu,
                "tau_neutrino_reduced_absorption_over_vacuum_scale": factor*i_tau,
                "detailed_balance_factor_exp_omega_over_T_minus_1": factor,
            })

    # Representative coupling points: weak, actual luminosity peak, strong tail.
    log_base = np.asarray([
        log_escaped_integral(source, angle_weights, total_columns, g)
        for g in couplings
    ])
    log_lum = 2.0*np.log(couplings)+log_base
    indices = {
        "weak_coupling": 0,
        "calculated_luminosity_peak": int(np.argmax(log_lum)),
        "strong_absorption_endpoint": len(couplings)-1,
    }
    selected = []
    for idx in sorted(set(indices.values())):
        g = float(couplings[idx])
        row = {
            "index": int(idx),
            "g": g,
            "reference_luminosity_erg_s": float(reference_lum[idx]),
            "baseline_log10_luminosity_erg_s": float(log_lum[idx]/np.log(10.0)),
            "remove_all_nu_mu_opacity": removal_diagnostic(
                source, angle_weights, total_columns, mu_columns, g
            ),
            "remove_all_nu_tau_opacity": removal_diagnostic(
                source, angle_weights, total_columns, tau_columns, g
            ),
            "remove_outer_nu_mu_opacity": removal_diagnostic(
                source, angle_weights, total_columns, mu_outer, g
            ),
            "remove_outer_nu_tau_opacity": removal_diagnostic(
                source, angle_weights, total_columns, tau_outer, g
            ),
            "remove_all_neutrino_opacity": removal_diagnostic(
                source, angle_weights, total_columns, neutrino_columns, g
            ),
            "remove_outer_neutrino_opacity": removal_diagnostic(
                source, angle_weights, total_columns, nu_outer, g
            ),
        }
        selected.append(row)

    shell_rows = []
    for i, label in enumerate(shell_labels):
        mu_tau_shell = source_weighted_mean_tau(source, angle_weights, shell_mu[i])
        tau_tau_shell = source_weighted_mean_tau(source, angle_weights, shell_tau[i])
        shell_rows.append({
            "shell": label,
            "nu_mu_mean_tau": mu_tau_shell,
            "nu_tau_mean_tau": tau_tau_shell,
            "combined_neutrino_mean_tau": mu_tau_shell+tau_tau_shell,
            "nu_mu_fraction_of_neutrino_tau": (
                mu_tau_shell/(mu_tau_shell+tau_tau_shell)
                if mu_tau_shell+tau_tau_shell > 0 else 0.0
            ),
        })

    return {
        "title": "B.16 neutrino opacity split into muon- and tau-neutrino flavors",
        "mass_MeV": mass,
        "scope": [
            "Pure-vector B.14--B.16 baseline at m=10 MeV.",
            "The neutrino production kernel is split exactly into I(mu_nu_mu)+I(0), corresponding to nu_mu and nu_tau.",
            "The B.1 source is held fixed when testing opacity removal.",
            "No source, coupling, opacity, or luminosity rescaling.",
        ],
        "physical_convention": {
            "nu_mu_production": "m_V^2/(8 pi omega) I(mu_nu_mu/T, omega/T, v)",
            "nu_tau_production": "m_V^2/(8 pi omega) I(0, omega/T, v)",
            "mu_nu_tau_assumption": "0, as in Blinov et al. because no tau leptons are populated in the PNS",
            "reduced_absorption_each_flavor": "(exp(omega/T)-1) Gamma_prod",
            "low_temperature_limit": (
                "For mu_nu=0 and omega/T >> 1, I ~ exp(-omega/T), so the "
                "reduced absorption approaches the time-dilated vacuum-decay scale."
            ),
        },
        "configuration": {
            "radial_order": radial_order,
            "energy_order": energy_order,
            "angular_order": angular_order,
            "path_order": path_order,
            "radius_km": radius_km,
            "energy_offset_MeV": energy_offset,
            "sample_radii_km": sample_radii,
            "sample_local_energies_MeV": sample_energies,
        },
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "identity": "reconstructed public-figure SFHo-18.8, t_pb=1 s; not original raw Garching table",
        },
        "fig7_reference": {
            "path": str(fig7_path),
            "sha256": sha256(fig7_path),
            "pdf_sha256": fig7.get("pdf_sha256"),
        },
        "eq_b1_source_measure": source_measure,
        "flavour_rate_sum_max_relative_residual": rate_sum_residual,
        "flavour_column_sum_max_relative_residual": flavour_column_residual,
        "angular_weight_max_residual": angle_residual,
        "mean_tau_by_flavour": {
            "nu_mu": mean_tau_mu,
            "nu_tau": mean_tau_tau,
            "combined_neutrino": mean_tau_nu,
            "all_channels": mean_tau_total,
        },
        "outer_r_ge_15km_mean_tau_by_flavour": {
            "nu_mu": mean_tau_mu_outer,
            "nu_tau": mean_tau_tau_outer,
            "combined_neutrino": mean_tau_nu_outer,
            "nu_mu_fraction_of_outer_neutrino_tau": (
                mean_tau_mu_outer/mean_tau_nu_outer if mean_tau_nu_outer else 0.0
            ),
            "nu_tau_fraction_of_outer_neutrino_tau": (
                mean_tau_tau_outer/mean_tau_nu_outer if mean_tau_nu_outer else 0.0
            ),
            "outer_neutrino_fraction_of_all_tau": (
                mean_tau_nu_outer/mean_tau_total if mean_tau_total else 0.0
            ),
        },
        "shell_mean_tau_by_flavour": shell_rows,
        "local_detailed_balance_samples": local_rows,
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
        "rate_sum_residual": result["flavour_rate_sum_max_relative_residual"],
        "column_sum_residual": result["flavour_column_sum_max_relative_residual"],
        "mean_tau_by_flavour": result["mean_tau_by_flavour"],
        "outer_mean_tau_by_flavour": result["outer_r_ge_15km_mean_tau_by_flavour"],
        "shells": result["shell_mean_tau_by_flavour"],
        "local_samples": result["local_detailed_balance_samples"],
        "couplings": result["representative_couplings"],
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
