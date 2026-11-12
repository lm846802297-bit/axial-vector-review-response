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
import sys
from pathlib import Path

import numpy as np

import rates
from finite_mixing.thermal_integrals.moving_compton import (
    moving_compton_matrix_elements,
)

HERE = Path(__file__).resolve().parent
M_MU = rates.M_MU
LITERATURE_DIR = HERE.parents[2] / "stellar-cooling-eft-literature-20261105"
sys.path.insert(0, str(LITERATURE_DIR))
import reference_matrix_element as ref


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


def direct_spinor_production_cross_sections(mass, photon_energy, order=256):
    """Independent direct-production result from explicit Dirac spinors.

    The reference module constructs gamma+mu -> mu+A' directly in the
    initial-muon rest frame and resolves the final A' using the medium-frame
    spatial-transverse projector. It returns (sigma_L, sigma_T1+T2).
    """
    sigma_t = ref.total_cross_section_lab(
        photon_energy, mass, 1.0, 0.0, mode="T", n_angle=order
    )
    sigma_l = ref.total_cross_section_lab(
        photon_energy, mass, 1.0, 0.0, mode="L", n_angle=order
    )
    return float(sigma_l), float(sigma_t)


def direct_spinor_differential_by_mode(mass, photon_energy, cosines):
    """Return d sigma/d cos(theta) for direct production in the medium frame."""
    exact_t = []
    exact_l = []
    for cosine in cosines:
        # reference_matrix_element returns d sigma/d Omega; integrate azimuth.
        exact_t.append(
            2.0 * math.pi * ref.differential_cross_section_lab(
                photon_energy, mass, float(cosine), 1.0, 0.0, mode="T"
            )
        )
        exact_l.append(
            2.0 * math.pi * ref.differential_cross_section_lab(
                photon_energy, mass, float(cosine), 1.0, 0.0, mode="L"
            )
        )
    return np.asarray(exact_t), np.asarray(exact_l)


def printed_b6_differential_formulas(mass, photon_energy, cosines):
    """Appendix B, Eq. (B.6a,b), copied with the paper's T/L labels."""
    alpha = rates.ALPHA
    alpha_x = 1.0 / (4.0 * math.pi)
    prefactor = math.pi * alpha * alpha_x / (
        M_MU * M_MU * photon_energy * photon_energy
    )
    c = np.asarray(cosines, dtype=float)
    b6a_t = prefactor * (mass * mass + 2.0 * photon_energy**2 * c)
    b6b_l = prefactor * (
        photon_energy**2 * (1.0 + c * c)
        - c * (mass * mass + 2.0 * photon_energy**2)
    )
    return b6a_t, b6b_l


def direct_vector_mediator_ward_residual(mass, photon_energy, cosine=0.3):
    """Explicit-spinor check of q_mu M^mu=0 for the conserved vector current."""
    p, k, p_prime, q = ref.lab_kinematics(
        photon_energy, mass, cosine, M_MU
    )
    maximum = 0.0
    for initial_spin in range(2):
        u_in = ref.u_spinor(p, M_MU, initial_spin)
        for final_spin in range(2):
            u_out = ref.u_spinor(p_prime, M_MU, final_spin)
            ubar = u_out.conj().T @ ref.GAMMA[0]
            for eps_gamma in ref.photon_polarizations():
                matrix = ref.amplitude_matrix(
                    p, k, p_prime, q, M_MU, eps_gamma, q, 1.0, 0.0
                )
                maximum = max(maximum, float(abs(ubar @ matrix @ u_in)))
    return maximum


def printed_low_energy_formulas(mass, photon_energy):
    """Section 5.2, Eq. (5.9a,b) as printed in arXiv:2610.35379v1."""
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
    # Use the established non-singular Ward benchmark. At the tiny M/E
    # production point, the physical longitudinal amplitude is very small,
    # so a relative Ward residual normalized by that mode becomes dominated
    # by floating-point cancellation rather than gauge noninvariance.
    ward_mass, ward_energy = 7.0, 41.0
    cosines = np.array([-0.7, 0.2, 0.8])
    eg, physical = rates.compton_matrix_elements(
        ward_mass, [ward_energy], cosines, current="vector"
    )
    _, photon_ward = rates.compton_matrix_elements(
        ward_mass, [ward_energy], cosines, current="vector", photon_ward=True
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
    crossed_scans = {
        str(order): exact_production_cross_sections(mass, photon_energy, order)
        for order in orders
    }
    crossed = crossed_scans[str(orders[-1])]
    crossed_t = float(crossed[1] + crossed[2])
    crossed_l = float(crossed[0])

    direct_l, direct_t = direct_spinor_production_cross_sections(
        mass, photon_energy, order=orders[-1]
    )
    direct_by_mode = np.array([direct_l, direct_t / 2.0, direct_t / 2.0])
    direct_crossed_residual = relative_difference(direct_by_mode, crossed)

    sigma_t_paper, sigma_l_paper, sigma_thomson = printed_low_energy_formulas(
        mass, photon_energy
    )
    cosines = np.linspace(-1.0, 1.0, 401)
    exact_t_dcos, exact_l_dcos = direct_spinor_differential_by_mode(
        mass, photon_energy, cosines
    )
    paper_b6a_t, paper_b6b_l = printed_b6_differential_formulas(
        mass, photon_energy, cosines
    )

    nodes, weights = np.polynomial.legendre.leggauss(512)
    b6a_nodes, b6b_nodes = printed_b6_differential_formulas(
        mass, photon_energy, nodes
    )
    b6a_integral = float(np.dot(weights, b6a_nodes))
    b6b_integral = float(np.dot(weights, b6b_nodes))
    phase = math.sqrt(1.0 - (mass / photon_energy) ** 2)

    mode_convergence = relative_difference(
        crossed_scans["128"], crossed_scans["256"]
    )
    projector = medium_frame_projector_checks(mass, photon_energy)
    wards = ward_checks(mass, photon_energy)
    direct_photon_ward = ref.ward_identity_residual(
        photon_energy, mass, 0.3, 1.0, 0.0
    )
    direct_vector_ward = direct_vector_mediator_ward_residual(
        mass, photon_energy, 0.3
    )

    sigma_t_reference = direct_t
    sigma_l_reference = direct_l
    paper_factor_a = mass * mass + 2.0 * photon_energy**2 * cosines
    paper_factor_b = (
        photon_energy**2 * (1.0 + cosines**2)
        - cosines * (mass * mass + 2.0 * photon_energy**2)
    )
    max_abs_over_thomson = lambda x: float(
        np.max(np.abs(x)) / sigma_thomson
    )

    payload = {
        "title": "Independent vector semi-Compton polarization audit",
        "source": {
            "arxiv": "2610.35379v1",
            "model_section": "Sec. 5.1-5.2; vector U(1)_{L_mu-L_tau} muon current",
            "integrated_low_energy_formulas": "Eq. (5.9a,b)",
            "medium_polarization_projector": "Eq. (A.15)",
            "exact_semi_compton_amplitude": "Appendix B, Eqs. (B.1a,b)",
            "printed_angular_differential_cross_sections": "Appendix B, Eqs. (B.6a,b)",
        },
        "scope": (
            "Direct explicit-Dirac-spinor production calculation in the initial-muon "
            "rest frame, cross-checked against the independent repository trace kernel "
            "by detailed reciprocity. No stellar profile or transport."
        ),
        "units": {"energy": "MeV", "cross_section": "MeV^-2"},
        "benchmark": {
            "mediator_mass_MeV": mass,
            "incoming_photon_energy_MeV": photon_energy,
            "muon_mass_MeV": M_MU,
            "g_vector": 1.0,
            "g_axial": 0.0,
            "initial_photon_polarization_average": 2,
            "medium_frame_mode_order": ["L", "T1", "T2"],
        },
        "method": {
            "direct_spinor_kernel": "reference_matrix_element.total_cross_section_lab",
            "direct_differential_kernel": "reference_matrix_element.differential_cross_section_lab",
            "independent_cross_check": (
                "rates.compton_kernels(current='vector') for inverse absorption, "
                "crossed with sigma_prod,h = 1/2 * (p_Aprime_CM/p_gamma_CM)^2 * sigma_abs,h"
            ),
            "projector_definition": (
                "P_T^{ij}=delta^{ij}-qhat^i*qhat^j, P_T^{0mu}=0; "
                "P_L=-g+q*q/m_Aprime^2-P_T"
            ),
            "thomson_reference": "8*pi*alpha*alpha_X/(3*m_mu^2), alpha_X=g_X^2/(4*pi)",
            "printed_formulas": (
                "Eq. (5.9) and Eq. (B.6) are compared with their printed T/L labels; "
                "no label swap or coefficient adjustment is made in the input formulas."
            ),
        },
        "direct_exact_production_cross_sections_MeV_minus2": {
            "T_sum": sigma_t_reference,
            "L": sigma_l_reference,
            "T1": float(direct_by_mode[1]),
            "T2": float(direct_by_mode[2]),
        },
        "crossed_trace_production_cross_sections_MeV_minus2": {
            "L": float(crossed[0]),
            "T1": float(crossed[1]),
            "T2": float(crossed[2]),
        },
        "sigma_thomson_MeV_minus2": sigma_thomson,
        "ratios_to_thomson": {
            "direct_exact_T_sum": sigma_t_reference / sigma_thomson,
            "direct_exact_L": sigma_l_reference / sigma_thomson,
            "paper_Eq5_9a_T_as_printed": sigma_t_paper / sigma_thomson,
            "paper_Eq5_9b_L_as_printed": sigma_l_paper / sigma_thomson,
        },
        "printed_Eq5_9_comparison": {
            "paper_T_over_exact_L": sigma_t_paper / sigma_l_reference,
            "paper_L_over_exact_T_sum": sigma_l_paper / sigma_t_reference,
            "exact_L_over_exact_T_sum": sigma_l_reference / sigma_t_reference,
            "direct_T_over_paper_L": sigma_t_reference / sigma_l_paper,
            "direct_L_over_paper_T": sigma_l_reference / sigma_t_paper,
        },
        "printed_EqB6_differential_comparison": {
            "EqB6a_printed_T_negative_fraction": float(np.mean(paper_b6a_t < 0.0)),
            "EqB6b_printed_L_negative_fraction": float(np.mean(paper_b6b_l < 0.0)),
            "EqB6a_T_minimum_over_angular_grid_MeV_minus2": float(
                np.min(paper_b6a_t)
            ),
            "EqB6b_L_minimum_over_angular_grid_MeV_minus2": float(
                np.min(paper_b6b_l)
            ),
            "exact_T_minimum_over_angular_grid_MeV_minus2": float(
                np.min(exact_t_dcos)
            ),
            "exact_L_minimum_over_angular_grid_MeV_minus2": float(
                np.min(exact_l_dcos)
            ),
            "max_abs_exact_T_minus_printed_B6b_over_Thomson": max_abs_over_thomson(
                exact_t_dcos - paper_b6b_l
            ),
            "max_abs_exact_L_minus_printed_B6a_over_Thomson": max_abs_over_thomson(
                exact_l_dcos - paper_b6a_t
            ),
            "max_abs_exact_T_minus_printed_B6a_over_Thomson": max_abs_over_thomson(
                exact_t_dcos - paper_b6a_t
            ),
            "max_abs_exact_L_minus_printed_B6b_over_Thomson": max_abs_over_thomson(
                exact_l_dcos - paper_b6b_l
            ),
            "angular_convention": (
                "The paper identifies theta as the scattering angle and integrates "
                "cos(theta) over [-1,1]. The signs are evaluated on that stated range."
            ),
        },
        "EqB6_integrals_and_Eq5_9_phase_factor": {
            "numerical_integral_B6a_MeV_minus2": b6a_integral,
            "numerical_integral_B6b_MeV_minus2": b6b_integral,
            "Eq5_9a_over_integral_B6a": sigma_t_paper / b6a_integral,
            "Eq5_9b_over_integral_B6b": sigma_l_paper / b6b_integral,
            "sqrt_1_minus_m2_over_E2": phase,
            "note": (
                "The printed B.6 angular expressions integrate without the common "
                "sqrt(1-m_Z'^2/E_gamma^2) factor present in Eq. (5.9)."
            ),
        },
        "independent_direct_vs_crossed_trace": {
            "max_relative_difference": direct_crossed_residual,
            "quadrature_orders": list(orders),
            "crossed_sigma_by_order_L_Tplus_Tminus": {
                order: [float(x) for x in crossed_scans[str(order)]]
                for order in orders
            },
        },
        "medium_rest_frame_projector_checks": projector,
        "ward_checks": {
            **wards,
            "direct_spinor_photon_ward_max_abs": float(direct_photon_ward),
            "direct_spinor_vector_mediator_ward_max_abs": float(direct_vector_ward),
        },
        "positivity": {
            "direct_exact_mode_cross_sections_nonnegative": bool(
                sigma_t_reference >= 0.0 and sigma_l_reference >= 0.0
            ),
            "direct_exact_differential_cross_sections_nonnegative": bool(
                np.all(exact_t_dcos >= 0.0) and np.all(exact_l_dcos >= 0.0)
            ),
        },
        "interpretation_flags": {
            "integrated_Eq5_9_TL_hierarchy_opposite_to_conserved_vector_limit": bool(
                sigma_t_paper < sigma_l_paper
                and sigma_t_reference > sigma_l_reference
            ),
            "printed_EqB6a_has_negative_differential_region": bool(
                np.any(paper_b6a_t < 0.0)
            ),
            "printed_EqB6b_has_negative_differential_region": bool(
                np.any(paper_b6b_l < 0.0)
            ),
            "EqB6b_shape_tracks_exact_transverse_mode": (
                max_abs_over_thomson(exact_t_dcos - paper_b6b_l)
                < max_abs_over_thomson(exact_t_dcos - paper_b6a_t)
            ),
        },
        "acceptance": {
            "thomson_transverse_limit_pass": abs(
                sigma_t_reference / sigma_thomson - 1.0
            ) < 5e-3,
            "conserved_vector_longitudinal_suppression_pass": (
                sigma_l_reference / sigma_t_reference < 1e-3
            ),
            "positive_exact_cross_sections_pass": bool(
                sigma_t_reference > 0.0 and sigma_l_reference > 0.0
                and np.all(exact_t_dcos >= 0.0)
                and np.all(exact_l_dcos >= 0.0)
            ),
            "direct_spinor_vs_crossed_trace_pass": direct_crossed_residual < 1e-3,
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
            ) < 1e-10,
            "photon_ward_pass": (
                wards["photon_ward_relative_residual"] < 2e-12
                and direct_photon_ward < 1e-7
            ),
            "vector_mediator_ward_pass": (
                wards["vector_mediator_ward_max_abs"] < 2e-9
                and direct_vector_ward < 1e-7
            ),
        },
    }
    return payload

def json_native(value):
    """Recursively convert NumPy scalars/arrays to standard JSON-native values."""

    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, dict):
        return {str(key): json_native(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_native(item) for item in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mass", type=float, default=0.001)
    parser.add_argument("--photon-energy", type=float, default=0.1)
    parser.add_argument("--output", type=Path, default=HERE / "outputs" / "vector_semicompton_polarization_audit.json")
    args = parser.parse_args()
    payload = json_native(build_audit(args.mass, args.photon_energy))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload["acceptance"], indent=2))
    print(json.dumps(payload["printed_Eq5_9_comparison"], indent=2))
    if not all(payload["acceptance"].values()):
        raise SystemExit("Exact vector-current physical acceptance checks failed")


if __name__ == "__main__":
    main()
