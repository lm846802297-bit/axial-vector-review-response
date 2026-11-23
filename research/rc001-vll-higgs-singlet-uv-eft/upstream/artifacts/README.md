# Artifacts

Versioned snapshots of research sources and computational artifacts that are too large, too binary, or too numerous to review line-by-line in ordinary text diffs. Per §8 of the [workflow specification](../docs/scientific-diff-workflow.md), each bundle records provenance, content hashes, and a human-readable summary rather than relying on the diff alone.

Bundles are **immutable**. Adopting a later source revision means adding a new bundle directory, not editing an existing one. Store the required extracted/native files directly inside the bundle; do not create a new ZIP/TAR archive as a substitute for those files. For run-level result submission and large-file alternatives, follow the [calculation-result archival policy](../docs/CALCULATION_RESULT_ARCHIVAL_POLICY.md).

## Bundles

| Bundle | Source version | Linked record | Size | Files |
|---|---|---|---|---|
| [higgs-portal-v66-20261019](higgs-portal-v66-20261019/) | Historical main document v66, dated 2026-10-19 (not the latest research version) | [RC-001](../research/RC-001-vll-higgs-singlet-uv-eft.md) (earlier source generation) | 12,445,122 bytes (12.45 MB) | 138 |

---

## higgs-portal-v66-20261019

A historical snapshot of the local working tree that produced the v66 main document on 2026-10-19. It is committed to provide a stable, hashable provenance trail for the derivations, scripts, audit records, and intermediate outputs associated with that historical state.

> **Historical status and scope caveat.** v66 is **not the latest research version** and must not be treated as the current source of truth. The current research baseline remains v153 as identified in [RC-001](../research/RC-001-vll-higgs-singlet-uv-eft.md); this bundle does not supersede it. This is a working archive, not a validated result set. The v66 document's own opening "unified conclusion status table" governs only the claims it records: any claim marked unresolved, in progress, or not yet verified remains so. Committing a script does not mean its output was independently confirmed, and committing an output does not establish the physical claim built on it.

### Contents

| Path | Contents |
|---|---|
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(66).md` | Main document, v66: reviewer-response route, one-loop \(s\)–\(h\) mixing, UV–EFT matching record, original-paper cross-check, execution plan |
| `work/` | Version-lineage workspace: correction, enhancement, reconstruction, polish, and validation scripts plus the intermediate drafts they produced |
| `work/latex-build/` | Pandoc + LaTeX typesetting attempt: `main.tex`, `main.pdf`, per-page render checks |
| `计算脚本/` | Computational index; see its [README](higgs-portal-v66-20261019/计算脚本/README.md) for the full inventory and the old-to-new path mapping |
| `计算脚本/section261/`, `计算脚本/section262/` | Per-section working sources, Mathematica sources, logs, manuscript fragments |
| `计算脚本/计算输出/` | Reproduction scripts and check logs for §§250–262 |
| `计算脚本/审计结果/DeepSeek66/` | Independent audit of the separate DeepSeek-generated v66 continuation (SHA-256 `5ded5e1f507af552f1b9c666695f3585821455def628ea8eaf00c2c8c91fe9a1`), plus recomputation sources/evidence; **not** an audit of the bundled main document (SHA-256 `082b9add00b2aecbba9e708cda834033b6c8391679d68ed4b86761ed0d464332`) |
| `计算脚本/整理记录/` | Pre/post-relocation SHA-256 manifest and path correspondence |

### Script families in `计算脚本/`

| Family | Role |
|---|---|
| `01`–`05` | Main HiggsPortal verification (pure Mathematica), third-party package run, FeynRules and SARAH model files, HiggsTools constraint scan |
| `audit_*` | Independent checks: Dirac traces per chirality path, Wick rotation signs, six-route geometry coefficients, denominator consistency |
| `build_*` | Pathwise matching integrands, six-cycle weight ledgers, six-labeled orderings |
| `derive_*` | Raw Minkowski numerator derivation and the Minkowski-to-Euclidean \(B\) kernel map |
| `verify_*` | Numerator-to-kernel checks and §245 matching verification |
| `*_verification.json`, `*_output.txt`, `*.csv` | Numerical and symbolic verification outputs retained as evidence |

### Verification status

| Item | Status |
|---|---|
| Document size and SHA-256 | 1,611,984 UTF-8 bytes; `082b9add00b2aecbba9e708cda834033b6c8391679d68ed4b86761ed0d464332` — independently recomputed on 2026-10-23 and matched |
| `计算脚本/section273_feyncalc_threshold_workflow.wl` | `8e2c7a36c5cacecf35194a92cde50e52ec457cb884684c719e5aafc6b67053ab` — annotated FeynArts/FeynCalc scaffold, **not executed** |
| `计算脚本/higgs_portal_threshold_key_result_audit.wl` | `f6a015c87ed01579703ffe1f4d5b5f1b546b670224fbe46e2571d744369473ed` — added after the v66 snapshot's audit chain |
| `计算脚本/run_uv_eft_audit_suite.py` | `ab4967866318d139706ee2fd42d1d2122808fa49687d39825f01196b3434ebb5` — orchestration only; see the B1/B3 sign warning in RC-001 |
| `计算脚本/计算输出/section262_reproduce.py` | `07ca907b58cad437e9bc1dca5fb3e97a1bb909dcc73ff3ca8ac46d8af0813f5c` |
| LaTeX intermediate files | Pruned before commit (`.aux`, `.log`, `.toc`, `.out`, `.fls`, `.fdb_latexmk`, `missfont.log`); `main.pdf` and render checks retained |

The 50 `sha256_after` entries in the relocation manifest and the four smaller-file hashes listed above were independently recomputed against the committed contents and matched. In a follow-up audit on 2026-10-23, the full v66 Markdown blob (Git blob `03b094c34177af4b8e864237290e15f7918f5f5d`) was also independently rehashed: its UTF-8 size is 1,611,984 bytes and its SHA-256 is `082b9add00b2aecbba9e708cda834033b6c8391679d68ed4b86761ed0d464332`, matching the recorded digest. The in-bundle manifest is retained as the original snapshot audit record; this later verification is recorded here and in PR #5. No physics calculation was rerun.

Python reproduction is self-contained per section:

```bash
python 计算脚本/计算输出/section262_reproduce.py
```

Mathematica entries (`01_HiggsPortal_主验算_纯MMA.m`, `section273_feyncalc_threshold_workflow.wl`) require a local Wolfram Engine. The FeynCalc scaffold additionally requires a custom FeynArts model file and a particle-label mapping that are **not** included.

### Version lineage and adoption policy

| Version | Role in this repository | Rule |
|---|---|---|
| **v66** (2026-10-19) | Historical, immutable artifact bundle in this directory | Preserve for provenance; it is not the latest research version and does not replace the active baseline. |
| **v153** | Current research baseline identified by [RC-001](../research/RC-001-vll-higgs-singlet-uv-eft.md) | Use as the baseline for the current record, while retaining its stated unresolved verification gaps. The primary v153 source is identified by its Library metadata and hash in RC-001. |
| **Future versions** | New research candidates, including any version later adopted as the baseline | Record the exact version/date, full filename, source location, byte count, SHA-256, and relationship to the previously adopted baseline. If source files are committed, add a new immutable bundle directory; never overwrite v66. Update RC-001 only when the new source is deliberately adopted, and record the substantive diff and evidence status. |

The version labels establish chronology and source identity, not scientific validity. The v66 archive alone does not prove byte-for-byte ancestry or scientific equivalence with v153. Hash agreement establishes file integrity only; it does not close any physics-verification gap or change a Claim status.

### Known gaps

- The historical validation records `计算脚本/计算输出/version54_validation.json` through `version66_validation.json`, plus `计算脚本/审计结果/DeepSeek66/DeepSeek第66版独立审计-20261020.md` and `audit_evidence.json`, preserve **43 workstation-path references across 15 archived text files**, including original `C:\\Users\\84680\\...` paths. These are historical provenance fields and old local links, not portable bundle paths; they may expose local directory names and will not resolve on another machine. They are retained to preserve the historical audit record. The relocation manifest and the documented portable helpers use bundle-relative paths. Do not rewrite these archived records in place; if sanitized copies are needed later, create separately named derivatives with their own hashes and an explicit note that they are derivatives.
- `计算脚本/section262/build_v66.py` is also a historical, non-self-contained builder: it expects the v65 and v64 main Markdown files at the bundle root, but those files are not included in this v66 snapshot. The sentence in the archived `计算脚本/README.md` about the workspace root retaining v66 and v65 refers to the original pre-archive local workspace; it does not mean v65 or v64 is present at the root of this committed bundle. The builder is preserved for traceability, not advertised as a runnable one-command reproduction entry point.
- Historical `prepare.py`, `markdown_qa.cjs`, and `section261/build_v65.py` now use explicit input/dependency paths. Their original source/input directories are not bundled, so those scripts are not self-contained reproduction commands.
- A static path audit found **12 archived calculation scripts** that hard-code `/mnt/data` for input, output, or module lookup (including `run_uv_eft_audit_suite.py`, several audit/ledger builders, and `derive_raw_minkowski_numerator.py`). These paths refer to the original execution environment and are not portable in this repository layout. The scripts are preserved as historical artifacts; they are not claimed to be runnable from a fresh checkout without adapting their paths and supplying the missing inputs.
- Historical intermediate drafts in `work/` (`v57_*.md`) are retained for traceability only and do not reflect current conclusions.
- `计算脚本/README.md` records one external reference (`work/tsk2_b0.m`) that was already unlocatable at relocation time and was not reconstructed.
