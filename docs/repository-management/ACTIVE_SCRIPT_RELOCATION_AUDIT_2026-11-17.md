# Active Major 2 / Major 3 / Major 4.2 script relocation audit — 2026-11-17

## Scope and decision

This PR relocates the three self-contained referee-response calculation packages from `计算脚本/` into dedicated `research/` workstream folders. The migration is organizational and provenance-focused; it does not change physical formulas, benchmark inputs, or numerical results.

- Major 2: Fig. 2 parameter-window benchmark.
- Major 3: optional response-only \(\sigma+3N_R\) neutrino seesaw construction and charged-lepton/VLL diagnostic.
- Major 4.2: momentum-dependent kinetic mixing and conditional NA64 comparison.

The original manuscript model remains the one-VEV (S+\mathrm{VLL}) theory. The Major 3 (sigma+3N_R) construction remains a response-only optional completion and is not promoted to the non-neutrino model baseline.

## File migration

Eight files move into three folders:

| Old folder | New folder | Files |
|---|---|---:|
| `计算脚本/Major2_Fig2/` | `research/major2-parameter-window-20261117/` | 2 |
| `计算脚本/PMNS_Major3/` | `research/major3-neutrino-response-optional-seesaw-20261117/` | 4 |
| `计算脚本/Major42_kinetic/` | `research/major4-2-kinetic-mixing-20261117/` | 2 |

Six files are byte-identical moves. Two Major 3 files receive path-metadata-only edits:

1. The runner's docstring and recorded invocation now point to its new path. Its repository-root calculation (`HERE.parents[1]`) remains valid because the package stays one directory below `research/`.
2. The saved JSON updates only `calculation_script`, `runner_script` and `invocation` in its `reproducibility` object. All numerical inputs, matrices, masses, residuals, caveats and the core-script SHA-256 are unchanged.

The Major 2 and Major 4.2 scripts use `Path(__file__).resolve().parents[2]`; their new locations preserve the same two-directory depth below the repository root. All output directories remain siblings of their scripts. The exact old/new blob mapping, sizes and available SHA-256 values are recorded in [the manifest](ACTIVE_SCRIPT_RELOCATION_MANIFEST_2026-11-17.csv).

## Dependency and workflow audit

- Major 2 depends on Python and `mpmath`; its source inputs are the root 2026-11-04 response TeX, the pinned Overleaf v6 source and the Fig. 2 plot PDF. The current Fig. 2 display window is (m_{A'}\in[10^{-3},10^2]\,\mathrm{GeV}), (g_X\in[10^{-6},1]); these are display endpoints, not a universal allowed region.
- Major 3 depends on Python and NumPy. The core reconstruction is a tree-level existence benchmark from NuFIT 6.1 central values, not a fit or constraint scan. The charged-lepton/VLL script is a separate illustrative texture diagnostic and does not calculate LFV branching ratios.
- Major 4.2 depends on Python and `mpmath`. Its NA64 Fig. 3 intervals are manual visual read-offs with stated uncertainty; the comparison is not a detector-level recast.
- The workflow inventory contains no dedicated workflow that runs these three legacy folders. The PMNS-named `.github/workflows/axial-goldstone-pmns-regression.yml` runs the separate `research/stellar-cooling-two-vev-20261105/` regression suite and does not consume the response-only PMNS scripts. No workflow YAML is changed by this PR.

## Path references and indexes

Updated the research directory index, main research index, legacy calculation index, current decision ledger, the three Major 2 / 3 / 4.2 comparison/validation records, and the two historical PMNS/LFV technical notes that still linked to the old folder. Their commands now point to the new locations. The legacy `计算脚本/` directory remains in place for Major 1 tools, Section 250–262 materials, DeepSeek66 audit evidence, and other historical scripts; it is not renamed or removed.

## Validation boundary

- The six byte-identical moves preserve their original Git blob SHA and byte size.
- The two Major 3 metadata edits preserve all numerical fields; the new runner SHA-256 is `0bf63f72a35a88ab0d536531f17c3370aae2c72788ce162d689ad6dc28bb66b1`; the updated JSON SHA-256 is `52041694f5f32c7895992b86c5c7325994a5dec11b6f87f14fcf0ed0a0e596fd`. The original 2026-11-04 hashes remain documented in the historical validation record.
- No scientific calculation, Python/NumPy/mpmath execution, TeX build, or workflow run is performed by this relocation PR. The change is limited to paths, README navigation, and the two declared provenance strings/files.
- The full Markdown/TXT register and Git-tree counts are reconciled in this PR. Relative Markdown links in the changed entry points and the three new workstream folders are checked against the branch tree.
- A successful structural audit does not promote any of these benchmark results to a full fit, detector-level recast, or general UV constraint.
