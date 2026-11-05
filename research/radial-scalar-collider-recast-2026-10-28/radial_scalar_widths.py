"""Leading radial-scalar partial widths in the original one-VEV UV model.

Field content: the original S + VLL model only. No extra scalar VEV,
right-handed neutrinos, or neutrino-sector completion is introduced.

The benchmark uses m_A'=2 g_X v_s and y_sll=m_l/v_s (seesaw-like limit),
with negligible Higgs-portal mixing and decoupled VLLs. Included widths are
mu+mu-, tau+tau-, on-shell A'A', and the leading mu/tau-loop gamma-gamma mode.
The separate off_shell_cascades.py module evaluates one-on-shell/one-virtual
A' three-body modes. This calculator alone does not contain those modes.
"""
from __future__ import annotations

from math import asin, log, pi, sqrt
from typing import Mapping, Optional

M_E_GEV = 0.00051099895
M_MU_GEV = 0.1056583755
M_TAU_GEV = 1.77686
ALPHA_EM = 1.0 / 137.035999084
HBAR_C_GEV_M = 1.973269804e-16
SM_HIGGS_VEV_GEV = 246.0


def leptophilic_scalar_xi_from_vs(vs_GeV: float) -> float:
    if vs_GeV <= 0:
        raise ValueError("vs_GeV must be positive")
    return SM_HIGGS_VEV_GEV / vs_GeV


def rescale_coupling_limit_for_branching_fraction(
    coupling_limit_benchmark: float, br_benchmark: float, br_uv: float,
) -> float:
    if coupling_limit_benchmark <= 0:
        raise ValueError("coupling_limit_benchmark must be positive")
    if not 0.0 < br_benchmark <= 1.0:
        raise ValueError("br_benchmark must lie in (0, 1]")
    if not 0.0 < br_uv <= 1.0:
        raise ValueError("br_uv must lie in (0, 1]")
    return coupling_limit_benchmark * sqrt(br_benchmark / br_uv)


def fermion_pair_width(ms_GeV: float, y_sff: float, mf_GeV: float) -> float:
    """Tree-level width for CP-even s with L_int=-y_sff s fbar f."""
    if ms_GeV <= 0 or mf_GeV < 0:
        raise ValueError("ms_GeV must be positive and mf_GeV non-negative")
    if ms_GeV <= 2.0 * mf_GeV:
        return 0.0
    beta2 = 1.0 - 4.0 * mf_GeV**2 / ms_GeV**2
    return abs(y_sff)**2 * ms_GeV / (8.0 * pi) * beta2**1.5


def vector_pair_width(ms_GeV: float, mA_GeV: float, vs_GeV: float) -> float:
    """Tree-level width s->A'A' for the original canonical radial mode.

    The original paper writes L_int=(m_A'^2/v_s) s A'_mu A'^mu,
    equivalent to g_sAA=2 m_A'^2/v_s in the 1/2 g s A_mu A^mu convention.
    """
    if ms_GeV <= 0 or mA_GeV <= 0 or vs_GeV <= 0:
        raise ValueError("ms_GeV, mA_GeV, and vs_GeV must be positive")
    if ms_GeV <= 2.0 * mA_GeV:
        return 0.0
    r = (mA_GeV / ms_GeV) ** 2
    beta = sqrt(1.0 - 4.0 * r)
    return ms_GeV**3 / (32.0 * pi * vs_GeV**2) * beta * (1.0 - 4.0*r + 12.0*r*r)


def _fermion_loop_form_factor(tau: float) -> complex:
    """CP-even spin-1/2 gamma-gamma form factor; tau=4 m_f^2/m_s^2."""
    if tau <= 0:
        raise ValueError("tau must be positive")
    if tau >= 1.0:
        f = asin(1.0 / sqrt(tau)) ** 2
    else:
        root = sqrt(1.0 - tau)
        log_term = log((1.0 + root) / (1.0 - root))
        f = -0.25 * (log_term - 1j*pi) ** 2
    return 2.0 * tau * (1.0 + (1.0 - tau) * f)


def photon_pair_width_lepton_loops(ms_GeV: float, vs_GeV: float) -> float:
    """Leading one-loop s->gamma gamma from muon and tau loops.

    Uses y_sll=m_l/v_s and the standard CP-even fermion form factor.
    The electron has no direct Yukawa in the original U(1)_{L_mu-L_tau}
    model. Heavy-VLL loop terms are omitted in the decoupling benchmark.
    """
    if ms_GeV <= 0 or vs_GeV <= 0:
        raise ValueError("ms_GeV and vs_GeV must be positive")
    amp = (
        _fermion_loop_form_factor(4.0*M_MU_GEV**2/ms_GeV**2)
        + _fermion_loop_form_factor(4.0*M_TAU_GEV**2/ms_GeV**2)
    )
    return ALPHA_EM**2 * ms_GeV**3 / (256.0*pi**3*vs_GeV**2) * abs(amp)**2


def evaluate_point(
    ms_GeV: float,
    mA_GeV: float,
    gX: float,
    *,
    y_smu: Optional[float] = None,
    y_stau: Optional[float] = None,
    additional_widths_GeV: Optional[Mapping[str, float]] = None,
    all_channels_included: bool = False,
    lambdaS_max: float = 4.0*pi,
) -> dict:
    """Evaluate included widths and model relations at one UV point.

    all_channels_included remains a caller assertion. Do not set it True
    for the Belle-II benchmark until off-shell A'A'^*, portal modes, and any
    relevant VLL-loop contributions have been assessed. The separate
    off_shell_cascades.py module computes the one-on-shell/one-virtual
    three-body modes for m_s/2 <= m_A' < m_s.
    """
    if ms_GeV <= 0 or mA_GeV <= 0 or gX <= 0 or lambdaS_max <= 0:
        raise ValueError("masses, gX, and lambdaS_max must be positive")
    vs = mA_GeV/(2.0*gX)
    ymu = M_MU_GEV/vs if y_smu is None else float(y_smu)
    ytau = M_TAU_GEV/vs if y_stau is None else float(y_stau)
    widths = {
        "mu_mu": fermion_pair_width(ms_GeV, ymu, M_MU_GEV),
        "tau_tau": fermion_pair_width(ms_GeV, ytau, M_TAU_GEV),
        "Aprime_AAprime": vector_pair_width(ms_GeV, mA_GeV, vs),
        "gamma_gamma_lepton_loops": photon_pair_width_lepton_loops(ms_GeV, vs),
    }
    for name, width in (additional_widths_GeV or {}).items():
        if width < 0:
            raise ValueError(f"additional width {name!r} must be non-negative")
        if name in widths:
            raise ValueError(f"additional width name {name!r} duplicates a built-in channel")
        widths[name] = float(width)
    width_sum = sum(widths.values())
    fractions = {k: v/width_sum for k, v in widths.items()} if width_sum > 0 else {}
    lam = ms_GeV**2/(2.0*vs**2)
    complete = bool(all_channels_included)
    return {
        "ms_GeV": ms_GeV, "mA_GeV": mA_GeV, "gX": gX, "vs_GeV": vs,
        "y_smu": ymu, "y_stau": ytau,
        "yukawa_source": "explicit_input" if y_smu is not None or y_stau is not None else "mass_proportional_benchmark",
        "lambdaS": lam, "lambdaS_max": lambdaS_max,
        "passes_declared_perturbativity": lam <= lambdaS_max,
        "partial_widths_GeV": widths,
        "sum_of_included_widths_GeV": width_sum,
        "fractions_among_included_channels": fractions,
        "branching_fractions_complete": complete,
        "ctau_m": HBAR_C_GEV_M/width_sum if complete and width_sum > 0 else None,
        "ctau_upper_bound_from_included_widths_m": HBAR_C_GEV_M/width_sum if width_sum > 0 else None,
        "off_shell_AAprime_channels_included": False,
        "portal_channels_included": False,
        "VLL_loop_in_gamma_gamma": False,
        "status": "caller_asserts_all_open_channels_included" if complete else "included_widths_only_total_width_is_lower_bound",
    }
