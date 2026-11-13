#!/usr/bin/env python3
"""Post-process complete P1-B E1 full-radial scan.

Checks complete radial/energy coverage, compares the original 5-knot energy
interpolant with the one-bisection 9-knot PCHIP interpolant, and ranks all
1686 adjacent radial intervals by their direct-neighbor variation proxy.
This script does not call the collision kernel; it only analyzes archived data.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from pathlib import Path
import numpy as np
from scipy.interpolate import PchipInterpolator

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for p in (ROOT,HERE):
    if str(p) not in sys.path: sys.path.insert(0,str(p))
import audit_b13_local_kernel_radial_energy_10mev as audit

PROFILE=ROOT/"data"/"sfho188_digitized.csv"
EXPECTED_PROFILE_SHA256="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
SCAN_SCRIPT=HERE/"run_p1b_e1_global_energy_scan.py"
BASE_X=np.asarray([0.5,2.0,6.0,18.0,36.0],float)

def bisect_sqrt_x(nodes):
    return np.asarray(sorted(set(nodes.tolist()+[(0.5*(math.sqrt(a)+math.sqrt(b)))**2 for a,b in zip(nodes[:-1],nodes[1:])])),float)

def rel(a,b):
    a=float(a);b=float(b)
    return abs(a-b)/max(abs(a),abs(b),1e-300)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input-dir",type=Path,required=True); ap.add_argument("--output-dir",type=Path,required=True)
    ap.add_argument("--top-n",type=int,default=60)
    args=ap.parse_args(); args.output_dir.mkdir(parents=True,exist_ok=True)
    profile_sha=hashlib.sha256(PROFILE.read_bytes()).hexdigest(); source_sha=hashlib.sha256(SCAN_SCRIPT.read_bytes()).hexdigest()
    if profile_sha!=EXPECTED_PROFILE_SHA256: raise RuntimeError("profile SHA mismatch")
    chunks={}
    for f in sorted(args.input_dir.glob("chunk_*.json")):
        d=json.loads(f.read_text())
        if d.get("profile_sha256")==profile_sha and d.get("source_sha256")==source_sha:
            chunks[int(d["chunk_index"])]=d
    if len(chunks)!=1687: raise RuntimeError(f"Expected 1687 verified chunks, found {len(chunks)}")
    if sorted(chunks)!=list(range(1687)): raise RuntimeError("Chunk indices are incomplete or duplicated")
    table=np.genfromtxt(PROFILE,delimiter=",",names=True); radii=np.asarray(table["r_km"],float)
    coarse_x=bisect_sqrt_x(BASE_X); validation=bisect_sqrt_x(coarse_x)
    old_mid=np.asarray([x for x in coarse_x if not np.any(np.isclose(x,BASE_X,rtol=0,atol=1e-13))])
    new_mid=np.asarray([x for x in validation if not np.any(np.isclose(x,coarse_x,rtol=0,atol=1e-13))])
    node_records={}; node_energy=[]; max_db=0.;max_shell=0.;all_finite=True
    for idx in range(1687):
        d=chunks[idx]; recs=d["records"]
        if len(recs)!=17: raise RuntimeError(f"radial index {idx}: expected 17 energy records, got {len(recs)}")
        points={float(r["x"]):r for r in recs}
        if len(points)!=17 or any(float(x) not in points for x in validation): raise RuntimeError(f"radial index {idx}: energy coverage mismatch")
        node_records[idx]=points
        for r in recs:
            max_db=max(max_db,float(r["maximum_mode_detailed_balance_relative_residual"]))
            max_shell=max(max_shell,float(r["final_muon_shell_relative_error"]))
            all_finite=all_finite and bool(r["all_rates_finite_and_nonnegative"])
        errs_old=[];errs_new=[]
        for charge in audit.CHARGES:
            old_values=np.asarray([points[float(x)]["charge_resolved"][charge]["absorption"] for x in BASE_X],float)
            old_interps=[PchipInterpolator(np.sqrt(BASE_X),np.log(np.maximum(old_values[:,j],1e-300))) for j in range(3)]
            new_values=np.asarray([points[float(x)]["charge_resolved"][charge]["absorption"] for x in coarse_x],float)
            new_interps=[PchipInterpolator(np.sqrt(coarse_x),np.log(np.maximum(new_values[:,j],1e-300))) for j in range(3)]
            for x in old_mid:
                direct=np.asarray(points[float(x)]["charge_resolved"][charge]["absorption"],float)
                for j,mode in enumerate(audit.MODES):
                    pred=float(np.exp(old_interps[j](math.sqrt(float(x)))))
                    errs_old.append({"x_mid":float(x),"charge":charge,"mode":mode,"relative_error":rel(direct[j],pred)})
            for x in new_mid:
                direct=np.asarray(points[float(x)]["charge_resolved"][charge]["absorption"],float)
                for j,mode in enumerate(audit.MODES):
                    pred=float(np.exp(new_interps[j](math.sqrt(float(x)))))
                    errs_new.append({"x_mid":float(x),"charge":charge,"mode":mode,"relative_error":rel(direct[j],pred)})
        wold=max(errs_old,key=lambda z:z["relative_error"]); wnew=max(errs_new,key=lambda z:z["relative_error"])
        node_energy.append({"radial_index":idx,"radius_km":float(radii[idx]),"old_5knot_max_error":wold["relative_error"],"old_worst":wold,
          "refined_9knot_max_error":wnew["relative_error"],"refined_worst":wnew})
    radial_intervals=[]
    fields=("absorption","production")
    for i in range(1686):
        p0=node_records[i];p1=node_records[i+1];best=None;max_abs=0.0
        for x in validation:
            for charge in audit.CHARGES:
                for field in fields:
                    a=np.asarray(p0[float(x)]["charge_resolved"][charge][field],float)
                    b=np.asarray(p1[float(x)]["charge_resolved"][charge][field],float)
                    for j,mode in enumerate(audit.MODES):
                        e=rel(a[j],b[j]); ad=abs(float(a[j]-b[j]))
                        if best is None or e>best["relative_change"]:
                            best={"x":float(x),"charge":charge,"field":field,"mode":mode,"left_value":float(a[j]),"right_value":float(b[j]),"relative_change":e,"absolute_change":ad}
                        max_abs=max(max_abs,ad)
        radial_intervals.append({"left_radial_index":i,"right_radial_index":i+1,"r_left_km":float(radii[i]),"r_right_km":float(radii[i+1]),
          "dr_km":float(radii[i+1]-radii[i]),"maximum_neighbor_relative_change":best["relative_change"],"worst_channel":best,"maximum_absolute_change":max_abs})
    radial_intervals.sort(key=lambda z:z["maximum_neighbor_relative_change"],reverse=True)
    old=np.asarray([z["old_5knot_max_error"] for z in node_energy]);new=np.asarray([z["refined_9knot_max_error"] for z in node_energy])
    max_old=max(node_energy,key=lambda z:z["old_5knot_max_error"]);max_new=max(node_energy,key=lambda z:z["refined_9knot_max_error"])
    summary={"run":"P1B-E1-GLOBAL-POSTPROCESS","profile_sha256":profile_sha,"scan_source_sha256":source_sha,"radial_nodes":1687,"energy_nodes_per_radius":17,
      "direct_b13_evaluations":1687*17,"base_energy_knots_x":BASE_X.tolist(),"one_bisection_energy_knots_x":coarse_x.tolist(),
      "old_5knot_pchip":{"median_max_error":float(np.median(old)),"p95_max_error":float(np.quantile(old,.95)),"maximum_error":float(old.max()),
        "radial_nodes_over_1pct":int(np.sum(old>=.01)),"worst_node":max_old},
      "refined_9knot_pchip":{"median_max_error":float(np.median(new)),"p95_max_error":float(np.quantile(new,.95)),"maximum_error":float(new.max()),
        "radial_nodes_over_1pct":int(np.sum(new>=.01)),"worst_node":max_new,"all_radial_nodes_pass_1pct":bool(new.max()<.01)},
      "maximum_detailed_balance_residual":max_db,"maximum_final_muon_mass_shell_residual":max_shell,"all_rates_finite_nonnegative":bool(all_finite),
      "top_radial_neighbor_intervals":radial_intervals[:args.top_n],"radial_neighbor_intervals_total":len(radial_intervals),
      "quadrature_acceptance":"low-order global scan only; high-order checks remain a separate stage","full_star_transport_claimed":False}
    (args.output_dir/"GLOBAL_ENERGY_AND_RADIAL_SUMMARY.json").write_text(json.dumps(summary,indent=2)+"\n")
    with (args.output_dir/"RADIAL_NODE_ENERGY_ERRORS.csv").open("w") as f:
        f.write("radial_index,radius_km,old_5knot_max_error,refined_9knot_max_error,old_worst_x,old_worst_charge,old_worst_mode,refined_worst_x,refined_worst_charge,refined_worst_mode\n")
        for z in node_energy:
            a=z["old_worst"];b=z["refined_worst"]
            f.write(f"{z['radial_index']},{z['radius_km']:.12g},{z['old_5knot_max_error']:.12g},{z['refined_9knot_max_error']:.12g},{a['x_mid']},{a['charge']},{a['mode']},{b['x_mid']},{b['charge']},{b['mode']}\n")
    (args.output_dir/"TOP60_RADIAL_NEIGHBOR_INTERVALS.json").write_text(json.dumps(radial_intervals[:args.top_n],indent=2)+"\n")
    print(json.dumps({k:v for k,v in summary.items() if k!="top_radial_neighbor_intervals"},indent=2))

if __name__=="__main__":main()
