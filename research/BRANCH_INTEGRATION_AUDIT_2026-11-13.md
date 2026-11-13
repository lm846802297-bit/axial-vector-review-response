# 2026-11-13 branch integration audit

Audit baseline: main at `4fdb7ea3b0e85412525322b6b3d584365a852363`, after the C4-C4-B and separate two-VEV integrations.

## Integration completed

- **PR #84 — merged:** C4-C4-B full-radial, energy-dependent local-scattering archive. It adds the 7,224-row result set, 340 stratified high-order comparisons, radial-grid checks, provenance, and checksums. This remains a fixed-local-energy, flat-space total-scattering diagnostic; it is not full SN transport, an escape probability, a Blinov Fig. 7 reproduction, or an SN1987A exclusion.
- **PR #85 — merged:** separate two-VEV axial microphysics benchmark. It preserves the exact two-VEV Goldstone map, generic vacuum semi-Compton amplitude, current-level widths, homogeneous optically thin rate, tests, and convergence record. It is explicitly an alternative model extension, not the original one-VEV model used in the paper.
- **PR #82 — closed as superseded by #84.** The older PR replayed the long pre-squash C4-C4 branch history and was conflict-marked; #84 transferred only the true incremental result files onto current main.
- **PR #83 — closed as duplicate of #77.** Its head commit was already merged by #77.
- No open PRs remained at the end of this audit.

## How to interpret the branch comparison

GitHub listed 90 non-main branch refs at the audit. 75 reported `ahead_by > 0` against main. This is not equivalent to 75 unmerged research packages: many branches were integrated by squash merge, so their old commit ancestry remains divergent even when the corresponding file content is already in main.

The following major research workstreams are already represented in main through merged PRs:

- Original-model axial stellar-cooling mapping and semi-Compton microphysics: PR #53.
- Major 4.4 axial-EFT benchmark and the moving-muon/EOS work carried through its base branch: PR #56 (with the PR #57 work merged into that base before the final PR #56 integration).
- Original-model Belle II radial-scalar reinterpretation: PR #68.
- Higgs–singlet mixing and UV–EFT matching audits: PR #69.
- Neutrino-mass response: PR #72.
- Research-result archival, extraction-before-upload, and CI-optional policies: PRs #73, #80, and #81.
- C4-C4-A/Aq source and runner: PR #79; the subsequent C4-C4-B results are now in PR #84.

These branches must not be re-imported solely because their ahead counts remain large.

## Branches intentionally not promoted in this pass

- `research/higgs-signal-strength-two-benchmarks-2026-10-28`: preliminary non-degenerate screening based on inherited fixed-self-energy proxy values. Its limitations are explicit, and the later PR #69 work contains the more developed mass-eigenstate, portal-threshold, and complex-pole analysis. Do not treat the old proxy as a current physical mixing angle or Higgs exclusion.
- `research/radial-scalar-two-vev-belleii-20261105-current-main`: raw supplemental-data fragments only. Its scalar four-muon table is a formatting variant of the Belle II source table already archived with provenance in PR #68; the additional vector-control file is not accompanied by a self-contained source manifest or analysis record.
- `transfer/p1iii-eos-latest-source-20261111`: temporary source-package workflow, not a new EOS calculation/result archive.
- `transfer/pr57-source-bundle-20261110` and `transfer/sfho-frdm-release-transfer-20261111`: no tree-level file delta against main; their source/data content is already represented in the merged research history.
- `work/hs-mixing-one-loop-20261027`: older one-loop working note and response draft, superseded by PR #69 and the later matching/pole records.
- The old PR #30 axial recast and PR #32/#52 radial-scalar drafts are superseded by the later original-model archives in PRs #53/#56 and #68, respectively.
- Historical `docs/*` and `review/*` branches map to already merged response, audit, or archival PRs. They are not separate new results.

## Scientific boundaries retained

- The pure-vector Blinov Fig. 7 reproduction remains **not passed** at the 10 MeV strong-absorption end; this audit does not change that status.
- PR #84 does not turn a local total-scattering optical depth into an absorption-only transport solution or an SN cooling limit.
- PR #85 is a separately scoped two-VEV extension and does not alter the original one-VEV manuscript model.
- Neither PR #84 nor PR #85 modifies the manuscript or referee-facing response.

## Repository workflow

Future research integrations should start from current main, use a focused clean branch, preserve native calculation outputs and provenance, and submit a PR. Do not merge stale divergent branch histories wholesale merely to eliminate `ahead_by` counts. CI is optional and is not a prerequisite for research execution or integration.

## Post-integration re-audit after PR #87–#89 (2026-11-13)

Audit baseline: `main` at `a74707637837dfd577e15e530c896959ed12baa2`, after the moving-muon recovery and the current-main Overleaf bundle plus checksum correction.

### Complete branch inventory

The repository had 96 branch refs including `main`; all 95 non-main refs were compared against the audited main SHA. The result was:

| Compare category | Branch refs |
|---|---:|
| Diverged (ahead and behind) | 79 |
| Behind-only (no branch-side commits ahead) | 16 |
| Ahead-only | 0 |
| Identical non-main refs | 0 |
| Total non-main refs | 95 |

Within the 79 diverged refs, 76 had branch-side changed-path entries and 3 had none. The compare endpoint uses merge-base/three-dot semantics; `ahead_by`, `behind_by`, and changed-path counts are not a substitute for checking whether a squash-merged tree's content is already in main. The complete inventory, including every branch name and head SHA, is in [BRANCH_INVENTORY_2026-11-13.json](BRANCH_INVENTORY_2026-11-13.json).

### Three requested workstreams

| Workstream | Post-merge branch comparison | Integration decision |
|---|---|---|
| Moving-muon source `research/moving-muon-thermal-rates-20261107` | ahead 1,578 / behind 13; 41 branch-side paths | Do not merge wholesale. PR #87 extracted only the six missing B.13/B.16 artifacts onto a clean branch and merged them. Later profile/provenance edits are not imported because the archived results were generated with the earlier profile hash. |
| Major 4.4 source `codex/major44-axial-cooling-constraints-20261105` | ahead 786 / behind 13; 13 branch-side paths | No new bulk import. PR #77 already merged the eight provenance-only JSON refreshes, the relative-import test fix, and the review record. PR #83 was a duplicate of #77. The three roundoff-only numerical outputs remain excluded. |
| Major 3 source `review/major3-two-block-neutrino-response-20261109` | ahead 31 / behind 39; 5 branch-side paths | Do not merge the historical branch. PR #72 is already integrated; PR #88 rebuilt the Overleaf package from current main, and PR #89 corrected and verified its SHA-256 manifests. |

The clean recovery/delivery branches also remain in the inventory after squash merges: `research/moving-muon-b13-b16-recovery-20261113` (ahead 4 / behind 3), `deliverable/major3-overleaf-bundle-20261113` (ahead 1 / behind 2), and `fix/major3-overleaf-sha256-manifest-20261113` (ahead 2 / behind 1). Their PRs are merged; their remaining ancestry divergence is not a reason to merge them again.

### Other branch families retained without bulk integration

- `research/c4c4-energy-dependence-20261112` remains a large historical/working branch (ahead 696 / behind 12); PR #84 already transferred the scoped C4-C4-B full-radial archive. Do not replay the full branch history.
- `research/two-vev-axial-stellar-microphysics-main-20261113` is the separate two-VEV workstream already represented by PR #85; it does not replace the original one-VEV model.
- `research/stellar-cooling-review-package-20261113` remains a separate review-package branch (ahead 29 / behind 3; 23 branch-side paths) and was not part of these three integrations.
- `research/major1-higgs-scalar-mixing-20261109` and `research/major1-scalar-pole-belleii-20261109` remain separate active research lines; this audit does not fold their large calculation histories into the current task.
- The CI placeholder ref `${GITHUB_REF_NAME}` is retained as a workflow-generated branch reference, not treated as a research package.
- Old `docs/*`, `review/*`, and transfer refs remain historical snapshots unless a separately reviewed, unique content delta is established. No branches were deleted or force-synchronized.

### Current scientific gate

The pure-vector Blinov Fig. 7 reproduction remains **NOT PASSED** at the 10 MeV strong-absorption end. The B.13 10 MeV grid-convergence result is a numerical convergence statement for its fixed-`omega` benchmark, not physical Fig. 7 acceptance. The companion 0.1 MeV radial refinement remains not converged. No opacity/profile rescaling and no new axial constraint curve are accepted by this branch integration.

### Final repository state

PRs #87, #88, and #89 are merged. PR #77 is merged; PR #83 is closed as its duplicate. PRs #84 and #85 are merged. No open PRs were present at the audited snapshot. The only work in this update is the branch inventory and status/audit documentation.

## Post-inventory corrections after PR #90 and PR #91 (2026-11-13)

- PR #90 merged the checksum-only correction to `RECOVERED_B13_B16_SHA256SUMS_2026-11-13.txt`. The exact stored report bytes hash to `485bc6ce837f6bd45b9dd7958c7049b5426f5d6508638c9976f2b55267bbd4f4`; the other four manifest entries were already correct. No B.13/B.16 calculation, source code, or scientific conclusion changed.
- PR #91 merged the branch inventory and status/audit documentation at `d106b9a6f16116918a92da775fa7113b2718a221`.
- The inventory JSON is intentionally pinned to the pre-follow-up main snapshot `a74707637837dfd577e15e530c896959ed12baa2`. Two refs were added after that snapshot: `fix/b13-b16-sha256-manifest-20261113` (PR #90; checksum-only) and `docs/post-merge-branch-audit-20261113` (PR #91; documentation-only). Neither contains new physics results.
- Latest main after both follow-on merges is `dc3e3339238cbae7b72f73228518ca36a89a837d`; no open PRs remained at this point.
