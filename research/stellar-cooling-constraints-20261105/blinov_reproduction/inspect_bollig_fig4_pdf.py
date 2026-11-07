#!/usr/bin/env python3
"""Inspect Bollig et al. arXiv v7 PDF vector paths for Fig. 4 (muon degeneracy).

This extracts only public-paper figure geometry, not simulation data.
"""
from __future__ import annotations
import argparse, csv, hashlib, json
from pathlib import Path
import pymupdf\nimport numpy as np

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--pdf",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    raw=a.pdf.read_bytes()
    doc=pymupdf.open(stream=raw,filetype="pdf")
    page=doc[2]  # printed page 3, Fig. 3 and Fig. 4
    rows=[]
    for i,d in enumerate(page.get_drawings()):
        items=d.get("items",[])
        pts=[]
        kinds={}
        for item in items:
            kinds[item[0]]=kinds.get(item[0],0)+1
            for v in item[1:]:
                if hasattr(v,"x") and hasattr(v,"y"):
                    pts.append([float(v.x),float(v.y)])
                elif isinstance(v,(tuple,list)) and len(v)>=2 and all(isinstance(z,(int,float)) for z in v[:2]):
                    pts.append([float(v[0]),float(v[1])])
        rect=d.get("rect")
        rows.append({
            "index":i,
            "rect":[float(rect.x0),float(rect.y0),float(rect.x1),float(rect.y1)] if rect else None,
            "color":list(d["color"]) if d.get("color") else None,
            "fill":list(d["fill"]) if d.get("fill") else None,
            "width":float(d["width"]) if d.get("width") is not None else None,
            "closePath":bool(d.get("closePath")),
            "item_count":len(items),
            "item_kinds":kinds,
            "point_count":len(pts),
            "first_points":pts[:4],
            "last_points":pts[-4:] if pts else [],
        })
    # Fig. 4, yellow SFHo-18.8 curve. The color and legend are cross-checked
    # against the published figure. Axes are calibrated from PDF tick paths:
    # r=5,10,15,20 km at x=390.4282,443.4384,496.4469,549.4571;
    # mu_mu/T=+2,0,-2,-4 at y=187.6936,208.4416,229.1909,249.9405.
    curve_index = 193
    drawing = page.get_drawings()[curve_index]
    color = list(drawing["color"]) if drawing.get("color") else None
    if color is None or max(abs(a-b) for a,b in zip(color,[0.7,0.7,0.0])) > 0.01:
        raise ValueError(f"Expected yellow SFHo-18.8 curve at path 193, got {color}")
    points=[]
    for item in drawing["items"]:
        if item[0] != "l":
            raise ValueError(f"Unexpected non-line item in Fig. 4 path: {item[0]}")
        points.extend([[float(item[1].x),float(item[1].y)],
                       [float(item[2].x),float(item[2].y)]])
    pnts=np.asarray(points,dtype=float)
    pnts=pnts[np.argsort(pnts[:,0],kind="stable")]
    _,keep=np.unique(pnts[:,0],return_index=True)
    pnts=pnts[keep]
    x0,x20=348.020751953125,549.4570922851562
    y0,y2=208.44161987304688,187.69357299804688
    radius=1.0+(pnts[:,0]-x0)*19.0/(x20-x0)
    degeneracy=(y0-pnts[:,1])*2.0/(y0-y2)
    curve=np.column_stack([radius,degeneracy])
    csv_path=a.output.with_name("bollig_fig4_sfho188_muon_degeneracy.csv")
    csv_path.parent.mkdir(parents=True,exist_ok=True)
    np.savetxt(csv_path,curve,delimiter=",",header="r_km,mu_mu_over_T",comments="",fmt="%.10g")
    samples=[]
    for r in [1,5,8,10,12,15,18,20]:
        b=float(np.interp(r,radius,degeneracy))
        samples.append({"r_km":r,"bollig_fig4_mu_mu_over_T":b})
    result={
        "title":"Bollig et al. Fig. 4 public-PDF vector-path audit",
        "source":"https://arxiv.org/pdf/2005.07141v7",
        "pdf_sha256":hashlib.sha256(raw).hexdigest(),
        "page_index":2,
        "page_rect":[float(page.rect.x0),float(page.rect.y0),float(page.rect.x1),float(page.rect.y1)],
        "drawing_count":len(rows),
        "fig4_curve":{"drawing_index":curve_index,"rgb":color,"path_segments":len(drawing["items"]),
                      "deduplicated_vertices":len(curve),"line_width_pdf_points":float(drawing["width"]),
                      "radius_calibration":{"r1_x":x0,"r20_x":x20},
                      "degeneracy_calibration":{"mu_over_T_plus2_y":y2,"mu_over_T_zero_y":y0,
                                                "mu_over_T_minus2_y":229.1908721923828,
                                                "mu_over_T_minus4_y":249.9405059814453},
                      "samples":samples,"csv":str(csv_path.name)},
        "drawings":rows,
        "limitations":["PDF paths are public figure geometry, not original simulation samples.",
                       "The digitized line is the SFHo-18.8 yellow curve, identified from the legend.",
                       "The curve is a published plotting output; it is not a substitute for the original simulation table."],
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"pdf_sha256":result["pdf_sha256"],"drawing_count":len(rows),
                      "output":str(a.output)},indent=2))
if __name__=="__main__": main()
