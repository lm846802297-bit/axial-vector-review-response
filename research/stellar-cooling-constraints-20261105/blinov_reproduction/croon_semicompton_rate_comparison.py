"""Controlled comparison of Croon Eq. (4.7) and Blinov et al. 2026 Eq. (B.16).

This module compares only the published non-recoil / nonrelativistic-muon
approximations. It is not the full moving-muon phase-space kernel.

Units: MeV for masses, energies and temperature; natural units hbar=c=kB=1.
The returned rates use the same normalization convention as the cited
equations and are intended for dimensionless equation-level regression tests.
"""
from __future__ import annotations

from math import expm1, isfinite, pi, sqrt

M_MU_MEV = 105.6583755
ALPHA_EM = 1.0 / 137.035999084


def _validate(mv_mev: float, omega_mev: float, temperature_mev: float,
              n_mu: float, f_deg: float, g: float) -> None:
    values = (mv_mev, omega_mev, temperature_mev, n_mu, f_deg, g)
    if not all(isfinite(float(x)) for x in values):
        raise ValueError("all inputs must be finite")
    if mv_mev <= 0.0 or omega_mev <= mv_mev or temperature_mev <= 0.0:
        raise ValueError("require 0 < mV < omega and T > 0")
    if n_mu < 0.0 or f_deg < 0.0 or g < 0.0:
        raise ValueError("n_mu, F_deg and g must be non-negative")


def vector_speed(mv_mev: float, omega_mev: float) -> float:
    if mv_mev <= 0.0 or omega_mev <= mv_mev:
        raise ValueError("require 0 < mV < omega")
    return sqrt(1.0 - (mv_mev / omega_mev) ** 2)


def croon_eq47_rate(mv_mev: float, omega_mev: float, temperature_mev: float,
                    n_mu: float, f_deg: float, g: float,
                    alpha_em: float = ALPHA_EM,
                    m_mu_mev: float = M_MU_MEV) -> float:
    """Croon et al. (2021), Eq. (4.7), literal printed NR/no-recoil rate."""
    _validate(mv_mev, omega_mev, temperature_mev, n_mu, f_deg, g)
    if alpha_em <= 0.0 or m_mu_mev <= 0.0:
        raise ValueError("alpha_em and m_mu must be positive")
    v = vector_speed(mv_mev, omega_mev)
    alpha_v = g * g / (4.0 * pi)
    bose = 1.0 / expm1(omega_mev / temperature_mev)
    prefactor = 8.0 * pi * alpha_em * alpha_v / (3.0 * m_mu_mev**2)
    return prefactor * n_mu * f_deg * bose * v


def blinov_eq_b16_nr_rate(mv_mev: float, omega_mev: float,
                          temperature_mev: float, n_mu: float,
                          f_deg: float, g: float,
                          alpha_em: float = ALPHA_EM,
                          m_mu_mev: float = M_MU_MEV) -> float:
    """Blinov et al. (2026), Eq. (B.16) with the Eq. (B.14) NR cross section."""
    _validate(mv_mev, omega_mev, temperature_mev, n_mu, f_deg, g)
    if alpha_em <= 0.0 or m_mu_mev <= 0.0:
        raise ValueError("alpha_em and m_mu must be positive")
    v = vector_speed(mv_mev, omega_mev)
    alpha_v = g * g / (4.0 * pi)
    bose = 1.0 / expm1(omega_mev / temperature_mev)
    sigma_forward = (
        8.0 * pi * alpha_em * alpha_v / (3.0 * m_mu_mev**2)
        * (1.0 + mv_mev**2 / (2.0 * omega_mev**2)) * v
    )
    return (2.0 / v) * n_mu * f_deg * bose * sigma_forward


def corrected_to_croon_ratio(mv_mev: float, omega_mev: float) -> float:
    """Algebraic ratio implied by Eqs. (4.7), (B.14) and (B.16)."""
    v = vector_speed(mv_mev, omega_mev)
    return 2.0 * (1.0 + mv_mev**2 / (2.0 * omega_mev**2)) / v
