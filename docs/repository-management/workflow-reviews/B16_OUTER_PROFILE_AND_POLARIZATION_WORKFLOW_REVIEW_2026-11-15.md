# B.16 outer-profile and polarization workflow review

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: 38acc0837d9457d3c96b25a1ae00c3ded5635931

## Scope

Static review of six workflow definitions associated with the B.16 outer-shell profile, inverse-decay and polarization records. The workflow YAML files remain in .github/workflows. This review records triggers, branch guards, permissions, dependencies, tests, commands, output behavior and known historical run evidence. It does not claim that these workflows ran on the maintenance PR.

## Individual workflow review

| Workflow | Static result | Main execution and caveat |
|---|---|---|
| b16-outer-escape-angular-distribution.yml | REVIEWED_WITH_NOTES | Push is path-filtered to the moving-muon research branch; workflow_dispatch is also available, but the job guard requires that branch. Runs two analytic geometry/statistics tests and the 10 MeV direction/emission-radius audit. contents:write commits the JSON output. |
| b16-outer-profile-input-audit.yml | REVIEWED_WITH_NOTES | Same branch/manual guard. Runs three shell-grid/analytic-chord tests, then the 22--25 km profile/input interpolation audit. Checks production axial outputs before committing JSON. |
| b16-outer-profile-interpolation.yml | REVIEWED_WITH_NOTES | Same branch/manual guard. Runs the path-grid interpolation scan and checks production outputs, but has no dedicated unit-test step. contents:write is used for JSON commit-back. |
| b16-outer-shell-polarization-resolved.yml | REVIEWED_WITH_NOTES | Same branch/manual guard. Runs four mode-sum, detailed-balance and direction-reversal tests; runs 48-point mode rates and a 512-point direct phase-space check; explicitly asserts profile SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. |
| b16-neutrino-inverse-decay-audit.yml | REVIEWED_WITH_NOTES | Same branch/manual guard. Runs four B.6/B.10/B.4 regression tests and a 192-point direct angular integral. The paired JSON uses the historical 501-node profile, so it must not be treated as a current-profile transport result. |
| b16-neutrino-inverse-decay-direct.yml | REVIEWED_WITH_NOTES | Same branch/manual guard. Runs the 512-point direct mode-resolved phase-space audit and commits its JSON, but has no dedicated test step in this workflow. |

## Shared workflow controls

- All six workflows use ubuntu-latest, set up Python 3.12, and install NumPy/SciPy after upgrading pip. The package versions are not pinned, so a historical green run is not a guarantee of byte-identical future reproduction.
- All six have contents:write because they commit generated JSON back to the research branch. The job-level branch guard prevents these jobs from running on another branch, including this maintenance branch. Consider artifacts plus contents:read for future audits that do not require durable source-tree outputs.
- The production-output diff checks are useful isolation guards. They establish that the selected production files were not changed by the workflow run, not that the physical transport result is accepted.
- The path-interpolation and direct-inverse-decay workflows lack a dedicated test step; their numerical commands still run, but future revisions should add small analytic regression tests.
- No dependency lock or exact NumPy/SciPy version pin is present in these six YAML files.

## Historical run evidence

Four run records were fetched from the GitHub Actions API and confirmed completed with conclusion success:

| Run | Workflow | Research-branch commit |
|---:|---|---|
| 42486733302 | Outer-shell angular distribution | 5bda11f13e11fa8a4ece16306eb728dddf4c611b |
| 42450499283 | Outer-profile input audit | 5feab1135998df4765496f45b8cd8a2627843458 |
| 42479382380 | Outer-profile path interpolation | aa78b55fac8d6b26575c2fb9821ef8949f340d29 |
| 42450822390 | Neutrino inverse-decay audit | 71e00efeb72b664f98b23d8dd7623e0828356383 |

These runs were executed on research/moving-muon-thermal-rates-20261107 at earlier SHAs. They are historical execution evidence, not CI checks for PR #115. No run was asserted for the outer-shell polarization workflow or the direct inverse-decay workflow in this review.

## Register update

The six workflows are now REVIEWED_WITH_NOTES in WORKFLOW_AUDIT_REGISTER.csv. The register totals are 47 REVIEWED_WITH_NOTES, 16 HISTORICAL_CANDIDATE and 52 PENDING. The 115-file inventory is unchanged.
