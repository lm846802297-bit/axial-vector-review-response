#!/usr/bin/env python3
"""High-order convergence check at the previously flagged 417.895 MeV hot-shell point."""
from __future__ import annotations
import hashlib,json,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
RADIUS_KM=8.4821412022467;OMEGA_MEV=417.89463280068736
ORDERS=((10,6,6,6),(14,8,8,8),(18,10,10,10),(22,12,12,12),(26,14,14,14),(30,16,16,16),(34,18,18,18),(38,20,20,20))
TOL=1e-3

def main():
    if hashlib.sha256(PROFILE.read_bytes()).hexdigest()!=PROFILE_SHA:raise RuntimeError("profile SHA mismatch")
    if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
    if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as audit
    table=np.genfromtxt(PROFILE,delimiter=",",names=True);radii=np.asarray(table["r_km"],float)
    def fast_load(path,rr):
        rr=np.asarray(rr,float)
        return {n:np.interp(rr,radii,np.asarray(table[c],float)) for n,c in
            {"T":"T_MeV","mu_mu":"mu_mu_MeV","mu_numu":"mu_numu_MeV","lapse":"lapse"}.items()}
    audit.load_profile=fast_load
    temp=float(np.interp(RADIUS_KM,radii,np.asarray(table["T_MeV"],float)))
    cache={};values=[];changes=[]
    for order in ORDERS:
        value=audit.evaluate_point(PROFILE,RADIUS_KM,OMEGA_MEV,order,cache)
        if values:
            comparison=audit.compare_points(values[-1],value)
            changes.append({"from":list(values[-1]["orders"]),"to":list(value["orders"]),
                "maximum_relative_change":comparison["maximum_relative_change"],
                "per_charge_and_field_max_relative_change":comparison["per_charge_and_field_max_relative_change"]})
        values.append(value)
        if changes and changes[-1]["maximum_relative_change"]<TOL:break
    result={"run":"P1B-E1-GLOBAL-03-HOT-SHELL-HIGH-ORDER","profile_sha256":PROFILE_SHA,
        "radius_km":RADIUS_KM,"omega_local_MeV":OMEGA_MEV,"temperature_MeV":temp,
        "x":(OMEGA_MEV-10.0)/temp,"orders_ladder":[list(v["orders"]) for v in values],
        "successive_order_changes":changes,"final_successive_order_change":changes[-1]["maximum_relative_change"],
        "quadrature_pass_0p1pct":changes[-1]["maximum_relative_change"]<TOL,
        "maximum_detailed_balance_residual":values[-1]["maximum_mode_detailed_balance_relative_residual"],
        "final_muon_mass_shell_residual":values[-1]["final_muon_shell_relative_error"],
        "all_rates_finite_nonnegative":values[-1]["all_rates_finite_and_nonnegative"],
        "scope":"Single previously flagged hot-shell high-energy point; not a full-profile high-order scan."}
    out=HERE/"results"/"P1B_E1_GLOBAL_2D_MIDPOINT_2026-11-14"/"HOT_SHELL_417MeV_HIGH_ORDER.json"
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()
