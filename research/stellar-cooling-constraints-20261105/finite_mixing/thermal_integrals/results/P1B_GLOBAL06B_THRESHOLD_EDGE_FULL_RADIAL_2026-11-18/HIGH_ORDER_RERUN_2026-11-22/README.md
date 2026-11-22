# B.13 high-order rerun — 2026-11-22

This directory records the local primary 431-point P1B-GLOBAL06B targeted high-order run, its exact source/input identity, and independent CI reproductions.

- Local primary run: 431 points, 2,155 ordered evaluations, four workers, 343.5815 s.
- Complete archived push reproduction: [run #45048755752](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45048755752), artifact #14764174323, archive commit `04d7064602b3246e760ba6d80d0c4a0be7744418`.
- Exact PR-event validation: [run #45050501965](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45050501965); Calculate and Validate passed, archive job skipped by design, token read-only.
- The archived artifact contains five native files; all five SHA-256 values match the manifest and all five Git blob SHA-1 values match the committed branch files.
- Local, archived CI and PR-event outputs agree across 10,344 charge/mode rate components after key alignment.
- All targeted quadrature and interpolation gates pass.
- Full 1,687-node global high-order acceptance remains false.

See [the detailed report](../../../../../../../../../../../../docs/repository-management/B13_HIGH_ORDER_TARGETED_RERUN_2026-11-22.md), [the provenance JSON](B13_HIGH_ORDER_PROVENANCE.json), [the local/CI comparison](LOCAL_CI_CROSS_RUN_COMPARISON.json), and [the source identity map](SOURCE_FILE_IDENTITY.json).
