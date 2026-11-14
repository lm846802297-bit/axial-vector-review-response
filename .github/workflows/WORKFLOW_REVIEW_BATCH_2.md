# GitHub Actions workflow review — second sample (2026-11-14)

Reviewed 15 YAML files from the B.1/B.2/B.16/EOS/Fig. 7/finite-mixing/Major 1 groups.

| Workflow | Outcome | Findings |
|---|---|---|
| b16-full-b1b2-independent.yml | HISTORICAL_CANDIDATE | Pinned to the historical moving-muon branch; write permission and long run. Preserve as independent validation lane pending branch/run-history check. |
| b16-global-polarization-transport.yml | HISTORICAL_CANDIDATE | Same branch pin, write permission and 240-minute timeout. Distinct global mode-resolved transport gate, not a local amplitude test. |
| b16-p1iii-eos-full-profile.yml | HISTORICAL_CANDIDATE | Branch-pinned, write-enabled profile/EOS archival. Verify exact profile and EOS versions before reuse. |
| b16-p1iiie-c4c4b-full-radial-energy-dependence.yml | HISTORICAL_CANDIDATE | Triggered on the C4-C4 energy branch and commits full-radial outputs. Check PR #84/#85 integration and run history before deprecation. |
| b16-p1iiie-c4c3-radial-scattering.yml | REVIEWED_WITH_NOTES | Read-only permissions, exact checkout and targeted C4-C3 tests. Trigger remains on a historical branch. |
| b2-path-energy-convergence.yml | HISTORICAL_CANDIDATE | Branch-pinned, write-enabled B.2 energy/path convention test; not full transport acceptance. |
| bollig-profile-vector-audit.yml | HISTORICAL_CANDIDATE | Branch-pinned and write-enabled profile/vector comparison. Check whether newer profile/EOS provenance supersedes its inputs. |
| caputo-muon-density-vector-audit.yml | HISTORICAL_CANDIDATE | Branch-pinned, write-enabled source comparison. Do not overwrite newer reconstructed-profile inputs without a like-for-like definition audit. |
| fig7-six-mass-reproduction.yml | HISTORICAL_CANDIDATE | Older Major 4.4 branch and write-enabled. Six-mass reproduction is historical baseline, not current full-band transport validation. |
| fig7-ultrafine-0p1.yml | HISTORICAL_CANDIDATE | Branch-pinned fine-mass scan. Current priorities do not authorize a broad new scan; preserve as history pending relevance check. |
| finite-mixing-model-map.yml | HISTORICAL_CANDIDATE | Read-only short model-map test, but trigger pinned to older Major 4.4 branch. |
| independent-belleii-pointwise-audit.yml | REVIEWED_WITH_NOTES | Dedicated Major 1 scalar-pole/Belle II branch and output archival. Keep separate from the full detector-response recast gate. |
| independent-higgs-scalar-matrix-audit.yml | REVIEWED_WITH_NOTES | Dedicated Major 1 branch, exact triggering checkout and tests. Narrow write permission if output commit-back is not needed. Subcalculation pass is not complete pole/mixing acceptance. |
| p1b-source-bundle.yml | REVIEWED_WITH_NOTES | Read-only source/input snapshot artifact for local reproduction. Good source-bundle pattern; artifact is not a numerical result. |
| p1iii-eos-c4c3-radial-scattering.yml | REVIEWED_WITH_NOTES | Read-only exact C4-C3 radial-scattering test. Local scattering/opacity gate, not final SN transport. |

## Cross-cutting findings

1. Most B.16/B.2/EOS/Fig. 7 workflows are pinned to older research branches. This is consistent with preserving provenance, but active status cannot be inferred from YAML alone.
2. Several numerical workflows use contents: write even where results may already be archived. Audit whether write-back is necessary; change permissions only in a separate tested PR.
3. Read-only workflows are preferable for audits that do not mutate repository state.
4. Full B.1/B.2, global polarization transport, EOS reconstruction, C4-C3/C4-C4 and Fig. 7 scans have distinct inputs and acceptance criteria.
5. Do not delete historical workflows until branch existence, recent runs, callers and scientific provenance have been checked.

The 15 outcomes are recorded in WORKFLOW_AUDIT_REGISTER.csv. No workflow YAML, trigger, permission, branch or numerical output was changed.
