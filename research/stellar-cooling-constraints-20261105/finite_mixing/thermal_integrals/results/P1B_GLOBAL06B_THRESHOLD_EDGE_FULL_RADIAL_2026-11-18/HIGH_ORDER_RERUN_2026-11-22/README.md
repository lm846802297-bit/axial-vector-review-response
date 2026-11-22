# B.13 high-order rerun — 2026-11-22

This directory records the local primary 431-point P1B-GLOBAL06B targeted high-order run, its exact input/source identity, and the independent GitHub Actions reproduction.

- Local primary run: exit status 0, 4 workers, 343.5815 s.
- Independent CI run [#45043212683](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45043212683): Calculate, Validate and Archive all succeeded.
- CI artifact ID: `14762941323`; ZIP SHA-256: `20cb282c2f43237d9190b59a2056e1fd8b5a405410a83238e900121b22ff9e70`.
- All five CI artifact files match the archived Git blobs byte-for-byte.
- 431 unique `(r,x)` points; 2,155 ordered quadrature evaluations.
- Local and CI results agree across 10,344 charge/mode rate components after key alignment.
- All targeted quadrature and interpolation gates pass.
- Full 1,687-node global high-order acceptance remains false.

See [the detailed report](../../../../../../../../../../../../docs/repository-management/B13_HIGH_ORDER_TARGETED_RERUN_2026-11-22.md), [the provenance JSON](B13_HIGH_ORDER_PROVENANCE.json), [the local/CI comparison](LOCAL_CI_CROSS_RUN_COMPARISON.json), and [the source identity map](SOURCE_FILE_IDENTITY.json).
