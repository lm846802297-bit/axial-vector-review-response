#!/usr/bin/env python3
"""C1 vector benchmark: mode-resolved B.7 + exact moving-muon B.13 transport.

This calculation replaces Croon Eqs. (4.6)-(4.7) by the repository's
mode-resolved B.7 neutrino and exact-recoil B.13 semi-Compton kernels, while
keeping Croon's radial transport geometry and boundary choices:

* production and interior opacity are integrated over r <= R_nu(T=3 MeV);
* optical depth is radial, with no lapse/redshift or angular escape average;
* the R_far=100 km continuation contains the two-flavour vacuum neutrino
  decay width, but no outer semi-Compton opacity because the 25--100 km
  muon susceptibility is not available;
* R_far=R_nu is retained as a separate comparison.

All local rates are coefficients multiplying g_X^2. The pure-vector endpoint
(g_V/g_X=1, g_A/g_X=0) is used as the external Croon benchmark. The B.13
kernel retains both muon charges, all three A' polarizations, exact recoil,
Fermi blocking, and photon Bose enhancement. B.7 retains nu_mu and nu_tau,
with the profile muon-neutrino chemical potential and mu_nu_tau=0.

The initial run is a numerical C1 pilot, not a complete Croon reproduction:
the public profile is a reconstructed SFHo-18.8 profile and the outer
muon-opacity tail remains unavailable.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import cumulative_simpson, simpson

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from rates import neutrino_rates
from finite_mixing.moving_muon_compton import moving_muon_compton_rates
from croon_c0_luminosity import (
    M_MU,
    ALPHA_EM,
    MEV_INV_PER_KM,
    MEV2_TO_ERG_PER_SECOND,
    vectorized_muon_susceptibility,
)

DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "croon_c1_b13_vector_transport_2026-11-19.json"
DEFAULT_CSV = HERE / "outputs" / "croon_c1_b13_vector_transport_2026-11-19.csv"
CROON_MASSES_MEV = (1.0e-7, 1.0e-6, 1.0e-5, 0.1, 10.0, 200.0)
MODES = ("L", "+", "-")
CHARGES = ("mu_minus", "mu_plus")
R_FAR_KM = 100.0
T_NU_MEV = 3.0
PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def neutrinosphere_radius(r_km: np.ndarray, temperature: np.ndarray,
                          cutoff_MeV: float = T_NU_MEV) -> float:
    r = np.asarray(r_km, float)
    t = np.asarray(temperature, float)
    crossings = np.where((t[:-1] - cutoff_MeV) * (t[1:] - cutoff_MeV) <= 0.0)[0]
    candidates = [int(i) for i in crossings if t[i] >= cutoff_MeV and t[i + 1] <= cutoff_MeV]
    if candidates:
        i = candidates[-1]
        f = (cutoff_MeV - t[i]) / (t[i + 1] - t[i])
        return float(r[i] + f * (r[i + 1] - r[i]))
    slope = (t[-1] - t[-2]) / (r[-1] - r[-2])
    if not (slope < 0.0 and t[-1] > cutoff_MeV):
        raise ValueError("No outward T=3 MeV crossing or valid final-cell extrapolation")
    return float(r[-1] + (cutoff_MeV - t[-1]) / slope)


def sample_profile(profile_path: Path, radial_points: int) -> dict:
    rows = np.genfromtxt(profile_path, delimiter=",", names=True)
    required = ("r_km", "T_MeV", "mu_mu_MeV", "mu_numu_MeV")
    if rows.dtype.names is None or any(name not in rows.dtype.names for name in required):
        raise ValueError(f"Profile must contain columns {required}")
    r_src = np.asarray(rows["r_km"], float)
    t_src = np.asarray(rows["T_MeV"], float)
    mu_src = np.asarray(rows["mu_mu_MeV"], float)
    munu_src = np.asarray(rows["mu_numu_MeV"], float)
    if np.any(np.diff(r_src) <= 0.0):
        raise ValueError("Profile radius must be strictly increasing")

    r_nu = neutrinosphere_radius(r_src, t_src)
    slope_t = (t_src[-1] - t_src[-2]) / (r_src[-1] - r_src[-2])
    nonzero = np.flatnonzero(mu_src > 0.0)
    if len(nonzero) == 0:
        raise ValueError("Profile contains no positive muon chemical potential")
    r_mu_edge = float(r_src[nonzero[-1]])
    r_mu_zero = float(r_src[min(nonzero[-1] + 1, len(r_src) - 1)])

    r = np.unique(np.r_[
        np.linspace(0.0, r_nu, int(radial_points)),
        r_mu_edge, r_mu_zero, r_nu
    ])
    t = np.interp(r, r_src, t_src)
    mu = np.interp(r, r_src, mu_src)
    munu = np.interp(r, r_src, munu_src)
    outside = r > r_src[-1]
    t[outside] = t_src[-1] + slope_t * (r[outside] - r_src[-1])
    mu[outside] = 0.0
    munu[outside] = 0.0
    t[-1] = T_NU_MEV
    return {
        "r_km": r,
        "temperature_MeV": t,
        "mu_mu_MeV": mu,
        "mu_numu_MeV": munu,
        "R_nu_km": float(r_nu),
        "r_mu_last_nonzero_km": r_mu_edge,
        "r_mu_first_zero_km": r_mu_zero,
        "source_rows": int(len(rows)),
        "profile_sha256": sha256(profile_path),
    }


def energy_quadrature(mass_MeV: float, max_temperature_MeV: float,
                      order: int = 32) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Gauss rule for omega=m+Tmax*y^2, y in [0,6]."""
    if mass_MeV <= 0.0 or max_temperature_MeV <= 0.0 or order < 8:
        raise ValueError("Invalid mass, maximum temperature, or energy order")
    z, w = leggauss(int(order))
    y = 3.0 * (z + 1.0)
    wy = 3.0 * w
    omega = mass_MeV + max_temperature_MeV * y * y
    domega_weights = 2.0 * max_temperature_MeV * y * wy
    momentum = np.sqrt(np.maximum((omega - mass_MeV) * (omega + mass_MeV), 0.0))
    phase_energy = omega * omega * momentum / (2.0 * np.pi**2)
    return omega, domega_weights, phase_energy


def outer_vacuum_neutrino_opacity_per_g2(
    mass_MeV: float, omega_MeV: np.ndarray, path_km: float
) -> np.ndarray:
    """B.7 two-flavour vacuum net-decay opacity, per mode and per g_X^2.

    In the vacuum limit each flavour contributes m^2/(24*pi*omega) to
    each physical vector mode. Summing nu_mu and nu_tau gives
    m^2/(12*pi*omega), which is the opacity used on the outer path.
    """
    omega = np.asarray(omega_MeV, float)
    if mass_MeV <= 0.0 or np.any(omega < mass_MeV) or path_km < 0.0:
        raise ValueError("Invalid mass, energy, or outer path")
    return (path_km * MEV_INV_PER_KM
            * mass_MeV * mass_MeV / (12.0 * np.pi * omega))


def radial_optical_depth(kappa: np.ndarray, r_nat: np.ndarray) -> np.ndarray:
    """Return tau(r)=integral_r^Rnu kappa dr, preserving energy and mode axes."""
    values = np.asarray(kappa, float)
    radius = np.asarray(r_nat, float)
    if values.ndim != 3 or values.shape[0] != len(radius):
        raise ValueError("kappa must have shape (n_radius,n_energy,3)")
    if np.any(np.diff(radius) <= 0.0):
        raise ValueError("Radius must be strictly increasing")
    cumulative = cumulative_simpson(values, x=radius, axis=0, initial=0.0)
    return np.maximum(cumulative[-1][None, :, :] - cumulative, 0.0)


def integrate_spherical_source(
    source: np.ndarray, r_nat: np.ndarray, domega_weights: np.ndarray
) -> float:
    """Integrate a 3-mode source array over radius and energy."""
    radial = simpson(np.asarray(source, float), x=np.asarray(r_nat, float), axis=0)
    return float(np.sum(np.asarray(domega_weights)[:, None] * radial))


def integrate_spherical_source_by_mode(
    source: np.ndarray, r_nat: np.ndarray, domega_weights: np.ndarray
) -> np.ndarray:
    """Integrate a (radius, energy, mode) source and retain (L,+,-)."""
    radial = simpson(np.asarray(source, float), x=np.asarray(r_nat, float), axis=0)
    return np.sum(np.asarray(domega_weights)[:, None] * radial, axis=0)


def _compute_mass(
    mass: float,
    profile: dict,
    energy_order: int,
    inner_orders: tuple[int, int, int, int],
    neutrino_order: int,
    susceptibility_order: int,
    couplings: np.ndarray,
    muon_current: tuple[float, float] = (1.0, 0.0),
) -> tuple[dict, list[dict]]:
    r_km = profile["r_km"]
    temp = profile["temperature_MeV"]
    mu_mu = profile["mu_mu_MeV"]
    mu_numu = profile["mu_numu_MeV"]
    r_nat = r_km * MEV_INV_PER_KM
    n_r = len(r_km)

    omega, domega_weights, phase = energy_quadrature(
        mass, float(np.max(temp)), energy_order
    )
    n_e = len(omega)
    kappa_nu = np.zeros((n_r, n_e, 3))
    prod_nu = np.zeros_like(kappa_nu)
    abs_nu = np.zeros_like(kappa_nu)
    prod_sc_minus = np.zeros_like(kappa_nu)
    abs_sc_minus = np.zeros_like(kappa_nu)
    prod_sc_plus = np.zeros_like(kappa_nu)
    abs_sc_plus = np.zeros_like(kappa_nu)

    max_nu_db = 0.0
    max_sc_db = 0.0
    max_shell_error = 0.0
    min_matrix_element = math.inf

    for ir in range(n_r):
        t = float(temp[ir])
        mu = float(mu_mu[ir])
        munu = float(mu_numu[ir])

        pn, an = neutrino_rates(
            mass, omega, t, munu, order=neutrino_order
        )
        prod_nu[ir] = pn
        abs_nu[ir] = an
        expected_nu = np.exp(-omega / t)[:, None] * an
        nu_res = np.abs(pn - expected_nu) / np.maximum(
            np.maximum(np.abs(pn), np.abs(expected_nu)), 1.0e-300
        )
        max_nu_db = max(max_nu_db, float(np.max(nu_res)))

        for ie, energy in enumerate(omega):
            local = moving_muon_compton_rates(
                mass, float(energy), t, mu,
                g_vector=float(muon_current[0]),
                g_axial=float(muon_current[1]), orders=inner_orders
            )
            max_shell_error = max(
                max_shell_error,
                float(local["diagnostics"]["final_muon_shell_relative_error"])
            )
            for charge, p_array, a_array in (
                ("mu_minus", prod_sc_minus, abs_sc_minus),
                ("mu_plus", prod_sc_plus, abs_sc_plus),
            ):
                item = local["charge_resolved"][charge]
                p = np.asarray(item["production"], float)
                a = np.asarray(item["absorption"], float)
                p_array[ir, ie] = p
                a_array[ir, ie] = a
                expected = math.exp(-float(energy) / t) * a
                residual = np.abs(p - expected) / np.maximum(
                    np.maximum(np.abs(p), np.abs(expected)), 1.0e-300
                )
                max_sc_db = max(max_sc_db, float(np.max(residual)))
                min_matrix_element = min(
                    min_matrix_element,
                    float(item["minimum_matrix_element_before_roundoff_clip"])
                )

    prod_sc = prod_sc_minus + prod_sc_plus
    abs_sc = abs_sc_minus + abs_sc_plus
    prod_total = prod_nu + prod_sc
    abs_total = abs_nu + abs_sc

    # The net absorption coefficient is Gamma_abs-Gamma_prod, equivalently
    # (1-exp(-omega/T))*Gamma_abs by exact local detailed balance.
    reduced_factor = -np.expm1(-omega[None, :] / temp[:, None])
    kappa_total = reduced_factor[:, :, None] * abs_total
    tau_inside = radial_optical_depth(kappa_total, r_nat)

    phase3 = phase[None, :, None]
    volume = 4.0 * np.pi * r_nat[:, None, None]**2
    source_nu = volume * phase3 * prod_nu
    source_sc_minus = volume * phase3 * prod_sc_minus
    source_sc_plus = volume * phase3 * prod_sc_plus
    source_sc = source_sc_minus + source_sc_plus
    source_total = source_nu + source_sc

    # Croon Eq. (4.7) reference, on the same radial/energy grid and with the
    # literal single-mu-minus susceptibility convention.
    chi_minus = vectorized_muon_susceptibility(
        temp, mu_mu, order=susceptibility_order, include_antimuons=False
    )
    bose = 1.0 / np.expm1(np.minimum(omega[None, :] / temp[:, None], 700.0))
    velocity = np.sqrt(np.maximum(1.0 - (mass / omega)**2, 0.0))
    gamma_croon_sc = (
        2.0 * ALPHA_EM / (3.0 * M_MU**2)
        * chi_minus[:, None] * velocity[None, :] * bose
    )
    source_croon_sc = volume[:, :, 0] * phase[None, :] * gamma_croon_sc

    thin_nu = integrate_spherical_source(source_nu, r_nat, domega_weights)
    thin_sc_minus = integrate_spherical_source(
        source_sc_minus, r_nat, domega_weights
    )
    thin_sc_plus = integrate_spherical_source(
        source_sc_plus, r_nat, domega_weights
    )
    thin_sc = thin_sc_minus + thin_sc_plus
    thin_croon_sc = float(np.sum(
        domega_weights[None, :]
        * simpson(source_croon_sc, x=r_nat, axis=0)[None, :]
    ))
    thin_total = thin_nu + thin_sc

    # Retain the three physical polarizations separately before summing.
    thin_nu_modes = integrate_spherical_source_by_mode(source_nu, r_nat, domega_weights)
    thin_sc_minus_modes = integrate_spherical_source_by_mode(
        source_sc_minus, r_nat, domega_weights
    )
    thin_sc_plus_modes = integrate_spherical_source_by_mode(
        source_sc_plus, r_nat, domega_weights
    )
    thin_sc_modes = thin_sc_minus_modes + thin_sc_plus_modes
    thin_total_modes = thin_nu_modes + thin_sc_modes

    # Per-radius source ratios after energy integration, retaining L,+,-.
    q_nu_by_mode = np.sum(
        domega_weights[None, :, None] * phase[None, :, None] * prod_nu, axis=1
    )
    q_sc_minus_by_mode = np.sum(
        domega_weights[None, :, None] * phase[None, :, None] * prod_sc_minus,
        axis=1
    )
    q_sc_plus_by_mode = np.sum(
        domega_weights[None, :, None] * phase[None, :, None] * prod_sc_plus,
        axis=1
    )
    q_sc_minus = np.sum(q_sc_minus_by_mode, axis=1)
    q_sc_plus = np.sum(q_sc_plus_by_mode, axis=1)
    q_croon = np.sum(
        domega_weights[None, :] * phase[None, :] * gamma_croon_sc, axis=1
    )
    local_rows = []
    for ir in range(n_r):
        row = {
            "mass_MeV": float(mass),
            "r_km": float(r_km[ir]),
            "T_MeV": float(temp[ir]),
            "mu_mu_MeV": float(mu_mu[ir]),
            "mu_numu_MeV": float(mu_numu[ir]),
            "chi_mu_minus_MeV3": float(chi_minus[ir]),
            "Q_B7_nu_mu_plus_nu_tau_per_g2_MeV5": float(np.sum(q_nu_by_mode[ir])),
            "Q_B13_mu_minus_per_g2_MeV5": float(q_sc_minus[ir]),
            "Q_B13_mu_plus_per_g2_MeV5": float(q_sc_plus[ir]),
            "Q_B13_mu_pm_per_g2_MeV5": float(q_sc_minus[ir] + q_sc_plus[ir]),
            "Q_B7_plus_B13_per_g2_MeV5": float(
                np.sum(q_nu_by_mode[ir]) + q_sc_minus[ir] + q_sc_plus[ir]
            ),
            "Q_Croon_Eq47_mu_minus_per_g2_MeV5": float(q_croon[ir]),
            "B13_mu_minus_over_Croon_Eq47": (
                float(q_sc_minus[ir] / q_croon[ir]) if q_croon[ir] > 0.0 else None
            ),
            "B13_mu_pm_over_Croon_Eq47": (
                float((q_sc_minus[ir] + q_sc_plus[ir]) / q_croon[ir])
                if q_croon[ir] > 0.0 else None
            ),
        }
        for im, mode in enumerate(MODES):
            row[f"Q_B7_{mode}_per_g2_MeV5"] = float(q_nu_by_mode[ir, im])
            row[f"Q_B13_mu_minus_{mode}_per_g2_MeV5"] = float(
                q_sc_minus_by_mode[ir, im]
            )
            row[f"Q_B13_mu_plus_{mode}_per_g2_MeV5"] = float(
                q_sc_plus_by_mode[ir, im]
            )
            row[f"Q_B13_mu_pm_{mode}_per_g2_MeV5"] = float(
                q_sc_minus_by_mode[ir, im] + q_sc_plus_by_mode[ir, im]
            )
            row[f"Q_B7_plus_B13_{mode}_per_g2_MeV5"] = float(
                q_nu_by_mode[ir, im]
                + q_sc_minus_by_mode[ir, im]
                + q_sc_plus_by_mode[ir, im]
            )
        local_rows.append(row)

    outer_tail_100 = outer_vacuum_neutrino_opacity_per_g2(
        mass, omega, R_FAR_KM - float(profile["R_nu_km"])
    )
    outer_tail_zero = np.zeros_like(outer_tail_100)
    curve = []
    for g in couplings:
        g2 = float(g * g)
        record = {"g_X": float(g)}
        for label, outer_tail in (
            ("Rfar_Rnu", outer_tail_zero),
            ("Rfar_100km_vacuum_nu_tail", outer_tail_100),
        ):
            tau = tau_inside + outer_tail[None, :, None]
            attenuation = np.exp(-g2 * tau)
            radial_energy_mode = simpson(
                source_total * attenuation, x=r_nat, axis=0
            )
            luminosity_mev2 = g2 * float(np.sum(
                domega_weights[:, None] * radial_energy_mode
            ))
            luminosity_by_mode_mev2 = g2 * np.sum(
                domega_weights[:, None] * radial_energy_mode, axis=0
            )
            luminosity_erg_s = float(
                luminosity_mev2 * MEV2_TO_ERG_PER_SECOND
            )
            mode_luminosity_erg_s = (
                luminosity_by_mode_mev2 * MEV2_TO_ERG_PER_SECOND
            )
            record[label] = luminosity_erg_s
            record[f"{label}_by_mode_erg_s"] = {
                mode: float(mode_luminosity_erg_s[im])
                for im, mode in enumerate(MODES)
            }
            record[f"{label}_mode_sum_relative_residual"] = float(
                abs(float(np.sum(mode_luminosity_erg_s)) - luminosity_erg_s)
                / max(abs(luminosity_erg_s), 1e-300)
            )
        curve.append(record)

    # Charge- and mode-resolved optically-thin contributions for exact channel audit.
    return {
        "mass_MeV": float(mass),
        "profile_sha256": profile["profile_sha256"],
        "R_nu_km": float(profile["R_nu_km"]),
        "radial_points": int(n_r),
        "energy_order": int(energy_order),
        "energy_points": int(n_e),
        "polarization_modes": list(MODES),
        "inner_orders": list(inner_orders),
        "neutrino_angular_order": int(neutrino_order),
        "maximum_B7_mode_detailed_balance_residual": max_nu_db,
        "maximum_B13_charge_mode_detailed_balance_residual": max_sc_db,
        "maximum_final_muon_shell_relative_error": max_shell_error,
        "minimum_B13_matrix_element_before_roundoff_clip": (
            None if not math.isfinite(min_matrix_element) else float(min_matrix_element)
        ),
        "thin_source_per_g2_erg_s": {
            "B7_nu_mu_plus_nu_tau": float(thin_nu * MEV2_TO_ERG_PER_SECOND),
            "B13_mu_minus": float(thin_sc_minus * MEV2_TO_ERG_PER_SECOND),
            "B13_mu_plus": float(thin_sc_plus * MEV2_TO_ERG_PER_SECOND),
            "B13_mu_pm": float(thin_sc * MEV2_TO_ERG_PER_SECOND),
            "B7_plus_B13": float(thin_total * MEV2_TO_ERG_PER_SECOND),
            "Croon_Eq47_mu_minus_only": float(thin_croon_sc * MEV2_TO_ERG_PER_SECOND),
        },
        "thin_source_by_mode_per_g2_erg_s": {
            "B7_nu_mu_plus_nu_tau": {
                mode: float(thin_nu_modes[im] * MEV2_TO_ERG_PER_SECOND)
                for im, mode in enumerate(MODES)
            },
            "B13_mu_minus": {
                mode: float(thin_sc_minus_modes[im] * MEV2_TO_ERG_PER_SECOND)
                for im, mode in enumerate(MODES)
            },
            "B13_mu_plus": {
                mode: float(thin_sc_plus_modes[im] * MEV2_TO_ERG_PER_SECOND)
                for im, mode in enumerate(MODES)
            },
            "B13_mu_pm": {
                mode: float(thin_sc_modes[im] * MEV2_TO_ERG_PER_SECOND)
                for im, mode in enumerate(MODES)
            },
            "B7_plus_B13": {
                mode: float(thin_total_modes[im] * MEV2_TO_ERG_PER_SECOND)
                for im, mode in enumerate(MODES)
            },
        },
        "thin_source_mode_sum_relative_residuals": {
            "B7_nu_mu_plus_nu_tau": float(
                abs(np.sum(thin_nu_modes) - thin_nu) / max(abs(thin_nu), 1e-300)
            ),
            "B13_mu_minus": float(
                abs(np.sum(thin_sc_minus_modes) - thin_sc_minus)
                / max(abs(thin_sc_minus), 1e-300)
            ),
            "B13_mu_plus": float(
                abs(np.sum(thin_sc_plus_modes) - thin_sc_plus)
                / max(abs(thin_sc_plus), 1e-300)
            ),
            "B13_mu_pm": float(
                abs(np.sum(thin_sc_modes) - thin_sc) / max(abs(thin_sc), 1e-300)
            ),
            "B7_plus_B13": float(
                abs(np.sum(thin_total_modes) - thin_total)
                / max(abs(thin_total), 1e-300)
            ),
        },
        "thin_source_ratios": {
            "B13_mu_minus_over_Croon_Eq47": (
                float(thin_sc_minus / thin_croon_sc) if thin_croon_sc > 0.0 else None
            ),
            "B13_mu_pm_over_Croon_Eq47": (
                float(thin_sc / thin_croon_sc) if thin_croon_sc > 0.0 else None
            ),
        },
        "coupling_curve": curve,
        "local_profile": local_rows,
        "outer_opacity": (
            "B.7 two-flavour vacuum decay per mode from Rnu to Rfar=100 km; "
            "outer B.13 semi-Compton opacity is omitted because no validated "
            "25--100 km muon-susceptibility profile is available"
        ),
    }, local_rows


def compute_c1(
    profile_path: Path = DEFAULT_PROFILE,
    masses: tuple[float, ...] = (10.0,),
    radial_points: int = 101,
    energy_order: int = 32,
    inner_orders: tuple[int, int, int, int] = (12, 8, 8, 8),
    neutrino_order: int = 96,
    susceptibility_order: int = 128,
    coupling_count: int = 121,
) -> dict:
    if sha256(profile_path) != PROFILE_SHA256:
        raise ValueError("The C1 run is pinned to the reviewed public SFHo profile SHA-256")
    profile = sample_profile(profile_path, radial_points)
    couplings = np.logspace(-11.0, 0.0, int(coupling_count))
    results = {}
    local_all = []
    for mass in masses:
        item, local_rows = _compute_mass(
            float(mass), profile, energy_order, inner_orders,
            neutrino_order, susceptibility_order, couplings
        )
        results[f"{mass:.9g}"] = item
        local_all.extend(local_rows)
    return {
        "title": "C1 modern vector benchmark: B.7 plus exact moving-muon B.13 with Croon radial transport",
        "status": "C1 interior-profile transport calculation; outer semi-Compton opacity remains unavailable",
        "source_profile": {
            "path": str(profile_path),
            "sha256": profile["profile_sha256"],
            "rows": profile["source_rows"],
            "R_nu_km_from_T_equals_3_MeV": profile["R_nu_km"],
            "r_mu_last_nonzero_km": profile["r_mu_last_nonzero_km"],
            "r_mu_first_zero_km": profile["r_mu_first_zero_km"],
            "radial_points": len(profile["r_km"]),
        },
        "model": {
            "current": "pure vector endpoint: gV/gX=1, gA/gX=0",
            "neutrino_flavours": "nu_mu with profile mu_numu(r), plus nu_tau with mu_numu_tau=0",
            "muon_targets": "both mu_minus and mu_plus, separately retained",
            "mediator_modes": ["L", "+", "-"],
            "dimuon_channel": "closed for all Croon Fig. 2 masses because 200 MeV < 2*m_mu",
        },
        "transport": {
            "volume_element": "4*pi*r^2 dr",
            "optical_depth": "radial integral of reduced absorption Gamma_abs-Gamma_prod, mode by mode",
            "angular_escape_average": "omitted to match Croon radial prescription",
            "lapse_redshift": "omitted to match Croon Sec. 3 comparison",
            "R_far_values_km": [profile["R_nu_km"], R_FAR_KM],
            "outer_neutrino_opacity": "B.7 two-flavour vacuum decay width per mode",
            "outer_semicompton_opacity": "omitted; no validated 25--100 km muon susceptibility",
        },
        "numerics": {
            "radial_points_requested": int(radial_points),
            "energy_order": int(energy_order),
            "inner_orders": list(inner_orders),
            "neutrino_angular_order": int(neutrino_order),
            "susceptibility_order": int(susceptibility_order),
            "coupling_count": int(coupling_count),
            "coupling_range": [float(couplings[0]), float(couplings[-1])],
            "energy_map": "omega=m+Tmax*y^2, y in [0,6], Gauss-Legendre in y",
            "radial_integrator": "cumulative_simpson for optical depth; Simpson for luminosity",
        },
        "masses": results,
        "scope": (
            "The C1 calculation replaces Croon Eqs. (4.6)-(4.7) with the "
            "mode-resolved Blinov B.7 neutrino kernel and exact-recoil B.13 "
            "moving-muon Compton kernel. It keeps Croon's radial transport "
            "geometry. It is a public-profile reconstruction and does not "
            "include the unknown 25--100 km semi-Compton opacity."
        ),
        "local_profile_rows": local_all,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--masses", type=str, default="10.0",
                        help="comma-separated masses in MeV; use --all-croon-masses for Fig. 2 set")
    parser.add_argument("--all-croon-masses", action="store_true")
    parser.add_argument("--radial-points", type=int, default=101)
    parser.add_argument("--energy-order", type=int, default=32)
    parser.add_argument("--inner-orders", type=str, default="12,8,8,8")
    parser.add_argument("--neutrino-order", type=int, default=96)
    parser.add_argument("--susceptibility-order", type=int, default=128)
    parser.add_argument("--coupling-count", type=int, default=121)
    args = parser.parse_args()
    masses = CROON_MASSES_MEV if args.all_croon_masses else tuple(
        float(x) for x in args.masses.split(",") if x.strip()
    )
    orders = tuple(int(x) for x in args.inner_orders.split(","))
    if len(orders) != 4:
        raise ValueError("--inner-orders must contain four comma-separated integers")
    result = compute_c1(
        args.profile, tuple(masses), args.radial_points, args.energy_order,
        orders, args.neutrino_order, args.susceptibility_order,
        args.coupling_count
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    rows = result.pop("local_profile_rows")
    import csv
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        with args.csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    summary = {
        "profile": result["source_profile"],
        "masses": {
            key: {
                "thin_source_per_g2_erg_s": value["thin_source_per_g2_erg_s"],
                "thin_source_ratios": value["thin_source_ratios"],
                "max_B7_DB": value["maximum_B7_mode_detailed_balance_residual"],
                "max_B13_DB": value["maximum_B13_charge_mode_detailed_balance_residual"],
                "coupling_points": len(value["coupling_curve"]),
            }
            for key, value in result["masses"].items()
        },
        "output_json": str(args.output),
        "output_csv": str(args.csv),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
