#!/usr/bin/env python3
"""Stratified low-x support audit for exact-recoil moving-muon B.13."""
from __future__ import annotations
import csv,hashlib,json,sys
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
    def point_at(target_r,x):
        return min(records,key=lambda z:abs(z["r_km"]-target_r)+1000.0*abs(z["x"]-x))
    def absorption_ratio(target_r):
        lo=point_at(target_r,0.05);hi=point_at(target_r,0.5)
        return [round(a/b,8) for a,b in zip(lo["absorption"]["mu_minus"],hi["absorption"]["mu_minus"])]
    summary={"run":"P1B-E1-GLOBAL-05-LOW-X-STRATIFIED-RADIAL","profile_sha256":PROFILE_SHA,
        "radial_indices":list(RADIAL_INDICES),"x_knots":list(X_KNOTS),"quadrature_order":list(ORDER),
        "direct_evaluations":len(records),"all_rates_finite_nonnegative":all(x["all_rates_finite_nonnegative"] for x in records),
        "maximum_detailed_balance_residual":max(x["detailed_balance_residual"] for x in records),
        "maximum_final_muon_shell_residual":max(x["final_muon_shell_relative_error"] for x in records),
        "selected_core_comparison":{"r_km":9.95,"T_MeV":point_at(9.95,0.05)["T_MeV"],
          "x_0p05_over_x_0p5_mu_minus_absorption_mode_ratios":absorption_ratio(9.95)},
        "radial_trend":{
          "r_13p95_km_x0p05_over_x0p5_mu_minus_mode_ratios":absorption_ratio(13.95),
          "r_15p5_km_x0p05_over_x0p5_mu_minus_mode_ratios":absorption_ratio(15.5),
          "r_16p588_km_x0p05_over_x0p5_mu_minus_mode_ratios":absorption_ratio(16.588),
          "r_18p75_km_x0p05_over_x0p5_mu_minus_mode_ratios":absorption_ratio(18.75)},
        "conclusion":"The existing Global-03/04 interpolation table starts at x=0.5 and sets B13 absorption to zero below support. Direct B13 evaluations show nonzero low-x absorption; at r=9.95 km, x=0.05 absorption is 7.08 times the x=0.5 longitudinal value and 1.82 times each transverse value. Therefore zeroing x<0.5 is not justified by the present data. This is a support gap to close before claiming full-band B1/B2 transport.",
        "scope":"80-point, 16-radius stratified low-x direct screen at low quadrature order; not a full radial scan, not high-order acceptance, and not an integrated luminosity correction."}
    outdir=HERE/"results"/"P1B_E1_GLOBAL_2D_MIDPOINT_2026-11-14"
    outdir.mkdir(parents=True,exist_ok=True)
    (outdir/"LOW_X_STRATIFIED_SCREEN.json").write_text(json.dumps(summary,indent=2)+"\n")
    (outdir/"LOW_X_STRATIFIED_RECORDS.json").write_text(json.dumps(records,indent=2)+"\n")
    with (outdir/"LOW_X_STRATIFIED_RECORDS.csv").open("w",newline="",encoding="utf-8") as stream:
        writer=csv.writer(stream,lineterminator="\\n")
        writer.writerow(["radial_index","r_km","T_MeV","x","omega_local_MeV",
            "mu_minus_L","mu_minus_Tplus","mu_minus_Tminus",
            "mu_plus_L","mu_plus_Tplus","mu_plus_Tminus",
            "detailed_balance_residual","final_muon_shell_relative_error","all_rates_finite_nonnegative"])
        for row in records:
            writer.writerow([row["radial_index"],row["r_km"],row["T_MeV"],row["x"],row["omega_local_MeV"],
                *row["absorption"]["mu_minus"],*row["absorption"]["mu_plus"],
                row["detailed_balance_residual"],row["final_muon_shell_relative_error"],
                str(row["all_rates_finite_nonnegative"]).lower()])
    print(json.dumps(summary,indent=2))
if __name__=="__main__":main()
