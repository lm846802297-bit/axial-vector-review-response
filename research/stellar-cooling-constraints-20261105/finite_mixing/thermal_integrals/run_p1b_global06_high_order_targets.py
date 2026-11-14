#!/usr/bin/env python3
"""Targeted high-order convergence checks for Global-06 low-x B.13 data."""
from __future__ import annotations
import argparse, hashlib, json, math, sys, time
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
PROFILE=ROOT/"data"/"sfho188_digitized.csv"
PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
MASS_MEV=10.0
X_GRID=np.asarray([0.05,0.07285533905932738,0.1,0.14571067811865476,
                   0.2,0.2697875655532295,0.35,0.4216650066335189,0.5])
X_VALIDATION=np.asarray([0.060891504294495524,0.08589150429449552,
                         0.12178300858899109,0.17178300858899104,
                         0.23359067416492213,0.3085906741649221,
                         0.3849987549751391,0.4599987549751393])
ORDERS=((10,6,6,6),(14,8,8,8),(18,10,10,10),(22,12,12,12),(26,14,14,14))
EXTENSION=(30,16,16,16)
TOL=1.0e-3

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--global06-dir",type=Path,default=HERE/"results"/"P1B_GLOBAL06_LOW_X_FULL_RADIAL_2026-11-14")
    ap.add_argument("--top-radial",type=int,default=10)
    ap.add_argument("--top-energy",type=int,default=10)
    ap.add_argument("--output",type=Path,default=None)
    args=ap.parse_args()
    started=time.time()
    if sha(PROFILE)!=PROFILE_SHA:raise RuntimeError("profile SHA mismatch")
    if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
    if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
    import audit_b13_local_kernel_radial_energy_10mev as audit
    table=np.genfromtxt(PROFILE,delimiter=",",names=True)
    radii=np.asarray(table["r_km"],float)
    def fast_load(_path,rr):
        rr=np.asarray(rr,float)
        return {n:np.interp(rr,radii,np.asarray(table[c],float)) for n,c in
            {"T":"T_MeV","mu_mu":"mu_mu_MeV","mu_numu":"mu_numu_MeV","lapse":"lapse"}.items()}
    audit.load_profile=fast_load
    cache={}
    summary=json.loads((args.global06_dir/"GLOBAL06_SUMMARY.json").read_text())
    radial=json.loads((args.global06_dir/"RADIAL_NEIGHBOR_RANKING_TOP60.json").read_text())
    energy=json.loads((args.global06_dir/"ENERGY_INTERPOLATION_CHECKS.json").read_text())
    radial_targets=radial[:args.top_radial]
    energy_targets=sorted(energy,key=lambda z:z["maximum_channel_relative_error"],reverse=True)[:args.top_energy]

    def evaluate(r,x):
        t=float(np.interp(r,radii,np.asarray(table["T_MeV"],float)))
        omega=MASS_MEV+x*t
        ladder=[audit.evaluate_point(PROFILE,r,omega,o,cache) for o in ORDERS]
        changes=[audit.compare_points(ladder[i-1],ladder[i])["maximum_relative_change"] for i in range(1,len(ladder))]
        if changes[-1]>=TOL:
            ladder.append(audit.evaluate_point(PROFILE,r,omega,EXTENSION,cache))
            changes.append(audit.compare_points(ladder[-2],ladder[-1])["maximum_relative_change"])
        return {"r_km":float(r),"x":float(x),"omega_local_MeV":float(omega),
            "orders":[v["orders"] for v in ladder],"successive_changes":changes,
            "final_change":changes[-1],"quadrature_pass":bool(changes[-1]<TOL),
            "detailed_balance_max":max(v["maximum_mode_detailed_balance_relative_residual"] for v in ladder),
            "mass_shell_max":max(v["final_muon_shell_relative_error"] for v in ladder),
            "finite_nonnegative":all(v["all_rates_finite_and_nonnegative"] for v in ladder),
            "final_payload":ladder[-1]}

    radial_results=[]
    for rank,item in enumerate(radial_targets,1):
        i=int(item["left_index"])
        r0=float(radii[i]);r1=float(radii[i+1]);rm=0.5*(r0+r1)
        points=[]
        by_r={}
        for r in (r0,rm,r1):
            by_r[r]={}
            for x in X_GRID:
                p=evaluate(r,float(x));points.append(p);by_r[r][float(x)]=p
        radial_interp_errors=[]
        for x in X_GRID:
            left=by_r[r0][float(x)]["final_payload"]
            mid=by_r[rm][float(x)]["final_payload"]
            right=by_r[r1][float(x)]["final_payload"]
            channel={}
            for q in ("mu_minus","mu_plus"):
                channel[q]={}
                for imode,mode in enumerate(("L","+","-")):
                    a=left["charge_resolved"][q]["absorption"][imode]
                    b=right["charge_resolved"][q]["absorption"][imode]
                    pred=math.exp(0.5*(math.log(a)+math.log(b))) if a>0 and b>0 else 0.5*(a+b)
                    truth=mid["charge_resolved"][q]["absorption"][imode]
                    channel[q][mode]=abs(pred-truth)/max(abs(pred),abs(truth),1.0e-300)
            radial_interp_errors.append({"x":float(x),"maximum_channel_error":max(v for q in channel.values() for v in q.values()),"channel_errors":channel})
        radial_results.append({"rank":rank,"interval_index":i,"r_left_km":r0,
            "r_mid_km":rm,"r_right_km":r1,"points":points,
            "maximum_high_order_midpoint_interpolation_error":max(z["maximum_channel_error"] for z in radial_interp_errors),
            "radial_interpolation_checks":radial_interp_errors,
            "all_quadrature_pass":all(p["quadrature_pass"] for p in points)})

    energy_results=[]
    for rank,item in enumerate(energy_targets,1):
        r=float(item["r_km"]);x=float(item["x_validation"])
        grid_points=[evaluate(r,float(xx)) for xx in X_GRID]
        validation_points=[evaluate(r,float(xx)) for xx in X_VALIDATION]
        validation_index=int(np.argmin(np.abs(X_VALIDATION-x)))
        direct=validation_points[validation_index]
        channel_errors={}
        for q in ("mu_minus","mu_plus"):
            channel_errors[q]={}
            for imode,mode in enumerate(("L","+","-")):
                y=[p["final_payload"]["charge_resolved"][q]["absorption"][imode] for p in grid_points]
                if min(y)>0:
                    pred=float(np.exp(PchipInterpolator(np.sqrt(X_GRID),np.log(y))(math.sqrt(x))))
                else:
                    pred=max(float(PchipInterpolator(np.sqrt(X_GRID),y)(math.sqrt(x))),0.0)
                truth=direct["final_payload"]["charge_resolved"][q]["absorption"][imode]
                channel_errors[q][mode]=abs(pred-truth)/max(abs(pred),abs(truth),1.0e-300)
        energy_ladders=grid_points+validation_points
        energy_results.append({"rank":rank,"radial_index":int(item["radial_index"]),
            "direct_low_order_error":float(item["maximum_channel_relative_error"]),
            "high_order_validation":direct,
            "high_order_pchip_error":max(v for q in channel_errors.values() for v in q.values()),
            "high_order_pchip_channel_errors":channel_errors,
            "maximum_detailed_balance_residual":max(p["detailed_balance_max"] for p in energy_ladders),
            "maximum_mass_shell_residual":max(p["mass_shell_max"] for p in energy_ladders),
            "all_rates_finite_nonnegative":all(p["finite_nonnegative"] for p in energy_ladders),
            "maximum_final_order_change":max(p["final_change"] for p in energy_ladders),
            "all_grid_and_validation_quadrature_pass":all(p["quadrature_pass"] for p in energy_ladders)})

    all_points=[p for group in radial_results for p in group["points"]]+[
        item["high_order_validation"] for item in energy_results]
    result={
      "run":"P1B-GLOBAL-06-HIGH-ORDER-TARGETS",
      "profile_sha256":PROFILE_SHA,
      "source_global06_summary":summary,
      "orders_ladder":[list(x) for x in ORDERS]+[list(EXTENSION)],
      "criterion_successive_order_change_below":TOL,
      "radial_target_intervals":len(radial_results),
      "energy_target_points":len(energy_results),
      "radial_results":radial_results,
      "energy_results":energy_results,
      "acceptance":{
        "all_targeted_quadrature_pass":all(p["quadrature_pass"] for p in all_points) and all(x["all_grid_and_validation_quadrature_pass"] for x in energy_results),
        "maximum_high_order_radial_midpoint_interpolation_error":max(x["maximum_high_order_midpoint_interpolation_error"] for x in radial_results),
        "maximum_high_order_energy_pchip_error":max(x["high_order_pchip_error"] for x in energy_results),
        "maximum_final_successive_order_change":max(
            [p["final_change"] for p in all_points]+[x["maximum_final_order_change"] for x in energy_results]),
        "maximum_detailed_balance_residual":max(
            [p["detailed_balance_max"] for p in all_points]+[x["maximum_detailed_balance_residual"] for x in energy_results]),
        "maximum_mass_shell_residual":max(
            [p["mass_shell_max"] for p in all_points]+[x["maximum_mass_shell_residual"] for x in energy_results]),
        "all_rates_finite_nonnegative":all(p["finite_nonnegative"] for p in all_points) and all(x["all_rates_finite_nonnegative"] for x in energy_results),
        "full_global_high_order_acceptance":False
      },
      "runtime_seconds":time.time()-started,
      "scope":"Selected worst energy interpolation points and top radial-variation intervals only; not exhaustive high-order validation."
    }
    out=args.output or args.global06_dir/"HIGH_ORDER_TARGETED_SUMMARY.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result["acceptance"],indent=2))
    print(f"Saved {out}")

if __name__=="__main__":main()
