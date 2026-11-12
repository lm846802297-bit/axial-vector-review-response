#!/usr/bin/env python3
"""P1-B.2 source-frozen high-energy thermodynamic-input sensitivity audit.

The B.1 source is evaluated once on the frozen profile. The script then changes
only B.2 opacity inputs in 8--15 km and recomputes the 210--510 MeV escape
integral. It uses the independent scalar reference module, not production
rates.py or transport.py.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from reference import (
    DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S,
    decay_production, compton_production,
    negative_muon_density_and_degeneracy,
    radial_rule, load_profile, energy_weights, scalar_optical_depths,
)

MASS_MEV = 10.0
COUPLING = 4.171689650228597e-8
RADIUS_KM = 25.0
BAND = (210.0, 510.0)
SOURCE_ORDER = 200
OPACITY_ORDER = 640
ENERGY_ORDER = 200
ENERGY_OFFSET_MEV = 1000.0
ANGLE_ORDER = 32
PATH_ORDER = 64
PERTURBATION_SHELL = (8.0, 15.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def b1_measure(radius, radial_weights, energies, lapse, production, mass):
    weights = energy_weights(energies, mass / lapse)
    momentum = np.sqrt(np.maximum(energies**2 - mass**2, 0.0))
    geometry = (
        4.0 * np.pi * (radius * KM_TO_MEV_INV)**2
        * radial_weights * KM_TO_MEV_INV * lapse**2
    )
    phase_space = momentum * energies**2 / (2.0 * np.pi**2)
    return (
        geometry[:, None] * weights * phase_space[None, :]
        * production * MEV2_TO_ERG_S
    )


def build_source(profile_path: Path):
    source_r, source_rw = radial_rule(RADIUS_KM, SOURCE_ORDER)
    opacity_nodes, _ = radial_rule(RADIUS_KM, OPACITY_ORDER)
    radial_grid = np.unique(np.r_[0.0, opacity_nodes, RADIUS_KM])
    opacity_profile = load_profile(profile_path, radial_grid)
    energies = MASS_MEV + np.geomspace(
        max(MASS_MEV * 1.0e-6, 1.0e-6), ENERGY_OFFSET_MEV, ENERGY_ORDER
    )
    energies = np.unique(np.r_[energies, MASS_MEV / opacity_profile["lapse"]])
    energies = energies[energies > MASS_MEV * (1.0 + 1.0e-10)]
    energies.sort()

    source_profile = load_profile(profile_path, source_r)
    n_mu, f_deg = negative_muon_density_and_degeneracy(
        source_profile["T"], source_profile["mu_mu"]
    )
    neutrino, dimuon = decay_production(
        MASS_MEV, energies[None, :],
        source_profile["T"][:, None],
        source_profile["mu_numu"][:, None],
        source_profile["mu_mu"][:, None],
    )
    compton = compton_production(
        MASS_MEV, energies[None, :],
        source_profile["T"][:, None],
        n_mu[:, None], f_deg[:, None],
    )
    lapse = source_profile["lapse"]
    source_nu = b1_measure(
        source_r, source_rw, energies, lapse, neutrino, MASS_MEV
    )
    source_compton = b1_measure(
        source_r, source_rw, energies, lapse, compton, MASS_MEV
    )
    source_dimuon = b1_measure(
        source_r, source_rw, energies, lapse, dimuon, MASS_MEV
    )
    return (
        source_r, radial_grid, opacity_profile, energies,
        source_nu, source_compton, source_dimuon,
    )


def opacity_channels(profile, energies):
    n_mu, f_deg = negative_muon_density_and_degeneracy(
        profile["T"], profile["mu_mu"]
    )
    neutrino, dimuon = decay_production(
        MASS_MEV, energies[None, :],
        profile["T"][:, None],
        profile["mu_numu"][:, None],
        profile["mu_mu"][:, None],
    )
    compton = compton_production(
        MASS_MEV, energies[None, :],
        profile["T"][:, None],
        n_mu[:, None], f_deg[:, None],
    )
    x = energies[None, :] / profile["T"][:, None]
    factor = np.expm1(np.minimum(x, 700.0))
    return {
        "neutrino": factor * neutrino,
        "compton": factor * compton,
        "total": factor * (neutrino + dimuon + compton),
    }


def evaluate_scenario(name, scale_T, scale_numu, scale_mumu, *,
                      profile, radial_grid, source_r, source_band,
                      energies_band, coupling):
    varied = {key: np.array(value, copy=True)
              for key, value in profile.items()}
    mask = (
        (radial_grid >= PERTURBATION_SHELL[0])
        & (radial_grid <= PERTURBATION_SHELL[1])
    )
    varied["T"][mask] *= scale_T
    varied["mu_numu"][mask] *= scale_numu
    varied["mu_mu"][mask] *= scale_mumu

    channels = opacity_channels(varied, energies_band)
    columns, angle_weights = scalar_optical_depths(
        source_r, radial_grid, channels["total"],
        MASS_MEV, energies_band, RADIUS_KM, ANGLE_ORDER, PATH_ORDER,
    )
    columns_nu, _ = scalar_optical_depths(
        source_r, radial_grid, channels["neutrino"],
        MASS_MEV, energies_band, RADIUS_KM, ANGLE_ORDER, PATH_ORDER,
    )
    columns_compton, _ = scalar_optical_depths(
        source_r, radial_grid, channels["compton"],
        MASS_MEV, energies_band, RADIUS_KM, ANGLE_ORDER, PATH_ORDER,
    )

    g2 = coupling**2
    source_sum = float(np.sum(source_band))
    thin = g2 * source_sum
    escape_by_source = np.einsum(
        "rae,a->re", np.exp(-g2 * columns), angle_weights
    )
    luminosity = g2 * float(np.sum(source_band * escape_by_source))
    mean_tau_nu = float(np.sum(
        source_band[:, None, :] * columns_nu
        * angle_weights[None, :, None]
    ) / source_sum)
    mean_tau_compton = float(np.sum(
        source_band[:, None, :] * columns_compton
        * angle_weights[None, :, None]
    ) / source_sum)
    return {
        "name": name,
        "scale_T_8_15km": scale_T,
        "scale_mu_numu_8_15km": scale_numu,
        "scale_mu_mu_8_15km": scale_mumu,
        "source_frozen": True,
        "escaped_luminosity_erg_s": luminosity,
        "relative_change_vs_baseline": None,
        "escape_probability": luminosity / thin,
        "source_weighted_mean_tau_per_g2": {
            "neutrino": mean_tau_nu,
            "semi_compton": mean_tau_compton,
        },
    }


def run(profile_path: Path, coupling: float):
    (
        source_r, radial_grid, opacity_profile, energies,
        source_nu, source_compton, source_dimuon,
    ) = build_source(profile_path)
    mask = (energies >= BAND[0]) & (energies < BAND[1])
    energies_band = energies[mask]
    source_band = (
        source_nu[:, mask] + source_compton[:, mask] + source_dimuon[:, mask]
    )
    source_per_g2 = float(np.sum(source_band))
    thin = coupling**2 * source_per_g2
    scenarios = [
        ("baseline", 1.0, 1.0, 1.0),
        ("T_minus10pct", 0.9, 1.0, 1.0),
        ("T_plus10pct", 1.1, 1.0, 1.0),
        ("mu_numu_minus10pct", 1.0, 0.9, 1.0),
        ("mu_numu_plus10pct", 1.0, 1.1, 1.0),
        ("mu_mu_minus10pct_at_fixed_T", 1.0, 1.0, 0.9),
        ("mu_mu_plus10pct_at_fixed_T", 1.0, 1.0, 1.1),
        ("T_and_mu_mu_minus10pct_fixed_eta", 0.9, 1.0, 0.9),
        ("T_and_mu_mu_plus10pct_fixed_eta", 1.1, 1.0, 1.1),
    ]
    rows = [
        evaluate_scenario(
            name, st, sn, sm, profile=opacity_profile,
            radial_grid=radial_grid, source_r=source_r,
            source_band=source_band, energies_band=energies_band,
            coupling=coupling,
        )
        for name, st, sn, sm in scenarios
    ]
    baseline = rows[0]["escaped_luminosity_erg_s"]
    for row in rows:
        row["relative_change_vs_baseline"] = (
            row["escaped_luminosity_erg_s"] / baseline - 1.0
        )
    return {
        "title": "P1-B.2 source-frozen high-energy thermodynamic-input sensitivity",
        "mass_MeV": MASS_MEV,
        "coupling": coupling,
        "profile_sha256": sha256(profile_path),
        "profile_vertices": int(len(np.genfromtxt(
            profile_path, delimiter=",", names=True
        ))),
        "configuration": {
            "source_radial_nodes": int(len(source_r)),
            "opacity_radial_nodes": int(len(radial_grid)),
            "total_energy_nodes": int(len(energies)),
            "band_energy_nodes_MeV": energies_band.tolist(),
            "angular_order": ANGLE_ORDER,
            "path_order": PATH_ORDER,
            "energy_band_MeV": list(BAND),
            "opacity_perturbation_shell_km": list(PERTURBATION_SHELL),
            "propagation": "fixed omega, scalar B.2, Euclidean chord",
        },
        "source": {
            "per_g2": source_per_g2,
            "thin_band_luminosity_erg_s": thin,
            "neutrino_fraction": float(np.sum(source_nu[:, mask]) / source_per_g2),
            "semi_compton_fraction": float(np.sum(source_compton[:, mask]) / source_per_g2),
        },
        "results": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--coupling", type=float, default=COUPLING)
    parser.add_argument("--output", type=Path, default=(
        Path(__file__).resolve().parent / "outputs"
        / "b16_p1b2_thermodynamic_input_sensitivity_2026-11-10.json"
    ))
    args = parser.parse_args()
    result = run(args.profile, args.coupling)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "baseline_luminosity_erg_s": result["results"][0]["escaped_luminosity_erg_s"],
        "source_channel_fractions": {
            "neutrino": result["source"]["neutrino_fraction"],
            "semi_compton": result["source"]["semi_compton_fraction"],
        },
        "relative_changes": {
            row["name"]: row["relative_change_vs_baseline"]
            for row in result["results"]
        },
    }, indent=2))


if __name__ == "__main__":
    main()
