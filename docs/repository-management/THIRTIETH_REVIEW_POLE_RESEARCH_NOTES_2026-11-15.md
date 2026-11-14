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
