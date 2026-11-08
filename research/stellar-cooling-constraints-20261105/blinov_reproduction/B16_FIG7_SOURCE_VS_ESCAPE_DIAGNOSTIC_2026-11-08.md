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
