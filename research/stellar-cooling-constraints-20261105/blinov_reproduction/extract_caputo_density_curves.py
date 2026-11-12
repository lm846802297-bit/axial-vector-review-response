#!/usr/bin/env python3
"""Extract Caputo Fig. 1 lower-panel density curves from arXiv source PDF."""
from __future__ import annotations
import argparse, csv, hashlib, json, tarfile
from pathlib import Path
import numpy as np
import pymupdf

EXPECTED_PDF_SHA256 = "19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e"
ARCHIVE_MEMBER = "figures/SNProfile.pdf"
PATHS = {
    "nB_over_n0": (158, "#0000FF"),
    "np_over_n0": (159, "#FF0000"),
    "ne_over_n0": (160, "#FF00FF"),
    "nmu_over_n0": (161, "#00AA00"),
}
X0_PT, X20_PT = 47.52, 324.0
Y_AT_1E4_PT, DECADE_PT = 442.918, 41.4718

def vertices(drawing):
    pts=[]
    for item in drawing["items"]:
        if item[0] != "l":
            raise ValueError(f"Expected line segment, got {item[0]!r}")
        pts.extend([tuple(item[1]), tuple(item[2])])
    pts=np.asarray(pts,dtype=float)
    pts=pts[np.argsort(pts[:,0],kind="stable")]
    _,keep=np.unique(pts[:,0],return_index=True)
    return pts[keep]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source",type=Path,help="arXiv source tar.gz or extracted SNProfile.pdf")
    ap.add_argument("--outdir",type=Path,default=Path("outputs"))
    args=ap.parse_args()
    if args.source.name.endswith(".tar.gz"):
        with tarfile.open(args.source,"r:gz") as tf:
            member=tf.extractfile(ARCHIVE_MEMBER)
            if member is None: raise FileNotFoundError(ARCHIVE_MEMBER)
            pdf=member.read()
        archive_sha=hashlib.sha256(args.source.read_bytes()).hexdigest()
    else:
        pdf=args.source.read_bytes()
        archive_sha=None
    pdf_sha=hashlib.sha256(pdf).hexdigest()
    if pdf_sha != EXPECTED_PDF_SHA256:
        raise ValueError(f"Unexpected source PDF SHA-256: {pdf_sha}")
    doc=pymupdf.open(stream=pdf,filetype="pdf")
    if len(doc)!=1: raise ValueError(f"Expected one-page PDF, got {len(doc)}")
    drawings=doc[0].get_drawings()
    args.outdir.mkdir(parents=True,exist_ok=True)
    rows=[]; meta={}
    for label,(idx,color) in PATHS.items():
        d=drawings[idx]; v=vertices(d)
        r=(v[:,0]-X0_PT)*20.0/(X20_PT-X0_PT)
        n=10.0**(-4.0+(Y_AT_1E4_PT-v[:,1])/DECADE_PT)
        for (x,y),rr,nn in zip(v,r,n):
            rows.append({"curve":label,"path_index":idx,"pdf_x_pt":f"{x:.9f}",
              "pdf_y_pt":f"{y:.9f}","r_km":f"{rr:.12g}","n_over_n0":f"{nn:.12g}",
              "inside_plotted_x_range":str(rr<=20.0+1e-9).lower()})
        meta[label]={"path_index":idx,"stroke_rgb":list(d["color"]),"color_hex":color,
          "unique_vertices":len(v),"r_range_km":[float(r.min()),float(r.max())],
          "n_over_n0_range":[float(n.min()),float(n.max())],
          "off_plot_vertices":int(np.count_nonzero(r>20.0))}
    out=args.outdir/"caputo_density_curves_vertices_2026-11-11.csv"
    with out.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    record={"source":"Caputo, Raffelt, Vitagliano, arXiv:2109.03244v3, Fig. 1 lower panel",
      "source_archive_sha256":archive_sha,"source_pdf_member":ARCHIVE_MEMBER,
      "source_pdf_sha256":pdf_sha,"normalization_n0_fm3":0.181,
      "coordinate_transform":{"radius_km":"(x_pt-47.52)*20/(324.0-47.52)",
      "density":"10**(-4+(442.918-y_pt)/41.4718)","visible_radius_range_km":[0,20]},
      "vector_paths":meta,"caveats":[
      "These are digitized public-figure curves, not raw Garching simulation tables.",
      "The nB path has 47 vertices beyond the visible 0-20 km frame; they are flagged and must not be used as plotted data or physical extrapolation.",
      "Do not identify n_B-n_p as free-neutron density or n_p as free-proton density without composition closure."]}
    (args.outdir/"caputo_density_curve_provenance_2026-11-11.json").write_text(
      json.dumps(record,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"pdf_sha256":pdf_sha,"archive_sha256":archive_sha,
      "rows":len(rows),"paths":meta},indent=2))
if __name__=="__main__": main()
