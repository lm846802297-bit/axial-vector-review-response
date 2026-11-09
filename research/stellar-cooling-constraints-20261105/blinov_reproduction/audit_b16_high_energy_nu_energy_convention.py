"""Fixed-omega versus conserved-E_infinity neutrino opacity on high-energy rays.

The fixed-omega branch follows the printed Eq. (B.2). The alternative uses
omega_local(s)=omega_source*N(source)/N(path), while deliberately retaining
the same Euclidean chord and ds. This is a redshift-only diagnostic, not full
GR ray tracing. It isolates the neutrino inverse-decay channel.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

from reference import KM_TO_MEV_INV, decay_production, load_profile, radial_rule

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_FIG7 = ROOT / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_high_energy_nu_energy_convention_10mev_2026-11-10.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def chord_tau(profile_path: Path, opacity_grid: np.ndarray, mass: float,
              coupling: float, source_radius: float, cosine: float,
              source_energy: float, path_order: int,
              redshifted: bool) -> dict:
    profile = load_profile(profile_path, opacity_grid)
    z, w = leggauss(path_order)
    smax = -cosine * source_radius + np.sqrt(
        25.0**2 - source_radius**2 + source_radius**2 * cosine**2
    )
    s = smax * (1.0 + z) / 2.0
    position = np.sqrt(np.maximum(
        source_radius**2 + s**2 + 2.0 * source_radius * s * cosine, 0.0
    ))

    temperature = np.interp(position, opacity_grid, profile["T"])
    mu_numu = np.interp(position, opacity_grid, profile["mu_numu"])
    mu_mu = np.interp(position, opacity_grid, profile["mu_mu"])
    lapse_path = np.interp(position, opacity_grid, profile["lapse"])
    lapse_source = float(np.interp(
        source_radius, opacity_grid, profile["lapse"]
    ))
    if redshifted:
        omega_local = source_energy * lapse_source / lapse_path
    else:
        omega_local = np.full_like(position, source_energy)

    velocity = np.sqrt(np.maximum(1.0 - (mass / omega_local)**2, 0.0))
    neutrino, _ = decay_production(
        mass, omega_local, temperature, mu_numu, mu_mu
    )
    x = omega_local / temperature
    absorption = np.exp(np.minimum(x, 700.0)) * neutrino
    reduced_absorption = -np.expm1(-x) * absorption
    column = (
        np.sum(smax * w / 2.0 * reduced_absorption / velocity)
        * KM_TO_MEV_INV
    )
    return {
        "tau": float(coupling**2 * column),
        "minimum_local_over_source_energy": float(np.min(omega_local / source_energy)),
        "maximum_local_over_source_energy": float(np.max(omega_local / source_energy)),
        "minimum_local_vector_speed": float(np.min(velocity)),
    }


def run(profile_path: Path, fig7_path: Path, mass: float = 10.0) -> dict:
    fig7 = json.loads(fig7_path.read_text(encoding="utf-8"))
    vertices = fig7["reference_vertices"][str(float(mass))]
    coupling = float(vertices["g"][-1])

    energies = (110.0, 210.0, 510.0)
    radii = (8.0, 10.0, 12.5)
    directions = (0.25, 0.75, 0.95)
    opacity_orders = (640, 1280)
    path_orders = (64, 128, 256)
    cases = []

    for opacity_order in opacity_orders:
        opacity_nodes, _ = radial_rule(25.0, opacity_order)
        opacity_grid = np.unique(np.r_[0.0, opacity_nodes, 25.0])
        for radius in radii:
            for cosine in directions:
                for energy in energies:
                    tau = {}
                    for path_order in path_orders:
                        tau[str(path_order)] = {
                            "fixed_omega": chord_tau(
                                profile_path, opacity_grid, mass, coupling,
                                radius, cosine, energy, path_order, False
                            ),
                            "conserved_E_infinity": chord_tau(
                                profile_path, opacity_grid, mass, coupling,
                                radius, cosine, energy, path_order, True
                            ),
                        }
                    cases.append({
                        "opacity_order": opacity_order,
                        "opacity_grid_node_count": int(len(opacity_grid)),
                        "emission_radius_km": radius,
                        "cos_theta": cosine,
                        "source_energy_MeV": energy,
                        "tau_by_path_order": tau,
                    })

    lookup = {
        (row["opacity_order"], row["emission_radius_km"],
         row["cos_theta"], row["source_energy_MeV"]): row["tau_by_path_order"]
        for row in cases
    }
    comparisons = []
    for radius in radii:
        for cosine in directions:
            for energy in energies:
                q640 = lookup[(640, radius, cosine, energy)]
                q1280 = lookup[(1280, radius, cosine, energy)]
                fixed = q640["256"]["fixed_omega"]["tau"]
                red = q640["256"]["conserved_E_infinity"]["tau"]
                comparisons.append({
                    "emission_radius_km": radius,
                    "cos_theta": cosine,
                    "source_energy_MeV": energy,
                    "tau_redshift_over_fixed": red / fixed,
                    "fixed_path64_to128": (
                        q640["128"]["fixed_omega"]["tau"]
                        / q640["64"]["fixed_omega"]["tau"] - 1.0
                    ),
                    "fixed_path128_to256": (
                        q640["256"]["fixed_omega"]["tau"]
                        / q640["128"]["fixed_omega"]["tau"] - 1.0
                    ),
                    "redshift_path64_to128": (
                        q640["128"]["conserved_E_infinity"]["tau"]
                        / q640["64"]["conserved_E_infinity"]["tau"] - 1.0
                    ),
                    "redshift_path128_to256": (
                        q640["256"]["conserved_E_infinity"]["tau"]
                        / q640["128"]["conserved_E_infinity"]["tau"] - 1.0
                    ),
                    "opacity640_to1280_fixed": (
                        q1280["256"]["fixed_omega"]["tau"] / fixed - 1.0
                    ),
                    "opacity640_to1280_redshift": (
                        q1280["256"]["conserved_E_infinity"]["tau"] / red - 1.0
                    ),
                })

    return {
        "title": "High-energy neutrino B.2 energy-convention comparison",
        "mass_MeV": mass,
        "coupling": coupling,
        "channel": "neutrino inverse decay only",
        "fixed_convention": "omega_source held fixed along the full Euclidean chord",
        "alternative_convention": "omega_local(s)=omega_source*N(source)/N(path), conserved E_infinity",
        "alternative_scope": "redshift-only sensitivity; Euclidean ds and chord geometry are unchanged",
        "energies_MeV": list(energies),
        "source_radii_km": list(radii),
        "cos_theta": list(directions),
        "opacity_orders": list(opacity_orders),
        "path_orders": list(path_orders),
        "comparisons": comparisons,
        "summary": {
            "redshift_over_fixed_tau_min": min(x["tau_redshift_over_fixed"] for x in comparisons),
            "redshift_over_fixed_tau_max": max(x["tau_redshift_over_fixed"] for x in comparisons),
            "redshift_over_fixed_tau_mean": float(np.mean([
                x["tau_redshift_over_fixed"] for x in comparisons
            ])),
            "max_fixed_path_refinement": max(
                max(abs(x["fixed_path64_to128"]), abs(x["fixed_path128_to256"]))
                for x in comparisons
            ),
            "max_redshift_path_refinement": max(
                max(abs(x["redshift_path64_to128"]), abs(x["redshift_path128_to256"]))
                for x in comparisons
            ),
            "max_opacity_grid_refinement_fixed": max(
                abs(x["opacity640_to1280_fixed"]) for x in comparisons
            ),
            "max_opacity_grid_refinement_redshift": max(
                abs(x["opacity640_to1280_redshift"]) for x in comparisons
            ),
        },
        "execution": {
            "profile_sha256": sha256(profile_path),
            "fig7_sha256": sha256(fig7_path),
            "engine": "Python/NumPy reference implementation",
        },
        "interpretation": [
            "The alternative changes only the local energy argument and local vector speed in the neutrino opacity kernel.",
            "It is not a complete GR ray trace because the spatial metric factor and curved ray trajectory are not included.",
            "The two energy conventions remain separate; the printed fixed-omega Eq. (B.2) remains the reproduction baseline.",
            "No source, profile, or axial-vector result is modified.",
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
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
