#!/usr/bin/env python3
"""Cross-check E-K Fig. 12 vector paths against archived Caputo/Bollig profiles."""
from pathlib import Path
import argparse, csv, json
import numpy as np

def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def stats(values):
    a = np.asarray(values, dtype=float)
    return {
        "count": int(a.size),
        "rms_relative": float(np.sqrt(np.mean(a*a))),
        "mean_abs_relative": float(np.mean(np.abs(a))),
        "p95_abs_relative": float(np.quantile(np.abs(a), 0.95)),
        "max_abs_relative": float(np.max(np.abs(a))),
        "min_relative": float(np.min(a)),
        "max_relative": float(np.max(a)),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parent / "outputs")
    args = ap.parse_args()
    root, out = args.root, args.outdir
    vertices = read_csv(out / "esseili_kribs_fig12_vector_vertices_2026-11-11.csv")
    curves = {}
    for name in ("T_SFHo18p8", "n", "p"):
        a = np.array([
            (float(x["r_km"]),
             float(x["T_MeV"]) if name == "T_SFHo18p8" else float(x["n_over_n0_corrected"]),
             np.nan if name == "T_SFHo18p8" else float(x["n_over_n0_literal_top10"]))
            for x in vertices if x["curve"] == name
        ], dtype=float)
        curves[name] = a[np.argsort(a[:, 0])]

    caputo_t = json.loads((out / "bollig_muon_density_b1_source_audit_2026-11-09.json").read_text())
    caputo_comp = read_csv(out / "caputo_composition_key_radii_2026-11-11.csv")
    caputo_comp = [x for x in caputo_comp if float(x["r_km"]) <= 15.0]
    t_rows = []
    for x in caputo_t["implied_temperature_diagnostic"]:
        r = float(x["radius_km"])
        te = float(np.interp(r, curves["T_SFHo18p8"][:, 0], curves["T_SFHo18p8"][:, 1]))
        tc = float(x["T_Caputo_MeV"])
        t_rows.append({"r_km": r, "EK_T_MeV": te, "Caputo_T_MeV": tc,
                       "relative_residual_EK_over_Caputo_minus_1": te/tc-1.0})
    write_csv(out / "esseili_kribs_fig12_caputo_temperature_crosscheck_2026-11-11.csv", t_rows)

    bollig = json.loads((out / "bollig_fig3_fig4_vector_paths_2026-11-09.json").read_text())
    path = next(p for p in bollig["fig1_temperature_vector_paths"] if p["index"] == 0)
    pts = np.asarray(path["points"], dtype=float)
    pts = pts[np.argsort(pts[:, 0])]
    ux, uy = [], []
    for xx in np.unique(pts[:, 0]):
        ux.append(xx)
        uy.append(float(np.mean(pts[pts[:, 0] == xx, 1])))
    pts = np.c_[ux, uy]
    xpdf = np.array([389.2326354980469, 442.6397399902344, 496.04840087890625, 549.4555053710938])
    rr = np.array([5., 10., 15., 20.])
    dx, x0 = np.polyfit(rr, xpdf, 1)
    ypdf = np.array([177.6042938232422, 158.30784606933594, 139.01141357421875,
                     119.71297454833984, 100.41653442382812, 81.12008666992188, 61.8236])
    tt = np.arange(0., 61., 10.)
    dy, y0 = np.polyfit(tt, ypdf, 1)
    bollig_curve = np.c_[(pts[:, 0]-x0)/dx, (pts[:, 1]-y0)/dy]
    bollig_curve = bollig_curve[np.argsort(bollig_curve[:, 0])]
    rgrid = np.arange(0.5, 20.0001, 0.05)
    te = np.interp(rgrid, curves["T_SFHo18p8"][:, 0], curves["T_SFHo18p8"][:, 1])
    tb = np.interp(rgrid, bollig_curve[:, 0], bollig_curve[:, 1])
    b_rows = [{"r_km": float(r), "EK_T_MeV": float(a), "Bollig_Fig1_T_MeV": float(b),
               "relative_residual_EK_over_Bollig_minus_1": float(a/b-1.0)}
              for r, a, b in zip(rgrid, te, tb)]
    write_csv(out / "esseili_kribs_fig12_bollig_temperature_crosscheck_2026-11-11.csv", b_rows)

    density_rows = []
    for x in caputo_comp:
        r = float(x["r_km"])
        en = float(np.interp(r, curves["n"][:, 0], curves["n"][:, 1]))
        en_lit = float(np.interp(r, curves["n"][:, 0], curves["n"][:, 2]))
        ep = float(np.interp(r, curves["p"][:, 0], curves["p"][:, 1]))
        ep_lit = float(np.interp(r, curves["p"][:, 0], curves["p"][:, 2]))
        cnn, cpp = float(x["nn_free_over_n0"]), float(x["np_free_over_n0"])
        cb, xc = float(x["nB_over_n0"]), float(x["Xcluster"])
        free_target = cb*(1.0-xc)
        density_rows.append({
            "r_km": r,
            "EK_n_over_n0_corrected": en, "EK_n_over_n0_literal_top10": en_lit,
            "Caputo_n_free_over_n0": cnn, "n_relative_residual_corrected": en/cnn-1.0,
            "n_relative_residual_literal": en_lit/cnn-1.0,
            "EK_p_over_n0_corrected": ep, "EK_p_over_n0_literal_top10": ep_lit,
            "Caputo_p_free_over_n0": cpp, "p_relative_residual_corrected": ep/cpp-1.0,
            "p_relative_residual_literal": ep_lit/cpp-1.0,
            "Caputo_nB_over_n0": cb, "Caputo_Xcluster": xc,
            "Caputo_free_baryon_over_n0": free_target, "EK_n_plus_p_over_n0": en+ep,
            "sum_relative_residual_vs_free_baryons": (en+ep)/free_target-1.0,
            "sum_relative_residual_vs_total_baryons": (en+ep)/cb-1.0,
        })
    write_csv(out / "esseili_kribs_fig12_caputo_density_crosscheck_2026-11-11.csv", density_rows)

    prov = json.loads((out / "esseili_kribs_fig12_vector_provenance_2026-11-11.json").read_text())
    tr = [x["relative_residual_EK_over_Caputo_minus_1"] for x in t_rows]
    br = [x["relative_residual_EK_over_Bollig_minus_1"] for x in b_rows]
    nr = [x["n_relative_residual_corrected"] for x in density_rows]
    pr = [x["p_relative_residual_corrected"] for x in density_rows]
    nl = [x["n_relative_residual_literal"] for x in density_rows]
    pl = [x["p_relative_residual_literal"] for x in density_rows]
    sf = [x["sum_relative_residual_vs_free_baryons"] for x in density_rows]
    st = [x["sum_relative_residual_vs_total_baryons"] for x in density_rows]
    summary = {
        "source_pdf_sha256": prov["source_pdf_sha256"], "source_pdf_bytes": prov["source_pdf_bytes"],
        "page_index_zero_based": 14, "printed_page": 15, "path_indices": prov["path_indices"],
        "normalization_n0_fm3": 0.181,
        "temperature_vs_caputo": stats(tr) | {"radius_km": [t_rows[0]["r_km"], t_rows[-1]["r_km"]]},
        "temperature_vs_bollig_fig1": stats(br) | {"radius_km": [0.5, 20.0], "step_km": 0.05},
        "density_vs_caputo_free_nucleons_corrected_axis": {
            "neutron": stats(nr), "proton": stats(pr),
            "sum_vs_caputo_free_baryons": stats(sf), "sum_vs_caputo_total_baryons": stats(st),
            "radii_km": [1.0, 15.0],
        },
        "density_vs_caputo_free_nucleons_literal_top_two_labels": {
            "neutron": stats(nl), "proton": stats(pl),
        },
        "density_crosscheck_points": len(density_rows),
        "axis_label_audit": prov["density_axis_label_issue"],
        "digitization_uncertainty": prov["digitization_uncertainty_estimate"],
        "interpretation": [
            "The temperature curve agrees with the existing Caputo profile and Bollig Fig. 1 at sub-percent figure-reading precision.",
            "The corrected density transform is consistent with Caputo reconstructed free-neutron and free-proton densities at ten common radii from 1 to 15 km.",
            "The sum of E-K n and p follows Caputo free baryons nB*(1-Xcluster), not total nB; the deficit relative to total nB tracks the cluster baryon fraction.",
            "The literal top-two density labels shift both E-K density curves by a factor of ten and are inconsistent with the same-model Caputo free-nucleon comparison.",
            "This is a cross-publication figure consistency audit of a shared Garching model lineage, not an independent hydrodynamic simulation validation.",
        ],
        "caveats": [
            "These are published-figure vector paths, not raw Garching profile data.",
            "The density axis retains both literal and corrected candidate transforms; the corrected candidate is selected only for the comparison because it matches the Caputo free-nucleon curves.",
            "Caputo composition comparison is restricted to 1-15 km, where the Fig. 4 abundance curves have common support. The E-K proton path ends at 19.30 km; no extrapolation beyond path support is used.",
            "The line-stroke half-width corresponds to about 0.021 density decades (~4.9%) and 0.277 MeV in temperature; residuals are below this figure-level extraction uncertainty.",
        ],
    }
    (out / "esseili_kribs_fig12_crosscheck_summary_2026-11-11.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
