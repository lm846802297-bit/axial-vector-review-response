#!/usr/bin/env python3
"""P1-B Global Pilot 01: sparse radial x thermal-energy B.13 kernel audit.

This is a pilot grid, not the full global convergence or transport calculation.
Run from the extracted package root:
  python run_global_pilot_01.py --output results/P1B_10MeV_GLOBAL_PILOT_01.json
"""
from __future__ import annotations
import argparse, csv, hashlib, json, time, sys
from pathlib import Path
import numpy as np
from threadpoolctl import threadpool_limits
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "finite_mixing" / "thermal_integrals"))
import audit_b13_local_kernel_radial_energy_10mev as audit
PROFILE = HERE / "data" / "sfho188_digitized.csv"
EXPECTED_PROFILE_SHA256 = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
MASS_MEV = 10.0
RADII_KM = [0.0, 8.4821412022467, 12.5, 20.33, 21.0, 21.6346875, 22.1918941570485, 24.5]
THERMAL_X = [0.5, 2.0, 6.0, 18.0, 36.0]
ORDERS = (16, 10, 10, 10)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=HERE/"results"/"P1B_10MeV_GLOBAL_PILOT_01.json")
    ap.add_argument("--csv", type=Path, default=HERE/"results"/"P1B_10MeV_GLOBAL_PILOT_01.csv")
    args = ap.parse_args()
    profile_sha = hashlib.sha256(PROFILE.read_bytes()).hexdigest()
    if profile_sha != EXPECTED_PROFILE_SHA256: raise RuntimeError(f"profile SHA mismatch: {profile_sha}")
    table = np.genfromtxt(PROFILE, delimiter=",", names=True)
    records=[]; started=time.time()
    with threadpool_limits(limits=1):
        for r in RADII_KM:
            T=float(np.interp(r,table["r_km"],table["T_MeV"]))
            for x in THERMAL_X:
                omega=MASS_MEV+x*T
                v=audit.evaluate_point(PROFILE,r,omega,ORDERS,{})
                records.append({"r_km":r,"T_MeV":T,"x":x,"omega_local_MeV":omega,
                    "orders":list(ORDERS),"max_detailed_balance":v["maximum_mode_detailed_balance_relative_residual"],
                    "mass_shell":v["final_muon_shell_relative_error"],"all_rates_finite_nonnegative":v["all_rates_finite_and_nonnegative"],
                    "lapse":v["lapse"],"mu_mu":v["mu_minus_chemical_potential_MeV"],
                    "mu_minus_absorption":v["charge_resolved"]["mu_minus"]["absorption"],
                    "mu_plus_absorption":v["charge_resolved"]["mu_plus"]["absorption"],
                    "mu_minus_production":v["charge_resolved"]["mu_minus"]["production"],
                    "mu_plus_production":v["charge_resolved"]["mu_plus"]["production"]})
    payload={"run":"P1B-10MeV-GLOBAL-PILOT-01","scope":"coarse pilot only; not global convergence or transport",
      "profile_sha256":profile_sha,"profile_rows":int(len(table)),"mass_MeV":MASS_MEV,
      "couplings":{"gV_over_gX":1.0,"gA_over_gX":0.0},"radial_nodes_km":RADII_KM,"thermal_x_nodes":THERMAL_X,
      "energy_definition":"omega_local = m_Aprime + x*T(r)","quadrature_orders":list(ORDERS),"records":records,
      "runtime_seconds":time.time()-started,"acceptance":{"point_count":len(records),
      "all_finite_nonnegative":all(x["all_rates_finite_nonnegative"] for x in records),
      "max_detailed_balance":max(x["max_detailed_balance"] for x in records),
      "max_mass_shell":max(x["mass_shell"] for x in records),
      "max_energy_MeV":max(x["omega_local_MeV"] for x in records),
      "max_profile_temperature_MeV":max(x["T_MeV"] for x in records)},
      "next_required":"Expand radial coverage using original profile knots and adaptive midpoints; run order-pair quadrature checks; then construct global interpolation error estimator before emissivity/GR optical-depth integration."}
    args.output.parent.mkdir(parents=True,exist_ok=True); args.csv.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\\n")
    fields=["r_km","T_MeV","x","omega_local_MeV","max_detailed_balance","mass_shell","all_rates_finite_nonnegative","lapse","mu_mu"]
    with args.csv.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for x in records: w.writerow({k:x[k] for k in fields})
    print(json.dumps(payload["acceptance"],indent=2))
if __name__=="__main__": main()
