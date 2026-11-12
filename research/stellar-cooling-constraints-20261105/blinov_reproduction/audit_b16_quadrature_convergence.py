"""One-factor-at-a-time and combined quadrature convergence audit for B.16.

Uses the existing literal fixed-omega Appendix-B B.1/B.2 calculation.
No source, opacity, coupling, or luminosity rescaling is introduced.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

try:
    from .audit_b16_emission_radius_escape import run_audit, DEFAULT_PROFILE, DEFAULT_FIG7
except ImportError:
    from audit_b16_emission_radius_escape import run_audit, DEFAULT_PROFILE, DEFAULT_FIG7

HERE=Path(__file__).resolve().parent
DEFAULT_OUTPUT=HERE/"outputs"/"b16_quadrature_convergence_10mev_2026-11-08.json"

CONFIGS={
    "baseline_40_100_16_32":(40,100,16,32),
    "radial_60":(60,100,16,32),
    "energy_150":(40,150,16,32),
    "angular_24":(40,100,24,32),
    "path_48":(40,100,16,48),
    "combined_60_150_24_48":(60,150,24,48),
}

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def summarize(result):
    points=result["representative_couplings"]
    chosen={}
    for p in points:
        chosen[str(p["index"])]={
            "g":p["g"],
            "luminosity_erg_s":p["calculated_luminosity_erg_s"],
            "escape_fraction":p["global_escape_fraction"],
            "relative_difference_vs_fig7":p["relative_difference_vs_fig7"],
        }
    return {
        "configuration":result["configuration"],
        "internal_closure":result["internal_closure"],
        "source_distribution":{
            "mean_radius_km":result["optically_thin_source_radial_distribution"]["mean_emission_radius_km"],
            "median_radius_km":result["optically_thin_source_radial_distribution"]["median_emission_radius_km"],
            "p90_radius_km":result["optically_thin_source_radial_distribution"]["p90_emission_radius_km"],
            "shell_fractions":{x["shell"]:x["source_fraction"] for x in result["optically_thin_source_radial_distribution"]["shells"]},
        },
        "points":chosen,
    }

def run(profile_path=DEFAULT_PROFILE,fig7_path=DEFAULT_FIG7,mass=10.0,energy_offset=1000.0):
    results={}
    raw={}
    for name,(nr,ne,na,ns) in CONFIGS.items():
        result=run_audit(
            profile_path,fig7_path,mass,nr,ne,na,ns,25.0,energy_offset
        )
        raw[name]=result
        results[name]=summarize(result)

    baseline=results["baseline_40_100_16_32"]
    comparisons={}
    for name,current in results.items():
        if name== "baseline_40_100_16_32":
            continue
        point_comparison={}
        for idx,point in current["points"].items():
            base=baseline["points"][idx]
            point_comparison[idx]={
                "g":point["g"],
                "luminosity_relative_change_vs_baseline":point["luminosity_erg_s"]/base["luminosity_erg_s"]-1.0,
                "escape_fraction_absolute_change":point["escape_fraction"]-base["escape_fraction"],
            }
        comparisons[name]={
            "source_mean_radius_relative_change":current["source_distribution"]["mean_radius_km"]/baseline["source_distribution"]["mean_radius_km"]-1.0,
            "source_median_radius_absolute_change_km":current["source_distribution"]["median_radius_km"]-baseline["source_distribution"]["median_radius_km"],
            "source_p90_radius_absolute_change_km":current["source_distribution"]["p90_radius_km"]-baseline["source_distribution"]["p90_radius_km"],
            "points":point_comparison,
            "max_abs_luminosity_relative_change_at_representative_points":max(abs(x["luminosity_relative_change_vs_baseline"]) for x in point_comparison.values()),
        }
    return {
        "title":"B.16 fixed-omega quadrature convergence at mV=10 MeV",
        "scope":[
            "Literal Appendix-B fixed-omega B.1/B.2 prescription.",
            "One-factor-at-a-time radial, energy, angular, and path quadrature tests plus a combined higher-order test.",
            "All calculations use the same digitized SFHo-18.8 profile and Fig. 7 digitization.",
            "No normalization or curve fitting.",
        ],
        "mass_MeV":mass,
        "energy_offset_MeV":energy_offset,
        "profile_sha256":sha256(profile_path),
        "fig7_reference_sha256":sha256(fig7_path),
        "configurations":results,
        "comparisons_to_baseline":comparisons,
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    p.add_argument("--fig7",type=Path,default=DEFAULT_FIG7)
    p.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    p.add_argument("--mass",type=float,default=10.0)
    p.add_argument("--energy-offset",type=float,default=1000.0)
    a=p.parse_args()
    d=run(a.profile,a.fig7,a.mass,a.energy_offset)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"configurations":{k:{"quadrature":v["configuration"],"closure":v["internal_closure"],"source":v["source_distribution"]} for k,v in d["configurations"].items()},"comparisons":d["comparisons_to_baseline"]},indent=2))
    print(f"Saved {a.output}")

if __name__=="__main__":
    main()
