# Forty-sixth review: B.1 energy variables and B.2 lapse-redshift propagation

Review date: 2026-11-15  
Reviewed branch: \`maintenance/repository-organization-audit-20261114\`  
Scope: the B.1/B.2 energy-convention audit, the lapse-redshift diagnostic implementation and archived output, and the published Blinov et al. version of record.

Primary source: Blinov et al., *JHEP* 06 (2026) 155, arXiv:2511.09619, [DOI:10.1007/JHEP06(2026)155](https://doi.org/10.1007/JHEP06(2026)155), main text Sec. 4.1 and Appendix B.1–B.5.

## 1. Executive result

The B.1 local-energy versus energy-at-infinity transformation is exact and correctly implemented. No B.1 redshift normalization error was found.

The unresolved physical issue is B.2: the published main text calls \(\omega\) the energy at spatial infinity, while the Appendix-B.2 ray exponent writes a single \(\omega\) in the local absorption kernel and local vector speed at every point along the chord, without displaying the conversion to local energy. The repository's fixed-\(\omega\) lane is a literal reproduction of the printed argument. It is not equivalent to conserved-\(E_\infty\) propagation when the lapse varies.

The separate lapse-redshift diagnostic is correctly implemented for its stated approximation: it updates the local energy, local collision kernels, local vector speed, and \(1/v_V\) factor along the chord. It still uses a Euclidean straight chord and Euclidean path element, so it is not full GR ray tracing.

This is a publication-level notation/implementation ambiguity, not enough evidence to assert a definite author error or to claim that either branch reproduces the unpublished Fig. 7 code.

## 2. B.1 energy-variable transformation

The printed Appendix-B.1 expression uses the local source energy:
\[
L_\infty
=\int 4\pi r^2dr\,N(r)^2
\int_{m_V/N(r)}^\infty d\omega_{\rm loc}\,
\frac{k_{\rm loc}\omega_{\rm loc}^2}{2\pi^2}
\Gamma_{\rm prod}^{\rm loc}(r,\omega_{\rm loc})\,O.
\]
The lower limit is the escape condition
\[
E_\infty=N(r)\omega_{\rm loc}>m_V.
\]
With \(E_\infty=N(r)\omega_{\rm loc}\),
\[
\omega_{\rm loc}=\frac{E_\infty}{N(r)},\quad
d\omega_{\rm loc}=\frac{dE_\infty}{N(r)},\quad
k_{\rm loc}=\frac{\sqrt{E_\infty^2-N(r)^2m_V^2}}{N(r)}.
\]
Consequently,
\[
N(r)^2 k_{\rm loc}\omega_{\rm loc}^2d\omega_{\rm loc}
=
\frac{E_\infty^2\sqrt{E_\infty^2-N(r)^2m_V^2}}{N(r)^2}
\,dE_\infty.
\]
The lower limit becomes \(E_\infty=m_V\), and the local source kernel is evaluated at \(E_\infty/N(r)\). This is an exact change of variables, not a different physical prescription.

The independent B.1 local-energy and \(E_\infty\) integrations agree channel by channel at stored precision:
- neutrino inverse decay: \(2.924014280393587\times10^{70}\) erg/s per \(g^2\);
- muon-Compton: \(1.3803538885385007\times10^{70}\) erg/s per \(g^2\);
- total: \(4.304368168932088\times10^{70}\) erg/s per \(g^2\).

Acceptance run: [GitHub Actions #42573725261](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42573725261). The separate \(-0.443\%\) difference against the older archived B.16 source is a source-grid/profile/interpolation residual, not a failure of the energy-variable transformation.

## 3. Physical B.2 energy along a path

For a vector produced at \(r_{\rm src}\) with local energy \(\omega_{\rm src}\), the conserved Killing energy in a static background is
\[
E_\infty=N(r_{\rm src})\omega_{\rm src}.
\]
At a path point \(r'(s)\), its local energy and speed must be
\[
\omega_{\rm loc}(s)=\frac{E_\infty}{N(r'(s))}
=\omega_{\rm src}\frac{N(r_{\rm src})}{N(r'(s))},
\]
\[
v_V(s)=\sqrt{1-\frac{m_V^2}{\omega_{\rm loc}(s)^2}}.
\]
Thus a lapse-only optical depth on a fixed Euclidean chord is
\[
\tau_{\rm lapse}
=\int_0^{s_{\max}}ds\,
\frac{\Gamma_{\rm abs}^{*,\rm loc}
(r'(s),\omega_{\rm loc}(s))}
{v_V(s)}.
\]
The local absorption kernel includes its local thermal factors and detailed-balance relation. It is not sufficient to redshift only the source energy or only the opacity argument while keeping \(v_V\) fixed.

The published Eq. (B.2) prints
\[
\Gamma_{\rm abs}^{*}(r'(s),\omega)/v_V(\omega)
\]
with the same \(\omega\) at every path point. It does not explicitly show \(E_\infty/N(r'(s))\) in either the local rate or speed. Because the main text identifies \(\omega\) as energy at infinity, the local conversion may have been intended implicitly; because the Appendix-B.2 equation prints a fixed argument, a literal implementation instead holds the local kernel argument fixed. The paper does not resolve this in the displayed equation, and its numerical code is not public.

The repository must therefore preserve two distinct lanes:
1. **Fixed-\(\omega\) literal B.2 reproduction:** same argument along the chord, as printed.
2. **Conserved-\(E_\infty\) lapse-redshift diagnostic:** local energy and local speed updated along the chord.

Do not describe the first as a physically complete GR ray, and do not describe the second as a full GR result.

## 4. Code-level audit of the lapse-redshift diagnostic

The function \`redshifted_scalar_optical_depths\` in \`audit_b16_global_redshift.py\` was inspected. It:
1. forms \(E_\infty=N_{\rm src}\omega_{\rm src}\);
2. computes \(\omega_{\rm loc}(s)=E_\infty/N(r'(s))\);
3. recomputes local neutrino, dimuon, and Compton production kernels at \(\omega_{\rm loc}(s)\);
4. reconstructs reduced absorption using the local \(x=\omega_{\rm loc}/T(r')\) detailed-balance factor;
5. recomputes \(v_V(s)=\sqrt{1-m_V^2/\omega_{\rm loc}(s)^2}\);
6. integrates with \(ds/v_V(s)\);
7. assigns zero escape probability to source modes with \(E_\infty\le m_V\).

These operations are consistent with lapse redshift in a static background. The approximation is in the path geometry: it keeps the Euclidean straight chord and \(ds\), omitting the spatial metric factor and gravitational ray bending.

The code docstring and this audit were updated to state explicitly that both the local kernels and \(v_V(s)\) are recomputed. No numerical code path or archived output was changed.

## 5. Numerical consequence at 10 MeV

For the archived 40-radius, 100-energy, 16-angle, 32-path-order diagnostic on the vertex-preserving reconstructed profile:

| Metric | Fixed-\(\omega\) literal B.2 | Conserved-\(E_\infty\) lapse-redshift |
|---|---:|---:|
| Weak endpoint vs Fig. 7 | \(-8.8853\%\) | \(-8.8991\%\) |
| Reference peak vs Fig. 7 | \(+2.5688\%\) | \(-2.7704\%\) |
| Strong endpoint vs Fig. 7 | \(+92.2406\%\) | \(+36.7448\%\) |
| Strong-endpoint shift vs fixed-\(\omega\) | 0 | \(-28.8679\%\) |

At the strong endpoint, the escape fraction changes from \(3.23921\times10^{-4}\) to \(2.30412\times10^{-4}\). Along the sampled paths, the local/source energy ratio spans 0.8007–1.2265 and the minimum local vector speed is 0.3929.

The lapse-redshift prescription substantially changes the strong-absorption tail but does not reproduce Fig. 7. It is not a fit and does not justify an opacity rescaling.

Machine-readable output: \`outputs/b16_global_redshift_audit_2026-11-09.json\`, SHA \`c324f75198ab49916f0880c1b07fb9652a9c1abd\`.

## 6. Limitations and decision

1. B.1 redshift normalization is closed by an exact variable transformation and an independent numerical equivalence test.
2. B.2 fixed-\(\omega\) versus conserved-\(E_\infty\) path treatment remains unresolved at the publication/implementation level.
3. The lapse-redshift diagnostic is not full GR because it retains a Euclidean path measure and straight chord.
4. A full GR extension needs a same-snapshot spatial metric (or \(A(r)\)/enclosed mass) and geodesic propagation, not only \(N(r)\).
5. The reconstructed public-figure profile is not the original Garching raw snapshot.
6. Neither path prescription reproduces Fig. 7; no opacity/source/luminosity rescaling is allowed.

No production rates, B.1 source normalization, B.2 baseline, Fig. 7 reference, manuscript, referee response, or axial-vector constraint output was changed.



## Current-tree, workflow, and independent-band reconciliation (2026-11-16)

The current-tree implementation audit_b16_global_redshift.py was inspected at the function level. Its path-redshift branch computes \(E_\infty=N_{\rm src}\omega_{\rm src}\), updates \(\omega_{\rm loc}=E_\infty/N(r')\) at each chord node, reevaluates the local neutrino/dimuon/Compton production kernels and detailed-balance reduced absorption, updates \(v_V=\sqrt{1-m_V^2/\omega_{\rm loc}^2}\), and integrates with \(ds/v_V\). It also assigns zero escape to source modes with \(E_\infty\le m_V\). The Euclidean chord and \(ds\) are retained; the implementation is a lapse-redshift diagnostic, not a GR geodesic calculation.

The B.1 equivalence output was independently fetched from the current tree. Local-energy and \(E_\infty\) integrals agree channel by channel: neutrino \(2.924014280393587\times10^{70}\), dimuon \(0\), Compton \(1.3803538885385007\times10^{70}\), and total \(4.304368168932088\times10^{70}\) erg s\(^{-1}\) per \(g^2\). The maximum stored relative difference is \(2.22\times10^{-16}\). The original acceptance workflow #42573725261 is completed successfully; the current pinned 2026-11-15 B.1 JSON records run commit 6c2cdf858cf908f5ba390f4dfae82e01abb132fc, matching the separately completed-successfully pinned run #43650570961.

The 10 MeV full 25-coupling comparison in b16_global_redshift_audit_2026-11-09.json uses the 40-radius / 100-energy / 16-angle / 32-path grid and current reconstructed-profile SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. Its fixed-\(\omega\) versus path-redshift residuals reproduce §5: weak endpoint \(-8.8853\%/-8.8991\%\), peak \(+2.5688\%/-2.7704\%\), and strong endpoint \(+92.2406\%/+36.7448\%\). The strong-end escape fraction changes from \(3.23921\times10^{-4}\) to \(2.30412\times10^{-4}\); the path energy ratio is 0.8007–1.2265 and minimum local vector speed is 0.3929. Workflow #42585105214 for the global redshift audit completed successfully on the JSON's recorded commit. The B.2 path-energy and opacity-interpolation convergence workflows #42585105236 and #42585105244 also completed successfully.

A separate 2026-11-15 NumPy cross-runtime output is present for the 210–510 MeV band only (10 selected energy nodes from the 842-node full grid; source radial order 200, opacity radial order 640, angle order 32, path order 64). It gives fixed-\(\omega\) escaped luminosity \(1.70178483\times10^{52}\) erg/s and path-redshift \(1.22367050\times10^{52}\) erg/s, a \(-28.0949\%\) shift in this band. Direct local-rate recomputation differs from the bilinear-opacity interpolation result by \(+0.5021\%\) in escaped luminosity. This is an independent high-energy-band sensitivity check; it is not the 25-coupling full-energy curve in §5 and must not be mixed with it.

The fixed-\(\omega\) branch remains the literal Appendix-B.2 reproduction lane; the conserved-\(E_\infty\) branch remains a separate sensitivity lane. Neither reproduces Fig. 7, and neither resolves the paper's notation/implementation ambiguity. The neighboring 0.1/1 MeV B.13 low-mass global-convergence jobs on the same 2026-11-09 commit did not pass; this review makes no low-mass convergence claim. No source, opacity, coupling, profile, luminosity, Fig. 7 reference, SN1987A limit, manuscript, referee response, or axial-vector constraint was modified.
