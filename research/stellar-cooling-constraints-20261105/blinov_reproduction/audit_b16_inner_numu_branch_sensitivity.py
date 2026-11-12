#!/usr/bin/env python3
"""Stress-test the negative Caputo mu_numu branch in the 8--12 km shell.

The full B.1 source and B.2 opacity are recomputed after scaling the baseline
negative mu_numu branch. This includes an exact sign-flip symmetry diagnostic,
a zero-branch counterfactual, and +/-10% magnitude stresses. None is a proposed
profile correction or statistical uncertainty interval.
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
DEFAULT_JSON = HERE / "outputs" / "b16_inner_numu_branch_sensitivity_8_12km_10mev_2026-11-09.json"
DEFAULT_MD = HERE / "B16_INNER_NUMU_BRANCH_SENSITIVITY_8_12KM_2026-11-09.md"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
R_MIN, R_MAX = 8.0, 12.0
SCALES = (-1.0, 0.0, 0.9, 1.0, 1.1)
POINTS = {"weak_endpoint": 0, "reference_peak": 17, "strong_endpoint": 24}
ABSORPTION_SHELLS = {"8-10 km", "10-12 km"}
EMISSION_SHELLS_8_15 = {"8-10 km", "10-12 km", "12-15 km"}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scale_name(scale):
    return f"mu_numu_scale_{scale:g}"


def transform_profile(source, destination, scale):
    with Path(source).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    selected, original, ratios = [], [], []
    for row in rows:
        r = float(row["r_km"])
        if R_MIN <= r <= R_MAX:
            t = float(row["T_MeV"])
            mu = float(row["mu_numu_MeV"])
            selected.append(r)
            original.append(mu)
            ratios.append(mu/t)
            row["mu_numu_MeV"] = format(mu*scale, ".15g")
    if len(selected) < 2 or selected[0] > R_MIN+1e-8 or selected[-1] < R_MAX-1e-8:
        raise RuntimeError(f"8--12 km mu_numu branch support incomplete: n={len(selected)}")
    if max(original) >= -1e-6:
        raise RuntimeError("The 8--12 km baseline is not strictly the negative mu_numu branch")
    with Path(destination).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return {
        "support_km":[R_MIN,R_MAX],
        "node_count":len(selected),
        "baseline_mu_numu_range_MeV":[min(original),max(original)],
        "baseline_mu_numu_over_T_range":[min(ratios),max(ratios)],
        "scale":scale,
        "assigned_mu_numu_range_MeV":[min(x*scale for x in original),max(x*scale for x in original)],
    }


def path_tau_fraction(result, emission_shells=None):
    matrix=result["source_weighted_mean_tau_by_emission_and_absorption_shell"]["neutrino"]
    numerator=denominator=0.0
    for row in matrix:
        if emission_shells is not None and row["emission_shell"] not in emission_shells:
            continue
        w=float(row["source_weight"])
        denominator+=w*float(row["mean_total_tau_per_g2"])
        for shell in row["mean_tau_by_absorption_shell"]:
            if shell["absorption_shell"] in ABSORPTION_SHELLS:
                numerator+=w*float(shell["mean_tau_per_g2"])
    return numerator/denominator if denominator else None


def source_fraction_8_12(result):
    shells=result["optically_thin_source_radial_distribution"]["shells"]
    return sum(float(x["source_fraction"]) for x in shells if x["shell"] in ABSORPTION_SHELLS)


def point_summary(point):
    return {
        "index":int(point["index"]),
        "g":float(point["g"]),
        "L_thin_erg_s":float(point["optically_thin_luminosity_erg_s"]),
        "P_escape":float(point["global_escape_fraction"]),
        "L_escaped_erg_s":float(point["calculated_luminosity_erg_s"]),
        "L_Fig7_erg_s":float(point["reference_luminosity_erg_s"]),
        "relative_difference_vs_Fig7":float(point["relative_difference_vs_fig7"]),
    }


def run(profile_path=DEFAULT_PROFILE,fig7_path=DEFAULT_FIG7,
        mass=10.0,nr=40,ne=100,na=32,ns=32,radius=25.0,energy_offset=1000.0):
    profile_path,fig7_path=Path(profile_path),Path(fig7_path)
    profile_hash=sha256(profile_path)
    if profile_hash!=EXPECTED_PROFILE_SHA256:
        raise RuntimeError("Unexpected profile SHA-256: "+profile_hash)
    scenarios={}
    with tempfile.TemporaryDirectory(prefix="b16_inner_numu_8_12_") as tmp:
        tmp=Path(tmp)
        for scale in SCALES:
            name=scale_name(scale)
            altered=tmp/f"profile_{name}.csv"
            transform=transform_profile(profile_path,altered,scale)
            result=run_audit(altered,fig7_path,mass,nr,ne,na,ns,radius,energy_offset)
            by_index={int(p["index"]):p for p in result["representative_couplings"]}
            scenarios[name]={
                "profile_transform":transform,
                "points":{label:point_summary(by_index[index]) for label,index in POINTS.items()},
                "B1_source_fraction_emitted_in_8_12km":source_fraction_8_12(result),
                "B2_neutrino_path_tau_fraction_8_12km_all_emission":path_tau_fraction(result),
                "B2_neutrino_path_tau_fraction_8_12km_8_15km_emission":path_tau_fraction(result,EMISSION_SHELLS_8_15),
                "internal_closure":result["internal_closure"],
            }
    baseline=scenarios[scale_name(1.0)]
    comparisons={}
    for name,scenario in scenarios.items():
        if name==scale_name(1.0):
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
    sign={}
    minus=scenarios[scale_name(-1.0)]
    for label in POINTS:
        plus=baseline["points"][label]
        flip=minus["points"][label]
        sign[label]={
            "sign_flip_escaped_luminosity_ratio":flip["L_escaped_erg_s"]/plus["L_escaped_erg_s"],
            "sign_flip_escape_probability_ratio":flip["P_escape"]/plus["P_escape"],
        }
    return {
        "title":"B.16 sensitivity to the negative mu_numu branch in 8--12 km",
        "mass_MeV":mass,
        "profile_sha256":profile_hash,
        "fig7_reference_sha256":sha256(fig7_path),
        "varied_field":"mu_numu_MeV only, for 8 <= r_km <= 12",
        "scales":list(SCALES),
        "configuration":{
            "radial_order":nr,"energy_order":ne,"angular_order":na,
            "path_order":ns,"radius_km":radius,"energy_offset_MeV":energy_offset,
        },
        "interpretation_limits":[
            "The scale=0 case is an extreme zero-branch counterfactual; 0.9 and 1.1 are +/-10% magnitude stresses.",
            "The scale=-1 case flips the sign only as a charge-conjugation symmetry diagnostic; it is not a physical alternative profile.",
            "Each scenario recomputes the complete B.1 source and B.2 opacity; no source or opacity is rescaled.",
            "The negative mu_numu branch is encoded in the visible Caputo Fig. 1 profile but is not independently cross-checked by Bollig Figs. 1 and 4.",
            "Production axial-vector files and constraints are not modified.",
        ],
        "scenarios":scenarios,
        "comparisons_to_baseline":comparisons,
        "charge_conjugation_sign_crosscheck":sign,
    }


def make_report(data):
    def pct(x):
        return "n/a" if x is None else f"{100*x:.6g}%"
    lines=[
        "# B.16 negative mu_numu branch sensitivity in 8--12 km",
        "",
        "Date: 2026-11-09",
        "Benchmark: 10 MeV pure-vector B.16 reference, fixed-omega B.2.",
        "",
        "## Motivation",
        "",
        "The Caputo profile contains a resolved negative mu_numu branch throughout 8--12 km. Its baseline range is -20.43 to -4.31 MeV, with mu_numu/T from -0.526 to -0.166. This interval lies in the main 8--15 km emission region and contributes appreciably to the neutrino inverse-decay path. The 12--15 km figure-floor test does not test this larger inner negative branch.",
        "",
        "## Controlled variations",
        "",
        f"- Profile SHA-256: {data['profile_sha256']}",
        "- Only mu_numu is changed, only in 8--12 km. T, mu_mu, lapse, radial grid, energy grid, angular quadrature, path quadrature, couplings, and Fig. 7 reference are fixed.",
        "- scale=0 removes the branch; scales 0.9 and 1.1 vary its magnitude by +/-10%; scale=-1 flips the sign solely as a symmetry diagnostic.",
        "- Every scenario recomputes the complete B.1 source and B.2 opacity.",
        f"- Global quadrature: N_r={data['configuration']['radial_order']}, N_E={data['configuration']['energy_order']}, N_omega={data['configuration']['angular_order']}, N_s={data['configuration']['path_order']}.",
        "",
        "## Strong-endpoint results",
        "",
        "| mu_numu treatment in 8--12 km | L_escaped / baseline | P_escape / baseline | Shift in L/L_Fig.7 - 1 |",
        "|---|---:|---:|---:|",
    ]
    for scale in (-1.0,0.0,0.9,1.0,1.1):
        name=scale_name(scale)
        if scale==1.0:
            lines.append("| baseline negative branch | 100% | 100% | 0 |")
        else:
            c=data["comparisons_to_baseline"][name]["strong_endpoint"]
            label={-1.0:"sign-flipped branch",0.0:"branch set to zero",0.9:"magnitude reduced 10%",1.1:"magnitude increased 10%"}[scale]
            lines.append(f"| {label} | {pct(c['escaped_luminosity_ratio_vs_baseline'])} | {pct(c['escape_probability_ratio_vs_baseline'])} | {pct(c['Fig7_relative_difference_shift'])} |")
    base=data["scenarios"][scale_name(1.0)]
    lines.extend([
        "",
        "## Baseline diagnostics",
        "",
        f"- B.1 thin-source fraction emitted in 8--12 km: {pct(base['B1_source_fraction_emitted_in_8_12km'])}.",
        f"- B.2 neutrino path-tau fraction in 8--12 km for 8--15 km emission: {pct(base['B2_neutrino_path_tau_fraction_8_12km_8_15km_emission'])}.",
        f"- B.2 neutrino path-tau fraction in 8--12 km for all emission radii: {pct(base['B2_neutrino_path_tau_fraction_8_12km_all_emission'])}.",
        "",
        "## Charge-conjugation sign check",
        "",
        "| Coupling point | L(sign-flipped)/L(baseline) | P_escape(sign-flipped)/P_escape(baseline) |",
        "|---|---:|---:|",
    ])
    for label,values in data["charge_conjugation_sign_crosscheck"].items():
        lines.append(f"| {label} | {values['sign_flip_escaped_luminosity_ratio']:.12g} | {values['sign_flip_escape_probability_ratio']:.12g} |")
    lines.extend([
        "",
        "## Interpretation",
        "",
        "The sign-flip test checks whether the integrated neutrino-antineutrino pair phase space is invariant under mu_numu -> -mu_numu after symmetric angular integration. The magnitude and zero-branch tests quantify the sensitivity to the negative branch itself.",
        "",
        "The scale=0 case is an extreme counterfactual, not a proposed physical profile. The +/-10% cases are controlled stress tests, not statistical uncertainty intervals. No profile or luminosity rescaling is applied.",
        "",
        "## Reproducibility",
        "",
        "- Script: audit_b16_inner_numu_branch_sensitivity.py",
        "- Machine-readable output: outputs/b16_inner_numu_branch_sensitivity_8_12km_10mev_2026-11-09.json",
        "- Production axial-vector files and constraints remain unchanged.",
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
        "charge_conjugation_sign_crosscheck":data["charge_conjugation_sign_crosscheck"],
        "baseline_source_fraction_8_12":data["scenarios"][scale_name(1.0)]["B1_source_fraction_emitted_in_8_12km"],
        "baseline_path_tau_fraction_8_12":data["scenarios"][scale_name(1.0)]["B2_neutrino_path_tau_fraction_8_12km_8_15km_emission"],
    },indent=2))
    print(f"Saved {a.output_json}")
    print(f"Saved {a.output_md}")


if __name__=="__main__":
    main()
