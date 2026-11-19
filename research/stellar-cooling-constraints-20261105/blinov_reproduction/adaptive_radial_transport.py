#!/usr/bin/env python3
"""Independent adaptive radial integration for supernova surface escape layers.

The source and reduced opacity are interpolated separately with shape-preserving
PCHIP polynomials. The optical depth is the exact antiderivative of the opacity
interpolant. The attenuated radial integral is then evaluated by QUADPACK's
adaptive Gauss-Kronrod routine, with explicit split points at fixed optical
depth layers so a thin R_nu boundary layer cannot be missed by a fixed grid.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq


_OPTICAL_DEPTH_LEVELS = (
    80.0, 64.0, 48.0, 32.0, 16.0, 8.0, 4.0, 2.0, 1.0,
    0.5, 0.1, 0.01,
)


class AdaptiveRadialProfile:
    """Continuous radial source/opacity representation for one (omega, mode).

    radius_nat is in MeV^-1. source_per_g2 includes 4*pi*r^2 and phase space,
    while reduced_opacity_per_g2 is Gamma_abs-Gamma_prod; both omit g_X^2.

    integrate(g_X) returns g_X^2 * integral dr S exp[-g_X^2 tau_inside].
    An optional outer optical depth is applied as a separate exact exponential.
    """

    def __init__(self, radius_nat, source_per_g2, reduced_opacity_per_g2):
        radius = np.asarray(radius_nat, dtype=float)
        source = np.asarray(source_per_g2, dtype=float)
        opacity = np.asarray(reduced_opacity_per_g2, dtype=float)

        if radius.ndim != 1 or source.shape != radius.shape or opacity.shape != radius.shape:
            raise ValueError("radius, source, and opacity must be one-dimensional arrays of equal length")
        if radius.size < 3 or not np.all(np.isfinite(radius)):
            raise ValueError("at least three finite radial nodes are required")
        if not np.all(np.isfinite(source)) or not np.all(np.isfinite(opacity)):
            raise ValueError("source and opacity must be finite")
        if np.any(np.diff(radius) <= 0.0):
            raise ValueError("radius must be strictly increasing")
        if np.any(source < 0.0) or np.any(opacity < 0.0):
            raise ValueError("source and reduced opacity must be nonnegative")

        self.length = float(radius[-1] - radius[0])
        if not math.isfinite(self.length) or self.length <= 0.0:
            raise ValueError("radial interval must have positive finite length")

        # Normalize to [0,1] to avoid loss of precision for radii of order
        # 10^16--10^17 MeV^-1.
        self.x = (radius - radius[0]) / self.length
        self.source_values = source.copy()
        self.opacity_values = opacity.copy()
        self.source_spline = PchipInterpolator(self.x, source, extrapolate=False)
        self.opacity_spline = PchipInterpolator(
            self.x, opacity * self.length, extrapolate=False
        )
        self.opacity_antiderivative = self.opacity_spline.antiderivative()

        opacity_integral_at_surface = float(self.opacity_antiderivative(1.0))
        opacity_integral_at_center = float(self.opacity_antiderivative(0.0))
        self.tau0 = opacity_integral_at_surface - opacity_integral_at_center
        tolerance = 128.0 * np.finfo(float).eps * max(
            abs(opacity_integral_at_surface),
            abs(opacity_integral_at_center),
            1.0,
        )
        if self.tau0 < -tolerance:
            raise ValueError("interpolated reduced opacity gives negative optical depth")
        self.tau0 = max(self.tau0, 0.0)
        self.tau_knots = np.maximum(
            opacity_integral_at_surface
            - np.asarray(self.opacity_antiderivative(self.x), dtype=float),
            0.0,
        )
        if np.any(np.diff(self.tau_knots) > tolerance):
            raise ValueError("interpolated optical depth is not monotone")

        self._opacity_integral_at_surface = opacity_integral_at_surface
        self._max_source = float(np.max(source))

    def tau(self, x):
        """Optical depth from normalized radius x to the R_nu boundary."""
        value = (
            self._opacity_integral_at_surface
            - float(self.opacity_antiderivative(float(x)))
        )
        return max(value, 0.0)

    @property
    def surface_source_over_opacity(self):
        """High-coupling surface limit S(R_nu)/kappa(R_nu), if finite."""
        surface_opacity = float(self.opacity_values[-1])
        if surface_opacity <= 0.0:
            return None
        return float(self.source_values[-1] / surface_opacity)

    def integrate(self, g_x, tau_outer=0.0, epsrel=1.0e-8):
        """Return the adaptive radial integral and its absolute error estimate.

        The returned quantity is
            g_X^2 exp[-g_X^2 tau_outer] integral dr S(r) exp[-g_X^2 tau(r)].
        """
        coupling = float(g_x)
        outer_tau = float(tau_outer)
        relative_tolerance = float(epsrel)
        if not math.isfinite(coupling) or coupling < 0.0:
            raise ValueError("g_X must be finite and nonnegative")
        if not math.isfinite(outer_tau) or outer_tau < 0.0:
            raise ValueError("outer optical depth must be finite and nonnegative")
        if (
            not math.isfinite(relative_tolerance)
            or relative_tolerance < 50.0 * np.finfo(float).eps
        ):
            raise ValueError("epsrel is below QUADPACK's supported relative tolerance")

        coupling2 = coupling * coupling
        outer_exponent = coupling2 * outer_tau
        if coupling2 == 0.0 or self._max_source == 0.0 or outer_exponent > 745.0:
            return 0.0, 0.0

        points = []
        scaled_total_tau = coupling2 * self.tau0
        if scaled_total_tau > 80.0:
            active = (
                (self.tau_knots <= 80.0 / coupling2)
                & (self.tau_knots > 0.0)
                & (self.x > 0.0)
                & (self.x < 1.0)
            )
            points.extend(self.x[active].tolist())

            # Resolve the optically thin escape layer explicitly. Roots are
            # found on the monotone opacity antiderivative, not sampled tau.
            for level in _OPTICAL_DEPTH_LEVELS:
                target_tau = level / coupling2
                if 0.0 < target_tau < self.tau0:
                    try:
                        root = brentq(
                            lambda z: self.tau(z) - target_tau,
                            0.0,
                            1.0,
                            xtol=1.0e-14,
                            rtol=4.0 * np.finfo(float).eps,
                        )
                    except ValueError:
                        continue
                    if 0.0 < root < 1.0:
                        points.append(float(root))

        # Deduplicate only at floating-point resolution. A wider cut could
        # erase the very thin layer that this routine is designed to resolve.
        points.sort()
        unique_points = []
        minimum_spacing = 64.0 * np.finfo(float).eps
        for point in points:
            if (
                minimum_spacing < point < 1.0 - minimum_spacing
                and (
                    not unique_points
                    or point - unique_points[-1] > minimum_spacing
                )
            ):
                unique_points.append(point)

        def integrand(x):
            exponent = coupling2 * self.tau(x)
            if exponent > 745.0:
                return 0.0
            return float(self.source_spline(x)) * math.exp(-exponent)

        value, error = quad(
            integrand,
            0.0,
            1.0,
            points=unique_points or None,
            epsabs=0.0,
            epsrel=relative_tolerance,
            limit=max(300, len(unique_points) + 100),
        )
        prefactor = coupling2 * self.length * math.exp(-outer_exponent)
        return float(prefactor * value), float(prefactor * error)
