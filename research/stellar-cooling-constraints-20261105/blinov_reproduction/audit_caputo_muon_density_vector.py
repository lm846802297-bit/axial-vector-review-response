"""Audit the Caputo Fig. 1 muon-density vector path and axis calibration.

Downloads the public arXiv source archive, verifies the SNProfile.pdf hash,
extracts the exact PDF drawing path used for n_mu/n0, and compares the
reconstructed vertices against the committed CSV. No production output is
modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import tarfile
import urllib.request
from pathlib import Path

import numpy as np
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE_DIR = ROOT / "latex-build" / "sources"
ARCHIVE = SOURCE_DIR / "SNProfile.pdf.tar.gz"
PDF = SOURCE_DIR / "SNProfile.pdf"
CSV = ROOT / "data" / "n_mu_over_n0_caputo_vertices.csv"
OUT = HERE / "outputs" / "caputo_muon_density_vector_audit_2026-11-09.json"
URL = "https://arxiv.org/src/2109.03244v3"
MEMBER = "figures/SNProfile.pdf"
EXPECTED_SHA256 = "19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e"


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def extract_vertices(drawing):
    points = []
    kinds = []
    for item in drawing["items"]:
        kinds.append(item[0])
        if item[0] != "l":
            continue
        points.extend([tuple(item[1]), tuple(item[2])])
    if not points:
        return np.empty((0, 2)), kinds
    p = np.asarray(points, dtype=float)
    p = p[np.argsort(p[:, 0], kind="stable")]
    _, keep = np.unique(p[:, 0], return_index=True)
    return p[keep], kinds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    if not PDF.exists():
        urllib.request.urlretrieve(URL, ARCHIVE)
        with tarfile.open(ARCHIVE) as tar:
            member = tar.extractfile(MEMBER)
            if member is None:
                raise RuntimeError(f"Missing {MEMBER} in arXiv source archive")
            PDF.write_bytes(member.read())
    actual_sha = sha256(PDF)
    if actual_sha != EXPECTED_SHA256:
        raise RuntimeError(f"SNProfile.pdf SHA mismatch: {actual_sha}")

    doc = pymupdf.open(PDF)
    page = doc[0]
    drawings = page.get_drawings()
    text_spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text_spans.append({
                    "text": span["text"],
                    "bbox": [float(x) for x in span["bbox"]],
                })

    # The existing profile extraction selects drawing path 161 for n_mu/n0.
    selected_index = 161
    selected = drawings[selected_index]
    selected_points, selected_kinds = extract_vertices(selected)
    color = [float(x) for x in selected["color"]] if selected.get("color") else None

    # Keep all compact black line paths in the lower-panel plotting region.
    axis_candidates = []
    for index, d in enumerate(drawings):
        rect = [float(x) for x in d["rect"]]
        if rect[0] < 35 or rect[2] > 335 or rect[1] < 220 or rect[3] > 465:
            continue
        width, height = rect[2] - rect[0], rect[3] - rect[1]
        if (width <= 5.0 or height <= 5.0) and d.get("color") == (0.0, 0.0, 0.0):
            pts, kinds = extract_vertices(d)
            axis_candidates.append({
                "index": index, "rect": rect,
                "width": float(d["width"]) if d.get("width") is not None else None,
                "item_kinds": kinds,
                "points": [[float(x), float(y)] for x, y in pts],
            })

    # Reproduce the committed extraction formula exactly.
    radius = (selected_points[:, 0] - 47.52) * 20.0 / (324.0 - 47.52)
    n_over_n0 = 10.0 ** (-4.0 + (442.918 - selected_points[:, 1]) / 41.4718)

    # Compare with committed CSV, interpolating the CSV at every extracted
    # source vertex. This verifies the current extraction path and formula.
    csv = np.genfromtxt(CSV, delimiter=",", names=True)
    csv_interp = np.interp(radius, csv["r_km"], csv["value"])
    rel = n_over_n0 / csv_interp - 1.0

    payload = {
        "source_url": URL,
        "source_member": MEMBER,
        "pdf_sha256": actual_sha,
        "page_index": 0,
        "page_rect": [float(x) for x in page.rect],
        "drawing_count": len(drawings),
        "selected_density_path": {
            "index": selected_index,
            "color": color,
            "rect": [float(x) for x in selected["rect"]],
            "item_kinds": selected_kinds,
            "point_count": int(len(selected_points)),
            "first_points": [[float(x), float(y)] for x, y in selected_points[:5]],
            "last_points": [[float(x), float(y)] for x, y in selected_points[-5:]],
        },
        "existing_mapping": {
            "radius_km": "(x_pdf - 47.52)*20/(324-47.52)",
            "n_mu_over_n0": "10**(-4 + (442.918-y_pdf)/41.4718)",
            "csv_vs_pdf_vertex_mean_abs_relative_difference": float(np.mean(np.abs(rel))),
            "csv_vs_pdf_vertex_max_abs_relative_difference": float(np.max(np.abs(rel))),
        },
        "text_spans_lower_panel": [
            x for x in text_spans
            if x["bbox"][0] < 335 and 220 <= x["bbox"][1] <= 465
        ],
        "axis_path_candidates": axis_candidates,
        "sampled_curve_vertices": [
            {"r_km": float(r), "n_mu_over_n0": float(n)}
            for r, n in zip(radius[::max(1, len(radius)//30)], n_over_n0[::max(1, len(radius)//30)])
        ],
        "scope": "vector path and calibration inventory only; no production rates or profiles changed",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "pdf_sha256": actual_sha,
        "selected_density_path": payload["selected_density_path"],
        "mapping": payload["existing_mapping"],
        "axis_path_count": len(axis_candidates),
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
