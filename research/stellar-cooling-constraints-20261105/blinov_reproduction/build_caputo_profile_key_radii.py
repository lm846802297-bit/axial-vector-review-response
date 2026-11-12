#!/usr/bin/env python3
"""Build the Caputo SFHo-18.8 key-radius snapshot input for the SFHo EOS."""
from __future__ import annotations
import argparse, csv, hashlib, json
from pathlib import Path
import numpy as np

N0_CAPUTO_FM3 = 0.181
RADII_KM = (1.0, 5.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--temperature-csv", type=Path, required=True)
    ap.add_argument("--composition-csv", type=Path, required=True)
    ap.add_argument("--profile-csv", type=Path, required=True)
    ap.add_argument("--provenance-json", type=Path, required=True)
    args = ap.parse_args()

    trows = read_csv(args.temperature_csv)
    crows = read_csv(args.composition_csv)
    tr = np.array([float(x["r_km"]) for x in trows])
    tv = np.array([float(x["value"]) for x in trows])
    if np.any(np.diff(tr) <= 0.0):
        raise ValueError("temperature vertices must be strictly increasing in radius")
    crows = sorted(crows, key=lambda x: float(x["r_km"]))
    selected = [x for x in crows if float(x["r_km"]) in RADII_KM]
    if [float(x["r_km"]) for x in selected] != list(RADII_KM):
        raise ValueError("composition key-radius CSV does not contain the exact 1--15 km set")

    rows = []
    for x in selected:
        r = float(x["r_km"])
        if r < tr[0] or r > tr[-1]:
            raise ValueError(f"temperature interpolation would extrapolate at r={r}")
        nB_over_n0 = float(x["nB_over_n0"])
        Yn = float(x["Yn"])
        Yp = float(x["Yp"])
        Yp_tot = float(x["Ye_plus_Ymu"])
        Xcluster = float(x["Xcluster"])
        Ycluster_charge = float(x["Ycluster_charge"])
        if abs(Yn + Yp + Xcluster - 1.0) > 5e-5:
            raise ValueError(f"Caputo baryon composition fails closure at r={r}")
        if abs(Ycluster_charge - (Yp_tot - Yp)) > 5e-5:
            raise ValueError(f"Caputo cluster charge fails closure at r={r}")
        rows.append({
            "r_km": r,
            "T_MeV": float(np.interp(r, tr, tv)),
            "nB_over_n0": nB_over_n0,
            "nB_fm3": nB_over_n0 * N0_CAPUTO_FM3,
            "Yn_free": Yn,
            "Yp_free": Yp,
            "Yp_tot": Yp_tot,
            "Xcluster": Xcluster,
            "Ycluster_charge": Ycluster_charge,
        })

    args.profile_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.profile_csv.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({
                key: (f"{value:.12g}" if isinstance(value, float) else value)
                for key, value in row.items()
            })

    provenance = {
        "source": "Caputo, Raffelt, Vitagliano, arXiv:2109.03244v3",
        "temperature_source": "Fig. 1 upper-panel T(r), linearly interpolated in radius",
        "composition_source": "Fig. 1 lower-panel nB and Fig. 4 upper-panel Yn,Yp,Ye+Ymu",
        "temperature_csv": str(args.temperature_csv),
        "temperature_csv_sha256": sha256(args.temperature_csv),
        "composition_key_radii_csv": str(args.composition_csv),
        "composition_key_radii_csv_sha256": sha256(args.composition_csv),
        "normalization_n0_fm3": N0_CAPUTO_FM3,
        "EOS_coordinate": "Yp_tot=Ye+Ymu; free-proton abundance Yp is not the EOS coordinate",
        "selected_radii_km": list(RADII_KM),
        "profile_csv_sha256": sha256(args.profile_csv),
    }
    args.provenance_json.parent.mkdir(parents=True, exist_ok=True)
    args.provenance_json.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(provenance, indent=2))

if __name__ == "__main__":
    main()
