# B.16 10 MeV vector benchmark: outer inputs, inverse decay, and direction-resolved escape

**Date:** 2026-11-08  
**Status:** Steps 1--3 completed; literature equation mapping completed; full Fig. 7 discrepancy remains unresolved.  
**Benchmark:** \(m_V=10\) MeV, pure-vector \(L_\mu-L_\tau\) current, fixed-\(\omega\) Appendix-B prescription, reconstructed SFHo-18.8 profile at 1 s post-bounce.  
**Do not use this diagnostic to update the axial-vector curve.**

## Executive result

The 22--25 km outer-profile audit, an independent neutrino inverse-decay phase-space calculation, and a direction-resolved escape calculation all pass their internal numerical checks.

No outer-shell input/interpolation error or neutrino inverse-decay algebra error large enough to explain the approximately \(92\%\) high-coupling Fig. 7 luminosity excess is found.

The outer shell is not irrelevant: at the strong endpoint it contributes a non-negligible optical depth. However, for the dominant 8--15 km emission region, the inner path contributes substantially more optical depth than the 22--25 km segment. The surviving high-coupling population is strongly biased toward outward emission directions.

The remaining discrepancy must therefore be investigated as a whole-path/source-versus-escape problem, not corrected by changing the outer profile, rescaling a rate, or changing \(R_{\max}\).

## 1. Outer-profile inputs and interpolation

### 1.1 Provenance and physical support

The archived profile is a public-figure reconstruction, not the original Garching simulation table. The baseline temperature, muon chemical potential, and muon-neutrino chemical potential are extracted from Caputo, Raffelt and Vitagliano, arXiv:2109.03244v3, Fig. 1. The lapse is extracted from Ferreira, Marsh and Ravensburg, arXiv:2510.14469v1, Fig. 1, for the SFHo-18.8 model.

The source paper identifies the cold reference model as SFHo-18.8 at \(t_{\rm pb}=1\) s. Blinov et al. use the \(s18.8\)-SFHo-MUONS model at the same post-bounce time. The profile identity is therefore consistent at the model/time level, but the numerical input remains reconstructed from published figures rather than read from the raw simulation archive.

The raw profile file contains 501 nodes from 0 to 25 km at 0.05 km spacing. In the 22--25 km interval:

- \(T\) decreases from 3.5514 to 3.0338 MeV.
- \(N(r)\) increases from 0.90850 to 0.91991.
- The plotted \(\mu_\mu\) path ends at 22.1919 km at its 1 MeV plot floor; it is set to zero beyond that point.
- The plotted \(\mu_{\nu_\mu}\) branches end at 13.1099 km and 18.4230 km; it is zero in the outer 22--25 km interval.
- \(\mu_{\nu_\tau}=0\) follows Blinov et al.'s stated treatment because the simulation profile does not provide this chemical potential.

The \(\mu_\mu\) cutoff is not a substantial outer Compton-opacity omission. The independently evaluated negative-muon density is \(6.81\times10^{-14}\,\mathrm{fm}^{-3}\) at 20 km, \(5.45\times10^{-19}\,\mathrm{fm}^{-3}\) at 24 km, and \(7.05\times10^{-20}\,\mathrm{fm}^{-3}\) at 25 km.

The zero \(\mu_{\nu_\mu}\) value does not switch off neutrino inverse decay. The thermal zero-chemical-potential contribution remains in the \(\nu_\mu\) rate, and the \(\nu_\tau\) contribution is also retained with \(\mu_{\nu_\tau}=0\).

### 1.2 Lapse continuation

The digitized lapse curve ends at 23.9998 km. The baseline continues it to 25 km using a Schwarzschild exterior form matched continuously at 24 km, with
\[
r_s=24\,[1-N(24)^2]=3.8440\ {\rm km}.
\]

In the literal fixed-\(\omega\) B.2 path opacity, the lapse does not appear along the absorption path. It enters the B.1 source measure through \(N(r)^2\) and the local escape-energy threshold \(m_V/N(r)\).

The B.1 source fraction emitted at \(r\geq22\) km is only \(7.276\times10^{-4}\), and at \(r\geq24\) km only \(2.050\times10^{-4}\). The 22--25 km lapse continuation therefore affects only a very small fraction of the source.

A direct B.1 sensitivity test compares the baseline matched-Schwarzschild continuation with two diagnostic alternatives:

| Lapse continuation | Change in total B.1 source | Change in strong-end escape fraction |
|---|---:|---:|
| Matched Schwarzschild baseline | 0 | 0 |
| Freeze \(N=N(24\,\mathrm{km})\) | \(-1.16\times10^{-6}\) | \(-2.45\times10^{-4}\) |
| Linear extrapolation of the 23--24 km slope | \(+7.40\times10^{-8}\) | \(+1.80\times10^{-5}\) |

These alternatives are sensitivity brackets, not replacements for the matched exterior prescription. They demonstrate that the 24--25 km lapse continuation is not responsible for the Fig. 7 discrepancy.

### 1.3 Interpolation of the local opacity

The 0.05 km input profile is first sampled on the composite radial quadrature grid and the local rates are then interpolated along the outgoing path. The coarsest spacing in the outer part of that grid is 0.680 km. A direct comparison with rates evaluated on the original 0.05 km profile gives:

| Quantity in 22--25 km | Maximum relative interpolation error |
|---|---:|
| Temperature | 0.122% |
| Lapse | 0.0040% |
| \(\mu_{\nu_\mu}\) | 0 (baseline is zero throughout) |
| \(\mu_\mu\) | 9.50% |

The relatively larger \(\mu_\mu\) interpolation error occurs near its cutoff, where the muon density is already exponentially negligible. The peak Compton reduced-absorption rate in this shell is only \(1.35\times10^{-15}\) of the peak neutrino reduced-absorption rate.

For 8--15 km sources, the source-weighted mean optical depth accumulated only in 22--25 km changes by \(1.23\times10^{-5}\) when the opacity is evaluated directly on the 0.05 km input nodes. The strong-end outer-shell escape factor changes by only \(7.18\times10^{-6}\) relatively.

**Conclusion for Step 1:** no outer-profile interpolation or lapse-boundary error capable of explaining the high-coupling discrepancy is identified. The public-figure reconstruction remains a systematic limitation relative to the unavailable raw simulation data.

## 2. Independent neutrino inverse-decay phase-space audit

The equation mapping must be kept precise. In the notation of the local audit:

- B.6 is the direct neutrino-pair phase-space integral.
- B.10 is the neutrino inverse-decay detailed-balance relation.
- B.4 is the reduced-absorption identity.
- B.19 is the Compton detailed-balance relation, not the neutrino inverse-decay relation.

In the published Blinov et al. Appendix B these correspond to the neutrino production phase-space integral and its reduction in Eqs. (22)--(25), neutrino detailed balance in Eq. (26), and Compton detailed balance in Eq. (35). The reduced absorption used in the transport equation is Eq. (20).

An independent 192-point Gauss--Legendre integration evaluates
\[
I_{\rm prod}=\frac12\int_{-1}^{1}dc\,
 f_{\bar\nu}(E_1;-\mu_\nu)f_\nu(E_2;\mu_\nu),
\]
and separately evaluates the inverse occupation factor
\[
I_{\rm abs}=\frac12\int_{-1}^{1}dc\,
 [1-f_{\bar\nu}(E_1;-\mu_\nu)]
 [1-f_\nu(E_2;\mu_\nu)].
\]

The direct angular integral is compared with the independent analytic Fermi-integral implementation, the production rate in the reference code, the inverse rate, and the reduced absorption.

| Check | Maximum relative/log residual |
|---|---:|
| Direct B.6 integral vs analytic \(\nu_\mu\) integral | \(4.41\times10^{-14}\) |
| Direct B.6 integral vs analytic \(\nu_\tau\) integral | \(5.12\times10^{-14}\) |
| Direct B.6 total vs reference production rate | \(4.76\times10^{-14}\) |
| B.10 detailed balance, \(\nu_\mu\) | \(3.55\times10^{-15}\) |
| B.10 detailed balance, \(\nu_\tau\) | \(3.55\times10^{-15}\) |
| B.10 inverse rate vs direct inverse phase-space integral | \(1.82\times10^{-15}\) |
| B.4 two equivalent reduced-absorption forms | \(1.82\times10^{-15}\) |
| B.19 Compton detailed-balance identity | \(3.79\times10^{-16}\) |

At radii 22, 23, 24, and 25 km, the independent B.6 total production rate agrees with the reference implementation to better than \(6.6\times10^{-15}\). The outer profile has \(\mu_{\nu_\mu}=0\), but the thermal inverse-decay rate remains finite, as required.

**Conclusion for Step 2:** the neutrino inverse-decay phase-space integral, flavor sum, detailed balance, and reduced-absorption algebra are independently reproduced. No missing factor in this chain is found.

## 3. Direction-resolved escape for 8--15 km sources

The 8--15 km emission region accounts for 79.61% of the total B.1 source. The B.2 optical depth is split into the inner path (up to 22 km) and the outer 22--25 km shell. The outer-shell integral is evaluated in the radial coordinate with the exact chord Jacobian
\[
\frac{ds}{dr'}=\frac{r'}{\sqrt{r'^2-b^2}},
\qquad b=r\sqrt{1-\cos^2\theta}.
\]
The shell geometry tests verify the analytic path length and the expected symmetry of the outer-shell path under \(\cos\theta\to-\cos\theta\).

At the strong-absorption endpoint \(g=4.17169\times10^{-8}\), the source-weighted mean optical depths per \(g^2\) are
\[
\langle\tau_{\rm inner}/g^2\rangle=7.5711\times10^{15},
\qquad
\langle\tau_{\rm outer}/g^2\rangle=1.5634\times10^{15}.
\]
Thus the inner path contributes substantially more than the 22--25 km segment.

### 3.1 Direction bins at the strong endpoint

| \(\cos\theta\) bin | Mean inner \(\tau\) | Mean outer \(\tau\) | Mean total \(\tau\) | Fraction of escaping luminosity |
|---|---:|---:|---:|---:|
| \([-1,-0.5]\) | 17.545 | 2.631 | 20.176 | 0.543% |
| \([-0.5,0]\) | 14.728 | 2.807 | 17.534 | 2.785% |
| \([0,0.5]\) | 11.458 | 2.807 | 14.265 | 20.852% |
| \([0.5,1]\) | 8.980 | 2.631 | 11.611 | 75.821% |

The surviving population is strongly biased toward outward directions. This is a consequence of the full chord geometry and inner-core absorption; it is not an outer-boundary artifact.

The source-weighted outer optical-depth quantiles at the strong endpoint are
\[
\tau_{\rm outer}^{(10,50,90)\%}=(1.084,\ 2.150,\ 5.006),
\]
while the corresponding total optical-depth quantiles for the escaping population are
\[
\tau_{\rm total,esc}^{(10,50,90)\%}=(3.701,\ 5.164,\ 7.307).
\]

At the Fig. 7 luminosity peak, the outer-shell-only escape factor for 8--15 km sources is 0.8262; at the strong endpoint it is 0.1504. The inner-path-only factors are 0.4146 and \(9.294\times10^{-4}\), respectively. The full source-weighted escape probabilities for this selected emission region are 0.3549 at the peak and \(3.538\times10^{-4}\) at the strong endpoint.

**Conclusion for Step 3:** the outer shell matters, especially at strong coupling, but it is not the dominant optical-depth contribution for the main 8--15 km source region. Full angular averaging is essential, and the escaping population is dominated by outward trajectories.

## 4. Comparison with the published Blinov Appendix B

The literal numerical implementation matches the structure of the published equations:

| Published equation | Physical content | Implementation check |
|---|---|---|
| Eq. (17) | B.1 luminosity source, \(N(r)^2\), and local escape-energy threshold \(m_V/N(r)\) | Source measure includes \(N^2\) and the lower energy bound |
| Eqs. (18)--(19) | Full direction average and chord endpoint \(s_{\max}\) | Full angular integral and chord geometry |
| Eq. (20) | Reduced absorption \((1-e^{-\omega/T})\Gamma_{\rm abs}\) | Both algebraically equivalent forms checked |
| Eq. (21) | Vector speed \(v_V=\sqrt{1-m_V^2/\omega^2}\) | \(1/v_V\) retained in the optical depth |
| Eqs. (22)--(25) | Neutrino inverse-decay phase space and analytic Fermi integral | Direct angular integration agrees with analytic result |
| Eq. (26) | Neutrino inverse-decay detailed balance | Independently verified |
| Eq. (35) | Compton detailed balance | Separately verified; not confused with neutrino detailed balance |

The published paper explicitly identifies \(R_{\max}=R_\nu\simeq25\) km, sets \(\mu_{\nu_\tau}=0\) because the simulations do not provide that profile, and uses the SFHo-18.8 muonic supernova model at 1 s post-bounce. The present benchmark follows those choices.

The literal B.2 opacity in Eq. (18) uses \(\Gamma_{\rm abs}^{*}(r',\omega)\) along the path with the same displayed energy argument \(\omega\). The path-redshift alternative is therefore kept as a separate sensitivity diagnostic and is not silently substituted into the fixed-\(\omega\) reproduction.

Relevant primary sources:

- Blinov et al., [arXiv:2511.09619v2](https://arxiv.org/html/2511.09619v2), Appendix B.
- Caputo, Raffelt and Vitagliano, [arXiv:2109.03244v3](https://arxiv.org/html/2109.03244v3), Fig. 1 and the SFHo-18.8 cold reference model at 1 s.
- Ferreira, Marsh and Ravensburg, [arXiv:2510.14469v1](https://arxiv.org/html/2510.14469v1), Sec. III and Fig. 1, including the SFHo-18.8 lapse profile at 1 s.

The Caputo and Ferreira figure reconstructions are not identical inputs: their plotted \(\mu_\mu\) curves differ substantially despite the same model label. The baseline retains Caputo's \(\mu_\mu\), because its Fermi-integrated muon density agrees with the independently plotted Caputo density at the checked radii. Ferreira contributes the lapse only. This source discrepancy remains documented and unresolved at the raw-simulation level; the present outer-shell audit does not claim to recover the private Garching table.

## 5. Source-versus-escape diagnosis of the remaining Fig. 7 mismatch

At the weak endpoint, the escape probability required to match the digitized Fig. 7 luminosity while holding the calculated B.1 source fixed is 1.0952, which is impossible for a pure attenuation factor. This is a source-side normalization/profile issue.

At the Fig. 7 peak, the required and calculated escape probabilities are 0.34365 and 0.35247, differing by about 2.5%.

At the strong endpoint, they are
\[
P_{\rm esc}^{\rm calc}=3.2392\times10^{-4},
\qquad
P_{\rm esc}^{\rm req}=1.6850\times10^{-4}.
\]
The required-to-calculated ratio is 0.5202, corresponding to an effective escape-exponent difference of 0.6536. This is a whole-path averaged statement, not a uniform shift of every ray's optical depth.

The 0.18% path-grid interpolation effect, the \(10^{-5}\)-level outer-shell opacity interpolation effect, the \(10^{-6}\)-level lapse-source effect, and the \(10^{-14}\)-level inverse-decay algebra residuals are all far below the strong-end Fig. 7 discrepancy.

**Current diagnosis:** the discrepancy is not explained by the 22--25 km profile interpolation, the 24--25 km lapse continuation, the neutrino inverse-decay phase-space formula, or the tested chord/direction geometry. The remaining investigation must focus on the full source/opacity inputs and the whole-path escape calculation. No rate rescaling or empirical correction is justified.

## 6. Reproducibility files and workflows

Machine-readable results:

- outputs/b16_outer_profile_inputs_10mev_2026-11-08.json
- outputs/b16_lapse_boundary_sensitivity_10mev_2026-11-08.json
- outputs/b16_outer_profile_interpolation_10mev_2026-11-08.json
- outputs/b16_neutrino_inverse_decay_10mev_2026-11-08.json
- outputs/b16_directional_escape_8_15km_10mev_2026-11-08.json
- outputs/b16_emission_radius_escape_10mev_2026-11-08.json
- outputs/b16_quadrature_convergence_10mev_2026-11-08.json

Independent scripts:

- audit_b16_outer_profile_inputs.py
- audit_b16_lapse_boundary_sensitivity.py
- audit_b16_outer_profile_interpolation.py
- audit_b16_neutrino_inverse_decay.py
- audit_b16_directional_escape_8_15.py
- audit_b16_emission_radius_escape.py
- audit_b16_quadrature_convergence.py

The corresponding GitHub Actions audits pass, including 3 outer-shell geometry tests, 4 inverse-decay tests, and 3 directional-escape tests. The workflows also verify that the production axial-vector rate, transport, and plot outputs remain unchanged.

## 7. Next step

Proceed to the independent whole-curve comparison with the published Fig. 7 inputs, keeping the source-side weak-coupling discrepancy separate from the strong-coupling escape discrepancy. In particular, isolate the inner-path absorption channels for the surviving outward trajectories and compare their local inputs with the exact Appendix-B expressions. The 25 km boundary, the B.1 source normalization, and the validated neutrino inverse-decay formula remain fixed.

**The axial-vector scan remains frozen until the pure-vector Fig. 7 benchmark is understood.**
