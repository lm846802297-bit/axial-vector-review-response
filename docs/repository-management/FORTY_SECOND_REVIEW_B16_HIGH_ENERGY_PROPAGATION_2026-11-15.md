# Individual review: six B.16 high-energy propagation and GR records

Review date: 2026-11-15. Baseline branch: \`maintenance/repository-organization-audit-20261114\`. Six B.16 records were read in full and cross-checked against their Python source, test modules, archived JSON, and historical GitHub Actions logs. This is an implementation/provenance review, not a new full transport calculation.

## 1. Document-by-document outcomes

| Document | Outcome | Findings and disposition |
|---|---|---|
| \`B16_GR_ENERGY_AND_RAY_PROPAGATION_REQUIREMENTS_2026-11-09.md\` | \`PASS_WITH_NOTES\` | The distinction between the paper's flat pseudo-Newtonian Euclidean-chord prescription and a full-GR extension is correct. The generic static-spherical ray kernel has seven passing tests, but it is not applied to a fabricated SFHo metric. Corrected older wording that left the displayed B.2 energy convention ambiguous: the printed integrand uses fixed \(\omega\); only the unpublished implementation's actual coding choice remains unknowable. |
| \`B16_HIGH_ENERGY_CHANNEL_KERNEL_AUDIT_2026-11-10.md\` | \`PASS_WITH_NOTES\` | Corrected the Fermi-pair equation reference from B.25 to B.9. Found and fixed a sign error in the Python direct-angular helper: it had evaluated \((1-f_1)(1-f_2)\) rather than \(f_1f_2\). Four new pinned regression tests pass. The archived full channel result is still V8-only; the complete Python calculation has not yet produced a separate NumPy JSON. |
| \`B16_HIGH_ENERGY_NU_CHORD_CONVERGENCE_2026-11-10.md\` | \`PASS_WITH_NOTES\` | Corrected the pair-average equation reference to B.9. The V8 refinement values are internally consistent, but the referenced Python script was not executed, no dedicated test covers the 36-ray scan, and the V8 JSON has no Python script hash. The document now states these limits and does not claim strict NumPy reproduction. |
| \`B16_HIGH_ENERGY_OUTER_TEMPERATURE_SENSITIVITY_2026-11-10.md\` | \`REVISION_REQUIRED\` | The archived result is a V8-only frozen-source, high-energy transport sensitivity. No matching Python source or script hash exists in the repository. Existing Python all-energy temperature scripts recompute B.1+B.2 and are not equivalent to this \(210\text{--}510\) MeV fixed-source calculation. A matching NumPy implementation and output are still required. |
| \`B16_HIGH_ENERGY_PATH_REDSHIFT_AUDIT_2026-11-10.md\` | \`REVISION_REQUIRED\` | The global \(210\text{--}510\) MeV fixed-\(\omega\)/path-redshift comparison is V8-only. The repository Python script \`audit_b16_high_energy_nu_energy_convention.py\` is a selected-ray diagnostic, not the global energy-integrated calculation. The two must not be presented as matching implementations. The document now records the missing global NumPy run. |
| \`B16_INDEPENDENT_ANALYTIC_PATH_INTEGRATION_AUDIT_2026-11-09.md\` | \`PASS_WITH_NOTES\` | This is the one full independent B.2 path result in this six-document set with a Python run, source commit, and script SHA. Same-grid reproduction is \(1.11\times10^{-16}\) maximum relative difference; adaptive QUADPACK/Simpson comparison is \(1.15\times10^{-6}\) maximum. Its historical workflow installed unpinned NumPy/SciPy, so the environment is not locked. The new pinned lane reruns its unit tests, not the full integration. |

## 2. Source and test inspection

### Fermi-pair angular average

The paper's production kernel uses the two neutrino occupation factors \(f(E_1,\mu)f(E_2,-\mu)\); the blocking complements belong to the absorption integral. In \`audit_b16_channel_resolved_energy.py\`, the original \`expit\` arguments had the wrong signs. The corrected helper is
\[
\operatorname{expit}\!\left(\frac{\mu-E_1}{T}\right)
\operatorname{expit}\!\left(\frac{-\mu-E_2}{T}\right).
\]

The separate \`audit_b16_neutrino_b7_b9_kernel.py\` implementation uses a stable logistic function \(1/(1+e^x)\) with \(x=(E-\mu)/T\), which has the correct occupancy sign. The new regression module compares both direct angular implementations with the repository analytic average and the published Eq. (B.9) closed form.

### Propagation and GR

- \`audit_b16_high_energy_nu_chord_convergence.py\` exists, but the archived high-energy chord JSON is from V8 and the Python script has not been executed.
- \`audit_b16_high_energy_nu_energy_convention.py\` evaluates selected local rays; it does not generate the global \(210\text{--}510\) MeV luminosity comparison in the path-redshift document.
- No matching Python script was found for the frozen-source high-energy outer-temperature V8 diagnostic.
- \`audit_b16_path_independent.py\` is tied to the archived Python output by \`run_commit_sha\` and \`code_sha256\`. Its test module has five tests.
- \`gr_ray_transport.py\` is a generic geometry solver. Seven tests cover flat chords, redshift, toy Schwarzschild radial propagation, and finite-boundary/turning-point semantics. They do not supply the missing same-snapshot \(A(r)\) or \(M(r)\) profile.

## 3. Historical numerical evidence (kept separate by runtime)

| Diagnostic | Archived result | Runtime qualification |
|---|---:|---|
| B.9 direct angular average | Maximum residuals \(2.89\times10^{-15}\) to \(3.11\times10^{-15}\) across the archived orders | V8 cross-runtime JSON; not a NumPy result |
| High-energy neutrino chord | Path 32→64: \(1.987\times10^{-5}\); path 128→256: \(2.822\times10^{-6}\); opacity 640→1280: \(9.350\times10^{-7}\) | V8 cross-runtime JSON; Python script not run |
| Outer \(T(22\text{--}25\,\mathrm{km})\) stress | \(-30\%\) to \(+30\%\) changes high-energy escaped luminosity by \(-0.385\%\) to \(+0.387\%\) | V8-only; no matching Python source |
| High-energy path-redshift | \(210\text{--}510\) MeV escaped luminosity changes by \(-28.09\%\) | V8-only global band; targeted-ray Python script is a different calculation |
| Independent analytic B.2 path | Same-grid maximum residual \(1.11\times10^{-16}\); adaptive quadrature maximum residual \(1.15\times10^{-6}\) | Strict Python execution, but historical dependencies were unpinned |

The global all-energy redshift-only result, which moves the 10 MeV strong-endpoint residual from about \(+92.24\%\) to \(+36.74\%\), is a separate output and is not averaged with the high-energy-band \(-28.09\%\) result.

## 4. New pinned regression lane

Added \`requirements-b16-audit.txt\` and \`.github/workflows/b16-high-energy-kernel-regression.yml\` with Python 3.12.14, NumPy 2.5.4, and SciPy 1.18.1 pinned. Run [#43646106550](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43646106550) passed:

- new Fermi-pair tests: 4/4;
- B.6/B.10/B.4 neutrino-kernel tests: 4/4;
- independent analytic B.2 path tests: 5/5;
- generic GR ray tests: 7/7.

Total: **20/20 tests**.

This is a pinned regression lane. It does not run the full channel-resolved, 36-ray chord, outer-temperature, or global path-redshift calculations and does not claim a strict NumPy reproduction of their V8 JSONs.

## 5. Remaining reproducibility gates

1. Run \`audit_b16_channel_resolved_energy.py\` in NumPy and archive a separate JSON with script hash, commit SHA, profile hash, and dependency versions.
2. Run the Python chord-convergence script with the same 36 rays and grids as the V8 record; add explicit tests and predeclared acceptance tolerances.
3. Implement the frozen-source \(210\text{--}510\) MeV outer-temperature transport sensitivity in Python; do not substitute the existing self-consistent all-energy stress tests.
4. Implement the global energy-integrated \(210\text{--}510\) MeV path-redshift comparison in Python; do not substitute the targeted-ray script.
5. Rerun the full independent analytic B.2 integration under the pinned environment if a dependency-locked full output is required.
6. Keep the generic GR kernel separate from a physical full-GR SN result until same-snapshot \(N(r)\) and \(A(r)\) or \(M(r)\) data are available.

## 6. Physical disposition

The printed Eq. (B.2) uses fixed \(\omega\) along the Euclidean chord. The path-redshift branch is a separate counterfactual sensitivity and is not full GR. The missing \(A(r)\) or \(M(r)\) profile blocks a full-GR extension, not reproduction of the paper's stated flat-spatial-coordinate approximation.

No source, opacity, coupling, energy cutoff, production axial-vector output, or constraint curve is modified. The \(+92\%\) Fig. 7 strong-endpoint discrepancy remains unresolved; no rescaling or fitted correction is authorized.

## 7. Baseline register

The 462-document baseline register now records **264 individually reviewed** and **198 pending**. Outcome totals: 2 PASS, 162 PASS_WITH_NOTES, 89 HISTORICAL, 11 REVISION_REQUIRED, and 198 PENDING.
