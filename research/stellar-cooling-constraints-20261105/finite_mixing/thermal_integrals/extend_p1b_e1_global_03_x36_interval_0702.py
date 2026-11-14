#!/usr/bin/env python3
"""Extend the interval-702 x=36 high-energy B.13 quadrature check to order 36."""
from __future__ import annotations
import hashlib,json,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
ORDERS=((32,18,18,18),(36,20,20,20))
def main():
    if hashlib.sha256(PROFILE.read_bytes()).hexdigest()!=PROFILE_SHA:raise RuntimeError("profile SHA mismatch")
    if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
    if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as audit
    table=np.genfromtxt(PROFILE,delimiter=",",names=True);radii=np.asarray(table["r_km"],float)
    def fast_load(path,rr):
        rr=np.asarray(rr,float)
        return {n:np.interp(rr,radii,np.asarray(table[c],float)) for n,c in {"T":"T_MeV","mu_mu":"mu_mu_MeV","mu_numu":"mu_numu_MeV","lapse":"lapse"}.items()}
    audit.load_profile=fast_load
    results=[]
    for i in (702,703):
        r=float(radii[i]);temp=float(np.interp(r,radii,np.asarray(table["T_MeV"],float)))
        omega=10.0+36.0*temp;cache={}
        first=audit.evaluate_point(PROFILE,r,omega,ORDERS[0],cache)
        second=audit.evaluate_point(PROFILE,r,omega,ORDERS[1],cache)
        delta=audit.compare_points(first,second)["maximum_relative_change"]
        results.append({"radial_index":i,"radius_km":r,"temperature_MeV":temp,"x":36.0,"omega_local_MeV":omega,
            "orders":[list(ORDERS[0]),list(ORDERS[1])],"maximum_successive_order_change":delta,
            "pass_0p1pct":delta<1e-3,"detailed_balance_residual":second["maximum_mode_detailed_balance_relative_residual"],
            "final_muon_mass_shell_residual":second["final_muon_shell_relative_error"]})
    result={"run":"P1B-E1-GLOBAL-03-X36-HIGH-ORDER-EXTENSION","profile_sha256":PROFILE_SHA,
        "interval_index":702,"energy_coordinate_x":36.0,"endpoints":results,
        "both_endpoints_pass_0p1pct":all(x["pass_0p1pct"] for x in results),
        "scope":"Only the two interval-702 x=36 endpoints; no global high-order quadrature claim."}
    out=HERE/"results"/"P1B_E1_GLOBAL_2D_MIDPOINT_2026-11-14"/"X36_ENDPOINT_EXTENSION_0702.json"
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()
