"""Audit raw PDF path geometry and the archived Fig. 7 digitization.

This is targeted at the 10 MeV high-coupling tail. It checks the actual
line-segment path in the pinned source PDF, axis-frame coordinates, monotonicity
of the coupling coordinate, points clipped by the visible luminosity range,
and exact reconstruction of the 25 archived 10 MeV reference vertices.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import fitz
import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_REFERENCE = HERE / "outputs" / "vector_audit" / "luminosity_comparison.json"
DEFAULT_OUTPUT = HERE / "outputs" / "fig7_digitization_geometry_2026-11-08.json"

EXPECTED_PDF_SHA256 = "4d7d1d10bfe2b52992af94df98749fa3adac887c009cbf98515fa12e6c48fdb5"
CURVES = [
    (1e-6, 39, 83, (0.12156862765550613, 0.46666666865348816, 0.7058823704719543)),
    (1e-5, 40, 83, (1.0, 0.49803921580314636, 0.054901961237192154)),
    (0.1, 41, 45, (0.1725490242242813, 0.6274510025978088, 0.1725490242242813)),
    (1.0, 42, 34, (0.8392156958580017, 0.15294118225574493, 0.1568627506494522)),
    (10.0, 43, 27, (0.5803921818733215, 0.40392157435417175, 0.7411764860153192)),
    (200.0, 44, 14, (0.5490196347236633, 0.33725491166114807, 0.29411765933036804)),
]

# Axis-frame endpoints are pinned to the PDF drawing paths for the four axes.
X_LEFT = 54.82951354980469
X_RIGHT = 397.99951171875
Y_BOTTOM = 195.54043579101562
Y_TOP = 20.904434204101562
LOG10_ALPHA_MIN = -22.0
LOG10_ALPHA_MAX = -6.0
LOG10_L_MIN = 52.0
LOG10_L_MAX = 55.0


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ordered_polyline(drawing: dict) -> np.ndarray:
    """Recover the source path in segment order without sorting/deduplication."""
    points = []
    for item in drawing.get("items", []):
        if item[0] != "l":
            raise ValueError(f"Expected line segment, received {item[0]!r}")
        start, end = np.asarray(item[1], float), np.asarray(item[2], float)
        if not points:
            points.append(start)
        if not np.allclose(points[-1], start, rtol=0.0, atol=1e-4):
            raise ValueError("Source path is discontinuous between line segments")
        points.append(end)
    if len(points) < 2:
        raise ValueError("Source path has fewer than two vertices")
    return np.asarray(points, float)


def legacy_polyline(drawing: dict) -> np.ndarray:
    """Reproduce the historical sort-by-x/unique-x digitization operation."""
    points = ordered_polyline(drawing)
    order = np.argsort(points[:, 0], kind="stable")
    points = points[order]
    _, keep = np.unique(points[:, 0], return_index=True)
    return points[keep]


def transform_pdf_coordinates(xy: np.ndarray) -> dict:
    """Apply the exact axis transform used in compare_vector_luminosity.py."""
    xy = np.asarray(xy, float)
    log_alpha = LOG10_ALPHA_MIN + (
        (xy[:, 0] - X_LEFT)/(X_RIGHT-X_LEFT)
        * (LOG10_ALPHA_MAX-LOG10_ALPHA_MIN)
    )
    alpha = 10.0**log_alpha
    g = np.sqrt(4.0*np.pi*alpha)
    log_luminosity = LOG10_L_MIN + (
        (Y_BOTTOM-xy[:, 1])/(Y_BOTTOM-Y_TOP)
        * (LOG10_L_MAX-LOG10_L_MIN)
    )
    luminosity = 10.0**log_luminosity
    return {
        "log10_alpha": log_alpha,
        "alpha": alpha,
        "g": g,
        "log10_luminosity": log_luminosity,
        "luminosity_erg_s": luminosity,
    }


def visible_luminosity_mask(transformed: dict) -> np.ndarray:
    return (
        (transformed["luminosity_erg_s"] >= 10.0**LOG10_L_MIN)
        & (transformed["luminosity_erg_s"] <= 10.0**LOG10_L_MAX)
    )


def validate_axis_tick_words(words: list) -> dict:
    """Validate the log-axis coordinate map against labels embedded in the PDF."""
    x_ticks = []
    y_ticks = []
    for word in words:
        label = str(word[4])
        bbox = [float(x) for x in word[:4]]
        x_center = (bbox[0]+bbox[2])/2.0
        y_center = (bbox[1]+bbox[3])/2.0
        # The standalone PDF also contains a legend with 1 x 10^-6 and
        # 1 x 10^-5. Keep only tick labels adjacent to the actual axes.
        if re.fullmatch(r"10[−-]\d+", label) and y_center > 180.0:
            exponent = int(label[2:].replace("−", "-"))
            x_ticks.append((exponent, x_center))
        elif re.fullmatch(r"10(?:5[2-5])", label) and x_center < 50.0:
            exponent = int(label[2:])
            y_ticks.append((exponent, y_center))

    x_ticks.sort(key=lambda item: item[0])
    y_ticks.sort(key=lambda item: item[0])
    expected_x_exponents = list(range(-22, -5, 2))
    expected_y_exponents = [52, 53, 54, 55]
    if [x[0] for x in x_ticks] != expected_x_exponents:
        raise ValueError(f"Unexpected horizontal-axis tick labels: {x_ticks}")
    if [y[0] for y in y_ticks] != expected_y_exponents:
        raise ValueError(f"Unexpected vertical-axis tick labels: {y_ticks}")

    expected_x_positions = [
        X_LEFT+(exponent-LOG10_ALPHA_MIN)
        /(LOG10_ALPHA_MAX-LOG10_ALPHA_MIN)*(X_RIGHT-X_LEFT)
        for exponent in expected_x_exponents
    ]
    expected_y_positions = [
        Y_BOTTOM-(exponent-LOG10_L_MIN)
        /(LOG10_L_MAX-LOG10_L_MIN)*(Y_BOTTOM-Y_TOP)
        for exponent in expected_y_exponents
    ]
    x_residuals = [
        actual-expected
        for (_, actual), expected in zip(x_ticks, expected_x_positions)
    ]
    y_residuals = [
        actual-expected
        for (_, actual), expected in zip(y_ticks, expected_y_positions)
    ]
    if max(max(abs(x) for x in x_residuals),
           max(abs(y) for y in y_residuals)) > 1.0:
        raise ValueError(
            f"Axis tick labels disagree with the log transform: "
            f"x={x_residuals}, y={y_residuals}"
        )
    return {
        "horizontal_ticks": [
            {"log10_alpha": exponent, "pdf_x_center": actual,
             "expected_pdf_x": expected, "residual_pdf_points": residual}
            for (exponent, actual), expected, residual in zip(
                x_ticks, expected_x_positions, x_residuals
            )
        ],
        "vertical_ticks": [
            {"log10_luminosity": exponent, "pdf_y_center": actual,
             "expected_pdf_y": expected, "residual_pdf_points": residual}
            for (exponent, actual), expected, residual in zip(
                y_ticks, expected_y_positions, y_residuals
            )
        ],
        "maximum_absolute_tick_position_residual_pdf_points": float(
            max(max(abs(x) for x in x_residuals),
                max(abs(y) for y in y_residuals))
        ),
        "tolerance_pdf_points": 1.0,
    }


def audit(source_pdf: Path, reference_json: Path) -> dict:
    pdf_sha = sha256(source_pdf)
    if pdf_sha != EXPECTED_PDF_SHA256:
        raise ValueError(f"Pinned Fig. 7 source PDF changed: {pdf_sha}")

    document = fitz.open(source_pdf)
    if document.page_count != 1:
        raise ValueError(f"Expected one-page Fig. 7 source PDF, got {document.page_count}")
    page = document[0]
    drawings = page.get_drawings()
    if len(drawings) != 56:
        raise ValueError(f"Expected 56 source drawing paths, got {len(drawings)}")

    # Read axis paths from the source PDF, rather than trusting hard-coded
    # coordinates alone. Drawings 46--49 are the left, right, top and bottom
    # plot-frame edges in the pinned source.
    axis_indices = {"left": 46, "right": 47, "bottom": 48, "top": 49}
    axis_geometry = {}
    for name, index in axis_indices.items():
        path = drawings[index]
        if len(path["items"]) != 1 or path["items"][0][0] != "l":
            raise ValueError(f"Axis drawing {index} is not a single line")
        axis_geometry[name] = {
            "drawing_index": index,
            "start": list(path["items"][0][1]),
            "end": list(path["items"][0][2]),
            "color": path["color"],
            "width": path["width"],
        }

    frame = {
        "x_left": float(axis_geometry["left"]["start"][0]),
        "x_right": float(axis_geometry["right"]["start"][0]),
        "y_bottom": float(axis_geometry["bottom"]["start"][1]),
        "y_top": float(axis_geometry["top"]["start"][1]),
    }
    frame_residuals = {
        "x_left_minus_pinned": frame["x_left"]-X_LEFT,
        "x_right_minus_pinned": frame["x_right"]-X_RIGHT,
        "y_bottom_minus_pinned": frame["y_bottom"]-Y_BOTTOM,
        "y_top_minus_pinned": frame["y_top"]-Y_TOP,
    }
    if max(abs(x) for x in frame_residuals.values()) > 1e-5:
        raise ValueError(f"PDF axis frame disagrees with pinned transform: {frame_residuals}")

    reference = json.loads(reference_json.read_text(encoding="utf-8"))
    output_curves = {}
    for mass, index, expected_count, expected_color in CURVES:
        drawing = drawings[index]
        if len(drawing["items"]) != expected_count:
            raise ValueError(
                f"m={mass:g} MeV drawing item count changed: {len(drawing['items'])}"
            )
        if drawing["fill"] is not None or not np.allclose(
            drawing["color"], expected_color, rtol=0.0, atol=1e-8
        ):
            raise ValueError(f"m={mass:g} MeV drawing identity/color changed")

        ordered = ordered_polyline(drawing)
        legacy = legacy_polyline(drawing)
        ordered_transformed = transform_pdf_coordinates(ordered)
        legacy_transformed = transform_pdf_coordinates(legacy)
        keep = visible_luminosity_mask(legacy_transformed)
        visible_xy = legacy[keep]
        visible = {key: value[keep] for key, value in legacy_transformed.items()}

        dx = np.diff(ordered[:, 0])
        monotonic_order = bool(np.all(dx >= -1e-7))
        duplicate_x = np.flatnonzero(np.abs(dx) <= 1e-7)
        backwards_x = np.flatnonzero(dx < -1e-7)
        archived = reference["reference_vertices"][str(float(mass))]
        archived_g = np.asarray(archived["g"], float)
        archived_l = np.asarray(archived["luminosity_erg_s"], float)
        if len(archived_g) != len(visible["g"]):
            raise ValueError(
                f"m={mass:g} MeV archived point count {len(archived_g)} "
                f"does not match PDF-derived visible count {len(visible['g'])}"
            )
        g_residual = np.abs(archived_g/visible["g"]-1.0)
        l_residual = np.abs(archived_l/visible["luminosity_erg_s"]-1.0)
        max_g_residual = float(np.max(g_residual))
        max_l_residual = float(np.max(l_residual))
        if max(max_g_residual, max_l_residual) > 1e-10:
            raise ValueError(
                f"m={mass:g} MeV archived digitization does not reconstruct "
                f"from pinned source PDF: g={max_g_residual:g}, L={max_l_residual:g}"
            )

        order_preserved = bool(np.array_equal(
            np.argsort(ordered[:, 0], kind="stable"), np.arange(len(ordered))
        ))
        off_frame = legacy[~keep]
        off_frame_values = transform_pdf_coordinates(off_frame) if len(off_frame) else None
        curve_record = {
            "mass_MeV": mass,
            "drawing_index": index,
            "drawing_color": list(drawing["color"]),
            "source_line_segments": len(drawing["items"]),
            "ordered_source_vertices": len(ordered),
            "legacy_unique_x_vertices": len(legacy),
            "visible_vertices_used_in_reference": len(visible_xy),
            "vertices_outside_luminosity_frame": len(off_frame),
            "source_path_x_monotonic": monotonic_order,
            "legacy_x_sort_preserves_path_order": order_preserved,
            "zero_or_near_zero_dx_segment_count": int(len(duplicate_x)),
            "negative_dx_segment_count": int(len(backwards_x)),
            "min_dx_pdf_points": float(np.min(dx)),
            "max_dx_pdf_points": float(np.max(dx)),
            "raw_path_pdf_bbox": {
                "xmin": float(np.min(ordered[:, 0])),
                "xmax": float(np.max(ordered[:, 0])),
                "ymin": float(np.min(ordered[:, 1])),
                "ymax": float(np.max(ordered[:, 1])),
            },
            "archived_vertices_max_relative_reconstruction_error": {
                "g": max_g_residual,
                "luminosity": max_l_residual,
            },
            "visible_first_point": {
                "pdf_xy": visible_xy[0].tolist(),
                "g": float(visible["g"][0]),
                "luminosity_erg_s": float(visible["luminosity_erg_s"][0]),
            },
            "visible_last_point": {
                "pdf_xy": visible_xy[-1].tolist(),
                "g": float(visible["g"][-1]),
                "luminosity_erg_s": float(visible["luminosity_erg_s"][-1]),
            },
            "last_eight_visible_points_in_increasing_g": [
                {
                    "pdf_x": float(xy[0]),
                    "pdf_y": float(xy[1]),
                    "g": float(g),
                    "luminosity_erg_s": float(l),
                }
                for xy, g, l in zip(
                    visible_xy[-8:],
                    visible["g"][-8:],
                    visible["luminosity_erg_s"][-8:],
                )
            ],
            "off_frame_points": [] if off_frame_values is None else [
                {
                    "pdf_x": float(xy[0]),
                    "pdf_y": float(xy[1]),
                    "g": float(g),
                    "luminosity_erg_s": float(l),
                }
                for xy, g, l in zip(
                    off_frame, off_frame_values["g"],
                    off_frame_values["luminosity_erg_s"],
                )
            ],
        }
        if mass == 10.0:
            high_g_order = np.argsort(ordered_transformed["g"], kind="stable")
            high_g_order = high_g_order[-10:]
            visible_tail_g = visible["g"][-8:]
            visible_tail_l = visible["luminosity_erg_s"][-8:]
            curve_record["high_coupling_tail_audit"] = {
                "source_path_ordered_high_g_tail": [
                    {
                        "pdf_x": float(ordered[i, 0]),
                        "pdf_y": float(ordered[i, 1]),
                        "g": float(ordered_transformed["g"][i]),
                        "luminosity_erg_s": float(ordered_transformed["luminosity_erg_s"][i]),
                        "inside_visible_luminosity_frame": bool(
                            visible_luminosity_mask(ordered_transformed)[i]
                        ),
                    }
                    for i in high_g_order
                ],
                "visible_tail_monotonic_in_g": bool(
                    np.all(np.diff(visible_tail_g) >= -1e-12)
                ),
                "visible_tail_monotonic_in_luminosity": bool(
                    np.all(np.diff(visible_tail_l) <= 1e-12)
                ),
                "first_visible_to_last_visible_luminosity_ratio": float(
                    visible["luminosity_erg_s"][-1]/visible["luminosity_erg_s"][0]
                ),
                "last_visible_to_previous_luminosity_ratio": float(
                    visible["luminosity_erg_s"][-1]/visible["luminosity_erg_s"][-2]
                ) if len(visible["luminosity_erg_s"]) > 1 else None,
            }
        output_curves[str(float(mass))] = curve_record

    words = page.get_text("words")
    text_items = [
        {"text": str(word[4]), "bbox": [float(x) for x in word[:4]]}
        for word in words
    ]
    axis_tick_validation = validate_axis_tick_words(words)
    return {
        "title": "Raw PDF drawing geometry audit of Blinov Fig. 7 digitization",
        "source": {
            "url": "https://arxiv.org/src/2511.09619v2",
            "archive_member": "luminosity_snapshot_t=1.pdf",
            "pdf_sha256": pdf_sha,
            "page_count": document.page_count,
            "page_rect": [float(x) for x in page.rect],
            "drawing_count": len(drawings),
            "reference_json_sha256": sha256(reference_json),
        },
        "axis_frame": frame,
        "axis_frame_residuals_vs_digitization_constants": frame_residuals,
        "axis_geometry": axis_geometry,
        "axis_tick_validation": axis_tick_validation,
        "coordinate_transform": {
            "alpha_V": "10^[-22+16*(x-X_LEFT)/(X_RIGHT-X_LEFT)]",
            "g_mu_tau": "sqrt(4*pi*alpha_V)",
            "luminosity_erg_s": "10^[52+3*(Y_BOTTOM-y)/(Y_BOTTOM-Y_TOP)]",
            "visible_luminosity_window_erg_s": [1e52, 1e55],
            "reference_digitization_clips_only_on_luminosity": True,
        },
        "pdf_text_words": text_items,
        "curves": output_curves,
        "conclusion": (
            "The archived 25-point Fig. 7 vertices are accepted only if their "
            "g and luminosity coordinates reconstruct from the pinned PDF "
            "paths to the stated numerical tolerance. Path order, duplicate-x "
            "segments, visible-frame clipping, and the high-coupling 10 MeV "
            "tail are reported explicitly."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = audit(args.source, args.reference)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    ten = result["curves"]["10.0"]
    print(json.dumps({
        "pdf_sha256": result["source"]["pdf_sha256"],
        "axis_frame": result["axis_frame"],
        "axis_tick_validation": result["axis_tick_validation"],
        "ten_mev": {
            "source_vertices": ten["ordered_source_vertices"],
            "visible_vertices": ten["visible_vertices_used_in_reference"],
            "off_frame_vertices": ten["vertices_outside_luminosity_frame"],
            "x_monotonic": ten["source_path_x_monotonic"],
            "sort_preserves_path_order": ten["legacy_x_sort_preserves_path_order"],
            "duplicate_x_segments": ten["zero_or_near_zero_dx_segment_count"],
            "backwards_x_segments": ten["negative_dx_segment_count"],
            "reconstruction": ten["archived_vertices_max_relative_reconstruction_error"],
            "tail": ten["high_coupling_tail_audit"],
            "off_frame_points": ten["off_frame_points"],
        },
        "output": str(args.output),
    }, indent=2))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
