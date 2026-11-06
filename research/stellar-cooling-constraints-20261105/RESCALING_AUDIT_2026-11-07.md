# Coupling-axis rescaling audit — 2026-11-07

## Scope and motivation

The user proposed using coupling-axis rescaling to test the vector-current calculation without repeating the B.13 thermal phase-space integration. This is implemented as a post-processing audit of already archived luminosity curves.

The audit reads only:

1. blinov_reproduction/outputs/blinov_literal_scan.json;
2. blinov_reproduction/outputs/fig4_fig7_comparison.json;
3. outputs/vector_audit/luminosity_comparison.json.

It does not import or execute the thermal-rate, matrix-element, opacity, or stellar-transport routines. No B.13 integral, Compton kernel, optical-depth integral, or luminosity scan is rerun. The input files, production scripts, saved axial scan, figures, manuscript, and referee-response TeX/PDF are unchanged.

## Definition and fitting procedure

For a possible common coupling-normalization mismatch, test

\[
L_{\rm calc}(\kappa g_{\rm ref}) \simeq L_{\rm ref}(g_{\rm ref}).
\]

This is motivated by the common scaling

\[
\Gamma_{\rm prod}\propto g_X^2,\qquad
\Gamma_{\rm abs}\propto g_X^2,\qquad
\tau\propto g_X^2.
\]

A genuine coupling redefinition therefore rescales production and absorption together; it is not equivalent to multiplying the final luminosity by a constant.

The audit uses:

- \(0.90\leq\kappa\leq1.10\);
- a fixed grid spacing of \(2.5\times10^{-4}\);
- piecewise-linear interpolation in \(\log L\) versus \(\log g\);
- no extrapolation;
- a fixed set of reference points for every trial \(\kappa\);
- minimization of the RMS logarithmic residual \(\log[L_{\rm calc}(\kappa g)/L_{\rm ref}(g)]\).

Both logarithmic residuals and ordinary relative residuals are reported. The per-mass fits are diagnostic; the global fit tests whether a single common rescaling exists.

## Independent literal Blinov scalar prescription: Fig. 7

The per-mass results are:

| \(m_V\) | Baseline mean absolute relative residual | Baseline maximum | Best \(\kappa\) | Rescaled mean absolute relative residual | Rescaled maximum |
|---:|---:|---:|---:|---:|---:|
| 1 MeV | 1.60% | 5.54% | 0.9975 | 1.66% | 3.85% |
| 10 MeV | 15.64% | 91.35% | 1.06675 | 3.34% | 7.22% |
| 200 MeV | 0.71% | 1.59% | 1.00175 | 0.66% | 1.36% |

The 10 MeV pointwise Fig. 7 discrepancy is substantially reduced by a mass-specific horizontal shift. This is useful evidence that part of the difference is curve-position-like. It is not evidence for a universal coupling convention: the 1 and 200 MeV curves prefer values very close to unity, whereas the 10 MeV curve prefers a value about 6.7% higher.

A single global fit to all 69 Fig. 7 points gives

\[
\kappa_{\rm global}=1.0300.
\]

Even at this best common value, the mean absolute relative residual is about 6.25% and the maximum is about 47.5%. The high-coupling tail of the 10 MeV curve remains the dominant failure. Thus no single near-unity rescaling reconciles all three masses.

## Independent Fig. 4 contour-boundary cross-check

The original, unrescaled literal scan already reproduces the digitized Fig. 4 lower and upper crossings at the four available masses to within 2.60%:

| \(m_V\) | Lower-bound difference | Upper-bound difference |
|---:|---:|---:|
| 1 MeV | +0.81% | -0.86% |
| 10 MeV | +0.33% | +0.97% |
| 100 MeV | -0.89% | +0.98% |
| 200 MeV | -1.31% | +2.60% |

The 10 MeV Fig. 7 best-fit value, \(\kappa=1.06675\), moves both Fig. 4 boundaries away from the reference:

| \(m_V\) | Unscaled lower / upper difference | After mass-specific Fig. 7 rescaling |
|---:|---:|---:|
| 1 MeV | +0.81% / -0.86% | +1.07% / -0.59% |
| 10 MeV | +0.33% / +0.97% | -5.94% / -5.34% |
| 200 MeV | -1.31% / +2.60% | -1.49% / +2.42% |

At 100 MeV no Fig. 7 pointwise reference curve is available, so no mass-specific fit is quoted. Applying the global \(\kappa=1.03\) as a diagnostic would shift its lower/upper boundary differences to approximately -3.78% / -1.96%.

This is the decisive cross-check: the 10 MeV Fig. 4 boundaries were already close before rescaling, while the rescaling inferred from Fig. 7 makes them roughly 5–6% too low. The Fig. 7 discrepancy is therefore not consistently described as a single horizontal coupling-normalization error. The luminosity-curve shape and/or the ingredients entering the trapping tail must also matter.

## Existing mode-resolved vector control: separate diagnostic

The archived exact_modes curve from outputs/vector_audit/luminosity_comparison.json was also passed through the same near-unity rescaling procedure. Its best fits land on the edge of the search interval, and the remaining pointwise residuals are very large.

This is not a like-for-like reproduction test of the scalar Appendix-B prescription: the mode-resolved calculation uses polarization-dependent Compton kernels and mode-resolved attenuation, whereas the literal reference uses the paper's scalar summed-opacity prescription. The failed rescaling is therefore recorded as a diagnostic, not as a stand-alone proof of an error in the mode-resolved production solver. A physical comparison still requires matching one ingredient at a time.

## Decision

1. Do not apply any fitted kappa to the production vector scan, axial scan, or constraint figures.
2. Do not change the Compton normalization, the factor of 2, the factor of 3, or the positive/negative charge convention based on this fit.
3. Retain the original Fig. 4 and Fig. 7 comparison results; the rescaling audit is an additional diagnostic, not a replacement.
4. Keep PR #56 Open / Draft. The vector control is not declared validated.
5. Use the result to narrow the next investigation: explain the 10 MeV Fig. 7 curve-shape/trapping-tail discrepancy while preserving the already-close Fig. 4 contour boundaries. Prefer targeted comparisons of archived source and opacity components over repeating the full B.13 integration.

## Reproducibility

Implementation and tests: rescaling_audit/README.md.

The generated machine-readable report is rescaling_audit/outputs/rescaling_audit.json. It records SHA-256 hashes for the three input JSON files and the audit script. The dedicated GitHub Actions workflow runs only this post-processing audit; it does not invoke the existing full numerical scan workflow.
