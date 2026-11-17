# Eighty-sixth review: Fig. 7 source and convergence workflows

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `109f5cdc420fccd007c8d13cc5bc085124fb2202`  
Scope: eight workflows for Fig. 7 source-PDF drawing/digitization checks, the 10 MeV equation-chain and three-layer audits, spatial weighting, and scalar-scan resolution studies.

This is a static review of automation wiring and evidence boundaries. No workflow, test, or calculation was run. A converged scalar scan or digitization audit does not by itself reproduce the full transport curve or establish a physical exclusion.

## Inventory

| Workflow | Current Git blob | Scope | Status |
|---|---|---|---|
| `.github/workflows/fig7-10mev-equation-chain-audit.yml` | `c47d947261a8a938b9ab25a5b37e417f9bfd5f1e` | 10 MeV local-to-global equation-chain diagnostic | `REVIEWED_WITH_NOTES` |
| `.github/workflows/fig7-10mev-three-layer-audit.yml` | `4581ca8b282984e47049c213d656365fec3cdc8d` | 10 MeV source/opacity/transport decomposition | `REVIEWED_WITH_NOTES` |
| `.github/workflows/fig7-digitization-geometry-audit.yml` | `9eddfa8f8c267f7b0850636fc934b7e0d1428a3d` | Raw PDF geometry and 10 MeV tail digitization | `REVIEWED_WITH_NOTES` |
| `.github/workflows/fig7-highres-convergence.yml` | `0953b10ba3a6df11ff5ae4da2b3afc254ad17c9b` | Seven-mass high-resolution scalar scan and comparison | `REVIEWED_WITH_NOTES` |
| `.github/workflows/fig7-refined-scan.yml` | `a46b50007da8318b3c4e060297b8ada71650ca8a` | Six-mass refined scalar scan | `REVIEWED_WITH_NOTES` |
| `.github/workflows/fig7-source-drawings.yml` | `c51b1a9c2b7b9fbf86c77a9bb65103757a4ad387` | Pinned source-PDF drawing geometry and digitization audit | `REVIEWED_WITH_NOTES` |
| `.github/workflows/fig7-spatial-weight-matrix.yml` | `068b3302ab30601e14ec79b6e682da256035b225` | Joint source-radius/absorber-radius weight audit | `REVIEWED_WITH_NOTES` |
| `.github/workflows/fig7-ultrafine-light-mass.yml` | `69b6e7c65fbdad460e32b387e6497c540490635f` | Ultrafine quadrature for two ultralight masses | `REVIEWED_WITH_NOTES` |

## Shared behavior

All eight use manual dispatch; their push triggers are limited to one of the moving-muon or legacy-named codex research branches, with job-level branch guards. They use Ubuntu/Python 3.12, workflow-wide `contents: write`, and unpinned NumPy/SciPy. Each commits JSON outputs to the research branch. None of the scalar-scan workflows has a dedicated test step.

## Findings by workflow

- **Equation-chain audit:** runs the 10 MeV Eq. 17--20 and 31--33 diagnostic and archives JSON. The path filter includes the driver, shared reference implementation, reconstructed profile and Fig. 7 JSON. There is no test step, production-file immutability check, or separate YAML-level numerical acceptance gate.
- **Three-layer audit:** runs a focused regression test, computes the source/opacity/transport decomposition, checks production and referee-response files are unchanged, then commits JSON. Its push filter omits `reference.py`, the default profile and Fig. 7 input; changes to these inputs alone will not trigger the workflow. The archive step uses a direct push without a rebase/retry guard.
- **Digitization geometry:** runs path/coordinate tests, downloads the versioned arXiv v2 source archive, and calls a driver that checks the pinned PDF SHA, all six drawing paths and the 25 archived 10 MeV reference vertices. The workflow itself does not hash the downloaded archive, but the driver validates the extracted PDF. The path filter omits the default Fig. 7 JSON used for comparison. The result is a digitization-provenance check, not a luminosity recalculation.
- **High-resolution scalar scan:** computes a seven-mass scan, compares it with the Fig. 7 reference and a baseline scan, then commits three JSONs. The trigger filter names only `compare_fig7_resolution.py`; it omits the scan implementation, comparison helper, profile, Fig. 7 input and baseline scan files. There is no test or explicit fail-threshold step shown.
- **Refined scalar scan:** computes a six-mass finer-grid scan and two comparisons, then commits outputs. The push filter contains only the workflow file, so changes to the scan/comparison code or inputs do not trigger it automatically. It remains manually dispatchable on the guarded legacy branch. No focused tests or explicit numeric acceptance thresholds are in the workflow.
- **Source drawings:** downloads the versioned arXiv v2 source archive, records archive/PDF hashes and drawing metadata, checks the six digitized curves against the PDF paths, then commits JSON. It does not run a focused test or a production immutability check. The workflow records source hashes; the inspected driver does not enforce a predeclared expected archive hash.
- **Spatial-weight matrix:** runs focused bookkeeping tests and a joint production/absorber spatial audit with profile, Fig. 7 and path-integral references, then commits JSON using a staged-diff guard and output-conflict handling. The path filter includes the driver, test, Eq. (B.2) helper, profile and three-layer input. There is no separate YAML-level numeric threshold block.
- **Ultrafine light-mass scan:** computes two ultralight mass curves and compares them with the reference and a finer-grid baseline before committing three JSONs. Its push filter contains only the workflow file. It has no focused test or explicit numerical acceptance thresholds; changes to the scan code, shared reference implementation, profile or Fig. 7 input will not trigger it automatically.

All scan runs are diagnostics of the configured scalar, fixed-profile implementation. They do not update production axial outputs or substitute for the unresolved vector strong-absorption discrepancy.

## Maintenance notes

- Expand push filters for the three-layer, digitization and scan workflows to cover every code and data dependency; the refined and ultrafine scans currently trigger on workflow-file changes alone.
- Add explicit acceptance thresholds and focused tests to the heavy scalar scans, or document that their role is exploratory and retain them as manual-only.
- Use a guarded archive step with rebase/retry rather than direct `git push` for the three-layer output.
- Keep source-archive/PDF hashes tied to an expected version and preserve the 10 MeV curve-digitization comparison as separate provenance evidence.
- Workflow-wide write access and unpinned numerical dependencies remain reproducibility/least-privilege follow-ups.
