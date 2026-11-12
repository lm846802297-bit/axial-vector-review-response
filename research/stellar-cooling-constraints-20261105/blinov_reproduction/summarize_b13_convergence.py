#!/usr/bin/env python3
"""Aggregate independent global B.13 radial, energy, direction and path convergence scans."""
from __future__ import annotations
import argparse, json, math, shutil
from pathlib import Path

EXPECTED = {
    "baseline": (40, 100, 16, 32),
    "radial60": (60, 100, 16, 32),
    "radial80": (80, 100, 16, 32),
    "energy150": (40, 150, 16, 32),
    "energy200": (40, 200, 16, 32),
    "angle24": (40, 100, 24, 32),
    "angle32": (40, 100, 32, 32),
    "path48": (40, 100, 16, 48),
    "path64": (40, 100, 16, 64),
}
B13 = "B13_mu_minus_consistent_source_and_opacity"
VARIANTS = ("B16_reference", B13)
FIELDS = {
    "Lthin": "optically_thin_luminosity_erg_s",
    "Pesc": "escape_fraction",
    "Ltotal": "calculated_luminosity_erg_s",
}


def read_inputs(input_dir: Path) -> dict[str, dict]:
    found = {}
    for path in sorted(input_dir.glob("summary_*.json")):
        case = path.stem.removeprefix("summary_")
        if case in EXPECTED:
            if case in found:
                raise ValueError(f"Duplicate summary for {case}")
            found[case] = json.loads(path.read_text(encoding="utf-8"))
    missing = sorted(set(EXPECTED) - set(found))
    if missing:
        raise ValueError(f"Missing convergence cases: {missing}")
    profile_sha = None
    for case, data in found.items():
        cfg = data["configuration"]
        actual = (int(cfg["radial_order"]), int(cfg["energy_order"]),
                  int(cfg["angular_order"]), int(cfg["path_order"]))
        if actual != EXPECTED[case]:
            raise ValueError(f"{case}: expected {EXPECTED[case]}, got {actual}")
        if float(data["mass_MeV"]) != 10.0:
            raise ValueError(f"{case}: expected 10 MeV")
        sha = data["profile"]["sha256"]
        if profile_sha is None:
            profile_sha = sha
        elif sha != profile_sha:
            raise ValueError(f"{case}: profile fingerprint mismatch")
        closure = data["archived_B16_baseline"]["max_relative_reproduction_residual"]
        if closure is None or float(closure) > 2.0e-10:
            raise ValueError(f"{case}: matched-grid B.16 closure failed: {closure}")
        if data["configuration"]["B13_kernel_orders"] != [12, 8, 8, 8]:
            raise ValueError(f"{case}: local B.13 kernel quadrature was changed")
        residuals = data["B13_numerical_validation"]["maximum_residuals"]
        if max(float(v) for v in residuals.values()) > 1.0e-10:
            raise ValueError(f"{case}: detailed-balance/closure residual too large")
    return found


def rows(data: dict, variant: str) -> list[dict]:
    return data["variant_results"][variant]["points"]


def peak_index(data: dict, variant: str) -> int:
    p = rows(data, variant)
    return max(range(len(p)), key=lambda i: float(p[i]["reference_luminosity_erg_s"]))


def rel(fine: float, coarse: float) -> float:
    return fine / coarse - 1.0 if coarse else (0.0 if fine == 0.0 else math.inf)


def compare_pair(coarse: dict, fine: dict) -> dict:
    result = {}
    for variant in VARIANTS:
        c, f = rows(coarse, variant), rows(fine, variant)
        if len(c) != len(f):
            raise ValueError("Coupling grids differ")
        ip = peak_index(coarse, variant)
        result[variant] = {}
        for label, field in FIELDS.items():
            shifts = [rel(float(y[field]), float(x[field])) for x, y in zip(c, f)]
            result[variant][label] = {
                "max_abs_relative_change": max(abs(x) for x in shifts),
                "mean_abs_relative_change": sum(abs(x) for x in shifts) / len(shifts),
                "weak_endpoint_relative_change": shifts[0],
                "reference_peak_relative_change": shifts[ip],
                "strong_endpoint_relative_change": shifts[-1],
            }
    return result


def shell_diagnostics(data: dict, variant: str) -> dict:
    diag = data["radial_source_diagnostics"]
    if variant == "B16_reference":
        sk, ek = "B16_total_B1_source_fraction", "B16_strong_endpoint_escape_fraction_in_shell"
    else:
        sk, ek = "B13_mu_minus_total_B1_source_fraction", "B13_mu_minus_strong_endpoint_escape_fraction_in_shell"
    global_escape = float(data["variant_results"][variant]["strong_endpoint_escape_fraction"])
    out = {}
    for name, lo, hi in (("5_10km", 5.0, 10.0), ("10_15km", 10.0, 15.0)):
        selected = [r for r in diag if float(r["emission_shell_km"][0]) >= lo - 1e-12
                    and float(r["emission_shell_km"][1]) <= hi + 1e-12]
        source = sum(float(r[sk]) for r in selected)
        escaped = sum(float(r[sk]) * float(r[ek]) for r in selected)
        out[name] = {
            "source_fraction": source,
            "escaped_luminosity_fraction": escaped / global_escape if global_escape else 0.0,
        }
    return out


def pct(x: float) -> str:
    return f"{100*x:.4f}%"


def build_report(input_dir: Path, output_dir: Path, report_path: Path, aggregate_path: Path) -> dict:
    data = read_inputs(input_dir)
    baseline = data["baseline"]
    pairs = {
        "radial_40_to_60": compare_pair(data["baseline"], data["radial60"]),
        "radial_60_to_80": compare_pair(data["radial60"], data["radial80"]),
        "energy_100_to_150": compare_pair(data["baseline"], data["energy150"]),
        "energy_150_to_200": compare_pair(data["energy150"], data["energy200"]),
        "angle_16_to_24": compare_pair(data["baseline"], data["angle24"]),
        "angle_24_to_32": compare_pair(data["angle24"], data["angle32"]),
        "path_32_to_48": compare_pair(data["baseline"], data["path48"]),
        "path_48_to_64": compare_pair(data["path48"], data["path64"]),
    }
    cases = {}
    for name, d in data.items():
        cases[name] = {
            "configuration": d["configuration"],
            "B16_metrics_vs_Fig7": d["variant_results"]["B16_reference"]["metrics_vs_fig7"],
            "B13_metrics_vs_Fig7": d["variant_results"][B13]["metrics_vs_fig7"],
            "B13_thin_luminosity_ratio_vs_B16": d["variant_results"][B13]["thin_luminosity_ratio_vs_B16"],
            "B13_strong_endpoint_escape_fraction": d["variant_results"][B13]["strong_endpoint_escape_fraction"],
            "B13_numerical_validation": d["B13_numerical_validation"],
            "B16_archived_closure_residual": d["archived_B16_baseline"]["max_relative_reproduction_residual"],
            "B16_radial_shell_diagnostics": shell_diagnostics(d, "B16_reference"),
            "B13_radial_shell_diagnostics": shell_diagnostics(d, B13),
        }

    finest = {
        "radial": ("radial_60_to_80", 0.01, 0.01, 0.02),
        "energy": ("energy_150_to_200", 0.01, 0.01, 0.02),
        "angular": ("angle_24_to_32", 0.01, 0.01, 0.02),
        "path": ("path_48_to_64", 0.01, 0.01, 0.02),
    }
    acceptance = {}
    for dimension, (pair, thin_tol, peak_tol, strong_tol) in finest.items():
        m = pairs[pair][B13]
        a = m["Lthin"]["max_abs_relative_change"] < thin_tol
        b = abs(m["Ltotal"]["reference_peak_relative_change"]) < peak_tol
        c = abs(m["Ltotal"]["strong_endpoint_relative_change"]) < strong_tol
        acceptance[dimension] = {
            "comparison": pair, "Lthin_max_change_below_1pct": a,
            "peak_Ltotal_change_below_1pct": b,
            "strong_endpoint_Ltotal_change_below_2pct": c,
            "passed": a and b and c,
        }

    aggregate = {
        "title": "Global B.13 exact-Compton transport convergence audit",
        "date": "2026-11-09", "mass_MeV": 10.0,
        "profile_sha256": baseline["profile"]["sha256"],
        "fixed_physics": {
            "current": "pure vector, g_V=1, g_A=0",
            "B13_kernel_orders": [12, 8, 8, 8],
            "B13_refined_point_check_orders": [16, 10, 10, 10],
            "B2": "published scalar, polarization-summed, fixed-omega Eq. (B.2)",
            "charge_convention": "mu-minus only, matching the single-species Eq. (B.17)",
            "profile_provenance": "1687-row vertex-preserving reconstruction from public figures; not raw Garching output",
        },
        "cases": cases, "pairwise_convergence": pairs,
        "acceptance": acceptance,
        "overall_passed": all(x["passed"] for x in acceptance.values()),
        "interpretation": (
            "The numerical tolerances are audit criteria, not physical bounds. "
            "Pesc and radial-shell fractions are retained separately to expose source/escape cancellations."
        ),
    }
    aggregate_path.parent.mkdir(parents=True, exist_ok=True)
    aggregate_path.write_text(json.dumps(aggregate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in sorted(input_dir.glob("summary_*.json")):
        destination = output_dir / path.name
        # input_dir and output_dir may intentionally be identical in CI.
        if path.resolve() == destination.resolve():
            continue
        shutil.copy2(path, destination)

    lines = [
        "# Global B.13 exact-Compton transport convergence audit", "",
        "Date: 2026-11-09  ",
        "Status: **" + ("all finest-step criteria passed" if aggregate["overall_passed"] else "one or more finest-step criteria not yet passed") + "**", "",
        "## 1. Scope and fixed physics", "",
        "This is Phase A only: global radial, energy, direction, and path quadrature convergence at the 10 MeV pure-vector benchmark. The B.13 local collision-kernel quadrature remains fixed at (12, 8, 8, 8), with the existing pointwise refinement check at (16, 10, 10, 10). No collision model, stellar profile, B.2 propagation convention, coupling normalization, or axial-vector calculation is changed.", "",
        f"- Profile SHA-256: {baseline['profile']['sha256']}",
        "- Profile: 1687-row vertex-preserving reconstruction from public figures; not the original Garching raw simulation table.",
        "- Transport: scalar, polarization-summed, fixed-omega Eq. (B.2).",
        "- B.13 Compton source and reduced opacity are replaced together.",
        "- Primary charge convention: mu-minus only, matching Eq. (B.17).",
        "- Every scan point regenerates the B.16 reference on the identical grid and checks its closure before the B.13 replacement.", "",
        "## 2. Grid configurations", "",
        "| Case | Radial order | Energy order | Direction order | Path order |",
        "|---|---:|---:|---:|---:|",
    ]
    for name, cfg in EXPECTED.items():
        lines.append(f"| {name} | {cfg[0]} | {cfg[1]} | {cfg[2]} | {cfg[3]} |")
    lines += [
        "",
        "The radial rule is composite over fixed interfaces at 0, 5, 8, 10, 12, 15, 18, 20, 22, 24, and 25 km. The final energy grid also includes radius-dependent emission-threshold nodes, so its node count exceeds the input energy order.", "",
        "## 3. Pairwise convergence shifts", "",
        "Each row changes only the named quadrature dimension. Shifts are fine grid relative to the immediately coarser grid. The table shows the B.13 mu-minus consistent source-plus-opacity result.", "",
        "| Refinement | max all-coupling |ΔLthin| | max all-coupling |ΔPesc| | |ΔLtotal| at Fig. 7 peak | |ΔLtotal| at strong endpoint |",
        "|---|---:|---:|---:|---:|",
    ]
    for name, pair in pairs.items():
        m = pair[B13]
        lines.append(f"| {name.replace('_', ' ')} | {pct(m['Lthin']['max_abs_relative_change'])} | {pct(m['Pesc']['max_abs_relative_change'])} | {pct(abs(m['Ltotal']['reference_peak_relative_change']))} | {pct(abs(m['Ltotal']['strong_endpoint_relative_change']))} |")
    lines += [
        "",
        "The machine-readable result also reports the same shifts for the B.16 reference implementation, separating convergence of the published approximate kernel from convergence of the exact B.13 replacement.", "",
        "## 4. Finest-step acceptance", "",
        "Provisional audit criteria: maximum all-coupling change in optically thin luminosity below 1%; change in luminosity at the digitized Fig. 7 peak below 1%; and change at the strong-coupling endpoint below 2%. These are numerical tolerances, not physical bounds.", "",
        "| Dimension | Finest comparison | Lthin < 1% | Peak Ltotal < 1% | Strong-end Ltotal < 2% | Result |",
        "|---|---|---:|---:|---:|---|",
    ]
    for dim, item in acceptance.items():
        lines.append(f"| {dim} | {item['comparison'].replace('_', ' ')} | {'PASS' if item['Lthin_max_change_below_1pct'] else 'FAIL'} | {'PASS' if item['peak_Ltotal_change_below_1pct'] else 'FAIL'} | {'PASS' if item['strong_endpoint_Ltotal_change_below_2pct'] else 'FAIL'} | **{'PASS' if item['passed'] else 'NOT YET PASSED'}** |")
    lines += [
        "",
        "## 5. Escape and radial-source diagnostics", "",
        "Pesc is reported separately because source and escape changes can cancel in Ltotal. The aggregate JSON records the 5–10 km and 10–15 km fractions of the B.1 source and escaped strong-endpoint luminosity for B.16 and B.13.", "",
        "| Case | B.13 source, 5–10 km | B.13 escaped L, 5–10 km | B.13 source, 10–15 km | B.13 escaped L, 10–15 km |",
        "|---|---:|---:|---:|---:|",
    ]
    for name, item in cases.items():
        d = item["B13_radial_shell_diagnostics"]
        lines.append(f"| {name} | {pct(d['5_10km']['source_fraction'])} | {pct(d['5_10km']['escaped_luminosity_fraction'])} | {pct(d['10_15km']['source_fraction'])} | {pct(d['10_15km']['escaped_luminosity_fraction'])} |")
    lines += [
        "",
        "## 6. Closure and decision", "",
        "Every grid point must reproduce its own same-grid B.16 baseline with maximum relative residual below 2e-10. B.13 detailed-balance, absorption/production, and final muon-shell residuals must remain below 1e-10. Each job commits its compact numerical summary directly to the research branch. Full local-rate arrays and matching B.16 files are generated in the job workspace but are not persisted; the exact configurations and scripts allow them to be regenerated.", "",
        "No empirical source, opacity, coupling, or luminosity rescaling is applied. No axial-vector curve is regenerated or modified. If a finest-step criterion fails, Phase A remains open and only the failed quadrature dimension is refined.", "",
        "## 7. Reproducibility", "",
        "- Aggregate JSON: outputs/b13_global_convergence_summary_2026-11-09.json",
        "- Per-grid summaries: outputs/b13_global_convergence_2026-11-09/summary_*.json",
        "- Full local-rate arrays and matched B.16 files: associated GitHub Actions workflow artifacts.",
        "- Scripts: audit_b16_global_redshift.py, audit_b13_global_transport.py, summarize_b13_global_transport.py, summarize_b13_convergence.py.",
    ]
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return aggregate


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input-dir", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--report", type=Path, required=True)
    p.add_argument("--aggregate", type=Path, required=True)
    a = p.parse_args()
    result = build_report(a.input_dir, a.output_dir, a.report, a.aggregate)
    print(json.dumps({"overall_passed": result["overall_passed"],
                      "acceptance": result["acceptance"],
                      "cases": list(result["cases"]),
                      "report": str(a.report), "aggregate": str(a.aggregate)},
                     indent=2), flush=True)


if __name__ == "__main__":
    main()
