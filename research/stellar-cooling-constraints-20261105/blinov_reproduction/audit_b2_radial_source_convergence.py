#!/usr/bin/env python3
"""High-order B.2 radial-source quadrature convergence at 0.1 and 1 MeV.

Only the B.1 source radial Gauss order is varied. The B.2 opacity interpolation
grid and the energy grid are held fixed independently of the source nodes.
Angular and path quadratures are also fixed. Both literal fixed-omega and
path-redshift-only diagnostics use the same profile and coupling grid.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from blinov_reproduction.audit_b16_global_redshift import (
    DEFAULT_FIG7, DEFAULT_PROFILE, run_mass,
)

ORDERS=(80,100,120,160,200)

def summarize(x):
    fixed=x["eq_b2_fixed_omega_baseline"]["points"]
    red=x["path_redshift_only_diagnostic"]["points"]
    ref=np.asarray([p["reference_luminosity_erg_s"] for p in fixed])
    lf=np.asarray([p["calculated_luminosity_erg_s"] for p in fixed])
    lr=np.asarray([p["calculated_luminosity_erg_s"] for p in red])
    thin=np.asarray([p["optically_thin_luminosity_erg_s"] for p in fixed])
    peak=int(np.argmax(ref))
    def delta(a,b):
        d=np.asarray(b)/np.asarray(a)-1
        return {"max_abs_pct":float(np.max(np.abs(d))*100),
                "peak_pct":float(d[peak]*100),
                "strong_pct":float(d[-1]*100),
                "weak_pct":float(d[0]*100)}
    return {
      "radial_order":x["configuration"]["radial_order"],
      "opacity_order":x["configuration"]["opacity_order"],
      "actual_radial_node_count":len(x["eq_b1_source_measure"]["radial_measure_MeVminus3"]),
      "source_grid_mode":x["configuration"]["source_grid_mode"],
      "source_grid_sha256":x["configuration"]["source_grid_sha256"],
      "opacity_grid_node_count":x["configuration"]["opacity_radial_node_count"],
      "opacity_grid_sha256":x["configuration"]["opacity_grid_sha256"],
      "energy_node_count":x["configuration"]["energy_node_count"],
      "energy_grid_sha256":x["configuration"]["energy_grid_sha256"],
      "thin_luminosity_erg_s_at_first_coupling":float(thin[0]),
      "fixed_vs_fig7":x["eq_b2_fixed_omega_baseline"]["curve_metrics"],
      "redshifted_vs_fig7":x["path_redshift_only_diagnostic"]["curve_metrics"],
      "source_mean_radius_km":x["source_radial_distribution"]["mean_emission_radius_km"],
      "source_shell_fractions":x["source_radial_distribution"]["shell_fractions"],
      "fixed_luminosity":lf.tolist(),
      "redshifted_luminosity":lr.tolist(),
      "redshift_shift_vs_fixed":delta(lf,lr),
      "luminosity_vs_previous_order":None,
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mass",type=float,required=True)
    p.add_argument("--orders",default="80,100,120,160,200")
    p.add_argument("--profile",type=Path,default=DEFAULT_PROFILE)
    p.add_argument("--fig7",type=Path,default=DEFAULT_FIG7)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    expected="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
    ph=hashlib.sha256(a.profile.read_bytes()).hexdigest()
    if ph!=expected: raise RuntimeError(f"profile hash mismatch: {ph}")
    orders=[int(x) for x in a.orders.split(",")]
    rows=[]
    for n in orders:
      print(f"Running B.2 radial order {n}, m={a.mass:g} MeV",flush=True)
      raw=run_mass(
        a.mass,a.profile,a.fig7,n,100,16,32,25.0,1000.0,
        opacity_order=640,separate_source_grid=True
      )
      rows.append(summarize(raw))
    for i in range(1,len(rows)):
      prev,cur=rows[i-1],rows[i]
      cur["luminosity_vs_previous_order"]={
       "fixed": {
        "max_abs_pct":float(np.max(np.abs(np.asarray(cur["fixed_luminosity"])/np.asarray(prev["fixed_luminosity"])-1))*100),
        "peak_pct":float((cur["fixed_luminosity"][int(np.argmax([p["reference_luminosity_erg_s"] for p in raw["eq_b2_fixed_omega_baseline"]["points"]]))]/prev["fixed_luminosity"][int(np.argmax([p["reference_luminosity_erg_s"] for p in raw["eq_b2_fixed_omega_baseline"]["points"]]))]-1)*100),
        "strong_pct":float((cur["fixed_luminosity"][-1]/prev["fixed_luminosity"][-1]-1)*100)},
       "redshifted": {
        "max_abs_pct":float(np.max(np.abs(np.asarray(cur["redshifted_luminosity"])/np.asarray(prev["redshifted_luminosity"])-1))*100),
        "strong_pct":float((cur["redshifted_luminosity"][-1]/prev["redshifted_luminosity"][-1]-1)*100)}
      }
    fixed_keys=("opacity_grid_node_count","opacity_grid_sha256",
                 "energy_node_count","energy_grid_sha256")
    for key in fixed_keys:
      if len({row[key] for row in rows}) != 1:
        raise ArithmeticError(f"{key} changed while only the source radial order was varied")
    if any(row["source_grid_mode"] != "independent" for row in rows):
      raise ArithmeticError("The source radial grid is not independent of opacity")
    if len({row["source_grid_sha256"] for row in rows}) != len(rows):
      raise ArithmeticError("The source radial grid did not change across the order ladder")

    grid_isolation={
      "source_radial_grid_varied":True,
      "opacity_grid_fixed":True,
      "energy_grid_fixed":True,
      "opacity_grid_node_count":rows[0]["opacity_grid_node_count"],
      "opacity_grid_sha256":rows[0]["opacity_grid_sha256"],
      "energy_node_count":rows[0]["energy_node_count"],
      "energy_grid_sha256":rows[0]["energy_grid_sha256"],
      "source_grid_sha256_by_order":{
        str(row["radial_order"]):row["source_grid_sha256"] for row in rows
      },
    }
    out={"date":"2026-11-09","mass_MeV":a.mass,"profile_sha256":ph,
         "fixed_quadratures":{"energy_order":100,"angular_order":16,"path_order":32,"opacity_order":640},
         "grid_isolation":grid_isolation,
         "radial_orders":rows,
         "acceptance_target":{"max_abs_luminosity_change_pct":1.0,
           "note":"Project numerical screening target; not a physical uncertainty."}}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"mass_MeV":a.mass,"grid_isolation":grid_isolation,
      "orders":[
        {"radial_order":r["radial_order"],
         "source_nodes":r["actual_radial_node_count"],
         "opacity_nodes":r["opacity_grid_node_count"],
         "energy_nodes":r["energy_node_count"],
         "change":r["luminosity_vs_previous_order"]}
        for r in rows]},indent=2),flush=True)
if __name__=="__main__": main()
