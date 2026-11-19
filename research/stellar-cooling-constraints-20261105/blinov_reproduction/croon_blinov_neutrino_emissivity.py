"""Full-profile local emissivity comparison: Croon Eq. (4.6) vs Blinov B.7-B.10.

This integrates the energy-dependent local production rates over the massive-vector
phase space at each archived SFHo-18.8 profile radius. It is deliberately not
a radial luminosity, optical-depth, or transport calculation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

HERE = Path(__file__).resolve().parent
DEFAULT_PROFILE = HERE.parent / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "croon_blinov_neutrino_emissivity_profile_2026-11-19.json"


def _fermi(x: np.ndarray) -> np.ndarray:
    return np.exp(-np.logaddexp(0.0, np.asarray(x, dtype=float)))


def _bose(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    ex = np.exp(-x)
    return ex / (-np.expm1(-x))


def energy_phase_grid(mass: float, temperature: float, order: int = 64):
    """Gauss-Legendre integration in x=(omega-m)/T=y^2, x in [0,36]."""
    if mass <= 0.0 or temperature <= 0.0 or order < 8:
        raise ValueError("Require mass>0, temperature>0, and energy order>=8")
    z, w = leggauss(order)
    ymax = 6.0
    y = 0.5 * ymax * (z + 1.0)
    wy = 0.5 * ymax * w
    omega = mass + temperature * y * y
    domega = 2.0 * temperature * y * wy
    momentum = np.sqrt(np.maximum(omega * omega - mass * mass, 0.0))
    phase = domega * omega * omega * momentum / (2.0 * np.pi**2)
    return omega, phase


def local_rate_spectra(
    mass: float,
    temperature: float,
    mu_numu: float,
    mu_nutau: float = 0.0,
    energy_order: int = 64,
    angular_order: int = 128,
) -> dict:
    """Return per-g_X^2 local B.7 and Croon spectra and energy emissivities."""
    if not np.all(np.isfinite([mass, temperature, mu_numu, mu_nutau])):
        raise ValueError("Inputs must be finite")
    if mass <= 0.0 or temperature <= 0.0:
        raise ValueError("Require mass>0 and temperature>0")
    if energy_order < 8 or angular_order < 8:
        raise ValueError("Quadrature orders must be >=8")

    omega, phase = energy_phase_grid(mass, temperature, energy_order)
    cosine, angular_weights = leggauss(angular_order)
    angular_weights = angular_weights / 2.0

    velocity = np.sqrt(np.maximum(1.0 - (mass / omega) ** 2, 0.0))
    e_bar = omega[:, None] * (1.0 + velocity[:, None] * cosine[None, :]) / 2.0
    e_nu = omega[:, None] * (1.0 - velocity[:, None] * cosine[None, :]) / 2.0

    def pair_average(mu_nu: float) -> np.ndarray:
        f_bar = _fermi((e_bar + mu_nu) / temperature)
        f_nu = _fermi((e_nu - mu_nu) / temperature)
        return np.sum(f_bar * f_nu * angular_weights[None, :], axis=1)

    i_numu = pair_average(mu_numu)
    i_nutau = pair_average(mu_nutau)

    # B.7: one-flavour vacuum width alpha_V*m_V/6, times 3 to
    # convert the spin-averaged width into a polarization sum. The two
    # L_mu-L_tau flavours are then added explicitly.
    b7_rate = mass * mass / (8.0 * np.pi * omega) * (i_numu + i_nutau)

    # Croon Eq. (4.6), literally as printed: alpha_V*m_V^2/(3 omega)*f_B.
    croon_rate = mass * mass / (12.0 * np.pi * omega) * _bose(omega / temperature)

    q_b7 = float(np.dot(phase, b7_rate))
    q_croon = float(np.dot(phase, croon_rate))
    return {
        "omega_MeV": omega.tolist(),
        "phase_space_weights_MeV3": phase.tolist(),
        "I_numu": i_numu.tolist(),
        "I_nutau": i_nutau.tolist(),
        "B7_two_flavour_rate_per_g2_MeV": b7_rate.tolist(),
        "Croon_Eq46_rate_per_g2_MeV": croon_rate.tolist(),
        "Q_B7_two_flavour_per_g2_MeV5": q_b7,
        "Q_Croon_Eq46_per_g2_MeV5": q_croon,
        "Q_B7_over_Q_Croon": q_b7 / q_croon,
        "energy_order": int(energy_order),
        "angular_order": int(angular_order),
    }


def load_profile(path: Path) -> np.ndarray:
    rows = np.genfromtxt(path, delimiter=",", names=True)
    required = {"r_km", "T_MeV", "mu_numu_MeV", "lapse"}
    missing = required.difference(rows.dtype.names or ())
    if missing:
        raise ValueError(f"Profile missing columns: {sorted(missing)}")
    if not np.all(np.isfinite(rows["r_km"])) or not np.all(np.isfinite(rows["T_MeV"])):
        raise ValueError("Profile radius and temperature must be finite")
    if np.any(rows["T_MeV"] <= 0.0):
        raise ValueError("Profile temperatures must be positive")
    return rows


MEV_INV_PER_KM = 1.0e5 / (197.3269804e-13)
MEV2_TO_ERG_PER_SECOND = 1.602176634e-6 / 6.582119569e-22


def _piecewise_linear_spherical_integral(r_mev_inv: np.ndarray, q_mev5: np.ndarray) -> float:
    """Exact integral of 4*pi*r^2*Q(r) when Q is linear on each radial cell."""
    r = np.asarray(r_mev_inv, dtype=float)
    q = np.asarray(q_mev5, dtype=float)
    if r.ndim != 1 or q.ndim != 1 or len(r) != len(q) or len(r) < 2:
        raise ValueError("r and q must be one-dimensional arrays with equal length >=2")
    if not np.all(np.isfinite(r)) or not np.all(np.isfinite(q)):
        raise ValueError("r and q must be finite")
    if np.any(np.diff(r) <= 0.0) or np.any(q < 0.0):
        raise ValueError("r must increase strictly and q must be nonnegative")
    a = r[:-1]
    b = r[1:]
    slope = np.diff(q) / np.diff(r)
    segment = (
        q[:-1] * (b**3 - a**3) / 3.0
        + slope * ((b**4 - a**4) / 4.0 - a * (b**3 - a**3) / 3.0)
    )
    return float(4.0 * np.pi * np.sum(segment))


def free_streaming_volume_integral(
    r_km: np.ndarray,
    temperature_MeV: np.ndarray,
    q_b7_MeV5: np.ndarray,
    q_croon_MeV5: np.ndarray,
    neutrinosphere_temperature_MeV: float = 3.0,
) -> dict:
    """Croon Eq. (3.1) optically-thin neutrino-coalescence channel only.

    Uses the literal flat radial volume 4*pi*r^2 dr, no lapse/redshift, and
    linearly extrapolates the last profile cell to the T=3 MeV neutrinosphere.
    Returned luminosities are per g_X^2.
    """
    r = np.asarray(r_km, dtype=float)
    temp = np.asarray(temperature_MeV, dtype=float)
    qb = np.asarray(q_b7_MeV5, dtype=float)
    qc = np.asarray(q_croon_MeV5, dtype=float)
    if not (r.ndim == temp.ndim == qb.ndim == qc.ndim == 1):
        raise ValueError("Profile arrays must be one-dimensional")
    if not (len(r) == len(temp) == len(qb) == len(qc)) or len(r) < 2:
        raise ValueError("Profile arrays must have equal length >=2")
    if not np.all(np.isfinite(np.concatenate([r, temp, qb, qc]))):
        raise ValueError("Profile arrays must be finite")
    if np.any(np.diff(r) <= 0.0) or np.any(temp <= 0.0):
        raise ValueError("Radius must increase and temperatures must be positive")
    if np.any(qb < 0.0) or np.any(qc < 0.0):
        raise ValueError("Emissivities must be nonnegative")

    cutoff = float(neutrinosphere_temperature_MeV)
    crossings = np.where(
        (temp[:-1] - cutoff) * (temp[1:] - cutoff) <= 0.0
    )[0]
    if len(crossings):
        # The outermost downward crossing is the neutrinosphere.
        candidates = [
            int(i) for i in crossings
            if temp[i] >= cutoff and temp[i + 1] <= cutoff
        ]
        if not candidates:
            raise ValueError("No outward downward T=3 MeV crossing found")
        i = candidates[-1]
        fraction = (cutoff - temp[i]) / (temp[i + 1] - temp[i])
        r_nu = float(r[i] + fraction * (r[i + 1] - r[i]))
        keep = i + 1
        r_use = r[:keep].copy()
        qb_use = qb[:keep].copy()
        qc_use = qc[:keep].copy()
        if r_nu > r_use[-1]:
            qb_nu = float(qb[i] + fraction * (qb[i + 1] - qb[i]))
            qc_nu = float(qc[i] + fraction * (qc[i + 1] - qc[i]))
            r_use = np.append(r_use, r_nu)
            qb_use = np.append(qb_use, qb_nu)
            qc_use = np.append(qc_use, qc_nu)
    else:
        # Public digitization stops just above 3 MeV; extrapolate only the
        # final profile cell, recording that this is a boundary extension.
        if not (temp[-2] > cutoff and temp[-1] > cutoff and temp[-1] < temp[-2]):
            raise ValueError("T=3 MeV crossing is not bracketed and final profile is not extrapolatable")
        r_nu = float(
            r[-1] + (cutoff - temp[-1]) * (r[-1] - r[-2]) / (temp[-1] - temp[-2])
        )
        qb_nu = float(qb[-1] + (qb[-1] - qb[-2]) * (r_nu - r[-1]) / (r[-1] - r[-2]))
        qc_nu = float(qc[-1] + (qc[-1] - qc[-2]) * (r_nu - r[-1]) / (r[-1] - r[-2]))
        if qb_nu < 0.0 or qc_nu < 0.0:
            raise ValueError("Linear emissivity extrapolation became negative")
        r_use = np.append(r, r_nu)
        qb_use = np.append(qb, qb_nu)
        qc_use = np.append(qc, qc_nu)

    r_natural = r_use * MEV_INV_PER_KM
    lb_nat = _piecewise_linear_spherical_integral(r_natural, qb_use)
    lc_nat = _piecewise_linear_spherical_integral(r_natural, qc_use)
    lb = lb_nat * MEV2_TO_ERG_PER_SECOND
    lc = lc_nat * MEV2_TO_ERG_PER_SECOND
    trap_b = float(np.trapezoid(4.0 * np.pi * r_natural**2 * qb_use, r_natural))
    trap_c = float(np.trapezoid(4.0 * np.pi * r_natural**2 * qc_use, r_natural))
    return {
        "neutrinosphere_temperature_MeV": cutoff,
        "neutrinosphere_radius_km": r_nu,
        "profile_supported_outer_radius_km": float(r[-1]),
        "outer_boundary_extension_km": float(r_nu - r[-1]),
        "boundary_extension_Q_B7_MeV5": float(qb_use[-1]),
        "boundary_extension_Q_Croon_MeV5": float(qc_use[-1]),
        "volume_measure": "4*pi*r^2*dr; no lapse, redshift, opacity, or escape factor",
        "radial_interpolation": "piecewise-linear Q(r); analytic integration of 4*pi*r^2*Q(r)",
        "Q_B7_free_streaming_luminosity_per_g2_erg_s": float(lb),
        "Q_Croon_free_streaming_luminosity_per_g2_erg_s": float(lc),
        "Q_B7_over_Q_Croon_free_streaming_luminosity": float(lb / lc),
        "trapezoid_check_B7_erg_s_per_g2": float(trap_b * MEV2_TO_ERG_PER_SECOND),
        "trapezoid_check_Croon_erg_s_per_g2": float(trap_c * MEV2_TO_ERG_PER_SECOND),
        "trapezoid_relative_difference_B7": float(trap_b / lb_nat - 1.0),
        "trapezoid_relative_difference_Croon": float(trap_c / lc_nat - 1.0),
        "scope": "optically-thin neutrino-pair-coalescence channel only; not total SN luminosity or a cooling bound",
    }


def run_profile(
    profile_path: Path = DEFAULT_PROFILE,
    mass: float = 10.0,
    energy_order: int = 64,
    angular_order: int = 128,
    convergence_order: int = 96,
    convergence_angular_order: int = 256,
) -> dict:
    rows = load_profile(profile_path)
    profile_hash = hashlib.sha256(profile_path.read_bytes()).hexdigest()
    radial = []
    for row in rows:
        point = local_rate_spectra(
            mass, float(row["T_MeV"]), float(row["mu_numu_MeV"]), 0.0,
            energy_order, angular_order
        )
        radial.append({
            "r_km": float(row["r_km"]),
            "T_MeV": float(row["T_MeV"]),
            "mu_numu_MeV": float(row["mu_numu_MeV"]),
            "lapse": float(row["lapse"]),
            "Q_B7_two_flavour_per_g2_MeV5": point["Q_B7_two_flavour_per_g2_MeV5"],
            "Q_Croon_Eq46_per_g2_MeV5": point["Q_Croon_Eq46_per_g2_MeV5"],
            "Q_B7_over_Q_Croon": point["Q_B7_over_Q_Croon"],
        })

    selected_radii = (0.0, 8.482141202, 12.5, 15.0, 22.0, 24.0)
    convergence = []
    for radius in selected_radii:
        index = int(np.argmin(np.abs(rows["r_km"] - radius)))
        row = rows[index]
        coarse = local_rate_spectra(
            mass, float(row["T_MeV"]), float(row["mu_numu_MeV"]), 0.0,
            energy_order, angular_order
        )
        fine = local_rate_spectra(
            mass, float(row["T_MeV"]), float(row["mu_numu_MeV"]), 0.0,
            convergence_order, convergence_angular_order
        )
        convergence.append({
            "requested_radius_km": radius,
            "actual_radius_km": float(row["r_km"]),
            "coarse_energy_order": energy_order,
            "coarse_angular_order": angular_order,
            "fine_energy_order": convergence_order,
            "fine_angular_order": convergence_angular_order,
            "relative_Q_B7_change": (
                fine["Q_B7_two_flavour_per_g2_MeV5"]
                / coarse["Q_B7_two_flavour_per_g2_MeV5"] - 1.0
            ),
            "relative_Q_Croon_change": (
                fine["Q_Croon_Eq46_per_g2_MeV5"]
                / coarse["Q_Croon_Eq46_per_g2_MeV5"] - 1.0
            ),
            "coarse_ratio": coarse["Q_B7_over_Q_Croon"],
            "fine_ratio": fine["Q_B7_over_Q_Croon"],
        })

    ratios = np.asarray([p["Q_B7_over_Q_Croon"] for p in radial])
    volume_integral = free_streaming_volume_integral(
        rows["r_km"], rows["T_MeV"],
        np.asarray([p["Q_B7_two_flavour_per_g2_MeV5"] for p in radial]),
        np.asarray([p["Q_Croon_Eq46_per_g2_MeV5"] for p in radial]),
    )
    min_index = int(np.argmin(ratios))
    max_index = int(np.argmax(ratios))
    return {
        "title": "Full-profile local emissivity: Blinov B.7-B.10 versus Croon Eq. (4.6)",
        "mass_MeV": float(mass),
        "profile_file": profile_path.name,
        "profile_sha256": profile_hash,
        "profile_row_count": int(len(rows)),
        "radial_domain_km": [float(rows["r_km"][0]), float(rows["r_km"][-1])],
        "flavour_assumptions": {
            "nu_mu": "mu_numu_MeV interpolated from archived SFHo-18.8 profile",
            "nu_tau": "mu_nutau=0, following the Blinov profile convention",
        },
        "normalization": {
            "B7": "mV^2/(8*pi*omega)*(I_numu+I_nutau) per g_X^2",
            "Croon_Eq46": "mV^2/(12*pi*omega)*1/(exp(omega/T)-1) per g_X^2",
            "ratio": "Q_B7/Q_Croon after the same massive-vector phase-space integral",
            "phase_space": "domega*omega^2*sqrt(omega^2-mV^2)/(2*pi^2), x=(omega-mV)/T in [0,36]",
        },
        "quadrature": {
            "energy_order": int(energy_order),
            "angular_order": int(angular_order),
            "selected_convergence_energy_order": int(convergence_order),
            "selected_convergence_angular_order": int(convergence_angular_order),
        },
        "radial_summary": {
            "minimum_ratio": float(ratios[min_index]),
            "minimum_ratio_radius_km": radial[min_index]["r_km"],
            "maximum_ratio": float(ratios[max_index]),
            "maximum_ratio_radius_km": radial[max_index]["r_km"],
        },
        "free_streaming_volume_integral": volume_integral,
        "selected_convergence": convergence,
        "radial_local_emissivity": radial,
        "scope": "local energy-integrated emissivity only; no radial volume integral, optical depth, escape probability, or luminosity",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--energy-order", type=int, default=64)
    parser.add_argument("--angular-order", type=int, default=128)
    parser.add_argument("--convergence-order", type=int, default=96)
    parser.add_argument("--convergence-angular-order", type=int, default=256)
    args = parser.parse_args()
    result = run_profile(
        args.profile, args.mass, args.energy_order, args.angular_order,
        args.convergence_order, args.convergence_angular_order
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "profile_sha256": result["profile_sha256"],
        "profile_row_count": result["profile_row_count"],
        "radial_summary": result["radial_summary"],
        "free_streaming_volume_integral": result["free_streaming_volume_integral"],
        "max_selected_Q_B7_relative_change": max(
            abs(p["relative_Q_B7_change"]) for p in result["selected_convergence"]
        ),
        "max_selected_Q_Croon_relative_change": max(
            abs(p["relative_Q_Croon_change"]) for p in result["selected_convergence"]
        ),
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
