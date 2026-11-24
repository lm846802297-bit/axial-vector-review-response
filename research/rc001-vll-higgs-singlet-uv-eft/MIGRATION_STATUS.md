# RC-001 upstream archive migration

**Status:** archive transfer, byte-integrity verification and dependency audit complete; PR [#135](https://github.com/lm846802297-bit/axial-vector-review-response/pull/135) merged into `main` on 2026-11-23.  
**Merge commit:** `a1940523eb5e345a5a9c03a06b9e0f4f63f4d378`  
**Source repository:** https://github.com/lm846802297-bit/high-energy-theory-research  
**Frozen source main:** `b2dd8f7e4427d0292bc299d273c780c05021fdab`  
**Merged source branch:** `migration/rc001-rehome-20261123`

## Canonical archive

The complete frozen source tree is mirrored under:

`research/rc001-vll-higgs-singlet-uv-eft/upstream/<original-source-path>`

This preserves the source-relative paths and original directory hierarchy. The target repository's existing Major 1 workstream is not overwritten. The source `research/README.md` remains within the mirrored `upstream/research/` directory.

## Archive-integrity acceptance

| Check | Result |
|---|---:|
| Source files in frozen inventory | 480 |
| Target mapped paths present | 480 |
| Git blob SHA matches | 480 |
| Byte sizes match | 480 |
| Missing paths | 0 |
| SHA/size mismatches | 0 |

The comparison was made against the remote source Git tree and the remote target branch tree. This establishes byte-for-byte archive identity at the Git blob level; it does not revalidate physical claims or recalculate any result.

## Dependency audit

**Audit baseline:** PR #135 HEAD `f34a41f0a707ffac063b9fe868555ae477c1bc62`; frozen source main `b2dd8f7e4427d0292bc299d273c780c05021fdab`.

### Markdown references

All 107 Markdown files in `upstream/` and the five target-side integration/navigation documents were scanned for relative Markdown links.

- Six references point to five shared infrastructure files that were intentionally not moved into the project archive. They remain available in the frozen central repository and should be opened through these pinned links:
  - [`projects/README.md`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/b2dd8f7e4427d0292bc299d273c780c05021fdab/projects/README.md)
  - [`projects/README.zh-CN.md`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/b2dd8f7e4427d0292bc299d273c780c05021fdab/projects/README.zh-CN.md)
  - [`docs/scientific-diff-workflow.md`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/b2dd8f7e4427d0292bc299d273c780c05021fdab/docs/scientific-diff-workflow.md)
  - [`docs/CALCULATION_RESULT_ARCHIVAL_POLICY.md`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/b2dd8f7e4427d0292bc299d273c780c05021fdab/docs/CALCULATION_RESULT_ARCHIVAL_POLICY.md)
  - [`templates/claim-evidence-matrix.md`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/b2dd8f7e4427d0292bc299d273c780c05021fdab/templates/claim-evidence-matrix.md)
- Eighteen link occurrences point to fourteen paths that were already absent from the frozen source tree: seventeen occurrences in `upstream/research/RC-001-portal-boundary-b1b3-reconciliation.md` and one SVG reference in the v66 manuscript. These are inherited source-record references, not missing files introduced by the transfer.
- The original blobs for the affected source Markdown files match the frozen source exactly. The archive was not edited to repair or rewrite historical references, preserving the 480/480 byte-identity requirement.

Pre-existing targets absent from the frozen source tree:

- `calculations/RC-001-portal-boundary-b1b3-reconciliation.py`
- `validation/RC-001-portal-boundary-b1b3-reconciliation.txt`
- `calculations/RC-001-six-cycle-trace-normalization-audit.py`
- `validation/RC-001-six-cycle-trace-normalization-audit.txt`
- `calculations/RC-001-six-cycle-oq2-candidate-kernel-ledger.py`
- `validation/RC-001-six-cycle-oq2-candidate-kernel-ledger.txt`
- `calculations/RC-001-fixed-sector-hard-soft-pole-ledger.py`
- `validation/RC-001-fixed-sector-hard-soft-pole-ledger.txt`
- `calculations/RC-001-C5-soft-bubble-trace-audit.py`
- `validation/RC-001-C5-soft-bubble-trace-audit.txt`
- `calculations/RC-001-six-cycle-simplex-integration.py`
- `validation/RC-001-six-cycle-simplex-integration.txt`
- `research/RC-001-tree-level-C5-matching-derivation.md`
- `artifacts/higgs-portal-v66-20261019/higgs_portal_mixing_feynman_diagrams.svg`

### Script and workflow paths

- All 136 Python files in `upstream/calculations/` were inspected. No hard-coded absolute paths were found; path-sensitive test helpers resolve sibling files relative to `__file__`.
- The 54 Python files in the archived v66 artifact bundle include twelve scripts with the original `/mnt/data` runtime convention:
  - `audit_dirac_traces_all_paths_three_patterns.py`
  - `audit_one_odd_path_kernel.py`
  - `audit_six_cycle_reverse_candidate_kernels.py`
  - `audit_six_route_geometry_coefficients.py`
  - `audit_six_routed_shifted_traces.py`
  - `build_pathwise_matching_integrands.py`
  - `build_six_cycle_path_weight_ledger.py`
  - `build_six_labeled_orderings.py`
  - `closed_form_mass_ratio_C1.py`
  - `derive_raw_minkowski_numerator.py`
  - `optimized_closed_forms_mass_ratio.py`
  - `run_uv_eft_audit_suite.py`
- Five v57 document-processing scripts (`enhance_v57.py`, `polish_v57.py`, `revise_v57.py`, `structure_v57.py`, and `validate_v57.py`) expect `审稿意见-gpt/` and/or `dw13678_report_1_a.md`, which are not part of the frozen archive. They remain historical source artifacts and are not treated as executable migration checks.
- Eleven non-Python scripts were also inspected. The JavaScript Markdown QA script uses `__dirname` to locate its sibling `source-for-pandoc.md`; no absolute path dependency was found in the archived Mathematica files.
- The three archived workflow YAML files use original repository-root-relative `calculations/`, `research/`, and `validation/` paths. They remain inert under `upstream/.github/workflows/`; any deliberate future reactivation must set the working directory to the mirrored `upstream/` root and be reviewed separately.

## Workflow disposition and target checks

The PR does not modify the target repository's root `.github/workflows/` directory. The relevant active Major 1 workflows retain their existing branch and path filters.

At the audited PR HEAD, GitHub reported zero workflow runs and zero check runs. No CI pass is claimed. The migration adds archived source and documentation only; no physical calculation was rerun, and no scientific validation status was changed.

## Unmerged source work

Source PR #9 and PR #14 are not part of the frozen source `main` snapshot. Their proposed changes remain separate and must not be represented as merged research results.

## Post-merge status

1. PR #135 is merged into the target repository's `main` at `a1940523eb5e345a5a9c03a06b9e0f4f63f4d378`.
2. A fresh Git-tree comparison against the frozen source commit confirms 480/480 mapped paths exist, all 480 Git blob SHAs match, all byte sizes match, and the total archived size is 14,283,294 bytes.
3. The separate cleanup PR in the source infrastructure repository has not been opened; the frozen source repository still retains its original files. This is a separate infrastructure follow-up and does not affect the target archive's integrity acceptance.

No physical calculation was rerun or modified by this archive migration. Software and archive checks are not physical validation.
