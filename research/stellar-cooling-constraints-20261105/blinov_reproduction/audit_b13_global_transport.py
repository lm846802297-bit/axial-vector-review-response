"""Global B.13 exact-Compton replacement test for the 10 MeV vector benchmark.

This diagnostic replaces the B.14--B.16 Compton source and reduced opacity
together, then evaluates the same Eq. (B.1)/(B.2) luminosity integral. It
retains the literal scalar, mode-summed B.2 prescription so that the only
changed collision channel is Compton. It does not update any production
constraint curve.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FINITE_MIXING = ROOT / "finite_mixing"
for item in (ROOT, FINITE_MIXING):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from blinov_reproduction.reference import (  # noqa: E402
    DEFAULT_PROFILE, radial_rule, load_profile, local_rates, scalar_optical_depths,
)
from blinov_reproduction.audit_b16_global_redshift import eq_b1_source_measure  # noqa: E402
from moving_muon_compton import moving_muon_compton_rates  # noqa: E402

DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_BASELINE = HERE / "outputs" / "b16_global_fig7_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b13_global_transport_vertex_preserving_10mev_2026-11-09.json"
MASS_MEV = 10.0
BASE_ORDERS = (12, 8, 8, 8)
REFINED_ORDERS = (16, 10, 10, 10)


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _curve_metrics(values, reference):
    values = np.asarray(values, float)
    reference = np.asarray(reference, float)
    rel = values / reference - 1.0
    peak = int(np.argmax(reference))
    return {
        "mean_absolute_relative_difference": float(np.mean(np.abs(rel))),
        "maximum_absolute_relative_difference": float(np.max(np.abs(rel))),
        "weak_endpoint_relative_difference": float(rel[0]),
        "reference_peak_relative_difference": float(rel[peak]),
        "strong_endpoint_relative_difference": float(rel[-1]),
    }


def _source_from_production(r, rw, energies, lapse_source, mass, production):
    return eq_b1_source_measure(
        r, rw, energies, lapse_source, mass, production
    )[0]


def _luminosity_curve(source, columns, couplings, reference_luminosity, angle_weights):
    rows = []
    luminosities = []
    thin_values = []
    escape_values = []
    for coupling, ref_lum in zip(couplings, reference_luminosity):
        escape = np.exp(-coupling * coupling * columns)
        angle_averaged_escape = np.einsum("rae,a->re", escape, angle_weights)
        thin = float(coupling * coupling * np.sum(source))
        luminosity = float(
            coupling * coupling * np.sum(source * angle_averaged_escape)
        )
        luminosities.append(luminosity)
        thin_values.append(thin)
        escape_values.append(luminosity / thin if thin > 0.0 else 0.0)
        rows.append({
            "g": float(coupling),
            "reference_luminosity_erg_s": float(ref_lum),
            "calculated_luminosity_erg_s": luminosity,
            "relative_difference_vs_fig7": luminosity / float(ref_lum) - 1.0,
            "optically_thin_luminosity_erg_s": thin,
            "escape_fraction": luminosity / thin if thin > 0.0 else 0.0,
        })
    return {
        "metrics_vs_fig7": _curve_metrics(luminosities, reference_luminosity),
        "thin_luminosity_ratio_vs_B16": (
            float(np.sum(source) / np.sum(_B16_SOURCE))
        ),
        "points": rows,
        "_luminosities": luminosities,
        "_thin": thin_values,
        "_escape": escape_values,
    }


# Set by run() immediately before evaluating the diagnostic variants.
_B16_SOURCE = None


def _species_totals(exact, species):
    item = exact["charge_resolved"][species]
    return (
        float(np.sum(item["production"])),
        float(np.sum(item["absorption"])),
        np.asarray(item["production"], float),
        np.asarray(item["absorption"], float),
    )


def _relative_residual(a, b):
    return float(abs(a - b) / max(abs(a), abs(b), 1.0e-300))


def run(
    profile_path=DEFAULT_PROFILE,
    fig7_path=DEFAULT_FIG7,
    baseline_path=DEFAULT_BASELINE,
    output_path=DEFAULT_OUTPUT,
    mass=MASS_MEV,
    radial_order=40,
    energy_order=100,
    angular_order=16,
    path_order=32,
    radius_km=25.0,
    energy_offset=1000.0,
    base_orders=BASE_ORDERS,
    refined_orders=REFINED_ORDERS,
    active_opacity_fraction_threshold=1.0e-8,
):
    global _B16_SOURCE
    started = time.time()

    fig7 = json.loads(Path(fig7_path).read_text(encoding="utf-8"))
    key = str(float(mass))
    vertices = fig7["reference_vertices"][key]
    couplings = np.asarray(vertices["g"], float)
    reference_luminosity = np.asarray(vertices["luminosity_erg_s"], float)

    r, rw = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
    profile = load_profile(profile_path, radial_grid)
    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), energy_offset, energy_order
    )
    energies = np.unique(np.r_[energies, mass / profile["lapse"]])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()

    # B.14--B.16 reference rates and exact B.1 source measure.
    rates_b16 = local_rates(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    source_index = np.searchsorted(radial_grid, r)
    lapse_source = profile["lapse"][source_index]
    source_b16 = _source_from_production(
        r, rw, energies, lapse_source, mass,
        rates_b16["production"][source_index]
    )
    _B16_SOURCE = source_b16

    columns_b16, angle_weights = scalar_optical_depths(
        r, radial_grid, rates_b16["reduced_absorption"],
        mass, energies, radius_km, angular_order, path_order
    )

    # Reproduce the archived B.16 calculation before introducing B.13.
    archived = json.loads(Path(baseline_path).read_text(encoding="utf-8"))
    archived_result = archived["results"][0]
    if float(archived_result["mass_MeV"]) != float(mass):
        raise ValueError("Archived B.16 baseline has a different mediator mass")
    if archived_result["profile"]["sha256"] != sha256(profile_path):
        raise ValueError("Archived B.16 baseline does not use the current profile SHA")
    archived_points = archived_result["eq_b2_fixed_omega_baseline"]["points"]
    if len(archived_points) != len(couplings):
        raise ValueError("Archived B.16 baseline has a different Fig. 7 coupling grid")

    b16_check = _luminosity_curve(
        source_b16, columns_b16, couplings, reference_luminosity, angle_weights
    )
    archived_lum = np.asarray(
        [item["calculated_luminosity_erg_s"] for item in archived_points], float
    )
    b16_reproduction_residual = float(np.max(
        np.abs(np.asarray(b16_check["_luminosities"]) - archived_lum)
        / np.maximum(np.abs(archived_lum), 1.0e-300)
    ))
    if b16_reproduction_residual > 2.0e-10:
        raise ArithmeticError(
            "B.16 baseline closure failed before B.13 replacement: "
            f"{b16_reproduction_residual:.3e}"
        )

    x = energies[None, :] / profile["T"][:, None]
    detailed_balance_factor = np.expm1(np.minimum(x, 700.0))
    reduced_nu = detailed_balance_factor * rates_b16["neutrino_production"]
    reduced_dimuon = detailed_balance_factor * rates_b16["dimuon_production"]
    reduced_b16_compton = np.maximum(
        rates_b16["reduced_absorption"] - reduced_nu - reduced_dimuon, 0.0
    )
    local_compton_fraction = np.divide(
        reduced_b16_compton,
        rates_b16["reduced_absorption"],
        out=np.zeros_like(reduced_b16_compton),
        where=rates_b16["reduced_absorption"] > 0.0,
    )
    max_fraction_by_radius = np.max(local_compton_fraction, axis=1)
    active_radius_mask = (
        max_fraction_by_radius >= active_opacity_fraction_threshold
    )

    # Energies below the smallest B.1 escape threshold are never emitted by
    # any source radius and therefore need no B.13 evaluation in B.2 either.
    global_emission_threshold = float(np.min(mass / lapse_source))
    active_energy_mask = energies > global_emission_threshold * (1.0 + 1.0e-12)

    # Initialize the exact arrays to the B.16 values. Where the B.16 Compton
    # fraction is below the declared threshold, retaining B.16 is a bounded
    # transport approximation; its source and tau weights are quantified below.
    b13_minus_production = np.asarray(
        rates_b16["compton_production"], float
    ).copy()
    b13_plus_production = np.zeros_like(b13_minus_production)
    b13_minus_reduced = reduced_b16_compton.copy()
    b13_plus_reduced = np.zeros_like(b13_minus_reduced)

    max_residuals = {
        "mu_minus_mode_detailed_balance": 0.0,
        "mu_plus_mode_detailed_balance": 0.0,
        "mu_minus_absorption_vs_production": 0.0,
        "mu_plus_absorption_vs_production": 0.0,
        "final_muon_shell": 0.0,
    }
    computed_points = 0
    ratio_grid = np.full_like(b13_minus_production, np.nan)
    total_points = int(np.count_nonzero(active_radius_mask)
                       * np.count_nonzero(active_energy_mask))
    ratio_samples = []

    active_indices = np.flatnonzero(active_radius_mask)
    for irank, ir in enumerate(active_indices, start=1):
        temperature = float(profile["T"][ir])
        mu_mu = float(profile["mu_mu"][ir])
        for ie in np.flatnonzero(active_energy_mask):
            omega = float(energies[ie])
            exact = moving_muon_compton_rates(
                mass, omega, temperature, mu_mu,
                1.0, 0.0, orders=tuple(base_orders)
            )
            pm, am, pm_modes, am_modes = _species_totals(exact, "mu_minus")
            pp, ap, pp_modes, ap_modes = _species_totals(exact, "mu_plus")
            boltzmann = float(np.exp(-omega / temperature))
            reduced_factor = float(-np.expm1(-omega / temperature))

            dbm = float(np.max(
                np.abs(pm_modes - boltzmann * am_modes)
                / np.maximum(np.abs(pm_modes), 1.0e-300)
            ))
            dbp = float(np.max(
                np.abs(pp_modes - boltzmann * ap_modes)
                / np.maximum(np.abs(pp_modes), 1.0e-300)
            ))
            max_residuals["mu_minus_mode_detailed_balance"] = max(
                max_residuals["mu_minus_mode_detailed_balance"], dbm
            )
            max_residuals["mu_plus_mode_detailed_balance"] = max(
                max_residuals["mu_plus_mode_detailed_balance"], dbp
            )
            max_residuals["mu_minus_absorption_vs_production"] = max(
                max_residuals["mu_minus_absorption_vs_production"],
                _relative_residual(pm, boltzmann * am)
            )
            max_residuals["mu_plus_absorption_vs_production"] = max(
                max_residuals["mu_plus_absorption_vs_production"],
                _relative_residual(pp, boltzmann * ap)
            )
            max_residuals["final_muon_shell"] = max(
                max_residuals["final_muon_shell"],
                float(exact["diagnostics"]["final_muon_shell_relative_error"])
            )

            b13_minus_production[ir, ie] = pm
            b13_plus_production[ir, ie] = pp
            b13_minus_reduced[ir, ie] = reduced_factor * am
            b13_plus_reduced[ir, ie] = reduced_factor * ap

            b16_local = float(rates_b16["compton_production"][ir, ie])
            if b16_local > 1.0e-280:
                ratio_value = pm / b16_local
                ratio_samples.append(ratio_value)
                ratio_grid[ir, ie] = ratio_value

            computed_points += 1
        print(
            f"B.13 exact grid: radius {irank}/{len(active_indices)} "
            f"({radial_grid[ir]:.6f} km), {computed_points}/{total_points} "
            f"points completed",
            flush=True,
        )

    # The mu-minus-only case is the like-for-like comparison with the single
    # negative-muon B.17 convention. The both-charge case is reported as the
    # physical charge-summed extension. Both replace source and opacity.
    b13_both_production = b13_minus_production + b13_plus_production
    b13_both_reduced = b13_minus_reduced + b13_plus_reduced

    production_b13_minus = (
        rates_b16["neutrino_production"]
        + rates_b16["dimuon_production"]
        + b13_minus_production
    )
    production_b13_both = (
        rates_b16["neutrino_production"]
        + rates_b16["dimuon_production"]
        + b13_both_production
    )
    source_b13_minus = _source_from_production(
        r, rw, energies, lapse_source, mass,
        production_b13_minus[source_index]
    )
    source_b13_both = _source_from_production(
        r, rw, energies, lapse_source, mass,
        production_b13_both[source_index]
    )

    reduced_b13_minus_total = reduced_nu + reduced_dimuon + b13_minus_reduced
    reduced_b13_both_total = reduced_nu + reduced_dimuon + b13_both_reduced
    columns_b13_minus, angles_minus = scalar_optical_depths(
        r, radial_grid, reduced_b13_minus_total,
        mass, energies, radius_km, angular_order, path_order
    )
    columns_b13_both, angles_both = scalar_optical_depths(
        r, radial_grid, reduced_b13_both_total,
        mass, energies, radius_km, angular_order, path_order
    )
    angle_residual = max(
        float(np.max(np.abs(angles_minus - angle_weights))),
        float(np.max(np.abs(angles_both - angle_weights))),
    )
    if angle_residual > 1.0e-14:
        raise ArithmeticError("B.13 replacement changed the B.2 angular weights")

    # Quantify the region left at the B.16 Compton value by the active-node
    # threshold. These are source-weighted and path-weighted omissions.
    source_compton_b16 = _source_from_production(
        r, rw, energies, lapse_source, mass,
        rates_b16["compton_production"][source_index]
    )
    source_inactive = source_b16[
        ~active_radius_mask[source_index], :
    ]
    source_compton_inactive = source_compton_b16[
        ~active_radius_mask[source_index], :
    ]
    inactive_source_fraction = (
        float(np.sum(source_inactive) / np.sum(source_b16))
        if np.sum(source_b16) else 0.0
    )
    inactive_compton_source_fraction = (
        float(np.sum(source_compton_inactive) / np.sum(source_compton_b16))
        if np.sum(source_compton_b16) else 0.0
    )
    inactive_reduced_compton = np.where(
        active_radius_mask[:, None], 0.0, reduced_b16_compton
    )
    inactive_compton_columns, _ = scalar_optical_depths(
        r, radial_grid, inactive_reduced_compton,
        mass, energies, radius_km, angular_order, path_order
    )
    baseline_mean_tau = float(np.sum(
        source_b16 * np.einsum("rae,a->re", columns_b16, angle_weights)
    ) / np.sum(source_b16))
    inactive_compton_mean_tau = float(np.sum(
        source_b16 * np.einsum("rae,a->re", inactive_compton_columns, angle_weights)
    ) / np.sum(source_b16))
    inactive_compton_tau_fraction = (
        inactive_compton_mean_tau / baseline_mean_tau
        if baseline_mean_tau > 0.0 else 0.0
    )

    # Independent local refinement at the three representative points already
    # used in the radial B.13 audit.
    refinement_checks = []
    for radius, omega in ((8.0, 15.0), (12.5, 20.0), (15.0, 30.0)):
        temperature = float(np.interp(radius, radial_grid, profile["T"]))
        mu_mu = float(np.interp(radius, radial_grid, profile["mu_mu"]))
        base = moving_muon_compton_rates(
            mass, omega, temperature, mu_mu, 1.0, 0.0,
            orders=tuple(base_orders)
        )
        fine = moving_muon_compton_rates(
            mass, omega, temperature, mu_mu, 1.0, 0.0,
            orders=tuple(refined_orders)
        )
        row = {"radius_km": radius, "omega_MeV": omega}
        for species in ("mu_minus", "mu_plus"):
            p_base = float(np.sum(base["charge_resolved"][species]["production"]))
            p_fine = float(np.sum(fine["charge_resolved"][species]["production"]))
            row[f"{species}_relative_refinement_change"] = _relative_residual(
                p_fine, p_base
            )
        refinement_checks.append(row)

    variants = {
        "B16_reference": (source_b16, columns_b16),
        "B13_mu_minus_source_only": (source_b13_minus, columns_b16),
        "B13_mu_minus_opacity_only": (source_b16, columns_b13_minus),
        "B13_mu_minus_consistent_source_and_opacity": (
            source_b13_minus, columns_b13_minus
        ),
        "B13_both_charges_source_only": (source_b13_both, columns_b16),
        "B13_both_charges_opacity_only": (source_b16, columns_b13_both),
        "B13_both_charges_consistent_source_and_opacity": (
            source_b13_both, columns_b13_both
        ),
    }

    variant_results = {}
    for name, (source, columns) in variants.items():
        curve = _luminosity_curve(
            source, columns, couplings, reference_luminosity, angle_weights
        )
        variant_results[name] = {
            "metrics_vs_fig7": curve["metrics_vs_fig7"],
            "thin_luminosity_ratio_vs_B16": curve["thin_luminosity_ratio_vs_B16"],
            "points": curve["points"],
            "mean_escape_fraction": float(np.mean(curve["_escape"])),
            "strong_endpoint_escape_fraction": float(curve["_escape"][-1]),
        }

    # Source-channel decomposition and charge fraction in the exact Compton
    # source. The same Eq. (B.1) measure is used for every channel.
    source_nu = _source_from_production(
        r, rw, energies, lapse_source, mass,
        rates_b16["neutrino_production"][source_index]
    )
    source_dimuon = _source_from_production(
        r, rw, energies, lapse_source, mass,
        rates_b16["dimuon_production"][source_index]
    )
    source_compton_minus = _source_from_production(
        r, rw, energies, lapse_source, mass,
        b13_minus_production[source_index]
    )
    source_compton_plus = _source_from_production(
        r, rw, energies, lapse_source, mass,
        b13_plus_production[source_index]
    )
    source_compton_both = source_compton_minus + source_compton_plus
    source_channel_summary = {
        "B16_reference": {
            "neutrino_fraction": float(np.sum(source_nu) / np.sum(source_b16)),
            "Compton_fraction": float(np.sum(source_compton_b16) / np.sum(source_b16)),
            "dimuon_fraction": float(np.sum(source_dimuon) / np.sum(source_b16)),
        },
        "B13_mu_minus": {
            "neutrino_fraction": float(np.sum(source_nu) / np.sum(source_b13_minus)),
            "Compton_fraction": float(np.sum(source_compton_minus) / np.sum(source_b13_minus)),
            "dimuon_fraction": float(np.sum(source_dimuon) / np.sum(source_b13_minus)),
        },
        "B13_both_charges": {
            "neutrino_fraction": float(np.sum(source_nu) / np.sum(source_b13_both)),
            "Compton_fraction": float(np.sum(source_compton_both) / np.sum(source_b13_both)),
            "dimuon_fraction": float(np.sum(source_dimuon) / np.sum(source_b13_both)),
        },
        "mu_plus_fraction_of_B13_Compton_source": (
            float(np.sum(source_compton_plus) / np.sum(source_compton_both))
            if np.sum(source_compton_both) else 0.0
        ),
    }

    # Source-weighted radial decomposition: this reveals whether the
    # strongest B.13/B.16 change is concentrated in the dense inner core.
    source_shell_edges = (0.0, 5.0, 8.0, 10.0, 12.0, 15.0, 18.0, 25.0)
    strong_g = float(couplings[-1])
    escape_b16_strong = np.einsum(
        "rae,a->re", np.exp(-strong_g**2 * columns_b16), angle_weights
    )
    escape_b13_minus_strong = np.einsum(
        "rae,a->re", np.exp(-strong_g**2 * columns_b13_minus), angle_weights
    )
    escape_b13_both_strong = np.einsum(
        "rae,a->re", np.exp(-strong_g**2 * columns_b13_both), angle_weights
    )
    radial_source_diagnostics = []
    for lo, hi in zip(source_shell_edges[:-1], source_shell_edges[1:]):
        mask = (r >= lo) & ((r < hi) if hi < radius_km else (r <= hi))
        if not np.any(mask):
            continue
        b16_total = float(np.sum(source_b16[mask]))
        b13m_total = float(np.sum(source_b13_minus[mask]))
        b13b_total = float(np.sum(source_b13_both[mask]))
        b16_comp = float(np.sum(source_compton_b16[mask]))
        b13m_comp = float(np.sum(source_compton_minus[mask]))
        b13p_comp = float(np.sum(source_compton_plus[mask]))
        b13b_comp = b13m_comp + b13p_comp
        b16_escaped = float(np.sum(source_b16[mask] * escape_b16_strong[mask]))
        b13m_escaped = float(np.sum(source_b13_minus[mask] * escape_b13_minus_strong[mask]))
        b13b_escaped = float(np.sum(source_b13_both[mask] * escape_b13_both_strong[mask]))
        radial_source_diagnostics.append({
            "emission_shell_km": [lo, hi],
            "B16_total_B1_source_fraction": (
                b16_total / float(np.sum(source_b16)) if np.sum(source_b16) else 0.0
            ),
            "B13_mu_minus_total_B1_source_fraction": (
                b13m_total / float(np.sum(source_b13_minus))
                if np.sum(source_b13_minus) else 0.0
            ),
            "B13_both_charges_total_B1_source_fraction": (
                b13b_total / float(np.sum(source_b13_both))
                if np.sum(source_b13_both) else 0.0
            ),
            "B13_mu_minus_over_B16_Compton_source_ratio": (
                b13m_comp / b16_comp if b16_comp else None
            ),
            "B13_both_charges_over_B16_Compton_source_ratio": (
                b13b_comp / b16_comp if b16_comp else None
            ),
            "mu_plus_fraction_of_B13_Compton_source": (
                b13p_comp / b13b_comp if b13b_comp else 0.0
            ),
            "B16_strong_endpoint_escape_fraction_in_shell": (
                b16_escaped / b16_total if b16_total else None
            ),
            "B13_mu_minus_strong_endpoint_escape_fraction_in_shell": (
                b13m_escaped / b13m_total if b13m_total else None
            ),
            "B13_both_charges_strong_endpoint_escape_fraction_in_shell": (
                b13b_escaped / b13b_total if b13b_total else None
            ),
        })

    # Source-weighted mean optical depths isolate the Compton opacity change
    # from the neutrino inverse-decay opacity. They are diagnostics, not a
    # replacement for the nonlinear direction-averaged escape integral.
    columns_b16_compton, _ = scalar_optical_depths(
        r, radial_grid, reduced_b16_compton,
        mass, energies, radius_km, angular_order, path_order
    )
    columns_b13_minus_compton, _ = scalar_optical_depths(
        r, radial_grid, b13_minus_reduced,
        mass, energies, radius_km, angular_order, path_order
    )
    columns_b13_both_compton, _ = scalar_optical_depths(
        r, radial_grid, b13_both_reduced,
        mass, energies, radius_km, angular_order, path_order
    )

    def source_weighted_tau(source, columns):
        average = np.einsum("rae,a->re", columns, angle_weights)
        return float(np.sum(source * average) / np.sum(source))

    opacity_weighted_diagnostics = {
        "B16_source_weighted_B16_Compton_tau_per_g2": source_weighted_tau(
            source_b16, columns_b16_compton
        ),
        "B16_source_weighted_B13_mu_minus_Compton_tau_per_g2": source_weighted_tau(
            source_b16, columns_b13_minus_compton
        ),
        "B13_mu_minus_source_weighted_B13_mu_minus_Compton_tau_per_g2": source_weighted_tau(
            source_b13_minus, columns_b13_minus_compton
        ),
        "B13_both_charge_source_weighted_B13_both_charge_Compton_tau_per_g2": source_weighted_tau(
            source_b13_both, columns_b13_both_compton
        ),
        "B16_source_weighted_B16_total_tau_per_g2": source_weighted_tau(
            source_b16, columns_b16
        ),
        "B13_mu_minus_source_weighted_B13_mu_minus_total_tau_per_g2": source_weighted_tau(
            source_b13_minus, columns_b13_minus
        ),
        "B13_both_charge_source_weighted_B13_both_charge_total_tau_per_g2": source_weighted_tau(
            source_b13_both, columns_b13_both
        ),
    }

    radial_rate_ratio_summary = []
    for ir, radius in enumerate(radial_grid):
        vals = ratio_grid[ir, np.isfinite(ratio_grid[ir])]
        if len(vals):
            radial_rate_ratio_summary.append({
                "radius_km": float(radius),
                "energy_node_count": int(len(vals)),
                "B13_mu_minus_over_B16_production_min": float(np.min(vals)),
                "B13_mu_minus_over_B16_production_median": float(np.median(vals)),
                "B13_mu_minus_over_B16_production_max": float(np.max(vals)),
            })

    active_radii = radial_grid[active_radius_mask]
    inactive_radii = radial_grid[~active_radius_mask]
    ratio_array = np.asarray(ratio_samples, float)
    output = {
        "title": "Global B.13 exact moving-muon Compton replacement in the 10 MeV vector B.1/B.2 benchmark",
        "mass_MeV": float(mass),
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "identity": "1687-row vertex-preserving reconstruction from public figures; not raw Garching simulation output",
        },
        "fig7_reference": {
            "path": str(fig7_path),
            "sha256": sha256(fig7_path),
            "points": int(len(couplings)),
        },
        "archived_B16_baseline": {
            "path": str(baseline_path),
            "sha256": sha256(baseline_path),
            "max_relative_reproduction_residual": b16_reproduction_residual,
        },
        "configuration": {
            "radial_order": int(radial_order),
            "energy_order": int(energy_order),
            "energy_offset_MeV": float(energy_offset),
            "angular_order": int(angular_order),
            "path_order": int(path_order),
            "radius_km": float(radius_km),
            "B13_kernel_orders": list(base_orders),
            "B13_refined_orders": list(refined_orders),
            "B13_current": "pure vector, g_V=1, g_A=0, rates per g_X^2",
            "B2_convention": "literal scalar mode-summed opacity in the fixed-omega Eq. (B.2) ray exponent",
            "charge_cases": {
                "mu_minus_only": "like-for-like with the single negative-muon distribution in B.17",
                "both_charges": "mu-minus plus mu-plus exact moving-muon Compton rates",
            },
            "active_opacity_fraction_threshold": float(active_opacity_fraction_threshold),
            "active_radial_node_count": int(len(active_indices)),
            "active_radial_nodes_km": active_radii.tolist(),
            "inactive_radial_nodes_km": inactive_radii.tolist(),
            "active_energy_node_count": int(np.count_nonzero(active_energy_mask)),
            "global_emission_threshold_MeV": global_emission_threshold,
            "exact_B13_kernel_evaluations": int(computed_points),
            "wall_time_seconds": float(time.time() - started),
        },
        "inactive_region_omission_diagnostic": {
            "maximum_inactive_local_B16_Compton_fraction_of_total_opacity": (
                float(np.max(max_fraction_by_radius[~active_radius_mask]))
                if np.any(~active_radius_mask) else 0.0
            ),
            "inactive_radial_nodes_fraction_of_total_B1_source": inactive_source_fraction,
            "inactive_radial_nodes_fraction_of_B16_Compton_source": inactive_compton_source_fraction,
            "inactive_radial_nodes_fraction_of_source_weighted_mean_B16_optical_depth": (
                inactive_compton_tau_fraction
            ),
            "interpretation": (
                "At inactive radial nodes the B.16 Compton term is retained. "
                "The omitted B.13 replacement is restricted to nodes whose "
                "maximum local Compton fraction is below the declared threshold; "
                "the associated B.1 source and B.2 path weights are reported."
            ),
        },
        "B13_numerical_validation": {
            "maximum_residuals": max_residuals,
            "refinement_checks": refinement_checks,
            "B13_mu_minus_over_B16_mu_minus_production_ratio": {
                "minimum": float(np.min(ratio_array)) if len(ratio_array) else None,
                "maximum": float(np.max(ratio_array)) if len(ratio_array) else None,
                "median": float(np.median(ratio_array)) if len(ratio_array) else None,
            },
            "mu_plus_fraction_of_exact_Compton_reduced_absorption_unweighted_grid_sum": (
                float(np.sum(b13_plus_reduced) / np.sum(b13_both_reduced))
                if np.sum(b13_both_reduced) else 0.0
            ),
            "angle_weight_residual": angle_residual,
        },
        "source_channel_fractions": source_channel_summary,
        "radial_source_diagnostics": radial_source_diagnostics,
        "opacity_weighted_diagnostics": opacity_weighted_diagnostics,
        "B13_local_rate_ratio_by_radius": radial_rate_ratio_summary,
        "local_rate_grid": {
            "radial_grid_km": radial_grid.tolist(),
            "energies_MeV": energies.tolist(),
            "active_radial_mask": active_radius_mask.tolist(),
            "active_energy_mask": active_energy_mask.tolist(),
            "B16_Compton_production_per_gX2": rates_b16["compton_production"].tolist(),
            "B13_mu_minus_Compton_production_per_gX2": b13_minus_production.tolist(),
            "B13_mu_plus_Compton_production_per_gX2": b13_plus_production.tolist(),
            "B16_Compton_reduced_absorption_per_gX2": reduced_b16_compton.tolist(),
            "B13_mu_minus_Compton_reduced_absorption_per_gX2": b13_minus_reduced.tolist(),
            "B13_mu_plus_Compton_reduced_absorption_per_gX2": b13_plus_reduced.tolist(),
            "B16_neutrino_production_per_gX2": rates_b16["neutrino_production"].tolist(),
            "B16_neutrino_reduced_absorption_per_gX2": reduced_nu.tolist(),
        },
        "variant_results": variant_results,
        "scope": [
            "B.13 exact Compton production and reduced absorption are replaced together in the consistent variants.",
            "B.13 mu-minus-only and mu-minus-plus-mu-plus cases are reported separately.",
            "The B.16 neutrino inverse-decay and dimuon channels are unchanged.",
            "The literal scalar mode-summed fixed-omega B.2 prescription is retained to isolate the Compton-kernel change.",
            "No empirical source, opacity, coupling, or luminosity rescaling is applied.",
            "No production axial-vector curve, manuscript, or referee-response file is modified.",
        ],
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": {
            "audit_script": sha256(Path(__file__)),
            "reference_script": sha256(HERE / "reference.py"),
            "moving_muon_kernel": sha256(FINITE_MIXING / "moving_muon_compton.py"),
            "profile": sha256(profile_path),
            "fig7_reference": sha256(fig7_path),
            "archived_B16_baseline": sha256(baseline_path),
        },
    }

    # Remove the private in-memory source/column arrays from the JSON payload.
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "mass_MeV": mass,
        "profile_sha256": output["profile"]["sha256"],
        "B16_baseline_reproduction_residual": b16_reproduction_residual,
        "active_radial_nodes": len(active_indices),
        "exact_kernel_evaluations": computed_points,
        "variants": {
            name: result["metrics_vs_fig7"]
            for name, result in variant_results.items()
        },
        "wall_time_seconds": output["configuration"]["wall_time_seconds"],
    }, indent=2), flush=True)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=MASS_MEV)
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--na", type=int, default=16)
    parser.add_argument("--ns", type=int, default=32)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    parser.add_argument("--kernel-orders", default="12,8,8,8")
    parser.add_argument("--refined-orders", default="16,10,10,10")
    parser.add_argument("--active-threshold", type=float, default=1.0e-8)
    args = parser.parse_args()
    base_orders = tuple(int(x) for x in args.kernel_orders.split(","))
    refined_orders = tuple(int(x) for x in args.refined_orders.split(","))
    if len(base_orders) != 4 or len(refined_orders) != 4:
        raise ValueError("Kernel orders must contain four comma-separated integers")
    run(
        args.profile, args.fig7, args.baseline, args.output,
        args.mass, args.nr, args.ne, args.na, args.ns,
        args.radius, args.energy_offset, base_orders, refined_orders,
        args.active_threshold,
    )


if __name__ == "__main__":
    main()
