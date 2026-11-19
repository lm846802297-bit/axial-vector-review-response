"""Digitize Croon Fig. 2 vector curves using the extracted PDF path inventory.

The axes are calibrated from the major tick marks and their printed labels.
Mass-to-colour matching is based on the colours of the in-plot text labels.
The black dashed curve is retained separately as the R_far=R_nu variant.
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


def match_label_paths(text_spans: list[dict], paths: list[dict]) -> dict:
    labels = {}
    for label in MASS_LABELS:
        candidates = [s for s in text_spans if s["text"].strip() == label]
        if len(candidates) != 1:
            raise RuntimeError(f"Expected one in-plot colour label {label!r}, found {len(candidates)}")
        target = _rgb_from_int(candidates[0]["color"])
        scored = [
            (_colour_distance(p["stroke_rgb"], target), p)
            for p in paths if p.get("stroke_rgb") is not None
            and p.get("flattened_points")
        ]
        distance, chosen = min(scored, key=lambda item: item[0])
        if distance > 0.35:
            raise RuntimeError(f"Could not match label {label!r} to a vector path (colour distance {distance})")
        labels[label] = {
            "path_index": int(chosen["index"]),
            "colour_distance": float(distance),
            "label_colour_rgb": target.tolist(),
            "path_colour_rgb": chosen["stroke_rgb"],
        }
    return labels


def digitize_points(points: list[list[float]], axes: dict) -> list[dict]:
    x0, y0, x1, y1 = axes["plot_rect_pdf_points"]
    xs = axes["x_log10_g_from_pdf_x"]
    ys = axes["y_log10_L_from_pdf_y"]
    out = []
    for index, (x, y) in enumerate(points):
        if x < x0-1e-6 or x > x1+1e-6 or y < y0-1e-6 or y > y1+1e-6:
            continue
        logg = xs["slope"]*x + xs["intercept"]
        logL = ys["slope"]*y + ys["intercept"]
        out.append({
            "point_index": int(index),
            "pdf_x": float(x),
            "pdf_y": float(y),
            "log10_g": float(logg),
            "log10_L_erg_s": float(logL),
            "g": float(10.0**logg),
            "L_erg_s": float(10.0**logL),
        })
    return out


def run(input_path: Path = DEFAULT_INPUT, csv_path: Path = DEFAULT_CSV,
        json_path: Path = DEFAULT_JSON) -> dict:
    source = json.loads(input_path.read_text(encoding="utf-8"))
    paths = source["vector_paths"]
    axes = calibrate_axes(paths)
    label_matches = match_label_paths(source["text_spans"], paths)
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
