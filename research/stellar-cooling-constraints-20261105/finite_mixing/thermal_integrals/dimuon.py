"""Full mediator-momentum integral for in-medium dimuon inverse decay.

The local fixed-energy rates are reused from the parent rates.py module.
All energies, temperatures, masses and chemical potentials are in MeV.
Returned emissivities are in the natural units implied by rates.py.
"""
from __future__ import annotations

import numpy as np

from rates import M_MU, charged_muon_decay_rates_mixed


def _mapped_legendre(order: int, scale: float):
    """Gauss-Legendre nodes/weights mapped from x in (0,1) to k in (0,infty)."""
    if order < 16:
        raise ValueError("Use at least 16 nodes for the semi-infinite momentum integral")
    if not np.isfinite(scale) or scale <= 0:
        raise ValueError("scale must be finite and positive")
    z, w = np.polynomial.legendre.leggauss(order)
    x = (z + 1.0) / 2.0
    wx = w / 2.0
    k = scale * x / (1.0 - x)
    jac = scale / (1.0 - x) ** 2
    return k, wx * jac


def dimuon_thermal_integral(
    mass: float,
    temperature: float,
    mu_mu: float,
    g_vector: float,
    g_axial: float,
    *,
    order: int = 96,
    scale: float | None = None,
):
    """Integrate the exact 1<->2 dimuon channel over mediator momentum.

    Returns per-mode energy emissivity Q_h = integral d^3k/(2pi)^3
    omega Gamma_prod,h and number absorption integral A_h =
    integral d^3k/(2pi)^3 Gamma_abs,h, together with the spectral arrays.

    The two charge states and Pauli factors are included by
    charged_muon_decay_rates_mixed. The channel is exactly closed at and
    below 2*m_mu. The mediator momentum integral is isotropic.
    """
    vals = (mass, temperature, mu_mu, g_vector, g_axial)
    if not all(np.isfinite(v) for v in vals):
        raise ValueError("All inputs must be finite")
    if mass <= 0 or temperature <= 0:
        raise ValueError("Require positive mediator mass and temperature")
    if mass <= 2.0 * M_MU or (g_vector == 0.0 and g_axial == 0.0):
        zeros = np.zeros(3)
        empty = np.zeros((0, 3))
        return {
            "Q_by_mode": zeros.copy(),
            "absorption_number_by_mode": zeros.copy(),
            "momentum": np.zeros(0),
            "energy": np.zeros(0),
            "production_spectrum": empty.copy(),
            "absorption_spectrum": empty.copy(),
        }

    if scale is None:
        scale = max(temperature, mass)
    momentum, weights = _mapped_legendre(order, float(scale))
    energy = np.hypot(momentum, mass)
    production, absorption = charged_muon_decay_rates_mixed(
        mass, energy, temperature, mu_mu, g_vector, g_axial
    )
    phase = weights * momentum**2 / (2.0 * np.pi**2)
    q_by_mode = np.einsum("i,ih,i->h", phase, production, energy)
    absorption_by_mode = np.einsum("i,ih->h", phase, absorption)
    return {
        "Q_by_mode": q_by_mode,
        "absorption_number_by_mode": absorption_by_mode,
        "momentum": momentum,
        "energy": energy,
        "production_spectrum": production,
        "absorption_spectrum": absorption,
    }
