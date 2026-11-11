#!/usr/bin/env python3
"""Scan the central finite-difference step for the full-radial Fdeg identity."""
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
    NucleonEOSState,
    phase_space_integrals,
)

HERE = Path(__file__).resolve().parent
EXPECTED_C2_GIT_BLOB_SHA = "c472040a4551e68ffadbf7addf9402663f99e7e3"
STEP_LABELS = ("1e-2", "3e-3", "1e-3", "3e-4", "2e-4", "1e-4", "3e-5", "1e-5", "3e-6")
STEP_FRACTIONS = (1e-2, 3e-3, 1e-3, 3e-4, 2e-4, 1e-4, 3e-5, 1e-5, 3e-6)
SELECTED_STEP_LABEL = "3e-5"
SELECTED_STEP_FRACTION = 3.0e-5
ORDER = 2048
TAIL_T = 45.0
SPECIES = ("n", "p")
OUTPUT_COLUMNS = (
    "r_km", "species", "step_fraction_h_over_T", "h_MeV",
    "F_direct", "F_density_derivative", "abs_difference",
    "relative_difference", "C2_reference",
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
    required = {"r_km", "Fnn_deg", "Fpp_deg", "nu_n_EOS_MeV", "nu_p_EOS_MeV"}
    if not required.issubset(raw[0]):
        raise ValueError(f"missing C2 columns: {sorted(required-set(raw[0]))}")
    return [{key: float(value) for key, value in row.items()} for row in raw]


def _rms(values: list[float]) -> float:
    return math.sqrt(math.fsum(value*value for value in values)/len(values))


def analyze_profile(
    profile_rows: list[dict[str, float]],
    reference_rows: list[dict[str, float]],
) -> tuple[list[dict], dict]:
    if len(profile_rows) != 301 or len(reference_rows) != 301:
        raise ValueError("C3-B requires exactly 301 aligned radial states")

    records: list[dict] = []
    for index, (row, reference) in enumerate(zip(profile_rows, reference_rows)):
        if abs(row["r_km"]-reference["r_km"]) > 1e-12:
            raise ValueError(f"C1/C2 radial mismatch at row {index}")
        for species in SPECIES:
            state = state_from_profile_row(row, species)
            number0, blocked0 = phase_space_integrals(
                state, order=ORDER, tail_T=TAIL_T
            )
            if number0 <= 0.0 or not (0.0 <= blocked0 <= number0):
                raise ArithmeticError(
                    f"invalid direct integral for {species} at r={row['r_km']}"
                )
            f_direct = blocked0/number0
            ref_key = "Fnn_deg" if species == "n" else "Fpp_deg"
            c2_reference = reference[ref_key]
            if abs(f_direct-c2_reference) >= 5e-12:
                raise ArithmeticError(
                    f"direct Fdeg does not reproduce C2 at r={row['r_km']} ({species})"
                )

            for label, step_fraction in zip(STEP_LABELS, STEP_FRACTIONS):
                h = step_fraction*row["T_MeV"]
                plus = NucleonEOSState(
                    state.species,
                    state.temperature_mev,
                    state.effective_mass_mev,
                    state.scalar_potential_mev,
                    state.chemical_potential_star_mev+h,
                )
                minus = NucleonEOSState(
                    state.species,
                    state.temperature_mev,
                    state.effective_mass_mev,
                    state.scalar_potential_mev,
                    state.chemical_potential_star_mev-h,
                )
                n_plus, _ = phase_space_integrals(
                    plus, order=ORDER, tail_T=TAIL_T
                )
                n_minus, _ = phase_space_integrals(
                    minus, order=ORDER, tail_T=TAIL_T
                )
                f_derivative = (
                    row["T_MeV"]*(n_plus-n_minus)/(2.0*h*number0)
                )
                absolute = f_derivative-f_direct
                relative = absolute/f_direct
                if not all(math.isfinite(value) for value in (
                    f_direct, f_derivative, absolute, relative, h
                )):
                    raise ArithmeticError(
                        f"non-finite step-scan result for {species} at r={row['r_km']}"
                    )
                records.append({
                    "r_km": row["r_km"],
                    "species": species,
                    "step_fraction_h_over_T": step_fraction,
                    "h_MeV": h,
                    "F_direct": f_direct,
                    "F_density_derivative": f_derivative,
                    "abs_difference": absolute,
                    "relative_difference": relative,
                    "C2_reference": c2_reference,
                })

    summary_by_species = {}
    for species in SPECIES:
        summary_by_species[species] = {}
        for label in STEP_LABELS:
            group = [
                record for record in records
                if record["species"] == species
                and math.isclose(
                    record["step_fraction_h_over_T"],
                    STEP_FRACTIONS[STEP_LABELS.index(label)],
                    rel_tol=0.0, abs_tol=1e-16,
                )
            ]
            relative = [record["relative_difference"] for record in group]
            absolute = [record["abs_difference"] for record in group]
            rel_ext = max(group, key=lambda record: abs(record["relative_difference"]))
            abs_ext = max(group, key=lambda record: abs(record["abs_difference"]))
            summary_by_species[species][label] = {
                "rms_relative": _rms(relative),
                "max_abs_relative": abs(rel_ext["relative_difference"]),
                "max_signed_relative": rel_ext["relative_difference"],
                "max_abs_relative_at_km": rel_ext["r_km"],
                "max_abs_absolute_difference": abs(abs_ext["abs_difference"]),
                "max_abs_absolute_difference_at_km": abs_ext["r_km"],
            }

    truncation_scaling = {}
    for species in SPECIES:
        large = summary_by_species[species]["1e-2"]
        small = summary_by_species[species]["1e-3"]
        truncation_scaling[species] = {
            "max_error_ratio_1e_2_over_1e_3":
                large["max_abs_relative"]/small["max_abs_relative"],
            "rms_error_ratio_1e_2_over_1e_3":
                large["rms_relative"]/small["rms_relative"],
        }

    selected = {
        species: summary_by_species[species][SELECTED_STEP_LABEL]
        for species in SPECIES
    }
    acceptance = {
        "points_301": len({record["r_km"] for record in records}) == 301,
        "nine_step_sizes": len(STEP_FRACTIONS) == 9,
        "selected_step_3e_5_below_1e_8": max(
            selected["n"]["max_abs_relative"],
            selected["p"]["max_abs_relative"],
        ) < 1e-8,
        "central_difference_large_step_scales_as_h2": all(
            80.0 < truncation_scaling[species]["max_error_ratio_1e_2_over_1e_3"] < 120.0
            for species in SPECIES
        ),
        "all_direct_factors_in_unit_interval": all(
            0.0 < record["F_direct"] < 1.0 for record in records
        ),
        "all_density_derivatives_positive": all(
            record["F_density_derivative"] > 0.0 for record in records
        ),
    }
    radii = sorted({record["r_km"] for record in records})
    summary = {
        "title": "P1-IIIe-C3B full-radial finite-difference step scan",
        "date": "2026-11-11",
        "status": "PASS: finite-difference truncation and roundoff regimes resolved over all radial points",
        "scope": (
            "301-point t_pb=1 s Caputo SFHo-18.8 published-figure snapshot; "
            "local static degeneracy identity; not a time-space weighted core average."
        ),
        "provenance": {
            "C1_profile_sha256":
                "97d6a88a95d0a636ac359ae981b1b06ec33b88b0f106bfb88d203cb0f9fbbc59",
            "C2_occupation_csv_git_blob_sha": EXPECTED_C2_GIT_BLOB_SHA,
            "radial_points": len(radii),
            "radial_range_km": [radii[0], radii[-1]],
            "radial_step_km": 0.05,
            "snapshot_time_post_bounce_s": 1.0,
        },
        "method": {
            "quadrature_order": ORDER,
            "tail_T": TAIL_T,
            "difference": "central two-point finite difference of n'(nu)",
            "step_fractions_h_over_T": list(STEP_FRACTIONS),
            "held_fixed": ["T", "m_N*", "U_N", "xi_SPP"],
            "varied": "mu_N^nonrel by +/-h at fixed U_N",
        },
        "species": summary_by_species,
        "selected_shared_step": {
            "step_fraction_h_over_T": SELECTED_STEP_FRACTION,
            "max_species_max_relative":
                max(selected["n"]["max_abs_relative"], selected["p"]["max_abs_relative"]),
        },
        "truncation_scaling_ratio": truncation_scaling,
        "acceptance": acceptance,
        "overall_pass": all(acceptance.values()),
        "interpretation": [
            "At h/T=1e-2 to 1e-3, the maximum residual falls by approximately 100 when h is reduced by 10, consistent with O(h^2) central-difference truncation error.",
            "The shared working step is h/T=3e-5; it keeps both species below 1e-8 relative error over the full radial profile.",
            "For smaller steps (1e-5 and 3e-6), the residual rises again, consistent with cancellation/roundoff in n'(nu+h)-n'(nu-h).",
            "The step scan does not alter the primary C2 occupation or Fdeg values; it only validates the numerical derivative method.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C3-B acceptance failed: {acceptance}")
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
        "selected_shared_step": summary["selected_shared_step"],
        "species": summary["species"],
        "acceptance": summary["acceptance"],
    }, indent=2))


if __name__ == "__main__":
    main()
