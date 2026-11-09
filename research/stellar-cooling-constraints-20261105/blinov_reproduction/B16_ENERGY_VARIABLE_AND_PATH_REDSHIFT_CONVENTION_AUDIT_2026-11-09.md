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
