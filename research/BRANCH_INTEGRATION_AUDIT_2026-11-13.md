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


## Post-PR94 archive extraction and branch cleanup (2026-11-13)

Audit baseline: main at `2bebb38c7ff8966b048b133d67c1aa7bd37aa496`, immediately after PR #94.

### Archive integration

- **PR #94 — merged:** extracted the verified Major 3 Overleaf package, the Higgs-portal Markdown/SVG handoff, and the pinned axial stellar-cooling review snapshot. No generated ZIP or Base64 ZIP container remains in the main tree.
- The Overleaf archive was 777,561 bytes with SHA-256 `6c3d74091df33f316ea01694738a5b2392d9a882576704a7c3690a6569037323`. Its ZIP CRC, archive digest, and all embedded file hashes were verified. The original external manifest is preserved in the extracted directory.
- The stellar review package contains 75 extracted archive members from the 12 non-overlapping parts selected by its original packager. Its package manifest preserves each encoded-part hash, decoded-archive hash, size, and member count. The 18 source/profile SHA-256 entries and 24 reference/test Git blob SHA-1 entries were independently matched.
- The 75-member snapshot is kept under `review_package_extracted/` to preserve the pinned source baseline `81d9b2faf16eb39879b759b05afce46732c925d7`; it does not overwrite the active calculation tree.
- **PR #93 — closed as superseded:** its ZIP/Base64 packaging path was not merged. The report and index are represented by extracted files; the ZIP-building workflow is not part of main.
- Official SFHo/FRDM upstream EOS archives remain under the EOS data directory pending a separate, verified table-extraction/data-reader migration. They are original source inputs rather than generated delivery packages.

### Completed-branch synchronization

The following completed or superseded branch refs were moved to the post-PR94 main SHA after their results were verified in main or the corresponding PR was closed:

- `deliverable/major3-overleaf-bundle-20261113` and `fix/major3-overleaf-sha256-manifest-20261113` (PRs #88/#89; extracted contents now in main).
- `overleaf-export/reply-letter-20261109` and `overleaf-package-2026-11-09` (obsolete archive-only delivery branches).
- `chore/extract-generated-archives-20261113` (PR #94 merged).
- `fix/b13-b16-sha256-manifest-20261113` (PR #90 merged; checksum-only).
- `research/major44-postmerge-followup-20261113` (PR #83 duplicate of already-merged PR #77).
- `research/moving-muon-b13-b16-recovery-20261113` (PR #87 merged; six selected files are in main).

The obsolete ZIP file was also removed from `review/major3-two-block-neutrino-response-20261109` without discarding the branch's other historical review work. The former PR #93 branch is synchronized after its report/index have been copied to main.

### Ref inventory

At the post-PR94 audit snapshot, there were 100 refs including main. After the nine completed/superseded branch synchronizations, all 99 non-main refs were compared with main: 74 diverged, 16 behind-only, 9 identical, and 0 ahead-only. Three diverged refs had no branch-side changed-path entries. The full earlier 96-ref per-branch inventory is retained as a historical snapshot; the new post-PR94 summary is recorded in the inventory JSON.

The branch named `${GITHUB_REF_NAME}` is not an archive-only artifact: compared with `research/major1-higgs-scalar-mixing-20261109`, it carries one additional commit and three independent fermion-sector audit outputs. It is preserved for separate Major 1 review, not reset or merged in this archive-cleanup pass.

### Scientific acceptance boundary

The pure-vector Blinov Fig. 7 physical benchmark remains **NOT PASSED** at the 10 MeV strong-absorption end. This archive cleanup does not alter the B.13/B.16 calculations, the vector benchmark, the axial-vector limit, or any astrophysical interpretation.


## Post-main consolidation, physics cross-check, and current workstream audit (2026-11-13)

**Audit baseline:** current main at ca998e3c2845579e5183158d6328a557b3fd2ed4. This is later than the pinned 100-ref post-PR94 inventory snapshot. The historical inventory JSON remains unchanged and must not be mistaken for a live inventory of every current ref.

### PR #100 disposition

PR #100 was closed without merging. Its four actual file changes would have replaced the current two-VEV shared thermal adapters with older standalone copies. The two-VEV map, matrix element, width helper, tests, and validation record were already represented in main through PR #85 and the subsequent shared-code consolidation. The temporary PR #100 branch was moved back to the current main tree. No unique physics result was lost.

### Formula/code review of the two-VEV microphysics

The new research/stellar-cooling-two-vev-20261105/PHYSICS_CROSSCHECK_2026-11-13.md records the formula-level review:

- The scalar kinetic terms give \(m_{A'}^2=g_X^2(4v_s^2+v_\sigma^2)\); the eaten and orthogonal CP-odd directions are normalized and orthogonal.
- The projected \(S\)-phase Goldstone coupling equals the longitudinal axial-current divergence result for the stated pure-axial convention \(|g_A|=|g_X|\).
- The two-VEV extension contains a physical CP-odd state \(a_\perp\) with a nonzero charged-lepton coupling when \(v_\sigma\ne0\); its scalar-potential mass and constraints are outside this prototype.
- The inclusive active-neutrino trace is 2 for a unitary three-flavour PMNS rotation of \(Q_\nu=\mathrm{diag}(0,1,-1)\). This does not include non-negligible active-heavy mixing, open charged-\(N_R\) thresholds, or a complete Majorana-channel width calculation.
- The vacuum semi-Compton checks establish the electromagnetic Ward contraction and stated vector limits; they do not by themselves establish an \(A'\)-Goldstone Ward identity or medium-rest-frame T/L transport.
- The thermal code is homogeneous, optically thin, and polarization-summed. Its stored order scan changes both Gauss–Legendre and azimuthal orders together; an independent azimuthal-order scan remains open.

No new SN transport result or astrophysical limit is inferred from these checks.

### Major 1 branch comparison

- PR #68 and PR #69 are merged. Their canonical Belle II and Higgs–singlet research files are in main.
- The branch research/major1-higgs-scalar-mixing-20261109 has no branch-only file paths relative to current main. Its 15 same-path differences are older copies of shared project/status and stellar-cooling files, not a new Major 1 result.
- The branch research/major1-scalar-pole-belleii-20261109 has one branch-only generated ZIP, higgs_portal_mixing_md_with_svg.zip; its extracted Markdown/SVG counterpart is already in deliverables/higgs_portal_mixing_md_with_svg/.
- The independent fermion-sector audit is now in main under research/major1-higgs-scalar-mixing-20261109/independent_fermion_sector_audit_snapshot_20261113/. The older branch note that the outputs existed only on ${GITHUB_REF_NAME} is superseded.

### Major 4.4 and C4-C4 branch comparison

- PR #56 and PR #77 are merged; PR #83 was a duplicate of #77 and remains closed. Any earlier line in this audit or PROJECT_STATUS that labels PR #77 Draft/Open is historical and superseded.
- The old codex/major44-axial-cooling-constraints-20261105 branch has one branch-only generated Higgs-portal ZIP. Its three differing numerical JSON records were checked against main: the vector/axial scan differs only in final floating-point digits; the dimuon validation has six last-digit differences; and the SFHo local Compton record differs only in final digits/runtime metadata. The current-main files are retained; no old numerical output is copied over them.
- PR #79 and PR #84 are merged. The C4-C4 and C4-C4-B branches each have one branch-only generated ZIP, while their research outputs are already in main. Their local-rate and radial-opacity records remain diagnostics, not full SN transport acceptance.
- The Major 4.4 physical gate is unchanged: pure-vector Blinov Fig. 7 remains **NOT PASSED** at the 10 MeV strong-absorption end.

### Historical extraction metadata preserved without a duplicate source tree

The old research/major44-postmerge-followup-20261113 and ${GITHUB_REF_NAME} trees contain 82 branch-only paths under review_package_extracted/. Of these, 70 file blobs are byte-identical to canonical files elsewhere in current main. The remaining 12 are original package-provenance records (manifest, original checksums, original README/requirements, and part-level metadata). They are retained as native files under:

research/stellar-cooling-collaborator-archive-20261113/provenance/original-review-package/

The original manifest pins source commit 48bbe212d9a239b9e23bc45d455302b1f8fdcec1, numerical baseline 81d9b2faf16eb39879b759b05afce46732c925d7, 12 input parts, and 75 extracted members. The source payload itself is not copied a second time. The two-VEV convergence CSV on the old branch is byte-identical to the canonical CSV under the original-UV directory.

### Current ref count and branch handling

The repository currently exposes 108 refs including main. The earlier 100-ref JSON remains a pinned historical snapshot. This audit adds exact tree-content findings for the named workstreams above; it does not claim that the historical JSON is a fresh full 108-ref comparison.

Completed branch histories are not merged wholesale merely to reduce ahead/behind counts. After the provenance metadata is moved to main, only branches whose remaining tree differences are generated ZIPs, byte-identical duplicates, or superseded copies are candidates for a history-preserving sync to current main. The original PR commits and research history are retained; no branch is force-reset as a substitute for reviewing its content.

### Generated archive policy

The collaborator ZIP is now a local-only handoff. The repository keeps the builder script, native files, provenance, and checksums. The GitHub Actions workflow is validation-only and no longer builds or uploads a ZIP artifact. Original scientific input archives are separately documented as upstream source inputs and are not generated delivery bundles.


### Legacy GitHub Actions ZIP artifacts — one-time cleanup still required

The previous packaging workflows uploaded 13 ZIP artifacts before the local-only policy was applied. The current validation workflow no longer creates or uploads archives, but the earlier artifacts remain stored until deleted or expired.

| Artifact ID | Name | Expiry (UTC) |
|---:|---|---|
| 14005115238 | Stellar_Cooling_Research_Archive_2026-11-13 | 2026-12-13 02:28 |
| 14005065033 | Stellar_Cooling_Research_Archive_2026-11-13 | 2026-12-13 02:27 |
| 14004496598 | Stellar_Cooling_Research_Archive_2026-11-13 | 2026-12-13 02:25 |
| 14000599612 | axial-stellar-constraints-review-package | 2026-11-14 01:26 |
| 14000328688 | axial-stellar-constraints-review-package | 2026-11-14 01:22 |
| 14000509052 | axial-stellar-constraints-review-package | 2026-11-14 01:21 |
| 14000008862 | axial-stellar-constraints-review-package | 2026-11-14 01:20 |
| 13999268425 | axial-stellar-constraints-review-package | 2026-11-14 01:07 |
| 13998919607 | axial-stellar-constraints-review-package | 2026-11-14 01:05 |
| 14000626053 | axial-stellar-constraints-review-package | 2026-11-14 01:05 |
| 13998493850 | axial-stellar-constraints-review-package | 2026-12-13 00:47 |
| 13998169336 | axial-stellar-constraints-review-package | 2026-12-13 00:47 |
| 13999345496 | axial-stellar-constraints-review-package | 2026-12-13 00:46 |

A one-time manual workflow, .github/workflows/delete-legacy-zip-artifacts.yml, deletes only these exact artifact IDs after the operator selects the explicit confirmation input. The cleanup workflow must be run once from the repository Actions page with the explicit confirmation input. If it is not run, the artifacts expire at the dates above.
