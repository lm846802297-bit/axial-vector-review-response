"""Audit the SFHo-18.8 public-figure reconstruction in the 12--15 km region.

This script is deliberately diagnostic. It does not alter rates or transport.
It checks the source-PDF drawing-path identity, compares independent published
profiles, checks the Caputo muon density against its own plotted density curve,
and quantifies the local sensitivity to the plotted muon-neutrino chemical
potential floor and to the alternative muon-chemical-potential digitization.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pymupdf

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import extract_profile as ep
from blinov_reproduction.reference import (
    M_MU, fermi_pair_average, negative_muon_density_and_degeneracy,
)

RADII = (8.0, 9.0, 10.0, 11.0, 12.0, 12.5, 13.0, 13.1, 13.15, 13.5, 14.0, 14.5, 15.0, 16.0, 18.0, 20.0)
ENERGIES = (12.0, 15.0, 20.0, 30.0, 50.0, 80.0, 100.0)
N0_FM3 = 0.181
HBARC_MEV_FM = 197.3269804
CAPUTO_TOP_PANEL = {"x0": 47.52, "x1": 324.0}
FERREIRA_MUMU_PANEL = {
    "x0": 378.199, "x1": 637.547,
    "y50": 300.168, "y300": 183.070,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_curve(path: Path) -> np.ndarray:
    return np.genfromtxt(path, delimiter=",", names=True)


def interp_curve(curve: np.ndarray, radius: float) -> float:
    return float(np.interp(radius, curve["r_km"], curve["value"]))


def line_points(drawing):
    """Return points for all-line PDF paths; skip non-polyline drawing items."""
    points = []
    for item in drawing["items"]:
        if item[0] != "l":
            return None
        points.extend((tuple(item[1]), tuple(item[2])))
    if len(points) < 4:
        return None
    points = np.asarray(points, dtype=float)
    points = points[np.argsort(points[:, 0], kind="stable")]
    _, keep = np.unique(points[:, 0], return_index=True)
    return points[np.sort(keep)]


def drawing_record(page, index: int, sample_mapping=None, sample_radii=RADII):
    drawings = page.get_drawings()
    d = drawings[index]
    pts = line_points(d)
    record = {
        "index": index,
        "rect": [float(x) for x in d["rect"]],
        "color": list(d["color"]) if d.get("color") is not None else None,
        "fill": list(d["fill"]) if d.get("fill") is not None else None,
        "width": float(d["width"]) if d.get("width") is not None else None,
        "dashes": d.get("dashes"),
        "type": d.get("type"),
        "item_count": len(d["items"]),
        "is_all_line_polyline": pts is not None,
    }
    if pts is not None:
        record["point_count"] = int(len(pts))
        record["x_range_pdf"] = [float(pts[0, 0]), float(pts[-1, 0])]
        record["y_range_pdf"] = [float(np.min(pts[:, 1])), float(np.max(pts[:, 1]))]
        if sample_mapping == "ferreira_mu_mu":
            x0, x1 = FERREIRA_MUMU_PANEL["x0"], FERREIRA_MUMU_PANEL["x1"]
            y50, y300 = FERREIRA_MUMU_PANEL["y50"], FERREIRA_MUMU_PANEL["y300"]
            r = (pts[:, 0] - x0) * 20.0 / (x1 - x0)
            value = 50.0 + (y50 - pts[:, 1]) * 250.0 / (y50 - y300)
            field = "sample_mu_MeV"
        elif sample_mapping == "caputo_mu_mu":
            x0, x1 = CAPUTO_TOP_PANEL["x0"], CAPUTO_TOP_PANEL["x1"]
            r = 0.1 + (pts[:, 0] - x0) * 19.9 / (x1 - x0)
            value = 10.0 ** (
                (215.559 - pts[:, 1]) / ((215.559 - 56.180) / 2.0)
            )
            field = "sample_mu_MeV"
        else:
            return record
        order = np.argsort(r)
        r, value = r[order], value[order]
        keep = (r >= 0.0) & (r <= 20.0)
        r, value = r[keep], value[keep]
        if len(r) > 1:
            ur, ui = np.unique(r, return_index=True)
            r, value = ur, value[ui]
            record[field] = {
                f"{rr:g}": float(np.interp(rr, r, value))
                if r[0] <= rr <= r[-1] else None
                for rr in sample_radii
            }
    return record

def candidate_drawings(page, x0, x1, y0, y1, sample_mapping=None):
    candidates = []
    for index, d in enumerate(page.get_drawings()):
        pts = line_points(d)
        if pts is None or len(pts) < 12:
            continue
        rect = [float(x) for x in d["rect"]]
        if rect[2] - rect[0] < 100.0:
            continue
        if rect[2] <= x0 or rect[0] >= x1 or rect[3] <= y0 or rect[1] >= y1:
            continue
        if rect[1] < y0 - 25.0 or rect[3] > y1 + 25.0:
            continue
        rec = drawing_record(page, index, sample_mapping=sample_mapping)
        if rec.get("point_count", 0) >= 12:
            candidates.append(rec)
    candidates.sort(key=lambda x: (x["rect"][2] - x["rect"][0], x["point_count"]), reverse=True)
    return candidates


def density_and_susceptibility(T: float, mu: float):
    density, fdeg = negative_muon_density_and_degeneracy(
        np.asarray([T], dtype=float), np.asarray([mu], dtype=float)
    )
    n_mev3 = float(density[0])
    chi_mev3 = n_mev3 * float(fdeg[0])
    conv = HBARC_MEV_FM**3
    return {
        "n_mu_MeV3": n_mev3,
        "n_mu_fm3": n_mev3 / conv,
        "n_mu_Fdeg_MeV3": chi_mev3,
        "n_mu_Fdeg_fm3": chi_mev3 / conv,
        "Fdeg": float(fdeg[0]),
    }


def neutrino_pair_rate(mu: float, omega: float, temperature: float, mass: float):
    velocity = np.sqrt(max(1.0 - (mass / omega) ** 2, 0.0))
    return float(fermi_pair_average(mu, omega, temperature, velocity)
                 + fermi_pair_average(0.0, omega, temperature, velocity))


def resampling_error(raw: np.ndarray, grid_r: np.ndarray, grid_y: np.ndarray,
                     sign: float = 1.0):
    selected = []
    for i in range(len(raw) - 1):
        x0, y0 = raw[i]
        x1, y1 = raw[i + 1]
        xm = 0.5 * (x0 + x1)
        if 12.0 <= xm <= 15.0:
            yr = sign * 0.5 * (y0 + y1)
            yg = float(np.interp(xm, grid_r, grid_y))
            err = abs(yg - yr) / max(abs(yr), 1.0e-300)
            selected.append((err, xm, yr, yg))
    if not selected:
        return None
    err, x, yr, yg = max(selected)
    return {
        "max_relative_error": float(err),
        "at_radius_km": float(x),
        "raw_polyline_value": float(yr),
        "resampled_grid_value": float(yg),
        "number_of_tested_segment_midpoints": len(selected),
    }


def run(source_dir: Path, data_dir: Path):
    cap_pdf = source_dir / "SNProfile.pdf"
    fer_pdf = source_dir / "SNModelComparison.pdf"
    for path in (cap_pdf, fer_pdf):
        expected = ep.EXPECTED_SHA256[path.name]
        actual = sha256(path)
        if actual != expected:
            raise ValueError(f"PDF hash mismatch for {path.name}: {actual}")

    cap_doc = pymupdf.open(cap_pdf)
    fer_doc = pymupdf.open(fer_pdf)
    cap_page = cap_doc[0]
    fer_page = fer_doc[0]

    caputo_indices = {"T": 0, "mu_mu": 1, "minus_mu_numu": 6,
                      "plus_mu_numu": 7, "n_mu_over_n0": 161}
    ferreira_indices = {"T": 1, "mu_mu_candidate": 394, "lapse_candidate": 610}
    target_paths = {
        "caputo": {name: drawing_record(cap_page, idx)
                   for name, idx in caputo_indices.items()},
        "ferreira": {name: drawing_record(fer_page, idx)
                     for name, idx in ferreira_indices.items()},
    }

    panel = FERREIRA_MUMU_PANEL
    candidates = candidate_drawings(
        fer_page, panel["x0"], panel["x1"], panel["y300"], panel["y50"],
        sample_mapping="ferreira_mu_mu"
    )

    csv_path = data_dir / "sfho188_digitized.csv"
    csv = np.genfromtxt(csv_path, delimiter=",", names=True)
    region = (csv["r_km"] >= 12.0) & (csv["r_km"] <= 15.0)
    rr = csv["r_km"][region]
    T_cap = csv["T_MeV"][region]
    T_fer = csv["T_Ferreira_MeV"][region]
    mu_cap = csv["mu_mu_MeV"][region]
    mu_fer = csv["mu_mu_Ferreira_MeV"][region]
    mu_numu = csv["mu_numu_MeV"][region]
    lapse = csv["lapse"][region]

    nplot_curve = read_curve(data_dir / "n_mu_over_n0_caputo_vertices.csv")
    rows = []
    for radius in RADII:
        row = {
            name: float(np.interp(radius, csv["r_km"], csv[name]))
            for name in csv.dtype.names
        }
        T = float(row["T_MeV"])
        mc = float(row["mu_mu_MeV"])
        mf = float(row["mu_mu_Ferreira_MeV"])
        dc = density_and_susceptibility(T, mc)
        df = density_and_susceptibility(T, mf)
        df_own_T = density_and_susceptibility(float(row["T_Ferreira_MeV"]), mf)
        nplot = interp_curve(nplot_curve, radius) * N0_FM3
        rows.append({
            "radius_km": radius,
            "T_Caputo_MeV": T,
            "T_Ferreira_MeV": float(row["T_Ferreira_MeV"]),
            "T_relative_difference": float((row["T_Ferreira_MeV"] - T) / T),
            "mu_mu_Caputo_MeV": mc,
            "mu_mu_Ferreira_MeV": mf,
            "mu_mu_relative_difference": float((mf - mc) / mc),
            "mu_mu_over_T_Caputo": mc / T,
            "mu_mu_over_T_Ferreira": mf / T,
            "mu_numu_MeV": float(row["mu_numu_MeV"]),
            "lapse": float(row["lapse"]),
            "Caputo_fermi_density": dc,
            "Ferreira_mu_mu_fermi_density_using_Caputo_T": df,
            "Ferreira_mu_mu_fermi_density_using_Ferreira_T": df_own_T,
            "Caputo_plotted_muon_density_fm3": nplot,
            "Caputo_density_to_own_plot_ratio": dc["n_mu_fm3"] / nplot,
            "Ferreira_density_to_Caputo_plot_ratio_using_Caputo_T": df["n_mu_fm3"] / nplot,
            "Ferreira_density_to_Caputo_plot_ratio_using_Ferreira_T": df_own_T["n_mu_fm3"] / nplot,
            "susceptibility_ratio_Ferreira_over_Caputo": (
                df["n_mu_Fdeg_MeV3"] / dc["n_mu_Fdeg_MeV3"]
            ),
        })

    energy_effects = []
    for radius in RADII:
        row = {
            name: float(np.interp(radius, csv["r_km"], csv[name]))
            for name in csv.dtype.names
        }
        T, mu = float(row["T_MeV"]), float(row["mu_numu_MeV"])
        if radius <= 13.11:
            current = mu
            test_mu = 0.0
        else:
            current = 0.0
            test_mu = 1.0
        effects = []
        for omega in ENERGIES:
            baseline = neutrino_pair_rate(current, omega, T, 10.0)
            alternative = neutrino_pair_rate(test_mu, omega, T, 10.0)
            effects.append({
                "omega_MeV": omega,
                "relative_change_for_alternative_mu_numu": (
                    alternative / baseline - 1.0
                ),
            })
        energy_effects.append({
            "radius_km": radius,
            "T_MeV": T,
            "current_mu_numu_MeV": current,
            "alternative_mu_numu_MeV": test_mu,
            "effects": effects,
        })

    grid_r = csv["r_km"]
    raw_specs = {
        "T_Caputo": ("T_caputo_vertices.csv", "T_MeV", 1.0),
        "mu_mu_Caputo": ("mu_mu_caputo_vertices.csv", "mu_mu_MeV", 1.0),
        "minus_mu_numu_Caputo": ("minus_mu_numu_caputo_vertices.csv", "mu_numu_MeV", -1.0),
        "T_Ferreira": ("T_ferreira_vertices.csv", "T_Ferreira_MeV", 1.0),
        "mu_mu_Ferreira": ("mu_mu_ferreira_vertices.csv", "mu_mu_Ferreira_MeV", 1.0),
        "lapse_Ferreira": ("lapse_ferreira_vertices.csv", "lapse", 1.0),
    }
    resampling = {}
    for name, (filename, column, sign) in raw_specs.items():
        raw = read_curve(data_dir / filename)
        resampling[name] = resampling_error(
            np.column_stack((raw["r_km"], raw["value"])),
            grid_r, csv[column], sign=sign
        )

    return {
        "title": "SFHo-18.8 profile input audit in the 12--15 km region",
        "profile_identity": "public-figure reconstruction at t_pb=1 s; not original Garching raw simulation data",
        "source_pdfs": {
            "SNProfile.pdf": {"sha256": sha256(cap_pdf), "source": ep.SOURCES["SNProfile.pdf"][0]},
            "SNModelComparison.pdf": {"sha256": sha256(fer_pdf), "source": ep.SOURCES["SNModelComparison.pdf"][0]},
        },
        "curve_path_identity": {
            "selected_path_indices": {"caputo": caputo_indices, "ferreira": ferreira_indices},
            "selected_path_details": target_paths,
            "all_candidate_paths_in_Ferreira_mu_mu_panel": candidates,
            "manual_review_status": (
                "Confirmed 2026-11-09 from Ferreira Fig. 1 caption: path 394 is the orange dashed SFHo-18.8 curve at t=1 s post-bounce. "
                "The same named model/time is shown in Caputo Fig. 1, and both papers cite Bollig et al. "
                "The curve identity is confirmed; the numerical mu_mu discrepancy and profile-file/convention origin remain unresolved."
            ),
        },
        "region_summary": {
            "T_Caputo_vs_Ferreira_max_abs_relative_difference": float(np.max(np.abs((T_fer - T_cap) / T_cap))),
            "T_Caputo_vs_Ferreira_mean_abs_relative_difference": float(np.mean(np.abs((T_fer - T_cap) / T_cap))),
            "mu_mu_Ferreira_vs_Caputo_min_relative_difference": float(np.min((mu_fer - mu_cap) / mu_cap)),
            "mu_mu_Ferreira_vs_Caputo_max_relative_difference": float(np.max((mu_fer - mu_cap) / mu_cap)),
            "mu_mu_Ferreira_vs_Caputo_mean_relative_difference": float(np.mean((mu_fer - mu_cap) / mu_cap)),
            "mu_numu_abs_max_MeV": float(np.max(np.abs(mu_numu))),
            "lapse_min": float(np.min(lapse)),
            "lapse_max": float(np.max(lapse)),
            "lapse_is_monotone_increasing": bool(np.all(np.diff(lapse) > 0.0)),
        },
        "pointwise_profile_and_density_checks": rows,
        "mu_numu_floor_sensitivity": energy_effects,
        "resampling_error_against_raw_pdf_polyline": resampling,
        "interpretation": [
            "The Caputo mu_mu curve is checked against the independent n_mu curve in the lower panel of the same Fig. 1.",
            "The Ferreira mu_mu curve identity is confirmed by the figure caption, but it remains a diagnostic-only same-model reconstruction until its numerical discrepancy with Caputo is resolved.",
            "The neutrino-pair rate is even in mu_numu; the sign of the negative branch does not change the pair rate, while its magnitude does.",
            "The lapse has no independent Caputo comparison in Fig. 1; this audit checks only the Ferreira curve and interpolation over 12--15 km.",
            "This audit does not change any opacity, path integral, luminosity, coupling, or axial-vector constraint curve.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path,
                        default=HERE / "latex-build" / "sources")
    parser.add_argument("--data-dir", type=Path, default=HERE / "data")
    parser.add_argument("--output", type=Path,
                        default=HERE / "data" / "profile_12_15km_audit_2026-11-09.json")
    args = parser.parse_args()
    result = run(args.source_dir, args.data_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "region_summary": result["region_summary"],
        "selected_paths": result["curve_path_identity"]["selected_path_details"],
        "candidate_paths": result["curve_path_identity"]["all_candidate_paths_in_Ferreira_mu_mu_panel"],
        "output": str(args.output),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
