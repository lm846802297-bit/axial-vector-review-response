#!/usr/bin/env python3
"""High-order B.13 polarization anchor at three low-x threshold coordinates."""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DEFAULT_PROFILE=ROOT/"data"/"sfho188_digitized.csv"
DEFAULT_OUTPUT=HERE/"results"/"P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18"/"POLARIZATION_ANCHOR_SUMMARY.json"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
ORDERS=((10,6,6,6),(14,8,8,8),(18,10,10,10),(22,12,12,12),(26,14,14,14))
EXTENSION=(30,16,16,16)
TOL=1e-3
RADIUS_KM=8.24821831451522
X_VALUES=(0.0,0.015,0.05)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    ap.add_argument("--radius-km",type=float,default=RADIUS_KM)
    ap.add_argument("--x-values",type=float,nargs="+",default=list(X_VALUES))
    ap.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    args=ap.parse_args()
    import hashlib
    digest=hashlib.sha256(args.profile.read_bytes()).hexdigest()
    if digest!=PROFILE_SHA:raise RuntimeError("SFHo profile SHA-256 mismatch")
    if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
    if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as audit
    bg=audit.load_profile(args.profile,np.asarray([args.radius_km]))
    temp=float(bg["T"][0]);lapse=float(bg["lapse"][0])
    points=[]
    for x in args.x_values:
        omega=10.0+float(x)*temp;cache={}
        ladder=[audit.evaluate_point(args.profile,args.radius_km,omega,o,cache) for o in ORDERS]
        changes=[audit.compare_points(ladder[i-1],ladder[i])["maximum_relative_change"] for i in range(1,len(ladder))]
        if changes[-1]>=TOL:
            ladder.append(audit.evaluate_point(args.profile,args.radius_km,omega,EXTENSION,cache))
            changes.append(audit.compare_points(ladder[-2],ladder[-1])["maximum_relative_change"])
        p=ladder[-1];m=p["total_absorption_by_mode"];tavg=.5*(m[1]+m[2]);total=sum(m)
        points.append({
          "x":float(x),"omega_local_MeV":omega,"absorption_modes":m,
          "L_over_T_average":m[0]/tavg if tavg>0 else None,
          "L_fraction":m[0]/total if total>0 else 0.0,
          "T_each_fraction":.5*(m[1]+m[2])/total if total>0 else 0.0,
          "successive_order_changes":changes,"final_successive_order_change":changes[-1],
          "longitudinal_suppression_vs_T_percent":100*(1-m[0]/tavg) if tavg>0 else None,
          "detailed_balance_residual":p["maximum_mode_detailed_balance_relative_residual"],
          "mass_shell_residual":p["final_muon_shell_relative_error"],
          "plus_minus_relative_difference":abs(m[1]-m[2])/max(m[1],m[2],1e-300),
          "finite_nonnegative":p["all_rates_finite_and_nonnegative"],
          "charge_resolved":{q:{"absorption":p["charge_resolved"][q]["absorption"]} for q in ("mu_minus","mu_plus")}
        })
    result={"run":"P1B-GLOBAL06B-POLARIZATION-ANCHOR-HIGH-ORDER","profile_sha256":digest,
      "radius_km":args.radius_km,"temperature_MeV":temp,"lapse":lapse,
      "order_ladder":[list(x) for x in ORDERS]+[list(EXTENSION)],"points":points,
      "scope":"B.13 moving-muon semi-Compton local absorption at one radial anchor only; not full B.2 transport."}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(args.output),"all_pass":all(x["final_successive_order_change"]<TOL and x["finite_nonnegative"] for x in points)},indent=2))

if __name__=="__main__":main()
