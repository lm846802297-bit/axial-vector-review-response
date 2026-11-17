# Eighty-fourth review: Bollig figure and muon-density workflow provenance

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `57c02466cf573ceb379c7f3334153f919c1032a2`  
Scope: four workflows that inspect or compare Bollig Figs. 3/4 and audit muon density, B.1 source closure, and outer thermodynamic profile inputs.

This is a static workflow/provenance review. No workflow, test, or calculation was run. The digitized public-figure curves are not original simulation tables, and the existing Caputo/Bollig absolute-density difference remains unresolved.

## Inventory

| Workflow | Current Git blob | Scope | Status |
|---|---|---|---|
| `.github/workflows/bollig-fig3-crosscheck.yml` | `59d947cb9ff532c8302216007c555fc8fbc0aac0` | Bollig Fig. 3 PDF vector inventory | `REVIEWED_WITH_NOTES` |
| `.github/workflows/bollig-fig4-muon-profile.yml` | `724a3716a84406cd72f34249bd3f1fb35d672d92` | Bollig Fig. 4 vector paths and muon-profile provenance | `REVIEWED_WITH_NOTES` |
| `.github/workflows/bollig-muon-density-b1-audit.yml` | `5ff7eaff9f16f2ed17da4e8a0844acdf8792ddac` | Fig. 3 density, Fermi density and B.1 source audit | `REVIEWED_WITH_NOTES` |
| `.github/workflows/bollig-outer-thermodynamic-profile.yml` | `dbfbe8f5710dd524e6b4b02fd82e33fc13240315` | Caputo/Bollig outer (T) and (mu_mu/T) profile comparison | `REVIEWED_WITH_NOTES` |

## Findings

### Fig. 3 vector inventory

This push-only workflow is restricted to the moving-muon branch and the vector-inspection script/workflow paths. The script downloads public arXiv v7 PDF 2005.07141 and extracts Fig. 3 drawing geometry; it archives a JSON inventory by direct `git push`. There is no manual dispatch, no job-level branch guard, no focused test, and no PDF SHA-256 check in the workflow or driver. The path filter does not include a source-version/hash manifest. It grants `contents: write` and uses a simple push without a rebase/retry path; the concurrency group serializes with the 12--15 km profile audit on the same ref, but does not protect against other writers.

### Fig. 4 muon profile

This workflow supports push and manual dispatch on the legacy-named `codex/major44-axial-cooling-constraints-20261105` branch, which still exists. It checks out the triggering SHA, downloads versioned public PDF v7, extracts vector paths, runs the Caputo/Ferreira provenance audit, then commits four generated geometry/density/provenance files. It has no dedicated test or explicit numerical acceptance block. The PDF URL includes a version but the workflow does not verify a pinned file hash before parsing. Its push paths omit the data/profile inputs consumed by the provenance audit. It grants workflow-wide write permission; archive updates use rebase retries.

### Muon density and B.1 source audit

This workflow checks out the event SHA, runs the independent density/Fermi-integral/B.1 source driver, verifies production code and outputs remain unchanged, and commits JSON. The driver compares the archived public Fig. 3/4 geometry with Caputo profile data and independently checks the Fermi-density calculation and B.1 source closure. The push filter includes the driver, reference implementation, profile, Caputo density points, vector-path metadata and workflow, but the YAML does not run a focused test or state separate numeric thresholds. The driver’s density analysis does not determine whether Bollig Fig. 3 plots (n_mu) or net density; it therefore does not close the documented cross-paper absolute-density convention issue.

### Outer thermodynamic profile

This workflow checks out the event SHA, runs the comparison on coordinates inside the source PDF vectors without extrapolation, checks that production axial outputs are untouched, and commits JSON plus Markdown. The driver downloads the versioned Bollig v7 PDF and validates its SHA-256 and curve identity. The workflow does not run a separate test or acceptance block; the profile source is path-filtered, while the external PDF is fetched by the driver. NumPy/PyMuPDF are installed without version constraints.

## Maintenance notes

- Keep PDF version and hash checks together. The Fig. 3 vector inventory currently lacks a source hash assertion; Fig. 4 should validate its downloaded PDF bytes before using the geometry.
- Add the profile/data inputs to the Fig. 4 workflow's push filters and consider a shared pinned source-PDF acquisition helper.
- Replace direct push with the guarded fetch/rebase/retry archive pattern or use workflow artifacts; limit write access to the commit step.
- Interpret figure digitization as a public-curve cross-check, not original simulation output. The absolute-density convention discrepancy remains open; no density rescaling is justified by these workflows.
