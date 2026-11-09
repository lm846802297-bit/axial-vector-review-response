"""Independent B.1 optically-thin source integral for the 10 MeV vector benchmark.

This script does not import or call eq_b1_source_measure, energy_weights,
radial_rule, or load_profile. It evaluates the printed B.1 source integral
using a separate composite Gauss-Legendre rule in radius and in
x=log(omega-m_V). The local production kernels are intentionally shared:
this audit isolates B.1 integration, not the collision-kernel derivation.

The escape factor is set to one. The output is therefore the optically-thin
source L_thin, resolved into neutrino inverse decay, dimuon inverse decay,
and muon-Compton production. It is not yet the full trapped luminosity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .reference import (
        DEFAULT_PROFILE,
        KM_TO_MEV_INV,
        MEV2_TO_ERG_S,
        negative_muon_density_and_degeneracy,
        decay_production,
        compton_production,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE,
        KM_TO_MEV_INV,
        MEV2_TO_ERG_S,
        negative_muon_density_and_degeneracy,
        decay_production,
        compton_production,
    )

HERE = Path(__file__).resolve().parent
DEFAULT_BASELINE = HERE / "outputs" / "b16_global_fig7_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_b1_independent_thin_source_10mev_2026-11-09.json"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
SHELL_EDGES_KM = np.array([0., 5., 8., 10., 12., 15., 18., 20., 22., 25.])


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_profile_direct(path: Path) -> dict[str, np.ndarray]:
    """Read and interpolate the public-profile table without reference helpers."""
    table = np.genfromtxt(path, delimiter=",", names=True)
    required = ("r_km", "T_MeV", "mu_mu_MeV", "mu_numu_MeV", "lapse")
    if table.dtype.names is None or any(x not in table.dtype.names for x in required):
        raise ValueError(f"Profile must contain columns {required}")
    radius = np.asarray(table["r_km"], float)
    if np.any(np.diff(radius) < 0.0):
        raise ValueError("Profile radii must be sorted")
    return {
        "radius_table": radius,
        "T_table": np.asarray(table["T_MeV"], float),
        "mu_mu_table": np.asarray(table["mu_mu_MeV"], float),
        "mu_numu_table": np.asarray(table["mu_numu_MeV"], float),
        "lapse_table": np.asarray(table["lapse"], float),
    }


def interpolate_profile(table: dict[str, np.ndarray], radii: np.ndarray) -> dict[str, np.ndarray]:
    r = np.asarray(radii, float)
    return {
        "T": np.interp(r, table["radius_table"], table["T_table"]),
        "mu_mu": np.interp(r, table["radius_table"], table["mu_mu_table"]),
        "mu_numu": np.interp(r, table["radius_table"], table["mu_numu_table"]),
        "lapse": np.interp(r, table["radius_table"], table["lapse_table"]),
    }


def composite_gauss(edges: np.ndarray, order: int) -> tuple[np.ndarray, np.ndarray]:
    """Composite Gauss-Legendre nodes and weights on an arbitrary partition."""
    edges = np.asarray(edges, float)
    if edges.ndim != 1 or len(edges) < 2 or np.any(np.diff(edges) <= 0.0):
        raise ValueError("Integration edges must be strictly increasing")
    if order < 1:
        raise ValueError("Gauss order must be positive")
    x, w = leggauss(int(order))
    left, right = edges[:-1, None], edges[1:, None]
    nodes = (left + right) / 2.0 + (right - left) * x[None, :] / 2.0
    weights = (right - left) * w[None, :] / 2.0
    return nodes.ravel(), weights.ravel()


def log_energy_rule(
    mass_mev: float,
    lower_energy_mev: float,
    energy_offset_mev: float,
    panels: int,
    order: int,
    scale_mev: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Return omega nodes and d-omega weights using x=log((omega-m)/scale).

    The exact radius-dependent lower limit is inserted before quadrature.
    energy_offset_mev denotes omega_max - m_V.
    """
    delta_min = float(lower_energy_mev) - float(mass_mev)
    if delta_min <= 0.0:
        raise ValueError("B.1 escape threshold must exceed the vector rest mass")
    if energy_offset_mev <= delta_min:
        raise ValueError("Energy upper limit must exceed the local lower limit")
    if panels < 1 or order < 1 or scale_mev <= 0.0:
        raise ValueError("Invalid logarithmic energy quadrature configuration")

    x_min = np.log(delta_min / scale_mev)
    x_max = np.log(energy_offset_mev / scale_mev)
    x_edges = np.linspace(x_min, x_max, int(panels) + 1)
    x_nodes, x_weights = composite_gauss(x_edges, order)
    delta = scale_mev * np.exp(x_nodes)
    omega = mass_mev + delta
    # d omega = (omega-m) dx
    omega_weights = x_weights * delta
    return omega, omega_weights


def integrate_one_radius(
    mass_mev: float,
    temperature_mev: float,
    mu_numu_mev: float,
    mu_mu_mev: float,
    lapse: float,
    n_mu: float,
    f_deg: float,
    energy_panels: int,
    energy_order: int,
    energy_offset_mev: float,
) -> dict[str, float]:
    """Direct energy quadrature of each production channel at one radius."""
    omega_min = mass_mev / lapse
    omega, d_omega = log_energy_rule(
        mass_mev, omega_min, energy_offset_mev, energy_panels, energy_order
    )
    momentum = np.sqrt(np.maximum(omega * omega - mass_mev * mass_mev, 0.0))
    spectral_density = momentum * omega**2 / (2.0 * np.pi**2)

    # The production kernels are evaluated at the new quadrature nodes;
    # no old energy-grid interpolation or energy_weights are used.
    nu_rate, dimuon_rate = decay_production(
        mass_mev, omega, temperature_mev, mu_numu_mev, mu_mu_mev
    )
    compton_rate = compton_production(
        mass_mev, omega, temperature_mev, n_mu, f_deg
    )
    common = d_omega * spectral_density
    return {
        "neutrino": float(np.dot(common, nu_rate)),
        "dimuon": float(np.dot(common, dimuon_rate)),
        "compton": float(np.dot(common, compton_rate)),
    }


def radial_state_from_edges(
    table: dict[str, np.ndarray],
    edges: np.ndarray,
    radial_order: int,
) -> dict[str, np.ndarray]:
    """Build a radial quadrature state on an explicitly supplied partition."""
    radii, weights_km = composite_gauss(np.asarray(edges, float), radial_order)
    profile = interpolate_profile(table, radii)
    n_mu, f_deg = negative_muon_density_and_degeneracy(
        profile["T"], profile["mu_mu"]
    )
    radial_prefactor = (
        4.0 * np.pi * (radii * KM_TO_MEV_INV) ** 2
        * (weights_km * KM_TO_MEV_INV)
        * profile["lapse"] ** 2
        * MEV2_TO_ERG_S
    )
    return {
        "radii_km": radii,
        "weights_km": weights_km,
        "radial_prefactor": radial_prefactor,
        "T": profile["T"],
        "mu_mu": profile["mu_mu"],
        "mu_numu": profile["mu_numu"],
        "lapse": profile["lapse"],
        "n_mu": np.asarray(n_mu, float),
        "F_deg": np.asarray(f_deg, float),
    }


def radial_state(
    table: dict[str, np.ndarray],
    radius_km: float,
    radial_panels: int,
    radial_order: int,
) -> dict[str, np.ndarray]:
    """Independent equal-width radial quadrature, unrelated to radial_rule."""
    edges = np.linspace(0.0, radius_km, int(radial_panels) + 1)
    return radial_state_from_edges(table, edges, radial_order)


def integrate_source(
    state: dict[str, np.ndarray],
    mass_mev: float,
    energy_panels: int,
    energy_order: int,
    energy_offset_mev: float,
) -> dict:
    """Integrate B.1 with O=1, retaining channel and radial contributions."""
    names = ("neutrino", "dimuon", "compton")
    radial_contributions = {name: np.zeros(len(state["radii_km"])) for name in names}
    for i in range(len(state["radii_km"])):
        spectral = integrate_one_radius(
            mass_mev,
            float(state["T"][i]),
            float(state["mu_numu"][i]),
            float(state["mu_mu"][i]),
            float(state["lapse"][i]),
            float(state["n_mu"][i]),
            float(state["F_deg"][i]),
            energy_panels,
            energy_order,
            energy_offset_mev,
        )
        for name in names:
            radial_contributions[name][i] = (
                state["radial_prefactor"][i] * spectral[name]
            )

    totals = {name: float(np.sum(radial_contributions[name])) for name in names}
    total = float(sum(totals.values()))
    fractions = {
        name: (value / total if total > 0.0 else 0.0)
        for name, value in totals.items()
    }
    shell_contributions = {}
    r = state["radii_km"]
    shell_index = np.digitize(r, SHELL_EDGES_KM[1:-1], right=False)
    for j, (lo, hi) in enumerate(zip(SHELL_EDGES_KM[:-1], SHELL_EDGES_KM[1:])):
        key = f"{lo:g}-{hi:g} km"
        shell_contributions[key] = {
            name: float(np.sum(radial_contributions[name][shell_index == j]))
            for name in names
        }
        shell_contributions[key]["total"] = sum(shell_contributions[key].values())
    return {
        "total_erg_s_per_g2": total,
        "channels_erg_s_per_g2": totals,
        "channel_fractions": fractions,
        "radial_contributions_erg_s_per_g2": {
            name: radial_contributions[name].tolist() for name in names
        },
        "shell_contributions_erg_s_per_g2": shell_contributions,
        "number_of_radial_nodes": int(len(r)),
        "number_of_energy_nodes_per_radius": int(energy_panels * energy_order),
        "energy_panels": int(energy_panels),
        "energy_gauss_order": int(energy_order),
        "energy_upper_MeV": float(mass_mev + energy_offset_mev),
    }


def relative_difference(a: float, b: float):
    if b == 0.0:
        return 0.0 if a == 0.0 else None
    return float(a / b - 1.0)


def convergence_entry(label: str, result: dict, reference: dict) -> dict:
    channels = {}
    for name, value in result["channels_erg_s_per_g2"].items():
        channels[name] = {
            "value_erg_s_per_g2": value,
            "relative_difference_vs_reference": relative_difference(
                value, reference["channels_erg_s_per_g2"][name]
            ),
        }
    return {
        "label": label,
        "total_erg_s_per_g2": result["total_erg_s_per_g2"],
        "relative_difference_vs_reference": relative_difference(
            result["total_erg_s_per_g2"], reference["total_erg_s_per_g2"]
        ),
        "channels": channels,
    }


def run(
    profile_path: Path = DEFAULT_PROFILE,
    baseline_path: Path = DEFAULT_BASELINE,
    output_path: Path = DEFAULT_OUTPUT,
    mass_mev: float = 10.0,
    radius_km: float = 25.0,
    radial_order: int = 4,
    energy_order: int = 4,
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
    baseline_channels = {
        name: float(value["thin_source_erg_s_per_g2"])
        for name, value in baseline_result["source_channel_fractions"].items()
    }
    baseline_total = float(sum(baseline_channels.values()))
    baseline_reference = {
        "total_erg_s_per_g2": baseline_total,
        "channels_erg_s_per_g2": baseline_channels,
    }

    # A. Radial convergence, with an independent 1 km base partition.
    radial_results = []
    for panels in (25, 50, 100):
        state = radial_state(table, radius_km, panels, radial_order)
        result = integrate_source(
            state, mass_mev, energy_panels=160, energy_order=energy_order,
            energy_offset_mev=1000.0
        )
        radial_results.append({
            "radial_panels_1km_base": panels,
            "radial_order_per_panel": radial_order,
            "result": result,
        })

    # B. Energy convergence, at a fixed 0.5 km radial partition.
    energy_state = radial_state(table, radius_km, 50, radial_order)
    energy_results = []
    for panels in (80, 120, 180, 240):
        result = integrate_source(
            energy_state, mass_mev, panels, energy_order, 1000.0
        )
        energy_results.append({"energy_panels": panels, "result": result})

    # C. High-energy-tail convergence, independent of the baseline cutoff.
    tail_results = []
    for offset in (500.0, 1000.0, 2000.0, 4000.0):
        result = integrate_source(
            energy_state, mass_mev, 240, energy_order, offset
        )
        tail_results.append({"energy_offset_MeV": offset, "result": result})

    # D. Final high-resolution independent B.1 source integral.
    final_state = radial_state(table, radius_km, 100, radial_order)
    final = integrate_source(
        final_state, mass_mev, 240, energy_order, 2000.0
    )

    # E. Match the archived 40-node radial rule exactly, but replace its
    # energy-grid/energy_weights integration with the independent direct
    # log-energy Gauss integral. This separates radial-rule and energy-rule
    # contributions to any B.1 source residual.
    archived_radial_edges = np.array(
        [0., 5., 8., 10., 12., 15., 18., 20., 22., 24., radius_km]
    )
    archived_radial_state = radial_state_from_edges(
        table, archived_radial_edges, radial_order=4
    )
    same_radial_direct_energy = integrate_source(
        archived_radial_state, mass_mev, 240, energy_order, 2000.0
    )
    same_radial_comparison = {
        name: {
            "direct_energy_integral_erg_s_per_g2": same_radial_direct_energy["channels_erg_s_per_g2"][name],
            "archived_erg_s_per_g2": baseline_channels[name],
            "relative_difference": relative_difference(
                same_radial_direct_energy["channels_erg_s_per_g2"][name],
                baseline_channels[name],
            ),
        }
        for name in ("neutrino", "dimuon", "compton")
    }
    same_radial_comparison["total"] = {
        "direct_energy_integral_erg_s_per_g2": same_radial_direct_energy["total_erg_s_per_g2"],
        "archived_erg_s_per_g2": baseline_total,
        "relative_difference": relative_difference(
            same_radial_direct_energy["total_erg_s_per_g2"], baseline_total
        ),
    }

    radial_reference = radial_results[-1]["result"]
    energy_reference = energy_results[-1]["result"]
    tail_reference = tail_results[-1]["result"]
    radial_summary = [
        {
            "radial_panels": item["radial_panels_1km_base"],
            "number_of_radial_nodes": item["result"]["number_of_radial_nodes"],
            "total_erg_s_per_g2": item["result"]["total_erg_s_per_g2"],
            "relative_difference_vs_100_panel_result": relative_difference(
                item["result"]["total_erg_s_per_g2"],
                radial_reference["total_erg_s_per_g2"],
            ),
            "channel_fractions": item["result"]["channel_fractions"],
        }
        for item in radial_results
    ]
    energy_summary = [
        {
            "energy_panels": item["energy_panels"],
            "number_of_energy_nodes_per_radius": item["result"]["number_of_energy_nodes_per_radius"],
            "total_erg_s_per_g2": item["result"]["total_erg_s_per_g2"],
            "relative_difference_vs_240_panel_result": relative_difference(
                item["result"]["total_erg_s_per_g2"],
                energy_reference["total_erg_s_per_g2"],
            ),
            "channel_fractions": item["result"]["channel_fractions"],
        }
        for item in energy_results
    ]
    tail_summary = [
        {
            "energy_offset_MeV": item["energy_offset_MeV"],
            "energy_upper_MeV": item["result"]["energy_upper_MeV"],
            "total_erg_s_per_g2": item["result"]["total_erg_s_per_g2"],
            "relative_difference_vs_4000MeV_offset": relative_difference(
                item["result"]["total_erg_s_per_g2"],
                tail_reference["total_erg_s_per_g2"],
            ),
            "channel_fractions": item["result"]["channel_fractions"],
        }
        for item in tail_results
    ]

    final_channels = final["channels_erg_s_per_g2"]
    final_comparison = {
        name: {
            "independent_erg_s_per_g2": final_channels[name],
            "archived_erg_s_per_g2": baseline_channels[name],
            "relative_difference": relative_difference(
                final_channels[name], baseline_channels[name]
            ),
        }
        for name in ("neutrino", "dimuon", "compton")
    }
    final_comparison["total"] = {
        "independent_erg_s_per_g2": final["total_erg_s_per_g2"],
        "archived_erg_s_per_g2": baseline_total,
        "relative_difference": relative_difference(
            final["total_erg_s_per_g2"], baseline_total
        ),
    }

    payload = {
        "source": "Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B, Eq. (B.1)",
        "scope": "Optically-thin B.1 source integral with O(r,omega)=1; not the full trapped luminosity.",
        "method": (
            "Independent composite Gauss-Legendre radial integration on equal-width "
            "1 km base panels; independent composite Gauss-Legendre energy integration "
            "in x=log(omega-mV), with the exact radius-dependent lower limit mV/N(r) "
            "inserted for every radial node. Production kernels are evaluated directly "
            "at the new energy quadrature nodes."
        ),
        "deliberately_not_used": [
            "eq_b1_source_measure",
            "energy_weights",
            "radial_rule",
            "load_profile",
            "any B.2 path-integration routine",
        ],
        "shared_physics": [
            "The same archived SFHo-18.8 reconstructed profile is used.",
            "The local neutrino inverse-decay and muon-Compton production kernels are shared with the Appendix-B reference implementation.",
            "The single negative-muon density convention printed in Eq. (B.17) is retained.",
        ],
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": sha256(Path(__file__)),
        "profile": {
            "path": Path(profile_path).name,
            "sha256": profile_sha,
            "number_of_profile_rows": int(len(table["radius_table"])),
        },
        "baseline_reference_sha256": sha256(baseline_path),
        "configuration": {
            "mass_MeV": float(mass_mev),
            "radius_km": float(radius_km),
            "radial_order_per_panel": int(radial_order),
            "energy_gauss_order": int(energy_order),
            "radial_convergence_panels": [25, 50, 100],
            "energy_convergence_panels": [80, 120, 180, 240],
            "energy_tail_offsets_MeV": [500.0, 1000.0, 2000.0, 4000.0],
            "final_radial_panels": 100,
            "final_energy_panels": 240,
            "final_energy_offset_MeV": 2000.0,
        },
        "archived_b16_b1_source": {
            "channels_erg_s_per_g2": baseline_channels,
            "total_erg_s_per_g2": baseline_total,
            "channel_fractions": {
                name: value / baseline_total for name, value in baseline_channels.items()
            },
        },
        "radial_convergence": radial_summary,
        "energy_convergence": energy_summary,
        "high_energy_tail_convergence": tail_summary,
        "same_radial_grid_independent_energy_check": {
            "purpose": "Reproduce the archived 40-node radial quadrature nodes and weights, while replacing the archived energy grid/energy_weights with direct log-energy Gauss integration.",
            "number_of_radial_nodes": int(len(archived_radial_state["radii_km"])),
            "result": same_radial_direct_energy,
            "comparison_with_archived": same_radial_comparison,
        },
        "final_independent_b1_source": final,
        "comparison_with_archived_b16_b1": final_comparison,
        "closure": {
            "sum_of_channels_relative_difference": relative_difference(
                sum(final_channels.values()), final["total_erg_s_per_g2"]
            ),
            "dimuon_channel_expected_closed_for_10MeV": bool(mass_mev < 2.0 * 105.6583755),
            "dimuon_channel_value": final_channels["dimuon"],
        },
        "elapsed_seconds": float(time.time() - started),
        "limitations": [
            "The escape factor is set to one; this validates the B.1 optically-thin source, not the full B.1+B.2 luminosity.",
            "The profile is reconstructed from public figures and is not the original Garching simulation table.",
            "The local production kernels are shared and are not independently re-derived in this audit.",
            "The single negative-muon density convention is retained; this audit does not revisit the physical species-counting convention.",
            "The source-energy variable follows the literal Appendix-B lower limit and N(r)^2 prefactor; this audit does not resolve the main-text versus Appendix-B energy-language issue.",
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
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--radius", type=float, default=25.0)
    parser.add_argument("--radial-order", type=int, default=4)
    parser.add_argument("--energy-order", type=int, default=4)
    args = parser.parse_args()
    result = run(
        args.profile, args.baseline, args.output, args.mass, args.radius,
        args.radial_order, args.energy_order
    )
    print(json.dumps({
        "output": str(args.output),
        "profile": result["profile"],
        "archived_source": result["archived_b16_b1_source"],
        "radial_convergence": result["radial_convergence"],
        "energy_convergence": result["energy_convergence"],
        "high_energy_tail_convergence": result["high_energy_tail_convergence"],
        "final_independent_source": {
            "total_erg_s_per_g2": result["final_independent_b1_source"]["total_erg_s_per_g2"],
            "channels_erg_s_per_g2": result["final_independent_b1_source"]["channels_erg_s_per_g2"],
            "channel_fractions": result["final_independent_b1_source"]["channel_fractions"],
        },
        "comparison_with_archived": result["comparison_with_archived_b16_b1"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
