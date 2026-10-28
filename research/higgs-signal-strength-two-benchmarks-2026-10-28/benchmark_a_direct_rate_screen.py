#!/usr/bin/env python3
"""Conservative direct-production rate screen for Benchmark A.

This is not an experimental recast. It asks whether a Higgs-mixing-induced
production rate could plausibly approach the ATLAS low-mass S -> Zd Zd -> 4l
sensitivity scale, while explicitly not transferring that limit to m_A'=10 GeV
because the ATLAS selection requires every dilepton pairing to exceed 11.105 GeV
and its generated Zd masses start at 15 GeV.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import hypot

M_H_GEV = 125.25
PI_HS_REAL_GEV2 = -0.4133
PI_HS_IMAG_GEV2 = -0.1132

# Conservative envelope above the SM ggF cross section across 65--110 GeV.
# 100 pb = 100,000 fb. This intentionally overestimates the production rate.
SIGMA_GGF_SM_UPPER_PB = 100.0
ATLAS_LOW_MASS_GLOBAL_MIN_LIMIT_FB = 0.14
BR_APRIME_TO_MUMU_PROXY = 1.0 / 3.0


@dataclass(frozen=True)
class ScreenRow:
    m_s_GeV: float
    epsilon_nd: float
    sigma_production_upper_fb: float
    sigma_4mu_upper_fb: float
    ratio_min_limit_to_inclusive_rate: float
    ratio_min_limit_to_4mu_rate: float


def screen_point(m_s_GeV: float) -> ScreenRow:
    """Compute a fixed-self-energy non-degenerate proxy; never an exclusion."""
    if m_s_GeV <= 0:
        raise ValueError("m_s_GeV must be positive")
    delta_m2 = abs(M_H_GEV**2 - m_s_GeV**2)
    if delta_m2 == 0:
        raise ValueError("The non-degenerate proxy is undefined at m_s = m_h")

    pi_abs = hypot(PI_HS_REAL_GEV2, PI_HS_IMAG_GEV2)
    epsilon = pi_abs / delta_m2
    sigma_upper_fb = epsilon**2 * SIGMA_GGF_SM_UPPER_PB * 1000.0
    # BR(s -> A'A') <= 1; the 4mu estimate uses the tree-level L_mu-L_tau
    # BR(A' -> mu+mu-) ~= 1/3 and neglects loop-induced electron channels.
    sigma_4mu_upper_fb = sigma_upper_fb * BR_APRIME_TO_MUMU_PROXY**2
    return ScreenRow(
        m_s_GeV=m_s_GeV,
        epsilon_nd=epsilon,
        sigma_production_upper_fb=sigma_upper_fb,
        sigma_4mu_upper_fb=sigma_4mu_upper_fb,
        ratio_min_limit_to_inclusive_rate=(
            ATLAS_LOW_MASS_GLOBAL_MIN_LIMIT_FB / sigma_upper_fb
        ),
        ratio_min_limit_to_4mu_rate=(
            ATLAS_LOW_MASS_GLOBAL_MIN_LIMIT_FB / sigma_4mu_upper_fb
        ),
    )


def main() -> None:
    print(
        "m_s_GeV,epsilon_nd,sigma_prod_upper_fb,"
        "sigma_4mu_upper_fb,min_limit_over_prod,min_limit_over_4mu"
    )
    for mass in (65.0, 80.0, 100.0, 110.0):
        r = screen_point(mass)
        print(
            f"{r.m_s_GeV:.1f},{r.epsilon_nd:.8e},"
            f"{r.sigma_production_upper_fb:.8e},"
            f"{r.sigma_4mu_upper_fb:.8e},"
            f"{r.ratio_min_limit_to_inclusive_rate:.4g},"
            f"{r.ratio_min_limit_to_4mu_rate:.4g}"
        )
    print(
        "CAVEAT: the 0.14 fb value is the global minimum published in a different "
        "daughter-mass region (m_Zd >= 15 GeV); it is a sensitivity scale only, "
        "not a transferred limit at m_A'=10 GeV."
    )


if __name__ == "__main__":
    main()
