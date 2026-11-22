# B.13 targeted high-order rerun — 2026-11-22

## Local primary calculation

The local primary calculation completed with exit status 0: 431 unique `(r,x)` points, 2,155 ordered quadrature evaluations, four workers and 343.5815 s runtime. The local runner was Linux / Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 on AMD EPYC 9V74. The exact source driver, frozen target input, profile and imported dependencies are identified by source commit `e49908762e90271f4bc84be75e19577431febd4c`; all 12 entries in `SOURCE_FILE_IDENTITY.json` match their Git blob SHA-1, SHA-256 and byte count.

## Independent GitHub Actions runs

### Initial archival attempt — run #45041173008

The calculation, validation and artifact upload passed, but the archive job failed because `CI_RUN.log` matched a repository ignore rule. The failed attempt is retained as historical evidence and is not used as the archive acceptance.

### First complete archive — run #45043212683

[Run #45043212683](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45043212683) completed Calculate, Validate and Archive successfully. It reproduced 431/431 task points and archived artifact #14762941323 in commit `8b5d28b58951623e375436478e6a524670e7ee18`. This is the CI run referenced by the original local/CI comparison record.

### Exact-head push reproduction — run #45048755752

[Run #45048755752](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45048755752) completed Calculate, Validate and Archive successfully on branch commit `1ee26f742e9f03cbccdd4237bbc8bb1c790ce91a`. It used Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0 on Ubuntu 24.04 / Intel Xeon 6975P-C, four workers, 485.5 s runtime. Its artifact #14764174323 has ZIP SHA-256:

`5714902f8d44be284e5f067d99dcccff16556a1e9552f9f38a5bf1c993d8ff0d`

The archive commit is `04d7064602b3246e760ba6d80d0c4a0be7744418`. The five artifact files (raw points, acceptance summary, independent validation report, CI environment and CI log) were downloaded and verified: their SHA-256 values match `CI_OUTPUT_HASHES.sha256`, and their Git blob SHA-1 values match the files committed on the B.13 branch (**5/5**).

### Pull-request event reproduction — run #45050501965

[Run #45050501965](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45050501965) validated PR #133's branch head `b328f1bfba935ed50c8aee4ed0c15c1b273e0b33` (event merge SHA `38c2ed77ee95c6c9b3f9741d50dbc3bd5d3851c4`). Calculate, validation, and artifact upload passed; the archive job was intentionally skipped for the `pull_request` event. The job had `contents: read` only. Artifact #14765736550 was downloaded; it is retained as a PR-event artifact, not committed to the branch.

## Numerical cross-checks

The original [local/CI comparison report](../../research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_RERUN_2026-11-22/LOCAL_CI_CROSS_RUN_COMPARISON.json) compares the local run with CI run #45043212683. I also independently compared the archived #45048755752 result with #45043212683, and the PR-event #45050501965 artifact with the archived #45048755752 result.

For each pair:
- 431/431 identical task keys after alignment by `(r_km,x)`;
- identical quadrature order ladders;
- 10,344 charge/mode rate components compared;
- maximum absolute and relative rate differences: 0;
- maximum final-order-change difference: 0;
- maximum detailed-balance residual difference: 0;
- maximum mass-shell residual difference: 0.

The raw JSON files are not byte-identical because row order and run-specific metadata differ. The numerical payloads are identical.

## Numerical acceptance and scientific boundary

`N_(r,x)=431`, `N_eval=2155`. The maximum final successive-order change is `3.29220848525901e-4`; maximum radial midpoint interpolation error is `8.311070322862653e-4`; maximum energy PCHIP error is `6.716564877619043e-4`. Maximum detailed-balance and mass-shell residuals are `5.027846521385086e-15` and `2.0432421890821873e-13`.

This is a targeted high-order audit of the ten worst radial intervals and ten worst low-`x` energy points, not full 1,687-node global high-order acceptance. The provenance retains:

`"full_global_high_order_acceptance": false`

No production rate, opacity, transport output, Fig. 7 result or axial-vector constraint is changed.


## Latest independent CI reproductions

### Read-only PR-event validation — run #45052985191

[Run #45052985191](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45052985191) validated PR #133 at head `e0e5ea8a9599dedce5d14429a0e19aeca39b4653` (event merge SHA `bb32e67c0704ed0dfb9b43eb731d0badbc75fb4d`). The Calculate job completed all 431 points and independent validation; artifact #14766419782 was uploaded. The archive job was skipped by design and the job token was `contents: read`. Runtime was 456.835 s on Ubuntu 24.04 / Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 / Intel Xeon 6975P-C, four workers.

### Latest exact-workflow push reproduction — run #45054965537

[Run #45054965537](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/45054965537) ran on exact workflow head `e2a9bea45c84f996ab728ec0d29bafa4cfd7c8cc`, workflow blob `2a250a2dc32d2c3c676b7220c838ba52e5382525`. Calculate, Validate and Archive all succeeded. The calculation job had `contents: read`; only the guarded archive job had `contents: write`.

- Calculate job: `137308041672`; archive job: `137311756148`.
- Artifact #14766494558, 199,597 bytes; ZIP SHA-256 `05b71bc6bd27dbe42ba0f5eed975861c16ec8fe181ff913924d84e791058e487`.
- Archive commit: `27204a98aacac2eb2df9731fec30a894dfd2616a`.
- Environment: Ubuntu 24.04, Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, AMD EPYC 7763, four visible vCPUs, 16,760,344,576 bytes RAM.
- Runtime: 709.780 s; 431/431 points; 2,155 ordered evaluations.
- All five artifact files match the branch's Git blob SHA-1 and `CI_OUTPUT_HASHES.sha256` entries byte-for-byte.

## Cross-run numerical comparison

The four Intel Xeon runs (#45043212683, #45048755752, #45050501965 and #45052985191) have identical task-key sets and quadrature ladders and match exactly across 10,344 charge/mode rate components.

The AMD EPYC run #45054965537 was compared against those Intel runs after alignment by `(r_km,x)`:
- 431/431 task keys and identical quadrature order ladders;
- 10,344 rate components;
- maximum absolute rate difference: `2.220446049250313e-16`;
- maximum relative rate difference: `5.141200469148187e-16`;
- maximum final-order-change difference: `4.153554699990326e-16`;
- maximum detailed-balance residual difference: `3.537854528309584e-16`;
- maximum mass-shell residual difference: `0`.

These are floating-point roundoff-scale differences across CPU architectures. The targeted convergence and physical closure gates remain passed.

## Provenance hash reconciliation

The current local files were rehashed from their committed bytes. The environment hash is `9372d470c0fbb9629de515e7b94415b6ed82874877bedee9abffea434f809b50`, the run-command hash is `e1246d7e89358c74f614b5b7c1cbdca659749d062faa73017681829b29b46d2c`, and the updated comparison-report hash is `50e91d3ad929c1b3d3936d43b0c018d963c79b604a65b93164f23bf5ae59d4d8`; the output manifest also includes the corrected local run summary hash `80916409f3eae841d2944f929ecf2988107fd2f679d03d527da3d3508ebc06a2`. The original raw result, acceptance summary, local validation report and run log hashes continue to match.

The local run record's validator hash `00e6d1ef2c75d23e3e9b774ac30f7bbb7a427b9f77cdfc9f739b7cc22858284a` does not match the committed validator file (`c15cb3d706bd4ee03beae83755dd465fef8197e38d1699952edaee0440433d36`, Git blob `1f3a10da5f4aa33c25b371333d76ff8f6a2a4f2a`). The exact local validator bytes are not present in repository history or the retained local runtime files. This identity gap is explicitly recorded; the committed validator is a separate reproducible validator that was compiled and executed successfully by the independent CI runs.

## Workflow inventory and permission review

The B.13 branch now has **119 workflow YAML files and 119 unique register entries**, with zero missing, duplicate or extra entries. The workflow README has 119 links. Status counts are 104 `REVIEWED_WITH_NOTES`, 14 `HISTORICAL_CANDIDATE`, one `ACTIVE`, and zero pending.

The B.13 workflow uses `contents: read` by default and for Calculate. Only the separate push archive job receives `contents: write`. PR events `opened`, `reopened` and `ready_for_review` run read-only validation; `synchronize` is excluded so an archive-bot commit does not request an approval-gated PR workflow. Push path filters exclude generated output files. Before write-back and before every retry rebase, the archive job compares the workflow, local run summary, source identity and independent validator Git blobs against the latest branch; it refuses stale output and retries at most five times.

The final branch head before this metadata refresh was `27204a98aacac2eb2df9731fec30a894dfd2616a`. No production rate, opacity, transport result, Fig. 7 value or axial-vector constraint is changed.
