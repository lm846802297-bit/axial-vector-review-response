# B.16 Fig. 7 discrepancy: source normalization versus escape probability

**Status:** diagnostic separation completed for the 10 MeV vector benchmark.  
**Baseline:** fixed-omega Appendix-B B.1/B.2, \((N_r,N_E,N_\Omega,N_s)=(40,100,16,32)\).  
**Profile limitation:** public-figure digitization of SFHo-18.8, not the original simulation table.

## 1. Separation identity

For each coupling, write
\[
L_{\rm calc}(g)=L_{\rm thin}^{\rm calc}(g)\,P_{\rm esc}^{\rm calc}(g),
\]
where the optically thin source is evaluated from the B.1 measure and
\[
P_{\rm esc}^{\rm calc}
=\frac{\int dV\,dE\,d\Omega\;S_{\rm B.1}\,e^{-g^2\tau}}
{\int dV\,dE\;S_{\rm B.1}}.
\]

The escape probability that would be required to match the digitized Fig. 7 luminosity, while holding the calculated thin source fixed, is
\[
P_{\rm esc}^{\rm req}(g)=\frac{L_{\rm Fig.7}(g)}{L_{\rm thin}^{\rm calc}(g)}.
\]
If this ratio exceeds one, no nonnegative absorption opacity can reconcile the reference point with the current source normalization.

## 2. Three representative points

| Point | \(g\) | \(P_{\rm esc}^{\rm calc}\) | \(P_{\rm esc}^{\rm req}\) | Required / calculated |
|---|---:|---:|---:|---:|
| Weak endpoint | \(4.7964\times10^{-10}\) | 0.997870 | 1.095184 | 1.09752 |
| Fig. 7 peak | \(1.1341\times10^{-8}\) | 0.352473 | 0.343647 | 0.97496 |
| Strong endpoint | \(4.1717\times10^{-8}\) | \(3.23918\times10^{-4}\) | \(1.68498\times10^{-4}\) | 0.52019 |

At the weak endpoint, the required escape probability is greater than unity. Therefore, the approximately 8.9% luminosity deficit cannot be fixed by changing the absorption calculation alone; the optically thin source normalization/profile/B.1 input must first be reconciled.

At the Fig. 7 peak, the required escape probability differs from the calculated one by only 2.50% relative to the calculated value.

At the strong endpoint, the required escape probability is 0.5202 times the calculated value. In effective-optical-depth language,
\[
\Delta\tau_{\rm eff}
=-\ln\!\left(\frac{P_{\rm esc}^{\rm req}}{P_{\rm esc}^{\rm calc}}\right)
=0.6536.
\]
This is a statement about the logarithm of the fully averaged escape probability, not a uniform additive shift to every ray's optical depth.

## 3. What this establishes

1. The weak-coupling mismatch is a source-side issue, not an opacity issue.
2. The peak is reproduced at the few-percent level.
3. The growing high-coupling discrepancy is primarily an escape/opacity-side issue, after factoring out the fixed B.1 source.
4. The quadrature convergence envelope is below 0.33%, so the 92% high-end luminosity discrepancy is not explained by the tested numerical resolutions.
5. The raw Fig. 7 PDF coordinate audit confirms that the last visible 10 MeV point is genuinely at \(g=4.17169\times10^{-8}\), \(L=1.26781\times10^{52}\,\mathrm{erg/s}\); it is not a path-order or axis-clipping artifact.

## 4. Next diagnostic priority

Do not rescale the opacity or luminosity. The next calculation should isolate the high-coupling escape mismatch by emission shell and by absorption channel, using the existing emission-radius/absorption-shell matrix. In particular:

- compare the escape-probability distribution over emission radius at the Fig. 7 peak and strong endpoint;
- test whether the final radial shell and the outer boundary at 25 km materially affect the high-coupling tail;
- compare neutrino and semi-Compton contributions to the *escape exponent* for the source-weighted escaping population, rather than only comparing their unattenuated mean optical depths;
- keep the source-side normalization discrepancy as a separate issue.

This is the narrowest next step that can locate the high-coupling discrepancy without modifying the physical model.


## 4. Emission-radius distribution: thin source versus escaping population (completed 2026-11-10)

The archived emission-radius calculation now completes the earlier source-versus-escape diagnostic. At the strong endpoint \(g=4.17168965\times10^{-8}\), the global source-weighted escape probability is \(3.23918\times10^{-4}\). The table separates the B.1 emission measure from the same measure after multiplication by the full angularly averaged survival probability.

| Emission shell | B.1 thin-source fraction | Shell-averaged escape probability | Escaped-luminosity fraction |
|---|---:|---:|---:|
| 0--5 km | 0.910% | \(1.254\times10^{-5}\) | 0.0352% |
| 5--8 km | 17.508% | \(1.798\times10^{-4}\) | 9.720% |
| 8--10 km | 39.812% | \(4.020\times10^{-4}\) | 49.406% |
| 10--12 km | 26.081% | \(3.801\times10^{-4}\) | 30.601% |
| 12--15 km | 13.718% | \(1.613\times10^{-4}\) | 6.833% |
| 15--16.5 km | 1.266% | \(1.151\times10^{-5}\) | 0.0450% |
| 16.5--18.5 km | 0.429% | \(1.734\times10^{-6}\) | 0.00230% |
| 18.5--20 km | 0.129% | \(9.584\times10^{-7}\) | 0.000381% |
| 20--22 km | 0.0745% | \(4.879\times10^{-6}\) | 0.00112% |
| 22--25 km | 0.0728% | \(1.494\times10^{-2}\) | 3.356% |

The 8--12 km shells contain \(65.893\%\) of the thin source but \(80.007\%\) of the escaping luminosity. The 8--15 km region contains \(79.612\%\) of the thin source and \(86.840\%\) of the escaping luminosity. The 22--25 km emission shell contains only \(0.0728\%\) of the thin source but \(3.356\%\) of the escaping luminosity; its shell-averaged escape probability is about 46.1 times the global mean. This is an emission-radius effect and must not be confused with the optical depth accumulated in the 22--25 km path shell.

The source-channel composition also changes under escape weighting:

| Channel | Thin-source fraction | Escaped-luminosity fraction |
|---|---:|---:|
| Compton | 32.005% | 45.855% |
| \(\nu_\mu\) inverse decay | 33.411% | 26.982% |
| \(\nu_\tau\) inverse decay | 34.585% | 27.163% |

Thus the escaping population is not a simple radial or channel copy of the B.1 source. Compton has a larger escape fraction than either neutrino channel at this endpoint, even though neutrino inverse decay dominates the total B.2 attenuation.

**Reference limitation:** Fig. 7 publishes an integrated luminosity curve, not a radius-resolved emission distribution. The table is therefore an internal, source-weighted transport diagnostic; it is not a direct digitization or comparison to a Fig. 7 radial profile.

The machine-readable result is outputs/b16_emission_radius_escape_10mev_2026-11-08.json. No source, opacity, profile, coupling, luminosity, or axial-vector curve is changed by this decomposition.


## 5. High-coupling shell attribution and the 25 km boundary

At the strong endpoint \(g=4.17169\times10^{-8}\), removing one absorption shell at a time while holding the source fixed gives:

| Removed absorption shell | Luminosity enhancement |
|---|---:|
| 0--5 km | 1.013 |
| 5--8 km | 1.214 |
| 8--10 km | 2.090 |
| 10--12 km | 2.530 |
| 12--15 km | 2.943 |
| 15--16.5 km | 1.588 |
| 16.5--18.5 km | 1.869 |
| 18.5--20 km | 1.590 |
| 20--22 km | 1.844 |
| 22--25 km | 4.056 |

These are nonlinear leave-one-shell-out sensitivity factors; they are not additive contributions. The outermost 22--25 km shell is the largest individual shell sensitivity at the strong endpoint. Removing all opacity at \(r\geq15\) km raises the luminosity by a factor 114.1, while removing all neutrino opacity raises it by a factor 963.0. Removing all Compton opacity raises it by a factor 2.49.

The 25 km outer boundary is **not an arbitrary numerical truncation**. Blinov et al. explicitly identify \(R_{\max}\) with the neutrinosphere radius \(R_\nu\simeq25\) km: vectors produced inside this radius must survive to beyond it to count as ballistic energy loss. This is stated in Appendix B, in the discussion immediately following Eqs. (B.1)--(B.5), and is consistent with Sec. 4.1, which places the neutrinosphere at approximately 25 km. We therefore do not extend the integration domain beyond 25 km or reinterpret the outermost shell as missing stellar matter.

**Consequence for the next step:** inspect the reconstructed thermodynamic inputs and the exact path integral specifically over 22--25 km, and compare their influence on the strong-coupling escape distribution. The literature-defined \(R_{\max}=25\) km remains fixed. The discrepancy must not be “fixed” by changing this radius without an independent physical justification.

## 6. Next step

The source-versus-escape decomposition is complete. The remaining high-coupling discrepancy is now a B.2 path problem rather than an unidentified B.1 emission-radius weighting problem. Proceed with the independent path-integral and angle-integration cross-check over the dominant 8--22 km path region, retaining the 22--25 km contribution and the fixed-\(\omega\) B.16 benchmark. Do not rescale the opacity, alter the 25 km boundary, or substitute the B.13 alternative kernel for this benchmark.
