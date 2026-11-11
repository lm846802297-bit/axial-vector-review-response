#!/usr/bin/env python3
"""Verify the local Fdeg density-derivative identity over the full C1 SFHo profile."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import (
    load_profile,
    state_from_profile_row,
)
from audit_b16_p1iii_eos_nucleon_distribution import (
    degeneracy_factor_from_density_derivative,
    phase_space_integrals,
)

HERE = Path(__file__).resolve().parent
EXPECTED_C2_GIT_BLOB_SHA = "c472040a4551e68ffadbf7addf9402663f99e7e3"
EXPECTED_C1_PROFILE_SHA256 = "97d6a88a95d0a636ac359ae981b1b06ec33b88b0f106bfb88d203cb0f9fbbc59"
ORDER = 2048
TAIL_T = 45.0
STEP_FRACTION = 3.0e-5
SPECIES = ("n", "p")
OUTPUT_COLUMNS = (
    "r_km", "T_MeV",
    "Fnn_direct", "Fnn_density_derivative", "Fnn_abs_difference",
    "Fnn_relative_difference", "Fnn_C2_reference",
    "Fnn_direct_vs_C2_abs_difference", "Fnn_h_MeV",
    "Fpp_direct", "Fpp_density_derivative", "Fpp_abs_difference",
    "Fpp_relative_difference", "Fpp_C2_reference",
    "Fpp_direct_vs_C2_abs_difference", "Fpp_h_MeV",
)


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    payload = f"blob {len(data)}\0".encode("ascii") + data
    return hashlib.sha1(payload).hexdigest()


def load_c2_reference(path: Path) -> list[dict[str, float]]:
    actual_sha = git_blob_sha1(path)
    if actual_sha != EXPECTED_C2_GIT_BLOB_SHA:
        raise ValueError(f"C2 occupation CSV Git blob SHA mismatch: {actual_sha}")
    with path.open("r", newline="", encoding="utf-8") as stream:
        raw = list(csv.DictReader(stream))
    if len(raw) != 301:
        raise ValueError(f"expected 301 C2 occupation rows, found {len(raw)}")
    required = {
        "r_km", "Fnn_deg", "Fpp_deg", "nu_n_EOS_MeV", "nu_p_EOS_MeV",
    }
    if not required.issubset(raw[0]):
        raise ValueError(f"missing C2 reference columns: {sorted(required-set(raw[0]))}")
    return [{key: float(value) for key, value in row.items()} for row in raw]


def _rms(values: list[float]) -> float:
    return math.sqrt(math.fsum(value*value for value in values)/len(values))


def _max_abs(records: list[dict], key: str) -> dict:
    return max(records, key=lambda row: abs(row[key]))


def analyze_profile(
    profile_rows: list[dict[str, float]],
    reference_rows: list[dict[str, float]],
) -> tuple[list[dict], dict]:
    if len(profile_rows) != len(reference_rows):
        raise ValueError("C1 and C2 inputs have different radial lengths")

    records: list[dict] = []
    for index, (row, reference) in enumerate(zip(profile_rows, reference_rows)):
        if abs(row["r_km"]-reference["r_km"]) > 1e-12:
            raise ValueError(f"C1/C2 radial mismatch at row {index}")
        out = {"r_km": row["r_km"], "T_MeV": row["T_MeV"]}
        for species in SPECIES:
            state = state_from_profile_row(row, species)
            number, blocked = phase_space_integrals(
                state, order=ORDER, tail_T=TAIL_T
            )
            if number <= 0.0 or not (0.0 <= blocked <= number):
                raise ArithmeticError(
                    f"invalid phase-space integrals for {species} at r={row['r_km']}"
                )
            f_direct = blocked/number
            f_derivative = degeneracy_factor_from_density_derivative(
                state,
                order=ORDER,
                tail_T=TAIL_T,
                step_fraction=STEP_FRACTION,
            )
            c2_key = "Fnn_deg" if species == "n" else "Fpp_deg"
            f_c2 = reference[c2_key]
            if not all(math.isfinite(value) for value in (f_direct, f_derivative, f_c2)):
                raise ArithmeticError(
                    f"non-finite Fdeg for {species} at r={row['r_km']}"
                )
            out.update({
                f"{species}_F_direct": f_direct,
                f"{species}_F_density_derivative": f_derivative,
                f"{species}_abs_difference": f_derivative-f_direct,
                f"{species}_relative_difference": (f_derivative-f_direct)/f_direct,
                f"{species}_C2_reference": f_c2,
                f"{species}_direct_vs_C2_abs_difference": f_direct-f_c2,
                f"{species}_h_MeV": STEP_FRACTION*row["T_MeV"],
            })
        records.append(out)

    species_summary = {}
    for species in SPECIES:
        rel_key = f"{species}_relative_difference"
        abs_key = f"{species}_abs_difference"
        c2_key = f"{species}_direct_vs_C2_abs_difference"
        direct_key = f"{species}_F_direct"
        rel_ext = _max_abs(records, rel_key)
        abs_ext = _max_abs(records, abs_key)
        c2_ext = _max_abs(records, c2_key)
        species_summary[species] = {
            "Fdeg_range": [
                min(row[direct_key] for row in records),
                max(row[direct_key] for row in records),
            ],
            "rms_relative_difference": _rms(
                [row[rel_key] for row in records]
            ),
            "max_abs_relative_difference": abs(rel_ext[rel_key]),
            "max_signed_relative_difference": rel_ext[rel_key],
            "max_abs_relative_at_km": rel_ext["r_km"],
            "max_abs_absolute_difference": abs(abs_ext[abs_key]),
            "max_abs_absolute_difference_at_km": abs_ext["r_km"],
            "max_abs_direct_vs_C2_reference": abs(c2_ext[c2_key]),
            "direct_vs_C2_at_km": c2_ext["r_km"],
        }

    radii = [row["r_km"] for row in records]
    steps = [b-a for a, b in zip(radii[:-1], radii[1:])]
    acceptance = {
        "points_301": len(records) == 301,
        "uniform_grid_0p05km": max(abs(step-0.05) for step in steps) < 1e-8,
        "neutron_derivative_identity_below_1e_8":
            species_summary["n"]["max_abs_relative_difference"] < 1e-8,
        "proton_derivative_identity_below_1e_8":
            species_summary["p"]["max_abs_relative_difference"] < 1e-8,
        "direct_integral_matches_C2_archive_below_5e_12": max(
            species_summary["n"]["max_abs_direct_vs_C2_reference"],
            species_summary["p"]["max_abs_direct_vs_C2_reference"],
        ) < 5e-12,
        "all_factors_between_zero_and_one": all(
            0.0 < row[f"{species}_F_direct"] < 1.0
            and 0.0 < row[f"{species}_F_density_derivative"] < 1.0
            for row in records for species in SPECIES
        ),
    }
    summary = {
        "title": "P1-IIIe-C3A full-radial degeneracy-factor derivative identity",
        "date": "2026-11-11",
        "status": "PASS: direct blocked integral agrees with finite-difference density derivative at all 301 radii",
        "scope": (
            "301-point t_pb=1 s Caputo SFHo-18.8 published-figure snapshot; "
            "local static degeneracy identity only; not a time-space weighted core average."
        ),
        "provenance": {
            "C1_profile_sha256": EXPECTED_C1_PROFILE_SHA256,
            "C2_occupation_csv_git_blob_sha": EXPECTED_C2_GIT_BLOB_SHA,
            "radial_points": len(records),
            "radial_range_km": [radii[0], radii[-1]],
            "radial_step_km": 0.05,
            "snapshot_time_post_bounce_s": 1.0,
        },
        "convention": {
            "F_direct": "integral p^2 f(1-f) / integral p^2 f",
            "F_density_derivative":
                "T/n' * [n'(nu+h)-n'(nu-h)]/(2h)",
            "fixed_parameters": ["T", "m_N*", "U_N", "xi_SPP"],
            "varied_parameter":
                "mu_N^nonrel by +/-h at fixed U_N, hence nu_N by +/-h",
            "step_fraction_h_over_T": STEP_FRACTION,
            "quadrature_order": ORDER,
            "tail_T": TAIL_T,
            "spin_degeneracy": 2,
        },
        "species": species_summary,
        "acceptance": acceptance,
        "overall_pass": all(acceptance.values()),
        "interpretation": [
            "The direct blocked integral and the thermodynamic density derivative are evaluated by independent numerical routes.",
            "The derivative is taken at fixed T, m_N*, U_N and xi; only mu_N^nonrel, equivalently nu_N, is varied.",
            "xi cancels in Fdeg because it multiplies both n' and its derivative at fixed xi.",
            "The result is a local identity check at one t_pb=1 s snapshot; it is not the global weighted degeneracy factor in Fiorillo Table 1.",
            "No dynamic response, B.2 opacity, transport, luminosity, Fig. 7 benchmark, manuscript, or axial cooling curve is modified.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C3-A acceptance failed: {acceptance}")
    return records, summary


def write_csv(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows({
            key: f"{row[key]:.16g}" for key in OUTPUT_COLUMNS
        } for row in records)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--c2-reference", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()

    profile_rows = load_profile(args.profile)
    reference_rows = load_c2_reference(args.c2_reference)
    records, summary = analyze_profile(profile_rows, reference_rows)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(summary, indent=2, allow_nan=False)+"\n",
        encoding="utf-8",
    )
    write_csv(args.output_csv, records)
    print(json.dumps({
        "overall_pass": summary["overall_pass"],
        "species": summary["species"],
        "acceptance": summary["acceptance"],
    }, indent=2))


if __name__ == "__main__":
    main()
