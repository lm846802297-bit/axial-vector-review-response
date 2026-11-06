#!/usr/bin/env python3
"""Exact single-VEV map for the original paper's U(1)_{L_mu-L_tau} UV model.

Conventions:
    S = (v_s + s + i a_s) / sqrt(2),  Q_X(S) = +2
    D_mu = partial_mu - i g_X Q_X A'_mu

The gauge-boson mass and eaten Goldstone are
    m_A' = 2 |g_X| v_s
    G = a_s

There is only one CP-odd phase from S, and it is entirely eaten. In the
small-VLL-mixing, mass-proportional charged-lepton benchmark,
    g_Gll = m_l / v_s
which agrees with the longitudinal-current relation
    2 |g_A^l| m_l / m_A'
when |g_A^l| = |g_X|.

This module describes the original paper's field content only. It does not
introduce another scalar or a modified symmetry-breaking sector.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class SingleVEVPoint:
    v_s: float
    g_x: float

    def __post_init__(self) -> None:
        if not math.isfinite(self.v_s) or not math.isfinite(self.g_x):
            raise ValueError("all inputs must be finite")
        if self.v_s <= 0.0 or self.g_x == 0.0:
            raise ValueError("require v_s > 0 and nonzero g_x")

    @property
    def m_a(self) -> float:
        return 2.0 * abs(self.g_x) * self.v_s

    @property
    def goldstone_s_projection(self) -> float:
        return 1.0

    def goldstone_lepton_yukawa(self, m_l: float) -> float:
        if not math.isfinite(m_l) or m_l < 0.0:
            raise ValueError("m_l must be finite and non-negative")
        return m_l / self.v_s

    def longitudinal_current_yukawa(self, m_l: float, g_a: float | None = None) -> float:
        if not math.isfinite(m_l) or m_l < 0.0:
            raise ValueError("m_l must be finite and non-negative")
        coupling = abs(self.g_x if g_a is None else g_a)
        return 2.0 * coupling * m_l / self.m_a

    @classmethod
    def from_mediator_inputs(cls, m_a: float, g_x: float) -> "SingleVEVPoint":
        if not math.isfinite(m_a) or not math.isfinite(g_x):
            raise ValueError("all inputs must be finite")
        if m_a <= 0.0 or g_x == 0.0:
            raise ValueError("require m_A' > 0 and nonzero g_x")
        return cls(v_s=m_a / (2.0 * abs(g_x)), g_x=g_x)


def eaten_goldstone(a_s: float) -> float:
    """Return the canonically normalized phase; the sole phase is eaten."""
    if not math.isfinite(a_s):
        raise ValueError("a_s must be finite")
    return a_s
