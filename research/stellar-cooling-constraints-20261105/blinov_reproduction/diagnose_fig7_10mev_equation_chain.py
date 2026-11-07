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

try:
    from .reference import (
        DEFAULT_PROFILE, M_MU, ALPHA, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        energy_weights, load_profile, local_rates,
        negative_muon_density_and_degeneracy, radial_rule,
        scalar_optical_depths,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE, M_MU, ALPHA, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        energy_weights, load_profile, local_rates,
        negative_muon_density_and_degeneracy, radial_rule,
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


def _profile_rate_and_source(profile_path, radius_km, nr, ne, energy_offset):
    r, rw = radial_rule(radius_km, nr)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
    p = load_profile(profile_path, radial_grid)
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
        "reduced": reduced_direct, "source": source,
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
        shell_tau_stats.append({
            "g": float(g),
            "source_weighted_mean_extra_tau_24_25": float(
                np.average(tau_shell, weights=weights_tau)),
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
        "interpretation": "Quadrature-only changes; no opacity normalization is altered.",
    }
    eq17 = {
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
