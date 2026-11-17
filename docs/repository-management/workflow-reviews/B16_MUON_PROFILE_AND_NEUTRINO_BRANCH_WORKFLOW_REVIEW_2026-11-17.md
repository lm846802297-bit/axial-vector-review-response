# Eightieth review: muon-profile and neutrino-branch workflow wiring

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `770c646633c9ee2aa46a6f484a22725815884aa2`  
Scope: five B.16 workflows for flavour-resolved neutrino opacity, positive-branch and full-profile sensitivities, muon chemical-potential provenance, and a 10 MeV Ferreira-profile diagnostic.

This is a static workflow and provenance review. No workflow, test, or calculation was run, and no historical Actions run records were re-queried. The review changes no production calculation or scientific result. A workflow review is not scientific acceptance.

## Inventory

| Workflow | Current Git blob | Trigger branch | Status |
|---|---|---|---|
| `.github/workflows/b16-neutrino-flavour-opacity.yml` | `6051fd8657371fbae7d3dd53c62ca5b9e593520e` | `research/moving-muon-thermal-rates-20261107` | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-numu-positive-branch-sensitivity.yml` | `3ca1b22ccedb06a8595d4457fa038132d59cb19c` | `research/moving-muon-thermal-rates-20261107` | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-numu-profile-sensitivity.yml` | `20d83de77ab03ed412b8bedf425f71a0275f1bc0` | `research/moving-muon-thermal-rates-20261107` | `REVIEWED_WITH_NOTES` |
| `.github/workflows/muon-chemical-potential-audit.yml` | `890153dd8a8b8a061ff10ca04b4cf68d9022180d` | `research/moving-muon-thermal-rates-20261107` | `REVIEWED_WITH_NOTES` |
| `.github/workflows/muon-profile-sensitivity-10mev.yml` | `e6e4a47d28f195e73f8f4462fa11d949d2e0f855` | `codex/major44-axial-cooling-constraints-20261105` | `REVIEWED_WITH_NOTES` |

## Shared workflow behavior

All five use `workflow_dispatch`, check out the triggering commit SHA, run on `ubuntu-latest` with Python 3.12, install unpinned NumPy/SciPy, grant workflow-wide `contents: write`, and commit generated JSON back to the triggering branch. Each job has a branch-name guard. The four moving-muon workflows use a concurrency group without cancelling in-progress runs; their archive steps use an empty-staging check and fetch/rebase/push retries. The legacy-named muon-profile workflow has a more specialized rebase-conflict path for generated JSON files.

The write permission is used only for result archival; separating calculation from the commit step would allow the calculation job to use read-only permissions. Dependency versions are not locked, so reruns can resolve a different numerical environment.

## Per-workflow findings

### Flavour-resolved neutrino opacity

The workflow runs its focused flavour-opacity tests and a 10 MeV, finite-grid decomposition, checks that production axial files are unchanged, then commits the JSON output. The test checks the decomposition's channel bookkeeping and symmetry, while the workflow does not enforce a global transport or physical acceptance threshold.

The push filter covers the driver, its test and the workflow file, but not the imported shared B.1/B.2 audit helpers, reconstructed profile inputs, or the default Fig. 7 luminosity reference. A helper or reference-only change therefore will not trigger this workflow on push.

### Positive muon-neutrino branch sensitivity

The driver varies the positive `mu_numu` branch in a restricted radial region and compares the resulting escape/luminosity diagnostic. This is a one-factor stress test, not an uncertainty estimate or a measurement of profile error. The workflow runs no dedicated unit test; production-output immutability is checked before committing its JSON.

Its push filter includes only the driver and workflow. It omits the shared emission-radius/escape implementation, the profile and Fig. 7 reference inputs, and other rate/opacity helpers used downstream. Changes to those files alone will not trigger this run.

### Whole-profile muon-neutrino sensitivity

The workflow runs the focused profile-scaling test, evaluates the 10 MeV sensitivity cases, verifies production outputs remain unchanged, and commits a JSON result. The test covers scaling behavior and the identity point; it does not establish a full transport solution.

The push filter includes the driver and focused test but omits the shared emission-radius/escape code, profile data, and the default Fig. 7 reference. The sensitivity factors are prescribed scenarios, not a statistical uncertainty band.

### Muon chemical-potential and density audit

The workflow runs inversion/convention tests and evaluates selected radii (0, 5, 8, 10, 12 and 15 km) against the Caputo density digitization, then checks production outputs and archives JSON. Its path filter includes the driver, test, SFHo digitized profile, and Caputo density points.

The audit's internal Fermi-integral consistency and selected-radius comparisons do not resolve the documented difference between Caputo's absolute muon density and Bollig Fig. 3, nor establish which plotted density convention Bollig used. No rescaling or replacement of the adopted baseline follows from this workflow alone.

### 10 MeV Ferreira-profile sensitivity

This workflow runs the focused profile test, the chemical-potential provenance audit, and a one-factor comparison using the Ferreira profile; it protects production and referee-response files and commits two JSON outputs. The branch `codex/major44-axial-cooling-constraints-20261105` still exists in the current branch search, so the legacy-looking name alone does not justify marking this workflow historical. The explicit branch guard means manual dispatch is limited to that branch.

The push filter includes the diagnostic drivers, test and two data files, but omits the shared three-layer Fig. 7 decomposition helper and profile-provenance sidecar read by the diagnostic path. It also uses the older branch's profile and workflow context. The recorded Ferreira-vs-Caputo comparison is a scenario diagnostic; it does not supersede the adopted Caputo baseline or resolve the absolute-density discrepancy.

## Repository follow-up

- All five entries are now individually reviewed as `REVIEWED_WITH_NOTES`; none is classified historical solely from its branch name.
- Consider adding the actual shared helpers and default reference/profile inputs to each push path filter, or using a shared workflow for dependency-aware triggers.
- Limit `contents: write` to the archive step and pin or constrain numerical dependencies for reproducible reruns.
- Keep stress-test outputs separate from physical acceptance claims. The open Caputo/Bollig density-convention question remains open.

