from pathlib import Path
import hashlib,json,re,subprocess,sys

work=Path(__file__).resolve().parent
root=work.parents[1]
out=root/"计算脚本"/"计算输出"
stem="higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)"
baseline=root/(stem+"(65).md")
target=root/(stem+"(66).md")
older=root/(stem+"(64).md")
old_report=json.loads((out/"version65_validation.json").read_text(encoding="utf-8"))
sha=lambda b:hashlib.sha256(b).hexdigest()
base=baseline.read_bytes();old=older.read_bytes()
assert sha(base)==old_report["output_sha256"]
assert sha(old)==old_report["backup_sha256"]
assert base.startswith(old)
v53=base[:old_report["v53_original_content_prefix_bytes"]]
assert sha(v53)==old_report["v53_original_content_prefix_sha256_verified"]
assert "## 第 262 节：" not in base.decode("utf-8-sig")

code=(work/"check_section262.py").read_text(encoding="utf-8")
wl=(work/"section262_mathematica.wl").read_text(encoding="utf-8")
wl_raw=(work/"section262_mathematica_checks.txt").read_bytes()
wl_stdout=wl_raw.decode("utf-8-sig")
assert "ENGINE 14.2.0 for Microsoft Windows (64-bit)" in wl_stdout
assert "RESULT: 25 Mathematica symbolic checks passed; 6 high-precision B0 integrals passed" in wl_stdout
assert len(re.findall(r"^PASS \d+ ",wl_stdout,flags=re.M))==25
assert len(re.findall(r"^INTEGRAL ",wl_stdout,flags=re.M))==6
assert not any(x in wl_stdout for x in ["FAIL","Syntax::","NIntegrate::","Set::","General::"])

appendix=(work/"section262.md").read_text(encoding="utf-8")
assert not any(ord(x)<32 and x not in "\n\t" for x in appendix)
for a,b in [(r"\[",r"\]"),(r"\(",r"\)")]:
    assert appendix.count(a)==appendix.count(b),(a,b,appendix.count(a),appendix.count(b))
formulas=re.findall(r"\\\[(.*?)\\\]|\\\((.*?)\\\)",appendix,flags=re.S)
for display,inline in formulas:
    expr=display or inline;depth=0
    for token in re.findall(r"\\[{}]|[{}]",expr):
        if token=="{":depth+=1
        elif token=="}":depth-=1
        assert depth>=0,expr
    assert depth==0,expr
assert len(formulas)>150,len(formulas)
subsections=re.findall(r"^### (262\.\d+) ",appendix,flags=re.M)
assert subsections==[f"262.{i}" for i in range(1,13)]
fence=chr(96)*3
assert sum(l.startswith(fence) or l.startswith("~~~") for l in appendix.splitlines())%2==0
for needle in ["第 66 版新增","第 263 节","62 exact light-fermion checks passed",
               "25 Mathematica symbolic checks passed","维数八","接触图","tadpole","资料库"]:
    assert needle in appendix,needle
sources={"<!-- SECTION262_REPRODUCE_CODE -->":("python",code),
         "<!-- SECTION262_MATHEMATICA_CODE -->":("mathematica",wl)}
for marker,(lang,source) in sources.items():
    assert appendix.count(marker)==1
    appendix=appendix.replace(marker,fence+lang+"\n"+source.rstrip()+"\n"+fence+"\n")

checker=out/"section262_reproduce.py"
wl_path=out/"section262_mathematica.wl"
wl_log=out/"section262_mathematica_checks.txt"
log=out/"section262_checks.txt"
report_path=out/"version66_validation.json"
for path in [target,checker,wl_path,wl_log,log,report_path]:
    assert not path.exists(),f"exclusive create refused {path}"
with checker.open("x",encoding="utf-8",newline="\n") as h:h.write(code)
with wl_path.open("x",encoding="utf-8",newline="\n") as h:h.write(wl)
with wl_log.open("xb") as h:h.write(wl_raw)
run=subprocess.run([sys.executable,str(checker)],capture_output=True,text=True,encoding="utf-8",check=True)
assert not run.stderr,run.stderr
assert "RESULT: 62 exact light-fermion checks passed; 8 B0 integrals, 3 derivative integrals and 3 massless-limit cases passed" in run.stdout
for regex,n in [(r"^PASS \d+ ",62),(r"^B0_INTEGRAL ",8),(r"^DERIVATIVE ",3),(r"^MASSLESS_LIMIT ",3)]:
    assert len(re.findall(regex,run.stdout,flags=re.M))==n,regex
with log.open("x",encoding="utf-8",newline="\n") as h:h.write(run.stdout)
payload=base+appendix.encode("utf-8")
with target.open("xb") as h:h.write(payload)
readback=target.read_bytes()
assert readback==payload and readback.startswith(base)
assert sha(baseline.read_bytes())==old_report["output_sha256"]
assert sha(older.read_bytes())==old_report["backup_sha256"]
final=payload.decode("utf-8-sig")
assert final.count("## 第 262 节：")==1
for marker,(lang,source) in sources.items():
    assert marker not in final
    assert fence+lang+"\n"+source.rstrip()+"\n"+fence in final
for sec in range(250,262):
    old_code=(out/f"section{sec}_reproduce.py").read_text(encoding="utf-8-sig").rstrip()
    assert fence+"python\n"+old_code+"\n"+fence in final,sec
report={
 "client_date":"2026-10-20","output_version":66,"backup_version":65,
 "output_path":str(target),"backup_path":str(baseline),
 "output_bytes":len(payload),"appendix_bytes":len(appendix.encode("utf-8")),
 "output_sha256":sha(payload),"backup_sha256":sha(base),
 "v65_exact_byte_prefix_of_v66":True,
 "v53_original_content_prefix_sha256_verified":sha(v53),
 "section262_subsections":subsections,"math_expressions_checked":len(formulas),
 "math_delimiters_braces_code_fences_balanced":True,"control_characters_checked":True,
 "python_version":sys.version.split()[0],"python_exact_checks":62,
 "python_B0_parameter_integrals":8,"python_derivative_integrals":3,
 "python_Decimal50_massless_limit_cases":3,
 "python_numerical_method":"16384-segment Simpson; quartic endpoint map; split at light threshold roots",
 "mathematica_run":True,"mathematica_version":"14.2.0 for Microsoft Windows (64-bit) (December 26, 2024)",
 "mathematica_exact_checks":25,"mathematica_B0_cases":6,
 "mathematica_NIntegrate_real_calls":6,"mathematica_NIntegrate_cut_interval_calls":2,
 "mathematica_WorkingPrecision":40,"mathematica_AccuracyGoal":25,"mathematica_PrecisionGoal":25,
 "mathematica_B0_error_assertion":"<1e-23",
 "mathematica_exit_code":0,"mathematica_log_is_captured_native_output":True,
 "checker_sha256":sha(checker.read_bytes()),"python_log_sha256":sha(log.read_bytes()),
 "mathematica_source_sha256":sha(wl_path.read_bytes()),"mathematica_log_sha256":sha(wl_log.read_bytes()),
 "embedded_sources_equal_delivered":True,"prior_250_to_261_embedded_checkers_verified":True,
 "contact_vertex_included":True,"CW_Hessian_and_tadpole_signs_checked":True,
 "dimension6_covariant_counterterm":"-q0*abs(C5)^2*DeltaUV*abs(D(S_l H))^2",
 "dimension8_potential_counterterm":"+q0*abs(C5)^4*DeltaUV*X^2*Y^2",
 "strict_Minv2_result_separated_from_exact_light_mass_soft_function":True,
 "full_dimension8_matching_performed":False,"full_model_pole_spectrum_completed":False,
 "numerical_values_are_model_benchmarks":False,
 "feynarts_run":False,"feyncalc_run":False,"matchete_run":False,"matchmakereft_run":False,
 "library_updated":False,"planned_main_versions":[66,65],
 "older_document_eligible_for_removal":str(older),
 "older_document_sha256_before_removal":sha(old),
 "older_document_exact_content_verified_in_both_retained_versions":True,
 "next_section":263,
 "new_section_line":next(i for i,l in enumerate(final.splitlines(),1) if l.startswith("## 第 262 节："))
}
with report_path.open("x",encoding="utf-8") as h:json.dump(report,h,ensure_ascii=False,indent=2)
print(json.dumps(report,ensure_ascii=False,indent=2))
