#!/usr/bin/env python3
"""Independently verify Fig. 7 digitization against pinned PDF vector paths.

This checks the PDF drawing identity, legend-color correspondence, log-axis
calibration, and every stored (g, luminosity) point for all six mass curves.
It does not infer author data between the vertices of the published path.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_DRAWINGS = HERE / "outputs" / "fig7_source_drawings_2026-11-07.json"
DEFAULT_COMPARISON = HERE / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "fig7_digitization_audit_2026-11-07.json"

CURVES = [
    ("1e-06", 1e-6, 39, 83, (0.12156862765550613, 0.46666666865348816, 0.7058823704719543)),
    ("1e-05", 1e-5, 40, 83, (1.0, 0.49803921580314636, 0.054901961237192154)),
    ("0.1", 0.1, 41, 45, (0.1725490242242813, 0.6274510025978088, 0.1725490242242813)),
    ("1.0", 1.0, 42, 34, (0.8392156958580017, 0.15294118225574493, 0.1568627506490196)),
    ("10.0", 10.0, 43, 27, (0.5803921818733215, 0.40392157435417175, 0.7411764860153198)),
    ("200.0", 200.0, 44, 14, (0.5490196347236633, 0.33725491166114807, 0.29411765933036804)),
]


def audit(drawings_path: Path, comparison_path: Path) -> dict:
    source = json.loads(drawings_path.read_text(encoding="utf-8"))
    comparison = json.loads(comparison_path.read_text(encoding="utf-8"))
    if source["pdf_sha256"] != comparison["pdf_sha256"]:
        raise AssertionError("PDF SHA-256 differs between drawing audit and luminosity data")

    drawings = source["drawings"]
    if len(drawings) != 56:
        raise AssertionError(f"Expected 56 drawing objects, found {len(drawings)}")

    # Axis rectangle and major ticks are native vector objects in the same PDF.
    left_x = float(drawings[46]["rect"][0])
    right_x = float(drawings[47]["rect"][0])
    bottom_y = float(drawings[48]["rect"][1])
    top_y = float(drawings[49]["rect"][1])
    x_tick_x = np.asarray([drawings[i]["rect"][0] for i in range(2, 11)], float)
    y_tick_y = np.asarray([drawings[i]["rect"][1] for i in range(11, 15)], float)
    expected_x_tick_x = np.linspace(left_x, right_x, 9)
    expected_y_tick_y = np.linspace(bottom_y, top_y, 4)
    x_tick_residual = float(np.max(np.abs(x_tick_x - expected_x_tick_x)))
    y_tick_residual = float(np.max(np.abs(y_tick_y - expected_y_tick_y)))
    if x_tick_residual > 2e-5 or y_tick_residual > 2e-5:
        raise AssertionError("Major tick marks are inconsistent with a linear log-axis transform")

    # Tick labels visible in both the pinned arXiv source PDF and the
    # version-of-record PDF: alpha_V=10^-22...10^-6 and L=10^52...10^55.
    x_log_ticks = np.arange(-22.0, -5.999, 2.0)
    y_log_ticks = np.arange(52.0, 56.0, 1.0)
    x_tick_labels = [
        {"pdf_x": float(x), "log10_alpha_V": float(a)}
        for x, a in zip(x_tick_x, x_log_ticks)
    ]
    y_tick_labels = [
        {"pdf_y": float(y), "log10_luminosity_erg_s": float(v)}
        for y, v in zip(y_tick_y, y_log_ticks)
    ]

    # Legend line samples use the same colors as the six data paths.
    rows = []
    for key, mass, index, item_count, expected_color in CURVES:
        drawing = drawings[index]
        if drawing["index"] != index:
            raise AssertionError(f"Drawing index mismatch for m={mass:g} MeV")
        if drawing["item_count"] != item_count:
            raise AssertionError(f"Path item count changed for m={mass:g} MeV")
        if drawing.get("fill") is not None:
            raise AssertionError(f"Expected an unfilled curve path for m={mass:g} MeV")
        color = np.asarray(drawing["color"], float)
        if not np.allclose(color, expected_color, rtol=0.0, atol=1e-8):
            raise AssertionError(f"Curve color changed for m={mass:g} MeV")

        legend = drawings[50 + (index - 39)]
        if legend["item_count"] != 2 or not np.allclose(
            legend["color"], expected_color, rtol=0.0, atol=1e-8
        ):
            raise AssertionError(f"Legend color does not identify m={mass:g} MeV path")

        vertices = drawing.get("path_vertices")
        if not vertices or len(vertices) != item_count + 1:
            raise AssertionError(f"Raw vector vertices missing/incomplete for m={mass:g} MeV")
        xy = np.asarray(vertices, float)
        if xy.ndim != 2 or xy.shape[1] != 2 or not np.all(np.isfinite(xy)):
            raise AssertionError(f"Malformed vector vertices for m={mass:g} MeV")

        # Figure 7 axes: alpha_V is logarithmic from 1e-22 to 1e-6;
        # luminosity is logarithmic from 1e52 to 1e55 erg/s.
        alpha = 10.0 ** (-22.0 + 16.0 * (xy[:, 0] - left_x) / (right_x - left_x))
        coupling = np.sqrt(4.0 * np.pi * alpha)
        luminosity = 10.0 ** (
            52.0 + 3.0 * (bottom_y - xy[:, 1]) / (bottom_y - top_y)
        )
        visible = (luminosity >= 1e52) & (luminosity <= 1e55)
        coupling_visible = coupling[visible]
        luminosity_visible = luminosity[visible]

        stored = comparison["reference_vertices"][key]
        stored_g = np.asarray(stored["g"], float)
        stored_l = np.asarray(stored["luminosity_erg_s"], float)
        if stored["drawing_index"] != index:
            raise AssertionError(f"Stored drawing index mismatch for m={mass:g} MeV")
        if stored["source_item_count"] != item_count:
            raise AssertionError(f"Stored item count mismatch for m={mass:g} MeV")
        if not np.allclose(stored_g, coupling_visible, rtol=5e-13, atol=0.0):
            raise AssertionError(f"Coupling digitization mismatch for m={mass:g} MeV")
        if not np.allclose(stored_l, luminosity_visible, rtol=5e-13, atol=0.0):
            raise AssertionError(f"Luminosity digitization mismatch for m={mass:g} MeV")

        # The horizontal axis is alpha_V, while the solver uses g_{mu tau}.
        alpha_roundtrip = stored_g**2 / (4.0 * np.pi)
        alpha_from_pdf = 10.0 ** (
            -22.0 + 16.0 * (
                xy[visible, 0] - left_x
            ) / (right_x - left_x)
        )
        alpha_roundtrip_residual = float(np.max(
            np.abs(alpha_roundtrip / alpha_from_pdf - 1.0)
        ))

        rows.append({
            "mass_MeV": mass,
            "drawing_index": index,
            "pdf_path_segments": item_count,
            "raw_pdf_vertices": int(len(vertices)),
            "visible_digitized_vertices": int(np.count_nonzero(visible)),
            "curve_color_rgb": color.tolist(),
            "max_relative_g_reconstruction_residual": float(np.max(
                np.abs(stored_g / coupling_visible - 1.0)
            )),
            "max_relative_luminosity_reconstruction_residual": float(np.max(
                np.abs(stored_l / luminosity_visible - 1.0)
            )),
            "max_relative_alpha_roundtrip_residual": alpha_roundtrip_residual,
            "first_visible_point": {
                "g": float(stored_g[0]),
                "luminosity_erg_s": float(stored_l[0]),
            },
            "last_visible_point": {
                "g": float(stored_g[-1]),
                "luminosity_erg_s": float(stored_l[-1]),
            },
        })

    ten = next(row for row in rows if row["mass_MeV"] == 10.0)
    if ten["visible_digitized_vertices"] != 25:
        raise AssertionError("The 10 MeV curve does not reproduce the archived 25 visible vertices")

    return {
        "title": "Blinov Fig. 7 vector-path digitization audit",
        "status": "PASS_EXACT_PDF_VECTOR_PATH_RECONSTRUCTION",
        "source_url": source["source_url"],
        "source_archive_sha256": source["archive_sha256"],
        "source_pdf_sha256": source["pdf_sha256"],
        "comparison_pdf_sha256": comparison["pdf_sha256"],
        "page_rect": source["page_rect"],
        "plot_axes_pdf_coordinates": {
            "x_min": left_x, "x_max": right_x,
            "y_top": top_y, "y_bottom": bottom_y,
        },
        "axis_calibration": {
            "x_major_ticks": x_tick_labels,
            "y_major_ticks": y_tick_labels,
            "max_x_tick_spacing_residual_pdf_points": x_tick_residual,
            "max_y_tick_spacing_residual_pdf_points": y_tick_residual,
            "x_variable": "alpha_V = g_mu_tau^2/(4*pi)",
            "x_log10_range": [-22.0, -6.0],
            "y_variable": "L_V [erg/s]",
            "y_log10_range": [52.0, 55.0],
        },
        "curve_results": rows,
        "ten_MeV_result": ten,
        "limitations": [
            "These are exact centerline vertices of the plotted PDF polylines, not author-provided numerical tables.",
            "The 10 MeV source path has 27 line segments (28 raw vertices), of which 25 lie inside the visible plotting frame.",
            "The digitization audit verifies path identity, color/legend correspondence, axis calibration and all stored transformed vertices; it does not infer the authors' unplotted interpolation or original simulation samples.",
            "The version-of-record Fig. 7 was independently visually compared with the pinned arXiv v2 source figure.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--drawings", type=Path, default=DEFAULT_DRAWINGS)
    parser.add_argument("--comparison", type=Path, default=DEFAULT_COMPARISON)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = audit(args.drawings, args.comparison)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "source_pdf_sha256": result["source_pdf_sha256"],
        "axis_calibration": result["axis_calibration"],
        "curve_results": result["curve_results"],
    }, indent=2))


if __name__ == "__main__":
    main()
