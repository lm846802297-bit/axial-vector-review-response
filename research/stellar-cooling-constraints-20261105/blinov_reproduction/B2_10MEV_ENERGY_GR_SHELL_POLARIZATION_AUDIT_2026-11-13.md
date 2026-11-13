# 10 MeV B.2 follow-up: energy, GR geometry, shells, high-energy escape and polarization

**Date:** 2026-11-13  
**Benchmark:** \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
**Fig. 7 reference:** \(1.26781475907372\times10^{52}\) erg/s  
**Profile SHA-256:** \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## Executive decision

1. B.1 local source energy and \(E_\infty\) are exactly equivalent by a change of variables; independent channel integrations agree at stored precision.
2. B.2 fixed-\(\omega\) and conserved-\(E_\infty\) path prescriptions are distinct. The redshift-only variant lowers the 10 MeV strong-endpoint residual from +92.43% to +36.91%, but it is not the literal printed B.2 formula.
3. A general static-spherical GR geodesic/opacity kernel is implemented and six tests pass. The public-figure SFHo-18.8 profile has no same-snapshot \(B(r)=\sqrt{g_{rr}}\) or enclosed-mass profile, so no physical full-GR result is claimed. The Garching pseudo-Newtonian model used by the published calculation explicitly adopts flat spatial coordinates; \(B=1\) and Euclidean chords are the paper-level geometry.
4. 56.71% of the source-weighted mean total optical depth accumulates at \(r\ge15\) km. The 15--22 km group contributes 39.34 percentage points and 22--25 km another 17.37.
5. 110--510 MeV contributes 94.43% of escaped luminosity while containing only 43.28% of the thin source; 210--510 MeV alone contributes 69.76%.
6. Local \(L,+,-\) sums and detailed balance pass. Scalar-sum and independent mode-resolved transport are not interchangeable; keep them as separate reproduction and physical-transport lanes.

No opacity multiplier, source rescaling, mass scan expansion, or axial-vector curve update is made.

## 1. B.1 energy-variable audit

The printed B.1 integral uses local energy at the source, with \(\omega_{\min}=m_V/N(r)\). Set
\[
E_\infty=N(r)\omega_{\rm loc},\quad
k_{\rm loc}=\frac{\sqrt{E_\infty^2-N^2m_V^2}}{N},\quad
d\omega_{\rm loc}=\frac{dE_\infty}{N}.
\]
Then
\[
N^2k_{\rm loc}\omega_{\rm loc}^2d\omega_{\rm loc}
=\frac{E_\infty^2\sqrt{E_\infty^2-N^2m_V^2}}{N^2}\,dE_\infty.
\]
The lower limit becomes \(E_\infty=m_V\), and the local rate is evaluated at \(E_\infty/N(r)\). The independent numerical integrations agree channel by channel:
- neutrino inverse decay: \(2.924014280393587\times10^{70}\) erg s\(^{-1}\) per \(g^2\);
- semi-Compton: \(1.3803538885385007\times10^{70}\) erg s\(^{-1}\) per \(g^2\);
- total: \(4.304368168932088\times10^{70}\) erg s\(^{-1}\) per \(g^2\).

Thus B.1 has no remaining physical energy-variable ambiguity.

## 2. B.2 path-energy convention

The printed B.2 expression uses the same \(\omega\) along the Euclidean chord:
\[
\tau=\int_0^{s_{\max}}ds\,
\frac{\Gamma_{\rm abs}^*(r'(s),\omega)}{v_V(\omega)}.
\]
The main text describes \(\omega\) as energy at spatial infinity, while the B.1 printed integral is in local source energy. B.1 is reconciled by the Jacobian above; B.2 does not explicitly state whether its local collision kernel should use fixed \(\omega\) or \(E_\infty/N(r'(s))\).

For conserved Killing energy,
\[
\omega_{\rm loc}(s)=\omega_{\rm src}\frac{N(r_{\rm src})}{N(r'(s))}.
\]

| B.2 path convention | Luminosity | Residual vs Fig. 7 |
|---|---:|---:|
| Literal fixed-\(\omega\) | \(2.439635957\times10^{52}\) erg/s | +92.43% |
| Conserved-\(E_\infty\), redshift-only | \(1.735803372\times10^{52}\) erg/s | +36.91% |

The redshift-only result is 28.85% below the fixed-\(\omega\) result, but retains Euclidean chords and flat spatial measure. It is a sensitivity test, not a full GR ray trace or a replacement for the printed baseline. The authors' unpublished numerical implementation is needed to settle the notation ambiguity conclusively.

## 3. Full GR path geometry

Use
\[
ds^2=-N(r)^2dt^2+B(r)^2dr^2+r^2d\Omega^2,\qquad B=\sqrt{g_{rr}}.
\]
For a massive vector with conserved \(E_\infty,L\),
\[
\omega_{\rm loc}=E_\infty/N,\qquad
p_{\hat r}=\sqrt{\omega_{\rm loc}^2-m_V^2-L^2/r^2}.
\]
Then
\[
\frac{d\ell_{\rm loc}}{dr}=B\frac{k_{\rm loc}}{|p_{\hat r}|},\quad
\frac{d\phi}{dr}=B\frac{L}{r^2|p_{\hat r}|},\quad
\boxed{\frac{d\tau}{dr}=\Gamma_{\rm abs}^*(r,\omega_{\rm loc})B
\frac{\omega_{\rm loc}}{|p_{\hat r}|}}.
\]
Initially inward rays require a turning-point integration. \(E_\infty>m_V\) is necessary but does not by itself guarantee that a finite-angular-momentum ray reaches \(R_{\max}\).

For a Euclidean chord parameter \(s\), \(dr/ds=\mu_r\), the spatial proper increment would be
\[
d\ell=ds\sqrt{1+[B(r)^2-1]\mu_r^2},
\]
not generally \(Bds\). A true GR ray is geodesic, not a Euclidean chord. A complete GR source integral also requires \(dV_{\rm proper}=4\pi r^2B(r)dr\); changing only the path is a propagation extension, not a full GR luminosity.

The current 1687-row profile has columns \(r,T,\mu_\mu,\mu_{\nu_\mu},N\) and comparison fields, but no \(B(r)\), \(g_{rr}\), or \(M(r)\). The lapse alone does not determine the interior spatial metric. No synthetic TOV profile or lapse-only inference is used. Caputo et al., Supplemental Material C, explicitly state that the Garching pseudo-Newtonian model is interpreted with flat spatial coordinates and distant-observer time; therefore the published prescription uses flat spatial geometry. The new general GR kernel is retained for a future authorized same-snapshot metric input.

### Code validation

\`gr_ray_transport.py\` implements conserved-energy/angular-momentum propagation, radial turning points, proper path length, bending, and local-energy opacity evaluation. Six unit tests pass: flat radial path, inward/outward flat chords, tangential limit, Killing-energy redshift, bound-energy escape gate, and a Schwarzschild toy metric. The Schwarzschild test is only a code-validation toy model, not the SFHo-18.8 metric.

## 4. Radial path-shell decomposition

High-order source-weighted mean total optical-depth shares, including neutrino inverse decay and Compton:

| Path shell | Share of mean total \(\tau\) |
|---|---:|
| 0--5 km | 1.40% |
| 5--8 km | 6.36% |
| 8--10 km | 10.47% |
| 10--12 km | 10.59% |
| 12--15 km | 14.48% |
| 15--16.5 km | 7.85% |
| 16.5--18.5 km | 11.21% |
| 18.5--20 km | 8.70% |
| 20--22 km | 11.57% |
| 22--25 km | 17.37% |

The 15--22 km group contributes 39.34%; 22--25 km contributes 17.37%; together \(r\ge15\) km contributes 56.71%. A separate 8--15 km source, neutrino-only path audit gives 75.54% in 8--22 km and 19.07% in 22--25 km. These have different denominators and must not be averaged. Both show that the outer shell matters, but the combined 15--22 km path is larger.

These are optical-depth shares, not additive luminosity fractions; the survival factor is exponential.

## 5. High-energy escape

| Energy bin | Thin-source fraction | Escaped-luminosity fraction | Mean source-weighted \(\tau\) |
|---|---:|---:|---:|
| 60--110 MeV | 35.925% | 0.963% | 16.13 |
| 110--210 MeV | 33.611% | 24.674% | 11.08 |
| 210--510 MeV | 9.670% | 69.756% | 7.72 |
| 510--1010 MeV | 0.0214% | 1.170% | 4.76 |

The combined 110--510 MeV band supplies 43.28% of the thin source and 94.43% of escaped luminosity. Its source is 59.13% neutrino and 40.87% Compton; its escaped luminosity is 52.46% neutrino and 47.54% Compton.

The targeted high-energy neutrino B.2 chord test varied path order 32--256 and opacity radial grids 320--1280. The largest path refinement was below \(2.0\times10^{-5}\), and the final radial-grid refinement below \(9.4\times10^{-7}\). The dominant high-energy chord is numerically converged; the Fig. 7 discrepancy is not explained by under-resolved high-energy chord quadrature.

## 6. Scalar-sum versus mode-resolved propagation

Local closure results:
- production mode sum vs scalar rate: \(1.67\times10^{-14}\);
- absorption mode sum vs scalar rate: \(1.60\times10^{-14}\);
- mode-by-mode detailed balance: \(3.42\times10^{-14}\);
- integrated source mode-sum closure: \(6.29\times10^{-16}\);
- integrated reduced-opacity mode-sum closure: \(1.10\times10^{-12}\).

At \(r=12\) km, \(\omega=300\) MeV, the neutrino source fractions are \((L,+,-)=(35.61,31.89,32.51)\%\). The B.14 no-recoil Compton weights are \(w_L=5.55\times10^{-4}\), \(w_+=w_-=0.499722\); this is not a full recoil-resolved polarization kernel.

The exact mode-resolved escape is
\[
L_{\rm esc}^{\rm mode}=\sum_h\int d\Pi\,Q_h e^{-\tau_h},
\]
not \((\sum_hQ_h)e^{-\sum_h\tau_h}\). The current diagnostic gives:
- literal scalar B.2: \(2.43964\times10^{52}\) erg/s;
- independent \(L,+,-\) propagation with B.14 Compton weights: \(1.86306\times10^{54}\) erg/s, 76.37 times the scalar result.

This is not a correction factor. It is a different transport prescription.

The printed equations explicitly sum vector polarizations in B.6; B.7 has a factor of three because the vacuum width is averaged over initial vector polarizations while thermal production is summed; B.10 gives detailed balance without another factor of three. A literal reading therefore suggests a polarization-summed \(\Gamma_{\rm abs}\). But an opacity in a single-particle attenuation exponent should be per occupied mode or a properly source-weighted effective rate. B.2 does not explicitly state the polarization averaging convention. This is a real normalization ambiguity in the paper-level transport prescription.

**Decision:** retain scalar B.2 for equation-level Fig. 7 reproduction; use mode-resolved attenuation for physical transport of incoherent polarization eigenmodes; do not silently substitute one for the other. Replace the approximate B.14 Compton split with a recoil-resolved polarization kernel before treating the mode-resolved luminosity as final.

## 7. Disposition

| Item | Status |
|---|---|
| B.1 energy variable | Passed, exact Jacobian |
| B.2 path energy | Quantified; fixed-\(\omega\) remains literal baseline |
| Full GR path metric | Generic solver tested; physical \(B(r)\) unavailable; paper model is spatially flat |
| Outer shells | Quantified; 15--25 km is important |
| High-energy escape | Quantified; 110--510 MeV dominates escape |
| Polarization | Local rates pass; scalar/mode transport ambiguity remains |

The pure-vector Fig. 7 gate remains **not passed**. The axial-vector curve is unchanged. The next calculation is a per-mode collision-term normalization derivation plus an exact Compton polarization kernel, not another broad mass scan.

## References

- Blinov et al., JHEP 06 (2026) 155, Sec. 4.1 and Appendix B. https://doi.org/10.1007/JHEP06(2026)155
- Caputo et al., PRL 128 (2022) 221103, Supplemental Material C, arXiv:2201.09890. https://arxiv.org/abs/2201.09890
- Caputo, Raffelt and Vitagliano, JCAP 08 (2022) 045, Eqs. (4.22)--(4.24), arXiv:2204.11862. https://arxiv.org/abs/2204.11862


## 8. P0 Boltzmann state-counting follow-up — 2026-11-13

The analytic follow-up is archived in [B2_POLARIZATION_BOLTZMANN_STATE_COUNTING_AUDIT_2026-11-13.md](B2_POLARIZATION_BOLTZMANN_STATE_COUNTING_AUDIT_2026-11-13.md).

For fixed mode \(h\), the collision term is
\[
C_h=\Gamma_{{\rm prod},h}(1+f_h)-\Gamma_{{\rm abs},h}f_h,
\qquad
\Gamma_{{\rm prod},h}=e^{-\omega/T}\Gamma_{{\rm abs},h}.
\]
Summing modes gives a closed scalar equation only after an occupation closure is specified. For equal occupations \(f_h=F/3\), the total absorption coefficient is the mode average \(\sum_h\Gamma_{{\rm abs},h}^{*}/3\). For unequal occupations it is the occupation-weighted rate \(\sum_h\Gamma_{{\rm abs},h}^{*}f_h/F\).

The B.6--B.10 printed equation chain remains sum-to-sum: B.7's factor of three converts the averaged vacuum width to the summed thermal production rate, and B.10 adds no further degeneracy factor. The literal scalar B.2 baseline is therefore retained unchanged for equation-level reproduction, while its interpretation as a per-particle opacity remains under-specified. Physical no-mixing propagation uses each \(\Gamma_{{\rm abs},h}^{*}\) separately.

Seven algebraic tests pass. This does not replace the exact B.13 Compton polarization kernel or close the Fig. 7 benchmark.
