#!/usr/bin/env python3
"""Reproduce the targeted high-order Global-06B threshold-edge checks.

The committed HIGH_ORDER_TARGETS_INPUT.json freezes the ten worst radial
intervals and ten worst low-x energy-interpolation validation points from the
full 1687-radius low-order screen. The script computes all unique (r,x)
positions, retaining charge and L,+,- channels separately.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys, time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
from scipy.interpolate import PchipInterpolator

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
DEFAULT_TARGETS=HERE/"results"/"P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18"/"HIGH_ORDER_TARGETS_INPUT.json"
DEFAULT_OUTPUT=HERE/"results"/"P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18"
ORDERS=((10,6,6,6),(14,8,8,8),(18,10,10,10),(22,12,12,12),(26,14,14,14))
EXTENSION=(30,16,16,16)
TOL=1.0e-3
CHARGES=("mu_minus","mu_plus")
MODES=("L","+","-")
_AUDIT=_TABLE=_RADII=_PROFILE=None

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):h.update(b)
    return h.hexdigest()

def init_worker(profile_path):
    global _AUDIT,_TABLE,_RADII,_PROFILE
    _PROFILE=Path(profile_path)
    if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
    if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as audit
    _AUDIT=audit
    _TABLE=np.genfromtxt(_PROFILE,delimiter=",",names=True)
    _RADII=np.asarray(_TABLE["r_km"],float)
    def fast_load(_path,rr):
        rr=np.asarray(rr,float)
        return {n:np.interp(rr,_RADII,np.asarray(_TABLE[c],float)) for n,c in
          {"T":"T_MeV","mu_mu":"mu_mu_MeV","mu_numu":"mu_numu_MeV","lapse":"lapse"}.items()}
    _AUDIT.load_profile=fast_load

def evaluate_task(task):
    r,x=task
    temp=float(np.interp(r,_RADII,np.asarray(_TABLE["T_MeV"],float)))
    omega=10.0+x*temp
    cache={}
    ladder=[_AUDIT.evaluate_point(_PROFILE,r,omega,o,cache) for o in ORDERS]
    changes=[_AUDIT.compare_points(ladder[i-1],ladder[i])["maximum_relative_change"] for i in range(1,len(ladder))]
    if changes[-1]>=TOL:
        ladder.append(_AUDIT.evaluate_point(_PROFILE,r,omega,EXTENSION,cache))
        changes.append(_AUDIT.compare_points(ladder[-2],ladder[-1])["maximum_relative_change"])
    final=ladder[-1]
    return {"r_km":float(r),"x":float(x),"omega_local_MeV":float(omega),
      "orders":[v["orders"] for v in ladder],"successive_changes":changes,
      "final_change":changes[-1],"quadrature_pass":bool(changes[-1]<TOL),
      "detailed_balance_max":max(v["maximum_mode_detailed_balance_relative_residual"] for v in ladder),
      "mass_shell_max":max(v["final_muon_shell_relative_error"] for v in ladder),
      "finite_nonnegative":all(v["all_rates_finite_and_nonnegative"] for v in ladder),
      "final_payload":final}

def rel(a,b):
    return abs(a-b)/max(abs(a),abs(b),1e-300)

def interp_energy(values,x,xgrid):
    values=np.asarray(values,float)
    if np.all(values>0):
        return float(np.exp(PchipInterpolator(np.sqrt(xgrid),np.log(values))(math.sqrt(x))))
    return max(float(PchipInterpolator(np.sqrt(xgrid),values)(math.sqrt(x))),0.0)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--targets",type=Path,default=DEFAULT_TARGETS)
    ap.add_argument("--profile",type=Path,default=PROFILE)
    ap.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    ap.add_argument("--workers",type=int,default=4)
    args=ap.parse_args()
    started=time.time()
    if sha(args.profile)!=PROFILE_SHA:raise RuntimeError("SFHo profile SHA-256 mismatch")
    targets=json.loads(args.targets.read_text(encoding="utf-8"))
    if targets["source_profile_sha256"]!=PROFILE_SHA:raise RuntimeError("target/profile provenance mismatch")
    xgrid=np.asarray(targets["x_grid"],float);xval=np.asarray(targets["x_validation"],float)
    table=np.genfromtxt(args.profile,delimiter=",",names=True);radii=np.asarray(table["r_km"],float)
    taskmap={}
    def add(r,x):taskmap[(round(float(r),12),round(float(x),14))]=(float(r),float(x))
    radial_targets=targets["radial_top10"];energy_targets=targets["energy_worst10"]
    for item in radial_targets:
        i=int(item["left_index"]);r0=float(radii[i]);r1=float(radii[i+1]);rm=.5*(r0+r1)
        for r in (r0,rm,r1):
            for x in xgrid:add(r,x)
    for item in energy_targets:
        r=float(item["r_km"])
        for x in np.r_[xgrid,xval]:add(r,x)
    tasks=list(taskmap.values());results={}
    with ProcessPoolExecutor(max_workers=args.workers,initializer=init_worker,initargs=(str(args.profile),)) as pool:
        futures={pool.submit(evaluate_task,t):t for t in tasks}
        for n,f in enumerate(as_completed(futures),1):
            p=f.result();results[(round(p["r_km"],12),round(p["x"],14))]=p
            if n%50==0 or n==len(tasks):print(f"high-order points {n}/{len(tasks)}",flush=True)
    radial_results=[]
    for rank,item in enumerate(radial_targets,1):
        i=int(item["left_index"]);r0=float(radii[i]);r1=float(radii[i+1]);rm=.5*(r0+r1)
        checks=[]
        for x in xgrid:
            left=results[(round(r0,12),round(float(x),14))]["final_payload"]
            mid=results[(round(rm,12),round(float(x),14))]["final_payload"]
            right=results[(round(r1,12),round(float(x),14))]["final_payload"]
            errors={}
            for q in CHARGES:
                errors[q]={}
                for im,mode in enumerate(MODES):
                    a=left["charge_resolved"][q]["absorption"][im]
                    b=right["charge_resolved"][q]["absorption"][im]
                    pred=math.exp(.5*(math.log(a)+math.log(b))) if a>0 and b>0 else .5*(a+b)
                    truth=mid["charge_resolved"][q]["absorption"][im]
                    errors[q][mode]=rel(pred,truth)
            checks.append({"x":float(x),"maximum_channel_error":max(v for z in errors.values() for v in z.values()),"channel_errors":errors})
        points=[results[(round(r,12),round(float(x),14))] for r in (r0,rm,r1) for x in xgrid]
        radial_results.append({"rank":rank,"interval_index":i,"r_left_km":r0,"r_mid_km":rm,"r_right_km":r1,
          "maximum_high_order_midpoint_interpolation_error":max(z["maximum_channel_error"] for z in checks),
          "radial_interpolation_checks":checks,"all_quadrature_pass":all(p["quadrature_pass"] for p in points)})
    energy_results=[]
    for rank,item in enumerate(energy_targets,1):
        r=float(item["r_km"]);x=float(item["x_validation"])
        grid=[results[(round(r,12),round(float(xx),14))] for xx in xgrid]
        validation=[results[(round(r,12),round(float(xx),14))] for xx in xval]
        direct=results[(round(r,12),round(x,14))]
        errors={}
        for q in CHARGES:
            errors[q]={}
            for im,mode in enumerate(MODES):
                y=[p["final_payload"]["charge_resolved"][q]["absorption"][im] for p in grid]
                truth=direct["final_payload"]["charge_resolved"][q]["absorption"][im]
                errors[q][mode]=rel(interp_energy(y,x,xgrid),truth)
        allp=grid+validation
        energy_results.append({"rank":rank,"radial_index":int(item["radial_index"]),"r_km":r,"x_validation":x,
          "direct_low_order_error":float(item["maximum_channel_relative_error"]),
          "high_order_pchip_error":max(v for z in errors.values() for v in z.values()),
          "high_order_pchip_channel_errors":errors,
          "maximum_detailed_balance_residual":max(p["detailed_balance_max"] for p in allp),
          "maximum_mass_shell_residual":max(p["mass_shell_max"] for p in allp),
          "all_rates_finite_nonnegative":all(p["finite_nonnegative"] for p in allp),
          "maximum_final_order_change":max(p["final_change"] for p in allp),
          "all_grid_and_validation_quadrature_pass":all(p["quadrature_pass"] for p in allp)})
    allp=list(results.values())
    summary={"run":"P1B-GLOBAL06B-HIGH-ORDER-TARGETS","profile_sha256":PROFILE_SHA,
      "targets_sha256":sha(args.targets),"unique_r_x_points":len(tasks),
      "nominal_ordered_evaluations":sum(len(p["orders"]) for p in allp),
      "order_ladder":[list(x) for x in ORDERS]+[list(EXTENSION)],
      "criterion_successive_order_change_below":TOL,
      "targeted_radial_intervals":len(radial_results),"targeted_energy_worst_points":len(energy_results),
      "radial_results":radial_results,"energy_results":energy_results,
      "acceptance":{"all_targeted_quadrature_pass":all(p["quadrature_pass"] for p in allp) and all(x["all_grid_and_validation_quadrature_pass"] for x in energy_results),
        "maximum_high_order_radial_midpoint_interpolation_error":max(x["maximum_high_order_midpoint_interpolation_error"] for x in radial_results),
        "maximum_high_order_energy_pchip_error":max(x["high_order_pchip_error"] for x in energy_results),
        "maximum_final_successive_order_change":max(p["final_change"] for p in allp),
        "maximum_detailed_balance_residual":max(p["detailed_balance_max"] for p in allp),
        "maximum_mass_shell_residual":max(p["mass_shell_max"] for p in allp),
        "all_rates_finite_nonnegative":all(p["finite_nonnegative"] for p in allp),
        "full_global_high_order_acceptance":False},
      "runtime_seconds":time.time()-started,"workers":args.workers,
      "scope":"Top ten radial-variation intervals and ten worst low-x energy interpolation points only; not exhaustive high-order validation of all 1687 radial nodes."}
    args.output.mkdir(parents=True,exist_ok=True)
    (args.output/"HIGH_ORDER_TARGETED_POINTS.json").write_text(json.dumps(list(results.values()),separators=(",",":"))+"\n",encoding="utf-8")
    (args.output/"HIGH_ORDER_ACCEPTANCE_SUMMARY.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(summary["acceptance"],indent=2))
    print(f"unique points={len(tasks)} runtime={summary['runtime_seconds']:.1f}s")

if __name__=="__main__":main()
