"""Inspect the original Bollig et al. SFHo-18.8 Fig. 3/4 vector paths.

Updated 2026-11-09: this first-stage audit downloads the consolidated arXiv v7 PDF, extracts the
muon-density and muon-degeneracy plot geometry from page 3, and archives all
candidate vector paths with coordinates/colors. It does not modify any
profile, opacity, transport, luminosity, or axial output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

import pymupdf

URL = "https://arxiv.org/pdf/2005.07141v7"
PAGE_INDEX = 2
DEFAULT_OUTPUT = Path(__file__).resolve().parent / "outputs" / "bollig_fig3_fig4_vector_paths_2026-11-09.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def polyline_points(drawing):
    points = []
    for item in drawing["items"]:
        if item[0] != "l":
            return None
        points.extend((tuple(item[1]), tuple(item[2])))
    if len(points) < 4:
        return None
    return points


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    pdf = args.pdf
    if pdf is None:
        pdf = args.output.parent / "bollig_2005.07141v7.pdf"
        pdf.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(URL, pdf)

    doc = pymupdf.open(pdf)
    page = doc[PAGE_INDEX]
    drawings = page.get_drawings()
    candidates = []
    for index, d in enumerate(drawings):
        pts = polyline_points(d)
        if pts is None:
            continue
        rect = [float(v) for v in d["rect"]]
        if rect[2] - rect[0] < 25 or rect[3] - rect[1] < 2:
            continue
        # Page 3 contains the two relevant plots below the model table.
        # Keep vector paths intersecting the central figure band for manual
        # identification of the muon-density and muon-degeneracy curves.
        if rect[3] < 150 or rect[1] > 500:
            continue
        color = d.get("color")
        candidates.append({
            "index": index,
            "rect": rect,
            "color": [float(x) for x in color] if color is not None else None,
            "fill": [float(x) for x in d["fill"]] if d.get("fill") is not None else None,
            "width": float(d["width"]) if d.get("width") is not None else None,
            "type": d.get("type"),
            "item_count": len(d["items"]),
            "point_count": len(pts),
            "points": [[float(p[0]), float(p[1])] for p in pts],
        })

    payload = {
        "source_url": URL,
        "pdf_sha256": sha256(pdf),
        "pdf_page_count": len(doc),
        "page_index": PAGE_INDEX,
        "page_rect": [float(x) for x in page.rect],
        "page_text": page.get_text("text"),
        "candidate_vector_paths": candidates,
        "scope": "vector-path extraction only; no physical curve is selected automatically",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "pdf_sha256": payload["pdf_sha256"],
        "page_rect": payload["page_rect"],
        "number_of_drawings": len(drawings),
        "number_of_candidate_paths": len(candidates),
        "candidates": [
            {k: v for k, v in x.items() if k != "points"}
            for x in candidates
        ],
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
