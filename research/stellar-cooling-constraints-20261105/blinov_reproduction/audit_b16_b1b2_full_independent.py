"""End-to-end independent B.1+B.2 luminosity integration for the 10 MeV vector benchmark.

The B.1 source integral is evaluated with the independent logarithmic-energy
and equal-width radial Gauss rules from audit_b16_b1_independent. For each
source radius and its own exact-threshold energy quadrature, the local
absorption profile is evaluated over the independent radial opacity grid.
The B.2 chord integral is then computed with the analytic piecewise-linear
path integrator from audit_b16_path_independent. No legacy B.1 energy_weights,
radial_rule, scalar_optical_depths, or path-length quadrature is called.

The literal Appendix-B fixed-omega convention is retained. The local
production and absorption kernels are shared with the reference implementation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np

try:
    from .reference import (
        DEFAULT_PROFILE,
        KM_TO_MEV_INV,
        MEV2_TO_ERG_S,
        negative_muon_density_and_degeneracy,
        decay_production,
        compton_production,
    )
    from .audit_b16_b1_independent import (
        DEFAULT_PROFILE as B1_DEFAULT_PROFILE,
        DEFAULT_BASELINE as B1_DEFAULT_BASELINE,
        DEFAULT_OUTPUT as B1_DEFAULT_OUTPUT,
        read_profile_direct,
        interpolate_profile,
        radial_state,
        log_energy_rule,
        sha256,
    )
    from .audit_b16_path_independent import (
        DEFAULT_FIG7,
        DEFAULT_BASELINE as B2_DEFAULT_BASELINE,
        DEFAULT_OUTPUT as B2_DEFAULT_OUTPUT,
        analytic_chord_columns,
        gauss_angle_rule,
    )
    from .audit_b16_global_redshift import curve_metrics
except ImportError:
    from reference import (
        DEFAULT_PROFILE,
        KM_TO_MEV_INV,
        MEV2_TO_ERG_S,
        negative_muon_density_and_degeneracy,
        decay_production,
        compton_production,
    )
    from audit_b16_b1_independent import (
        DEFAULT_PROFILE as B1_DEFAULT_PROFILE,
        DEFAULT_BASELINE as B1_DEFAULT_BASELINE,
        DEFAULT_OUTPUT as B1_DEFAULT_OUTPUT,
        read_profile_direct,
        interpolate_profile,
        radial_state,
        log_energy_rule,
        sha256,
    )
    from audit_b16_path_independent import (
        DEFAULT_FIG7,
        DEFAULT_BASELINE as B2_DEFAULT_BASELINE,
        DEFAULT_OUTPUT as B2_DEFAULT_OUTPUT,
        analytic_chord_columns,
        gauss_angle_rule,
    )
    from audit_b16_global_redshift import curve_metrics

HERE = Path(__file__).resolve().parent
DEFAULT_BASELINE = HERE / "outputs" / "b16_global_fig7_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_B1_OUTPUT = HERE / "outputs" / "b16_b1_independent_thin_source_10mev_2026-11-09.json"
DEFAULT_B2_OUTPUT = HERE / "outputs" / "b16_path_independent_analytic_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_full_b1b2_independent_10mev_2026-11-09.json"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
CHANNELS = ("neutrino", "dimuon", "compton")


def angular_escape_factors(
    optical_depths: np.ndarray,
    angular_weights: np.ndarray,
    couplings: np.ndarray,
) -> np.ndarray:
    """Return <exp(-g^2 tau)> for [angle,energy] tau and all couplings."""
    tau = np.asarray(optical_depths, float)
    weights = np.asarray(angular_weights, float)
    g = np.asarray(couplings, float)
    if tau.ndim != 2 or tau.shape[0] != len(weights):
        raise ValueError("Optical depths must have shape (n_angle,n_energy)")
    if np.any(tau < -1.0e-12) or np.any(g <= 0.0):
        raise ValueError("Optical depths must be nonnegative and couplings positive")
    return np.einsum(
        "a,gae->ge",
        weights,
        np.exp(-g[:, None, None] ** 2 * np.maximum(tau, 0.0)[None, :, :]),
    )


def evaluate_full_curve(
    table: dict[str, np.ndarray],
    mass_mev: float,
    couplings: np.ndarray,
    radius_km: float,
    radial_panels: int,
    radial_order: int,
    energy_panels: int,
    energy_order: int,
    energy_offset_mev: float,
    angular_order: int,
) -> dict:
    """Compute the full B.1+B.2 luminosity curve with O(r,omega) included."""
    state = radial_state(table, radius_km, radial_panels, radial_order)
    source_radii = np.asarray(state["radii_km"], float)
    radial_prefactor = np.asarray(state["radial_prefactor"], float)

    # The source quadrature nodes themselves define the independent opacity
    # interpolation grid; the center and outer endpoint are added explicitly.
    opacity_radii = np.unique(np.r_[0.0, source_radii, radius_km])
    opacity_profile = interpolate_profile(table, opacity_radii)
    n_mu, f_deg = negative_muon_density_and_degeneracy(
        opacity_profile["T"], opacity_profile["mu_mu"]
    )
    n_mu = np.asarray(n_mu, float)
    f_deg = np.asarray(f_deg, float)
    source_indices = np.searchsorted(opacity_radii, source_radii)
    if not np.array_equal(opacity_radii[source_indices], source_radii):
        raise ArithmeticError("Source radii are not exact members of opacity grid")

    angle_nodes, angle_weights = gauss_angle_rule(angular_order)
    g = np.asarray(couplings, float)
    luminosity_channels = {
        name: np.zeros(len(g), dtype=float) for name in CHANNELS
    }
    thin_channels = {name: 0.0 for name in CHANNELS}
    max_tau = 0.0
    min_escape = 1.0
    radial_records = []

    for ir, source_radius in enumerate(source_radii):
        omega, d_omega = log_energy_rule(
            mass_mev,
            mass_mev / float(state["lapse"][ir]),
            energy_offset_mev,
            energy_panels,
            energy_order,
        )
        # Evaluate all local production and reduced-absorption channels on the
        # full opacity radial grid at this source node's energy quadrature.
        nu_rate, dimuon_rate = decay_production(
            mass_mev,
            omega[None, :],
            opacity_profile["T"][:, None],
            opacity_profile["mu_numu"][:, None],
            opacity_profile["mu_mu"][:, None],
        )
        compton_rate = compton_production(
            mass_mev,
            omega[None, :],
            opacity_profile["T"][:, None],
            n_mu[:, None],
            f_deg[:, None],
        )
        production_channels = {
            "neutrino": np.asarray(nu_rate, float),
            "dimuon": np.asarray(dimuon_rate, float),
            "compton": np.asarray(compton_rate, float),
        }
        production_total = sum(production_channels.values())
        x = omega[None, :] / opacity_profile["T"][:, None]
        reduced_absorption = (
            np.expm1(np.minimum(x, 700.0)) * production_total
        )
        if not np.all(np.isfinite(reduced_absorption)):
            raise FloatingPointError("Non-finite reduced absorption rate")

        tau = analytic_chord_columns(
            np.asarray([source_radius]),
            opacity_radii,
            reduced_absorption,
            mass_mev,
            omega,
            radius_km,
            angle_nodes,
        )[0]
        max_tau = max(max_tau, float(np.max(tau)))
        escape = angular_escape_factors(tau, angle_weights, g)
        min_escape = min(min_escape, float(np.min(escape)))

        source_index = int(source_indices[ir])
        momentum = np.sqrt(np.maximum(omega * omega - mass_mev * mass_mev, 0.0))
        phase_space = momentum * omega**2 / (2.0 * np.pi**2)
        spectral_weights = d_omega * phase_space

        for name in CHANNELS:
            source_rate = production_channels[name][source_index]
            thin_channels[name] += (
                radial_prefactor[ir] * float(np.dot(spectral_weights, source_rate))
            )
            channel_integral = np.einsum(
                "ge,e->g", escape, spectral_weights * source_rate
            )
            luminosity_channels[name] += (
                radial_prefactor[ir] * g**2 * channel_integral
            )

        if ir % 20 == 0 or ir == len(source_radii) - 1:
            radial_records.append({
                "source_node_index": int(ir),
                "source_radius_km": float(source_radius),
                "energy_nodes": int(len(omega)),
                "maximum_optical_depth_at_unit_coupling": float(np.max(tau)),
            })
            print(
                f"radial source node {ir+1}/{len(source_radii)} "
                f"(r={source_radius:.4f} km) completed",
                flush=True,
            )

    thin_total = float(sum(thin_channels.values()))
    luminosity_total = sum(luminosity_channels.values())
    escape_fraction = luminosity_total / (g**2 * thin_total)
    return {
        "radial_panels": int(radial_panels),
        "radial_order": int(radial_order),
        "number_of_source_radial_nodes": int(len(source_radii)),
        "number_of_opacity_radial_nodes": int(len(opacity_radii)),
        "energy_panels_per_source_radius": int(energy_panels),
        "energy_gauss_order": int(energy_order),
        "energy_nodes_per_source_radius": int(energy_panels * energy_order),
        "energy_upper_MeV": float(mass_mev + energy_offset_mev),
        "angular_order": int(angular_order),
        "thin_source_erg_s_per_g2": thin_total,
        "thin_source_channels_erg_s_per_g2": thin_channels,
        "thin_source_channel_fractions": {
            name: thin_channels[name] / thin_total for name in CHANNELS
        },
        "luminosity_erg_s": luminosity_total.tolist(),
        "luminosity_channels_erg_s": {
            name: values.tolist() for name, values in luminosity_channels.items()
        },
        "escape_fraction": escape_fraction.tolist(),
        "maximum_optical_depth_at_unit_coupling": max_tau,
        "minimum_angular_escape_average_on_grid": min_escape,
        "radial_progress_samples": radial_records,
    }


def run(
    profile_path: Path = DEFAULT_PROFILE,
    baseline_path: Path = DEFAULT_BASELINE,
    b1_output_path: Path = DEFAULT_B1_OUTPUT,
    b2_output_path: Path = DEFAULT_B2_OUTPUT,
    fig7_path: Path = DEFAULT_FIG7,
    output_path: Path = DEFAULT_OUTPUT,
    mass_mev: float = 10.0,
    radius_km: float = 25.0,
    radial_order: int = 4,
    energy_order: int = 4,
    energy_panels: int = 80,
    energy_offset_mev: float = 2000.0,
    angular_order: int = 16,
) -> dict:
    started = time.time()
    profile_sha = sha256(profile_path)
    if profile_sha != EXPECTED_PROFILE_SHA256:
        raise ValueError(
            f"Unexpected profile SHA-256 {profile_sha}; expected {EXPECTED_PROFILE_SHA256}"
        )
    table = read_profile_direct(profile_path)

    baseline = json.loads(Path(baseline_path).read_text(encoding="utf-8"))
    baseline_result = baseline["results"][0]
    if baseline_result["profile"]["sha256"] != profile_sha:
        raise ValueError("Archived B.16 baseline has a different profile")
    archived_points = baseline_result["eq_b2_fixed_omega_baseline"]["points"]
    archived_g = np.asarray([point["g"] for point in archived_points], float)
    archived_luminosity = np.asarray(
        [point["calculated_luminosity_erg_s"] for point in archived_points], float
    )

    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    fig7_vertices = fig7["reference_vertices"][str(float(mass_mev))]
    couplings = np.asarray(fig7_vertices["g"], float)
    fig7_luminosity = np.asarray(fig7_vertices["luminosity_erg_s"], float)
    np.testing.assert_allclose(archived_g, couplings, rtol=2.0e-14, atol=0.0)

    b1 = json.loads(Path(b1_output_path).read_text(encoding="utf-8"))
    b2 = json.loads(Path(b2_output_path).read_text(encoding="utf-8"))
    if b1["profile"]["sha256"] != profile_sha or b2["profile"]["sha256"] != profile_sha:
        raise ValueError("Independent B.1/B.2 outputs use a different profile")

    # The 100-node calculation is a radial-resolution diagnostic. The
    # 200-node result is the final independent B.1+B.2 curve.
    coarse = evaluate_full_curve(
        table, mass_mev, couplings, radius_km,
        radial_panels=25, radial_order=radial_order,
        energy_panels=energy_panels, energy_order=energy_order,
        energy_offset_mev=energy_offset_mev, angular_order=angular_order,
    )
    final = evaluate_full_curve(
        table, mass_mev, couplings, radius_km,
        radial_panels=50, radial_order=radial_order,
        energy_panels=energy_panels, energy_order=energy_order,
        energy_offset_mev=energy_offset_mev, angular_order=angular_order,
    )

    coarse_curve = np.asarray(coarse["luminosity_erg_s"], float)
    final_curve = np.asarray(final["luminosity_erg_s"], float)
    coarse_vs_final = final_curve / coarse_curve - 1.0
    final_vs_archived = final_curve / archived_luminosity - 1.0
    final_vs_fig7 = final_curve / fig7_luminosity - 1.0

    b1_highres_total = float(b1["final_independent_b1_source"]["total_erg_s_per_g2"])
    b1_source_closure = final["thin_source_erg_s_per_g2"] / b1_highres_total - 1.0
    archived_b16_thin = float(
        baseline_result["source_channel_fractions"]["neutrino"]["thin_source_erg_s_per_g2"]
        + baseline_result["source_channel_fractions"]["compton"]["thin_source_erg_s_per_g2"]
        + baseline_result["source_channel_fractions"]["dimuon"]["thin_source_erg_s_per_g2"]
    )

    payload = {
        "source": "Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B, Eqs. (B.1)--(B.5), (B.14)--(B.19)",
        "scope": "Full fixed-omega B.1+B.2 ballistic luminosity, with independently integrated source and analytic piecewise-linear chord optical depths.",
        "method": (
            "B.1: independent equal-width radial Gauss-Legendre quadrature and "
            "exact-threshold logarithmic-energy Gauss-Legendre quadrature. "
            "B.2: for each source radius and energy quadrature node, recompute "
            "the reduced absorption profile over the source-node opacity grid, "
            "then integrate each chord analytically segment by segment and "
            "perform the full Gauss-Legendre direction average."
        ),
        "independence_boundary": {
            "not_used": [
                "eq_b1_source_measure",
                "energy_weights",
                "radial_rule",
                "scalar_optical_depths",
                "path-length Gauss-Legendre integration",
            ],
            "shared": [
                "The reconstructed profile and its piecewise-linear interpolation.",
                "The local neutrino inverse-decay and muon-Compton production kernels.",
                "The negative-muon density and susceptibility convention of Eq. (B.17).",
                "The literal fixed-omega Eq. (B.2) convention.",
            ],
        },
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": sha256(Path(__file__)),
        "profile": {"path": Path(profile_path).name, "sha256": profile_sha},
        "baseline_reference_sha256": sha256(baseline_path),
        "independent_b1_output_sha256": sha256(b1_output_path),
        "independent_b2_output_sha256": sha256(b2_output_path),
        "fig7_reference_sha256": sha256(fig7_path),
        "configuration": {
            "mass_MeV": float(mass_mev),
            "radius_km": float(radius_km),
            "radial_order": int(radial_order),
            "energy_panels_per_source_radius": int(energy_panels),
            "energy_gauss_order": int(energy_order),
            "energy_upper_offset_MeV": float(energy_offset_mev),
            "angular_order": int(angular_order),
            "radial_panels_compared": [25, 50],
            "source_radial_nodes_compared": [100, 200],
            "coupling_points": int(len(couplings)),
        },
        "couplings": couplings.tolist(),
        "fig7_reference_luminosity_erg_s": fig7_luminosity.tolist(),
        "archived_b16_luminosity_erg_s": archived_luminosity.tolist(),
        "coarse_100_node_result": coarse,
        "final_200_node_result": final,
        "radial_convergence": {
            "final_vs_coarse_relative_shift": coarse_vs_final.tolist(),
            "maximum_absolute_luminosity_shift": float(np.max(np.abs(coarse_vs_final))),
            "mean_absolute_luminosity_shift": float(np.mean(np.abs(coarse_vs_final))),
        },
        "final_curve_metrics_vs_fig7": curve_metrics(final_curve, fig7_luminosity),
        "final_curve_metrics_vs_archived_b16": curve_metrics(final_curve, archived_luminosity),
        "maximum_absolute_relative_difference_vs_archived_b16": float(
            np.max(np.abs(final_vs_archived))
        ),
        "maximum_absolute_relative_difference_vs_fig7": float(
            np.max(np.abs(final_vs_fig7))
        ),
        "source_closure": {
            "final_200_node_thin_source_erg_s_per_g2": final["thin_source_erg_s_per_g2"],
            "independent_b1_400_node_thin_source_erg_s_per_g2": b1_highres_total,
            "relative_difference_vs_independent_b1_400_node": float(b1_source_closure),
            "archived_b16_thin_source_erg_s_per_g2": archived_b16_thin,
            "relative_difference_vs_archived_b16_thin_source": float(
                final["thin_source_erg_s_per_g2"] / archived_b16_thin - 1.0
            ),
        },
        "elapsed_seconds": float(time.time() - started),
        "limitations": [
            "The radial profile is reconstructed from public figures, not the original Garching simulation table.",
            "The local production and absorption kernels are shared and are not independently re-derived by this end-to-end integration.",
            "The B.2 geometry is the Euclidean straight chord in Appendix B, not full GR ray tracing.",
            "The fixed-omega Eq. (B.2) prescription is retained; this calculation does not resolve the main-text versus Appendix-B energy-language issue.",
            "The calculation is for the scalar/vector Appendix-B reference prescription and is not the production axial-vector curve.",
        ],
        "production_axial_outputs_modified": False,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--b1-output", type=Path, default=DEFAULT_B1_OUTPUT)
    parser.add_argument("--b2-output", type=Path, default=DEFAULT_B2_OUTPUT)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--radial-order", type=int, default=4)
    parser.add_argument("--energy-order", type=int, default=4)
    parser.add_argument("--energy-panels", type=int, default=80)
    parser.add_argument("--energy-offset", type=float, default=2000.0)
    parser.add_argument("--angular-order", type=int, default=16)
    args = parser.parse_args()
    result = run(
        args.profile, args.baseline, args.b1_output, args.b2_output, args.fig7,
        args.output, args.mass, args.radius, args.radial_order, args.energy_order,
        args.energy_panels, args.energy_offset, args.angular_order,
    )
    print(json.dumps({
        "output": str(args.output),
        "source_closure": result["source_closure"],
        "radial_convergence": result["radial_convergence"],
        "final_vs_fig7": result["final_curve_metrics_vs_fig7"],
        "final_vs_archived_b16": result["final_curve_metrics_vs_archived_b16"],
        "maximum_absolute_relative_difference_vs_fig7": result["maximum_absolute_relative_difference_vs_fig7"],
        "maximum_absolute_relative_difference_vs_archived_b16": result["maximum_absolute_relative_difference_vs_archived_b16"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
