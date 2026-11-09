"""Finite-width scalar line-shape convolution with analysis-specific response inputs.

The module is deliberately data-driven. It requires mass-dependent response
parameters and production-times-efficiency tables; it does not invent Belle II
Crystal-Ball parameters or scalar efficiencies. Both Belle II papers describe
their fitted signal response as a sum of two Crystal Ball functions sharing
one mean, but the complete mass-dependent fit parameters are not in the
archived numerical limit supplements.

The input spectral density is proportional to
  dN/dq = 2 q^2 Gamma_f(q) [sigma_prod(q) epsilon(q)] /
          {pi [(q^2-ms^2)^2 + q^2 Gamma_tot(q)^2]}.
It is then convolved with a normalized two-component Crystal-Ball mixture.

The four-muon adapter uses M_R=sqrt(q^2-4m_mu^2); the tau-pair adapter uses
M_recoil=q. This computes a reconstructed signal shape, not a new CLs limit.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np

M_MU_GEV = 0.1056583755

_NUMERIC_RESPONSE_COLUMNS = (
    "mass_GeV", "fraction_1", "mean_bias_GeV", "sigma_fit_GeV",
    "sigma_1_GeV", "alpha_1", "n_1",
    "sigma_2_GeV", "alpha_2", "n_2",
)
_REQUIRED_RESPONSE_COLUMNS = _NUMERIC_RESPONSE_COLUMNS + ("tail_side_1", "tail_side_2")


def fourmu_observable_mass(true_mass_GeV):
    q = np.asarray(true_mass_GeV, dtype=float)
    if np.any(q <= 2.0 * M_MU_GEV):
        raise ValueError("four-muon reduced mass requires q > 2 m_mu")
    return np.sqrt(q*q - 4.0*M_MU_GEV**2)


def tautau_observable_mass(true_mass_GeV):
    return np.asarray(true_mass_GeV, dtype=float)


def crystal_ball_pdf(x, mean, sigma, alpha, n, tail_side="left"):
    """Normalized one-sided Crystal-Ball density."""
    if sigma <= 0 or alpha <= 0 or n <= 1:
        raise ValueError("sigma and alpha must be positive and n must exceed one")
    if tail_side not in ("left", "right"):
        raise ValueError("tail_side must be 'left' or 'right'")
    z = (np.asarray(x, dtype=float) - mean) / sigma
    A = (n/alpha)**n * math.exp(-0.5*alpha*alpha)
    B = n/alpha - alpha
    raw = np.exp(-0.5*z*z)
    if np.ndim(z) == 0:
        in_tail = (z < -alpha) if tail_side == "left" else (z > alpha)
        if in_tail:
            base = (B-z) if tail_side == "left" else (B+z)
            raw = A * base**(-n)
    else:
        mask = (z < -alpha) if tail_side == "left" else (z > alpha)
        base = (B-z[mask]) if tail_side == "left" else (B+z[mask])
        raw[mask] = A * base**(-n)
    norm = (
        (n/alpha)*math.exp(-0.5*alpha*alpha)/(n-1.0)
        + math.sqrt(math.pi/2.0)*(1.0 + math.erf(alpha/math.sqrt(2.0)))
    )
    return raw / (sigma*norm)


def two_crystal_ball_mixture_pdf(
    x, mean, fraction_1,
    sigma_1, alpha_1, n_1, tail_side_1,
    sigma_2, alpha_2, n_2, tail_side_2,
):
    """Two normalized Crystal-Ball components sharing a common mean."""
    if not 0.0 <= fraction_1 <= 1.0:
        raise ValueError("fraction_1 must lie in [0,1]")
    p1 = crystal_ball_pdf(x, mean, sigma_1, alpha_1, n_1, tail_side_1)
    p2 = crystal_ball_pdf(x, mean, sigma_2, alpha_2, n_2, tail_side_2)
    return fraction_1*p1 + (1.0-fraction_1)*p2


def load_response_table(path: Path):
    """Load a mass-dependent two-CB response table; reject missing parameters."""
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("response table has no header")
        names = [x.strip() for x in reader.fieldnames]
        if any(x not in names for x in _REQUIRED_RESPONSE_COLUMNS):
            raise ValueError(f"response table must contain columns {_REQUIRED_RESPONSE_COLUMNS}")
        rows = list(reader)
    if len(rows) < 2:
        raise ValueError("at least two mass-dependent response rows are required")
    rows = [{k.strip(): v for k, v in row.items()} for row in rows]
    data = {}
    for key in _NUMERIC_RESPONSE_COLUMNS:
        try:
            data[key] = np.array([float(row[key]) for row in rows], dtype=float)
        except (TypeError, ValueError):
            raise ValueError(f"response table contains missing/non-numeric {key}")
        if not np.all(np.isfinite(data[key])):
            raise ValueError(f"response table contains non-finite {key}")
    for key in ("tail_side_1", "tail_side_2"):
        sides = [row[key].strip().lower() for row in rows]
        if any(side not in ("left", "right") for side in sides):
            raise ValueError(f"{key} values must be left or right")
        if len(set(sides)) != 1:
            raise ValueError(f"{key} must be constant over the mass grid")
        data[key] = sides[0]

    order = np.argsort(data["mass_GeV"])
    for key in _NUMERIC_RESPONSE_COLUMNS:
        data[key] = data[key][order]
    if np.any(np.diff(data["mass_GeV"]) <= 0):
        raise ValueError("response mass grid must be strictly increasing")
    if np.any((data["fraction_1"] < 0) | (data["fraction_1"] > 1)):
        raise ValueError("fraction_1 must lie in [0,1]")
    for key in ("sigma_fit_GeV", "sigma_1_GeV", "sigma_2_GeV", "alpha_1", "alpha_2"):
        if np.any(data[key] <= 0):
            raise ValueError(f"{key} must be positive")
    for key in ("n_1", "n_2"):
        if np.any(data[key] <= 1):
            raise ValueError(f"{key} must exceed one")
    return data


def _interp_response(response_table, observable_mass):
    x = response_table["mass_GeV"]
    if np.min(observable_mass) < x[0] or np.max(observable_mass) > x[-1]:
        raise ValueError("response table does not cover the true-mass grid")
    out = {
        key: np.interp(observable_mass, x, response_table[key])
        for key in _NUMERIC_RESPONSE_COLUMNS if key != "mass_GeV"
    }
    out["tail_side_1"] = response_table["tail_side_1"]
    out["tail_side_2"] = response_table["tail_side_2"]
    return out


def convolve_finite_width(
    *,
    pole_mass_GeV: float,
    true_mass_grid_GeV,
    gamma_total_GeV,
    gamma_final_GeV,
    production_times_efficiency,
    reconstructed_mass_grid_GeV,
    response_table,
    observable_transform,
    fit_window_halfwidth_sigma: float,
):
    """Return normalized reconstructed spectrum and fit-window fraction.

    The true-mass grid carries running total/final widths and the
    production-times-efficiency product. The response table is keyed in the
    fitted observable variable (M_R for four-mu, recoil mass for tau-pair).
    """
    q = np.asarray(true_mass_grid_GeV, dtype=float)
    gt = np.asarray(gamma_total_GeV, dtype=float)
    gf = np.asarray(gamma_final_GeV, dtype=float)
    pe = np.asarray(production_times_efficiency, dtype=float)
    rec = np.asarray(reconstructed_mass_grid_GeV, dtype=float)

    if pole_mass_GeV <= 0 or fit_window_halfwidth_sigma <= 0:
        raise ValueError("pole mass and fit-window multiplier must be positive")
    if q.ndim != 1 or len(q) < 16 or np.any(np.diff(q) <= 0):
        raise ValueError("true mass grid must be strictly increasing with >=16 points")
    if not (q[0] < pole_mass_GeV < q[-1]):
        raise ValueError("true-mass grid must bracket the scalar pole mass")
    if any(a.shape != q.shape for a in (gt, gf, pe)):
        raise ValueError("width and production/efficiency arrays must match true mass grid")
    if rec.ndim != 1 or len(rec) < 16 or np.any(np.diff(rec) <= 0):
        raise ValueError("reconstructed mass grid must be strictly increasing")
    if not all(np.all(np.isfinite(a)) for a in (q, gt, gf, pe, rec)):
        raise ValueError("all input arrays must be finite")
    if np.any(gt <= 0) or np.any(gf < 0) or np.any(gf > gt*(1+1e-10)):
        raise ValueError("require Gamma_total>0 and 0<=Gamma_final<=Gamma_total")
    if np.any(pe < 0):
        raise ValueError("production-times-efficiency must be nonnegative")

    obs_true = np.asarray(observable_transform(q), dtype=float)
    response = _interp_response(response_table, obs_true)
    denom = (q*q-pole_mass_GeV**2)**2 + q*q*gt*gt
    spectral = 2.0*q*q*gf*pe / (math.pi*denom)
    if not np.any(spectral > 0):
        raise ValueError("spectral signal weight is identically zero")

    # Trapezoidal quadrature weights for a possibly nonuniform true-mass grid.
    weights = np.empty_like(q)
    weights[0] = 0.5*(q[1]-q[0])
    weights[-1] = 0.5*(q[-1]-q[-2])
    weights[1:-1] = 0.5*(q[2:]-q[:-2])

    shape = np.zeros_like(rec)
    for i in range(len(q)):
        if spectral[i] == 0:
            continue
        mean = obs_true[i] + response["mean_bias_GeV"][i]
        shape += weights[i]*spectral[i]*two_crystal_ball_mixture_pdf(
            rec, mean, response["fraction_1"][i],
            response["sigma_1_GeV"][i], response["alpha_1"][i],
            response["n_1"][i], response["tail_side_1"],
            response["sigma_2_GeV"][i], response["alpha_2"][i],
            response["n_2"][i], response["tail_side_2"],
        )

    total_true_weight = float(np.trapezoid(spectral, q))
    if total_true_weight <= 0 or not math.isfinite(total_true_weight):
        raise ValueError("true-mass signal weight has nonpositive normalization")
    # Normalize to the full true-mass signal weight, not the finite reconstructed
    # grid integral. The latter may omit Crystal-Ball tails outside the supplied grid.
    shape /= total_true_weight
    reconstructed_grid_fraction = float(np.trapezoid(shape, rec))

    pole_observable = float(np.asarray(observable_transform(
        np.array([pole_mass_GeV], dtype=float)
    ))[0])
    sigma_pole = float(np.interp(
        pole_observable, response_table["mass_GeV"], response_table["sigma_fit_GeV"]
    ))
    mean_bias_pole = float(np.interp(
        pole_observable, response_table["mass_GeV"], response_table["mean_bias_GeV"]
    ))
    fit_mean = pole_observable + mean_bias_pole
    fit_lo = fit_mean - fit_window_halfwidth_sigma*sigma_pole
    fit_hi = fit_mean + fit_window_halfwidth_sigma*sigma_pole
    if fit_lo < rec[0] or fit_hi > rec[-1]:
        raise ValueError("reconstructed-mass grid does not cover the full experimental fit window")
    mask = (rec >= fit_lo) & (rec <= fit_hi)
    fit_fraction = float(np.trapezoid(shape[mask], rec[mask]))
    return {
        "reconstructed_mass_GeV": rec,
        "normalized_spectrum_per_GeV": shape,
        "fit_window": (fit_lo, fit_hi),
        "fit_window_fraction": fit_fraction,
        "reconstructed_grid_fraction": reconstructed_grid_fraction,
        "observable_true_mass_GeV": obs_true,
        "spectral_weight_per_GeV": spectral,
        "total_production_times_efficiency_weight": total_true_weight,
        "status": "shape_only_no_CLs_reinterpretation",
    }


def convolve_fourmu(**kwargs):
    kwargs["observable_transform"] = fourmu_observable_mass
    kwargs["fit_window_halfwidth_sigma"] = 30.0  # Belle II fit interval: 60 sigma total
    return convolve_finite_width(**kwargs)


def convolve_tautau(**kwargs):
    kwargs["observable_transform"] = tautau_observable_mass
    kwargs["fit_window_halfwidth_sigma"] = 20.0  # Belle II fit interval: 40 sigma total
    return convolve_finite_width(**kwargs)
