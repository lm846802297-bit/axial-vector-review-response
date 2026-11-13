#!/usr/bin/env python3
"""Analytic decay-width checks for the axial L_mu-L_tau stellar-cooling study.

This script computes tree-level A' -> nu nubar and A' -> mu+ mu- widths
for the pure-vector and pure-axial benchmarks, plus the finite right-mixing
formula used in the manuscript. The neutrino width is the inclusive light-
neutrino trace result for a unitary three-flavour PMNS rotation; heavy-neutrino
final states are assumed closed and are not included. It does not calculate supernova luminosities
or exclusion contours. Its widths depend on physical (m_A', g_X), not on a
choice of scalar VEV parameterization; use two_vev_axial_mapping.py for the
current UV-to-axial-current/Goldstone mapping.
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

    Assumptions: the inclusive width into all three effectively massless
    light-neutrino mass eigenstates is normalized by
    Tr(G_nu^dagger G_nu)=2, as for two unmixed massless L_mu-L_tau flavours.
    The corresponding one-active-chirality normalization is
    Gamma_nu = g_X^2 m_A'/(24 pi) Tr(G_nu^dagger G_nu), giving
    g_X^2 m_A'/(12 pi) when the trace is 2. The PMNS rotation is unitary,
    active-heavy mixing is negligible, all heavy-neutrino channels are
    kinematically closed, and only light-nu-nu plus mu+mu- final states are
    retained. Below dimuon threshold BR_nunu=1 under these assumptions.
    Majorana-state identical-particle factors or independent right-handed
    currents require a full mass-basis width calculation. If a heavy-neutrino
    threshold opens, or active-heavy mixing is non-negligible, extend the
    total width before using these branching fractions.
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
