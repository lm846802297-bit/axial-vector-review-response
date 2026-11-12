"""Resolve B.2 optical depth and escape by emission direction for 8--15 km sources.

The inner path opacity is computed with the existing channel-resolved B.2
integrator. The 22--25 km outer shell is replaced by the high-resolution
0.05 km-profile radial-coordinate integral audited in the outer-profile step.
The B.1 source is held fixed. No normalization or opacity rescaling is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

try:
    from .reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates
    from .audit_b16_global_redshift import eq_b1_source_measure
    from .audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel
    from .audit_b16_outer_profile_inputs import radial_shell_columns
except ImportError:
    from reference import DEFAULT_PROFILE, radial_rule, load_profile, local_rates
    from audit_b16_global_redshift import eq_b1_source_measure
    from audit_b16_shell_luminosity_sensitivity import shell_columns_by_channel
    from audit_b16_outer_profile_inputs import radial_shell_columns

HERE=Path(__file__).resolve().parent
DEFAULT_OUTPUT=HERE/"outputs"/"b16_directional_escape_8_15km_10mev_2026-11-08.json"
SHELLS=((8.0,10.0),(10.0,12.0),(12.0,15.0))
ANGLE_BINS=((-1.0,-0.5),(-0.5,0.0),(0.0,0.5),(0.5,1.0))
COUPLINGS={
    "fig7_peak":1.1341108687336194e-8,
    "strong_endpoint":4.171689650228597e-8,
}


def sha256(path:Path)->str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def weighted_quantile(values,weights,q):
    values=np.asarray(values,float).ravel()
    weights=np.asarray(weights,float).ravel()
    valid=np.isfinite(values)&np.isfinite(weights)&(weights>0.0)
    if not np.any(valid):
        return None
    values,weights=values[valid],weights[valid]
    order=np.argsort(values)
    values,weights=values[order],weights[order]
    cumulative=np.cumsum(weights)
    idx=min(int(np.searchsorted(cumulative,q*cumulative[-1])),len(values)-1)
    return float(values[idx])


def weighted_mean(values,weights):
    return float(np.sum(np.asarray(values)*np.asarray(weights))/np.sum(weights))


def run(
    profile_path=DEFAULT_PROFILE,mass=10.0,radial_order=40,
    energy_order=100,energy_offset=1000.0,angular_order=64,path_order=64,
    outer_radial_order=96,
):
    radius,radial_weights=radial_rule(25.0,radial_order)
    radial_grid=np.unique(np.r_[0.0,radius,25.0])
    profile=load_profile(profile_path,radial_grid)
    energies=mass+np.geomspace(
        max(mass*1.0e-6,1.0e-6),energy_offset,energy_order
    )
    energies=np.unique(np.r_[energies,mass/profile["lapse"]])
    energies=energies[energies>mass*(1.0+1.0e-10)]
    energies.sort()

    rates=local_rates(
        mass,energies[None,:],profile["T"][:,None],
        profile["mu_numu"][:,None],profile["mu_mu"][:,None]
    )
    source_indices=np.searchsorted(radial_grid,radius)
    source,source_meta=eq_b1_source_measure(
        radius,radial_weights,energies,profile["lapse"][source_indices],
        mass,rates["production"][source_indices]
    )

    shell_data=shell_columns_by_channel(
        radius,radial_grid,profile["T"],rates,mass,energies,
        25.0,angular_order,path_order
    )
    angles,angle_weights=leggauss(angular_order)
    angle_weights=angle_weights/2.0

    source_mask=(radius>=8.0)&(radius<=15.0)
    selected_r=radius[source_mask]
    selected_source=source[source_mask]

    # Preserve the inner-shell B.2 columns and replace only the outer shell
    # with the high-resolution 22--25 km radial-coordinate integration.
    all_shell_columns=np.asarray(shell_data["columns_by_shell"],float)
    inner_columns=np.sum(all_shell_columns[:-1],axis=0)[source_mask]
    coarse_outer=all_shell_columns[-1,source_mask]
    raw=np.genfromtxt(profile_path,delimiter=",",names=True)
    outer_mask=(raw["r_km"]>=22.0)&(raw["r_km"]<=25.0)
    outer_r=np.asarray(raw["r_km"][outer_mask],float)
    outer_rates=local_rates(
        mass,energies[None,:],
        np.asarray(raw["T_MeV"][outer_mask],float)[:,None],
        np.asarray(raw["mu_numu_MeV"][outer_mask],float)[:,None],
        np.asarray(raw["mu_mu_MeV"][outer_mask],float)[:,None]
    )
    outer_columns,outer_angles,outer_weights=radial_shell_columns(
        selected_r,energies,outer_r,outer_rates["reduced_absorption"],
        mass,angular_order,outer_radial_order
    )
    if not np.allclose(angles,outer_angles,rtol=0.0,atol=2e-15):
        raise AssertionError("Outer-shell and full-path angle grids do not match")
    total_columns=inner_columns+outer_columns

    source_angle_weights=selected_source[:,None,:]*angle_weights[None,:,None]
    total_weight=float(np.sum(source_angle_weights))
    if total_weight<=0.0:
        raise ValueError("Selected 8--15 km B.1 source weight is zero")

    # The outer-shell path length depends on impact parameter b=r sin(theta),
    # hence is invariant under cos(theta)->-cos(theta). Verify this numerically.
    outer_symmetry=float(np.max(
        np.abs(outer_columns-outer_columns[:,::-1,:])
        /np.maximum(outer_columns,1.0e-300)
    ))

    by_shell={}
    for lo,hi in SHELLS:
        mask=(selected_r>=lo)&(selected_r<hi if hi<15.0 else selected_r<=hi)
        w=source_angle_weights[mask]
        by_shell[f"{lo:g}-{hi:g}km"]={
            "source_fraction_within_8_15km":float(np.sum(selected_source[mask])/np.sum(selected_source)),
            "source_weighted_mean_tau_outer_per_g2":weighted_mean(outer_columns[mask],w),
            "source_weighted_mean_tau_inner_per_g2":weighted_mean(inner_columns[mask],w),
            "source_weighted_mean_tau_total_per_g2":weighted_mean(total_columns[mask],w),
        }

    results={}
    for label,g in COUPLINGS.items():
        tau_outer=g*g*outer_columns
        tau_inner=g*g*inner_columns
        tau_total=g*g*total_columns
        escape=np.exp(-tau_total)
        p_full=float(np.sum(source_angle_weights*escape)/total_weight)
        p_outer=float(np.sum(source_angle_weights*np.exp(-tau_outer))/total_weight)
        p_inner=float(np.sum(source_angle_weights*np.exp(-tau_inner))/total_weight)
        escaped_weights=source_angle_weights*escape
        angle_rows=[]
        for lo,hi in ANGLE_BINS:
            mask=(angles>=lo)&(angles<hi if hi<1.0 else angles<=hi)
            w=source_angle_weights[:,mask,:]
            escaped=escaped_weights[:,mask,:]
            angle_rows.append({
                "cos_theta_bin":[lo,hi],
                "thin_source_fraction":float(np.sum(w)/total_weight),
                "escaped_luminosity_fraction":float(np.sum(escaped)/np.sum(escaped_weights)),
                "mean_escape_probability":float(np.sum(escaped)/np.sum(w)),
                "source_weighted_mean_tau_outer":weighted_mean(tau_outer[:,mask,:],w),
                "source_weighted_mean_tau_inner":weighted_mean(tau_inner[:,mask,:],w),
                "source_weighted_mean_tau_total":weighted_mean(tau_total[:,mask,:],w),
            })

        emission_rows=[]
        for shell_name,(lo,hi) in zip(by_shell.keys(),SHELLS):
            mask=(selected_r>=lo)&(selected_r<hi if hi<15.0 else selected_r<=hi)
            w=source_angle_weights[mask]
            emission_rows.append({
                "emission_shell":shell_name,
                "thin_source_fraction_within_8_15km":float(np.sum(selected_source[mask])/np.sum(selected_source)),
                "mean_escape_probability":float(np.sum(w*escape[mask])/np.sum(w)),
                "escaped_luminosity_fraction_within_8_15km":float(np.sum(w*escape[mask])/np.sum(escaped_weights)),
                "mean_tau_outer":weighted_mean(tau_outer[mask],w),
                "mean_tau_inner":weighted_mean(tau_inner[mask],w),
                "mean_tau_total":weighted_mean(tau_total[mask],w),
            })

        # Directional distribution of the escaping source, including both
        # source radius and energy weights.
        results[label]={
            "g":g,
            "source_weighted_escape_probability_8_15km":p_full,
            "outer_shell_only_escape_factor_8_15km":p_outer,
            "inner_path_only_escape_factor_8_15km":p_inner,
            "tau_total_quantiles_source_weighted":{
                "p10":weighted_quantile(tau_total,source_angle_weights,0.10),
                "p50":weighted_quantile(tau_total,source_angle_weights,0.50),
                "p90":weighted_quantile(tau_total,source_angle_weights,0.90),
            },
            "tau_outer_quantiles_source_weighted":{
                "p10":weighted_quantile(tau_outer,source_angle_weights,0.10),
                "p50":weighted_quantile(tau_outer,source_angle_weights,0.50),
                "p90":weighted_quantile(tau_outer,source_angle_weights,0.90),
            },
            "tau_total_quantiles_escaping_population":{
                "p10":weighted_quantile(tau_total,escaped_weights,0.10),
                "p50":weighted_quantile(tau_total,escaped_weights,0.50),
                "p90":weighted_quantile(tau_total,escaped_weights,0.90),
            },
            "direction_bins":angle_rows,
            "emission_shells":emission_rows,
        }

    return {
        "title":"B.2 direction-resolved escape probability for 8--15 km sources",
        "mass_MeV":mass,
        "profile":{"path":str(profile_path),"sha256":sha256(profile_path)},
        "configuration":{
            "radial_order":radial_order,
            "energy_order":energy_order,
            "angular_order":angular_order,
            "full_path_order":path_order,
            "outer_shell_radial_order":outer_radial_order,
            "fixed_omega":True,
            "outer_shell_high_resolution_profile_nodes":int(len(outer_r)),
        },
        "source_fraction_8_15km_of_total_B1_source":float(np.sum(selected_source)/np.sum(source)),
        "source_weighted_mean_tau_outer_per_g2":weighted_mean(outer_columns,source_angle_weights),
        "source_weighted_mean_tau_inner_per_g2":weighted_mean(inner_columns,source_angle_weights),
        "source_weighted_mean_tau_total_per_g2":weighted_mean(total_columns,source_angle_weights),
        "outer_shell_cos_theta_symmetry_max_relative_residual":outer_symmetry,
        "emission_shell_baseline_summary":by_shell,
        "coupling_results":results,
        "interpretation":{
            "outer_shell": "For sources at r<=15 km, the 22--25 km shell path length depends on impact parameter and is symmetric under cos(theta)->-cos(theta).",
            "inner_path": "The inner optical depth need not be symmetric under cos(theta)->-cos(theta); backward-emitted vectors traverse more of the dense core.",
            "weighting": "The escaping-population direction fractions include the B.1 source spectrum and the full exp(-g^2 tau) survival factor.",
            "scope": "The B.1 source is held fixed. This is a directional transport diagnostic, not a new SN profile or a fitted correction.",
        },
        "eq_b1_source_measure":source_meta,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    p.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    p.add_argument("--mass",type=float,default=10.0)
    p.add_argument("--nr",type=int,default=40)
    p.add_argument("--ne",type=int,default=100)
    p.add_argument("--energy-offset",type=float,default=1000.0)
    p.add_argument("--angular-order",type=int,default=64)
    p.add_argument("--path-order",type=int,default=64)
    p.add_argument("--outer-radial-order",type=int,default=96)
    a=p.parse_args()
    d=run(a.profile,a.mass,a.nr,a.ne,a.energy_offset,a.angular_order,a.path_order,a.outer_radial_order)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print(json.dumps({
        "source_fraction_8_15km_of_total_B1_source":d["source_fraction_8_15km_of_total_B1_source"],
        "source_weighted_mean_tau_outer_per_g2":d["source_weighted_mean_tau_outer_per_g2"],
        "source_weighted_mean_tau_inner_per_g2":d["source_weighted_mean_tau_inner_per_g2"],
        "source_weighted_mean_tau_total_per_g2":d["source_weighted_mean_tau_total_per_g2"],
        "outer_shell_cos_theta_symmetry_max_relative_residual":d["outer_shell_cos_theta_symmetry_max_relative_residual"],
        "coupling_results":d["coupling_results"],
    },indent=2))
    print(f"Saved {a.output}")


if __name__=="__main__":
    main()
