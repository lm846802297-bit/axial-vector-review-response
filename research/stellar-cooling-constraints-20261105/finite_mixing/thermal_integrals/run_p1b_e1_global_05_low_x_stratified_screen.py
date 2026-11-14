#!/usr/bin/env python3
"""Stratified low-x support audit for exact-recoil moving-muon B.13."""
from __future__ import annotations
import hashlib,json,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
RADIAL_INDICES=(0,120,240,361,481,601,722,842,962,1024,1083,1203,1323,1444,1564,1685)
X_KNOTS=(0.05,0.1,0.2,0.35,0.5)
ORDER=(10,6,6,6)

def main():
    if hashlib.sha256(PROFILE.read_bytes()).hexdigest()!=PROFILE_SHA:raise RuntimeError("profile SHA mismatch")
    if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
    if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as audit
    table=np.genfromtxt(PROFILE,delimiter=",",names=True)
    radii=np.asarray(table["r_km"],float)
    def fast_load(path,r):
        r=np.asarray(r,float)
        return {n:np.interp(r,radii,np.asarray(table[c],float)) for n,c in
            {"T":"T_MeV","mu_mu":"mu_mu_MeV","mu_numu":"mu_numu_MeV","lapse":"lapse"}.items()}
    audit.load_profile=fast_load
    records=[]
    for i in RADIAL_INDICES:
        r=float(radii[i]);temp=float(table["T_MeV"][i]);cache={}
        for x in X_KNOTS:
            value=audit.evaluate_point(PROFILE,r,10.0+x*temp,ORDER,cache)
            records.append({"radial_index":i,"r_km":r,"T_MeV":temp,"x":x,"omega_local_MeV":10.0+x*temp,
                "absorption":{q:value["charge_resolved"][q]["absorption"] for q in ("mu_minus","mu_plus")},
                "production":{q:value["charge_resolved"][q]["production"] for q in ("mu_minus","mu_plus")},
                "detailed_balance_residual":value["maximum_mode_detailed_balance_relative_residual"],
                "final_muon_shell_relative_error":value["final_muon_shell_relative_error"],
                "all_rates_finite_nonnegative":value["all_rates_finite_and_nonnegative"]})
    summary={"run":"P1B-E1-GLOBAL-05-LOW-X-STRATIFIED-RADIAL","profile_sha256":PROFILE_SHA,
        "radial_indices":list(RADIAL_INDICES),"x_knots":list(X_KNOTS),"quadrature_order":list(ORDER),
        "direct_evaluations":len(records),"all_rates_finite_nonnegative":all(x["all_rates_finite_nonnegative"] for x in records),
        "maximum_detailed_balance_residual":max(x["detailed_balance_residual"] for x in records),
        "maximum_final_muon_shell_residual":max(x["final_muon_shell_relative_error"] for x in records),
        "scope":"80-point stratified radial low-x support screen at low quadrature order; not a high-order global acceptance."}
    out=HERE/"results"/"P1B_E1_GLOBAL_2D_MIDPOINT_2026-11-14"/"LOW_X_STRATIFIED_SCREEN.json"
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps({"summary":summary,"records":records},indent=2)+"\n")
    print(json.dumps(summary,indent=2))
if __name__=="__main__":main()
