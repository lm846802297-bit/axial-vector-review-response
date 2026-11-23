"""Independent literal scalar implementation of Blinov et al., arXiv:2511.09619v2.

This module intentionally does not import the production rates.py or transport.py.
It implements the published scalar prescription (Appendix B, Eqs. 17--35) as a
reproducibility reference. It does NOT claim that scalar opacity is equivalent
to mode-resolved propagation when the three opacities differ. All rates are
for unit g_{mu tau}; multiply rates by g^2.

Units: MeV, km at the API boundary, hbar=c=1 internally.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import expit
from numpy.polynomial.legendre import leggauss

M_MU = 105.6583755
ALPHA = 1.0 / 137.035999084
KM_TO_MEV_INV = 1.0e18 / 197.3269804
MEV2_TO_ERG_S = 1.602176634e-6 / 6.582119569e-22
HERE = Path(__file__).resolve().parent
DEFAULT_PROFILE = HERE.parent / "data" / "sfho188_digitized.csv"


def fermi_pair_average(mu, omega, temperature, velocity):
    """Blinov Eq. (25): angular average of f_1 f_2, independent antiderivative."""
    mu, omega, temperature, velocity = np.broadcast_arrays(
        np.asarray(mu, float), np.asarray(omega, float),
        np.asarray(temperature, float), np.asarray(velocity, float))
    if np.any(temperature <= 0) or np.any(omega <= 0):
        raise ValueError("Require positive temperature and mediator energy")
    half = omega * velocity / 2.0
    emin, emax = omega / 2.0 - half, omega / 2.0 + half
    width = 2.0 * half
    safe_width = np.where(width > 0.0, width, 1.0)
    mean_f = np.zeros_like(omega)
    for sign in (1.0, -1.0):
        mean_f += temperature / safe_width * (
            np.logaddexp(0.0, (sign * mu - emin) / temperature)
            - np.logaddexp(0.0, (sign * mu - emax) / temperature))
    inv_bose = np.exp(-omega / temperature) / (-np.expm1(-omega / temperature))
    result = (1.0 - mean_f) * inv_bose
    rest = (expit((mu - omega / 2.0) / temperature)
            * expit((-mu - omega / 2.0) / temperature))
    # Besides v -> 0, the antiderivative loses precision when omega/T is
    # tiny: the Fermi-angle average approaches one and 1-mean_f cancels.
    # The rest-limit angular average is accurate to O((omega/T)^2) here.
    result = np.where((velocity < 1.0e-7) | (omega / temperature < 1.0e-3),
                      rest, result)
    if np.any(result < -1.0e-12):
        raise FloatingPointError("Fermi-pair average became negative")
    return np.maximum(result, 0.0)


def decay_production(mass, omega, temperature, mu_numu, mu_mu):
    """Blinov Eqs. (23)--(28): summed neutrino and dimuon production rates."""
    mass, omega, temperature, mu_numu, mu_mu = np.broadcast_arrays(
        np.asarray(mass, float), np.asarray(omega, float),
        np.asarray(temperature, float), np.asarray(mu_numu, float),
        np.asarray(mu_mu, float))
    if np.any(mass <= 0) or np.any(omega < mass) or np.any(temperature <= 0):
        raise ValueError("Require mass>0, omega>=mass and T>0")
    velocity = np.sqrt(np.maximum(1.0 - (mass / omega) ** 2, 0.0))
    inu = (fermi_pair_average(mu_numu, omega, temperature, velocity)
           + fermi_pair_average(np.zeros_like(mu_numu), omega, temperature, velocity))
    neutrino = mass ** 2 / (8.0 * np.pi * omega) * inu

    dimuon = np.zeros_like(neutrino)
    open_channel = mass > 2.0 * M_MU
    if np.any(open_channel):
        beta = np.sqrt(np.maximum(1.0 - (2.0 * M_MU / mass[open_channel]) ** 2, 0.0))
        width = (mass[open_channel] / (12.0 * np.pi)
                 * (1.0 + 2.0 * M_MU ** 2 / mass[open_channel] ** 2) * beta)
        imumu = fermi_pair_average(
            mu_mu[open_channel], omega[open_channel], temperature[open_channel],
            velocity[open_channel] * beta)
        dimuon[open_channel] = 3.0 * mass[open_channel] / omega[open_channel] * width * imumu
    return neutrino, dimuon


def negative_muon_density_and_degeneracy(temperature, chemical_potential):
    """Blinov Eq. (33), using the single f_mu(E,mu_mu) species as printed."""
    temperature, chemical_potential = np.broadcast_arrays(
        np.asarray(temperature, float), np.asarray(chemical_potential, float))
    if np.any(temperature <= 0):
        raise ValueError("Temperature must be positive")
    density = np.empty_like(temperature)
    susceptibility = np.empty_like(temperature)
    for index in np.ndindex(temperature.shape):
        t = float(temperature[index])
        mu = float(chemical_potential[index])

        def occupation(p):
            return float(expit((mu - np.hypot(p, M_MU)) / t))

        # The outer SN profile reaches n_mu << 1e-9 MeV^3.  An absolute
        # tolerance of 1e-9 therefore lets QUADPACK stop before resolving
        # the dilute Fermi tail and can bias n_mu F_deg by O(10%).  Request
        # relative convergence for these positive integrals instead.
        n_int = quad(lambda p: p * p * occupation(p), 0.0, np.inf,
                     epsabs=0.0, epsrel=2e-9, limit=200)[0] / np.pi**2
        chi_int = quad(lambda p: p * p * occupation(p) * (1.0 - occupation(p)),
                       0.0, np.inf, epsabs=0.0, epsrel=2e-9, limit=200)[0] / np.pi**2
        density[index] = n_int
        susceptibility[index] = chi_int
    degeneracy = np.divide(susceptibility, density,
                           out=np.zeros_like(density), where=density > 0)
    return density, degeneracy


def compton_production(mass, omega, temperature, n_mu, f_deg):
    """Blinov Eqs. (30)--(32), no-recoil/nonrelativistic-muon prescription."""
    mass, omega, temperature, n_mu, f_deg = np.broadcast_arrays(
        np.asarray(mass, float), np.asarray(omega, float),
        np.asarray(temperature, float), np.asarray(n_mu, float),
        np.asarray(f_deg, float))
    if np.any(omega < mass) or np.any(temperature <= 0):
        raise ValueError("Require omega>=mass and T>0")
    velocity = np.sqrt(np.maximum(1.0 - (mass / omega) ** 2, 0.0))
    alpha_v = 1.0 / (4.0 * np.pi)
    sigma_mu_gamma_to_mu_v = (
        8.0 * np.pi * ALPHA * alpha_v / (3.0 * M_MU**2)
        * (1.0 + mass**2 / (2.0 * omega**2)) * velocity)
    bose = 1.0 / np.expm1(np.minimum(omega / temperature, 700.0))
    result = np.zeros_like(omega)
    moving = velocity > 0.0
    result[moving] = (
        n_mu[moving] * f_deg[moving] * (2.0 / velocity[moving])
        * bose[moving] * sigma_mu_gamma_to_mu_v[moving])
    return result


def local_rates(mass, omega, temperature, mu_numu, mu_mu):
    """Return scalar production/absorption components following Eqs. 23--35."""
    n_mu, f_deg = negative_muon_density_and_degeneracy(temperature, mu_mu)
    nu, dimuon = decay_production(mass, omega, temperature, mu_numu, mu_mu)
    compton = compton_production(mass, omega, temperature, n_mu, f_deg)
    production = nu + dimuon + compton
    x = np.asarray(omega, float) / np.asarray(temperature, float)
    absorption = np.exp(np.minimum(x, 700.0)) * production
    reduced_absorption = -np.expm1(-x) * absorption
    return {
        "neutrino_production": nu,
        "dimuon_production": dimuon,
        "compton_production": compton,
        "production": production,
        "absorption": absorption,
        "reduced_absorption": reduced_absorption,
        "n_mu": n_mu,
        "F_deg": f_deg,
    }


def radial_rule(radius_km, order):
    """Composite Gauss rule with fixed interfaces used to resolve the hot core."""
    if radius_km <= 0 or order < 8:
        raise ValueError("Require radius>0 and radial order>=8")
    interfaces = np.array([0., 5., 8., 10., 12., 15., 18., 20., 22., 24., radius_km])
    edges = np.unique(interfaces[(interfaces >= 0.0) & (interfaces <= radius_km)])
    if edges[0] != 0.0:
        edges = np.r_[0.0, edges]
    if edges[-1] != radius_km:
        edges = np.r_[edges, radius_km]
    x, w = leggauss(max(4, int(np.ceil(order / (len(edges) - 1)))))
    nodes, weights = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        nodes.append((a + b) / 2.0 + (b - a) * x / 2.0)
        weights.append((b - a) * w / 2.0)
    return np.concatenate(nodes), np.concatenate(weights)


def load_profile(path, radii):
    """Interpolate the archived reconstructed SFHo-18.8 profile."""
    data = np.genfromtxt(path, delimiter=",", names=True)
    required = ("r_km", "T_MeV", "mu_mu_MeV", "mu_numu_MeV", "lapse")
    if any(name not in data.dtype.names for name in required):
        raise ValueError(f"Profile must contain columns {required}")
    return {name: np.interp(radii, data["r_km"], data[column])
            for name, column in {
                "T": "T_MeV", "mu_mu": "mu_mu_MeV",
                "mu_numu": "mu_numu_MeV", "lapse": "lapse"}.items()}


def energy_weights(energies, lower_bounds):
    """Integrate a piecewise-linear energy integrand above radius-dependent cutoffs."""
    e = np.asarray(energies, float)
    lower = np.asarray(lower_bounds, float)[:, None]
    a = np.maximum(e[:-1], lower)
    b = np.broadcast_to(e[1:], a.shape)
    length = np.maximum(b - a, 0.0)
    slope = np.where(length > 0.0,
                     ((b - e[:-1])**2 - (a - e[:-1])**2) / (2.0 * np.diff(e)),
                     0.0)
    weights = np.zeros((len(lower), len(e)))
    weights[:, :-1] += length - slope
    weights[:, 1:] += slope
    return weights


def scalar_optical_depths(source_radii, radial_grid, reduced_absorption,
                          mass, energies, radius_km, angular_order=16,
                          path_order=32):
    """Blinov Eqs. (18)--(21): scalar opacity and full chord/direction average."""
    r = np.asarray(source_radii, float)[:, None]
    angles, angle_weights = leggauss(angular_order)
    path_x, path_w = leggauss(path_order)
    path_w = path_w / 2.0
    velocity = np.sqrt(np.maximum(1.0 - (mass / np.asarray(energies))**2, 0.0))
    columns = np.zeros((len(source_radii), len(angles), len(energies)))
    for ia, cosine in enumerate(angles):
        smax = -cosine * r + np.sqrt(
            radius_km**2 - r**2 + r**2 * cosine**2)
        s = smax * (1.0 + path_x[None, :]) / 2.0
        position = np.sqrt(np.maximum(
            r**2 + s**2 + 2.0 * r * s * cosine, 0.0))
        path_weights = smax * path_w[None, :]
        for ie in range(len(energies)):
            rate_along_path = np.interp(
                position.ravel(), radial_grid, reduced_absorption[:, ie]
            ).reshape(position.shape)
            columns[:, ia, ie] = (
                np.sum(path_weights * rate_along_path, axis=1)
                * KM_TO_MEV_INV / velocity[ie])
    return columns, angle_weights / 2.0


def evaluate_mass(mass, profile_path=DEFAULT_PROFILE, couplings=None,
                  radial_order=40, energy_order=100, angular_order=16,
                  path_order=32, radius_km=25.0, energy_offset=1000.0):
    """Independent literal Eq. (17) scan for one mediator mass."""
    if couplings is None:
        couplings = np.geomspace(1e-10, 1e-5, 121)
    couplings = np.asarray(couplings, float)
    if np.any(couplings <= 0):
        raise ValueError("Couplings must be positive")
    r, rw = radial_rule(radius_km, radial_order)
    radial_grid = np.unique(np.r_[0.0, r, radius_km])
    p = load_profile(profile_path, radial_grid)
    energies = mass + np.geomspace(max(mass * 1e-6, 1e-6), energy_offset, energy_order)
    energies = np.unique(np.r_[energies, mass / p["lapse"]])
    energies = energies[energies > mass * (1.0 + 1e-10)]
    energies.sort()

    rates = local_rates(mass, energies[None, :],
                        p["T"][:, None], p["mu_numu"][:, None],
                        p["mu_mu"][:, None])
    columns, angle_weights = scalar_optical_depths(
        r, radial_grid, rates["reduced_absorption"], mass, energies,
        radius_km, angular_order, path_order)
    escape_by_coupling = lambda g: np.einsum(
        "rae,a->re", np.exp(-g**2 * columns), angle_weights)

    source_index = np.searchsorted(radial_grid, r)
    lapse = p["lapse"][source_index]
    production = rates["production"][source_index]
    lower = mass / lapse
    eweights = energy_weights(energies, lower)
    momentum = np.sqrt(np.maximum(energies**2 - mass**2, 0.0))
    geometry = (4.0 * np.pi * (r * KM_TO_MEV_INV)**2
                * rw * KM_TO_MEV_INV * lapse**2)
    phase_space = momentum * energies**2 / (2.0 * np.pi**2)
    source = (geometry[:, None] * eweights * phase_space[None, :]
              * production * MEV2_TO_ERG_S)
    luminosities = np.array([
        g**2 * np.sum(source * escape_by_coupling(g)) for g in couplings
    ])
    return {
        "mass_MeV": float(mass),
        "couplings": couplings.tolist(),
        "luminosity_erg_s": luminosities.tolist(),
        "thin_luminosity_erg_s": float(np.sum(source)),
        "profile": str(Path(profile_path).name),
        "config": {
            "radial_order": radial_order, "energy_order": energy_order,
            "angular_order": angular_order, "path_order": path_order,
            "radius_km": radius_km, "energy_offset_MeV": energy_offset,
            "opacity": "literal scalar Appendix-B prescription",
            "muon_species": "single negative-muon distribution as printed in Eq. (33)",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path,
                        default=HERE / "outputs" / "blinov_literal_scan.json")
    parser.add_argument("--masses", default="1,10,100,200")
    parser.add_argument("--gmin", type=float, default=1e-10)
    parser.add_argument("--gmax", type=float, default=1e-5)
    parser.add_argument("--gcount", type=int, default=121)
    parser.add_argument("--nr", type=int, default=40)
    parser.add_argument("--ne", type=int, default=100)
    parser.add_argument("--na", type=int, default=16)
    parser.add_argument("--ns", type=int, default=32)
    parser.add_argument("--energy-offset", type=float, default=1000.0)
    args = parser.parse_args()
    couplings = np.geomspace(args.gmin, args.gmax, args.gcount)
    results = []
    for mass in (float(x) for x in args.masses.split(",")):
        result = evaluate_mass(
            mass, args.profile, couplings, args.nr, args.ne,
            args.na, args.ns, 25.0, args.energy_offset)
        results.append(result)
        peak = max(result["luminosity_erg_s"])
        print(f"m={mass:g} MeV: Lmax={peak:.6e} erg/s", flush=True)
    payload = {
        "source": "Blinov et al., arXiv:2511.09619v2, Appendix B, Eqs. (17)-(35)",
        "implementation": "independent scalar literal reference; no imports from production rates.py or transport.py",
        "run_commit_sha": os.environ.get("GITHUB_SHA"),
        "reference_code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "profile_sha256": hashlib.sha256(args.profile.read_bytes()).hexdigest(),
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
