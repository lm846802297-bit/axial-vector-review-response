#!/usr/bin/env python3
"""Inspect the pinned arXiv source PDF used for Blinov Fig. 7 digitization.

The source archive is downloaded by the dedicated GitHub Actions workflow.
Only PDF drawing metadata and SHA-256 provenance are archived; the source PDF
itself is not redistributed.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import tarfile
from pathlib import Path

import fitz


CURVE_DRAWING_INDICES = {39, 40, 41, 42, 43, 44}


def path_vertices(drawing: dict) -> list[list[float]]:
    """Return the exact connected polyline vertices from a PDF drawing."""
    vertices: list[list[float]] = []
    for item in drawing.get("items", []):
        if item[0] != "l":
            raise RuntimeError(
                f"Expected line-segment path at drawing {drawing.get('seqno')}; "
                f"found item type {item[0]!r}"
            )
        start, end = item[1], item[2]
        first = [float(start.x), float(start.y)]
        last = [float(end.x), float(end.y)]
        if not vertices:
            vertices.append(first)
        elif (abs(vertices[-1][0] - first[0]) > 1e-4
              or abs(vertices[-1][1] - first[1]) > 1e-4):
            raise RuntimeError("Discontinuous PDF curve path")
        vertices.append(last)
    return vertices


def extract_text_spans(page) -> list[dict]:
    """Archive text labels and their PDF boxes for independent axis/legend checks."""
    spans = []
    for block in page.get_text("dict").get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                value = span.get("text", "").strip()
                if value:
                    spans.append({
                        "text": value,
                        "bbox": [float(x) for x in span.get("bbox", [])],
                        "font": span.get("font"),
                        "size": float(span.get("size", 0.0)),
                    })
    return spans


def inspect(archive: Path) -> dict:
    archive_bytes = archive.read_bytes()
    archive_sha = hashlib.sha256(archive_bytes).hexdigest()
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:*") as bundle:
        matches = [
            member for member in bundle.getmembers()
            if Path(member.name).name == "luminosity_snapshot_t=1.pdf"
        ]
        if len(matches) != 1:
            raise RuntimeError(
                "Expected exactly one luminosity_snapshot_t=1.pdf in the "
                f"arXiv source archive; found {len(matches)}"
            )
        member = matches[0]
        stream = bundle.extractfile(member)
        if stream is None:
            raise RuntimeError("Could not read source PDF from arXiv archive")
        pdf_bytes = stream.read()

    pdf_sha = hashlib.sha256(pdf_bytes).hexdigest()
    document = fitz.open(stream=pdf_bytes, filetype="pdf")
    if document.page_count < 1:
        raise RuntimeError("Source PDF has no pages")
    page = document[0]
    drawings = page.get_drawings()
    rows = []
    for index, drawing in enumerate(drawings):
        rect = drawing.get("rect")
        rows.append({
            "index": index,
            "type": drawing.get("type"),
            "color": drawing.get("color"),
            "fill": drawing.get("fill"),
            "width": drawing.get("width"),
            "item_count": len(drawing.get("items", [])),
            "rect": list(rect) if rect is not None else None,
            "close_path": drawing.get("closePath"),
            "path_vertices": (
                path_vertices(drawing)
                if index in CURVE_DRAWING_INDICES else None
            ),
        })
    return {
        "source_url": "https://arxiv.org/src/2511.09619v2",
        "archive_sha256": archive_sha,
        "archive_member": member.name,
        "pdf_sha256": pdf_sha,
        "page_count": document.page_count,
        "page_rect": list(page.rect),
        "drawing_count": len(drawings),
        "drawings": rows,
        "text_spans": extract_text_spans(page),
        "note": (
            "The six plotted curve paths (drawing indices 39-44) are archived "
            "as exact PDF polyline vertices, together with axis/legend drawing "
            "metadata and text-span boxes. audit_fig7_digitization.py checks "
            "their colors, legend correspondence, log-axis calibration and "
            "every stored transformed point against luminosity_comparison.json."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = inspect(args.archive)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "archive_sha256": result["archive_sha256"],
        "archive_member": result["archive_member"],
        "pdf_sha256": result["pdf_sha256"],
        "page_rect": result["page_rect"],
        "drawing_count": result["drawing_count"],
        "candidate_drawings": [
            row for row in result["drawings"]
            if row["index"] in range(35, 50)
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
