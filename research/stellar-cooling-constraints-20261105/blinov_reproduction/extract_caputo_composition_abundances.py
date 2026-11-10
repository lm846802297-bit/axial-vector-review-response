#!/usr/bin/env python3
"""Extract Caputo Fig. 1 densities and Fig. 4 abundances from arXiv:2109.03244v3.

The script reads the original vector paths from the checksum-pinned source PDFs.
It reconstructs free neutrons from Yn*nB; it never substitutes nB-np for n_n.
"""
from __future__ import annotations
import argparse, hashlib, json, tarfile
from pathlib import Path
import numpy as np
import pandas as pd
import pymupdf

ARCHIVE_SHA256 = "2e4a1280460bce9a5f7596d3dfd1d3e0f4752f2e1706e85d3a2c20b5f9dbbd8e"
PDF_SHA256 = {
    "figures/SNProfile.pdf": "19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e",
    "figures/ScreeningPlot.pdf": "39d66c37dd67d73fbe1b3afe2f5e2a532e0e040e9d220e66ec389abb5daf17ab",
}

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def read_member(archive: Path, name: str) -> bytes:
    with tarfile.open(archive, "r:gz") as tf:
        member = tf.extractfile(name)
        if member is None:
            raise FileNotFoundError(name)
        return member.read()

def read_vector_curve(doc, path_index, x0, x1, y0, y1, rmax, ymap):
    if len(doc) != 1:
        raise ValueError(f"Expected one-page PDF, got {len(doc)} pages")
    drawings = doc[0].get_drawings()
    d = drawings[path_index]
    pts = []
    for item in d["items"]:
        if item[0] != "l":
            continue
        for point in (item[1], item[2]):
            if x0-1e-6 <= point.x <= x1+1e-6 and y0-1e-6 <= point.y <= y1+1e-6:
                pts.append((point.x, point.y))
    if not pts:
        raise ValueError(f"No in-frame vertices for PDF path {path_index}")
    a = np.asarray(pts, dtype=float)
    a = a[np.argsort(a[:, 0], kind="stable")]
    v = pd.DataFrame(a, columns=["x_pt", "y_pt"]).groupby("x_pt", as_index=False).mean()
    return pd.DataFrame({
        "r_km": (v.x_pt.to_numpy()-x0)*rmax/(x1-x0),
        "value": ymap(v.y_pt.to_numpy()),
    })

def interp(frame, radius):
    f = frame.sort_values("r_km")
    return np.interp(radius, f.r_km, f.value, left=np.nan, right=np.nan)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source_archive", type=Path)
    ap.add_argument("--outdir", type=Path, default=Path("outputs"))
    ap.add_argument("--step-km", type=float, default=0.05)
    args = ap.parse_args()

    archive_sha = digest(args.source_archive.read_bytes())
    if archive_sha != ARCHIVE_SHA256:
        raise ValueError(f"Unexpected archive SHA-256: {archive_sha}")
    pdf = {name: read_member(args.source_archive, name) for name in PDF_SHA256}
    pdf_sha = {name: digest(data) for name, data in pdf.items()}
    for name, expected in PDF_SHA256.items():
        if pdf_sha[name] != expected:
            raise ValueError(f"Unexpected SHA-256 for {name}: {pdf_sha[name]}")

    # Caputo Fig. 1 lower panel: nB, np, ne, nmu, normalized to n0=0.181 fm^-3.
    sn = pymupdf.open(stream=pdf["figures/SNProfile.pdf"], filetype="pdf")
    dens_axis = (47.52, 324.0, 235.559, 442.922, 20.0)
    dens_map = lambda y: 10.0**(-4.0 + (442.918-y)/41.4718)
    dens_paths = {"nB_over_n0":158, "np_over_n0":159, "ne_over_n0":160, "nmu_over_n0":161}
    dens = {
        k: read_vector_curve(sn, i, *dens_axis, dens_map)
        for k, i in dens_paths.items()
    }

    # Caputo Fig. 4 upper panel: Yp (orange), 1-Yn (blue), Ye+Ymu (green).
    comp = pymupdf.open(stream=pdf["figures/ScreeningPlot.pdf"], filetype="pdf")
    comp_axis = (47.52, 324.0, 8.199, 215.559, 40.0)
    comp_map = lambda y: 0.6-(y-8.199)*0.6/(215.559-8.199)
    comp_paths = {"Yp":0, "one_minus_Yn":1, "Ye_plus_Ymu":2}
    abund = {
        k: read_vector_curve(comp, i, *comp_axis, comp_map)
        for k, i in comp_paths.items()
    }

    rmin = max(v.r_km.min() for v in [*dens.values(), *abund.values()])
    rmax = min(15.2, *(v.r_km.max() for v in [*dens.values(), *abund.values()]))
    r = np.arange(max(0.2, rmin), rmax+args.step_km/2, args.step_km)
    nB, np1, ne, nmu = [interp(dens[k], r) for k in
                        ("nB_over_n0","np_over_n0","ne_over_n0","nmu_over_n0")]
    Yp, one_minus_Yn, Yell = [interp(abund[k], r) for k in
                              ("Yp","one_minus_Yn","Ye_plus_Ymu")]
    Yn = 1.0-one_minus_Yn
    Xcl = one_minus_Yn-Yp
    Qcl = Yell-Yp
    ZA = np.divide(Qcl, Xcl, out=np.full_like(Xcl, np.nan), where=Xcl>1e-4)
    Yp_f1 = np1/nB
    Yell_f1 = (ne+nmu)/nB
    nn_free = Yn*nB
    np_free = Yp*nB

    result = pd.DataFrame({
        "r_km":r, "nB_over_n0":nB, "nn_free_over_n0":nn_free,
        "np_free_over_n0":np_free, "np_fig1_over_n0":np1,
        "ne_over_n0":ne, "nmu_over_n0":nmu, "Yn":Yn, "Yp":Yp,
        "Ye_plus_Ymu":Yell, "Xcluster":Xcl, "Ycluster_charge":Qcl,
        "ZoverA_eff":ZA, "Yp_fig1":Yp_f1, "Yell_fig1":Yell_f1,
        "Yp_fig1_rel_diff":(Yp_f1-Yp)/Yp,
        "Yell_fig1_rel_diff":(Yell_f1-Yell)/Yell,
    })

    def rel_metrics(x):
        x = np.asarray(x)
        return {"rms_relative":float(np.sqrt(np.mean(x*x))),
                "max_abs_relative":float(np.max(np.abs(x)))}
    q1, q4 = Yell_f1-Yp_f1, Qcl
    summary = {
        "source_archive_sha256":archive_sha, "pdf_sha256":pdf_sha,
        "fig1_density_paths":dens_paths, "fig4_abundance_paths":comp_paths,
        "fig1_vertices":{k:int(len(v)) for k,v in dens.items()},
        "fig4_vertices":{k:int(len(v)) for k,v in abund.items()},
        "cross_figure_validation":{
            "Yp_Fig4_vs_np_over_nB_Fig1":rel_metrics((Yp_f1-Yp)/Yp),
            "Ye_plus_Ymu_Fig4_vs_(ne+nmu)_over_nB_Fig1":rel_metrics((Yell_f1-Yell)/Yell),
            "cluster_charge_absolute_difference":{
                "rms":float(np.sqrt(np.mean((q1-q4)**2))),
                "max_abs":float(np.max(np.abs(q1-q4))),
            },
        },
        "definitions":{
            "Yn":"free-neutron abundance per baryon",
            "Yp":"free-proton abundance per baryon",
            "Xcluster":"1-Yn-Yp, total baryon mass fraction in nuclei/clusters",
            "Ycluster_charge":"Ye+Ymu-Yp, cluster positive charge per baryon",
            "warning":"Do not infer n_n_free=nB-n_p_free; use n_n_free=Yn*nB.",
        },
        "r_grid_km":[float(r[0]),float(r[-1])],
        "step_km":args.step_km,
    }
    args.outdir.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.outdir/"caputo_composition_profiles_2026-11-11.csv", index=False)
    (args.outdir/"caputo_composition_closure_2026-11-11.json").write_text(
        json.dumps(summary, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
