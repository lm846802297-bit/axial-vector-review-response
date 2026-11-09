# B.1 energy variable and B.2 path-redshift convention audit (2026-11-09)

## Executive conclusion

The published Appendix-B formulae contain a convention that should be stated explicitly when interpreting the gravitational terms:

- The B.1 integration variable is the **local energy at the production point**, not the conserved energy at infinity. The lower limit \(\omega_{\min}=m_V/N(r)\) is the local escape threshold, and the prefactor \(N(r)^2\) converts local energy/time to luminosity at infinity.
- The literal B.2 expression inserts the same \(\omega\) into \(\Gamma_{\rm abs}^*(r'(s),\omega)\) along the entire chord. Taken literally, this holds the local energy argument fixed along the path.
- The main-text discussion describes \(\omega\) as the energy at spatial infinity. That wording is not consistent with the local-energy interpretation implied by the B.1 lower limit unless an additional conversion is understood implicitly.

The repository retains the literal Appendix-B implementation as the Fig. 7 reproduction baseline. A separate redshift-only diagnostic changes the local energy along the path but retains Euclidean straight chords; it is not a full GR calculation and is not substituted for the baseline.

## 1. Direct reading of B.1

The version-of-record Appendix B gives
\[
L_V=\int_0^{R_{\max}}dr\,4\pi r^2N(r)^2
\int_{m_V/N(r)}^\infty d\omega\,
\frac{k\omega^2}{2\pi^2}\,
\Gamma_{\rm prod}(r,\omega)\,O(r,\omega).
\]

The lower limit follows from the escape condition for a vector produced with local energy \(\omega_{\rm loc}\):
\[
E_\infty=N(r)\omega_{\rm loc}>m_V
\quad\Longrightarrow\quad
\omega_{\rm loc}>\frac{m_V}{N(r)}.
\]
The factor \(N(r)^2\) accounts for gravitational redshift of energy and time dilation in the luminosity measured at infinity. Thus the \(\omega\) integrated in this form is local at the source.

## 2. Direct reading of B.2

The published ray optical depth is written with
\[
\tau(r,\omega,\cos\theta)=
\int_0^{s_{\max}}ds\,
\frac{\Gamma_{\rm abs}^*(r'(s),\omega)}{v_V}.
\]
The same \(\omega\) appears at every path point. No explicit lapse ratio is written in the argument of the local absorption kernel. The repository's fixed-\(\omega\) implementation therefore follows the literal Appendix-B expression.

If instead \(E_\infty=N(r)\omega_{\rm src}\) is conserved along the path, the local energy should be
\[
\omega_{\rm loc}(s)=
\omega_{\rm src}\frac{N(r)}{N(r'(s))}.
\]
This is the prescription used by the separate redshift-only diagnostic. It changes only the local energy argument in the opacity kernel; it does not include spatial-curvature corrections to the path length.

## 3. Numerical comparison at 10 MeV

For the current vertex-preserving profile (SHA-256 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c)):

| Quantity | Fixed-\(\omega\) Appendix-B baseline | Path-redshift-only diagnostic |
|---|---:|---:|
| Weak endpoint difference vs Fig. 7 | -8.8853% | -8.8991% |
| Reference peak difference vs Fig. 7 | +2.5688% | -2.7704% |
| Strong endpoint difference vs Fig. 7 | +92.2406% | +36.7448% |
| Strong-endpoint luminosity shift relative to fixed-\(\omega\) | 0 | -28.8679% |

The redshift-only variant reduces the strong-endpoint discrepancy but does not reproduce Fig. 7. It also changes the peak residual, so it cannot be described as a uniform normalization correction.

## 4. Why this is not yet a full GR propagation calculation

A complete GR path treatment requires more than the lapse function. For a static spherical metric,
\[
ds^2=-N(r)^2dt^2+A(r)^2dr^2+r^2d\Omega^2,
\]
the proper path element and ray geometry depend on the spatial metric function \(A(r)\), while the local energy follows the conserved Killing energy. The current public-figure profile contains a lapse reconstruction but not an independently tabulated \(A(r)\) or enclosed-mass profile over the complete path. Consequently, the redshift-only test is not a substitute for a full GR geodesic/transport calculation.

## 5. Decision

1. Keep fixed-\(\omega\) as the paper-faithful Appendix-B reproduction baseline.
2. Retain path-redshift-only as a separate physical sensitivity diagnostic.
3. Do not rescale opacity or luminosity to force agreement.
4. Do not claim that the path-redshift-only result is a full GR result.
5. If a full GR extension is pursued later, obtain a consistent metric (at minimum \(N(r)\) and \(A(r)\), or \(N(r)\) and enclosed mass) from the same SFHo-18.8 snapshot before changing the transport model.

No production axial-vector curve, source normalization, absorption rate, or referee-response text is changed by this audit.


## 6. Version-of-record source adjudication (2026-11-09)

Primary source: Blinov, Fox, Kelly, Plestid and Zhou, *L_mu-L_tau gauge bosons in beam dumps and supernovae*, JHEP 06 (2026) 155, DOI [10.1007/JHEP06(2026)155](https://doi.org/10.1007/JHEP06(2026)155), arXiv:2511.09619. This check uses the published version of record (published 15 June 2026), rather than relying only on the preprint.

### 6.1 Energy notation across the main text and Appendix B

The published main text, Sec. 4.1, immediately below Eq. (4.2), describes \\(\\omega\\) as the energy carried by the vector at spatial infinity. Appendix B uses the same symbol in a different-looking way:

- Eq. (B.1) contains \\(N(r)^2\\) and the local escape threshold \\(\\omega_{\\min}=m_V/N(r)\\). With the local phase-space measure and local production rate appearing in that equation, this identifies the integration variable as the energy measured locally at the production point.
- Eq. (B.2) inserts the same \\(\\omega\\) into \\(\\Gamma^*_{\\rm abs}(r'(s),\\omega)\\) all along the chord.
- Eqs. (B.4) and (B.5) use that same energy in the local thermal factor and vector speed.

Thus the source-energy interpretation implied by Appendix B.1, the fixed energy argument printed in B.2, and the phrase “energy ... at spatial infinity” in Sec. 4.1 are not all the same convention unless an implicit conversion is supplied. The article does not write that conversion explicitly in B.2.

For the reproduction task, the code therefore retains the literal Appendix-B prescription as one clearly defined branch. The redshift-only diagnostic remains a distinct physically motivated alternative; it is not substituted into the published-form baseline and is not called full GR.

### 6.2 Compton prescription: formal rate versus approximate reduction

The version of record presents Eq. (B.13) as the thermal phase-space integral for \\(\\mu\\gamma\\to\\mu V\\). It then discusses the non-relativistic-muon/no-recoil approximation, gives the approximate cross section in Eq. (B.14), and derives the compact thermal-rate expressions in Eqs. (B.15)--(B.16).

The Fig. 7 discussion says that the luminosity is evaluated using Eq. (B.1) and the physics inputs described in Appendix B, but it does not separately identify the numerical Compton implementation as either the full Eq. (B.13) integral or the reduced Eq. (B.16) expression. The formal presentation of B.13 and the subsequent approximate reduction therefore need to be distinguished when describing what is directly established by the article.

Current project convention: retain the B.16 closed-form calculation as the operational historical benchmark, and retain the exact moving-muon B.13 calculation as a separate alternative. This is a controlled comparison, not proof that the unpublished Fig. 7 code used B.16. No choice is made by fitting either branch to Fig. 7.

The article's data-availability and code-availability statements say that no associated data and no associated code are deposited. The original numerical implementation therefore cannot be inspected from the publication itself.

### 6.3 Reproduction consequence

For the current vertex-preserving profile B at 10 MeV:

- literal fixed-\\(\\omega\\), B.16 working benchmark: strong-endpoint residual \\( +92.24\\% \\);
- path-redshift-only diagnostic with the same Euclidean chord measure: strong-endpoint residual \\( +36.74\\% \\);
- consistent global B.13 source-and-opacity replacement: strong-endpoint residual \\( +131.53\\% \\).

These are different physical prescriptions, not interchangeable numerical refinements. None reproduces Fig. 7. The B.13 result remains a separate diagnostic and is not promoted to a final precision prediction until its dedicated global convergence output is fully archived.

### 6.4 Decision

1. Preserve the literal fixed-\\(\\omega\\) Appendix-B calculation and its B.16 working Compton implementation for continuity with the current benchmark.
2. Keep the redshift-only and B.13 calculations separate, with their assumptions visible.
3. Do not state that the published Fig. 7 code is known to use B.16 unless independent implementation evidence becomes available.
4. Do not infer a full GR result from the redshift-only diagnostic.
5. Do not alter the production axial-vector curve or use empirical rescaling to improve the vector comparison.


## 7. Current-profile rerun and machine-readable archive (2026-11-09)

The path-redshift diagnostic has now been rerun on the exact vertex-preserving profile B used by the current B.16 benchmark. The archived JSON records profile SHA-256:

`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

Configuration is unchanged from the prior diagnostic: (N_r=40), (N_\omega=100), (N_\theta=16), (N_s=32), (R_{\max}=25\) km; masses (m_V=0.1,1,10\) MeV. The 10 MeV result is:

| Fig. 7 point | Fixed-\(\omega\) baseline | Path-redshift-only |
|---|---:|---:|
| Weak endpoint | -8.8853% | -8.8991% |
| Reference peak | +2.5688% | -2.7704% |
| Strong endpoint | +92.2406% | +36.7448% |
| Strong-endpoint shift relative to fixed-\(\omega\) | 0 | -28.8679% |

At the strong endpoint, the fixed-\(\omega\) escape fraction is (3.23921\times10^{-4}), while the path-redshift-only value is (2.30412\times10^{-4}). The optically thin source is held fixed between the two prescriptions.

The current-profile output is archived at:

`outputs/b16_global_redshift_audit_2026-11-09.json`

GitHub Actions [Run #42568420651](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42568420651) passed the global-integral regression tests, the three-mass radial-weight/fixed-energy/path-redshift calculation, the production-output immutability check, and the archive step.

A second, simultaneously queued duplicate run (#42568424558) also completed its numerical calculation and tests, but its archive step encountered an add/add conflict because the first run had already archived the same dated output. The successful first run and its committed JSON are the authoritative record; the duplicate archive conflict does not indicate a numerical failure.

This closes the profile-provenance gap for the redshift-only sensitivity result. It does not change the interpretation: the path-redshift result remains a diagnostic with Euclidean path measure, not full GR, and the fixed-\(\omega\) Appendix-B branch remains the paper-reproduction baseline.
