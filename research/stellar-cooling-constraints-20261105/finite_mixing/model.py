"""UV coupling map for the finite-mixing vector--axial stellar-cooling study.

Convention:
    L_int = A'_mu * mu_bar gamma^mu (g_V + g_A gamma^5) mu.

The production rates module uses gamma^mu(-gamma^5) as its unit axial
basis. Therefore its coefficient corresponding to this convention is
-g_A, not g_A.
"""
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class MuonCouplings:
    g_x: float
    theta_mu_r: float
    g_vector: float
    g_axial: float
    g_left: float
    g_right: float

    @property
    def code_vector_coefficient(self) -> float:
        """Coefficient of the rates.py gamma^mu vector basis."""
        return self.g_vector

    @property
    def code_axial_minus_gamma5_coefficient(self) -> float:
        """Coefficient of the rates.py gamma^mu(-gamma^5) basis."""
        return -self.g_axial

    @property
    def abs_vector_to_axial_ratio(self) -> float:
        if self.g_axial == 0.0:
            return math.inf if self.g_vector != 0.0 else math.nan
        return abs(self.g_vector / self.g_axial)


def muon_couplings(g_x: float, theta_mu_r: float) -> MuonCouplings:
    """Return mass-basis couplings for 0 <= theta_mu_r <= pi/2.

    The chiral couplings are g_L = g_V - g_A = g_X and
    g_R = g_V + g_A = -g_X cos(2 theta_mu_r).
    """
    gx = float(g_x)
    theta = float(theta_mu_r)
    if not math.isfinite(gx) or gx < 0.0:
        raise ValueError("g_x must be finite and nonnegative")
    if not math.isfinite(theta) or not 0.0 <= theta <= math.pi / 2.0:
        raise ValueError("theta_mu_r must be finite and lie in [0, pi/2]")

    if theta == 0.0:
        s2, c2 = 0.0, 1.0
    elif theta == math.pi / 2.0:
        s2, c2 = 1.0, 0.0
    else:
        s2 = math.sin(theta) ** 2
        c2 = math.cos(theta) ** 2
    gv = gx * s2
    ga = -gx * c2
    return MuonCouplings(
        g_x=gx,
        theta_mu_r=theta,
        g_vector=gv,
        g_axial=ga,
        g_left=gv - ga,
        g_right=gv + ga,
    )


def neutrino_couplings(g_x: float) -> tuple[float, float]:
    """Return (g_nu_mu, g_nu_tau); these do not depend on theta_mu_r."""
    gx = float(g_x)
    if not math.isfinite(gx) or gx < 0.0:
        raise ValueError("g_x must be finite and nonnegative")
    return gx, -gx
