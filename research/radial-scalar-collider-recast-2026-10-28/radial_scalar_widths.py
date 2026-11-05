"""Partial-width calculator scaffold for the original paper's UV radial scalar.

Model scope: the original one-VEV field content, with m_A_prime = 2 g_X v_s.
This module is not a calculator for an extended scalar sector.

This module computes only the explicitly listed muon, tau, and A' A' channels
plus caller-supplied extra widths. It does not by itself establish a collider
exclusion. Unless all_channels_included=True is explicitly supplied, the
normalized fractions are fractions among included channels only and the
proper decay length is deliberately left undefined.
"""
from __future__ import annotations

from math import pi, sqrt
from typing import Mapping, Optional

M_MU_GEV = 0.1056583755
M_TAU_GEV = 1.77686
HBAR_C_GEV_M = 1.973269804e-16


def fermion_pair_width(ms_GeV: float, y_sff: float, mf_GeV: float) -> float:
    """Tree-level width for a CP-even scalar with L_int = -y s fbar f."""
    if ms_GeV <= 0 or mf_GeV < 0:
        raise ValueError("ms_GeV must be positive and mf_GeV non-negative")
    if ms_GeV <= 2.0 * mf_GeV:
        return 0.0
    beta2 = 1.0 - 4.0 * mf_GeV**2 / ms_GeV**2
    return abs(y_sff) ** 2 * ms_GeV / (8.0 * pi) * beta2 ** 1.5


def vector_pair_width(ms_GeV: float, mA_GeV: float, vs_GeV: float) -> float:
    """Width s -> A' A' for the canonical radial-mode normalization.

    Assumes m_A' = 2 g_X v_s and the coupling obtained by expanding
    |D_mu S|^2 with S=(v_s+s)/sqrt(2). The threshold is strict: ms > 2 mA.
    """
    if ms_GeV <= 0 or mA_GeV <= 0 or vs_GeV <= 0:
        raise ValueError("ms_GeV, mA_GeV, and vs_GeV must be positive")
    if ms_GeV <= 2.0 * mA_GeV:
        return 0.0
    r = (mA_GeV / ms_GeV) ** 2
    beta = sqrt(1.0 - 4.0 * r)
    return (
        ms_GeV**3
        / (32.0 * pi * vs_GeV**2)
        * beta
        * (1.0 - 4.0 * r + 12.0 * r**2)
    )


def evaluate_point(
    ms_GeV: float,
    mA_GeV: float,
    gX: float,
    *,
    y_smu: Optional[float] = None,
    y_stau: Optional[float] = None,
    additional_widths_GeV: Optional[Mapping[str, float]] = None,
    all_channels_included: bool = False,
    lambdaS_max: float = 4.0 * pi,
) -> dict:
    """Evaluate a benchmark's known partial widths and perturbativity check.

    If Yukawas are omitted, the mass-proportional benchmark y_sll=m_l/v_s is
    used. Exact mass-eigenstate Yukawas can instead be passed explicitly.

    all_channels_included is a caller assertion, not an automatic check.
    Set it True only after every kinematically open channel has been included.
    """
    if ms_GeV <= 0 or mA_GeV <= 0 or gX <= 0 or lambdaS_max <= 0:
        raise ValueError("masses, gX, and lambdaS_max must be positive")
    vs_GeV = mA_GeV / (2.0 * gX)
    ymu = M_MU_GEV / vs_GeV if y_smu is None else float(y_smu)
    ytau = M_TAU_GEV / vs_GeV if y_stau is None else float(y_stau)

    widths = {
        "mu_mu": fermion_pair_width(ms_GeV, ymu, M_MU_GEV),
        "tau_tau": fermion_pair_width(ms_GeV, ytau, M_TAU_GEV),
        "Aprime_Aprime": vector_pair_width(ms_GeV, mA_GeV, vs_GeV),
    }
    for name, width in (additional_widths_GeV or {}).items():
        if width < 0:
            raise ValueError(f"additional width {name!r} must be non-negative")
        if name in widths:
            raise ValueError(f"additional width name {name!r} duplicates a built-in channel")
        widths[name] = float(width)

    total_known_width = sum(widths.values())
    fractions_among_included = (
        {name: width / total_known_width for name, width in widths.items()}
        if total_known_width > 0
        else {}
    )
    lambdaS = ms_GeV**2 / (2.0 * vs_GeV**2)
    complete = bool(all_channels_included)
    ctau_m = HBAR_C_GEV_M / total_known_width if complete and total_known_width > 0 else None

    return {
        "ms_GeV": ms_GeV,
        "mA_GeV": mA_GeV,
        "gX": gX,
        "vs_GeV": vs_GeV,
        "y_smu": ymu,
        "y_stau": ytau,
        "yukawa_source": "explicit_input" if y_smu is not None or y_stau is not None else "mass_proportional_benchmark",
        "lambdaS": lambdaS,
        "lambdaS_max": lambdaS_max,
        "passes_declared_perturbativity": lambdaS <= lambdaS_max,
        "partial_widths_GeV": widths,
        "sum_of_included_widths_GeV": total_known_width,
        "fractions_among_included_channels": fractions_among_included,
        "branching_fractions_complete": complete,
        "ctau_m": ctau_m,
        "status": (
            "caller_asserts_all_open_channels_included"
            if complete
            else "partial_widths_only_no_exclusion_claim"
        ),
    }
