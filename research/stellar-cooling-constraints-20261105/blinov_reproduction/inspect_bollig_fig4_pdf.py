#!/usr/bin/env python3
"""Inspect Bollig et al. arXiv v7 PDF vector paths for Fig. 4 (muon degeneracy).

This extracts only public-paper figure geometry, not simulation data.
"""
from __future__ import annotations
import argparse, csv, hashlib, json
from pathlib import Path
import pymupdf
import numpy as np

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
    y0,y2=236.10794067382812,208.44161987304688
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
    # Fig. 3, yellow SFHo-18.8 muon number-density curve. The axis is
    # logarithmic in n_mu [fm^-3], with major ticks 1e-7,...,1e-2 and a
    # top frame at 1e-1. The x axis is linear from 0 to 20 km.
    fig3_curve_index = 33
    fig3 = page.get_drawings()[fig3_curve_index]
    fig3_color = list(fig3["color"]) if fig3.get("color") else None
    if fig3_color is None or max(abs(a-b) for a,b in zip(fig3_color,[0.7,0.7,0.0])) > 0.01:
        raise ValueError(f"Expected yellow SFHo-18.8 Fig. 3 curve at path 33, got {fig3_color}")
    fig3_points=[]
    for item in fig3["items"]:
        if item[0] != "l":
            raise ValueError(f"Unexpected non-line item in Fig. 3 path: {item[0]}")
        fig3_points.extend([[float(item[1].x),float(item[1].y)],
                            [float(item[2].x),float(item[2].y)]])
    p3=np.asarray(fig3_points,dtype=float)
    p3=p3[(p3[:,0]>=95.28073120117188)&(p3[:,0]<=286.44146728515625)]
    p3=p3[np.argsort(p3[:,0],kind="stable")]
    _,keep3=np.unique(p3[:,0],return_index=True)
    p3=p3[keep3]
    r3=(p3[:,0]-95.28073120117188)*20.0/(286.44146728515625-95.28073120117188)
    logn3=-7.0+(285.0899658203125-p3[:,1])*6.0/(285.0899658203125-166.94435119628906)
    n3=10.0**logn3
    curve3=np.column_stack([r3,n3])
    fig3_csv=a.output.with_name("bollig_fig3_sfho188_muon_density.csv")
    np.savetxt(fig3_csv,curve3,delimiter=",",header="r_km,n_mu_fm3",comments="",fmt="%.10g")
    fig3_samples=[]
    for rr in [1,5,8,10,12,15,18,20]:
        if rr>=r3[0] and rr<=r3[-1]:
            fig3_samples.append({"r_km":rr,"bollig_fig3_n_mu_fm3":float(np.interp(rr,r3,n3))})
    fig3_result={
        "drawing_index":fig3_curve_index,"rgb":fig3_color,
        "path_segments":len(fig3["items"]),"deduplicated_visible_vertices":len(curve3),
        "line_width_pdf_points":float(fig3["width"]),
        "radius_calibration":{"r0_x":95.28073120117188,"r20_x":286.44146728515625},
        "density_calibration":{"n_1e-7_y":285.0899658203125,
                               "n_1e-2_y":186.6345672607422,
                               "n_1e-1_top_frame_y":166.94435119628906},
        "samples":fig3_samples,"csv":fig3_csv.name
    }

    text_spans=[]
    for block in page.get_text("dict").get("blocks",[]):
        for line in block.get("lines",[]):
            for span in line.get("spans",[]):
                bbox=span.get("bbox",[0,0,0,0])
                if bbox[0]>300 and bbox[2]<610 and bbox[1]>145 and bbox[3]<330:
                    text_spans.append({"text":span.get("text",""),
                                       "bbox":[float(v) for v in bbox]})
    result={
        "title":"Bollig et al. Fig. 4 public-PDF vector-path audit",
        "source":"https://arxiv.org/pdf/2005.07141v7",
        "pdf_sha256":hashlib.sha256(raw).hexdigest(),
        "page_index":2,
        "page_rect":[float(page.rect.x0),float(page.rect.y0),float(page.rect.x1),float(page.rect.y1)],
        "drawing_count":len(rows),
        "fig3_curve":fig3_result,
        "fig4_curve":{"drawing_index":curve_index,"rgb":color,"path_segments":len(drawing["items"]),
                      "deduplicated_vertices":len(curve),"line_width_pdf_points":float(drawing["width"]),
                      "radius_calibration":{"r1_x":x0,"r20_x":x20},
                      "degeneracy_calibration":{"mu_over_T_plus2_y":y2,"mu_over_T_zero_y":y0,
                                                "mu_over_T_minus2_y":229.1908721923828,
                                                "mu_over_T_minus4_y":249.9405059814453},
                      "samples":samples,"csv":str(csv_path.name)},
        "drawings":rows,
        "text_spans":text_spans,
        "limitations":["PDF paths are public figure geometry, not original simulation samples.",
                       "The digitized line is the SFHo-18.8 yellow curve, identified from the legend.",
                       "The curve is a published plotting output; it is not a substitute for the original simulation table."],
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"pdf_sha256":result["pdf_sha256"],"drawing_count":len(rows),
                      "output":str(a.output)},indent=2))
if __name__=="__main__": main()
