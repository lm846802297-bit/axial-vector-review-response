"""Channel-resolved opacity sensitivity diagnostic for Blinov Fig. 7 at 10 MeV.

The production source is held fixed while individual inverse-process opacity
components are rescaled. These are diagnostic perturbations only, not alternative
physical predictions or fitted corrections.
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
        DEFAULT_PROFILE, MEV2_TO_ERG_S, KM_TO_MEV_INV, energy_weights,
        load_profile, local_rates, radial_rule, scalar_optical_depths,
    )
except ImportError:  # direct script execution from this directory
    from reference import (
        DEFAULT_PROFILE, MEV2_TO_ERG_S, KM_TO_MEV_INV, energy_weights,
        load_profile, local_rates, radial_rule, scalar_optical_depths,
    )

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "fig7_10mev_opacity_sensitivity.json"


def evaluate_with_opacity_scales(mass, profile_path, couplings, scales,
                                 radial_order=40, energy_order=100,
                                 angular_order=16, path_order=32,
                                 radius_km=25.0, energy_offset=1000.0):
    """Hold production fixed and scale only the named absorption components."""
    r, rw = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
    p = load_profile(profile_path, radial_grid)
    energies = mass + np.geomspace(
        max(mass * 1e-6, 1e-6), energy_offset, energy_order)
    energies = np.unique(np.r_[energies, mass / p["lapse"]])
    energies = energies[energies > mass * (1.0 + 1e-10)]
    energies.sort()

    rates = local_rates(
        mass, energies[None, :], p["T"][:, None],
        p["mu_numu"][:, None], p["mu_mu"][:, None])
    x = energies[None, :] / p["T"][:, None]
    detailed_balance_factor = (
        -np.expm1(-x) * np.exp(np.minimum(x, 700.0)))
    reduced_absorption = detailed_balance_factor * (
        scales["neutrino"] * rates["neutrino_production"]
        + scales["compton"] * rates["compton_production"]
        + scales["dimuon"] * rates["dimuon_production"]
    )

    columns, angle_weights = scalar_optical_depths(
        r, radial_grid, reduced_absorption, mass, energies,
        radius_km, angular_order, path_order)
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
    escape = lambda g: np.einsum(
        "rae,a->re", np.exp(-g**2 * columns), angle_weights)
    luminosity = np.array([
        g**2 * np.sum(source * escape(g)) for g in couplings
    ])
    return luminosity, float(np.sum(source))


def run(profile, fig7_path, radial_order=40, energy_order=100,
        angular_order=16, path_order=32):
    fig7 = json.loads(fig7_path.read_text(encoding="utf-8"))
    points = fig7["reference_vertices"]["10.0"]
    couplings = np.asarray(points["g"], dtype=float)
    reference = np.asarray(points["luminosity_erg_s"], dtype=float)
    scenarios = {
        "baseline": {"neutrino": 1.0, "compton": 1.0, "dimuon": 1.0},
        "neutrino_opacity_half": {"neutrino": 0.5, "compton": 1.0, "dimuon": 1.0},
        "neutrino_opacity_double": {"neutrino": 2.0, "compton": 1.0, "dimuon": 1.0},
        "compton_opacity_half": {"neutrino": 1.0, "compton": 0.5, "dimuon": 1.0},
        "compton_opacity_double": {"neutrino": 1.0, "compton": 2.0, "dimuon": 1.0},
        "all_opacity_half": {"neutrino": 0.5, "compton": 0.5, "dimuon": 0.5},
        "all_opacity_double": {"neutrino": 2.0, "compton": 2.0, "dimuon": 2.0},
    }
    result = {
        "purpose": "one-factor opacity sensitivity of the 10 MeV Fig. 7 curve",
        "interpretation": (
            "Production is held fixed. Only the named inverse-process opacity "
            "components are rescaled; no rescaling is asserted to be physical."
        ),
        "mass_MeV": 10.0,
        "profile_sha256": hashlib.sha256(profile.read_bytes()).hexdigest(),
        "fig7_input_sha256": hashlib.sha256(fig7_path.read_bytes()).hexdigest(),
        "fig7_pdf_sha256": fig7.get("pdf_sha256"),
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "quadrature": {
            "radial_order": radial_order, "energy_order": energy_order,
            "angular_order": angular_order, "path_order": path_order,
        },
        "scenarios": [],
    }
    for name, scales in scenarios.items():
        luminosity, thin = evaluate_with_opacity_scales(
            10.0, profile, couplings, scales,
            radial_order, energy_order, angular_order, path_order)
        relative = luminosity / reference - 1.0
        result["scenarios"].append({
            "name": name, "opacity_scales": scales,
            "thin_luminosity_erg_s": thin,
            "max_abs_relative_difference": float(np.max(np.abs(relative))),
            "mean_abs_relative_difference": float(np.mean(np.abs(relative))),
            "relative_difference_low_coupling": float(relative[0]),
            "relative_difference_peak_reference": float(relative[int(np.argmax(reference))]),
            "relative_difference_high_coupling": float(relative[-1]),
            "points": [
                {"g": float(g), "reference_erg_s": float(ref),
                 "calculated_erg_s": float(calc), "relative_difference": float(delta)}
                for g, ref, calc, delta in zip(couplings, reference, luminosity, relative)
            ],
        })
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--na", type=int, default=16)
    parser.add_argument("--ns", type=int, default=32)
    args = parser.parse_args()
    result = run(args.profile, args.fig7, args.nr, args.ne, args.na, args.ns)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([
        {k: row[k] for k in (
            "name", "opacity_scales", "thin_luminosity_erg_s",
            "max_abs_relative_difference", "mean_abs_relative_difference",
            "relative_difference_low_coupling",
            "relative_difference_peak_reference",
            "relative_difference_high_coupling",
        )}
        for row in result["scenarios"]
    ], indent=2))


if __name__ == "__main__":
    main()
