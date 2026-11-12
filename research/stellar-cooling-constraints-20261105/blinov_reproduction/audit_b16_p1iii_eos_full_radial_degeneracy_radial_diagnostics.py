#!/usr/bin/env python3
"""C3-C radial diagnostics of EOS-consistent nucleon degeneracy factors."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import expit
from scipy.stats import spearmanr

from audit_b16_p1iii_eos_full_radial_occupation import (
    load_profile,
    state_from_profile_row,
)
from audit_b16_p1iii_eos_nucleon_distribution import phase_space_integrals

HERE = Path(__file__).resolve().parent
EXPECTED_C2_GIT_BLOB_SHA = "c472040a4551e68ffadbf7addf9402663f99e7e3"
REL_ORDER = 2048
NR_ROOT_ORDER = 512
NR_FINAL_ORDER = 2048
TAIL_T = 45.0
SPECIES = ("n", "p")
OUTPUT_COLUMNS = (
    "r_km", "species", "T_MeV", "mstar_MeV", "nu_rel_MeV",
    "eta_nu_over_T", "theta_T_over_mstar", "X_free", "Xcluster_EOS",
    "Fdeg_rel", "Fdeg_NR_fixed_nu", "Fdeg_NR_density_matched",
    "nu_NR_density_matched_MeV", "delta_nu_NR_minus_rel_MeV",
    "NR_fixed_nu_relative_shift", "NR_density_matched_relative_shift",
    "NR_density_match_relative_residual", "C2_Fdeg_reference",
)


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii")+data).hexdigest()


def load_c2_reference(path: Path) -> list[dict[str, float]]:
    digest = git_blob_sha1(path)
    if digest != EXPECTED_C2_GIT_BLOB_SHA:
        raise ValueError(f"C2 occupation CSV Git blob SHA mismatch: {digest}")
    with path.open("r", newline="", encoding="utf-8") as stream:
        raw = list(csv.DictReader(stream))
    if len(raw) != 301:
        raise ValueError(f"expected 301 C2 rows, found {len(raw)}")
    return [{key: float(value) for key, value in row.items()} for row in raw]


@lru_cache(maxsize=8)
def _quadrature(order: int) -> tuple[np.ndarray, np.ndarray]:
    x, w = leggauss(order)
    return x, w


def nonrelativistic_integrals(
    temperature_mev: float,
    effective_mass_mev: float,
    chemical_potential_mev: float,
    *,
    order: int,
) -> tuple[float, float]:
    """Return (n', n'_blocked) in MeV^3 for K_NR=p^2/(2m*)."""
    if temperature_mev <= 0.0 or effective_mass_mev <= 0.0:
        raise ValueError("T and m* must be positive")
    kmax = max(chemical_potential_mev, 0.0)+TAIL_T*temperature_mev
    pmax = math.sqrt(2.0*effective_mass_mev*kmax)
    x, w = _quadrature(order)
    p = 0.5*pmax*(x+1.0)
    weights = 0.5*pmax*w
    kinetic = p*p/(2.0*effective_mass_mev)
    occupation = expit((chemical_potential_mev-kinetic)/temperature_mev)
    measure = weights*p*p/(math.pi**2)
    number = float(np.sum(measure*occupation))
    blocked = float(np.sum(measure*occupation*(1.0-occupation)))
    return number, blocked


def solve_nonrelativistic_mu_at_fixed_density(
    temperature_mev: float,
    effective_mass_mev: float,
    target_density_mev3: float,
    initial_guess_mev: float,
) -> float:
    """Solve n'_NR(mu)=n'_rel at fixed T and m*."""
    lo = -50.0*temperature_mev
    hi = max(initial_guess_mev, 0.0)+50.0*temperature_mev
    n_hi, _ = nonrelativistic_integrals(
        temperature_mev, effective_mass_mev, hi, order=NR_ROOT_ORDER
    )
    while n_hi < target_density_mev3:
        hi += 50.0*temperature_mev
        n_hi, _ = nonrelativistic_integrals(
            temperature_mev, effective_mass_mev, hi, order=NR_ROOT_ORDER
        )
    for _ in range(72):
        mid = 0.5*(lo+hi)
        n_mid, _ = nonrelativistic_integrals(
            temperature_mev, effective_mass_mev, mid, order=NR_ROOT_ORDER
        )
        if n_mid < target_density_mev3:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo+hi)


def _correlation(x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    pearson = float(np.corrcoef(x, y)[0, 1])
    spearman = float(spearmanr(x, y).statistic)
    return {"pearson_r": pearson, "spearman_rho": spearman}


def _linear_r2(y: np.ndarray, *predictors: np.ndarray) -> float:
    design = np.column_stack([np.ones(len(y)), *predictors])
    coefficients, *_ = np.linalg.lstsq(design, y, rcond=None)
    residual = y-design@coefficients
    centered = y-np.mean(y)
    return float(1.0-np.dot(residual, residual)/np.dot(centered, centered))


def _range(values: np.ndarray) -> list[float]:
    return [float(np.min(values)), float(np.max(values))]


def _rms(values: np.ndarray) -> float:
    return float(np.sqrt(np.mean(values*values)))


def _max_abs_record(records: list[dict], key: str) -> dict:
    return max(records, key=lambda record: abs(record[key]))


def analyze(
    profile_rows: list[dict[str, float]],
    c2_rows: list[dict[str, float]],
) -> tuple[list[dict], dict]:
    if len(profile_rows) != 301 or len(c2_rows) != 301:
        raise ValueError("C3-C requires 301 aligned radial points")

    records: list[dict] = []
    composition_closure = []
    for index, (row, c2) in enumerate(zip(profile_rows, c2_rows)):
        radius = row["r_km"]
        if abs(radius-c2["r_km"]) > 1e-12:
            raise ValueError(f"C1/C2 radial mismatch at row {index}")
        composition_closure.append(
            row["X_n"]+row["X_p"]+row["Xcluster_EOS"]-1.0
        )
        for species in SPECIES:
            state = state_from_profile_row(row, species)
            temperature = state.temperature_mev
            mass = state.effective_mass_mev
            nu = state.effective_chemical_potential_mev
            eta = nu/temperature
            theta = temperature/mass
            x_free = row[f"X_{species}"]
            x_cluster = max(0.0, row["Xcluster_EOS"])
            c2_key = "Fnn_deg" if species == "n" else "Fpp_deg"
            c2_fdeg = c2[c2_key]

            n_rel, blocked_rel = phase_space_integrals(
                state, order=REL_ORDER, tail_T=TAIL_T
            )
            f_rel = blocked_rel/n_rel
            if abs(f_rel-c2_fdeg) >= 5e-12:
                raise ArithmeticError(
                    f"relativistic Fdeg does not reproduce C2 at r={radius}, {species}"
                )

            n_nr_fixed, blocked_nr_fixed = nonrelativistic_integrals(
                temperature, mass, nu, order=NR_FINAL_ORDER
            )
            f_nr_fixed = blocked_nr_fixed/n_nr_fixed

            nu_nr = solve_nonrelativistic_mu_at_fixed_density(
                temperature, mass, n_rel, nu
            )
            n_nr_matched, blocked_nr_matched = nonrelativistic_integrals(
                temperature, mass, nu_nr, order=NR_FINAL_ORDER
            )
            f_nr_matched = blocked_nr_matched/n_nr_matched
            density_residual = n_nr_matched/n_rel-1.0

            records.append({
                "r_km": radius,
                "species": species,
                "T_MeV": temperature,
                "mstar_MeV": mass,
                "nu_rel_MeV": nu,
                "eta_nu_over_T": eta,
                "theta_T_over_mstar": theta,
                "X_free": x_free,
                "Xcluster_EOS": x_cluster,
                "Fdeg_rel": f_rel,
                "Fdeg_NR_fixed_nu": f_nr_fixed,
                "Fdeg_NR_density_matched": f_nr_matched,
                "nu_NR_density_matched_MeV": nu_nr,
                "delta_nu_NR_minus_rel_MeV": nu_nr-nu,
                "NR_fixed_nu_relative_shift": (f_nr_fixed-f_rel)/f_rel,
                "NR_density_matched_relative_shift": (f_nr_matched-f_rel)/f_rel,
                "NR_density_match_relative_residual": density_residual,
                "C2_Fdeg_reference": c2_fdeg,
            })

    species_summary = {}
    for species in SPECIES:
        group = [record for record in records if record["species"] == species]
        col = lambda key: np.asarray([record[key] for record in group], dtype=float)
        eta, theta, f_rel = col("eta_nu_over_T"), col("theta_T_over_mstar"), col("Fdeg_rel")
        x_free, x_cluster = col("X_free"), col("Xcluster_EOS")
        fixed_shift = col("NR_fixed_nu_relative_shift")
        matched_shift = col("NR_density_matched_relative_shift")
        delta_nu = col("delta_nu_NR_minus_rel_MeV")
        max_fixed = _max_abs_record(group, "NR_fixed_nu_relative_shift")
        max_matched = _max_abs_record(group, "NR_density_matched_relative_shift")
        species_summary[species] = {
            "ranges": {
                "eta_nu_over_T": _range(eta),
                "T_over_mstar": _range(theta),
                "mstar_MeV": _range(col("mstar_MeV")),
                "T_MeV": _range(col("T_MeV")),
                "X_free": _range(x_free),
                "Xcluster_EOS": _range(x_cluster),
                "Fdeg_relativistic": _range(f_rel),
                "Fdeg_nonrel_fixed_nu": _range(col("Fdeg_NR_fixed_nu")),
                "Fdeg_nonrel_density_matched": _range(col("Fdeg_NR_density_matched")),
            },
            "correlations": {
                "Fdeg_vs_eta": _correlation(f_rel, eta),
                "Fdeg_vs_T_over_mstar": _correlation(f_rel, theta),
                "Fdeg_vs_X_free": _correlation(f_rel, x_free),
                "Fdeg_vs_Xcluster": _correlation(f_rel, x_cluster),
                "eta_vs_T_over_mstar": _correlation(eta, theta),
            },
            "linear_regression_R2": {
                "eta_only": _linear_r2(f_rel, eta),
                "eta_and_T_over_mstar": _linear_r2(f_rel, eta, theta),
                "eta_and_X_free": _linear_r2(f_rel, eta, x_free),
            },
            "nonrelativistic_fixed_nu": {
                "max_abs_relative_shift": abs(max_fixed["NR_fixed_nu_relative_shift"]),
                "at_r_km": max_fixed["r_km"],
                "rms_relative_shift": _rms(fixed_shift),
                "mean_signed_relative_shift": float(np.mean(fixed_shift)),
                "all_points_nonrel_below_rel": bool(np.all(fixed_shift < 0.0)),
            },
            "nonrelativistic_density_matched": {
                "max_abs_relative_shift": abs(max_matched["NR_density_matched_relative_shift"]),
                "at_r_km": max_matched["r_km"],
                "rms_relative_shift": _rms(matched_shift),
                "mean_signed_relative_shift": float(np.mean(matched_shift)),
                "max_abs_mu_shift_MeV": float(np.max(np.abs(delta_nu))),
                "rms_mu_shift_MeV": _rms(delta_nu),
                "max_abs_density_match_residual": float(np.max(np.abs(col("NR_density_match_relative_residual")))),
                "all_points_nonrel_below_rel": bool(np.all(matched_shift < 0.0)),
            },
            "max_abs_C2_reproduction_difference": float(
                np.max(np.abs(f_rel-col("C2_Fdeg_reference")))
            ),
            "sample_points": [
                {
                    key: record[key]
                    for key in (
                        "r_km", "eta_nu_over_T", "theta_T_over_mstar",
                        "X_free", "Xcluster_EOS", "Fdeg_rel",
                        "Fdeg_NR_fixed_nu", "Fdeg_NR_density_matched",
                        "delta_nu_NR_minus_rel_MeV",
                    )
                }
                for record in (group[0], group[96], group[196], group[-1])
            ],
        }

    radii = [row["r_km"] for row in profile_rows]
    radial_steps = np.diff(radii)
    max_closure = float(np.max(np.abs(composition_closure)))
    acceptance = {
        "301_aligned_radial_points": len(profile_rows) == 301 and len(records) == 602,
        "uniform_0p05km_grid": float(np.max(np.abs(radial_steps-0.05))) < 1e-8,
        "relativistic_Fdeg_reproduces_C2": max(
            species_summary["n"]["max_abs_C2_reproduction_difference"],
            species_summary["p"]["max_abs_C2_reproduction_difference"],
        ) < 5e-12,
        "composition_closure_below_1e_8": max_closure < 1e-8,
        "NR_density_match_below_1e_8": max(
            species_summary["n"]["nonrelativistic_density_matched"]["max_abs_density_match_residual"],
            species_summary["p"]["nonrelativistic_density_matched"]["max_abs_density_match_residual"],
        ) < 1e-8,
        "all_Fdeg_values_in_0_1": all(
            0.0 < record[key] < 1.0
            for record in records
            for key in ("Fdeg_rel", "Fdeg_NR_fixed_nu", "Fdeg_NR_density_matched")
        ),
        "NR_corrections_finite_and_negative": all(
            math.isfinite(record[key]) and record[key] < 0.0
            for record in records
            for key in ("NR_fixed_nu_relative_shift", "NR_density_matched_relative_shift")
        ),
        "Fdeg_monotonic_with_eta_on_snapshot": all(
            species_summary[s]["correlations"]["Fdeg_vs_eta"]["spearman_rho"] < -0.999
            for s in SPECIES
        ),
    }
    summary = {
        "title": "P1-IIIe-C3C full-radial degeneracy-factor physical diagnostics",
        "date": "2026-11-11",
        "status": "PASS: dimensionless dependence and relativistic-dispersion comparison quantified",
        "scope": (
            "301-point t_pb=1 s Caputo SFHo-18.8 published-figure snapshot; "
            "local static quasiparticle occupations only; not a time-space weighted core average."
        ),
        "provenance": {
            "profile": "outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv",
            "profile_git_blob_sha": "9ff7818b0679992c0a9ba402330ec7f0d1f3041b",
            "C2_occupation": "outputs/p1iii_eos_full_radial_occupation_2026-11-11.csv",
            "C2_occupation_git_blob_sha": EXPECTED_C2_GIT_BLOB_SHA,
            "radial_points": len(profile_rows),
            "radial_range_km": [radii[0], radii[-1]],
            "radial_step_km": 0.05,
            "snapshot_time_post_bounce_s": 1.0,
        },
        "dimensionless_form": {
            "eta": "nu_N/T",
            "theta": "T/m_N*",
            "momentum_substitution": "p=sqrt(2*m_N* T)*y",
            "K_rel_over_T": "(sqrt(1+2*theta*y^2)-1)/theta",
            "exact_statement": "Fdeg_rel = F(eta,theta); xi_SPP and X_N do not enter explicitly in the ratio.",
            "nonrelativistic_limit": "theta->0 gives K/T=y^2 and Fdeg_NR=F_NR(eta).",
        },
        "numerical_method": {
            "relativistic_quadrature_order": REL_ORDER,
            "nonrelativistic_root_quadrature_order": NR_ROOT_ORDER,
            "nonrelativistic_final_quadrature_order": NR_FINAL_ORDER,
            "kinetic_energy_tail_T": TAIL_T,
            "NR_comparison_A": "same T, m*, and nu as relativistic EOS state; density is not constrained to match",
            "NR_comparison_B": "same T, m*, and n' as relativistic EOS state; solve nu_NR before evaluating Fdeg",
            "density_convention": "per available volume V'; xi_SPP cancels in the Fdeg ratio",
        },
        "composition_closure_max_abs": max_closure,
        "species": species_summary,
        "acceptance": acceptance,
        "overall_pass": all(acceptance.values()),
        "interpretation": [
            "The local relativistic Fdeg is a function of eta=nu/T and theta=T/m*; eta is the dominant radial correlator in this one-snapshot profile.",
            "X_N and Xcluster correlate with Fdeg along the radial profile, but they are not independent explicit arguments of the local Fdeg formula; their influence is mediated by EOS state variables, especially nu/T.",
            "A radial correlation is not a causal or universal EOS relation: this dataset is one radial trajectory at one post-bounce time.",
            "At fixed nu, the nonrelativistic dispersion gives a lower Fdeg than the relativistic dispersion throughout this profile.",
            "At fixed density, the nonrelativistic chemical potential must be refitted; the resulting Fdeg difference is larger and is the more controlled comparison for an EOS state with specified density.",
            "Neither approximation comparison changes the relativistic C2 baseline.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C3-C acceptance failed: {acceptance}")
    return records, summary


def write_csv(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows({
            key: f"{record[key]:.16g}" if isinstance(record[key], float) else record[key]
            for key in OUTPUT_COLUMNS
        } for record in records)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--c2-reference", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()
    profile_rows = load_profile(args.profile)
    c2_rows = load_c2_reference(args.c2_reference)
    records, summary = analyze(profile_rows, c2_rows)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(summary, indent=2, allow_nan=False)+"\n", encoding="utf-8"
    )
    write_csv(args.output_csv, records)
    print(json.dumps({
        "overall_pass": summary["overall_pass"],
        "composition_closure_max_abs": summary["composition_closure_max_abs"],
        "species": {
            species: {
                "correlations": summary["species"][species]["correlations"],
                "linear_regression_R2": summary["species"][species]["linear_regression_R2"],
                "nonrelativistic_fixed_nu": summary["species"][species]["nonrelativistic_fixed_nu"],
                "nonrelativistic_density_matched": summary["species"][species]["nonrelativistic_density_matched"],
            }
            for species in SPECIES
        },
        "acceptance": summary["acceptance"],
    }, indent=2))


if __name__ == "__main__":
    main()
