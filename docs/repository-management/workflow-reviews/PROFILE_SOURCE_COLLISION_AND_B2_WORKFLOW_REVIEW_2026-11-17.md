# Eighty-fifth review: profile-source, collision-integral and B.2 audit workflows

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `8366e8139e62a1b50408e61a39f41c17851122ad`  
Scope: four workflows for collaborator-source validation, Caputo off-frame figure vertices, direct collision-integral checks, and an independent Eq. (B.2) path integral.

This is a static workflow/provenance review. No workflow, test, or calculation was run. The checks described below have bounded software/model scopes and do not establish full supernova transport acceptance.

## Inventory

| Workflow | Current Git blob | Scope | Status |
|---|---|---|---|
| `.github/workflows/build-stellar-cooling-review-archive.yml` | `14f76d295ca242cc1539ce1598f5c1e77617aab0` | Manual validation of collaborator-source tests and outputs | `REVIEWED_WITH_NOTES` |
| `.github/workflows/caputo-offframe-thermodynamic-audit.yml` | `507a727bec95832f043c0519a6e496f497345f2a` | Caputo Fig. 1 off-frame thermodynamic vertices | `REVIEWED_WITH_NOTES` |
| `.github/workflows/direct-collision-integrals.yml` | `3c73888180ec3c295cd58fcdf170d3d63589b994` | Independent neutrino-coalescence and semi-Compton integrals | `REVIEWED_WITH_NOTES` |
| `.github/workflows/eq-b2-independent-path-integral.yml` | `67c96d1eafdf10dc9c1e60fdf789b27f8bc351e1` | Independent Eq. (B.2) path/angular quadrature | `REVIEWED_WITH_NOTES` |

## Findings

### Collaborator-source validation

This workflow is manual-dispatch only, uses a read-only token and Python 3.11, installs the collaborator archive's review requirements, runs axial-core tests while excluding the Blinov reproduction directory, runs both one-VEV/two-VEV mapping test suites, smoke-tests the shared thermal adapters, validates saved axial outputs, and generates a temporary log-log figure/interpolation audit. It deliberately creates no ZIP, artifact, or release.

The job has no branch guard; manual selection can run against the selected ref. Its validation results and generated figure are ephemeral because the workflow does not upload an artifact. The workflow does not claim to build or publish the collaborator archive despite the archival wording in its filename.

### Caputo off-frame thermodynamic vertices

The workflow checks out the event SHA, runs the off-frame audit, checks that production axial outputs are unchanged, and commits JSON/Markdown. The driver downloads the versioned Caputo source PDF, validates the embedded SHA-256, checks vector-path/clipping support and compares extracted vertices with committed temperature and muon-potential data. The path filter covers the driver, workflow and the directly compared temperature/μ data. It uses broad write permission for archival; NumPy/PyMuPDF are not version-pinned.

The audit tests source-figure extraction and stored digitization consistency. The off-frame plotted vertices remain public-figure geometry, not newly recovered simulation data.

### Direct collision integrals

Pushes are restricted to the legacy-named `codex/major44-axial-cooling-constraints-20261105` branch, but the job itself has no branch guard and the workflow supports manual dispatch. Thus a manual run can execute on another selected branch, and the archive step pushes to that branch. The workflow grants `contents: write`.

It runs two focused test modules, including detailed-balance regressions, then computes an independent adaptive collision-integral JSON and commits it with a staged-diff guard and rebase retries. The driver documents its boundary: neutrino coalescence/inverse decay is integrated independently by flavor and mode; semi-Compton uses the published B.14--B.19 non-recoil approximation, not the full moving-muon B.13 phase-space integral. The path filter includes the production rates, audit/tests, profile and matrix-element reference. NumPy/SciPy are unpinned and there is no explicit job-level branch condition.

### Independent Eq. (B.2) path integral

The workflow is branch-guarded for the legacy-named codex branch, checks out the event SHA, runs focused path-integral tests and a fixed-profile independent geometric path/angular audit, then archives JSON. Before committing, it detects whether an equivalent result is already present and preserves its original run provenance; conflicts on the generated output are handled explicitly. The filter includes the driver/test, `reference.py`, profile, Fig. 7 three-layer reference and workflow.

It uses workflow-wide write permission and unpinned NumPy/SciPy. The independent calculation is a scalar, polarization-summed Eq. (B.2) path audit with frozen local rates/profile inputs. It is not a new local-rate derivation or a full axial transport result.

## Maintenance notes

- Add a job-level branch guard to direct collision-integral manual dispatch before allowing the archive step to push, or restrict dispatch to the intended legacy branch.
- Keep the collaborator validation job's no-artifact behavior explicit; preserve downloadable evidence only if an artifact contract is added.
- Pin numerical dependencies and narrow write permissions to the archive steps where possible.
- Maintain each audit's declared approximations: off-frame digitization is not raw simulation data; direct semi-Compton is the non-recoil approximation; Eq. (B.2) checks do not establish full transport.
