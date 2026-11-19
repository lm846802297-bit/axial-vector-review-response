"""Equation-level audit of the Lai et al. (2024) trapping/plateau prescription.

This module does not claim a full supernova reproduction. It isolates:
  * the thin-shell plateau cancellation L_inf ~ R_nu^2 int(dot_eps/kappa) d omega;
  * the full-angle versus two-ray geometric factor;
  * printed Croon/Lai semi-Compton inverse-mean-free-path normalizations;
  * the printed Croon/Lai two-neutrino-flavour coalescence normalizations.

All rate functions return coefficients per g_Z'^2. Natural units are used.
"""
from __future__ import annotations

import numpy as np

ALPHA_EM = 1.0 / 137.035999084
M_MU_MEV = 105.6583755


def bose_occupation(omega_MeV: np.ndarray | float, temperature_MeV: float):
    omega = np.asarray(omega_MeV, dtype=float)
    if temperature_MeV <= 0.0 or np.any(omega <= 0.0):
        raise ValueError("Require positive energy and temperature")
    x = omega / temperature_MeV
    return 1.0 / np.expm1(x)


def croon_semicompton_absorption_length_coefficient(
    omega_MeV: np.ndarray,
    temperature_MeV: float,
    mass_MeV: float,
    chi_mu_MeV3: float,
) -> np.ndarray:
    """Croon Eq. (4.7) detailed-balance continuation used in the C0 lane.

    Returns kappa_Croon/g^2 = Gamma_abs/g^2 with no additional 1/v factor.
    The source uses Gamma_prod/g^2 = 2 alpha chi v f_B/(3 m_mu^2).
    """
    omega = np.asarray(omega_MeV, dtype=float)
    if mass_MeV < 0.0 or chi_mu_MeV3 < 0.0 or np.any(omega < mass_MeV):
        raise ValueError("Unphysical semi-Compton inputs")
    v = np.sqrt(np.maximum(1.0 - (mass_MeV / omega) ** 2, 0.0))
    return (
        2.0 * ALPHA_EM / (3.0 * M_MU_MEV**2)
        * chi_mu_MeV3 * v * (1.0 + bose_occupation(omega, temperature_MeV))
    )


def lai_semicompton_inverse_mfp_coefficient(
    omega_MeV: np.ndarray,
    temperature_MeV: float,
    mass_MeV: float,
    chi_mu_MeV3: float,
) -> np.ndarray:
    """Lai et al. Eqs. (21)-(23): inverse mean free path / g^2.

    Eq. (21) has the explicit 2/3 polarization/statistical factor; Eq. (15)
    converts the lab absorption rate to inverse mean free path, cancelling
    the final Z' velocity in the semi-Compton channel.
    """
    omega = np.asarray(omega_MeV, dtype=float)
    if mass_MeV < 0.0 or chi_mu_MeV3 < 0.0 or np.any(omega < mass_MeV):
        raise ValueError("Unphysical semi-Compton inputs")
    return (
        4.0 * ALPHA_EM / (9.0 * M_MU_MEV**2)
        * chi_mu_MeV3 * (1.0 + bose_occupation(omega, temperature_MeV))
    )


def lai_over_croon_semicompton_opacity_ratio(
    omega_MeV: np.ndarray,
    mass_MeV: float,
) -> np.ndarray:
    """Ratio of the printed Lai Eq. (23) to the Croon/C0 absorption coefficient."""
    omega = np.asarray(omega_MeV, dtype=float)
    if mass_MeV < 0.0 or np.any(omega <= 0.0) or np.any(omega < mass_MeV):
        raise ValueError("Unphysical energy or mass")
    v = np.sqrt(np.maximum(1.0 - (mass_MeV / omega) ** 2, 0.0))
    if np.any(v <= 0.0):
        raise ValueError("The ratio is singular exactly at the massive-vector threshold")
    return 2.0 / (3.0 * v)


def croon_generic_neutrino_coalescence_coefficient(
    omega_MeV: np.ndarray, mass_MeV: float, temperature_MeV: float
) -> np.ndarray:
    """Croon Eq. (4.6), generic one-neutrino-flavour rate / g^2."""
    omega = np.asarray(omega_MeV, dtype=float)
    if mass_MeV < 0.0 or np.any(omega < mass_MeV):
        raise ValueError("Unphysical neutrino coalescence inputs")
    return mass_MeV**2 / (12.0 * np.pi * omega) * bose_occupation(omega, temperature_MeV)


def croon_lmutau_neutrino_coalescence_coefficient(
    omega_MeV: np.ndarray, mass_MeV: float, temperature_MeV: float
) -> np.ndarray:
    """Croon Sec. 4.4: factor-two L_mu-L_tau neutrino-flavour transfer."""
    return 2.0 * croon_generic_neutrino_coalescence_coefficient(
        omega_MeV, mass_MeV, temperature_MeV
    )


def lai_two_flavour_neutrino_coalescence_coefficient(
    omega_MeV: np.ndarray, mass_MeV: float, temperature_MeV: float
) -> np.ndarray:
    """Lai et al. Eq. (10), including nu_mu and nu_tau, per g^2."""
    omega = np.asarray(omega_MeV, dtype=float)
    if mass_MeV < 0.0 or np.any(omega < mass_MeV):
        raise ValueError("Unphysical neutrino coalescence inputs")
    return mass_MeV**2 / (4.0 * np.pi * omega) * np.exp(-omega / temperature_MeV)


def lai_over_croon_lmutau_neutrino_ratio(
    omega_MeV: np.ndarray, mass_MeV: float, temperature_MeV: float
) -> np.ndarray:
    lai = lai_two_flavour_neutrino_coalescence_coefficient(
        omega_MeV, mass_MeV, temperature_MeV
    )
    croon = croon_lmutau_neutrino_coalescence_coefficient(
        omega_MeV, mass_MeV, temperature_MeV
    )
    if np.any(croon <= 0.0):
        raise ValueError("Croon reference rate must be positive")
    return lai / croon


def plateau_luminosity_natural_units(
    neutrinosphere_radius_MeV_inv: float,
    omega_MeV: np.ndarray,
    emissivity_spectrum_per_g2_MeV4: np.ndarray,
    inverse_mfp_per_g2_MeV: np.ndarray,
) -> float:
    """Lai Eq. (E2) plateau coefficient, independent of g.

    L_inf = pi R_nu^2 int d omega [ (d epsdot/d omega)/kappa_att ],
    where both numerator and inverse mean free path are normalized per g^2.
    """
    omega = np.asarray(omega_MeV, dtype=float)
    emissivity = np.asarray(emissivity_spectrum_per_g2_MeV4, dtype=float)
    opacity = np.asarray(inverse_mfp_per_g2_MeV, dtype=float)
    if (omega.ndim != 1 or len(omega) < 2 or emissivity.shape != omega.shape
            or opacity.shape != omega.shape):
        raise ValueError("All spectral arrays must be one-dimensional and equal length >=2")
    if (not np.all(np.isfinite(omega)) or not np.all(np.isfinite(emissivity))
            or not np.all(np.isfinite(opacity)) or np.any(np.diff(omega) <= 0.0)
            or np.any(emissivity < 0.0) or np.any(opacity <= 0.0)
            or neutrinosphere_radius_MeV_inv <= 0.0):
        raise ValueError("Invalid plateau integral inputs")
    integrand = emissivity / opacity
    return float(np.pi * neutrinosphere_radius_MeV_inv**2 * np.trapezoid(integrand, omega))


def plateau_luminosity_at_coupling(
    coupling: float,
    neutrinosphere_radius_MeV_inv: float,
    omega_MeV: np.ndarray,
    emissivity_spectrum_per_g2_MeV4: np.ndarray,
    inverse_mfp_per_g2_MeV: np.ndarray,
) -> float:
    """Finite-g thin-shell expression; should equal the g-independent plateau."""
    if coupling <= 0.0:
        raise ValueError("Coupling must be positive")
    eps = coupling**2 * np.asarray(emissivity_spectrum_per_g2_MeV4, dtype=float)
    kappa = coupling**2 * np.asarray(inverse_mfp_per_g2_MeV, dtype=float)
    return plateau_luminosity_natural_units(
        neutrinosphere_radius_MeV_inv, omega_MeV, eps, kappa
    )


def full_angle_surface_geometry_factor() -> float:
    """Outward projected flux divided by the full isotropic angular measure."""
    return float(np.trapezoid(np.array([0.0, 1.0]), np.array([0.0, 1.0])) / 2.0)


def two_ray_surface_geometry_factor() -> float:
    """The +/- radial-ray prescription's plateau factor, as stated in Lai App. E."""
    return 0.5


def geometry_factor_ratio_two_ray_to_full_angle() -> float:
    return two_ray_surface_geometry_factor() / full_angle_surface_geometry_factor()
