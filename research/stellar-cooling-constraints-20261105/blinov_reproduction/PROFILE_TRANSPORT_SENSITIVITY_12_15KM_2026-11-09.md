# Full B.1+B.2 transport sensitivity to the 12--15 km uncertainty and 8--15 km source region

Date: 2026-11-09  
Benchmark: \(m_V=10\) MeV, \(g=4.17168965\times10^{-8}\), \(R_{\max}=25\) km.  
Numerics: radial order 40, energy order 100, angular order 32; fixed \(\omega\) along B.2 paths.  
Status: **the \(\mu_{\nu_\mu}\) plotting-floor assumptions have negligible impact on the strong-endpoint escape probability. The alternative \(\mu_\mu\) digitization produces a visible but insufficient change; it remains a diagnostic-only input pending source-definition confirmation.**

## 1. Calculation design

The calculation reuses the existing pure-vector B.1 source, local production/absorption kernels, channel decomposition, and analytic B.2 ray-shell integration. The same radial, energy, angular, and path conventions are used for all profile variants.

Only one profile input is changed in each variant:

- Baseline: Caputo \(T,\mu_\mu,\mu_{\nu_\mu}\), with the existing Ferreira lapse.
- A: set \(\mu_{\nu_\mu}=0\) over 12--15 km.
- B: replace only \(\mu_\mu\) over 12--15 km with the alternative Ferreira digitization. This is a diagnostic substitution, not an adopted physical profile.
- C: in the unresolved interval 13.109927--15 km, set \(\mu_{\nu_\mu}=-1\) MeV, using the magnitude of the logarithmic plot's resolution floor. This is a stress-test envelope, not a reconstructed continuation.

The B.1 source and B.2 opacity are both recalculated for each variant. In addition, the escape probability is recomputed with the **baseline B.1 source held fixed**, isolating the opacity/transport response from any source-normalization change.

No empirical rescaling is applied. No axial-vector output is generated.

## 2. Strong-endpoint baseline

The baseline full B.1+B.2 calculation gives:

\[
P_{\rm esc}^{\rm base}=3.23935379\times10^{-4}.
\]

The source-weighted mean optical-depth coefficient in the 12--15 km path shell is:

\[
\left\langle\frac{\tau_{12-15}}{g^2}\right\rangle_{\rm source}
=1.34833765\times10^{15}.
\]

Its channel decomposition is:

| Channel | \(\langle\tau_{12-15}/g^2\rangle\) |
|---|---:|
| \(\nu_\mu\) inverse decay | \(6.26118509\times10^{14}\) |
| \(\nu_\tau\) inverse decay | \(6.26475877\times10^{14}\) |
| Compton | \(9.57432659\times10^{13}\) |
| Dimuon | 0 |

The dimuon channel is closed for \(m_V=10\) MeV.

## 3. Full transport results

| Variant | B.1 thin-source ratio | Escape ratio, own source | Escape ratio, fixed baseline source | Escaped B.1 integral ratio |
|---|---:|---:|---:|---:|
| A: \(\mu_{\nu_\mu}=0\) in 12--15 km | 1.0000548 | 0.9998914 | 0.9999339 | 0.9999462 |
| B: diagnostic Ferreira \(\mu_\mu\), 12--15 km | 1.0064587 | 0.9329868 | 0.9329672 | 0.9390127 |
| B2: diagnostic Ferreira \(\mu_\mu\), 8--15 km | 1.2709188 | 0.6608578 | 0.6197762 | 0.8398966 |
| C: unresolved \(|\mu_{\nu_\mu}|=1\) MeV envelope | 0.9999912 | 1.0000262 | 1.0000179 | 1.0000174 |

The ratios are relative to the baseline at the same \(m_V\), \(g\), and numerical settings.

### 3.1 Variant A: zeroing the resolved negative \(\mu_{\nu_\mu}\) branch

Setting \(\mu_{\nu_\mu}=0\) over the entire 12--15 km interval changes:

- B.1 source normalization by \(+0.00548\%\);
- source-weighted escape probability by \(-0.01086\%\);
- the fixed-source escape probability by \(-0.00661\%\);
- the 12--15 km shell's source-weighted total \(\tau/g^2\) by \(+0.0231\%\).

At the sampled local points, the largest change in the \(\nu_\mu\) reduced absorption is \(0.373\%\), at \(r=12\) km and \(\omega=12\) MeV. The integrated transport response is much smaller.

### 3.2 Variant B: alternative \(\mu_\mu\) digitization

Replacing only the 12--15 km \(\mu_\mu\) profile gives:

- B.1 source normalization: \(+0.646\%\);
- source-weighted escape probability: \(-6.701\%\);
- fixed-source escape probability: \(-6.703\%\);
- escaped B.1 integral: \(-6.099\%\);
- source-weighted 12--15 km total \(\tau/g^2\): \(+3.600\%\).

The change is entirely in the Compton channel. Its shell-averaged \(\tau/g^2\) rises from \(9.5743\times10^{13}\) to \(1.4428\times10^{14}\), while the two neutrino inverse-decay shell contributions remain unchanged to the displayed precision.

The local Compton reduced absorption rises by approximately 19% at 12 km and 52--53% around 13--14 km for the sampled energies. However, Compton is subdominant in the shell's total opacity, so the full source-weighted escape probability changes by only about 6.7%.

**This is not an alternative model choice.** The Ferreira Fig. 1 caption explicitly identifies the dashed orange curve as SFHo-18.8 at 1 s post-bounce, the same named model and snapshot as Caputo Fig. 1; both papers cite the Bollig et al. simulation. The result therefore quantifies the impact of a second published reconstruction of the same nominal background. The origin of the 9.5--17.2% difference in \(\mu_\mu\) remains unresolved, so this curve is not adopted as the baseline.

### 3.3 Variant B2: same-model \(\mu_\mu\) reconstruction over the full 8--15 km source region

The 12--15 km substitution misses the largest discrepancy between the published curves. Extending the diagnostic replacement over 8--15 km gives:

- B.1 source normalization: \(+27.09\%\);
- source-weighted escape probability: \(-33.91\%\);
- fixed-baseline-source escape probability: \(-38.02\%\);
- escaped B.1 integral: \(-16.01\%\).

The effect is concentrated at smaller radii. At radial order 120, the B.1 source ratios in the emission intervals 8--10, 10--12, and 12--15 km are 1.533, 1.192, and 1.047, respectively.

Using the same baseline source weighting, the path-shell optical-depth ratios are:

| Path shell | Ferreira / Caputo total \(\langle\tau/g^2\rangle\) |
|---|---:|
| 8--10 km | 1.497 |
| 10--12 km | 1.183 |
| 12--15 km | 1.038 |

The change is entirely in Compton opacity and production. The neutrino inverse-decay channels are unchanged. In the 8--10 km shell, the Compton contribution increases by more than a factor of two; this is the main reason the full 8--15 km substitution has a much larger transport effect than the 12--15 km-only test.

The source and opacity changes partially oppose each other in the escaped B.1 integral: the source grows by about 27%, while the own-source escape probability falls by about 34%. The net escaped B.1 integral is therefore about 16% lower.

This remains a diagnostic substitution between two published reconstructions of the same nominal SFHo-18.8, 1 s post-bounce model. It is not a profile selection.

### 3.4 Variant C: unresolved \(\mu_{\nu_\mu}\) plotting-floor envelope \(\mu_{\nu_\mu}\) plotting-floor envelope

Extending the last resolved magnitude, \(|\mu_{\nu_\mu}|=1\) MeV, over the unresolved 13.109927--15 km interval changes:

- B.1 source normalization by \(-0.000878\%\);
- source-weighted escape probability by \(+0.00262\%\);
- fixed-source escape probability by \(+0.00179\%\);
- escaped B.1 integral by \(+0.00174\%\);
- the 12--15 km shell's total \(\tau/g^2\) by \(-0.00819\%\).

This is a deliberately conservative plot-floor stress test, not a claim that the physical chemical potential remains at \(-1\) MeV. Its effect is negligible for the present benchmark.

## 4. Comparison with the Fig. 7 discrepancy

The previously identified strong-endpoint target requires approximately

\[
\frac{P_{\rm esc}^{\rm required}}{P_{\rm esc}^{\rm base}}
\simeq 0.520.
\]

The 8--15 km diagnostic B2 gives the largest change. At radial order 120,

\[
\frac{P_{\rm esc}^{\rm B2, fixed source}}
     {P_{\rm esc}^{\rm base}}
=0.62389,
\]

compared with the target 0.520. It remains about 20% above the required escape probability. The own-source escape ratio is 0.66554, while the escaped B.1 integral ratio is 0.84453 because the B.1 source normalization also increases.

The narrower 12--15 km variant B gives only 0.933 for the fixed-source escape ratio. Variants A and C remain negligible. Thus the same-model \(\mu_\mu\) discrepancy over 8--15 km is a potentially important contributor to the strong-endpoint difference, but it does not by itself close it.

Consequently:

1. The \(\mu_{\nu_\mu}\) support/floor ambiguity in 12--15 km cannot explain the strong-endpoint mismatch.
2. The tested \(\mu_\mu\) alternative can move the result in the required direction, but its full effect is only about a 6.7% reduction in escape probability and its physical provenance is not yet established.
3. None of these profile variations closes the discrepancy. They do not justify changing the opacity normalization or applying a global correction.

## 5. Decisions

- Keep the Caputo \(\mu_\mu\) profile as the current baseline; do not average it with the Ferreira digitization.
- Keep the current \(\mu_{\nu_\mu}\) zero-outside-support convention, but label it as a figure-resolution assumption rather than a physical boundary condition.
- Record the floor-envelope result as a quantified uncertainty check.
- Do not alter B.1 normalization, B.2 opacity, \(R_{\max}\), the fixed-\(\omega\) convention, or the production axial-vector calculation.
- Keep the vector benchmark and axial-vector curve frozen pending the remaining independent source/background comparison.

## 6. Remaining work

The dominant unresolved input question is now sharply defined: two papers plot different \(\mu_\mu(r)\) curves while both identifying the background as SFHo-18.8 at 1 s post-bounce and citing Bollig et al. The 8--15 km diagnostic shows that this difference materially changes the Compton source and opacity. The next check is the exact profile-file/version and chemical-potential convention used in each post-processing analysis, together with the full 8--15 km muon-density consistency test. The Garching archive lists radial profiles in a protected directory that currently returns HTTP 401, so no raw table has been obtained. Figure digitization remains the only reproducible comparison available without authorized archive access.

The next numerical investigation should therefore focus on the full radial \(\mu_\mu(r)\) and muon-density consistency, not on another scan of the \(\mu_{\nu_\mu}\) floor. In particular, verify that the plotted \(\mu_\mu\), \(T\), and \(n_\mu\) belong to the same profile and chemical-potential convention.

## 7. Reproducibility

- Script: audit_profile_transport_sensitivity.py
- Machine-readable output: outputs/profile_transport_sensitivity_12_15km_2026-11-09.json
- Profile input: ../data/sfho188_digitized.csv
- Radial convergence driver: audit_profile_radial_convergence.py
- Radial convergence output: outputs/profile_radial_convergence_8_15km_2026-11-09.json
- Workflow: .github/workflows/profile-12-15km-audit.yml

The workflow runs the profile regression tests, regenerates hash-pinned source-PDF digitizations, executes the controlled B.1+B.2 profile variants, checks radial orders 40/80/120, and verifies that the production axial files remain unchanged.
