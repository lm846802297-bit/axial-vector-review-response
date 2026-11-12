"""Global 10 MeV B.16 polarization-resolved transport diagnostic with B.14 mode weights.

The literal scalar B.2 result is retained as the reference. The three
inverse-neutrino-decay polarization modes are propagated separately. The
B.14 no-recoil Thomson-limit inverse cross sections imply Compton mode weights
w_L=(m_V^2/omega^2)/(2+m_V^2/omega^2) and
w_+=w_-=1/(2+m_V^2/omega^2). The same weights are used for Compton source
and opacity by detailed balance. This is a mode-resolved diagnostic, not a
replacement scalar baseline.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        radial_rule, load_profile, local_rates, scalar_optical_depths,
    )
    from .audit_b16_global_redshift import (
        DEFAULT_FIG7, eq_b1_source_measure, float_array_sha256,
    )
    import rates as production_rates
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S,
        radial_rule, load_profile, local_rates, scalar_optical_depths,
    )
    from audit_b16_global_redshift import (
        DEFAULT_FIG7, eq_b1_source_measure, float_array_sha256,
    )
    import rates as production_rates

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "outputs" / "b16_global_polarization_transport_b14_split_10mev_2026-11-10.json"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source_measure(r, rw, e, lapse, mass, prod):
    return eq_b1_source_measure(r, rw, e, lapse, mass, prod)[0]


def metrics(values, reference):
    ratio = np.asarray(values, float) / np.asarray(reference, float) - 1.0
    peak = int(np.argmax(reference))
    return {
        "n_points": int(len(ratio)),
        "weak_endpoint_relative_difference": float(ratio[0]),
        "reference_peak_relative_difference": float(ratio[peak]),
        "strong_absorption_relative_difference": float(ratio[-1]),
        "mean_absolute_relative_difference": float(np.mean(np.abs(ratio))),
        "maximum_absolute_relative_difference": float(np.max(np.abs(ratio))),
        "relative_differences": ratio.tolist(),
    }


def run(profile_path=DEFAULT_PROFILE, fig7_path=DEFAULT_FIG7, mass=10.0,
        radial_order=200, opacity_order=640, energy_order=200,
        angular_order=32, path_order=64, energy_offset=1000.0,
        neutrino_order=48):
    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    key = str(float(mass))
    vertices = fig7["reference_vertices"][key]
    couplings = np.asarray(vertices["g"], float)
    reference_lum = np.asarray(vertices["luminosity_erg_s"], float)

    # Keep B.1 source nodes independent of the B.2 opacity interpolation grid.
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

    # Scalar reference rates and exact polarization-resolved nu_mu+nu_tau rates.
    scalar_source_rates = local_rates(
        mass, energies[None, :], source_profile["T"][:, None],
        source_profile["mu_numu"][:, None], source_profile["mu_mu"][:, None]
    )
    source_prod_modes, _ = production_rates.neutrino_rates(
        mass, energies[None, :], source_profile["T"][:, None],
        source_profile["mu_numu"][:, None], order=neutrino_order
    )
    scalar_opacity_rates = local_rates(
        mass, energies[None, :], opacity_profile["T"][:, None],
        opacity_profile["mu_numu"][:, None], opacity_profile["mu_mu"][:, None]
    )
    opacity_prod_modes, opacity_abs_modes = production_rates.neutrino_rates(
        mass, energies[None, :], opacity_profile["T"][:, None],
        opacity_profile["mu_numu"][:, None], order=neutrino_order
    )

    # B.4 reduced absorption for each mode; scalar Compton contribution is
    # separated by subtracting the exact mode-summed neutrino contribution.
    x_op = energies[None, :] / opacity_profile["T"][:, None]
    reduced_nu_modes = -np.expm1(-x_op)[..., None] * opacity_abs_modes
    reduced_nu_sum = np.sum(reduced_nu_modes, axis=-1)
    reduced_total = scalar_opacity_rates["reduced_absorption"]
    reduced_compton = reduced_total - reduced_nu_sum
    opacity_closure = float(np.max(
        np.abs(reduced_total - reduced_nu_sum - reduced_compton)
        / np.maximum(np.abs(reduced_total), 1.0e-300)
    ))
    if np.min(reduced_compton) < -1.0e-10 * max(float(np.max(reduced_total)), 1.0):
        raise ArithmeticError("Mode-summed neutrino opacity exceeds total scalar opacity")

    # B.1 source measures: neutrino modes are exact; Compton is split equally
    # only to make a controlled full-source polarization diagnostic.
    source_nu_modes = np.stack([
        source_measure(
            source_r, source_rw, energies, source_profile["lapse"], mass,
            source_prod_modes[..., mode]
        )
        for mode in range(3)
    ])
    source_compton = source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        scalar_source_rates["compton_production"]
    )
    source_total_scalar = source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        scalar_source_rates["production"]
    )
    source_nu_scalar = source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        scalar_source_rates["neutrino_production"]
    )
    source_mode_sum_residual = float(np.max(
        np.abs(np.sum(source_nu_modes, axis=0) - source_nu_scalar)
        / np.maximum(np.abs(source_nu_scalar), 1.0e-300)
    ))
    source_channel_residual = float(np.max(
        np.abs(source_nu_scalar + source_compton - source_total_scalar)
        / np.maximum(np.abs(source_total_scalar), 1.0e-300)
    ))
    compton_ratio = mass**2 / energies**2
    compton_mode_weights = np.stack([
        compton_ratio,
        np.ones_like(energies),
        np.ones_like(energies),
    ]) / (2.0 + compton_ratio)[None, :]
    source_modes_total = (
        source_nu_modes + source_compton[None, :, :] * compton_mode_weights[:, None, :]
    )

    # Literal scalar optical depth and the three polarization-specific columns.
    columns_scalar, angle_weights = scalar_optical_depths(
        source_r, opacity_grid, reduced_total, mass, energies, 25.0,
        angular_order, path_order
    )
    columns_modes = []
    for mode in range(3):
        reduced_mode_total = (
            reduced_nu_modes[..., mode]
            + reduced_compton * compton_mode_weights[mode][None, :]
        )
        columns, mode_weights = scalar_optical_depths(
            source_r, opacity_grid, reduced_mode_total, mass, energies, 25.0,
            angular_order, path_order
        )
        if np.max(np.abs(mode_weights - angle_weights)) > 1.0e-14:
            raise ArithmeticError("Polarization modes do not share identical angular weights")
        columns_modes.append(columns)
    columns_modes = np.stack(columns_modes)

    # Average-opacity diagnostic: total source propagated with the mean of the
    # three mode opacities. It is distinct from mode-resolved source weighting.
    columns_average = np.mean(columns_modes, axis=0)

    source_total_norm = float(np.sum(source_total_scalar))
    source_mode_norm = float(np.sum(source_modes_total))
    if abs(source_mode_norm / source_total_norm - 1.0) > 1.0e-10:
        raise ArithmeticError("Mode-resolved source does not close to scalar B.1 source")

    rows = []
    scalar_lums, mode_lums, average_lums = [], [], []
    for g, ref_l in zip(couplings, reference_lum):
        esc_scalar = np.exp(-g*g*columns_scalar)
        avg_scalar = np.einsum("rae,a->re", esc_scalar, angle_weights)
        lum_scalar = float(g*g*np.sum(source_total_scalar*avg_scalar))

        mode_lum_parts = []
        for mode in range(3):
            esc = np.exp(-g*g*columns_modes[mode])
            avg = np.einsum("rae,a->re", esc, angle_weights)
            mode_lum_parts.append(float(g*g*np.sum(source_modes_total[mode]*avg)))
        lum_mode = float(sum(mode_lum_parts))

        esc_average = np.exp(-g*g*columns_average)
        avg_average = np.einsum("rae,a->re", esc_average, angle_weights)
        lum_average = float(g*g*np.sum(source_total_scalar*avg_average))

        thin = float(g*g*source_total_norm)
        scalar_lums.append(lum_scalar)
        mode_lums.append(lum_mode)
        average_lums.append(lum_average)
        rows.append({
            "g": float(g),
            "reference_luminosity_erg_s": float(ref_l),
            "literal_scalar_luminosity_erg_s": lum_scalar,
            "mode_resolved_B14_compton_weights_luminosity_erg_s": lum_mode,
            "average_opacity_luminosity_erg_s": lum_average,
            "optically_thin_luminosity_erg_s": thin,
            "literal_scalar_escape_fraction": lum_scalar / thin,
            "mode_resolved_B14_compton_weights_escape_fraction": lum_mode / thin,
            "average_opacity_escape_fraction": lum_average / thin,
            "mode_luminosity_fractions": [x/lum_mode for x in mode_lum_parts],
            "mode_resolved_B14_compton_weights_over_literal_scalar": lum_mode/lum_scalar,
            "scalar_relative_difference_vs_fig7": lum_scalar/float(ref_l)-1.0,
            "mode_resolved_B14_compton_weights_relative_difference_vs_fig7": lum_mode/float(ref_l)-1.0,
            "average_opacity_relative_difference_vs_fig7": lum_average/float(ref_l)-1.0,
        })

    tau_channel_fraction = {
        "neutrino": float(np.sum(source_total_scalar * 0.0) + np.mean(reduced_nu_sum) / max(np.mean(reduced_total),1e-300)),
        "compton": float(np.mean(reduced_compton) / max(np.mean(reduced_total),1e-300)),
    }
    return {
        "title": "Global 10 MeV B.16 polarization-resolved transport diagnostic",
        "mass_MeV": float(mass),
        "profile": {"path": str(profile_path), "sha256": sha256(profile_path),
                    "identity": "vertex-preserving public-figure reconstruction; not raw Garching simulation data"},
        "fig7_reference_sha256": sha256(fig7_path),
        "configuration": {
            "source_radial_order": radial_order,
            "opacity_order": opacity_order,
            "opacity_grid_node_count": int(len(opacity_grid)),
            "energy_order": energy_order,
            "energy_grid_node_count": int(len(energies)),
            "angular_order": angular_order,
            "path_order": path_order,
            "neutrino_mode_rate_order": neutrino_order,
            "source_grid_sha256": float_array_sha256(source_r),
            "opacity_grid_sha256": float_array_sha256(opacity_grid),
            "energy_grid_sha256": float_array_sha256(energies),
            "fixed_omega": True,
        },
        "source": {
            "total_B1_source_erg_s_per_g2": source_total_norm,
            "neutrino_source_fraction": float(np.sum(source_nu_scalar)/source_total_norm),
            "compton_source_fraction": float(np.sum(source_compton)/source_total_norm),
            "neutrino_mode_source_fractions": [
                float(np.sum(source_nu_modes[i])/np.sum(source_nu_scalar)) for i in range(3)
            ],
            "compton_mode_split": "B.14 no-recoil Thomson-limit weights: w_L=(m_V^2/omega^2)/(2+m_V^2/omega^2), w_+=w_-=1/(2+m_V^2/omega^2); same weights applied to source and opacity",
            "source_mode_sum_closure_residual": source_mode_sum_residual,
            "source_channel_closure_residual": source_channel_residual,
        },
        "opacity": {
            "neutrino_mode_sum_closure_residual": float(np.max(
                np.abs(reduced_nu_sum - (reduced_total-reduced_compton))
                / np.maximum(np.abs(reduced_total),1.0e-300)
            )),
            "total_reduced_opacity_closure_residual": opacity_closure,
            "mean_grid_fraction_neutrino": tau_channel_fraction["neutrino"],
            "mean_grid_fraction_compton": tau_channel_fraction["compton"],
            "compton_opacity_mode_split": "B.14 no-recoil Thomson-limit mode weights; not a full recoil-resolved Compton kernel",
        },
        "metrics_vs_fig7": {
            "literal_scalar": metrics(scalar_lums, reference_lum),
            "mode_resolved_B14_compton_weights": metrics(mode_lums, reference_lum),
            "average_opacity": metrics(average_lums, reference_lum),
        },
        "points": rows,
        "interpretation_limits": [
            "The literal scalar result reproduces the repository's current B.2 implementation and is retained unchanged.",
            "The mode-resolved neutrino opacity uses the exact L,+,- B.6/B.10 rates from rates.neutrino_rates.",
            "The Compton mode decomposition uses the B.14 no-recoil Thomson-limit inverse-cross-section ratios; it is not a full recoil-resolved Compton kernel.",
            "A discrepancy reduced by this test does not by itself prove that the paper's Fig. 7 implementation used mode-resolved transport.",
            "No coupling, source, opacity, or luminosity rescaling is applied; no axial-vector output is changed."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--nr", type=int, default=200)
    parser.add_argument("--opacity-order", type=int, default=640)
    parser.add_argument("--ne", type=int, default=200)
    parser.add_argument("--na", type=int, default=32)
    parser.add_argument("--ns", type=int, default=64)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    parser.add_argument("--neutrino-order", type=int, default=64)
    args = parser.parse_args()
    result = run(
        args.profile, args.fig7, args.mass, args.nr, args.opacity_order,
        args.ne, args.na, args.ns, args.energy_offset, args.neutrino_order
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "source": result["source"],
        "opacity": result["opacity"],
        "metrics_vs_fig7": {
            k: {kk: vv for kk, vv in v.items() if kk != "relative_differences"}
            for k, v in result["metrics_vs_fig7"].items()
        },
        "strong_endpoint": result["points"][-1],
        "output": str(args.output),
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
