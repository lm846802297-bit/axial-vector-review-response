#!/usr/bin/env python3
"""Audit inverse-neutrino-decay absorption in the 15--25 km PNS envelope.

The diagnostic separates the nu_mu and nu_tau channels, checks the cold
(vacuum-decay) limit of the reduced opacity, resolves optical depth by
absorber radius and production radius, and tests the unresolved |mu_nu_mu|<1
MeV profile envelope. Opacity-only shell removal is explicitly diagnostic;
the chemical-potential envelope recomputes production and absorption together.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np

try:
    from .reference import (
        DEFAULT_PROFILE, MEV2_TO_ERG_S, KM_TO_MEV_INV,
        energy_weights, fermi_pair_average, load_profile, local_rates,
        radial_rule, scalar_optical_depths,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE, MEV2_TO_ERG_S, KM_TO_MEV_INV,
        energy_weights, fermi_pair_average, load_profile, local_rates,
        radial_rule, scalar_optical_depths,
    )

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_OUTPUT = HERE / "outputs" / "outer_neutrino_absorption_audit.json"
MASS_MEV = 10.0
G_HIGH = 4.171689650228597e-8
RMAX_KM = 25.0
SHELLS = [(0., 5.), (5., 10.), (10., 15.), (15., 20.), (20., 25.)]
SOURCE_BINS = SHELLS


def build_state(profile_path, nr=40, ne=100, na=16, ns=32,
                mass=MASS_MEV, energy_offset=1000.0, mu_outer=None,
                mu_nutau_outer=None):
    r, rw = radial_rule(RMAX_KM, nr)
    radial_grid = np.unique(np.r_[0.0, r, RMAX_KM])
    p = load_profile(profile_path, radial_grid)
    if mu_outer is not None:
        p["mu_numu"] = p["mu_numu"].copy()
        p["mu_numu"][radial_grid >= 15.0] = float(mu_outer)

    energies = mass + np.geomspace(
        max(mass * 1e-6, 1e-6), energy_offset, ne)
    energies = np.unique(np.r_[energies, mass / p["lapse"]])
    energies = energies[energies > mass * (1.0 + 1e-10)]
    energies.sort()

    rates = local_rates(
        mass, energies[None, :], p["T"][:, None],
        p["mu_numu"][:, None], p["mu_mu"][:, None])
    velocity = np.sqrt(np.maximum(1.0 - (mass / energies)**2, 0.0))
    prefactor = mass**2 / (8.0 * np.pi * energies)
    mu_grid = p["mu_numu"][:, None]
    temp_grid = p["T"][:, None]
    v_grid = velocity[None, :]
    omega_grid = energies[None, :]
    i_numu = fermi_pair_average(mu_grid, omega_grid, temp_grid, v_grid)
    mu_nutau = np.zeros_like(p["mu_numu"])
    if mu_nutau_outer is not None:
        mu_nutau[radial_grid >= 15.0] = float(mu_nutau_outer)
    i_nutau = fermi_pair_average(
        mu_nutau[:, None], omega_grid, temp_grid, v_grid)
    i_nutau_zero = fermi_pair_average(
        np.zeros_like(mu_grid), omega_grid, temp_grid, v_grid)
    nu_numu_prod = prefactor[None, :] * i_numu
    nu_nutau_prod = prefactor[None, :] * i_nutau
    nu_nutau_zero_prod = prefactor[None, :] * i_nutau_zero
    x = omega_grid / temp_grid
    db_factor = (-np.expm1(-x)) * np.exp(np.minimum(x, 700.0))
    nu_numu_red = nu_numu_prod * db_factor
    nu_nutau_red = nu_nutau_prod * db_factor
    nu_nutau_zero_red = nu_nutau_zero_prod * db_factor
    nu_total_red = nu_numu_red + nu_nutau_red
    comp_red = rates["compton_production"] * db_factor
    dimu_red = rates["dimuon_production"] * db_factor
    total_red = nu_total_red + comp_red + dimu_red
    # local_rates contains the baseline zero-chemical-potential nu_tau
    # channel. Add only the change induced by the synthetic tau profile.
    expected_total_red = (
        rates["reduced_absorption"]
        + nu_nutau_red - nu_nutau_zero_red
    )
    mismatch = np.max(np.abs(total_red - expected_total_red)
                      / np.maximum(np.abs(total_red), 1e-300))
    if mismatch > 2e-11:
        raise AssertionError(f"Split reduced opacity fails total-rate identity: {mismatch}")

    source_index = np.searchsorted(radial_grid, r)
    lapse = p["lapse"][source_index]
    production = rates["production"][source_index]
    lower = mass / lapse
    eweights = energy_weights(energies, lower)
    momentum = np.sqrt(np.maximum(energies**2 - mass**2, 0.0))
    geometry = (4.0 * np.pi * (r * KM_TO_MEV_INV)**2
                * rw * KM_TO_MEV_INV * lapse**2)
    phase_space = momentum * energies**2 / (2.0 * np.pi**2)
    source = (geometry[:, None] * eweights * phase_space[None, :]
              * production * MEV2_TO_ERG_S)

    return {
        "r": r, "rw": rw, "radial_grid": radial_grid, "profile": p,
        "energies": energies, "rates": rates, "velocity": velocity,
        "i_numu": i_numu, "i_nutau": i_nutau,
        "mu_nutau": mu_nutau,
        "nu_numu_prod": nu_numu_prod, "nu_nutau_prod": nu_nutau_prod,
        "nu_numu_red": nu_numu_red, "nu_nutau_red": nu_nutau_red,
        "nu_total_red": nu_total_red, "comp_red": comp_red,
        "dimu_red": dimu_red, "total_red": total_red, "source": source,
        "mass": mass, "na": na, "ns": ns,
        "rate_split_max_relative_residual": float(mismatch),
    }


def opacity_columns(state, reduced):
    return scalar_optical_depths(
        state["r"], state["radial_grid"], reduced,
        state["mass"], state["energies"], RMAX_KM,
        state["na"], state["ns"])


def luminosity(state, reduced_total, coupling=G_HIGH):
    columns, angle_weights = opacity_columns(state, reduced_total)
    escape = np.einsum(
        "rae,a->re", np.exp(-coupling**2 * columns), angle_weights)
    return float(coupling**2 * np.sum(state["source"] * escape))


def shell_masks(radial_grid):
    return {
        f"{lo:g}-{hi:g}km": (
            (radial_grid >= lo)
            & ((radial_grid < hi) if hi < RMAX_KM else (radial_grid <= hi)))
        for lo, hi in SHELLS
    }


def optical_depth_decomposition(state, coupling=G_HIGH):
    masks = shell_masks(state["radial_grid"])
    columns_by_channel = {}
    for channel, reduced in (
        ("numu", state["nu_numu_red"]),
        ("nutau", state["nu_nutau_red"]),
        ("neutrino_total", state["nu_total_red"]),
    ):
        columns_by_channel[channel] = {}
        for shell, mask in masks.items():
            shell_rate = np.where(mask[:, None], reduced, 0.0)
            columns, angles = opacity_columns(state, shell_rate)
            columns_by_channel[channel][shell] = columns

    # Source-weighted means are weighted by the actual luminosity source and
    # the isotropic emission-direction measure. They are not opacity-only means.
    weights = state["source"][:, None, :] * angles[None, :, None]
    total_weight = float(np.sum(weights))
    result = {"coupling": coupling, "source_weighted_mean_tau_by_absorber_shell": {},
              "source_weighted_mean_tau_by_production_and_absorber_shell": {}}
    for channel, shells in columns_by_channel.items():
        result["source_weighted_mean_tau_by_absorber_shell"][channel] = {}
        result["source_weighted_mean_tau_by_production_and_absorber_shell"][channel] = {}
        for absorber_shell, cols in shells.items():
            tau = coupling**2 * cols
            result["source_weighted_mean_tau_by_absorber_shell"][channel][absorber_shell] = (
                float(np.sum(weights * tau) / max(total_weight, 1e-300)))
            by_source = {}
            for lo, hi in SOURCE_BINS:
                smask = ((state["r"] >= lo)
                         & ((state["r"] < hi) if hi < RMAX_KM else (state["r"] <= hi)))
                w = weights[smask]
                denom = float(np.sum(w))
                by_source[f"{lo:g}-{hi:g}km"] = (
                    float(np.sum(w * tau[smask]) / denom) if denom > 0 else None)
            result["source_weighted_mean_tau_by_production_and_absorber_shell"][channel][absorber_shell] = by_source

    total_nu = sum(result["source_weighted_mean_tau_by_absorber_shell"]["neutrino_total"].values())
    outer_nu = sum(result["source_weighted_mean_tau_by_absorber_shell"]["neutrino_total"][k]
                   for k in ("15-20km", "20-25km"))
    result["outer_15_25_fraction_of_neutrino_mean_tau"] = (
        float(outer_nu / total_nu) if total_nu > 0 else None)
    return result


def local_kernel_table(state):
    radii = [15., 17., 18., 20., 22., 24., 25.]
    energies = [10.1, 12., 15., 20., 30., 50., 100.]
    rows = []
    for radius in radii:
        t = float(np.interp(radius, state["radial_grid"], state["profile"]["T"]))
        mu = float(np.interp(radius, state["radial_grid"], state["profile"]["mu_numu"]))
        for omega in energies:
            if omega <= state["mass"]:
                continue
            v = np.sqrt(1.0 - (state["mass"] / omega)**2)
            beta = omega / t
            i0 = float(fermi_pair_average(0.0, omega, t, v))
            ia = float(fermi_pair_average(mu, omega, t, v))
            cold_ratio_tau = (np.expm1(min(beta, 700.0)) * i0)
            cold_ratio_numu = (np.expm1(min(beta, 700.0)) * ia)
            rows.append({
                "r_km": radius, "T_MeV": t, "mu_numu_MeV_reconstructed": mu,
                "omega_MeV": omega, "omega_over_T": beta,
                "mu_numu_over_T": mu / t,
                "reduced_opacity_over_zeroT_limit_numu": cold_ratio_numu,
                "reduced_opacity_over_zeroT_limit_nutau": cold_ratio_tau,
                "numu_to_zero_mu_ratio": ia / i0 if i0 > 0 else None,
            })
    return rows


def muon_neutrino_envelope(profile_path, couplings=(G_HIGH,)):
    variants = [("baseline", None), ("outer_mu0", 0.0),
                ("outer_mu1", 1.0), ("outer_mu2", 2.0)]
    rows = []
    for label, mu_outer in variants:
        state = build_state(profile_path, mu_outer=mu_outer)
        l = luminosity(state, state["total_red"], couplings[0])
        tau = optical_depth_decomposition(state, couplings[0])
        rows.append({
            "variant": label,
            "mu_numu_override_for_r_ge_15_km_MeV": mu_outer,
            "luminosity_erg_s": l,
            "relative_to_baseline": None,
            "outer_15_25_fraction_of_neutrino_mean_tau":
                tau["outer_15_25_fraction_of_neutrino_mean_tau"],
        })
    base = rows[0]["luminosity_erg_s"]
    for row in rows:
        row["relative_to_baseline"] = row["luminosity_erg_s"] / base - 1.0
    return rows


def tau_neutrino_outer_profile_envelope(profile_path, coupling=G_HIGH):
    """Stress-test the unplotted nu_tau chemical potential outside 15 km.

    The public Caputo profile contains mu_nu_mu but no separate mu_nu_tau
    curve. Zero is the current baseline; nonzero constants are diagnostics,
    not claims about the underlying Garching simulation.
    """
    variants = [("baseline_mu_nutau_zero", 0.0),
                ("outer_mu_nutau_1MeV", 1.0),
                ("outer_mu_nutau_2MeV", 2.0),
                ("outer_mu_nutau_5MeV", 5.0),
                ("outer_mu_nutau_10MeV", 10.0)]
    rows = []
    for label, value in variants:
        state = build_state(profile_path, mu_nutau_outer=value)
        lum = luminosity(state, state["total_red"], coupling)
        tau = optical_depth_decomposition(state, coupling)
        rows.append({
            "variant": label,
            "mu_nutau_override_for_r_ge_15_km_MeV": value,
            "luminosity_erg_s": lum,
            "relative_to_baseline": None,
            "outer_15_25_fraction_of_neutrino_mean_tau":
                tau["outer_15_25_fraction_of_neutrino_mean_tau"],
        })
    base = rows[0]["luminosity_erg_s"]
    for row in rows:
        row["relative_to_baseline"] = row["luminosity_erg_s"] / base - 1.0
    return rows


def opacity_only_shell_tests(state, coupling=G_HIGH):
    base = luminosity(state, state["total_red"], coupling)
    masks = shell_masks(state["radial_grid"])
    cases = [("baseline", {})]
    for shell in ("15-20km", "20-25km"):
        cases.extend([
            (f"remove_neutrino_pair_absorption_{shell}", {shell: 0.0}),
            (f"half_neutrino_pair_absorption_{shell}", {shell: 0.5}),
            (f"double_neutrino_pair_absorption_{shell}", {shell: 2.0}),
        ])
    cases.append(("remove_neutrino_pair_absorption_15-25km",
                  {"15-20km": 0.0, "20-25km": 0.0}))
    rows = []
    for label, scales in cases:
        reduced = state["total_red"].copy()
        for shell, scale in scales.items():
            mask = masks[shell]
            reduced[mask, :] += (scale - 1.0) * state["nu_total_red"][mask, :]
        l = luminosity(state, reduced, coupling)
        rows.append({
            "case": label, "shell_opacity_scales": scales,
            "luminosity_erg_s": l, "relative_to_baseline": l / base - 1.0,
            "warning": "Opacity-only perturbation; not a physical profile variation."
        })
    return rows


def quadrature_check(profile_path, couplings=(G_HIGH,)):
    cases = [
        ("baseline_40_16_32", 40, 16, 32),
        ("double_angular_path_40_32_64", 40, 32, 64),
        ("triple_angular_path_40_48_96", 40, 48, 96),
        ("double_radial_and_angular_path_80_32_64", 80, 32, 64),
    ]
    rows = []
    for label, nr, na, ns in cases:
        state = build_state(profile_path, nr=nr, na=na, ns=ns)
        l = luminosity(state, state["total_red"], couplings[0])
        rows.append({"case": label, "nr": nr, "na": na, "ns": ns,
                     "luminosity_erg_s": l})
    base = rows[0]["luminosity_erg_s"]
    for row in rows:
        row["relative_to_baseline"] = row["luminosity_erg_s"] / base - 1.0
    return rows


def run(profile_path):
    state = build_state(profile_path)
    decomp = optical_depth_decomposition(state)
    return {
        "title": "Outer 15--25 km neutrino inverse-decay absorption audit",
        "status": "diagnostic_complete_not_a_curve_fit",
        "source": "Blinov et al., arXiv:2511.09619v2, Appendix B, Eqs. (B1)--(B10)",
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "profile_sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
        "quadrature": {"nr": 40, "ne": 100, "na": 16, "ns": 32,
                       "Rmax_km": RMAX_KM},
        "model": {
            "mass_MeV": MASS_MEV, "coupling_high_absorption": G_HIGH,
            "nu_mu_profile_source": "Caputo Fig. 1; |mu_numu| curves are digitized only while >=1 MeV",
            "outer_mu_numu_baseline": "zero-filled where the public logarithmic plot does not resolve |mu_numu|<1 MeV",
            "nu_tau_assumption": "mu_nu_tau=0, as in the existing two-flavor implementation",
            "outer_temperature": "Caputo public PDF vector path through 25 km; no fitted tail",
        },
        "rate_split_max_relative_residual": state["rate_split_max_relative_residual"],
        "local_kernel_and_cold_limit_checks": local_kernel_table(state),
        "optical_depth_decomposition": decomp,
        "mu_numu_outer_profile_envelope": muon_neutrino_envelope(profile_path),
        "mu_nutau_outer_profile_stress_test": tau_neutrino_outer_profile_envelope(profile_path),
        "opacity_only_shell_sensitivity": opacity_only_shell_tests(state),
        "quadrature_convergence": quadrature_check(profile_path),
        "interpretation": [
            "The inverse-decay reduced opacity is split into nu_mu and nu_tau channels and summed back to the existing total reduced opacity; the rate identity is checked numerically.",
            "At low outer temperatures the reduced opacity approaches the time-dilated vacuum-decay limit. Therefore a falling T(r) does not make the outer neutrino absorption vanish.",
            "The public Caputo plot resolves |mu_nu_mu| only above about 1 MeV. The zero-filled outer tail is an input convention, not an exact raw-profile statement; constant 1 and 2 MeV outer envelopes quantify its effect with production and absorption recomputed together.",
            "No separate mu_nu_tau curve is present in the public Caputo profile. The baseline sets mu_nu_tau=0; constant 1, 2, 5 and 10 MeV outer stress tests quantify sensitivity but are not alternative physical profiles.",
            "The absorber-shell optical-depth table is weighted over the actual production source, emitted energies, and isotropic directions. It distinguishes absorber radius from production radius.",
            "Opacity-only shell removal is a diagnostic decomposition and is not a physical alternative prediction.",
            "No arbitrary opacity multiplier or fitted profile is adopted.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.profile)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "outer_fraction": result["optical_depth_decomposition"]["outer_15_25_fraction_of_neutrino_mean_tau"],
        "mu_numu_envelope": result["mu_numu_outer_profile_envelope"],
        "opacity_shell_tests": result["opacity_only_shell_sensitivity"],
        "quadrature": result["quadrature_convergence"],
    }, indent=2))


if __name__ == "__main__":
    main()
