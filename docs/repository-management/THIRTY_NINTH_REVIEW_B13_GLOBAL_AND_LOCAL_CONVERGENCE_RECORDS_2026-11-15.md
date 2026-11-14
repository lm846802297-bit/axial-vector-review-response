# Individual review: B.13 global and local convergence records

Review date: 2026-11-15. Baseline branch: maintenance/repository-organization-audit-20261114. This batch reviews the next six B.13 records in register order. Saved summary JSONs, scripts and tests were inspected; no global transport scan was rerun.

| Document | Outcome | Findings and disposition |
|---|---|---|
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_GLOBAL_STAGE_A_CONVERGENCE_STATUS_2026-11-09.md | HISTORICAL | This is a 23-section cumulative Stage-A status record covering the B.13/B.16 local kernel, B.1/B.2 source-opacity transport, profile/metric limitations, and grid refinements. It correctly distinguishes numerical closure from Fig. 7 reproduction and preserves the raw-profile/GR-data limitations. Added a historical banner pointing to later PR #113 full-profile B.13/B.2 work and fixed one malformed display-equation delimiter in the optical-depth expression. |
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_GLOBAL_TRANSPORT_AUDIT_2026-11-09.md | HISTORICAL | The 10-MeV global B.13 source-plus-opacity replacement is a controlled stress test, not a paper-regime validation or an axial-vector result. Its compact summary supports a B.13 strong-endpoint Fig. 7 residual of about +131.53%; this is not an improvement over the B.16 +92.24% baseline. The full point-array blob exists by path/hash but was not returned as readable text by the file reader, so no point-by-point reparse of that large blob is claimed. Dated PR #57 Draft status was superseded by the later PR #113 record. |
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_GLOBAL_TRANSPORT_CONVERGENCE_AUDIT_2026-11-09.md | HISTORICAL | The 10-MeV scan passes the stated finest-step radial, energy, angular and path criteria. The separate 0.1-MeV companion does not: its radial 60-to-80 refinement fails, with the recorded total-luminosity and escape-probability shifts exceeding the project thresholds. Updated the heading/status so the 10-MeV pass cannot be read as an all-mass convergence claim. Later PR #113 contains subsequent full-profile B.13/B.2 work. |
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_LOCAL_KERNEL_QUADRATURE_CONVERGENCE_2026-11-09.md | PASS_WITH_NOTES | The archived local-kernel JSON reports a maximum 16-to-20 refinement change of 0.08908%, 20-to-24 change of 0.03016%, maximum final-muon shell residual \(1.63\times10^{-13}\), and mode detailed-balance residual \(1.51\times10^{-15}\), passing the explicitly adopted 0.1% local screening target at the three sampled points. The audit script and JSON exist. The note's ten moving-muon regression tests are distinct from this quadrature audit; no dedicated test_b13_local_kernel_convergence.py file was found. Updated its stale "future global calculation" sentence to point to the subsequent three-mass/global records. |
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_NONRELATIVISTIC_MUON_APPROXIMATION_DIAGNOSTIC_2026-11-09.md | PASS_WITH_NOTES | The independent script, test file, workflow and JSON exist. The output reports source-weighted mean muon speed 0.7614, RMS 0.7754, 6.84% of the weighted source below \(v=0.5\), and 28.31% above \(v=0.9\). The note correctly treats this as a distribution-moment diagnostic, not a direct B.14 rate-error estimate. Updated the old "global B.13 comparison remains future" decision because the three-mass comparison was subsequently completed; its 0.1/1-MeV curves are still baseline-grid only. |
| research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_THREE_MASS_SOURCE_OPACITY_AND_CONVERGENCE_AUDIT_2026-11-09.md | PASS_WITH_NOTES | The three compact summary JSONs for 0.1, 1 and 10 MeV exist and share the stated 1687-row vertex-preserving profile fingerprint. The source-weighted B.13/B.16 Compton-source ratios are about 0.338, 0.338 and 0.340; reduced-opacity ratios are about 0.353, 0.352 and 0.360. The B.13-consistent source-plus-opacity curves have maximum absolute Fig. 7 differences of 79.31%, 138.98% and 131.53%, respectively. The 0.1/1-MeV curves use the baseline global grid and are not independently grid-converged; 10 MeV is a stress test. The note correctly rejects empirical rescaling and any axial-constraint update. Added a top-level acceptance boundary and linked the later PR #113 refinement. |

## Cross-document interpretation

- Local-kernel convergence is strong at the sampled points, but it is not a uniform error bound over the full radius-energy domain.
- The 10-MeV global convergence pass does not transfer to 0.1 MeV; the companion 0.1-MeV radial refinement fails.
- The three-mass B.13 comparison changes both production and reduced absorption consistently. It is not equivalent to changing opacity alone and cannot be interpreted as a single global coupling rescaling.
- B.13 does not restore Fig. 7 agreement in these runs. The B.13 strong-endpoint discrepancy is larger than the B.16 baseline at 10 MeV; 0.1/1-MeV global curves remain baseline-grid diagnostics.
- PR #113 later added full-profile B.13/B.2 refinements, but the raw same-snapshot GR metric and the pure-vector Fig. 7 acceptance gate remain separate issues.

## Updated baseline register

The register remains 462 documents. After this batch:

- PASS: 2
- PASS_WITH_NOTES: 150
- HISTORICAL: 86
- REVISION_REQUIRED: 8
- PENDING: 216
- Individually reviewed: 246 / 462

No production rate, local kernel, global transport scan, opacity, coupling, axial curve, or manuscript was modified or rerun. Changes are limited to historical-status notes, scope boundaries, and one Markdown equation-delimiter repair.
