"""Digitize Croon Fig. 2 vector curves using the extracted PDF path inventory.

The axes are calibrated from the major tick marks. The PDF's legend text is
black, so curve identity is assigned from the measured vector-stroke palette
and checked against the in-plot label positions. The black dashed curve is
retained separately as the R_far=R_nu variant.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "outputs" / "croon_fig2_vector_paths_2026-11-19.json"
DEFAULT_CSV = HERE / "outputs" / "croon_fig2_digitized_curves_2026-11-19.csv"
DEFAULT_JSON = HERE / "outputs" / "croon_fig2_digitized_curves_2026-11-19.json"

MASS_LABELS = ("200 MeV", "10 MeV", "0.1 MeV", "10 eV", "1 eV", "0.1 eV")
MASS_VALUES_MEV = {
    "200 MeV": 200.0,
    "10 MeV": 10.0,
    "0.1 MeV": 0.1,
    "10 eV": 1.0e-5,
    "1 eV": 1.0e-6,
    "0.1 eV": 1.0e-7,
}
# The PDF's legend text is black; the curve strokes carry the mass palette.
# These are the measured vector stroke colours from the source PDF.
MASS_STROKE_RGB = {
    "200 MeV": (0.0, 1.0, 1.0),
    "10 MeV": (0.0078431377, 0.9686274529, 0.4901960790),
    "0.1 MeV": (0.0, 0.0, 1.0),
    "10 eV": (1.0, 0.6470588446, 0.0),
    "1 eV": (1.0, 0.0, 0.0),
    "0.1 eV": (0.0, 0.0, 0.0),
}


def _rgb_from_int(value: int) -> np.ndarray:
    return np.asarray([
        (value >> 16) & 255,
        (value >> 8) & 255,
        value & 255,
    ], dtype=float) / 255.0


def _colour_distance(a, b) -> float:
    return float(np.linalg.norm(np.asarray(a, float)-np.asarray(b, float)))


def _near(a: float, b: float, tolerance: float) -> bool:
    return abs(float(a)-float(b)) <= tolerance


def calibrate_axes(paths: list[dict]) -> dict:
    black = [
        p for p in paths
        if p.get("stroke_rgb") is not None
        and max(p["stroke_rgb"]) < 0.03
        and p.get("width") is not None
        and p["width"] < 1.0
    ]
    vertical = [
        p for p in black
        if abs(p["rect"][2]-p["rect"][0]) < 0.02
        and p["rect"][3]-p["rect"][1] > 150.0
    ]
    horizontal = [
        p for p in black
        if abs(p["rect"][3]-p["rect"][1]) < 0.02
        and p["rect"][2]-p["rect"][0] > 300.0
    ]
    if len(vertical) < 2 or len(horizontal) < 2:
        raise RuntimeError("Could not identify the rectangular plot frame")
    left = min(vertical, key=lambda p: p["rect"][0])
    right = max(vertical, key=lambda p: p["rect"][0])
    bottom = max(horizontal, key=lambda p: p["rect"][1])
    top = min(horizontal, key=lambda p: p["rect"][1])
    x0, x1 = left["rect"][0], right["rect"][0]
    y0, y1 = top["rect"][1], bottom["rect"][1]

    x_ticks = [
        p for p in black
        if abs(p["rect"][2]-p["rect"][0]) < 0.02
        and 5.0 <= p["rect"][3]-p["rect"][1] <= 6.5
        and _near(p["rect"][3], y1, 0.02)
    ]
    x_ticks = sorted(x_ticks, key=lambda p: p["rect"][0])
    if len(x_ticks) != 6:
        raise RuntimeError(f"Expected 6 major x ticks, found {len(x_ticks)}")

    y_ticks = [
        p for p in black
        if abs(p["rect"][3]-p["rect"][1]) < 0.02
        and 5.0 <= p["rect"][2]-p["rect"][0] <= 6.5
        and _near(p["rect"][0], x0, 0.02)
    ]
    y_ticks = sorted(y_ticks, key=lambda p: p["rect"][1])
    if len(y_ticks) != 5:
        raise RuntimeError(f"Expected 5 major y ticks, found {len(y_ticks)}")

    x_positions = np.asarray([0.5*(p["rect"][0]+p["rect"][2]) for p in x_ticks])
    x_logg = np.asarray([-11., -9., -7., -5., -3., -1.])
    y_positions = np.asarray([0.5*(p["rect"][1]+p["rect"][3]) for p in y_ticks])
    y_logL = np.asarray([55., 54., 53., 52., 51.])
    x_slope, x_intercept = np.polyfit(x_positions, x_logg, 1)
    y_slope, y_intercept = np.polyfit(y_positions, y_logL, 1)

    return {
        "plot_rect_pdf_points": [float(x0), float(y0), float(x1), float(y1)],
        "x_major_tick_positions_pdf": x_positions.tolist(),
        "x_major_tick_log10_g": x_logg.tolist(),
        "x_log10_g_from_pdf_x": {
            "slope": float(x_slope), "intercept": float(x_intercept)
        },
        "y_major_tick_positions_pdf": y_positions.tolist(),
        "y_major_tick_log10_L": y_logL.tolist(),
        "y_log10_L_from_pdf_y": {
            "slope": float(y_slope), "intercept": float(y_intercept)
        },
        "x_tick_fit_max_abs_residual_dex": float(np.max(np.abs(
            x_slope*x_positions+x_intercept-x_logg
        ))),
        "y_tick_fit_max_abs_residual_dex": float(np.max(np.abs(
            y_slope*y_positions+y_intercept-y_logL
        ))),
    }


def match_label_paths(
    text_spans: list[dict], paths: list[dict], axes: dict | None = None
) -> dict:
    """Match each in-plot mass label to one unique source-PDF vector curve.

    The legend text itself is black. Curve identities therefore use the
    measured PDF stroke palette, while the text-span bounding boxes establish
    that the matching mass labels are actually inside the plot panel.
    """
    labels = {}
    selected_path_indices: set[int] = set()
    plot_rect = axes["plot_rect_pdf_points"] if axes is not None else None
    for label in MASS_LABELS:
        candidates = []
        for span in text_spans:
            if span["text"].strip() != label:
                continue
            if plot_rect is not None:
                bbox = span.get("bbox")
                if bbox is None or len(bbox) != 4:
                    continue
                cx = 0.5 * (float(bbox[0]) + float(bbox[2]))
                cy = 0.5 * (float(bbox[1]) + float(bbox[3]))
                x0, y0, x1, y1 = plot_rect
                if not (x0 <= cx <= x1 and y0 <= cy <= y1):
                    continue
            candidates.append(span)
        if len(candidates) != 1:
            raise RuntimeError(
                f"Expected one in-plot mass label {label!r}, found {len(candidates)}"
            )

        target = np.asarray(MASS_STROKE_RGB[label], dtype=float)
        eligible = [
            p for p in paths
            if p.get("stroke_rgb") is not None
            and p.get("flattened_points")
            and p["rect"][2]-p["rect"][0] > 50.0
            and p["rect"][3]-p["rect"][1] > 50.0
        ]
        if label == "0.1 eV":
            eligible = [
                p for p in eligible
                if max(p["stroke_rgb"]) < 0.03 and p.get("dashes") == "[] 0"
            ]
        else:
            eligible = [
                p for p in eligible
                if p.get("dashes") in (None, "[] 0")
                and max(p["stroke_rgb"]) > 0.05
            ]
        scored = [
            (_colour_distance(p["stroke_rgb"], target), p)
            for p in eligible
        ]
        if not scored:
            raise RuntimeError(f"No eligible vector path found for label {label!r}")
        scored.sort(key=lambda item: item[0])
        distance, chosen = scored[0]
        if distance > 0.03:
            raise RuntimeError(
                f"Could not match label {label!r} to a vector path "
                f"(stroke-colour distance {distance})"
            )
        if len(scored) > 1 and abs(scored[1][0]-distance) < 1e-8:
            raise RuntimeError(
                f"Ambiguous curve matching for label {label!r}: "
                f"paths {chosen['index']} and {scored[1][1]['index']}"
            )
        chosen_index = int(chosen["index"])
        if chosen_index in selected_path_indices:
            raise RuntimeError(
                f"Ambiguous curve matching: labels already selected vector path {chosen_index}"
            )
        selected_path_indices.add(chosen_index)
        labels[label] = {
            "path_index": chosen_index,
            "colour_distance": float(distance),
            "label_stroke_rgb": target.tolist(),
            "path_colour_rgb": chosen["stroke_rgb"],
            "legend_text_colour_rgb": _rgb_from_int(candidates[0]["color"]).tolist(),
        }
    return labels


def _clip_segment_to_rect(
    p0: tuple[float, float],
    p1: tuple[float, float],
    rect: tuple[float, float, float, float],
) -> tuple[tuple[float, float], tuple[float, float], float, float] | None:
    """Liang-Barsky clip of one PDF-coordinate segment to the plot rectangle."""
    x0, y0, x1, y1 = rect
    ax, ay = p0
    bx, by = p1
    dx, dy = bx-ax, by-ay
    p = (-dx, dx, -dy, dy)
    q = (ax-x0, x1-ax, ay-y0, y1-ay)
    t0, t1 = 0.0, 1.0
    for pi, qi in zip(p, q):
        if abs(pi) < 1e-15:
            if qi < 0.0:
                return None
            continue
        ratio = qi/pi
        if pi < 0.0:
            t0 = max(t0, ratio)
        else:
            t1 = min(t1, ratio)
        if t0 > t1:
            return None
    start = (ax+t0*dx, ay+t0*dy)
    stop = (ax+t1*dx, ay+t1*dy)
    return start, stop, float(t0), float(t1)


def digitize_points(points: list[list[float]], axes: dict) -> list[dict]:
    """Clip every vector segment to the plot before converting PDF to log axes.

    Merely retaining vertices inside the frame loses curve portions whose
    endpoints lie outside the frame. Intersections with the frame are inserted
    by segment clipping, which is essential for Raffelt-line crossings.
    """
    rect = tuple(float(x) for x in axes["plot_rect_pdf_points"])
    xs = axes["x_log10_g_from_pdf_x"]
    ys = axes["y_log10_L_from_pdf_y"]
    out: list[dict] = []

    def append_point(x: float, y: float, segment_index: int, segment_t: float) -> None:
        if out and abs(out[-1]["pdf_x"]-x) < 1e-10 and abs(out[-1]["pdf_y"]-y) < 1e-10:
            return
        logg = xs["slope"]*x + xs["intercept"]
        logL = ys["slope"]*y + ys["intercept"]
        out.append({
            "point_index": int(segment_index),
            "segment_index": int(segment_index),
            "segment_t": float(segment_t),
            "pdf_x": float(x),
            "pdf_y": float(y),
            "log10_g": float(logg),
            "log10_L_erg_s": float(logL),
            "g": float(10.0**logg),
            "L_erg_s": float(10.0**logL),
        })

    for index, (p0, p1) in enumerate(zip(points[:-1], points[1:])):
        clipped = _clip_segment_to_rect(
            (float(p0[0]), float(p0[1])),
            (float(p1[0]), float(p1[1])),
            rect,
        )
        if clipped is None:
            continue
        start, stop, t0, t1 = clipped
        append_point(start[0], start[1], index, t0)
        append_point(stop[0], stop[1], index, t1)
    return out


def run(input_path: Path = DEFAULT_INPUT, csv_path: Path = DEFAULT_CSV,
        json_path: Path = DEFAULT_JSON) -> dict:
    source = json.loads(input_path.read_text(encoding="utf-8"))
    paths = source["vector_paths"]
    axes = calibrate_axes(paths)
    label_matches = match_label_paths(source["text_spans"], paths, axes)
    by_index = {p["index"]: p for p in paths}

    curves = {}
    csv_rows = []
    for label in MASS_LABELS:
        match = label_matches[label]
        path = by_index[match["path_index"]]
        points = digitize_points(path["flattened_points"], axes)
        curves[label] = {
            "mass_MeV": MASS_VALUES_MEV[label],
            "source_path_index": match["path_index"],
            "colour_distance": match["colour_distance"],
            "stroke_rgb": path["stroke_rgb"],
            "dashes": path["dashes"],
            "point_count_inside_axes": len(points),
            "points": points,
        }
        for row in points:
            csv_rows.append({
                "curve": label,
                "mass_MeV": MASS_VALUES_MEV[label],
                "variant": "Rfar=100km",
                **row,
            })

    # The black dashed path is the explicitly shown R_far=R_nu sensitivity.
    black_solid_index = label_matches["0.1 eV"]["path_index"]
    black_dashed = [
        p for p in paths
        if p.get("stroke_rgb") == [0.0, 0.0, 0.0]
        and p["index"] != black_solid_index
        and p.get("dashes") not in (None, "[] 0")
        and p.get("flattened_points")
        and p["rect"][2]-p["rect"][0] > 100.0
        and p["rect"][3]-p["rect"][1] > 50.0
    ]
    if len(black_dashed) != 1:
        raise RuntimeError(f"Expected one black dashed Rfar=Rnu path, found {len(black_dashed)}")
    dashed_points = digitize_points(black_dashed[0]["flattened_points"], axes)
    curves["0.1 eV (Rfar=Rnu)"] = {
        "mass_MeV": MASS_VALUES_MEV["0.1 eV"],
        "source_path_index": int(black_dashed[0]["index"]),
        "colour_distance": 0.0,
        "stroke_rgb": black_dashed[0]["stroke_rgb"],
        "dashes": black_dashed[0]["dashes"],
        "point_count_inside_axes": len(dashed_points),
        "points": dashed_points,
    }
    for row in dashed_points:
        csv_rows.append({
            "curve": "0.1 eV (Rfar=Rnu)",
            "mass_MeV": MASS_VALUES_MEV["0.1 eV"],
            "variant": "Rfar=Rnu",
            **row,
        })

    # The magenta horizontal line is the SN1987A 3e52 erg/s reference.
    magenta = [
        p for p in paths
        if p.get("stroke_rgb") is not None
        and p["stroke_rgb"][0] > 0.9 and p["stroke_rgb"][2] > 0.9
        and p["rect"][2]-p["rect"][0] > 300.0
        and p["rect"][3]-p["rect"][1] < 0.1
    ]
    if len(magenta) != 1:
        raise RuntimeError(f"Expected one magenta SN1987A line, found {len(magenta)}")
    sn_line = digitize_points(magenta[0]["flattened_points"], axes)
    sn_logL = float(np.mean([p["log10_L_erg_s"] for p in sn_line]))

    result = {
        "source_pdf_sha256": source["pdf_sha256"],
        "source_page_index": source["page_index"],
        "axis_calibration": axes,
        "curve_label_path_matches": label_matches,
        "curves": curves,
        "SN1987A_reference_line": {
            "source_path_index": int(magenta[0]["index"]),
            "log10_L_erg_s": sn_logL,
            "L_erg_s": float(10.0**sn_logL),
            "expected_reference_erg_s": 3.0e52,
            "relative_difference_from_3e52": float(10.0**sn_logL/3.0e52-1.0),
        },
        "scope": "vector-curve points digitized from the published Croon Fig. 2 PDF; no interpolation or rescaling of theoretical curves",
    }
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        writer.writeheader()
        writer.writerows(csv_rows)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()
    result = run(args.input, args.csv, args.json)
    print(json.dumps({
        "axis_calibration": result["axis_calibration"],
        "curve_counts": {
            name: curve["point_count_inside_axes"]
            for name, curve in result["curves"].items()
        },
        "SN1987A_reference_line": result["SN1987A_reference_line"],
        "csv": str(args.csv),
        "json": str(args.json),
    }, indent=2))


if __name__ == "__main__":
    main()
