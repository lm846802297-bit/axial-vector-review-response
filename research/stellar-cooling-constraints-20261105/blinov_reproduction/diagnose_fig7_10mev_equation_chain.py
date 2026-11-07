"""Equation-by-equation numerical audit of the 10 MeV Blinov Fig. 7 tail.

No physical rate is rescaled. The script checks Eq. (31)-(33) local
semi-Compton inputs, Eq. (20) reduced opacity, Eq. (18) chord optical depth,
and Eq. (17) source measure/lapse/radius dependence. It evaluates only the
three representative couplings (weak, peak, high-absorption) for the
controlled transport variants.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import expit

try:
    from .reference import (
        DEFAULT_PROFILE, M_MU, ALPHA, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        energy_weights, load_profile, local_rates,
        negative_muon_density_and_degeneracy, fermi_pair_average, radial_rule,
        scalar_optical_depths,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE, M_MU, ALPHA, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        energy_weights, load_profile, local_rates,
        negative_muon_density_and_degeneracy, fermi_pair_average, radial_rule,
        scalar_optical_depths,
    )

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "fig7_10mev_equation_chain_audit.json"
MASS = 10.0


def _relative(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.max(np.abs(a-b) / np.maximum(np.abs(b), 1e-300)))


def _eqb10_direct_detailed_balance(profile_path):
    """Independent angular-integral check of neutrino Eq. (B10)."""
    data = np.genfromtxt(profile_path, delimiter=",", names=True)
    rows = []
    for radius in (0.0, 5.0, 10.0, 15.0, 20.0, 24.0):
        temperature = float(np.interp(radius, data["r_km"], data["T_MeV"]))
        mu_numu = float(np.interp(radius, data["r_km"], data["mu_numu_MeV"]))
        for omega in (10.5, 15.0, 30.0, 50.0):
            velocity = np.sqrt(1.0-(MASS/omega)**2)
            for flavour, mu in (("numu", mu_numu), ("nutau", 0.0)):
                def f1(z):
                    return expit((mu-omega*(1.0+velocity*z)/2.0)/temperature)
                def f2(z):
                    return expit((-mu-omega*(1.0-velocity*z)/2.0)/temperature)
                prod_direct = 0.5*quad(
                    lambda z: f1(z)*f2(z), -1.0, 1.0,
                    epsabs=1e-14, epsrel=2e-11)[0]
                abs_direct = 0.5*quad(
                    lambda z: (1.0-f1(z))*(1.0-f2(z)), -1.0, 1.0,
                    epsabs=1e-14, epsrel=2e-11)[0]
                prod_kernel = float(fermi_pair_average(
                    mu, omega, temperature, velocity))
                rows.append({
                    "r_km": radius, "flavour": flavour,
                    "T_MeV": temperature, "mu_MeV": mu,
                    "omega_MeV": omega,
                    "production_direct_angular": prod_direct,
                    "production_kernel": prod_kernel,
                    "production_relative_residual":
                        abs(prod_kernel-prod_direct)/max(abs(prod_direct),1e-300),
                    "detailed_balance_ratio": abs_direct/(
                        np.exp(omega/temperature)*max(prod_direct,1e-300)),
                    "detailed_balance_relative_residual": abs(
                        abs_direct/(np.exp(omega/temperature)
                                    *max(prod_direct,1e-300))-1.0),
                })
    return rows


def _profile_rate_and_source(profile_path, radius_km, nr, ne, energy_offset,
                             temperature_scale=1.0):
    r, rw = radial_rule(radius_km, nr)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
    p = load_profile(profile_path, radial_grid)
    p["T"] = p["T"] * temperature_scale
    energies = MASS + np.geomspace(1e-5, energy_offset, ne)
    energies = np.unique(np.r_[energies, MASS / p["lapse"]])
    energies = energies[energies > MASS * (1.0 + 1e-10)]
    energies.sort()

    rates = local_rates(
        MASS, energies[None, :], p["T"][:, None],
        p["mu_numu"][:, None], p["mu_mu"][:, None])
    x = energies[None, :] / p["T"][:, None]
    # Eq. (20), evaluated in a numerically stable form.
    reduced_direct = -np.expm1(-x) * rates["absorption"]
    reduced_neutrino = (
        -np.expm1(-x) * np.exp(np.minimum(x, 700.0))
        * rates["neutrino_production"])
    reduced_compton = (
        -np.expm1(-x) * np.exp(np.minimum(x, 700.0))
        * rates["compton_production"])
    reduced_from_prod = (
        -np.expm1(-x) * np.exp(np.minimum(x, 700.0))
        * rates["production"])
    eq20_residual = _relative(reduced_direct, reduced_from_prod)

    # Eq. (31)-(33): independently reconstruct the semi-Compton coefficient.
    velocity = np.sqrt(np.maximum(1.0-(MASS/energies)**2, 0.0))
    n_mu = rates["n_mu"]
    f_deg = rates["F_deg"]
    sigma = (8.0*np.pi*ALPHA*(1.0/(4.0*np.pi))/(3.0*M_MU**2)
             * (1.0+MASS**2/(2.0*energies**2))*velocity)
    bose = 1.0/np.expm1(np.minimum(energies[None, :]/p["T"][:, None], 700.0))
    reconstructed_compton = np.zeros_like(rates["compton_production"])
    mask = velocity > 0.0
    reconstructed_compton[:, mask] = (
        n_mu * f_deg
        * (2.0/velocity[mask])[None, :]
        * bose[:, mask] * sigma[mask][None, :])
    eq31_residual = _relative(
        reconstructed_compton, rates["compton_production"])

    # Eq. (17): d^3k/(2pi)^3 * omega, transformed from k to omega.
    # k^2 dk * omega = k omega^2 d omega.
    k = np.sqrt(np.maximum(energies**2-MASS**2, 0.0))
    measure_k = k * energies**2 / (2.0*np.pi**2)
    dk_domega = np.divide(energies, k, out=np.zeros_like(k), where=k > 0)
    measure_jacobian = k**2 * energies * dk_domega / (2.0*np.pi**2)
    eq17_jacobian_residual = _relative(
        measure_k[1:], measure_jacobian[1:])

    source_index = np.searchsorted(radial_grid, r)
    lapse = p["lapse"][source_index]
    lower = MASS/lapse
    eweights = energy_weights(energies, lower)
    phase_space = measure_k
    geometry = (4.0*np.pi*(r*KM_TO_MEV_INV)**2
                * rw*KM_TO_MEV_INV*lapse**2)
    source = (geometry[:, None] * eweights
              * phase_space[None, :] * rates["production"][source_index]
              * MEV2_TO_ERG_S)
    source_no_lapse2 = source / np.maximum(lapse[:, None]**2, 1e-300)
    return {
        "r": r, "rw": rw, "radial_grid": radial_grid, "profile": p,
        "energies": energies, "rates": rates,
        "reduced": reduced_direct,
        "reduced_neutrino": reduced_neutrino,
        "reduced_compton": reduced_compton,
        "source": source,
        "source_no_lapse2": source_no_lapse2,
        "eq20_residual": eq20_residual,
        "eq31_residual": eq31_residual,
        "eq17_jacobian_residual": eq17_jacobian_residual,
    }


def _luminosity_for_setup(setup, radius_km, na, ns, couplings):
    cols, angle_weights = scalar_optical_depths(
        setup["r"], setup["radial_grid"], setup["reduced"],
        MASS, setup["energies"], radius_km,
        angular_order=na, path_order=ns)
    escape_by_g = []
    for g in couplings:
        escape = np.einsum(
            "rae,a->re", np.exp(-g*g*cols), angle_weights)
        escape_by_g.append(float(g*g*np.sum(setup["source"]*escape)))
    return np.asarray(escape_by_g), cols


def _redshifted_optical_depths(setup, radius_km, angular_order, path_order):
    """Evaluate opacity with conserved E_infinity and local omega=E_inf/N(r')."""
    source_radii = setup["r"]
    radial_grid = setup["radial_grid"]
    energies = setup["energies"]
    reduced = setup["reduced"]
    lapse_grid = setup["profile"]["lapse"]
    source_index = np.searchsorted(radial_grid, source_radii)
    lapse_source = lapse_grid[source_index]

    angles, angle_weights = np.polynomial.legendre.leggauss(angular_order)
    angle_weights = angle_weights / 2.0
    path_x, path_w = np.polynomial.legendre.leggauss(path_order)
    path_w = path_w / 2.0
    columns = np.zeros((len(source_radii), len(angles), len(energies)))

    for ia, cosine in enumerate(angles):
        smax = -cosine*source_radii + np.sqrt(
            radius_km**2-source_radii**2+source_radii**2*cosine**2)
        s = smax[:, None]*(1.0+path_x[None, :])/2.0
        position = np.sqrt(np.maximum(
            source_radii[:, None]**2+s**2
            +2.0*source_radii[:, None]*s*cosine, 0.0))
        path_weights = smax[:, None]*path_w[None, :]
        lapse_path = np.interp(
            position.ravel(), radial_grid, lapse_grid).reshape(position.shape)

        for ie, omega_source in enumerate(energies):
            # E_inf=N(r_source)*omega_source is conserved along the ray.
            omega_path = omega_source*lapse_source[:, None]/lapse_path
            velocity_path = np.sqrt(np.maximum(
                1.0-(MASS/omega_path)**2, 0.0))

            # Bilinear interpolation of Gamma_red(r, omega_local).
            ir = np.searchsorted(radial_grid, position, side="right")-1
            ir = np.clip(ir, 0, len(radial_grid)-2)
            ie_local = np.searchsorted(energies, omega_path, side="right")-1
            ie_local = np.clip(ie_local, 0, len(energies)-2)
            r0, r1 = radial_grid[ir], radial_grid[ir+1]
            e0, e1 = energies[ie_local], energies[ie_local+1]
            fr = np.divide(position-r0, r1-r0,
                           out=np.zeros_like(position), where=(r1>r0))
            fe = np.divide(omega_path-e0, e1-e0,
                           out=np.zeros_like(omega_path), where=(e1>e0))
            q00 = reduced[ir, ie_local]
            q01 = reduced[ir, ie_local+1]
            q10 = reduced[ir+1, ie_local]
            q11 = reduced[ir+1, ie_local+1]
            rate = ((1.0-fr)*(1.0-fe)*q00
                    +(1.0-fr)*fe*q01
                    +fr*(1.0-fe)*q10
                    +fr*fe*q11)
            integrand = np.divide(
                rate, velocity_path,
                out=np.zeros_like(rate), where=velocity_path>0.0)
            columns[:, ia, ie] = np.sum(path_weights*integrand, axis=1)*KM_TO_MEV_INV

    return columns, angle_weights


def _eq33_finite_difference(profile_path):
    data = np.genfromtxt(profile_path, delimiter=",", names=True)
    samples = []
    for radius in (0.0, 5.0, 8.0, 10.0, 15.0, 20.0, 24.0):
        t = float(np.interp(radius, data["r_km"], data["T_MeV"]))
        mu = float(np.interp(radius, data["r_km"], data["mu_mu_MeV"]))
        n, fdeg = negative_muon_density_and_degeneracy(t, mu)
        step = max(1e-3, 1e-4*t)
        np_, _ = negative_muon_density_and_degeneracy(t, mu+step)
        nm_, _ = negative_muon_density_and_degeneracy(t, mu-step)
        # If chi = integral f(1-f), then T dn/dmu = chi = n F_deg.
        chi_fd = t*(float(np_)-float(nm_))/(2.0*step)
        chi_eq33 = float(n)*float(fdeg)
        samples.append({
            "r_km": radius, "T_MeV": t, "mu_mu_MeV": mu,
            "n_mu_MeV3": float(n), "F_deg": float(fdeg),
            "T_dn_dmu_finite_difference": chi_fd,
            "n_F_deg": chi_eq33,
            "relative_residual": abs(chi_fd-chi_eq33)/max(abs(chi_eq33),1e-300),
        })
    return samples


def run(profile_path, fig7_path, nr=88, ne=180, na=24, ns=64,
        energy_offset=1000.0):
    fig7 = json.loads(fig7_path.read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"]["10.0"]
    g_all = np.asarray(vertices["g"], float)
    l_ref_all = np.asarray(vertices["luminosity_erg_s"], float)
    idx = [0, int(np.argmax(l_ref_all)), len(g_all)-1]
    couplings = g_all[idx]
    reference = l_ref_all[idx]

    baseline = _profile_rate_and_source(
        profile_path, 25.0, nr, ne, energy_offset)
    l_base, cols_base = _luminosity_for_setup(
        baseline, 25.0, na, ns, couplings)
    cols_redshift, angle_weights_redshift = _redshifted_optical_depths(
        baseline, 25.0, na, ns)
    l_redshift = []
    for g in couplings:
        esc_redshift = np.einsum(
            "rae,a->re", np.exp(-g*g*cols_redshift),
            angle_weights_redshift)
        l_redshift.append(float(g*g*np.sum(baseline["source"]*esc_redshift)))
    l_redshift = np.asarray(l_redshift)
    temperature_sensitivity = []
    for tscale in (0.95, 1.0, 1.05):
        if tscale == 1.0:
            tsetup = baseline
        else:
            tsetup = _profile_rate_and_source(
                profile_path, 25.0, nr, ne, energy_offset,
                temperature_scale=tscale)
        t_luminosity, _ = _luminosity_for_setup(
            tsetup, 25.0, na, ns, couplings)
        for name, g, ref_lum, calc_lum in zip(
            ("weak", "reference_peak", "high_absorption"),
            couplings, reference, t_luminosity
        ):
            temperature_sensitivity.append({
                "temperature_scale": tscale,
                "point": name,
                "g": float(g),
                "calculated_luminosity_erg_s": float(calc_lum),
                "reference_luminosity_erg_s": float(ref_lum),
                "relative_residual": float(calc_lum/ref_lum-1.0),
            })

    # Radial source/escape decomposition: retain the same local rates and
    # transport, but integrate their contributions in five fixed radial shells.
    source_idx = np.searchsorted(baseline["radial_grid"], baseline["r"])
    total_prod = np.maximum(
        baseline["rates"]["production"][source_idx, :], 1e-300)
    channel_sources = {
        key: baseline["source"] * baseline["rates"][rate_key][source_idx, :]
        / total_prod
        for key, rate_key in (
            ("neutrino", "neutrino_production"),
            ("compton", "compton_production"),
            ("dimuon", "dimuon_production"))
    }
    radial_shells = []
    radial_edges = (0.0, 5.0, 10.0, 15.0, 20.0, 25.0)
    for point, g in zip(("weak", "reference_peak", "high_absorption"), couplings):
        escape = np.einsum(
            "rae,a->re", np.exp(-g*g*cols_base),
            np.polynomial.legendre.leggauss(na)[1]/2.0)
        for lo, hi in zip(radial_edges[:-1], radial_edges[1:]):
            mask = (baseline["r"] >= lo) & (baseline["r"] < hi if hi < 25 else baseline["r"] <= hi)
            row = {"point": point, "g": float(g),
                   "radial_bin_km": [lo, hi]}
            for channel, src in channel_sources.items():
                row[channel+"_thin_erg_s"] = float(g*g*np.sum(src[mask]))
                row[channel+"_escaped_erg_s"] = float(
                    g*g*np.sum(src[mask]*escape[mask]))
            row["total_thin_erg_s"] = float(
                sum(row[k+"_thin_erg_s"] for k in channel_sources))
            row["total_escaped_erg_s"] = float(
                sum(row[k+"_escaped_erg_s"] for k in channel_sources))
            radial_shells.append(row)

    # Decompose optical depth by the radius of the absorbing material along
    # each chord. This is distinct from the production-radius shell split above.
    opacity_path_shells = []
    path_edges = (0.0, 5.0, 10.0, 15.0, 20.0, 25.0)
    for channel, rate_key in (
        ("neutrino", "reduced_neutrino"),
        ("compton", "reduced_compton"),
    ):
        reduced_channel = baseline[rate_key]
        for lo, hi in zip(path_edges[:-1], path_edges[1:]):
            mask_path = (
                (baseline["radial_grid"] >= lo)
                & ((baseline["radial_grid"] < hi)
                   if hi < 25.0 else (baseline["radial_grid"] <= hi)))
            reduced_shell = np.where(
                mask_path[:, None], reduced_channel, 0.0)
            shell_columns, shell_angles = scalar_optical_depths(
                baseline["r"], baseline["radial_grid"], reduced_shell,
                MASS, baseline["energies"], 25.0,
                angular_order=na, path_order=ns)
            source_weights = baseline["source"][:, None, :] * shell_angles[None, :, None]
            norm = max(float(np.sum(source_weights)), 1e-300)
            for point, g in zip(
                ("weak", "reference_peak", "high_absorption"), couplings
            ):
                opacity_path_shells.append({
                    "channel": channel, "absorber_radius_bin_km": [lo, hi],
                    "point": point, "g": float(g),
                    "source_weighted_mean_tau_contribution": float(
                        np.sum(source_weights * (g*g*shell_columns))/norm),
                })

    # Split the neutrino inverse-decay opacity by flavour and test the
    # small/uncertain mu_nu_mu tail specifically in the outer PNS shells.
    omega_grid = baseline["energies"][None, :]
    temp_grid = baseline["profile"]["T"][:, None]
    mu_numu_grid = baseline["profile"]["mu_numu"][:, None]
    velocity_grid = np.sqrt(np.maximum(
        1.0-(MASS/omega_grid)**2, 0.0))
    x_grid = omega_grid/temp_grid
    balance_factor = (
        -np.expm1(-x_grid)*np.exp(np.minimum(x_grid, 700.0)))
    prefactor_nu = MASS*MASS/(8.0*np.pi*omega_grid)
    i_numu = fermi_pair_average(
        mu_numu_grid, omega_grid, temp_grid, velocity_grid)
    i_nutau = fermi_pair_average(
        np.zeros_like(mu_numu_grid), omega_grid, temp_grid, velocity_grid)
    reduced_numu = balance_factor*prefactor_nu*i_numu
    reduced_nutau = balance_factor*prefactor_nu*i_nutau
    flavour_opacity = []
    neutrino_flavour_sum_closure = _relative(
        reduced_numu+reduced_nutau, baseline["reduced_neutrino"])
    outer_mu_sensitivity = []
    source_weights = (
        baseline["source"][:, None, :]
        * np.polynomial.legendre.leggauss(na)[1][None, :, None]/2.0
    )
    source_norm = max(float(np.sum(source_weights)), 1e-300)
    for flavour, reduced_flavour in (
        ("numu", reduced_numu), ("nutau", reduced_nutau)
    ):
        for lo, hi in zip(path_edges[:-1], path_edges[1:]):
            mask_path = (
                (baseline["radial_grid"] >= lo)
                & ((baseline["radial_grid"] < hi)
                   if hi < 25.0 else (baseline["radial_grid"] <= hi)))
            reduced_shell = np.where(
                mask_path[:, None], reduced_flavour, 0.0)
            shell_columns, _ = scalar_optical_depths(
                baseline["r"], baseline["radial_grid"], reduced_shell,
                MASS, baseline["energies"], 25.0,
                angular_order=na, path_order=ns)
            flavour_opacity.append({
                "flavour": flavour, "absorber_radius_bin_km": [lo, hi],
                "high_absorption_g": float(couplings[-1]),
                "source_weighted_mean_tau_contribution": float(
                    np.sum(source_weights
                           * (couplings[-1]**2*shell_columns))/source_norm),
            })

    for scale_name, outer_scale in (
        ("zero_mu_numu_outer_r_ge_15km", 0.0),
        ("baseline_mu_numu_outer_r_ge_15km", 1.0),
        ("double_mu_numu_outer_r_ge_15km", 2.0),
    ):
        mu_variant = np.where(
            baseline["radial_grid"][:, None] >= 15.0,
            outer_scale*mu_numu_grid, mu_numu_grid)
        i_variant = fermi_pair_average(
            mu_variant, omega_grid, temp_grid, velocity_grid)
        reduced_variant = balance_factor*prefactor_nu*i_variant
        for lo, hi in ((15.0, 20.0), (20.0, 25.0)):
            mask_path = (
                (baseline["radial_grid"] >= lo)
                & ((baseline["radial_grid"] < hi)
                   if hi < 25.0 else (baseline["radial_grid"] <= hi)))
            reduced_shell = np.where(
                mask_path[:, None], reduced_variant, 0.0)
            shell_columns, _ = scalar_optical_depths(
                baseline["r"], baseline["radial_grid"], reduced_shell,
                MASS, baseline["energies"], 25.0,
                angular_order=na, path_order=ns)
            outer_mu_sensitivity.append({
                "scenario": scale_name,
                "absorber_radius_bin_km": [lo, hi],
                "high_absorption_g": float(couplings[-1]),
                "source_weighted_mean_tau_contribution": float(
                    np.sum(source_weights
                           * (couplings[-1]**2*shell_columns))/source_norm),
            })

    # Compare the reduced inverse-decay opacity with the vacuum decay
    # width in the outer PNS, where final-state neutrino blocking weakens.
    outer_local_absorption = []
    for target_r in (15.0, 20.0, 24.5):
        ir = int(np.argmin(np.abs(baseline["radial_grid"]-target_r)))
        tloc = float(baseline["profile"]["T"][ir])
        muloc = float(baseline["profile"]["mu_numu"][ir])
        for eloc in (10.1, 20.0, 50.0):
            vloc = float(np.sqrt(max(1.0-(MASS/eloc)**2, 0.0)))
            xloc = eloc/tloc
            bal = -np.expm1(-xloc)*np.exp(min(xloc, 700.0))
            i_mu_loc = float(fermi_pair_average(
                muloc, eloc, tloc, vloc))
            i_tau_loc = float(fermi_pair_average(
                0.0, eloc, tloc, vloc))
            pref_loc = MASS*MASS/(8.0*np.pi*eloc)
            vac_one_flavour = MASS*MASS/(24.0*np.pi*eloc)
            vac_polarization_sum = 3.0*vac_one_flavour
            outer_local_absorption.append({
                "r_km": float(baseline["radial_grid"][ir]),
                "T_MeV": tloc, "mu_numu_MeV": muloc,
                "omega_MeV": eloc, "omega_over_T": xloc,
                "numu_reduced_rate_over_polarization_summed_vacuum_width":
                    bal*pref_loc*i_mu_loc/vac_polarization_sum,
                "nutau_reduced_rate_over_polarization_summed_vacuum_width":
                    bal*pref_loc*i_tau_loc/vac_polarization_sum,
            })

    # Separate radial/energy quadrature and high-energy-cutoff convergence
    # diagnostics for the optically thin source and the escaped luminosity.
    quadrature_sensitivity = []
    variants = (
        ("radial_order_x2", 2*nr, ne, energy_offset),
        ("energy_order_x2", nr, 2*ne, energy_offset),
        ("energy_cutoff_x2", nr, ne, 2.0*energy_offset),
    )
    for variant, nrv, nev, eoff in variants:
        setup = _profile_rate_and_source(
            profile_path, 25.0, nrv, nev, eoff)
        lum, _ = _luminosity_for_setup(setup, 25.0, na, ns, couplings)
        thin = np.array([g*g*np.sum(setup["source"]) for g in couplings])
        for point, g, l0, lv, thin0, thinv in zip(
            ("weak", "reference_peak", "high_absorption"),
            couplings, l_base, lum,
            np.array([g*g*np.sum(baseline["source"]) for g in couplings]),
            thin
        ):
            quadrature_sensitivity.append({
                "variant": variant, "point": point, "g": float(g),
                "baseline_luminosity_erg_s": float(l0),
                "variant_luminosity_erg_s": float(lv),
                "relative_luminosity_change": float(lv/l0-1.0),
                "baseline_thin_source_erg_s": float(thin0),
                "variant_thin_source_erg_s": float(thinv),
                "relative_thin_source_change": float(thinv/thin0-1.0),
            })

    l_path2, cols_path2 = _luminosity_for_setup(
        baseline, 25.0, na, 2*ns, couplings)
    l_angle2, cols_angle2 = _luminosity_for_setup(
        baseline, 25.0, 2*na, ns, couplings)

    # Compare angle-averaged columns because the raw arrays have different
    # angular axes when the quadrature order changes.
    tau_angle_base = np.einsum(
        "rae,a->re", cols_base, np.polynomial.legendre.leggauss(na)[1]/2.0)
    tau_angle_refined = np.einsum(
        "rae,a->re", cols_angle2, np.polynomial.legendre.leggauss(2*na)[1]/2.0)

    # Boundary diagnostic with identical source nodes and local rates:
    # only shorten the outward propagation boundary from 25 to 24 km.
    inner_mask = baseline["r"] <= 24.0
    inner_r = baseline["r"][inner_mask]
    cols24_same_source, angle_weights24 = scalar_optical_depths(
        inner_r, baseline["radial_grid"], baseline["reduced"],
        MASS, baseline["energies"], 24.0,
        angular_order=na, path_order=ns)
    cols25_same_source = cols_base[inner_mask]
    angle_weights25 = np.polynomial.legendre.leggauss(na)[1] / 2.0
    cols_nu25, _ = scalar_optical_depths(
        baseline["r"], baseline["radial_grid"], baseline["reduced_neutrino"],
        MASS, baseline["energies"], 25.0,
        angular_order=na, path_order=ns)
    cols_nu24, _ = scalar_optical_depths(
        inner_r, baseline["radial_grid"], baseline["reduced_neutrino"],
        MASS, baseline["energies"], 24.0,
        angular_order=na, path_order=ns)
    cols_nu25_inner = cols_nu25[inner_mask]
    cols_nu24_inner = cols_nu24
    cols_compton25_inner = np.maximum(cols25_same_source-cols_nu25_inner, 0.0)
    cols_compton24_inner = np.maximum(cols24_same_source-cols_nu24_inner, 0.0)
    source_inner = baseline["source"][inner_mask]
    shell_tau_unit = np.maximum(cols25_same_source-cols24_same_source, 0.0)
    l24_same_source = []
    l25_same_source = []
    shell_tau_stats = []
    for g in couplings:
        esc24 = np.einsum(
            "rae,a->re", np.exp(-g*g*cols24_same_source), angle_weights24)
        esc25 = np.einsum(
            "rae,a->re", np.exp(-g*g*cols25_same_source), angle_weights25)
        l24_same_source.append(float(g*g*np.sum(source_inner*esc24)))
        l25_same_source.append(float(g*g*np.sum(source_inner*esc25)))
        weights_tau = source_inner[:, None, :] * angle_weights25[None, :, None]
        tau_shell = g*g*shell_tau_unit
        shell_tau_nu = g*g*np.maximum(cols_nu25_inner-cols_nu24_inner, 0.0)
        shell_tau_compton = g*g*np.maximum(
            cols_compton25_inner-cols_compton24_inner, 0.0)
        shell_tau_stats.append({
            "g": float(g),
            "source_weighted_mean_extra_tau_24_25": float(
                np.average(tau_shell, weights=weights_tau)),
            "source_weighted_mean_extra_tau_neutrino": float(
                np.average(shell_tau_nu, weights=weights_tau)),
            "source_weighted_mean_extra_tau_compton": float(
                np.average(shell_tau_compton, weights=weights_tau)),
            "source_weighted_mean_total_tau_25km": float(
                np.average(g*g*cols25_same_source, weights=weights_tau)),
            "source_weighted_mean_tau_neutrino_25km": float(
                np.average(g*g*cols_nu25_inner, weights=weights_tau)),
            "source_weighted_mean_tau_compton_25km": float(
                np.average(g*g*cols_compton25_inner, weights=weights_tau)),
        })
    l24_same_source = np.asarray(l24_same_source)
    l25_same_source = np.asarray(l25_same_source)

    # Source-only (optically thin) Eq. (17) diagnostics.
    thin25 = np.array([g*g*np.sum(baseline["source"]) for g in couplings])
    thin24 = np.array([g*g*np.sum(
        baseline["source"][baseline["r"] <= 24.0]) for g in couplings])
    thin25_no_lapse2 = np.array([
        g*g*np.sum(baseline["source_no_lapse2"]) for g in couplings])

    eq18 = {
        "path_order_comparison": [
            {"g": float(g), "L_path_base": float(a), "L_path_2x": float(b),
             "relative_change": float(b/a-1.0)}
            for g, a, b in zip(couplings, l_base, l_path2)
        ],
        "angular_order_comparison": [
            {"g": float(g), "L_angle_base": float(a), "L_angle_2x": float(b),
             "relative_change": float(b/a-1.0)}
            for g, a, b in zip(couplings, l_base, l_angle2)
        ],
        "column_path_max_relative_difference": _relative(cols_path2, cols_base),
        "angle_averaged_column_max_relative_difference":
            _relative(tau_angle_refined, tau_angle_base),
        "gravitational_redshift_along_path": [
            {"g": float(g), "L_fixed_local_omega": float(a),
             "L_conserved_Einf": float(b),
             "relative_change": float(b/a-1.0)}
            for g, a, b in zip(couplings, l_base, l_redshift)
        ],
        "redshifted_column_max_relative_difference":
            _relative(cols_redshift, cols_base),
        "redshift_convention": (
            "Diagnostic: E_inf=N(r_source)*omega_source is conserved; "
            "the local energy along the path is omega(r')=E_inf/N(r'). "
            "This tests the gravitational redshift stated in Appendix B; "
            "the fixed-local-omega result is retained as the literal baseline."
        ),
        "interpretation": "Quadrature-only changes and a separate GR redshift diagnostic; no opacity normalization is altered.",
    }
    eq17 = {
        "global_temperature_profile_scale_sensitivity": temperature_sensitivity,
        "radial_shell_source_and_escape_decomposition": radial_shells,
        "absorber_radius_shell_optical_depth_decomposition": opacity_path_shells,
        "neutrino_flavour_absorption_by_shell": flavour_opacity,
        "neutrino_flavour_sum_closure_max_relative_residual": neutrino_flavour_sum_closure,
        "outer_mu_numu_absorption_sensitivity": outer_mu_sensitivity,
        "outer_neutrino_absorption_vs_vacuum_width": outer_local_absorption,
        "radial_energy_cutoff_quadrature_sensitivity": quadrature_sensitivity,
        "same_source_nodes_boundary_24_vs_25_km": [
            {"g": float(g), "L_R24_same_sources": float(a),
             "L_R25_same_sources": float(b),
             "relative_change_R24_over_R25": float(a/b-1.0),
             "thin_R24_source_mask": float(c), "thin_R25_full": float(d)}
            for g, a, b, c, d in zip(
                couplings, l24_same_source, l25_same_source, thin24, thin25)
        ],
        "extra_outer_shell_opacity_24_25_km": shell_tau_stats,
        "omit_lapse_squared_diagnostic_only": [
            {"g": float(g), "L_with_N2_thin": float(a),
             "L_without_N2_thin": float(b),
             "ratio_without_over_with": float(b/a)}
            for g, a, b in zip(couplings, thin25, thin25_no_lapse2)
        ],
        "energy_measure_jacobian_max_relative_residual":
            baseline["eq17_jacobian_residual"],
        "interpretation": (
            "N(r)^2 is retained as required by the luminosity-at-infinity "
            "prescription. Removing it is a diagnostic, not an alternative."
        ),
    }
    source_idx = np.searchsorted(baseline["radial_grid"], baseline["r"])
    source_den = np.maximum(
        baseline["rates"]["production"][source_idx, :], 1e-300)
    source_channel_fractions = {}
    for key, rate_key in (
        ("neutrino", "neutrino_production"),
        ("compton", "compton_production"),
        ("dimuon", "dimuon_production"),
    ):
        channel_source = (
            baseline["source"]
            * baseline["rates"][rate_key][source_idx, :] / source_den)
        source_channel_fractions[key] = float(
            np.sum(channel_source) / max(np.sum(baseline["source"]), 1e-300))
    eq31_33 = {
        "compton_rate_reconstruction_max_relative_residual":
            baseline["eq31_residual"],
        "eq33_susceptibility_finite_difference": _eq33_finite_difference(profile_path),
        "eqb10_direct_angular_detailed_balance": _eqb10_direct_detailed_balance(profile_path),
        "source_channel_fractions_optically_thin": source_channel_fractions,
        "interpretation": (
            "The finite-difference identity tests F_deg = (T/n_mu) "
            "dn_mu/dmu_mu. The Compton reconstruction checks the literal "
            "Eq. (31)-(33) algebra in the local kernel."
        ),
    }
    rows = []
    for name, g, ref, calc in zip(("weak", "reference_peak", "high_absorption"),
                                  couplings, reference, l_base):
        rows.append({
            "point": name, "g": float(g),
            "reference_luminosity_erg_s": float(ref),
            "calculated_luminosity_erg_s": float(calc),
            "relative_residual": float(calc/ref-1.0),
            "thin_luminosity_erg_s": float(g*g*np.sum(baseline["source"])),
            "escape_fraction": float(calc/(g*g*np.sum(baseline["source"]))),
        })

    report = {
        "title": "10 MeV Blinov Fig. 7 equation-chain audit",
        "status": "diagnostic_only_no_physical_rescaling",
        "source": "Blinov et al., arXiv:2511.09619v2, Appendix B, Eqs. (17)-(35)",
        "mass_MeV": MASS,
        "profile_sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
        "fig7_sha256": hashlib.sha256(fig7_path.read_bytes()).hexdigest(),
        "fig7_pdf_sha256": fig7.get("pdf_sha256"),
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "quadrature": {
            "radial_order": nr, "energy_order": ne,
            "angular_order": na, "path_order": ns,
            "energy_offset_MeV": energy_offset,
            "radius_km": 25.0,
        },
        "eq31_33": eq31_33,
        "eq20": {
            "stable_reduced_absorption_max_relative_residual":
                baseline["eq20_residual"],
            "identity": "Gamma_red=(1-exp(-omega/T))*Gamma_abs=(exp(omega/T)-1)*Gamma_prod",
        },
        "eq18": eq18,
        "eq17": eq17,
        "three_curve_points": rows,
        "interpretation": [
            "No coupling-dependent or channel-dependent normalization is fitted.",
            "The R=24 km comparison removes the 24-25 km exterior-lapse extension but also truncates that outer shell; it is a boundary sensitivity, not a replacement model.",
            "Path/angular order changes test numerical quadrature only.",
            "The local Eq. (31)-(33) algebra and Eq. (20) detailed-balance identity can pass while the external Fig. 7 comparison remains discrepant.",
        ],
    }
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--nr", type=int, default=88)
    parser.add_argument("--ne", type=int, default=180)
    parser.add_argument("--na", type=int, default=24)
    parser.add_argument("--ns", type=int, default=64)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()
    result = run(args.profile, args.fig7, args.nr, args.ne,
                 args.na, args.ns, args.energy_offset)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "eq31_33": {
            "compton_rate_reconstruction_max_relative_residual":
                result["eq31_33"]["compton_rate_reconstruction_max_relative_residual"],
            "eq33_max_relative_residual": max(
                x["relative_residual"]
                for x in result["eq31_33"]["eq33_susceptibility_finite_difference"]),
        },
        "eq20": result["eq20"],
        "eq18": result["eq18"],
        "eq17": result["eq17"],
        "points": result["three_curve_points"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
