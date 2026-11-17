#!/usr/bin/env python3
"""Full charged-lepton/VLL mass matrix and kappa-induced LFV current diagnostic.

Dependencies: Python 3 and NumPy.

This script:
  * builds the most general renormalizable 5x5 mass matrix for the charge
    assignments documented in the accompanying research note;
  * performs a full SVD and computes mass-basis X currents;
  * compares exact SVD currents to leading-order kappa-only estimates.

The default point is a diagnostic benchmark, NOT a fit or an experimentally
allowed point. Gauge-allowed off-diagonal entries other than kappa are set to
zero by an explicit texture assumption in this benchmark, not by U(1)_X.

See:
../../审稿意见-gpt/当前执行/带电轻子VLL完整质量矩阵与LFV一阶分析_2026-10-27.md
"""

from __future__ import annotations

import json
import math
from typing import Any

import numpy as np


def complex_matrix_json(matrix: np.ndarray) -> list[list[dict[str, float]]]:
    return [
        [{"re": float(z.real), "im": float(z.imag)} for z in row]
        for row in matrix
    ]


def build_mass_matrix(p: dict[str, complex | float]) -> np.ndarray:
    """Rows (eL, muL, tauL, E_muL, E_tauL), columns (eR, muR, tauR, E_muR, E_tauR).

    Gauge-allowed off-diagonal parameters are included explicitly:
      m_mutau, m_taumu: direct Higgs Yukawa mass entries;
      B_mutau, B_taumu: bare E_L--opposite-flavour right-handed masses;
      r_mutau, r_taumu: S-mediated off-diagonal VLL masses.
    """
    return np.array(
        [
            [p["m_e"], 0, 0, 0, 0],
            [0, 0, p["m_mutau"], p["m_Lmu"], 0],
            [0, p["m_taumu"], 0, 0, p["m_Ltau"]],
            [
                p["delta_mu"],
                p["B_mutau"],
                p["m_Rmu"],
                p["M_mu"],
                p["r_mutau"],
            ],
            [
                p["delta_tau"],
                p["B_taumu"],
                p["m_Rtau"],
                p["r_taumu"],
                p["M_tau"],
            ],
        ],
        dtype=complex,
    )


def sorted_svd_and_currents(
    mass_matrix: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    """Return ascending singular values, U_L, U_R, X currents, and SVD residual."""
    u_left, singular_values, vh_right = np.linalg.svd(mass_matrix)
    order = np.argsort(singular_values)
    u_left = u_left[:, order]
    u_right = vh_right.conj().T[:, order]
    singular_values = singular_values[order]

    x_left = np.diag([0.0, +1.0, -1.0, +1.0, -1.0])
    x_right = np.diag([0.0, -1.0, +1.0, +1.0, -1.0])

    g_left_over_gx = u_left.conj().T @ x_left @ u_left
    g_right_over_gx = u_right.conj().T @ x_right @ u_right
    diagonal = np.diag(singular_values)
    residual = float(
        np.linalg.norm(u_left.conj().T @ mass_matrix @ u_right - diagonal)
        / max(np.linalg.norm(mass_matrix), 1.0)
    )
    return (
        singular_values,
        u_left,
        u_right,
        g_left_over_gx,
        g_right_over_gx,
        residual,
    )


def main() -> None:
    # Standard Model charged-lepton masses in GeV.
    m_e = 0.00051099895
    m_mu = 0.1056583755
    m_tau = 1.77686

    # Explicit illustrative benchmark, not a fit.
    v_s = 10.0
    v_sigma = 1.0
    m_heavy_mu = 1.0e4
    m_heavy_tau = 1.8e4
    m_l_mu = 100.0
    m_l_tau = 100.0
    kappa_mu = 1.0e-5
    kappa_tau = 1.0e-5

    # Leading universal-seesaw choices m_R ~= m_l M_E / m_L.
    m_r_mu = m_mu * m_heavy_mu / m_l_mu
    m_r_tau = m_tau * m_heavy_tau / m_l_tau
    delta_mu = kappa_mu * v_sigma / math.sqrt(2.0)
    delta_tau = kappa_tau * v_sigma / math.sqrt(2.0)

    # All other gauge-allowed cross entries are explicitly set to zero here.
    # U(1)_X alone does not protect these zeros.
    p: dict[str, complex | float] = {
        "m_e": m_e,
        "m_mutau": 0.0,
        "m_taumu": 0.0,
        "m_Lmu": m_l_mu,
        "m_Ltau": m_l_tau,
        "delta_mu": delta_mu,
        "delta_tau": delta_tau,
        "B_mutau": 0.0,
        "B_taumu": 0.0,
        "m_Rmu": m_r_mu,
        "m_Rtau": m_r_tau,
        "M_mu": m_heavy_mu,
        "M_tau": m_heavy_tau,
        "r_mutau": 0.0,
        "r_taumu": 0.0,
    }

    mass_matrix = build_mass_matrix(p)
    (
        masses,
        u_left,
        u_right,
        g_left,
        g_right,
        svd_residual,
    ) = sorted_svd_and_currents(mass_matrix)

    # The first three singular states are identified as e, mu, tau only for
    # this chosen benchmark. For a general scan, identify them by SM-flavour
    # overlaps rather than assuming mass ordering alone.
    light_g_left = g_left[:3, :3]
    light_g_right = g_right[:3, :3]

    theta_r_emu_approx = abs(delta_mu / m_r_mu)
    theta_r_etau_approx = abs(delta_tau / m_r_tau)
    theta_r_emu_exact = abs(light_g_right[0, 1])
    theta_r_etau_exact = abs(light_g_right[0, 2])
    theta_l_emu_exact = abs(light_g_left[0, 1])
    theta_l_etau_exact = abs(light_g_left[0, 2])

    # Verify SVD conventions and the leading-order kappa-only relations.
    assert svd_residual < 1.0e-12, f"SVD residual too large: {svd_residual}"
    assert np.isclose(
        theta_r_emu_exact, theta_r_emu_approx, rtol=5.0e-3, atol=1.0e-14
    ), (theta_r_emu_exact, theta_r_emu_approx)
    assert np.isclose(
        theta_r_etau_exact, theta_r_etau_approx, rtol=5.0e-3, atol=1.0e-14
    ), (theta_r_etau_exact, theta_r_etau_approx)

    results: dict[str, Any] = {
        "status": "diagnostic benchmark; not a fit and not an exclusion result",
        "VEVs_GeV": {"vS": v_s, "vSigma": v_sigma},
        "benchmark": {
            "M_E_mu_GeV": m_heavy_mu,
            "M_E_tau_GeV": m_heavy_tau,
            "m_Lmu_GeV": m_l_mu,
            "m_Ltau_GeV": m_l_tau,
            "kappa_mu": kappa_mu,
            "kappa_tau": kappa_tau,
            "m_Rmu_GeV": m_r_mu,
            "m_Rtau_GeV": m_r_tau,
            "delta_mu_GeV": delta_mu,
            "delta_tau_GeV": delta_tau,
        },
        "texture_assumption": (
            "m_mutau=m_taumu=B_mutau=B_taumu=r_mutau=r_taumu=0; "
            "these entries are gauge-allowed and are not protected by U(1)_X alone"
        ),
        "mass_eigenvalues_ascending_GeV": masses.tolist(),
        "mass_matrix_GeV": complex_matrix_json(mass_matrix),
        "SVD_relative_residual": svd_residual,
        "light_mass_basis_G_left_over_gX": complex_matrix_json(light_g_left),
        "light_mass_basis_G_right_over_gX": complex_matrix_json(light_g_right),
        "off_diagonal_currents_over_gX": {
            "abs_G_R_e_mu": theta_r_emu_exact,
            "abs_G_R_e_tau": theta_r_etau_exact,
            "abs_G_L_e_mu": theta_l_emu_exact,
            "abs_G_L_e_tau": theta_l_etau_exact,
        },
        "leading_order_estimates": {
            "abs_delta_mu_over_mRmu": theta_r_emu_approx,
            "abs_delta_tau_over_mRtau": theta_r_etau_approx,
            "expected_thetaL_e_mu": (m_e / m_mu) * theta_r_emu_approx,
            "expected_thetaL_e_tau": (m_e / m_tau) * theta_r_etau_approx,
        },
        "interpretation": (
            "Current entries are normalized to gX. To obtain physical couplings, "
            "multiply by gX. No branching ratios are calculated. In particular, "
            "mu->3e and mu-e conversion require the diagonal electron and quark "
            "currents, including kinetic mixing; loop rates require a separate "
            "model-specific calculation."
        ),
    }
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
