#!/usr/bin/env python3
"""Re-audit archived C1 adaptive radial curves at both outer boundaries."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
COARSE = OUT / "croon_c1_b13_vector_transport_10mev_adaptive_radial_2026-11-20.json"
FINE = OUT / "croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_2026-11-20.json"
MANIFEST = OUT / "SHA256SUMS_croon_c1_adaptive_radial_2026-11-20.txt"
SUMMARY = OUT / "C1_RNU_10MEV_ADAPTIVE_RADIAL_CONVERGENCE_2026-11-20.json"
MODES = ("L", "+", "-")
LABELS = ("Rfar_Rnu_adaptive_quad", "Rfar_100km_vacuum_nu_tail_adaptive_quad")
FRACTION = 1e-8
TARGET = 1e-2

def metric(a_rows, b_rows, key, mode=None):
    if mode is None:
        a = np.asarray([r[key] for r in a_rows], float)
        b = np.asarray([r[key] for r in b_rows], float)
    else:
        k = key + "_by_mode_erg_s"
        a = np.asarray([r[k][mode] for r in a_rows], float)
        b = np.asarray([r[k][mode] for r in b_rows], float)
    peak = max(float(np.max(np.abs(b))), 1e-300)
    diff = np.abs(a-b)
    rel = diff/np.maximum(np.abs(b),1e-300)
    relevant = np.abs(b) > FRACTION*peak
    i_abs = int(np.argmax(diff))
    i_rel = int(np.argmax(rel))
    i_relevant = int(np.where(relevant)[0][np.argmax(rel[relevant])]) if np.any(relevant) else 0
    return {
        "max_absolute_difference_over_reference_peak": float(np.max(diff)/peak),
        "max_pointwise_relative_difference_above_1e-8_peak": float(np.max(rel[relevant])) if np.any(relevant) else 0.0,
        "at_g_X_max_absolute_difference": float(a_rows[i_abs]["g_X"]),
        "max_pointwise_relative_difference_all_points": float(np.max(rel)),
        "at_g_X_max_relative_difference_all_points": float(a_rows[i_rel]["g_X"]),
        "reference_fraction_of_peak_at_raw_relative_max": float(abs(b[i_rel])/peak),
        "at_g_X_max_relevant_relative_difference": float(a_rows[i_relevant]["g_X"]),
    }

def main():
    d0=json.loads(COARSE.read_text())
    d1=json.loads(FINE.read_text())
    i0=d0["masses"]["10"]; i1=d1["masses"]["10"]
    a=i0["coupling_curve"]; b=i1["coupling_curve"]
    assert i0["radial_points"]==103 and i1["radial_points"]==153
    assert i0["energy_points"]==i1["energy_points"]==32
    assert i0["adaptive_radial_enabled"] and i1["adaptive_radial_enabled"]
    assert len(a)==len(b)==121 and [x["g_X"] for x in a]==[x["g_X"] for x in b]

    curves={}
    for label in LABELS:
        curves[label]={
            "total":metric(a,b,label),
            "per_mode":{m:metric(a,b,label,m) for m in MODES},
        }
    all_metrics=[x for label in LABELS for x in
        [curves[label]["total"],*curves[label]["per_mode"].values()]]
    max_relevant=max(x["max_pointwise_relative_difference_above_1e-8_peak"] for x in all_metrics)
    max_abs_peak=max(x["max_absolute_difference_over_reference_peak"] for x in all_metrics)

    max_qerr=0.0; max_closure=0.0
    for item in (i0,i1):
        for row in item["coupling_curve"]:
            for label in ("Rfar_Rnu","Rfar_100km_vacuum_nu_tail"):
                key=label+"_adaptive_quad"
                modes=row[key+"_by_mode_erg_s"]
                assert set(modes)==set(MODES)
                closure=abs(sum(modes.values())-row[key])/max(abs(row[key]),1e-300)
                max_closure=max(max_closure,closure)
                max_qerr=max(max_qerr,row[key+"_relative_error_estimate"],
                    *row[key+"_relative_error_estimate_by_mode"].values())

    s0=i0["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"]
    s1=i1["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"]
    surface_rel=abs(sum(s0.values())-sum(s1.values()))/sum(s1.values())
    high_g={}
    for name,item in (("103",i0),("153",i1)):
        high=item["coupling_curve"][-1]["Rfar_Rnu_adaptive_quad_by_mode_erg_s"]
        surface=item["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"]
        high_g[name]={m:abs(high[m]-surface[m])/surface[m] for m in MODES}

    raw=curves["Rfar_100km_vacuum_nu_tail_adaptive_quad"]["total"]
    radial={
        "coarse_radial_points":103,
        "fine_radial_points":153,
        "coupling_points":121,
        "Rfar_Rnu":curves["Rfar_Rnu_adaptive_quad"],
        "Rfar_100km_vacuum_nu_tail":curves["Rfar_100km_vacuum_nu_tail_adaptive_quad"],
        "max_relevant_pointwise_relative_difference_all_boundaries_and_modes":max_relevant,
        "max_absolute_difference_over_curve_peak_all_boundaries_and_modes":max_abs_peak,
        "relevant_region_definition":"Reference luminosity > 1e-8 of the 153-node curve peak",
        "one_percent_target_met":max_relevant<TARGET and max_abs_peak<TARGET,
        "all_boundaries_and_modes_below_0_12_percent":max_relevant<0.0012,
        "raw_100km_tail_relative_max":raw["max_pointwise_relative_difference_all_points"],
        "raw_100km_tail_relative_max_at_g_X":raw["at_g_X_max_relative_difference_all_points"],
        "raw_100km_tail_reference_fraction_of_peak_at_relative_max":raw["reference_fraction_of_peak_at_raw_relative_max"],
        "surface_asymptote_103_vs_153_relative_difference":surface_rel,
        "max_QUADPACK_relative_error_estimate_both_grids":max_qerr,
        "max_three_mode_closure_residual_both_grids":max_closure,
        "high_coupling_surface_residual_by_mode":high_g,
    }
    manifest=[]
    for line in MANIFEST.read_text().splitlines():
        expected,name=line.split(maxsplit=1)
        p=OUT/Path(name).name
        actual=hashlib.sha256(p.read_bytes()).hexdigest()
        manifest.append({"file":p.name,"sha256":actual,"matches":actual==expected})
    radial["checksum_manifest_verified"]=all(x["matches"] for x in manifest)
    assert radial["one_percent_target_met"]
    assert radial["checksum_manifest_verified"]
    assert max_qerr<1e-6 and max_closure<1e-12 and surface_rel<1e-6

    summary=json.loads(SUMMARY.read_text())
    summary["status"]="PASS: 103/153-node adaptive radial convergence below 0.12% for both outer boundaries and all three polarizations"
    summary["radial_grid_convergence"]=radial
    summary["radial_grid_convergence"]["checksum_validation"]=manifest
    SUMMARY.write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
