#!/usr/bin/env python3
"""Validate the full-radial Global-06B B.13 polarization scan output."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np

EXPECTED_PROFILE_SHA="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
EXPECTED_X=(0.0,0.015,0.05)
DB_TOL=2e-10
SHELL_TOL=2e-10
QUAD_TOL=1e-3
TRANSVERSE_TOL=1e-12
THRESHOLD_ISOTROPY_TOL=1e-3

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("directory",type=Path)
    args=ap.parse_args()
    summary=json.loads((args.directory/"RADIAL_POLARIZATION_SUMMARY.json").read_text())
    points=json.loads((args.directory/"RADIAL_POLARIZATION_POINTS.json").read_text())
    if summary["profile_sha256"]!=EXPECTED_PROFILE_SHA:raise SystemExit("FAIL: profile SHA mismatch")
    if summary["radial_nodes_in_profile"]!=1687:raise SystemExit("FAIL: expected 1687 profile nodes")
    if summary["radial_stride"]!=1 or not summary["acceptance"]["full_1687_radius_coverage"]:
        raise SystemExit("FAIL: scan is not full radial coverage")
    if tuple(summary["x_values"])!=EXPECTED_X:raise SystemExit("FAIL: unexpected x anchors")
    if len(points)!=1687*len(EXPECTED_X):raise SystemExit("FAIL: point count mismatch")
    by_x={x:sorted([p for p in points if p["x"]==x],key=lambda p:p["r_km"]) for x in EXPECTED_X}
    reference_r=np.asarray([p["r_km"] for p in by_x[0.0]],float)
    for x,group in by_x.items():
        if len(group)!=1687:raise SystemExit(f"FAIL: x={x} has {len(group)} radial points")
        radii=np.asarray([p["r_km"] for p in group],float)
        if not np.array_equal(radii,reference_r):raise SystemExit(f"FAIL: radial grid differs at x={x}")
    charge_closure=0.0
    mode_fraction_closure=0.0
    for point in points:
        total_abs=np.asarray(point["absorption_modes"],float)
        charge_abs=sum(np.asarray(point["charge_resolved_absorption"][q],float) for q in ("mu_minus","mu_plus"))
        charge_closure=max(charge_closure,float(np.max(np.abs(total_abs-charge_abs)/np.maximum(np.abs(total_abs),1e-300))))
        mode_fraction_closure=max(mode_fraction_closure,abs(float(sum(point["mode_fractions"]))-1.0))
    if charge_closure>=1e-12:raise SystemExit(f"FAIL: charge-sum closure max={charge_closure:.6e}")
    if mode_fraction_closure>=1e-12:raise SystemExit(f"FAIL: mode-fraction closure max={mode_fraction_closure:.6e}")
    max_quad=max(p["final_change"] for p in points)
    max_db=max(p["detailed_balance_max"] for p in points)
    max_shell=max(p["mass_shell_max"] for p in points)
    max_pm=max(p["plus_minus_relative_difference"] for p in points)
    if not all(p["quadrature_pass"] for p in points) or max_quad>=QUAD_TOL:
        raise SystemExit(f"FAIL: quadrature convergence max={max_quad:.6e}")
    if max_db>=DB_TOL:raise SystemExit(f"FAIL: detailed balance max={max_db:.6e}")
    if max_shell>=SHELL_TOL:raise SystemExit(f"FAIL: mass shell max={max_shell:.6e}")
    if max_pm>=TRANSVERSE_TOL:raise SystemExit(f"FAIL: transverse equality max={max_pm:.6e}")
    threshold=np.asarray([p["L_over_T_average"] for p in by_x[0.0]],float)
    threshold_dev=float(np.max(np.abs(threshold-1.0)))
    if threshold_dev>=THRESHOLD_ISOTROPY_TOL:
        raise SystemExit(f"FAIL: threshold isotropy max deviation={threshold_dev:.6e}")
    ratio_ranges={}
    for x,group in by_x.items():
        ratios=np.asarray([p["L_over_T_average"] for p in group],float)
        ratio_ranges[str(x)]={"min":float(np.min(ratios)),"max":float(np.max(ratios))}
    # Compare energy ordering at identical radial vertices. This is reported,
    # not imposed as a hard pass condition, because non-monotone local inputs
    # must remain visible rather than being hidden by a blanket assertion.
    ordering_violations=0
    for i in range(1687):
        ratios=[by_x[x][i]["L_over_T_average"] for x in EXPECTED_X]
        if not (ratios[0]>=ratios[1]>=ratios[2]):ordering_violations+=1
    result={"validation":"PASS","radial_nodes":1687,"x_anchors":list(EXPECTED_X),
      "points":len(points),"maximum_quadrature_change":max_quad,
      "maximum_detailed_balance_residual":max_db,"maximum_mass_shell_residual":max_shell,
      "maximum_transverse_plus_minus_difference":max_pm,\n      "maximum_charge_sum_closure_residual":charge_closure,\n      "maximum_mode_fraction_closure_residual":mode_fraction_closure,
      "maximum_threshold_isotropy_deviation":threshold_dev,
      "L_over_T_ranges":ratio_ranges,"nonmonotone_energy_ordering_radii":ordering_violations}
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
