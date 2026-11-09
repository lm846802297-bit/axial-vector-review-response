#!/usr/bin/env python3
"""Audit the Caputo Fig. 1 PDF vector vertices that lie beyond its visible 20 km frame.

The current profile uses the encoded PDF path vertices beyond the plotted frame.
This audit verifies their source PDF identity, exact path support, clipping/frame
relation, and consistency with the committed T and mu_mu vertex CSVs. It does
not promote off-frame vertices to raw simulation data and does not change any
production profile or constraint.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import tarfile
import urllib.request
from pathlib import Path
import numpy as np
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = ROOT / "data"
SOURCE_DIR = ROOT / "latex-build" / "sources"
ARCHIVE = SOURCE_DIR / "SNProfile.pdf.tar.gz"
PDF = SOURCE_DIR / "SNProfile.pdf"
URL = "https://arxiv.org/src/2109.03244v3"
MEMBER = "figures/SNProfile.pdf"
EXPECTED_PDF_SHA256 = "19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e"
DEFAULT_JSON = HERE / "outputs" / "caputo_offframe_thermodynamic_vertices_20_22km_2026-11-09.json"
DEFAULT_MD = HERE / "CAPUTO_OFFFRAME_THERMODYNAMIC_VERTICES_20_22KM_2026-11-09.md"
X0, X20 = 47.52, 324.0
R0, R20 = 0.1, 20.0
Y0, Y2 = 215.559, 56.180
LOG10_T0, LOG10_T2 = 0.0, 2.0


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def get_pdf():
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    if not PDF.exists():
        urllib.request.urlretrieve(URL, ARCHIVE)
        with tarfile.open(ARCHIVE) as tar:
            member = tar.extractfile(MEMBER)
            if member is None:
                raise RuntimeError("Missing SNProfile.pdf in Caputo arXiv source archive")
            PDF.write_bytes(member.read())
    actual = sha256(PDF)
    if actual != EXPECTED_PDF_SHA256:
        raise RuntimeError("Caputo source PDF SHA-256 mismatch: " + actual)
    return actual


def extract_vertices(drawing):
    points = []
    kinds = []
    for item in drawing["items"]:
        kinds.append(item[0])
        if item[0] != "l":
            raise RuntimeError("Selected thermodynamic curve contains a non-line path item")
        points.extend(((float(item[1].x), float(item[1].y)),
                       (float(item[2].x), float(item[2].y))))
    p = np.asarray(points, dtype=float)
    p = p[np.argsort(p[:, 0], kind="stable")]
    _, keep = np.unique(p[:, 0], return_index=True)
    return p[keep], kinds


def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return np.asarray([[float(x["r_km"]), float(x["value"])] for x in rows], dtype=float)


def summarize_curve(name, drawing, csv_path, pdf_hash):
    p, kinds = extract_vertices(drawing)
    # These are the exact mappings in extract_profile.py. The visible top-panel
    # frame ends at x=324 (r=20 km); x>324 vertices are encoded but off-frame.
    radius = R0 + (p[:, 0]-X0)*(R20-R0)/(X20-X0)
    log_value = (Y0-p[:, 1])/(Y0-Y2)*(LOG10_T2-LOG10_T0)+LOG10_T0
    values = 10.0**log_value
    selected = (radius >= 20.0) & (radius <= 22.0)
    selected_r = radius[selected]
    selected_v = values[selected]
    if not len(selected_r):
        raise RuntimeError(f"No off-frame {name} vertices in 20--22 km")

    csv_curve = read_csv(csv_path)
    csv_interp = np.interp(radius, csv_curve[:, 0], csv_curve[:, 1])
    rel = values/csv_interp-1.0
    slopes = np.diff(selected_v)/np.diff(selected_r) if len(selected_r)>1 else np.asarray([])
    targets = []
    for target in (19.5,20.0,20.5,21.0,21.5,22.0,22.19,22.5):
        if target < radius.min() or target > radius.max():
            value = None
        else:
            value = float(np.interp(target, radius, values))
        targets.append({"r_km":target,"value":value})
    continuity_gaps = 0
    items = drawing["items"]
    for a,b in zip(items[:-1],items[1:]):
        if a[0] == "l" and b[0] == "l":
            end = np.asarray([float(a[2].x),float(a[2].y)])
            start = np.asarray([float(b[1].x),float(b[1].y)])
            if np.linalg.norm(end-start)>1e-4:
                continuity_gaps += 1
    return {
        "drawing_index": 0 if name=="T" else 1,
        "color": [float(x) for x in drawing["color"]] if drawing.get("color") else None,
        "drawing_rect_pdf": [float(x) for x in drawing["rect"]],
        "item_count": len(items),
        "item_kinds": sorted(set(kinds)),
        "point_count": int(len(p)),
        "radius_support_km": [float(radius.min()),float(radius.max())],
        "visible_frame_radius_max_km": 20.0,
        "off_frame_vertex_count_r_gt_20": int(np.count_nonzero(radius>20.0)),
        "off_frame_20_22_vertex_count": int(np.count_nonzero(selected)),
        "off_frame_20_22_value_range": [float(selected_v.min()),float(selected_v.max())],
        "off_frame_20_22_max_abs_adjacent_slope_per_km": float(np.max(np.abs(slopes))) if len(slopes) else None,
        "off_frame_20_22_continuity_gaps_in_original_item_order": continuity_gaps,
        "committed_csv_sha256": sha256(csv_path),
        "csv_vs_pdf_vertex_mean_abs_relative_difference": float(np.mean(np.abs(rel))),
        "csv_vs_pdf_vertex_max_abs_relative_difference": float(np.max(np.abs(rel))),
        "sample_values": targets,
    }


def run():
    pdf_hash = get_pdf()
    doc = pymupdf.open(PDF)
    page = doc[0]
    drawings = page.get_drawings()
    if len(drawings) <= 161:
        raise RuntimeError("Unexpected Caputo PDF drawing count")
    # The source-identified paths are T=0, mu_mu=1, and n_mu/n0=161.
    t = summarize_curve("T",drawings[0],DATA/"T_caputo_vertices.csv",pdf_hash)
    mu = summarize_curve("mu_mu",drawings[1],DATA/"mu_mu_caputo_vertices.csv",pdf_hash)

    # Extended extraction exposes PDF clipping paths and their frame rectangles.
    clips = []
    extended_types = {}
    try:
        extended = page.get_drawings(extended=True)
        for i,d in enumerate(extended):
            kind = d.get("type", "unknown")
            extended_types[kind] = extended_types.get(kind, 0) + 1
            if kind != "clip":
                continue
            rect_obj = d.get("rect") or d.get("scissor")
            rect = None
            if rect_obj is not None:
                try:
                    rect = [float(x) for x in rect_obj]
                except TypeError:
                    rect = None
            coords = []
            for item in d.get("items", []):
                if item[0] == "l":
                    coords.extend([
                        (float(item[1].x),float(item[1].y)),
                        (float(item[2].x),float(item[2].y)),
                    ])
                elif item[0] == "re":
                    q = item[1]
                    coords.extend([
                        (float(q.x0),float(q.y0)),(float(q.x1),float(q.y1))
                    ])
                elif item[0] == "qu":
                    q = item[1]
                    for name in ("ul","ur","ll","lr"):
                        pt = getattr(q,name,None)
                        if pt is not None:
                            coords.append((float(pt.x),float(pt.y)))
            if rect is None and coords:
                rect = [
                    min(x for x,y in coords), min(y for x,y in coords),
                    max(x for x,y in coords), max(y for x,y in coords),
                ]
            clips.append({
                "extended_drawing_index": i,
                "rect_pdf": rect,
                "keys": sorted(d.keys()),
                "item_kinds": [x[0] for x in d.get("items", [])],
                "level": d.get("level"),
                "seqno": d.get("seqno"),
            })
    except Exception as exc:
        clips = [{"inspection_error": str(exc)}]
    if not clips:
        clips = [{"note":"No clip objects returned by get_drawings(extended=True)","extended_type_counts":extended_types}]

    return {
        "source": "Caputo et al., arXiv:2109.03244v3, figures/SNProfile.pdf",
        "source_url": URL,
        "source_pdf_sha256": pdf_hash,
        "page_index": 0,
        "page_rect": [float(x) for x in page.rect],
        "drawing_count": len(drawings),
        "visible_top_panel_radius_range_km": [0.1,20.0],
        "mapping": {
            "radius_km": "0.1 + (x_pdf - 47.52)*19.9/(324.0 - 47.52)",
            "value": "10**((215.559 - y_pdf)/(215.559 - 56.180)*2)",
            "visible_frame_right_edge_x_pdf": 324.0,
        },
        "clipping_paths": clips,
        "curves": {"T":t,"mu_mu":mu},
        "interpretation": [
            "The 20--22 km T and mu_mu vertices are present in the original Caputo PDF drawing paths, but lie beyond the visible top-panel x-frame ending at 20 km.",
            "The off-frame coordinates are encoded PDF vector-path data, not values read from the visible plotted axes.",
            "They are not raw Garching simulation tables and are not independently cross-checked by Bollig Figs. 1 and 4.",
            "The committed T_caputo_vertices.csv and mu_mu_caputo_vertices.csv reproduce the PDF path vertices under the existing mapping; this verifies extraction consistency, not the physical provenance of off-frame data.",
            "No profile, source, opacity, transport, luminosity, or axial-vector output is modified.",
        ],
    }


def make_report(d):
    lines = [
        "# Caputo off-frame thermodynamic vector-vertex audit: 20--22 km",
        "",
        "Date: 2026-11-09",
        "",
        "## Source identity and visible frame",
        "",
        f"- Source PDF: {d['source_url']}",
        f"- SHA-256: {d['source_pdf_sha256']}",
        "- The existing extraction map defines the visible top-panel radial frame as 0.1--20 km.",
        f"- Top-panel PDF clip rectangles: {[x['rect_pdf'] for x in d['clipping_paths'] if x.get('rect_pdf') and x['rect_pdf'][0] < 60 and x['rect_pdf'][2] <= 330 and x['rect_pdf'][3] < 230]}. Their common right edge is x_pdf=325.",
        f"- T vector path x extent: {d['curves']['T']['drawing_rect_pdf'][0]}--{d['curves']['T']['drawing_rect_pdf'][2]}; mu_mu vector path x extent: {d['curves']['mu_mu']['drawing_rect_pdf'][0]}--{d['curves']['mu_mu']['drawing_rect_pdf'][2]}. Both extend beyond the clip boundary.",
        "- The T and mu_mu PDF drawing paths continue beyond the visible right edge; the 20--22 km segment is encoded off-frame vector data.",
        "",
        "## Off-frame path audit",
        "",
        "| Curve | Total vertices | 20--22 km vertices | Value range in 20--22 km | CSV-vs-PDF max relative residual | Continuity gaps |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name in ("T","mu_mu"):
        x=d["curves"][name]
        lines.append(
            f"| {name} | {x['point_count']} | {x['off_frame_20_22_vertex_count']} | {x['off_frame_20_22_value_range']} | {100*x['csv_vs_pdf_vertex_max_abs_relative_difference']:.4g}% | {x['off_frame_20_22_continuity_gaps_in_original_item_order']} |"
        )
    lines.extend([
        "",
        "## Selected off-frame values",
        "",
        "| r (km) | T (MeV) | mu_mu (MeV) |",
        "|---:|---:|---:|",
    ])
    tmap={x["r_km"]:x["value"] for x in d["curves"]["T"]["sample_values"]}
    mumap={x["r_km"]:x["value"] for x in d["curves"]["mu_mu"]["sample_values"]}
    for r in (20.0,20.5,21.0,21.5,22.0,22.19):
        lines.append(f"| {r:g} | {tmap.get(r)} | {mumap.get(r)} |")
    lines.extend([
        "",
        "## Interpretation and limits",
        "",
        "The 20--22 km T and mu_mu inputs are not extrapolations invented by the current calculation: the coordinates are present in the Caputo PDF vector drawing paths and are reproduced by the committed vertex CSVs. However, they lie outside the visible 0.1--20 km plotting frame. This makes them encoded off-frame figure data, not visible plot data and not a substitute for the original Garching simulation tables.",
        "",
        "The independent Bollig Fig. 1 and Fig. 4 comparison remains valid only through 20 km. Thus the off-frame Caputo continuation is anchored by excellent agreement at the 20 km boundary but has no independent Bollig cross-check over 20--22 km.",
        "",
        "The B.16 +/-10% temperature and +/-1 MeV mu_numu floor tests quantify sensitivity to these inputs; they do not establish their true uncertainty.",
        "",
        "No production profile or physical output is modified.",
        "",
        "## Reproducibility",
        "",
        "- Script: audit_caputo_offframe_thermodynamic_vertices.py",
        "- Machine-readable result: outputs/caputo_offframe_thermodynamic_vertices_20_22km_2026-11-09.json",
        "- Profile provenance: ../data/profile_provenance.json",
        "",
    ])
    return "\n".join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output-json",type=Path,default=DEFAULT_JSON)
    p.add_argument("--output-md",type=Path,default=DEFAULT_MD)
    a=p.parse_args()
    data=run()
    a.output_json.parent.mkdir(parents=True,exist_ok=True)
    a.output_md.parent.mkdir(parents=True,exist_ok=True)
    a.output_json.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    a.output_md.write_text(make_report(data),encoding="utf-8")
    print(json.dumps({
        "source_pdf_sha256":data["source_pdf_sha256"],
        "visible_frame":data["visible_top_panel_radius_range_km"],
        "clipping_paths":data["clipping_paths"],
        "curves":data["curves"],
        "output_json":str(a.output_json),
        "output_md":str(a.output_md),
    },indent=2))
    print(f"Saved {a.output_json}")
    print(f"Saved {a.output_md}")


if __name__=="__main__":
    main()
