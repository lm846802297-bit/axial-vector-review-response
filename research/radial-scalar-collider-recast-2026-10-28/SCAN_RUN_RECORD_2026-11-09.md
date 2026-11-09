# Regenerated Belle II radial-scalar width scan — 2026-11-09

**PR:** #68  
**Workflow:** https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42560249275  
**Source commit:** 4e90cd971e5cd3264294958f261bd9ce05825e01  
**Archive commit:** 9ae7955f6b2a6d3f8112b1f3772889bb54f58a56  
**Status:** scan and unit tests passed; output archived

## 1. Frozen run configuration

| Parameter | Value |
|---|---:|
| Scalar mass grid | 0.212--10 GeV, 48 points |
| \(A'\) mass grid | 0.001--100 GeV, 48 points |
| Gauge coupling grid | \(10^{-6}\)--0.1, 32 points |
| Total points | 73,728 |
| \(\theta_{\mu R}\) | \(10^{-2}\) |
| \(\theta_{\tau R}\) | \(10^{-2}\) |
| Three-body quadrature | 192 |
| Four-body quadrature | 128 |
| Python | 3.13.18 |
| NumPy | 2.3.5 |

This is the historical PR #52 collider benchmark: negligible Higgs-portal mixing as an explicit assumption, decoupled VLLs in the scalar-width calculation, and both right-handed angles fixed to \(10^{-2}\). It is a self-contained benchmark for this collider study; it is not obtained by importing a Higgs--scalar mixing or complex-pole result.

## 2. Test result

**58 tests passed; 0 failures.**

The suite covers radial-scalar widths, three-body cascades, double-virtual four-body bounds, promptness diagnostics, the finite-width kernel, benchmark mapping, and scan classification. The exact test output is archived in the derived scan directory.

## 3. Grid and width-regime counts

| Diagnostic | Count |
|---|---:|
| Total points | 73,728 |
| \(\lambda_S\leq4\pi\) | 68,351 |
| Scalar Yukawas \(|y_{s\ell\ell}|^2\leq4\pi\) | 67,344 |
| Both scalar-quartic and scalar-Yukawa criteria | 66,617 |
| Exact primary-width points under the declared benchmark | 46,336 |
| Points with nontrivial branching-fraction intervals | 27,392 |
| On-shell \(A'A'\) | 42,240 |
| One-on-shell/one-virtual three-body | 4,096 |
| Double-virtual four-body bounded regime | 27,392 |

The three kinematic regimes sum to 73,728. The historical summary key points_with_bounded_branching_fractions=73728 counts all rows with a valid interval, including degenerate intervals in exact regions. It is not the count of points with nonzero interval width.

## 4. Width and exchange diagnostics

| Quantity | Result |
|---|---:|
| Maximum identical-pair exchange Cauchy upper bound / direct widths | \(1.849013677\times10^{-6}\) |
| Maximum \(\Gamma_s/m_s\), all points | \(4.391025\times10^4\) |
| Maximum \(\Gamma_s/m_s\), \(\lambda_S\leq4\pi\) subset | 0.293776 |
| Maximum \(\Gamma_s/m_s\), combined \(\lambda_S\) plus scalar-Yukawa subset | 0.293407 |
| Combined-subset points with \(\Gamma_s/m_s>1\) | 0 |
| Maximum \(y_{s\tau\tau}\), all points | 355.372 |
| Maximum \(y_{s\tau\tau}\), \(\lambda_S\leq4\pi\) subset | 39.196 |

The all-grid maximum \(\Gamma_s/m_s\) is dominated by points that fail scalar-sector perturbativity criteria. The \(\lambda_S\leq4\pi\) condition alone is insufficient: some such points have nonperturbative scalar Yukawa couplings. The combined subset imposes both criteria, but does not include every VLL/portal perturbativity condition of the full UV theory.

The double-virtual four-body contribution is evaluated in the diagonal-pairing spectral treatment. Identical-flavour exchange is bounded with a Cauchy--Schwarz upper bound rather than explicitly integrated. The branching-fraction intervals preserve that limitation.

## 5. Archived outputs and hashes

Directory: data/derived/scan-pr52-thetaR-1e-2/

- original_uv_width_scan.csv.gz — compressed 73,728-row CSV.
- original_uv_width_scan_summary.json — scan configuration and diagnostics.
- SHA256SUMS.txt — hashes of the uncompressed CSV and JSON summary.
- source-sha256.txt — source-code and test hashes.
- source-commit.txt — exact source commit.
- python-version.txt and numerical-dependencies.txt — environment.
- unit-tests.txt — complete 58-test output.

SHA-256:
- Uncompressed CSV: 67ec36a50c65b9c03de9e63c83039feb965f12335dbd3984be92d4ab214ca783
- Summary JSON: 98e507bbc00e8966b71722238d5326ab9802f6dd12f03cd6de42fcb322671664

## 6. Interpretation boundary

This is a successful regeneration of the declared PR #52 collider benchmark, not a model-specific Belle II detector-level recast. It does not supply the real mass-dependent Crystal Ball response, production-times-efficiency arrays, lifetime-dependent detector efficiency, or detector-level likelihood. No global allowed scalar-mass interval is claimed.

Any alternate VLL-angle or portal benchmark must be defined and evaluated as a separate collider benchmark. It is not a prerequisite for, or an input imported from, the independent Higgs--scalar mixing research workstream.
