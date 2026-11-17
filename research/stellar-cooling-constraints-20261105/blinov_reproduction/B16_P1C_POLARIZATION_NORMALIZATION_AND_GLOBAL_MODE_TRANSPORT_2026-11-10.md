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

1. The B.6--B.7 production normalization and B.10 sum-to-sum detailed-balance identity do not justify inserting another factor of three into the local summed rate. However, Eq. (B.2) inserts a single scalar \(\Gamma_{\rm abs}^{*}\) into the ray exponent without specifying whether it is a sum over incident vector polarizations, an average over the three incident states, or shorthand for a polarization closure. Preserve the literal scalar B.2 implementation as the equation-level reproduction lane, but do not claim that its exponent is unambiguously a per-mode attenuation rate or that the paper definitely contains a factor-of-three error.
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


## 6. Independent review qualification (2026-11-15)

### 6.1 B.2 state-counting interpretation

The later analytic Boltzmann audit, B2_POLARIZATION_BOLTZMANN_STATE_COUNTING_AUDIT_2026-11-13.md, narrows the interpretation stated in the original P1-C decision. The factor of three in B.7 converts the polarization-averaged vacuum width into the polarization-summed thermal production rate. Under the B.6 spin-sum convention, B.10 is sum-to-sum detailed balance and does not introduce another factor of three.

The remaining ambiguity is specifically in B.2: the paper inserts one scalar \(\Gamma_{\rm abs}^{*}\) into the ray exponent but does not state whether this is the sum over incident vector polarizations, the arithmetic average over three states, or shorthand for an assumed polarization closure. The literal B.2 numerical lane must remain unchanged, but its scalar exponent must not be described as an unambiguously per-mode physical attenuation rate. This is an interpretation qualification, not evidence that the published calculation definitely has a factor-of-three error.

Keep three distinct lanes: (i) literal scalar equation-level reproduction; (ii) no-mixing propagation with a separate \(\tau_h\) for each mode; and (iii) equal-occupation average-opacity closure, only when its population/mixing assumption is explicit.

### 6.2 Later exact-B.13 comparison

The archived P1-C mode result is specifically a 210--510 MeV band calculation using B.14 no-recoil Thomson-limit Compton weights:

- B.16 literal scalar band: \(1.7017848288\times10^{52}\) erg/s;
- B.14 mode-resolved band: \(6.6158287761\times10^{53}\) erg/s;
- ratio: 38.8758.

The later exact-B.13 moving-muon calculation in results/P1B_B2_EXACT_B13_2026-11-14/ provides a like-for-like B.16 closure at \(1.7017848289\times10^{52}\) erg/s (relative residual \(-1.01\times10^{-7}\)). With both muon charges included, it obtains \(2.1001262\times10^{52}\) erg/s for the B.13 scalar-sum prescription and \(6.05812455\times10^{53}\) erg/s for independent mode-resolved transport. The latter is 35.5987 times the B.16 scalar band, not a universal correction factor.

The exact-B.13 and B.14 mode splits applied to the same B.13 scalar Compton source change the mode-resolved luminosity by only 0.0024%; the roughly 8.4% difference from the archived P1-C B.14 mode result is driven primarily by the overall recoil-resolved Compton source/opacity, not by the detailed polarization split. The exact-B.13 global result remains restricted to 210--510 MeV. Its low-x interpolation pilot is incomplete, so it is not a full-band Fig. 7 reproduction.

### 6.3 Producer/source provenance

The archived P1-C JSON identifies a direct V8 binary64 calculation. The checked-in Python driver audit_b16_global_polarization_transport_b14_split.py is a separate implementation: its default output filename differs from the archived P1-C filename, and its output schema (profile, fig7_reference_sha256, metrics_vs_fig7, points) differs from the archived V8 schema (calculation, equation_normalization, source_closure, results). It must not be represented as the exact producer of the archived JSON. The algebraic tests in polarization_boltzmann_state_counting.py validate state-counting identities, not the full P1-C radial/energy/angle integration.

The archived numbers remain useful, inspectable evidence with a closed B.16 scalar-band reference, but the exact V8 producer source/invocation is not present in this tree. A future reproducibility closure should archive that producer or regenerate a separately named output from the Python driver and compare it explicitly.

**Review disposition: PASS_WITH_NOTES.** The B.14 calculation remains a valid restricted-band diagnostic; the B.2 scalar-opacity interpretation and the producer provenance are now qualified. No source, opacity, coupling, transport output, Fig. 7 curve, or axial-vector constraint is changed.
