#!/usr/bin/env python3
"""Exploratory smooth daughter-neutrino reprocessing extension of the 10 MeV B.2 band.

This is not the literal Blinov baseline. It keeps the B.1 source and scalar B.2
opacity inside 25 km, then multiplies the vacuum-limit V->nu nu opacity outside
25 km by (1-P_pair^E), where P_pair^E is a transport-only daughter-energy
survival proxy built from the public SFHo-18.8 density figure.

Run from blinov_reproduction:
python audit_b16_smooth_daughter_reprocessing_b2.py
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S, radial_rule,
        load_profile, local_rates, scalar_optical_depths,
    )
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_rmax_boundary_sensitivity import truncated_sphere_columns
except ImportError:
    from reference import (
        DEFAULT_PROFILE, KM_TO_MEV_INV, MEV2_TO_ERG_S, radial_rule,
        load_profile, local_rates, scalar_optical_depths,
    )
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_rmax_boundary_sensitivity import truncated_sphere_columns

HERE = Path(__file__).resolve().parent
DEFAULT_P1C = HERE / "outputs" / "b16_p1c_global_polarization_b14_split_10mev_2026-11-10.json"
DEFAULT_P1D = HERE / "outputs" / "b16_rmax_boundary_sensitivity_10mev_2026-11-10.json"
DEFAULT_PHASE = HERE / "outputs" / "b16_escape_phase_space_10mev_2026-11-10_v8_crosscheck.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_smooth_daughter_reprocessing_b2_10mev_2026-11-10.json"

MASS = 10.0
COUPLING = 4.171689650228597e-8
RMAX_BASE = 25.0
RUN_CASES = {
    "low": (("equal", 30.0),),
    "central": (("equal", 27.5), ("equal", 30.0), ("L", 30.0), ("T", 30.0)),
    "high": (("equal", 30.0), ("L", 30.0), ("T", 30.0)),
}
TAILS = {
    "low": {"nB20_over_n0": 0.5e-3, "H_km": 0.9},
    "central": {"nB20_over_n0": 1.0e-3, "H_km": 1.2},
    "high": {"nB20_over_n0": 2.0e-3, "H_km": 1.3},
}


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pair_escape_table(
    energies: np.ndarray,
    radii: np.ndarray,
    tail: dict,
    weighting: str,
    daughter_order: int = 256,
) -> np.ndarray:
    """Energy-weighted pair survival under radial nu-N scattering optical depth."""
    z, zw = leggauss(daughter_order)
    weights = {
        "L": 0.75 * (1.0 - z**2),
        "plus": 0.375 * (1.0 + z)**2,
        "minus": 0.375 * (1.0 - z)**2,
    }
    beta = np.sqrt(1.0 - (MASS / energies) ** 2)
    result = np.empty((len(energies), len(radii)))
    for ie, omega in enumerate(energies):
        e1 = omega * (1.0 + beta[ie] * z) / 2.0
        e2 = omega * (1.0 - beta[ie] * z) / 2.0
        for ir, radius in enumerate(radii):
            tau100 = (
                tail["nB20_over_n0"] * tail["H_km"] * 1.0e5 / 25.0
                * np.exp(-(radius - 20.0) / tail["H_km"])
            )
            tau1 = tau100 * (e1 / 100.0) ** 2
            tau2 = tau100 * (e2 / 100.0) ** 2
            mode_escape = {}
            for mode, wmode in weights.items():
                norm = np.dot(zw, wmode)
                escaped = np.dot(
                    zw, wmode * (e1 * np.exp(-tau1) + e2 * np.exp(-tau2))
                ) / omega
                mode_escape[mode] = escaped / norm
            if weighting == "L":
                result[ie, ir] = mode_escape["L"]
            elif weighting == "T":
                result[ie, ir] = 0.5 * (mode_escape["plus"] + mode_escape["minus"])
            elif weighting == "equal":
                result[ie, ir] = (
                    mode_escape["L"] + mode_escape["plus"] + mode_escape["minus"]
                ) / 3.0
            else:
                raise ValueError(f"Unknown polarization weighting {weighting}")
    return result


def smooth_extra_columns(
    source_radii: np.ndarray,
    energies: np.ndarray,
    pair_table: np.ndarray,
    pair_radii: np.ndarray,
    radius_km: float,
    angular_order: int = 32,
    path_order: int = 64,
) -> tuple[np.ndarray, np.ndarray]:
    """Extra outer-shell opacity Gamma_vac*(1-P_pair^E) along each vector ray."""
    angles, angle_weights = leggauss(angular_order)
    angle_weights = angle_weights / 2.0
    path_x, path_w = leggauss(path_order)
    velocity = np.sqrt(1.0 - (MASS / energies) ** 2)
    vacuum_nu = MASS**2 / (4.0 * np.pi * energies)
    columns = np.zeros((len(source_radii), len(angles), len(energies)))

    for ir, r0 in enumerate(source_radii):
        for ia, cosine in enumerate(angles):
            impact = r0 * np.sqrt(max(0.0, 1.0 - cosine**2))
            z25 = np.sqrt(max(0.0, RMAX_BASE**2 - impact**2))
            zR = np.sqrt(max(0.0, radius_km**2 - impact**2))
            if zR <= z25:
                continue
            midpoint = 0.5 * (z25 + zR)
            half_width = 0.5 * (zR - z25)
            z = midpoint + half_width * path_x
            rho = np.sqrt(impact**2 + z**2)
            for ie in range(len(energies)):
                p_pair = np.interp(rho, pair_radii, pair_table[ie])
                reprocessing = 1.0 - p_pair
                integral = half_width * np.dot(
                    path_w, vacuum_nu[ie] * reprocessing
                )
                columns[ir, ia, ie] = (
                    integral * KM_TO_MEV_INV / velocity[ie]
                )
    return columns, angle_weights


def luminosity(
    source: np.ndarray,
    columns: np.ndarray,
    coupling: float,
    angle_weights: np.ndarray,
) -> float:
    escape_average = np.einsum(
        "rae,a->re", np.exp(-coupling**2 * columns), angle_weights
    )
    return coupling**2 * float(np.sum(source * escape_average))


def run(
    profile_path: Path = DEFAULT_PROFILE,
    p1c_path: Path = DEFAULT_P1C,
    p1d_path: Path = DEFAULT_P1D,
    phase_path: Path = DEFAULT_PHASE,
    mass: float = MASS,
    coupling: float = COUPLING,
    source_order: int = 200,
    opacity_order: int = 640,
    energy_order: int = 200,
    angular_order: int = 32,
    path_order: int = 64,
    daughter_order: int = 256,
) -> dict:
    p1c = json.loads(p1c_path.read_text(encoding="utf-8"))
    p1d = json.loads(p1d_path.read_text(encoding="utf-8"))
    phase = json.loads(phase_path.read_text(encoding="utf-8"))["result"]

    source_r, source_rw = radial_rule(RMAX_BASE, source_order)
    opacity_r, _ = radial_rule(RMAX_BASE, opacity_order)
    opacity_grid = np.unique(np.r_[0.0, opacity_r, RMAX_BASE])
    source_profile = load_profile(profile_path, source_r)
    opacity_profile = load_profile(profile_path, opacity_grid)

    energies = mass + np.geomspace(
        max(mass * 1.0e-6, 1.0e-6), 1000.0, energy_order
    )
    energies = np.unique(np.r_[energies, mass / opacity_profile["lapse"]])
    energies = energies[energies > mass * (1.0 + 1.0e-10)]
    energies.sort()
    band_mask = (energies >= 210.0) & (energies <= 510.0)
    band_energies = energies[band_mask]
    if len(band_energies) != 10:
        raise ArithmeticError(f"Expected ten band nodes, got {len(band_energies)}")

    source_rates = local_rates(
        mass, energies[None, :], source_profile["T"][:, None],
        source_profile["mu_numu"][:, None], source_profile["mu_mu"][:, None],
    )
    source_full, _ = eq_b1_source_measure(
        source_r, source_rw, energies, source_profile["lapse"], mass,
        source_rates["production"],
    )
    source = source_full[:, band_mask]

    opacity_rates = local_rates(
        mass, band_energies[None, :], opacity_profile["T"][:, None],
        opacity_profile["mu_numu"][:, None], opacity_profile["mu_mu"][:, None],
    )
    reduced = opacity_rates["reduced_absorption"]

    base_columns, angle_weights = scalar_optical_depths(
        source_r, opacity_grid, reduced, mass, band_energies,
        RMAX_BASE, angular_order, path_order,
    )
    thin_band = coupling**2 * float(np.sum(source))
    baseline_band = luminosity(source, base_columns, coupling, angle_weights)

    # Sharp full-vacuum Rmax=30 km is used only as a closure check against P1-D.
    sharp_columns, sharp_weights = truncated_sphere_columns(
        source_r, opacity_grid, reduced, mass, band_energies,
        30.0, angular_order, path_order,
    )
    sharp30_band = luminosity(source, sharp_columns, coupling, sharp_weights)

    pair_radii = np.linspace(25.0, 30.0, 101)
    smooth_results = {}
    for tail_name, tail in TAILS.items():
        smooth_results[tail_name] = {}
        for weighting, radius in RUN_CASES[tail_name]:
            pair_table = pair_escape_table(
                band_energies, pair_radii, tail, weighting, daughter_order
            )
            extra, extra_weights = smooth_extra_columns(
                source_r, band_energies, pair_table, pair_radii, radius,
                angular_order, path_order,
            )
            # The base and outer angular quadratures are identical.
            if not np.allclose(extra_weights, angle_weights, rtol=0.0, atol=1e-15):
                raise ArithmeticError("Angular weights do not match the B.2 baseline")
            smooth_columns = base_columns + extra
            band_lum = luminosity(source, smooth_columns, coupling, angle_weights)
            full_proxy = (
                phase["calculated_luminosity_erg_s"]
                - baseline_band + band_lum
            )
            smooth_results[tail_name][f"{weighting}_Rmax_{radius:g}_km"] = {
                "band_luminosity_erg_s": band_lum,
                "relative_band_change_vs_Rmax25": band_lum / baseline_band - 1.0,
                "band_only_total_proxy_erg_s": full_proxy,
                "proxy_residual_vs_Fig7": (
                    full_proxy / phase["reference_luminosity_erg_s"] - 1.0
                ),
            }

    source_total = float(np.sum(source))
    source_outside_15 = float(
        np.sum(source[source_r > 15.0]) / source_total
    )
    expected_thin = float(p1c["source_closure"]["thin_band_luminosity_erg_s"])
    expected_base = float(p1d["baseline_closure"]["Rmax25_path64_luminosity_erg_s"])
    expected_sharp = float(
        next(x for x in p1d["boundary_scan"] if x["Rmax_km"] == 30.0)
        ["luminosity_path64_erg_s"]
    )
    closures = {
        "B1_source_relative_to_P1C": thin_band / expected_thin - 1.0,
        "Rmax25_band_relative_to_P1D_path64": baseline_band / expected_base - 1.0,
        "sharp_Rmax30_band_relative_to_P1D_path64": sharp30_band / expected_sharp - 1.0,
        "source_fraction_outside_15km": source_outside_15,
    }
    if abs(closures["B1_source_relative_to_P1C"]) > 1e-8:
        raise ArithmeticError("B.1 band source does not close to P1-C")
    if abs(closures["Rmax25_band_relative_to_P1D_path64"]) > 1e-8:
        raise ArithmeticError("Literal B.2 band does not close to P1-D")
    if abs(closures["sharp_Rmax30_band_relative_to_P1D_path64"]) > 1e-8:
        raise ArithmeticError("Sharp Rmax=30 band does not close to P1-D")

    return {
        "title": "Smooth daughter-neutrino reprocessing extension of the 10 MeV B.2 high-energy band",
        "date": "2026-11-10",
        "benchmark": {
            "mass_MeV": mass,
            "coupling": coupling,
            "energy_band_MeV": [210.0, 510.0],
            "energy_nodes_MeV": band_energies.tolist(),
            "profile_sha256": sha256(profile_path),
        },
        "configuration": {
            "source_radial_nodes": len(source_r),
            "opacity_radial_nodes": len(opacity_grid),
            "full_energy_nodes": len(energies),
            "band_energy_nodes": len(band_energies),
            "angular_order": angular_order,
            "path_order": path_order,
            "daughter_angle_order": daughter_order,
            "source_frozen_at_Rmax_km": RMAX_BASE,
            "outer_compton_opacity": 0.0,
            "outer_reduced_neutrino_opacity": (
                "mV^2/(4*pi*omega) * [1-P_pair^E(omega,r)]"
            ),
        },
        "closures": closures,
        "baseline": {
            "thin_band_luminosity_erg_s": thin_band,
            "Rmax25_band_luminosity_erg_s": baseline_band,
            "full_V8_phase_space_luminosity_erg_s": phase["calculated_luminosity_erg_s"],
            "Fig7_reference_luminosity_erg_s": phase["reference_luminosity_erg_s"],
            "full_baseline_residual_vs_Fig7": phase["relative_difference_vs_fig7"],
        },
        "sharp_Rmax30_conditional": {
            "band_luminosity_erg_s": sharp30_band,
            "relative_band_change_vs_Rmax25": sharp30_band / baseline_band - 1.0,
            "band_only_total_proxy_erg_s": (
                phase["calculated_luminosity_erg_s"] - baseline_band + sharp30_band
            ),
            "proxy_residual_vs_Fig7": (
                (phase["calculated_luminosity_erg_s"] - baseline_band + sharp30_band)
                / phase["reference_luminosity_erg_s"] - 1.0
            ),
            "note": "Full vacuum-limit opacity over 25--30 km; extreme sharp-boundary diagnostic only.",
        },
        "smooth_results": smooth_results,
        "limitations": [
            "The daughter survival probability is built from a figure-level radial nu-N transport optical depth, not the heavy-flavor energy sphere.",
            "The model treats a daughter scattering as reprocessing its energy and omits energy-changing pair kernels, recoil, correlations, degeneracy, weak magnetism, and angular neutrino transport.",
            "The 20--25 km density tail is extrapolated from the Caputo et al. Fig. 1 read-off; low/central/high tail parameters are stresses, not statistical confidence intervals.",
            "Equal, longitudinal-only, and transverse-only polarization weights are diagnostics; the actual production polarization density matrix is channel- and phase-space-dependent.",
            "The full total-luminosity comparison is a band-only proxy: all other energy bins are held at the V8 phase-space baseline.",
            "The V8 phase-space total is a cross-runtime result with non-bitwise NumPy grid hashes; B.1, Rmax=25, and sharp Rmax=30 band closures to P1-C/P1-D are checked explicitly.",
            "No baseline Rmax, source, opacity normalization, Fig. 7 curve, or axial-vector result is changed.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--p1c", type=Path, default=DEFAULT_P1C)
    parser.add_argument("--p1d", type=Path, default=DEFAULT_P1D)
    parser.add_argument("--phase", type=Path, default=DEFAULT_PHASE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.profile, args.p1c, args.p1d, args.phase)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "closures": result["closures"],
        "baseline": result["baseline"],
        "sharp_Rmax30": result["sharp_Rmax30_conditional"],
        "smooth_results": result["smooth_results"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
