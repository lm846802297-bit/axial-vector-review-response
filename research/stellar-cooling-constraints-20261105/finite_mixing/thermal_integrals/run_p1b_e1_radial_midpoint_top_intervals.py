#!/usr/bin/env python3
"""Direct B.13 midpoint verification for the top radial-neighbor intervals.

For each selected adjacent pair of original SFHo radial nodes, evaluates the
exact-recoil B.13 kernel at the true radial midpoint for all nine refined
energy knots x=(omega_local-m_A')/T(r_mid). It compares the direct midpoint
with the same log-linear radial interpolation used by audit.interpolate_cell,
while reconstructing production/reduced absorption/spectral source at the
midpoint from exact detailed balance.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys, time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
for p in (ROOT,HERE):
    if str(p) not in sys.path:sys.path.insert(0,str(p))
import audit_b13_local_kernel_radial_energy_10mev as audit
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
EXPECTED_PROFILE_SHA256="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
ORDERS=(10,6,6,6);MASS=10.0
BASE_X=np.asarray([0.5,2.0,6.0,18.0,36.0],float)
def bisect_sqrt_x(nodes):
 return np.asarray(sorted(set(nodes.tolist()+[(0.5*(math.sqrt(a)+math.sqrt(b)))**2 for a,b in zip(nodes[:-1],nodes[1:])])),float)
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--global-dir",type=Path,required=True);ap.add_argument("--top-intervals",type=Path,required=True)
 ap.add_argument("--output-dir",type=Path,required=True);ap.add_argument("--start",type=int,default=0);ap.add_argument("--end",type=int,default=None)
 args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
 sha=hashlib.sha256(PROFILE.read_bytes()).hexdigest()
 if sha!=EXPECTED_PROFILE_SHA256:raise RuntimeError("profile SHA mismatch")
 top=json.loads(args.top_intervals.read_text());table=np.genfromtxt(PROFILE,delimiter=",",names=True);radii=np.asarray(table["r_km"],float)
 coarse=bisect_sqrt_x(BASE_X); intervals=top[args.start:args.end]
 chunk_cache={}
 def point(idx,x):
  if idx not in chunk_cache:
   d=json.loads((args.global_dir/f"chunk_{idx:04d}.json").read_text())
   if d.get("profile_sha256")!=sha:raise RuntimeError(f"profile hash mismatch in chunk {idx}")
   chunk_cache[idx]={float(r["x"]):r for r in d["records"]}
  return chunk_cache[idx][float(x)]
 results=[]
 for n,interval in enumerate(intervals,args.start):
  i=int(interval["left_radial_index"]);r0=float(radii[i]);r1=float(radii[i+1]);rm=0.5*(r0+r1)
  bg=audit.load_profile(PROFILE,np.asarray([rm],float));tm=float(bg["T"][0]);cache={};per_x=[]
  for x in coarse:
   omega=MASS+float(x)*tm
   direct=audit.evaluate_point(PROFILE,rm,omega,ORDERS,cache)
   left=point(i,x);right=point(i+1,x)
   prediction=audit.interpolate_cell(left,left,right,right,omega,tm)
   comparison=audit.compare_midpoint_to_interpolation(direct,prediction)
   per_x.append({"x":float(x),"omega_mid_MeV":omega,"maximum_relative_error":comparison["maximum_relative_error"],
     "per_charge_field_mode_relative_error":comparison["per_charge_field_mode_relative_error"],
     "direct_max_detailed_balance_residual":direct["maximum_mode_detailed_balance_relative_residual"],
     "direct_final_muon_shell_residual":direct["final_muon_shell_relative_error"],
     "direct_all_rates_finite_nonnegative":direct["all_rates_finite_and_nonnegative"]})
  worst=max(per_x,key=lambda z:z["maximum_relative_error"])
  payload={"run":"P1B-E1-RADIAL-MIDPOINT-TOP-INTERVALS","profile_sha256":sha,"left_radial_index":i,"right_radial_index":i+1,
   "r_left_km":r0,"r_right_km":r1,"r_mid_km":rm,"dr_km":r1-r0,"temperature_mid_MeV":tm,"orders":list(ORDERS),
   "neighbor_change_screen":interval,"energy_knots_x":coarse.tolist(),"midpoint_checks":per_x,
   "maximum_radial_midpoint_interpolation_error":worst["maximum_relative_error"],"worst_energy_x":worst["x"],
   "all_rates_finite_nonnegative":all(z["direct_all_rates_finite_nonnegative"] for z in per_x),
   "maximum_detailed_balance_residual":max(z["direct_max_detailed_balance_residual"] for z in per_x),
   "maximum_final_muon_shell_residual":max(z["direct_final_muon_shell_residual"] for z in per_x),
   "radial_midpoint_pass_1pct":bool(worst["maximum_relative_error"]<1e-2),
   "scope":"Direct low-order B.13 radial-midpoint checks for selected top neighbor-variation intervals only."}
  out=args.output_dir/f"interval_{i:04d}_{i+1:04d}.json";tmp=out.with_suffix(".tmp");tmp.write_text(json.dumps(payload,separators=(",",":"))+"\n");tmp.replace(out)
  results.append(payload);print(f"interval {i}-{i+1} r={r0:.6f}-{r1:.6f} km max midpoint error={worst['maximum_relative_error']:.4%}",flush=True)
 all_results=[]
 for f in sorted(args.output_dir.glob("interval_*.json")):
  d=json.loads(f.read_text())
  if d.get("profile_sha256")==sha:all_results.append(d)
 if all_results:
  summary={"run":"P1B-E1-RADIAL-MIDPOINT-TOP-INTERVALS","profile_sha256":sha,"intervals_checked":len(all_results),
   "maximum_radial_midpoint_interpolation_error":max(x["maximum_radial_midpoint_interpolation_error"] for x in all_results),
   "intervals_over_1pct":sum(x["maximum_radial_midpoint_interpolation_error"]>=1e-2 for x in all_results),
   "all_direct_rates_finite_nonnegative":all(x["all_rates_finite_nonnegative"] for x in all_results),
   "maximum_detailed_balance_residual":max(x["maximum_detailed_balance_residual"] for x in all_results),
   "maximum_final_muon_mass_shell_residual":max(x["maximum_final_muon_shell_residual"] for x in all_results),
   "worst_interval":max(all_results,key=lambda x:x["maximum_radial_midpoint_interpolation_error"]),
   "quadrature_acceptance":"low-order midpoint screening only; high-order verification of worst intervals remains separate",
   "scope":"Top-neighbor-change radial intervals only; not exhaustive radial-midpoint validation."}
  (args.output_dir/"SUMMARY.json").write_text(json.dumps(summary,indent=2)+"\n")
  print(json.dumps({k:v for k,v in summary.items() if k!="worst_interval"},indent=2))
if __name__=="__main__":main()
