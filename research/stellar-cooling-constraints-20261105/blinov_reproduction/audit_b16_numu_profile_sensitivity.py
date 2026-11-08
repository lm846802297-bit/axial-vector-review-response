"""Stress-test the reconstructed muon-neutrino chemical-potential profile.

All other digitized background fields are held fixed. This is a profile-input
sensitivity diagnostic, not a claim that +/-10% is a statistical error bar.
The baseline B.1/B.2 fixed-omega calculation is rerun self-consistently for
each scaled mu_nu_mu profile.
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

HERE=Path(__file__).resolve().parent
DEFAULT_OUTPUT=HERE/"outputs"/"b16_numu_profile_sensitivity_10mev_2026-11-08.json"
SCALES=(0.0,0.9,1.0,1.1)
POINT_LABELS={"weak_endpoint":0,"fig7_peak":17,"strong_endpoint":24}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_scaled_profile(source: Path, destination: Path, scale: float):
    with source.open(newline="",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        fields=reader.fieldnames
        if not fields or "mu_numu_MeV" not in fields:
            raise ValueError("Profile must contain mu_numu_MeV")
        rows=list(reader)
    for row in rows:
        value=float(row["mu_numu_MeV"])
        row["mu_numu_MeV"]=format(scale*value,".12g")
    with destination.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def point_summary(point):
    thin=float(point["optically_thin_luminosity_erg_s"])
    escaped=float(point["calculated_luminosity_erg_s"])
    reference=float(point["reference_luminosity_erg_s"])
    pcalc=float(point["global_escape_fraction"])
    preq=reference/thin if thin>0 else None
    fractions={
        name:float(channel["fraction_of_total_thin_source"])
        for name,channel in point["source_channels"].items()
    }
    return {
        "index":int(point["index"]),
        "g":float(point["g"]),
        "L_thin_erg_s":thin,
        "P_escape_calculated":pcalc,
        "L_escaped_erg_s":escaped,
        "L_Fig7_erg_s":reference,
        "P_escape_required_for_Fig7":preq,
        "required_over_calculated_escape":preq/pcalc if pcalc>0 else None,
        "thin_source_channel_fractions":fractions,
    }


def run(profile_path=DEFAULT_PROFILE,fig7_path=DEFAULT_FIG7,mass=10.0,
        nr=40,ne=100,na=16,ns=32,radius=25.0,energy_offset=1000.0):
    scenarios={}
    with tempfile.TemporaryDirectory(prefix="b16_numu_profile_") as tmp:
        tmp=Path(tmp)
        for scale in SCALES:
            scaled=tmp/f"profile_numu_scale_{scale:g}.csv"
            write_scaled_profile(profile_path,scaled,scale)
            result=run_audit(
                scaled,fig7_path,mass,nr,ne,na,ns,radius,energy_offset
            )
            by_index={int(p["index"]):p for p in result["representative_couplings"]}
            scenarios[f"scale_{scale:g}"]={
                "mu_numu_scale":scale,
                "points":{
                    label:point_summary(by_index[idx])
                    for label,idx in POINT_LABELS.items()
                },
                "source_mu_numu_range_MeV":[
                    min(float(x["mu_numu_MeV"]) for x in csv.DictReader(profile_path.open())),
                    max(float(x["mu_numu_MeV"]) for x in csv.DictReader(profile_path.open())),
                ],
                "closure":result["internal_closure"],
            }

    baseline=scenarios["scale_1"]
    comparisons={}
    for name,scenario in scenarios.items():
        if name=="scale_1":
            continue
        comparisons[name]={}
        for label,point in scenario["points"].items():
            base=baseline["points"][label]
            comparisons[name][label]={
                "L_thin_ratio_vs_baseline":point["L_thin_erg_s"]/base["L_thin_erg_s"],
                "P_escape_ratio_vs_baseline":point["P_escape_calculated"]/base["P_escape_calculated"],
                "L_escaped_ratio_vs_baseline":point["L_escaped_erg_s"]/base["L_escaped_erg_s"],
                "required_over_calculated_escape":point["required_over_calculated_escape"],
            }
    return {
        "title":"B.16 10 MeV sensitivity to the reconstructed muon-neutrino chemical potential",
        "mass_MeV":mass,
        "scope":[
            "Scales only the digitized mu_numu(r); T, mu_mu, lapse, geometry, quadrature, and Fig. 7 reference remain unchanged.",
            "Each scenario is recomputed self-consistently in both B.1 source and B.2 opacity.",
            "The 0 and +/-10% cases are stress tests, not statistical uncertainty intervals.",
            "The fixed-omega B.2 prescription is used throughout.",
            "No coupling or opacity rescaling is introduced.",
        ],
        "profile_sha256":sha256(profile_path),
        "fig7_reference_sha256":sha256(fig7_path),
        "configuration":{"radial_order":nr,"energy_order":ne,"angular_order":na,"path_order":ns,"radius_km":radius,"energy_offset_MeV":energy_offset},
        "scenarios":scenarios,
        "comparisons_to_baseline":comparisons,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    p.add_argument("--fig7",type=Path,default=DEFAULT_FIG7)
    p.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    p.add_argument("--mass",type=float,default=10.0)
    p.add_argument("--nr",type=int,default=40)
    p.add_argument("--ne",type=int,default=100)
    p.add_argument("--na",type=int,default=16)
    p.add_argument("--ns",type=int,default=32)
    p.add_argument("--radius",type=float,default=25.0)
    p.add_argument("--energy-offset",type=float,default=1000.0)
    a=p.parse_args()
    d=run(a.profile,a.fig7,a.mass,a.nr,a.ne,a.na,a.ns,a.radius,a.energy_offset)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"scenarios":d["scenarios"],"comparisons":d["comparisons_to_baseline"]},indent=2))
    print(f"Saved {a.output}")


if __name__=="__main__":
    main()
