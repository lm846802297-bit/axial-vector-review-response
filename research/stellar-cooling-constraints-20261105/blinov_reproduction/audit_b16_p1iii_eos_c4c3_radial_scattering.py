#!/usr/bin/env python3
"""C4-C3: 301-point radial EOS total-scattering rates and flat-space optical depth."""
from __future__ import annotations
import argparse, csv, json, math, os
from pathlib import Path
import numpy as np

from audit_b16_p1iii_eos_full_radial_occupation import load_profile
from audit_b16_p1iii_eos_c4b2_effective_mass_collision_kernel import HBARC, INCIDENT_ENERGY
from audit_b16_p1iii_eos_c4c1_exact_outgoing_energy_support import load_c2_reference
from audit_b16_p1iii_eos_c4c2_full_angle_total_scattering import (
    LOCAL_COS_ORDER, LOCAL_EPRIME_ORDER, LOCAL_P_ORDER, LOCAL_PHI_ORDER,
    LOCAL_SUPPORT_SCAN, integrate_total_rate,
)

HERE = Path(__file__).resolve().parent
PROFILE = HERE / "outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv"
C2 = HERE / "outputs/p1iii_eos_full_radial_occupation_2026-11-11.csv"
C4C2_REFERENCE = HERE / "outputs/p1iiie_c4c2_full_angle_total_rates_2026-11-11.csv"
KM_TO_MEV_INV = 1.0e18 / 197.3269804
SPECIES = ("n", "p")
ANTINU = ("False", "True")


def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"empty output: {path}")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def shard_indices(shard_index, shard_count, npoints=301):
    if shard_count < 1 or not 0 <= shard_index < shard_count:
        raise ValueError("invalid shard index/count")
    return range(npoints * shard_index // shard_count,
                 npoints * (shard_index + 1) // shard_count)


def compute_rate_shard(profile, c2, indices, incident_energy=INCIDENT_ENERGY):
    rows = []
    for i in indices:
        s, occ = profile[i], c2[i]
        if abs(s["r_km"] - occ["r_km"]) > 1e-12:
            raise ValueError(f"C1/C2 radial mismatch at index {i}")
        xi, nB = s["xi_SPP"], s["nB_fm3"]
        for species in SPECIES:
            X = s[f"X_{species}"]
            nprime = occ[f"nprime_{species}_fm3"]
            nu = occ[f"nu_{species}_EOS_MeV"]
            mstar = s[f"mstar_{species}_MeV"]
            nfree = xi * nprime
            nfree_eos = X * nB
            if min(xi, nprime, nfree_eos) <= 0:
                raise ArithmeticError(f"non-positive free-nucleon density at r={s['r_km']} km")
            closure = nfree / nfree_eos - 1.0
            for anti in (False, True):
                gamma, root = integrate_total_rate(
                    incident_energy, species, anti, s["T_MeV"], nu, mstar,
                    n_cos=LOCAL_COS_ORDER, order_ep=LOCAL_EPRIME_ORDER,
                    order_p=LOCAL_P_ORDER, order_phi=LOCAL_PHI_ORDER,
                    support_scan_points=LOCAL_SUPPORT_SCAN,
                )
                if not math.isfinite(gamma) or gamma <= 0:
                    raise ArithmeticError(f"non-positive rate at r={s['r_km']} km, {species}, anti={anti}")
                rows.append({
                    "profile_index": i, "r_km": s["r_km"], "species": species,
                    "antinu": str(anti), "E_MeV": incident_energy, "T_MeV": s["T_MeV"],
                    "mstar_MeV": mstar, "nu_MeV": nu, "X_free": X, "xi_SPP": xi,
                    "nB_fm3": nB, "nprime_available_fm3": nprime,
                    "n_free_total_volume_fm3": nfree, "n_free_EOS_target_fm3": nfree_eos,
                    "density_closure_relative_residual": closure,
                    "gamma_available_volume_MeV": gamma,
                    "sigma_per_target_MeV_minus2": gamma / (nprime * HBARC**3),
                    "kappa_sc_MeV": xi * gamma,
                    "n_cos": LOCAL_COS_ORDER, "n_Eprime": LOCAL_EPRIME_ORDER,
                    "n_p": LOCAL_P_ORDER, "n_phi": LOCAL_PHI_ORDER,
                    "support_root_max_relative_residual": root,
                })
    return rows


def tau_from_kappa(r_km, kappa_mev):
    r = np.asarray(r_km, dtype=float)
    k = np.asarray(kappa_mev, dtype=float)
    if r.ndim != 1 or k.ndim != 1 or len(r) != len(k) or len(r) < 2:
        raise ValueError("r and kappa must be equal-length one-dimensional arrays")
    if not np.all(np.isfinite(r)) or not np.all(np.isfinite(k)):
        raise ValueError("non-finite radial coordinate or opacity")
    if np.any(np.diff(r) <= 0) or np.any(k < 0):
        raise ValueError("r must increase and kappa must be non-negative")
    tau = np.zeros_like(r)
    for i in range(len(r) - 2, -1, -1):
        dr = (r[i + 1] - r[i]) * KM_TO_MEV_INV
        tau[i] = tau[i + 1] + 0.5 * (k[i] + k[i + 1]) * dr
    return tau


def merge_shards(shard_dir, profile, c2, output_dir, source_commit="local"):
    shard_files = sorted(Path(shard_dir).glob("rates_shard_*.csv"))
    if not shard_files:
        raise FileNotFoundError(f"no rate shards in {shard_dir}")
    raw = [row for path in shard_files for row in read_csv(path)]
    if len(raw) != 1204:
        raise ValueError(f"expected 1204 local rates, found {len(raw)}")
    rows = [{k: (v if k in ("species", "antinu") else float(v)) for k, v in row.items()} for row in raw]
    rows.sort(key=lambda x: (int(x["profile_index"]), x["species"], x["antinu"]))
    keys = [(int(x["profile_index"]), x["species"], x["antinu"]) for x in rows]
    expected = [(i, sp, anti) for i in range(301) for sp in SPECIES for anti in ANTINU]
    if len(set(keys)) != 1204 or keys != expected:
        raise ValueError("rate shards contain missing, duplicated, or unordered cases")

    r = np.asarray([x["r_km"] for x in profile], dtype=float)
    if len(r) != 301 or abs(r[0] - 0.2) > 1e-10 or abs(r[-1] - 15.2) > 1e-10:
        raise ValueError("unexpected C1 radial endpoints")
    if np.max(np.abs(np.diff(r) - 0.05)) > 1e-8:
        raise ValueError("C1 radial grid is not the 0.05-km base grid")
    rate = {(int(x["profile_index"]), x["species"], x["antinu"]): x for x in rows}

    kappa = {}
    for anti in ANTINU:
        for sp in SPECIES:
            kappa[f"{sp}_{anti}"] = np.asarray(
                [rate[(i, sp, anti)]["kappa_sc_MeV"] for i in range(301)], dtype=float
            )
        kappa[f"total_{anti}"] = kappa[f"n_{anti}"] + kappa[f"p_{anti}"]
    tau = {key: tau_from_kappa(r, values) for key, values in kappa.items()}

    radial = []
    for i, s in enumerate(profile):
        o = c2[i]
        row = {
            "profile_index": i, "r_km": s["r_km"], "T_MeV": s["T_MeV"],
            "nB_fm3": s["nB_fm3"], "xi_SPP": s["xi_SPP"], "X_n": s["X_n"], "X_p": s["X_p"],
            "nprime_n_available_fm3": o["nprime_n_fm3"],
            "nprime_p_available_fm3": o["nprime_p_fm3"],
            "n_n_free_total_volume_fm3": s["xi_SPP"] * o["nprime_n_fm3"],
            "n_p_free_total_volume_fm3": s["xi_SPP"] * o["nprime_p_fm3"],
            "n_n_free_EOS_target_fm3": s["X_n"] * s["nB_fm3"],
            "n_p_free_EOS_target_fm3": s["X_p"] * s["nB_fm3"],
            "density_closure_relative_residual_n": s["xi_SPP"] * o["nprime_n_fm3"] / (s["X_n"] * s["nB_fm3"]) - 1,
            "density_closure_relative_residual_p": s["xi_SPP"] * o["nprime_p_fm3"] / (s["X_p"] * s["nB_fm3"]) - 1,
        }
        for sp in SPECIES:
            for anti in ANTINU:
                row[f"gamma_{sp}_{anti}_available_MeV"] = rate[(i, sp, anti)]["gamma_available_volume_MeV"]
                row[f"kappa_{sp}_{anti}_MeV"] = kappa[f"{sp}_{anti}"][i]
                row[f"tau_{sp}_{anti}_0p05"] = tau[f"{sp}_{anti}"][i]
        for anti in ANTINU:
            row[f"kappa_total_{anti}_MeV"] = kappa[f"total_{anti}"][i]
            row[f"tau_total_{anti}_0p05"] = tau[f"total_{anti}"][i]
        radial.append(row)

    # C4-C2 regression: the four previously computed radii must reproduce exactly.
    ref_path = C4C2_REFERENCE
    refs = read_csv(ref_path) if ref_path.exists() else []
    if refs and len(refs) != 16:
        raise ValueError("C4-C2 reference table must contain 16 rows")
    index_by_r = {round(float(profile[i]["r_km"]), 8): i for i in (0, 96, 196, 300)}
    c4c2_max = 0.0
    for ref in refs:
        i = index_by_r[round(float(ref["r_km"]), 8)]
        actual = rate[(i, ref["species"], ref["antinu"])]["gamma_available_volume_MeV"]
        c4c2_max = max(c4c2_max, abs(actual / float(ref["gamma_total_available_volume_MeV"]) - 1.0))

    convergence = []
    common = np.arange(0, 301, 10, dtype=int)  # 0.50-km nodes common to all three grids.
    for channel, fine in tau.items():
        for stride, step in ((2, 0.10), (5, 0.25)):
            idx = np.arange(0, 301, stride, dtype=int)
            if idx[-1] != 300:
                idx = np.append(idx, 300)
            coarse = tau_from_kappa(r[idx], kappa[channel][idx])
            pos = {int(v): j for j, v in enumerate(idx)}
            coarse_common = np.asarray([coarse[pos[int(v)]] for v in common])
            fine_common = fine[common]
            diff = np.abs(coarse_common - fine_common)
            tau0 = fine[0]
            mask = fine_common > 1e-3 * tau0
            max_tail_safe = float(np.max(diff[mask] / fine_common[mask])) if np.any(mask) else 0.0
            convergence.append({
                "channel": channel, "grid_step_km": step, "tau_inner_0p05": tau0,
                "tau_inner_coarse": float(coarse[0]),
                "relative_inner_difference": abs(float(coarse[0]) / tau0 - 1.0),
                "max_abs_difference_over_tau_inner_on_common_nodes": float(np.max(diff) / tau0),
                "max_relative_difference_where_tau_gt_1e_3_tau0": max_tail_safe,
                "common_nodes": len(common),
            })

    max_dn = max(abs(x["density_closure_relative_residual_n"]) for x in radial)
    max_dp = max(abs(x["density_closure_relative_residual_p"]) for x in radial)
    max_root = max(float(x["support_root_max_relative_residual"]) for x in rows)
    grid10 = max(x["max_abs_difference_over_tau_inner_on_common_nodes"] for x in convergence if x["grid_step_km"] == 0.10)
    grid25 = max(x["max_abs_difference_over_tau_inner_on_common_nodes"] for x in convergence if x["grid_step_km"] == 0.25)
    monotone = all(np.all(np.diff(v) <= 1e-12 * max(v[0], 1.0)) and np.all(v >= 0) for v in tau.values())
    acceptance = {
        "301_radial_points": len(profile) == 301,
        "1204_local_species_sign_cases": len(rows) == 1204,
        "all_local_rates_positive": all(float(x["gamma_available_volume_MeV"]) > 0 for x in rows),
        "C2_neutron_density_closure_below_1_percent": max_dn < 1e-2,
        "C2_proton_density_closure_below_1_percent": max_dp < 1e-2,
        "support_root_residual_below_1e_7": max_root < 1e-7,
        "tau_nonnegative_and_radially_monotone": monotone,
        "0p10km_radial_integral_within_1_percent": grid10 < 1e-2,
        "0p25km_radial_integral_within_1_percent": grid25 < 1e-2,
        "C4C2_four_radius_local_rate_reproduction_below_1e_8": (not refs) or c4c2_max < 1e-8,
    }
    summary = {
        "title": "P1-IIIe-C4C3 301-point radial total scattering and flat-space optical depth",
        "date": "2026-11-11", "source_commit": source_commit,
        "scope": "Caputo SFHo-18.8 published-figure snapshot at t_pb=1 s; fixed local incident energy; flat-space radial diagnostic only.",
        "provenance": {
            "profile_git_blob_sha_expected": "9ff7818b0679992c0a9ba402330ec7f0d1f3041b",
            "c2_occupation_git_blob_sha_expected": "c472040a4551e68ffadbf7addf9402663f99e7e3",
            "radial_points": 301, "radial_range_km": [float(r[0]), float(r[-1])],
            "base_radial_step_km": 0.05, "incident_local_energy_MeV": INCIDENT_ENERGY,
            "species": list(SPECIES), "incoming_states": ["nu", "antinu"],
        },
        "collision_kernel": {
            "source": "Existing C4-B2/C4-C1/C4-C2 implementation; no new collision kernel.",
            "quadrature": {"cosine": LOCAL_COS_ORDER, "outgoing_energy": LOCAL_EPRIME_ORDER,
                           "initial_momentum": LOCAL_P_ORDER, "azimuth": LOCAL_PHI_ORDER,
                           "support_scan_points": LOCAL_SUPPORT_SCAN},
            "available_volume_rate_definition": "Gamma_N^avail already contains nprime_N from the Fermi occupation integral; kappa_N=xi_SPP*Gamma_N^avail, with xi applied exactly once.",
        },
        "units": {"kappa": "MeV = inverse length in natural units", "radial_coordinate": "km",
                  "km_to_MeV_inverse": KM_TO_MEV_INV,
                  "tau": "dimensionless; dr_km is converted to MeV^-1 before integration"},
        "density_closure": {
            "max_abs_relative_residual_neutron": max_dn, "max_abs_relative_residual_proton": max_dp,
            "primary_density_used_for_opacity": "xi_SPP*nprime_N from EOS-tabulated Fermi occupations",
            "EOS_target_density": "X_N*nB is a closure diagnostic; it is not used to renormalize rates",
        },
        "maxima": {"support_root_relative_residual": max_root,
                   "radial_tau_0p10_max_abs_difference_over_tau_inner": grid10,
                   "radial_tau_0p25_max_abs_difference_over_tau_inner": grid25,
                   "C4C2_four_radius_local_rate_max_relative_difference": c4c2_max if refs else None},
        "acceptance": acceptance, "overall_pass": all(acceptance.values()),
        "interpretation": [
            "Fixed-local-energy, flat-space radial scattering optical-depth diagnostic only.",
            "Not a redshifted transport optical depth, a full escape probability, or a transport solution.",
            "Neutrino and antineutrino incoming states are kept separate.",
            "Total scattering, angular transport, and energy-transfer moments remain separate C4-D tasks.",
        ],
    }
    out = Path(output_dir)
    write_csv(out / "radial_rates_301x4.csv", rows)
    write_csv(out / "radial_opacity_tau_0p05km.csv", radial)
    write_csv(out / "radial_tau_grid_convergence.csv", convergence)
    (out / "summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    if not summary["overall_pass"]:
        raise AssertionError(f"C4-C3 acceptance failed: {acceptance}")
    return summary


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile", type=Path, default=PROFILE)
    p.add_argument("--c2-reference", type=Path, default=C2)
    p.add_argument("--shard-index", type=int)
    p.add_argument("--shard-count", type=int, default=1)
    p.add_argument("--output-csv", type=Path)
    p.add_argument("--merge-dir", type=Path)
    p.add_argument("--output-dir", type=Path)
    p.add_argument("--source-commit", default=os.environ.get("GITHUB_SHA", "local"))
    a = p.parse_args()
    profile, c2 = load_profile(a.profile), load_c2_reference(a.c2_reference)
    if a.merge_dir:
        if not a.output_dir:
            p.error("--output-dir is required with --merge-dir")
        s = merge_shards(a.merge_dir, profile, c2, a.output_dir, a.source_commit)
        print(json.dumps({"overall_pass": s["overall_pass"], "maxima": s["maxima"], "acceptance": s["acceptance"]}, indent=2))
    else:
        if a.shard_index is None or a.output_csv is None:
            p.error("--shard-index and --output-csv are required for a rate shard")
        idx = shard_indices(a.shard_index, a.shard_count, len(profile))
        rows = compute_rate_shard(profile, c2, idx)
        write_csv(a.output_csv, rows)
        print(json.dumps({"shard_index": a.shard_index, "shard_count": a.shard_count,
                          "radial_indices": [idx.start, idx.stop - 1], "rows": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
