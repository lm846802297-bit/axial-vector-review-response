#!/usr/bin/env python3
"""C4-A: EOS-effective-mass dynamic scalar response and sum-rule validation."""
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

from audit_b16_p1iii_eos_full_radial_occupation import (
    load_profile,
    state_from_profile_row,
)
from audit_b16_p1iii_eos_nucleon_distribution import phase_space_integrals

HERE = Path(__file__).resolve().parent
EXPECTED_C2_GIT_BLOB_SHA = "c472040a4551e68ffadbf7addf9402663f99e7e3"
SELECTED_PROFILE_INDICES = (0, 96, 196, 300)
Q_VALUES_MEV = (1.0, 3.0, 10.0, 30.0, 100.0, 200.0, 500.0)
DB_Q0_OVER_T = (0.1, 0.5, 1.0, 2.0, 4.0)
P_ORDER = 600
Q0_ORDER = 240
STATIC_P_ORDER = 160
STATIC_C_ORDER = 160
TAIL_T = 45.0
HBARC = 197.3269804
SPECIES = ("n", "p")
RESPONSE_COLUMNS = (
    "r_km", "species", "T_MeV", "mstar_MeV", "nu_MeV",
    "eta_nu_over_T", "theta_T_over_mstar", "q_MeV", "q0_MeV",
    "S_MeV2",
)
SUMRULE_COLUMNS = (
    "r_km", "species", "q_MeV", "I_dynamic_MeV3",
    "I_static_MeV3", "sum_rule_relative_residual",
    "q0_zero_blocked_MeV3", "I_static_over_q0_zero_blocked",
    "max_detailed_balance_relative_residual",
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


def _pmax(mass: float, temperature: float, nu: float) -> float:
    emax = mass+max(nu, 0.0)+TAIL_T*temperature
    return math.sqrt(emax*emax-mass*mass)


def _pmin(q0: float, q: float, mass: float) -> float:
    if q <= abs(q0) or q <= 0.0:
        return math.inf
    a = q0/q
    A = (q0*q0-q*q)/(2.0*q)
    eb = (a*A+math.sqrt(A*A+(1.0-a*a)*mass*mass))/(1.0-a*a)
    return abs(a*eb+A)


def dynamic_response(
    q0: float,
    q: float,
    mass: float,
    temperature: float,
    nu: float,
) -> float:
    """Spin-summed ideal quasiparticle response S(q0,q), in MeV^2.

    The local quasiparticle energy is E*=sqrt(p^2+m*^2). The constant
    vector potential cancels from the same-species energy transfer; the
    occupation is f=[exp((E*-m*-nu)/T)+1]^-1.
    """
    if q <= abs(q0) or q <= 0.0:
        return 0.0
    lo = _pmin(q0, q, mass)
    hi = _pmax(mass, temperature, nu)
    if lo >= hi:
        return 0.0
    x, w = _quadrature(P_ORDER)
    p = 0.5*(hi-lo)*(x+1.0)+lo
    wp = 0.5*(hi-lo)*w
    ei = np.sqrt(p*p+mass*mass)
    ef = ei+q0
    if np.any(ef <= 0.0):
        raise ArithmeticError("non-positive final quasiparticle energy")
    fi = expit((nu-(ei-mass))/temperature)
    ff = expit((nu-(ef-mass))/temperature)
    integrand = p*ef*fi*(1.0-ff)
    return float(np.sum(wp*integrand)/(math.pi*q))


def static_structure_factor(
    q: float,
    mass: float,
    temperature: float,
    nu: float,
) -> float:
    """Direct 3D static integral 2 int d^3p/(2pi)^3 f_i(1-f_f), MeV^3."""
    pmax = _pmax(mass, temperature, nu)
    xp, wp = _quadrature(STATIC_P_ORDER)
    xc, wc = _quadrature(STATIC_C_ORDER)
    p = 0.5*pmax*(xp+1.0)
    weights_p = 0.5*pmax*wp
    ei = np.sqrt(p*p+mass*mass)
    fi = expit((nu-(ei-mass))/temperature)
    pfinal2 = (
        p[:, None]*p[:, None]+q*q
        +2.0*p[:, None]*q*xc[None, :]
    )
    ef = np.sqrt(np.maximum(pfinal2, 0.0)+mass*mass)
    ff = expit((nu-(ef-mass))/temperature)
    angular = np.sum(wc[None, :]*(1.0-ff), axis=1)
    return float(np.sum(weights_p*p*p*fi*angular)/(2.0*math.pi**2))


def dynamic_sum_rule(
    q: float,
    mass: float,
    temperature: float,
    nu: float,
) -> tuple[float, list[tuple[float, float]]]:
    """Integrate int dq0/(2pi) S(q0,q), retaining q0-resolved nodes."""
    x, w = _quadrature(Q0_ORDER)
    q0_values = q*x
    responses = [
        dynamic_response(float(q0), q, mass, temperature, nu)
        for q0 in q0_values
    ]
    integral = float(q*np.dot(w, responses)/(2.0*math.pi))
    return integral, list(zip(q0_values.tolist(), responses))


def detailed_balance_residuals(
    q: float,
    mass: float,
    temperature: float,
    nu: float,
) -> list[float]:
    residuals = []
    for multiple in DB_Q0_OVER_T:
        q0 = min(0.5*q, multiple*temperature)
        positive = dynamic_response(q0, q, mass, temperature, nu)
        negative = dynamic_response(-q0, q, mass, temperature, nu)
        if positive <= 0.0 or negative <= 0.0:
            raise ArithmeticError(
                f"response support vanished in detailed-balance test q={q}, q0={q0}"
            )
        ratio = negative/(positive*math.exp(-q0/temperature))
        residuals.append(ratio-1.0)
    return residuals


def analyze(
    profile_rows: list[dict[str, float]],
    c2_rows: list[dict[str, float]],
) -> tuple[list[dict], list[dict], dict]:
    if len(profile_rows) != 301 or len(c2_rows) != 301:
        raise ValueError("C4-A requires the 301-point C1/C2 radial profile")
    response_records: list[dict] = []
    sumrule_records: list[dict] = []
    for index in SELECTED_PROFILE_INDICES:
        row, c2 = profile_rows[index], c2_rows[index]
        if abs(row["r_km"]-c2["r_km"]) > 1e-12:
            raise ValueError(f"C1/C2 radius mismatch at selected index {index}")
        for species in SPECIES:
            state = state_from_profile_row(row, species)
            mass = state.effective_mass_mev
            temperature = state.temperature_mev
            nu = state.effective_chemical_potential_mev
            if abs(nu-c2[f"nu_{species}_EOS_MeV"]) > 1e-10:
                raise ValueError(f"EOS chemical potential mismatch at r={row['r_km']}")
            prefix = "Fnn" if species == "n" else "Fpp"
            nprime = c2[f"nprime_{species}_fm3"]*HBARC**3
            fdeg = c2[f"{prefix}_deg"]
            blocked_q0 = nprime*fdeg
            direct_n, direct_blocked = phase_space_integrals(
                state, order=2048, tail_T=TAIL_T
            )
            if abs(direct_blocked/blocked_q0-1.0) > 5e-12:
                raise ArithmeticError("q0=0 blocked integral does not reproduce C2")

            for q in Q_VALUES_MEV:
                idyn, q0_rows = dynamic_sum_rule(q, mass, temperature, nu)
                istat = static_structure_factor(q, mass, temperature, nu)
                db = detailed_balance_residuals(q, mass, temperature, nu)
                max_db = max(abs(value) for value in db)
                sumrule_records.append({
                    "r_km": row["r_km"],
                    "species": species,
                    "q_MeV": q,
                    "I_dynamic_MeV3": idyn,
                    "I_static_MeV3": istat,
                    "sum_rule_relative_residual": idyn/istat-1.0,
                    "q0_zero_blocked_MeV3": blocked_q0,
                    "I_static_over_q0_zero_blocked": istat/blocked_q0,
                    "max_detailed_balance_relative_residual": max_db,
                })
                for q0, response in q0_rows:
                    response_records.append({
                        "r_km": row["r_km"],
                        "species": species,
                        "T_MeV": temperature,
                        "mstar_MeV": mass,
                        "nu_MeV": nu,
                        "eta_nu_over_T": nu/temperature,
                        "theta_T_over_mstar": temperature/mass,
                        "q_MeV": q,
                        "q0_MeV": q0,
                        "S_MeV2": response,
                    })

    by_species = {}
    for species in SPECIES:
        group = [record for record in sumrule_records if record["species"] == species]
        small_q = [record for record in group if record["q_MeV"] in (1.0, 3.0)]
        by_species[species] = {
            "max_abs_sum_rule_relative_residual": max(
                abs(record["sum_rule_relative_residual"]) for record in group
            ),
            "max_abs_detailed_balance_relative_residual": max(
                record["max_detailed_balance_relative_residual"] for record in group
            ),
            "max_abs_q1_static_vs_q0_blocked": max(
                abs(record["I_static_over_q0_zero_blocked"]-1.0)
                for record in small_q if record["q_MeV"] == 1.0
            ),
            "max_abs_q3_static_vs_q0_blocked": max(
                abs(record["I_static_over_q0_zero_blocked"]-1.0)
                for record in small_q if record["q_MeV"] == 3.0
            ),
        }

    acceptance = {
        "four_representative_radii_and_both_species": (
            len(sumrule_records) == 56 and len(response_records) == 56*Q0_ORDER
        ),
        "dynamic_static_sum_rule_below_1e_8": max(
            by_species["n"]["max_abs_sum_rule_relative_residual"],
            by_species["p"]["max_abs_sum_rule_relative_residual"],
        ) < 1e-8,
        "detailed_balance_below_1e_8": max(
            by_species["n"]["max_abs_detailed_balance_relative_residual"],
            by_species["p"]["max_abs_detailed_balance_relative_residual"],
        ) < 1e-8,
        "q1_static_limit_matches_nF_below_1e_4": max(
            by_species["n"]["max_abs_q1_static_vs_q0_blocked"],
            by_species["p"]["max_abs_q1_static_vs_q0_blocked"],
        ) < 1e-4,
        "q3_static_limit_matches_nF_below_1e_3": max(
            by_species["n"]["max_abs_q3_static_vs_q0_blocked"],
            by_species["p"]["max_abs_q3_static_vs_q0_blocked"],
        ) < 1e-3,
        "all_response_values_nonnegative": all(
            record["S_MeV2"] >= 0.0 for record in response_records
        ),
        "C2_blocked_integral_reproduced": True,
    }
    radii = [
        profile_rows[index]["r_km"] for index in SELECTED_PROFILE_INDICES
    ]
    summary = {
        "title": "P1-IIIe-C4A EOS-effective-mass dynamic scalar response",
        "date": "2026-11-11",
        "status": "PASS: dynamic/static sum rule, detailed balance, and q->0 susceptibility checked",
        "scope": (
            "Local scalar quasiparticle response at four selected radii of the "
            "t_pb=1 s Caputo SFHo-18.8 published-figure snapshot; no weak tensor, "
            "B.2 opacity, transport, or luminosity."
        ),
        "provenance": {
            "profile": "outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv",
            "C2_occupation": "outputs/p1iii_eos_full_radial_occupation_2026-11-11.csv",
            "C2_occupation_git_blob_sha": EXPECTED_C2_GIT_BLOB_SHA,
            "selected_profile_indices_zero_based": list(SELECTED_PROFILE_INDICES),
            "selected_radii_km": radii,
            "species": list(SPECIES),
            "q_values_MeV": list(Q_VALUES_MEV),
            "q0_Gauss_Legendre_order": Q0_ORDER,
            "momentum_Gauss_Legendre_order": P_ORDER,
            "static_p_and_cosine_orders": [STATIC_P_ORDER, STATIC_C_ORDER],
            "kinetic_energy_tail_T": TAIL_T,
        },
        "quasiparticle_convention": {
            "Estar_p": "sqrt(p^2+mstar_N(r)^2)",
            "kinetic_energy": "E_star-mstar_N",
            "occupation": "1/[exp((E_star-mstar_N-nu_N(r))/T(r))+1]",
            "nu_N": "mu_N^nonrel-U_N",
            "same_species_energy_transfer": "q0=E_star(p+q)-E_star(p); constant U_N cancels",
            "spin_degeneracy": 2,
            "response": "S_N(q0,q)=1/(pi*q) integral_{pmin}^infinity dp p*(E_star+q0)*f_i*(1-f_f)",
            "units": "S in MeV^2; int dq0/(2pi) S in MeV^3",
        },
        "species": by_species,
        "acceptance": acceptance,
        "overall_pass": all(acceptance.values()),
        "interpretation": [
            "The finite-q dynamic response is evaluated with the same m*_N and nu_N as the C2 EOS occupation.",
            "The dynamic/static sum rule checks the exact q0 integration against the independent three-dimensional static integral.",
            "Detailed balance is checked only where both response directions are numerically supported; q0/T is capped at 4 to avoid testing exponentially tiny tails.",
            "The q=1 and 3 MeV static integrals approach the q=0 susceptibility n'_N Fdeg from C2.",
            "This scalar response is a thermodynamic/phase-space validation layer, not the full vector/axial weak tensor.",
            "RPA, NN correlations, in-medium vertex corrections, and radial B.2 transport are outside this stage.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C4-A acceptance failed: {acceptance}")
    return response_records, sumrule_records, summary


def _write_csv(path: Path, records: list[dict], columns: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows({
            key: f"{record[key]:.16g}" if isinstance(record[key], float) else record[key]
            for key in columns
        } for record in records)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--c2-reference", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-response-csv", type=Path, required=True)
    parser.add_argument("--output-sumrule-csv", type=Path, required=True)
    args = parser.parse_args()
    profile_rows = load_profile(args.profile)
    c2_rows = load_c2_reference(args.c2_reference)
    response, sumrules, summary = analyze(profile_rows, c2_rows)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(summary, indent=2, allow_nan=False)+"\n", encoding="utf-8"
    )
    _write_csv(args.output_response_csv, response, RESPONSE_COLUMNS)
    _write_csv(args.output_sumrule_csv, sumrules, SUMRULE_COLUMNS)
    print(json.dumps({
        "overall_pass": summary["overall_pass"],
        "species": summary["species"],
        "acceptance": summary["acceptance"],
    }, indent=2))


if __name__ == "__main__":
    main()
