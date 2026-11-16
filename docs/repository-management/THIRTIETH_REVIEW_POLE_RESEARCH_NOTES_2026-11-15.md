# Individual review: pole, cascade and scalar-width notes

Baseline `3809b3166055e783c41f6aab4886e85bca101e3c`, 2026-11-15. Each note was read in full and checked against the associated script reruns in the prior output review. No CMS publication/efficiency revalidation, independent gauge-complete pole calculation or detector-level likelihood is claimed.

| Document under `research/major1-higgs-scalar-mixing-20261109/` | Individual outcome |
|---|---|
| `BENCHMARK_A_CMS_VECTOR_CASCADE_2026-11-10.md` | Script-reported branching and longitudinal fractions agree to stated precision, but depend on an isolated-pole estimate and spin-dependent acceptance. Added warning that the exact-momentum pole driver emitted a numerical IntegrationWarning on rerun. Experimental sensitivity/acceptance was not independently checked. REVISION_REQUIRED pending numerical convergence. |
| `EXACT_MOMENTUM_FERMION_MATCHED_POLES_2026-11-10.md` | Selected pole values reproduce the archived summary in a zero-exit rerun, but SciPy reported roundoff preventing requested integration tolerance. Added a warning; integral stability/error estimates must be checked before relying on quoted digits. Fixed diagonal widths and incomplete EFT/gauge sectors remain. REVISION_REQUIRED. |
| `PLAN_C_LITE_COMPLEX_POLE_RESIDUES_2026-11-10.md` | The separate Plan-C-lite driver exits 0 and reproduces the stated two-pole residue examples. Complex residues are correctly not treated as probabilities. Fixed diagonal widths and incomplete matching are explicit. PASS_WITH_NOTES. |
| `SINGLET_SCALAR_DIRECT_WIDTH_AUDIT_2026-11-10.md` | Direct-width script exits 0; displayed A/B threshold widths and perturbativity-ceiling ratios match to stated precision. The note retains the no-double-counting and omitted-channel limitations. PASS_WITH_NOTES. |

A successful script exit does not remove the exact-momentum integrator's warning. No physical pole result or archived numerical value was altered.


## Follow-up numerical tolerance scan (2026-11-15)

The exact-momentum pole quadrature was rerun at three requested tolerances (`2e-8`, `2e-9`, `2e-10`) for both benchmarks and all six pole pairs. Each run still emitted four `IntegrationWarning` messages. The pole mass/width shifts relative to the archived tolerance were below `1e-13 GeV` / `6e-13 GeV`, and the largest complex Higgs-residue shift was `5.81e-8`. The warning calls are in the hierarchical heavy–light Feynman-parameter pairing; the returned pole numbers are stable under this tolerance variation, but requested integration errors remain uncertified. The result, script and machine-readable output are preserved in `research/major1-higgs-scalar-mixing-20261109/POLE_QUADRATURE_TOLERANCE_AUDIT_2026-11-15.md`, `.py` and `.json`. Both the exact-momentum pole note and dependent CMS cascade note remain `REVISION_REQUIRED` until an independent integration method is compared.


## Follow-up independent numerical and provenance review (2026-11-16)

The 2026-11-15 dispositions above were correct for the evidence available at that time. The independent endpoint-quadrature audit completed on 2026-11-16 supersedes the two numerical-convergence blockers:

| Document | 2026-11-15 disposition | Current document-review disposition | What changed |
|---|---|---|---|
| BENCHMARK_A_CMS_VECTOR_CASCADE_2026-11-10.md | REVISION_REQUIRED | PASS_WITH_NOTES | The four legacy QUADPACK warnings in its pole input are independently closed for the declared fermion-sector grid. The CMS comparison remains a conditional isolated-pole theory estimate, not a vector-specific recast. |
| EXACT_MOMENTUM_FERMION_MATCHED_POLES_2026-11-10.md | REVISION_REQUIRED | PASS_WITH_NOTES | Composite Gauss-Legendre and independent mpmath tanh-sinh checks close the endpoint integration warning; all six benchmark pole pairs converge across GL orders 32–128. |
| PLAN_C_LITE_COMPLEX_POLE_RESIDUES_2026-11-10.md | PASS_WITH_NOTES | PASS_WITH_NOTES | The approximate propagator, fixed widths, candidate hard term and incomplete matching limitations remain explicit. |
| SINGLET_SCALAR_DIRECT_WIDTH_AUDIT_2026-11-10.md | PASS_WITH_NOTES | PASS_WITH_NOTES | The direct tree-level width formulas and tabulated benchmark values were independently recomputed; the result remains a partial width audit. |

The independent audit reports four legacy warning calls in the 20 TeV–muon heavy-light pairing, an endpoint scale of approximately 2.8e-11, GL64/GL96 agreement with 90-digit tanh-sinh at at most 3.54e-15, a maximum hard-remainder change of 1.37e-12 GeV^2 across orders 32–128, a maximum complex R_hh change of 7.45e-10, maximum determinant residual 6.08e-9 GeV^4, and maximum residue-sum deviation 7.56e-9. These numbers match the current machine-readable JSON and pole-output text. The numerical gate is therefore closed for the stated two benchmarks and six-pole-pair grid only.

### Provenance and reproducibility qualifications

1. The independent audit JSON embeds the correct SHA-256 of the current production pole driver, and its recorded Git blob ID matches the current JSON. However, three other SHA-256 values printed in the independent audit report (for the independent driver, human-readable pole output and regression test module) do not match the current committed file bytes. Their original values are retained as historical records; current hashes are now recorded in the checksum-reconciliation section of POLE_QUADRATURE_INDEPENDENT_AUDIT_2026-11-16.md. This is a provenance discrepancy, not a demonstrated numerical discrepancy.
2. The five regression-test methods are present. No dedicated Actions run or committed standalone unittest stdout log for this test module was found; the “five tests pass” statement is treated as a recorded local-run result, not CI acceptance. This review did not claim to rerun the tests.
3. The CMS cascade script embeds R_hh and R_hs as literal constants. The independent quadrature JSON stores R_hh but not R_hs; moreover, the script's hard-coded R_hh differs from the current Benchmark-A, m_s=125.25 GeV JSON value by 2.52e-8 in complex absolute magnitude. This is small relative to the quoted cascade precision but confirms the literal is not the current serialized output. The cascade arithmetic is reproducible conditional on the hard-coded residue ratio, but the committed machine-readable artifacts do not yet provide a complete output-to-input reconstruction of R_hs. The cascade remains PASS_WITH_NOTES, not a validated physical rate.
4. The independent-audit links in the CMS cascade, exact-momentum pole and historical tolerance-audit notes were corrected to point to the actual docs/repository-management location.

### Scientific acceptance boundary

The numerical warning is closed, but the exact-momentum result is still a fermion-sector matched diagnostic with fixed Plan-C-lite diagonal widths. It does not include the full diagonal self-energies and field counterterms, complete same-order EFT matching/counterterms, gauge/Goldstone/ghost completion, mixing-induced Standard-Model widths, or a detector-level coherent likelihood. The CMS comparison is not a spin-1 recast; the scalar direct-width table omits mixing-induced and other open channels. No gauge-independent physical pole, complete scalar width, Higgs signal strength, allowed/excluded interval, collider exclusion, or revised physical constraint is claimed.

No production amplitude, self-energy formula, pole value, width, model input, collider limit or stellar-cooling result was changed in this follow-up. Only documentation links and provenance/status records were clarified.
