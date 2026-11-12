"""Angular and emission-radius resolved 22--25 km opacity for 10 MeV vectors.

The B.1 source is held fixed. Local rates are evaluated on the archived 0.05 km
figure-reconstructed radial profile. The outer-shell optical depth is integrated
in r with ds/dr=r/sqrt(r^2-b^2), avoiding a discontinuous path-coordinate mask.
The inner path opacity is summed from the same fixed-omega B.2 shell integrator.

This is a diagnostic on the reconstructed public-figure profile, not a new SN
model and not a replacement for the raw Garching snapshot.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .reference import DEFAULT_PROFILE, local_rates, radial_rule, KM_TO_MEV_INV
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_outer_profile_inputs import radial_shell_columns
    from .audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel
except ImportError:
    from reference import DEFAULT_PROFILE, local_rates, radial_rule, KM_TO_MEV_INV
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_outer_profile_inputs import radial_shell_columns
    from audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
DEFAULT_FIG7=ROOT/"outputs"/"vector_audit"/"luminosity_comparison.json"
DEFAULT_OUTPUT=HERE/"outputs"/"b16_outer_escape_angular_distribution_10mev_2026-11-08.json"
SHELL_EDGES=(0.,5.,8.,10.,12.,15.,16.5,18.5,20.,22.,25.)
EMISSION_BINS=((8.,10.),(10.,12.),(12.,15.))
DIRECTION_BINS={
    "inward_radial":(-1.0,-0.8),
    "inward_oblique":(-0.8,-0.2),
    "tangential":(-0.2,0.2),
    "outward_oblique":(0.2,0.8),
    "outward_radial":(0.8,1.0),
}
COUPLINGS={
    "fig7_peak":1.1341108687336194e-8,
    "strong_endpoint":4.171689650228597e-8,
}

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def weighted_quantile(values,weights,q):
    values=np.asarray(values,float).ravel()
    weights=np.asarray(weights,float).ravel()
    valid=np.isfinite(values)&np.isfinite(weights)&(weights>0)
    if not np.any(valid):
        return None
    v,w=values[valid],weights[valid]
    order=np.argsort(v)
    v,w=v[order],w[order]
    c=np.cumsum(w)
    return float(v[min(int(np.searchsorted(c,q*c[-1])),len(v)-1)])

def summarize_distribution(values,weights):
    values=np.asarray(values,float)
    weights=np.asarray(weights,float)
    norm=float(np.sum(weights))
    if norm<=0:
        return {"weight":0.0,"mean":None,"q50":None,"q90":None,"q99":None,"maximum":None}
    return {
        "weight":norm,
        "mean":float(np.sum(values*weights)/norm),
        "q50":weighted_quantile(values,weights,.50),
        "q90":weighted_quantile(values,weights,.90),
        "q99":weighted_quantile(values,weights,.99),
        "maximum":float(np.max(values[weights>0])),
    }

def escape_probability(columns,weights,g):
    den=float(np.sum(weights))
    return float(np.sum(weights*np.exp(-g*g*columns))/den) if den else 0.0

def run(profile_path=DEFAULT_PROFILE,fig7_path=DEFAULT_FIG7,mass=10.0,
        radial_order=40,energy_order=100,angular_order=64,path_order=64,
        outer_radial_order=96,energy_offset=1000.0):
    raw=np.genfromtxt(profile_path,delimiter=",",names=True)
    radial_grid=np.asarray(raw["r_km"],float)
    if not np.isclose(radial_grid[0],0.) or not np.isclose(radial_grid[-1],25.):
        raise ValueError("Profile must cover 0--25 km")
    temp=np.asarray(raw["T_MeV"],float)
    mu_numu=np.asarray(raw["mu_numu_MeV"],float)
    mu_mu=np.asarray(raw["mu_mu_MeV"],float)
    lapse=np.asarray(raw["lapse"],float)

    source_r,source_rw=radial_rule(25.0,radial_order)
    energies=mass+np.geomspace(max(mass*1e-6,1e-6),energy_offset,energy_order)
    energies=np.unique(np.r_[energies,mass/np.interp(source_r,radial_grid,lapse)])
    energies=energies[energies>mass*(1+1e-10)]
    energies.sort()

    rates=local_rates(mass,energies[None,:],temp[:,None],mu_numu[:,None],mu_mu[:,None])
    src_idx=np.searchsorted(radial_grid,source_r)
    source,source_meta=eq_b1_source_measure(
        source_r,source_rw,energies,lapse[src_idx],mass,rates["production"][src_idx]
    )
    emask=(source_r>=8.0)&(source_r<=15.0)
    rsel=source_r[emask]
    ssel=source[emask]
    if len(rsel)==0:
        raise ValueError("No source quadrature nodes in 8--15 km")

    # Evaluate full path opacity on the dense 0.05 km profile grid.
    dense_shell=shell_columns_by_channel(
        rsel,radial_grid,temp,rates,mass,energies,25.0,angular_order,path_order
    )
    shell_columns=np.asarray(dense_shell["columns_by_shell"],float)
    angle_weights=np.asarray(dense_shell["angle_weights"],float)
    angles,_=leggauss(angular_order)
    angles=np.asarray(angles,float)

    # Reintegrate 22--25 km directly in radial coordinate for each impact parameter.
    dense_reduced=np.asarray(rates["reduced_absorption"],float)
    outer_columns,outer_angles,outer_weights=radial_shell_columns(
        rsel,energies,radial_grid,dense_reduced,mass,
        angular_order,outer_radial_order,22.0,25.0
    )
    if not np.allclose(angles,outer_angles,rtol=0,atol=1e-14):
        raise AssertionError("Angular quadratures differ")
    # Last shell in shell_columns is 22--25 km; replace its path-mask estimate
    # by the direct radial-coordinate integral.
    inner_columns=np.sum(shell_columns[:-1],axis=0)
    total_columns=inner_columns+outer_columns
    source_weights=ssel[:,None,:]*angle_weights[None,:,None]
    full_den=float(np.sum(source_weights))
    if full_den<=0:
        raise ValueError("Selected B.1 source has zero weight")

    # Geometric impact parameter and path length through the outer shell.
    b=rsel[:,None]*np.sqrt(np.maximum(1.0-angles[None,:]**2,0.0))
    outer_length=np.sqrt(25.0**2-b*b)-np.sqrt(22.0**2-b*b)
    source_shells={}
    for lo,hi in EMISSION_BINS:
        m=(rsel>=lo)&(rsel<hi if hi<15.0 else rsel<=hi)
        source_shells[f"{lo:g}-{hi:g} km"]={
            "source_fraction_within_8_15km":float(np.sum(ssel[m])/np.sum(ssel))
        }

    results={}
    for tag,g in COUPLINGS.items():
        tau_outer=g*g*outer_columns
        tau_inner=g*g*inner_columns
        tau_total=tau_outer+tau_inner
        escaped_weight=source_weights*np.exp(-tau_total)
        outer_escaped_weight=source_weights*np.exp(-tau_outer)
        by_emission={}
        for lo,hi in EMISSION_BINS:
            m=(rsel>=lo)&(rsel<hi if hi<15.0 else rsel<=hi)
            w=source_weights[m]
            by_emission[f"{lo:g}-{hi:g} km"]={
                "source_fraction_within_8_15km":float(np.sum(ssel[m])/np.sum(ssel)),
                "outer_tau_unattenuated_source_weight":summarize_distribution(tau_outer[m],w),
                "outer_tau_conditioned_on_full_escape":summarize_distribution(tau_outer[m],escaped_weight[m]),
                "full_tau_unattenuated_source_weight":summarize_distribution(tau_total[m],w),
                "outer_shell_escape_probability":escape_probability(outer_columns[m],w,g),
                "full_path_escape_probability":escape_probability(total_columns[m],w,g),
            }

        by_direction={}
        for label,(lo,hi) in DIRECTION_BINS.items():
            am=(angles>=lo)&(angles<(hi if hi<1 else hi+1e-12))
            w=source_weights[:,am,:]
            by_direction[label]={
                "cos_theta_range":[lo,hi],
                "outer_tau_unattenuated_source_weight":summarize_distribution(tau_outer[:,am,:],w),
                "outer_tau_conditioned_on_full_escape":summarize_distribution(tau_outer[:,am,:],escaped_weight[:,am,:]),
                "full_tau_unattenuated_source_weight":summarize_distribution(tau_total[:,am,:],w),
                "outer_shell_escape_probability":escape_probability(outer_columns[:,am,:],w,g),
                "full_path_escape_probability":escape_probability(total_columns[:,am,:],w,g),
                "source_weight_fraction":float(np.sum(w)/full_den),
            }

        # Combined emission-shell x direction bins.
        joint={}
        for lo,hi in EMISSION_BINS:
            rm=(rsel>=lo)&(rsel<hi if hi<15.0 else rsel<=hi)
            joint[f"{lo:g}-{hi:g} km"]={}
            for label,(alo,ahi) in DIRECTION_BINS.items():
                am=(angles>=alo)&(angles<(ahi if ahi<1 else ahi+1e-12))
                w=source_weights[rm][:,am,:]
                joint[f"{lo:g}-{hi:g} km"][label]={
                    "source_weight_fraction":float(np.sum(w)/full_den),
                    "outer_tau_q50_q90_q99":[
                        weighted_quantile(tau_outer[rm][:,am,:],w,q)
                        for q in (.5,.9,.99)
                    ],
                    "outer_tau_escape_probability":escape_probability(outer_columns[rm][:,am,:],w,g),
                    "full_escape_probability":escape_probability(total_columns[rm][:,am,:],w,g),
                }

        results[tag]={
            "g":g,
            "selected_8_15km_source_fraction_of_global_B1":float(np.sum(ssel)/np.sum(source)),
            "outer_shell_escape_probability_8_15km":escape_probability(outer_columns,source_weights,g),
            "full_path_escape_probability_8_15km":escape_probability(total_columns,source_weights,g),
            "outer_tau_unattenuated_source_weight":summarize_distribution(tau_outer,source_weights),
            "outer_tau_conditioned_on_full_escape":summarize_distribution(tau_outer,escaped_weight),
            "full_tau_unattenuated_source_weight":summarize_distribution(tau_total,source_weights),
            "emission_shells":by_emission,
            "directions":by_direction,
            "emission_shell_direction_joint":joint,
        }

    return {
        "title":"B.16 outer-shell optical depth resolved by emission radius and direction",
        "mass_MeV":mass,
        "scope":[
            "B.1 source is held fixed and restricted to emission radii 8--15 km.",
            "The full fixed-omega B.2 opacity is evaluated on the 0.05 km reconstructed profile.",
            "The 22--25 km shell is independently integrated in r using ds/dr=r/sqrt(r^2-b^2).",
            "The final shell's path-mask quadrature is replaced by the direct radial-coordinate result.",
            "The profile is reconstructed from public figures, not the original raw Garching snapshot.",
            "No rescaling or axial-current substitution is applied.",
        ],
        "profile":{"path":str(profile_path),"sha256":sha256(profile_path),"radial_nodes":len(radial_grid)},
        "fig7_reference":{"path":str(fig7_path),"sha256":sha256(fig7_path)},
        "configuration":{
            "radial_source_order":radial_order,"energy_order":len(energies),
            "angular_order":angular_order,"inner_path_order":path_order,
            "outer_radial_order":outer_radial_order,"Rmax_km":25.0,
            "outer_shell_km":[22.0,25.0],
            "direction_bins":DIRECTION_BINS,
        },
        "source_measure":source_meta,
        "selected_source":{
            "radius_range_km":[float(np.min(rsel)),float(np.max(rsel))],
            "source_fraction_within_8_15km_by_shell":source_shells,
            "global_source_fraction_8_15km":float(np.sum(ssel)/np.sum(source)),
        },
        "geometry":{
            "impact_parameter_range_km":[float(np.min(b)),float(np.max(b))],
            "outer_shell_path_length_range_km":[float(np.min(outer_length)),float(np.max(outer_length))],
            "outer_shell_path_length_formula":"sqrt(25^2-b^2)-sqrt(22^2-b^2)",
        },
        "closure":{
            "inner_plus_outer_shape_matches":bool(total_columns.shape==outer_columns.shape),
            "angular_weights_sum":float(np.sum(angle_weights)),
            "angular_weights_match_direct_radial_integral":bool(np.allclose(angle_weights,outer_weights,rtol=0,atol=1e-14)),
            "minimum_outer_column":float(np.min(outer_columns)),
            "minimum_total_column":float(np.min(total_columns)),
            "negative_columns":int(np.count_nonzero(total_columns<0)),
        },
        "couplings":results,
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    p.add_argument("--fig7",type=Path,default=DEFAULT_FIG7)
    p.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    p.add_argument("--mass",type=float,default=10.0)
    p.add_argument("--nr",type=int,default=40)
    p.add_argument("--ne",type=int,default=100)
    p.add_argument("--na",type=int,default=64)
    p.add_argument("--ns",type=int,default=64)
    p.add_argument("--outer-radial-order",type=int,default=96)
    p.add_argument("--energy-offset",type=float,default=1000.0)
    a=p.parse_args()
    d=run(a.profile,a.fig7,a.mass,a.nr,a.ne,a.na,a.ns,a.outer_radial_order,a.energy_offset)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps({
        "source":d["selected_source"],"geometry":d["geometry"],"closure":d["closure"],
        "couplings":{k:{
            "outer_escape":v["outer_shell_escape_probability_8_15km"],
            "full_escape":v["full_path_escape_probability_8_15km"],
            "outer_tau":v["outer_tau_unattenuated_source_weight"],
            "outer_tau_given_escape":v["outer_tau_conditioned_on_full_escape"],
            "directions":v["directions"],
        } for k,v in d["couplings"].items()}
    },indent=2))
    print(f"Saved {a.output}")

if __name__=="__main__":
    main()
