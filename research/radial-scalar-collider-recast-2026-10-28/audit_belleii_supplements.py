#!/usr/bin/env python3
"""Audit and reproduce the published Belle II scalar benchmark curves.

This script reconstructs the published coupling-limit curves from the official
numerical supplements. It does NOT rerun Belle II event selection, detector
simulation, likelihood fits, or the CLs calculation, and it does NOT produce a
UV-model exclusion by itself.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path


FOUR_MUON_COLUMNS = {
    "mass": "mass",
    "xsec_obs": "cross_section_upper_limit(obs)",
    "xsec_exp": "cross_section_expected(med)",
    "xsec_m1": "-1 sigma (cross_section)",
    "xsec_p1": "+1sigma(cross_section)",
    "xsec_m2": "-2sigma (cross_section)",
    "xsec_p2": "+2sigma(cross_section)",
    "gs_obs": "gs_upper_limit(obs)",
    "gs_exp": "gs_expected (med)",
    "gs_m1": "-1 sigma (gs)",
    "gs_p1": "+1sigma(gs)",
    "gs_m2": "-2sigma (gs)",
    "gs_p2": "+2sigma(gs)",
    "xsec_central": "cross_section_central_values",
    "gs_central": "gs_central_values",
}

TAU_MASS = "m [GeV/c^2]"
TAU_XSEC = [
    "xsec_UL_obs [fb]", "xsec_UL_exp [fb]",
    "xsec_UL_exp -1sigma [fb]", "xsec_UL_exp +1sigma [fb]",
    "xsec_UL_exp -2sigma [fb]", "xsec_UL_exp +2sigma [fb]",
]
TAU_GPRIME = [
    "g'_UL_obs", "g'_UL_exp", "g'_UL_exp -1sigma",
    "g'_UL_exp +1sigma", "g'_UL_exp -2sigma", "g'_UL_exp +2sigma",
]
TAU_XI = [
    "xi_UL_obs", "xi_UL_exp", "xi_UL_exp -1sigma",
    "xi_UL_exp +1sigma", "xi_UL_exp -2sigma", "xi_UL_exp +2sigma",
]
TAU_ALP = [
    "{c_{\\ell\\ell}/\\Lambda}_UL_obs [TeV^-1]",
    "{c_{\\ell\\ell}/\\Lambda}_UL_exp [TeV^-1]",
    "{c_{\\ell\\ell}/\\Lambda}_UL_exp -1sigma [TeV^-1]",
    "{c_{\\ell\\ell}/\\Lambda}_UL_exp +1sigma [TeV^-1]",
    "{c_{\\ell\\ell}/\\Lambda}_UL_exp -2sigma [TeV^-1]",
    "{c_{\\ell\\ell}/\\Lambda}_UL_exp +2sigma [TeV^-1]",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_fourmu(path: Path) -> tuple[list[str], list[dict[str, float]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError(f"empty four-muon supplement: {path}")
    header = re.split(r"\s*>>\s*", lines[0].strip())
    rows = []
    for lineno, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != len(header):
            raise ValueError(
                f"{path}:{lineno}: expected {len(header)} fields, got {len(fields)}"
            )
        rows.append(dict(zip(header, map(float, fields))))
    return header, rows


def read_tau(path: Path) -> tuple[list[str], list[dict[str, float]]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        if reader.fieldnames is None:
            raise ValueError(f"missing CSV header: {path}")
        header = list(reader.fieldnames)
        rows = []
        for lineno, row in enumerate(reader, start=2):
            if not row or all(v is None or not v.strip() for v in row.values()):
                continue
            try:
                rows.append({k: float(v) for k, v in row.items()})
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{path}:{lineno}: non-numeric field: {exc}") from exc
    return header, rows


def assert_finite(rows: list[dict[str, float]], name: str) -> None:
    for i, row in enumerate(rows):
        for key, value in row.items():
            if not math.isfinite(value):
                raise AssertionError(f"{name} row {i} field {key} is not finite")


def assert_band_order(rows: list[dict[str, float]], columns: list[str], name: str) -> None:
    for i, row in enumerate(rows):
        values = [row[c] for c in columns]
        if not all(a < b for a, b in zip(values, values[1:])):
            raise AssertionError(f"{name} expected-band ordering failed at row {i}: {values}")


def extrema(rows: list[dict[str, float]], mass_col: str, value_col: str) -> dict:
    low = min(rows, key=lambda r: r[value_col])
    high = max(rows, key=lambda r: r[value_col])
    return {
        "min": low[value_col], "min_mass_GeV": low[mass_col],
        "max": high[value_col], "max_mass_GeV": high[mass_col],
    }


def audit(data_dir: Path) -> dict:
    four_path = data_dir / "four-muon" / "S_supplemental.txt"
    tau_csv_path = data_dir / "tau-pair" / "limits.csv"
    tau_txt_path = data_dir / "tau-pair" / "limits.txt"

    for p in (four_path, tau_csv_path, tau_txt_path):
        if not p.is_file():
            raise FileNotFoundError(p)

    four_header, four = read_fourmu(four_path)
    tau_header, tau = read_tau(tau_csv_path)
    tau_txt = tau_txt_path.read_bytes()
    tau_csv = tau_csv_path.read_bytes()
    if tau_csv != tau_txt:
        raise AssertionError("limits.csv and limits.txt are not byte-identical")

    assert len(four_header) == 15
    assert len(four) == 2317
    assert len(tau_header) == 27
    assert len(tau) == 2384
    assert_finite(four, "four-muon")
    assert_finite(tau, "tau-pair")

    four_mass = [r[FOUR_MUON_COLUMNS["mass"]] for r in four]
    if not all(a < b for a, b in zip(four_mass, four_mass[1:])):
        raise AssertionError("four-muon mass grid is not strictly increasing")

    tau_mass = [r[TAU_MASS] for r in tau]
    if not all(a <= b for a, b in zip(tau_mass, tau_mass[1:])):
        raise AssertionError("tau-pair mass grid is not non-decreasing")

    assert_band_order(
        four,
        [FOUR_MUON_COLUMNS[k] for k in ("gs_m2", "gs_m1", "gs_exp", "gs_p1", "gs_p2")],
        "four-muon gS",
    )
    assert_band_order(
        four,
        [FOUR_MUON_COLUMNS[k] for k in ("xsec_m2", "xsec_m1", "xsec_exp", "xsec_p1", "xsec_p2")],
        "four-muon cross section",
    )
    for name, cols in (
        ("tau-pair cross section", TAU_XSEC[4:5] + TAU_XSEC[2:3] + TAU_XSEC[1:2] + TAU_XSEC[3:4] + TAU_XSEC[5:6]),
        ("tau-pair g-prime", [TAU_GPRIME[i] for i in (4, 2, 1, 3, 5)]),
        ("tau-pair xi", [TAU_XI[i] for i in (4, 2, 1, 3, 5)]),
        ("tau-pair ALP", [TAU_ALP[i] for i in (4, 2, 1, 3, 5)]),
    ):
        assert_band_order(tau, cols, name)

    # Four-muon scalar production is quadratic in gS. The six published
    # cross-section and gS UL quantiles must imply one common sigma_ref(m).
    xcols = [FOUR_MUON_COLUMNS[k] for k in ("xsec_obs", "xsec_exp", "xsec_m1", "xsec_p1", "xsec_m2", "xsec_p2")]
    gcols = [FOUR_MUON_COLUMNS[k] for k in ("gs_obs", "gs_exp", "gs_m1", "gs_p1", "gs_m2", "gs_p2")]
    sigma_ref_rows = []
    rel_spreads = []
    for row in four:
        norms = [row[x] / row[g] ** 2 for x, g in zip(xcols, gcols)]
        mean = sum(norms) / len(norms)
        sigma_ref_rows.append(mean)
        rel_spreads.append((max(norms) - min(norms)) / mean)
    if max(rel_spreads) > 1.1e-3:
        raise AssertionError("four-muon gS quadratic normalization is inconsistent")

    # The signed central-fit coupling and cross section are also consistent
    # with the same normalization, except when the central fit rounds to zero.
    central_residuals = []
    for row, sigma_ref in zip(four, sigma_ref_rows):
        gc = row[FOUR_MUON_COLUMNS["gs_central"]]
        xc = row[FOUR_MUON_COLUMNS["xsec_central"]]
        if gc != 0.0:
            sigma_from_central = abs(xc) / gc**2
            central_residuals.append(abs(sigma_from_central - sigma_ref) / sigma_ref)

    mass_counts = Counter(tau_mass)
    duplicate_masses = []
    for mass, count in mass_counts.items():
        if count > 1:
            group = [r for r in tau if r[TAU_MASS] == mass]
            if any(r != group[0] for r in group[1:]):
                raise AssertionError(f"non-identical duplicate rows at mass {mass}")
            duplicate_masses.append({"mass_GeV": mass, "identical_rows": count})

    # Conditional original-UV overlay. This is valid only when A'A' and
    # portal/other channels are closed/negligible, the scalar remains prompt
    # and narrow, and the Belle scalar-specific efficiency applies unchanged.
    m_mu, m_tau, m_e, v = 0.1056583755, 1.77686, 0.00051099895, 246.0
    sqrt_8pi = math.sqrt(8.0 * math.pi)

    def lepton_weight(ms: float, ml: float) -> float:
        if ms <= 2.0 * ml:
            return 0.0
        return ml**2 * (1.0 - 4.0 * ml**2 / ms**2)**1.5

    def last_below(rows, ratio_key, mass_key):
        eligible = [r for r in rows if r[ratio_key] < 1.0]
        if not eligible:
            return None
        last = max(eligible, key=lambda r: r[mass_key])
        next_rows = [r for r in rows if r[mass_key] > last[mass_key]]
        nxt = min(next_rows, key=lambda r: r[mass_key]) if next_rows else None
        return {
            "last_mass_GeV_below_boundary": last[mass_key],
            "ratio_at_last_point": last[ratio_key],
            "next_mass_GeV": nxt[mass_key] if nxt else None,
            "ratio_at_next_point": nxt[ratio_key] if nxt else None,
        }

    four_uv = []
    for row in four:
        ms = row["mass"]
        wmu, wtau = lepton_weight(ms, m_mu), lepton_weight(ms, m_tau)
        br_mu_uv = wmu / (wmu + wtau) if wmu + wtau else 1.0
        g_pert = sqrt_8pi * m_mu / ms
        item = {
            "mass": ms,
            "obs_ratio": (row[FOUR_MUON_COLUMNS["gs_obs"]] / math.sqrt(br_mu_uv)) / g_pert,
            "exp_ratio": (row[FOUR_MUON_COLUMNS["gs_exp"]] / math.sqrt(br_mu_uv)) / g_pert,
        }
        four_uv.append(item)

    tau_uv = []
    for row in tau:
        ms = row[TAU_MASS]
        wmu, wtau, we = (lepton_weight(ms, ml) for ml in (m_mu, m_tau, m_e))
        br_tau_uv = wtau / (wmu + wtau) if wmu + wtau else 0.0
        br_tau_belle = wtau / (wmu + wtau + we) if wmu + wtau + we else 0.0
        xi_pert = sqrt_8pi * v / ms
        xi_obs_uv = row[TAU_XI[0]] * math.sqrt(br_tau_belle / br_tau_uv)
        xi_exp_uv = row[TAU_XI[1]] * math.sqrt(br_tau_belle / br_tau_uv)
        tau_uv.append({
            "mass": ms,
            "obs_ratio": xi_obs_uv / xi_pert,
            "exp_ratio": xi_exp_uv / xi_pert,
            "br_tau_uv": br_tau_uv,
            "br_tau_belle": br_tau_belle,
        })

    result = {
        "files": {
            "S_supplemental.txt": {
                "bytes": four_path.stat().st_size,
                "sha256": sha256(four_path),
                "rows": len(four),
                "columns": len(four_header),
                "mass_range_GeV": [min(four_mass), max(four_mass)],
            },
            "limits.csv": {
                "bytes": tau_csv_path.stat().st_size,
                "sha256": sha256(tau_csv_path),
                "rows": len(tau),
                "columns": len(tau_header),
                "mass_range_GeV": [min(tau_mass), max(tau_mass)],
                "byte_identical_to_limits_txt": True,
            },
            "limits.txt": {
                "bytes": tau_txt_path.stat().st_size,
                "sha256": sha256(tau_txt_path),
                "rows": len(tau),
                "columns": len(tau_header),
                "byte_identical_to_limits_csv": True,
            },
        },
        "four_muon": {
            "gS_observed_90CL": extrema(four, "mass", FOUR_MUON_COLUMNS["gs_obs"]),
            "gS_expected_median": extrema(four, "mass", FOUR_MUON_COLUMNS["gs_exp"]),
            "xsec_observed_fb": extrema(four, "mass", FOUR_MUON_COLUMNS["xsec_obs"]),
            "quadratic_sigma_ref_relative_spread_median": sorted(rel_spreads)[len(rel_spreads)//2],
            "quadratic_sigma_ref_relative_spread_max": max(rel_spreads),
            "central_fit_normalization_relative_residual_median": sorted(central_residuals)[len(central_residuals)//2],
            "central_fit_normalization_relative_residual_p99": sorted(central_residuals)[int(0.99*(len(central_residuals)-1))],
            "central_fit_zero_rows": sum(r[FOUR_MUON_COLUMNS["gs_central"]] == 0.0 for r in four),
            "rows_in_excluded_Jpsi_window_3p07_to_3p12_GeV": sum(3.07 <= m <= 3.12 for m in four_mass),
        },
        "tau_pair": {
            "unique_mass_points": len(mass_counts),
            "exact_duplicate_mass_rows": len(tau) - len(mass_counts),
            "exact_duplicate_masses": sorted(duplicate_masses, key=lambda x: x["mass_GeV"]),
            "xi_observed_90CL": extrema(tau, TAU_MASS, TAU_XI[0]),
            "xi_expected_median": extrema(tau, TAU_MASS, TAU_XI[1]),
            "xsec_observed_fb": extrema(tau, TAU_MASS, TAU_XSEC[0]),
        },
        "conditional_original_uv_overlay": {
            "assumptions": [
                "Original one-VEV mass-proportional Yukawas y_sll=m_l/v_s.",
                "s -> A'A' is kinematically closed; portal and other extra widths are negligible.",
                "Prompt/narrow-resonance and Belle scalar-specific selection-efficiency assumptions remain valid.",
                "Perturbativity criterion is lambda_S <= 4 pi, so xi_max=sqrt(8 pi) v/m_s and y_mu_max=sqrt(8 pi) m_mu/m_s."
            ],
            "four_muon_observed_last_point_below_perturbativity": last_below(four_uv, "obs_ratio", "mass"),
            "four_muon_expected_last_point_below_perturbativity": last_below(four_uv, "exp_ratio", "mass"),
            "tau_pair_observed_last_point_below_perturbativity": last_below(tau_uv, "obs_ratio", "mass"),
            "tau_pair_expected_last_point_below_perturbativity": last_below(tau_uv, "exp_ratio", "mass"),
            "tau_branching_fraction_max_relative_difference_Belle_vs_UV": max(
                abs(r["br_tau_belle"] - r["br_tau_uv"]) / r["br_tau_uv"] for r in tau_uv
            ),
            "warning": (
                "This is a pointwise coupling/branching-fraction overlay, not a full collider recast. "
                "Observed curves fluctuate, so last-below points are not universal mass cutoffs. "
                "Opening A'A' or portal channels changes the branching fractions and weakens the direct-channel limits."
            ),
        },
        "validation_scope": (
            "Published numerical benchmark curves reconstructed from the official tables. "
            "No detector simulation, selection-efficiency recalculation, event-level likelihood, "
            "or CLs fit was rerun. The UV overlay is conditional and does not claim a complete exclusion."
        ),
        "source_count_discrepancies": {
            "four_muon": (
                "The supplement has 2317 rows, whereas the paper text reports 2315 fits; "
                "the supplement rows have unique, strictly increasing masses. This 2-row "
                "difference is unresolved and must be retained as a source discrepancy."
            ),
            "tau_pair": (
                "The supplement has 2384 rows, matching the paper's stated 2384 fits, but "
                "contains three exact duplicate mass rows; keep raw data unchanged and "
                "deduplicate only for plotting/unique-mass summaries."
            ),
        },
    }
    return result


def make_plots(data_dir: Path, output_dir: Path) -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise RuntimeError("matplotlib is required only for --plots") from exc

    _, four = read_fourmu(data_dir / "four-muon" / "S_supplemental.txt")
    _, tau = read_tau(data_dir / "tau-pair" / "limits.csv")
    tau = list({tuple(sorted(r.items())): r for r in tau}.values())
    tau.sort(key=lambda r: r[TAU_MASS])
    output_dir.mkdir(parents=True, exist_ok=True)

    m = [r["mass"] for r in four]
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.fill_between(m, [r[FOUR_MUON_COLUMNS["gs_m2"]] for r in four],
                    [r[FOUR_MUON_COLUMNS["gs_p2"]] for r in four], alpha=0.22, label="Expected UL ±2σ")
    ax.fill_between(m, [r[FOUR_MUON_COLUMNS["gs_m1"]] for r in four],
                    [r[FOUR_MUON_COLUMNS["gs_p1"]] for r in four], alpha=0.38, label="Expected UL ±1σ")
    ax.plot(m, [r[FOUR_MUON_COLUMNS["gs_exp"]] for r in four], ls=":", lw=0.9, label="Median expected")
    ax.plot(m, [r[FOUR_MUON_COLUMNS["gs_obs"]] for r in four], lw=0.65, label="Observed 90% CL UL")
    ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(0.2, 10); ax.set_ylim(1e-4, 1)
    ax.set_xlabel(r"$m_S$ [GeV/$c^2$]"); ax.set_ylabel(r"90% CL upper limit on $g_S$")
    ax.legend(fontsize=8); ax.grid(True, which="both", alpha=0.18); fig.tight_layout()
    fig.savefig(output_dir / "belleii_fourmu_scalar_gS.png", dpi=200); plt.close(fig)

    m = [r[TAU_MASS] for r in tau]
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.fill_between(m, [r[TAU_XI[4]] for r in tau], [r[TAU_XI[5]] for r in tau], alpha=0.22, label="Expected UL ±2σ")
    ax.fill_between(m, [r[TAU_XI[2]] for r in tau], [r[TAU_XI[3]] for r in tau], alpha=0.38, label="Expected UL ±1σ")
    ax.plot(m, [r[TAU_XI[1]] for r in tau], ls=":", lw=0.9, label="Median expected")
    ax.plot(m, [r[TAU_XI[0]] for r in tau], lw=0.65, label="Observed 90% CL UL")
    ax.set_yscale("log"); ax.set_xlim(3, 10); ax.set_ylim(1e1, 1e4)
    ax.set_xlabel(r"$m_S$ [GeV/$c^2$]"); ax.set_ylabel(r"90% CL upper limit on $\xi$")
    ax.legend(fontsize=8); ax.grid(True, which="both", alpha=0.18); fig.tight_layout()
    fig.savefig(output_dir / "belleii_tautau_scalar_xi.png", dpi=200); plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True,
                        help="directory containing four-muon/ and tau-pair/")
    parser.add_argument("--output-json", type=Path)
    parser.add_argument("--plots-dir", type=Path)
    args = parser.parse_args()
    result = audit(args.data_dir)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(rendered + "\n", encoding="utf-8")
    if args.plots_dir:
        make_plots(args.data_dir, args.plots_dir)


if __name__ == "__main__":
    main()
