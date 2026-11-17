# Seventy-ninth review: outer-profile sensitivity workflow wiring

Review date: 2026-11-17  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Reviewed branch head before this report: `bc4176539e4e53c0502633a074e2885e9546924c`  
Scope: four B.16 workflows that stress-test temperature or muon-neutrino chemical-potential continuations in the 20--22 km and 22--25 km shells. YAML definitions were checked against their drivers, shared B.1/B.2 implementation, profile input and archived interpretation notes.

This is a static workflow/provenance review. No workflow was dispatched; no tests or calculations were run; historical Actions run records were not re-queried in this batch; no scientific result or production output was changed. The reports describe bounded stress tests of a reconstructed profile, not measured profile uncertainties or a statistical error band.

## Workflow inventory

| Workflow | Current Git blob | Scope | Disposition |
|---|---|---|---|
| `.github/workflows/b16-outer-22-25-temperature-sensitivity.yml` | `c56522d49aa36a43ba08caf4f0866fb3f1b27d50` | Temperature stress test in 22--25 km | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-outer-numu-22-25km-sensitivity.yml` | `99dd4b921dfdcbe9d237952d944f952c2b65610e` | Muon-neutrino chemical-potential stress test in 22--25 km | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-outer-numu-floor-sensitivity.yml` | `51e6599010d399a84343892fcf0d4104f33d431c` | Figure-floor stress test in 20--22 km | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-outer-temperature-sensitivity.yml` | `abfad14387b21c97be8db3617c5f06785eff9e1d` | Temperature stress test in 20--22 km | `REVIEWED_WITH_NOTES` |

## Findings

### Shared workflow structure

All four workflows trigger on pushes to `research/moving-muon-thermal-rates-20261107` and manual dispatch, guard the job with `github.ref_name`, and check out the triggering `github.sha`. They run on Ubuntu with Python 3.12, install unpinned NumPy/SciPy, grant `contents: write` for the entire job, and archive generated JSON/Markdown by committing to the research branch with a fetch/rebase/push retry loop. Their concurrency settings do not cancel in-progress runs. The scripts call the shared `audit_b16_emission_radius_escape.py` path calculation, which in turn uses the profile, global B.1 source, flavor-resolved rates and shell-opacity helpers.

### Trigger coverage and runtime checks

- All four push path filters include the workflow, the top-level sensitivity driver and `sfho188_digitized.csv`, but omit the shared `audit_b16_emission_radius_escape.py` implementation and its imported rate/opacity helpers. A change to a shared dependency alone will not start these push workflows.
- The 20--22 km temperature, 20--22 km chemical-potential floor, and 22--25 km temperature workflows also omit the default Fig. 7 input `research/stellar-cooling-constraints-20261105/outputs/vector_audit/luminosity_comparison.json`. The 22--25 km chemical-potential workflow includes that reference path, but still omits shared helpers.
- None of the four has a separate unit-test or syntax-compilation step. The 22--25 km chemical-potential workflow checks the profile SHA, scenario names, selected baseline shell diagnostics and sign symmetry. The other three primarily check that production axial files remain unchanged before archiving; they do not assert the report's numerical sensitivity values or a convergence threshold.
- Workflow-wide write access is only needed for the final archive operation. Splitting computation and archival into separate jobs would allow read-only permissions for the compute stage.
- The archive steps include an empty-staging guard and handle concurrent pushes through rebase retries. The three temperature/floor workflows archive both JSON and Markdown; the 22--25 km chemical-potential workflow does likewise.

### Physical scope and provenance boundary

The four drivers use the current reconstructed profile fingerprint `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c` and recompute the B.1 source and B.2 opacity for their prescribed variations. The corresponding notes identify the tested changes as stress scenarios, not inferred outer profiles or statistical intervals. Bollig Figs. 1 and 4 provide cross-check support through 20 km; they do not establish the 20--22 km continuation. The 22--25 km Caputo temperature input is extracted from off-frame PDF vertices rather than raw Garching tables. The notes keep those limitations explicit and do not use the variants to tune the profile or rescale Fig. 7.

The existing notes report that outer shells contribute materially to neutrino path optical depth while the tested \(\mu_\nu\) variations have small effects on the cited endpoints. This review did not recompute those values or assess whether the chosen stress envelopes cover the physical profile uncertainty.

## Follow-up

1. Add shared helper and reference-input paths to the push filters, or provide another mechanism that guarantees the runs follow changes in those dependencies.
2. Add syntax/tests for each driver or document why those checks are intentionally not part of the workflow.
3. Keep sensitivity calculations and archive commits in separate permission scopes where practical.
4. Keep the stress-test interpretation distinct from a measured uncertainty band, full GR transport, and the Fig. 7 acceptance result.
5. Pin NumPy/SciPy versions for stable long-term reproduction, or identify a checked-in lock file.

These four entries move from `PENDING` to `REVIEWED_WITH_NOTES`. No workflow YAML, calculation code, profile input, numerical output, opacity, luminosity, constraint curve, manuscript text or physical parameter was changed.
