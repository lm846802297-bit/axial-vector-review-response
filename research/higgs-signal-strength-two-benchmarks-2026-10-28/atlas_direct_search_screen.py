#!/usr/bin/env python3
"""Conservative ATLAS S -> A'A' -> 4l rate screen for Benchmark B.

This script is an analytic sensitivity-scale check, not a detector-level recast.
It uses the fixed-self-energy non-degenerate proxy at m_s=150 GeV because the
ATLAS paper documents its high-mass signal MC samples starting at that mass.
The exact HEPData Table 15 observed limit near (m_s,m_A')=(150,63) GeV has not
been extracted here; the published global minimum 0.05 fb is used only as a
conservative sensitivity scale, not as a point-specific limit.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt

M_H_GEV = 125.25
M_APRIME_GEV = 63.0
G_X = 0.1
V_S_GEV = 315.0
PI_HS_REAL_GEV2 = -0.09300
PI_HS_IMAG_GEV2 = -0.02547

# Deliberately conservative 13 TeV SM gluon-fusion upper envelope.
SIGMA_GGF_SM_UPPER_FB = 50_000.0  # 50 pb = 50,000 fb
ATLAS_GLOBAL_MIN_OBSERVED_LIMIT_FB = 0.05


@dataclass(frozen=True)
class ScreenResult:
    m_s_GeV: float
    mixing_proxy: float
    mixing_proxy_squared: float
    sigma_production_upper_fb: float
    sigma_4mu_upper_fb: float
    gamma_s_to_aprime_pair_GeV: float
    ratio_to_global_best_limit: float


def gamma_scalar_to_aprime_pair(m_s_GeV: float) -> float:
    """Tree-level width for s -> A'A' in the benchmark normalization."""
    if m_s_GeV <= 2.0 * M_APRIME_GEV:
        return 0.0
    r = (M_APRIME_GEV / m_s_GeV) ** 2
    beta = sqrt(1.0 - 4.0 * r)
    return (
        m_s_GeV**3 / (32.0 * pi * V_S_GEV**2)
        * beta
        * (1.0 - 4.0 * r + 12.0 * r**2)
    )


def screen_point(m_s_GeV: float = 150.0) -> ScreenResult:
    """Return an upper-envelope screen; do not interpret as an exclusion."""
    if m_s_GeV <= 0:
        raise ValueError("m_s_GeV must be positive")
    pi_abs = sqrt(PI_HS_REAL_GEV2**2 + PI_HS_IMAG_GEV2**2)
    delta_m2 = abs(M_H_GEV**2 - m_s_GeV**2)
    if delta_m2 == 0:
        raise ValueError("The non-degenerate proxy is undefined at m_s = m_h")
    epsilon = pi_abs / delta_m2
    sigma_upper = epsilon**2 * SIGMA_GGF_SM_UPPER_FB
    # BR(A' -> mu+mu-) ~= 1/3 for the stated tree-level L_mu-L_tau channels;
    # BR(s -> A'A') <= 1, so sigma(4mu) <= sigma_prod/9.
    return ScreenResult(
        m_s_GeV=m_s_GeV,
        mixing_proxy=epsilon,
        mixing_proxy_squared=epsilon**2,
        sigma_production_upper_fb=sigma_upper,
        sigma_4mu_upper_fb=sigma_upper / 9.0,
        gamma_s_to_aprime_pair_GeV=gamma_scalar_to_aprime_pair(m_s_GeV),
        ratio_to_global_best_limit=ATLAS_GLOBAL_MIN_OBSERVED_LIMIT_FB / sigma_upper,
    )


def main() -> None:
    result = screen_point()
    print("ATLAS S -> A'A' -> 4l conservative screen (not a recast)")
    print(f"m_s = {result.m_s_GeV:.1f} GeV")
    print(f"epsilon_nd = {result.mixing_proxy:.8e}")
    print(f"sigma(gg->s) upper envelope = {result.sigma_production_upper_fb:.8e} fb")
    print(f"sigma(gg->s->4mu) upper envelope = {result.sigma_4mu_upper_fb:.8e} fb")
    print(f"Gamma(s->A'A') = {result.gamma_s_to_aprime_pair_GeV:.8e} GeV")
    print(
        "global-best-limit / production-upper-envelope = "
        f"{result.ratio_to_global_best_limit:.3g}"
    )
    print("No point-specific observed limit or exclusion is returned.")


if __name__ == "__main__":
    main()
