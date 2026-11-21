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


def lai_neutrino_inverse_mfp_coefficient(
    omega_MeV: np.ndarray,
    mass_MeV: float,
) -> np.ndarray:
    """Lai Eq. (20): two-flavour Z' -> nu nu-bar inverse mean free path / g^2."""
    omega = np.asarray(omega_MeV, dtype=float)
    if mass_MeV <= 0.0 or np.any(omega <= mass_MeV):
        raise ValueError("Require positive mass and energies strictly above threshold")
    velocity = np.sqrt(1.0 - (mass_MeV / omega) ** 2)
    return mass_MeV**2 / (12.0 * np.pi * omega * velocity)


def lai_semicompton_production_coefficient(
    omega_MeV: np.ndarray,
    temperature_MeV: float,
    mass_MeV: float,
    chi_mu_MeV3: float,
) -> np.ndarray:
    """Lai Eq. (11): semi-Compton production rate / g^2."""
    omega = np.asarray(omega_MeV, dtype=float)
    if (temperature_MeV <= 0.0 or mass_MeV < 0.0 or chi_mu_MeV3 < 0.0
            or np.any(omega <= mass_MeV)):
        raise ValueError("Unphysical semi-Compton production inputs")
    velocity = np.sqrt(1.0 - (mass_MeV / omega) ** 2)
    return (
        2.0 * ALPHA_EM / (3.0 * M_MU_MEV**2)
        * chi_mu_MeV3 * velocity * bose_occupation(omega, temperature_MeV)
    )


def lai_semicompton_to_neutrino_opacity_ratio(
    omega_MeV: np.ndarray,
    temperature_MeV: float,
    mass_MeV: float,
    chi_mu_MeV3: float,
) -> np.ndarray:
    """Eq. (23) semi-Compton opacity divided by Eq. (20) two-flavour decay opacity."""
    omega = np.asarray(omega_MeV, dtype=float)
    if chi_mu_MeV3 < 0.0:
        raise ValueError("Muon susceptibility cannot be negative")
    kappa_sc = lai_semicompton_inverse_mfp_coefficient(
        omega, temperature_MeV, mass_MeV, chi_mu_MeV3
    )
    kappa_nu = lai_neutrino_inverse_mfp_coefficient(omega, mass_MeV)
    return kappa_sc / kappa_nu


def lai_semicompton_to_neutrino_production_ratio(
    omega_MeV: np.ndarray,
    temperature_MeV: float,
    mass_MeV: float,
    chi_mu_MeV3: float,
) -> np.ndarray:
    """Eq. (11) semi-Compton production divided by Eq. (10) two-flavour coalescence."""
    omega = np.asarray(omega_MeV, dtype=float)
    if chi_mu_MeV3 < 0.0:
        raise ValueError("Muon susceptibility cannot be negative")
    gamma_sc = lai_semicompton_production_coefficient(
        omega, temperature_MeV, mass_MeV, chi_mu_MeV3
    )
    gamma_nu = lai_two_flavour_neutrino_coalescence_coefficient(
        omega, mass_MeV, temperature_MeV
    )
    return gamma_sc / gamma_nu


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


MEV2_TO_ERG_PER_SECOND = 1.602176634e-6 / 6.582119569e-22
MEV_INV_PER_KM = 1.0e5 / (197.3269804e-13)


def lai_neutrino_only_plateau(
    mass_MeV: float,
    temperature_MeV: float,
    neutrinosphere_radius_km: float,
    energy_order: int = 256,
    tail_in_T: float = 40.0,
) -> dict:
    """Lai thin-shell plateau from nu_mu+nu_tau coalescence/decay only.

    Uses Lai Eq. (7), Eq. (10), Eq. (20), and Appendix E Eq. (E2).
    It deliberately omits semi-Compton and loop-bremsstrahlung channels.
    """
    from numpy.polynomial.legendre import leggauss

    if (mass_MeV < 0.0 or temperature_MeV <= 0.0
            or neutrinosphere_radius_km <= 0.0 or energy_order < 16
            or tail_in_T < 20.0):
        raise ValueError("Invalid mass, temperature, radius, or quadrature settings")
    z, weights = leggauss(energy_order)
    x = 0.5 * tail_in_T * (z + 1.0)
    wx = 0.5 * tail_in_T * weights
    omega = mass_MeV + temperature_MeV * x
    v2 = np.maximum(1.0 - (mass_MeV / omega) ** 2, 0.0)
    integrand = omega**3 * v2 * np.exp(-omega / temperature_MeV)
    spectral_integral = float(temperature_MeV * np.dot(wx, integrand))

    r_nu = neutrinosphere_radius_km * MEV_INV_PER_KM
    luminosity_natural = 3.0 * r_nu**2 / (2.0 * np.pi) * spectral_integral
    luminosity_erg_s = luminosity_natural * MEV2_TO_ERG_PER_SECOND

    massless_limit = 9.0 / np.pi * r_nu**2 * temperature_MeV**4
    return {
        "mass_MeV": float(mass_MeV),
        "temperature_MeV": float(temperature_MeV),
        "neutrinosphere_radius_km": float(neutrinosphere_radius_km),
        "energy_order": int(energy_order),
        "tail_in_T": float(tail_in_T),
        "spectral_integral_MeV4": spectral_integral,
        "L_nu_only_plateau_natural_MeV2": float(luminosity_natural),
        "L_nu_only_plateau_erg_s": float(luminosity_erg_s),
        "massless_limit_erg_s": float(massless_limit * MEV2_TO_ERG_PER_SECOND),
        "relative_to_massless_limit": float(luminosity_natural / massless_limit),
        "scope": "neutrino-pair coalescence/decay channel only; omits semi-Compton and loop-bremsstrahlung",
    }


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
