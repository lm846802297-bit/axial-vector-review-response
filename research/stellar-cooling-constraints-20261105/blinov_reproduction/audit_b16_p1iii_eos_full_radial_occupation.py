#!/usr/bin/env python3
"""Reconstruct neutron/proton Fermi occupations over the full C1 SFHo profile."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

from audit_b16_p1iii_eos_nucleon_distribution import (
    HBARC_MEV_FM,
    NucleonEOSState,
    phase_space_integrals,
    state_from_available_volume_density,
)

HERE = Path(__file__).resolve().parent
EXPECTED_PROFILE_SHA256 = "97d6a88a95d0a636ac359ae981b1b06ec33b88b0f106bfb88d203cb0f9fbbc59"
ORDERS = (512, 1024, 2048)
TAIL_T = 45.0
SPECIES = ("n", "p")
OUTPUT_COLUMNS = (
    "r_km", "T_MeV", "nB_fm3", "xi_SPP", "X_n", "X_p",
    "nprime_n_fm3", "nprime_p_fm3",
    "n_n_total_fm3", "n_p_total_fm3",
    "n_n_target_EOS_fm3", "n_p_target_EOS_fm3",
    "nu_n_EOS_MeV", "nu_p_EOS_MeV",
    "delta_nu_n_MeV", "delta_nu_p_MeV",
    "Fnn_deg", "Fpp_deg",
    "Fnn_deg_density_matched", "Fpp_deg_density_matched",
    "density_rel_residual_n", "density_rel_residual_p",
    "delta_Fnn_deg", "delta_Fpp_deg",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_profile(path: Path) -> list[dict[str, float]]:
    digest = sha256_file(path)
    if digest != EXPECTED_PROFILE_SHA256:
        raise ValueError(f"C1 input SHA-256 mismatch: {digest}")
    with path.open("r", newline="", encoding="utf-8") as stream:
        raw = list(csv.DictReader(stream))
    if len(raw) != 301:
        raise ValueError(f"expected 301 radial points, found {len(raw)}")
    required = {
        "r_km", "T_MeV", "nB_fm3", "xi_SPP", "X_n", "X_p",
        "mstar_n_MeV", "mstar_p_MeV", "U_n_MeV", "U_p_MeV",
        "mu_n_nonrel_MeV", "mu_p_nonrel_MeV",
        "n_n_free_fm3", "n_p_free_fm3",
    }
    if not required.issubset(raw[0]):
        raise ValueError(f"missing profile columns: {sorted(required-set(raw[0]))}")
    rows = [{key: float(value) for key, value in row.items()} for row in raw]
    radii = [row["r_km"] for row in rows]
    steps = [b-a for a, b in zip(radii[:-1], radii[1:])]
    if any(step <= 0 for step in steps) or max(abs(x-0.05) for x in steps) > 1e-8:
        raise ValueError("C1 radial grid is not strictly increasing at 0.05 km")
    for i, row in enumerate(rows):
        if row["T_MeV"] <= 0 or row["nB_fm3"] <= 0:
            raise ValueError(f"non-positive T or nB at row {i}")
        if not 0 < row["xi_SPP"] <= 1:
            raise ValueError(f"unphysical xi at row {i}")
        if row["mstar_n_MeV"] <= 0 or row["mstar_p_MeV"] <= 0:
            raise ValueError(f"non-positive effective mass at row {i}")
        if min(row["X_n"], row["X_p"]) < 0 or row["X_n"]+row["X_p"] > 1+1e-8:
            raise ValueError(f"unphysical free-nucleon fractions at row {i}")
    return rows


def state_from_profile_row(row: dict[str, float], species: str) -> NucleonEOSState:
    return NucleonEOSState(
        species=species,
        temperature_mev=row["T_MeV"],
        effective_mass_mev=row[f"mstar_{species}_MeV"],
        scalar_potential_mev=row[f"U_{species}_MeV"],
        chemical_potential_star_mev=row[f"mu_{species}_nonrel_MeV"],
    )


def _integrals(state: NucleonEOSState, order: int) -> tuple[float, float]:
    return phase_space_integrals(state, order=order, tail_T=TAIL_T)


def _rms(values: list[float]) -> float:
    return math.sqrt(math.fsum(value*value for value in values)/len(values))


def _extreme(records: list[dict], key: str) -> dict:
    row = max(records, key=lambda item: abs(item[key]))
    return {"value": row[key], "abs_value": abs(row[key]), "r_km": row["r_km"]}


def analyze_profile_rows(rows: list[dict[str, float]]) -> tuple[list[dict], dict]:
    records: list[dict] = []
    hbarc3 = HBARC_MEV_FM**3
    for row in rows:
        out = {
            "r_km": row["r_km"], "T_MeV": row["T_MeV"],
            "nB_fm3": row["nB_fm3"], "xi_SPP": row["xi_SPP"],
            "X_n": row["X_n"], "X_p": row["X_p"],
        }
        for species in SPECIES:
            state = state_from_profile_row(row, species)
            nu = state.effective_chemical_potential_mev
            target = row[f"X_{species}"]*row["nB_fm3"]
            target_caputo = row[f"n_{species}_free_fm3"]
            xi = row["xi_SPP"]
            if target <= 0 or target_caputo <= 0:
                raise ValueError(f"non-positive {species} target at r={row['r_km']}")
            integrals = {order: _integrals(state, order) for order in ORDERS}
            n512, b512 = integrals[512]
            n1024, b1024 = integrals[1024]
            n2048, b2048 = integrals[2048]
            nprime = n2048/hbarc3
            fdeg = b2048/n2048
            actual = xi*nprime
            matched = state_from_available_volume_density(
                species=species,
                temperature_mev=row["T_MeV"],
                effective_mass_mev=row[f"mstar_{species}_MeV"],
                density_per_available_volume_fm3=target/xi,
                order=512,
                tail_T=TAIL_T,
            )
            matched_n, matched_blocked = _integrals(matched, 2048)
            fdeg_matched = matched_blocked/matched_n
            nu_matched = matched.effective_chemical_potential_mev
            prefix = "Fnn" if species == "n" else "Fpp"
            out.update({
                f"nprime_{species}_fm3": nprime,
                f"n_{species}_total_fm3": actual,
                f"n_{species}_target_EOS_fm3": target,
                f"nu_{species}_EOS_MeV": nu,
                f"delta_nu_{species}_MeV": nu_matched-nu,
                f"{prefix}_deg": fdeg,
                f"{prefix}_deg_density_matched": fdeg_matched,
                f"density_rel_residual_{species}": actual/target-1,
                f"delta_{prefix}_deg": fdeg_matched-fdeg,
                f"quadrature_rel_change_{species}_2048_vs_512": n2048/n512-1,
                f"quadrature_abs_F_change_{species}_2048_vs_512": abs(b2048/n2048-b512/n512),
                f"quadrature_rel_change_{species}_2048_vs_1024": n2048/n1024-1,
                f"quadrature_abs_F_change_{species}_2048_vs_1024": abs(b2048/n2048-b1024/n1024),
                f"density_rel_residual_vs_Caputo_{species}": actual/target_caputo-1,
            })
        records.append(out)

    species_summary = {}
    for species in SPECIES:
        residual_key = f"density_rel_residual_{species}"
        caputo_key = f"density_rel_residual_vs_Caputo_{species}"
        actual_key = f"n_{species}_total_fm3"
        target_key = f"n_{species}_target_EOS_fm3"
        nu_key = f"delta_nu_{species}_MeV"
        prefix = "Fnn" if species == "n" else "Fpp"
        f_key = f"{prefix}_deg"
        fm_key = f"{prefix}_deg_density_matched"
        df_key = f"delta_{prefix}_deg"
        density_diffs = [r[actual_key]-r[target_key] for r in records]
        max_density_row = max(records, key=lambda r: abs(r[actual_key]-r[target_key]))
        density_ext = _extreme(records, residual_key)
        nu_ext = _extreme(records, nu_key)
        df_ext = _extreme(records, df_key)
        species_summary[species] = {
            "density": {
                "rms_relative": _rms([r[residual_key] for r in records]),
                "max_abs_relative": density_ext["abs_value"],
                "max_abs_relative_at_km": density_ext["r_km"],
                "max_abs_density_fm3": abs(max_density_row[actual_key]-max_density_row[target_key]),
                "max_abs_density_at_km": max_density_row["r_km"],
                "rms_abs_density_fm3": _rms(density_diffs),
                "max_abs_vs_caputo": _extreme(records, caputo_key)["abs_value"],
            },
            "nprime_range": [
                min(r[f"nprime_{species}_fm3"] for r in records),
                max(r[f"nprime_{species}_fm3"] for r in records),
            ],
            "actual_range": [
                min(r[actual_key] for r in records), max(r[actual_key] for r in records),
            ],
            "Fdeg_range": [min(r[f_key] for r in records), max(r[f_key] for r in records)],
            "Fdeg_matched_range": [min(r[fm_key] for r in records), max(r[fm_key] for r in records)],
            "max_abs_delta_nu_MeV": nu_ext["abs_value"],
            "delta_nu_at_km": nu_ext["r_km"],
            "max_abs_delta_Fdeg": df_ext["abs_value"],
            "delta_Fdeg_at_km": df_ext["r_km"],
            "quadrature_max_relative_n_change_2048_vs_512": max(
                abs(r[f"quadrature_rel_change_{species}_2048_vs_512"]) for r in records
            ),
            "quadrature_max_abs_F_change_2048_vs_512": max(
                r[f"quadrature_abs_F_change_{species}_2048_vs_512"] for r in records
            ),
        }

    radii = [row["r_km"] for row in rows]
    steps = [b-a for a, b in zip(radii[:-1], radii[1:])]
    acceptance = {
        "points_301": len(rows) == 301,
        "uniform_grid_0p05km": max(abs(step-0.05) for step in steps) < 1e-8,
        "neutron_density_closure_below_1pct": species_summary["n"]["density"]["max_abs_relative"] < 1e-2,
        "proton_density_closure_below_1pct": species_summary["p"]["density"]["max_abs_relative"] < 1e-2,
        "neutron_delta_nu_below_0p12MeV": species_summary["n"]["max_abs_delta_nu_MeV"] < 0.12,
        "proton_delta_nu_below_0p20MeV": species_summary["p"]["max_abs_delta_nu_MeV"] < 0.20,
        "density_matched_Fdeg_shift_below_5e_4": max(
            species_summary["n"]["max_abs_delta_Fdeg"],
            species_summary["p"]["max_abs_delta_Fdeg"],
        ) < 5e-4,
        "quadrature_2048_vs512_below_1e_10": max(
            species_summary["n"]["quadrature_max_relative_n_change_2048_vs_512"],
            species_summary["p"]["quadrature_max_relative_n_change_2048_vs_512"],
            species_summary["n"]["quadrature_max_abs_F_change_2048_vs_512"],
            species_summary["p"]["quadrature_max_abs_F_change_2048_vs_512"],
        ) < 1e-10,
    }
    c1_path = HERE/"outputs"/"caputo_sfho_eos_profile_full_0p05km_2026-11-11.json"
    c1 = json.loads(c1_path.read_text(encoding="utf-8"))
    summary = {
        "title": "P1-IIIe-C2 full-radial EOS-consistent nucleon Fermi distributions",
        "date": "2026-11-11",
        "status": "PASS: sub-percent local density closure",
        "scope": "301-point t_pb=1 s Caputo SFHo-18.8 published-figure snapshot; not raw time-dependent Garching simulation data and not a mass-time weighted core average.",
        "provenance": {
            "input_profile": "outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv",
            "input_profile_sha256": EXPECTED_PROFILE_SHA256,
            "source_archive_sha256": c1["source"]["archive_sha256"],
            "eos_tables_sha256": c1["eos_tables_sha256"],
            "eos_coordinate": "Yp_tot=Ye+Ymu",
            "radial_points": len(rows),
            "radial_range_km": [radii[0], radii[-1]],
            "radial_step_km": 0.05,
            "snapshot_time_post_bounce_s": 1.0,
        },
        "convention": {
            "mu_F_star": "mu_N^nonrel",
            "U_N": "m_N^*-m_N+SigmaV_N^tot",
            "nu_N": "mu_N^nonrel-U_N",
            "K_N": "sqrt(p^2+m_N*^2)-m_N*",
            "density_per_available_volume": "1/[pi^2*(hbar*c)^3] integral dp p^2 f",
            "total_volume_density": "xi_SPP*n_N'",
            "EOS_target": "X_N^EOS*n_B",
            "spin_degeneracy": 2,
            "hbarc_MeV_fm": HBARC_MEV_FM,
        },
        "numerical_method": {
            "quadrature": "Gauss-Legendre; Kmax=max(nu,0)+45T",
            "orders": list(ORDERS),
            "density_matched": "diagnostic only; target n'_N=X_N*nB/xi",
        },
        "species": species_summary,
        "thresholds": {
            "max_abs_relative_density_residual": 0.01,
            "max_abs_delta_nu_n_MeV": 0.12,
            "max_abs_delta_nu_p_MeV": 0.20,
            "max_abs_delta_Fdeg": 5e-4,
            "max_abs_quadrature_change": 1e-10,
        },
        "acceptance": acceptance,
        "overall_pass": all(acceptance.values()),
        "interpretation": [
            "Primary occupations use tabulated Hempel/Fiorillo chemical potentials without density refitting.",
            "Density-matched chemical potentials are diagnostics only and do not replace the EOS baseline.",
            "The largest relative proton residual occurs in the outer low-free-proton-abundance region and remains below 1%.",
            "Local Fdeg ranges are static t_pb=1 s snapshot diagnostics, not Fiorillo Table 1 space-time weighted averages.",
            "No dynamic response, B.2 opacity, transport, luminosity, Fig. 7 benchmark, manuscript, or axial cooling curve is modified.",
        ],
    }
    if not summary["overall_pass"]:
        raise AssertionError(f"C2 acceptance failed: {acceptance}")
    return records, summary


def write_csv(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows({
            key: (f"{row[key]:.16g}" if isinstance(row[key], float) else row[key])
            for key in OUTPUT_COLUMNS
        } for row in records)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()
    rows = load_profile(args.profile)
    records, summary = analyze_profile_rows(rows)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(summary, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    write_csv(args.output_csv, records)
    print(json.dumps({"overall_pass": summary["overall_pass"], "species": summary["species"]}, indent=2))


if __name__ == "__main__":
    main()
