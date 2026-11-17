#!/usr/bin/env python3
"""Recompute B.13 source fractions from the recovered 10 MeV JSON artifact.

Separates the historical flat local-source proxy from an Eq. (B.1)-motivated
midpoint measure containing lapse^2 and omega_local >= m/N(r). Neither is a
B.2 escaped luminosity; the midpoint rule is diagnostic, not the production
radial Gauss / piecewise-linear energy integration.
"""
from __future__ import annotations
import argparse, hashlib, json, math
from collections import defaultdict
from pathlib import Path

PROFILE_SHA = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
CHARGES = ("mu_minus", "mu_plus")
MODES = ("L", "+", "-")
FOUR_PI = 4.0 * math.pi
NAMES = (
    "flat_local_no_lapse_no_threshold",
    "eq_b1_midpoint_lapse_no_threshold",
    "eq_b1_midpoint_lapse_midpoint_threshold",
    "eq_b1_midpoint_lapse_fractional_threshold",
)

def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def fractions(values):
    total = sum(values.values())
    if total <= 0:
        raise ValueError("non-positive source integral")
    return {k: {"integral": float(v), "fraction": float(v / total)}
            for k, v in sorted(values.items())}

def calculate(archive):
    grid = archive["grid"]
    rnodes = list(map(float, grid["radii_km"]))
    enodes = list(map(float, grid["omega_local_MeV"]))
    mass = float(archive["physics_scope"]["mediator_mass_MeV"])
    rows = archive["radial_energy_midpoint_results"]
    ne = len(enodes) - 1
    if len(rows) != (len(rnodes)-1)*ne:
        raise ValueError("midpoint count does not match the archived grid")

    cm = {n: defaultdict(float) for n in NAMES}
    shells = {n: defaultdict(float) for n in NAMES}
    closure = transverse = 0.0
    lapse_range = [math.inf, 0.0]
    threshold_range = [math.inf, 0.0]

    for index, row in enumerate(rows):
        ir, ie = divmod(index, ne)
        r0, r1 = rnodes[ir:ir+2]
        e0, e1 = enodes[ie:ie+2]
        r = 0.5*(r0+r1)
        y = 0.5*(math.sqrt(max(e0-mass, 0.0))+math.sqrt(max(e1-mass, 0.0)))
        omega = mass+y*y
        if abs(row["radius_midpoint_km"]-r) > 2e-10*max(1.0,abs(r)):
            raise ValueError(f"radial midpoint mismatch at row {index}")
        if abs(row["omega_midpoint_MeV"]-omega) > 2e-10*max(1.0,abs(omega)):
            raise ValueError(f"energy midpoint mismatch at row {index}")

        p = row["order_ladder"][-1]
        if p["mode_order"] != list(MODES) or p["orders"] != row["final_order"]:
            raise ValueError(f"mode/order mismatch at row {index}")
        lapse = float(p["lapse"])
        threshold = mass/lapse
        lapse_range = [min(lapse_range[0],lapse),max(lapse_range[1],lapse)]
        threshold_range = [min(threshold_range[0],threshold),max(threshold_range[1],threshold)]

        dr, de = r1-r0, e1-e0
        w0 = FOUR_PI*r*r*dr*de
        w1 = w0*lapse*lapse
        w2 = w1 if omega >= threshold else 0.0
        w3 = FOUR_PI*r*r*lapse*lapse*dr*max(0.0,e1-max(e0,threshold))
        weights = (w0,w1,w2,w3)
        source = {q:p["charge_resolved"][q]["spectral_source"] for q in CHARGES}
        mode_sums = [sum(float(source[q][i]) for q in CHARGES) for i in range(3)]
        for a,b in zip(mode_sums,p["total_spectral_source_by_mode"]):
            closure=max(closure,abs(a-b)/max(abs(a),abs(b),1e-300))
        transverse=max(transverse,abs(mode_sums[1]-mode_sums[2])/max(mode_sums[1],mode_sums[2],1e-300))
        shell=f"{2*int(r//2)}-{2*int(r//2)+2} km"
        for j,name in enumerate(NAMES):
            for q in CHARGES:
                for i,mode in enumerate(MODES):
                    cm[name][f"{q}/{mode}"] += weights[j]*float(source[q][i])
            shells[name][shell] += weights[j]*sum(mode_sums)

    result={}
    for name in NAMES:
        c=cm[name]
        charge={q:sum(v for k,v in c.items() if k.startswith(q+"/")) for q in CHARGES}
        mode={m:sum(v for k,v in c.items() if k.endswith("/"+m)) for m in MODES}
        total=sum(c.values())
        result[name]={
            "integral_internal_units":float(total),
            "charge_mode_contributions":fractions(dict(c)),
            "charge_contributions":fractions(charge),
            "mode_contributions":fractions(mode),
            "radial_shell_contributions":fractions(dict(shells[name])),
            "8_12_km_fraction":float((shells[name].get("8-10 km",0)+shells[name].get("10-12 km",0))/total),
        }
    flat=result[NAMES[0]]["integral_internal_units"]
    lapse=result[NAMES[1]]["integral_internal_units"]
    mid=result[NAMES[2]]["integral_internal_units"]
    frac=result[NAMES[3]]["integral_internal_units"]
    return result,{
        "maximum_charge_sum_closure_relative_residual":closure,
        "maximum_transverse_plus_minus_source_difference":transverse,
        "lapse_range":lapse_range,
        "local_escape_threshold_m_over_lapse_MeV_range":threshold_range,
        "lapse_squared_factor_ratio_no_threshold":lapse/flat,
        "fraction_retained_by_local_escape_threshold_after_lapse_weighting":frac/lapse,
        "midpoint_cut_vs_fractional_cut_relative_difference":abs(mid-frac)/frac,
    }

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--archive-json",type=Path,required=True,
                    help="Extracted p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.json")
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    archive=json.loads(args.archive_json.read_text(encoding="utf-8"))
    profile_sha=archive["physics_scope"]["profile_sha256"]
    if profile_sha != PROFILE_SHA: raise ValueError("profile SHA-256 mismatch")
    if float(archive["physics_scope"]["mediator_mass_MeV"]) != 10.0:
        raise ValueError("this audit is fixed to the 10 MeV benchmark")
    schemes,diagnostics=calculate(archive)
    result={
        "status":"RECOMPUTED_FROM_HISTORICAL_JSON_ARCHIVE_SOURCE_ONLY_NOT_B2",
        "source_run_id":43376779901,"source_artifact_id":14015517843,
        "source_artifact_zip_sha256":"2c2e2ef8610abfa16bc9e423937f974061ece101911fb9c6503e65901bb55715",
        "archive_json_sha256":sha256(args.archive_json),"profile_sha256":profile_sha,
        "mass_MeV":10.0,"grid_node_count":len(archive["grid_node_results"]),
        "radial_energy_direct_midpoint_count":len(archive["radial_energy_midpoint_results"]),
        "radial_node_count":len(archive["grid"]["radii_km"]),
        "energy_node_count":len(archive["grid"]["omega_local_MeV"]),
        "direct_midpoint_final_order":archive["radial_energy_midpoint_results"][0]["final_order"],
        "source_definition":"spectral_source = omega^2*sqrt(omega^2-m^2)/(2*pi^2) times B.13 local production rate, per g_X^2",
        "primary_measure":"4*pi*r^2*lapse^2*dr*domega with omega_local >= m/lapse; direct cell-midpoint quadrature; km-to-MeV^-1 and MeV^2-to-erg/s conversions omitted",
        "integration_scope":"B.13 moving-muon semi-Compton source only; excludes neutrino inverse decay, dimuon, B.2 attenuation, angular ray average, and full GR ray transport",
        "global_p1b_acceptance":archive["acceptance"],
        "schemes":schemes,"diagnostics":diagnostics,
        "interpretation_boundary":[
            "The flat measure reproduces the historical local-source proxy but omits the Eq. (B.1) lapse-squared factor and local escape threshold.",
            "The primary result is an Eq. (B.1)-motivated direct midpoint diagnostic, not the production radial Gauss / piecewise-linear energy integration.",
            "The 8-12 km concentration is robust under both measures; it does not determine the B.2 optical-depth distribution.",
            "Polarization fractions are local source fractions, not escaped-luminosity fractions.",
            "The historical P1-B overall acceptance remains failed; this post-processing does not change interpolation or quadrature acceptance."
        ]}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"schemes":{
        k:{"integral_internal_units":v["integral_internal_units"],"8_12_km_fraction":v["8_12_km_fraction"]}
        for k,v in schemes.items()},"diagnostics":diagnostics},indent=2))

if __name__=="__main__": main()
