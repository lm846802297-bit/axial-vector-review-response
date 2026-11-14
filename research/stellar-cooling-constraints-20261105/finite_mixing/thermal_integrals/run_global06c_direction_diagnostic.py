#!/usr/bin/env python3
"""Global-06C-A: one-coordinate-at-a-time B.13 quadrature diagnosis.

Diagnostic only, not a full-profile acceptance run. Keeps the 10 MeV
pure-vector benchmark and compares all charge/mode/rate channels.
"""
from __future__ import annotations
import argparse, hashlib, json, sys, time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8cccbac240c001c"
R_KM=8.482141202
X_POINTS=(0.05,0.5,2.0,6.0,11.196,18.0,26.228,36.0)
ANCHOR=(36,20,20,20)
LADDERS={"n_p":(20,24,28,32,36),"n_mu":(12,14,16,18,20),
         "n_gamma":(12,14,16,18,20),"n_phi":(12,14,16,18,20)}
def sha(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for b in iter(lambda:f.read(1<<20),b""): h.update(b)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument("--profile",type=Path,default=PROFILE)
 ap.add_argument("--output",type=Path,default=HERE/"results"/"GLOBAL06C_A_DIRECTION_DIAGNOSTIC.json")
 ap.add_argument("--radius-km",type=float,default=R_KM)
 ap.add_argument("--x",type=float,nargs="*",default=list(X_POINTS))
 ap.add_argument("--anchor",type=int,nargs=4,default=list(ANCHOR))
 a=ap.parse_args()
 if sha(a.profile)!=PROFILE_SHA: raise RuntimeError("SFHo profile SHA-256 mismatch")
 if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
 if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
 import audit_b13_local_kernel_radial_energy_10mev as audit
 tab=np.genfromtxt(a.profile,delimiter=",",names=True); radii=np.asarray(tab["r_km"],float)
 def fast_load(_path,rr):
  rr=np.asarray(rr,float)
  return {n:np.interp(rr,radii,np.asarray(tab[c],float)) for n,c in
   {"T":"T_MeV","mu_mu":"mu_mu_MeV","mu_numu":"mu_numu_MeV","lapse":"lapse"}.items()}
 audit.load_profile=fast_load
 temp=float(np.interp(a.radius_km,radii,np.asarray(tab["T_MeV"],float)))
 anchor=tuple(a.anchor); cache={}; rows=[]; start=time.time()
 for x in a.x:
  omega=10.0+float(x)*temp
  ref=audit.evaluate_point(a.profile,a.radius_km,omega,anchor,cache)
  for idx,name in enumerate(("n_p","n_mu","n_gamma","n_phi")):
   ladder=[]
   for order in LADDERS[name]:
    orders=list(anchor); orders[idx]=order; orders=tuple(orders)
    val=audit.evaluate_point(a.profile,a.radius_km,omega,orders,cache)
    cmp=audit.compare_points(ref,val)
    ladder.append({"orders":list(orders),"max_channel_difference_vs_anchor":cmp["maximum_relative_change"],
      "per_charge_and_field":cmp["per_charge_and_field_max_relative_change"],
      "detailed_balance":val["maximum_mode_detailed_balance_relative_residual"],
      "mass_shell":val["final_muon_shell_relative_error"],
      "finite_nonnegative":val["all_rates_finite_and_nonnegative"]})
   rows.append({"x":float(x),"omega_local_MeV":omega,"direction":name,"ladder":ladder})
 result={"run":"GLOBAL-06C-A-DIRECTION-DIAGNOSTIC","profile_sha256":PROFILE_SHA,
  "radius_km":a.radius_km,"temperature_MeV":temp,"x_points":list(map(float,a.x)),
  "anchor_orders":list(anchor),"direction_ladders":{k:list(v) for k,v in LADDERS.items()},
  "results":rows,"runtime_seconds":time.time()-start,
  "scope":"Core-radius one-coordinate-at-a-time diagnosis only; not full-profile high-order acceptance."}
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps({"points":len(rows),"unique_kernel_evaluations":len(cache),
                   "runtime_seconds":result["runtime_seconds"],"output":str(a.output)},indent=2))
if __name__=="__main__": main()
