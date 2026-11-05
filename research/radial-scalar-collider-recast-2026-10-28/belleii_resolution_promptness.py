"""Belle II resolution and promptness bookkeeping for the scalar searches.

Publication-derived inputs:
- four-muon reduced-mass resolution: 2--2.5 MeV below 1 GeV, rising to
  about 5 MeV near 5 GeV and falling to 2.5 MeV at 9 GeV;
- both analyses require track DCA below 0.5 cm transverse and 2.0 cm longitudinal;
- SuperKEKB lab boost beta*gamma ~= 0.28.

The returned beta-gamma is a conservative kinematic maximum for
e+e- -> mu+mu-s, with the dimuon recoil at threshold and the scalar emitted
along the lab boost. It is not a production-spectrum average. Track DCA is
not identical to parent flight distance, so lengths are geometry proxies,
not detector efficiencies.
"""
from __future__ import annotations
import math

M_MU_GEV = 0.1056583755
SQRT_S_GEV = 10.58
BETA_GAMMA_CM_LAB = 0.28
GAMMA_CM_LAB = math.sqrt(1.0 + BETA_GAMMA_CM_LAB**2)
BETA_CM_LAB = BETA_GAMMA_CM_LAB / GAMMA_CM_LAB
TRACK_DCA_TRANSVERSE_M = 0.005
TRACK_DCA_LONGITUDINAL_M = 0.020


def scalar_beta_gamma_lab_max(ms_GeV: float) -> float:
    if ms_GeV <= 0.0 or ms_GeV >= SQRT_S_GEV - 2.0*M_MU_GEV:
        raise ValueError("scalar mass outside e+e- -> mu+mu-s kinematic range")
    s = SQRT_S_GEV**2
    E_star = (s + ms_GeV**2 - 4.0*M_MU_GEV**2) / (2.0*SQRT_S_GEV)
    p_star = math.sqrt(max(0.0, E_star**2 - ms_GeV**2))
    p_lab_max = GAMMA_CM_LAB * (p_star + BETA_CM_LAB*E_star)
    return p_lab_max / ms_GeV


def aprime_beta_gamma_lab_max(ms_GeV: float, mA_GeV: float) -> float | None:
    """Maximum lab beta*gamma for an on-shell A' daughter, if kinematically open."""
    if ms_GeV <= 0.0 or mA_GeV <= 0.0:
        raise ValueError("masses must be positive")
    if mA_GeV >= ms_GeV:
        return None
    s = SQRT_S_GEV**2
    E_s_star = (s + ms_GeV**2 - 4.0*M_MU_GEV**2) / (2.0*SQRT_S_GEV)
    p_s_star = math.sqrt(max(0.0, E_s_star**2 - ms_GeV**2))
    gamma_s = E_s_star / ms_GeV
    beta_s = p_s_star / E_s_star
    if mA_GeV < ms_GeV/2.0:
        E_A_rest = ms_GeV/2.0
        p_A_rest = math.sqrt(max(0.0, ms_GeV**2/4.0 - mA_GeV**2))
    else:
        E_A_rest = (ms_GeV**2 + mA_GeV**2)/(2.0*ms_GeV)
        p_A_rest = (ms_GeV**2 - mA_GeV**2)/(2.0*ms_GeV)
    E_A_star = gamma_s*(E_A_rest + beta_s*p_A_rest)
    p_A_star = gamma_s*(p_A_rest + beta_s*E_A_rest)
    p_A_lab_max = GAMMA_CM_LAB*(p_A_star + BETA_CM_LAB*E_A_star)
    return p_A_lab_max/mA_GeV


def fourmu_sigma_MR_envelope_GeV(ms_GeV: float) -> tuple[float, float] | None:
    """Conservative envelope of the published reduced-mass resolution."""
    if not 0.212 <= ms_GeV <= 9.0:
        return None
    if ms_GeV < 1.0:
        return (0.0020, 0.0025)
    if ms_GeV < 9.0:
        return (0.0025, 0.0050)
    return (0.0025, 0.0025)


def fourmu_width_resolution_ratios(ms_GeV: float, gamma_s_GeV: float) -> dict | None:
    """Convert natural width to reduced-mass width and compare to resolution."""
    sigma_range = fourmu_sigma_MR_envelope_GeV(ms_GeV)
    if sigma_range is None:
        return None
    m_reduced = math.sqrt(ms_GeV**2 - 4.0*M_MU_GEV**2)
    gamma_reduced = gamma_s_GeV*ms_GeV/m_reduced
    sigma_min, sigma_max = sigma_range
    return {
        "Gamma_MR_GeV": gamma_reduced,
        "sigma_MR_min_GeV": sigma_min,
        "sigma_MR_max_GeV": sigma_max,
        "Gamma_over_sigma_lower_resolution": gamma_reduced/sigma_min,
        "Gamma_over_sigma_upper_resolution": gamma_reduced/sigma_max,
    }
