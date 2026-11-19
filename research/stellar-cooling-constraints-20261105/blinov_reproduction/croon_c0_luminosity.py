"""Croon-literal C0 luminosity adapter for the mV=10 MeV public SFHo profile.

Implements Croon Eqs. (3.2)-(3.4), (4.6), and (4.7) literally:
flat 4*pi*r^2 dr volume, radial optical depth without 1/vV, no angular
escape average, no lapse/redshift, and the analytic outer neutrino vacuum tail.

The muon susceptibility n_mu*Fdeg is reconstructed from the tabulated
(mu_mu,T) using a free relativistic Fermi gas. This is a public-profile
reconstruction, not the raw Garching n_mu/Fdeg table.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from numpy.polynomial.legendre import leggauss

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from finite_mixing.b13_b16_comparison import muon_density_and_susceptibility

DEFAULT_PROFILE = HERE.parent / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "croon_c0_luminosity_10mev_2026-11-19.json"

M_MU = 105.6583755
ALPHA_EM = 1.0 / 137.035999084
R_FAR_KM = 100.0
T_NU_MEV = 3.0
MEV_INV_PER_KM = 1.0e5 / (197.3269804e-13)
MEV2_TO_ERG_PER_SECOND = 1.602176634e-6 / 6.582119569e-22


def _bose(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    ex = np.exp(-x)
    return ex / (-np.expm1(-x))


def neutrinosphere_radius(r_km: np.ndarray, temperature: np.ndarray,
                          cutoff_MeV: float = T_NU_MEV) -> float:
    r = np.asarray(r_km, float)
    t = np.asarray(temperature, float)
    crossings = np.where((t[:-1] - cutoff_MeV) * (t[1:] - cutoff_MeV) <= 0.0)[0]
    candidates = [int(i) for i in crossings if t[i] >= cutoff_MeV and t[i+1] <= cutoff_MeV]
    if candidates:
        i = candidates[-1]
        f = (cutoff_MeV - t[i]) / (t[i+1] - t[i])
        return float(r[i] + f * (r[i+1] - r[i]))
    if not (t[-2] > cutoff_MeV and t[-1] > cutoff_MeV and t[-1] < t[-2]):
        raise ValueError("No outward T=3 MeV crossing or valid final-cell extrapolation")
    return float(r[-1] + (cutoff_MeV - t[-1]) * (r[-1] - r[-2]) / (t[-1] - t[-2]))


def vectorized_muon_susceptibility(
    temperature_MeV: np.ndarray,
    mu_mu_MeV: np.ndarray,
    order: int = 128,
    include_antimuons: bool = False,
) -> np.ndarray:
    """Return chi_mu = n_mu Fdeg for mu- only, as in Bollig Eq. (2).

    Set include_antimuons=True only for a separate charge-conjugate sensitivity
    test; Croon's baseline n_mu Fdeg is the simulated negative-muon population.
    """
    temp = np.asarray(temperature_MeV, dtype=float)
    mu = np.asarray(mu_mu_MeV, dtype=float)
    if temp.ndim != 1 or mu.ndim != 1 or len(temp) != len(mu):
        raise ValueError("T and mu_mu must be equal-length one-dimensional arrays")
    if np.any(temp <= 0.0) or not np.all(np.isfinite(temp)) or not np.all(np.isfinite(mu)):
        raise ValueError("Require finite mu_mu and positive finite temperatures")
    if order < 8:
        raise ValueError("Susceptibility quadrature order must be >=8")

    z, weights = leggauss(order)
    x_max = np.maximum(36.0, np.maximum(np.abs(mu) - M_MU, 0.0) / temp + 36.0)
    t_max = np.sqrt(x_max)
    t = 0.5 * t_max[:, None] * (z[None, :] + 1.0)
    wt = 0.5 * t_max[:, None] * weights[None, :]
    x = t * t
    p = np.sqrt(temp[:, None] * x * (2.0 * M_MU + temp[:, None] * x))
    energy = M_MU + temp[:, None] * x
    radial = 2.0 * temp[:, None] * p * energy * t * wt / np.pi**2

    f_minus = np.exp(-np.logaddexp(0.0, (energy - mu[:, None]) / temp[:, None]))
    chi_minus = np.sum(radial * f_minus * (1.0 - f_minus), axis=1)
    if not include_antimuons:
        return chi_minus
    f_plus = np.exp(-np.logaddexp(0.0, (energy + mu[:, None]) / temp[:, None]))
    chi_plus = np.sum(radial * f_plus * (1.0 - f_plus), axis=1)
    return chi_minus + chi_plus


def outer_vacuum_neutrino_tau_per_g2(
    mass_MeV: float, omega_MeV: np.ndarray, r_nu_km: float,
    r_far_km: float = R_FAR_KM,
    neutrino_flavour_factor: float = 2.0,
) -> np.ndarray:
    """Croon Eq. (3.3) vacuum tail, doubled for the two Lmu-Ltau flavours."""
    omega = np.asarray(omega_MeV, dtype=float)
    if (mass_MeV <= 0.0 or np.any(omega < mass_MeV)
            or r_far_km < r_nu_km or neutrino_flavour_factor <= 0.0):
        raise ValueError("Invalid mass, energy, radial boundary, or flavour factor")
    length = (r_far_km - r_nu_km) * MEV_INV_PER_KM
    return neutrino_flavour_factor * length * mass_MeV**2 / (12.0 * np.pi * omega)


def _piecewise_linear_spherical_integral(r_mev_inv: np.ndarray, q_mev5: np.ndarray) -> float:
    r = np.asarray(r_mev_inv, dtype=float)
    q = np.asarray(q_mev5, dtype=float)
    a, b = r[:-1], r[1:]
    slope = np.diff(q) / np.diff(r)
    segment = q[:-1] * (b**3-a**3)/3.0 + slope * (
        (b**4-a**4)/4.0 - a*(b**3-a**3)/3.0
    )
    return float(4.0*np.pi*np.sum(segment))


def _extend_profile_to_rnu(
    rows, chi: np.ndarray, include_antimuons: bool = False
) -> tuple[np.ndarray, ...]:
    r = np.asarray(rows["r_km"], float)
    t = np.asarray(rows["T_MeV"], float)
    mu = np.asarray(rows["mu_mu_MeV"], float)
    r_nu = neutrinosphere_radius(r, t)
    mu_nu = float(mu[-1] + (mu[-1]-mu[-2])*(r_nu-r[-1])/(r[-1]-r[-2]))
    chi_nu = float(vectorized_muon_susceptibility(
        np.array([T_NU_MEV]), np.array([mu_nu]), order=128,
        include_antimuons=include_antimuons
    )[0])
    return (
        np.append(r, r_nu),
        np.append(t, T_NU_MEV),
        np.append(mu, mu_nu),
        np.append(chi, chi_nu),
        r_nu,
    )


def build_croon_optical_depth(
    mass_MeV: float,
    r_km: np.ndarray,
    temperature_MeV: np.ndarray,
    chi_mu_MeV3: np.ndarray,
    omega_grid_MeV: np.ndarray,
    r_far_km: float = R_FAR_KM,
    outer_temperature_envelope_MeV: float = 0.0,
    neutrino_flavour_factor: float = 2.0,
) -> np.ndarray:
    """Return tau_C(omega,r)/g_X^2 for all energies and source radii."""
    r = np.asarray(r_km, float)
    temp = np.asarray(temperature_MeV, float)
    chi = np.asarray(chi_mu_MeV3, float)
    omega = np.asarray(omega_grid_MeV, float)
    if len(r) != len(temp) or len(r) != len(chi) or np.any(np.diff(r) <= 0.0):
        raise ValueError("Radial inputs must have matching lengths and increasing r")
    if (np.any(omega < mass_MeV) or np.any(temp <= 0.0) or np.any(chi < 0.0)
            or neutrino_flavour_factor <= 0.0):
        raise ValueError("Unphysical optical-depth inputs")

    velocity = np.sqrt(np.maximum(1.0-(mass_MeV/omega)**2, 0.0))
    bose = _bose(omega[:, None] / temp[None, :])
    one_plus_bose = 1.0 + bose

    # Croon Eq. (4.6) absorption via detailed balance:
    # Gamma_abs/g^2 = mV^2/(12*pi*omega) * (1+f_B).
    kappa_nu = neutrino_flavour_factor * (mass_MeV**2/(12.0*np.pi*omega))[:, None] * one_plus_bose

    # Croon Eq. (4.7) absorption via detailed balance:
    # Gamma_abs/g^2 = 2 alpha_EM/(3 m_mu^2) * chi_mu * vV * (1+f_B).
    kappa_sc = (
        2.0*ALPHA_EM/(3.0*M_MU**2)
        * velocity[:, None] * chi[None, :] * one_plus_bose
    )
    kappa = kappa_nu + kappa_sc

    r_nat = r * MEV_INV_PER_KM
    increments = 0.5*(kappa[:, :-1]+kappa[:, 1:]) * np.diff(r_nat)[None, :]
    cumulative = np.concatenate(
        [np.cumsum(increments[:, ::-1], axis=1)[:, ::-1],
         np.zeros((len(omega), 1))],
        axis=1,
    )

    outer_length = (r_far_km-r[-1]) * MEV_INV_PER_KM
    if outer_length < 0.0:
        raise ValueError("Rfar must lie outside Rnu")
    if outer_temperature_envelope_MeV <= 0.0:
        outer_factor = np.ones_like(omega)
    else:
        outer_factor = 1.0 + _bose(omega/outer_temperature_envelope_MeV)
    outer_tail = (
        neutrino_flavour_factor * outer_length * mass_MeV**2/(12.0*np.pi*omega) * outer_factor
    )
    return cumulative + outer_tail[:, None]


def _local_energy_grid(mass: float, temperature: float, z: np.ndarray, w: np.ndarray):
    y = 3.0*(z+1.0)
    wy = 3.0*w
    omega = mass + temperature*y*y
    domega = 2.0*temperature*y*wy
    momentum = np.sqrt(np.maximum(omega*omega-mass*mass, 0.0))
    phase = domega*omega*omega*momentum/(2.0*np.pi**2)
    return omega, phase


def run_c0_luminosity(
    profile_path: Path = DEFAULT_PROFILE,
    mass_MeV: float = 10.0,
    couplings: np.ndarray | None = None,
    energy_order: int = 64,
    tau_grid_points: int = 301,
    susceptibility_order: int = 128,
    neutrino_flavour_factor: float = 2.0,
    include_antimuons: bool = False,
) -> dict:
    rows = np.genfromtxt(profile_path, delimiter=",", names=True)
    required = ("r_km", "T_MeV", "mu_mu_MeV")
    if any(k not in rows.dtype.names for k in required):
        raise ValueError(f"Profile must contain {required}")
    profile_hash = hashlib.sha256(profile_path.read_bytes()).hexdigest()

    chi = vectorized_muon_susceptibility(
        rows["T_MeV"], rows["mu_mu_MeV"], order=susceptibility_order,
        include_antimuons=include_antimuons
    )
    r, temp, mu, chi, r_nu = _extend_profile_to_rnu(
        rows, chi, include_antimuons=include_antimuons
    )
    t_max = float(np.max(temp))
    u_tau = np.linspace(0.0, 6.0, tau_grid_points)
    omega_tau = mass_MeV + t_max*u_tau*u_tau

    tau_vac = build_croon_optical_depth(
        mass_MeV, r, temp, chi, omega_tau,
        R_FAR_KM, outer_temperature_envelope_MeV=0.0,
        neutrino_flavour_factor=neutrino_flavour_factor
    )
    tau_T3 = build_croon_optical_depth(
        mass_MeV, r, temp, chi, omega_tau,
        R_FAR_KM, outer_temperature_envelope_MeV=T_NU_MEV,
        neutrino_flavour_factor=neutrino_flavour_factor
    )
    tau_Rnu = build_croon_optical_depth(
        mass_MeV, r, temp, chi, omega_tau,
        r_nu, outer_temperature_envelope_MeV=0.0,
        neutrino_flavour_factor=neutrino_flavour_factor
    )

    zE, wE = leggauss(energy_order)
    local = []
    for i in range(len(r)):
        omega, phase = _local_energy_grid(mass_MeV, float(temp[i]), zE, wE)
        fB = _bose(omega/temp[i])
        velocity = np.sqrt(np.maximum(1.0-(mass_MeV/omega)**2, 0.0))
        gamma_nu = neutrino_flavour_factor * mass_MeV**2/(12.0*np.pi*omega) * fB
        gamma_sc = (
            2.0*ALPHA_EM/(3.0*M_MU**2) * chi[i] * velocity * fB
        )
        tau_lo = np.interp(omega, omega_tau, tau_vac[:, i])
        tau_hi = np.interp(omega, omega_tau, tau_T3[:, i])
        tau_rnu = np.interp(omega, omega_tau, tau_Rnu[:, i])
        local.append({
            "phase": phase,
            "gamma_nu_per_g2": gamma_nu,
            "gamma_sc_per_g2": gamma_sc,
            "tau_vac_per_g2": tau_lo,
            "tau_T3_per_g2": tau_hi,
            "tau_Rnu_per_g2": tau_rnu,
        })

    r_nat = r*MEV_INV_PER_KM
    qfree_nu = np.asarray([
        np.dot(x["phase"], x["gamma_nu_per_g2"]) for x in local
    ])
    qfree_sc = np.asarray([
        np.dot(x["phase"], x["gamma_sc_per_g2"]) for x in local
    ])
    free_nu_nat = _piecewise_linear_spherical_integral(r_nat, qfree_nu)
    free_sc_nat = _piecewise_linear_spherical_integral(r_nat, qfree_sc)

    if couplings is None:
        couplings = np.logspace(-11.0, -7.0, 81)
    couplings = np.asarray(couplings, dtype=float)
    if np.any(couplings <= 0.0) or not np.all(np.isfinite(couplings)):
        raise ValueError("Couplings must be positive and finite")

    curve = []
    for g in couplings:
        g2 = float(g*g)
        record = {"g_X": float(g)}
        for label, tau_key in (("vacuum_tail", "tau_vac_per_g2"),
                               ("Rfar_Rnu", "tau_Rnu_per_g2"),
                               ("T3_outer_envelope", "tau_T3_per_g2")):
            q_nu = np.empty(len(r))
            q_sc = np.empty(len(r))
            for i, x in enumerate(local):
                attenuation = np.exp(-g2*x[tau_key])
                q_nu[i] = g2*np.dot(x["phase"], x["gamma_nu_per_g2"]*attenuation)
                q_sc[i] = g2*np.dot(x["phase"], x["gamma_sc_per_g2"]*attenuation)
            l_nu = _piecewise_linear_spherical_integral(r_nat, q_nu)*MEV2_TO_ERG_PER_SECOND
            l_sc = _piecewise_linear_spherical_integral(r_nat, q_sc)*MEV2_TO_ERG_PER_SECOND
            record[label] = {
                "L_nu_coalescence_erg_s": float(l_nu),
                "L_semi_compton_erg_s": float(l_sc),
                "L_total_erg_s": float(l_nu+l_sc),
            }
        curve.append(record)

    return {
        "title": "Croon Eq. (3.4) Lmu-Ltau two-neutrino-flavour luminosity adapter, mV=10 MeV",
        "profile_file": profile_path.name,
        "profile_sha256": profile_hash,
        "profile_rows": int(len(rows)),
        "mass_MeV": float(mass_MeV),
        "R_nu_km": float(r_nu),
        "R_far_km": float(R_FAR_KM),
        "neutrino_flavour_factor": float(neutrino_flavour_factor),
        "neutrino_flavour_source": "Croon et al., Sec. 4.4: L_mu-L_tau doubles both differential power Q and absorptive optical depth relative to the generic single-neutrino-flavour case",
        "temperature_max_MeV": t_max,
        "muon_susceptibility": {
            "definition": "chi_mu = int 2 d^3p/(2pi)^3 f_mu-(1-f_mu-); matches the single negative-muon species in Bollig Eq. (2) and Croon n_mu Fdeg",
            "charge_conjugate_mu_plus_included": bool(include_antimuons),
            "source": "reconstructed from the Caputo/Bollig-validated mu_mu and T profiles with a free relativistic Fermi gas; not raw Garching n_mu/Fdeg",
            "quadrature_order": int(susceptibility_order),
        },
        "Croon_literal_transport": {
            "optical_depth": "tau=integral_r^Rfar dr Gamma_abs; no explicit 1/vV",
            "volume_measure": "4*pi*r^2*dr",
            "lapse_redshift": "omitted",
            "angular_escape_average": "omitted",
            "outer_neutrino_opacity": "vacuum tail to Rfar=100 km; T=3 MeV outer thermal envelope is a separate sensitivity case; Rfar=Rnu is also reported",
            "outer_semicompton_opacity": "zero once muon susceptibility vanishes",
        },
        "quadrature": {
            "local_energy_order": int(energy_order),
            "optical_depth_energy_grid_points": int(tau_grid_points),
        },
        "free_streaming_channel_luminosity_per_g2_erg_s": {
            "nu_coalescence": float(free_nu_nat*MEV2_TO_ERG_PER_SECOND),
            "semi_compton": float(free_sc_nat*MEV2_TO_ERG_PER_SECOND),
            "total": float((free_nu_nat+free_sc_nat)*MEV2_TO_ERG_PER_SECOND),
        },
        "coupling_curve": curve,
        "scope": "Croon Eqs. (3.3)-(3.4), (4.6)-(4.7) with the Sec. 4.4 L_mu-L_tau two-neutrino-flavour factor; public-profile reconstruction, not a raw-Garching reproduction and not an axial-vector result",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=10.0)
    parser.add_argument("--energy-order", type=int, default=64)
    parser.add_argument("--tau-grid-points", type=int, default=301)
    parser.add_argument("--susceptibility-order", type=int, default=128)
    parser.add_argument("--neutrino-flavour-factor", type=float, default=2.0)
    parser.add_argument("--include-antimuons", action="store_true")
    args = parser.parse_args()
    result = run_c0_luminosity(
        args.profile, args.mass, energy_order=args.energy_order,
        tau_grid_points=args.tau_grid_points,
        susceptibility_order=args.susceptibility_order,
        neutrino_flavour_factor=args.neutrino_flavour_factor,
        include_antimuons=args.include_antimuons
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({
        "profile_sha256": result["profile_sha256"],
        "R_nu_km": result["R_nu_km"],
        "neutrino_flavour_factor": result["neutrino_flavour_factor"],
        "muon_susceptibility": result["muon_susceptibility"],
        "free_streaming_channel_luminosity_per_g2_erg_s": result["free_streaming_channel_luminosity_per_g2_erg_s"],
        "coupling_curve": result["coupling_curve"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
