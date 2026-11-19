"""Full source-weighted Croon C0 upper-envelope test for outer muon opacity.

The calculation asks whether a constant continuation of the last resolved
muon susceptibility can explain the solid/dashed 0.1 eV separation in Croon
Fig. 2. It uses the actual C0 radial source, local energy quadrature, detailed
balance, and source-radius-dependent optical depth. The continuation is a
conditional envelope, not a reconstructed Garching profile.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from croon_c0_luminosity import (
    ALPHA_EM,
    M_MU,
    MEV2_TO_ERG_PER_SECOND,
    MEV_INV_PER_KM,
    R_FAR_KM,
    T_NU_MEV,
    _bose,
    _local_energy_grid,
    _piecewise_linear_spherical_integral,
    build_croon_optical_depth,
    neutrinosphere_radius,
    vectorized_muon_susceptibility,
)

HERE = Path(__file__).resolve().parent
DEFAULT_PROFILE = HERE.parent / "data" / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "croon_outer_muon_opacity_envelope_2026-11-19.json"
DEFAULT_COUPLINGS = np.array([3e-6, 1e-5, 1e-4, 1e-3, 1e-2, 3e-2])
PAPER_MEDIAN_SOLID_DASHED_RATIO = 3.38190


def _prepare_profile(
    profile_path: Path, susceptibility_order: int, include_antimuons: bool = False
) -> dict:
    rows = np.genfromtxt(profile_path, delimiter=",", names=True)
    required = {"r_km", "T_MeV", "mu_mu_MeV"}
    if rows.dtype.names is None or not required.issubset(rows.dtype.names):
        raise ValueError(f"Profile must contain columns {sorted(required)}")

    r_src = np.asarray(rows["r_km"], dtype=float)
    temperature_src = np.asarray(rows["T_MeV"], dtype=float)
    mu_src = np.asarray(rows["mu_mu_MeV"], dtype=float)
    if len(r_src) < 3 or np.any(np.diff(r_src) <= 0.0):
        raise ValueError("Profile radii must be strictly increasing")

    r_nu = neutrinosphere_radius(r_src, temperature_src)
    mu_nu = float(
        mu_src[-1]
        + (mu_src[-1] - mu_src[-2])
        * (r_nu - r_src[-1]) / (r_src[-1] - r_src[-2])
    )
    chi_src = vectorized_muon_susceptibility(
        temperature_src, mu_src, order=susceptibility_order,
        include_antimuons=include_antimuons,
    )
    chi_nu = float(
        vectorized_muon_susceptibility(
            np.array([T_NU_MEV]),
            np.array([mu_nu]),
            order=susceptibility_order,
            include_antimuons=include_antimuons,
        )[0]
    )

    r = np.append(r_src, r_nu)
    temperature = np.append(temperature_src, T_NU_MEV)
    mu_mu = np.append(mu_src, mu_nu)
    chi = np.append(chi_src, chi_nu)
    edge_candidates = np.flatnonzero(mu_mu > 0.0)
    if len(edge_candidates) == 0:
        raise ValueError("The profile has no positive muon chemical-potential sample")
    edge = int(edge_candidates[-1])

    try:
        profile_label = str(profile_path.resolve().relative_to(HERE.parents[2].resolve()))
    except ValueError:
        profile_label = profile_path.name

    return {
        "r_km": r,
        "temperature_MeV": temperature,
        "mu_mu_MeV": mu_mu,
        "chi_mu_MeV3": chi,
        "r_nu_km": float(r_nu),
        "edge_index": edge,
        "r_edge_km": float(r[edge]),
        "T_edge_MeV": float(temperature[edge]),
        "mu_edge_MeV": float(mu_mu[edge]),
        "chi_edge_MeV3": float(chi[edge]),
        "profile_sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
        "profile_rows": int(len(rows)),
        "profile_path": profile_label,
        "include_antimuons": bool(include_antimuons),
    }


def _luminosity(r_nat: np.ndarray, source_weighted: np.ndarray,
                attenuation_tau: np.ndarray, coupling: float) -> float:
    attenuated = coupling**2 * np.sum(
        source_weighted * np.exp(-coupling**2 * attenuation_tau), axis=1
    )
    return (
        _piecewise_linear_spherical_integral(r_nat, attenuated)
        * MEV2_TO_ERG_PER_SECOND
    )


def run_outer_muon_opacity_envelope(
    profile_path: Path = DEFAULT_PROFILE,
    mass_MeV: float = 1.0e-7,
    couplings: np.ndarray = DEFAULT_COUPLINGS,
    energy_order: int = 96,
    tau_grid_points: int = 601,
    susceptibility_order: int = 256,
    neutrino_flavour_factor: float = 2.0,
    paper_ratio_target: float = PAPER_MEDIAN_SOLID_DASHED_RATIO,
    include_antimuons: bool = False,
) -> dict:
    """Run the source-weighted edge-envelope and effective-susceptibility tests."""
    profile_path = Path(profile_path)
    if mass_MeV <= 0.0 or energy_order < 32 or tau_grid_points < 31:
        raise ValueError("Require positive mass, energy order >=32, and tau grid >=31")
    if susceptibility_order < 32 or neutrino_flavour_factor <= 0.0:
        raise ValueError("Require susceptibility order >=32 and positive flavour factor")
    couplings = np.asarray(couplings, dtype=float)
    if couplings.ndim != 1 or len(couplings) == 0 or np.any(couplings <= 0.0):
        raise ValueError("Couplings must be a nonempty positive one-dimensional array")
    if np.any(np.diff(couplings) <= 0.0):
        raise ValueError("Couplings must be strictly increasing")

    profile = _prepare_profile(profile_path, susceptibility_order, include_antimuons)
    r = profile["r_km"]
    temperature = profile["temperature_MeV"]
    chi = profile["chi_mu_MeV3"]
    r_nu = profile["r_nu_km"]
    r_edge = profile["r_edge_km"]
    T_edge = profile["T_edge_MeV"]
    chi_edge = profile["chi_edge_MeV3"]
    r_nat = r * MEV_INV_PER_KM

    t_max = float(np.max(temperature))
    u_tau = np.linspace(0.0, 6.0, int(tau_grid_points))
    omega_tau = mass_MeV + t_max * u_tau**2
    tau_vac = build_croon_optical_depth(
        mass_MeV, r, temperature, chi, omega_tau,
        R_FAR_KM, neutrino_flavour_factor=neutrino_flavour_factor,
    )
    tau_rnu = build_croon_optical_depth(
        mass_MeV, r, temperature, chi, omega_tau,
        r_nu, neutrino_flavour_factor=neutrino_flavour_factor,
    )

    z_energy, w_energy = np.polynomial.legendre.leggauss(int(energy_order))
    n_r = len(r)
    source_weighted = np.empty((n_r, energy_order), dtype=float)
    tau_vac_local = np.empty_like(source_weighted)
    tau_rnu_local = np.empty_like(source_weighted)
    tau_outer_T3 = np.empty_like(source_weighted)
    tau_outer_Tedge = np.empty_like(source_weighted)
    chi_prefactor = 2.0 * ALPHA_EM / (3.0 * M_MU**2)
    length_T3 = (R_FAR_KM - r_nu) * MEV_INV_PER_KM
    length_edge = (R_FAR_KM - r_edge) * MEV_INV_PER_KM

    for i, (T_i, chi_i) in enumerate(zip(temperature, chi)):
        omega, phase = _local_energy_grid(
            mass_MeV, float(T_i), z_energy, w_energy
        )
        f_bose = _bose(omega / T_i)
        velocity = np.sqrt(np.maximum(1.0 - (mass_MeV / omega)**2, 0.0))
        gamma_nu = (
            neutrino_flavour_factor * mass_MeV**2
            / (12.0 * np.pi * omega) * f_bose
        )
        gamma_sc = chi_prefactor * chi_i * velocity * f_bose
        source_weighted[i] = phase * (gamma_nu + gamma_sc)
        tau_vac_local[i] = np.interp(omega, omega_tau, tau_vac[:, i])
        tau_rnu_local[i] = np.interp(omega, omega_tau, tau_rnu[:, i])
        tau_outer_T3[i] = (
            chi_prefactor * chi_edge * velocity
            * (1.0 + _bose(omega / T_NU_MEV)) * length_T3
        )
        tau_outer_Tedge[i] = (
            chi_prefactor * chi_edge * velocity
            * (1.0 + _bose(omega / T_edge)) * length_edge
        )

    luminosity_rows = []
    for coupling in couplings:
        L_vac = _luminosity(r_nat, source_weighted, tau_vac_local, float(coupling))
        L_rnu = _luminosity(r_nat, source_weighted, tau_rnu_local, float(coupling))
        L_T3 = _luminosity(
            r_nat, source_weighted, tau_vac_local + tau_outer_T3, float(coupling)
        )
        L_Tedge = _luminosity(
            r_nat, source_weighted, tau_vac_local + tau_outer_Tedge, float(coupling)
        )
        luminosity_rows.append({
            "g_X": float(coupling),
            "L_Rfar100_vacuum_tail_erg_s": L_vac,
            "L_RfarRnu_erg_s": L_rnu,
            "L_Rfar100_outer_chi_edge_T3_erg_s": L_T3,
            "L_Rfar100_outer_chi_edge_Tedge_erg_s": L_Tedge,
            "Rnu_over_vacuum_luminosity_ratio": L_rnu / L_vac,
            "vacuum_over_T3_envelope_luminosity_ratio": L_vac / L_T3,
            "vacuum_over_Tedge_envelope_luminosity_ratio": L_vac / L_Tedge,
            "Rnu_over_T3_envelope_luminosity_ratio": L_rnu / L_T3,
            "Rnu_over_Tedge_envelope_luminosity_ratio": L_rnu / L_Tedge,
        })

    # A constant outer susceptibility is only an equivalent parameter. Solve
    # for it separately at the two ends of the published plateau; do not treat
    # it as a recovered radial profile.
    def required_chi(coupling: float) -> dict:
        # The paper ratio is dashed R_far=R_nu divided by solid R_far=100 km.
        # The numerator therefore uses tau_Rnu, while the denominator retains
        # the vacuum neutrino tail plus the trial outer semi-Compton opacity.
        base = _luminosity(r_nat, source_weighted, tau_rnu_local, coupling)
        def ratio(candidate: float) -> float:
            tau_extra = np.empty_like(tau_outer_T3)
            # tau_outer_T3 is linear in chi_edge; rescale it to the candidate.
            tau_extra[:] = tau_outer_T3 * (candidate / chi_edge)
            trial = _luminosity(
                r_nat, source_weighted, tau_vac_local + tau_extra, coupling
            )
            return base / trial

        low, high = 0.0, max(chi_edge, 1.0e-12)
        while ratio(high) < paper_ratio_target and high < 1.0e8:
            high *= 10.0
        if ratio(high) < paper_ratio_target:
            raise RuntimeError("Could not bracket the effective outer susceptibility")
        for _ in range(64):
            middle = 0.5 * (low + high)
            if ratio(middle) < paper_ratio_target:
                low = middle
            else:
                high = middle
        value = 0.5 * (low + high)
        return {
            "g_X": float(coupling),
            "target_solid_dashed_ratio": float(paper_ratio_target),
            "chi_required_MeV3": float(value),
            "chi_required_over_digitized_edge_value": float(value / chi_edge),
            "achieved_ratio": float(ratio(value)),
            "interpretation": (
                "constant Rnu-to-Rfar susceptibility equivalent only; "
                "not a reconstructed physical radial profile"
            ),
        }

    return {
        "title": "Croon 0.1 eV full source-weighted outer muon-opacity envelope",
        "source_paper": "Croon et al., JHEP 01 (2021) 107, arXiv:2006.13942",
        "equations": ["Eqs. (3.3)-(3.4)", "Eq. (4.6)", "Eq. (4.7)"],
        "profile": {
            "path": profile["profile_path"],
            "sha256": profile["profile_sha256"],
            "rows": profile["profile_rows"],
            "R_nu_km": r_nu,
            "chi_mu_Rnu_MeV3": float(profile["chi_mu_MeV3"][-1]),
            "muon_targets": "mu-minus only" if not include_antimuons else "mu-minus plus mu-plus",
            "last_nonzero_digitized_muon_sample": {
                "r_km": r_edge,
                "T_MeV": T_edge,
                "mu_mu_MeV": profile["mu_edge_MeV"],
                "chi_mu_MeV3": chi_edge,
            },
        },
        "model": {
            "mass_MeV": float(mass_MeV),
            "neutrino_flavour_factor": float(neutrino_flavour_factor),
            "R_far_km": float(R_FAR_KM),
            "production_radius_limit_km": float(r_nu),
            "energy_measure": "domega * k * omega^2 / (2*pi^2); the emitted-particle energy is included exactly once",
            "transport": "radial optical depth with detailed-balance absorption; no angular escape average or lapse/redshift",
            "muon_targets": "mu-minus only (literal Bollig/Croon convention)" if not include_antimuons else "mu-minus plus mu-plus equilibrium distributions (separate charge-conjugate sensitivity, not the literal Croon baseline)",
        },
        "outer_envelopes": {
            "T3": {
                "chi_mu_MeV3": chi_edge,
                "path_km": [r_nu, R_FAR_KM],
                "T_outer_MeV": T_NU_MEV,
                "assumption": "conditional envelope: chi_mu(r) does not exceed the last nonzero digitized value for r>=R_nu; T<=3 MeV outside R_nu; not a measured tail",
            },
            "edge_T": {
                "chi_mu_MeV3": chi_edge,
                "path_km": [r_edge, R_FAR_KM],
                "T_outer_MeV": T_edge,
                "assumption": "conditional envelope: chi_mu(r) does not exceed the last nonzero digitized value beyond r_edge; T does not exceed T_edge; neither is a measured outer profile",
            },
        },
        "quadrature": {
            "susceptibility_order": int(susceptibility_order),
            "local_energy_order": int(energy_order),
            "optical_depth_energy_grid_points": int(tau_grid_points),
        },
        "luminosity_comparison": luminosity_rows,
        "effective_constant_outer_susceptibility": [
            required_chi(float(couplings[0])),
            required_chi(float(couplings[-1])),
        ],
        "paper_reference": {
            "median_solid_over_dashed_luminosity_ratio": float(paper_ratio_target),
            "digitized_g_interval": [3.0e-6, 3.0e-2],
            "interpretation": "published median ratio of the 0.1 eV Rfar=Rnu dashed curve to the Rfar=100 km solid curve; not a local optical depth",
        },
        "limitations": [
            "The outer envelopes are conditional sensitivity assumptions, not Garching simulation data.",
            "A non-monotonic outer muon-rich layer is not excluded by the public inner profile.",
            "The constant-susceptibility equivalent does not reconstruct a radial opacity profile.",
            "The calculation is a vector C0 benchmark and does not produce an axial-vector cooling limit.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--mass", type=float, default=1.0e-7)
    parser.add_argument("--energy-order", type=int, default=96)
    parser.add_argument("--tau-grid-points", type=int, default=601)
    parser.add_argument("--susceptibility-order", type=int, default=256)
    args = parser.parse_args()
    result = run_outer_muon_opacity_envelope(
        profile_path=args.profile,
        mass_MeV=args.mass,
        energy_order=args.energy_order,
        tau_grid_points=args.tau_grid_points,
        susceptibility_order=args.susceptibility_order,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "profile": result["profile"],
        "luminosity_comparison": result["luminosity_comparison"],
        "effective_constant_outer_susceptibility": result["effective_constant_outer_susceptibility"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
