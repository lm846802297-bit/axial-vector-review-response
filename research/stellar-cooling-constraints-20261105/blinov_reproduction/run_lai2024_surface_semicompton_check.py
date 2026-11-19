"""Check Lai's claim that inverse semi-Compton opacity is negligible at R_nu.

The comparison uses the public profile-B digitization. The last nonzero muon
sample is also evaluated as a conditional edge-value envelope; it is not
treated as the measured neutrinosphere susceptibility.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from croon_c0_luminosity import (
    DEFAULT_PROFILE,
    T_NU_MEV,
    neutrinosphere_radius,
    vectorized_muon_susceptibility,
)
from lai2024_plateau_equation_audit import (
    lai_semicompton_to_neutrino_opacity_ratio,
    lai_semicompton_to_neutrino_production_ratio,
)

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "outputs" / "lai2024_surface_semicompton_check_2026-11-19.json"
ENERGY_OVER_T = (2.0, 3.0, 4.0, 5.0, 8.0)
MASSES_MEV = (
    ("0.1 eV", 1.0e-7),
    ("2 eV", 2.0e-6),
    ("10 eV", 1.0e-5),
    ("0.1 MeV", 0.1),
    ("1 MeV", 1.0),
    ("10 MeV", 10.0),
)


def run_surface_semicompton_check(
    profile_path: Path = DEFAULT_PROFILE,
    susceptibility_order: int = 256,
) -> dict:
    profile_path = Path(profile_path)
    rows = np.genfromtxt(profile_path, delimiter=",", names=True)
    required = {"r_km", "T_MeV", "mu_mu_MeV"}
    if rows.dtype.names is None or not required.issubset(rows.dtype.names):
        raise ValueError(f"Profile must contain columns {sorted(required)}")

    r = np.asarray(rows["r_km"], dtype=float)
    temperature = np.asarray(rows["T_MeV"], dtype=float)
    mu_mu = np.asarray(rows["mu_mu_MeV"], dtype=float)
    r_nu = neutrinosphere_radius(r, temperature, T_NU_MEV)
    mu_nu = float(
        mu_mu[-1]
        + (mu_mu[-1] - mu_mu[-2]) * (r_nu - r[-1]) / (r[-1] - r[-2])
    )
    chi_nu = float(vectorized_muon_susceptibility(
        np.array([T_NU_MEV]), np.array([mu_nu]), order=susceptibility_order
    )[0])

    edge_candidates = np.flatnonzero(mu_mu > 0.0)
    if len(edge_candidates) == 0:
        raise ValueError("Profile has no nonzero digitized muon chemical-potential sample")
    edge = int(edge_candidates[-1])
    chi_edge = float(vectorized_muon_susceptibility(
        np.array([temperature[edge]]),
        np.array([mu_mu[edge]]),
        order=susceptibility_order,
    )[0])

    rows_out = []
    for mass_label, mass in MASSES_MEV:
        for energy_over_T in ENERGY_OVER_T:
            omega = energy_over_T * T_NU_MEV
            if omega <= mass:
                continue
            for susceptibility_label, chi in (
                ("public_profile_Rnu_extrapolation", chi_nu),
                ("conditional_last_nonzero_edge_envelope", chi_edge),
            ):
                opacity_ratio = float(lai_semicompton_to_neutrino_opacity_ratio(
                    np.array([omega]), T_NU_MEV, mass, chi
                )[0])
                production_ratio = float(lai_semicompton_to_neutrino_production_ratio(
                    np.array([omega]), T_NU_MEV, mass, chi
                )[0])
                rows_out.append({
                    "mass_label": mass_label,
                    "mass_MeV": mass,
                    "omega_over_Tnu": energy_over_T,
                    "omega_MeV": omega,
                    "susceptibility_case": susceptibility_label,
                    "chi_mu_MeV3": chi,
                    "kappa_sC_over_kappa_nu": opacity_ratio,
                    "Gamma_sC_prod_over_Gamma_nu_prod": production_ratio,
                })

    summaries = []
    for mass_label, mass in (("0.1 eV", 1.0e-7), ("2 eV", 2.0e-6), ("10 eV", 1.0e-5)):
        for susceptibility_label, chi in (
            ("public_profile_Rnu_extrapolation", chi_nu),
            ("conditional_last_nonzero_edge_envelope", chi_edge),
        ):
            ratios = []
            for energy_over_T in ENERGY_OVER_T:
                omega = energy_over_T * T_NU_MEV
                ratios.append(float(lai_semicompton_to_neutrino_opacity_ratio(
                    np.array([omega]), T_NU_MEV, mass, chi
                )[0]))
            summaries.append({
                "mass_label": mass_label,
                "susceptibility_case": susceptibility_label,
                "max_kappa_sC_over_kappa_nu_over_omega_over_T_2_to_8": max(ratios),
                "ratios_at_omega_over_T_2_3_4_5_8": ratios,
            })

    return {
        "title": "Lai 2024 surface semi-Compton opacity check",
        "source_paper": "Lai, Leung and Lin, Phys. Rev. D 110, 103023 (2024), arXiv:2401.16023",
        "equations": ["Eq. (10)", "Eq. (11)", "Eq. (20)", "Eq. (23)"],
        "profile": {
            "path": str(profile_path),
            "sha256": hashlib.sha256(profile_path.read_bytes()).hexdigest(),
            "rows": int(len(rows)),
            "R_nu_km": float(r_nu),
            "T_nu_MeV": float(T_NU_MEV),
            "mu_mu_Rnu_extrapolated_MeV": mu_nu,
            "chi_mu_Rnu_extrapolated_MeV3": chi_nu,
            "last_nonzero_digitized_sample": {
                "r_km": float(r[edge]),
                "T_MeV": float(temperature[edge]),
                "mu_mu_MeV": float(mu_mu[edge]),
                "chi_mu_MeV3": chi_edge,
            },
        },
        "conventions": {
            "neutrino_inverse_mfp": "Lai Eq. (20), includes nu_mu and nu_tau",
            "semicompton_inverse_mfp": "Lai Eq. (23), including 2/3 detailed-balance factor and lab-rate-to-inverse-mfp velocity conversion",
            "semicompton_production": "Lai Eq. (11)",
            "edge_case": "conditional envelope only; the last nonzero digitized point is a plotting-floor sample, not a measured R_nu value",
        },
        "energy_over_Tnu": list(ENERGY_OVER_T),
        "mass_points": [{"label": name, "mass_MeV": mass} for name, mass in MASSES_MEV],
        "pointwise_results": rows_out,
        "summary": summaries,
        "interpretation": [
            "At R_nu, the public profile's extrapolated muon susceptibility makes inverse semi-Compton opacity negligible compared with two-flavour neutrino decay for the eV-scale Lai benchmarks.",
            "Even using the last nonzero digitized edge susceptibility as a constant conditional envelope, the semi-Compton opacity remains below one percent of neutrino decay for m_Z'=2 eV over omega/T_nu=2..8.",
            "For m_Z'=0.1 eV, the same edge envelope can make local semi-Compton opacity comparable to or larger than neutrino decay; this is an outer-profile sensitivity, not evidence that Lai's R_nu surface contains such a muon population.",
            "The check supports Lai's stated omission of inverse semi-Compton absorption at the neutrinosphere for the eV benchmark, but does not reproduce the full plateau because inverse loop-bremsstrahlung remains a separate opacity channel.",
        ],
        "not_included": [
            "inverse loop-bremsstrahlung opacity",
            "full angular luminosity integral",
            "raw Garching muon profile",
            "any axial-vector rate or cooling limit",
        ],
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--susceptibility-order", type=int, default=256)
    args = parser.parse_args()
    result = run_surface_semicompton_check(
        profile_path=args.profile,
        susceptibility_order=args.susceptibility_order,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "profile": result["profile"],
        "summary": result["summary"],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
