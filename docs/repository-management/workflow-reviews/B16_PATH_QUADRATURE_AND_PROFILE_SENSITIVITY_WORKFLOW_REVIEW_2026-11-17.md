# Eighty-third review: B.16 path quadrature and profile-shell workflows

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `36941808e8dd7ca9ab93fee4736b542a28c1e737`  
Scope: four workflows for an independent analytic B.2 path integration, fixed-ω quadrature convergence, shell-removal luminosity sensitivity, and 8--15 km profile-input sensitivity.

This is a static review of workflow configuration and connected inputs. No workflow, test, or calculation was run in this review. The prior reports and YAML contain checks, but this review does not independently validate their outputs or the physical transport model.

## Inventory

| Workflow | Current Git blob | Scope | Status |
|---|---|---|---|
| `.github/workflows/b16-path-independent-analytic.yml` | `304f7e06eb21c87489c2746b0f5674dc32f9c1e9` | Independent analytic B.2 path quadrature | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-quadrature-convergence.yml` | `b38debf2f7572ac06c5faabbdab07a6fffdcd98f` | Fixed-ω B.16 quadrature scan | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-shell-luminosity-sensitivity.yml` | `17924003183fe74ab99b47eb8f7eff2c8bc18375` | Radial-shell opacity-removal diagnostic | `REVIEWED_WITH_NOTES` |
| `.github/workflows/profile-12-15km-audit.yml` | `c26eca33f08fe99ccecaff258d4a0226a2dcbf04` | Reconstructed 8--15 km profile and B.1+B.2 sensitivity | `REVIEWED_WITH_NOTES` |

## Findings

All four workflows trigger on pushes to the moving-muon research branch and manual dispatch, with a branch guard and Ubuntu/Python 3.12 runner. They install unpinned NumPy/SciPy; the profile workflow also installs unpinned PyMuPDF. All have workflow-wide `contents: write` for committing generated results. The first workflow explicitly checks out the named branch rather than the triggering `github.sha`; this creates a moving-ref provenance difference from the other three, which check out the event SHA. The path-independent workflow and profile workflow use non-cancelling concurrency/rebase retries; the other two use the same general archive pattern.

### Independent analytic path

The workflow runs focused tests, recomputes the 10 MeV B.2 path integral with several angular/path orders, verifies the profile SHA and baseline-reproduction residual, checks independent angular quadrature and a bounded final luminosity shift, protects production axial outputs, and commits the JSON. Its path filter includes the driver, test, shared `reference.py` and global-redshift source helper, profile, Fig. 7 input and archived comparison. The checkout should be pinned to the event SHA for an auditable run snapshot.

### Fixed-ω quadrature convergence

The workflow runs the one-factor/combined quadrature scan and archives JSON after checking production axial outputs. It does not run a focused test or an explicit numerical acceptance step in the workflow. The push filter includes the scan driver and emission-radius helper but omits other imported helpers and both default profile/Fig. 7 inputs; changes to those sources alone will not trigger the scan. The result is a quadrature diagnostic, not a full-transport validation.

### Shell luminosity sensitivity

The focused test and 10 MeV shell-removal driver are run, followed by an immutability check and JSON commit. The driver holds the B.1 source fixed while removing selected B.2 shell-opacity contributions, so the output is a diagnostic decomposition rather than an alternate physical supernova model. The push filter omits the default profile, Fig. 7 reference and shared rate/source helpers. The workflow has no separate numeric acceptance gate for its reported shell fractions or luminosity changes.

### 8--15 km profile sensitivity

The workflow downloads hash-pinned public source PDFs, regenerates digitized profiles, runs profile regression tests, audits source-curve identities, computes full B.1+B.2 profile sensitivity and radial convergence, checks production outputs, and commits the regenerated profile inputs and JSONs. Its recursive data path filter covers the profile inputs and outputs along with the named drivers/tests. The source PDFs are downloaded at run time rather than checked in; their expected SHA-256 values are embedded in the extraction driver. Dependencies are unpinned, and the YAML has no separate assertion step for the two newly generated transport JSONs beyond checks performed inside the invoked drivers.

## Maintenance notes

- Pin the independent analytic workflow to `github.sha` to align its provenance with the other push/manual workflows.
- Expand quadrature and shell-sensitivity path filters to include imported helpers and default profile/Fig. 7 inputs.
- Narrow write permission to the archive job where practical; pin Python packages for reproducible environments.
- Keep the shell-removal interpretation explicit: it partitions a fixed-source optical-depth diagnostic, not a self-consistent changed stellar model.
- A passing profile regression or numerical run is not evidence that the reconstructed profile or full B.1+B.2 transport has passed scientific acceptance.
