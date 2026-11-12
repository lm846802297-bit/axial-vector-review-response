#!/usr/bin/env python3
"""Build a dense Caputo/Garching SFHo-18.8 snapshot input for the SFHo EOS.

The composition CSV is generated from the checksum-pinned native PDF paths in
Caputo Fig. 1 and Fig. 4.  Temperature is interpolated from the already
archived Fig. 1 vector vertices.  This is a published-figure reconstruction,
not a raw time-dependent Garching simulation dump.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np

N0_CAPUTO_FM3 = 0.181
SOURCE_ARCHIVE_SHA256 = "2e4a1280460bce9a5f7596d3dfd1d3e0f4752f2e1706e85d3a2c20b5f9dbbd8e"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def build_profile_rows(
    temperature_rows: list[dict[str, str]],
    composition_rows: list[dict[str, str]],
    step_km: float = 0.05,
) -> list[dict[str, float]]:
    if not np.isfinite(step_km) or step_km <= 0.0:
        raise ValueError("step_km must be finite and positive")
    if len(temperature_rows) < 2 or len(composition_rows) < 2:
        raise ValueError("temperature and composition inputs need at least two rows")

    t_required = {"r_km", "value"}
    c_required = {
        "r_km", "nB_over_n0", "Yn", "Yp", "Ye_plus_Ymu",
        "Xcluster", "Ycluster_charge",
    }
    if not t_required.issubset(temperature_rows[0]):
        raise ValueError(f"temperature CSV requires {sorted(t_required)}")
    if not c_required.issubset(composition_rows[0]):
        raise ValueError(f"composition CSV requires {sorted(c_required)}")

    t = sorted(
        [(float(row["r_km"]), float(row["value"])) for row in temperature_rows],
        key=lambda item: item[0],
    )
    c = sorted(composition_rows, key=lambda row: float(row["r_km"]))
    tr = np.asarray([item[0] for item in t], dtype=float)
    tv = np.asarray([item[1] for item in t], dtype=float)
    cr = np.asarray([float(row["r_km"]) for row in c], dtype=float)

    if not np.all(np.isfinite(tr)) or not np.all(np.isfinite(tv)):
        raise ValueError("temperature vertices contain non-finite values")
    if np.any(np.diff(tr) <= 0.0):
        raise ValueError("temperature radii must be strictly increasing")
    if np.any(np.diff(cr) <= 0.0):
        raise ValueError("composition radii must be strictly increasing")
    if cr[0] < tr[0] or cr[-1] > tr[-1]:
        raise ValueError("temperature interpolation would extrapolate beyond its source")
    if not np.allclose(np.diff(cr), step_km, rtol=0.0, atol=1e-8):
        raise ValueError("composition profile is not on the requested uniform radial grid")

    temperatures = np.interp(cr, tr, tv)
    if np.any(~np.isfinite(temperatures)) or np.any(temperatures <= 0.0):
        raise ValueError("interpolated temperature must be finite and positive")

    rows: list[dict[str, float]] = []
    for radius, temperature, source in zip(cr, temperatures, c):
        nB_over_n0 = float(source["nB_over_n0"])
        Yn = float(source["Yn"])
        Yp = float(source["Yp"])
        Yp_tot = float(source["Ye_plus_Ymu"])
        Xcluster = float(source["Xcluster"])
        Ycluster_charge = float(source["Ycluster_charge"])
        values = (nB_over_n0, Yn, Yp, Yp_tot, Xcluster, Ycluster_charge)
        if not np.all(np.isfinite(values)):
            raise ValueError(f"non-finite composition input at r={radius:g} km")
        if nB_over_n0 <= 0.0:
            raise ValueError(f"non-positive baryon density at r={radius:g} km")
        if min(Yn, Yp, Xcluster, Ycluster_charge) < -5e-5:
            raise ValueError(f"negative abundance at r={radius:g} km")
        if not (0.01 <= Yp_tot <= 0.60):
            raise ValueError(f"Yp_tot outside the SFHo SPP grid at r={radius:g} km")
        if abs(Yn + Yp + Xcluster - 1.0) > 5e-5:
            raise ValueError(f"baryon composition does not close at r={radius:g} km")
        if abs(Ycluster_charge - (Yp_tot - Yp)) > 5e-5:
            raise ValueError(f"cluster charge does not close at r={radius:g} km")
        if Yp_tot + 5e-5 < Yp:
            raise ValueError(f"total proton fraction is below free Yp at r={radius:g} km")

        nB = nB_over_n0 * N0_CAPUTO_FM3
        nn = Yn * nB
        np_free = Yp * nB
        ncluster = Xcluster * nB
        if abs(nn + np_free + ncluster - nB) > 5e-5 * nB:
            raise ValueError(f"free-plus-cluster baryon density fails at r={radius:g} km")

        rows.append({
            "r_km": float(radius),
            "T_MeV": float(temperature),
            "nB_over_n0": nB_over_n0,
            "nB_fm3": nB,
            "Yn_free": Yn,
            "Yp_free": Yp,
            "Yp_tot": Yp_tot,
            "Xcluster": Xcluster,
            "Ycluster_charge": Ycluster_charge,
            "n_n_free_fm3": nn,
            "n_p_free_fm3": np_free,
            "n_cluster_baryon_fm3": ncluster,
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--temperature-csv", type=Path, required=True)
    parser.add_argument("--composition-csv", type=Path, required=True)
    parser.add_argument("--profile-csv", type=Path, required=True)
    parser.add_argument("--provenance-json", type=Path, required=True)
    parser.add_argument("--step-km", type=float, default=0.05)
    args = parser.parse_args()

    temperature_rows = read_csv(args.temperature_csv)
    composition_rows = read_csv(args.composition_csv)
    rows = build_profile_rows(temperature_rows, composition_rows, args.step_km)

    args.profile_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.profile_csv.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows({
            key: f"{value:.12g}" for key, value in row.items()
        } for row in rows)

    radii = np.asarray([row["r_km"] for row in rows])
    provenance = {
        "source": "Caputo, Raffelt, Vitagliano, arXiv:2109.03244v3",
        "source_archive_sha256": SOURCE_ARCHIVE_SHA256,
        "temperature_source": "Fig. 1 upper-panel T(r), linearly interpolated from native PDF vector vertices",
        "composition_source": "Fig. 1 lower-panel nB and Fig. 4 upper-panel Yn, Yp, Ye+Ymu, extracted from native PDF vector paths",
        "temperature_csv": str(args.temperature_csv),
        "temperature_csv_sha256": sha256(args.temperature_csv),
        "composition_profile_csv": str(args.composition_csv),
        "composition_profile_csv_sha256": sha256(args.composition_csv),
        "normalization_n0_fm3": N0_CAPUTO_FM3,
        "eos_Yp_coordinate": "Yp_tot=Ye+Ymu; free-proton abundance Yp is not the EOS coordinate",
        "radial_grid_km": {
            "min": float(radii[0]),
            "max": float(radii[-1]),
            "step": args.step_km,
            "points": len(rows),
        },
        "profile_csv": str(args.profile_csv),
        "profile_csv_sha256": sha256(args.profile_csv),
        "scope": "digitized published t_pb=1 s snapshot; not raw time-dependent Garching profile data",
    }
    args.provenance_json.parent.mkdir(parents=True, exist_ok=True)
    args.provenance_json.write_text(
        json.dumps(provenance, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(provenance, indent=2))


if __name__ == "__main__":
    main()
