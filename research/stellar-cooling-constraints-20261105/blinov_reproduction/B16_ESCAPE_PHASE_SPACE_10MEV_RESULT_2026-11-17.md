# B.16 10 MeV escape phase-space audit — 2026-11-17

## Status

**PASS for the B.16 phase-space decomposition against the archived high-order vector baseline.**

This result closes the current-main energy-grid identity, global baseline closure, joint radius–energy–direction normalization, and all checked one-dimensional marginals. It does **not** reproduce the published Fig. 7 10 MeV strong-absorption tail; that separate discrepancy remains open.

## Reproducibility configuration

| Quantity | Value |
|---|---:|
| Vector mass \(m_{A'}\) | 10 MeV |
| Coupling at the checked Fig. 7 endpoint | \(4.171689650228597\times10^{-8}\) |
| Source radial order / nodes | 200 / 200 |
| Opacity radial order / nodes | 640 / 642 |
| Energy order / nodes | 200 / 842 |
| Angular order | 32 |
| Chord/path order | 64 |
| Path energy convention | Fixed \(\omega\) along the full Eq. (B.2) chord |
| Python / NumPy / SciPy | 3.12.16 / 2.5.4 / 1.18.1 |

The calculation uses the reconstructed public-figure SFHo-18.8 profile already archived in the repository. It is not the original Garching simulation table.

## Grid identity

The phase-space calculation reproduces all archived high-order grid fingerprints exactly:

| Grid | Nodes | SHA-256 |
|---|---:|---|
| Source radial grid | 200 | \`1a007702d1f7c8b81200e648a763f7f1a0e3565a39d57c8174dada5aad1a4cb5\` |
| Opacity radial grid | 642 | \`6701fc3fe06bf07879612e591ae62c494f673928bc18f169d4b6f3fabed7d378\` |
| Energy grid | 842 | \`036e6d772f43acf97601c3846b475e8e1c14200d4d82de1dd9af30f01bb87ea3\` |

Profile SHA-256:
\`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.

The historical failed-run energy hash \`db6f613c...\` was not reproduced from the current main inputs. The independent grid diagnostic and the production phase-space run both reproduce the archived \`036e6d77...\` fingerprint. No baseline hash was changed.

## Global luminosity and baseline closure

| Quantity | Calculated | Archived baseline / Fig. 7 reference |
|---|---:|---:|
| Optically thin luminosity | \(7.502476933641651\times10^{55}\) erg/s | Same baseline |
| Escaping vector luminosity | \(2.439635957361032\times10^{52}\) erg/s | \(1.26781475907372\times10^{52}\) erg/s (Fig. 7 digitization) |
| Global source-weighted escape probability | \(3.251774019352985\times10^{-4}\) | Same baseline |

Baseline closure residuals:

- Luminosity: \(-2.220446049250313\times10^{-16}\).
- Optically thin luminosity: \(0\).
- Escape probability: \(-5.421010862427522\times10^{-20}\).

The calculated luminosity is **92.4284% above the digitized Fig. 7 reference** at this endpoint. This is the previously identified 10 MeV strong-absorption discrepancy. Matching the archived numerical baseline is not evidence that Fig. 7 itself has been reproduced.

## Regional decomposition

| Region | Fraction of global thin source | Fraction of global escaped luminosity | Source-weighted escape probability | Non-empty joint cells |
|---|---:|---:|---:|---:|
| All emission radii | 1.000000 | 1.000000 | \(3.25177\times10^{-4}\) | 508 |
| Dominant 8–15 km emission | 0.796522 | 0.868551 | \(3.54583\times10^{-4}\) | 152 |

The 8–15 km source fraction is 79.6522%, within the previously specified 75–85% validation interval.

## Joint-table and marginal closure

The full radius–energy–direction table is normalized separately for:

1. all emission radii;
2. the dominant 8–15 km emission region.

Both thin-source and escaped-luminosity fractions close to unity in each region. Reconstructed one-dimensional marginals agree with their stored partitions with a maximum absolute residual of

\[
6.661338147750939\times10^{-16}.
\]

The 8–15 km energy partition contains a \(10\text{–}11\) MeV bin with exactly zero source and escaped weight. The sparse joint table intentionally omits empty cells. The validator therefore treats an omitted bin as zero only when its stored one-dimensional marginal is exactly zero; a missing non-zero bin or an unexpected joint-table label remains a hard failure.

Regression tests cover this behavior. No phase-space cell or physical contribution was rescaled, filled, or discarded to force closure.

## Validation record

- [Energy-grid identity workflow](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44054718118) — passed.
- [Strict phase-space reproduction workflow](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44059347513) — passed.
- The production result JSON is archived beside this report as \`outputs/b16_escape_phase_space_10mev_2026-11-17.json\`.
- The axial-vector production files and constraint outputs were verified unchanged.

## Scope and remaining work

This closes the current-main B.16 escape phase-space decomposition against its archived vector baseline. It does not close:

- the Fig. 7 10 MeV strong-absorption discrepancy;
- the independent muon-density definition audit;
- the 12–15 km profile provenance and dual-density comparison;
- the remaining collider, UV-order, or two-VEV convergence checks.

No axial-vector limit curve is updated by this audit.
