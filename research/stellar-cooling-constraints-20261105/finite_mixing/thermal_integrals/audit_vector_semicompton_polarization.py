#!/usr/bin/env python3
"""Independent vector-current T/L audit for the semi-Compton source formulas.

The repository rate kernel is evaluated for the time-reversed absorption
process A' + mu -> gamma + mu. Reciprocity in the CM frame maps each fixed
A' polarization to the corresponding final A' polarization in production:
  sigma_prod,h = (1/2) (p_A'/p_gamma)^2 sigma_abs,h.
The factor 1/2 averages the two initial photon polarizations in production;
the absorption kernel sums over final photon polarizations. The CM momentum
ratio is computed from the Kallen function, not from lab three-momenta.

This script deliberately separates the exact Dirac-kernel result from the
low-energy expressions as printed in arXiv:2610.35379v1, Eqs. (58a,b).
It does not silently swap labels or alter a coefficient to force agreement.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

import rates
from finite_mixing.thermal_integrals.moving_compton import (
    moving_compton_matrix_elements,
)

HERE = Path(__file__).resolve().parent
M_MU = rates.M_MU


def relative_difference(a, b):
    aa = np.asarray(a, dtype=float)
    bb = np.asarray(b, dtype=float)
    return float(np.max(np.abs(aa - bb) / np.maximum(np.abs(bb), 1e-300)))


def exact_production_cross_sections(mass, photon_energy, order=128):
    """Return exact production sigma for (L,+,-), in MeV^-2.

    rates.compton_kernels returns v_A' * sigma_abs for a fixed incident
    A' polarization and sums the two final photon polarizations. The reverse
    production process averages the two initial photon polarizations.
    """
    e_vector = photon_energy - mass * mass / (2.0 * M_MU)
    if e_vector <= mass:
        raise ValueError("Photon energy is below the physical semi-Compton threshold")
    _, weighted_absorption = rates.compton_kernels(
        mass, [e_vector], order=order, current="vector"
    )
    v_vector = math.sqrt(e_vector * e_vector - mass * mass) / e_vector
    sigma_abs = np.sum(weighted_absorption[0], axis=0) / v_vector

    s = M_MU * M_MU + 2.0 * M_MU * photon_energy
    lam = (s - M_MU * M_MU - mass * mass) ** 2 - (
        4.0 * M_MU * M_MU * mass * mass
    )
    p_ratio_squared = lam / ((s - M_MU * M_MU) ** 2)
    if lam <= 0.0 or p_ratio_squared <= 0.0:
        raise ArithmeticError("Unphysical CM two-body momentum ratio")
    sigma_prod = 0.5 * p_ratio_squared * sigma_abs
    return sigma_prod


def printed_low_energy_formulas(mass, photon_energy):
    """Eq. (58a,b) as transcribed from arXiv:2610.35379v1."""
    alpha = rates.ALPHA
    alpha_x = 1.0 / (4.0 * math.pi)  # g_X = 1
    root = math.sqrt(1.0 - (mass / photon_energy) ** 2)
    sigma_t = (
        2.0 * math.pi * alpha * alpha_x * mass * mass
        / (M_MU * M_MU * photon_energy * photon_energy) * root
    )
    sigma_l = (
        8.0 * math.pi * alpha * alpha_x / (3.0 * M_MU * M_MU) * root
    )
    sigma_thomson = (
        8.0 * math.pi * alpha * alpha_x / (3.0 * M_MU * M_MU)
    )
    return sigma_t, sigma_l, sigma_thomson


def medium_frame_projector_checks(mass, omega):
    """Check covariant U-frame L/T polarization projectors explicitly."""
    metric = np.diag([1.0, -1.0, -1.0, -1.0])
    k = math.sqrt(omega * omega - mass * mass)
    q = np.array([omega, 0.0, 0.0, k])
    u = np.array([1.0, 0.0, 0.0, 0.0])
    q_dot_u = float(q @ metric @ u)
    eps_l = (q_dot_u * q - mass * mass * u) / (
        mass * math.sqrt(q_dot_u * q_dot_u - mass * mass)
    )
    eps_x = np.array([0.0, 1.0, 0.0, 0.0])
    eps_y = np.array([0.0, 0.0, 1.0, 0.0])
    total = -metric + np.outer(q, q) / (mass * mass)
    p_l = np.outer(eps_l, eps_l)
    p_t = total - p_l
    p_t_explicit = np.outer(eps_x, eps_x) + np.outer(eps_y, eps_y)

    dot = lambda a, b: float(a @ metric @ b)
    return {
        "q_dot_eps_l": dot(q, eps_l),
        "eps_l_norm_plus_one": dot(eps_l, eps_l) + 1.0,
        "eps_x_norm_plus_one": dot(eps_x, eps_x) + 1.0,
        "eps_y_norm_plus_one": dot(eps_y, eps_y) + 1.0,
        "eps_l_dot_eps_x": dot(eps_l, eps_x),
        "eps_l_dot_eps_y": dot(eps_l, eps_y),
        "p_t_explicit_max_abs_residual": float(
            np.max(np.abs(p_t - p_t_explicit))
        ),
        "q_contraction_p_t_max_abs": float(
            np.max(np.abs(q @ metric @ p_t))
        ),
        "u_contraction_p_t_max_abs": float(
            np.max(np.abs(u @ metric @ p_t))
        ),
        "completeness_max_abs_residual": float(
            np.max(np.abs(p_l + p_t - total))
        ),
    }


def ward_checks(mass, photon_energy):
    e_vector = photon_energy - mass * mass / (2.0 * M_MU)
    cosines = np.array([-0.7, 0.2, 0.8])
    eg, physical = rates.compton_matrix_elements(
        mass, [e_vector], cosines, current="vector"
    )
    _, photon_ward = rates.compton_matrix_elements(
        mass, [e_vector], cosines, current="vector", photon_ward=True
    )
    photon_residual = float(
        np.max(
            np.abs(photon_ward)
            / np.maximum(eg[..., None] ** 2 * np.abs(physical), 1e-300)
        )
    )

    args = (
        20.0, 45.0, np.array([25.0, 80.0]),
        np.array([0.2, -0.4]), np.array([-0.3, 0.7]),
        np.array([0.5, 2.1]), 1.0, 0.0,
    )
    _, _, mediator_ward = moving_compton_matrix_elements(
        *args, vector_mediator_ward=True
    )
    return {
        "photon_ward_relative_residual": photon_residual,
        "vector_mediator_ward_max_abs": float(
            np.max(np.abs(mediator_ward[:, 0]))
        ),
    }


def build_audit(mass=0.001, photon_energy=0.1):
    orders = (32, 64, 128, 256)
    scans = {
        str(order): exact_production_cross_sections(mass, photon_energy, order)
        for order in orders
    }
    exact = scans[str(orders[-1])]
    sigma_t_exact = float(exact[1] + exact[2])
    sigma_l_exact = float(exact[0])
    sigma_t_paper, sigma_l_paper, sigma_thomson = printed_low_energy_formulas(
        mass, photon_energy
    )
    paper_factor = mass * mass + 2.0 * photon_energy * photon_energy * np.linspace(-1, 1, 401)

    mode_convergence = relative_difference(scans["128"], scans["256"])
    projector = medium_frame_projector_checks(mass, photon_energy)
    wards = ward_checks(mass, photon_energy)

    payload = {
        "title": "Independent vector semi-Compton polarization audit",
        "source_formula": "arXiv:2610.35379v1, Eqs. (58a,b), (77), and (106a) as transcribed for this audit",
        "scope": (
            "Exact repository Dirac trace for the inverse process, crossed to "
            "production using CM detailed reciprocity; no stellar profile or transport."
        ),
        "units": {"energy": "MeV", "cross_section": "MeV^-2"},
        "benchmark": {
            "mediator_mass_MeV": mass,
            "incoming_photon_energy_MeV": photon_energy,
            "muon_mass_MeV": M_MU,
            "g_vector": 1.0,
            "g_axial": 0.0,
            "initial_photon_polarization_average": 2,
            "production_mode_order": ["L", "+", "-"],
        },
        "method": {
            "exact_kernel": "rates.compton_kernels(current='vector')",
            "crossing": "sigma_prod,h = 1/2 * (p_Aprime_CM/p_gamma_CM)^2 * sigma_abs,h",
            "cm_momentum_ratio_squared": "lambda(s,m_mu^2,m_Aprime^2)/(s-m_mu^2)^2",
            "thomson_reference": "8*pi*alpha*alpha_X/(3*m_mu^2), alpha_X=g_X^2/(4*pi)",
            "paper_formula_status": "printed Eq. (58a,b) is compared literally; labels and coefficients are not silently altered",
        },
        "exact_sigma_production_by_mode_MeV_minus2": {
            "L": float(exact[0]), "+": float(exact[1]), "-": float(exact[2])
        },
        "exact_sigma_T_sum_MeV_minus2": sigma_t_exact,
        "exact_sigma_L_MeV_minus2": sigma_l_exact,
        "sigma_thomson_MeV_minus2": sigma_thomson,
        "ratios_to_thomson": {
            "exact_T_sum": sigma_t_exact / sigma_thomson,
            "exact_L": sigma_l_exact / sigma_thomson,
            "paper_T_as_printed": sigma_t_paper / sigma_thomson,
            "paper_L_as_printed": sigma_l_paper / sigma_thomson,
        },
        "printed_formula_comparison": {
            "paper_T_over_exact_L": sigma_t_paper / sigma_l_exact,
            "paper_L_over_exact_T_sum": sigma_l_paper / sigma_t_exact,
            "exact_L_over_exact_T_sum": sigma_l_exact / sigma_t_exact,
        },
        "quadrature": {
            "orders": list(orders),
            "relative_difference_order128_to256": mode_convergence,
            "sigma_by_order": {
                order: [float(x) for x in scans[str(order)]]
                for order in orders
            },
        },
        "eq106a_printed_angular_factor_diagnostic": {
            "factor": "m_Aprime^2 + 2*E_gamma^2*cos(theta)",
            "minimum_MeV2": float(np.min(paper_factor)),
            "negative_fraction_on_uniform_cosine_grid": float(
                np.mean(paper_factor < 0.0)
            ),
            "convention_warning": (
                "This sign check assumes the standard Compton scattering-angle "
                "cos(theta) in [-1,1]; verify the source's angular convention before "
                "classifying it as a paper error."
            ),
        },
        "medium_rest_frame_projector_checks": projector,
        "ward_checks": wards,
        "positivity": {
            "minimum_exact_mode_cross_section_MeV_minus2": float(np.min(exact)),
            "all_exact_mode_cross_sections_nonnegative": bool(np.all(exact >= 0.0)),
        },
        "acceptance": {
            "thomson_transverse_limit_pass": abs(sigma_t_exact / sigma_thomson - 1.0) < 5e-3,
            "conserved_vector_longitudinal_suppression_pass": sigma_l_exact / sigma_t_exact < 1e-3,
            "positive_exact_cross_sections_pass": bool(np.all(exact >= 0.0)),
            "quadrature_convergence_pass": mode_convergence < 1e-5,
            "medium_frame_projectors_pass": max(
                abs(projector["q_dot_eps_l"]),
                abs(projector["eps_l_norm_plus_one"]),
                abs(projector["eps_x_norm_plus_one"]),
                abs(projector["eps_y_norm_plus_one"]),
                abs(projector["p_t_explicit_max_abs_residual"]),
                abs(projector["q_contraction_p_t_max_abs"]),
                abs(projector["u_contraction_p_t_max_abs"]),
                abs(projector["completeness_max_abs_residual"]),
            ) < 1e-12,
            "photon_ward_pass": wards["photon_ward_relative_residual"] < 2e-12,
            "vector_mediator_ward_pass": wards["vector_mediator_ward_max_abs"] < 2e-9,
        },
    }
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mass", type=float, default=0.001)
    parser.add_argument("--photon-energy", type=float, default=0.1)
    parser.add_argument("--output", type=Path, default=HERE / "outputs" / "vector_semicompton_polarization_audit.json")
    args = parser.parse_args()
    payload = build_audit(args.mass, args.photon_energy)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload["acceptance"], indent=2))
    print(json.dumps(payload["printed_formula_comparison"], indent=2))
    if not all(payload["acceptance"].values()):
        raise SystemExit("Exact vector-current physical acceptance checks failed")


if __name__ == "__main__":
    main()
