#!/usr/bin/env python3
"""High-order B.13 polarization scan at every SFHo radial vertex.

This scan samples x=0, 0.015, and 0.05 at all 1687 profile radii. It is a
radial-coverage diagnostic, not the full nine-knot B.1 energy integral or B.2
transport. Each point retains mu-/mu+ and L,+,- separately.
"""
from __future__ import annotations
import argparse,hashlib,json,sys,time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DEFAULT_PROFILE=ROOT/"data"/"sfho188_digitized.csv"
DEFAULT_OUTPUT=HERE/"results"/"P1B_GLOBAL06B_FULL_RADIAL_POLARIZATION_2026-11-18"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
ORDERS=((18,10,10,10),(22,12,12,12),(26,14,14,14))
EXTENSION=(30,16,16,16)
TOL=1e-3
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
    p=ladder[-1]
    abs_modes=p["total_absorption_by_mode"]
    tavg=.5*(abs_modes[1]+abs_modes[2])
    total=sum(abs_modes)
    return {
      "r_km":float(r),"x":float(x),"omega_local_MeV":float(omega),
      "orders":[v["orders"] for v in ladder],"successive_order_changes":changes,
      "final_change":changes[-1],"quadrature_pass":bool(changes[-1]<TOL),
      "detailed_balance_max":max(v["maximum_mode_detailed_balance_relative_residual"] for v in ladder),
      "mass_shell_max":max(v["final_muon_shell_relative_error"] for v in ladder),
      "finite_nonnegative":all(v["all_rates_finite_and_nonnegative"] for v in ladder),
      "absorption_modes":abs_modes,
      "L_over_T_average":abs_modes[0]/tavg if tavg>0 else None,
      "mode_fractions":[v/total for v in abs_modes] if total>0 else [0.0,0.0,0.0],
      "plus_minus_relative_difference":abs(abs_modes[1]-abs_modes[2])/max(abs_modes[1],abs_modes[2],1e-300),
      "charge_resolved_absorption":{q:p["charge_resolved"][q]["absorption"] for q in CHARGES},
      "charge_resolved_production":{q:p["charge_resolved"][q]["production"] for q in CHARGES},
      "charge_resolved_reduced_absorption":{q:p["charge_resolved"][q]["reduced_absorption"] for q in CHARGES}
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    ap.add_argument("--x-values",type=float,nargs="+",default=[0.0,0.015,0.05])
    ap.add_argument("--workers",type=int,default=4)
    ap.add_argument("--radial-stride",type=int,default=1,help="Use every Nth profile radius; 1 means all 1687 nodes")
    ap.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    args=ap.parse_args()
    started=time.time()
    if sha(args.profile)!=PROFILE_SHA:raise RuntimeError("SFHo profile SHA-256 mismatch")
    table=np.genfromtxt(args.profile,delimiter=",",names=True)
    radii=np.asarray(table["r_km"],float)
    if args.radial_stride<1:raise ValueError("--radial-stride must be >=1")
    scan_radii=radii[::args.radial_stride]
    tasks=[(float(r),float(x)) for x in args.x_values for r in scan_radii]
    results=[]
    with ProcessPoolExecutor(max_workers=args.workers,initializer=init_worker,initargs=(str(args.profile),)) as pool:
        futures=[pool.submit(evaluate_task,t) for t in tasks]
        for n,f in enumerate(as_completed(futures),1):
            results.append(f.result())
            if n%100==0 or n==len(futures):print(f"radial polarization points {n}/{len(futures)}",flush=True)
    results.sort(key=lambda z:(z["x"],z["r_km"]))
    by_x={}
    for x in args.x_values:
        subset=[z for z in results if z["x"]==float(x)]
        by_x[str(float(x))]={
          "radial_points":len(subset),
          "all_quadrature_pass":all(z["quadrature_pass"] for z in subset),
          "maximum_final_order_change":max(z["final_change"] for z in subset),
          "maximum_detailed_balance_residual":max(z["detailed_balance_max"] for z in subset),
          "maximum_mass_shell_residual":max(z["mass_shell_max"] for z in subset),
          "all_rates_finite_nonnegative":all(z["finite_nonnegative"] for z in subset),
          "L_over_T_average_range":[min(z["L_over_T_average"] for z in subset if z["L_over_T_average"] is not None),max(z["L_over_T_average"] for z in subset if z["L_over_T_average"] is not None)],
          "maximum_plus_minus_relative_difference":max(z["plus_minus_relative_difference"] for z in subset)
        }
    summary={"run":"P1B-GLOBAL06B-FULL-RADIAL-POLARIZATION-SCAN","profile_sha256":PROFILE_SHA,
      "radial_nodes_in_profile":len(radii),"radial_nodes_scanned":len(scan_radii),"radial_stride":args.radial_stride,"x_values":[float(x) for x in args.x_values],
      "unique_r_x_points":len(tasks),"workers":args.workers,"runtime_seconds":time.time()-started,
      "order_ladder":[list(x) for x in ORDERS]+[list(EXTENSION)],
      "successive_order_tolerance":TOL,"by_x":by_x,
      "acceptance":{"all_points_pass":all(z["quadrature_pass"] for z in results),
        "all_rates_finite_nonnegative":all(z["finite_nonnegative"] for z in results),
        "full_1687_radius_coverage":bool(args.radial_stride==1 and len(scan_radii)==len(radii)),"full_nine_knot_energy_coverage":False,
        "complete_B1_source":False,"B2_transport":False},
      "scope":"B.13 moving-muon semi-Compton only; all radial vertices at three x anchors. Not the full low-x energy integral or B.2 transport."}
    args.output.mkdir(parents=True,exist_ok=True)
    (args.output/"RADIAL_POLARIZATION_POINTS.json").write_text(json.dumps(results,separators=(",",":"))+"\n",encoding="utf-8")
    (args.output/"RADIAL_POLARIZATION_SUMMARY.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":main()
