"""Channel-resolved B.1 source and B.2 opacity decomposition for mV=10 MeV.

The script preserves the literal B.16 reference kernels and fixed-omega
Eq. (B.2) propagation. It separates neutrino inverse decay and no-recoil
semi-Compton source/opacity terms, then reports energy-binned escape weights.
It also checks the analytic Fermi-pair average against direct angular
quadrature at representative core radii and high energies.

This is a diagnostic of the existing pure-vector reference calculation.
It does not modify the axial-vector constraint curve or apply rescaling.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from scipy.special import expit
from numpy.polynomial.legendre import leggauss

from reference import (
    ALPHA, KM_TO_MEV_INV, MEV2_TO_ERG_S, M_MU,
    energy_weights, fermi_pair_average, load_profile, local_rates,
    radial_rule, scalar_optical_depths,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_BASELINE = HERE / "outputs" / "b16_global_high_order_independent_grid_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_channel_resolved_energy_10mev_2026-11-10.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source_measure(r, rw, energies, lapse, mass, production):
    """Eq. (B.1) source measure excluding the angular escape probability."""
    eweights = energy_weights(energies, mass / lapse)
    momentum = np.sqrt(np.maximum(energies**2 - mass**2, 0.0))
    geometry = (
        4.0 * np.pi * (r * KM_TO_MEV_INV)**2
        * rw * KM_TO_MEV_INV * lapse**2
    )
    spectral = momentum * energies**2 / (2.0 * np.pi**2)
    return (
        geometry[:, None] * eweights * spectral[None, :]
        * production * MEV2_TO_ERG_S
    )


def direct_pair_average(mu, omega, temperature, mass, order):
    """Independent 1/2 integral dcos(theta) f(E1,mu) f(E2,-mu)."""
    z, w = leggauss(order)
    velocity = np.sqrt(max(1.0 - (mass / omega)**2, 0.0))
    e1 = omega * (1.0 + velocity * z) / 2.0
    e2 = omega * (1.0 - velocity * z) / 2.0
    return float(0.5 * np.sum(
        w * expit((e1 - mu) / temperature)
        * expit((e2 + mu) / temperature)
    ))


def pair_average_audit(profile_path: Path, mass: float) -> dict:
    data = np.genfromtxt(profile_path, delimiter=",", names=True)
    radii = (8.0, 10.0, 12.5, 15.0)
    energies = (60.0, 110.0, 210.0, 510.0, 1010.0)
    orders = (128, 256, 512, 1024)
    rows = []
    for radius in radii:
        temperature = float(np.interp(radius, data["r_km"], data["T_MeV"]))
        mu_numu = float(np.interp(radius, data["r_km"], data["mu_numu_MeV"]))
        for omega in energies:
            velocity = np.sqrt(max(1.0 - (mass / omega)**2, 0.0))
            for species, mu in (("mu_numu", mu_numu), ("mu_zero", 0.0)):
                analytic = float(fermi_pair_average(mu, omega, temperature, velocity))
                direct = []
                for order in orders:
                    value = direct_pair_average(mu, omega, temperature, mass, order)
                    direct.append({
                        "order": order,
                        "value": value,
                        "relative_residual": value / analytic - 1.0,
                    })
                rows.append({
                    "radius_km": radius,
                    "temperature_MeV": temperature,
                    "mu_numu_MeV": mu_numu,
                    "energy_MeV": omega,
                    "species": species,
                    "analytic_pair_average": analytic,
                    "direct_angular_quadrature": direct,
                })
    max_residual = {
        str(order): max(
            abs(row["direct_angular_quadrature"][i]["relative_residual"])
            for row in rows
        )
        for i, order in enumerate(orders)
    }
    return {
        "method": "independent direct angular integral of f(E1,mu) f(E2,-mu)",
        "radii_km": list(radii),
        "energies_MeV": list(energies),
        "quadrature_orders": list(orders),
        "maximum_absolute_relative_residual_by_order": max_residual,
        "points": rows,
    }


def run(profile_path: Path, fig7_path: Path, baseline_path: Path,
        mass: float = 10.0, radial_order: int = 200,
        opacity_order: int = 640, energy_order: int = 200,
        angular_order: int = 32, path_order: int = 64,
        radius_km: float = 25.0, energy_offset: float = 1000.0) -> dict:
    fig7 = json.loads(fig7_path.read_text(encoding="utf-8"))
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))["result"]
    vertices = fig7["reference_vertices"][str(float(mass))]
    coupling = float(vertices["g"][-1])
    fig7_luminosity = float(vertices["luminosity_erg_s"][-1])
    baseline_point = baseline["eq_b2_fixed_omega_baseline"]["points"][-1]

    source_r, source_rw = radial_rule(radius_km, radial_order)
    opacity_r, _ = radial_rule(radius_km, opacity_order)
    opacity_grid = np.unique(np.r_[0.0, opacity_r, radius_km])
    source_profile = load_profile(profile_path, source_r)
    opacity_profile = load_profile(profile_path, opacity_grid)

    energies = mass + np.geomspace(1.0e-5, energy_offset, energy_order)
    energies = np.unique(np.r_[energies, mass / opacity_profile["lapse"]])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()

    source_rates = local_rates(
        mass, energies[None, :], source_profile["T"][:, None],
        source_profile["mu_numu"][:, None], source_profile["mu_mu"][:, None]
    )
    opacity_rates = local_rates(
        mass, energies[None, :], opacity_profile["T"][:, None],
        opacity_profile["mu_numu"][:, None], opacity_profile["mu_mu"][:, None]
    )

    source_nu = source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        source_rates["neutrino_production"]
    )
    source_compton = source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        source_rates["compton_production"]
    )
    source_total = source_nu + source_compton

    # Split reduced absorption using the same detailed-balance factor as B.19.
    x = energies[None, :] / opacity_profile["T"][:, None]
    balance_factor = (
        -np.expm1(-x) * np.exp(np.minimum(x, 700.0))
    )
    reduced_nu = balance_factor * opacity_rates["neutrino_production"]
    reduced_compton = balance_factor * opacity_rates["compton_production"]
    columns_nu, angle_weights = scalar_optical_depths(
        source_r, opacity_grid, reduced_nu, mass, energies,
        radius_km, angular_order, path_order
    )
    columns_compton, angle_weights_compton = scalar_optical_depths(
        source_r, opacity_grid, reduced_compton, mass, energies,
        radius_km, angular_order, path_order
    )
    angle_residual = float(np.max(np.abs(angle_weights - angle_weights_compton)))
    if angle_residual > 1.0e-14:
        raise ArithmeticError("Channel-separated optical-depth calls changed angular weights")

    tau_nu = coupling**2 * columns_nu
    tau_compton = coupling**2 * columns_compton
    survival = np.exp(-(tau_nu + tau_compton))
    base_nu = source_nu[:, None, :] * angle_weights[None, :, None]
    base_compton = source_compton[:, None, :] * angle_weights[None, :, None]
    base = base_nu + base_compton
    escaped_nu = base_nu * survival
    escaped_compton = base_compton * survival
    escaped = escaped_nu + escaped_compton

    thin = float(np.sum(source_total))
    escaped_sum = float(np.sum(escaped))
    luminosity_thin = coupling**2 * thin
    luminosity_both = coupling**2 * escaped_sum

    # Opacity-only counterfactuals keep the B.1 source fixed.
    luminosity_nu_opacity_only = coupling**2 * float(np.sum(
        base * np.exp(-tau_nu)
    ))
    luminosity_compton_opacity_only = coupling**2 * float(np.sum(
        base * np.exp(-tau_compton)
    ))
    total_loss = luminosity_thin - luminosity_both
    shapley_nu = 0.5 * (
        (luminosity_thin - luminosity_nu_opacity_only)
        + (luminosity_compton_opacity_only - luminosity_both)
    )
    shapley_compton = 0.5 * (
        (luminosity_thin - luminosity_compton_opacity_only)
        + (luminosity_nu_opacity_only - luminosity_both)
    )

    edges = np.array([
        mass, mass + 1, mass + 2, mass + 3, mass + 5, mass + 7.5,
        mass + 10, mass + 15, mass + 20, mass + 30, mass + 50,
        mass + 100, mass + 200, mass + 500, energies[-1] * (1.0 + 1e-12)
    ])
    energy_bins = []
    for i, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
        mask = (
            (energies >= lo)
            & (energies <= hi if i == len(edges) - 2 else energies < hi)
        )
        if not np.any(mask):
            continue
        bnu = float(np.sum(source_nu[:, mask]))
        bco = float(np.sum(source_compton[:, mask]))
        enu = float(np.sum(escaped_nu[:, :, mask]))
        eco = float(np.sum(escaped_compton[:, :, mask]))
        b = bnu + bco
        e = enu + eco
        tau_nu_source = float(np.sum(base[:, :, mask] * tau_nu[:, :, mask]) / b)
        tau_co_source = float(np.sum(base[:, :, mask] * tau_compton[:, :, mask]) / b)
        tau_nu_escape = float(np.sum(escaped[:, :, mask] * tau_nu[:, :, mask]) / e)
        tau_co_escape = float(np.sum(escaped[:, :, mask] * tau_compton[:, :, mask]) / e)
        thin_bin = coupling**2 * b
        both_bin = coupling**2 * e
        nu_only_bin = coupling**2 * float(np.sum(
            base[:, :, mask] * np.exp(-tau_nu[:, :, mask])
        ))
        co_only_bin = coupling**2 * float(np.sum(
            base[:, :, mask] * np.exp(-tau_compton[:, :, mask])
        ))
        loss_nu = 0.5 * ((thin_bin - nu_only_bin) + (co_only_bin - both_bin))
        loss_co = 0.5 * ((thin_bin - co_only_bin) + (nu_only_bin - both_bin))
        energy_bins.append({
            "bin": f"{lo:g}-{hi:g} MeV",
            "source": {
                "neutrino_fraction_in_bin": bnu / b,
                "compton_fraction_in_bin": bco / b,
                "neutrino_fraction_of_global_source": bnu / thin,
                "compton_fraction_of_global_source": bco / thin,
            },
            "escaped": {
                "neutrino_fraction_in_bin": enu / e,
                "compton_fraction_in_bin": eco / e,
                "neutrino_fraction_of_global_escape": enu / escaped_sum,
                "compton_fraction_of_global_escape": eco / escaped_sum,
                "escape_probability": e / b,
            },
            "mean_tau": {
                "neutrino_source_weighted": tau_nu_source,
                "compton_source_weighted": tau_co_source,
                "total_source_weighted": tau_nu_source + tau_co_source,
                "neutrino_escape_weighted": tau_nu_escape,
                "compton_escape_weighted": tau_co_escape,
                "total_escape_weighted": tau_nu_escape + tau_co_escape,
            },
            "counterfactual_luminosity_erg_s": {
                "both_opacities": both_bin,
                "neutrino_opacity_only": nu_only_bin,
                "compton_opacity_only": co_only_bin,
                "optically_thin": thin_bin,
            },
            "opacity_loss_shapley_erg_s": {
                "neutrino": loss_nu, "compton": loss_co,
            },
        })

    core_mask = (source_r >= 8.0) & (source_r < 15.0)
    core_thin = float(np.sum(source_total[core_mask, :]))
    core_escape = float(np.sum(escaped[core_mask, :, :]))
    core_nu_thin = float(np.sum(source_nu[core_mask, :]))
    core_compton_thin = float(np.sum(source_compton[core_mask, :]))
    core_nu_escape = float(np.sum(escaped_nu[core_mask, :, :]))
    core_compton_escape = float(np.sum(escaped_compton[core_mask, :, :]))

    mean_tau_nu = float(np.sum(base * tau_nu) / thin)
    mean_tau_compton = float(np.sum(base * tau_compton) / thin)
    mean_tau_nu_escape = float(np.sum(escaped * tau_nu) / escaped_sum)
    mean_tau_compton_escape = float(np.sum(escaped * tau_compton) / escaped_sum)

    result = {
        "title": "10 MeV channel-resolved B.1 source and B.2 opacity decomposition",
        "status": "python_reference_script_for_reproduction",
        "mass_MeV": mass,
        "coupling": coupling,
        "fig7_reference_luminosity_erg_s": fig7_luminosity,
        "integrated": {
            "optically_thin_luminosity_erg_s": luminosity_thin,
            "calculated_luminosity_erg_s": luminosity_both,
            "relative_difference_vs_fig7": luminosity_both / fig7_luminosity - 1.0,
            "escape_probability": escaped_sum / thin,
            "source_channel_luminosity_fractions": {
                "neutrino": float(np.sum(source_nu) / thin),
                "compton": float(np.sum(source_compton) / thin),
            },
            "escaped_luminosity_channel_fractions": {
                "neutrino": float(np.sum(escaped_nu) / escaped_sum),
                "compton": float(np.sum(escaped_compton) / escaped_sum),
            },
            "escaped_luminosity_by_source_channel_erg_s": {
                "neutrino": coupling**2 * float(np.sum(escaped_nu)),
                "compton": coupling**2 * float(np.sum(escaped_compton)),
            },
        },
        "opacity_decomposition": {
            "mean_tau_source_weighted": {
                "neutrino": mean_tau_nu,
                "compton": mean_tau_compton,
                "total": mean_tau_nu + mean_tau_compton,
            },
            "mean_tau_escape_weighted": {
                "neutrino": mean_tau_nu_escape,
                "compton": mean_tau_compton_escape,
                "total": mean_tau_nu_escape + mean_tau_compton_escape,
            },
            "counterfactual_luminosity_erg_s": {
                "both_opacities": luminosity_both,
                "neutrino_opacity_only": luminosity_nu_opacity_only,
                "compton_opacity_only": luminosity_compton_opacity_only,
                "optically_thin": luminosity_thin,
            },
            "shapley_attribution_of_total_luminosity_suppression_erg_s": {
                "neutrino": shapley_nu, "compton": shapley_compton,
            },
            "shapley_fraction_of_suppression": {
                "neutrino": shapley_nu / total_loss,
                "compton": shapley_compton / total_loss,
            },
        },
        "core_8_15km": {
            "source_fraction": core_thin / thin,
            "escaped_fraction": core_escape / escaped_sum,
            "source_channel_fractions": {
                "neutrino": core_nu_thin / core_thin,
                "compton": core_compton_thin / core_thin,
            },
            "escaped_channel_fractions": {
                "neutrino": core_nu_escape / core_escape,
                "compton": core_compton_escape / core_escape,
            },
        },
        "energy_bins": energy_bins,
        "neutrino_pair_average_independent_angular_check": pair_average_audit(
            profile_path, mass
        ),
        "execution": {
            "engine": "Python/NumPy/SciPy reference implementation",
            "source_radial_order": radial_order,
            "source_radial_nodes": len(source_r),
            "opacity_radial_order": opacity_order,
            "opacity_radial_nodes": len(opacity_grid),
            "energy_order": energy_order,
            "energy_nodes": len(energies),
            "angular_order": angular_order,
            "path_order": path_order,
            "profile_sha256": sha256(profile_path),
            "fig7_sha256": sha256(fig7_path),
            "baseline_sha256": sha256(baseline_path),
            "angular_weight_sum": float(np.sum(angle_weights)),
            "max_channel_angle_weight_residual": angle_residual,
            "comparison_to_archived_B16_baseline": {
                "luminosity_relative_residual": luminosity_both / baseline_point["calculated_luminosity_erg_s"] - 1.0,
                "thin_luminosity_relative_residual": luminosity_thin / baseline_point["optically_thin_luminosity_erg_s"] - 1.0,
                "escape_probability_absolute_residual": escaped_sum / thin - baseline_point["escape_fraction"],
            },
        },
        "interpretation": [
            "Channel source fractions use the B.1 production terms and the same total B.2 survival factor.",
            "Opacity-only counterfactuals keep the total B.1 source fixed and are diagnostics, not alternative physical models.",
            "Shapley opacity-loss attribution symmetrizes the order dependence of removing the two opacity channels.",
            "The exact B.13 global source-plus-opacity replacement is a separate archived calculation; it is not mixed into this B.16 reference result.",
            "No empirical rescaling, profile modification, or axial-vector curve update is performed.",
        ],
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    args = parser.parse_args()
    result = run(args.profile, args.fig7, args.baseline, mass=args.mass)
    payload = {
        "result": result,
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "script_sha256": sha256(Path(__file__)),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "luminosity_erg_s": result["integrated"]["calculated_luminosity_erg_s"],
        "relative_difference_vs_fig7": result["integrated"]["relative_difference_vs_fig7"],
        "source_channel_fractions": result["integrated"]["source_channel_luminosity_fractions"],
        "opacity_shapley_fractions": result["opacity_decomposition"]["shapley_fraction_of_suppression"],
        "neutrino_pair_check_max": result["neutrino_pair_average_independent_angular_check"]["maximum_absolute_relative_residual_by_order"],
    }, indent=2))


if __name__ == "__main__":
    main()
