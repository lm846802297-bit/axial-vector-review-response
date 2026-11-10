# P1-C polarization normalization and global mode-resolved transport (2026-11-10)

**PR:** #57  
**Branch:** \`research/moving-muon-thermal-rates-20261107\`  
**Benchmark:** \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
**Profile:** vertex-preserving SFHo-18.8 reconstruction, SHA-256  
\`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Polarization normalization from the published equations

Write the three polarization weights in the two-body decay kinematics as
\[
W_L(z)=\frac34(1-z^2),\qquad
W_+(z)=\frac38(1+z)^2,\qquad
W_-(z)=\frac38(1-z)^2.
\]
They satisfy
\[
\int_{-1}^{1}W_h(z)\,dz=1,\qquad
W_L+W_++W_-=\frac32.
\]
For one neutrino flavour, the mode-resolved production rate per \(g^2\) is
\[
\Gamma^{\rm prod}_h(\omega)
=\frac{m_V^2}{24\pi\omega}
\int_{-1}^{1}dz\,W_h(z)
f_\nu(E_1)f_{\bar\nu}(E_2).
\]
Summing the three modes gives
\[
\sum_h\Gamma^{\rm prod}_h
=\frac{m_V^2}{8\pi\omega}
\left[\frac12\int_{-1}^{1}dz\,
f_\nu(E_1)f_{\bar\nu}(E_2)\right],
\]
which is the scalar B.7 normalization used by the current B.1 implementation. The same sum is taken over the \(\nu_\mu\) and \(\nu_\tau\) flavours.

Detailed balance holds mode by mode:
\[
\Gamma^{\rm prod}_h=e^{-\omega/T}\Gamma^{\rm abs}_h,
\qquad
\Gamma_h^*=(1-e^{-\omega/T})\Gamma_h^{\rm abs}
=(e^{\omega/T}-1)\Gamma_h^{\rm prod}.
\]
Summing this relation gives the scalar reduced opacity
\[
\Gamma_{\rm abs}^{*,\rm sum}=\sum_h\Gamma_h^*.
\]

The published Appendix B carries the polarization sum through its production expression, corresponding absorption expression, and detailed-balance relation. Under that literal equation chain, the \(\Gamma_{\rm abs}\) entering Eq. (B.2) is the polarization-summed scalar rate. The current scalar B.2 code therefore matches the literal published normalization. **There is no basis for inserting or removing a factor of three in the scalar reproduction code.**

This does not make scalar transport equivalent to independent propagation of the three modes. If the modes propagate separately, the escaped luminosity is
\[
L_{\rm esc}^{\rm mode}\propto
\sum_h\Gamma_h^{\rm prod}
\left\langle e^{-\tau_h}\right\rangle,
\]
which is not the same as
\[
\left\langle e^{-\sum_h\tau_h}\right\rangle
\quad\text{or}\quad
\left\langle e^{-\sum_h\tau_h/3}\right\rangle.
\]
The scalar Eq. (B.2) prescription and mode-resolved transport are distinct approximations.

## 2. Correcting the Compton split in the mode-resolved diagnostic

The earlier global mode-resolved diagnostic split the scalar B.14 Compton source and opacity equally among \(L,+,-\). That was a convenient closure, but it is not the mode decomposition implied by the B.14 no-recoil Thomson-limit inverse cross sections.

The mode weights following from those cross sections are
\[
w_L(\omega)=\frac{m_V^2/\omega^2}{2+m_V^2/\omega^2},
\qquad
w_+(\omega)=w_-(\omega)=
\frac{1}{2+m_V^2/\omega^2}.
\]
They sum to one and are applied identically to the Compton source and opacity, as required by detailed balance. In the 210--510 MeV band:
- at 210 MeV, \(w_L=0.1133\%\);
- at 300 MeV, \(w_L=0.0555\%\);
- at 510 MeV, \(w_L=0.0192\%\).

Thus the B.14 Compton channel is almost entirely transverse in this high-energy band. The equal-third split is not the appropriate B.14 mode decomposition.

## 3. Direct global high-energy calculation

The V8 binary64 calculation uses:
\[
(N_r,N_{\rm opacity},N_E,N_\theta,N_s,N_z,N_p)
=(200,642,842,32,64,64,128),
\]
where \(N_z\) is the neutrino two-body angular quadrature and \(N_p\) is the muon-susceptibility momentum quadrature. The 210--510 MeV band contains ten energy nodes. The source and scalar opacity close against the archived scalar result at relative residuals \(2.22\times10^{-16}\) and \(6.66\times10^{-16}\), respectively.

| Transport prescription | Escaped luminosity (erg/s) | Escape fraction | Ratio to scalar B.2 |
|---|---:|---:|---:|
| Literal scalar polarization sum | \(1.701785\times10^{52}\) | \(2.34580\times10^{-3}\) | 1 |
| Mode resolved, B.14 Compton weights | \(6.615829\times10^{53}\) | \(9.11949\times10^{-2}\) | **38.88** |
| Mode resolved, equal Compton thirds (old diagnostic) | \(6.975075\times10^{53}\) | \(9.61469\times10^{-2}\) | 40.99 |
| Scalar average opacity \(\sum_h\tau_h/3\) | \(6.972998\times10^{53}\) | \(9.61183\times10^{-2}\) | 40.97 |

The B.14-weighted mode-resolved luminosity is distributed as 27.41% longitudinal, 36.34% \(+\), and 36.25% \(-\). The mode-specific source-weighted mean optical depths per \(g^2\) are:

| Channel | \(L\) | \(+\) | \(-\) |
|---|---:|---:|---:|
| Neutrino inverse decay | \(1.18683\times10^{15}\) | \(1.08717\times10^{15}\) | \(1.12298\times10^{15}\) |
| Semi-Compton | \(8.24\times10^{11}\) | \(5.18913\times10^{14}\) | \(5.18913\times10^{14}\) |

The large difference between scalar and mode-resolved luminosities is caused by the exponential survival factor: the scalar exponent uses the sum of the three mode opacities, whereas each mode-resolved trajectory uses only its own opacity. The result is not a small normalization correction.

**Crucially, the mode-resolved treatment increases the high-energy escaped luminosity by a factor of 38.9.** Since the current scalar strong-endpoint result is already too bright relative to Fig. 7, this alternative moves in the wrong direction and cannot explain the existing \(+92.2406\%\) residual.

## 4. P1-C decision

1. The literal B.2 scalar implementation uses the polarization-summed opacity implied by the published B.6--B.10 equation chain. Do not change its factor-of-three normalization.
2. The mode-resolved calculation is a distinct transport prescription, not an algebraically equivalent rewriting of the scalar equation.
3. The improved B.14 Compton mode split is almost entirely transverse; it changes the earlier equal-split mode-resolved result by about 5.1%, but does not change the qualitative conclusion.
4. Mode-resolved propagation increases, rather than decreases, the high-energy escape luminosity. It does not solve the scalar Fig. 7 mismatch.
5. The literal scalar baseline, B.1 source, coupling, profile, Fig. 7 curve, and all axial-vector results remain unchanged.

**P1-C polarization-normalization audit: complete for the published scalar equation mapping and the 210--510 MeV global mode-resolved diagnostic.**

## 5. Next targeted B.2 check

The next useful physical sensitivity is the outer boundary \(R_{\max}=R_\nu\simeq25\) km. Quantify how the source-frozen high-energy escape integral changes when the absorbing/trapping boundary is moved inward within the reconstructed profile, and separately estimate the extra optical depth that would accrue if the neutrino-trapping boundary were farther out. Keep \(R_\nu=25\) km as the literal paper baseline; do not treat an extended-boundary stress test as a replacement without independent evidence for the energy-dependent neutrinosphere.


## Follow-up: P1-D outer-boundary audit completed (2026-11-10)

The targeted \(R_{\max}\) sensitivity requested above has now been calculated and archived in [B16_P1D_RMAX_BOUNDARY_SENSITIVITY_2026-11-10.md](B16_P1D_RMAX_BOUNDARY_SENSITIVITY_2026-11-10.md), with a reproducibility script and machine-readable output.

For the source-frozen 210--510 MeV band at the 10 MeV strong-endpoint point:
- \(R_{\max}=24\) km raises the escaped band luminosity by 28.84% relative to 25 km;
- \(R_{\max}=22\) km raises it by 116.06%;
- a conditional vacuum-limit neutrino-opacity extension to 26 km lowers it by 22.42%.

The 25 km paper prescription remains the baseline. The extension is conditional on continued neutrino trapping and is not adopted as a replacement. The next unresolved issue is the provenance/physical definition of the effective neutrinosphere radius for the exact SFHo-18.8 snapshot, not another increase in path quadrature order.
