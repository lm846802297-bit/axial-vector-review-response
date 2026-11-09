# Bollig--Caputo muon-density reconciliation and B.1 source audit

Date: 2026-11-09  
Benchmark: SFHo-18.8, \(t_{\rm pb}=1\) s; \(m_V=10\) MeV for the B.1/B.2 reference implementation.  
Status: **Caputo \(T(r)\) and \(\mu_\mu/T\) independently reproduce Bollig Figs. 1 and 4 at the \(10^{-4}\) relative level. Caputo's plotted \(n_\mu\) is internally consistent with its relativistic Fermi--Dirac reconstruction. However, the absolute density curve in Bollig Fig. 3 is 5--10% lower over the important outer part of the muon-rich region. The discrepancy is real at the published-curve level and is not resolved by the current public data.**

## 1. Scope and source data

The comparison uses the original published PDF vector paths, not screenshot pixel sampling:

- Bollig et al., arXiv:2005.07141v7:
  - Fig. 1: temperature \(T(r)\), yellow SFHo-18.8 curve, PDF path 0 on page index 1.
  - Fig. 3: absolute muon number density \(n_\mu(r)\), yellow SFHo-18.8 curve, path 33 on page index 2.
  - Fig. 4: degeneracy parameter \(\mu_\mu/T\), yellow SFHo-18.8 curve, path 193 on page index 2.
- Caputo et al., arXiv:2109.03244v3, Fig. 1:
  - \(T(r)\) and \(\mu_\mu(r)\) from the reconstructed SFHo-18.8 profile.
  - \(n_\mu/n_0\) from the green lower-panel curve, source PDF path 161.
  - The figure caption specifies \(n_0=0.181\ {\rm fm}^{-3}\).

PDF SHA-256 values:

- Bollig consolidated v7 PDF: 8267f8b1de184163308728c44000425ce58085c1d5bd799d0cbc1e4e8d740d61
- Caputo SNProfile.pdf: 19ca5ee492dea689a4a9851e999f7d05d0f26be7dfc820e817cc5bc310065c8e

The axis mappings use the actual PDF vector tick marks. In particular, Fig. 4 calibration does not use the text bounding boxes of tick labels, whose glyph origins are offset from the tick lines.

## 2. Temperature and degeneracy-parameter comparisons

The direct comparisons are:

| Quantity | Interval | Mean absolute relative difference | Maximum absolute relative difference |
|---|---:|---:|---:|
| Caputo \(T(r)\) vs. Bollig Fig. 1 | 5--15 km | 0.00266% | 0.00990% |
| Caputo \(T(r)\) vs. Bollig Fig. 1 | 12--15 km | 0.00331% | 0.00980% |
| Caputo \(\mu_\mu/T\) vs. Bollig Fig. 4 | 5--15 km | 0.00646% | 0.02127% |
| Caputo \(\mu_\mu/T\) vs. Bollig Fig. 4 | 12--15 km | 0.00518% | 0.01434% |

These comparisons independently support the use of the Caputo \(T(r)\) and \(\mu_\mu(r)\) reconstruction as the working thermodynamic baseline for this SFHo-18.8, 1 s benchmark.

This statement is specifically about \(T\) and \(\mu_\mu/T\). It does not certify that every other profile quantity, including the absolute muon density and neutrino chemical potentials, is identical to the raw Garching background.

## 3. Absolute-density comparison: Bollig Fig. 3 versus Caputo Fig. 1

Convert the Caputo curve according to its published normalization:

\[
n_\mu^{\rm Caputo}(r)=0.181\ {\rm fm}^{-3}
\left(\frac{n_\mu}{n_0}\right)_{\rm Caputo}(r).
\]

At the Caputo density-curve vertices in the common radial interval:

| Interval | Mean absolute relative difference | Maximum absolute relative difference |
|---|---:|---:|
| 5--15 km | 5.07% | 10.18% |
| 12--15 km | 8.80% | 10.18% |

The exact interpolated endpoint at 15.0 km gives a 10.84% difference; the maximum values in the table above are over the original digitized vertices, whose last point lies slightly inside 15 km.

Representative values, in \({\rm fm}^{-3}\):

| \(r\) (km) | Bollig Fig. 3 | Caputo Fig. 1 | Caputo / Bollig - 1 |
|---:|---:|---:|---:|
| 5 | \(4.6191\times10^{-4}\) | \(4.6954\times10^{-4}\) | +1.65% |
| 8 | \(4.6094\times10^{-3}\) | \(4.6839\times10^{-3}\) | +1.62% |
| 10 | \(4.3793\times10^{-3}\) | \(4.5149\times10^{-3}\) | +3.09% |
| 12 | \(1.8289\times10^{-3}\) | \(1.9544\times10^{-3}\) | +6.86% |
| 12.5 | \(1.3143\times10^{-3}\) | \(1.4158\times10^{-3}\) | +7.72% |
| 13 | \(8.7160\times10^{-4}\) | \(9.4449\times10^{-4}\) | +8.36% |
| 14 | \(2.7575\times10^{-4}\) | \(3.0235\times10^{-4}\) | +9.65% |
| 15 | \(3.6602\times10^{-5}\) | \(4.0570\times10^{-5}\) | +10.84% |

The residual grows systematically toward the outer edge of the muon-rich region. It is not a constant normalization offset.

## 4. Independent relativistic Fermi--Dirac density reconstruction

Using the Caputo \(T(r)\) and \(\mu_\mu(r)\), the negative-muon density is independently evaluated as

\[
n_{\mu^-}
=\frac{1}{\pi^2}\int_0^\infty dp\,
\frac{p^2}{\exp[(\sqrt{p^2+m_\mu^2}-\mu_\mu)/T]+1}.
\]

The positive-muon contribution is separately evaluated by \(\mu_\mu\to-\mu_\mu\). The integral includes the two spin states.

Comparison of the independent \(n_{\mu^-}\) integral with the Caputo plotted density gives:

| Interval | Mean absolute relative difference | Maximum absolute relative difference |
|---|---:|---:|
| 5--15 km | 0.471% | 0.538% |
| 12--15 km | 0.472% | 0.538% |

Thus Caputo's \(T,\mu_\mu\), and plotted \(n_\mu\) are internally consistent with the relativistic negative-muon Fermi--Dirac density at better than 0.6% over the tested interval.

The \(\mu^+\) density is small in the relevant shell. At 12 km it is \(1.66\times10^{-6}\ {\rm fm}^{-3}\), compared with \(n_{\mu^-}=1.944\times10^{-3}\ {\rm fm}^{-3}\); at 15 km it is negligible. Whether the plotted density is interpreted as \(n_{\mu^-}\) or the net \(n_{\mu^-}-n_{\mu^+}\) therefore cannot explain the 8--10% Bollig--Caputo difference.

## 5. What the combined comparison establishes

The independent comparisons yield a specific tension:

1. Caputo \(T(r)\) agrees with Bollig Fig. 1 to below \(0.01\%\) on the dense thermodynamic grid.
2. Caputo \(\mu_\mu/T\) agrees with Bollig Fig. 4 to below \(0.022\%\) on the dense thermodynamic grid.
3. Caputo's plotted \(n_\mu\) agrees with the Fermi density implied by its own \(T,\mu_\mu\) to below \(0.54\%\).
4. Nevertheless, Bollig Fig. 3 gives a density about 5% lower on average over 5--15 km and about 9% lower on average over 12--15 km.

At fixed Bollig Fig. 4 \(\mu_\mu/T\), inverting the relativistic Fermi integral to reproduce the Bollig Fig. 3 density would require a temperature about 1.1% below the directly digitized Bollig Fig. 1 temperature in 12--15 km. This is a diagnostic of the figure-level tension, not an adopted replacement temperature profile.

The available public plots do not determine whether the difference originates in the profile version, a thermodynamic-density convention, or a plotting/data-processing difference. The raw Garching tables used in the original simulation are not available in the repository. Therefore, no claim is made that the three published curves have been reconciled.

## 6. B.1 source definition: exact match to the published one-species convention

The Compton source in the Blinov reference implementation uses

\[
n_\mu F_{\rm deg}
=\frac{1}{\pi^2}\int_0^\infty dp\,p^2 f_{\mu^-}(1-f_{\mu^-}),
\]

with one negative-muon Fermi distribution and two spin states. This is the printed B.17 convention. It is not a sum over \(\mu^-\) and \(\mu^+\), and there is no missing extra factor of two.

The independent audit verifies:

- The reference implementation negative-muon density versus the separate relativistic Fermi integral: zero residual at the stored numerical precision.
- \(n_\mu F_{\rm deg}\) versus the independently integrated susceptibility: maximum relative residual \(2.22\times10^{-16}\).
- The direct B.16 Compton source expression versus the reference implementation: maximum relative residual \(3.33\times10^{-16}\).

The B.1 Compton source is therefore not changed. The density convention and degeneracy factor are consistent with the published formula.

### 6.1 Consequence for the weak-coupling Fig. 7 source mismatch

The weak-coupling B.16 calculation has \(P_{\rm esc}\simeq0.9979\), so its \(-8.89\%\) luminosity difference from Fig. 7 is effectively a thin-source normalization difference. The absolute-density discrepancy in Bollig Fig. 3 should not be identified directly with that source mismatch.

The reason is that the B.1 Compton factor is the product

\[
n_\mu F_{\rm deg}
=\frac{1}{\pi^2}\int dp\,p^2 f_{\mu^-}(1-f_{\mu^-}),
\]

not \(n_\mu\) by itself. When \(F_{\rm deg}\) is defined consistently from the same Fermi distribution, the product is the susceptibility integral fixed by \(T\) and \(\mu_\mu\). It is not obtained by multiplying the plotted absolute density by an independently fixed degeneracy factor. The independently checked Caputo \(T,\mu_\mu/T\) inputs therefore determine the working B.1 susceptibility; substituting the lower Bollig Fig. 3 density as a standalone normalization would break that definition.

As a scale comparison only, the B.16 Compton source is about \(32.0\%\) of the total B.1 source. Even an unjustified uniform \(8.8\%\) reduction of the entire Compton source would change the total optically thin source by only about \(2.8\%\). Moreover, the measured \(8.8\%\) density difference is an average over 12--15 km, not a demonstrated uniform correction to the full Compton source. It cannot account for the full \(8.89\%\) weak-end deficit on its own. The full 12--15 km shell contributes only \(13.72\%\) of the total B.1 source. Even the deliberately overconservative assumption that all source in this shell were Compton and that the full \(8.8\%\) density offset acted directly on it would change the total source by at most \(1.21\%\). The actual effect under a consistent B.17 susceptibility definition is not obtained by applying that density rescaling.

Therefore:

- retain the Fermi-integrated \(n_\mu F_{\rm deg}\) source;
- do not rescale the B.1 Compton source using the Bollig Fig. 3 density ratio;
- keep the weak-end source-normalization mismatch as unresolved pending a separate audit of the remaining B.1 source inputs and the Fig. 7 digitized reference.


### 6.2 Charge-conjugate convention and source-weighted size of the density tension (2026-11-10)

A fresh, independent composite-Simpson integration was run directly from the frozen profile at \(r=5,8,10,12,15\) km. It uses \(p\in[0,1000]\) MeV, 20,000 equal subintervals, \(E_\mu=\sqrt{p^2+m_\mu^2}\), and \((\hbar c)=197.3269804\) MeV fm. The reconstructed \(n_{\mu^-}\) and \(n_{\mu^-}F_{\rm deg}\) agree with the archived independent Fermi-integral values at these points to a maximum relative difference below \(8.3\times10^{-9}\).

| \(r\) (km) | \(n_{\mu^-}\) (fm\(^{-3}\)) | \(F_{\rm deg}\) | \(n_{\mu^+}/n_{\mu^-}\) |
|---:|---:|---:|---:|
| 5 | \(4.670997\times10^{-4}\) | 0.962300 | 1.242% |
| 8 | \(4.660747\times10^{-3}\) | 0.871282 | 1.033% |
| 10 | \(4.494302\times10^{-3}\) | 0.841716 | 0.284% |
| 12 | \(1.943681\times10^{-3}\) | 0.871681 | 0.0857% |
| 15 | \(4.013552\times10^{-5}\) | 0.988346 | 0.00825% |

The positive-muon fraction falls below \(0.086\%\) over 12--15 km. Consequently, interpreting the plotted quantity as net density rather than negative-muon density cannot explain the discrepancy: over 12--15 km the plotted-density comparison is 6.85--10.84%, while the Fermi-reconstructed negative-muon-density comparison is 6.32--9.63%. The charge-conjugate convention can produce a percent-level distinction only toward the inner 5--8 km region.

The channel-resolved B.1 output further sharpens the source-weighting argument. Compton accounts for \(32.0048\%\) of the total thin source, but the 12--15 km shell contains only \(3.7320\%\) of the Compton source. Thus this shell's Compton contribution is \(1.1944\%\) of the total B.1 source. Applying the mean 8.8% Fig. 3 density offset to that component alone would shift the total source by only about \(0.105\%\); even using the 10.84% endpoint offset gives about \(0.130\%\). These are density-only sensitivity estimates, not B.17-consistent replacements.

Across 5--15 km, a piecewise-linear interpolation of the digitized density residuals, weighted by the actual B.1 Compton shell fractions, gives an illustrative total-source shift of about \(0.96\%\) if \(n_\mu\) alone is replaced while \(F_{\rm deg}\) is artificially held fixed. This is not a physical prescription: B.17 requires the product \(n_\mu F_{\rm deg}\) to be evaluated from the same Fermi distribution. The estimate only quantifies why the plotted-density tension cannot account for the \(-8.885\%\) weak-endpoint B.1/B.16 luminosity deficit.

The original Fig. 3 density discrepancy therefore remains a genuine figure-level provenance tension, but neither a net-versus-negative-muon convention nor a standalone density normalization provides a justified correction to the B.1 source.

## 7. Baseline-input freeze decision

Freeze the following as the current internally consistent working inputs:

- Caputo \(T(r)\), independently checked against Bollig Fig. 1.
- Caputo \(\mu_\mu(r)\), equivalently its \(\mu_\mu/T\) profile, independently checked against Bollig Fig. 4.
- \(n_{\mu^-}(r)\) and \(F_{\rm deg}(r)\) derived from the full relativistic Fermi--Dirac distribution using the frozen \(T,\mu_\mu\).
- The B.1 Compton factor \(n_\mu F_{\rm deg}\), without an empirical rescaling.

Keep the following distinctions explicit:

- Caputo's plotted \(n_\mu\) is an internal consistency check, not a replacement for the Fermi-integrated B.1 input.
- Bollig Fig. 3 remains a source-level absolute-density cross-check with an unresolved 5--10% discrepancy; do not rescale either curve to force agreement.
- The current \(\mu_{\nu_\mu}\) and lapse inputs remain the existing reconstructed-profile baseline. The \(\mu_{\nu_\mu}\) plotting-floor test shows negligible transport sensitivity in 12--15 km, but this does not certify every raw neutrino-profile value.
- No production, opacity, transport, luminosity, or axial-vector output is changed by this audit.

## 8. Reproducibility

- Bollig PDF vector extraction: audit_bollig_muon_profile_crosscheck.py
- Independent density and B.1 source audit: audit_bollig_muon_density_and_b1_source.py
- Caputo source vector audit: audit_caputo_muon_density_vector.py
- Machine-readable output: outputs/bollig_muon_density_b1_source_audit_2026-11-09.json
- Caputo vector inventory: outputs/caputo_muon_density_vector_audit_2026-11-09.json
- Successful B.1/density audit workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42527477573
- Successful Caputo vector audit workflow: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42526643916

Both workflows preserve the production rates, transport, and published axial outputs.
