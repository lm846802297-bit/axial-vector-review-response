# Individual review: independent B.1 source and full B.1+B.2 luminosity

Review date: 2026-11-15. Baseline branch: `maintenance/repository-organization-audit-20261114`. This review covers the independent optically-thin B.1 source audit, the full end-to-end B.1+B.2 luminosity audit, their Python implementations/tests, the pinned workflows, and the archived machine-readable outputs. It is an implementation and numerical-provenance review; it does not claim an independent derivation of the shared local collision kernels or a full-GR supernova calculation.

## 1. Document-by-document outcomes

| Document | Outcome | Findings and disposition |
|---|---|---|
| `B16_INDEPENDENT_B1_THIN_SOURCE_AUDIT_2026-11-09.md` | `PASS_WITH_NOTES` | Read the full audit, script, tests, old output and pinned output. The independent source calculation avoids the legacy B.1 energy weights and radial rule, evaluates production kernels at new log-energy quadrature nodes, and inserts the exact radius-dependent lower limit \(m_V/N(r)\). The pinned 400-node result is \(4.30436817\times10^{70}\) erg/s per \(g^2\), \(-0.443024\%\) relative to archived B.16. Matched 40-node radial comparison isolates \(-0.575495\%\) from the archived energy-grid integration. Six tests and pinned provenance/convergence/Jacobian checks pass. Escape factor is set to one; local kernels and muon-density convention are shared. |
| `B16_FULL_INDEPENDENT_B1B2_LUMINOSITY_AUDIT_2026-11-09.md` | `PASS_WITH_NOTES` | Read the full end-to-end audit, source, tests, old output and pinned output. The pinned 200-node/320-energy-node/16-angle calculation uses independent B.1 source quadrature and analytic piecewise-linear B.2 chords. It reproduces archived B.16 to \(0.445059\%\) maximum and \(0.397526\%\) mean absolute relative difference over all 25 couplings. The Fig. 7 residual remains \(-9.2908\%\) at weak coupling and \(+92.0542\%\) at strong absorption. Four tests and all pinned input-SHA/source-closure checks pass. |

## 2. B.1 source audit: numerical evidence

Pinned run: [#43650570961](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43650570961). Runtime: Python 3.12.14 / NumPy 2.5.4 / SciPy 1.18.1.

- Six quadrature/Jacobian tests pass.
- Radial convergence from 200 to 400 nodes is \(2.1411\times10^{-5}\) relative.
- Energy-panel sequence 80/120/180/240 is identical to stored precision.
- The 1000-to-4000 MeV cutoff difference is \(2.5746\times10^{-9}\).
- Local-energy and \(E_\infty\) formulations agree to \(2.22\times10^{-16}\) in the total source.
- The dimuon inverse-decay channel is exactly closed at \(m_V=10\) MeV.

The same-40-node comparison is important: it keeps the archived radial nodes/weights fixed while replacing the archived energy-grid interpolation with direct energy quadrature. It therefore isolates the \(-0.575495\%\) energy-integration residual. Refining the radial integral to 400 nodes shifts the source upward by about \(0.1332\%\), leaving the net \(-0.443024\%\) difference against archived B.16.

## 3. Full B.1+B.2 audit: numerical evidence

Pinned run: [#43651020195](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43651020195). Runtime: Python 3.12.14 / NumPy 2.5.4 / SciPy 1.18.1.

The workflow explicitly consumes the separately pinned B.1 and B.2 outputs and verifies their file SHA-256 values, run commits, shared profile SHA, archived B.16 baseline SHA, and Fig. 7 digitization SHA. Four angular escape-factor tests pass. The 100-to-200-source-node refinement changes the full curve by at most \(0.19867\%\).

| Metric | vs archived B.16 | vs digitized Fig. 7 |
|---|---:|---:|
| Mean absolute relative difference | 0.397526% | 15.88556% |
| Maximum absolute relative difference | 0.445059% | 92.05416% |
| Weak endpoint | -0.445059% | -9.290812% |
| Reference peak | -0.406173% | +2.152171% |
| Strong-absorption endpoint | -0.096994% | +92.05416% |

The final 200-node thin source is \(4.3042760061\times10^{70}\) erg/s per \(g^2\), within \(2.14115\times10^{-5}\) relative of the separately pinned 400-node B.1 source. The independent full curve is therefore numerically consistent with the archived B.16 implementation, but both retain the large strong-endpoint mismatch with Fig. 7.

## 4. Workflow and provenance review

Both new workflows were statically reviewed and executed successfully.

### B.1 source workflow

- Workflow: `.github/workflows/b16-b1-independent-source-pinned.yml`
- Run: [#43650570961](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43650570961)
- Six tests, full source integration, provenance, radial/energy/tail convergence, Jacobian closure and production-output invariance passed.

### Full B.1+B.2 workflow

- Workflow: `.github/workflows/b16-full-b1b2-independent-pinned.yml`
- Run: [#43651020195](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43651020195)
- Four tests, pinned B.1/B.2 input SHA checks, 25-point full curve, source closure and production-output invariance passed.

Both workflows pin Python 3.12.14 / NumPy 2.5.4 / SciPy 1.18.1, use GitHub-hosted runners, require the reviewed maintenance branch, and restrict write-back to the corresponding generated JSON output. Neither uses repository secrets or modifies production axial-vector source/constraint outputs.

## 5. Scientific boundary and next steps

### Pinned source-versus-escape decomposition

The updated [source-versus-escape diagnostic](../../research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_FIG7_SOURCE_VS_ESCAPE_DIAGNOSTIC_2026-11-08.md) derives the required escape probability from the pinned 25-point B.1+B.2 output. At the weak endpoint, \(P_{\rm esc}^{\rm req}=1.10008>1\), so the weak-end deficit cannot be fixed by increasing absorption. The required and calculated escape probabilities cross between \(g=9.42\times10^{-9}\) and \(1.13\times10^{-8}\). At the strong endpoint, \(P_{\rm esc}^{\rm req}/P_{\rm esc}^{\rm calc}=0.52069\), corresponding to an averaged effective exponent difference \(+0.65261\). A global source rescaling that repairs the weak end worsens the strong end; a global opacity reduction that repairs the strong end worsens the weak end. This is a diagnostic decomposition, not a fitted correction.


Established within the stated scope:
1. The independent B.1 optically-thin source quadrature is numerically converged and closes with the local-energy/\(E_\infty\) Jacobian.
2. The independent B.2 analytic chord implementation is numerically reproduced separately.
3. Their full combination reproduces archived B.16 to better than \(0.45\%\) over all 25 couplings.
4. The order-one Fig. 7 strong-endpoint discrepancy persists after the independent B.1+B.2 recomputation.

Not established:
1. The reconstructed public-figure profile is not the original Garching s18.8-SFHo-MUONS raw snapshot. A fresh 2026-11-15 check of the official archive confirms that both the Bollig2016 radial-neutrino and hydro-profile endpoints return HTTP 401; only authorized archive access or an explicitly authorized transfer can close this provenance gap. See [profile availability audit](../../research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_PUBLIC_PROFILE_AND_METRIC_SOURCE_AVAILABILITY_AUDIT_2026-11-09.md).
2. The local production and absorption kernels are shared with the Appendix-B reference implementation; they have not all been independently re-derived in this end-to-end calculation.
3. The negative-muon density/species convention is shared.
4. The fixed-\(\omega\) Appendix-B prescription versus the main-text energy-at-infinity language remains a physical convention question.
5. The Euclidean straight-chord calculation is not full-GR ray tracing; same-snapshot \(A(r)\) or \(M(r)\) data remain necessary for that extension.

The next research stage should target these shared physical inputs and conventions, beginning with a controlled comparison of the reconstructed stellar profile against independent SFHo-18.8 literature snapshots and a separate derivation audit of the local production/absorption kernels. Do not expand quadrature grids without a demonstrated convergence need, and do not fit an opacity, source or luminosity rescaling to Fig. 7.

## 6. Register status

The 462-document baseline register now contains 282 individually reviewed and 180 pending (183 PASS_WITH_NOTES, 2 PASS, 9 REVISION_REQUIRED, 88 HISTORICAL). The separate workflow register contains 115 YAML workflows: 40 individually reviewed, 16 historical candidates and 59 pending. This review report and its workflow-review records are supplementary and do not increase the 462-document baseline.


## Current-tree and pinned-output reconciliation (2026-11-16)

Both source reports in §1 remain present and retain their `PASS_WITH_NOTES` baseline dispositions. The current pinned B.1 JSON is present at blob `1bfe090d8c0dd1987f6d8c999dec08424f0ec0cb`; its 400-node source is (4.3043681689\times10^{70}) erg s(^{-1}) per (g^2), the 200-to-400-node shift is (2.14115\times10^{-5}), the 1000-to-4000 MeV tail shift is (2.57464\times10^{-9}), and the 10 MeV dimuon channel is exactly zero. The pinned full B.1+B.2 JSON is present at blob `f6a61a337474167fa0819f5435eb595e10df7ea5); its maximum difference from archived B.16 is (0.445059\%), while the strong-end Fig. 7 residual remains (+92.0542\%). The two JSON `run_commit_sha` values match the head SHAs of Actions runs #43650570961 and #43651020195; both runs were independently fetched and completed successfully. The source and end-to-end regression modules contain six and four tests, respectively.

The calculation remains independent in the B.1 source quadrature and B.2 path integration, not in the shared local collision-kernel derivation. It uses the reconstructed 1687-row profile, not the original Garching raw simulation table, and the fixed-(\omega) Euclidean-chord prescription, not full-GR transport. No opacity/source rescaling or axial-vector production output is inferred.
