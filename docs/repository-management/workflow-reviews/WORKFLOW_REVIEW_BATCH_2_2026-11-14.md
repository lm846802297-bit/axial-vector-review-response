# GitHub Actions workflow review — second sample (2026-11-14)

## Scope

Reviewed the complete YAML of 15 B.1/B.2/B.16/EOS/Fig. 7/finite-mixing/Major 1 workflows. The review covered branch/path filters, permissions, checkout ref, runner/timeouts, dependency setup, test/command targets, and artifact/write-back behavior. Historical run logs and all caller references were not exhaustively checked.

## Per-workflow findings

| Workflow | Outcome | Findings |
|---|---|---|
| b16-full-b1b2-independent.yml | HISTORICAL_CANDIDATE | Push trigger pinned to research/moving-muon-thermal-rates-20261107; write permission and long numerical run. Preserve as an independent historical validation lane pending branch/run-history check. |
| b16-global-polarization-transport.yml | HISTORICAL_CANDIDATE | Same historical branch pin, write permission and 240-minute timeout. Distinct global mode-resolved transport gate; do not conflate with local amplitude checks. |
| b16-p1iii-eos-full-profile.yml | HISTORICAL_CANDIDATE | Same historical branch pin; write permission; builds profile/EOS artifacts. Current main has archived EOS outputs, but workflow may remain useful for reproducibility. Verify exact source/profile versions before reuse. |
| b16-p1iiie-c4c4b-full-radial-energy-dependence.yml | HISTORICAL_CANDIDATE | Triggered on research/c4c4-energy-dependence-20261112 and commits full-radial outputs. PR #84/#85 integration history must be checked before classifying as superseded. |
| b16-p1iiie-c4c3-radial-scattering.yml | REVIEWED_WITH_NOTES | Read-only permissions and targeted C4-C3 tests; exact checkout. Good least-privilege pattern. Trigger remains pinned to old moving-muon branch; check run history before dispatch. |
| b2-path-energy-convergence.yml | HISTORICAL_CANDIDATE | Historical branch pin, write permission and up to 120-minute run. It checks a specific B.2 energy/path convention, not the complete physical transport acceptance. |
| bollig-profile-vector-audit.yml | HISTORICAL_CANDIDATE | Branch-pinned and write-enabled, archives profile/vector cross-check. Current status has more recent profile/EOS provenance; confirm whether this remains a reusable audit or only an archival workflow. |
| caputo-muon-density-vector-audit.yml | HISTORICAL_CANDIDATE | Branch-pinned, write-enabled source comparison. Preserve source provenance; do not overwrite newer reconstructed-profile inputs without a like-for-like definition audit. |
| fig7-six-mass-reproduction.yml | HISTORICAL_CANDIDATE | Older Major 4.4 branch, write-enabled. Six-mass reproduction is a historical baseline lane, not current global 1687-radius/full-band validation. |
| fig7-ultrafine-0p1.yml | HISTORICAL_CANDIDATE | Branch-pinned, write-enabled, 30-minute fine-mass run. The current status prioritizes the 10 MeV strong-absorption issue and does not authorize a new broad mass scan; keep as history pending relevance check. |
| finite-mixing-model-map.yml | HISTORICAL_CANDIDATE | Read-only, short model-map test, but trigger is pinned to the older Major 4.4 branch. Good least-privilege setup; check branch and run status. |
| independent-belleii-pointwise-audit.yml | REVIEWED_WITH_NOTES | Dedicated Major 1 scalar-pole/Belle II branch, write-enabled output archival. It is separate from the radial-scalar recast's full detector-response gate; preserve distinction. |
| independent-higgs-scalar-matrix-audit.yml | REVIEWED_WITH_NOTES | Dedicated Major 1 branch, exact triggering checkout, tests and output archival. Write permission should be narrowed if output commit-back is not required. Subcalculation success is not complete pole/mixing acceptance. |
| p1b-source-bundle.yml | REVIEWED_WITH_NOTES | Read-only workflow exports a pinned source/input snapshot as an artifact for local reproduction. This aligns with source-bundle policy; check artifact retention and avoid treating the bundle as a numerical result. |
| p1iii-eos-c4c3-radial-scattering.yml | REVIEWED_WITH_NOTES | Read-only permissions and targeted C4-C3 radial-scattering test. It appears to use the historical moving-muon branch and is a local scattering/opacity gate, not a final SN transport result. |

## Cross-cutting findings

1. Most B.16/B.2/EOS/Fig. 7 workflows are branch-pinned to older research branches. This is consistent with preserving research provenance, but their active status cannot be inferred from YAML alone.
2. Several numerical workflows use contents: write even when their scientific result may already be archived. Audit whether they need to commit outputs; if not, switch to read-only only in a separate tested change.
3. Read-only workflows (C4-C3 and source bundle) are preferable for audits that do not mutate repository state.
4. Full B.1/B.2, global polarization transport, EOS profile reconstruction, C4-C3/C4-C4, and Fig. 7 mass scans are distinct calculations with separate inputs and acceptance criteria.
5. Do not delete historical workflows until branch existence, recent runs, downstream references and scientific provenance have been checked.

The 15 outcomes have been recorded in WORKFLOW_AUDIT_REGISTER.csv. No workflow YAML, trigger, permission, branch or numerical output was changed.