"""Full A' momentum integral for mu+ mu- <-> A'."""

from __future__ import annotations
import math
import sys
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import rates


def thermal_dimuon_emissivity(
    mass, temperature, mu_mu, g_vector=0.0, g_axial=-1.0,
    energy_order=24, angular_order=64, x_max=36.0
):
    """Return mode-resolved emissivity in MeV^5 per g_X^2.

    Q_h = (2 pi^2)^-1 int_M^infty d omega omega^2 sqrt(omega^2-M^2)
          Gamma_prod,h(omega).
    The existing mixed-current Dirac trace and exact threshold are reused;
    this function performs the full on-shell A' energy/momentum integral.
    """
    mass, temperature, mu_mu = map(float, (mass, temperature, mu_mu))
    g_vector, g_axial = float(g_vector), float(g_axial)
    if not all(math.isfinite(x) for x in
               (mass, temperature, mu_mu, g_vector, g_axial)):
        raise ValueError("All inputs must be finite")
    if mass <= 0 or temperature <= 0 or energy_order < 4 or angular_order < 4 or x_max <= 0:
        raise ValueError("Invalid mass, temperature, quadrature order, or cutoff")
    threshold = 2.0*rates.M_MU
    if mass <= threshold:
        return {
            "open": False, "threshold_MeV": threshold,
            "emissivity_by_mode_MeV5": [0.0, 0.0, 0.0],
            "emissivity_total_MeV5": 0.0,
            "energy_MeV": [], "production_MeV": [], "absorption_MeV": [],
            "max_detailed_balance_relative_error": 0.0,
        }

    # y=sqrt((omega-M)/T) smooths the threshold momentum sqrt(omega-M).
    z, w = leggauss(energy_order)
    y_max = math.sqrt(x_max)
    y = 0.5*y_max*(z+1.0)
    w_y = 0.5*y_max*w
    omega = mass+temperature*y*y
    q_momentum = np.sqrt(np.maximum((omega-mass)*(omega+mass),0.0))
    production, absorption = rates.charged_muon_decay_rates_mixed(
        mass, omega, temperature, mu_mu, g_vector, g_axial,
        order=angular_order
    )
    spectral_weight = (
        2.0*temperature*y*w_y*omega**2*q_momentum/(2.0*math.pi**2)
    )
    q_mode = np.einsum("i,ih->h",spectral_weight,production)
    balance = np.exp(-omega/temperature)[:,None]*absorption
    rel = np.abs(production-balance)/np.maximum(np.abs(production),1e-300)
    return {
        "open": True,
        "threshold_MeV": threshold,
        "mass_over_threshold": mass/threshold,
        "temperature_MeV": temperature,
        "muon_chemical_potential_MeV": mu_mu,
        "couplings_normalized_to_gX": {
            "g_vector": g_vector, "g_axial": g_axial
        },
        "energy_MeV": omega.tolist(),
        "mediator_momentum_MeV": q_momentum.tolist(),
        "production_MeV": production.tolist(),
        "absorption_MeV": absorption.tolist(),
        "emissivity_by_mode_MeV5": q_mode.tolist(),
        "emissivity_total_MeV5": float(np.sum(q_mode)),
        "max_detailed_balance_relative_error": float(np.max(rel)),
        "quadrature": {
            "energy_order": energy_order,
            "angular_order": angular_order,
            "x_max": x_max
        },
    }
