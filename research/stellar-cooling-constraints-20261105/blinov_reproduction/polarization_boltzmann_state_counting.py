"""State-counting identities for polarization-resolved Boltzmann transport.

All rates are per physical polarization unless the caller explicitly sums them.
This module is algebraic support for the P0 audit; it is not a stellar-rate solver.
"""
from __future__ import annotations

from math import exp, expm1
from typing import Sequence


def _check_modes(*arrays: Sequence[float]) -> int:
    if not arrays or not arrays[0]:
        raise ValueError("at least one polarization mode is required")
    n = len(arrays[0])
    if any(len(a) != n for a in arrays):
        raise ValueError("all mode arrays must have equal length")
    return n


def _check_nonnegative(*arrays: Sequence[float]) -> None:
    if any(x < 0.0 for array in arrays for x in array):
        raise ValueError("rates, occupations, sources and optical depths must be non-negative")


def mode_collision_terms(
    gamma_prod: Sequence[float],
    gamma_abs: Sequence[float],
    occupations: Sequence[float],
) -> tuple[float, ...]:
    """Return C_h = Gamma_prod,h (1+f_h) - Gamma_abs,h f_h."""
    _check_modes(gamma_prod, gamma_abs, occupations)
    _check_nonnegative(gamma_prod, gamma_abs, occupations)
    return tuple(
        p * (1.0 + f) - a * f
        for p, a, f in zip(gamma_prod, gamma_abs, occupations)
    )


def unpolarized_total_collision(
    gamma_prod: Sequence[float],
    gamma_abs: Sequence[float],
    total_occupation: float,
) -> float:
    """Sum the mode collision terms under f_h = F/N_modes."""
    _check_modes(gamma_prod, gamma_abs)
    _check_nonnegative(gamma_prod, gamma_abs)
    if total_occupation < 0.0:
        raise ValueError("total occupation must be non-negative")
    f = total_occupation / len(gamma_prod)
    return sum(
        p * (1.0 + f) - a * f
        for p, a in zip(gamma_prod, gamma_abs)
    )


def effective_absorption_rate(
    gamma_abs: Sequence[float],
    occupations: Sequence[float],
) -> float:
    """Return sum_h Gamma_abs,h f_h / sum_h f_h."""
    _check_modes(gamma_abs, occupations)
    _check_nonnegative(gamma_abs, occupations)
    total_f = sum(occupations)
    if total_f <= 0.0:
        raise ValueError("total occupation must be positive")
    return sum(a * f for a, f in zip(gamma_abs, occupations)) / total_f


def reduced_absorption_rates(
    gamma_abs: Sequence[float],
    omega_over_temperature: float,
) -> tuple[float, ...]:
    """Return (1-exp(-omega/T))*Gamma_abs,h, stably evaluated."""
    _check_modes(gamma_abs)
    _check_nonnegative(gamma_abs)
    if omega_over_temperature < 0.0:
        raise ValueError("omega/T must be non-negative")
    factor = -expm1(-omega_over_temperature)
    return tuple(factor * a for a in gamma_abs)


def mode_escape_luminosity(
    source: Sequence[float],
    optical_depth: Sequence[float],
) -> float:
    """Return sum_h Q_h exp(-tau_h)."""
    _check_modes(source, optical_depth)
    _check_nonnegative(source, optical_depth)
    return sum(q * exp(-tau) for q, tau in zip(source, optical_depth))


def scalar_escape_sum_opacity(
    source: Sequence[float],
    optical_depth: Sequence[float],
) -> float:
    """Return (sum_h Q_h) exp(-sum_h tau_h), the literal sum-opacity form."""
    _check_modes(source, optical_depth)
    _check_nonnegative(source, optical_depth)
    return sum(source) * exp(-sum(optical_depth))


def scalar_escape_average_opacity(
    source: Sequence[float],
    optical_depth: Sequence[float],
) -> float:
    """Return (sum_h Q_h) exp(-mean_h tau_h), an equal-population scalar closure."""
    _check_modes(source, optical_depth)
    _check_nonnegative(source, optical_depth)
    return sum(source) * exp(-sum(optical_depth) / len(optical_depth))
