"""Strict NumPy reproduction of the 10 MeV high-energy B.2 sensitivities.

Reproduces the archived V8-only 210--510 MeV fixed-source outer-temperature
stress tests and fixed-omega versus path-redshift comparison. The source
weights are built from the full 842-node B.1 energy grid; only the ten
210--510 MeV nodes are retained for opacity and escape calculations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from reference import (
    KM_TO_MEV_INV,
    MEV2_TO_ERG_S,
    energy_weights,
    load_profile,
    local_rates,
    radial_rule,
    scalar_optical_depths,
)
from audit_b16_global_redshift import redshifted_scalar_optical_depths

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_V8_OUTER = HERE / "outputs" / "b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-10.json"
DEFAULT_V8_REDSHIFT = HERE / "outputs" / "b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-10.json"
DEFAULT_OUTPUT_DIR = HERE / "outputs"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build_inputs(profile_path: Path, fig7_path: Path, mass: float,
                 radial_order: int, opacity_order: int, energy_order: int,
                 radius_km: float, energy_offset: float):
    profile_hash = sha256(profile_path)
    if profile_hash != EXPECTED_PROFILE_SHA256:
        raise RuntimeError(f"Unexpected reconstructed profile SHA-256: {profile_hash}")

    fig7 = json.loads(fig7_path.read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
    coupling = float(vertices["g"][-1])

    source_r, source_rw = radial_rule(radius_km, radial_order)
    opacity_r, _ = radial_rule(radius_km, opacity_order)
    opacity_grid = np.unique(np.r_[0.0, opacity_r, radius_km])
    source_profile = load_profile(profile_path, source_r)
    opacity_profile = load_profile(profile_path, opacity_grid)

    full_energies = mass + np.geomspace(1.0e-5, energy_offset, energy_order)
    full_energies = np.unique(np.r_[full_energies, mass / opacity_profile["lapse"]])
    full_energies = full_energies[full_energies > mass * (1.0 + 1.0e-10)]
    full_energies.sort()
    band_mask = (full_energies >= 210.0) & (full_energies <= 510.0)
    energies = full_energies[band_mask]
    if len(energies) != 10:
        raise RuntimeError(f"Expected ten high-energy nodes, found {len(energies)}")

    # Preserve B.1 energy quadrature weights from the complete energy grid.
    # Restricting the energy grid before constructing weights would change
    # the source integral at the 210 and 510 MeV band edges.
    eweights = energy_weights(
        full_energies, mass / source_profile["lapse"]
    )[:, band_mask]
    momentum = np.sqrt(np.maximum(energies**2 - mass**2, 0.0))
    spectral = momentum * energies**2 / (2.0 * np.pi**2)
    geometry = (
        4.0 * np.pi * (source_r * KM_TO_MEV_INV)**2
        * source_rw * KM_TO_MEV_INV * source_profile["lapse"]**2
    )

    source_rates = local_rates(
        mass, energies[None, :], source_profile["T"][:, None],
        source_profile["mu_numu"][:, None], source_profile["mu_mu"][:, None]
    )
    source_nu = (
        geometry[:, None] * eweights * spectral[None, :]
        * source_rates["neutrino_production"] * MEV2_TO_ERG_S
    )
    source_compton = (
        geometry[:, None] * eweights * spectral[None, :]
        * source_rates["compton_production"] * MEV2_TO_ERG_S
    )
    source_total = source_nu + source_compton

    return {
        "fig7": fig7,
        "coupling": coupling,
        "source_r": source_r,
        "source_rw": source_rw,
        "opacity_grid": opacity_grid,
        "source_profile": source_profile,
        "opacity_profile": opacity_profile,
        "full_energies": full_energies,
        "energies": energies,
        "source_nu": source_nu,
        "source_compton": source_compton,
        "source_total": source_total,
        "source_weight_per_g2": float(np.sum(source_total)),
        "radius_km": float(radius_km),
        "profile_sha256": profile_hash,
        "fig7_sha256": sha256(fig7_path),
    }


def reduced_opacity_components(mass: float, energies: np.ndarray,
                               profile: dict) -> tuple[np.ndarray, np.ndarray]:
    rates = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    x = energies[None, :] / profile["T"][:, None]
    detailed_balance = -np.expm1(-x) * np.exp(np.minimum(x, 700.0))
    return (
        detailed_balance * rates["neutrino_production"],
        detailed_balance * rates["compton_production"],
    )


def fixed_omega_columns(inputs: dict, mass: float, angular_order: int,
                        path_order: int, opacity_profile: dict | None = None):
    profile = inputs["opacity_profile"] if opacity_profile is None else opacity_profile
    reduced_nu, reduced_compton = reduced_opacity_components(
        mass, inputs["energies"], profile
    )
    columns_nu, angle_weights = scalar_optical_depths(
        inputs["source_r"], inputs["opacity_grid"], reduced_nu,
        mass, inputs["energies"], inputs["radius_km"], angular_order, path_order
    )
    columns_compton, angle_weights_compton = scalar_optical_depths(
        inputs["source_r"], inputs["opacity_grid"], reduced_compton,
        mass, inputs["energies"], inputs["radius_km"], angular_order, path_order
    )
    angle_residual = float(np.max(np.abs(angle_weights - angle_weights_compton)))
    if angle_residual > 1.0e-14:
        raise ArithmeticError("Channel-separated optical-depth calls changed angle weights")
    return columns_nu + columns_compton, angle_weights, {
        "neutrino_columns": columns_nu,
        "compton_columns": columns_compton,
        "angle_weight_residual": angle_residual,
    }


def summarize_band(columns: np.ndarray, angle_weights: np.ndarray,
                   coupling: float, source_nu: np.ndarray,
                   source_compton: np.ndarray, source_total: np.ndarray,
                   energies: np.ndarray, band: tuple[float, float] = (210.0, 510.0),
                   upper_inclusive: bool = True) -> dict:
    mask = (energies >= band[0]) & (
        energies <= band[1] if upper_inclusive else energies < band[1]
    )
    if not np.any(mask):
        raise ValueError(f"No energy nodes in requested band {band}")
    nu = source_nu[:, mask]
    compton = source_compton[:, mask]
    source = source_total[:, mask]
    tau = coupling**2 * columns[:, :, mask]
    survival = np.exp(-tau)
    source_angle = source[:, None, :] * angle_weights[None, :, None]
    escaped_angle = source_angle * survival
    source_sum = float(np.sum(source))
    escaped_sum = float(np.sum(escaped_angle))
    nu_escaped = float(np.sum(nu[:, None, :] * angle_weights[None, :, None] * survival))
    compton_escaped = float(np.sum(
        compton[:, None, :] * angle_weights[None, :, None] * survival
    ))
    return {
        "energy_band_MeV": [float(band[0]), float(band[1])],
        "source_weight_per_g2": source_sum,
        "escaped_weight_per_g2": escaped_sum,
        "escape_probability": escaped_sum / source_sum,
        "mean_tau_source_weighted": float(np.sum(source_angle * tau) / source_sum),
        "mean_tau_escape_weighted": float(np.sum(escaped_angle * tau) / escaped_sum),
        "nu_source_fraction": float(np.sum(nu) / source_sum),
        "compton_source_fraction": float(np.sum(compton) / source_sum),
        "nu_escaped_source_fraction": nu_escaped / escaped_sum,
        "compton_escaped_source_fraction": compton_escaped / escaped_sum,
        "escape_luminosity_erg_s": coupling**2 * escaped_sum,
    }


def outer_temperature_sensitivity(inputs: dict, mass: float,
                                  angular_order: int, path_order: int) -> dict:
    coupling = inputs["coupling"]
    baseline_columns, angle_weights, baseline_detail = fixed_omega_columns(
        inputs, mass, angular_order, path_order
    )
    baseline = summarize_band(
        baseline_columns, angle_weights, coupling,
        inputs["source_nu"], inputs["source_compton"], inputs["source_total"],
        inputs["energies"]
    )
    scenarios = []

    def add_scenario(region: str, lo: float, hi: float, scale: float):
        varied = {
            key: np.asarray(value).copy()
            for key, value in inputs["opacity_profile"].items()
        }
        shell = (inputs["opacity_grid"] >= lo) & (inputs["opacity_grid"] <= hi)
        if not np.any(shell):
            raise RuntimeError(f"No opacity nodes in temperature shell {region}")
        varied["T"][shell] *= scale
        columns, weights, detail = fixed_omega_columns(
            inputs, mass, angular_order, path_order, varied
        )
        summary = summarize_band(
            columns, weights, coupling,
            inputs["source_nu"], inputs["source_compton"], inputs["source_total"],
            inputs["energies"]
        )
        scenarios.append({
            "scenario": (
                "baseline" if scale == 1.0
                else f"T({region}) {(scale-1.0)*100:+.0f}%"
            ),
            "region": region,
            "scale": float(scale),
            **summary,
            "escaped_high_energy_ratio_vs_baseline": (
                summary["escape_luminosity_erg_s"] / baseline["escape_luminosity_erg_s"] - 1.0
            ),
            "angle_weight_residual": detail["angle_weight_residual"],
        })

    scenarios.append({
        "scenario": "baseline",
        "region": "none",
        "scale": 1.0,
        **baseline,
        "escaped_high_energy_ratio_vs_baseline": 0.0,
        "angle_weight_residual": baseline_detail["angle_weight_residual"],
    })
    for scale in (0.7, 0.9, 1.1, 1.3):
        add_scenario("22-25", 22.0, 25.0, scale)
    for scale in (0.9, 1.1):
        add_scenario("20-22", 20.0, 22.0, scale)

    return {
        "title": "10 MeV high-energy escape response to outer-temperature stress tests",
        "status": "strict_numpy_transport_only_sensitivity",
        "mass_MeV": float(mass),
        "coupling": coupling,
        "energy_band_MeV": [210.0, 510.0],
        "profile_sha256": inputs["profile_sha256"],
        "fig7_sha256": inputs["fig7_sha256"],
        "configuration": {
            "source_radial_order": 200,
            "opacity_radial_order": 640,
            "energy_order": 200,
            "full_energy_nodes": int(len(inputs["full_energies"])),
            "high_energy_nodes": int(len(inputs["energies"])),
            "energy_nodes_MeV": inputs["energies"].tolist(),
            "temperature_variations": "opacity-only; B.1 source weights held fixed",
            "path_energy_convention": "fixed omega, printed Eq. (B.2)",
            "angular_order": angular_order,
            "path_order": path_order,
        },
        "results": scenarios,
        "limitations": [
            "Temperature changes are stress tests, not statistical uncertainty intervals.",
            "B.1 source weights are frozen; only B.2 opacity is recomputed.",
            "The profile is a public-figure reconstruction, not the original Garching simulation table.",
            "No opacity rescaling, source modification, or axial-vector result is made.",
        ],
    }


def bilinear_redshifted_columns(inputs: dict, mass: float,
                                angular_order: int, path_order: int):
    """B.2 redshift-only opacity using bilinear (r, omega_local) interpolation.

    This reproduces the interpolation prescription recorded in the archived
    V8 high-energy diagnostic. It is deliberately kept separate from
    redshifted_scalar_optical_depths(), which recomputes local rates directly
    from interpolated thermodynamic fields at each path node.
    """
    source_r = inputs["source_r"]
    source_lapse = inputs["source_profile"]["lapse"]
    radial_grid = inputs["opacity_grid"]
    profile = inputs["opacity_profile"]
    full_energies = inputs["full_energies"]
    source_energies = inputs["energies"]
    radius_km = inputs["radius_km"]

    rates = local_rates(
        mass, full_energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    opacity_grid_omega = rates["reduced_absorption"]

    angles, angle_weights = leggauss(angular_order)
    path_x, path_w = leggauss(path_order)
    path_w = path_w / 2.0
    columns = np.zeros((len(source_r), len(angles), len(source_energies)))
    min_energy_ratio = np.inf
    max_energy_ratio = 0.0
    min_local_velocity = 1.0

    for ia, cosine in enumerate(angles):
        r = source_r[:, None]
        smax = -cosine * r + np.sqrt(
            radius_km**2 - r**2 + r**2 * cosine**2
        )
        s = smax * (1.0 + path_x[None, :]) / 2.0
        position = np.sqrt(np.maximum(
            r**2 + s**2 + 2.0 * r * s * cosine, 0.0
        ))
        path_weights = smax * path_w[None, :]

        lapse_path = np.interp(
            position.ravel(), radial_grid, profile["lapse"]
        ).reshape(position.shape)
        omega_local = (
            source_energies[None, None, :]
            * source_lapse[:, None, None]
            / lapse_path[:, :, None]
        )
        ratio = omega_local / source_energies[None, None, :]
        min_energy_ratio = min(min_energy_ratio, float(np.min(ratio)))
        max_energy_ratio = max(max_energy_ratio, float(np.max(ratio)))
        velocity = np.sqrt(np.maximum(1.0 - (mass / omega_local)**2, 0.0))
        if np.any(velocity <= 0.0):
            raise FloatingPointError("A propagating path-redshift mode reached v_V=0")
        min_local_velocity = min(min_local_velocity, float(np.min(velocity)))

        # Locate the four corners of the (radius, local-energy) interpolation
        # cell for every source radius, path node, and selected emission energy.
        r_hi = np.searchsorted(radial_grid, position, side="right")
        r_hi = np.clip(r_hi, 1, len(radial_grid) - 1)
        r_lo = r_hi - 1
        r_fraction = (
            (position - radial_grid[r_lo])
            / (radial_grid[r_hi] - radial_grid[r_lo])
        )

        e_hi = np.searchsorted(full_energies, omega_local, side="right")
        e_hi = np.clip(e_hi, 1, len(full_energies) - 1)
        e_lo = e_hi - 1
        e_fraction = (
            (omega_local - full_energies[e_lo])
            / (full_energies[e_hi] - full_energies[e_lo])
        )

        rlo = r_lo[:, :, None]
        rhi = r_hi[:, :, None]
        low_r_low_e = opacity_grid_omega[rlo, e_lo]
        low_r_high_e = opacity_grid_omega[rlo, e_hi]
        high_r_low_e = opacity_grid_omega[rhi, e_lo]
        high_r_high_e = opacity_grid_omega[rhi, e_hi]

        low_r = low_r_low_e * (1.0 - e_fraction) + low_r_high_e * e_fraction
        high_r = high_r_low_e * (1.0 - e_fraction) + high_r_high_e * e_fraction
        reduced_along_path = (
            low_r * (1.0 - r_fraction[:, :, None])
            + high_r * r_fraction[:, :, None]
        )
        columns[:, ia, :] = (
            np.sum(
                path_weights[:, :, None] * reduced_along_path / velocity,
                axis=1
            ) * KM_TO_MEV_INV
        )

    info = {
        "minimum_local_to_source_energy_ratio": min_energy_ratio,
        "maximum_local_to_source_energy_ratio": max_energy_ratio,
        "minimum_local_vector_velocity": min_local_velocity,
        "interpolation": "bilinear in radius and local energy on the full opacity grid",
    }
    return columns, angle_weights / 2.0, info


def fixed_vs_redshift(inputs: dict, mass: float,
                      angular_order: int, path_order: int) -> dict:
    fixed_columns, fixed_weights, fixed_detail = fixed_omega_columns(
        inputs, mass, angular_order, path_order
    )

    # The archived V8 result specifies bilinear interpolation in radius and
    # local energy. Reproduce that algorithm explicitly before comparing.
    redshift_columns, redshift_weights, redshift_info = bilinear_redshifted_columns(
        inputs, mass, angular_order, path_order
    )
    angle_residual = float(np.max(np.abs(fixed_weights - redshift_weights)))
    if angle_residual > 1.0e-14:
        raise ArithmeticError("Fixed and path-redshift angular weights differ")

    # Independent alternative: evaluate local rates directly at each path
    # point. This is not the V8 interpolation algorithm and is retained as a
    # discretization/interpolation sensitivity check, not mixed into the
    # strict V8 comparison.
    direct_columns, direct_weights, direct_info = redshifted_scalar_optical_depths(
        inputs["source_r"], inputs["opacity_grid"], inputs["opacity_profile"],
        mass, inputs["energies"], inputs["radius_km"], angular_order, path_order,
        source_lapse=inputs["source_profile"]["lapse"]
    )
    direct_angle_residual = float(np.max(np.abs(fixed_weights - direct_weights)))
    if direct_angle_residual > 1.0e-14:
        raise ArithmeticError("Direct-rate and fixed angular weights differ")

    fixed = summarize_band(
        fixed_columns, fixed_weights, inputs["coupling"],
        inputs["source_nu"], inputs["source_compton"], inputs["source_total"],
        inputs["energies"]
    )
    redshift = summarize_band(
        redshift_columns, redshift_weights, inputs["coupling"],
        inputs["source_nu"], inputs["source_compton"], inputs["source_total"],
        inputs["energies"]
    )
    direct = summarize_band(
        direct_columns, direct_weights, inputs["coupling"],
        inputs["source_nu"], inputs["source_compton"], inputs["source_total"],
        inputs["energies"]
    )
    subbands = []
    for lo, hi in ((210.0, 300.0), (300.0, 510.0)):
        fixed_sub = summarize_band(
            fixed_columns, fixed_weights, inputs["coupling"],
            inputs["source_nu"], inputs["source_compton"], inputs["source_total"],
            inputs["energies"], (lo, hi), upper_inclusive=(hi == 510.0)
        )
        redshift_sub = summarize_band(
            redshift_columns, redshift_weights, inputs["coupling"],
            inputs["source_nu"], inputs["source_compton"], inputs["source_total"],
            inputs["energies"], (lo, hi), upper_inclusive=(hi == 510.0)
        )
        direct_sub = summarize_band(
            direct_columns, direct_weights, inputs["coupling"],
            inputs["source_nu"], inputs["source_compton"], inputs["source_total"],
            inputs["energies"], (lo, hi), upper_inclusive=(hi == 510.0)
        )
        subbands.append({
            "bin": f"{lo:g}-{hi:g} MeV",
            "fixed": fixed_sub,
            "path_redshift": redshift_sub,
            "direct_local_rate_recomputation": direct_sub,
            "relative_escaped_luminosity_change": (
                redshift_sub["escape_luminosity_erg_s"]
                / fixed_sub["escape_luminosity_erg_s"] - 1.0
            ),
            "direct_vs_bilinear_relative_difference": (
                direct_sub["escape_luminosity_erg_s"]
                / redshift_sub["escape_luminosity_erg_s"] - 1.0
            ),
        })

    return {
        "title": "10 MeV high-energy B.2 fixed-omega versus path-redshift comparison",
        "status": "strict_numpy_energy_resolved_diagnostic",
        "mass_MeV": float(mass),
        "coupling": inputs["coupling"],
        "profile_sha256": inputs["profile_sha256"],
        "fig7_sha256": inputs["fig7_sha256"],
        "configuration": {
            "emission_energy_band_MeV": [210.0, 510.0],
            "energy_nodes_MeV": inputs["energies"].tolist(),
            "source_radial_order": 200,
            "opacity_radial_order": 640,
            "energy_order": 200,
            "full_energy_node_count": int(len(inputs["full_energies"])),
            "high_energy_node_count": int(len(inputs["energies"])),
            "angular_order": angular_order,
            "path_order": path_order,
            "fixed_omega": "omega_local(s)=omega_source",
            "path_redshift": "omega_local(s)=omega_source*N(source)/N(path)",
            "path_redshift_opacity_interpolation": "bilinear in radius and local energy",
            "source_weights": "same B.1 source weights in both variants",
        },
        "fixed_omega": {
            **fixed,
            "source_per_g2": fixed["source_weight_per_g2"],
            "escaped_per_g2": fixed["escaped_weight_per_g2"],
            "escaped_luminosity_erg_s": fixed["escape_luminosity_erg_s"],
        },
        "path_redshift": {
            **redshift,
            "source_per_g2": redshift["source_weight_per_g2"],
            "escaped_per_g2": redshift["escaped_weight_per_g2"],
            "escaped_luminosity_erg_s": redshift["escape_luminosity_erg_s"],
            "kinematic_range": redshift_info,
        },
        "direct_local_rate_recomputation": {
            **direct,
            "source_per_g2": direct["source_weight_per_g2"],
            "escaped_per_g2": direct["escaped_weight_per_g2"],
            "escaped_luminosity_erg_s": direct["escape_luminosity_erg_s"],
            "kinematic_range": direct_info,
            "qualification": (
                "Independent alternative that recomputes local rates from "
                "interpolated thermodynamic fields at each path node; not the "
                "bilinear opacity interpolation used by the archived V8 result."
            ),
        },
        "interpolation_sensitivity": {
            "direct_vs_bilinear_escaped_luminosity_relative_difference": (
                direct["escape_luminosity_erg_s"]
                / redshift["escape_luminosity_erg_s"] - 1.0
            ),
            "direct_vs_bilinear_escape_probability_relative_difference": (
                direct["escape_probability"] / redshift["escape_probability"] - 1.0
            ),
            "direct_vs_bilinear_mean_tau_relative_difference": (
                direct["mean_tau_source_weighted"]
                / redshift["mean_tau_source_weighted"] - 1.0
            ),
        },
        "relative_change": {
            "escaped_luminosity": (
                redshift["escape_luminosity_erg_s"] / fixed["escape_luminosity_erg_s"] - 1.0
            ),
            "escape_probability": redshift["escape_probability"] / fixed["escape_probability"] - 1.0,
            "mean_tau_source_weighted": (
                redshift["mean_tau_source_weighted"] / fixed["mean_tau_source_weighted"] - 1.0
            ),
        },
        "sub_bands": subbands,
        "checks": {
            "source_weight_per_g2": fixed["source_weight_per_g2"],
            "fixed_escape_per_g2": fixed["escaped_weight_per_g2"],
            "fixed_angle_weight_sum": float(np.sum(fixed_weights)),
            "redshift_angle_weight_sum": float(np.sum(redshift_weights)),
            "angle_weight_max_absolute_residual": angle_residual,
            "direct_angle_weight_max_absolute_residual": direct_angle_residual,
            "fixed_channel_angle_weight_residual": fixed_detail["angle_weight_residual"],
        },
    }


def add_v8_comparisons(outer: dict, redshift: dict,
                       v8_outer_path: Path, v8_redshift_path: Path):
    v8_outer = json.loads(v8_outer_path.read_text(encoding="utf-8"))["result"]
    v8_redshift = json.loads(v8_redshift_path.read_text(encoding="utf-8"))["result"]
    v8_outer_rows = {row["scenario"]: row for row in v8_outer["results"]}
    outer_comparison = {}
    for row in outer["results"]:
        old = v8_outer_rows[row["scenario"]]
        outer_comparison[row["scenario"]] = {
            key: {
                "numpy": float(row[key]),
                "v8": float(old[key]),
                "relative_residual": float(row[key]) / float(old[key]) - 1.0 if old[key] else None,
            }
            for key in (
                "source_weight_per_g2", "escaped_weight_per_g2",
                "escape_probability", "mean_tau_source_weighted",
                "mean_tau_escape_weighted", "escape_luminosity_erg_s",
                "escaped_high_energy_ratio_vs_baseline",
            )
        }
    redshift_comparison = {}
    for label, numpy_row, v8_row in (
        ("fixed_omega", redshift["fixed_omega"], v8_redshift["fixed_omega"]),
        ("path_redshift", redshift["path_redshift"], v8_redshift["path_redshift"]),
    ):
        redshift_comparison[label] = {}
        for key in (
            "source_per_g2", "escaped_per_g2", "escape_probability",
            "mean_tau_source_weighted", "mean_tau_escape_weighted",
            "nu_source_fraction", "compton_source_fraction",
            "nu_escaped_source_fraction", "compton_escaped_source_fraction",
            "escaped_luminosity_erg_s",
        ):
            old = float(v8_row[key])
            new = float(numpy_row[key])
            redshift_comparison[label][key] = {
                "numpy": new, "v8": old,
                "relative_residual": new / old - 1.0 if old else None,
            }
    redshift_comparison["relative_change"] = {
        key: {
            "numpy": float(redshift["relative_change"][key]),
            "v8": float(v8_redshift["relative_change"][key]),
            "absolute_difference": float(redshift["relative_change"][key]) - float(v8_redshift["relative_change"][key]),
        }
        for key in ("escaped_luminosity", "escape_probability", "mean_tau_source_weighted")
    }
    outer["comparison_to_archived_v8"] = {
        "reference_json_sha256": sha256(v8_outer_path),
        "scenarios": outer_comparison,
    }
    redshift["comparison_to_archived_v8"] = {
        "reference_json_sha256": sha256(v8_redshift_path),
        "quantities": redshift_comparison,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--v8-outer", type=Path, default=DEFAULT_V8_OUTER)
    parser.add_argument("--v8-redshift", type=Path, default=DEFAULT_V8_REDSHIFT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--radial-order", type=int, default=200)
    parser.add_argument("--opacity-order", type=int, default=640)
    parser.add_argument("--energy-order", type=int, default=200)
    parser.add_argument("--angular-order", type=int, default=32)
    parser.add_argument("--path-order", type=int, default=64)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()

    inputs = build_inputs(
        args.profile, args.fig7, args.mass, args.radial_order,
        args.opacity_order, args.energy_order, args.radius, args.energy_offset
    )
    outer = outer_temperature_sensitivity(
        inputs, args.mass, args.angular_order, args.path_order
    )
    redshift = fixed_vs_redshift(
        inputs, args.mass, args.angular_order, args.path_order
    )
    add_v8_comparisons(outer, redshift, args.v8_outer, args.v8_redshift)

    common = {
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "script_sha256": sha256(Path(__file__)),
        "runtime": {
            "engine": "Python/NumPy/SciPy",
            "numpy": np.__version__,
        },
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    outer_path = args.output_dir / "b16_high_energy_outer_temperature_sensitivity_10mev_2026-11-15_numpy.json"
    redshift_path = args.output_dir / "b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-15_numpy.json"
    outer_path.write_text(json.dumps({**common, "result": outer}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    redshift_path.write_text(json.dumps({**common, "result": redshift}, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "outer_temperature": {
            row["scenario"]: {
                "escape_probability": row["escape_probability"],
                "escaped_luminosity_erg_s": row["escape_luminosity_erg_s"],
                "ratio_vs_baseline": row["escaped_high_energy_ratio_vs_baseline"],
            }
            for row in outer["results"]
        },
        "fixed_vs_redshift": {
            "fixed_escape_probability": redshift["fixed_omega"]["escape_probability"],
            "redshift_escape_probability": redshift["path_redshift"]["escape_probability"],
            "escaped_luminosity_change": redshift["relative_change"]["escaped_luminosity"],
            "mean_tau_change": redshift["relative_change"]["mean_tau_source_weighted"],
        },
        "output_files": [str(outer_path), str(redshift_path)],
    }, indent=2))


if __name__ == "__main__":
    main()
