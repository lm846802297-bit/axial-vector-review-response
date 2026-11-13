# Branch disposition audit — 2026-11-13

**Comparison base:** main at \`8b2f8570886bc5fbc7ac64232de94fa7f5e701f9\`  
**Method:** compare complete Git trees by path and blob SHA, then inspect changed source/output files. Ahead/behind counts are reported as history metadata only; they are not used as a substitute for tree comparison.

## 1. Active branch — preserve

| Branch | PR | Tree-level finding | Decision |
|---|---:|---|---|
| \`research/fig7-10mev-transport-localization-20261113\` | #102, open draft | Four changed files contain the new 10 MeV local-rate/polarization/escape localization analysis | **Keep active.** This is unresolved Major 4.4 research, not a superseded branch. |

PR #102 updates the literal 10 MeV Fig. 7 residual to +92.43%; the redshift-only diagnostic gives +36.91% and still does not close the discrepancy. Its matched local mode sums and detailed-balance checks close at approximately \(10^{-14}\), while the escape integral remains open. Do not merge or delete this branch as part of housekeeping; review its numerical inputs and physical interpretation separately.

## 2. Major 1 branch comparison

### Higgs–singlet mixing

- Branch: \`research/major1-higgs-scalar-mixing-20261109\`
- History comparison: 421 ahead / 30 behind.
- Tree comparison: **zero branch-only paths and zero unique blobs**.
- The 15 differing same-path files are shared project/status and stellar-cooling files, not new Major 1 scalar-mixing calculations. The Major 1 research files themselves are byte-identical to their current-main counterparts.

**Decision:** no source or numerical result needs merging. Preserve this branch as a historical development record for the extensive UV scalar, counterterm, RGE, EFT, and fermion-sector work. Do not delete it merely because the tree is integrated.

### Belle II scalar pole

- Branch: \`research/major1-scalar-pole-belleii-20261109\`
- History comparison: 35 ahead / 30 behind.
- One branch-only file: \`higgs_portal_mixing_md_with_svg.zip\`.
- Its extracted Markdown/SVG deliverables already exist under \`deliverables/higgs_portal_mixing_md_with_svg/\`; the ZIP is not a unique scientific source.

**Decision:** no new calculation needs merging. Preserve the branch history for the scalar-pole/Belle II recast, but do not reintroduce its generated ZIP.

## 3. Major 4.4 branch comparison

Branch: \`codex/major44-axial-cooling-constraints-20261105\` (786 ahead / 30 behind).

- One branch-only file is the generated Higgs-portal ZIP; the extracted counterpart is already in main.
- The Fig. 4/Fig. 7 comparison JSON is byte-identical to main.
- The vector/axial response scan has 17 changed numeric fields; the largest absolute difference is \(2.56\times10^{-16}\). The largest relative differences occur only in near-zero interference entries of order \(10^{-15}\).
- The dimuon thermal validation has 7 changed numeric fields; the largest absolute difference is \(4.55\times10^{-13}\), with the physical rate values differing at the last floating-point digit.
- The SFHo local Compton JSON has 201 changed fields. Excluding runtime and residual diagnostics, physical rate values differ by at most \(5.3\times10^{-16}\) relatively; the largest absolute change among the non-runtime/non-residual numeric fields is \(2.25\times10^{-16}\). Runtime differs by 34.2 s and is execution metadata, not physics.
- The branch's EFT regression workflow differs by one comment only; it adds no test or acceptance condition.

**Decision:** keep current-main numerical outputs; do not copy the branch JSON or workflow back. Preserve the long branch history as an archive because it records the development of the Major 4.4 calculation. The pure-vector Fig. 7 10 MeV physical gate remains NOT PASSED.

## 4. C4-C4-A and C4-C4-B

### C4-C4-A energy dependence

- Branch: \`research/c4c4-energy-dependence-20261112\` (696 ahead / 29 behind).
- One branch-only file is the generated Higgs-portal ZIP.
- The local-rate and radial-opacity research outputs are already in main.
- The branch's B.16 escape audit script is older than main's version.

### C4-C4-B full radial energy dependence

- Branch: \`research/c4c4b-full-radial-results-main-20261113\` (1 ahead / 23 behind).
- One branch-only file is the generated Higgs-portal ZIP.
- The full-radial report, 7,224 local-rate rows, 1,806 radial opacity/tau rows, channel ratios, quadrature checks, radial-grid checks, and summary JSON are byte-identical to main.
- The branch's \`audit_b16_escape_phase_space.py\` is an older 463-line version. Main's 481-line version additionally fingerprints the source PDF and compares the 10 MeV reference vertices to the archived baseline with a \(5\times10^{-15}\) relative provenance tolerance.

**Decision:** no C4-C4-B output is missing from main. Retain the stricter main audit implementation. Keep the branch as a short-lived historical research record until the active 10 MeV localization work is resolved; it is not a source of newer radial data.

## 5. Two-VEV microphysics branch

Branch: \`research/two-vev-axial-stellar-microphysics-main-20261113\` (1 ahead / 22 behind).

- Two branch-only paths: \`higgs_portal_mixing_md_with_svg.zip\` and \`research/stellar-cooling-two-vev-20261105/thermal-convergence-2026-11-05.csv\`.
- The CSV blob is byte-identical to the canonical CSV in the original-UV model directory.
- The generated ZIP's extracted Markdown/SVG counterpart is already in main.
- The branch contains standalone copies of the thermal-rate and convergence programs. Current main uses thin model adapters over the shared thermal implementation; the branch copies are superseded duplicates, not additional model physics.

**Decision:** do not merge the old standalone thermal programs. Preserve the branch history until the two-VEV formula/code review is complete; then it can be retired without copying its old implementations.

## 6. Collaborator archive branch

Branch: \`research/stellar-cooling-collaborator-archive-20261113\` (2 ahead / 4 behind).

- Zero branch-only paths and zero unique blobs.
- Six same-path documentation/workflow differences are superseded by PR #101 and PR #104.
- Current main has the corrected local-only ZIP policy, provenance index, and validation-only workflow.

**Decision:** no content needs merging. Keep as a short-lived archive until the final documentation snapshot is accepted.

## 7. Branch refs whose commits are already reachable from main

The following two groups have been checked against main and have \`ahead_by=0\`. Their commits are already reachable from main, so deleting these branch refs does not discard commit history.

### Group A — head \`304498ad21880097e8f46b26823ef85e9213e231\` (main is 6 commits ahead)

1. \`chore/extract-generated-archives-20261113\`
2. \`deliverable/major3-overleaf-bundle-20261113\`
3. \`fix/b13-b16-sha256-manifest-20261113\`
4. \`fix/major3-overleaf-sha256-manifest-20261113\`
5. \`overleaf-export/reply-letter-20261109\`
6. \`overleaf-package-2026-11-09\`
7. \`research/major44-postmerge-followup-20261113\`
8. \`research/moving-muon-b13-b16-recovery-20261113\`

The two research branches include the retired \`review_package_extracted/\` tree. Its 70 duplicate file blobs are already present at canonical main paths; the 12 unique provenance metadata records were moved to \`research/stellar-cooling-collaborator-archive-20261113/provenance/original-review-package/\` in PR #101.

### Group B — head \`309b0cbd4e5d6976b63fa47978a31aac4fe9b245\` (main is 12 commits ahead)

1. \`\${GITHUB_REF_NAME}\`
2. \`docs/post-pr94-archive-policy-and-review-index-20261113\`
3. \`research/stellar-cooling-review-package-20261113\`

**Decision:** these 11 refs are safe first-batch deletion candidates. Their commits are already in main; no unique file content depends on the branch refs.

## 8. Other completed housekeeping branches

- \`docs/finalize-legacy-zip-cleanup-20261113\`: its complete tree is identical to main after PR #104; the PR retains the squash-merge history.
- \`chore/one-time-cleanup-legacy-zip-artifacts-20261113\`: contains only the temporary one-time cleanup workflow; PRs #103 and #104 retain its purpose and deletion record.
- \`docs/main-research-index-physics-crosscheck-archive-policy-20261113\`: contains the temporary cleanup workflow that was later removed; the final documentation is in main.

These are candidates for later deletion after the first-batch ancestry-safe refs are pruned.

## 9. Branch preservation policy

- Preserve branches with meaningful independent development history even when their final files are integrated: Major 1 Higgs mixing, Major 1 Belle II, Major 4.4, and C4-C4-A.
- Preserve the active PR #102 branch and the ongoing axial/Goldstone cross-check branch until their work is reviewed and integrated.
- Do not force-reset a divergent branch to main to make Ahead/Behind appear clean.
- Delete only refs whose head commit is already reachable from main, or whose remaining differences are demonstrably superseded and whose PR/history records are retained.
- GitHub main remains the canonical source of native files, extracted data, reports, figures, tests, provenance, and checksums. Generated ZIPs remain local-only handoff files.
