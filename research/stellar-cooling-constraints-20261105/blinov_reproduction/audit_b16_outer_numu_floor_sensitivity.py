#!/usr/bin/env python3
"""Stress-test the unresolved mu_numu figure-floor convention in 20--22 km.

The baseline sets mu_numu=0 outside the resolved Caputo branches. This audit
recomputes the complete B.1 source and B.2 opacity after assigning +/-1 MeV
through 20--22 km, the plotted resolution-floor scale. These are stress tests,
not inferred profiles or statistical uncertainty intervals.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import tempfile
from pathlib import Path

try:
    from .audit_b16_emission_radius_escape import run_audit, DEFAULT_PROFILE, DEFAULT_FIG7
except ImportError:
    from audit_b16_emission_radius_escape import run_audit, DEFAULT_PROFILE, DEFAULT_FIG7

HERE = Path(__file__).resolve().parent
DEFAULT_JSON = HERE / "outputs" / "b16_outer_numu_floor_sensitivity_20_22km_10mev_2026-11-09.json"
DEFAULT_MD = HERE / "B16_OUTER_NUMU_FLOOR_SENSITIVITY_20_22KM_2026-11-09.md"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
R_MIN, R_MAX = 20.0, 22.0
SCENARIOS = {"mu_numu_minus_1MeV": -1.0, "baseline_zero": 0.0, "mu_numu_plus_1MeV": 1.0}
POINTS = {"weak_endpoint": 0, "reference_peak": 17, "strong_endpoint": 24}
EMISSION_SHELLS_8_15 = {"8-10 km", "10-12 km", "12-15 km"}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def transform_profile(source, destination, value):
    with Path(source).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    selected, original = [], []
    for row in rows:
        r = float(row["r_km"])
        if R_MIN <= r <= R_MAX:
            original.append(float(row["mu_numu_MeV"]))
            selected.append(r)
            row["mu_numu_MeV"] = format(value, ".15g")
    if len(selected) < 2 or selected[0] > R_MIN+1e-8 or selected[-1] < R_MAX-1e-8:
        raise RuntimeError(f"20--22 km mu_numu support incomplete: n={len(selected)}")
    if max(abs(x) for x in original) > 1e-12:
        raise RuntimeError("Baseline mu_numu is not zero throughout 20--22 km; inspect before applying floor stress test")
    with Path(destination).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return {
        "support_km": [R_MIN, R_MAX],
        "node_count": len(selected),
        "baseline_mu_numu_range_MeV": [min(original), max(original)],
        "assigned_mu_numu_MeV": value,
    }


def path_tau_fraction(result, emission_shells=None):
    matrix = result["source_weighted_mean_tau_by_emission_and_absorption_shell"]["neutrino"]
    numerator = denominator = 0.0
    for row in matrix:
        if emission_shells is not None and row["emission_shell"] not in emission_shells:
            continue
        w = float(row["source_weight"])
        denominator += w*float(row["mean_total_tau_per_g2"])
        for shell in row["mean_tau_by_absorption_shell"]:
            if shell["absorption_shell"] == "20-22 km":
                numerator += w*float(shell["mean_tau_per_g2"])
    return numerator/denominator if denominator else None


def point_summary(point):
    return {
        "index": int(point["index"]),
        "g": float(point["g"]),
        "L_thin_erg_s": float(point["optically_thin_luminosity_erg_s"]),
        "P_escape": float(point["global_escape_fraction"]),
        "L_escaped_erg_s": float(point["calculated_luminosity_erg_s"]),
        "L_Fig7_erg_s": float(point["reference_luminosity_erg_s"]),
        "relative_difference_vs_Fig7": float(point["relative_difference_vs_fig7"]),
    }


def run(profile_path=DEFAULT_PROFILE, fig7_path=DEFAULT_FIG7,
        mass=10.0, nr=40, ne=100, na=32, ns=32, radius=25.0, energy_offset=1000.0):
    profile_path, fig7_path = Path(profile_path), Path(fig7_path)
    profile_hash = sha256(profile_path)
    if profile_hash != EXPECTED_PROFILE_SHA256:
        raise RuntimeError(f"Unexpected profile SHA-256: {profile_hash}")
    scenarios = {}
    with tempfile.TemporaryDirectory(prefix="b16_outer_numu_floor_20_22_") as tmp:
        tmp = Path(tmp)
        for name, value in SCENARIOS.items():
            altered = tmp / f"profile_{name}.csv"
            transform = transform_profile(profile_path, altered, value)
            result = run_audit(altered, fig7_path, mass, nr, ne, na, ns, radius, energy_offset)
            by_index = {int(p["index"]): p for p in result["representative_couplings"]}
            source_shells = result["optically_thin_source_radial_distribution"]["shells"]
            source_fraction = next(
                (float(x["source_fraction"]) for x in source_shells if x["shell"] == "20-22 km"),
                None,
            )
            scenarios[name] = {
                "profile_transform": transform,
                "points": {label: point_summary(by_index[index]) for label,index in POINTS.items()},
                "B1_source_fraction_emitted_in_20_22km": source_fraction,
                "B2_neutrino_path_tau_fraction_20_22km_all_emission": path_tau_fraction(result),
                "B2_neutrino_path_tau_fraction_20_22km_8_15km_emission": path_tau_fraction(result, EMISSION_SHELLS_8_15),
                "internal_closure": result["internal_closure"],
            }
    baseline = scenarios["baseline_zero"]
    comparisons = {}
    for name, scenario in scenarios.items():
        if name == "baseline_zero":
            continue
        comparisons[name] = {}
        for label, point in scenario["points"].items():
            base = baseline["points"][label]
            comparisons[name][label] = {
                "thin_source_ratio_vs_baseline": point["L_thin_erg_s"]/base["L_thin_erg_s"],
                "escape_probability_ratio_vs_baseline": point["P_escape"]/base["P_escape"],
                "escaped_luminosity_ratio_vs_baseline": point["L_escaped_erg_s"]/base["L_escaped_erg_s"],
                "Fig7_relative_difference_shift": point["relative_difference_vs_Fig7"]-base["relative_difference_vs_Fig7"],
            }
    sign_symmetry = {}
    for label in POINTS:
        minus = scenarios["mu_numu_minus_1MeV"]["points"][label]
        plus = scenarios["mu_numu_plus_1MeV"]["points"][label]
        sign_symmetry[label] = {
            "escaped_luminosity_plus_over_minus": plus["L_escaped_erg_s"]/minus["L_escaped_erg_s"],
            "escape_probability_plus_over_minus": plus["P_escape"]/minus["P_escape"],
        }
    return {
        "title": "B.16 sensitivity to the unresolved mu_numu floor in 20--22 km",
        "mass_MeV": mass,
        "profile_sha256": profile_hash,
        "fig7_reference_sha256": sha256(fig7_path),
        "varied_field": "mu_numu_MeV only, for 20 <= r_km <= 22",
        "scenarios_MeV": SCENARIOS,
        "configuration": {
            "radial_order": nr, "energy_order": ne, "angular_order": na,
            "path_order": ns, "radius_km": radius, "energy_offset_MeV": energy_offset,
        },
        "interpretation_limits": [
            "The +/-1 MeV assignments are figure-resolution-floor stress tests, not measured chemical-potential profiles.",
            "Each scenario recomputes the complete B.1 source and B.2 opacity; no source or opacity is rescaled.",
            "The original Bollig Fig. 1 and Fig. 4 plotting frames stop at 20 km; this 20--22 km chemical-potential continuation is not independently verified by those figures.",
            "The baseline profile sets mu_numu=0 in this interval because no branch is resolved there.",
            "Production axial-vector files and constraints are not modified.",
        ],
        "scenarios": scenarios,
        "comparisons_to_baseline": comparisons,
        "charge_conjugation_sign_crosscheck": sign_symmetry,
    }


def make_report(data):
    def pct(x):
        return f"{100*x:.6g}%"
    lines = [
        "# B.16 unresolved mu_numu floor sensitivity in 20--22 km",
        "",
        "Date: 2026-11-09",
        "Benchmark: 10 MeV pure-vector B.16 reference, fixed-omega B.2.",
        "",
        "## Motivation",
        "",
        "The Caputo reconstruction sets mu_numu=0 in 20--22 km because no resolved branch is present above the approximately 1 MeV figure floor. Bollig Figs. 1 and 4 do not cover this radial interval. The 20--22 km shell contributes about 12.7--12.8% of the source-weighted neutrino inverse-decay path optical depth for the dominant 8--15 km emission region.",
        "",
        "## Controlled variation",
        "",
        f"- Profile SHA-256: {data['profile_sha256']}",
        "- Only mu_numu is varied, and only in 20--22 km; T, mu_mu, lapse, radial grid, and all other inputs are fixed.",
        "- The assigned values +1 MeV and -1 MeV are figure-floor stress tests, not inferred profiles or statistical uncertainty intervals.",
        "- Every scenario recomputes the complete B.1 source and B.2 opacity.",
        f"- Global quadrature: N_r={data['configuration']['radial_order']}, N_E={data['configuration']['energy_order']}, N_omega={data['configuration']['angular_order']}, N_s={data['configuration']['path_order']}.",
        "",
        "## Results",
        "",
        "| mu_numu in 20--22 km | Weak L_escaped / baseline | Peak L_escaped / baseline | Strong L_escaped / baseline | Strong P_escape / baseline |",
        "|---:|---:|---:|---:|---:|",
        "| -1 MeV | " + pct(data["comparisons_to_baseline"]["mu_numu_minus_1MeV"]["weak_endpoint"]["escaped_luminosity_ratio_vs_baseline"]) + " | " + pct(data["comparisons_to_baseline"]["mu_numu_minus_1MeV"]["reference_peak"]["escaped_luminosity_ratio_vs_baseline"]) + " | " + pct(data["comparisons_to_baseline"]["mu_numu_minus_1MeV"]["strong_endpoint"]["escaped_luminosity_ratio_vs_baseline"]) + " | " + pct(data["comparisons_to_baseline"]["mu_numu_minus_1MeV"]["strong_endpoint"]["escape_probability_ratio_vs_baseline"]) + " |",
        "| 0 MeV | 100% | 100% | 100% | 100% |",
        "| +1 MeV | " + pct(data["comparisons_to_baseline"]["mu_numu_plus_1MeV"]["weak_endpoint"]["escaped_luminosity_ratio_vs_baseline"]) + " | " + pct(data["comparisons_to_baseline"]["mu_numu_plus_1MeV"]["reference_peak"]["escaped_luminosity_ratio_vs_baseline"]) + " | " + pct(data["comparisons_to_baseline"]["mu_numu_plus_1MeV"]["strong_endpoint"]["escaped_luminosity_ratio_vs_baseline"]) + " | " + pct(data["comparisons_to_baseline"]["mu_numu_plus_1MeV"]["strong_endpoint"]["escape_probability_ratio_vs_baseline"]) + " |",
        "",
        "## Baseline diagnostics",
        "",
        f"- B.1 thin-source fraction emitted in 20--22 km: {pct(data['scenarios']['baseline_zero']['B1_source_fraction_emitted_in_20_22km'])}.",
        f"- B.2 neutrino path-tau fraction in 20--22 km for 8--15 km emission: {pct(data['scenarios']['baseline_zero']['B2_neutrino_path_tau_fraction_20_22km_8_15km_emission'])}.",
        "",
        "## Sign symmetry and interpretation",
        "",
        "The +1 MeV and -1 MeV cases are compared explicitly. A near-unity ratio is a numerical check of the expected charge-conjugation symmetry of the pair-production/absorption phase space under the symmetric angular integration; any residual is reported rather than assumed away.",
        "",
        "The stress test quantifies only the unresolved chemical-potential floor. It does not establish the true mu_numu profile and is not used to tune the background or rescale the vector curve.",
        "",
        "## Reproducibility",
        "",
        "- Script: audit_b16_outer_numu_floor_sensitivity.py",
        "- Machine-readable output: outputs/b16_outer_numu_floor_sensitivity_20_22km_10mev_2026-11-09.json",
        "- Production axial-vector files and constraints remain unchanged.",
        "",
    ]
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    p.add_argument("--fig7", type=Path, default=DEFAULT_FIG7)
    p.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    p.add_argument("--output-md", type=Path, default=DEFAULT_MD)
    p.add_argument("--mass", type=float, default=10.0)
    p.add_argument("--nr", type=int, default=40)
    p.add_argument("--ne", type=int, default=100)
    p.add_argument("--na", type=int, default=32)
    p.add_argument("--ns", type=int, default=32)
    p.add_argument("--radius", type=float, default=25.0)
    p.add_argument("--energy-offset", type=float, default=1000.0)
    a = p.parse_args()
    data = run(a.profile,a.fig7,a.mass,a.nr,a.ne,a.na,a.ns,a.radius,a.energy_offset)
    a.output_json.parent.mkdir(parents=True,exist_ok=True)
    a.output_md.parent.mkdir(parents=True,exist_ok=True)
    a.output_json.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    a.output_md.write_text(make_report(data),encoding="utf-8")
    print(json.dumps({
        "comparisons_to_baseline": data["comparisons_to_baseline"],
        "charge_conjugation_sign_crosscheck": data["charge_conjugation_sign_crosscheck"],
        "baseline_source_fraction": data["scenarios"]["baseline_zero"]["B1_source_fraction_emitted_in_20_22km"],
        "baseline_20_22_path_tau_fraction": data["scenarios"]["baseline_zero"]["B2_neutrino_path_tau_fraction_20_22km_8_15km_emission"],
    },indent=2))
    print(f"Saved {a.output_json}")
    print(f"Saved {a.output_md}")


if __name__ == "__main__":
    main()
