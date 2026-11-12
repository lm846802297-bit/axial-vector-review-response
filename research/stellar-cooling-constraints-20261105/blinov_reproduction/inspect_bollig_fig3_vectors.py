"""Inspect vector paths and text in Bollig et al. Fig. 3 (muon density)."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import urllib.request

import fitz

PDF_URL = "https://arxiv.org/pdf/2005.07141v7"
PAGE_INDEX = 2


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def flatten_path_items(items):
    points = []
    for item in items:
        kind = item[0]
        if kind == "l":
            points.extend([[float(item[1].x), float(item[1].y)],
                           [float(item[2].x), float(item[2].y)]])
        elif kind == "c":
            points.extend([[float(p.x), float(p.y)] for p in item[1:]])
        elif kind == "re":
            rect = item[1]
            points.extend([[float(rect.x0), float(rect.y0)],
                           [float(rect.x1), float(rect.y1)]])
    return points


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="bollig_fig3_") as tmp:
        pdf = args.pdf or (Path(tmp) / "Bollig_2005.07141v7.pdf")
        if args.pdf is None:
            urllib.request.urlretrieve(PDF_URL, pdf)
        pdf_sha = sha256(pdf)
        doc = fitz.open(pdf)
        page = doc[PAGE_INDEX]

        text_spans = []
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    bbox = [float(x) for x in span["bbox"]]
                    if bbox[0] < 330 and bbox[1] < 330:
                        text_spans.append({
                            "text": span["text"],
                            "bbox": bbox,
                            "size": float(span["size"]),
                        })

        candidates = []
        for index, drawing in enumerate(page.get_drawings()):
            rect = drawing["rect"]
            if rect.x0 >= 330 or rect.y0 >= 330:
                continue
            if rect.x1 > 330 or rect.y1 > 330:
                continue
            points = flatten_path_items(drawing["items"])
            candidates.append({
                "index": index,
                "color": drawing.get("color"),
                "fill": drawing.get("fill"),
                "dashes": drawing.get("dashes"),
                "width": drawing.get("width"),
                "rect": [float(rect.x0), float(rect.y0),
                         float(rect.x1), float(rect.y1)],
                "item_count": len(drawing["items"]),
                "point_count": len(points),
                "points_first_last": points[:4] + points[-4:] if points else [],
                "closePath": drawing.get("closePath"),
                "type": drawing.get("type"),
            })

    payload = {
        "source": "Bollig et al., arXiv:2005.07141v7",
        "pdf_url": PDF_URL,
        "pdf_sha256": pdf_sha,
        "page_index": PAGE_INDEX,
        "figure": "Fig. 3, muon number density",
        "text_spans_upper_left": text_spans,
        "vector_paths_upper_left": candidates,
        "note": (
            "This is a path/text inventory only. The SFHo-18.8 curve must be "
            "identified from the Fig. 3 legend before digitizing; no curve is "
            "selected automatically by color alone."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "pdf_sha256": pdf_sha,
        "text_span_count": len(text_spans),
        "candidate_path_count": len(candidates),
        "candidate_paths": candidates,
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
