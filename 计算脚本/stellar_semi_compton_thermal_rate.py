#!/usr/bin/env python3
"""Thermal muon semi-Compton emissivity in a homogeneous SN-matter cell.

Process: mu^-/mu^+ + gamma -> mu^-/mu^+ + A'.

This is a local, optically thin production calculation in natural units.
It includes isotropic Fermi-Dirac muon/antimuon distributions, the photon
Bose-Einstein distribution, final-state muon Pauli blocking, and the exact
tree-level vacuum amplitude from stellar_semi_compton_axial_matrix_element.py.
The total A' polarization sum is evaluated in the CM frame; the emitted
A' energy and final muon blocking are evaluated in the medium rest frame.

Outputs:
  event rate density R [MeV^4]
  A' energy emissivity Q [MeV^5]

It does NOT solve SN radial profiles, in-medium dispersion, absorption/trapping,
neutrino coalescence, or a global SN1987A/LESN exclusion. A converged result
requires quadrature-order and cutoff stability checks.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np

import stellar_semi_compton_axial_matrix_element as sc


@dataclass(frozen=True)
class ThermalResult:
    event_rate_mev4: float
    emissivity_mev5: float
    p_max_mev: float
    photon_max_mev: float
    quadrature_order: int
    phi_order: int


def fermi_dirac(energy: float, temperature: float, chemical_potential: float) -> float:
    x = (energy - chemical_potential) / temperature
    if x > 50.0:
        return math.exp(-x)
    if x < -50.0:
        return 1.0
    return 1.0 / (math.exp(x) + 1.0)


def bose_einstein(energy: float, temperature: float) -> float:
    x = energy / temperature
    if x <= 0.0:
        return math.inf
    if x > 50.0:
        return math.exp(-x)
    return 1.0 / math.expm1(x)


def boost_to_cm(v: np.ndarray, beta: np.ndarray) -> np.ndarray:
    """Rotationless Lorentz boost from the medium frame into the pair CM frame."""
    beta2 = float(np.dot(beta, beta))
    if beta2 < 1e-30:
        return v.copy()
    if beta2 >= 1.0:
        raise ValueError("Unphysical CM boost")
    gamma = 1.0 / math.sqrt(1.0 - beta2)
    bp = float(np.dot(beta, v[1:]))
    energy = gamma * (v[0] - bp)
    spatial = v[1:] + (
        (gamma - 1.0) * bp / beta2 - gamma * v[0]
    ) * beta
    return np.concatenate(([energy], spatial))


def medium_four_velocity_in_amplitude_cm(
    muon_energy: float,
    photon_energy: float,
    muon_momentum: float,
    cos_muon_photon: float,
    invariant_s: float,
) -> np.ndarray:
    """Express U_medium=(1,0,0,0) in CM axes with incoming photon along +z.

    In the medium frame the photon is along +z and the muon momentum lies in
    the x-z plane. We first boost U and k to the pair CM, then rotate the CM
    axes so that k_CM is the +z axis used by the matrix-element routine.
    """
    sin_psi = math.sqrt(max(1.0 - cos_muon_photon**2, 0.0))
    p_vec = np.array([
        muon_momentum * sin_psi,
        0.0,
        muon_momentum * cos_muon_photon + photon_energy,
    ])
    total_energy = muon_energy + photon_energy
    beta_cm = p_vec / total_energy
    beta2 = float(np.dot(beta_cm, beta_cm))
    if beta2 >= 1.0:
        raise ValueError("Initial pair has an unphysical CM velocity")
    gamma_cm = total_energy / math.sqrt(invariant_s)

    k_medium = np.array([photon_energy, 0.0, 0.0, photon_energy])
    k_cm_unrotated = boost_to_cm(k_medium, beta_cm)
    alpha = math.atan2(k_cm_unrotated[1], k_cm_unrotated[3])

    # U_CM before the rotation has spatial part -gamma*beta.
    ux0, uz0 = -gamma_cm * beta_cm[0], -gamma_cm * beta_cm[2]
    ca, sa = math.cos(alpha), math.sin(alpha)
    ux = ca * ux0 - sa * uz0
    uz = sa * ux0 + ca * uz0
    return np.array([gamma_cm, ux, 0.0, uz])


def minkowski_dot(a: np.ndarray, b: np.ndarray) -> float:
    return float(a[0] * b[0] - np.dot(a[1:], b[1:]))


def thermal_emissivity(
    temperature_mev: float,
    muon_chemical_potential_mev: float,
    vector_mass_mev: float,
    g_v: float,
    g_a: float,
    order: int = 8,
    phi_order: int | None = None,
    p_max_mev: float | None = None,
    photon_max_mev: float | None = None,
) -> ThermalResult:
    """Compute the optically thin local muon semi-Compton rate and emissivity.

    The chemical potential is the total mu^- chemical potential (including
    rest mass); mu^+ uses the opposite chemical potential. Initial spin
    degeneracies (2 for muons and 2 for photons) are included explicitly.
    """
    T = temperature_mev
    ma = vector_mass_mev
    m = sc.M_MU_MEV
    if T <= 0.0 or ma <= 0.0 or order < 2:
        raise ValueError("Require T>0, m_A'>0 and quadrature order >=2")
    if phi_order is None:
        phi_order = max(8, 2 * order)
    if phi_order < 4:
        raise ValueError("phi_order must be >=4")

    threshold = ma + ma * ma / (2.0 * m)
    if p_max_mev is None:
        p_fermi = math.sqrt(max(muon_chemical_potential_mev**2 - m*m, 0.0))
        p_max_mev = max(12.0*T, 6.0*math.sqrt(m*T), p_fermi + 12.0*T)
    if photon_max_mev is None:
        photon_max_mev = max(20.0*T, 2.0*threshold + 10.0*T)
    if p_max_mev <= 0.0 or photon_max_mev <= 0.0:
        raise ValueError("Integration cutoffs must be positive")

    nodes, weights = np.polynomial.legendre.leggauss(order)
    p_nodes = 0.5 * p_max_mev * (nodes + 1.0)
    p_weights = 0.5 * p_max_mev * weights
    w_nodes = 0.5 * photon_max_mev * (nodes + 1.0)
    w_weights = 0.5 * photon_max_mev * weights
    c_nodes, c_weights = nodes, weights
    theta_nodes, theta_weights = nodes, weights
    phi_values = 2.0 * math.pi * np.arange(phi_order) / phi_order
    phi_weight = 2.0 * math.pi / phi_order

    # The 1/(2 pi^4) factor includes both initial spin degeneracies (2*2)
    # and the 4 pi * 2 pi orientation integral for isotropic initial states.
    common_prefactor = 1.0 / (2.0 * math.pi**4)
    event_integral = 0.0
    energy_integral = 0.0

    for p, wp in zip(p_nodes, p_weights):
        e_mu = math.sqrt(p*p + m*m)
        beta_mu = p / e_mu
        gamma_mu = e_mu / m
        p_measure = float(wp) * p*p

        for omega, ww in zip(w_nodes, w_weights):
            f_gamma = bose_einstein(float(omega), T)
            omega_measure = float(ww) * omega*omega * f_gamma
            if omega_measure == 0.0:
                continue

            for cpsi, wc in zip(c_nodes, c_weights):
                cpsi = float(cpsi)
                flux_velocity = 1.0 - beta_mu * cpsi
                e_star = gamma_mu * omega * flux_velocity
                if e_star <= threshold:
                    continue

                # Angle between the medium-frame time direction's spatial
                # part in the muon rest frame and the incoming photon in that
                # frame; useful for checking the boost geometry. The CM
                # implementation below uses the exact four-vector transform.
                invariant_s = m*m + 2.0*m*e_star
                u_cm = medium_four_velocity_in_amplitude_cm(
                    e_mu, float(omega), float(p), cpsi, invariant_s
                )

                initial_muon_mu = muon_chemical_potential_mev
                initial_muon_plus = -muon_chemical_potential_mev
                f_minus = fermi_dirac(e_mu, T, initial_muon_mu)
                f_plus = fermi_dirac(e_mu, T, initial_muon_plus)
                if f_minus == 0.0 and f_plus == 0.0:
                    continue

                blocked_sigma = 0.0
                energy_weighted_sigma = 0.0
                for ctheta, wtheta in zip(theta_nodes, theta_weights):
                    ctheta = float(ctheta)
                    dsigma_domega = sc.differential_cross_section_cm(
                        e_star, ma, ctheta, g_v, g_a, mode="all"
                    )
                    if dsigma_domega == 0.0:
                        continue
                    _, _, _, q_phi0 = sc.cm_kinematics(
                        e_star, ma, ctheta, 0.0
                    )
                    # CM q energy/momentum and p' energy/momentum do not
                    # depend on azimuth; only their projections on U_CM do.
                    phi_block_sum = 0.0
                    phi_energy_sum = 0.0
                    for phi in phi_values:
                        _, _, p_prime, q = sc.cm_kinematics(
                            e_star, ma, ctheta, float(phi)
                        )
                        e_q_medium = minkowski_dot(q, u_cm)
                        e_prime_medium = minkowski_dot(p_prime, u_cm)
                        # Tiny negative roundoff is not physical.
                        e_q_medium = max(e_q_medium, ma)
                        e_prime_medium = max(e_prime_medium, m)
                        block_minus = 1.0 - fermi_dirac(
                            e_prime_medium, T, initial_muon_mu
                        )
                        block_plus = 1.0 - fermi_dirac(
                            e_prime_medium, T, initial_muon_plus
                        )
                        phi_block_sum += phi_weight * (
                            f_minus * block_minus + f_plus * block_plus
                        )
                        phi_energy_sum += phi_weight * e_q_medium * (
                            f_minus * block_minus + f_plus * block_plus
                        )

                    blocked_sigma += float(wtheta) * dsigma_domega * phi_block_sum
                    energy_weighted_sigma += (
                        float(wtheta) * dsigma_domega * phi_energy_sum
                    )

                initial_weight = (
                    p_measure * omega_measure * float(wc)
                    * flux_velocity
                )
                event_integral += initial_weight * blocked_sigma
                energy_integral += initial_weight * energy_weighted_sigma

    return ThermalResult(
        event_rate_mev4=common_prefactor * event_integral,
        emissivity_mev5=common_prefactor * energy_integral,
        p_max_mev=float(p_max_mev),
        photon_max_mev=float(photon_max_mev),
        quadrature_order=order,
        phi_order=phi_order,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--temperature", type=float, default=30.0,
                        help="medium temperature in MeV")
    parser.add_argument("--muon-chemical-potential", type=float, default=0.0,
                        help="total mu^- chemical potential in MeV")
    parser.add_argument("--mass", type=float, default=1.0,
                        help="A' mass in MeV")
    parser.add_argument("--g-v", type=float, default=0.0,
                        help="vector A'-muon coupling")
    parser.add_argument("--g-a", type=float, default=1.0,
                        help="axial A'-muon coupling")
    parser.add_argument("--order", type=int, default=8,
                        help="Gauss-Legendre order for p, omega, cos(psi), cos(theta)")
    parser.add_argument("--phi-order", type=int, default=None,
                        help="uniform azimuthal quadrature order")
    parser.add_argument("--p-max", type=float, default=None,
                        help="optional muon momentum cutoff in MeV")
    parser.add_argument("--photon-max", type=float, default=None,
                        help="optional photon energy cutoff in MeV")
    args = parser.parse_args()

    result = thermal_emissivity(
        args.temperature, args.muon_chemical_potential, args.mass,
        args.g_v, args.g_a, args.order, args.phi_order,
        args.p_max, args.photon_max
    )
    print("quantity,value,unit")
    print(f"event_rate_density,{result.event_rate_mev4:.10e},MeV^4")
    print(f"energy_emissivity,{result.emissivity_mev5:.10e},MeV^5")
    print(f"p_max,{result.p_max_mev:.8g},MeV")
    print(f"photon_max,{result.photon_max_mev:.8g},MeV")
    print(f"quadrature_order,{result.quadrature_order},dimensionless")
    print(f"phi_order,{result.phi_order},dimensionless")


if __name__ == "__main__":
    main()
