# Eighty-seventh review: remaining collider, vector-response and absorption workflows

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `cf95089ce7f929b815d22b9bfbeb0a831b8d7d5d`  
Scope: the final six pending workflow entries: native-vector Fig. 12 extraction, four-body tensor and Belle II width scans, outer-neutrino absorption, vector/axial response, and vector-coupling rescaling.

This is a static review of triggers, input paths, permissions, command wiring and declared scope. No workflow, test, or calculation was run.

## Inventory

| Workflow | Current Git blob | Scope | Status |
|---|---|---|---|
| `.github/workflows/fig12-vector-extraction.yml` | `79d945e78650fdb14a241c35e98067251d67c32e` | Fig. 12 PDF vector extraction and profile cross-check | `REVIEWED_WITH_NOTES` |
| `.github/workflows/independent-fourbody-tensor-audit.yml` | `c1fe5e09d8e9022aaed22e9ac9bc4e7c44e1f13f` | Independent double-virtual four-body tensor audit | `REVIEWED_WITH_NOTES` |
| `.github/workflows/major1-scalar-belleii.yml` | `00fbdc1f6888fbef69b5a068889a3ed1d095e112` | Historical PR #52 width scan regeneration and Belle II recast | `REVIEWED_WITH_NOTES` |
| `.github/workflows/outer-neutrino-absorption-audit.yml` | `43ce1d465089b2829a7d2d336cc9ff2144748ac9` | Outer neutrino inverse-decay absorption diagnostic | `REVIEWED_WITH_NOTES` |
| `.github/workflows/vector-axial-response-scan.yml` | `b362e1437af5c1f15e1407aa93caffd7c229932d` | Finite-mixing vector/axial response and thermal-integral scans | `REVIEWED_WITH_NOTES` |
| `.github/workflows/vector-rescaling-audit.yml` | `2cd796b8ae863bc6bee90c1d4f14662b062ea10e` | Post-processing audit of vector coupling rescaling | `REVIEWED_WITH_NOTES` |

## Findings

### Fig. 12 vector extraction

The workflow is push/manual on the moving-muon branch but checks out that branch by name rather than the triggering commit SHA. It downloads the published APS PDF from a SCOAP3 mirror and validates a hard-coded SHA-256 before extracting geometry and running profile cross-checks. It then commits generated outputs by direct push. The path filter includes the two drivers, workflow and a report, but does not include the Caputo profile or other data/reference files the cross-check reads. There is no branch guard, concurrency control, or rebase retry. It grants workflow-wide write permission; PyMuPDF/NumPy are unpinned. The output is native-figure geometry and a cross-check, not original simulation data.

### Independent four-body tensor audit

The workflow runs focused tests and recomputes a double-virtual tensor/quadrature audit, writes a SHA256SUMS file, and commits the report. It uses Python 3.13 with exact NumPy/SciPy pins and has a non-cancelling concurrency group. Pushes are limited to the scalar/Belle II research branch, while manual dispatch and the commit step have no job-level branch guard. It uses workflow-wide write permission. The code/test path filter is narrow and appropriate for the declared audit; outputs are committed rather than uploaded as an artifact.

### Major 1 scalar Belle II scan

This long-running workflow (240-minute timeout) runs the scalar test suite, regenerates a historical PR #52 benchmark width scan, reinterprets intervals using the current Belle II inputs, hashes/compresses outputs and commits both scan and recast. Python 3.13 and NumPy/SciPy are pinned. The push filter covers production width/cascade/scanner scripts and tests, but omits the raw Belle II limit files consumed by the recast; a data-only update will not trigger it. The workflow has no job-level branch guard for manual dispatch and commits to the selected ref after a pull/rebase. It is explicitly a regeneration/recast of a historical benchmark and should not be presented as a current complete global scan.

### Outer neutrino absorption

The workflow has push/manual triggers guarded to the legacy codex branch, runs the diagnostic driver and commits JSON using fetch/rebase/push retries. The trigger filter includes only the driver and workflow, omitting its default profile, Fig. 7 reference, and shared rate/opacity dependencies. No focused test or numerical threshold is visible in the YAML. It is an absorption diagnostic; it does not complete the unresolved vector Fig. 7 benchmark or establish an axial exclusion.

### Vector/axial response scan

The workflow runs finite-mixing tests, local response and thermal-integral validation scripts, creates an SFHo local Compton map, and commits selected JSON outputs. It uses Python 3.12, installs NumPy without a version pin, grants write permission, and cancels any in-progress run for the same ref. It has no job-level branch guard for manual dispatch. The filter covers the finite-mixing source tree (excluding outputs), production rates and matrix-element reference, but not the default SFHo profile data used by the local rate map. One moving-Compton diagnostic is deliberately written to /tmp and removed from the worktree rather than archived. Its output set is therefore intentionally partial.

### Vector coupling rescaling

The guarded legacy-branch workflow runs rescaling regression tests, produces a post-processing JSON and verifies that baseline scans, luminosity reference and production axial files remain untouched. It commits JSON via direct `git push`, without a rebase/retry path. The path filter covers only the rescaling audit and workflow, so changes to the baseline scan/reference inputs alone do not trigger it. It grants workflow-wide write permission and installs unpinned NumPy.

## Maintenance notes

- Pin Fig. 12 checkout to the triggering SHA and include the profile/reference data in its push path filter.
- Add job-level branch guards to the four-body, Belle II and vector/axial manual-dispatch jobs where archival writes must stay on a specific research branch.
- Include Belle II raw limit files and the SFHo profile in the relevant path filters.
- Expand the outer-neutrino and rescaling triggers to cover their shared inputs; replace direct pushes with guarded rebase/retry archiving.
- Keep historical PR #52 regeneration distinct from the current bounded-width recast and distinguish vector diagnostics from axial physical acceptance.
