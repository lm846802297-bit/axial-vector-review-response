"""Independent explicit-spinor audit of the moving-muon B.13 Compton trace.

This audit does not reuse the production Dirac trace to form the reference:
it builds on-shell Dirac spinors, sums explicit initial/final muon spins and
two physical photon polarizations, and compares with moving_muon_point_kernel.
All energies and masses are in MeV.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
FINITE_MIXING = HERE.parent
ROOT = FINITE_MIXING.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from finite_mixing.moving_muon_compton import moving_muon_point_kernel

M_MU = 105.6583755
E2 = 4.0 * math.pi / 137.035999084
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)
GAMMA = np.empty((4, 4, 4), dtype=complex)
GAMMA[0] = np.block([[I2, Z2], [Z2, -I2]])
for _i, _sigma in enumerate(PAULI, start=1):
    GAMMA[_i] = np.block([[Z2, _sigma], [-_sigma, Z2]])
GAMMA5 = 1j * GAMMA[0] @ GAMMA[1] @ GAMMA[2] @ GAMMA[3]
G0 = GAMMA[0]
METRIC = np.array([1.0, -1.0, -1.0, -1.0])
I4 = np.eye(4, dtype=complex)

KINEMATIC_POINTS = (
    (10.0, 30.0, 80.0, 0.40, -0.30, 1.20),
    (10.0, 30.0, 80.0, -0.20, 0.60, 2.10),
    (10.0, 45.0, 130.0, 0.75, -0.85, 0.40),
    (10.0, 25.0, 50.0, -0.65, 0.20, 5.20),
    (10.0, 80.0, 180.0, 0.10, 0.90, 3.20),
)
CURRENT_CASES = (
    ("vector_mu_minus", 1.0, 0.0, 1.0),
    ("vector_mu_plus", 1.0, 0.0, -1.0),
    ("axial_mu_minus", 0.0, -1.0, 1.0),
    ("axial_mu_plus", 0.0, -1.0, -1.0),
    ("mixed_mu_minus", 0.3, -0.7, 1.0),
    ("mixed_mu_plus", 0.3, -0.7, -1.0),
)


def slash(vector):
    vector = np.asarray(vector, dtype=complex)
    return sum(METRIC[mu] * vector[mu] * GAMMA[mu] for mu in range(4))


def dirac_u(momentum, spin):
    """Positive-energy Dirac spinor normalized to ubar(p)u(p)=2m."""
    energy = float(momentum[0])
    spatial = np.asarray(momentum[1:], dtype=float)
    chi = np.zeros(2, dtype=complex)
    chi[int(spin)] = 1.0
    sigma_dot_p = sum(PAULI[i] * spatial[i] for i in range(3))
    lower = sigma_dot_p @ chi / (energy + M_MU)
    return math.sqrt(energy + M_MU) * np.concatenate((chi, lower))


def photon_polarizations(direction):
    """Construct two real, orthonormal photon polarizations transverse to n."""
    n = np.asarray(direction, dtype=float)
    n = n / np.linalg.norm(n)
    reference = np.array([0.0, 1.0, 0.0])
    if abs(float(np.dot(reference, n))) > 0.9:
        reference = np.array([1.0, 0.0, 0.0])
    e1 = np.cross(reference, n)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    e2 /= np.linalg.norm(e2)
    return (np.concatenate(([0.0], e1)), np.concatenate(([0.0], e2)))


def exact_kinematics(mass, energy, p_abs, cos_mu, cos_gamma, phi_gamma):
    K = math.sqrt(energy * energy - mass * mass)
    sin_mu = math.sqrt(max(0.0, 1.0 - cos_mu * cos_mu))
    p_in = np.array([
        math.hypot(M_MU, p_abs),
        p_abs * sin_mu,
        0.0,
        p_abs * cos_mu,
    ])
    n_gamma = np.array([
        math.sqrt(max(0.0, 1.0 - cos_gamma * cos_gamma)) * math.cos(phi_gamma),
        math.sqrt(max(0.0, 1.0 - cos_gamma * cos_gamma)) * math.sin(phi_gamma),
        cos_gamma,
    ])
    q = np.array([energy, 0.0, 0.0, K])
    denominator = (
        p_in[0] + energy - np.dot(p_in[1:], n_gamma) - K * cos_gamma
    )
    photon_energy = (
        mass * mass + 2.0 * (p_in[0] * energy - p_in[3] * K)
    ) / (2.0 * denominator)
    photon = np.concatenate(([photon_energy], photon_energy * n_gamma))
    p_out = p_in + q - photon
    shell = abs(
        p_out[0] ** 2 - np.dot(p_out[1:], p_out[1:]) - M_MU ** 2
    ) / M_MU ** 2
    return p_in, q, photon, p_out, K, denominator, shell


def explicit_spinor_kernel(
    mass, energy, p_abs, cos_mu, cos_gamma, phi_gamma,
    g_vector, g_axial, charge_sign
):
    p_in, q, photon, p_out, K, denominator, shell = exact_kinematics(
        mass, energy, p_abs, cos_mu, cos_gamma, phi_gamma
    )
    prop_s = (
        slash(p_in + q) + M_MU * I4
    ) / (mass * mass + 2.0 * (p_in[0] * energy - p_in[3] * K))
    prop_u = (
        slash(p_in - photon) + M_MU * I4
    ) / (-2.0 * (p_in[0] * photon[0] - np.dot(p_in[1:], photon[1:])))
    eps_l_vector = np.array(
        [-mass / (energy + K), 0.0, 0.0, mass / (energy + K)],
        dtype=complex,
    )
    eps_l_axial = np.array(
        [K / mass, 0.0, 0.0, energy / mass], dtype=complex
    )
    eps_plus = np.array([0.0, 1.0, 1j, 0.0], dtype=complex) / math.sqrt(2.0)
    eps_minus = np.array([0.0, 1.0, -1j, 0.0], dtype=complex) / math.sqrt(2.0)
    mediator_modes = (
        (eps_l_vector, eps_l_axial),
        (eps_plus, eps_plus),
        (eps_minus, eps_minus),
    )
    photon_modes = photon_polarizations(photon[1:] / photon[0])

    mode_m2 = []
    mode_ward = []
    for eps_vector, eps_axial in mediator_modes:
        vertex = (
            g_vector * slash(eps_vector)
            + charge_sign * g_axial * slash(eps_axial) @ GAMMA5
        )
        physical_sum = 0.0
        ward_sum = 0.0
        for initial_spin in range(2):
            u_initial = dirac_u(p_out, initial_spin)
            for final_spin in range(2):
                ubar_final = dirac_u(p_in, final_spin).conjugate() @ G0
                for eps_gamma in photon_modes:
                    amplitude = (
                        vertex @ prop_s @ slash(eps_gamma)
                        + slash(eps_gamma) @ prop_u @ vertex
                    )
                    value = ubar_final @ amplitude @ u_initial
                    physical_sum += abs(value) ** 2
                ward_amplitude = (
                    vertex @ prop_s @ slash(photon)
                    + slash(photon) @ prop_u @ vertex
                )
                ward_value = ubar_final @ ward_amplitude @ u_initial
                ward_sum += abs(ward_value) ** 2
        mode_m2.append(E2 * physical_sum / 2.0)
        mode_ward.append(
            math.sqrt(ward_sum / max(physical_sum, 1.0e-300))
        )
    return {
        "matrix_element_squared_by_mode": mode_m2,
        "photon_ward_amplitude_residual_by_mode": mode_ward,
        "final_muon_shell_relative_error": shell,
        "photon_energy_MeV": float(photon[0]),
    }


def vector_longitudinal_shift_residual(
    mass, energy, p_abs, cos_mu, cos_gamma, phi_gamma
):
    p_in, q, photon, p_out, K, denominator, shell = exact_kinematics(
        mass, energy, p_abs, cos_mu, cos_gamma, phi_gamma
    )
    eps_physical = np.array([K / mass, 0.0, 0.0, energy / mass], complex)
    eps_shifted = eps_physical - q / mass
    prop_s = (
        slash(p_in + q) + M_MU * I4
    ) / (mass * mass + 2.0 * (p_in[0] * energy - p_in[3] * K))
    prop_u = (
        slash(p_in - photon) + M_MU * I4
    ) / (-2.0 * (p_in[0] * photon[0] - np.dot(p_in[1:], photon[1:])))
    physical_norm = 0.0
    difference_norm = 0.0
    for initial_spin in range(2):
        u_initial = dirac_u(p_out, initial_spin)
        for final_spin in range(2):
            ubar_final = dirac_u(p_in, final_spin).conjugate() @ G0
            for eps_gamma in photon_polarizations(photon[1:] / photon[0]):
                G = slash(eps_gamma)
                A_physical = (
                    slash(eps_physical) @ prop_s @ G
                    + G @ prop_u @ slash(eps_physical)
                )
                A_shifted = (
                    slash(eps_shifted) @ prop_s @ G
                    + G @ prop_u @ slash(eps_shifted)
                )
                a = ubar_final @ A_physical @ u_initial
                b = ubar_final @ A_shifted @ u_initial
                physical_norm += abs(a) ** 2
                difference_norm += abs(a - b) ** 2
    return math.sqrt(difference_norm / max(physical_norm, 1.0e-300))


def run_audit():
    rows = []
    max_trace_relative_residual = 0.0
    max_photon_ward_residual = 0.0
    max_shell_residual = 0.0
    max_vector_longitudinal_shift_residual = 0.0
    min_mode_m2 = math.inf

    for ip, point in enumerate(KINEMATIC_POINTS):
        mass, energy, p_abs, cos_mu, cos_gamma, phi_gamma = point
        for label, g_vector, g_axial, charge_sign in CURRENT_CASES:
            explicit = explicit_spinor_kernel(
                *point, g_vector, g_axial, charge_sign
            )
            trace = moving_muon_point_kernel(
                mass, energy, p_abs, cos_mu, cos_gamma, phi_gamma,
                g_vector, g_axial, charge_sign
            )
            explicit_m2 = np.asarray(
                explicit["matrix_element_squared_by_mode"], dtype=float
            )
            trace_m2 = np.asarray(
                trace["matrix_element_squared_by_mode"], dtype=float
            )
            relative = np.abs(explicit_m2 - trace_m2) / np.maximum(
                np.abs(trace_m2), 1.0e-300
            )
            row = {
                "point_index": ip,
                "kinematics": {
                    "mass_MeV": mass,
                    "energy_MeV": energy,
                    "initial_muon_momentum_MeV": p_abs,
                    "cos_theta_mu": cos_mu,
                    "cos_theta_gamma": cos_gamma,
                    "relative_azimuth": phi_gamma,
                },
                "current": label,
                "g_vector": g_vector,
                "g_axial_code_convention": g_axial,
                "charge_sign": charge_sign,
                "explicit_spinor_M2_by_mode": explicit_m2.tolist(),
                "trace_M2_by_mode": trace_m2.tolist(),
                "relative_residual_by_mode": relative.tolist(),
                "max_photon_ward_amplitude_residual": max(
                    explicit["photon_ward_amplitude_residual_by_mode"]
                ),
                "final_muon_shell_relative_error": explicit[
                    "final_muon_shell_relative_error"
                ],
                "minimum_mode_M2": float(np.min(explicit_m2)),
            }
            rows.append(row)
            max_trace_relative_residual = max(
                max_trace_relative_residual, float(np.max(relative))
            )
            max_photon_ward_residual = max(
                max_photon_ward_residual,
                float(row["max_photon_ward_amplitude_residual"]),
            )
            max_shell_residual = max(
                max_shell_residual,
                float(row["final_muon_shell_relative_error"]),
            )
            min_mode_m2 = min(min_mode_m2, float(np.min(explicit_m2)))

        vector_shift = vector_longitudinal_shift_residual(*point)
        max_vector_longitudinal_shift_residual = max(
            max_vector_longitudinal_shift_residual, vector_shift
        )

    return {
        "title": "Independent explicit-spinor validation of the exact moving-muon B.13 polarization kernel",
        "status": "local_independent_spinor_check_completed",
        "mode_order": ["L", "+", "-"],
        "profile_independent_kinematic_points": len(KINEMATIC_POINTS),
        "current_charge_combinations_per_point": len(CURRENT_CASES),
        "total_point_current_cases": len(rows),
        "polarization_matrix_element_count": 3 * len(rows),
        "summary": {
            "maximum_explicit_spinor_vs_dirac_trace_relative_residual": max_trace_relative_residual,
            "maximum_explicit_photon_ward_amplitude_residual": max_photon_ward_residual,
            "maximum_final_muon_shell_relative_error": max_shell_residual,
            "maximum_vector_longitudinal_ward_shift_relative_residual": max_vector_longitudinal_shift_residual,
            "minimum_explicit_mode_matrix_element_squared": min_mode_m2,
            "all_mode_matrix_elements_nonnegative": min_mode_m2 >= 0.0,
        },
        "acceptance": {
            "trace_vs_spinor_relative_tolerance": 1.0e-10,
            "photon_ward_amplitude_tolerance": 1.0e-10,
            "final_muon_shell_tolerance": 1.0e-10,
            "vector_longitudinal_shift_tolerance": 1.0e-10,
            "passed": (
                max_trace_relative_residual < 1.0e-10
                and max_photon_ward_residual < 1.0e-10
                and max_shell_residual < 1.0e-10
                and max_vector_longitudinal_shift_residual < 1.0e-10
                and min_mode_m2 >= 0.0
            ),
        },
        "conventions": {
            "spinor_normalization": "ubar(p)u(p)=2m_mu",
            "initial_muon_spin": "explicit sum followed by average 1/2",
            "final_muon_spin": "explicit sum",
            "photon_polarizations": "two explicit orthonormal real transverse vectors",
            "mediator_polarizations": "L,+,-; vector L uses Ward-equivalent epsilon_L-q/m, axial L uses physical epsilon_L",
            "mu_plus_axial_interference": "charge_sign=-1 reverses the relative vector-axial term",
            "matrix_element_normalization": "e^2=4*pi/137.035999084 included; rates remain per g_X^2",
        },
        "point_results": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "outputs" / "b13_moving_muon_explicit_spinor_audit_2026-11-13.json",
    )
    args = parser.parse_args()
    result = run_audit()
    if not result["acceptance"]["passed"]:
        raise SystemExit("Explicit-spinor B.13 audit failed its acceptance criteria")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result["summary"], indent=2, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
