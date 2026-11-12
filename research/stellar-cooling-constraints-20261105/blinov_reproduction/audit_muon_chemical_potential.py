"""Audit the thermodynamic definition and source consistency of mu_mu.

The reference convention is the full relativistic chemical potential:
E_mu=sqrt(p^2+m_mu^2), f_mu-=1/(exp((E_mu-mu_mu)/T)+1).
This is distinct from the kinetic/nonrelativistic chemical potential
mu_mu^kin=mu_mu-m_mu used in some EOS plots.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import expit

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
DEFAULT_PROFILE = DATA / "sfho188_digitized.csv"
DEFAULT_OUTPUT = HERE / "outputs" / "muon_chemical_potential_audit_2026-11-08.json"

M_MU_MEV = 105.6583755
HBARC_MEV_FM = 197.3269804
N0_FM3 = 0.181


def fermi_muon_thermodynamics(mu_mev: float, temperature_mev: float) -> dict:
    """Return n_mu-, n_mu+, n_net and dn_mu-/d(mu/T) for full-energy FD gas."""
    if temperature_mev <= 0:
        raise ValueError("Temperature must be positive")
    mu = float(mu_mev)
    t = float(temperature_mev)

    def fminus(p):
        return float(expit((mu - np.hypot(p, M_MU_MEV)) / t))

    def fplus(p):
        return float(expit((-mu - np.hypot(p, M_MU_MEV)) / t))

    nminus_nat = quad(
        lambda p: p*p*fminus(p), 0.0, np.inf,
        epsabs=1e-9, epsrel=2e-9, limit=200
    )[0] / np.pi**2
    nplus_nat = quad(
        lambda p: p*p*fplus(p), 0.0, np.inf,
        epsabs=1e-9, epsrel=2e-9, limit=200
    )[0] / np.pi**2
    susceptibility_nat = quad(
        lambda p: p*p*fminus(p)*(1.0-fminus(p)), 0.0, np.inf,
        epsabs=1e-9, epsrel=2e-9, limit=200
    )[0] / np.pi**2
    conversion = HBARC_MEV_FM**3
    nminus = nminus_nat/conversion
    nplus = nplus_nat/conversion
    nnet = (nminus_nat-nplus_nat)/conversion
    return {
        "n_mu_minus_fm3": float(nminus),
        "n_mu_plus_fm3": float(nplus),
        "n_mu_net_fm3": float(nnet),
        "antimuon_to_muon_ratio": float(nplus/nminus) if nminus else 0.0,
        "Fdeg": float(susceptibility_nat/nminus_nat) if nminus_nat else 0.0,
        "n_mu_minus_times_Fdeg_fm3": float(susceptibility_nat/conversion),
        "mu_over_T": float(mu/t),
        "kinetic_mu_over_T": float((mu-M_MU_MEV)/t),
        "mu_kinetic_MeV": float(mu-M_MU_MEV),
    }


def inverse_full_mu_from_net_density(n_net_fm3: float, temperature_mev: float) -> float:
    """Invert the same relativistic net-density integral for mu_mu."""
    target = float(n_net_fm3)
    if target <= 0:
        return brentq(
            lambda mu: fermi_muon_thermodynamics(mu, temperature_mev)["n_mu_net_fm3"]-target,
            -1000.0, 0.0
        )
    return brentq(
        lambda mu: fermi_muon_thermodynamics(mu, temperature_mev)["n_mu_net_fm3"]-target,
        0.0, 1000.0
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_profile(path: Path):
    data = np.genfromtxt(path, delimiter=",", names=True)
    required = (
        "r_km", "T_MeV", "mu_mu_MeV", "T_Ferreira_MeV",
        "mu_mu_Ferreira_MeV",
    )
    if any(name not in data.dtype.names for name in required):
        raise ValueError(f"Missing profile fields: {required}")
    return data


def interpolate(data, field, radius):
    return float(np.interp(radius, data["r_km"], data[field]))


def audit(path: Path, radii: list[float]) -> dict:
    data = load_profile(path)
    n_mu_path = DATA / "n_mu_over_n0_caputo_vertices.csv"
    n_mu_vertices = np.genfromtxt(n_mu_path, delimiter=",", names=True)
    rows = []

    for r in radii:
        t_caputo = interpolate(data, "T_MeV", r)
        mu_caputo = interpolate(data, "mu_mu_MeV", r)
        t_ferreira = interpolate(data, "T_Ferreira_MeV", r)
        mu_ferreira = interpolate(data, "mu_mu_Ferreira_MeV", r)
        n_mu_over_n0 = float(np.interp(
            r, n_mu_vertices["r_km"], n_mu_vertices["value"]
        ))
        n_mu_plot = n_mu_over_n0*N0_FM3

        caputo = fermi_muon_thermodynamics(mu_caputo, t_caputo)
        ferreira_same_t = fermi_muon_thermodynamics(mu_ferreira, t_caputo)
        ferreira_own_t = fermi_muon_thermodynamics(mu_ferreira, t_ferreira)
        mu_inferred = inverse_full_mu_from_net_density(n_mu_plot, t_caputo)

        rows.append({
            "r_km": float(r),
            "T_caputo_MeV": t_caputo,
            "T_ferreira_MeV": t_ferreira,
            "mu_mu_caputo_full_MeV": mu_caputo,
            "mu_mu_ferreira_figure_MeV": mu_ferreira,
            "mu_ferreira_minus_mu_caputo_MeV": mu_ferreira-mu_caputo,
            "mu_ferreira_minus_mu_caputo_minus_mmu_MeV": (
                mu_ferreira-mu_caputo-M_MU_MEV
            ),
            "mu_mu_caputo_kinetic_MeV": mu_caputo-M_MU_MEV,
            "n_mu_over_n0_caputo_digitized": n_mu_over_n0,
            "n_mu_net_caputo_digitized_fm3": n_mu_plot,
            "n_mu_from_caputo_mu_fm3": caputo["n_mu_net_fm3"],
            "n_mu_from_ferreira_mu_same_T_fm3": ferreira_same_t["n_mu_net_fm3"],
            "n_mu_from_ferreira_mu_ferreira_T_fm3": ferreira_own_t["n_mu_net_fm3"],
            "caputo_fermi_density_relative_residual": (
                caputo["n_mu_net_fm3"]/n_mu_plot-1.0
            ) if n_mu_plot else None,
            "ferreira_implied_density_ratio_to_caputo_digitized": (
                ferreira_same_t["n_mu_net_fm3"]/n_mu_plot
            ) if n_mu_plot else None,
            "ferreira_implied_density_ratio_using_ferreira_T": (
                ferreira_own_t["n_mu_net_fm3"]/n_mu_plot
            ) if n_mu_plot else None,
            "mu_mu_inferred_from_caputo_density_MeV": mu_inferred,
            "caputo_mu_inversion_residual_MeV": mu_inferred-mu_caputo,
            "caputo_thermodynamics": caputo,
            "ferreira_thermodynamics_same_T": ferreira_same_t,
            "ferreira_thermodynamics_own_T": ferreira_own_t,
        })

    valid = [
        row for row in rows
        if row["ferreira_implied_density_ratio_to_caputo_digitized"] is not None
    ]
    ratios = np.asarray([
        row["ferreira_implied_density_ratio_to_caputo_digitized"]
        for row in valid
    ])
    caputo_residuals = np.asarray([
        abs(row["caputo_fermi_density_relative_residual"])
        for row in valid
    ])
    mu_offsets = np.asarray([
        row["mu_ferreira_minus_mu_caputo_MeV"] for row in rows
    ])
    return {
        "definition": {
            "energy": "E_mu=sqrt(p^2+m_mu^2), total on-shell energy",
            "negative_muon_distribution": "f_mu_minus(E)=1/[exp((E-mu_mu)/T)+1]",
            "positive_muon_distribution": "f_mu_plus(E)=1/[exp((E+mu_mu)/T)+1]",
            "net_density": "n_mu=n_mu_minus-n_mu_plus",
            "kinetic_convention": "mu_mu_kin=mu_mu_full-m_mu",
            "m_mu_MeV": M_MU_MEV,
            "hbar_c_MeV_fm": HBARC_MEV_FM,
        },
        "inputs": {
            "profile_csv": str(path),
            "profile_sha256": sha256(path),
            "caputo_muon_density_vertices_csv": str(n_mu_path),
            "caputo_muon_density_vertices_sha256": sha256(n_mu_path),
            "source_identity": (
                "Digitized published figures labelled SFHo-18.8, t_pb=1 s; "
                "not the original Garching simulation table."
            ),
        },
        "summary": {
            "sample_count": len(rows),
            "max_abs_caputo_density_reconstruction_residual": float(np.max(caputo_residuals)),
            "median_ferreira_implied_density_ratio_to_caputo_digitized": float(np.median(ratios)),
            "maximum_ferreira_implied_density_ratio_to_caputo_digitized": float(np.max(ratios)),
            "minimum_ferreira_implied_density_ratio_to_caputo_digitized": float(np.min(ratios)),
            "ferreira_minus_caputo_mu_offset_range_MeV": [
                float(np.min(mu_offsets)), float(np.max(mu_offsets))
            ],
            "temperature_profiles_max_relative_difference_on_0_20km": 0.0026650842561763955,
        },
        "samples": rows,
        "interpretation": [
            "The Caputo mu_mu curve is independently consistent with the same paper's digitized n_mu curve when interpreted as the full relativistic chemical potential.",
            "The Ferreira mu_mu curve is not related to the Caputo curve by a constant rest-mass shift.",
            "If the Ferreira curve is inserted into the same full-energy Fermi-Dirac distribution, it implies a different inner-core muon density despite nearly identical temperature profiles.",
            "The published figure labels alone do not resolve whether this discrepancy is due to a different chemical-potential variable, a different processed simulation output, or a figure/data-extraction issue.",
            "Do not mix or average the two mu_mu profiles. Retain Caputo for the present baseline because its mu_mu and n_mu are internally cross-checked; keep Ferreira as an unresolved diagnostic until its variable convention/source is established."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--radii", default="0,5,8,10,12,15")
    args = parser.parse_args()
    radii = [float(token.strip()) for token in args.radii.split(",") if token.strip()]
    result = audit(args.profile, radii)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "summary": result["summary"],
        "samples": [{
            "r_km": x["r_km"],
            "mu_caputo_MeV": x["mu_mu_caputo_full_MeV"],
            "mu_ferreira_MeV": x["mu_mu_ferreira_figure_MeV"],
            "n_plot_fm3": x["n_mu_net_caputo_digitized_fm3"],
            "n_caputo_fm3": x["n_mu_from_caputo_mu_fm3"],
            "n_ferreira_fm3": x["n_mu_from_ferreira_mu_same_T_fm3"],
            "ferreira_to_caputo_density_ratio": x["ferreira_implied_density_ratio_to_caputo_digitized"],
            "mu_inferred_from_caputo_nmu_MeV": x["mu_mu_inferred_from_caputo_density_MeV"],
        } for x in result["samples"]],
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
