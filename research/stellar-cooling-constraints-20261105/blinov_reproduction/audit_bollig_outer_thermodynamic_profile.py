#!/usr/bin/env python3
"""Compare Caputo SFHo-18.8 T and mu_mu/T to Bollig Figs. 1 and 4.

Only coordinates inside the original PDF vector paths and plot frames are used.
No extrapolation and no changes to source, opacity, transport, luminosity, or
axial-vector outputs.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path
import urllib.request
import numpy as np
import pymupdf

URL = "https://arxiv.org/pdf/2005.07141v7"
EXPECTED_PDF_SHA256 = "8267f8b1de184163308728c44000425ce58085c1d5bd799d0cbc1e4e8d740d61"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_PROFILE = ROOT / "data" / "sfho188_digitized.csv"
DEFAULT_PDF = HERE / "bollig_2005.07141v7.pdf"
DEFAULT_JSON = HERE / "outputs" / "bollig_outer_thermodynamic_profile_15_22km_2026-11-09.json"
DEFAULT_MD = HERE / "BOLLIG_OUTER_THERMODYNAMIC_PROFILE_15_22KM_2026-11-09.md"
YELLOW = [0.6999970078468323, 0.6999970078468323, 0.0]


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def points_from_drawing(drawing):
    points = []
    for item in drawing["items"]:
        if item[0] != "l":
            raise RuntimeError("Selected curve contains a non-line drawing item")
        points.extend(((float(item[1].x), float(item[1].y)),
                       (float(item[2].x), float(item[2].y))))
    if len(points) < 4:
        raise RuntimeError("Selected curve has too few vector vertices")
    out = []
    for x, y in sorted(points, key=lambda p: p[0]):
        if not out or abs(x - out[-1][0]) > 1e-8:
            out.append((x, y))
        else:
            out[-1] = (x, y)
    return np.asarray(out, dtype=float)


def linear_map(pdf_coordinates, physical_values):
    slope, intercept = np.polyfit(np.asarray(physical_values, float),
                                  np.asarray(pdf_coordinates, float), 1)
    return float(intercept), float(slope)


def find_horizontal_frame(drawings, y_reference):
    candidates = []
    for drawing in drawings:
        for item in drawing["items"]:
            if item[0] != "l":
                continue
            x1, y1 = float(item[1].x), float(item[1].y)
            x2, y2 = float(item[2].x), float(item[2].y)
            if abs(y1-y2) <= 0.25 and abs(y1-y_reference) <= 1.5 and abs(x2-x1) >= 100:
                candidates.append((abs(x2-x1), min(x1,x2), max(x1,x2), 0.5*(y1+y2)))
    if not candidates:
        return None
    length, xmin, xmax, y = max(candidates)
    return {"x_min_pdf": xmin, "x_max_pdf": xmax, "y_pdf": y, "length_pdf": length}


def read_profile(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    required = {"r_km", "T_MeV", "mu_mu_MeV"}
    if not rows or not required.issubset(rows[0]):
        raise RuntimeError("Profile lacks r_km, T_MeV, or mu_mu_MeV")
    out = []
    for row in rows:
        r, t, mu = float(row["r_km"]), float(row["T_MeV"]), float(row["mu_mu_MeV"])
        if t > 0:
            out.append({"r_km": r, "T_MeV": t, "mu_mu_MeV": mu, "eta": mu/t})
    return out


def support(points, x0, dx, frame):
    xmin, xmax = float(points[:,0].min()), float(points[:,0].max())
    if frame is None:
        lo, hi = xmin, xmax
        frame_info = None
    else:
        lo, hi = max(xmin, frame["x_min_pdf"]), min(xmax, frame["x_max_pdf"])
        frame_info = frame
    usable = [(lo-x0)/dx, (hi-x0)/dx] if hi >= lo else None
    return {
        "path_x_pdf": [xmin, xmax],
        "path_radius_km": [(xmin-x0)/dx, (xmax-x0)/dx],
        "frame": frame_info,
        "usable_radius_km": usable,
    }


def value_at(points, radius, x0, dx, y0, dy, curve_support):
    usable = curve_support["usable_radius_km"]
    if usable is None or radius < usable[0]-1e-9 or radius > usable[1]+1e-9:
        return None
    x_pdf = x0 + dx*radius
    y_pdf = float(np.interp(x_pdf, points[:,0], points[:,1]))
    return float((y_pdf-y0)/dy)


def summarize(rows, bkey, ckey, threshold=0.0):
    valid = [x for x in rows if x[bkey] is not None and x[ckey] is not None]
    if not valid:
        return {
            "count": 0,
            "radial_range_km": None,
            "mean_absolute_difference": None,
            "rms_difference": None,
            "maximum_absolute_difference": None,
            "minimum_signed_difference": None,
            "maximum_signed_difference": None,
            "relative_denominator_threshold": float(threshold),
            "relative_count": 0,
            "mean_absolute_relative_difference": None,
            "maximum_absolute_relative_difference": None,
            "minimum_relative_difference": None,
            "maximum_relative_difference": None,
        }
    b = np.asarray([x[bkey] for x in valid], float)
    c = np.asarray([x[ckey] for x in valid], float)
    delta = c-b
    mask = np.abs(b) > threshold
    rel = c[mask]/b[mask]-1 if np.any(mask) else np.asarray([])
    return {
        "count": int(len(valid)),
        "radial_range_km": [float(valid[0]["r_km"]), float(valid[-1]["r_km"])],
        "mean_absolute_difference": float(np.mean(np.abs(delta))),
        "rms_difference": float(np.sqrt(np.mean(delta*delta))),
        "maximum_absolute_difference": float(np.max(np.abs(delta))),
        "minimum_signed_difference": float(np.min(delta)),
        "maximum_signed_difference": float(np.max(delta)),
        "relative_denominator_threshold": float(threshold),
        "relative_count": int(len(rel)),
        "mean_absolute_relative_difference": float(np.mean(np.abs(rel))) if len(rel) else None,
        "maximum_absolute_relative_difference": float(np.max(np.abs(rel))) if len(rel) else None,
        "minimum_relative_difference": float(np.min(rel)) if len(rel) else None,
        "maximum_relative_difference": float(np.max(rel)) if len(rel) else None,
    }


def run(profile_path=DEFAULT_PROFILE, pdf_path=DEFAULT_PDF):
    profile_path, pdf_path = Path(profile_path), Path(pdf_path)
    if not pdf_path.exists():
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(URL, pdf_path)
    pdf_hash = sha256(pdf_path)
    if pdf_hash != EXPECTED_PDF_SHA256:
        raise RuntimeError("Unexpected Bollig PDF SHA-256: " + pdf_hash)

    doc = pymupdf.open(pdf_path)
    page1, page4 = doc[1], doc[2]
    drawings1, drawings4 = page1.get_drawings(), page4.get_drawings()
    d1, d4 = drawings1[0], drawings4[193]
    color1 = [float(x) for x in d1["color"]]
    color4 = [float(x) for x in d4["color"]]
    if color1 != YELLOW or color4 != YELLOW:
        raise RuntimeError("SFHo-18.8 yellow-curve identity check failed")

    fig1, fig4 = points_from_drawing(d1), points_from_drawing(d4)
    x1, dx1 = linear_map(
        [389.2326354980469, 442.63973974609375, 496.04840087890625, 549.4555053710938],
        [5.0, 10.0, 15.0, 20.0])
    y1, dy1 = linear_map(
        [177.6042938232422, 158.30784606933594, 139.01141357421875,
         119.71297454833984, 100.41653442382812, 81.12008666992188, 61.8236],
        [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0])
    x4, dx4 = linear_map(
        [390.42822265625, 443.4383544921875, 496.4469299316406, 549.4570922851562],
        [5.0, 10.0, 15.0, 20.0])
    y4, dy4 = linear_map(
        [291.43780517578125, 263.7730712890625, 236.10794067382812,
         208.44161987304688, 180.77688598632812],
        [-4.0, -2.0, 0.0, 2.0, 4.0])

    frame1 = find_horizontal_frame(drawings1, 177.6042938232422)
    frame4 = find_horizontal_frame(drawings4, 291.43780517578125)
    support1 = support(fig1, x1, dx1, frame1)
    support4 = support(fig4, x4, dx4, frame4)
    profile = read_profile(profile_path)

    intervals = {"15_20km": [15.0, 20.0], "20_22km": [20.0, 22.0]}
    results = {}
    for name, (lo, hi) in intervals.items():
        rows = []
        for item in profile:
            r = item["r_km"]
            if r < lo-1e-9 or r > hi+1e-9:
                continue
            tb = value_at(fig1, r, x1, dx1, y1, dy1, support1)
            eb = value_at(fig4, r, x4, dx4, y4, dy4, support4)
            mub = tb*eb if tb is not None and eb is not None else None
            rows.append({
                "r_km": r,
                "T_Bollig_MeV": tb,
                "T_Caputo_MeV": item["T_MeV"] if tb is not None else None,
                "eta_Bollig": eb,
                "eta_Caputo": item["eta"] if eb is not None else None,
                "mu_mu_Bollig_derived_MeV": mub,
                "mu_mu_Caputo_MeV": item["mu_mu_MeV"] if mub is not None else None,
            })
        results[name] = {
            "requested_interval_km": [lo, hi],
            "T_comparison": summarize(rows, "T_Bollig_MeV", "T_Caputo_MeV", 1e-12),
            "mu_over_T_comparison": summarize(rows, "eta_Bollig", "eta_Caputo", 0.1),
            "mu_mu_derived_comparison": summarize(rows, "mu_mu_Bollig_derived_MeV", "mu_mu_Caputo_MeV", 1.0),
            "rows": rows,
        }

    selected = []
    for target in (15.0,16.0,17.0,18.0,19.0,20.0,20.5,21.0,21.5,22.0):
        item = min(profile, key=lambda p: abs(p["r_km"]-target))
        r = item["r_km"]
        tb = value_at(fig1, r, x1, dx1, y1, dy1, support1)
        eb = value_at(fig4, r, x4, dx4, y4, dy4, support4)
        selected.append({
            "target_radius_km": target,
            "profile_node_radius_km": r,
            "T_Bollig_MeV": tb,
            "T_Caputo_MeV": item["T_MeV"] if tb is not None else None,
            "eta_Bollig": eb,
            "eta_Caputo": item["eta"] if eb is not None else None,
            "mu_mu_Bollig_derived_MeV": tb*eb if tb is not None and eb is not None else None,
            "mu_mu_Caputo_MeV": item["mu_mu_MeV"] if tb is not None and eb is not None else None,
        })

    joint = None
    if support1["usable_radius_km"] and support4["usable_radius_km"]:
        joint = [max(support1["usable_radius_km"][0], support4["usable_radius_km"][0]),
                 min(support1["usable_radius_km"][1], support4["usable_radius_km"][1])]
    return {
        "source": "Bollig et al., arXiv:2005.07141v7",
        "source_pdf_url": URL,
        "source_pdf_sha256": pdf_hash,
        "profile_sha256": sha256(profile_path),
        "profile_node_count": len(profile),
        "profile_radial_range_km": [profile[0]["r_km"], profile[-1]["r_km"]],
        "selected_curves": {
            "fig1_temperature": {"page_index": 1, "drawing_index": 0, "color": color1},
            "fig4_mu_over_T": {"page_index": 2, "drawing_index": 193, "color": color4},
        },
        "curve_support": {
            "fig1_temperature": support1,
            "fig4_mu_over_T": support4,
            "joint_usable_radius_km": joint,
        },
        "intervals": results,
        "selected_radii": selected,
        "policy": {
            "no_extrapolation": True,
            "only_points_inside_source_vector_path_and_detected_plot_frame_are_compared": True,
            "eta_relative_residual_uses_abs_Bollig_eta_greater_than_0p1": True,
            "mu_mu_relative_residual_uses_abs_derived_Bollig_mu_greater_than_1MeV": True,
            "mu_mu_Bollig_is_derived_from_fig1_T_times_fig4_eta": True,
            "production_and_axial_outputs_modified": False,
        },
    }


def make_report(data):
    def pct(x):
        return "n/a" if x is None else f"{100*x:.6g}%"
    lines = [
        "# Bollig original-source thermodynamic profile audit: 15--22 km",
        "",
        "Date: 2026-11-09",
        "Source: Bollig et al., arXiv:2005.07141v7, Figs. 1 and 4.",
        "",
        "## Scope",
        "",
        "This extends the original-PDF vector-path comparison beyond the previously checked 5--15 km interval. It compares Caputo T(r) with Bollig Fig. 1 and Caputo mu_mu/T with Bollig Fig. 4. The combined mu_mu comparison is derived from T_Bollig times (mu_mu/T)_Bollig; it is not an independent third observable.",
        "",
        "Only points inside the actual selected vector-path support and detected plot frame are compared. No extrapolation is performed. The original Garching simulation tables were not obtained in this audit.",
        "",
        "## Source and curve support",
        "",
        f"- Bollig PDF SHA-256: {data['source_pdf_sha256']}",
        f"- Caputo profile SHA-256: {data['profile_sha256']}",
        f"- Fig. 1: page 1, drawing path 0, color {data['selected_curves']['fig1_temperature']['color']}.",
        f"- Fig. 4: page 2, drawing path 193, color {data['selected_curves']['fig4_mu_over_T']['color']}.",
        f"- Fig. 1 usable radial support: {data['curve_support']['fig1_temperature']['usable_radius_km']} km.",
        f"- Fig. 4 usable radial support: {data['curve_support']['fig4_mu_over_T']['usable_radius_km']} km.",
        f"- Joint usable radial support: {data['curve_support']['joint_usable_radius_km']} km.",
        "",
        "## Interval results",
        "",
        "| Interval | Observable | Nodes | Mean abs. relative difference | Max abs. relative difference |",
        "|---|---|---:|---:|---:|",
    ]
    labels = [
        ("T_comparison", "T(r), Caputo vs Bollig Fig. 1"),
        ("mu_over_T_comparison", "mu_mu/T, Caputo vs Bollig Fig. 4"),
        ("mu_mu_derived_comparison", "mu_mu derived from T x mu_mu/T"),
    ]
    for interval, result in data["intervals"].items():
        for key, label in labels:
            s = result[key]
            lines.append(
                f"| {result['requested_interval_km'][0]:g}--{result['requested_interval_km'][1]:g} km | {label} | {s['count']} | {pct(s['mean_absolute_relative_difference'])} | {pct(s['maximum_absolute_relative_difference'])} |"
            )
    lines.extend([
        "",
        "## Selected radii",
        "",
        "| target r (km) | profile node (km) | T_Bollig | T_Caputo | eta_Bollig | eta_Caputo | mu_mu,Bollig derived | mu_mu,Caputo |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for x in data["selected_radii"]:
        def fmt(v):
            return "not covered" if v is None else f"{v:.7g}"
        lines.append(
            f"| {x['target_radius_km']:g} | {x['profile_node_radius_km']:.7g} | {fmt(x['T_Bollig_MeV'])} | {fmt(x['T_Caputo_MeV'])} | {fmt(x['eta_Bollig'])} | {fmt(x['eta_Caputo'])} | {fmt(x['mu_mu_Bollig_derived_MeV'])} | {fmt(x['mu_mu_Caputo_MeV'])} |"
        )
    lines.extend([
        "",
        "## Interpretation",
        "",
        "Zero supported nodes mean the original published vector curve does not cover that radial interval. This is not a failed numerical comparison: it is a lack of source coverage. Such a region must remain unvalidated by the published figure and must not be filled by extrapolation.",
        "",
        "The 20--22 km interval must be classified separately from the 15--20 km interval. The reconstructed CSV can contain values there even when the original comparison curve does not.",
        "",
        "No production rate, opacity, transport implementation, luminosity, vector benchmark, or axial-vector output is changed.",
        "",
        "## Reproducibility",
        "",
        "- Script: audit_bollig_outer_thermodynamic_profile.py",
        "- Machine-readable output: outputs/bollig_outer_thermodynamic_profile_15_22km_2026-11-09.json",
        "- PDF source: https://arxiv.org/pdf/2005.07141v7",
        "",
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    data = run(args.profile, args.pdf)
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.output_md.write_text(make_report(data), encoding="utf-8")
    print(json.dumps({
        "source_pdf_sha256": data["source_pdf_sha256"],
        "profile_sha256": data["profile_sha256"],
        "curve_support": data["curve_support"],
        "interval_summaries": {
            name: {key: value for key, value in result.items() if key != "rows"}
            for name, result in data["intervals"].items()
        },
        "selected_radii": data["selected_radii"],
        "json": str(args.output_json),
        "report": str(args.output_md),
    }, indent=2))


if __name__ == "__main__":
    main()
