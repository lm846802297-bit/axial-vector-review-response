#!/usr/bin/env python3
"""C4-C4 energy-dependent combined quadrature-convergence audit."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support import PROFILE_INDICES, SPECIES, load_c2_reference
from audit_b16_p1iii_eos_c4c2_full_angle_total_scattering import (
    LOCAL_SUPPORT_SCAN,
    integrate_total_rate,
)
from audit_b16_p1iii_eos_c4c4_energy_dependence import (
    ENERGY_GRID_MEV,
    NEW_ENERGIES_MEV,
    git_blob_sha,
    read_csv,
)

HERE = Path(__file__).resolve().parent
PROFILE_PATH = HERE / "outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_PATH = HERE / "outputs/p1iii_eos_full_radial_occupation_2026-11-11.csv"
BASE_SCAN_PATH = HERE / "outputs/c4c4_energy_dependence_2026-11-12/local_rates_96.csv"
EXPECTED_BASE_SCAN_GIT_BLOB = "8be3757cf28011132a82b5c2373aa3c1fa59d342"

BASE_ORDERS = {"cosine": 8, "Eprime": 48, "initial_momentum": 36, "azimuth": 12}
HIGH_ORDERS = {"cosine": 12, "Eprime": 72, "initial_momentum": 48, "azimuth": 16}
ANTINU_VALUES = (False, True)
RELATIVE_TOLERANCE = 1.0e-2
OUTPUT_FIELDS = (
    "E_MeV", "profile_index", "r_km", "species", "antinu",
    "gamma_base_MeV", "gamma_high_MeV", "relative_difference",
    "base_cosine_order", "base_Eprime_order", "base_initial_momentum_order", "base_azimuth_order",
    "high_cosine_order", "high_Eprime_order", "high_initial_momentum_order", "high_azimuth_order",
    "support_root_max_relative_residual",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"refusing to write an empty CSV: {path}")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def case_key(energy: float, radius: float, species: str, antinu: str | bool) -> tuple:
    anti = str(antinu)
    return (float(energy), round(float(radius), 8), species, anti)


def expected_keys(radii: tuple[float, ...] | list[float]) -> set[tuple]:
    return {
        case_key(energy, radius, species, anti)
        for energy in NEW_ENERGIES_MEV
        for radius in radii
        for species in SPECIES
        for anti in ANTINU_VALUES
    }


def relative_difference(high: float, base: float) -> float:
    if not (math.isfinite(high) and math.isfinite(base) and high > 0.0 and base > 0.0):
        raise ValueError("base and high-order rates must be finite and positive")
    return abs(high / base - 1.0)


def load_base_scan() -> list[dict[str, str]]:
    actual = git_blob_sha(BASE_SCAN_PATH)
    if actual != EXPECTED_BASE_SCAN_GIT_BLOB:
        raise ValueError(f"C4-C4 base scan blob SHA mismatch: expected {EXPECTED_BASE_SCAN_GIT_BLOB}, got {actual}")
    rows = read_csv(BASE_SCAN_PATH)
    if len(rows) != 96:
        raise ValueError(f"expected 96 C4-C4 base-scan rows, found {len(rows)}")
    return rows


def compute_energy_shard(
    energy: float,
    profile: list[dict[str, float]],
    c2: list[dict[str, float]],
    base_rows: list[dict[str, str]],
) -> list[dict]:
    if energy not in NEW_ENERGIES_MEV:
        raise ValueError(f"energy must be one of {NEW_ENERGIES_MEV}; 100 MeV is already the C4-C2 baseline")
    base_map = {
        case_key(float(row["E_MeV"]), float(row["r_km"]), row["species"], row["antinu"]): row
        for row in base_rows
    }
    rows = []
    for index in PROFILE_INDICES:
        state, occupation = profile[index], c2[index]
        if abs(state["r_km"] - occupation["r_km"]) > 1e-12:
            raise ValueError(f"C1/C2 radial mismatch at index {index}")
        for species in SPECIES:
            temperature = state["T_MeV"]
            mstar = state[f"mstar_{species}_MeV"]
            nu = occupation[f"nu_{species}_EOS_MeV"]
            for anti in ANTINU_VALUES:
                key = case_key(energy, state["r_km"], species, anti)
                if key not in base_map:
                    raise KeyError(f"missing C4-C4 base-rate case: {key}")
                base = base_map[key]
                gamma_base = float(base["gamma_available_volume_MeV"])
                gamma_high, root_residual = integrate_total_rate(
                    energy, species, anti, temperature, nu, mstar,
                    n_cos=HIGH_ORDERS["cosine"],
                    order_ep=HIGH_ORDERS["Eprime"],
                    order_p=HIGH_ORDERS["initial_momentum"],
                    order_phi=HIGH_ORDERS["azimuth"],
                    support_scan_points=LOCAL_SUPPORT_SCAN,
                )
                rows.append({
                    "E_MeV": energy,
                    "profile_index": index,
                    "r_km": state["r_km"],
                    "species": species,
                    "antinu": str(anti),
                    "gamma_base_MeV": gamma_base,
                    "gamma_high_MeV": gamma_high,
                    "relative_difference": relative_difference(gamma_high, gamma_base),
                    "base_cosine_order": int(float(base["cosine_quadrature_order"])),
                    "base_Eprime_order": int(float(base["Eprime_quadrature_order"])),
                    "base_initial_momentum_order": int(float(base["initial_momentum_order"])),
                    "base_azimuth_order": int(float(base["azimuth_order"])),
                    "high_cosine_order": HIGH_ORDERS["cosine"],
                    "high_Eprime_order": HIGH_ORDERS["Eprime"],
                    "high_initial_momentum_order": HIGH_ORDERS["initial_momentum"],
                    "high_azimuth_order": HIGH_ORDERS["azimuth"],
                    "support_root_max_relative_residual": root_residual,
                })
    return rows


def evaluate_rows(rows: list[dict], radii: tuple[float, ...] | list[float]) -> dict:
    observed = [
        case_key(float(row["E_MeV"]), float(row["r_km"]), row["species"], row["antinu"])
        for row in rows
    ]
    expected = expected_keys(radii)
    unique = set(observed)
    diffs = [float(row["relative_difference"]) for row in rows]
    roots = [float(row["support_root_max_relative_residual"]) for row in rows]
    positive_finite = all(
        math.isfinite(float(row["gamma_base_MeV"]))
        and math.isfinite(float(row["gamma_high_MeV"]))
        and float(row["gamma_base_MeV"]) > 0.0
        and float(row["gamma_high_MeV"]) > 0.0
        and math.isfinite(float(row["relative_difference"]))
        for row in rows
    )
    counts = {
        energy: sum(abs(float(row["E_MeV"]) - energy) < 1e-10 for row in rows)
        for energy in NEW_ENERGIES_MEV
    }
    per_energy_max = {
        str(energy): max(
            (float(row["relative_difference"]) for row in rows if abs(float(row["E_MeV"]) - energy) < 1e-10),
            default=math.inf,
        )
        for energy in NEW_ENERGIES_MEV
    }
    acceptance = {
        "exact_80_case_grid": len(rows) == 80 and len(unique) == 80 and unique == expected,
        "sixteen_cases_per_energy": all(counts[e] == 16 for e in NEW_ENERGIES_MEV),
        "base_and_high_rates_positive_finite": positive_finite,
        "support_root_residual_below_1e_7": bool(roots) and all(math.isfinite(x) and x < 1e-7 for x in roots),
        "combined_quadrature_difference_below_1_percent": bool(diffs) and max(diffs) < RELATIVE_TOLERANCE,
    }
    return {
        "acceptance": acceptance,
        "numerical_integrity_pass": all(
            acceptance[k] for k in (
                "exact_80_case_grid",
                "sixteen_cases_per_energy",
                "base_and_high_rates_positive_finite",
                "support_root_residual_below_1e_7",
            )
        ),
        "quadrature_convergence_pass": acceptance["combined_quadrature_difference_below_1_percent"],
        "max_relative_difference": max(diffs, default=math.inf),
        "max_support_root_relative_residual": max(roots, default=math.inf),
        "max_relative_difference_by_energy": per_energy_max,
        "case_counts_by_energy": {str(k): v for k, v in counts.items()},
    }


def merge_and_archive(shard_dir: Path, output_dir: Path, profile: list[dict[str, float]], source_commit: str) -> dict:
    shard_dir = Path(shard_dir)
    output_dir = Path(output_dir)
    radii = tuple(float(profile[index]["r_km"]) for index in PROFILE_INDICES)
    rows = []
    for energy in NEW_ENERGIES_MEV:
        path = shard_dir / f"convergence_E{int(energy)}.csv"
        if not path.is_file():
            raise FileNotFoundError(f"missing high-order convergence shard: {path}")
        shard = read_csv(path)
        if len(shard) != 16:
            raise ValueError(f"{path.name}: expected 16 rows, found {len(shard)}")
        rows.extend({
            key: (item[key] if key in ("species", "antinu") else float(item[key]))
            for key in OUTPUT_FIELDS
        } for item in shard)
    rows.sort(key=lambda row: (float(row["E_MeV"]), float(row["r_km"]), row["species"], row["antinu"]))
    checks = evaluate_rows(rows, radii)
    base_sha = git_blob_sha(BASE_SCAN_PATH)
    checks["acceptance"]["base_scan_blob_sha_matches"] = base_sha == EXPECTED_BASE_SCAN_GIT_BLOB
    checks["numerical_integrity_pass"] = checks["numerical_integrity_pass"] and checks["acceptance"]["base_scan_blob_sha_matches"]

    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "quadrature_convergence_80.csv", rows)
    summary = {
        "title": "C4-C4 energy-dependent combined quadrature convergence",
        "date": "2026-11-12",
        "stage": "C4-C4-Aq all five newly computed energies, all four radii and all channels",
        "source_commit": source_commit,
        "physical_validation_status": "not a transport or literature-reproduction acceptance",
        "energy_grid_MeV": list(NEW_ENERGIES_MEV),
        "radii_km": list(radii),
        "species": list(SPECIES),
        "incoming_states": ["nu", "antinu"],
        "case_count": len(rows),
        "base_quadrature": BASE_ORDERS,
        "combined_high_quadrature": HIGH_ORDERS,
        "relative_tolerance": RELATIVE_TOLERANCE,
        "base_scan_git_blob_sha": base_sha,
        "C4B2_kernel_git_blob_sha": "97a2706e978cd22f7ebc08c1f87ce6abd97ad0a7",
        "C4C1_support_git_blob_sha": "8f7291be8738e0273353a8c30039c6be1ed8e6a9",
        "C4C2_integrator_git_blob_sha": "2912788345e482e52308e02e6cbbc87c734a18b0",
        "profile_sha256": sha256_file(PROFILE_PATH),
        "C2_occupation_git_blob_sha": git_blob_sha(C2_PATH),
        **checks,
        "interpretation": [
            "This is a combined high-order comparison: cosine, outgoing-energy, initial-momentum, and azimuthal orders are all increased simultaneously.",
            "A pass establishes stability under this combined order increase; it does not isolate the contribution of each quadrature dimension.",
            "If the 1% threshold is exceeded, the archive is still retained and the responsible quadrature dimensions must be isolated in a follow-up.",
            "The comparison covers all 80 newly computed C4-C4-A cases; the 100-MeV C4-C2 reference is separately covered by the earlier C4-C2 convergence audit.",
            "No radial optical depth, transport solution, redshift, escape probability, hydrodynamic feedback, or supernova exclusion is inferred.",
        ],
    }
    write_json(output_dir / "summary.json", summary)
    readme = f"""# C4-C4-Aq combined quadrature-convergence audit

- Source commit: `{source_commit}`
- Cases: {len(rows)} (five new energies × four radii × two targets × two signs)
- Base orders: cosine 8, outgoing energy 48, initial momentum 36, azimuth 12
- High orders: cosine 12, outgoing energy 72, initial momentum 48, azimuth 16
- Relative-difference threshold: {RELATIVE_TOLERANCE:.1%}
- Numerical-integrity checks: {"PASS" if checks["numerical_integrity_pass"] else "FAIL"}
- Combined quadrature convergence: {"PASS" if checks["quadrature_convergence_pass"] else "NOT PASSED"}

All 80 high-order calculations are compared with the exact matching row in the byte-pinned C4-C4-A base archive. The high-order calculation increases all four quadrature orders simultaneously; it does not isolate individual sources of numerical error. If the 1% threshold is exceeded, the diagnostic rows remain archived and the quadrature dimensions must be separated in the next study.

This is a local-rate numerical convergence check, not physical transport or literature-reproduction acceptance.
"""
    (output_dir / "README.md").write_text(readme, encoding="utf-8")
    manifest = []
    for path in sorted(output_dir.iterdir()):
        if path.is_file() and path.name != "SHA256SUMS.txt":
            manifest.append(f"{sha256_file(path)}  {path.name}")
    (output_dir / "SHA256SUMS.txt").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--energy", type=float)
    parser.add_argument("--output-csv", type=Path)
    parser.add_argument("--merge-dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--check-summary", type=Path)
    parser.add_argument("--source-commit", default=os.environ.get("GITHUB_SHA", "local"))
    args = parser.parse_args()

    if args.check_summary is not None:
        summary = json.loads(args.check_summary.read_text(encoding="utf-8"))
        passed = bool(summary["numerical_integrity_pass"] and summary["quadrature_convergence_pass"])
        print(json.dumps({
            "numerical_integrity_pass": summary["numerical_integrity_pass"],
            "quadrature_convergence_pass": summary["quadrature_convergence_pass"],
            "max_relative_difference": summary["max_relative_difference"],
            "max_relative_difference_by_energy": summary["max_relative_difference_by_energy"],
        }, indent=2))
        if not passed:
            raise SystemExit(1)
        return

    profile = load_profile(PROFILE_PATH)
    c2 = load_c2_reference(C2_PATH)
    base_rows = load_base_scan()
    if args.merge_dir is not None:
        if args.output_dir is None:
            parser.error("--output-dir is required with --merge-dir")
        summary = merge_and_archive(args.merge_dir, args.output_dir, profile, args.source_commit)
        print(json.dumps({
            "numerical_integrity_pass": summary["numerical_integrity_pass"],
            "quadrature_convergence_pass": summary["quadrature_convergence_pass"],
            "max_relative_difference": summary["max_relative_difference"],
            "max_relative_difference_by_energy": summary["max_relative_difference_by_energy"],
            "acceptance": summary["acceptance"],
        }, indent=2))
        return

    if args.energy is None or args.output_csv is None:
        parser.error("--energy and --output-csv are required for a high-order energy shard")
    rows = compute_energy_shard(args.energy, profile, c2, base_rows)
    write_csv(args.output_csv, rows)
    print(json.dumps({
        "energy_MeV": args.energy,
        "rows": len(rows),
        "max_relative_difference": max(row["relative_difference"] for row in rows),
        "max_support_root_relative_residual": max(row["support_root_max_relative_residual"] for row in rows),
        "source_commit": args.source_commit,
    }, indent=2))


if __name__ == "__main__":
    main()
