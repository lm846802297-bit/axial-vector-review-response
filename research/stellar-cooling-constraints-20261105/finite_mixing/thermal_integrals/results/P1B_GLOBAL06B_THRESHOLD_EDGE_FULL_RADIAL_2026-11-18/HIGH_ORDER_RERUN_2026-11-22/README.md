# B.13 high-order rerun — 2026-11-22

This directory records the local primary 431-point P1B-GLOBAL06B targeted high-order run, its exact source/input identity, and independent CI reproductions.

- Local primary run: 431 points, 2,155 ordered evaluations, four workers, 343.5815 s.
- Exact source commit: `e49908762e90271f4bc84be75e19577431febd4c`; 12/12 source identity entries match Git blob SHA-1, SHA-256 and byte count.
- Canonical local/CI comparison: [run #45043212683](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45043212683); 431/431 points and all 10,344 charge/mode rate components matched exactly.
- Latest successful push reproduction: [run #45054965537](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45054965537), artifact #14766494558, archived in commit `27204a98aacac2eb2df9731fec30a894dfd2616a`. Calculate/Validate/Archive all passed; calculation token was read-only and only the guarded archive job had write permission.
- Latest PR-event validation: [run #45052985191](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45052985191); Calculate and Validate passed, artifact uploaded, archive job skipped by design, token read-only.
- Latest push artifact: ZIP SHA-256 `05b71bc6bd27dbe42ba0f5eed975861c16ec8fe181ff913924d84e791058e487`; five native files match their Git blobs and SHA-256 manifest byte-for-byte (5/5).
- Four Intel Xeon runs (#45043212683, #45048755752, #45050501965, #45052985191) are numerically identical after `(r_km,x)` alignment. The later AMD EPYC run #45054965537 differs from Intel by at most (2.22\times10^{-16}) absolute and (5.15\times10^{-16}) relative across 10,344 rate components; quadrature ladders and physical residuals agree to machine precision.
- All targeted quadrature and interpolation gates pass. Full 1,687-node global high-order acceptance remains false.

The local output manifest now contains corrected hashes for the environment, run command and post-run comparison, plus the local run summary. The original local validator hash claim is preserved separately from the committed validator hash: the exact local validator bytes are not recoverable from repository history, while the committed validator is independently compiled and executed successfully by CI.

See [the detailed report](../../../../../../../../../../../../docs/repository-management/B13_HIGH_ORDER_TARGETED_RERUN_2026-11-22.md), [the provenance JSON](B13_HIGH_ORDER_PROVENANCE.json), [the local/CI comparison](LOCAL_CI_CROSS_RUN_COMPARISON.json), [the source identity map](SOURCE_FILE_IDENTITY.json), and [the output hash manifest](LOCAL_OUTPUT_HASHES.sha256).
