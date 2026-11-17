#!/usr/bin/env python3
"""C4-C4-B: full-radial incident-energy dependence of EOS moving-nucleon scattering."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np
from numba import njit

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel import HBARC
import audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel as b2
import audit_b16_p1iii_eos_c4c2_full_angle_total_scattering as c4
import audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support as c1
from audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support import load_c2_reference, SPECIES

HERE = Path(__file__).resolve().parent
PROFILE_PATH = HERE / "outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2_PATH = HERE / "outputs/p1iii_eos_full_radial_occupation_2026-11-11.csv"
C4C3_BASELINE_PATH = HERE / "c4c3_direct_local_recomputation_2026-11-11/local_independent_radial_rates_301x4.csv"
# Historical byte-pinned anchor used by these archived comparisons.
C4C4A_PATH = HERE / "audit_provenance/c4c4_anchor_original_8be3757.csv"

EXPECTED_PROFILE_GIT_BLOB = "9ff7818b0679992c0a9ba402330ec7f0d1f3041b"
EXPECTED_C2_GIT_BLOB = "c472040a4551e68ffadbf7addf9402663f99e7e3"
EXPECTED_C4C3_BASELINE_GIT_BLOB = "2b060ffa863430c6e35a1355d0316c1d1c0b4c7c"
EXPECTED_C4C4A_GIT_BLOB = "8be3757cf28011132a82b5c2373aa3c1fa59d342"
EXPECTED_C4B2_GIT_BLOB = "97a2706e978cd22f7ebc08c1f87ce6abd97ad0a7"
EXPECTED_C4C1_GIT_BLOB = "8f7291be8738e0273353a8c30039c6be1ed8e6a9"
EXPECTED_C4C2_GIT_BLOB = "2912788345e482e52308e02e6cbbc87c734a18b0"

ENERGY_GRID_MEV = (10.0, 20.0, 40.0, 60.0, 100.0, 150.0)
NEW_ENERGIES_MEV = (10.0, 20.0, 40.0, 60.0, 150.0)
ANTINU_VALUES = (False, True)
RADIAL_POINTS = 301
RADIAL_SHARDS = 5
QUAD_SAMPLE_INDICES = (0, 30, 60, 90, 96, 120, 140, 142, 143, 160, 180, 196, 220, 240, 260, 280, 300)
BASE_ORDERS = {"cosine": 8, "Eprime": 48, "initial_momentum": 36, "azimuth": 12}
HIGH_ORDERS = {"cosine": 12, "Eprime": 72, "initial_momentum": 48, "azimuth": 16}
QUAD_RELATIVE_TOLERANCE = 1.0e-2
RADIAL_RELATIVE_TOLERANCE = 1.0e-2
SUPPORT_SCAN_POINTS = 10001
MEV_INV_TO_KM = HBARC * 1.0e-18
KM_TO_MEV_INV = 1.0e18 / HBARC

OUTPUT_FIELDS = (
    "E_MeV", "profile_index", "r_km", "species", "antinu",
    "T_MeV", "mstar_MeV", "nu_MeV", "X_free", "xi_SPP", "nB_fm3",
    "nprime_available_fm3", "n_free_total_volume_fm3",
    "n_free_EOS_target_fm3", "density_closure_relative_residual",
    "gamma_available_volume_MeV", "sigma_per_target_MeV_minus2",
    "kappa_sc_MeV", "lambda_sc_km", "n_cos", "n_Eprime", "n_p", "n_phi",
    "support_root_max_relative_residual", "source",
)
QUAD_FIELDS = (
    "E_MeV", "profile_index", "r_km", "species", "antinu",
    "gamma_base_MeV", "gamma_high_MeV", "relative_difference",
    "base_cosine_order", "base_Eprime_order", "base_initial_momentum_order", "base_azimuth_order",
    "high_cosine_order", "high_Eprime_order", "high_initial_momentum_order", "high_azimuth_order",
    "support_root_max_relative_residual",
)


def git_blob_sha(path: Path) -> str:
    data = Path(path).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def require_blob_sha(path: Path, expected: str, label: str) -> str:
    actual = git_blob_sha(path)
    if actual != expected:
        raise ValueError(f"{label} Git blob SHA mismatch: expected {expected}, got {actual}")
    return actual


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
    Path(path).write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def shard_indices(shard_index: int, shard_count: int, npoints: int = RADIAL_POINTS) -> range:
    if shard_count < 1 or not 0 <= shard_index < shard_count:
        raise ValueError("invalid radial shard index/count")
    return range(npoints * shard_index // shard_count, npoints * (shard_index + 1) // shard_count)


def relative_difference(high: float, base: float) -> float:
    if not (math.isfinite(high) and math.isfinite(base) and high > 0.0 and base > 0.0):
        raise ValueError("base and high-order rates must be finite and positive")
    return abs(high / base - 1.0)


def case_key(energy: float, index: int, species: str, antinu: str | bool) -> tuple:
    return (round(float(energy), 8), int(index), species, str(antinu))


def expected_rate_keys() -> set[tuple]:
    return {
        case_key(energy, index, species, anti)
        for energy in ENERGY_GRID_MEV
        for index in range(RADIAL_POINTS)
        for species in SPECIES
        for anti in ANTINU_VALUES
    }


def expected_quad_keys() -> set[tuple]:
    return {
        case_key(energy, index, species, anti)
        for energy in NEW_ENERGIES_MEV
        for index in QUAD_SAMPLE_INDICES
        for species in SPECIES
        for anti in ANTINU_VALUES
    }


def tau_from_kappa(r_km: np.ndarray, kappa_mev: np.ndarray) -> np.ndarray:
    r = np.asarray(r_km, dtype=float)
    k = np.asarray(kappa_mev, dtype=float)
    if r.ndim != 1 or k.ndim != 1 or len(r) != len(k) or len(r) < 2:
        raise ValueError("r and kappa must be equal-length one-dimensional arrays")
    if not np.all(np.isfinite(r)) or not np.all(np.isfinite(k)):
        raise ValueError("non-finite radial coordinate or opacity")
    if np.any(np.diff(r) <= 0.0) or np.any(k < 0.0):
        raise ValueError("r must increase and kappa must be non-negative")
    tau = np.zeros_like(r)
    for i in range(len(r) - 2, -1, -1):
        dr = (r[i + 1] - r[i]) * KM_TO_MEV_INV
        tau[i] = tau[i + 1] + 0.5 * (k[i] + k[i + 1]) * dr
    return tau


# Code copied from the C4-C3 local recomputation accelerator; this is a code-origin
# reference, not a runtime dependency. Only the innermost Dirac contraction is JIT-compiled.
GAMMA = np.asarray(b2.kernel.GAMMA)
METRIC = np.asarray(b2.kernel.METRIC)
IDENT = np.asarray(b2.kernel.IDENT)


@njit
def mm4(a, b):
    out = np.zeros((4, 4), np.complex128)
    for i in range(4):
        for j in range(4):
            z = 0.0j
            for k in range(4):
                z += a[i, k] * b[k, j]
            out[i, j] = z
    return out


@njit
def contract_numba(mstar, q0, qmag, qhat, e1, e2, qvec, vertex, barred, tensor, p, phi, gamma, metric, ident):
    ei = np.sqrt(p * p + mstar * mstar)
    cosine = (2.0 * ei * q0 + q0 * q0 - qmag * qmag) / (2.0 * p * qmag) if p > 1e-14 else 0.0
    if abs(cosine) > 1.0 + 2e-10:
        return 0.0
    cosine = max(-1.0, min(1.0, cosine))
    sine = np.sqrt(max(0.0, 1.0 - cosine * cosine))
    cp = np.cos(phi)
    sp = np.sin(phi)
    pv = np.zeros(3)
    pp = np.zeros(3)
    for i in range(3):
        pv[i] = p * (cosine * qhat[i] + sine * (cp * e1[i] + sp * e2[i]))
        pp[i] = pv[i] + qvec[i]
    ef = ei + q0
    pp2 = pp[0] * pp[0] + pp[1] * pp[1] + pp[2] * pp[2]
    if abs(np.sqrt(pp2 + mstar * mstar) - ef) > 2e-9 * max(1.0, ef):
        raise ArithmeticError("shell")
    pi = np.array([ei, pv[0], pv[1], pv[2]])
    pf = np.array([ef, pp[0], pp[1], pp[2]])
    si = np.zeros((4, 4), np.complex128)
    sf = np.zeros((4, 4), np.complex128)
    for mu in range(4):
        for a in range(4):
            for bb in range(4):
                si[a, bb] += metric[mu] * pi[mu] * gamma[mu, a, bb]
                sf[a, bb] += metric[mu] * pf[mu] * gamma[mu, a, bb]
    for a in range(4):
        for bb in range(4):
            si[a, bb] += mstar * ident[a, bb]
            sf[a, bb] += mstar * ident[a, bb]
    left = np.zeros((4, 4, 4), np.complex128)
    for mu in range(4):
        left[mu] = mm4(vertex[mu], si)
    acc = np.zeros((4, 4), np.complex128)
    for mu in range(4):
        for al in range(4):
            tmp = mm4(left[mu], barred[al])
            for a in range(4):
                for bb in range(4):
                    acc[a, bb] += tensor[mu, al] * tmp[a, bb]
    tr = 0.0j
    for a in range(4):
        for bb in range(4):
            tr += sf[a, bb] * acc[bb, a]
    return 0.5 * tr.real


def fast_contract(pre, p, phi):
    return contract_numba(
        pre["mstar"], pre["q0"], pre["qmag"], pre["qhat"],
        pre["e1"], pre["e2"], pre["qvec"], np.asarray(pre["vertex"]),
        np.asarray(pre["barred"]), np.asarray(pre["L"]), p, phi,
        GAMMA, METRIC, IDENT,
    )


def install_accelerator() -> None:
    b2.contract_moving_eos = fast_contract


def validate_kernel_source_pins() -> dict[str, str]:
    """Verify the exact imported kernel/support source blobs used by this run."""
    return {
        "C4-B2 effective-mass kernel": require_blob_sha(
            Path(b2.__file__), EXPECTED_C4B2_GIT_BLOB, "C4-B2 effective-mass kernel"
        ),
        "C4-C1 outgoing-energy support": require_blob_sha(
            Path(c1.__file__), EXPECTED_C4C1_GIT_BLOB, "C4-C1 outgoing-energy support"
        ),
        "C4-C2 full-angle integrator": require_blob_sha(
            Path(c4.__file__), EXPECTED_C4C2_GIT_BLOB, "C4-C2 full-angle integrator"
        ),
    }


def load_inputs() -> tuple[list[dict[str, float]], list[dict[str, float]]]:
    validate_kernel_source_pins()
    require_blob_sha(PROFILE_PATH, EXPECTED_PROFILE_GIT_BLOB, "C1 profile")
    require_blob_sha(C2_PATH, EXPECTED_C2_GIT_BLOB, "C2 occupation")
    profile = load_profile(PROFILE_PATH)
    c2 = load_c2_reference(C2_PATH)
    if len(profile) != RADIAL_POINTS or len(c2) != RADIAL_POINTS:
        raise ValueError("profile and C2 occupation must each contain 301 rows")
    for i, (state, occupation) in enumerate(zip(profile, c2)):
        if abs(state["r_km"] - occupation["r_km"]) > 1e-12:
            raise ValueError(f"C1/C2 radial mismatch at index {i}")
    return profile, c2


def compute_shard(energy, indices, profile, c2):
    if energy not in NEW_ENERGIES_MEV:
        raise ValueError(f"new calculation energy must be one of {NEW_ENERGIES_MEV}")
    install_accelerator()
    rate_rows, quad_rows = [], []
    sample_set = set(QUAD_SAMPLE_INDICES)
    for index in indices:
        state, occupation = profile[index], c2[index]
        xi, nB, temperature = state["xi_SPP"], state["nB_fm3"], state["T_MeV"]
        for species in SPECIES:
            X = state[f"X_{species}"]
            nprime = occupation[f"nprime_{species}_fm3"]
            nu = occupation[f"nu_{species}_EOS_MeV"]
            mstar = state[f"mstar_{species}_MeV"]
            if min(xi, nprime, X * nB) <= 0.0:
                raise ArithmeticError(f"non-positive density input at index={index}, species={species}")
            for anti in ANTINU_VALUES:
                gamma, root = c4.integrate_total_rate(
                    energy, species, anti, temperature, nu, mstar,
                    n_cos=BASE_ORDERS["cosine"], order_ep=BASE_ORDERS["Eprime"],
                    order_p=BASE_ORDERS["initial_momentum"], order_phi=BASE_ORDERS["azimuth"],
                    support_scan_points=SUPPORT_SCAN_POINTS,
                )
                if not math.isfinite(gamma) or gamma <= 0.0 or not math.isfinite(root) or root >= 1e-7:
                    raise ArithmeticError(f"invalid base rate at E={energy}, i={index}, {species}, anti={anti}")
                kappa = xi * gamma
                row = {
                    "E_MeV": energy, "profile_index": index, "r_km": state["r_km"],
                    "species": species, "antinu": str(anti), "T_MeV": temperature,
                    "mstar_MeV": mstar, "nu_MeV": nu, "X_free": X, "xi_SPP": xi,
                    "nB_fm3": nB, "nprime_available_fm3": nprime,
                    "n_free_total_volume_fm3": xi * nprime,
                    "n_free_EOS_target_fm3": X * nB,
                    "density_closure_relative_residual": xi * nprime / (X * nB) - 1.0,
                    "gamma_available_volume_MeV": gamma,
                    "sigma_per_target_MeV_minus2": gamma / (nprime * HBARC**3),
                    "kappa_sc_MeV": kappa, "lambda_sc_km": MEV_INV_TO_KM / kappa,
                    "n_cos": BASE_ORDERS["cosine"], "n_Eprime": BASE_ORDERS["Eprime"],
                    "n_p": BASE_ORDERS["initial_momentum"], "n_phi": BASE_ORDERS["azimuth"],
                    "support_root_max_relative_residual": root,
                    "source": "C4-C4-B direct recomputation",
                }
                rate_rows.append(row)
                if index in sample_set:
                    gamma_high, root_high = c4.integrate_total_rate(
                        energy, species, anti, temperature, nu, mstar,
                        n_cos=HIGH_ORDERS["cosine"], order_ep=HIGH_ORDERS["Eprime"],
                        order_p=HIGH_ORDERS["initial_momentum"], order_phi=HIGH_ORDERS["azimuth"],
                        support_scan_points=SUPPORT_SCAN_POINTS,
                    )
                    quad_rows.append({
                        "E_MeV": energy, "profile_index": index, "r_km": state["r_km"],
                        "species": species, "antinu": str(anti),
                        "gamma_base_MeV": gamma, "gamma_high_MeV": gamma_high,
                        "relative_difference": relative_difference(gamma_high, gamma),
                        "base_cosine_order": BASE_ORDERS["cosine"],
                        "base_Eprime_order": BASE_ORDERS["Eprime"],
                        "base_initial_momentum_order": BASE_ORDERS["initial_momentum"],
                        "base_azimuth_order": BASE_ORDERS["azimuth"],
                        "high_cosine_order": HIGH_ORDERS["cosine"],
                        "high_Eprime_order": HIGH_ORDERS["Eprime"],
                        "high_initial_momentum_order": HIGH_ORDERS["initial_momentum"],
                        "high_azimuth_order": HIGH_ORDERS["azimuth"],
                        "support_root_max_relative_residual": max(root, root_high),
                    })
    return rate_rows, quad_rows


def load_c4c3_baseline(profile, c2):
    require_blob_sha(C4C3_BASELINE_PATH, EXPECTED_C4C3_BASELINE_GIT_BLOB, "C4-C3 100-MeV baseline")
    raw = read_csv(C4C3_BASELINE_PATH)
    if len(raw) != RADIAL_POINTS * 4:
        raise ValueError(f"expected 1204 C4-C3 baseline rows, found {len(raw)}")
    rows = []
    seen = set()
    for item in raw:
        index, species, anti = int(item["profile_index"]), item["species"], item["antinu"]
        if not 0 <= index < RADIAL_POINTS or species not in SPECIES or anti not in ("False", "True"):
            raise ValueError(f"invalid C4-C3 baseline key: {item}")
        key = (index, species, anti)
        if key in seen:
            raise ValueError(f"duplicate C4-C3 baseline key: {key}")
        seen.add(key)
        state, occupation = profile[index], c2[index]
        if abs(float(item["r_km"]) - state["r_km"]) > 1e-12:
            raise ValueError(f"C4-C3 baseline radius mismatch at index {index}")
        if abs(float(item["E_MeV"]) - 100.0) > 1e-12:
            raise ValueError("C4-C3 baseline contains a non-100-MeV row")
        checks = (
            (float(item["T_MeV"]), state["T_MeV"], 1e-10, "temperature"),
            (float(item["mstar_MeV"]), state[f"mstar_{species}_MeV"], 1e-9, "effective mass"),
            (float(item["nu_MeV"]), occupation[f"nu_{species}_EOS_MeV"], 1e-9, "chemical potential"),
            (float(item["nprime_available_fm3"]), occupation[f"nprime_{species}_fm3"], 1e-12, "available density"),
            (float(item["xi_SPP"]), state["xi_SPP"], 1e-12, "filling factor"),
            (float(item["nB_fm3"]), state["nB_fm3"], 1e-12, "baryon density"),
            (float(item["X_free"]), state[f"X_{species}"], 1e-12, "free fraction"),
        )
        for actual, expected, tol, label in checks:
            if abs(actual - expected) > tol * max(1.0, abs(expected)):
                raise ValueError(f"C4-C3 {label} mismatch at index {index}, species={species}")
        gamma = float(item["gamma_available_volume_MeV"])
        kappa = float(item["kappa_sc_MeV"])
        if not (math.isfinite(gamma) and gamma > 0.0 and math.isfinite(kappa) and kappa > 0.0):
            raise ValueError(f"invalid C4-C3 baseline rate at index {index}, {species}, {anti}")
        if abs(kappa / (state["xi_SPP"] * gamma) - 1.0) > 5e-13:
            raise ValueError(f"C4-C3 xi_SPP normalization mismatch at index {index}, {species}, {anti}")
        rows.append({
            "E_MeV": 100.0, "profile_index": index, "r_km": float(item["r_km"]),
            "species": species, "antinu": anti, "T_MeV": float(item["T_MeV"]),
            "mstar_MeV": float(item["mstar_MeV"]), "nu_MeV": float(item["nu_MeV"]),
            "X_free": float(item["X_free"]), "xi_SPP": float(item["xi_SPP"]),
            "nB_fm3": float(item["nB_fm3"]),
            "nprime_available_fm3": float(item["nprime_available_fm3"]),
            "n_free_total_volume_fm3": float(item["n_free_total_volume_fm3"]),
            "n_free_EOS_target_fm3": float(item["n_free_EOS_target_fm3"]),
            "density_closure_relative_residual": float(item["density_closure_relative_residual"]),
            "gamma_available_volume_MeV": gamma,
            "sigma_per_target_MeV_minus2": float(item["sigma_per_target_MeV_minus2"]),
            "kappa_sc_MeV": kappa, "lambda_sc_km": MEV_INV_TO_KM / kappa,
            "n_cos": int(float(item["n_cos"])), "n_Eprime": int(float(item["n_Eprime"])),
            "n_p": int(float(item["n_p"])), "n_phi": int(float(item["n_phi"])),
            "support_root_max_relative_residual": float(item["support_root_max_relative_residual"]),
            "source": "C4-C3 archived baseline",
        })
    if len(seen) != RADIAL_POINTS * 4:
        raise ValueError(f"C4-C3 baseline key count is {len(seen)}, expected 1204")
    return rows


def validate_quadrature_rows(rows):
    expected = expected_quad_keys()
    keys = [case_key(row["E_MeV"], row["profile_index"], row["species"], row["antinu"]) for row in rows]
    unique = set(keys)
    diffs = [float(row["relative_difference"]) for row in rows]
    roots = [float(row["support_root_max_relative_residual"]) for row in rows]
    positive = all(
        math.isfinite(float(row["gamma_base_MeV"])) and float(row["gamma_base_MeV"]) > 0.0
        and math.isfinite(float(row["gamma_high_MeV"])) and float(row["gamma_high_MeV"]) > 0.0
        for row in rows
    )
    recomputed_ok = all(
        abs(relative_difference(float(row["gamma_high_MeV"]), float(row["gamma_base_MeV"])) - float(row["relative_difference"])) < 1e-12
        for row in rows
    )
    counts = {
        str(energy): sum(abs(float(row["E_MeV"]) - energy) < 1e-10 for row in rows)
        for energy in NEW_ENERGIES_MEV
    }
    per_energy = {
        str(energy): max(
            (float(row["relative_difference"]) for row in rows if abs(float(row["E_MeV"]) - energy) < 1e-10),
            default=math.inf,
        )
        for energy in NEW_ENERGIES_MEV
    }
    acceptance = {
        "exact_340_case_grid": len(rows) == 340 and len(unique) == 340 and unique == expected,
        "sixty_eight_cases_per_energy": all(counts[str(e)] == len(QUAD_SAMPLE_INDICES) * 4 for e in NEW_ENERGIES_MEV),
        "base_and_high_rates_positive_finite": positive,
        "stored_relative_differences_reproduce": recomputed_ok,
        "support_root_residual_below_1e_7": bool(roots) and all(math.isfinite(x) and x < 1e-7 for x in roots),
        "combined_quadrature_difference_below_1_percent": bool(diffs) and max(diffs) < QUAD_RELATIVE_TOLERANCE,
    }
    return {
        "acceptance": acceptance,
        "quadrature_convergence_pass": all(acceptance.values()),
        "case_counts_by_energy": counts,
        "max_relative_difference": max(diffs, default=math.inf),
        "max_relative_difference_by_energy": per_energy,
        "max_support_root_relative_residual": max(roots, default=math.inf),
    }


def build_radial_products(rows, profile):
    lookup = {
        case_key(row["E_MeV"], row["profile_index"], row["species"], row["antinu"]): row
        for row in rows
    }
    radial_rows, channel_rows, convergence_rows = [], [], []
    tau_by_energy = {}
    r = np.asarray([state["r_km"] for state in profile], dtype=float)
    common = np.arange(0, RADIAL_POINTS, 10, dtype=int)
    for energy in ENERGY_GRID_MEV:
        kappa = {}
        for species in SPECIES:
            for anti in ("False", "True"):
                key = f"{species}_{anti}"
                kappa[key] = np.asarray([
                    float(lookup[case_key(energy, i, species, anti)]["kappa_sc_MeV"])
                    for i in range(RADIAL_POINTS)
                ])
        kappa["total_False"] = kappa["n_False"] + kappa["p_False"]
        kappa["total_True"] = kappa["n_True"] + kappa["p_True"]
        tau = {key: tau_from_kappa(r, values) for key, values in kappa.items()}
        tau_by_energy[energy] = tau
        for i, state in enumerate(profile):
            row = {
                "E_MeV": energy, "profile_index": i, "r_km": state["r_km"],
                "T_MeV": state["T_MeV"], "nB_fm3": state["nB_fm3"], "xi_SPP": state["xi_SPP"],
            }
            for key in ("n_False", "n_True", "p_False", "p_True", "total_False", "total_True"):
                row[f"kappa_{key}_MeV"] = float(kappa[key][i])
                row[f"tau_{key}"] = float(tau[key][i])
            radial_rows.append(row)
            kn, kp = kappa["n_False"][i], kappa["p_False"][i]
            kan, kap = kappa["n_True"][i], kappa["p_True"][i]
            channel_rows.append({
                "E_MeV": energy, "profile_index": i, "r_km": state["r_km"],
                "kappa_n_over_kappa_p_nu": kn / kp,
                "kappa_n_over_kappa_p_antinu": kan / kap,
                "kappa_total_nu_MeV": kappa["total_False"][i],
                "kappa_total_antinu_MeV": kappa["total_True"][i],
                "kappa_total_nu_over_antinu": kappa["total_False"][i] / kappa["total_True"][i],
            })
        for channel, fine in tau.items():
            for stride, step in ((2, 0.10), (5, 0.25)):
                idx = np.arange(0, RADIAL_POINTS, stride, dtype=int)
                if idx[-1] != RADIAL_POINTS - 1:
                    idx = np.append(idx, RADIAL_POINTS - 1)
                coarse = tau_from_kappa(r[idx], kappa[channel][idx])
                positions = {int(value): j for j, value in enumerate(idx)}
                coarse_common = np.asarray([coarse[positions[int(value)]] for value in common])
                fine_common = fine[common]
                diff = np.abs(coarse_common - fine_common)
                tau0 = float(fine[0])
                mask = fine_common > 1e-3 * tau0
                max_rel_tail = float(np.max(diff[mask] / fine_common[mask])) if np.any(mask) else 0.0
                convergence_rows.append({
                    "E_MeV": energy, "channel": channel, "grid_step_km": step,
                    "tau_inner_0p05": tau0, "tau_inner_coarse": float(coarse[0]),
                    "relative_inner_difference": abs(float(coarse[0]) / tau0 - 1.0),
                    "max_abs_difference_over_tau_inner_on_common_nodes": float(np.max(diff) / tau0),
                    "max_relative_difference_where_tau_gt_1e_3_tau0": max_rel_tail,
                    "common_nodes": len(common),
                })
    grid10 = max(row["max_abs_difference_over_tau_inner_on_common_nodes"] for row in convergence_rows if row["grid_step_km"] == 0.10)
    grid25 = max(row["max_abs_difference_over_tau_inner_on_common_nodes"] for row in convergence_rows if row["grid_step_km"] == 0.25)
    monotone = all(
        np.all(np.isfinite(values)) and np.all(values >= 0.0)
        and np.all(np.diff(values) <= 1e-12 * max(float(values[0]), 1.0))
        for tau in tau_by_energy.values() for values in tau.values()
    )
    radial_acceptance = {
        "all_tau_nonnegative_and_radially_monotone": bool(monotone),
        "0p10km_radial_integral_within_1_percent": grid10 < RADIAL_RELATIVE_TOLERANCE,
        "0p25km_radial_integral_within_1_percent": grid25 < RADIAL_RELATIVE_TOLERANCE,
    }
    return radial_rows, channel_rows, convergence_rows, {
        "acceptance": radial_acceptance,
        "radial_grid_convergence_pass": all(radial_acceptance.values()),
        "max_0p10km_difference_over_tau_inner": grid10,
        "max_0p25km_difference_over_tau_inner": grid25,
    }


def build_energy_scaling(rows):
    baseline = {
        (int(row["profile_index"]), row["species"], row["antinu"]): row
        for row in rows if abs(float(row["E_MeV"]) - 100.0) < 1e-10
    }
    if len(baseline) != RADIAL_POINTS * 4:
        raise ValueError("energy scaling requires all 1204 C4-C3 100-MeV baseline rows")
    result = []
    for row in rows:
        base = baseline[(int(row["profile_index"]), row["species"], row["antinu"])]
        result.append({
            "E_MeV": float(row["E_MeV"]), "profile_index": int(row["profile_index"]),
            "r_km": float(row["r_km"]), "species": row["species"], "antinu": row["antinu"],
            "gamma_over_gamma_100MeV": float(row["gamma_available_volume_MeV"]) / float(base["gamma_available_volume_MeV"]),
            "sigma_over_sigma_100MeV": float(row["sigma_per_target_MeV_minus2"]) / float(base["sigma_per_target_MeV_minus2"]),
            "kappa_over_kappa_100MeV": float(row["kappa_sc_MeV"]) / float(base["kappa_sc_MeV"]),
            "lambda_over_lambda_100MeV": float(row["lambda_sc_km"]) / float(base["lambda_sc_km"]),
        })
    return result


def validate_rate_rows(rows, profile):
    expected = expected_rate_keys()
    keys = [case_key(row["E_MeV"], row["profile_index"], row["species"], row["antinu"]) for row in rows]
    unique = set(keys)
    counts = {
        str(energy): sum(abs(float(row["E_MeV"]) - energy) < 1e-10 for row in rows)
        for energy in ENERGY_GRID_MEV
    }
    positive = True
    xi_once = True
    roots = []
    for row in rows:
        vals = (
            float(row["gamma_available_volume_MeV"]), float(row["sigma_per_target_MeV_minus2"]),
            float(row["kappa_sc_MeV"]), float(row["lambda_sc_km"]),
        )
        positive &= all(math.isfinite(x) and x > 0.0 for x in vals)
        xi = float(row["xi_SPP"])
        gamma = float(row["gamma_available_volume_MeV"])
        kappa = float(row["kappa_sc_MeV"])
        xi_once &= abs(kappa / (xi * gamma) - 1.0) < 5e-13
        roots.append(float(row["support_root_max_relative_residual"]))
    max_dn = max(abs(float(row["density_closure_relative_residual"])) for row in rows if row["species"] == "n")
    max_dp = max(abs(float(row["density_closure_relative_residual"])) for row in rows if row["species"] == "p")
    acceptance = {
        "exact_7224_case_grid": len(rows) == 7224 and len(unique) == 7224 and unique == expected,
        "1204_cases_per_energy": all(counts[str(e)] == 1204 for e in ENERGY_GRID_MEV),
        "all_rates_and_derived_quantities_positive_finite": bool(positive),
        "xi_spp_applied_exactly_once": bool(xi_once),
        "support_root_residual_below_1e_7": bool(roots) and all(math.isfinite(x) and x < 1e-7 for x in roots),
        "density_closure_below_1_percent": max_dn < 1e-2 and max_dp < 1e-2,
        "301_point_profile": len(profile) == RADIAL_POINTS,
    }
    return {
        "acceptance": acceptance, "numerical_integrity_pass": all(acceptance.values()),
        "case_counts_by_energy": counts,
        "max_support_root_relative_residual": max(roots, default=math.inf),
        "max_abs_neutron_density_closure_residual": max_dn,
        "max_abs_proton_density_closure_residual": max_dp,
    }


def merge_and_archive(shard_dir: Path, output_dir: Path, source_commit: str) -> dict:
    profile, c2 = load_inputs()
    require_blob_sha(C4C3_BASELINE_PATH, EXPECTED_C4C3_BASELINE_GIT_BLOB, "C4-C3 baseline")
    require_blob_sha(C4C4A_PATH, EXPECTED_C4C4A_GIT_BLOB, "C4-C4-A anchor archive")
    rate_rows, quad_rows = [], []
    shard_dir = Path(shard_dir)
    for energy in NEW_ENERGIES_MEV:
        for shard_index in range(RADIAL_SHARDS):
            stem = f"E{int(energy)}_S{shard_index}"
            rate_path = shard_dir / f"rates_{stem}.csv"
            quad_path = shard_dir / f"quadrature_{stem}.csv"
            if not rate_path.is_file() or not quad_path.is_file():
                raise FileNotFoundError(f"missing rate/quadrature shard: {stem}")
            expected_indices = list(shard_indices(shard_index, RADIAL_SHARDS))
            expected_rate_count = len(expected_indices) * 4
            shard_rates, shard_quads = read_csv(rate_path), read_csv(quad_path)
            if len(shard_rates) != expected_rate_count:
                raise ValueError(f"{rate_path.name}: expected {expected_rate_count} rows, found {len(shard_rates)}")
            expected_quad_count = sum(i in QUAD_SAMPLE_INDICES for i in expected_indices) * 4
            if len(shard_quads) != expected_quad_count:
                raise ValueError(f"{quad_path.name}: expected {expected_quad_count} rows, found {len(shard_quads)}")
            rate_rows.extend({
                key: (item[key] if key in ("species", "antinu", "source") else float(item[key]))
                for key in OUTPUT_FIELDS
            } for item in shard_rates)
            quad_rows.extend({
                key: (item[key] if key in ("species", "antinu") else float(item[key]))
                for key in QUAD_FIELDS
            } for item in shard_quads)
    rate_rows.extend(load_c4c3_baseline(profile, c2))
    rate_rows.sort(key=lambda row: (float(row["E_MeV"]), int(row["profile_index"]), row["species"], row["antinu"]))
    quad_rows.sort(key=lambda row: (float(row["E_MeV"]), int(row["profile_index"]), row["species"], row["antinu"]))

    rate_checks = validate_rate_rows(rate_rows, profile)
    quad_checks = validate_quadrature_rows(quad_rows)
    radial_rows, channel_rows, convergence_rows, radial_checks = build_radial_products(rate_rows, profile)

    # Compare all 96 C4-C4-A anchors against the merged full-radial table.
    anchor_rows = read_csv(C4C4A_PATH)
    if len(anchor_rows) != 96:
        raise ValueError(f"expected 96 C4-C4-A anchor rows, found {len(anchor_rows)}")
    radius_to_index = {round(float(state["r_km"]), 8): i for i, state in enumerate(profile)}
    rate_lookup = {
        case_key(row["E_MeV"], row["profile_index"], row["species"], row["antinu"]): row
        for row in rate_rows
    }
    anchor_diffs = []
    for item in anchor_rows:
        index = radius_to_index[round(float(item["r_km"]), 8)]
        key = case_key(float(item["E_MeV"]), index, item["species"], item["antinu"])
        if key not in rate_lookup:
            raise KeyError(f"missing full-radial anchor case: {key}")
        actual = float(rate_lookup[key]["gamma_available_volume_MeV"])
        reference = float(item["gamma_available_volume_MeV"])
        anchor_diffs.append(abs(actual / reference - 1.0))
    max_anchor_diff = max(anchor_diffs, default=math.inf)
    anchor_pass = len(anchor_diffs) == 96 and max_anchor_diff < 1e-8

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    energy_ratios = build_energy_scaling(rate_rows)
    write_csv(output_dir / "local_rates_7224.csv", rate_rows)
    write_csv(output_dir / "energy_scaling_ratios_7224.csv", energy_ratios)
    write_csv(output_dir / "channel_ratios_1806.csv", channel_rows)
    write_csv(output_dir / "radial_opacity_tau_1806.csv", radial_rows)
    write_csv(output_dir / "quadrature_convergence_340.csv", quad_rows)
    write_csv(output_dir / "radial_grid_convergence_72.csv", convergence_rows)

    acceptance = {
        **rate_checks["acceptance"],
        "c4c3_100mev_baseline_blob_matches": git_blob_sha(C4C3_BASELINE_PATH) == EXPECTED_C4C3_BASELINE_GIT_BLOB,
        "c4c4a_anchor_blob_matches": git_blob_sha(C4C4A_PATH) == EXPECTED_C4C4A_GIT_BLOB,
        "all_96_c4c4a_anchor_rates_reproduced_below_1e_8": anchor_pass,
    }
    quadrature_record = {
        "base": BASE_ORDERS,
        "high_order": HIGH_ORDERS,
        "support_scan_points": SUPPORT_SCAN_POINTS,
        "high_order_sample_indices": list(QUAD_SAMPLE_INDICES),
        "high_order_sample_radii_km": [float(profile[i]["r_km"]) for i in QUAD_SAMPLE_INDICES],
        "high_order_case_count": len(quad_rows),
        "high_order_relative_tolerance": QUAD_RELATIVE_TOLERANCE,
        **quad_checks,
    }
    summary = {
        "title": "C4-C4-B full-radial EOS moving-nucleon scattering energy dependence",
        "date": "2026-11-13",
        "stage": "C4-C4-B 301-radius energy-dependent local rates and flat-space fixed-local-energy optical depth",
        "source_commit": source_commit,
        "physical_validation_status": "not a transport or literature-reproduction acceptance",
        "energy_grid_MeV": list(ENERGY_GRID_MEV),
        "newly_computed_energies_MeV": list(NEW_ENERGIES_MEV),
        "radial_points": RADIAL_POINTS,
        "radial_range_km": [float(profile[0]["r_km"]), float(profile[-1]["r_km"])],
        "radial_spacing_km": 0.05,
        "species": list(SPECIES),
        "incoming_states": ["nu", "antinu"],
        "case_count": len(rate_rows),
        "newly_recomputed_case_count": len(rate_rows) - 1204,
        "reused_C4C3_100MeV_baseline_case_count": 1204,
        "inputs": {
            "profile_path": str(PROFILE_PATH.relative_to(HERE)),
            "profile_git_blob_sha": git_blob_sha(PROFILE_PATH),
            "C2_occupation_path": str(C2_PATH.relative_to(HERE)),
            "C2_occupation_git_blob_sha": git_blob_sha(C2_PATH),
            "C4C3_100MeV_baseline_path": str(C4C3_BASELINE_PATH.relative_to(HERE)),
            "C4C3_100MeV_baseline_git_blob_sha": git_blob_sha(C4C3_BASELINE_PATH),
            "C4C4A_anchor_path": str(C4C4A_PATH.relative_to(HERE)),
            "C4C4A_anchor_git_blob_sha": git_blob_sha(C4C4A_PATH),
            "C4B2_kernel_git_blob_sha": EXPECTED_C4B2_GIT_BLOB,
            "C4C1_support_git_blob_sha": EXPECTED_C4C1_GIT_BLOB,
            "C4C2_integrator_git_blob_sha": EXPECTED_C4C2_GIT_BLOB,
            "C4C3_numba_accelerator_code_origin_blob_sha_reference_only": "821e39edfe235f5a8fcac6b2e074bb0dcb9631c6",
        },
        "acceptance": acceptance,
        "numerical_integrity_pass": all(acceptance.values()),
        "max_support_root_relative_residual": rate_checks["max_support_root_relative_residual"],
        "max_abs_neutron_density_closure_residual": rate_checks["max_abs_neutron_density_closure_residual"],
        "max_abs_proton_density_closure_residual": rate_checks["max_abs_proton_density_closure_residual"],
        "max_anchor_relative_difference_vs_C4C4A": max_anchor_diff,
        "anchor_case_count": len(anchor_diffs),
        "quadrature": quadrature_record,
        "radial_grid": {
            **radial_checks,
            "radial_relative_tolerance": RADIAL_RELATIVE_TOLERANCE,
            "comparison_rows": len(convergence_rows),
        },
        "interpretation": [
            "100-MeV local rates are reused from the separately validated C4-C3 301-radius archive and are not recomputed.",
            "The 100-MeV C4-C3 baseline is checked against the C4-C4-A anchor records; all energies are checked against all 96 C4-C4-A anchor records.",
            "The full radial energy scan uses fixed local incident energy at every radius and flat-space radial integration.",
            "The radial optical depth is a total-scattering diagnostic, not an absorption-only transport optical depth or escape probability.",
            "The high-order comparisons are stratified over 17 radial nodes; they are not a pointwise high-order calculation at all 301 radii.",
            "No gravitational redshift, energy redistribution, angular transport, hydrodynamic feedback, full Blinov Fig. 7 luminosity, or SN1987A exclusion is inferred.",
        ],
    }
    write_json(output_dir / "summary.json", summary)
    readme = f"""# C4-C4-B full-radial energy-dependence archive

- Source commit: {source_commit}
- Energies: {", ".join(str(int(x)) for x in ENERGY_GRID_MEV)} MeV
- Radial grid: {RADIAL_POINTS} points, {profile[0]["r_km"]:.2f}–{profile[-1]["r_km"]:.2f} km, 0.05 km spacing
- Local rate rows: {len(rate_rows)} (6020 new + 1204 reused from C4-C3 at 100 MeV)
- Stratified high-order cases: {len(quad_rows)}
- Numerical-integrity status: {"PASS" if summary["numerical_integrity_pass"] else "NOT PASSED"}
- Combined quadrature convergence: {"PASS" if quad_checks["quadrature_convergence_pass"] else "NOT PASSED"}
- Radial-grid convergence: {"PASS" if radial_checks["radial_grid_convergence_pass"] else "NOT PASSED"}
- Maximum C4-C4-A anchor difference: {max_anchor_diff:.6e}

The 100-MeV baseline is reused without recomputation from the byte-pinned C4-C3 301-radius archive. Five new energy slices are computed with the EOS moving-nucleon C4-B2/C4-C1/C4-C2 kernel. The filling factor xi_SPP is applied once in kappa_N = xi_SPP * Gamma_N_available.

The optical depth is a flat-space, fixed-local-energy radial integral. It is not a redshifted transport solution, escape probability, or SN1987A exclusion. The high-order quadrature comparison is stratified at 17 radial points per new energy, not evaluated at every radial point.
"""
    (output_dir / "README.md").write_text(readme, encoding="utf-8")
    provenance = f"""# C4-C4-B source and input provenance

- Profile Git blob SHA: {git_blob_sha(PROFILE_PATH)}
- C2 occupation Git blob SHA: {git_blob_sha(C2_PATH)}
- C4-C3 100-MeV 301x4 baseline Git blob SHA: {git_blob_sha(C4C3_BASELINE_PATH)}
- C4-C4-A 96-row anchor archive Git blob SHA: {git_blob_sha(C4C4A_PATH)}
- C4-B2 effective-mass kernel blob SHA: {EXPECTED_C4B2_GIT_BLOB}
- C4-C1 exact support blob SHA: {EXPECTED_C4C1_GIT_BLOB}
- C4-C2 full-angle integrator blob SHA: {EXPECTED_C4C2_GIT_BLOB}
- Reused C4-C3 Numba accelerator source blob SHA: 821e39edfe235f5a8fcac6b2e074bb0dcb9631c6

The C4-C3 100-MeV rates are reused, not recalculated. The C4-C4-A anchor archive is an independent unaccelerated reference for the four anchor radii. The Numba accelerator changes only the innermost Dirac-matrix contraction; it does not change phase-space support, Fermi factors, weak form factors, or quadrature nodes.
"""
    (output_dir / "SOURCE_PROVENANCE.md").write_text(provenance, encoding="utf-8")
    manifest = []
    for file in sorted(output_dir.iterdir()):
        if file.is_file() and file.name != "SHA256SUMS.txt":
            manifest.append(f"{sha256_file(file)}  {file.name}")
    (output_dir / "SHA256SUMS.txt").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--energy", type=float)
    parser.add_argument("--shard-index", type=int)
    parser.add_argument("--shard-count", type=int, default=RADIAL_SHARDS)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--merge-dir", type=Path)
    parser.add_argument("--check-summary", type=Path)
    parser.add_argument("--source-commit", default=os.environ.get("GITHUB_SHA", "local"))
    args = parser.parse_args()

    if args.check_summary is not None:
        summary = json.loads(args.check_summary.read_text(encoding="utf-8"))
        checks = (
            bool(summary["numerical_integrity_pass"])
            and bool(summary["quadrature"]["quadrature_convergence_pass"])
            and bool(summary["radial_grid"]["radial_grid_convergence_pass"])
        )
        print(json.dumps({
            "numerical_integrity_pass": summary["numerical_integrity_pass"],
            "quadrature_convergence_pass": summary["quadrature"]["quadrature_convergence_pass"],
            "radial_grid_convergence_pass": summary["radial_grid"]["radial_grid_convergence_pass"],
            "max_anchor_relative_difference_vs_C4C4A": summary["max_anchor_relative_difference_vs_C4C4A"],
            "max_quadrature_relative_difference": summary["quadrature"]["max_relative_difference"],
            "radial_grid": summary["radial_grid"],
        }, indent=2))
        if not checks:
            raise SystemExit(1)
        return

    if args.output_dir is None:
        parser.error("--output-dir is required")
    if args.merge_dir is not None:
        summary = merge_and_archive(args.merge_dir, args.output_dir, args.source_commit)
        print(json.dumps({
            "numerical_integrity_pass": summary["numerical_integrity_pass"],
            "quadrature_convergence_pass": summary["quadrature"]["quadrature_convergence_pass"],
            "radial_grid_convergence_pass": summary["radial_grid"]["radial_grid_convergence_pass"],
            "case_count": summary["case_count"],
            "max_anchor_relative_difference_vs_C4C4A": summary["max_anchor_relative_difference_vs_C4C4A"],
            "max_quadrature_relative_difference": summary["quadrature"]["max_relative_difference"],
        }, indent=2))
        return

    if args.energy is None or args.shard_index is None:
        parser.error("--energy and --shard-index are required for a compute shard")
    profile, c2 = load_inputs()
    indices = shard_indices(args.shard_index, args.shard_count)
    rates, quads = compute_shard(args.energy, indices, profile, c2)
    stem = f"E{int(args.energy)}_S{args.shard_index}"
    write_csv(args.output_dir / f"rates_{stem}.csv", rates)
    write_csv(args.output_dir / f"quadrature_{stem}.csv", quads)
    print(json.dumps({
        "energy_MeV": args.energy, "shard_index": args.shard_index,
        "radial_indices": [indices.start, indices.stop - 1],
        "rate_rows": len(rates), "quadrature_rows": len(quads),
        "max_support_root_relative_residual": max(row["support_root_max_relative_residual"] for row in rates),
        "max_quadrature_relative_difference": max(row["relative_difference"] for row in quads),
        "source_commit": args.source_commit,
    }, indent=2))


if __name__ == "__main__":
    main()
