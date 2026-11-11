#!/usr/bin/env python3
"""Extract native vector paths for SFHo-18.8 in Esseili-Kribs Fig. 12."""
from pathlib import Path
import argparse, csv, fitz, hashlib, json
import numpy as np

EXPECTED_PDF_SHA256S = {"d660eb390271b41c5c0c20ccd52cc57df891a78d30067a78f84bb6c228225a92", "c3b92fe6cf2a8bd3fec84925e2baababfe0c707327a68135013f953ed3d87d43"}
PAGE_INDEX = 14
PATHS = {"T_SFHo18p8": 25, "n": 181, "p": 182}
FRAMES = {
    "T_SFHo18p8": (79.77400207519531, 48.8079833984375, 294.02099609375, 166.64398193359375),
    "n": (338.89697265625, 48.8079833984375, 553.1439819335938, 166.64398193359375),
    "p": (338.89697265625, 48.8079833984375, 553.1439819335938, 166.64398193359375),
}
COLORS = {
    "T_SFHo18p8": (1.0, 0.5097887, 0.0196078),
    "n": (0.0, 0.5097887, 0.7842985),
    "p": (0.2, 0.7293965, 1.0),
}

def bezier_points(drawing, n_per_curve=64):
    pts = []
    for item in drawing["items"]:
        if item[0] == "l":
            p0, p1 = item[1], item[2]
            if not pts or np.linalg.norm(np.asarray(pts[-1]) - [p0.x, p0.y]) > 1e-9:
                pts.append([p0.x, p0.y])
            pts.append([p1.x, p1.y])
        elif item[0] == "c":
            p0, p1, p2, p3 = item[1:]
            if not pts or np.linalg.norm(np.asarray(pts[-1]) - [p0.x, p0.y]) > 1e-9:
                pts.append([p0.x, p0.y])
            for t in np.linspace(0.0, 1.0, n_per_curve + 1)[1:]:
                u = 1.0 - t
                x = u**3*p0.x + 3*u*u*t*p1.x + 3*u*t*t*p2.x + t**3*p3.x
                y = u**3*p0.y + 3*u*u*t*p1.y + 3*u*t*t*p2.y + t**3*p3.y
                pts.append([x, y])
        else:
            raise ValueError(f"Unexpected path item {item[0]!r}")
    a = np.asarray(pts, dtype=float)
    a = a[np.argsort(a[:, 0], kind="stable")]
    _, keep = np.unique(np.round(a[:, 0], 10), return_index=True)
    return a[np.sort(keep)]

def clip_curve_to_x(points, xmin, xmax):
    p = points[np.argsort(points[:, 0])]
    if xmin < p[0, 0]:
        raise ValueError("curve does not cover the left plot-frame boundary")
    xend = min(xmax, float(p[-1, 0]))
    y0, y1 = np.interp([xmin, xend], p[:, 0], p[:, 1])
    middle = p[(p[:, 0] > xmin) & (p[:, 0] < xend)]
    return np.vstack(([xmin, y0], middle, [xend, y1]))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--outdir", type=Path, required=True)
    args = ap.parse_args()
    raw = args.pdf.read_bytes()
    pdf_sha = hashlib.sha256(raw).hexdigest()
    if EXPECTED_PDF_SHA256S and pdf_sha not in EXPECTED_PDF_SHA256S:
        raise ValueError(f"PDF SHA-256 is not an approved pinned source: {pdf_sha}")
    page = fitz.open(stream=raw, filetype="pdf")[PAGE_INDEX]
    drawings = page.get_drawings()

    left_tick_x = np.array([126.17900085449219, 175.54400634765625,
                            224.90899658203125, 274.27398681640625])
    right_tick_x = np.array([385.302001953125, 434.6679992675781,
                             484.03399658203125, 533.3989868164062])
    radii = np.array([5., 10., 15., 20.])
    xsl, xil = np.polyfit(radii, left_tick_x, 1)
    xsr, xir = np.polyfit(radii, right_tick_x, 1)
    t_tick_y = np.array([151.18902587890625, 131.87200927734375,
                         112.55499267578125, 93.23797607421875,
                         73.9210205078125, 54.60302734375])
    t_ticks = np.arange(10., 61., 10.)
    ysl, yil = np.polyfit(t_ticks, t_tick_y, 1)

    # Preserve the exact PDF text objects around the right-panel logarithmic
    # y-axis. This distinguishes printed glyphs/superscripts from an OCR-based
    # reading of the rasterized figure.
    right_panel_axis_text_spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                x0, y0, x1, y1 = map(float, span["bbox"])
                if 548.0 <= x0 <= 620.0 and 45.0 <= y0 <= 180.0:
                    right_panel_axis_text_spans.append({
                        "text": span["text"],
                        "bbox_pdf_points": [x0, y0, x1, y1],
                        "font": span["font"],
                        "font_size_pt": float(span["size"]),
                    })
    right_panel_axis_text_spans.sort(key=lambda x: (x["bbox_pdf_points"][1], x["bbox_pdf_points"][0]))
    top_page_text_words = [
        {
            "text": str(word[4]),
            "bbox_pdf_points": [float(v) for v in word[:4]],
        }
        for word in page.get_text("words")
        if float(word[1]) < 190.0
    ]

    rows, meta = [], {}
    for name, path_index in PATHS.items():
        d = drawings[path_index]
        color = tuple(float(v) for v in d["color"])
        if any(abs(a-b) > 0.002 for a, b in zip(color, COLORS[name])):
            raise ValueError(f"Unexpected stroke color for {name}: {color}")
        x0, y0, x1, y1 = FRAMES[name]
        points = clip_curve_to_x(bezier_points(d), x0, x1)
        if np.any(points[:, 1] < y0-1e-6) or np.any(points[:, 1] > y1+1e-6):
            raise ValueError(f"{name} curve leaves the vertical plot frame")
        if name == "T_SFHo18p8":
            radius = (points[:, 0] - xil) / xsl
            value = (points[:, 1] - yil) / ysl
            peak = int(np.argmax(value))
            meta[name] = {
                "path_index": path_index, "stroke_rgb": color,
                "point_count_after_bezier_flattening_and_clipping": len(points),
                "visible_radius_km": [float(radius.min()), float(radius.max())],
                "peak_T_MeV": float(value[peak]), "peak_radius_km": float(radius[peak]),
            }
            for (x, y), r, t in zip(points, radius, value):
                rows.append({"curve": name, "path_index": path_index,
                             "pdf_x_pt": x, "pdf_y_pt": y, "r_km": r,
                             "T_MeV": t, "n_over_n0_corrected": "",
                             "n_over_n0_literal_top10": ""})
        else:
            radius = (points[:, 0] - xir) / xsr
            logn = -4.0 + (166.64398193359375 - points[:, 1]) / 25.6
            n_corrected = 10.0**logn
            n_literal = 10.0*n_corrected
            meta[name] = {
                "path_index": path_index, "stroke_rgb": color,
                "point_count_after_bezier_flattening_and_clipping": len(points),
                "visible_radius_km": [float(radius.min()), float(radius.max())],
                "visible_n_over_n0_corrected": [float(n_corrected.min()), float(n_corrected.max())],
            }
            for (x, y), r, nc, nl in zip(points, radius, n_corrected, n_literal):
                rows.append({"curve": name, "path_index": path_index,
                             "pdf_x_pt": x, "pdf_y_pt": y, "r_km": r,
                             "T_MeV": "", "n_over_n0_corrected": nc,
                             "n_over_n0_literal_top10": nl})

    args.outdir.mkdir(parents=True, exist_ok=True)
    csv_path = args.outdir / "esseili_kribs_fig12_vector_vertices_2026-11-11.csv"
    columns = ["curve", "path_index", "pdf_x_pt", "pdf_y_pt", "r_km",
               "T_MeV", "n_over_n0_corrected", "n_over_n0_literal_top10"]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columns, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    record = {
        "source": "Esseili & Kribs, Phys. Rev. D 114, 016023 (2026), DOI 10.1103/718s-7k7v; checksum-pinned SCOAP3 copy of the published APS PDF",
        "source_urls": ["https://repo.scoap3.org/records/109482", "https://scoap3-prod-backend.s3.cern.ch/media/harvested_files/10.1103/718s-7k7v/718s-7k7v.pdf", "https://journals.aps.org/prd/pdf/10.1103/718s-7k7v"],
        "source_pdf_sha256": pdf_sha, "source_pdf_bytes": len(raw),
        "pdf_page_index_zero_based": PAGE_INDEX, "printed_page": 15,
        "path_indices": PATHS, "plot_frames_pdf_points": FRAMES,
        "axis_calibration": {
            "radius_left": "(x_pdf - %.9f)/%.9f" % (xil, xsl),
            "radius_right": "(x_pdf - %.9f)/%.9f" % (xir, xsr),
            "temperature": "(y_pdf - %.9f)/%.9f" % (yil, ysl),
            "density_candidate": "log10(n/n0) = -4 + (166.643982 - y_pdf)/25.6; n0=0.181 fm^-3",
            "density_alternative_literal_top_tick": "10 times the candidate density",
        },
        "density_axis_label_issue": {
            "visual_reading_of_upper_tick_glyphs": ["10", "1", "10^-2", "10^-3", "10^-4"],
            "axis_tick_labels_are_extractable_text": bool(right_panel_axis_text_spans),
            "axis_tick_text_spans_found_in_right_margin": len(right_panel_axis_text_spans),
            "equal_tick_spacing_pdf_points": [25.56, 25.60, 25.61, 25.61],
            "interpretation": "The right-panel tick labels are not exposed as PDF text spans in the margin; they are vector glyphs. At the available raster resolution the upper two glyphs are visually ambiguous. Equal log spacing anchored by the lower three labels implies top-to-bottom tick values 1, 10^-1, 10^-2, 10^-3, 10^-4. A literal reading of the upper glyphs as 10 and 1 gives a density scale ten times larger and fails the same-model Caputo free-nucleon cross-check. Both mappings are retained; the corrected mapping is selected as a physically cross-validated calibration, not as proof of a typesetting error.",
        },
        "normalization_n0_fm3": 0.181, "curves": meta,
        "right_panel_axis_text_spans": right_panel_axis_text_spans,
        "top_page_text_words": top_page_text_words,
        "digitization_uncertainty_estimate": {
            "curve_stroke_width_pt": float(drawings[PATHS["n"]]["width"]),
            "radius_half_stroke_km": float(drawings[PATHS["n"]]["width"] / 2 / xsr),
            "temperature_half_stroke_MeV": float(drawings[PATHS["T_SFHo18p8"]]["width"] / 2 / abs(ysl)),
            "density_half_stroke_decades": float(drawings[PATHS["n"]]["width"] / 2 / 25.6),
        },
        "caveats": [
            "These are published-figure vector paths, not raw Garching profile data.",
            "The right-panel density axis has a top-two-tick label inconsistency; both literal and cross-checked corrected transforms are archived.",
            "The n and p paths are compared with Caputo reconstructed free-neutron and free-proton curves from the same Garching SFHo-18.8 model lineage.",
        ],
    }
    (args.outdir / "esseili_kribs_fig12_vector_provenance_2026-11-11.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(record, indent=2))

if __name__ == "__main__":
    main()
