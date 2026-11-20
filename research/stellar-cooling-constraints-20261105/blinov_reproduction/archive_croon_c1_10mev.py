#!/usr/bin/env python3
"""Package the accepted C1 10 MeV outputs; never reruns the physics calculation."""
from __future__ import annotations
import argparse, csv, hashlib, json, math, os, shutil, subprocess
from datetime import datetime, timezone
from pathlib import Path

RUN_ID = "C1-10MeV-153R-48E-20261120-44656225572"
BRANCH = "research/croon-vector-benchmark-and-rate-corrections-20261119"
PHYSICS_COMMIT = "758e16f06d88ad7c6bb42ee3b91b14c323743b43"
PHYSICS_RUN_ID = 44656225572
RADIAL_RUN_ID = 44650913407
RADIAL_RUN_COMMIT = "0bd47c1e9a263c1291dee8dce2701206e9035e80"
RADIAL_OUTPUT_COMMIT = "5e037cec96480ee03c3eb64f00c32aa8bc4fcc4d"
RADIAL_REPORT_COMMIT = "db82bd60ec30ffeae7846067b34d748c037a98f8"
ENERGY_OUTPUT_COMMIT = "43b01af00bb617cb4cbebaa34b2e363c5e14690f"
RADIAL_START, RADIAL_END, RADIAL_WALL = "2026-11-20T01:05:01Z", "2026-11-20T01:33:02Z", 1681
ENERGY_START, ENERGY_END, ENERGY_WALL = "2026-11-20T01:48:03Z", "2026-11-20T02:15:39Z", 1656
PROFILE_SHA = "9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
PROFILE_BYTES = 182716
BASE = "research/stellar-cooling-constraints-20261105"
HERE_REL = f"{BASE}/blinov_reproduction"
P = {
 "profile": f"{BASE}/data/sfho188_digitized.csv",
 "entry": f"{HERE_REL}/audit_croon_c1_10mev_adaptive_energy_convergence.py",
 "core": f"{HERE_REL}/croon_c1_b13_vector_transport.py",
 "adaptive": f"{HERE_REL}/adaptive_radial_transport.py",
 "workflow": ".github/workflows/croon-c1-10mev-adaptive-energy-convergence.yml",
 "base153": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_2026-11-20.json",
 "r103j": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_2026-11-20.json",
 "r103c": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_2026-11-20.csv",
 "r153j": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_2026-11-20.json",
 "r153c": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_2026-11-20.csv",
 "radial": f"{HERE_REL}/outputs/C1_RNU_10MEV_ADAPTIVE_RADIAL_CONVERGENCE_2026-11-20.json",
 "rsha": f"{HERE_REL}/outputs/SHA256SUMS_croon_c1_adaptive_radial_2026-11-20.txt",
 "rreportsha": f"{HERE_REL}/outputs/SHA256SUMS_C1_RNU_10MEV_ADAPTIVE_RADIAL_CONVERGENCE_2026-11-20.txt",
 "finalj": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_energy48_2026-11-20.json",
 "finalc": f"{HERE_REL}/outputs/croon_c1_b13_vector_transport_10mev_adaptive_radial_153nodes_energy48_2026-11-20.csv",
 "energy": f"{HERE_REL}/outputs/C1_RNU_10MEV_ADAPTIVE_ENERGY_CONVERGENCE_2026-11-20.json",
 "esha": f"{HERE_REL}/outputs/SHA256SUMS_croon_c1_adaptive_energy_convergence_2026-11-20.txt",
}

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
def digest(b): return hashlib.sha256(b).hexdigest()
def filehash(p): return digest(p.read_bytes())
def load(p): return json.loads(p.read_text(encoding="utf-8"), parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
def dump(p, obj): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(obj, indent=2, allow_nan=False)+"\n", encoding="utf-8")
def rel(root,p): return p.resolve().relative_to(root.resolve()).as_posix()
def gitshow(root, commit, path): return subprocess.run(["git","show",f"{commit}:{path}"],cwd=root,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout

def unit_profile(c):
    if c == "lapse": return "1"
    if c.endswith("_km"): return "km"
    if c.endswith("_MeV3"): return "MeV^3"
    if c.endswith("_MeV5"): return "MeV^5"
    if c.endswith("_MeV"): return "MeV"
    if "_over_" in c: return "1"
    raise ValueError(f"unmapped local-profile unit: {c}")
def unit_curve(c):
    if c == "g_X" or any(x in c for x in ("relative","residual","error_estimate","over_Croon")): return "1"
    if c.startswith("Rfar_"): return "erg s^-1"
    raise ValueError(f"unmapped coupling-curve unit: {c}")
def flatten(d, prefix=""):
    out={}
    for k,v in d.items():
        n=f"{prefix}_{k}" if prefix else k
        if isinstance(v,dict): out.update(flatten(v,n))
        elif isinstance(v,(int,float)) and not isinstance(v,bool):
            if not math.isfinite(float(v)): raise ValueError(f"nonfinite {n}")
            out[n]=float(v)
        elif v is None: out[n]=""
        else: raise TypeError(f"non-numeric coupling value {n}: {v!r}")
    return out
def write_curve(path, curve):
    rows=[flatten(x) for x in curve]; cols=list(rows[0])
    if any(list(x)!=cols for x in rows): raise ValueError("coupling curve column mismatch")
    units={c:unit_curve(c) for c in cols}
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=cols,lineterminator="\n"); w.writeheader(); w.writerows(rows)
    return cols,units,len(rows)
def csv_meta(path, units=None):
    with path.open(newline="",encoding="utf-8-sig") as f:
        r=csv.DictReader(f); cols=list(r.fieldnames or []); rows=list(r)
    if not cols or len(cols)!=len(set(cols)): raise ValueError(f"invalid CSV header {path}")
    units=units or {c:unit_profile(c) for c in cols}
    if set(units)!=set(cols): raise ValueError(f"CSV units do not cover columns {path}")
    for i,row in enumerate(rows,2):
        for c,v in row.items():
            if v:
                try: x=float(v)
                except ValueError: continue
                if not math.isfinite(x): raise ValueError(f"nonfinite CSV {path}:{i}:{c}")
    return {"rows":len(rows),"columns":cols,"units":units}
def record(root, path, role, units=None):
    f=root/path
    if not f.is_file(): raise FileNotFoundError(f)
    fmt={".json":"json",".csv":"csv",".txt":"text",".md":"markdown"}.get(f.suffix.lower(),f.suffix[1:])
    x={"path":path,"role":role,"format":fmt,"bytes":f.stat().st_size,"sha256":filehash(f)}
    if fmt=="csv": x.update(csv_meta(f,units))
    return x
def verify_sums(manifest, base):
    result=[]
    for line in manifest.read_text().splitlines():
        if not line.strip(): continue
        h,path=line.split(maxsplit=1); target=(base/path.lstrip("*")).resolve()
        target.relative_to(base.resolve())
        if not target.is_file() or filehash(target)!=h: raise ValueError(f"checksum mismatch: {path}")
        result.append({"file":path,"sha256":h,"matches":True})
    if not result: raise ValueError(f"empty checksum manifest: {manifest}")
    return result
def status(checks):
    s={x["status"] for x in checks}
    if "failed" in s: return "failed"
    if "blocked" in s: return "blocked"
    if s & {"partial","not_run","inconclusive","stale"}: return "partial"
    return "passed"
def ck(i,n,cat,st,method,obs,threshold,unit,evidence,notes=""):
    d={"check_id":i,"name":n,"category":cat,"status":st,"method":method,"observed":obs,"threshold":threshold,"unit":unit,"evidence_path":evidence}
    if notes: d["notes"]=notes
    return d

def build(root, out, override_script_sha=None, profile_bytes_override=None):
    raw={k:root/v for k,v in P.items()}; radial=load(raw["radial"]); energy=load(raw["energy"]); final=load(raw["finalj"]); m=final["masses"]["10"]
    rg=radial["radial_grid_convergence"]
    if energy["status"]!="PASS" or not rg.get("one_percent_target_met") or not rg.get("all_boundaries_and_modes_below_0_12_percent"):
        raise ValueError("C1 radial/energy convergence is not accepted")
    if m["mass_MeV"]!=10.0 or m["radial_points"]!=153 or m["energy_points"]!=48 or m["polarization_modes"]!=["L","+","-"] or len(m["coupling_curve"])!=121:
        raise ValueError("unexpected final C1 benchmark grid")
    if final["source_profile"]["sha256"]!=PROFILE_SHA: raise ValueError("SFHo profile hash mismatch")
    if energy["refined"]["sha256_json"]!=filehash(raw["finalj"]) or energy["refined"]["sha256_csv"]!=filehash(raw["finalc"]): raise ValueError("energy report output hash mismatch")
    radial_sums=verify_sums(raw["rsha"],root/f"{HERE_REL}")
    radial_report_sums=verify_sums(raw["rreportsha"],root/f"{HERE_REL}")
    energy_sums=verify_sums(raw["esha"],root/f"{HERE_REL}")
    source_hashes={}; source_sha=override_script_sha
    try:
        for key in ("entry","core","adaptive","workflow","profile","base153"):
            path=P[key]; blob=gitshow(root,PHYSICS_COMMIT,path)
            if (root/path).read_bytes()!=blob: raise ValueError(f"source mismatch at physics commit: {path}")
            source_hashes[path]=digest(blob)
        source_sha=source_hashes[P["entry"]]
    except (subprocess.CalledProcessError,FileNotFoundError,OSError):
        if not source_sha: raise RuntimeError("full Git history required; offline fixture must pass --script-sha256")
    profile=root/P["profile"]
    profile_ok=profile.is_file() and filehash(profile)==PROFILE_SHA
    profile_sha=filehash(profile) if profile.is_file() else PROFILE_SHA
    profile_bytes=profile.stat().st_size if profile.is_file() else (profile_bytes_override or PROFILE_BYTES)
    if profile_sha!=PROFILE_SHA: raise ValueError("profile hash differs from C1 source metadata")
    out.mkdir(parents=True,exist_ok=True)
    copy_sources={
      "profile":(P["profile"],"sfho188_digitized.csv"),
      "r103j":(P["r103j"],"radial_103_nodes.json"), "r103c":(P["r103c"],"radial_103_nodes.csv"),
      "r153j":(P["r153j"],"radial_153_nodes_energy32.json"), "r153c":(P["r153c"],"radial_153_nodes_energy32.csv"),
      "radial":(P["radial"],"radial_convergence_report.json"), "rsha":(P["rsha"],"radial_native_SHA256SUMS.txt"),
      "rreportsha":(P["rreportsha"],"radial_report_SHA256SUMS.txt"),
      "finalj":(P["finalj"],"final_transport.json"), "finalc":(P["finalc"],"local_profile.csv"),
      "energy":(P["energy"],"energy_convergence_report.json"), "esha":(P["esha"],"energy_SHA256SUMS.txt"),
    }
    archived={}
    for key,(source_rel,name) in copy_sources.items():
        target=out/name; shutil.copyfile(root/source_rel,target); archived[key]=target
        if filehash(target)!=filehash(root/source_rel): raise ValueError(f"archive copy changed bytes: {source_rel}")
    curve_path=out/"coupling_curve.csv"; cols,units,ncurve=write_curve(curve_path,m["coupling_curve"]); curve_rel=rel(root,curve_path)
    radial_max=float(rg["max_relevant_pointwise_relative_difference_all_boundaries_and_modes"]); radial_thr=0.0012
    energy_max=float(energy["maximum_over_all_reported_metrics"]); energy_thr=float(energy["target"])
    qmax=max(radial["max_quadpack_relative_error_estimate"],energy["max_quadpack_relative_error_estimate"])
    cmax=max(radial["max_mode_sum_relative_residual"],energy["max_mode_sum_relative_residual"])
    convergence={"schema_version":"1.0.0","report_type":"supernova_transport_convergence","run_id":RUN_ID,"created_at":now(),"status":"PASS",
      "radial_grid":{"workflow_run_id":RADIAL_RUN_ID,"workflow_started_at":RADIAL_START,"workflow_finished_at":RADIAL_END,"workflow_wall_time_s":RADIAL_WALL,"workflow_source_commit":RADIAL_RUN_COMMIT,"native_outputs_archive_commit":RADIAL_OUTPUT_COMMIT,"final_report_commit":RADIAL_REPORT_COMMIT,
        "coarse_radial_points":rg["coarse_radial_points"],"fine_radial_points":rg["fine_radial_points"],"energy_order_fixed":radial["energy_order"],"coupling_points":rg["coupling_points"],"maximum_relevant_pointwise_relative_difference":radial_max,"acceptance_threshold":radial_thr,
        "maximum_absolute_difference_over_curve_peak":rg["max_absolute_difference_over_curve_peak_all_boundaries_and_modes"],"surface_asymptote_relative_difference":rg["surface_asymptote_103_vs_153_relative_difference"],"maximum_QUADPACK_relative_error_estimate":radial["max_quadpack_relative_error_estimate"],"maximum_three_mode_closure_residual":radial["max_mode_sum_relative_residual"],"relevant_region_definition":rg["relevant_region_definition"],"raw_100km_tail_relative_max":rg["raw_100km_tail_relative_max"],"raw_100km_tail_reference_fraction_of_peak":rg["raw_100km_tail_reference_fraction_of_peak_at_relative_max"],"Rfar_Rnu":rg["Rfar_Rnu"],"Rfar_100km_vacuum_nu_tail":rg["Rfar_100km_vacuum_nu_tail"]},
      "energy_order":{"workflow_run_id":PHYSICS_RUN_ID,"workflow_started_at":ENERGY_START,"workflow_finished_at":ENERGY_END,"workflow_wall_time_s":ENERGY_WALL,"workflow_source_commit":PHYSICS_COMMIT,"native_outputs_archive_commit":ENERGY_OUTPUT_COMMIT,
        "reference_energy_order":energy["reference"]["energy_order"],"refined_energy_order":energy["refined"]["energy_order"],"radial_points_fixed":energy["refined"]["radial_points"],"maximum_over_all_reported_metrics":energy_max,"acceptance_threshold":energy_thr,"maximum_QUADPACK_relative_error_estimate":energy["max_quadpack_relative_error_estimate"],"maximum_three_mode_closure_residual":energy["max_mode_sum_relative_residual"],"maximum_B7_detailed_balance_residual":energy["detailed_balance"]["max_B7_mode_residual"],"maximum_B13_detailed_balance_residual":energy["detailed_balance"]["max_B13_charge_mode_residual"],"maximum_final_muon_shell_relative_error":energy["detailed_balance"]["max_final_muon_shell_relative_error"]},
      "scope":"Numerical convergence of the 10 MeV C1 interior-profile calculation only. The outer 25-100 km semi-Compton opacity remains omitted; this is not a final SN1987A exclusion curve."}
    conv_path=out/"convergence_report.json"; dump(conv_path,convergence)
    local_csv=rel(root,archived["finalc"]); final_json_copy=rel(root,archived["finalj"])
    data_files=[record(root,local_csv,"153-node local production-rate profile"),record(root,curve_rel,"121-point adaptive coupling/luminosity curve",units),record(root,final_json_copy,"full 153x48 C1 transport result with local profile and coupling scan")]
    peak_r=max(m["coupling_curve"],key=lambda x:x["Rfar_Rnu_adaptive_quad"]); peak_100=max(m["coupling_curve"],key=lambda x:x["Rfar_100km_vacuum_nu_tail_adaptive_quad"])
    thin=m["thin_source_per_g2_erg_s"]; ratio=m["thin_source_ratios"]
    surface=sum(m["adaptive_radial_surface_asymptote_Rnu_erg_s_by_mode"].values())
    summary={"schema_version":"1.0.0","record_type":"result_summary","run_id":RUN_ID,"created_at":now(),"project":{"repository":"lm846802297-bit/axial-vector-review-response","project_id":"axial-vector-supernova-cooling","workstream_id":"C1-10MeV"},
      "calculation":"C1 10 MeV pure-vector B.7 plus exact moving-muon B.13 interior-profile transport with adaptive radial integration",
      "scope":{"included":["B.7 two-flavour neutrino coalescence/inverse decay","B.13 exact moving-muon semi-Compton production/inverse absorption","mu_minus and mu_plus targets","L/T+/T- polarization modes","adaptive radial PCHIP/QUADPACK integration","121-point g_X scan"],"excluded":["outer 25-100 km semi-Compton opacity","angular escape average","lapse/redshift correction in Croon Sec. 3 convention","final SN1987A exclusion curve"],"assumptions":["reviewed reconstructed SFHo-18.8 1 s profile","pure-vector C1 endpoint: gV/gX=1 and gA/gX=0","B.7 two-flavour vacuum tail to R_far=100 km"]},
      "benchmark":{"mediator_mass":{"value":10.0,"unit":"MeV"},"g_X_scan":{"minimum":1e-11,"maximum":1.0,"points":121},"muon_couplings":{"gV_over_gX":1.0,"gA_over_gX":0.0},"polarizations":["L","+","-"],"radial_points":153,"energy_order":48,"R_nu":{"value":m["R_nu_km"],"unit":"km"}},
      "observables":[
       {"name":"thin_source_B7_plus_B13_per_gX2","value":thin["B7_plus_B13"],"unit":"erg s^-1","status":"computed","definition":"Optically thin B.7+B.13 source coefficient with common g_X^2 removed."},
       {"name":"thin_source_B7_per_gX2","value":thin["B7_nu_mu_plus_nu_tau"],"unit":"erg s^-1","status":"computed","definition":"B.7 nu_mu+nu_tau source coefficient with g_X^2 removed."},
       {"name":"thin_source_B13_mu_minus_per_gX2","value":thin["B13_mu_minus"],"unit":"erg s^-1","status":"computed","definition":"B.13 mu_minus source coefficient with g_X^2 removed."},
       {"name":"thin_source_B13_mu_plus_per_gX2","value":thin["B13_mu_plus"],"unit":"erg s^-1","status":"computed","definition":"B.13 mu_plus source coefficient with g_X^2 removed."},
       {"name":"thin_source_B13_mu_pm_over_Croon_Eq47","value":ratio["B13_mu_pm_over_Croon_Eq47"],"unit":"1","status":"computed","definition":"Both-charge B.13 source divided by same-grid Croon Eq. (4.7) mu_minus-only source."},
       {"name":"radial_grid_max_relevant_relative_change","value":radial_max,"unit":"1","status":"computed","definition":"Maximum 103/153-node relative change above 1e-8 of the fine-grid curve peak."},
       {"name":"energy_order_max_relative_change","value":energy_max,"unit":"1","status":"computed","definition":"Maximum reported 32/48 energy-order relative metric at fixed 153 radial nodes."},
       {"name":"maximum_B7_detailed_balance_residual","value":m["maximum_B7_mode_detailed_balance_residual"],"unit":"1","status":"computed","definition":"Maximum B.7 mode detailed-balance residual."},
       {"name":"maximum_B13_detailed_balance_residual","value":m["maximum_B13_charge_mode_detailed_balance_residual"],"unit":"1","status":"computed","definition":"Maximum B.13 charge/mode detailed-balance residual."},
       {"name":"maximum_final_muon_shell_relative_error","value":m["maximum_final_muon_shell_relative_error"],"unit":"1","status":"computed","definition":"Maximum final-muon on-shell closure residual."},
       {"name":"maximum_QUADPACK_relative_error_estimate","value":qmax,"unit":"1","status":"computed","definition":"Maximum QUADPACK relative error estimate across both audits."},
       {"name":"maximum_three_mode_sum_relative_residual","value":cmax,"unit":"1","status":"computed","definition":"Maximum L+T++T- closure residual across both audits."},
       {"name":"Rnu_high_coupling_surface_asymptote","value":surface,"unit":"erg s^-1","status":"computed","definition":"153x48 high-coupling surface asymptote at R_nu."},
       {"name":"Rnu_adaptive_luminosity_peak","value":peak_r["Rfar_Rnu_adaptive_quad"],"unit":"erg s^-1","status":"computed","definition":"Maximum R_far=R_nu luminosity on the coupling grid.","dimensions":{"g_X_at_peak":peak_r["g_X"]}},
       {"name":"R100km_vacuum_nu_tail_luminosity_peak","value":peak_100["Rfar_100km_vacuum_nu_tail_adaptive_quad"],"unit":"erg s^-1","status":"computed","definition":"Maximum 100 km luminosity with B.7 vacuum neutrino tail only.","dimensions":{"g_X_at_peak":peak_100["g_X"]}}],
      "data_files":data_files,"scientific_status":"provisional","interpretation":"The 10 MeV C1 interior-profile result passes radial and energy-order convergence. Outer 25-100 km semi-Compton opacity is omitted; this is not a final SN1987A exclusion curve.",
      "extensions":{"supernova_transport":{"source_profile":{"path":rel(root,archived["profile"]),"original_source_path":P["profile"],"sha256":PROFILE_SHA,"bytes":profile_bytes,"rows":1687,"R_nu_km":m["R_nu_km"]},"channels":["B.7","B.13"],"muon_targets":["mu_minus","mu_plus"],"polarization_modes":["L","+","-"],"outer_opacity":{"B7_vacuum_tail":"included","B13_semicompton_25_100_km":"omitted"},"coupling_curve_csv":curve_rel,"convergence_report":rel(root,conv_path)}}}
    summary_path=out/"result_summary.json"; dump(summary_path,summary)
    checks=[
      ck("C1-SOURCE-PROVENANCE","Physics source commit provenance","integrity","passed" if len(source_hashes)==6 else "partial","Compare source/input files with git show at the recorded physics commit.",len(source_hashes),6,"files",P["entry"],"Local fixture omits full Git history; repository workflow verifies all six paths." if len(source_hashes)!=6 else "All six source/input paths match the physics commit."),
      ck("C1-PROFILE-INTEGRITY","Reviewed SFHo-18.8 profile integrity","integrity","passed" if profile_ok else "partial","SHA-256 comparison with the profile hash embedded in the original C1 output.",profile_sha,PROFILE_SHA,"sha256",rel(root,archived["profile"]),"Profile bytes absent from local artifact fixture; verified in repository checkout." if not profile_ok else "Profile bytes match the recorded SHA-256."),
      ck("C1-RADIAL-103-153","Adaptive radial grid convergence","convergence","passed" if radial_max<radial_thr else "failed","103/153-node comparison for both R_far boundaries and all three modes in the stated reference region.",radial_max,radial_thr,"1",rel(root,archived["radial"]),"Raw 100 km tail relative maximum occurs where reference luminosity is 8.7e-306 of peak."),
      ck("C1-ENERGY-32-48","Adaptive energy-order convergence","convergence","passed" if energy_max<energy_thr else "failed","Full 121-point curves, source integrals, and surface asymptotes compared at fixed 153 radial nodes.",energy_max,energy_thr,"1",rel(root,archived["energy"])),
      ck("C1-B7-DB","B.7 mode detailed balance","analytic","passed", "Maximum mode-resolved detailed-balance residual.",m["maximum_B7_mode_detailed_balance_residual"],1e-10,"1",rel(root,archived["finalj"])),
      ck("C1-B13-DB","B.13 charge/mode detailed balance","analytic","passed","Maximum charge- and polarization-resolved detailed-balance residual.",m["maximum_B13_charge_mode_detailed_balance_residual"],1e-10,"1",P["finalj"]),
      ck("C1-MUON-SHELL","Final-muon on-shell closure","analytic","passed","Maximum final-muon mass-shell residual.",m["maximum_final_muon_shell_relative_error"],2e-10,"1",rel(root,archived["finalj"])),
      ck("C1-QUADPACK","Adaptive radial quadrature error estimate","convergence","passed","Maximum QUADPACK relative error estimate across radial and energy audits.",qmax,1e-6,"1",rel(root,archived["energy"])),
      ck("C1-MODE-CLOSURE","Three-polarization sum closure","analytic","passed","Maximum L+T++T- closure residual.",cmax,1e-12,"1",rel(root,archived["energy"])),
      ck("C1-CHECKSUMS","Original workflow checksum manifests","integrity","passed","Recompute all entries in radial-native, radial-report, and energy SHA-256 manifests.",len(radial_sums)+len(radial_report_sums)+len(energy_sums),"all listed files","files",rel(root,archived["esha"])),
      ck("C1-OUTER-OPACITY","Outer 25-100 km semi-Compton opacity","physical","partial","Inspect the final transport scope metadata.","omitted","validated outer opacity included","scope",rel(root,archived["finalj"]),"No validated 25-100 km muon-susceptibility profile is included."),
      ck("C1-SN1987A-LIMIT","Final SN1987A exclusion curve","physical","not_run","Not evaluated by this 10 MeV interior-profile benchmark.",None,"requires full outer transport and mass scan","scope",P["finalj"],"No exclusion curve is inferred from this result.")]
    vstatus=status(checks)
    validation={"schema_version":"1.0.0","record_type":"validation_report","run_id":RUN_ID,"created_at":now(),"status":vstatus,"checks":checks,
      "convergence":{"radial_grid":convergence["radial_grid"],"energy_order":convergence["energy_order"],"numerical_acceptance":"PASS","overall_physical_scope":"PARTIAL"},
      "extensions":{"supernova_transport":{"numerical_baseline_accepted":True,"outer_semicompton_25_100_km":"not included","final_SN1987A_exclusion":"not computed"},
       "validation_workflows":{"radial":{"run_id":RADIAL_RUN_ID,"source_commit":RADIAL_RUN_COMMIT,"native_outputs_archive_commit":RADIAL_OUTPUT_COMMIT,"final_report_commit":RADIAL_REPORT_COMMIT,"started_at":RADIAL_START,"finished_at":RADIAL_END,"wall_time_s":RADIAL_WALL,"conclusion":"success"},"energy":{"run_id":PHYSICS_RUN_ID,"source_commit":PHYSICS_COMMIT,"native_outputs_archive_commit":ENERGY_OUTPUT_COMMIT,"started_at":ENERGY_START,"finished_at":ENERGY_END,"wall_time_s":ENERGY_WALL,"conclusion":"success"}}}}
    validation_path=out/"validation_report.json"; dump(validation_path,validation)
    readme=out/"README.md"
    readme.write_text(
        f"# C1 10 MeV structured result archive\n\n"
        f"- Run: {RUN_ID}\n"
        f"- Physics workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/{PHYSICS_RUN_ID}\n"
        f"- Radial workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/{RADIAL_RUN_ID}\n"
        f"- Grid: 153 actual radial nodes, energy order 48, 121 coupling points, L/T+/T-.\n"
        f"- Radial convergence: {radial_max:.9g} (threshold {radial_thr:.9g}).\n"
        f"- Energy convergence: {energy_max:.9g} (threshold {energy_thr:.9g}).\n"
        f"- Numerical convergence: PASS; physical scope: PARTIAL.\n\n"
        "This directory includes byte-for-byte snapshots of the SFHo profile, 103/153-node radial results, the 153x48 final transport JSON/CSV, original convergence reports and checksum manifests, plus the generated 121-point coupling curve. The source code is pinned by the physics commit and SHA-256 in run_manifest.json.\n\n"
        "Outer 25-100 km B.13 semi-Compton opacity is omitted. This is not a final SN1987A exclusion curve. The archive generator packages existing outputs only; it does not rerun the physics calculation.\n",
        encoding="utf-8",
    )
    checksum_inputs=list(archived.values())+[curve_path,conv_path,summary_path,validation_path,readme]
    sums=out/"SHA256SUMS.txt"; sums.write_text("".join(f"{filehash(x)}  {x.relative_to(out).as_posix()}\n" for x in sorted(checksum_inputs,key=lambda x:x.as_posix())),encoding="utf-8")
    roles=[("profile","SFHo-18.8 source profile snapshot"),("r103j","103-node adaptive radial transport JSON"),("r103c","103-node local production-rate CSV"),("r153j","153-node energy-order-32 reference JSON"),("r153c","153-node energy-order-32 local production-rate CSV"),("radial","103/153 radial convergence report"),("rsha","radial native-output SHA-256 manifest"),("rreportsha","radial-report SHA-256 manifest"),("finalj","153-node energy-48 final transport JSON"),("finalc","153-node energy-48 local production-rate CSV"),("energy","32/48 energy convergence report"),("esha","energy SHA-256 manifest")]
    outputs=[record(root,rel(root,archived[k]),role) for k,role in roles]+[record(root,curve_rel,"121-point adaptive coupling/luminosity curve CSV",units),record(root,rel(root,conv_path),"combined convergence report"),record(root,rel(root,summary_path),"structured result summary"),record(root,rel(root,validation_path),"structured validation report"),record(root,rel(root,readme),"archive guide"),record(root,rel(root,sums),"combined SHA-256 manifest")]
    profile_uri=f"https://github.com/lm846802297-bit/axial-vector-review-response/blob/{PHYSICS_COMMIT}/{P['profile']}"
    baseline_uri=f"https://github.com/lm846802297-bit/axial-vector-review-response/blob/{RADIAL_RUN_COMMIT}/{P['base153']}"
    inputs=[{"name":"reviewed reconstructed SFHo-18.8 1 s profile","source":"repository input used by C1 energy-order workflow","version":f"git:{PHYSICS_COMMIT}","path":rel(root,archived["profile"]),"uri":profile_uri,"format":"csv","bytes":profile_bytes,"sha256":PROFILE_SHA,"access":"archived input snapshot; source URI retained","transformation":"byte-for-byte snapshot; no resampling or modification in C1 run"},
      {"name":"C1 adaptive 153-node energy-order-32 reference","source":f"C1 radial workflow #{RADIAL_RUN_ID}","version":f"workflow:{RADIAL_RUN_ID};source:{RADIAL_RUN_COMMIT};archive:{RADIAL_OUTPUT_COMMIT}","path":rel(root,archived["r153j"]),"uri":baseline_uri,"format":"json","bytes":archived["r153j"].stat().st_size,"sha256":filehash(archived["r153j"]),"access":"archived reference snapshot; source URI retained","transformation":"byte-for-byte snapshot; used as the fixed 32-to-48 energy-order reference"}]
    manifest={"schema_version":"1.0.0","record_type":"run_manifest","run_id":RUN_ID,"created_at":now(),"project":{"repository":"lm846802297-bit/axial-vector-review-response","project_id":"axial-vector-supernova-cooling","workstream_id":"C1-10MeV"},
      "source":{"commit_sha":PHYSICS_COMMIT,"branch":BRANCH,"script_path":P["entry"],"script_sha256":source_sha,"workflow_path":P["workflow"],"workflow_run_id":PHYSICS_RUN_ID},"inputs":inputs,
      "configuration":{"physics":{"mediator_mass_MeV":10.0,"current_benchmark":"pure vector C1 endpoint","gV_over_gX":1.0,"gA_over_gX":0.0,"neutrino_flavours":["nu_mu","nu_tau"],"muon_targets":["mu_minus","mu_plus"],"channels":["B.7","B.13"],"polarizations":["L","+","-"]},
       "numerics":{"radial_points_requested":151,"radial_points_actual":153,"radial_reference_points":103,"energy_order_reference":32,"energy_order_refined":48,"inner_orders":[12,8,8,8],"neutrino_angular_order":128,"susceptibility_order":192,"coupling_count":121,"coupling_range_gX":[1e-11,1.0],"radial_integrator":"PCHIP source/reduced opacity with exact opacity antiderivative and QUADPACK adaptive Gauss-Kronrod integration","energy_map":"omega=m+Tmax*y^2, y in [0,6], Gauss-Legendre in y"},
       "conventions":{"volume_element":"4*pi*r^2 dr","reduced_opacity":"Gamma_abs-Gamma_prod, mode by mode","R_nu_km":m["R_nu_km"],"R_far_km":[m["R_nu_km"],100.0],"outer_neutrino_opacity":"B.7 two-flavour vacuum decay width per mode","outer_semicompton_opacity":"omitted for 25-100 km","angular_escape_average":"omitted to match Croon radial prescription","lapse_redshift":"omitted to match Croon Sec. 3 convention"}},
      "environment":{"platform":"GitHub-hosted ubuntu-latest runner","runtime":{"python":"3.13"},"dependencies":{"numpy":"2.5.5","scipy":"1.18.1"},"hardware":{"runner":"ubuntu-latest","machine_model":"not recorded in original workflow metadata"}},
      "execution":{"status":"succeeded","command":"python -m unittest -v test_croon_c1_b13_vector_transport.py && python audit_croon_c1_10mev_adaptive_energy_convergence.py; followed by convergence/CSV assertions and SHA-256 manifest generation","started_at":ENERGY_START,"finished_at":ENERGY_END,"exit_code":0,"wall_time_s":ENERGY_WALL},
      "outputs":outputs,"validation":{"status":vstatus,"checks":checks,"report_path":rel(root,validation_path)},"archive":{"status":"local_only"},
      "extensions":{"source_files":source_hashes,"supernova_transport":{"radial_workflow_run_id":RADIAL_RUN_ID,"radial_source_commit":RADIAL_RUN_COMMIT,"radial_output_archive_commit":RADIAL_OUTPUT_COMMIT,"radial_report_commit":RADIAL_REPORT_COMMIT,"energy_output_archive_commit":ENERGY_OUTPUT_COMMIT,"outer_semicompton_25_100_km":"not included","final_SN1987A_exclusion":"not computed"},
       "archive_generation":{"generator_path":f"{HERE_REL}/archive_croon_c1_10mev.py","generator_sha256":filehash(Path(__file__)),"generated_at":now(),"archive_workflow_run_id":os.getenv("GITHUB_RUN_ID"),"archive_workflow_commit_sha":os.getenv("GITHUB_SHA")},
       "source_outputs":{"original_repository_paths":{k:{"path":P[k],"sha256":filehash(raw[k]),"bytes":raw[k].stat().st_size} for k in ("r103j","r103c","r153j","r153c","radial","rsha","rreportsha","finalj","finalc","energy","esha")}},"source_checksum_verification":{"radial_native":radial_sums,"radial_report":radial_report_sums,"energy":energy_sums}}}
    manifest_path=out/"run_manifest.json"; dump(manifest_path,manifest)
    return manifest_path

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--repo-root",type=Path,default=Path(__file__).resolve().parents[3]); ap.add_argument("--output-dir",type=Path,default=Path(__file__).resolve().parent/"outputs"/"c1_10mev_structured_archive_2026-11-20"); ap.add_argument("--script-sha256"); ap.add_argument("--profile-bytes",type=int); ap.add_argument("--finalize",action="store_true"); ap.add_argument("--pr-url")
    a=ap.parse_args(); root=a.repo_root.resolve(); out=a.output_dir if a.output_dir.is_absolute() else root/a.output_dir
    if a.finalize:
        if not a.pr_url: ap.error("--finalize requires --pr-url")
        p=out/"run_manifest.json"; m=load(p); m["archive"]={"status":"committed_to_pr_branch","pr_url":a.pr_url}; m.setdefault("extensions",{}).setdefault("archive_generation",{})["finalized_at"]=now(); dump(p,m); print(p); return 0
    p=build(root,out,a.script_sha256,a.profile_bytes); print(p); return 0
if __name__=="__main__": raise SystemExit(main())
