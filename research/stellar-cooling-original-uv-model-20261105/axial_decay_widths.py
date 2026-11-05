#!/usr/bin/env python3
"""Analytic decay-width checks for the original axial L_mu-L_tau model.

This script computes tree-level A' -> nu nubar and A' -> mu+ mu- widths
for the pure-vector and pure-axial benchmarks, plus the finite right-mixing
formula used in the original paper. The invisible width includes only the
original active-flavor nu_mu and nu_tau gauge-current channels, with their
opposite L_mu-L_tau charges and massless-neutrino kinematics; the electron
flavor is uncoupled. No extra neutrino states or neutrino-mass completion are
introduced. It does not calculate supernova luminosities or exclusion
contours. Its widths depend on physical (m_A', g_X); the original UV map is
provided by single_vev_axial_mapping.py.
"""

from math import cos, sin, sqrt

M_MU_MEV = 105.6583755


def beta_mu(m_a_mev: float) -> float:
    if m_a_mev <= 2.0 * M_MU_MEV:
        return 0.0
    return sqrt(1.0 - 4.0 * (M_MU_MEV / m_a_mev) ** 2)


def vector_muon_width_factor(m_a_mev: float) -> float:
    """Gamma_V(mumu) / [g_X^2 m_A / (12 pi)]."""
    if m_a_mev <= 2.0 * M_MU_MEV:
        return 0.0
    r = (M_MU_MEV / m_a_mev) ** 2
    return (1.0 + 2.0 * r) * beta_mu(m_a_mev)


def axial_muon_width_factor(m_a_mev: float) -> float:
    """Gamma_A(mumu) / [g_X^2 m_A / (12 pi)]."""
    if m_a_mev <= 2.0 * M_MU_MEV:
        return 0.0
    return beta_mu(m_a_mev) ** 3


def mixed_muon_width_factor(m_a_mev: float, theta_mu_r: float) -> float:
    """Finite-mixing width factor with gV=gX sin^2(theta), gA=-gX cos^2(theta)."""
    if m_a_mev <= 2.0 * M_MU_MEV:
        return 0.0
    r = (M_MU_MEV / m_a_mev) ** 2
    beta = beta_mu(m_a_mev)
    return beta * (
        sin(theta_mu_r) ** 4 * (1.0 + 2.0 * r)
        + cos(theta_mu_r) ** 4 * (1.0 - 4.0 * r)
    )


def axial_to_vector_width_ratio(m_a_mev: float) -> float:
    """Pure-axial / pure-vector muon partial-width ratio."""
    if m_a_mev <= 2.0 * M_MU_MEV:
        return float("nan")
    r = (M_MU_MEV / m_a_mev) ** 2
    return (1.0 - 4.0 * r) / (1.0 + 2.0 * r)


def neutrino_branching_fractions(m_a_mev: float) -> tuple[float, float]:
    """Return (BR_nunu_vector, BR_nunu_axial).

    Assumptions: only the original model's two massless active flavor
    channels nu_mu and nu_tau are included, with U(1)_X charges +1 and -1;
    nu_e is uncoupled. Their inclusive current trace is
    sum_alpha |q_alpha|^2 = 2. Only these invisible channels plus mu+mu-
    are retained. Below dimuon threshold BR_nunu=1 under these assumptions.
    This is not a neutrino-mass or additional-state calculation.
    """
    if m_a_mev <= 2.0 * M_MU_MEV:
        return 1.0, 1.0
    v_factor = vector_muon_width_factor(m_a_mev)
    a_factor = axial_muon_width_factor(m_a_mev)
    return 1.0 / (1.0 + v_factor), 1.0 / (1.0 + a_factor)


def main() -> None:
    masses = (220.0, 250.0, 300.0, 600.0)
    print("mA_MeV,beta_mu,GammaA_over_GammaV,BRnu_vector,BRnu_axial")
    for mass in masses:
        br_v, br_a = neutrino_branching_fractions(mass)
        print(
            f"{mass:.1f},{beta_mu(mass):.6f},"
            f"{axial_to_vector_width_ratio(mass):.6f},"
            f"{br_v:.6f},{br_a:.6f}"
        )

    # Basic analytic checks.
    assert beta_mu(2.0 * M_MU_MEV) == 0.0
    assert abs(axial_to_vector_width_ratio(220.0) - 0.053) < 0.002
    assert abs(neutrino_branching_fractions(220.0)[1] - 0.979) < 0.002
    assert abs(mixed_muon_width_factor(300.0, 0.0) - axial_muon_width_factor(300.0)) < 1e-12
    assert axial_to_vector_width_ratio(600.0) > axial_to_vector_width_ratio(300.0)
    print("checks=PASS")


if __name__ == "__main__":
    main()
