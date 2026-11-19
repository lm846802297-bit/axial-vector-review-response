"""Extract Croon et al. Fig. 2 vector paths and text geometry for transparent digitization.

This is a source-figure extraction stage only. It does not select curve
identities, calibrate axes, or alter the computed luminosity curves.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

import pymupdf

URL = "https://arxiv.org/pdf/2006.13942v2"
HERE = Path(__file__).resolve().parent
DEFAULT_PDF = HERE / "outputs" / "croon_2006.13942v2_source.pdf"
DEFAULT_JSON = HERE / "outputs" / "croon_fig2_vector_paths_2026-11-19.json"
DEFAULT_PNG = HERE / "outputs" / "croon_fig2_source_crop_2026-11-19.png"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def xy(point) -> list[float]:
    return [float(point.x), float(point.y)]


def bezier(p0, p1, p2, p3, samples: int = 24) -> list[list[float]]:
    out = []
    for i in range(samples + 1):
        t = i / samples
        u = 1.0 - t
        x = u**3*p0.x + 3*u*u*t*p1.x + 3*u*t*t*p2.x + t**3*p3.x
        y = u**3*p0.y + 3*u*u*t*p1.y + 3*u*t*t*p2.y + t**3*p3.y
        out.append([float(x), float(y)])
    return out


def flatten_drawing(drawing: dict, bezier_samples: int = 24) -> list[list[float]]:
    points: list[list[float]] = []
    for item in drawing["items"]:
        kind = item[0]
        if kind == "l":
            p1, p2 = item[1], item[2]
            if not points or points[-1] != xy(p1):
                points.append(xy(p1))
            points.append(xy(p2))
        elif kind == "c":
            p0, p1, p2, p3 = item[1], item[2], item[3], item[4]
            segment = bezier(p0, p1, p2, p3, bezier_samples)
            if points and points[-1] == segment[0]:
                segment = segment[1:]
            points.extend(segment)
        elif kind == "re":
            rect = item[1]
            points.extend([
                [float(rect.x0), float(rect.y0)],
                [float(rect.x1), float(rect.y0)],
                [float(rect.x1), float(rect.y1)],
                [float(rect.x0), float(rect.y1)],
                [float(rect.x0), float(rect.y0)],
            ])
        elif kind == "qu":
            quad = item[1]
            points.extend([xy(quad.ul), xy(quad.ur), xy(quad.lr), xy(quad.ll), xy(quad.ul)])
    return points


def find_figure_page(doc) -> tuple[int, str]:
    candidates = []
    for index, page in enumerate(doc):
        text = page.get_text("text")
        if "Figure 2:" in text or "Figure 2" in text:
            candidates.append((index, text))
    if len(candidates) != 1:
        raise RuntimeError(
            f"Expected one page containing Croon Fig. 2, found {[x[0] for x in candidates]}"
        )
    return candidates[0]


def extract_text_spans(page) -> list[dict]:
    spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                spans.append({
                    "text": span["text"],
                    "bbox": [float(x) for x in span["bbox"]],
                    "origin": [float(x) for x in span.get("origin", (0.0, 0.0))],
                    "font": span.get("font"),
                    "size": float(span["size"]),
                    "color": int(span["color"]),
                    "flags": int(span["flags"]),
                })
    return spans


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--png", type=Path, default=DEFAULT_PNG)
    parser.add_argument("--bezier-samples", type=int, default=32)
    args = parser.parse_args()

    args.pdf.parent.mkdir(parents=True, exist_ok=True)
    if not args.pdf.exists():
        urllib.request.urlretrieve(URL, args.pdf)

    doc = pymupdf.open(args.pdf)
    page_index, page_text = find_figure_page(doc)
    page = doc[page_index]
    drawings = page.get_drawings()

    paths = []
    for index, drawing in enumerate(drawings):
        rect = drawing["rect"]
        color = drawing.get("color")
        fill = drawing.get("fill")
        paths.append({
            "index": int(index),
            "rect": [float(rect.x0), float(rect.y0), float(rect.x1), float(rect.y1)],
            "stroke_rgb": [float(x) for x in color] if color is not None else None,
            "fill_rgb": [float(x) for x in fill] if fill is not None else None,
            "width": float(drawing["width"]) if drawing.get("width") is not None else None,
            "dashes": drawing.get("dashes"),
            "line_cap": drawing.get("lineCap"),
            "line_join": drawing.get("lineJoin"),
            "close_path": bool(drawing.get("closePath", False)),
            "fill_opacity": float(drawing["fill_opacity"]) if drawing.get("fill_opacity") is not None else None,
            "stroke_opacity": float(drawing["stroke_opacity"]) if drawing.get("stroke_opacity") is not None else None,
            "type": drawing.get("type"),
            "items": [
                {
                    "kind": item[0],
                    "points": [xy(p) for p in item[1:] if hasattr(p, "x") and hasattr(p, "y")],
                    "rect": [float(item[1].x0), float(item[1].y0), float(item[1].x1), float(item[1].y1)]
                    if item[0] == "re" else None,
                    "quad": [xy(item[1].ul), xy(item[1].ur), xy(item[1].lr), xy(item[1].ll)]
                    if item[0] == "qu" else None,
                }
                for item in drawing["items"]
            ],
            "flattened_points": flatten_drawing(drawing, args.bezier_samples),
        })

    text_spans = extract_text_spans(page)
    page_rect = [float(x) for x in page.rect]
    # Crop around the page's figure panel; keep the full panel and axis labels.
    # The exact crop is derived from the vector drawing extents and text spans,
    # then expanded by a small margin for visual inspection.
    curve_like = [
        p for p in paths
        if p["stroke_rgb"] is not None
        and p["rect"][2]-p["rect"][0] > 20.0
        and p["rect"][3]-p["rect"][1] > 2.0
    ]
    if curve_like:
        x0 = min(p["rect"][0] for p in curve_like)
        y0 = min(p["rect"][1] for p in curve_like)
        x1 = max(p["rect"][2] for p in curve_like)
        y1 = max(p["rect"][3] for p in curve_like)
        crop = pymupdf.Rect(
            max(page.rect.x0, x0-35.0), max(page.rect.y0, y0-30.0),
            min(page.rect.x1, x1+35.0), min(page.rect.y1, y1+35.0)
        )
    else:
        crop = page.rect
    pix = page.get_pixmap(matrix=pymupdf.Matrix(2.5, 2.5), clip=crop, alpha=False)
    args.png.parent.mkdir(parents=True, exist_ok=True)
    pix.save(args.png)

    payload = {
        "source_url": URL,
        "pdf_sha256": sha256(args.pdf),
        "pdf_page_count": len(doc),
        "page_index": page_index,
        "page_rect": page_rect,
        "figure_page_text": page_text,
        "figure_crop_rect": [float(crop.x0), float(crop.y0), float(crop.x1), float(crop.y1)],
        "text_spans": text_spans,
        "vector_path_count": len(paths),
        "vector_paths": paths,
        "scope": "all vector paths and text geometry extracted; no physical curve identities or axis calibration are selected automatically",
        "bezier_samples_per_segment": int(args.bezier_samples),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")

    print(json.dumps({
        "pdf_sha256": payload["pdf_sha256"],
        "pdf_page_count": payload["pdf_page_count"],
        "page_index": page_index,
        "page_rect": page_rect,
        "figure_crop_rect": payload["figure_crop_rect"],
        "vector_path_count": len(paths),
        "candidate_summary": [
            {
                "index": p["index"], "rect": p["rect"],
                "stroke_rgb": p["stroke_rgb"], "fill_rgb": p["fill_rgb"],
                "width": p["width"], "type": p["type"],
                "point_count": len(p["flattened_points"]),
            }
            for p in paths
            if p["stroke_rgb"] is not None and len(p["flattened_points"]) >= 4
        ],
        "output_json": str(args.output),
        "output_png": str(args.png),
    }, indent=2))


if __name__ == "__main__":
    main()
