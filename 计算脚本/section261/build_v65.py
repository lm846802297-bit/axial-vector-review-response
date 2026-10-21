from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

root=Path(__file__).resolve().parents[2]
work=Path(__file__).resolve().parent
out=root/"计算脚本"/"计算输出"
source_out=Path("C:/Users/84680/Documents/Codex/2026-10-19/referenced-chatgpt-conversation-this-is-an-2/outputs")
stem="higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)"
baseline_source=source_out/(stem+"(64).md")
baseline=root/(stem+"(64).md")
target=root/(stem+"(65).md")
original=root/(stem+"(53).md")
original_expected="6f14ea4a0f31df1c7809325719b952dcb914261938288e3bb84dd89fc01846c5"
sha=lambda b:hashlib.sha256(b).hexdigest()
old_report=json.loads((source_out/"version64_validation.json").read_text(encoding="utf-8-sig"))
base_bytes=baseline_source.read_bytes()
base_hash=sha(base_bytes)
assert base_hash==old_report["output_sha256"]
assert baseline.read_bytes()==base_bytes
original_report=json.loads((source_out/"version54_validation.json").read_text(encoding="utf-8-sig"))
original_bytes=base_bytes[:original_report["baseline_bytes"]]
assert sha(original_bytes)==original_expected
original_file_present=original.exists()
if original_file_present:
    assert original.read_bytes()==original_bytes
assert "## 第 261 节：" not in base_bytes.decode("utf-8-sig")

code=(work/"check_section261.py").read_text(encoding="utf-8")
wl=(work/"section261_mathematica.wl").read_text(encoding="utf-8")
native_wl_log=work/"section261_mathematica_checks.txt"
wl_stdout=native_wl_log.read_text(encoding="utf-8-sig")
assert "ENGINE 14.2.0 for Microsoft Windows (64-bit)" in wl_stdout
assert "RESULT: 25 Mathematica symbolic checks passed" in wl_stdout
assert len(re.findall(r"^PASS \d+ ",wl_stdout,flags=re.M))==25
assert not any(token in wl_stdout for token in ["FAIL ","Syntax::","Set::","SetDelayed::","Series::"])
appendix=(work/"section261.md").read_text(encoding="utf-8")
fence=chr(96)*3
markers={"<!-- SECTION261_REPRODUCE_CODE -->":("python",code),
         "<!-- SECTION261_MATHEMATICA_CODE -->":("mathematica",wl)}
assert not any(ord(ch)<32 and ch not in "\n\t" for ch in appendix)
for a,b in [(r"\[",r"\]"),(r"\(",r"\)")]:
    assert appendix.count(a)==appendix.count(b),(a,b)
formulas=re.findall(r"\\\[(.*?)\\\]|\\\((.*?)\\\)",appendix,flags=re.S)
for display,inline in formulas:
    depth=0
    for token in re.findall(r"\\[{}]|[{}]",display or inline):
        if token=="{":depth+=1
        elif token=="}":depth-=1
        assert depth>=0,display or inline
    assert depth==0,display or inline
assert len(formulas)>120,len(formulas)
subsections=re.findall(r"^### (261\.\d+) ",appendix,flags=re.M)
assert subsections==[f"261.{i}" for i in range(1,13)]
assert sum(line.startswith("~~~") or line.startswith(fence) for line in appendix.splitlines())%2==0
for required in ["第 65 版新增","第 262 节","59 exact broken-phase checks passed",
                 "25 Mathematica symbolic checks passed","局域","极点","资料库"]:
    assert required in appendix,required
for marker,(lang,source) in markers.items():
    assert appendix.count(marker)==1
    appendix=appendix.replace(marker,fence+lang+"\n"+source.rstrip()+"\n"+fence+"\n")

def copy_exclusive_or_verify(source,dest):
    payload=source.read_bytes()
    if dest.exists():
        assert dest.read_bytes()==payload,("refused overwrite",str(dest))
    else:
        with dest.open("xb") as handle:handle.write(payload)
    return sha(payload)

out.mkdir(exist_ok=True)
assert not target.exists()
assert baseline.read_bytes()==base_bytes
attachment_hashes={}
for src in sorted(source_out.iterdir()):
    if src.suffix in [".py",".txt",".json"]:
        attachment_hashes[src.name]=copy_exclusive_or_verify(src,out/src.name)
checker=out/"section261_reproduce.py"
wl_file=out/"section261_mathematica.wl"
wl_log=out/"section261_mathematica_checks.txt"
log_path=out/"section261_checks.txt"
report_path=out/"version65_validation.json"
for p in [checker,wl_file,wl_log,log_path,report_path]:
    assert not p.exists(),str(p)
with checker.open("x",encoding="utf-8",newline="\n") as h:h.write(code)
copy_exclusive_or_verify(work/"section261_mathematica.wl",wl_file)
copy_exclusive_or_verify(native_wl_log,wl_log)
run=subprocess.run([sys.executable,str(checker)],capture_output=True,text=True,encoding="utf-8",check=True)
assert not run.stderr,run.stderr
assert "RESULT: 59 exact broken-phase checks passed; 3 independent diagonalization cases and 3 truncation-scaling cases passed" in run.stdout
for pattern,n in [(r"^PASS \d+ ",59),(r"^NUMERIC ",3),(r"^ORDER ",3)]:
    assert len(re.findall(pattern,run.stdout,flags=re.M))==n
with log_path.open("x",encoding="utf-8",newline="\n") as h:h.write(run.stdout)
payload=base_bytes+appendix.encode("utf-8")
with target.open("xb") as h:h.write(payload)
assert target.read_bytes()==payload
assert payload.startswith(baseline.read_bytes())
if original_file_present:
    assert sha(original.read_bytes())==original_expected
assert sha(baseline_source.read_bytes())==base_hash
final=payload.decode("utf-8-sig")
assert final.count("## 第 261 节：")==1
for marker,(lang,source) in markers.items():
    assert marker not in final
    assert fence+lang+"\n"+source.rstrip()+"\n"+fence in final
for sec in range(250,261):
    previous=(out/f"section{sec}_reproduce.py").read_text(encoding="utf-8-sig").rstrip()
    assert fence+"python\n"+previous+"\n"+fence in final
assert sorted(p.name for p in root.glob(stem+"(*).md"))==sorted([target.name,baseline.name])
report={
 "client_date":"2026-10-20","output_version":65,"backup_version":64,
 "output_path":str(target),"baseline_path":str(baseline),
 "baseline_source_at_build":str(baseline_source),
 "output_bytes":len(payload),"appendix_bytes":len(appendix.encode("utf-8")),
 "output_sha256":sha(payload),"backup_sha256":sha(baseline.read_bytes()),
 "v64_is_exact_byte_prefix_of_v65":True,"desktop_v53_is_exact_byte_prefix_of_v65":True,
 "v53_original_content_prefix_bytes":len(original_bytes),
 "v53_original_content_prefix_sha256_verified":original_expected,
 "desktop_v53_file_present_at_build":original_file_present,
 "desktop_v64_backup_sha256_verified_unchanged":base_hash,
 "section261_subsections":subsections,"math_expressions_checked":len(formulas),
 "math_delimiters_braces_code_fences_balanced":True,
 "no_unexpected_control_characters":True,
 "python_engine":sys.version.split()[0],"python_exact_symbolic_checks":59,
 "independent_numeric_diagonalization_cases":3,"truncation_scaling_cases":3,
 "mathematica_run":True,
 "mathematica_version":"14.2.0 for Microsoft Windows (64-bit) (December 26, 2024)",
 "mathematica_system_id":"Windows-x86-64",
 "mathematica_symbolic_checks":25,
 "mathematica_exit_code":0,
 "mathematica_log_captured_from_actual_native_run":True,
 "mathematica_initial_sandbox_configuration_access_failed_then_native_run_succeeded":True,
 "python_checker_sha256":sha(checker.read_bytes()),
 "python_log_sha256":sha(log_path.read_bytes()),
 "mathematica_checker_sha256":sha(wl_file.read_bytes()),
 "mathematica_log_sha256":sha(wl_log.read_bytes()),
 "embedded_python_and_mathematica_sources_equal_delivered_files":True,
 "all_250_to_260_embedded_python_sources_equal_delivered_files":True,
 "prior_reproduction_attachments_copied_and_hash_verified":attachment_hashes,
 "local_mass_and_angle_only":True,"light_field_pole_self_energies_evaluated":False,
 "numerical_cases_are_model_benchmarks":False,
 "feynarts_run":False,"feyncalc_run":False,"matchete_run":False,"matchmakereft_run":False,
 "library_updated":False,"main_document_versions_in_current_workspace":[65,64],
 "next_section":262
}
with report_path.open("x",encoding="utf-8") as h:json.dump(report,h,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in report.items() if k!="prior_reproduction_attachments_copied_and_hash_verified"},ensure_ascii=False,indent=2))
