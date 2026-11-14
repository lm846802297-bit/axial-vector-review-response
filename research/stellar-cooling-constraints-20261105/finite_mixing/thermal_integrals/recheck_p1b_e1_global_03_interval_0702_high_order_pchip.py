#!/usr/bin/env python3
"""Recompute interval-702 2D PCHIP interpolation with the x=36 order-36 endpoint extension."""
from __future__ import annotations
import hashlib,json,math,sys
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
ORDERS=((16,10,10,10),(20,12,12,12),(24,14,14,14),(28,16,16,16),(32,18,18,18),(36,20,20,20))
COARSE=np.asarray([.5,1.125,2.,3.7320508075688767,6.,11.19615242270663,18.,26.227922061357848,36.])
MASS=10.0;INDEX=702;XM=8.397114317029972;TOL=1e-3

def main():
    if hashlib.sha256(PROFILE.read_bytes()).hexdigest()!=PROFILE_SHA:raise RuntimeError("profile SHA mismatch")
    if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
    if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as a
    table=np.genfromtxt(PROFILE,delimiter=",",names=True);radii=np.asarray(table["r_km"],float)
    def fast_load(path,rr):
        rr=np.asarray(rr,float)
        return {n:np.interp(rr,radii,np.asarray(table[c],float)) for n,c in
            {"T":"T_MeV","mu_mu":"mu_mu_MeV","mu_numu":"mu_numu_MeV","lapse":"lapse"}.items()}
    a.load_profile=fast_load
    r0=float(radii[INDEX]);r1=float(radii[INDEX+1]);rm=.5*(r0+r1);cache={}
    def evaluate(r,x):
        temp=float(np.interp(r,radii,np.asarray(table["T_MeV"],float)));omega=MASS+float(x)*temp
        vals=[];changes=[]
        for order in ORDERS:
            v=a.evaluate_point(PROFILE,r,omega,order,cache)
            if vals:
                delta=a.compare_points(vals[-1],v)["maximum_relative_change"]
                changes.append(delta)
            vals.append(v)
            if changes and changes[-1]<TOL:break
        return {"x":float(x),"omega":omega,"temperature":temp,"final":vals[-1],
            "orders":[list(v["orders"]) for v in vals],"last_change":changes[-1],"pass":changes[-1]<TOL}
    left={float(x):evaluate(r0,x) for x in COARSE}
    right={float(x):evaluate(r1,x) for x in COARSE}
    center=evaluate(rm,XM);omega=center["omega"];temp=center["temperature"]
    def pchip(endpoint,q):
        vals=np.asarray([endpoint[float(x)]["final"]["charge_resolved"][q]["absorption"] for x in COARSE],float)
        sx=np.sqrt(COARSE);out=[]
        for j in range(3):
            y=vals[:,j]
            out.append(float(np.exp(PchipInterpolator(sx,np.log(np.maximum(y,1e-300)))(math.sqrt(XM)))))
        return out
    a0={q:pchip(left,q) for q in ("mu_minus","mu_plus")}
    a1={q:pchip(right,q) for q in ("mu_minus","mu_plus")}
    amid={q:[a._interpolate_pair(a0[q][j],a1[q][j],.5) for j in range(3)] for q in ("mu_minus","mu_plus")}
    bol=math.exp(-omega/temp);red=-math.expm1(-omega/temp);k=math.sqrt(omega*omega-MASS*MASS);pref=omega*omega*k/(2*math.pi**2)
    pred={}
    for q,arr in amid.items():
        arr=np.asarray(arr,float);prod=bol*arr
        pred[q]={"absorption":arr.tolist(),"production":prod.tolist(),"reduced_absorption":(red*arr).tolist(),"spectral_source":(pref*prod).tolist()}
    pchip_error=a.compare_midpoint_to_interpolation(center["final"],pred)
    sx=np.sqrt(COARSE);j=max(0,min(int(np.searchsorted(sx,math.sqrt(XM))-1),len(COARSE)-2))
    x0=float(COARSE[j]);x1=float(COARSE[j+1])
    bilinear=a.interpolate_cell(left[x0]["final"],left[x1]["final"],right[x0]["final"],right[x1]["final"],omega,temp)
    bilinear_error=a.compare_midpoint_to_interpolation(center["final"],bilinear)
    nodes=list(left.values())+list(right.values())+[center]
    all_final=[x["final"] for x in nodes]
    result={"run":"P1B-E1-GLOBAL-03-INTERVAL-0702-HIGH-ORDER-PCHIP-RECHECK","profile_sha256":PROFILE_SHA,
        "interval_index":INDEX,"r_left_km":r0,"r_mid_km":rm,"r_right_km":r1,"x_mid":XM,"omega_mid_MeV":omega,
        "endpoint_energy_knots":9,"high_order_nodes":19,"orders_available":[list(x) for x in ORDERS],
        "all_quadrature_nodes_pass_0p1pct":all(x["pass"] for x in nodes),
        "maximum_successive_order_change":max(x["last_change"] for x in nodes),
        "pchip_then_radial_log_interpolation_error":pchip_error["maximum_relative_error"],
        "bilinear_log_interpolation_error":bilinear_error["maximum_relative_error"],
        "maximum_detailed_balance_residual":max(x["maximum_mode_detailed_balance_relative_residual"] for x in all_final),
        "maximum_final_muon_mass_shell_residual":max(x["final_muon_shell_relative_error"] for x in all_final),
        "all_rates_finite_nonnegative":all(x["all_rates_finite_and_nonnegative"] for x in all_final),
        "scope":"High-order recheck of interval 702 using all nine energy knots at both radial endpoints and the direct cell center."}
    out=HERE/"results"/"P1B_E1_GLOBAL_2D_MIDPOINT_2026-11-14"/"INTERVAL_0702_HIGH_ORDER_PCHIP_RECHECK.json"
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()
