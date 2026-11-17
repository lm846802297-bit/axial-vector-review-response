# Workflow review: B.16 high-energy kernel pinned NumPy regression

Review date: 2026-11-15  
Workflow: \`.github/workflows/b16-high-energy-kernel-regression.yml\`  
Reviewed commit: \`b8901a3fd6813390c3c707c31516242c0f25ad9e\`  
Run: [#43646106550](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43646106550)

## Static workflow review

- Trigger: push to the maintenance review branch, path-filtered to the B.16 audit helper, its tests, the pinned requirements file, and this workflow; manual \`workflow_dispatch\` is also enabled.
- Runner: GitHub-hosted \`ubuntu-latest\`.
- Runtime: Python 3.12.14; NumPy 2.5.4; SciPy 1.18.1, all explicitly checked at runtime.
- Permissions: \`contents: read\`; no repository write-back, secrets, or production-output mutation.
- Steps: install pinned numerical dependencies; record \`pip freeze\`; run four focused unittest modules.
- Timeout: 20 minutes.

## Executed result

Run #43646106550 completed successfully. All 20 tests passed:

| Suite | Tests |
|---|---:|
| B.16 channel-resolved Fermi-pair average | 4 |
| B.6/B.10/B.4 neutrino inverse-decay kernel | 4 |
| Independent analytic B.2 path helper | 5 |
| Generic static-spherical GR ray kernel | 7 |
| **Total** | **20** |

## Scope limitation

This is a pinned regression workflow, not a full B.16 transport run. It does not generate strict NumPy counterparts for the archived V8 channel-resolved, high-energy chord, frozen-source outer-temperature, or global path-redshift JSON files. A successful run validates the tested helper functions and generic geometry tests only; it does not close the Fig. 7 physical acceptance gate or authorize an axial-vector constraint update.

Outcome: \`REVIEWED_WITH_NOTES\`.
