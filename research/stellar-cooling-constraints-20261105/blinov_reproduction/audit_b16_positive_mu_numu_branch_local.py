#!/usr/bin/env python3
"""Local B.6/B.10 response to the resolved positive mu_numu profile branch.

This post-processing audit does not rerun B.1/B.2 transport. It evaluates the
exact scalar Fermi-pair average used by the B.16 neutrino inverse-decay kernel
at points inside the positive branch, and links the result to the existing
current-profile radial-shell decomposition.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from blinov_reproduction.reference import DEFAULT_PROFILE, fermi_pair_average


DEFAULT_PATH_AUDIT = HERE / "outputs" / "b16_inner_path_channel_directional_vertex_preserving_10mev_2026-11-09.json"
DEFAULT_OUTPUT = HERE / "outputs" / "b16_positive_mu_numu_branch_local_10mev_2026-11-09.json"
MASS_MEV = 10.0
SAMPLE_RADII_KM = (17.0, 17.5, 18.0)
SAMPLE_OMEGAS_MEV = (15.0, 20.0, 30.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(profile_path: Path, path_audit_path: Path, output_path: Path):
    data = np.genfromtxt(profile_path, delimiter=",", names=True)
    radius = np.asarray(data["r_km"], float)
    temperature = np.asarray(data["T_MeV"], float)
    mu_numu = np.asarray(data["mu_numu_MeV"], float)
    positive = mu_numu > 0.0
    if not np.any(positive):
        raise RuntimeError("No positive mu_numu branch found in the profile.")

    branch_indices = np.flatnonzero(positive)
    lo_i, hi_i = int(branch_indices[0]), int(branch_indices[-1])
    branch = {
        "lower_support_km": float(radius[lo_i]),
        "upper_support_km": float(radius[hi_i]),
        "node_count": int(np.count_nonzero(positive)),
        "mu_numu_min_MeV": float(np.min(mu_numu[positive])),
        "mu_numu_max_MeV": float(np.max(mu_numu[positive])),
        "temperature_min_MeV": float(np.min(temperature[positive])),
        "temperature_max_MeV": float(np.max(temperature[positive])),
        "maximum_mu_numu_over_T": float(np.max(mu_numu[positive] / temperature[positive])),
        "radius_at_maximum_mu_numu_over_T_km": float(
            radius[branch_indices[np.argmax(mu_numu[positive] / temperature[positive])]]
        ),
    }

    local_rows = []
    max_nu_mu_suppression = 0.0
    max_flavour_sum_suppression = 0.0
    max_evenness_residual = 0.0
    for r in SAMPLE_RADII_KM:
        t = float(np.interp(r, radius, temperature))
        mu = float(np.interp(r, radius, mu_numu))
        for omega in SAMPLE_OMEGAS_MEV:
            velocity = float(np.sqrt(1.0 - (MASS_MEV / omega) ** 2))
            i_mu = float(fermi_pair_average(mu, omega, t, velocity))
            i_mu_negative = float(fermi_pair_average(-mu, omega, t, velocity))
            i_zero = float(fermi_pair_average(0.0, omega, t, velocity))
            nu_mu_ratio = i_mu / i_zero
            total_flavour_sum_ratio = (i_mu + i_zero) / (2.0 * i_zero)
            nu_mu_suppression = 1.0 - nu_mu_ratio
            total_suppression = 1.0 - total_flavour_sum_ratio
            max_nu_mu_suppression = max(max_nu_mu_suppression, nu_mu_suppression)
            max_flavour_sum_suppression = max(max_flavour_sum_suppression, total_suppression)
            max_evenness_residual = max(
                max_evenness_residual,
                abs(i_mu - i_mu_negative) / max(abs(i_mu), 1.0e-300),
            )
            local_rows.append({
                "radius_km": r,
                "omega_MeV": omega,
                "temperature_MeV": t,
                "mu_numu_MeV": mu,
                "mu_numu_over_T": mu / t,
                "I_nu_mu_over_I_mu0": nu_mu_ratio,
                "nu_mu_rate_relative_change_vs_mu0": nu_mu_ratio - 1.0,
                "nu_mu_plus_nu_tau_rate_ratio_vs_both_mu0": total_flavour_sum_ratio,
                "nu_mu_plus_nu_tau_relative_change_vs_both_mu0": total_flavour_sum_ratio - 1.0,
                "I_evenness_relative_residual": abs(i_mu - i_mu_negative) / max(abs(i_mu), 1.0e-300),
            })

    path_audit = json.loads(path_audit_path.read_text(encoding="utf-8"))
    strong = next(x for x in path_audit["representative_couplings"] if x["label"] == "strong_endpoint")
    dominant = next(x for x in strong["regions"] if x["region"] == "dominant_8_15km_emission")
    shell = next(
        x for x in dominant["channel_shell_tau"]
        if x["channel"] == "nu_mu" and x["path_shell"] == "16.5-18.5km"
    )
    shell_tau_mu = float(shell["mean_tau_source_weighted_per_g2"])
    shell_tau_tau = float(next(
        x["mean_tau_source_weighted_per_g2"]
        for x in dominant["channel_shell_tau"]
        if x["channel"] == "nu_tau" and x["path_shell"] == "16.5-18.5km"
    ))
    total_nu_tau = float(dominant["mean_total_tau_source_weighted_per_g2"])
    shell_fraction = (shell_tau_mu + shell_tau_tau) / total_nu_tau

    result = {
        "title": "Local response of B.16 neutrino inverse decay to the positive mu_numu branch",
        "mass_MeV": MASS_MEV,
        "profile": {
            "path": str(profile_path),
            "sha256": sha256(profile_path),
            "identity": "current 1687-row vertex-preserving public-figure SFHo-18.8 reconstruction; not raw Garching data",
        },
        "branch": branch,
        "local_rate_samples": local_rows,
        "radial_path_context": {
            "path_audit_path": str(path_audit_path),
            "path_audit_sha256": sha256(path_audit_path),
            "mediator_mass_MeV": path_audit["mass_MeV"],
            "strong_endpoint_g": strong["g"],
            "dominant_8_15km_source_fraction_of_total_B1": dominant["source_fraction_of_total_B1"],
            "dominant_8_15km_source_weighted_escape_probability": dominant["source_weighted_escape_probability"],
            "16.5_18.5km_shell_nu_mu_tau_tau_per_g2": shell_tau_mu,
            "16.5_18.5km_shell_nu_tau_tau_per_g2": shell_tau_tau,
            "16.5_18.5km_shell_fraction_of_total_nu_mu_plus_nu_tau_path_tau": shell_fraction,
        },
        "summary": {
            "maximum_sampled_nu_mu_rate_suppression_vs_mu_numu_zero": max_nu_mu_suppression,
            "maximum_sampled_total_nu_mu_plus_nu_tau_suppression_vs_both_mu0": max_flavour_sum_suppression,
            "maximum_evenness_relative_residual_I_mu_equals_I_minus_mu": max_evenness_residual,
            "sign_of_mu_numu_changes_scalar_flavour_summed_rate": False,
            "scope": "local sampled-point response only; not a full B.1/B.2 branch-removal transport rerun",
        },
        "interpretation": [
            "The scalar Fermi-pair average is even in mu_numu because the two charge-conjugate terms enter symmetrically.",
            "The positive branch changes the nu_mu inverse-decay rate through its magnitude, not its sign.",
            "The nu_tau contribution is unchanged when mu_numu is varied; therefore the relative change in the nu_mu+nu_tau sum is approximately half the nu_mu-only change when the two zero-chemical-potential baselines are equal.",
            "The branch lies inside the 16.5--18.5 km path shell. Its local rate effect must be combined with the shell's path weight; this local audit does not itself determine the full escaped-luminosity response.",
        ],
        "scope": [
            "No B.1 source, B.2 path, coupling, or luminosity is recomputed.",
            "No profile values are modified.",
            "No source, opacity, or luminosity rescaling.",
            "No axial-vector production output or constraint curve is changed.",
        ],
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"branch": branch, "summary": result["summary"], "radial_path_context": result["radial_path_context"]}, indent=2))
    print(f"Saved {output_path}")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--path-audit", type=Path, default=DEFAULT_PATH_AUDIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    run(args.profile, args.path_audit, args.output)


if __name__ == "__main__":
    main()
