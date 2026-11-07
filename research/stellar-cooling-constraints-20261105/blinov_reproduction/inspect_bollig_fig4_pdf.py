#!/usr/bin/env python3
"""Inspect Bollig et al. arXiv v7 PDF vector paths for Fig. 4 (muon degeneracy).

This extracts only public-paper figure geometry, not simulation data.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import pymupdf

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
    result={
        "title":"Bollig et al. Fig. 4 public-PDF vector-path inventory",
        "source":"https://arxiv.org/pdf/2005.07141v7",
        "pdf_sha256":hashlib.sha256(raw).hexdigest(),
        "page_index":2,
        "page_rect":[float(page.rect.x0),float(page.rect.y0),float(page.rect.x1),float(page.rect.y1)],
        "drawing_count":len(rows),
        "drawings":rows,
        "limitations":["PDF paths are public figure geometry, not original simulation samples.",
                       "Curve-to-model identity requires color/legend and axis calibration checks."],
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"pdf_sha256":result["pdf_sha256"],"drawing_count":len(rows),
                      "output":str(a.output)},indent=2))
if __name__=="__main__": main()
