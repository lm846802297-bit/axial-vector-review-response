"""Audit the global B.16 vector luminosity: Eq. (B.1) weights, fixed-omega
baseline opacity, and a separately labeled path-redshift sensitivity test.

The baseline follows the published Eq. (B.2) literally: omega is held fixed
along a chord. The alternative changes only the local energy in the opacity
kernel according to conserved energy at infinity; it retains the same
Euclidean chord length and is therefore a redshift-only diagnostic, not a
fully GR ray-tracing calculation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        decay_production, compton_production,
        negative_muon_density_and_degeneracy,
        radial_rule, load_profile, local_rates,
        scalar_optical_depths, energy_weights,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        decay_production, compton_production,
        negative_muon_density_and_degeneracy,
        radial_rule, load_profile, local_rates,
        scalar_optical_depths, energy_weights,
    )

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_global_redshift_audit_2026-11-08.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def weighted_quantile(values, weights, q):
    values = np.asarray(values, float).ravel()
    weights = np.asarray(weights, float).ravel()
    valid = np.isfinite(values) & np.isfinite(weights) & (weights > 0.0)
    if not np.any(valid):
        return 0.0
    values, weights = values[valid], weights[valid]
    order = np.argsort(values)
    values, weights = values[order], weights[order]
    cdf = np.cumsum(weights)
    return float(values[min(np.searchsorted(cdf, q*cdf[-1]), len(values)-1)])


def eq_b1_source_measure(r, rw, energies, lapse, mass, production):
    """Literal Eq. (B.1) source measure, excluding the escape probability."""
    r = np.asarray(r, float)
    rw = np.asarray(rw, float)
    energies = np.asarray(energies, float)
    lapse = np.asarray(lapse, float)
    production = np.asarray(production, float)
    if production.shape != (len(r), len(energies)):
        raise ValueError("production must have shape (n_radius, n_energy)")
    lower = mass / lapse
    eweights = energy_weights(energies, lower)
    momentum = np.sqrt(np.maximum(energies**2 - mass**2, 0.0))
    radial_measure = (
        4.0*np.pi*(r*KM_TO_MEV_INV)**2
        * rw*KM_TO_MEV_INV*lapse**2
    )
    spectral_measure = momentum*energies**2/(2.0*np.pi**2)
    source = (
        radial_measure[:, None] * eweights
        * spectral_measure[None, :] * production * MEV2_TO_ERG_S
    )
    return source, {
        "radial_measure_MeVminus3": radial_measure.tolist(),
        "energy_lower_bound_MeV": lower.tolist(),
        "energy_weight_row_sums_MeV": np.sum(eweights, axis=1).tolist(),
        "spectral_measure_MeV3": spectral_measure.tolist(),
    }


def redshifted_scalar_optical_depths(
    source_radii, radial_grid, profile, mass, source_energies,
    radius_km, angular_order=16, path_order=32,
):
    """Diagnostic alternative: omega_loc(s)=omega_source*N_source/N(path).

    The Euclidean chord/path measure is intentionally unchanged. This
    isolates the effect of changing the energy argument in the local
    absorption kernel; it is not a complete GR propagation calculation.
    """
    source_radii = np.asarray(source_radii, float)
    radial_grid = np.asarray(radial_grid, float)
    source_energies = np.asarray(source_energies, float)
    r = source_radii[:, None]

    angles, angle_weights = leggauss(angular_order)
    path_x, path_w = leggauss(path_order)
    path_w = path_w/2.0

    source_indices = np.searchsorted(radial_grid, source_radii)
    source_lapse = profile["lapse"][source_indices]

    # The B.17 susceptibility is computed once on the radial grid and
    # interpolated along the chord. compton_production only uses n_mu*F_deg.
    n_mu_grid, fdeg_grid = negative_muon_density_and_degeneracy(
        profile["T"], profile["mu_mu"]
    )
    chi_grid = n_mu_grid*fdeg_grid

    columns = np.zeros((len(source_radii), len(angles), len(source_energies)))
    min_energy_ratio = np.inf
    max_energy_ratio = 0.0
    min_local_velocity = 1.0

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
        t_path = np.interp(flat, radial_grid, profile["T"]).reshape(position.shape)
        mu_mu_path = np.interp(
            flat, radial_grid, profile["mu_mu"]
        ).reshape(position.shape)
        mu_numu_path = np.interp(
            flat, radial_grid, profile["mu_numu"]
        ).reshape(position.shape)
        lapse_path = np.interp(
            flat, radial_grid, profile["lapse"]
        ).reshape(position.shape)
        chi_path = np.interp(flat, radial_grid, chi_grid).reshape(position.shape)

        # Conserved E_infinity = N_source*omega_source:
        # omega_local(path) = E_infinity/N(path).
        omega_local = (
            source_energies[None, None, :]
            * source_lapse[:, None, None]
            / lapse_path[:, :, None]
        )
        ratio = omega_local/source_energies[None, None, :]
        min_energy_ratio = min(min_energy_ratio, float(np.min(ratio)))
        max_energy_ratio = max(max_energy_ratio, float(np.max(ratio)))

        velocity = np.sqrt(np.maximum(1.0-(mass/omega_local)**2, 0.0))
        min_local_velocity = min(min_local_velocity, float(np.min(velocity)))
        if np.any(velocity <= 0.0):
            raise FloatingPointError("Path-redshift diagnostic reached v_V=0")

        neutrino, dimuon = decay_production(
            mass, omega_local, t_path[:, :, None],
            mu_numu_path[:, :, None], mu_mu_path[:, :, None]
        )
        compton = compton_production(
            mass, omega_local, t_path[:, :, None],
            chi_path[:, :, None], np.ones_like(chi_path[:, :, None])
        )
        production = neutrino+dimuon+compton
        x = omega_local/t_path[:, :, None]
        absorption = np.exp(np.minimum(x, 700.0))*production
        reduced_absorption = -np.expm1(-x)*absorption

        columns[:, ia, :] = (
            np.sum(
                path_weights[:, :, None]*reduced_absorption/velocity,
                axis=1
            )*KM_TO_MEV_INV
        )

    return columns, angle_weights/2.0, {
        "energy_ratio_local_over_source_min": min_energy_ratio,
        "energy_ratio_local_over_source_max": max_energy_ratio,
        "minimum_path_vector_speed": min_local_velocity,
        "path_measure": "same Euclidean chord ds as Eq. (B.2); no metric path-length correction",
    }


def curve_metrics(calculated, reference):
    calculated = np.asarray(calculated, float)
    reference = np.asarray(reference, float)
    relative = calculated/reference-1.0
    peak = int(np.argmax(reference))
    return {
        "n_points": int(len(relative)),
        "mean_absolute_relative_difference": float(np.mean(np.abs(relative))),
        "maximum_absolute_relative_difference": float(np.max(np.abs(relative))),
        "weak_coupling_relative_difference": float(relative[0]),
        "reference_peak_relative_difference": float(relative[peak]),
        "strong_absorption_relative_difference": float(relative[-1]),
        "relative_differences": relative.tolist(),
    }


def run_mass(
    mass, profile_path, fig7_path,
    radial_order=40, energy_order=100, angular_order=16, path_order=32,
    radius_km=25.0, energy_offset=1000.0,
):
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    key = str(float(mass))
    if key not in fig7["reference_vertices"]:
        raise KeyError(f"No digitized Fig. 7 reference curve for m={mass:g} MeV")
    vertices = fig7["reference_vertices"][key]
    couplings = np.asarray(vertices["g"], float)
    reference_luminosity = np.asarray(vertices["luminosity_erg_s"], float)

    r, rw = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
    p = load_profile(profile_path, radial_grid)
    energies = mass+np.geomspace(
        max(mass*1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass/p["lapse"]])
    energies = energies[energies > mass*(1.0+1.0e-10)]
    energies.sort()

    rates = local_rates(
        mass, energies[None, :], p["T"][:, None],
        p["mu_numu"][:, None], p["mu_mu"][:, None]
    )
    columns_fixed, angle_weights = scalar_optical_depths(
        r, radial_grid, rates["reduced_absorption"], mass, energies,
        radius_km, angular_order, path_order
    )
    columns_redshift, redshift_angles, redshift_info = (
        redshifted_scalar_optical_depths(
            r, radial_grid, p, mass, energies,
            radius_km, angular_order, path_order
        )
    )
    angle_residual = float(np.max(np.abs(angle_weights-redshift_angles)))
    if angle_residual > 1.0e-14:
        raise ArithmeticError("Fixed and redshifted angle weights differ")

    source_index = np.searchsorted(radial_grid, r)
    lapse_source = p["lapse"][source_index]
    production = rates["production"][source_index]
    source, source_measure = eq_b1_source_measure(
        r, rw, energies, lapse_source, mass, production
    )

    channel_sources = {}
    for channel, rate_key in (
        ("neutrino", "neutrino_production"),
        ("compton", "compton_production"),
        ("dimuon", "dimuon_production"),
    ):
        channel_source, _ = eq_b1_source_measure(
            r, rw, energies, lapse_source, mass,
            rates[rate_key][source_index]
        )
        channel_sources[channel] = channel_source

    radial_source = np.sum(source, axis=1)
    radial_norm = float(np.sum(radial_source))
    radial_summary = {
        "mean_emission_radius_km": float(np.sum(r*radial_source)/radial_norm),
        "median_emission_radius_km": weighted_quantile(r, radial_source, 0.50),
        "p90_emission_radius_km": weighted_quantile(r, radial_source, 0.90),
        "shell_fractions": {},
    }
    shell_edges = [0.0, 5.0, 8.0, 10.0, 12.0, 15.0, 18.0, 20.0, 22.0, radius_km]
    for lo, hi in zip(shell_edges[:-1], shell_edges[1:]):
        mask = (r >= lo) & (r < hi if hi < radius_km else r <= hi)
        radial_summary["shell_fractions"][f"{lo:g}-{hi:g} km"] = (
            float(np.sum(radial_source[mask])/radial_norm)
        )
    channel_source_summary = {
        name: {
            "thin_source_erg_s_per_g2": float(np.sum(value)),
            "fraction": float(np.sum(value)/radial_norm),
        }
        for name, value in channel_sources.items()
    }

    fixed_rows, redshift_rows = [], []
    for g, ref_l in zip(couplings, reference_luminosity):
        esc_fixed = np.exp(-g**2*columns_fixed)
        esc_redshift = np.exp(-g**2*columns_redshift)
        avg_fixed = np.einsum("rae,a->re", esc_fixed, angle_weights)
        avg_redshift = np.einsum("rae,a->re", esc_redshift, angle_weights)

        thin = float(g**2*np.sum(source))
        lum_fixed = float(g**2*np.sum(source*avg_fixed))
        lum_redshift = float(g**2*np.sum(source*avg_redshift))
        source_angle_weights = source[:, None, :]*angle_weights[None, :, None]
        tau_fixed = g**2*columns_fixed
        tau_redshift = g**2*columns_redshift
        mean_tau_fixed = float(np.average(tau_fixed, weights=source_angle_weights))
        mean_tau_redshift = float(np.average(tau_redshift, weights=source_angle_weights))

        fixed_rows.append({
            "g": float(g),
            "reference_luminosity_erg_s": float(ref_l),
            "calculated_luminosity_erg_s": lum_fixed,
            "relative_difference": lum_fixed/float(ref_l)-1.0,
            "optically_thin_luminosity_erg_s": thin,
            "escape_fraction": lum_fixed/thin,
            "source_weighted_mean_tau": mean_tau_fixed,
        })
        redshift_rows.append({
            "g": float(g),
            "reference_luminosity_erg_s": float(ref_l),
            "calculated_luminosity_erg_s": lum_redshift,
            "relative_difference": lum_redshift/float(ref_l)-1.0,
            "optically_thin_luminosity_erg_s": thin,
            "escape_fraction": lum_redshift/thin,
            "source_weighted_mean_tau": mean_tau_redshift,
            "luminosity_shift_vs_fixed_omega": lum_redshift/lum_fixed-1.0,
        })

    fixed_luminosities = [row["calculated_luminosity_erg_s"] for row in fixed_rows]
    redshift_luminosities = [row["calculated_luminosity_erg_s"] for row in redshift_rows]
    return {
        "mass_MeV": float(mass),
        "reference_axis_conversion": (
            "The digitized Fig. 7 abscissa is alpha_V; the source extraction "
            "converts it to g=sqrt(4*pi*alpha_V). Rates and opacity are "
            "normalized per g^2 and the scan uses this g."
        ),
        "configuration": {
            "radial_order": radial_order,
            "energy_order": energy_order,
            "angular_order": angular_order,
            "path_order": path_order,
            "radius_km": radius_km,
            "energy_offset_MeV": energy_offset,
            "couplings_are_g_not_alpha_V": True,
        },
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "identity": "reconstructed public-figure SFHo-18.8, t_pb=1 s profile; not original Garching raw table",
        },
        "fig7_reference": {
            "path": str(fig7_path),
            "sha256": sha256(fig7_path),
            "pdf_sha256": fig7.get("pdf_sha256"),
            "points": len(couplings),
        },
        "eq_b1_source_measure": source_measure,
        "source_radial_distribution": radial_summary,
        "source_channel_fractions": channel_source_summary,
        "eq_b2_fixed_omega_baseline": {
            "prescription": (
                "Gamma_abs_star(r'(s), omega_source)/v_V(omega_source), "
                "with the same omega argument along the complete chord."
            ),
            "curve_metrics": curve_metrics(fixed_luminosities, reference_luminosity),
            "points": fixed_rows,
        },
        "path_redshift_only_diagnostic": {
            "prescription": (
                "omega_local(s)=omega_source*N(source)/N(path); update local "
                "rates and v_V(s), while retaining the same Euclidean ds and "
                "straight chord. This is a sensitivity diagnostic, not the "
                "published Eq. (B.2) baseline or a full GR ray trace."
            ),
            "kinematic_range": redshift_info,
            "curve_metrics": curve_metrics(redshift_luminosities, reference_luminosity),
            "mean_absolute_luminosity_shift_vs_fixed": float(np.mean(np.abs(
                np.asarray(redshift_luminosities)/np.asarray(fixed_luminosities)-1.0
            ))),
            "maximum_absolute_luminosity_shift_vs_fixed": float(np.max(np.abs(
                np.asarray(redshift_luminosities)/np.asarray(fixed_luminosities)-1.0
            ))),
            "points": redshift_rows,
        },
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": {
            "audit_script": sha256(Path(__file__)),
            "reference_script": sha256(HERE/"reference.py"),
            "profile": sha256(profile_path),
            "fig7_reference": sha256(fig7_path),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--masses", default="0.1,1,10")
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--na", type=int, default=16)
    parser.add_argument("--ns", type=int, default=32)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()

    results = [
        run_mass(
            float(token.strip()), args.profile, args.fig7,
            args.nr, args.ne, args.na, args.ns,
            args.radius, args.energy_offset,
        )
        for token in args.masses.split(",") if token.strip()
    ]
    payload = {
        "title": "Global B.16 vector luminosity: radial source weights, Eq. (B.2) fixed-omega baseline, and path-redshift-only sensitivity",
        "paper_reference": {
            "citation": "Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619",
            "equations": "Appendix B, Eqs. (B.1)--(B.5), (B.14)--(B.19)",
            "published_path_energy_convention": (
                "Eq. (B.2) explicitly evaluates Gamma_abs_star(r'(s), omega) "
                "with one fixed omega along the chord. Gravitational source "
                "redshift enters Eq. (B.1) through N(r)^2 and omega_min=m_V/N(r)."
            ),
        },
        "scope": [
            "Pure-vector B.14--B.16 literature benchmark only.",
            "The baseline is the literal fixed-omega Eq. (B.2) prescription.",
            "The path-redshift alternative changes only the local energy argument and local vector speed; it retains the Euclidean chord measure and is not a full GR ray-tracing calculation.",
            "No coupling, production, absorption, opacity, profile, or luminosity rescaling.",
            "No axial curve, PR #56 file, manuscript, or referee-response file is modified.",
        ],
        "profile_provenance_warning": (
            "The radial profile is reconstructed from public figure paths. "
            "It is not the original s18.8-SFHo-MUONS simulation table used by Blinov et al."
        ),
        "results": results,
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n")
    for row in results:
        print(json.dumps({
            "mass_MeV": row["mass_MeV"],
            "fixed_omega_metrics": row["eq_b2_fixed_omega_baseline"]["curve_metrics"],
            "path_redshift_metrics": row["path_redshift_only_diagnostic"]["curve_metrics"],
            "mean_abs_L_shift": row["path_redshift_only_diagnostic"]["mean_absolute_luminosity_shift_vs_fixed"],
            "max_abs_L_shift": row["path_redshift_only_diagnostic"]["maximum_absolute_luminosity_shift_vs_fixed"],
            "source_radial_distribution": row["source_radial_distribution"],
        }, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
