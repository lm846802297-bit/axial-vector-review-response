"""Double-spectral estimate and bound for s -> A'^* A'^* -> 4f.

Original one-VEV S+VLL model only. Restricted to m_A' >= m_s, where both
A' propagators are off shell.

The integrated fermion-current tensors are decomposed into components
transverse and longitudinal to each virtual momentum. The A' propagator is
treated in unitary gauge. The diagonal-pairing contribution is evaluated by
a two-dimensional Gauss-Legendre integral over the physical four-body
invariant-mass triangle.

For identical fermion-pair species, the exchange interference is not
explicitly integrated. A Cauchy-Schwarz upper bound is returned:
Gamma_exact <= Gamma_distinct + 2 Gamma_same, with Gamma_same the diagonal
identical-pair contribution. This is a bound, not a precision exclusive
four-body prediction or detector-level recast.

For m_A' >= m_s the width term in the virtual propagator is numerically
negligible throughout the scan window (checked separately); omitting it makes
the leading result scale exactly as g_X^6 and permits a cached mass-grid scan.
"""
from __future__ import annotations

import math
from functools import lru_cache

import numpy as np

from radial_scalar_widths import M_MU_GEV, M_TAU_GEV


@lru_cache(maxsize=16)
def _legendre_rule(order: int):
    if order < 16:
        raise ValueError("quadrature order must be at least 16")
    return np.polynomial.legendre.leggauss(order)


def _species_spectral_components(s: np.ndarray, gX: float,
                                 theta_mu_R: float,
                                 theta_tau_R: float) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    """Return (H_T,H_L) for nu_mu, nu_tau, mu, tau.

    H_T and H_L include integrated two-body fermion phase space.
    For one massless Weyl neutrino, h_T = 2 g_X^2 s / 3 and h_L = 0.
    """
    s = np.asarray(s, dtype=float)
    result: dict[str, tuple[np.ndarray, np.ndarray]] = {}

    for name in ("nu_mu", "nu_tau"):
        h_t = (2.0 / 3.0) * gX**2 * s
        result[name] = (h_t / (8.0 * math.pi), np.zeros_like(s))

    for name, mf, theta in (
        ("mu", M_MU_GEV, theta_mu_R),
        ("tau", M_TAU_GEV, theta_tau_R),
    ):
        beta = np.sqrt(np.maximum(0.0, 1.0 - 4.0 * mf**2 / np.maximum(s, 1e-300)))
        gV2 = gX**2 * math.sin(theta)**4
        gA2 = gX**2 * math.cos(theta)**4
        h_t = (4.0 / 3.0) * (
            gV2 * (s + 2.0 * mf**2) + gA2 * (s - 4.0 * mf**2)
        )
        h_l = 8.0 * gA2 * mf**2 * np.ones_like(s)
        open_channel = s >= 4.0 * mf**2
        H_t = np.where(open_channel, beta * h_t / (8.0 * math.pi), 0.0)
        H_l = np.where(open_channel, beta * h_l / (8.0 * math.pi), 0.0)
        result[name] = (H_t, H_l)

    return result


def fourbody_spectral_widths(
    ms_GeV: float,
    mA_GeV: float,
    gX: float,
    *,
    quadrature_order: int = 128,
    theta_mu_R: float = 1.0e-2,
    theta_tau_R: float = 1.0e-2,
) -> dict:
    """Evaluate diagonal-pairing s -> A'^*A'^* -> 4f width and a bound.

    Valid for m_A' >= m_s. The returned diagonal-pairing contribution is
    factorized. Identical-species exchange interference is bounded, not
    explicitly calculated.
    """
    if ms_GeV <= 0.0 or mA_GeV <= 0.0 or gX <= 0.0:
        raise ValueError("masses and gX must be positive")
    if mA_GeV < ms_GeV:
        raise ValueError("double-virtual region requires mA_GeV >= ms_GeV")
    if quadrature_order < 16:
        raise ValueError("quadrature_order must be at least 16")

    nodes, weights = _legendre_rule(quadrature_order)
    u = 0.5 * (nodes + 1.0)
    w = 0.5 * weights
    x = u[:, None]
    y = u[None, :]

    # Triangle sqrt(s1)+sqrt(s2)<=ms, with s1=ms^2 x^2,
    # s2=ms^2 (1-x)^2 y^2.
    s1 = ms_GeV**2 * x**2 + np.zeros((quadrature_order, quadrature_order))
    s2 = ms_GeV**2 * (1.0 - x)**2 * y**2 + np.zeros((quadrature_order, quadrature_order))
    jacobian = 4.0 * ms_GeV**4 * x * (1.0 - x)**2 * y
    weight_2d = w[:, None] * w[None, :]

    kallen = np.maximum(
        0.0, (ms_GeV**2 - s1 - s2)**2 - 4.0 * s1 * s2
    )
    sqrt_kallen = np.sqrt(kallen)
    q1_dot_q2 = 0.5 * (ms_GeV**2 - s1 - s2)
    z = q1_dot_q2**2 / np.maximum(s1 * s2, 1e-300)

    # Tensor contractions of P_T(q1), P_L(q1) with P_T(q2), P_L(q2).
    C_TT = 2.0 + z
    C_TL = z - 1.0
    C_LL = z

    # Unit-gauge propagator acts on the longitudinal current component
    # with eigenvalue (1-s/m_A'^2).
    longitudinal_1 = (1.0 - s1 / mA_GeV**2)**2
    longitudinal_2 = (1.0 - s2 / mA_GeV**2)**2

    species_1 = _species_spectral_components(
        s1, gX, theta_mu_R, theta_tau_R
    )
    species_2 = _species_spectral_components(
        s2, gX, theta_mu_R, theta_tau_R
    )

    def contract(a, b):
        Ht1, Hl1 = a
        Ht2, Hl2 = b
        return (
            Ht1 * Ht2 * C_TT
            + Ht1 * (longitudinal_2 * Hl2) * C_TL
            + (longitudinal_1 * Hl1) * Ht2 * C_TL
            + (longitudinal_1 * Hl1) * (longitudinal_2 * Hl2) * C_LL
        )

    total_1 = (
        sum(v[0] for v in species_1.values()),
        sum(v[1] for v in species_1.values()),
    )
    total_2 = (
        sum(v[0] for v in species_2.values()),
        sum(v[1] for v in species_2.values()),
    )
    same_species_contraction = np.zeros((quadrature_order, quadrature_order))
    for name in species_1:
        same_species_contraction += contract(species_1[name], species_2[name])

    # Here s_i<=ms^2<=m_A'^2. The absorptive width term is negligible over
    # the declared scan; dropping it exposes exact g_X^6 scaling.
    denominator_1 = (s1 - mA_GeV**2)**2
    denominator_2 = (s2 - mA_GeV**2)**2
    common = (
        sqrt_kallen * jacobian * weight_2d
        / np.maximum(denominator_1 * denominator_2, 1e-300)
    )

    g_sAA = 2.0 * mA_GeV**2 / (mA_GeV / (2.0 * gX))
    # K_dist is the labeled-vector expression. A factor 1/2 is applied to
    # the inclusive ordered sum because the two virtual A' lines are identical.
    K_dist = g_sAA**2 / (64.0 * math.pi**3 * ms_GeV**3)
    total_diagonal = 0.5 * K_dist * float(
        np.sum(common * contract(total_1, total_2))
    )
    same_species_diagonal = 0.5 * K_dist * float(
        np.sum(common * same_species_contraction)
    )
    distinct_species = max(0.0, total_diagonal - same_species_diagonal)

    # For identical pairs, |M_direct-M_exchange|^2 is bounded by
    # 2(|M_direct|^2+|M_exchange|^2); integrated diagonal terms are equal.
    # Hence exact <= distinct + 2*same_species_diagonal.
    exchange_upper = distinct_species + 2.0 * same_species_diagonal

    return {
        "total_diagonal_pairing_GeV": total_diagonal,
        "same_species_diagonal_GeV": same_species_diagonal,
        "distinct_species_GeV": distinct_species,
        "identical_exchange_cauchy_upper_bound_GeV": exchange_upper,
        "ratio_upper_over_diagonal": (
            exchange_upper / total_diagonal if total_diagonal > 0.0 else 1.0
        ),
        "quadrature_order": quadrature_order,
        "running_width_in_propagator": False,
        "identical_flavor_exchange_explicitly_integrated": False,
        "status": "double_spectral_diagonal_with_identical_exchange_upper_bound",
    }
