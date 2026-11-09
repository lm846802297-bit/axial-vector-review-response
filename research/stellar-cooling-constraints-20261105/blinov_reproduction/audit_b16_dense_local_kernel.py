"""Dense local B.6--B.10 and B.14--B.19 audit on the full B.1+B.2 grid.

This audit evaluates 200 source radii and the 320 exact-threshold energy
quadrature nodes at each radius (64,000 r-omega points), matching the
end-to-end independent B.1+B.2 calculation. Neutrino production and
absorption are independently reconstructed from direct two-body angular
phase-space quadrature. The B.17 muon susceptibility is independently
recomputed with the transformed momentum integral, and B.14--B.19 are
evaluated directly.

The reference local kernels are compared against these independent
expressions point by point. No global source, opacity, path, luminosity,
or production axial-vector output is modified.
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
from scipy.special import expit

try:
    from .reference import (
        DEFAULT_PROFILE,
        ALPHA,
        M_MU,
        KM_TO_MEV_INV,
        negative_muon_density_and_degeneracy,
        local_rates,
        fermi_pair_average,
    )
    from .audit_b16_b1_independent import (
        read_profile_direct,
        interpolate_profile,
        composite_gauss,
        log_energy_rule,
        sha256,
    )
    from .audit_b16_local_absorption import (
        independent_muon_density_susceptibility,
    )
except ImportError:
    from reference import (
        DEFAULT_PROFILE,
        ALPHA,
        M_MU,
        KM_TO_MEV_INV,
        negative_muon_density_and_degeneracy,
        local_rates,
        fermi_pair_average,
    )
    from audit_b16_b1_independent import (
        read_profile_direct,
        interpolate_profile,
        composite_gauss,
        log_energy_rule,
        sha256,
    )
    from audit_b16_local_absorption import (
        independent_muon_density_susceptibility,
    )

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "outputs" / "b16_dense_local_kernel_audit_10mev_2026-11-09.json"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
MASS_MEV = 10.0
RADIUS_KM = 25.0
RADIAL_PANELS = 50
RADIAL_ORDER = 4
ENERGY_PANELS = 80
ENERGY_ORDER = 4
ENERGY_OFFSET_MEV = 2000.0
NEUTRINO_ANGULAR_ORDER = 512
NEUTRINO_ANGULAR_CHECK_ORDER = 256
SUSCEPTIBILITY_ORDER = 256


def rel_max(a: np.ndarray, b: np.ndarray) -> float:
    aa, bb = np.asarray(a, float), np.asarray(b, float)
    return float(np.max(np.abs(aa - bb) / np.maximum(np.abs(bb), 1.0e-300)))


def residual_summary(a: np.ndarray, b: np.ndarray) -> dict:
    aa, bb = np.asarray(a, float), np.asarray(b, float)
    residual = np.abs(aa - bb) / np.maximum(np.abs(bb), 1.0e-300)
    return {
        "maximum_relative_residual": float(np.max(residual)),
        "p99_relative_residual": float(np.quantile(residual, 0.99)),
        "rms_relative_residual": float(np.sqrt(np.mean(residual**2))),
        "number_of_points": int(residual.size),
    }


def direct_neutrino_pair_rates(
    mass_mev: float,
    omega_mev: np.ndarray,
    temperature_mev: float,
    chemical_potential_mev: float,
    order: int = NEUTRINO_ANGULAR_ORDER,
) -> tuple[np.ndarray, np.ndarray]:
    """Direct B.6 production and inverse-occupation absorption for one flavor."""
    omega = np.asarray(omega_mev, float)
    z, weights = leggauss(int(order))
    velocity = np.sqrt(np.maximum(1.0 - (mass_mev / omega) ** 2, 0.0))
    e1 = 0.5 * omega[None, :] * (1.0 + z[:, None] * velocity[None, :])
    e2 = 0.5 * omega[None, :] * (1.0 - z[:, None] * velocity[None, :])
    f1 = expit((chemical_potential_mev - e1) / temperature_mev)
    f2 = expit((-chemical_potential_mev - e2) / temperature_mev)
    production_stat = f1 * f2
    absorption_stat = (1.0 - f1) * (1.0 - f2)
    prefactor = mass_mev**2 / (16.0 * np.pi * omega)
    production = prefactor * np.einsum("z,ze->e", weights, production_stat)
    absorption = prefactor * np.einsum("z,ze->e", weights, absorption_stat)
    return production, absorption


def direct_compton_rates(
    mass_mev: float,
    omega_mev: np.ndarray,
    temperature_mev: float,
    susceptibility_mev3: float,
) -> dict[str, np.ndarray]:
    """Vectorized direct B.14--B.19 evaluation, all rates per g_X^2."""
    omega = np.asarray(omega_mev, float)
    velocity = np.sqrt(np.maximum(1.0 - (mass_mev / omega) ** 2, 0.0))
    alpha_v_per_g2 = 1.0 / (4.0 * np.pi)
    sigma = (
        8.0 * np.pi * ALPHA * alpha_v_per_g2 / (3.0 * M_MU**2)
        * (1.0 + mass_mev**2 / (2.0 * omega**2)) * velocity
    )
    x = omega / temperature_mev
    production = (
        2.0 / velocity
        * susceptibility_mev3
        / np.expm1(x)
        * sigma
    )
    absorption = np.exp(x) * production
    reduced = -np.expm1(-x) * absorption
    reduced_closed = (
        4.0 * ALPHA / (3.0 * M_MU**2)
        * susceptibility_mev3
        * (1.0 + mass_mev**2 / (2.0 * omega**2))
    )
    return {
        "sigma": sigma,
        "production": production,
        "absorption": absorption,
        "reduced_absorption": reduced,
        "reduced_closed": reduced_closed,
    }


def run(profile_path: Path = DEFAULT_PROFILE, output_path: Path = DEFAULT_OUTPUT) -> dict:
    started = time.time()
    profile_sha = sha256(profile_path)
    if profile_sha != EXPECTED_PROFILE_SHA256:
        raise ValueError(
            f"Unexpected profile SHA-256 {profile_sha}; expected {EXPECTED_PROFILE_SHA256}"
        )

    profile_table = read_profile_direct(profile_path)
    radial_edges = np.linspace(0.0, RADIUS_KM, RADIAL_PANELS + 1)
    radii, _ = composite_gauss(radial_edges, RADIAL_ORDER)
    profile = interpolate_profile(profile_table, radii)
    nr = len(radii)

    residuals = {
        key: [] for key in (
            "nu_mu_B6_production",
            "nu_tau_B6_production",
            "nu_mu_B10_absorption",
            "nu_tau_B10_absorption",
            "neutrino_B4_reduced_absorption",
            "muon_B17_density",
            "muon_B17_susceptibility",
            "muon_B17_degeneracy_factor",
            "compton_B16_production",
            "compton_B19_absorption",
            "compton_B4_reduced_absorption",
            "compton_B14_B16_velocity_cancellation",
            "total_production",
            "total_absorption",
            "total_reduced_absorption",
            "mu_numu_sign_invariance",
        )
    }
    angular_convergence = []
    point_count = 0
    min_omega = float("inf")
    max_omega = 0.0
    max_x = 0.0
    channel_max_by_radius = []

    for ir, radius in enumerate(radii):
        temperature = float(profile["T"][ir])
        mu_mu = float(profile["mu_mu"][ir])
        mu_numu = float(profile["mu_numu"][ir])
        omega, _ = log_energy_rule(
            MASS_MEV,
            MASS_MEV / float(profile["lapse"][ir]),
            ENERGY_OFFSET_MEV,
            ENERGY_PANELS,
            ENERGY_ORDER,
        )
        min_omega = min(min_omega, float(np.min(omega)))
        max_omega = max(max_omega, float(np.max(omega)))
        x = omega / temperature
        max_x = max(max_x, float(np.max(x)))

        # Reference implementation under test.
        rates = local_rates(
            MASS_MEV, omega, temperature, mu_numu, mu_mu
        )

        # Direct neutrino phase-space quadrature, separately for nu_mu and nu_tau.
        nu_mu_prod, nu_mu_abs = direct_neutrino_pair_rates(
            MASS_MEV, omega, temperature, mu_numu, NEUTRINO_ANGULAR_ORDER
        )
        nu_tau_prod, nu_tau_abs = direct_neutrino_pair_rates(
            MASS_MEV, omega, temperature, 0.0, NEUTRINO_ANGULAR_ORDER
        )
        nu_prod_direct = nu_mu_prod + nu_tau_prod
        nu_abs_direct = nu_mu_abs + nu_tau_abs
        nu_red_direct = -np.expm1(-x) * nu_abs_direct

        # Independent transformed B.17 integral for n_mu and chi_mu=n_mu F_deg.
        n_mu_direct, chi_direct, fdeg_direct = (
            independent_muon_density_susceptibility(
                temperature, mu_mu, SUSCEPTIBILITY_ORDER
            )
        )
        n_mu_ref = float(np.asarray(rates["n_mu"]))
        fdeg_ref = float(np.asarray(rates["F_deg"]))
        chi_ref = n_mu_ref * fdeg_ref
        comp_direct = direct_compton_rates(
            MASS_MEV, omega, temperature, chi_direct
        )

        # Sign reversal of mu_numu must leave the nu_mu anti-pair rate invariant.
        nu_mu_prod_flipped, _ = direct_neutrino_pair_rates(
            MASS_MEV, omega, temperature, -mu_numu, NEUTRINO_ANGULAR_ORDER
        )

        # Compare the direct angular integral against the closed B.6 expression.
        comparisons = {
            "nu_mu_B6_production": rel_max(
            nu_mu_prod,
            _analytic_neutrino_rate(MASS_MEV, omega, temperature, mu_numu),
        )
        comparisons["nu_tau_B6_production"] = rel_max(
            nu_tau_prod,
            _analytic_neutrino_rate(MASS_MEV, omega, temperature, 0.0),
        )
        comparisons["nu_mu_B10_absorption"] = rel_max(
            nu_mu_abs, np.exp(x) * nu_mu_prod
        )
        comparisons["nu_tau_B10_absorption"] = rel_max(
            nu_tau_abs, np.exp(x) * nu_tau_prod
        )
        comparisons["neutrino_B4_reduced_absorption"] = rel_max(
            nu_red_direct, np.expm1(x) * nu_prod_direct
        )
        comparisons["muon_B17_density"] = abs(n_mu_direct / n_mu_ref - 1.0)
        comparisons["muon_B17_susceptibility"] = abs(chi_direct / chi_ref - 1.0)
        comparisons["muon_B17_degeneracy_factor"] = abs(fdeg_direct / fdeg_ref - 1.0)
        comparisons["compton_B16_production"] = rel_max(
            comp_direct["production"], rates["compton_production"]
        )
        comparisons["compton_B19_absorption"] = rel_max(
            comp_direct["absorption"],
            np.exp(x) * comp_direct["production"],
        )
        comparisons["compton_B4_reduced_absorption"] = rel_max(
            comp_direct["reduced_absorption"],
            np.expm1(x) * comp_direct["production"],
        )
        comparisons["compton_B14_B16_velocity_cancellation"] = rel_max(
            comp_direct["reduced_absorption"], comp_direct["reduced_closed"]
        )
        total_prod_direct = nu_prod_direct + comp_direct["production"]
        total_abs_direct = nu_abs_direct + comp_direct["absorption"]
        total_red_direct = nu_red_direct + comp_direct["reduced_absorption"]
        comparisons["total_production"] = rel_max(
            total_prod_direct, rates["production"]
        )
        comparisons["total_absorption"] = rel_max(
            total_abs_direct, rates["absorption"]
        )
        comparisons["total_reduced_absorption"] = rel_max(
            total_red_direct, rates["reduced_absorption"]
        )
        comparisons["mu_numu_sign_invariance"] = rel_max(
            nu_mu_prod_flipped, nu_mu_prod
        )

        # A lower-order direct angular rule checks the 512-point angular
        # quadrature at every fifth source radius, over all energy nodes.
        if ir % 5 == 0:
            nu_mu_256, _ = direct_neutrino_pair_rates(
                MASS_MEV, omega, temperature, mu_numu,
                NEUTRINO_ANGULAR_CHECK_ORDER
            )
            nu_tau_256, _ = direct_neutrino_pair_rates(
                MASS_MEV, omega, temperature, 0.0,
                NEUTRINO_ANGULAR_CHECK_ORDER
            )
            angular_convergence.append({
                "radius_km": float(radius),
                "maximum_relative_change_256_to_512": rel_max(
                    nu_mu_256 + nu_tau_256, nu_prod_direct
                ),
            })

        for key, value in comparisons.items():
            residuals[key].append(float(value))
        point_count += len(omega)
        channel_max_by_radius.append({
            "radius_km": float(radius),
            "maximum_local_residual": float(max(comparisons.values())),
        })
        if ir % 20 == 0 or ir == nr - 1:
            print(
                f"dense local audit radial node {ir+1}/{nr} "
                f"(r={radius:.4f} km) completed",
                flush=True,
            )

    summary = {
        key: {
            "maximum_relative_residual": float(np.max(values)),
            "p99_relative_residual_over_radial_nodes": float(np.quantile(values, 0.99)),
            "rms_of_radial_maxima": float(np.sqrt(np.mean(np.asarray(values)**2))),
        }
        for key, values in residuals.items()
    }
    angular_max = float(max(x["maximum_relative_change_256_to_512"] for x in angular_convergence))
    payload = {
        "title": "Dense local B.6--B.10 and B.14--B.19 kernel audit on the full B.1+B.2 quadrature grid",
        "status": "completed",
        "scope": "Local production, absorption, reduced-absorption, and B.17 susceptibility formulae only; no global source or transport recomputation.",
        "profile": {
            "path": Path(profile_path).name,
            "sha256": profile_sha,
            "expected_sha256": EXPECTED_PROFILE_SHA256,
        },
        "configuration": {
            "mass_MeV": MASS_MEV,
            "number_of_radial_nodes": int(nr),
            "number_of_energy_nodes_per_radius": int(ENERGY_PANELS * ENERGY_ORDER),
            "total_radius_energy_points": int(point_count),
            "radial_panels": RADIAL_PANELS,
            "radial_order": RADIAL_ORDER,
            "energy_panels": ENERGY_PANELS,
            "energy_order": ENERGY_ORDER,
            "energy_upper_MeV": MASS_MEV + ENERGY_OFFSET_MEV,
            "neutrino_angular_order": NEUTRINO_ANGULAR_ORDER,
            "neutrino_angular_check_order": NEUTRINO_ANGULAR_CHECK_ORDER,
            "susceptibility_order": SUSCEPTIBILITY_ORDER,
            "omega_min_over_all_nodes_MeV": min_omega,
            "omega_max_over_all_nodes_MeV": max_omega,
            "maximum_omega_over_T": max_x,
        },
        "independent_methods": {
            "neutrino": "Direct two-body angular phase-space integral of f_nu(E1) f_antinu(E2) and inverse-occupation factors, separately for nu_mu and nu_tau.",
            "muon_susceptibility": "Independent transformed Gauss-Legendre integral in t=sqrt((E-m_mu)/T), following the printed one-species B.17 convention.",
            "compton": "Direct vectorized B.14 cross section, B.16 production, B.19 detailed balance, and B.4 reduced absorption using independently integrated chi_mu.",
            "reference_under_test": "reference.local_rates on exactly the same radius-dependent energy quadrature nodes.",
        },
        "maximum_residuals": summary,
        "angular_quadrature_check": {
            "number_of_radial_nodes_checked": len(angular_convergence),
            "maximum_relative_change_256_to_512": angular_max,
            "checks": angular_convergence,
        },
        "radial_maximum_residuals": channel_max_by_radius,
        "production_axial_outputs_modified": False,
        "limitations": [
            "The local production kernels are checked against direct local phase-space integrals, but this does not validate the physical no-recoil approximation against the exact moving-muon B.13 process.",
            "The audit uses the same reconstructed public-figure stellar profile as the global calculation, not the raw Garching simulation table.",
            "The fixed-omega Appendix-B energy prescription is retained.",
        ],
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "code_sha256": sha256(Path(__file__)),
        "elapsed_seconds": float(time.time() - started),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return payload


def _analytic_neutrino_rate(mass_mev, omega, temperature, chemical_potential):
    omega = np.asarray(omega, float)
    velocity = np.sqrt(np.maximum(1.0 - (mass_mev / omega)**2, 0.0))
    return (
        mass_mev**2 / (8.0 * np.pi * omega)
        * fermi_pair_average(chemical_potential, omega, temperature, velocity)
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.profile, args.output)
    print(json.dumps({
        "output": str(args.output),
        "configuration": result["configuration"],
        "maximum_residuals": result["maximum_residuals"],
        "angular_quadrature_check": result["angular_quadrature_check"],
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2), flush=True)


if __name__ == "__main__":
    main()
