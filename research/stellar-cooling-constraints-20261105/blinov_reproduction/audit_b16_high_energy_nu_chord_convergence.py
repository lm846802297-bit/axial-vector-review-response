"""Targeted B.2 chord convergence for the high-energy neutrino opacity.

This diagnostic fixes mV=10 MeV, the Fig. 7 strong-endpoint coupling, and the
literal fixed-omega Eq. (B.2) convention. It compares path Gauss orders and
independent radial opacity-interpolation grids for representative high-energy
rays emitted in the 8--12.5 km region. Only neutrino inverse-decay opacity is
included, isolating the dominant channel identified by the channel audit.
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
    KM_TO_MEV_INV, decay_production, load_profile, radial_rule,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_high_energy_nu_chord_convergence_10mev_2026-11-10.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build_neutrino_reduced_opacity(profile_path: Path, opacity_grid: np.ndarray,
                                   energies: np.ndarray, mass: float) -> np.ndarray:
    profile = load_profile(profile_path, opacity_grid)
    neutrino, _ = decay_production(
        mass, energies[None, :], profile["T"][:, None],
        profile["mu_numu"][:, None], profile["mu_mu"][:, None]
    )
    x = energies[None, :] / profile["T"][:, None]
    detailed_balance = (
        -np.expm1(-x) * np.exp(np.minimum(x, 700.0))
    )
    return detailed_balance * neutrino


def chord_tau(opacity_grid: np.ndarray, reduced_opacity: np.ndarray,
              radius: float, cosine: float, energy: float,
              mass: float, coupling: float, path_order: int) -> float:
    z, w = leggauss(path_order)
    smax = -cosine * radius + np.sqrt(
        25.0**2 - radius**2 + radius**2 * cosine**2
    )
    s = smax * (1.0 + z) / 2.0
    position = np.sqrt(np.maximum(
        radius**2 + s**2 + 2.0 * radius * s * cosine, 0.0
    ))
    energy_index = int(np.argmin(np.abs(ENERGIES - energy)))
    rate = np.interp(position, opacity_grid, reduced_opacity[:, energy_index])
    velocity = np.sqrt(1.0 - (mass / energy)**2)
    column = (
        np.sum(smax * w / 2.0 * rate)
        * KM_TO_MEV_INV / velocity
    )
    return float(coupling**2 * column)


ENERGIES = np.array([110.0, 210.0, 510.0])


def run(profile_path: Path, fig7_path: Path, mass: float = 10.0) -> dict:
    fig7 = json.loads(fig7_path.read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
    coupling = float(vertices["g"][-1])

    source_radii = (8.0, 10.0, 12.5)
    directions = (-0.25, 0.25, 0.75, 0.95)
    opacity_orders = (320, 640, 1280)
    path_orders = (32, 64, 128, 256)
    cases = []

    for opacity_order in opacity_orders:
        opacity_nodes, _ = radial_rule(25.0, opacity_order)
        opacity_grid = np.unique(np.r_[0.0, opacity_nodes, 25.0])
        reduced = build_neutrino_reduced_opacity(
            profile_path, opacity_grid, ENERGIES, mass
        )
        for radius in source_radii:
            for cosine in directions:
                for energy in ENERGIES:
                    tau = {
                        str(order): chord_tau(
                            opacity_grid, reduced, radius, cosine,
                            float(energy), mass, coupling, order
                        )
                        for order in path_orders
                    }
                    cases.append({
                        "opacity_order": opacity_order,
                        "opacity_grid_node_count": int(len(opacity_grid)),
                        "emission_radius_km": radius,
                        "cos_theta": cosine,
                        "energy_MeV": float(energy),
                        "tau_by_path_order": tau,
                    })

    # Pair each physical ray across opacity grids and path orders.
    lookup = {
        (row["opacity_order"], row["emission_radius_km"],
         row["cos_theta"], row["energy_MeV"]): row["tau_by_path_order"]
        for row in cases
    }
    refinements = []
    for radius in source_radii:
        for cosine in directions:
            for energy in ENERGIES:
                q320 = lookup[(320, radius, cosine, float(energy))]
                q640 = lookup[(640, radius, cosine, float(energy))]
                q1280 = lookup[(1280, radius, cosine, float(energy))]
                refinements.append({
                    "emission_radius_km": radius,
                    "cos_theta": cosine,
                    "energy_MeV": float(energy),
                    "path_32_to_64_at_opacity640": q640["64"] / q640["32"] - 1.0,
                    "path_64_to_128_at_opacity640": q640["128"] / q640["64"] - 1.0,
                    "path_128_to_256_at_opacity640": q640["256"] / q640["128"] - 1.0,
                    "opacity_320_to_640_at_path256": q640["256"] / q320["256"] - 1.0,
                    "opacity_640_to_1280_at_path256": q1280["256"] / q640["256"] - 1.0,
                })
    keys = (
        "path_32_to_64_at_opacity640",
        "path_64_to_128_at_opacity640",
        "path_128_to_256_at_opacity640",
        "opacity_320_to_640_at_path256",
        "opacity_640_to_1280_at_path256",
    )
    maxima = {
        key: max(abs(row[key]) for row in refinements)
        for key in keys
    }
    return {
        "title": "High-energy neutrino B.2 chord convergence",
        "mass_MeV": mass,
        "coupling": coupling,
        "channel": "neutrino inverse decay only",
        "energy_convention": "fixed omega along the full Eq. (B.2) chord",
        "energies_MeV": ENERGIES.tolist(),
        "source_radii_km": list(source_radii),
        "cos_theta": list(directions),
        "opacity_orders": list(opacity_orders),
        "path_orders": list(path_orders),
        "maximum_absolute_relative_refinement": maxima,
        "cases": cases,
        "refinements": refinements,
        "execution": {
            "profile_sha256": sha256(profile_path),
            "fig7_sha256": sha256(fig7_path),
            "engine": "Python/NumPy reference implementation",
        },
        "interpretation": [
            "This isolates the neutrino inverse-decay B.2 chord integral.",
            "The opacity radial grid and path quadrature are varied independently.",
            "It is a targeted local-ray convergence diagnostic, not a new global luminosity calculation.",
            "No source, profile, opacity prescription, or axial-vector result is changed.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    args = parser.parse_args()
    result = run(args.profile, args.fig7, args.mass)
    payload = {
        "result": result,
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "script_sha256": sha256(Path(__file__)),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["maximum_absolute_relative_refinement"], indent=2))


if __name__ == "__main__":
    main()
