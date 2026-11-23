# First-batch B.13/B.16 integration review — 2026-11-23

## Decision

The B.13/B.16 first batch is open as [PR #140](https://github.com/lm846802297-bit/axial-vector-review-response/pull/140). Its own pull-request checks and full diff review remain the merge gate. The three source PRs are integrated by path/blob overlay on the current mainline rather than by blindly merging their stale bases. The integration preserves the original calculation files and archives, retains the PR #134 strict validator, and incorporates the current-head B.13 result.

Sources:
- PR #121 — B.16 energy-grid identity, strict 10 MeV phase-space result, B.13 local-kernel recovery, and associated Fig. 7 diagnostics.
- PR #133 — B.13 431-point high-order provenance rerun.
- PR #134 — strict B.16 output-validator hardening and its provenance/review records.

The integration base is the mainline after the central standards-adoption merge, commit \`276cb335d466d1c1864448bcd222fe60d7fdcdc8\`. No files are deleted.

## B.16: strict 10 MeV phase-space acceptance

The archived reference contains 842 energy nodes with original SHA-256:

\`036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3\`.

A cross-runner diagnostic found that one interpolated threshold node can differ by one ULP. The integration therefore adds the immutable node-reference file and a shared validator. It retains exact SHA checks for the source and opacity grids and uses node-by-node comparison for the energy grid with \(5\times10^{-15}\) relative tolerance and zero absolute tolerance.

The strict production run [#45172485856](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45172485856) passed calculation, baseline checks, regression tests and result archival. The runtime energy-grid hash was \`db6f613c...\`; its maximum relative node difference from the archived reference was \(1.1675488289093305\times10^{-16}\), exactly one ULP. The original reference hash was not changed.

The independent validator run [#45173157775](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45173157775) passed compilation, the 24-test validator suite, and validation of the newly archived result.

The phase-space bookkeeping closes against the archived high-order baseline. The pure-vector 10 MeV Fig. 7 luminosity remains \(+92.4284\%\) above the digitized reference. No opacity rescaling, production axial-vector output, SN1987A limit, or exclusion curve is updated.

## B.13: targeted high-order provenance acceptance

The current-head run [#45172924204](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45172924204) passed Calculate, Validate and Archive.

- Source commit: \`e49908762e90271f4bc84be75e19577431febd4c\`.
- Environment: Ubuntu 24.04, AMD EPYC 7763, Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, four workers.
- Coverage: 431/431 targeted \((r,x)\) points and 2,155 ordered evaluations.
- Maximum final successive-order change: \(3.29220848525901\times10^{-4}\).
- Maximum energy PCHIP error: \(6.716564877619043\times10^{-4}\).
- Maximum radial midpoint error: \(8.311070322862653\times10^{-4}\).
- Maximum detailed-balance residual: \(5.027846521385086\times10^{-15}\).
- Maximum mass-shell residual: \(2.0432421890821873\times10^{-13}\).

The new run was compared with run #45054965537 after exact \((r,x)\) alignment. All 431 keys and order ladders match; 28,446 numerical leaf fields were compared with zero differences.

This is a targeted high-order acceptance. The full 1,687-node global high-order acceptance remains false. It does not establish full B.1/B.2 closure or update Fig. 7 or axial-vector constraints.

## Workflow and repository organization

The integration adds five B.13/B.16 workflows and registers two governance workflows already present on main but missing from the previous catalog. The resulting workflow inventory is 125 YAML files and 125 unique register entries:

- 110 \`REVIEWED_WITH_NOTES\`;
- 1 \`ACTIVE\`;
- 14 \`HISTORICAL_CANDIDATE\`;
- 0 \`PENDING\`.

The seven workflows and their permissions, branch/path guards, dependencies and run evidence are individually documented in [the first-batch workflow review](workflow-reviews/FIRST_BATCH_B13_B16_AND_GOVERNANCE_WORKFLOW_REVIEW_2026-11-23.md).

The integration also reconciles the document inventory. The tree contains 877 Markdown/text files: 462 baseline documents and 415 supplemental records. The 24 new B.13/B.16 documents and the two integration/review reports are individually registered as \`PASS_WITH_NOTES\`. The 242 pre-existing unregistered documents are now explicitly inventoried as \`PENDING\`, not silently marked as reviewed. Of these, 240 are in the RC001 upstream research archive and two are repository-management documents. The remaining work is a content review queue, not an inventory gap.

## Merge boundary and next work

1. Merge this first-batch integration PR after its own branch checks and full diff review.
2. Close PRs #121, #133 and #134 as superseded by the integrated branch, retaining their histories and run links.
3. Keep PR #123 as the separate Croon/Lai research integration. Its unresolved outer-opacity state remains explicit.
4. Keep PR #132 blocked on central PR #27 publication and Skill acceptance.
5. Review the 242 inventoried RC001 documents in bounded batches. Their \`PENDING\` status remains visible until each document is actually read and dispositioned.

No physical result is promoted beyond the acceptance scope stated above.
