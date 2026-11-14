#!/usr/bin/env python3
"""Dynamic multiprocessing scheduler for the immutable P1-B E1 global scan.

The per-radius chunk format and source hash are deliberately identical to
run_p1b_e1_global_energy_scan.py. This scheduler only redistributes missing
radial indices among worker processes; it does not change the physics kernel,
energy grid, quadrature order, or stored result schema.
"""
from __future__ import annotations
import argparse, hashlib, json, math, os, time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for p in (ROOT,HERE):
    if str(p) not in os.sys.path: os.sys.path.insert(0,str(p))
import audit_b13_local_kernel_radial_energy_10mev as audit

PROFILE=ROOT/"data"/"sfho188_digitized.csv"
EXPECTED_PROFILE_SHA256="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
MASS_MEV=10.0
ORDERS=(10,6,6,6)
BASE_X=np.asarray([0.5,2.0,6.0,18.0,36.0],float)
INTERP_TOL=1e-2
ORIGINAL_DRIVER=HERE/"run_p1b_e1_global_energy_scan.py"
PROFILE_SHA=hashlib.sha256(PROFILE.read_bytes()).hexdigest()
SOURCE_SHA=hashlib.sha256(ORIGINAL_DRIVER.read_bytes()).hexdigest()
TABLE=np.genfromtxt(PROFILE,delimiter=",",names=True)
RADII=np.asarray(TABLE["r_km"],float)
COARSE_X=np.asarray(sorted(set(BASE_X.tolist()+[(0.5*(math.sqrt(a)+math.sqrt(b)))**2 for a,b in zip(BASE_X[:-1],BASE_X[1:])])),float)
VALIDATION_X=np.asarray(sorted(set(COARSE_X.tolist()+[(0.5*(math.sqrt(a)+math.sqrt(b)))**2 for a,b in zip(COARSE_X[:-1],COARSE_X[1:])])),float)
NEW_X=np.asarray([x for x in VALIDATION_X if not np.any(np.isclose(x,COARSE_X,rtol=0,atol=1e-13))],float)

def compact_record(v):
    return {
      "radius_km":v["radius_km"],"omega_local_MeV":v["omega_local_MeV"],"temperature_MeV":v["temperature_MeV"],
      "mu_minus_chemical_potential_MeV":v["mu_minus_chemical_potential_MeV"],"lapse":v["lapse"],"x_max":v["x_max"],"orders":v["orders"],
      "charge_resolved":{q:{"production":v["charge_resolved"][q]["production"],"absorption":v["charge_resolved"][q]["absorption"],
        "reduced_absorption":v["charge_resolved"][q]["reduced_absorption"],"spectral_source":v["charge_resolved"][q]["spectral_source"]} for q in audit.CHARGES},
      "maximum_mode_detailed_balance_relative_residual":v["maximum_mode_detailed_balance_relative_residual"],
      "final_muon_shell_relative_error":v["final_muon_shell_relative_error"],
      "charge_sum_closure_relative_residual":v["charge_sum_closure_relative_residual"],
      "all_rates_finite_and_nonnegative":v["all_rates_finite_and_nonnegative"]}

def interpolate_errors(points):
    errors=[]
    for charge in audit.CHARGES:
        coarse=np.asarray([points[float(x)]["charge_resolved"][charge]["absorption"] for x in COARSE_X],float)
        interpolants=[PchipInterpolator(np.sqrt(COARSE_X),np.log(np.maximum(coarse[:,j],1e-300))) for j in range(3)]
        for x in NEW_X:
            direct=np.asarray(points[float(x)]["charge_resolved"][charge]["absorption"],float)
            for j,mode in enumerate(audit.MODES):
                pred=float(np.exp(interpolants[j](math.sqrt(float(x)))))
                obs=float(direct[j])
                errors.append({"x_mid":float(x),"charge":charge,"mode":mode,"direct_absorption":obs,"PCHIP_absorption":pred,
                  "relative_error":abs(obs-pred)/max(abs(obs),abs(pred),1e-300)})
    return errors

def do_chunk(task):
    idx,outdir=task
    out=Path(outdir)/f"chunk_{idx:04d}.json"
    if out.exists():
        old=json.loads(out.read_text())
        if old.get("profile_sha256")==PROFILE_SHA and old.get("source_sha256")==SOURCE_SHA:
            return {"index":idx,"status":"skipped_verified"}
        raise RuntimeError(f"Existing chunk provenance mismatch: {out}")
    radius=float(RADII[idx]); temp=float(TABLE["T_MeV"][idx]); cache={}; points={}; records=[]
    max_db=0.0; max_shell=0.0; nonnegative=True; started=time.time()
    for x in VALIDATION_X:
        omega=MASS_MEV+float(x)*temp
        v=audit.evaluate_point(PROFILE,radius,omega,ORDERS,cache)
        points[float(x)]=v
        max_db=max(max_db,v["maximum_mode_detailed_balance_relative_residual"])
        max_shell=max(max_shell,v["final_muon_shell_relative_error"])
        nonnegative=nonnegative and v["all_rates_finite_and_nonnegative"]
        records.append({"radial_index":idx,"x":float(x),**compact_record(v)})
    errors=interpolate_errors(points); worst=max(errors,key=lambda z:z["relative_error"])
    payload={"run":"P1B-E1-GLOBAL-ALL-RADIAL-KNOTS","chunk_index":idx,"radial_index_range_inclusive":[idx,idx],
      "profile_sha256":PROFILE_SHA,"source_sha256":SOURCE_SHA,"profile_rows":int(len(RADII)),"mass_MeV":MASS_MEV,
      "couplings":{"gV_over_gX":1.0,"gA_over_gX":0.0},"orders":list(ORDERS),"base_x":BASE_X.tolist(),"coarse_x":COARSE_X.tolist(),
      "validation_grid_x":VALIDATION_X.tolist(),"new_midpoint_x":NEW_X.tolist(),"records":records,
      "radial_interpolation_summaries":[{"radial_index":idx,"radius_km":radius,"maximum_interpolation_error":worst["relative_error"],
        "worst_x_mid":worst["x_mid"],"worst_charge":worst["charge"],"worst_mode":worst["mode"],"all_channel_errors":errors}],
      "acceptance":{"all_finite_nonnegative":bool(nonnegative),"maximum_detailed_balance_residual":max_db,
        "maximum_final_muon_shell_residual":max_shell,"maximum_energy_interpolation_error":worst["relative_error"],
        "interpolation_tolerance":INTERP_TOL,"interpolation_pass_in_chunk":bool(worst["relative_error"]<INTERP_TOL)},
      "runtime_seconds":time.time()-started}
    tmp=out.with_suffix(".tmp"); tmp.write_text(json.dumps(payload,separators=(",",":"))+"\n"); tmp.replace(out)
    return {"index":idx,"status":"completed","max_error":worst["relative_error"],"seconds":payload["runtime_seconds"]}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--workers",type=int,default=5); ap.add_argument("--start",type=int,default=0); ap.add_argument("--end",type=int,default=len(RADII))
    ap.add_argument("--indices",type=int,nargs="*",default=None)
    args=ap.parse_args()
    if PROFILE_SHA!=EXPECTED_PROFILE_SHA256: raise RuntimeError(f"profile SHA mismatch: {PROFILE_SHA}")
    if len(RADII)!=1687: raise RuntimeError(f"Expected 1687 radial nodes, got {len(RADII)}")
    args.output_dir.mkdir(parents=True,exist_ok=True)
    indices=args.indices if args.indices is not None else list(range(args.start,args.end))
    tasks=[(int(i),str(args.output_dir)) for i in indices]
    t0=time.time(); done=0
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures=[pool.submit(do_chunk,t) for t in tasks]
        for fut in as_completed(futures):
            result=fut.result(); done+=1
            if result["status"]=="completed":
                print(f"{done}/{len(tasks)} radial nodes: {result['index']} maxE={result['max_error']:.4%} time={result['seconds']:.1f}s",flush=True)
    files=sorted(args.output_dir.glob("chunk_*.json")); all_summaries=[]; completed=[]; max_db=0.; max_shell=0.; nonnegative=True
    for f in files:
        d=json.loads(f.read_text())
        if d.get("profile_sha256")!=PROFILE_SHA or d.get("source_sha256")!=SOURCE_SHA: continue
        completed.append(d["chunk_index"]); all_summaries.extend(d["radial_interpolation_summaries"])
        max_db=max(max_db,d["acceptance"]["maximum_detailed_balance_residual"])
        max_shell=max(max_shell,d["acceptance"]["maximum_final_muon_shell_residual"])
        nonnegative=nonnegative and d["acceptance"]["all_finite_nonnegative"]
    if all_summaries:
        vals=np.asarray([x["maximum_interpolation_error"] for x in all_summaries],float)
        worst=max(all_summaries,key=lambda x:x["maximum_interpolation_error"])
        summary={"run":"P1B-E1-GLOBAL-ALL-RADIAL-KNOTS","profile_sha256":PROFILE_SHA,"source_sha256":SOURCE_SHA,
          "profile_rows":len(RADII),"completed_chunks":sorted(completed),"total_chunks":len(RADII),"completed_radial_nodes":len(all_summaries),
          "maximum_energy_interpolation_error":float(vals.max()),"median_radial_node_maximum_error":float(np.median(vals)),
          "p95_radial_node_maximum_error":float(np.quantile(vals,.95)),"fraction_radial_nodes_over_1pct":float(np.mean(vals>=INTERP_TOL)),
          "maximum_detailed_balance_residual":max_db,"maximum_final_muon_mass_shell_residual":max_shell,
          "all_rates_finite_nonnegative":bool(nonnegative),"worst_location":worst,
          "global_low_order_interpolation_screen_pass":bool(len(all_summaries)==len(RADII) and vals.max()<INTERP_TOL),
          "quadrature_acceptance":"not tested by this low-order global screening run","full_star_transport_claimed":False,
          "scope":"Low-order global energy-interpolation screening; not global quadrature acceptance or full-star transport.",
          "runtime_seconds_this_invocation":time.time()-t0}
        (args.output_dir/"GLOBAL_SUMMARY.json").write_text(json.dumps(summary,indent=2)+"\n")
        print(json.dumps({k:v for k,v in summary.items() if k!="worst_location"},indent=2),flush=True)

if __name__=="__main__": main()
