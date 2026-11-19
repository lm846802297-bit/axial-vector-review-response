#!/usr/bin/env python3
"""Literal Croon et al. (2021) Sec. 3 / Eqs. (4.6)-(4.7) vector benchmark.

This is an isolated C0 transport lane. It deliberately does not import the
Blinov B.2/B.13 implementation and does not add a polarization, velocity,
lapse, redshift, or stimulated-emission convention from another paper.

The profile is the archived public-figure SFHo-18.8 reconstruction, not the
raw Garching simulation file used by Croon et al.; outputs are therefore
labelled preliminary public-profile reconstructions.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import cumulative_simpson, simpson
from scipy.special import expit


M_MU_MEV = 105.6583755
ALPHA_EM = 1.0 / 137.035999084
KM_TO_MEV_INV = 1.0e18 / 197.3269804
MEV2_TO_ERG_PER_S = 1.602176634e-6 / 6.582119569e-22
CROON_RAFFELT_ERG_PER_S = 3.0e52
R_FAR_KM = 100.0
RNU_T_MEV = 3.0
DEFAULT_PROFILE = (
    Path(__file__).resolve().parents[1] / "data" / "sfho188_digitized.csv"
)
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"

# The masses plotted in Croon et al. Fig. 2, converted to MeV.
CROON_MASSES_MEV = {
    "0.1 eV": 1.0e-7,
    "1 eV": 1.0e-6,
    "10 eV": 1.0e-5,
    "0.1 MeV": 0.1,
    "10 MeV": 10.0,
    "200 MeV": 200.0,
}
C_SEMICOMPTON_PER_G2 = 2.0 * ALPHA_EM / (3.0 * M_MU_MEV**2)


def bose_factor(omega_mev: np.ndarray, temperature_mev: np.ndarray) -> np.ndarray:
    """Bose occupation with a safe large-argument branch."""
    x = np.asarray(omega_mev, dtype=float) / np.asarray(temperature_mev, dtype=float)
    return 1.0 / np.expm1(np.minimum(x, 700.0))


def phase_space_weight(omega_mev: np.ndarray, mass_mev: float) -> np.ndarray:
    """Croon Eq. (3.2): k*omega^2/(2*pi^2), including the energy weight.

    Do not multiply this expression by another omega. The factor of omega in
    dP/dV is already included when d^3k is changed from k to omega.
    """
    omega = np.asarray(omega_mev, dtype=float)
    if np.any(omega < mass_mev):
        raise ValueError("Require omega >= mass")
    momentum = np.sqrt(np.maximum(omega**2 - mass_mev**2, 0.0))
    return momentum * omega**2 / (2.0 * np.pi**2)


def muon_susceptibility(
    temperature_mev: np.ndarray,
    chemical_potential_mev: np.ndarray,
    order: int = 256,
) -> np.ndarray:
    """Return n_mu*F_deg from Bollig Eq. (2), for the printed mu-minus species.

    n_mu F_deg = integral dp p^2 f_mu(1-f_mu)/pi^2.
    The spin multiplicity two is included. Antimuons are not added because
    Croon/Bollig's quoted F_deg is defined using the single f_mu species.
    """
    temperature, chemical_potential = np.broadcast_arrays(
        np.asarray(temperature_mev, dtype=float),
        np.asarray(chemical_potential_mev, dtype=float),
    )
    if np.any(temperature <= 0.0):
        raise ValueError("Temperature must be positive")
    if order < 32:
        raise ValueError("Momentum quadrature order must be at least 32")
    nodes, weights = leggauss(int(order))
    result = np.empty_like(temperature)
    for index in np.ndindex(temperature.shape):
        t = float(temperature[index])
        mu = float(chemical_potential[index])
        pmax = 20.0 * t
        p = 0.5 * pmax * (nodes + 1.0)
        energy = np.hypot(p, M_MU_MEV)
        occupation = expit((mu - energy) / t)
        result[index] = (
            0.5 * pmax
            * np.sum(weights * p**2 * occupation * (1.0 - occupation))
            / np.pi**2
        )
    return result


def croon_local_rates_per_g2(
    mass_mev: float,
    omega_mev: np.ndarray,
    temperature_mev: np.ndarray,
    muon_susceptibility_mev3: np.ndarray,
) -> dict[str, np.ndarray]:
    """Croon Eqs. (4.6)-(4.7), per g_Z'^2, with the printed conventions."""
    omega = np.asarray(omega_mev, dtype=float)
    temperature = np.asarray(temperature_mev, dtype=float)
    susceptibility = np.asarray(muon_susceptibility_mev3, dtype=float)
    if np.any(omega < mass_mev) or np.any(temperature <= 0.0):
        raise ValueError("Require omega >= mass and T > 0")

    bose = bose_factor(omega[None, :], temperature[:, None])
    momentum = np.sqrt(np.maximum(omega**2 - mass_mev**2, 0.0))
    velocity = np.divide(
        momentum, omega, out=np.zeros_like(momentum), where=omega > 0.0
    )

    # The Fig. 2 caption identifies the gauged U(1)_{L_mu-L_tau} model.
    # Eq. (4.6) is the generic one-flavour expression; Sec. 4.4 adds nu_tau,
    # so the Fig. 2 source and opacity both carry the explicit factor of two.
    neutrino_flavour_factor = 2.0
    neutrino = (
        neutrino_flavour_factor * mass_mev**2 / (12.0 * np.pi * omega[None, :]) * bose
    )

    # Croon Eq. (4.7): Thomson semi-Compton rate. The unpolarized Thomson
    # cross section is used literally; no extra initial-photon factor of two.
    semi_compton = (
        C_SEMICOMPTON_PER_G2
        * susceptibility[:, None]
        * velocity[None, :]
        * bose
    )

    # Detailed balance: Gamma_abs = exp(omega/T) Gamma_prod.
    # Since exp(omega/T) n_B = 1+n_B, this is stable numerically.
    neutrino_absorption = (
        neutrino_flavour_factor * mass_mev**2 / (12.0 * np.pi * omega[None, :]) * (1.0 + bose)
    )
    semi_compton_absorption = (
        C_SEMICOMPTON_PER_G2
        * susceptibility[:, None]
        * velocity[None, :]
        * (1.0 + bose)
    )
    return {
        "neutrino_production_per_g2": neutrino,
        "semi_compton_production_per_g2": semi_compton,
        "production_per_g2": neutrino + semi_compton,
        "neutrino_absorption_per_g2": neutrino_absorption,
        "semi_compton_absorption_per_g2": semi_compton_absorption,
        "absorption_per_g2": neutrino_absorption + semi_compton_absorption,
    }


def outer_vacuum_tau_per_g2(
    mass_mev: float, omega_mev: np.ndarray, rnu_km: float, rfar_km: float
) -> np.ndarray:
    """Croon outer vacuum-decay tail per g_Z'^2, including both L_mu-L_tau neutrino flavours."""
    if rfar_km < rnu_km:
        raise ValueError("R_far must be >= R_nu")
    omega = np.asarray(omega_mev, dtype=float)
    return (
        (rfar_km - rnu_km)
        * KM_TO_MEV_INV
        * 2.0
        * mass_mev**2
        / (12.0 * np.pi * omega)
    )


def load_and_sample_profile(
    profile_path: str | Path = DEFAULT_PROFILE,
    radial_step_km: float = 0.05,
) -> dict:
    """Load the public SFHo-18.8 reconstruction and build the C0 radial grid."""
    path = Path(profile_path)
    data = np.genfromtxt(path, delimiter=",", names=True)
    required = {"r_km", "T_MeV", "mu_mu_MeV"}
    if data.dtype.names is None or not required.issubset(data.dtype.names):
        raise ValueError(f"Profile must contain columns {sorted(required)}")
    r_src = np.asarray(data["r_km"], dtype=float)
    t_src = np.asarray(data["T_MeV"], dtype=float)
    mu_src = np.asarray(data["mu_mu_MeV"], dtype=float)
    if len(r_src) < 3 or np.any(np.diff(r_src) <= 0.0):
        raise ValueError("Profile radii must be strictly increasing")
    if radial_step_km <= 0.0:
        raise ValueError("Radial step must be positive")

    # The public profile ends at 25 km, slightly above T=3 MeV. Croon defines
    # R_nu by T=3 MeV, so extrapolate only the final short interval linearly.
    slope = (t_src[-1] - t_src[-2]) / (r_src[-1] - r_src[-2])
    if slope >= 0.0 or t_src[-1] <= RNU_T_MEV:
        raise ValueError("The final profile segment must cross T=3 MeV outward")
    rnu_km = r_src[-1] + (RNU_T_MEV - t_src[-1]) / slope
    if rnu_km <= r_src[-1]:
        raise ValueError("Invalid extrapolated neutrinosphere radius")

    # Preserve the last nonzero mu-minus profile point and the first zero point
    # so that the sharp end of the muon-rich region is not smeared by the grid.
    nonzero_mu = np.flatnonzero(mu_src > 0.0)
    if len(nonzero_mu) == 0:
        raise ValueError("No positive muon chemical potential in profile")
    last_mu = int(nonzero_mu[-1])
    r_mu_end = float(r_src[last_mu])
    r_mu_zero = float(r_src[min(last_mu + 1, len(r_src) - 1)])

    base = np.arange(0.0, rnu_km, radial_step_km)
    r_km = np.unique(np.r_[base, r_mu_end, r_mu_zero, rnu_km])
    temperature = np.interp(r_km, r_src, t_src)
    beyond = r_km > r_src[-1]
    temperature[beyond] = t_src[-1] + slope * (r_km[beyond] - r_src[-1])
    muon_chemical_potential = np.interp(r_km, r_src, mu_src)
    muon_chemical_potential[beyond] = 0.0
    if not np.isclose(temperature[-1], RNU_T_MEV, rtol=0.0, atol=1e-10):
        raise AssertionError("R_nu interpolation did not land at T=3 MeV")

    return {
        "profile_path": str(path),
        "profile_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "profile_source_rows": int(len(r_src)),
        "r_km": r_km,
        "temperature_mev": temperature,
        "muon_chemical_potential_mev": muon_chemical_potential,
        "muon_susceptibility_mev3": muon_susceptibility(
            temperature, muon_chemical_potential
        ),
        "rnu_km": float(rnu_km),
        "r_mu_end_km": r_mu_end,
        "r_mu_zero_km": r_mu_zero,
        "radial_step_km": float(radial_step_km),
    }


def energy_quadrature(
    mass_mev: float, max_temperature_mev: float, order: int
) -> tuple[np.ndarray, np.ndarray]:
    """Gauss rule for omega=m+Tmax*y^2, y in [0,6]."""
    if order < 32:
        raise ValueError("Energy quadrature order must be at least 32")
    x, w = leggauss(int(order))
    y = 3.0 * (x + 1.0)
    wy = 3.0 * w
    omega = mass_mev + max_temperature_mev * y**2
    domega_weights = wy * (2.0 * max_temperature_mev * y)
    return omega, domega_weights


def _rates_and_source(
    mass_mev: float, profile: dict, energy_order: int
) -> dict:
    r_km = profile["r_km"]
    temperature = profile["temperature_mev"]
    chi = profile["muon_susceptibility_mev3"]
    omega, energy_weights = energy_quadrature(
        mass_mev, float(np.max(temperature)), energy_order
    )
    rates = croon_local_rates_per_g2(mass_mev, omega, temperature, chi)
    phase = phase_space_weight(omega, mass_mev)
    r_nat = r_km * KM_TO_MEV_INV
    volume_phase = 4.0 * np.pi * r_nat[:, None] ** 2 * phase[None, :]
    source_nu = volume_phase * rates["neutrino_production_per_g2"]
    source_sc = volume_phase * rates["semi_compton_production_per_g2"]
    source_total = source_nu + source_sc
    tau_cumulative = cumulative_simpson(
        rates["absorption_per_g2"], x=r_nat, axis=0, initial=0.0
    )
    tau_inside = np.maximum(tau_cumulative[-1][None, :] - tau_cumulative, 0.0)
    thin_nu = np.dot(
        energy_weights, simpson(source_nu, x=r_nat, axis=0)
    ) * MEV2_TO_ERG_PER_S
    thin_sc = np.dot(
        energy_weights, simpson(source_sc, x=r_nat, axis=0)
    ) * MEV2_TO_ERG_PER_S
    return {
        "omega_mev": omega,
        "energy_weights": energy_weights,
        "r_nat": r_nat,
        "phase": phase,
        "source_total": source_total,
        "tau_inside_per_g2": tau_inside,
        "thin_neutrino_per_g2_erg_s": float(thin_nu),
        "thin_semi_compton_per_g2_erg_s": float(thin_sc),
    }


def luminosity_curve(
    mass_mev: float,
    couplings: np.ndarray,
    profile: dict,
    rfar_km: float = R_FAR_KM,
    energy_order: int = 160,
) -> np.ndarray:
    """Croon Eq. (3.4), using its own radial opacity prescription."""
    prepared = _rates_and_source(mass_mev, profile, energy_order)
    omega = prepared["omega_mev"]
    rnu = float(profile["rnu_km"])
    tau_outer = outer_vacuum_tau_per_g2(mass_mev, omega, rnu, rfar_km)
    total_tau = prepared["tau_inside_per_g2"] + tau_outer[None, :]
    result = np.empty(len(couplings), dtype=float)
    for i, coupling in enumerate(np.asarray(couplings, dtype=float)):
        attenuation = np.exp(-coupling**2 * total_tau)
        l_omega = simpson(
            prepared["source_total"] * attenuation,
            x=prepared["r_nat"],
            axis=0,
        )
        result[i] = (
            coupling**2
            * np.dot(prepared["energy_weights"], l_omega)
            * MEV2_TO_ERG_PER_S
        )
    return result


def thin_channel_fractions(
    mass_mev: float, profile: dict, energy_order: int = 160
) -> dict[str, float]:
    """Optically-thin source fractions, before any escape/attenuation factor."""
    prepared = _rates_and_source(mass_mev, profile, energy_order)
    nu = prepared["thin_neutrino_per_g2_erg_s"]
    sc = prepared["thin_semi_compton_per_g2_erg_s"]
    total = nu + sc
    return {
        "neutrino_fraction": float(nu / total),
        "semi_compton_fraction": float(sc / total),
        "neutrino_luminosity_per_g2_erg_s": float(nu),
        "semi_compton_luminosity_per_g2_erg_s": float(sc),
        "total_luminosity_per_g2_erg_s": float(total),
    }


def raffelt_crossings(
    couplings: np.ndarray,
    luminosity: np.ndarray,
    threshold: float = CROON_RAFFELT_ERG_PER_S,
) -> list[float]:
    """Log-log interpolation of every crossing of the stated luminosity line."""
    roots: list[float] = []
    for i in range(len(couplings) - 1):
        y0, y1 = float(luminosity[i]), float(luminosity[i + 1])
        if y0 <= 0.0 or y1 <= 0.0:
            continue
        if (y0 - threshold) * (y1 - threshold) < 0.0:
            x0, x1 = np.log10(couplings[i]), np.log10(couplings[i + 1])
            ly0, ly1 = np.log10(y0), np.log10(y1)
            root = 10.0 ** (
                x0 + (np.log10(threshold) - ly0) * (x1 - x0) / (ly1 - ly0)
            )
            roots.append(float(root))
    return roots


def compute_benchmark(
    profile_path: str | Path = DEFAULT_PROFILE,
    radial_step_km: float = 0.05,
    energy_order: int = 160,
    momentum_order: int = 256,
    coupling_count: int = 221,
) -> dict:
    profile = load_and_sample_profile(profile_path, radial_step_km)
    # Recompute chi with the requested momentum order, rather than silently
    # inheriting a fixed default from profile preparation.
    profile["muon_susceptibility_mev3"] = muon_susceptibility(
        profile["temperature_mev"],
        profile["muon_chemical_potential_mev"],
        order=momentum_order,
    )
    couplings = np.logspace(-11.0, 0.0, int(coupling_count))
    curves: dict[str, dict] = {}
    summary: dict[str, dict] = {}

    for label, mass in CROON_MASSES_MEV.items():
        luminosity = luminosity_curve(
            mass, couplings, profile, R_FAR_KM, energy_order
        )
        thin = thin_channel_fractions(mass, profile, energy_order)
        peak_index = int(np.argmax(luminosity))
        summary[label] = {
            "mass_mev": mass,
            "peak_g": float(couplings[peak_index]),
            "peak_luminosity_erg_s": float(luminosity[peak_index]),
            "raffelt_crossings_g": raffelt_crossings(couplings, luminosity),
            **thin,
        }
        curves[label] = {
            "mass_mev": mass,
            "g": couplings.tolist(),
            "L_erg_s": luminosity.tolist(),
        }
        if label == "0.1 eV":
            luminosity_rnu = luminosity_curve(
                mass, couplings, profile, float(profile["rnu_km"]), energy_order
            )
            curves["0.1 eV (Rfar=Rnu)"] = {
                "mass_mev": mass,
                "g": couplings.tolist(),
                "L_erg_s": luminosity_rnu.tolist(),
            }

    return {
        "status": "preliminary_public_profile_reconstruction_not_digitized_fig2_validation",
        "source_paper": "Croon et al., JHEP 01 (2021) 107, arXiv:2006.13942",
        "equations": ["Croon Eqs. (3.2)-(3.4)", "Croon Eqs. (4.6)-(4.7)"],
        "profile": {
            "path": profile["profile_path"],
            "sha256": profile["profile_sha256"],
            "source_rows": profile["profile_source_rows"],
            "radial_grid_points": int(len(profile["r_km"])),
            "radial_step_km": profile["radial_step_km"],
            "R_nu_km_from_T_equals_3_MeV": profile["rnu_km"],
            "last_nonzero_muon_profile_km": profile["r_mu_end_km"],
            "first_zero_muon_profile_km": profile["r_mu_zero_km"],
        },
        "transport": {
            "R_far_km": R_FAR_KM,
            "outer_opacity": "vacuum Zprime -> nu nu decay tail",
            "radial_optical_depth": "integral dr Gamma_abs; no extra 1/v",
            "volume_element": "4*pi*r^2 dr; no lapse/redshift factor",
            "detailed_balance": "Gamma_abs = exp(omega/T) Gamma_prod",
            "raffelt_line_erg_s": CROON_RAFFELT_ERG_PER_S,
        },
        "local_rate_conventions": {
            "neutrino": "Croon Eq. (4.6) generic one-flavour expression multiplied by two per Sec. 4.4 for the gauged L_mu-L_tau model shown in Fig. 2; zero neutrino chemical potentials",
            "semi_compton": "Croon Eq. (4.7), Thomson approximation, n_mu*F_deg from the single mu-minus distribution",
            "polarization": "no additional spin-1 polarization multiplier; the explicit factor two in neutrino source and opacity is the Sec. 4.4 nu_tau flavour multiplicity",
            "dimuon_channel": "closed for all plotted masses because 200 MeV < 2*m_mu",
        },
        "numerics": {
            "energy_order": int(energy_order),
            "momentum_order": int(momentum_order),
            "coupling_count": int(coupling_count),
            "coupling_min": float(couplings[0]),
            "coupling_max": float(couplings[-1]),
            "radial_integrator": "cumulative_simpson for optical depth; simpson for volume integral",
            "energy_map": "omega = m + Tmax*y^2, y in [0,6]",
        },
        "summary": summary,
        "curves": curves,
        "limitations": [
            "The profile is a Caputo-based public-figure reconstruction cross-checked against Bollig, not the raw Garching profile used by Croon.",
            "No digitized Croon Fig. 2 points have yet been fitted or compared quantitatively.",
            "This is the Croon-literal vector lane, not the corrected B.13 lane and not an axial-vector result.",
            "No kinetic mixing, gravitational lapse/redshift, Blinov B.2 transport, or Lai trapping prescription is included.",
        ],
    }


def write_outputs(result: dict, output_dir: str | Path = DEFAULT_OUTPUT_DIR) -> tuple[Path, Path]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    json_path = output / "croon_fig2_literal_transport_preliminary_2026-11-19.json"
    csv_path = output / "croon_fig2_literal_transport_preliminary_2026-11-19.csv"
    json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    labels = list(result["curves"])
    first = result["curves"][labels[0]]["g"]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["g_Zprime"] + labels)
        for i, g in enumerate(first):
            writer.writerow(
                [g] + [result["curves"][label]["L_erg_s"][i] for label in labels]
            )
    return json_path, csv_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", default=str(DEFAULT_PROFILE))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--radial-step-km", type=float, default=0.05)
    parser.add_argument("--energy-order", type=int, default=160)
    parser.add_argument("--momentum-order", type=int, default=256)
    parser.add_argument("--coupling-count", type=int, default=221)
    args = parser.parse_args()

    result = compute_benchmark(
        profile_path=args.profile,
        radial_step_km=args.radial_step_km,
        energy_order=args.energy_order,
        momentum_order=args.momentum_order,
        coupling_count=args.coupling_count,
    )
    json_path, csv_path = write_outputs(result, args.output_dir)
    print(json.dumps({
        "status": result["status"],
        "profile": result["profile"],
        "summary": result["summary"],
        "json": str(json_path),
        "csv": str(csv_path),
    }, indent=2))


if __name__ == "__main__":
    main()
