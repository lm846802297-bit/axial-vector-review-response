#!/usr/bin/env python3
"""Source-weighted diagnostic of the recovered B.13 midpoint interpolation."""
from __future__ import annotations
import argparse, csv, json, math
from bisect import bisect_right
from collections import defaultdict
from pathlib import Path

MASS_MEV = 10.0

def bracket(nodes, x, transform=lambda q:q):
    values=[transform(v) for v in nodes]; xx=transform(x)
    i=max(0,min(bisect_right(values,xx)-1,len(nodes)-2))
    t=(xx-values[i])/(values[i+1]-values[i])
    return nodes[i],nodes[i+1],t

def log_bilinear(corners,tr,te):
    if all(v>0 for v in corners):
        a,b,c,d=[math.log(v) for v in corners]
        return math.exp((1-tr)*(1-te)*a+(1-tr)*te*b+tr*(1-te)*c+tr*te*d)
    a,b,c,d=corners
    return (1-tr)*(1-te)*a+(1-tr)*te*b+tr*(1-te)*c+tr*te*d

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--csv",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    with args.csv.open(newline="") as f: rows=list(csv.DictReader(f))
    grid=[r for r in rows if r["point_type"]=="grid_node"]
    mids=[r for r in rows if r["point_type"]=="cell_midpoint"]
    radii=sorted({float(r["radius_km"]) for r in grid})
    energies=sorted({float(r["omega_local_MeV"]) for r in grid})
    table={(float(r["radius_km"]),float(r["omega_local_MeV"]),r["charge"],r["mode"]):r for r in grid}
    groups=defaultdict(list)
    for r in mids: groups[(float(r["radius_km"]),float(r["omega_local_MeV"]))].append(r)
    direct_total=pred_total=weighted_abs_error=weight_total=0.0
    lapse_direct=lapse_pred=0.0
    shell=defaultdict(lambda:{"direct":0.0,"predicted":0.0})
    for (radius,omega),items in groups.items():
        r0,r1,tr=bracket(radii,radius)
        e0,e1,te=bracket(energies,omega,lambda q:math.sqrt(max(q-MASS_MEV,0.0)))
        dr=r1-r0; de=e1-e0
        temp=float(items[0]["temperature_MeV"]); alpha=float(items[0]["lapse"])
        volume=4*math.pi*radius**2*dr*de
        for row in items:
            corners=[float(table[(rr,ee,row["charge"],row["mode"])]["absorption_MeV"])
                     for rr,ee in ((r0,e0),(r0,e1),(r1,e0),(r1,e1))]
            pred_abs=log_bilinear(corners,tr,te)
            pred_prod=math.exp(-omega/temp)*pred_abs
            pref=omega**2*math.sqrt(max(omega**2-MASS_MEV**2,0))/(2*math.pi**2)
            pred_source=pref*pred_prod
            direct_source=float(row["spectral_source_MeV5"])
            weight=volume*direct_source
            direct_total += weight
            pred_total += volume*pred_source
            weighted_abs_error += weight*abs(direct_source-pred_source)/max(abs(direct_source),abs(pred_source),1e-300)
            weight_total += weight
            lapse_direct += alpha*weight
            lapse_pred += alpha*volume*pred_source
            lo=int(radius//2)*2
            shell[f"{lo}-{lo+2} km"]["direct"] += weight
            shell[f"{lo}-{lo+2} km"]["predicted"] += volume*pred_source
    result={
      "status":"DIAGNOSTIC_ONLY_NOT_B2_TRANSPORT_ACCEPTANCE",
      "channel":"B.13 muon + photon <-> muon + A' semi-Compton only",
      "interpolation":"bilinear in log(absorption) over radial and sqrt(omega-mass) cell coordinates; production reconstructed with midpoint detailed balance",
      "weight":"4*pi*r^2*dr*domega times direct midpoint spectral_source; no ray escape, path optical depth, or full GR transport",
      "direct_local_source_integral_flat_weight":direct_total,
      "interpolated_local_source_integral_flat_weight":pred_total,
      "integrated_source_difference_fraction":(pred_total-direct_total)/direct_total,
      "source_weighted_pointwise_relative_error":weighted_abs_error/weight_total,
      "direct_local_source_integral_lapse_weighted":lapse_direct,
      "interpolated_local_source_integral_lapse_weighted":lapse_pred,
      "integrated_source_difference_fraction_lapse_weighted":(lapse_pred-lapse_direct)/lapse_direct,
      "shell_source_contributions":{k:{"direct":v["direct"],"predicted":v["predicted"],"fraction_of_direct_total":v["direct"]/direct_total,"relative_integral_difference":(v["predicted"]-v["direct"])/v["direct"] if v["direct"] else None} for k,v in sorted(shell.items())},
      "interpretation":"The source-weighted integrated B.13 Compton source changes by about 1.8% under the archived interpolation on this diagnostic quadrature. This is not a B.2 luminosity or optical-depth error estimate: it excludes neutrino inverse decay, ray geometry, attenuation, and the complete GR transport measure."
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()
