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
