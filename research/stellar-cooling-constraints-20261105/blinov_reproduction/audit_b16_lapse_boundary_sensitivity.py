"""Quantify the B.1 source sensitivity to the lapse continuation from 24 to 25 km.

The baseline is the digitized Ferreira lapse through 23.9998 km with the
matched Schwarzschild exterior continuation already stored in the profile.
Two deliberately simple alternatives (freeze at N(24), linear extrapolation
of the 23--24 km slope) bracket the effect of this short continuation interval.
All thermodynamic profiles, source quadrature, rates, energies and B.2 opacity
columns are held fixed. These alternatives are diagnostics, not replacements
for the published metric.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
import numpy as np

try:
    from .reference import DEFAULT_PROFILE,radial_rule,load_profile,local_rates
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel,log_escaped_integral
except ImportError:
    from reference import DEFAULT_PROFILE,radial_rule,load_profile,local_rates
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel,log_escaped_integral

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
DEFAULT_FIG7=ROOT/"outputs"/"vector_audit"/"luminosity_comparison.json"
DEFAULT_OUTPUT=HERE/"outputs"/"b16_lapse_boundary_sensitivity_10mev_2026-11-08.json"

def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def fractions(r,source):
    w=np.sum(source,axis=1)
    total=float(np.sum(w))
    return {
        "r_ge_22km":float(np.sum(w[r>=22.0])/total),
        "r_ge_24km":float(np.sum(w[r>=24.0])/total),
        "r_22_to_25km":float(np.sum(w[(r>=22.0)&(r<=25.0)])/total),
        "r_24_to_25km":float(np.sum(w[r>=24.0])/total),
    }

def run(profile_path=DEFAULT_PROFILE,fig7_path=DEFAULT_FIG7,mass=10.0,nr=40,ne=100,na=16,ns=32,energy_offset=1000.0):
    raw=np.genfromtxt(profile_path,delimiter=",",names=True)
    r,rw=radial_rule(25.0,nr)
    p=load_profile(profile_path,r)
    energies=mass+np.geomspace(max(mass*1e-6,1e-6),energy_offset,ne)
    energies=np.unique(np.r_[energies,mass/p["lapse"]])
    energies=energies[energies>mass*(1+1e-10)]
    energies.sort()
    rates=local_rates(mass,energies[None,:],p["T"][:,None],p["mu_numu"][:,None],p["mu_mu"][:,None])
    n23=float(np.interp(23.0,raw["r_km"],raw["lapse"]))
    n24=float(np.interp(24.0,raw["r_km"],raw["lapse"]))
    n25=float(np.interp(25.0,raw["r_km"],raw["lapse"]))
    base=np.asarray(p["lapse"],float)
    variants={
        "matched_schwarzschild_baseline":base,
        "freeze_at_N24":np.where(r>24.0,n24,base),
        "linear_extrapolation_of_23_24_slope":np.where(r>24.0,n24+(n24-n23)*(r-24.0),base),
    }
    # Opacity is lapse-independent in the literal fixed-omega B.2 prescription.
    # Compute it once and use the same columns for all source-weight variants.
    shell=shell_columns_by_channel(r,np.unique(np.r_[0.0,r,25.0]),p["T"],rates,mass,energies,25.0,na,ns)
    fig7=json.loads(Path(fig7_path).read_text())
    vertices=fig7["reference_vertices"][str(float(mass))]
    gvals=np.asarray(vertices["g"],float)
    indices={"weak":0,"peak":17,"strong":24}
    results={}
    for name,lapse in variants.items():
        source,meta=eq_b1_source_measure(r,rw,energies,lapse,mass,rates["production"])
        points={}
        for tag,idx in indices.items():
            g=float(gvals[idx])
            logesc=log_escaped_integral(source,shell["angle_weights"],shell["columns_total"],g)
            logthin=np.log(np.sum(source))
            points[tag]={
                "g":g,
                "escape_fraction":float(np.exp(np.clip(logesc-logthin,-745.0,0.0))),
                "thin_source_luminosity_relative_to_baseline":None,
            }
        results[name]={
            "total_B1_source_measure":float(np.sum(source)),
            "source_fractions":fractions(r,source),
            "points":points,
            "source_meta":meta,
        }
    baseline=results["matched_schwarzschild_baseline"]
    for name,v in results.items():
        v["relative_total_B1_source_change_vs_baseline"]=v["total_B1_source_measure"]/baseline["total_B1_source_measure"]-1.0
        for tag in indices:
            v["points"][tag]["thin_source_luminosity_relative_to_baseline"]=v["total_B1_source_measure"]/baseline["total_B1_source_measure"]-1.0
            v["points"][tag]["escape_fraction_relative_change_vs_baseline"]=v["points"][tag]["escape_fraction"]/baseline["points"][tag]["escape_fraction"]-1.0
    return {
        "title":"B.16 lapse-boundary sensitivity at mV=10 MeV",
        "scope":[
            "Only the 24--25 km lapse continuation is varied.",
            "Temperature, muon and neutrino chemical potentials, source quadrature, energy grid, and local production rates are unchanged.",
            "The fixed-omega B.2 opacity is lapse-independent along the path; the same opacity columns are used for every variant.",
            "Freeze and linear continuations are diagnostic brackets, not physical alternatives to the matched exterior solution.",
        ],
        "mass_MeV":mass,
        "profile_sha256":sha256(profile_path),
        "fig7_reference_sha256":sha256(fig7_path),
        "lapse_nodes":{"N23":n23,"N24":n24,"N25_baseline":n25,"matched_Schwarzschild_radius_km":24.0*(1.0-n24*n24)},
        "quadrature":{"radial_order":nr,"energy_order":ne,"angular_order":na,"path_order":ns},
        "variants":results,
    }

def main():
    q=argparse.ArgumentParser(description=__doc__)
    q.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    q.add_argument("--fig7",type=Path,default=DEFAULT_FIG7)
    q.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    q.add_argument("--mass",type=float,default=10.0)
    q.add_argument("--nr",type=int,default=40)
    q.add_argument("--ne",type=int,default=100)
    q.add_argument("--na",type=int,default=16)
    q.add_argument("--ns",type=int,default=32)
    q.add_argument("--energy-offset",type=float,default=1000.0)
    a=q.parse_args()
    d=run(a.profile,a.fig7,a.mass,a.nr,a.ne,a.na,a.ns,a.energy_offset)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"lapse_nodes":d["lapse_nodes"],"variants":{k:{"relative_total_B1_source_change_vs_baseline":v["relative_total_B1_source_change_vs_baseline"],"source_fractions":v["source_fractions"],"points":v["points"]} for k,v in d["variants"].items()}},indent=2))
    print(f"Saved {a.output}")

if __name__=="__main__":
    main()
