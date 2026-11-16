# Individual review: legacy EFT calculation notes and audit artifacts

Reviewed commit: `28916f7452cfcd98da032cbd05cd487c1acac892` (2026-11-15). This batch covers three generated calculation artifacts and three historical review artifacts in `计算脚本/`. It does not endorse a complete UV–EFT matching result or a model-level pole prediction.

| Document | Outcome | Findings and disposition |
|---|---|---|
| `计算脚本/derive_raw_minkowski_numerator_output.txt` | `PASS_WITH_NOTES` | The paired source `derive_raw_minkowski_numerator.py` explicitly defines the (+---) metric, vertex ordering and boundary of scope. Re-executed the source with only its output path redirected to `/tmp`; the generated 16-mask output is byte-identical to this file (SHA-256 `a03e5f799fedd186626b3fefa8ace3ebb0eadc3b17fccab4874d9d659a45d433`). This validates the exported symbolic trace payload and odd-slash checks, not model-specific vertex orientation, Wick rotation, loop integration or matching. Retain beside its source; link the source and this scope in any future index. |
| `计算脚本/section261/section261.md` | `PASS_WITH_NOTES` | Read the complete note and reran `python 计算脚本/section261/check_section261.py`: 59 exact checks, three diagonalization controls and three truncation-scaling controls pass. Its distinction between a local curvature/mixing angle and a physical pole is stated consistently, as are the fixed-VEV versus shifted-VEV input choices and the (M^{-2}) boundary. The dimensionless controls are not physical benchmark points; no full matching, gauge-complete pole or phenomenology is established. Keep as a dated research snapshot, not a finished prediction. |
| `计算脚本/section262/section262.md` | `PASS_WITH_NOTES` | Read the complete note and reran `python 计算脚本/section262/check_section262.py`: 62 exact checks, eight (B_0) integrals, three derivative integrals and three massless-limit controls pass. The note separates strict (M^{-2}) terms from retained higher-order light-mass pieces and explicitly requires additional sectors/input-scheme work before a full pole result. The Mathematica run is recorded in a historical log, but was not rerun here. Treat the Python checks as scoped implementation evidence, not an independent full diagram calculation. |
| `计算脚本/审计结果/DeepSeek66/DeepSeek第66版独立审计-20261020.md` | `HISTORICAL` | This is an archived critique of a separate 2026-10-20 v66 manuscript continuation, not the current section261/section262 pair. It records concrete counterexamples and also states that the exact source manuscript and full Mathematica evidence were not present in that handoff. Its absolute Windows paths are not portable, and its final numerical score is subjective rather than an auditable criterion. Preserve as a dated opinion/evidence record; do not treat it as the current model decision or as independently reproducible proof. |
| `计算脚本/审计结果/DeepSeek66/deepseek_assertions_rerun.txt` | `HISTORICAL` | The 73 printed assertions are an archived run record. The file itself says the historical rerun block was not executed; the separate review notes that at least 14 assertions compare identical expressions. No current rerun or independent verification is claimed. Retain as provenance for the 2026-10-20 audit only. |
| `计算脚本/审计结果/DeepSeek66/independent_review_checks.txt` | `HISTORICAL` | Archived Mathematica output reports seven verified identities, twelve counterexamples and three (B_0) integrals. The corresponding complete `.wl` source is referenced at a local Windows path and is not present in this repository, so the output is not independently reproducible from the current checkout. Retain as a historical result; do not use its output alone as a current calculation source. |

## Reproduction and file checks

The three local Python reruns exited zero in the current environment. The symbolic-output comparison was byte-for-byte exact. The two DeepSeek text logs were inspected as archived outputs and were not re-executed because their corresponding audit sources are not included here. No files were moved or deleted in this batch.

## Remaining limitation

The local section261/section262 scripts validate their declared symbolic and numerical subproblems. They do not establish that all diagrams, counterterms, gauge/Goldstone/ghost contributions, input conversions or detector observables are complete. Preserve those limitations in any navigation summary.


## Independent follow-up (2026-11-16)

**Current disposition: PASS_WITH_NOTES.** All six documents in the original table exist in the current tree. The paired source, checker and historical log files discussed below are also present. This follow-up corrects one false source-availability statement, adds two reproducibility qualifications, and preserves the original 2026-11-15 review as a dated record.

### 1. Minkowski numerator export

- The paired source \`计算脚本/derive_raw_minkowski_numerator.py\` is present. It constructs explicit four-dimensional Dirac matrices for metric \((+---)\), uses four independently labelled chiral vertices \(\Gamma_i=u_iP_R+v_iP_L\), and expands all \(2^4=16\) slash/mass masks in the stated order \(\Gamma_1N_1\Gamma_2N_2\Gamma_3N_3\Gamma_4N_4\). It asserts the odd-slash masks vanish.
- The current \`derive_raw_minkowski_numerator_output.txt\` has SHA-256 \`a03e5f799fedd186626b3fefa8ace3ebb0eadc3b17fccab4874d9d659a45d433\`, matching the digest recorded in the original review.
- **Portability note:** the checked-in generator writes to the hard-coded absolute path \`/mnt/data/derive_raw_minkowski_numerator_output.txt\`. The original review redirected this path for its comparison run; a clean Windows checkout or ordinary Linux checkout may not have \`/mnt/data\`. Before treating this as a portable reproduction command, change the default to a path relative to \`__file__\` or expose an output-path argument.
- This remains raw trace algebra only. It does not attach the model-specific vertex orientation/conjugations, perform loop integration, Wick rotation, UV–EFT matching, or a physical pole calculation.

### 2. Section 261/262 checker scope

- The Section 261 checker contains 59 dynamically executed exact-check calls after its loop expansions, plus three numerical diagonalization comparisons and three truncation-scaling cases. Its separate Mathematica log records 25 symbolic checks. The source itself explicitly says light-field pole self-energies have not yet been evaluated.
- The Section 262 checker contains 62 dynamically executed exact-check calls after loop expansions, plus eight \(B_0\) quadratures, three derivative-integral checks and three massless-limit cases. Its Mathematica log records 25 symbolic checks and six high-precision \(B_0\) integrals.
- The checker code and Mathematica logs are present. This follow-up inspected their declarations and scope but did **not** re-execute the Python or Mathematica programs. The original report's local Python exit-zero statement remains attributed to that dated run, not a new execution in this follow-up.
- These are implementation/algebra controls for the declared broken-phase EFT subproblems. They do not supply the missing scalar, gauge/Goldstone/ghost sectors, full same-order matching/counterterms, complete input/tadpole scheme, or a physical gauge-independent pole.

### 3. DeepSeek66 source-availability correction

The original table's final row said that the corresponding complete Mathematica \`.wl\` source was not present in the repository. **That statement is incorrect.** The exact path \`计算脚本/审计结果/DeepSeek66/independent_review.wl\` exists, as does \`independent_review_checks.txt\`; both files were already present at the review-report creation commit \`c7e2c5b58389c7c9f2720703b29cba240cce907f\`. The source and log are co-located in the current checkout:

- [Mathematica source](../../计算脚本/审计结果/DeepSeek66/independent_review.wl)
- [Recorded independent-review output](../../计算脚本/审计结果/DeepSeek66/independent_review_checks.txt)
- [73-assertion Python source](../../计算脚本/审计结果/DeepSeek66/deepseek_assertions_only.py)
- [73-assertion historical run log](../../计算脚本/审计结果/DeepSeek66/deepseek_assertions_rerun.txt)
- [Machine-readable audit evidence](../../计算脚本/审计结果/DeepSeek66/audit_evidence.json)

The Mathematica log records seven independent symbolic identities, twelve counterexamples and three \(B_0\) integrals. The Python log contains 73 PASS lines but explicitly states that the historical recursive rerun block was not executed; the machine-readable evidence records 14 calls whose actual and expected ASTs are identical. The source is therefore available, but the old Python PASS block is not proof that the recursive history rerun occurred. This follow-up did not re-run Mathematica 14.2 or the Python assertion script. The absolute Windows paths embedded in the 2026-10-20 DeepSeek report remain non-portable historical references; the repository-relative links above provide the current checkout paths.

### 4. Review-base provenance

The header's declared reviewed commit \`28916f7452cfcd98da032cbd05cd487c1acac892\` could not be resolved through this repository's commit endpoint or commit search. The review report itself was added by commit \`c7e2c5b58389c7c9f2720703b29cba240cce907f\`. Do not silently replace the declared reviewed commit with the report commit; the intended source-repository/base identity remains an unresolved provenance field.

### 5. Scientific boundary

No source calculation, section261/262 output, DeepSeek conclusion, model parameter, UV–EFT coefficient, scalar pole, collider constraint, stellar-cooling result or manuscript text was changed by this follow-up. The DeepSeek artifacts remain historical audit material; the Section 261/262 tests remain scoped subcalculation checks, not complete physical validation.
