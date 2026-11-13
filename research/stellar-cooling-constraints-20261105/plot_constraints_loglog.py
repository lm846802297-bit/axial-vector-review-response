"""Review-only constraint plot using per-mass log-log threshold crossings.

The original plot_constraints.py and its archived outputs are left unchanged.
This script draws the stored intervals from run_scan.find_intervals directly,
then compares the original Matplotlib contour interpolation with those
per-mass crossings. It is a presentation audit, not a new luminosity scan.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"


def read_scan(name: str):
    data = json.loads((OUT / name).read_text(encoding="utf-8"))
    masses = np.asarray([row["mass_MeV"] for row in data["results"]], dtype=float)
    couplings = np.asarray(data["couplings"], dtype=float)
    return data, masses, couplings


def merge_endpoint(axial, endpoint):
    if axial["config"] != endpoint["config"]:
        raise ValueError("Endpoint and baseline scan configurations differ")
    if axial["couplings"] != endpoint["couplings"]:
        raise ValueError("Endpoint and baseline coupling grids differ")
    rows = {float(row["mass_MeV"]): row for row in axial["results"]}
    rows.update({float(row["mass_MeV"]): row for row in endpoint["results"]})
    result = dict(axial)
    result["results"] = [rows[m] for m in sorted(rows)]
    return result


def interval_branches(rows, key):
    max_count = max((len(row.get(key, [])) for row in rows), default=0)
    branches = []
    masses = np.asarray([row["mass_MeV"] for row in rows], dtype=float)
    for index in range(max_count):
        lower = np.full(masses.shape, np.nan, dtype=float)
        upper = np.full(masses.shape, np.nan, dtype=float)
        for i, row in enumerate(rows):
            intervals = row.get(key, [])
            if index < len(intervals):
                lower[i], upper[i] = map(float, intervals[index])
        branches.append((lower, upper))
    return masses, branches


def contour_intersections(all_segments, x_value):
    values = []
    for segment in all_segments:
        vertices = np.asarray(segment, dtype=float)
        if vertices.ndim != 2 or vertices.shape[0] < 2:
            continue
        for p0, p1 in zip(vertices[:-1], vertices[1:]):
            if not np.all(np.isfinite([p0[0], p0[1], p1[0], p1[1]])):
                continue
            x0, y0 = p0
            x1, y1 = p1
            if x0 == x1:
                if np.isclose(x_value, x0, rtol=1e-12, atol=0.0):
                    values.extend([float(y0), float(y1)])
                continue
            if min(x0, x1) <= x_value <= max(x0, x1):
                t = (x_value - x0) / (x1 - x0)
                values.append(float(y0 + t * (y1 - y0)))
    if not values:
        return []
    values = sorted(values)
    unique = []
    for value in values:
        if not unique or not np.isclose(value, unique[-1], rtol=1e-8, atol=0.0):
            unique.append(value)
    return unique


def compare_original_contour(masses, couplings, luminosities, rows, threshold):
    z = (np.log10(np.maximum(luminosities, 1e-300)) -
         np.log10(threshold)).T
    fig, ax = plt.subplots()
    contour = ax.contour(masses, couplings, z, levels=[0.0])
    segments = contour.allsegs[0]
    exact_masses, branches = interval_branches(rows, "intervals_4p4e52")
    if len(branches) != 1:
        plt.close(fig)
        return {
            "status": "not_reduced_to_single_interval_per_mass",
            "branch_count": len(branches),
            "compared_mass_count": 0,
        }
    lower, upper = branches[0]
    lower_errors, upper_errors = [], []
    compared = 0
    for i, mass in enumerate(exact_masses):
        if not np.isfinite(lower[i]) or not np.isfinite(upper[i]):
            continue
        intersections = contour_intersections(segments, float(mass))
        if len(intersections) < 2:
            continue
        low_contour, high_contour = intersections[0], intersections[-1]
        lower_errors.append(abs(low_contour / lower[i] - 1.0))
        upper_errors.append(abs(high_contour / upper[i] - 1.0))
        compared += 1
    plt.close(fig)
    if not compared:
        return {"status": "no_comparable_contour_intersections",
                "compared_mass_count": 0}
    return {
        "status": "compared",
        "compared_mass_count": compared,
        "lower_max_abs_relative_difference": float(max(lower_errors)),
        "lower_rms_relative_difference": float(np.sqrt(np.mean(np.square(lower_errors)))),
        "upper_max_abs_relative_difference": float(max(upper_errors)),
        "upper_rms_relative_difference": float(np.sqrt(np.mean(np.square(upper_errors)))),
        "definition": "absolute relative difference between the original Matplotlib contour branch and the per-mass log-log interval boundary, sampled at the stored mass nodes",
    }


def draw_interval_boundaries(ax, rows, key, color, linestyle, label=None,
                             fill=False, alpha=0.18):
    masses, branches = interval_branches(rows, key)
    for index, (lower, upper) in enumerate(branches):
        valid = np.isfinite(lower) & np.isfinite(upper) & (lower > 0) & (upper > 0)
        if fill:
            ax.fill_between(masses, lower, upper, where=valid,
                            color=color, alpha=alpha, linewidth=0)
        line_label = label if index == 0 else None
        ax.plot(masses, np.where(valid, lower, np.nan), color=color,
                linestyle=linestyle, linewidth=1.7, label=line_label)
        ax.plot(masses, np.where(valid, upper, np.nan), color=color,
                linestyle=linestyle, linewidth=1.7)
    return masses, branches


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=OUT / "reviewed_loglog")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    axial, _, g = read_scan("axial.json")
    endpoint, _, _ = read_scan("endpoint.json")
    vector, mv, gv = read_scan("vector.json")
    axial = merge_endpoint(axial, endpoint)
    rows = axial["results"]
    masses = np.asarray([row["mass_MeV"] for row in rows], dtype=float)
    luminosities = np.asarray([row["luminosity_erg_s"] for row in rows], dtype=float)
    vector_luminosities = np.asarray(
        [row["luminosity_erg_s"] for row in vector["results"]], dtype=float
    )
    if luminosities.shape != (len(masses), len(g)):
        raise ValueError("Axial luminosity array does not match mass/coupling grid")
    if vector_luminosities.shape != (len(mv), len(gv)):
        raise ValueError("Vector luminosity array does not match mass/coupling grid")

    contour_audit = compare_original_contour(
        masses, g, luminosities, rows, 4.4e52
    )

    fig, (ax, frac) = plt.subplots(
        1, 2, figsize=(11.4, 4.8), gridspec_kw={"width_ratios": [1.65, 1]}
    )
    draw_interval_boundaries(
        ax, rows, "intervals_4p4e52", "#235d91", "-",
        label=r"Axial: $L_R=4.4\times10^{52}$ erg s$^{-1}$",
        fill=True, alpha=0.22
    )
    draw_interval_boundaries(
        ax, rows, "intervals_3e52", "#235d91", ":",
        label=r"Axial: $L_R=3.0\times10^{52}$ erg s$^{-1}$ (sensitivity)"
    )
    draw_interval_boundaries(
        ax, vector["results"], "intervals_4p4e52", "#252525", "--",
        label="Vector muon-current control only"
    )
    ax.fill_between([1, 500], 1e-6, 1e-4, color="#ece8de", alpha=0.6, zorder=-1)
    ax.text(2, 1.1e-5, "Original Fig. 2 window\n(shown overlap)",
            fontsize=8, color="#756c5b")
    ax.text(0.022, 3e-9,
            "Axial benchmark region:\n" +
            r"$L_{\rm axial}>4.4\times10^{52}$ erg s$^{-1}$",
            color="#235d91", fontsize=9)
    ax.set(
        xscale="log", yscale="log", xlim=(0.01, 500), ylim=(1e-14, 1e-4),
        xlabel=r"$m_{A^\prime}$ [MeV]",
        ylabel=r"$|g_X|\simeq|g_A^\mu|$"
    )
    ax.legend(loc="lower right", fontsize=7.2, frameon=False)

    for key, color in [
        ("Compton", "#b44b3b"),
        ("neutrino", "#235d91"),
        ("dimuon", "#53835a"),
    ]:
        values = np.asarray(
            [row["thin_fractions"][key] for row in rows], dtype=float
        )
        frac.plot(masses, values, lw=1.8, color=color, label=key)
    frac.axvline(2 * 105.6583755, color=".65", lw=0.8, ls=":")
    frac.set(
        xscale="log", yscale="log", xlim=(0.01, 500), ylim=(1e-4, 1.2),
        xlabel=r"$m_{A^\prime}$ [MeV]",
        ylabel="Optically thin production fraction"
    )
    frac.legend(frameon=False, loc="lower left")
    for axis in (ax, frac):
        axis.grid(which="major", alpha=0.15)
        axis.tick_params(which="both", direction="in", top=True, right=True)
    fig.suptitle("SN1987A: axial-EFT fixed-profile benchmark — log-log boundary review",
                 fontsize=12)
    fig.text(
        0.5, 0.012,
        "Per-mass log-log threshold crossings; lines connect discrete mass rows. "
        "Conditional ballistic benchmark, not a final SN1987A exclusion.",
        ha="center", fontsize=7.5
    )
    fig.tight_layout(rect=(0, 0.07, 1, 0.95))
    pdf = args.output_dir / "axial_stellar_constraints_loglog_review.pdf"
    png = args.output_dir / "axial_stellar_constraints_loglog_review.png"
    fig.savefig(pdf)
    fig.savefig(png, dpi=200)
    plt.close(fig)

    audit = {
        "purpose": "presentation-level comparison; no luminosity is recomputed",
        "source_files": ["outputs/axial.json", "outputs/endpoint.json",
                         "outputs/vector.json"],
        "primary_threshold_erg_s": 4.4e52,
        "sensitivity_threshold_erg_s": 3.0e52,
        "axial_mass_rows": int(len(masses)),
        "vector_mass_rows": int(len(mv)),
        "coupling_points_per_mass": int(len(g)),
        "coupling_range": [float(g.min()), float(g.max())],
        "boundary_method": "run_scan.find_intervals per mass: linear interpolation in (log g_X, log L); plot lines connect the resulting boundary samples on log-log axes",
        "original_plot_method": "Matplotlib contour/contourf on native linear mass and coupling coordinates, followed by logarithmic display axes",
        "original_contour_comparison": contour_audit,
        "limitations": [
            "The comparison is sampled at stored mass nodes and does not bound interpolation error between mass nodes.",
            "This is not a physical uncertainty estimate.",
            "The pure-vector line is an internal control, not a passed Blinov Fig. 7 reproduction.",
            "The fixed-profile axial scan still has the physical limitations documented in FIGURE_AUDIT.md.",
        ],
        "review_figure_files": [pdf.name, png.name],
    }
    (args.output_dir / "contour_interpolation_audit.json").write_text(
        json.dumps(audit, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(contour_audit, indent=2))


if __name__ == "__main__":
    main()
