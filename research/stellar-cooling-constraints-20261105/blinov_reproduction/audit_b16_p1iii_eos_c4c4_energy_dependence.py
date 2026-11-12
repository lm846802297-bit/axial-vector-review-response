#!/usr/bin/env python3
"""C4-C4: incident-energy dependence of EOS moving-nucleon neutral-current scattering."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel import HBARC
from audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support import (
    PROFILE_INDICES,
    SPECIES,
    load_c2_reference,
)
from audit_b16_p1iii_eos_c4c2_full_angle_total_scattering import (
    LOCAL_COS_ORDER,
    LOCAL_EPRIME_ORDER,
    LOCAL_P_ORDER,
    LOCAL_PHI_ORDER,
    LOCAL_SUPPORT_SCAN,
    integrate_total_rate,
)

HERE = Path(__file__).resolve().parent
PROFILE_PATH = HERE / "outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_PATH = HERE / "outputs/p1iii_eos_full_radial_occupation_2026-11-11.csv"
C4C2_REFERENCE_PATH = HERE / "outputs/p1iiie_c4c2_full_angle_total_rates_2026-11-11.csv"
EXPECTED_C4C2_REFERENCE_GIT_BLOB = "881b6459e8d9a1ac867b0f4dc47ac168d454e488"

# First-pass exploratory grid. 100 MeV is imported from the validated C4-C2
# anchor archive; only the other five energies are recomputed in C4-C4-A.
ENERGY_GRID_MEV = (10.0, 20.0, 40.0, 60.0, 100.0, 150.0)
NEW_ENERGIES_MEV = tuple(e for e in ENERGY_GRID_MEV if e != 100.0)
ANTINU_VALUES = (False, True)
MEV_INV_TO_KM = HBARC * 1.0e-18

OUTPUT_DIRNAME = "c4c4_energy_dependence_2026-11-12"
OUTPUT_FIELDS = (
    "E_MeV", "r_km", "species", "antinu", "T_MeV", "mstar_MeV",
    "nu_MeV", "eta_nu_over_T", "theta_T_over_mstar", "X_free",
    "xi_SPP", "nprime_fm3", "gamma_available_volume_MeV",
    "sigma_per_target_MeV_minus2", "kappa_sc_MeV", "lambda_sc_km",
    "cosine_quadrature_order", "Eprime_quadrature_order",
    "initial_momentum_order", "azimuth_order",
    "support_root_max_relative_residual", "source",
)


def git_blob_sha(path: Path) -> str:
    data = Path(path).read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with Path(path).open("r", newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


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
    Path(path).write_text(
        json.dumps(payload, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def opacity_and_mean_free_path(gamma_available: float, xi_spp: float) -> tuple[float, float]:
    """Return kappa=xi*Gamma [MeV] and lambda [km]; xi is applied once."""
    if not math.isfinite(gamma_available) or gamma_available <= 0.0:
        raise ValueError("available-volume rate must be finite and positive")
    if not math.isfinite(xi_spp) or not 0.0 < xi_spp <= 1.0:
        raise ValueError("xi_SPP must lie in (0, 1]")
    kappa = xi_spp * gamma_available
    return kappa, MEV_INV_TO_KM / kappa


def expected_case_keys(radii: tuple[float, ...] | list[float]) -> set[tuple]:
    return {
        (float(energy), round(float(radius), 8), species, str(anti))
        for energy in ENERGY_GRID_MEV
        for radius in radii
        for species in SPECIES
        for anti in ANTINU_VALUES
    }


def _row_key(row: dict) -> tuple:
    return (
        float(row["E_MeV"]),
        round(float(row["r_km"]), 8),
        str(row["species"]),
        str(row["antinu"]),
    )


def validate_records(rows: list[dict], radii: tuple[float, ...] | list[float]) -> dict:
    expected = expected_case_keys(radii)
    observed = [_row_key(row) for row in rows]
    observed_set = set(observed)
    expected_counts = {energy: len(radii) * len(SPECIES) * len(ANTINU_VALUES) for energy in ENERGY_GRID_MEV}
    actual_counts = {
        energy: sum(abs(float(row["E_MeV"]) - energy) < 1e-10 for row in rows)
        for energy in ENERGY_GRID_MEV
    }
    positive_finite = True
    closure_ok = True
    root_ok = True
    source_ok = True
    for row in rows:
        numeric = (
            float(row["gamma_available_volume_MeV"]),
            float(row["sigma_per_target_MeV_minus2"]),
            float(row["kappa_sc_MeV"]),
            float(row["lambda_sc_km"]),
            float(row["support_root_max_relative_residual"]),
        )
        positive_finite &= all(math.isfinite(x) and x > 0.0 for x in numeric[:4])
        xi = float(row["xi_SPP"])
        gamma = float(row["gamma_available_volume_MeV"])
        kappa = float(row["kappa_sc_MeV"])
        closure_ok &= abs(kappa / (xi * gamma) - 1.0) < 5e-13
        root_ok &= math.isfinite(numeric[4]) and numeric[4] < 1e-7
        energy = float(row["E_MeV"])
        expected_source = "C4-C2 archived baseline" if abs(energy - 100.0) < 1e-10 else "C4-C4 direct recomputation"
        source_ok &= row["source"] == expected_source

    baseline_rows = [row for row in rows if abs(float(row["E_MeV"]) - 100.0) < 1e-10]
    acceptance = {
        "exact_96_case_grid": len(rows) == len(expected) == 96 and observed_set == expected and len(observed) == len(observed_set),
        "sixteen_cases_per_energy": actual_counts == expected_counts,
        "all_rates_and_derived_quantities_positive_finite": bool(positive_finite),
        "xi_spp_applied_exactly_once": bool(closure_ok),
        "support_root_residual_below_1e-7": bool(root_ok),
        "100_mev_baseline_reused_not_recomputed": len(baseline_rows) == 16 and all(row["source"] == "C4-C2 archived baseline" for row in baseline_rows),
        "source_labels_match_energy_provenance": bool(source_ok),
    }
    return {
        "acceptance": acceptance,
        "numerical_integrity_pass": all(acceptance.values()),
        "case_counts_by_energy": {str(k): v for k, v in actual_counts.items()},
        "max_support_root_relative_residual": max(
            (float(row["support_root_max_relative_residual"]) for row in rows),
            default=math.inf,
        ),
    }


def compute_energy_rows(
    energy: float,
    profile: list[dict[str, float]],
    c2: list[dict[str, float]],
) -> list[dict]:
    if energy not in NEW_ENERGIES_MEV:
        raise ValueError(f"energy must be one of {NEW_ENERGIES_MEV}; 100 MeV is reused from C4-C2")
    rows = []
    for index in PROFILE_INDICES:
        state, occupation = profile[index], c2[index]
        if abs(state["r_km"] - occupation["r_km"]) > 1e-12:
            raise ValueError(f"C1/C2 radial mismatch at index {index}")
        for target in SPECIES:
            temperature = state["T_MeV"]
            mstar = state[f"mstar_{target}_MeV"]
            nu = occupation[f"nu_{target}_EOS_MeV"]
            nprime = occupation[f"nprime_{target}_fm3"]
            xi = state["xi_SPP"]
            gamma_per_target_volume = None
            for anti in ANTINU_VALUES:
                gamma, root_residual = integrate_total_rate(
                    energy, target, anti, temperature, nu, mstar,
                    n_cos=LOCAL_COS_ORDER,
                    order_ep=LOCAL_EPRIME_ORDER,
                    order_p=LOCAL_P_ORDER,
                    order_phi=LOCAL_PHI_ORDER,
                    support_scan_points=LOCAL_SUPPORT_SCAN,
                )
                kappa, mean_free_path_km = opacity_and_mean_free_path(gamma, xi)
                sigma = gamma / (nprime * HBARC**3)
                if gamma_per_target_volume is None:
                    gamma_per_target_volume = gamma
                rows.append({
                    "E_MeV": energy,
                    "r_km": state["r_km"],
                    "species": target,
                    "antinu": str(anti),
                    "T_MeV": temperature,
                    "mstar_MeV": mstar,
                    "nu_MeV": nu,
                    "eta_nu_over_T": nu / temperature,
                    "theta_T_over_mstar": temperature / mstar,
                    "X_free": state[f"X_{target}"],
                    "xi_SPP": xi,
                    "nprime_fm3": nprime,
                    "gamma_available_volume_MeV": gamma,
                    "sigma_per_target_MeV_minus2": sigma,
                    "kappa_sc_MeV": kappa,
                    "lambda_sc_km": mean_free_path_km,
                    "cosine_quadrature_order": LOCAL_COS_ORDER,
                    "Eprime_quadrature_order": LOCAL_EPRIME_ORDER,
                    "initial_momentum_order": LOCAL_P_ORDER,
                    "azimuth_order": LOCAL_PHI_ORDER,
                    "support_root_max_relative_residual": root_residual,
                    "source": "C4-C4 direct recomputation",
                })
    return rows


def load_c4c2_baseline() -> list[dict]:
    actual = git_blob_sha(C4C2_REFERENCE_PATH)
    if actual != EXPECTED_C4C2_REFERENCE_GIT_BLOB:
        raise ValueError(
            f"C4-C2 baseline Git blob SHA mismatch: expected {EXPECTED_C4C2_REFERENCE_GIT_BLOB}, got {actual}"
        )
    raw = read_csv(C4C2_REFERENCE_PATH)
    if len(raw) != 16:
        raise ValueError(f"expected 16 C4-C2 baseline rows, found {len(raw)}")
    rows = []
    for item in raw:
        if abs(float(item["E_MeV"]) - 100.0) > 1e-12:
            raise ValueError("C4-C2 baseline contains a non-100-MeV row")
        gamma = float(item["gamma_total_available_volume_MeV"])
        xi = float(item["xi_SPP"])
        kappa, mean_free_path_km = opacity_and_mean_free_path(gamma, xi)
        rows.append({
            "E_MeV": 100.0,
            "r_km": float(item["r_km"]),
            "species": item["species"],
            "antinu": str(item["antinu"]),
            "T_MeV": float(item["T_MeV"]),
            "mstar_MeV": float(item["mstar_MeV"]),
            "nu_MeV": float(item["nu_MeV"]),
            "eta_nu_over_T": float(item["eta_nu_over_T"]),
            "theta_T_over_mstar": float(item["theta_T_over_mstar"]),
            "X_free": float(item["X_free"]),
            "xi_SPP": xi,
            "nprime_fm3": float(item["nprime_fm3"]),
            "gamma_available_volume_MeV": gamma,
            "sigma_per_target_MeV_minus2": float(item["sigma_total_per_target_MeV_minus2"]),
            "kappa_sc_MeV": kappa,
            "lambda_sc_km": mean_free_path_km,
            "cosine_quadrature_order": int(float(item["cosine_quadrature_order"])),
            "Eprime_quadrature_order": int(float(item["Eprime_quadrature_order"])),
            "initial_momentum_order": int(float(item["initial_momentum_order"])),
            "azimuth_order": int(float(item["azimuth_order"])),
            "support_root_max_relative_residual": float(item["support_root_max_relative_residual"]),
            "source": "C4-C2 archived baseline",
        })
    return rows


def build_energy_ratios(rows: list[dict]) -> list[dict]:
    baseline_gamma = {}
    baseline_sigma = {}
    for row in rows:
        if abs(float(row["E_MeV"]) - 100.0) < 1e-10:
            key = (round(float(row["r_km"]), 8), row["species"], row["antinu"])
            baseline_gamma[key] = float(row["gamma_available_volume_MeV"])
            baseline_sigma[key] = float(row["sigma_per_target_MeV_minus2"])
    if len(baseline_gamma) != 16 or len(baseline_sigma) != 16:
        raise ValueError("energy ratios require all 16 C4-C2 100-MeV baseline rows")
    result = []
    for row in rows:
        key = (round(float(row["r_km"]), 8), row["species"], row["antinu"])
        result.append({
            "E_MeV": float(row["E_MeV"]),
            "r_km": float(row["r_km"]),
            "species": row["species"],
            "antinu": row["antinu"],
            "gamma_over_gamma_100MeV": float(row["gamma_available_volume_MeV"]) / baseline_gamma[key],
            "sigma_over_sigma_100MeV": float(row["sigma_per_target_MeV_minus2"]) / baseline_sigma[key],
            "kappa_sc_MeV": float(row["kappa_sc_MeV"]),
            "lambda_sc_km": float(row["lambda_sc_km"]),
        })
    return sorted(result, key=lambda x: (x["E_MeV"], x["r_km"], x["species"], x["antinu"]))


def build_channel_ratios(rows: list[dict]) -> list[dict]:
    lookup = {
        (float(row["E_MeV"]), round(float(row["r_km"]), 8), row["species"], row["antinu"]): float(row["kappa_sc_MeV"])
        for row in rows
    }
    result = []
    for energy in ENERGY_GRID_MEV:
        for radius in sorted({round(float(row["r_km"]), 8) for row in rows}):
            values = {}
            for anti in ("False", "True"):
                for species in SPECIES:
                    values[(species, anti)] = lookup[(energy, radius, species, anti)]
            knu = values[("n", "False")] + values[("p", "False")]
            kantinu = values[("n", "True")] + values[("p", "True")]
            result.append({
                "E_MeV": energy,
                "r_km": radius,
                "kappa_n_over_kappa_p_nu": values[("n", "False")] / values[("p", "False")],
                "kappa_n_over_kappa_p_antinu": values[("n", "True")] / values[("p", "True")],
                "kappa_total_nu_MeV": knu,
                "kappa_total_antinu_MeV": kantinu,
                "kappa_total_nu_over_antinu": knu / kantinu,
            })
    return result


def merge_and_archive(
    shard_dir: Path,
    output_dir: Path,
    profile: list[dict[str, float]],
    source_commit: str,
) -> dict:
    shard_dir = Path(shard_dir)
    output_dir = Path(output_dir)
    radii = tuple(float(profile[index]["r_km"]) for index in PROFILE_INDICES)
    rows = []
    for energy in NEW_ENERGIES_MEV:
        path = shard_dir / f"rates_E{int(energy)}.csv"
        if not path.is_file():
            raise FileNotFoundError(f"missing C4-C4 energy shard: {path}")
        shard = read_csv(path)
        if len(shard) != 16:
            raise ValueError(f"{path.name}: expected 16 rows, found {len(shard)}")
        for item in shard:
            rows.append({
                key: (item[key] if key in ("species", "antinu", "source") else float(item[key]))
                for key in OUTPUT_FIELDS
            })
    rows.extend(load_c4c2_baseline())
    rows.sort(key=lambda row: (float(row["E_MeV"]), float(row["r_km"]), row["species"], row["antinu"]))

    checks = validate_records(rows, radii)
    baseline_sha = git_blob_sha(C4C2_REFERENCE_PATH)
    checks["acceptance"]["C4C2_reference_blob_sha_matches"] = baseline_sha == EXPECTED_C4C2_REFERENCE_GIT_BLOB
    checks["numerical_integrity_pass"] = all(checks["acceptance"].values())
    if not checks["numerical_integrity_pass"]:
        raise AssertionError(f"C4-C4 numerical-integrity checks failed: {checks['acceptance']}")

    ratios = build_energy_ratios(rows)
    channel_ratios = build_channel_ratios(rows)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "local_rates_96.csv", rows)
    write_csv(output_dir / "energy_scaling_ratios.csv", ratios)
    write_csv(output_dir / "channel_ratios.csv", channel_ratios)

    profile_sha256 = sha256_file(PROFILE_PATH)
    c2_blob = git_blob_sha(C2_PATH)
    summary = {
        "title": "C4-C4 incident-energy dependence of EOS moving-nucleon neutral-current scattering",
        "date": "2026-11-12",
        "stage": "C4-C4-A four-radius local anchor scan",
        "numerical_integrity_pass": True,
        "physical_validation_status": "not a transport or literature-reproduction acceptance",
        "exploratory_energy_grid_MeV": list(ENERGY_GRID_MEV),
        "energy_grid_note": "The six-point grid is an exploratory first-pass choice, not a final physical boundary or a user-approved exclusion range.",
        "radii_km": list(radii),
        "species": list(SPECIES),
        "incoming_states": ["nu", "antinu"],
        "case_count": len(rows),
        "newly_recomputed_case_count": len(rows) - 16,
        "reused_100MeV_baseline_case_count": 16,
        "source_commit": source_commit,
        "inputs": {
            "profile_path": str(PROFILE_PATH.relative_to(HERE)),
            "profile_sha256": profile_sha256,
            "C2_occupation_path": str(C2_PATH.relative_to(HERE)),
            "C2_occupation_git_blob_sha": c2_blob,
            "C4C2_100MeV_reference_path": str(C4C2_REFERENCE_PATH.relative_to(HERE)),
            "C4C2_100MeV_reference_git_blob_sha": baseline_sha,
            "C4B2_kernel_git_blob_sha": "97a2706e978cd22f7ebc08c1f87ce6abd97ad0a7",
            "C4C1_support_git_blob_sha": "8f7291be8738e0273353a8c30039c6be1ed8e6a9",
            "C4C2_integrator_git_blob_sha": "2912788345e482e52308e02e6cbbc87c734a18b0",
        },
        "kernel": {
            "definition": "Gamma_N^avail(E,r)=2*pi*integral[-1,1] dcos(theta) integral[Eprime_min,Eprime_max] dEprime dGamma_N/(dEprime dOmegaprime)",
            "support": "Exact p_min(Eprime,cos(theta);mstar)<=p_max with the existing 45*T momentum-tail cutoff; roots are recomputed for each energy, radius, target and angular node.",
            "quadrature": {
                "cosine": LOCAL_COS_ORDER,
                "outgoing_energy": LOCAL_EPRIME_ORDER,
                "initial_momentum": LOCAL_P_ORDER,
                "azimuth": LOCAL_PHI_ORDER,
                "support_scan_points": LOCAL_SUPPORT_SCAN,
            },
            "opacity": "kappa_N=xi_SPP*Gamma_N^avail; xi_SPP is applied exactly once.",
            "mean_free_path": "lambda_N=1/kappa_N, converted from MeV^-1 to km using hbar*c=197.3269804 MeV fm.",
            "local_energy_convention": "Fixed local incident energy at each sampled radius; no gravitational redshift or energy redistribution.",
        },
        "acceptance": checks["acceptance"],
        "max_support_root_relative_residual": checks["max_support_root_relative_residual"],
        "interpretation": [
            "The output is a four-radius local total-scattering energy scan, not a 301-radius opacity or optical-depth calculation.",
            "The 100-MeV entries are reused byte-provenanced C4-C2 reference values and are not recomputed.",
            "The C4-C3 100-MeV 301-radius flat-space diagnostic remains the baseline and is not replaced.",
            "No transport, escape probability, redshift, hydrodynamic feedback, or supernova exclusion is inferred.",
            "The scan is not a physical validation of the pure-vector Blinov Fig. 7 benchmark.",
        ],
    }
    write_json(output_dir / "summary.json", summary)
    readme = f"""# C4-C4-A energy-dependence anchor scan

- Trigger/source commit: `{source_commit}`
- Numerical-integrity status: PASS
- Physical transport/reproduction status: NOT CLAIMED
- Energies: {", ".join(str(int(x)) for x in ENERGY_GRID_MEV)} MeV
- Anchor radii: {", ".join(str(x) for x in radii)} km
- Channels: neutron/proton × neutrino/antineutrino
- Cases: 96 total; 80 newly computed and 16 reused at 100 MeV from C4-C2.

The local rate is
`Gamma_N^avail = 2 pi integral dcos(theta) integral dEprime dGamma/(dEprime dOmega')`,
with the exact outgoing-energy support recalculated for every incident energy and angle. The same EOS effective masses, chemical potentials, Fermi occupations, final-state Pauli blocking, and weak form factors as C4-B2/C1/C2 are retained.

The total-volume scattering coefficient is `kappa_N = xi_SPP Gamma_N^avail`; `xi_SPP` is applied once. The mean free path is `lambda_N = 1/kappa_N`.

The six-point energy grid is an exploratory first-pass choice, not a final physical boundary or a user-approved exclusion range. This stage uses fixed local incident energy and flat-space local rates. It does not calculate a radial optical depth, transport solution, escape probability, or SN1987A constraint.

## Provenance

- C1 profile SHA-256: `{profile_sha256}`
- C2 occupation Git blob SHA: `{c2_blob}`
- C4-C2 100-MeV reference Git blob SHA: `{baseline_sha}`
- C4-B2/C1/C2 source blob SHAs are recorded in `summary.json`.

See `summary.json` for exact quadrature orders, all acceptance checks, and input provenance.
"""
    (output_dir / "README.md").write_text(readme, encoding="utf-8")
    manifest_lines = []
    for path in sorted(output_dir.iterdir()):
        if path.is_file() and path.name != "SHA256SUMS.txt":
            manifest_lines.append(f"{sha256_file(path)}  {path.name}")
    (output_dir / "SHA256SUMS.txt").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--energy", type=float)
    parser.add_argument("--output-csv", type=Path)
    parser.add_argument("--merge-dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--source-commit", default=os.environ.get("GITHUB_SHA", "local"))
    args = parser.parse_args()

    profile = load_profile(PROFILE_PATH)
    c2 = load_c2_reference(C2_PATH)
    if args.merge_dir is not None:
        if args.output_dir is None:
            parser.error("--output-dir is required with --merge-dir")
        summary = merge_and_archive(args.merge_dir, args.output_dir, profile, args.source_commit)
        print(json.dumps({
            "numerical_integrity_pass": summary["numerical_integrity_pass"],
            "case_count": summary["case_count"],
            "max_support_root_relative_residual": summary["max_support_root_relative_residual"],
            "acceptance": summary["acceptance"],
        }, indent=2))
        return

    if args.energy is None or args.output_csv is None:
        parser.error("--energy and --output-csv are required for an energy shard")
    rows = compute_energy_rows(args.energy, profile, c2)
    write_csv(args.output_csv, rows)
    print(json.dumps({
        "energy_MeV": args.energy,
        "rows": len(rows),
        "radii_km": [profile[i]["r_km"] for i in PROFILE_INDICES],
        "max_support_root_relative_residual": max(row["support_root_max_relative_residual"] for row in rows),
        "source_commit": args.source_commit,
    }, indent=2))


if __name__ == "__main__":
    main()
