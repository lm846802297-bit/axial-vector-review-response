#!/usr/bin/env python3
"""High-order direct B.13 checks for selected worst Global-03 2D cells."""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
ORDERS=((16,10,10,10),(20,12,12,12),(24,14,14,14),(28,16,16,16),(32,18,18,18))
TOL=1e-3
MASS=10.0

def load_audit():
    if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
    if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as a
    table=np.genfromtxt(PROFILE,delimiter=",",names=True)
    radii=np.asarray(table["r_km"],float)
    def fast_load_profile(path,rr):
        rr=np.asarray(rr,float)
        return {name:np.interp(rr,radii,np.asarray(table[col],float)) for name,col in
                {"T":"T_MeV","mu_mu":"mu_mu_MeV","mu_numu":"mu_numu_MeV","lapse":"lapse"}.items()}
    a.load_profile=fast_load_profile
    return a,table,radii

def evaluate_high_order(a,profile,radii,table,r,x,cache):
    temp=float(np.interp(r,radii,np.asarray(table["T_MeV"],float)))
    omega=MASS+float(x)*temp
    values=[a.evaluate_point(profile,r,omega,ORDERS[0],cache)]
    changes=[]
    for order in ORDERS[1:]:
        nxt=a.evaluate_point(profile,r,omega,order,cache)
        delta=a.compare_points(values[-1],nxt)["maximum_relative_change"]
        changes.append({"from":list(values[-1]["orders"]),"to":list(nxt["orders"]),"maximum_relative_change":delta})
        values.append(nxt)
        if delta<TOL: break
    return {"x":float(x),"omega":omega,"final":values[-1],
            "orders_ladder":[list(v["orders"]) for v in values],
            "successive_changes":changes,
            "final_change":changes[-1]["maximum_relative_change"],
            "quadrature_pass":changes[-1]["maximum_relative_change"]<TOL}

def pchip_absorption(endpoint,coarse_x,x):
    out={};sx=np.sqrt(np.asarray(coarse_x,float));se=math.sqrt(float(x))
    for charge in ("mu_minus","mu_plus"):
        vals=np.asarray([endpoint[float(k)]["final"]["charge_resolved"][charge]["absorption"] for k in coarse_x],float)
        modes=[]
        for j in range(3):
            y=vals[:,j]
            value=float(np.exp(PchipInterpolator(sx,np.log(np.maximum(y,1e-300)))(se))) if np.all(y>0) else float(PchipInterpolator(sx,y)(se))
            modes.append(max(value,0.0))
        out[charge]=modes
    return out

def reconstruct(absorption,omega,temp):
    boltz=math.exp(-omega/temp); reduced=-math.expm1(-omega/temp)
    momentum=math.sqrt(max(omega*omega-MASS*MASS,0.0))
    pref=omega*omega*momentum/(2*math.pi**2); out={}
    for q,arr in absorption.items():
        arr=np.asarray(arr,float); prod=boltz*arr
        out[q]={"absorption":arr.tolist(),"production":prod.tolist(),
                "reduced_absorption":(reduced*arr).tolist(),"spectral_source":(pref*prod).tolist()}
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--top-cells",type=Path,required=True)
    ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--top-n",type=int,default=10)
    args=ap.parse_args()
    if hashlib.sha256(PROFILE.read_bytes()).hexdigest()!=PROFILE_SHA: raise RuntimeError("profile SHA mismatch")
    a,table,radii=load_audit()
    coarse=np.asarray([.5,1.125,2.,3.7320508075688767,6.,11.19615242270663,18.,26.227922061357848,36.])
    selected=json.loads(args.top_cells.read_text())[:args.top_n]
    grouped={}
    for cell in selected: grouped.setdefault(int(cell["interval_index"]),[]).append(cell)
    args.output_dir.mkdir(parents=True,exist_ok=True)
    summaries=[]
    for idx,cells in sorted(grouped.items()):
        r0=float(radii[idx]);r1=float(radii[idx+1]);rm=.5*(r0+r1);cache={}
        left={float(x):evaluate_high_order(a,PROFILE,radii,table,r0,x,cache) for x in coarse}
        right={float(x):evaluate_high_order(a,PROFILE,radii,table,r1,x,cache) for x in coarse}
        cell_results=[]
        for cell in cells:
            xm=float(cell["x_mid"])
            center=evaluate_high_order(a,PROFILE,radii,table,rm,xm,cache)
            sx=np.sqrt(coarse);k=max(0,min(int(np.searchsorted(sx,math.sqrt(xm))-1),len(coarse)-2))
            x0=float(coarse[k]);x1=float(coarse[k+1]);omega=center["omega"];temp=center["final"]["temperature_MeV"]
            bilinear=a.interpolate_cell(left[x0]["final"],left[x1]["final"],right[x0]["final"],right[x1]["final"],omega,temp)
            eb=a.compare_midpoint_to_interpolation(center["final"],bilinear)["maximum_relative_error"]
            a0=pchip_absorption(left,coarse,xm);a1=pchip_absorption(right,coarse,xm)
            amid={q:[a._interpolate_pair(a0[q][j],a1[q][j],.5) for j in range(3)] for q in ("mu_minus","mu_plus")}
            ep=a.compare_midpoint_to_interpolation(center["final"],reconstruct(amid,omega,temp))["maximum_relative_error"]
            cell_results.append({"x_mid":xm,"omega_mid_MeV":omega,"quadrature_pass":center["quadrature_pass"],
                "final_successive_order_change":center["final_change"],"bilinear_log_high_order_error":eb,
                "pchip_then_radial_log_high_order_error":ep})
        endpoint_checks={side:[{"x":x,"orders_ladder":v["orders_ladder"],"final_change":v["final_change"],"pass":v["quadrature_pass"]}
                               for x,v in points.items()] for side,points in (("left",left),("right",right))}
        allpass=all(v["quadrature_pass"] for v in left.values()) and all(v["quadrature_pass"] for v in right.values()) and all(v["quadrature_pass"] for v in [evaluate_high_order(a,PROFILE,radii,table,rm,float(c["x_mid"]),cache) for c in cells])
        payload={"run":"P1B-E1-GLOBAL-03-TARGETED-HIGH-ORDER","interval_index":idx,"r_left_km":r0,"r_mid_km":rm,"r_right_km":r1,
            "profile_sha256":PROFILE_SHA,"orders_available":[list(x) for x in ORDERS],"quadrature_tolerance":TOL,
            "selected_cells":cells,"endpoint_quadrature":endpoint_checks,"cell_midpoint_checks":cell_results,
            "all_selected_nodes_pass_0p1pct":allpass,
            "scope":"Selected high-error cells only; not a full-profile high-order quadrature scan."}
        out=args.output_dir/f"interval_{idx:04d}_HIGH_ORDER.json"
        out.write_text(json.dumps(payload,indent=2)+"\n")
        summaries.append({"interval_index":idx,"all_selected_nodes_pass_0p1pct":allpass,"cell_checks":cell_results})
    result={"run":"P1B-E1-GLOBAL-03-TARGETED-HIGH-ORDER-SUMMARY","profile_sha256":PROFILE_SHA,
        "selected_cell_count":len(selected),"intervals":summaries,
        "all_selected_nodes_pass_0p1pct":all(x["all_selected_nodes_pass_0p1pct"] for x in summaries),
        "scope":"Selected worst interpolation intervals/cells only."}
    (args.output_dir/"SUMMARY.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
