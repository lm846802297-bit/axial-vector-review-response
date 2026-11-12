"""Audit outer-profile interpolation in the B.16 path-opacity integral.

Keep the B.1 source quadrature and source values fixed. Change only the radial
grid on which local rates are evaluated/interpolated along the outgoing path.
This tests whether the 40-node source quadrature grid is too coarse to serve
also as the path-opacity interpolation grid.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np

try:
    from .reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_shell_luminosity_sensitivity import (
        shell_columns_by_channel, log_escaped_integral
    )
except ImportError:
    from reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_shell_luminosity_sensitivity import (
        shell_columns_by_channel, log_escaped_integral
    )

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
DEFAULT_FIG7=ROOT/"outputs"/"vector_audit"/"luminosity_comparison.json"
DEFAULT_OUTPUT=HERE/"outputs"/"b16_outer_profile_interpolation_10mev_2026-11-08.json"
COUPLING_INDICES={"weak":0,"peak":17,"strong":24}

def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def calc(profile_path,fig7_path,mass=10.0,nr=40,ne=100,na=16,ns=32,radius=25.0,energy_offset=1000.0,steps=(0.5,0.25,0.1,0.05,0.025)):
    fig7=json.loads(Path(fig7_path).read_text())
    vertices=fig7["reference_vertices"][str(float(mass))]
    couplings=np.asarray(vertices["g"],float)
    ref_lum=np.asarray(vertices["luminosity_erg_s"],float)

    # Preserve the published/source-side quadrature and its local B.1 rates.
    r,rw=radial_rule(radius,nr)
    source_profile=load_profile(profile_path,r)
    energies=mass+np.geomspace(max(mass*1e-6,1e-6),energy_offset,ne)
    energies=np.unique(np.r_[energies,mass/source_profile["lapse"]])
    energies=energies[energies>mass*(1+1e-10)]
    energies.sort()
    source_rates=local_rates(
        mass,energies[None,:],source_profile["T"][:,None],
        source_profile["mu_numu"][:,None],source_profile["mu_mu"][:,None]
    )
    source,source_meta=eq_b1_source_measure(
        r,rw,energies,source_profile["lapse"],mass,source_rates["production"]
    )

    # The baseline path grid is exactly the source quadrature nodes plus endpoints.
    path_grids={"baseline_source_nodes":np.unique(np.r_[0.0,r,radius])}
    for dx in steps:
        n=int(round(radius/dx))
        path_grids[f"uniform_{radius/n:.5g}_km"]=np.linspace(0.0,radius,n+1)

    results={}
    for label,path_grid in path_grids.items():
        prof=load_profile(profile_path,path_grid)
        rates=local_rates(
            mass,energies[None,:],prof["T"][:,None],
            prof["mu_numu"][:,None],prof["mu_mu"][:,None]
        )
        shell=shell_columns_by_channel(
            r,path_grid,prof["T"],rates,mass,energies,radius,na,ns
        )
        cols=shell["columns_total"]
        points={}
        for tag,idx in COUPLING_INDICES.items():
            g=float(couplings[idx])
            logesc=log_escaped_integral(source,shell["angle_weights"],cols,g)
            logthin=np.log(np.sum(source))+2*np.log(g)
            loglum=logesc+2*np.log(g)
            points[tag]={
                "index":idx,"g":g,
                "luminosity_erg_s":float(np.exp(np.clip(loglum,-745,700))),
                "escape_fraction":float(np.exp(np.clip(logesc-np.log(np.sum(source)),-745,0))),
                "reference_luminosity_erg_s":float(ref_lum[idx]),
            }
        results[label]={
            "path_grid_nodes":len(path_grid),
            "maximum_path_grid_spacing_km":float(np.max(np.diff(path_grid))),
            "detailed_balance_channel_sum_relative_residual":shell["detailed_balance_channel_sum_relative_residual"],
            "shell_sum_to_direct_column_max_relative_residual":shell["shell_sum_to_direct_column_max_relative_residual"],
            "points":points,
        }

    base=results["baseline_source_nodes"]
    comparisons={}
    for label,current in results.items():
        comparisons[label]={
            tag:{
                "luminosity_relative_change_vs_baseline":v["luminosity_erg_s"]/base["points"][tag]["luminosity_erg_s"]-1.0,
                "escape_fraction_relative_change_vs_baseline":v["escape_fraction"]/base["points"][tag]["escape_fraction"]-1.0,
            } for tag,v in current["points"].items()
        }
    return {
        "title":"B.16 path-opacity interpolation grid audit at mV=10 MeV",
        "scope":[
            "B.1 source quadrature, source values, coupling points, energy grid, angular quadrature and path quadrature are held fixed.",
            "Only the radial grid used to evaluate local thermodynamic inputs/rates and interpolate rates along outgoing paths is refined.",
            "This is an interpolation-resolution diagnostic, not a change to the physical profile or outer radius.",
            "The profile remains a public-figure reconstruction, not the raw Garching simulation table.",
        ],
        "mass_MeV":mass,
        "source_quadrature":{"radial_order":nr,"energy_order":ne,"source_nodes":len(r),"source_measure":source_meta},
        "transport_quadrature":{"angular_order":na,"path_order":ns,"outer_radius_km":radius},
        "profile_sha256":sha256(profile_path),
        "fig7_reference_sha256":sha256(fig7_path),
        "path_grid_results":results,
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
    d=calc(a.profile,a.fig7,a.mass,a.nr,a.ne,a.na,a.ns,a.radius,a.energy_offset)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"grid_results":d["path_grid_results"],"comparisons":d["comparisons_to_baseline"]},indent=2))
    print(f"Saved {a.output}")

if __name__=="__main__":
    main()
