# B.16 local-rate, escape-phase-space and PR52 archive workflow review

Date: 2026-11-17  
Branch: `maintenance/close-baseline-revision-required-20261117`

## Scope

Reviewed the three new GitHub Actions workflows introduced for the 10 MeV
local-rate/polarization package, the global B.1/B.2 escape phase-space
decomposition, and PR52 scan-archive extraction. The review covers triggers,
branch guards, permissions, dependency pinning, output write-back, concurrency,
test coverage, and the recorded successful runs. It does not constitute
independent physics validation beyond the stated tests and numerical closures.

## Workflow dispositions

| Workflow | Trigger / guard | Runtime and validation | Successful run | Disposition |
|---|---|---|---|---|
| `.github/workflows/b16-local-rate-polarization-samples.yml` | Push to the closeout branch with explicit source/test/profile path filters; explicit job branch guard; no manual dispatch | Python 3.12; NumPy 2.5.4 / SciPy 1.18.1 pinned; local-rate tests; 54-point CSV/JSON/SVG generation; profile fingerprint and closure maxima checked | [#44031506218](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44031506218) | `REVIEWED_WITH_NOTES` |
| `.github/workflows/b16-escape-phase-space-closeout.yml` | Path-filtered push on closeout branch plus manual dispatch; explicit job branch guard | Python 3.12; NumPy 2.5.4 / SciPy 1.18.1 pinned; 8 regression tests; py_compile; high-order B.1/B.2; energy-grid, closure, marginal and joint-bin checks; JSON/CSV/SVG archived | [#44035746636](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44035746636) | `REVIEWED_WITH_NOTES` |
| `.github/workflows/scan-archive-integrity-closeout.yml` | Path-filtered push on closeout branch; explicit job branch guard; no manual dispatch | Python 3.12; standard-library streaming verifier; tests; gzip CRC, compressed/uncompressed SHA-256, byte count, CSV dimensions and row widths; JSON report archived | [#44033029862](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44033029862) | `REVIEWED_WITH_NOTES` |

All three declare `permissions: contents: write` at workflow scope. The token
permission is therefore available to every step in each job, not only the final
artifact write-back step; this is not step-scoped least privilege. The branch
guards, path filters and commit-pinned checkout of `github.sha` restrict the
execution target but do not narrow token scope. The two numerical workflows
pin NumPy/SciPy. The archive verifier uses only the Python standard library,
so it does not install numerical dependencies. Before these workflows are
reused with broader or recurring triggers, split computation/validation into a
`contents: read` job and artifact archival into a separate minimal
`contents: write` job.

## Review findings and residual workflow risks

1. **Branch containment:** all three jobs are guarded to
   `maintenance/close-baseline-revision-required-20261117`; no unguarded
   manual dispatch is present.
2. **Output loops:** generated-output paths are not in the push path filters,
   so bot archival commits do not recursively trigger the same workflow.
3. **Concurrency:** each workflow has a branch-scoped concurrency group with
   `cancel-in-progress: false`. These groups are workflow-specific and do
   not serialize writes across the three different workflows or unrelated
   branch writers.
4. **Write-back race:** the B.16 global escape workflow has a five-attempt
   fetch/rebase/push retry. The local-rate and PR52 archive workflows use a
   direct push without an equivalent retry. Their successful runs show no
   observed collision, but a concurrent writer could still cause a push
   rejection. If these workflows are made recurring or run concurrently,
   add a shared archival queue or the same bounded rebase retry.
5. **Action pinning:** third-party actions use major-version tags
   (`actions/checkout@v4`, `actions/setup-python@v5`) rather than immutable
   commit SHAs. This matches the existing repository convention but is not
   maximal supply-chain pinning.
6. **Permission scope:** the workflow-level `contents: write` grant is available
   during test and calculation steps. The current push/path/branch guards keep
   these closeout jobs on the trusted maintenance branch; a future reusable
   version should separate read-only computation from write-only archival.
7. **Scientific scope:** the B.16 workflow proves strict numerical
   reproducibility of the archived fixed-(\omega\) baseline and the
   correctness of the phase-space partitions. It does not pass the physical
   Fig. 7 gate: the calculated 10 MeV luminosity remains (+92.4284\%)
   above the plotted reference. The local-rate workflow is not a global
   escape calculation; the PR52 workflow is data-integrity verification,
   not a collider-physics rerun.

## Exact source commits

| Workflow | Reviewed workflow-file commit |
|---|---|
| B.16 local-rate package | `6c19558dc188efff2dcbc81015af9948ef36c20a` |
| PR52 scan archive integrity | `6e1a2d25b881ccb4959cc9570c663c392fdb0938` |
| B.16 escape phase space | `0b2d455104ff19c17daaac1f82e18de8ce7c9409` |

## Final disposition

All three new workflows are registered as `REVIEWED_WITH_NOTES`. Their
successful CI evidence and their write-back race limitations are explicit.
No workflow is merged into `main` by this review, and no scientific
acceptance is inferred from a green workflow alone.
