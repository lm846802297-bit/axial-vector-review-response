#!/usr/bin/env python3
"""Build CSV/SVG evidence from the archived P1-B B.13 local-kernel JSON.
Post-processing only: no new collision-kernel calculation is performed.
"""
from __future__ import annotations
import argparse,csv,hashlib,json
from pathlib import Path
JSON_SHA256="14c4405f9421aca517ff00310232ad9aead4c0cdd61868e2788125875cb84dc0"
ZIP_SHA256="2c2e2ef8610abfa16bc9e423937f974061ece101911fb9c6503e65901bb55715"
PROFILE_SHA256="9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c"
RUN_ID,ARTIFACT_ID=43376779901,14015517843
SOURCE_COMMIT="0f61bfc3e381402cbea9740958b9a2744f006040"
SOURCE_BRANCH="research/fig7-10mev-transport-localization-20261113-v2"
SOURCE_BLOBS={"audit_script":"96b70750333af1b89274b60ffb4bc9492514ecbf","test_script":"cb52f9947ca794795968724a11cca269c9d19c17","moving_muon_compton_py":"918d38504b8a0df1c21dfe243bc25eab9808e6a9","rates_py":"dd4d1accfd58a574e704f477f611299f15943465","reference_py":"374c8d69311231533faf9f8c4f8bea84d0f97b42","profile_csv":"e41df78c8035540760fbcb7ef592cd830171822e","profile_provenance_json":"08e697fddcc448681b58ac0a1d653addd879ed99"}
CHARGES,MODES=("mu_minus","mu_plus"),("L","+","-")
FIELDS=["point_type","radius_km","omega_local_MeV","temperature_MeV","mu_minus_chemical_potential_MeV","lapse","x_max","charge","mode","production_MeV","absorption_MeV","reduced_absorption_MeV","spectral_source_MeV5","detailed_balance_relative_residual","quadrature_orders","quadrature_refinement_relative_change","quadrature_pass","final_muon_shell_relative_error","direct_vs_interpolated_relative_error","interpolation_pass","energy_coverage_pass","charge_sum_closure_relative_residual"]
def sha(path):
 h=hashlib.sha256()
 with Path(path).open("rb") as f:
  for b in iter(lambda:f.read(1<<20),b""):h.update(b)
 return h.hexdigest()
def nested(obj,key):
 for part in key.split("."):obj=obj[part]
 return obj
def point_rows(p,kind):
 final=p["order_ladder"][-1]
 r=p["radius_km"] if kind=="grid_node" else p["radius_midpoint_km"]
 w0=p["omega_local_MeV"] if kind=="grid_node" else p["omega_midpoint_MeV"]
 direct=p.get("direct_vs_interpolated") or {}
 for charge in CHARGES:
  item=final["charge_resolved"][charge]
  for i,mode in enumerate(MODES):
   yield {"point_type":kind,"radius_km":r,"omega_local_MeV":w0,"temperature_MeV":final["temperature_MeV"],"mu_minus_chemical_potential_MeV":final["mu_minus_chemical_potential_MeV"],"lapse":final["lapse"],"x_max":final["x_max"],"charge":charge,"mode":mode,"production_MeV":item["production"][i],"absorption_MeV":item["absorption"][i],"reduced_absorption_MeV":item["reduced_absorption"][i],"spectral_source_MeV5":item["spectral_source"][i],"detailed_balance_relative_residual":item["mode_detailed_balance_relative_residual"][i],"quadrature_orders":"x".join(map(str,final["orders"])),"quadrature_refinement_relative_change":p["final_refinement_relative_change"],"quadrature_pass":p["quadrature_pass"],"final_muon_shell_relative_error":final["final_muon_shell_relative_error"],"direct_vs_interpolated_relative_error":direct.get("maximum_relative_error",""),"interpolation_pass":p.get("interpolation_pass",""),"energy_coverage_pass":p.get("energy_coverage_pass",""),"charge_sum_closure_relative_residual":final["charge_sum_closure_relative_residual"]}
def colour(v,t):
 if v<=t:return "#2a9d8f"
 if v<=2*t:return "#e9c46a"
 if v<=5*t:return "#f4a261"
 return "#d1495b"
def heatmap(title,subtitle,points,rkey,ekey,vkey,threshold,xlabel,ylabel,path):
 radii=sorted({float(p[rkey]) for p in points});energies=sorted({float(p[ekey]) for p in points})
 ri={v:i for i,v in enumerate(radii)};ei={v:i for i,v in enumerate(energies)}
 W,H,L,T,PW,PH=1280,760,130,115,1050,520
 cw,ch=PW/len(energies),PH/len(radii);vals=[float(nested(p,vkey)) for p in points]
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<rect width="100%" height="100%" fill="#fffdf8"/>',f'<text x="{W/2}" y="42" text-anchor="middle" font-family="Arial" font-size="25" font-weight="bold" fill="#17324d">{title}</text>',f'<text x="{W/2}" y="74" text-anchor="middle" font-family="Arial" font-size="15" fill="#44546a">{subtitle}</text>']
 for p in points:
  r,e,v=float(p[rkey]),float(p[ekey]),float(nested(p,vkey));x,y=L+ei[e]*cw,T+ri[r]*ch
  tip=f"r={r:.6g} km; omega={e:.6g} MeV; relative error={v:.6g}; threshold={threshold:.3g}"
  parts.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{cw+.3:.2f}" height="{ch+.3:.2f}" fill="{colour(v,threshold)}" stroke="#fffdf8"><title>{tip}</title></rect>')
 for i,e in enumerate(energies):
  if i in {0,len(energies)//4,len(energies)//2,3*len(energies)//4,len(energies)-1}:
   x=L+(i+.5)*cw;parts.append(f'<text x="{x:.1f}" y="{T+PH+25}" text-anchor="middle" font-family="Arial" font-size="13" fill="#17324d">{e:.4g}</text>')
 for i,r in enumerate(radii):
  if i in {0,len(radii)//4,len(radii)//2,3*len(radii)//4,len(radii)-1}:
   y=T+(i+.5)*ch+4;parts.append(f'<text x="{L-12}" y="{y:.1f}" text-anchor="end" font-family="Arial" font-size="13" fill="#17324d">{r:.4g}</text>')
 parts += [f'<text x="{L+PW/2}" y="{H-38}" text-anchor="middle" font-family="Arial" font-size="17" fill="#17324d">{xlabel}</text>',f'<text x="28" y="{T+PH/2}" transform="rotate(-90 28 {T+PH/2})" text-anchor="middle" font-family="Arial" font-size="17" fill="#17324d">{ylabel}</text>',f'<text x="{L}" y="{H-12}" font-family="Arial" font-size="13" fill="#44546a">{len(points)} points; max={max(vals):.6g}; threshold={threshold:.3g}</text>','<rect x="950" y="95" width="14" height="14" fill="#2a9d8f"/><text x="970" y="107" font-family="Arial" font-size="12" fill="#17324d">pass</text>','<rect x="1020" y="95" width="14" height="14" fill="#e9c46a"/><text x="1040" y="107" font-family="Arial" font-size="12" fill="#17324d">near threshold</text>','<rect x="1130" y="95" width="14" height="14" fill="#d1495b"/><text x="1150" y="107" font-family="Arial" font-size="12" fill="#17324d">fail</text>','</svg>']
 path.write_text("\n".join(parts)+"\n",encoding="utf-8")
def build(input_json,outdir):
 input_json,outdir=Path(input_json),Path(outdir);jhash=sha(input_json)
 if jhash!=JSON_SHA256:raise ValueError(f"original JSON SHA mismatch: {jhash}")
 d=json.loads(input_json.read_text(encoding="utf-8"))
 if d["status"]!="completed_numerical_audit" or d["physics_scope"]["profile_sha256"]!=PROFILE_SHA256:raise ValueError("source status/profile identity mismatch")
 grid,mids=d["grid_node_results"],d["radial_energy_midpoint_results"]
 if len(grid)!=513 or len(mids)!=468 or d["acceptance"]["overall_p1b_pass"] is not False:raise ValueError("point counts or failed-acceptance state changed")
 outdir.mkdir(parents=True,exist_ok=True);csvp=outdir/"p1b_b13_local_kernel_radial_energy_10mev_2026-11-13.csv"
 with csvp.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
  for p in grid:w.writerows(point_rows(p,"grid_node"))
  for p in mids:w.writerows(point_rows(p,"cell_midpoint"))
 gsvg=outdir/"grid_node_quadrature_refinement.svg"
 heatmap("P1-B local B.13 kernel: grid-node quadrature refinement","Archived 10 MeV run; final relative change (criterion 0.1%)",grid,"radius_km","omega_local_MeV","final_refinement_relative_change",1e-3,"Local energy omega (MeV)","Radius (km)",gsvg)
 isvg=outdir/"cell_midpoint_interpolation_error.svg"
 heatmap("P1-B local B.13 kernel: cell-midpoint interpolation error","Direct midpoint versus sequential log interpolation (criterion 1%)",mids,"radius_midpoint_km","omega_midpoint_MeV","direct_vs_interpolated.maximum_relative_error",1e-2,"Local energy omega (MeV)","Radial midpoint (km)",isvg)
 a=d["acceptance"];readmep=outdir/"README.md"
 readmep.write_text("# P1-B 10 MeV exact B.13 local-kernel archive\n\nThis package preserves and expands the original GitHub Actions numerical artifact. The CSV and SVG files are deterministic post-processing of the unchanged JSON, not a new collision-kernel calculation.\n\n"+f"- Original Actions run: [#{RUN_ID}](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/{RUN_ID})\n- Original artifact ID: {ARTIFACT_ID}; ZIP SHA-256: {ZIP_SHA256}\n- Original JSON SHA-256: {jhash}\n- Exact source commit: {SOURCE_COMMIT}\n- Reconstructed SFHo-18.8 profile SHA-256: {PROFILE_SHA256} (not raw Garching data)\n\n"+f"The JSON contains {len(grid)} grid nodes and {len(mids)} direct cell-midpoint evaluations. The long-form CSV has {(len(grid)+len(mids))*6} rows, retaining both muon charges and all three polarization modes separately.\n\n## Numerical acceptance (preserved, not promoted)\n\n"+f"- Detailed-balance maximum residual: {a['maximum_mode_detailed_balance_relative_residual']:.6g} (tolerance {a['detailed_balance_tolerance']:.3g}): PASS.\n- Final-muon mass-shell maximum residual: {a['maximum_final_muon_mass_shell_relative_error']:.6g} (tolerance {a['mass_shell_tolerance']:.3g}): PASS.\n- Local emissivity energy-order change: {a['maximum_local_emissivity_energy_order_change']:.6g}: PASS.\n- Grid-node quadrature refinement maximum: {a['maximum_grid_node_final_refinement_change']:.6g} (target {a['quadrature_relative_tolerance']:.3g}): FAIL.\n- Cell-midpoint refinement maximum: {a['maximum_cell_midpoint_final_refinement_change']:.6g}: FAIL.\n- Direct midpoint versus interpolation maximum: {a['maximum_direct_midpoint_vs_sequential_log_interpolation_error']:.6g} (target {a['interpolation_relative_tolerance']:.3g}): FAIL.\n\n**Overall P1-B local-kernel acceptance remains NOT PASSED.** This is not a B.2 optical-depth calculation, full Fig. 7 transport reproduction, or SN1987A constraint. No opacity rescaling or axial-vector limit update is authorized.\n",encoding="utf-8")
 return {"status":"ARCHIVED_EVIDENCE_ONLY_NUMERICAL_ACCEPTANCE_FAILED","source_run_id":RUN_ID,"source_artifact_id":ARTIFACT_ID,"source_branch":SOURCE_BRANCH,"source_commit":SOURCE_COMMIT,"input_json_file":input_json.name,"input_json_sha256":jhash,"artifact_zip_sha256":ZIP_SHA256,"profile_sha256":PROFILE_SHA256,"grid_nodes":len(grid),"cell_midpoints":len(mids),"csv_rows":(len(grid)+len(mids))*6,"source_git_blob_sha1":SOURCE_BLOBS,"source_sha256":d["source_sha256"],"acceptance":a,"outputs":{p.name:sha(p) for p in (csvp,gsvg,isvg,readmep)}}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("--input",required=True);p.add_argument("--output-dir",required=True);a=p.parse_args()
 m=build(a.input,a.output_dir);(Path(a.output_dir)/"MANIFEST.json").write_text(json.dumps(m,indent=2,sort_keys=True)+"\n",encoding="utf-8");print(json.dumps(m,indent=2,sort_keys=True))
if __name__=="__main__":main()
