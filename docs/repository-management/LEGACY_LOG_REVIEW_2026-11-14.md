# Legacy calculation-log review — 2026-11-14

Review base: `7c0d0521a3f780ef7a2e98d3ab0751a20cb7a2e6`. Read and classified 17 historical text logs: the Python section 250–262 outputs and two Mathematica logs, each of which also has a byte-identical section-directory copy. The review checks role, declared scope, result summaries and available provenance. Python reruns performed afterward are recorded below; this is not an independent loop derivation or acceptance of a current Higgs–singlet prediction.

| Historical log | Review observation |
|---|---|
| [计算脚本/计算输出/section250_checks.txt](../../计算脚本/计算输出/section250_checks.txt) | 56 checks; selected rational algebra, chiral traces and EOM; log explicitly excludes an automatic diagram census. |
| [计算脚本/计算输出/section251_checks.txt](../../计算脚本/计算输出/section251_checks.txt) | 59 exact checks and 3 decimal cases; constant-background determinant and selected vector merge; no FeynArts/FeynCalc run. |
| [计算脚本/计算输出/section252_checks.txt](../../计算脚本/计算输出/section252_checks.txt) | 46 exact checks on off-shell scalar amplitudes; no numerical integration or external diagram generator. |
| [计算脚本/计算输出/section253_checks.txt](../../计算脚本/计算输出/section253_checks.txt) | 68 exact checks and 3 numerical integrals; unbroken-phase heavy Dirac vector-current scope. |
| [计算脚本/计算输出/section254_checks.txt](../../计算脚本/计算输出/section254_checks.txt) | 68 exact checks and 3 neutral-background cases; CP-even two-scalar/two-gauge hard projection only. |
| [计算脚本/计算输出/section255_checks.txt](../../计算脚本/计算输出/section255_checks.txt) | 47 exact checks and 6 numerical cases; Yukawa light-fermion two-point and EOM subset. |
| [计算脚本/计算输出/section256_checks.txt](../../计算脚本/计算输出/section256_checks.txt) | 62 exact checks, 3 integrals and 3 hard limits; selected C5 matching, no external diagram generator. |
| [计算脚本/计算输出/section257_checks.txt](../../计算脚本/计算输出/section257_checks.txt) | 58 exact checks, 3 integrals and 3 hard limits; scalar/Yukawa matching, gauge exchange separate. |
| [计算脚本/计算输出/section258_checks.txt](../../计算脚本/计算输出/section258_checks.txt) | 74 exact checks, 6 integrals and 3 IR limits; off-shell gauge vertex and current-projection subset. |
| [计算脚本/计算输出/section259_checks.txt](../../计算脚本/计算输出/section259_checks.txt) | 53 exact checks, 9 integrals and 6 hard limits; explicitly records two printed-reference discrepancies, not agreement. |
| [计算脚本/计算输出/section260_checks.txt](../../计算脚本/计算输出/section260_checks.txt) | 69 exact assembly checks; historical ledger reports reruns of 250-259 and matches their current script/log hashes; no new diagram census. |
| [计算脚本/计算输出/section261_checks.txt](../../计算脚本/计算输出/section261_checks.txt) | 59 exact checks and 6 algebra/truncation controls; dimensionless cases are not a physical benchmark, and light-field pole self-energies were not evaluated. |
| [计算脚本/计算输出/section262_checks.txt](../../计算脚本/计算输出/section262_checks.txt) | 62 exact checks plus 8 B0, 3 derivative and 3 massless-limit controls; selected soft terms do not establish complete dimension-eight matching. |
| [计算脚本/计算输出/section261_mathematica_checks.txt](../../计算脚本/计算输出/section261_mathematica_checks.txt) | Historical Mathematica 14.2 Windows log: 25 symbolic checks; output and section-directory duplicate are byte-identical. No loop-diagram package was run. |
| [计算脚本/section261/section261_mathematica_checks.txt](../../计算脚本/section261/section261_mathematica_checks.txt) | Historical Mathematica 14.2 Windows log: 25 symbolic checks; output and section-directory duplicate are byte-identical. No loop-diagram package was run. |
| [计算脚本/计算输出/section262_mathematica_checks.txt](../../计算脚本/计算输出/section262_mathematica_checks.txt) | Historical Mathematica 14.2 Windows log: 25 symbolic checks and 6 B0 integrals; output and section-directory duplicate are byte-identical. No loop-diagram package was run. |
| [计算脚本/section262/section262_mathematica_checks.txt](../../计算脚本/section262/section262_mathematica_checks.txt) | Historical Mathematica 14.2 Windows log: 25 symbolic checks and 6 B0 integrals; output and section-directory duplicate are byte-identical. No loop-diagram package was run. |

## Integrity and boundaries

- The section 260 log contains 10 SHA-256 pairs for the section 250–259 Python scripts and archived logs. All 20 hashes were recomputed against this checkout and match. Each PASS-line count also matches its log's stated exact-check count.
- The two section 261 Mathematica script/log files and the corresponding section 262 files are byte-identical between `计算脚本/sectionNNN/` and `计算脚本/计算输出/`. Both copies remain because they belong to separately documented historical work and delivery paths.
- Section 259 specifically records two discrepancies relative to printed reference expressions; its “PASS” lines include checks that the discrepancies are nonzero. Do not summarize that log as complete agreement with the references.
- Sections 261 and 262 use dimensionless controls or selected soft terms, and explicitly do not establish a complete physical spectrum or dimension-eight matching. The two Mathematica logs report version 14.2 on Windows and no loop package; Mathematica was not run during this review.
- The historical exact counts and recorded software version describe those logs. Their integrity is not an independent verification of the derivations or of every present project decision.

## Local rerun after review

The 12 Python scripts for sections 250–259 and 261–262 were run in Python 3.12.14. All exited zero. Ten reproduced the archived stdout after suppressing only the dynamic `Python:` version line. Sections 253 and 262 differed in displayed floating-point residuals: section 253's one residual changed by about 8.67e-19, and section 262's maximum displayed closed-form error in this run was 8.916e-15. Their displayed main integral values and exact PASS lines remained the same. These are same-implementation checks, not independent physical re-derivations.

Section 260 was also run: its first 69 PASS lines match the historical log, then it exited 1 while comparing section 250 stdout byte-for-byte with its archive. The first difference is the embedded interpreter version (`3.12.14` locally versus archived `3.14.7`). Its strict full-stdout check is therefore environment-sensitive; moreover, the separately observed 253/262 residual differences show why dropping the version line alone is not a complete portable-comparison strategy. No historical script or log was modified. Mathematica was not run.

Reproduce from the repository root with `python 计算脚本/整理记录/audit_section_logs_2026_11_14.py > 计算脚本/整理记录/section_log_rerun_2026-11-14.json`. The [rerun JSON](../../计算脚本/整理记录/section_log_rerun_2026-11-14.json) records exits, archived/script SHA-256 values, equality flags and the section-260 failure. [Checksum manifest](../../计算脚本/整理记录/section_log_rerun_2026-11-14_SHA256SUMS.txt) identifies the orchestration script and JSON. Do not overwrite the historical logs with local output.


## 2. Independent current-tree audit (2026-11-16)

**Disposition of this review report: PASS_WITH_NOTES.** The 17-log inventory, the ten section-250–259 script/log fingerprint pairs, the Mathematica duplicate copies, the PASS-line counts and the explicitly retained section-259 reference discrepancies were independently checked. The following provenance gaps are added to prevent the historical rerun record from being overstated.

### 2.1 Checks independently confirmed

- The 17 historical text logs consist of the 13 section250–section262 output logs plus the four section261/262 Mathematica script/log copies. The section261 and section262 Mathematica source/log pairs are byte-identical between their section directories and the calculation-output directory.
- All 20 SHA-256 values for the section250–section259 Python scripts and archived text logs, as recorded in section260_checks.txt, were recomputed from the current maintenance-branch files and match.
- PASS-line counts match the stated exact-check counts for sections250–259 and 261–262. The section261 and section262 Mathematica logs each contain 25 PASS lines, identify Mathematica 14.2.0 for Windows 64-bit, and explicitly state that no loop-diagram package was loaded.
- Section259 still records the two nonzero reference discrepancies: \(25/216\) for the printed-minus-own Eq. 6.40 constant, and the printed \(-8/135\) versus the implementation's \(+8/135\) for Eq. 6.31. They are not counted as agreements.
- The rerun JSON records 12 Python runs with exit code zero. Ten stdout comparisons pass after removal of the dynamic Python-version line; sections253 and262 retain the documented small displayed floating-point residual differences. The section260 aggregate log has 69 PASS lines before its strict archived-stdout comparison fails at section250. The failure is a version-sensitive exact-output comparison (historical Python 3.14.7 versus rerun Python 3.12.14), not a failed symbolic PASS assertion.

### 2.2 Rerun source-fingerprint gaps

The 2026-11-14 SHA256SUMS file does not match the current committed bytes of the two files it names:

| File | SHA-256 listed in historical manifest | SHA-256 of current Git file |
|---|---|---|
| audit_section_logs_2026_11_14.py | 42402ef81ee459dc62b09a01202f3fcd3494d44c6260ae345db635021ac45001 | 9a4a45cc32bd6a27da613db97cad28c19d9e0c48836aad7f0d83f94685afe830 |
| section_log_rerun_2026-11-14.json | af2f0326479d134cf5c3a6600914bf33b9b15a6d09ee6a12060f7821ab3bf7d4 | 29c838c60f3aa3238c4f4c7c983e508144a38200f7b819630e92fa8974b4f0b1 |

The section261/262 entries in the rerun JSON also do not fingerprint the corresponding tracked files:

| Section/file | SHA in rerun JSON | Current Git-file SHA-256 |
|---|---|---|
| 261 reproduce script | 199fee49595f1623523dfbe76689a8a46bef08db85fef4cf7b99c20a4102ef82 | db8419d07098f3025ac8ef8448007e634bfcf61d481d336e85ff2217f3fb7799 |
| 261 archived log | 79999d7d0fef3fb8f4b03bb9e475a054bf9b3d48fe2a4a8cd07f30aa2b96db00 | 8381442ac971e231d151e3174aa10d5205446ba8535e530e8cc6cb959037cdc8 |
| 262 reproduce script | 07ca907b58cad437e9bc1dca5fb3e97a1bb909dcc73ff3ca8ac46d8af0813f5c | ffd9c80d0814312615e617f0d39247cc8206eb30a50625139a8ef78d55633b94 |
| 262 archived log | 0c1ed3b3988d2985e0a57765680d5ce5cb88b0f877a5a6d16011f93b64bab353 | dc8d2044fca2652b37cbe824374c00617099b7998dabdb1f60b60bc6b3ade7e2 |

These mismatches persist when the files are read at the report's stated review base and at the commit that added the rerun JSON/manifest. The committed rerun driver points to the tracked section261/262 reproduce paths, so the JSON's hashes do not currently establish byte identity with those paths. The later 31st review's check_section261.py and check_section262.py executions are separate scripts; they do not repair the provenance of this earlier 12-script rerun record.

A new file, section_log_rerun_current_SHA256SUMS_2026-11-16.txt, was added. It pins the current maintenance-branch bytes for the rerun driver/JSON and section260–262 scripts/logs. It is explicitly a current-tree manifest, not a replacement for the historical manifest and not evidence of which local files produced the original rerun.

### 2.3 Scientific boundary

The 250–259 hash-pinned script/log pairs and the recorded exact symbolic PASS counts are reproducible from the current tree. The 261/262 historical rerun source bytes and the old rerun-driver/JSON manifest remain unverified. Section260's strict comparison remains an environment/output-format failure after 69 symbolic assembly checks, not a new physics failure. Section259's two printed-reference discrepancies remain explicit.

The section261/262 Mathematica checks are dimensionless algebra controls; they do not compute light-field pole self-energies or a phenomenological scalar spectrum. None of these logs establishes a complete gauge-independent \(h-s\) complex pole, complete UV–EFT matching, or a final Higgs-constraint recast. No historical calculation log, production coefficient, model input or physical constraint was modified.
