#!/usr/bin/env python3
"""Stress-test the Caputo off-frame temperature in the 22--25 km B.2 path shell.

The complete B.1 source and B.2 opacity are recomputed for each temperature
variation. This is a controlled stress diagnostic, not a statistical
uncertainty band or a proposed correction to the reconstructed profile.
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
DEFAULT_JSON = HERE / "outputs" / "b16_outer_temperature_sensitivity_22_25km_10mev_2026-11-09.json"
DEFAULT_MD = HERE / "B16_OUTER_TEMPERATURE_SENSITIVITY_22_25KM_2026-11-09.md"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
R_MIN, R_MAX = 22.0, 25.0
SCALES = (0.9, 1.0, 1.1)
POINTS = {"weak_endpoint": 0, "reference_peak": 17, "strong_endpoint": 24}
EMISSION_SHELLS_8_15 = {"8-10 km", "10-12 km", "12-15 km"}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def transform_profile(source, destination, scale):
    with Path(source).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    selected, original = [], []
    for row in rows:
        r = float(row["r_km"])
        if R_MIN <= r <= R_MAX:
            t = float(row["T_MeV"])
            selected.append(r)
            original.append(t)
            row["T_MeV"] = format(t*scale, ".15g")
    if len(selected) < 2 or selected[0] > R_MIN+1e-8 or selected[-1] < R_MAX-1e-8:
        raise RuntimeError(f"22--25 km profile support incomplete: n={len(selected)}")
    with Path(destination).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return {
        "support_km": [R_MIN,R_MAX],
        "node_count": len(selected),
        "original_T_range_MeV": [min(original),max(original)],
        "scale": scale,
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
            if shell["absorption_shell"] == "22-25 km":
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


def run(profile_path=DEFAULT_PROFILE,fig7_path=DEFAULT_FIG7,
        mass=10.0,nr=40,ne=100,na=32,ns=32,radius=25.0,energy_offset=1000.0):
    profile_path,fig7_path=Path(profile_path),Path(fig7_path)
    profile_hash=sha256(profile_path)
    if profile_hash!=EXPECTED_PROFILE_SHA256:
        raise RuntimeError("Unexpected profile SHA-256: "+profile_hash)
    scenarios={}
    with tempfile.TemporaryDirectory(prefix="b16_outer_T_22_25_") as tmp:
        tmp=Path(tmp)
        for scale in SCALES:
            altered=tmp/f"profile_T22_25_scale_{scale:g}.csv"
            transform=transform_profile(profile_path,altered,scale)
            result=run_audit(altered,fig7_path,mass,nr,ne,na,ns,radius,energy_offset)
            by_index={int(p["index"]):p for p in result["representative_couplings"]}
            source_shells=result["optically_thin_source_radial_distribution"]["shells"]
            source_fraction=next(
                (float(x["source_fraction"]) for x in source_shells if x["shell"]=="22-25 km"),
                None,
            )
            scenarios[f"T_scale_{scale:g}"]={
                "profile_transform":transform,
                "points":{label:point_summary(by_index[index]) for label,index in POINTS.items()},
                "B1_source_fraction_emitted_in_22_25km":source_fraction,
                "B2_neutrino_path_tau_fraction_22_25km_all_emission":path_tau_fraction(result),
                "B2_neutrino_path_tau_fraction_22_25km_8_15km_emission":path_tau_fraction(result,EMISSION_SHELLS_8_15),
                "internal_closure":result["internal_closure"],
            }
    baseline=scenarios["T_scale_1"]
    comparisons={}
    for name,scenario in scenarios.items():
        if name=="T_scale_1":
            continue
        comparisons[name]={}
        for label,point in scenario["points"].items():
            base=baseline["points"][label]
            comparisons[name][label]={
                "thin_source_ratio_vs_baseline":point["L_thin_erg_s"]/base["L_thin_erg_s"],
                "escape_probability_ratio_vs_baseline":point["P_escape"]/base["P_escape"],
                "escaped_luminosity_ratio_vs_baseline":point["L_escaped_erg_s"]/base["L_escaped_erg_s"],
                "Fig7_relative_difference_shift":point["relative_difference_vs_Fig7"]-base["relative_difference_vs_Fig7"],
            }
    return {
        "title":"B.16 sensitivity to Caputo off-frame T(r) in the 22--25 km path shell",
        "mass_MeV":mass,
        "profile_sha256":profile_hash,
        "fig7_reference_sha256":sha256(fig7_path),
        "varied_field":"T_MeV only, for 22 <= r_km <= 25",
        "scales":list(SCALES),
        "configuration":{
            "radial_order":nr,"energy_order":ne,"angular_order":na,
            "path_order":ns,"radius_km":radius,"energy_offset_MeV":energy_offset,
        },
        "interpretation_limits":[
            "The +/-10% variations are stress tests, not statistical uncertainty intervals.",
            "Every scenario recomputes the complete B.1 source and B.2 opacity; no source or opacity is rescaled.",
            "The original Bollig Figs. 1 and 4 stop at 20 km. The Caputo T path in 22--25 km is encoded off-frame PDF vector data, not visible plot data or raw Garching tables.",
            "The baseline profile is a public-figure reconstruction and its off-frame continuation is not independently cross-checked against Bollig beyond 20 km.",
            "Production axial-vector files and constraints are not modified.",
        ],
        "scenarios":scenarios,
        "comparisons_to_baseline":comparisons,
    }


def make_report(data):
    def pct(x):
        return "n/a" if x is None else f"{100*x:.6g}%"
    lines=[
        "# B.16 temperature sensitivity in the 22--25 km shell",
        "",
        "Date: 2026-11-09",
        "Benchmark: 10 MeV pure-vector B.16 reference, fixed-omega B.2.",
        "",
        "## Motivation",
        "",
        "The 22--25 km shell is outside the original Bollig Fig. 1 and Fig. 4 frames. The current Caputo T(r) values in this interval are encoded off-frame PDF vector vertices, not visible plot data and not raw Garching simulation tables. The earlier direction-resolved B.16 synthesis assigns about 19.07% of the source-weighted neutrino inverse-decay path optical depth to this shell for dominant 8--15 km emission.",
        "",
        "## Controlled variation",
        "",
        f"- Profile SHA-256: {data['profile_sha256']}",
        f"- Off-frame baseline temperature range: {data['scenarios']['T_scale_1']['profile_transform']['original_T_range_MeV']}",
        f"- Varied nodes: {data['scenarios']['T_scale_1']['profile_transform']['node_count']}",
        "- Only T_MeV is varied, and only for 22 <= r <= 25 km; mu_mu, mu_numu, lapse, radial grid, energy grid, angular quadrature, path quadrature, couplings, and Fig. 7 reference are fixed.",
        "- Scales 0.9 and 1.1 are stress tests, not statistical uncertainty intervals.",
        "- Every scenario recomputes the complete B.1 source and B.2 opacity.",
        f"- Global quadrature: N_r={data['configuration']['radial_order']}, N_E={data['configuration']['energy_order']}, N_omega={data['configuration']['angular_order']}, N_s={data['configuration']['path_order']}.",
        "",
        "## Results",
        "",
        "| T scale in 22--25 km | Weak L_escaped / baseline | Peak L_escaped / baseline | Strong L_escaped / baseline | Strong P_escape / baseline |",
        "|---:|---:|---:|---:|---:|",
    ]
    for scale in (0.9,1.0,1.1):
        if scale==1.0:
            lines.append("| 1.0 | 100% | 100% | 100% | 100% |")
        else:
            c=data["comparisons_to_baseline"][f"T_scale_{scale:g}"]
            lines.append(
                f"| {scale:.1f} | {pct(c['weak_endpoint']['escaped_luminosity_ratio_vs_baseline'])} | {pct(c['reference_peak']['escaped_luminosity_ratio_vs_baseline'])} | {pct(c['strong_endpoint']['escaped_luminosity_ratio_vs_baseline'])} | {pct(c['strong_endpoint']['escape_probability_ratio_vs_baseline'])} |"
            )
    base=data["scenarios"]["T_scale_1"]
    lines.extend([
        "",
        "## Baseline diagnostics",
        "",
        "| Quantity | Baseline value |",
        "|---|---:|",
        f"| B.1 thin-source fraction emitted in 22--25 km | {pct(base['B1_source_fraction_emitted_in_22_25km'])} |",
        f"| B.2 neutrino path-tau fraction in 22--25 km, all emission radii | {pct(base['B2_neutrino_path_tau_fraction_22_25km_all_emission'])} |",
        f"| B.2 neutrino path-tau fraction in 22--25 km, 8--15 km emission | {pct(base['B2_neutrino_path_tau_fraction_22_25km_8_15km_emission'])} |",
        "",
        "## Interpretation",
        "",
        "The comparison separates the small B.1 emission contribution from the B.2 propagation effect. A change in escaped luminosity is primarily an outer-path opacity sensitivity if the thin-source ratio remains close to unity.",
        "",
        "This is a stress test of the off-frame Caputo continuation, not a determination of the true uncertainty in the original SFHo-18.8 simulation. No result is used to tune the profile or rescale the vector curve.",
        "",
        "## Reproducibility",
        "",
        "- Script: audit_b16_outer_temperature_sensitivity_22_25km.py",
        "- Machine-readable output: outputs/b16_outer_temperature_sensitivity_22_25km_10mev_2026-11-09.json",
        "- Production axial-vector curve remains frozen.",
        "",
    ])
    return "\n".join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    p.add_argument("--fig7",type=Path,default=DEFAULT_FIG7)
    p.add_argument("--output-json",type=Path,default=DEFAULT_JSON)
    p.add_argument("--output-md",type=Path,default=DEFAULT_MD)
    p.add_argument("--mass",type=float,default=10.0)
    p.add_argument("--nr",type=int,default=40)
    p.add_argument("--ne",type=int,default=100)
    p.add_argument("--na",type=int,default=32)
    p.add_argument("--ns",type=int,default=32)
    p.add_argument("--radius",type=float,default=25.0)
    p.add_argument("--energy-offset",type=float,default=1000.0)
    a=p.parse_args()
    data=run(a.profile,a.fig7,a.mass,a.nr,a.ne,a.na,a.ns,a.radius,a.energy_offset)
    a.output_json.parent.mkdir(parents=True,exist_ok=True)
    a.output_md.parent.mkdir(parents=True,exist_ok=True)
    a.output_json.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    a.output_md.write_text(make_report(data),encoding="utf-8")
    print(json.dumps({
        "comparisons_to_baseline":data["comparisons_to_baseline"],
        "baseline_22_25_diagnostics":{
            "source_fraction":data["scenarios"]["T_scale_1"]["B1_source_fraction_emitted_in_22_25km"],
            "path_tau_fraction_all_emission":data["scenarios"]["T_scale_1"]["B2_neutrino_path_tau_fraction_22_25km_all_emission"],
            "path_tau_fraction_8_15_emission":data["scenarios"]["T_scale_1"]["B2_neutrino_path_tau_fraction_22_25km_8_15km_emission"],
        },
    },indent=2))
    print(f"Saved {a.output_json}")
    print(f"Saved {a.output_md}")


if __name__=="__main__":
    main()
