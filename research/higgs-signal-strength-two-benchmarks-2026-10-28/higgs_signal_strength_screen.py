#!/usr/bin/env python3
"""Non-degenerate Higgs-rate screening proxy for two response-letter benchmarks.

This is not a physical pole-mixing calculation and does not recast an experiment.
It holds the matched one-loop Pi_hs(m_h^2) values fixed, masks near-degenerate
points, and estimates the visible 125 GeV Higgs signal-strength shift only for
m_s >= m_h/2. See higgs-signal-strength-first-pass.md for assumptions.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import cos, pi, sin, sqrt
from typing import Optional

M_H_GEV = 125.25
GAMMA_H_SM_GEV = 4.07e-3
NEAR_DEGENERACY_MASK_GEV = 1.0  # bookkeeping mask only, not a physical exclusion


@dataclass(frozen=True)
class Benchmark:
    name: str
    m_aprime_GeV: float
    gX: float
    vs_GeV: float
    pi_hs_real_GeV2: float
    pi_hs_imag_GeV2: float


BENCHMARKS = (
    Benchmark(
        name="A",
        m_aprime_GeV=10.0,
        gX=0.0705,
        vs_GeV=70.9,
        pi_hs_real_GeV2=-0.4133,
        pi_hs_imag_GeV2=-0.1132,
    ),
    Benchmark(
        name="B",
        m_aprime_GeV=63.0,
        gX=0.1,
        vs_GeV=315.0,
        pi_hs_real_GeV2=-0.09300,
        pi_hs_imag_GeV2=-0.02547,
    ),
)


def gamma_scalar_to_aprime_pair(
    scalar_mass_GeV: float, m_aprime_GeV: float, vs_GeV: float
) -> float:
    """Tree-level radial-scalar width s -> A' A' in the stated normalization."""
    if scalar_mass_GeV <= 0 or m_aprime_GeV <= 0 or vs_GeV <= 0:
        raise ValueError("masses and v_s must be positive")
    if scalar_mass_GeV <= 2.0 * m_aprime_GeV:
        return 0.0
    r = (m_aprime_GeV / scalar_mass_GeV) ** 2
    beta = sqrt(1.0 - 4.0 * r)
    return (
        scalar_mass_GeV**3
        / (32.0 * pi * vs_GeV**2)
        * beta
        * (1.0 - 4.0 * r + 12.0 * r**2)
    )


def screen_point(scalar_mass_GeV: float, benchmark: Benchmark) -> dict:
    """Return a conditional non-degenerate screen, never an exclusion label."""
    if scalar_mass_GeV <= 0:
        raise ValueError("scalar_mass_GeV must be positive")

    result = {
        "benchmark": benchmark.name,
        "m_s_GeV": scalar_mass_GeV,
        "status": "screen_only_not_experimental_classification",
        "mixing_proxy": None,
        "mu_visible_proxy": None,
        "delta_mu_visible_proxy": None,
        "gamma_h_to_aprime_pair_GeV": None,
    }

    if scalar_mass_GeV < M_H_GEV / 2.0:
        result["status"] = "unclassified_h_to_ss_kinematically_open"
        return result

    if abs(scalar_mass_GeV - M_H_GEV) < NEAR_DEGENERACY_MASK_GEV:
        result["status"] = "unclassified_near_degeneracy_requires_pole_solution"
        return result

    pi_abs = sqrt(
        benchmark.pi_hs_real_GeV2**2 + benchmark.pi_hs_imag_GeV2**2
    )
    delta_m2 = abs(M_H_GEV**2 - scalar_mass_GeV**2)
    epsilon = pi_abs / delta_m2

    # This maps a proxy to a small-angle estimate only away from pole overlap.
    theta_proxy = epsilon
    sin2 = sin(theta_proxy) ** 2
    cos2 = 1.0 - sin2

    gamma_aa = gamma_scalar_to_aprime_pair(
        M_H_GEV, benchmark.m_aprime_GeV, benchmark.vs_GeV
    )
    if gamma_aa > 0:
        # h-like state's A'A' width is approximated as sin(theta)^2 times
        # the singlet-like width at m_h. SM partial widths scale as cos^2.
        ratio_new_width = gamma_aa / GAMMA_H_SM_GEV
        mu_visible = cos2**2 / (cos2 + sin2 * ratio_new_width)
    else:
        # Isolated pole, universal mixing rescaling, and no extra Higgs width.
        mu_visible = cos2

    result.update(
        {
            "mixing_proxy": theta_proxy,
            "mu_visible_proxy": mu_visible,
            "delta_mu_visible_proxy": 1.0 - mu_visible,
            "gamma_h_to_aprime_pair_GeV": gamma_aa,
        }
    )
    return result


def main() -> None:
    masses = (65.0, 80.0, 100.0, 120.0, 125.25, 130.0, 150.0)
    header = (
        "benchmark,m_s_GeV,status,mixing_proxy,mu_visible_proxy,"
        "delta_mu_visible_proxy,gamma_h_to_AA_GeV"
    )
    print(header)
    for benchmark in BENCHMARKS:
        for mass in masses:
            r = screen_point(mass, benchmark)
            fields = (
                r["benchmark"],
                f'{r["m_s_GeV"]:.3f}',
                r["status"],
                "" if r["mixing_proxy"] is None else f'{r["mixing_proxy"]:.8e}',
                "" if r["mu_visible_proxy"] is None else f'{r["mu_visible_proxy"]:.12f}',
                "" if r["delta_mu_visible_proxy"] is None else f'{r["delta_mu_visible_proxy"]:.8e}',
                "" if r["gamma_h_to_aprime_pair_GeV"] is None else f'{r["gamma_h_to_aprime_pair_GeV"]:.8e}',
            )
            print(",".join(fields))


if __name__ == "__main__":
    main()
