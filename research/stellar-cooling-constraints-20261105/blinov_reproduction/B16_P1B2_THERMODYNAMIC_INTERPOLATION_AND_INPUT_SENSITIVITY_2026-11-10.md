# P1-B.2 thermodynamic interpolation and high-energy input sensitivity (2026-11-10)

**PR:** #57  
**Branch:** \`research/moving-muon-thermal-rates-20261107\`  
**Benchmark:** \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
**Profile:** vertex-preserving SFHo-18.8 reconstruction, SHA-256  
\`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Question

The P1 path/angle/radial-grid audit found no numerical integration error capable of explaining the fixed-\(\omega\) strong-endpoint residual. This follow-up asks two more specific questions:

1. Does linearly interpolating a precomputed opacity table differ materially from interpolating the underlying thermodynamic fields and evaluating the local B.16 kernel at the path point?
2. Which of the reconstructed local inputs \(T(r)\), \(\mu_{\nu_\mu}(r)\), and \(\mu_\mu(r)\) actually controls the high-energy B.2 propagation response in the important 8--15 km region?

The source is frozen in the sensitivity tests. Only the B.2 opacity is varied. The literal fixed-\(\omega\), scalar-opacity, Euclidean-chord prescription is retained throughout.

## 2. Opacity-table interpolation versus direct local-kernel evaluation

The current B.2 implementation precomputes the local reduced opacity on a 642-node radial grid and linearly interpolates that opacity along each chord. The alternative diagnostic instead interpolates \(T,\mu_{\nu_\mu},\mu_\mu\) from all 1687 retained profile vertices and recomputes the local B.16 kernel at every path node.

The 36-ray sample covers:
- source radii \(r_0=8,10,12.5,15\) km;
- energies \(\omega=210,300,510\) MeV;
- direction cosines \(\cos\theta=-0.75,0.25,0.75\).

Every chord is split at every radial crossing of the 1687-vertex profile. Four-point Gauss--Legendre integration is used per segment, with an independent eight-point path check. The muon susceptibility is evaluated with Gauss--Legendre integration over \(p\in[0,1200]\) MeV.

| Quantity | Maximum absolute relative difference: direct local kernel vs 642-node opacity interpolation |
|---|---:|
| Neutrino optical depth | \(1.13\times10^{-6}\) |
| Semi-Compton optical depth | \(1.432\times10^{-3}\) |
| Total optical depth | \(9.07\times10^{-6}\) |

The larger relative Compton-only difference is subdominant in the total optical depth for these rays. The direct-profile path integral itself is converged: the maximum GL4-to-GL8 relative change is \(5.66\times10^{-14}\) for the neutrino column, \(1.22\times10^{-13}\) for Compton, and \(3.73\times10^{-14}\) for the total.

The susceptibility quadrature is also converged at the sampled radii \(8,10,12.5,15,20,22,25\) km: GL96-to-GL128 differs by at most \(2.45\times10^{-15}\), and GL128-to-GL192 by at most \(1.45\times10^{-15}\).

**Result:** the opacity-table interpolation does not conceal a percent-level total B.2 propagation effect. Recomputing the local kernel from the thermodynamic fields changes the sampled total optical depth by at most \(9.07\times10^{-6}\).

## 3. Source-frozen global sensitivity of the 210--510 MeV B.2 band

The calculation uses the same high-order B.1 source weights and fixed-\(\omega\) B.2 integration as the archived high-energy result:
\[
(N_r,N_{\rm opacity},N_E,N_\theta,N_s)=(200,640,842,32,64).
\]
The 210--510 MeV band contains ten energy nodes. Its baseline optically-thin luminosity is \(7.25460048\times10^{54}\) erg/s, and its escaped luminosity is
\[
L_{\rm esc}^{\rm base}=1.70178483\times10^{52}\ {\rm erg/s}.
\]
The source fractions are 49.8764% neutrino inverse decay and 50.1236% semi-Compton. The source-weighted mean optical depths per \(g^2\) are \(3.39698\times10^{15}\) for neutrino inverse decay and \(1.03865\times10^{15}\) for semi-Compton.

Only the opacity inputs in \(8\leq r\leq15\) km are changed. The B.1 source weights, coupling, energy nodes, angular nodes, and path nodes remain fixed.

| B.2-only input variation in 8--15 km | Escaped luminosity (erg/s) | Change relative to baseline |
|---|---:|---:|
| Baseline | \(1.701785\times10^{52}\) | 0 |
| \(T\to0.9T\), \(\mu_\mu\) fixed | \(1.979068\times10^{52}\) | +16.2937% |
| \(T\to1.1T\), \(\mu_\mu\) fixed | \(1.440892\times10^{52}\) | -15.3306% |
| \(\mu_{\nu_\mu}\to0.9\mu_{\nu_\mu}\) | \(1.701384\times10^{52}\) | -0.02354% |
| \(\mu_{\nu_\mu}\to1.1\mu_{\nu_\mu}\) | \(1.702227\times10^{52}\) | +0.02598% |
| \(\mu_\mu\to0.9\mu_\mu\), \(T\) fixed | \(2.041284\times10^{52}\) | +19.9496% |
| \(\mu_\mu\to1.1\mu_\mu\), \(T\) fixed | \(1.380004\times10^{52}\) | -18.9084% |
| \(T,\mu_\mu\to0.9(T,\mu_\mu)\), fixed \(\mu_\mu/T\) | \(2.332265\times10^{52}\) | +37.0482% |
| \(T,\mu_\mu\to1.1(T,\mu_\mu)\), fixed \(\mu_\mu/T\) | \(1.151096\times10^{52}\) | -32.3595% |

The channel-resolved source-weighted mean optical depths show where the response comes from. The neutrino inverse-decay optical depth changes by less than about 0.74% under the temperature stress and by less than 0.02% under the \(\mu_{\nu_\mu}\) stress. The large luminosity response instead follows the semi-Compton optical depth: it changes from \(1.03865\times10^{15}\) at baseline to \(0.86431\) or \(1.23678\times10^{15}\) for the \(\mp10\%\) temperature tests, and to \(0.86466\) or \(1.24491\times10^{15}\) for the \(\mp10\%\) \(\mu_\mu\) tests. When \(T\) and \(\mu_\mu\) are varied together at fixed \(\mu_\mu/T\), the Compton mean optical depth changes to \(0.71261\) or \(1.46730\times10^{15}\).

**Interpretation:** the high-energy B.2 escape probability is sensitive to the inner semi-Compton opacity, even though the neutrino inverse-decay channel has the larger mean optical depth. The local \(\mu_{\nu_\mu}\) uncertainty is not the controlling input in this energy band.

## 4. Does the input sensitivity imply a plausible profile error?

No. The \(\pm10\%\) variations above are intentionally broad stress tests, not estimates of the actual profile uncertainty.

For the relevant SFHo-18.8, \(t_{\rm pb}=1\) s benchmark, the current Caputo reconstruction is independently compared with the original Bollig vector curves:
- \(T(r)\) versus Bollig Fig. 1 over 5--15 km: mean absolute relative difference \(0.00266\%\), maximum \(0.00990\%\);
- \(\mu_\mu/T\) versus Bollig Fig. 4 over 5--15 km: mean absolute relative difference \(0.00646\%\), maximum \(0.02127\%\).

The two source-level comparisons directly constrain the physically relevant coordinates \(T\) and \(\eta_\mu=\mu_\mu/T\). The local logarithmic response estimates from the controlled variations are
\[
\left.\frac{\partial\ln L_{\rm esc}}{\partial\ln T}\right|_{\mu_\mu}
\simeq-1.587,\qquad
\left.\frac{\partial\ln L_{\rm esc}}{\partial\ln\mu_\mu}\right|_T
\simeq-1.957,
\]
and
\[
\left.\frac{\partial\ln L_{\rm esc}}{\partial\ln T}\right|_{\eta_\mu}
\simeq-3.531.
\]
A first-order extrapolation of the maximum figure-level residuals gives response scales of about \(0.016\%\) from the \(T\) residual and \(0.042\%\) from the \(\eta_\mu\) residual; along the fixed-\(\eta_\mu\) direction the \(T\) residual corresponds to about \(0.035\%\). These are local linear estimates, not formal uncertainty bounds, but they are far below the \(+92.2406\%\) Fig. 7 discrepancy.

The \(\mu_{\nu_\mu}\) profile does not have an equally precise independent Bollig-figure cross-check. However, the present high-energy band changes by less than \(0.03\%\) under a \(\pm10\%\) variation of that input, consistent with the earlier negative- and positive-branch tests.

The Bollig Fig. 3 absolute muon-density tension must remain separate: B.17 uses the susceptibility \(n_\mu F_{\rm deg}\) determined by the same Fermi distribution, so the plotted density difference is not a justified standalone rescaling of the Compton opacity.

## 5. P1-B decision

1. The current 642-node opacity interpolation is numerically adequate for the sampled high-energy rays; direct local-kernel evaluation changes total \(\tau\) by at most \(9.07\times10^{-6}\).
2. The high-energy B.2 luminosity is locally sensitive to the inner semi-Compton opacity, but the baseline \(T\) and \(\mu_\mu/T\) profiles are independently anchored to Bollig Figs. 1 and 4 at the \(10^{-4}\) relative scale.
3. The \(\mu_{\nu_\mu}\) input is not a plausible source of an order-one high-energy propagation discrepancy within the tested variations.
4. No source, opacity, profile, coupling, Fig. 7 curve, or axial-vector output is modified. No empirical rescaling is applied.

**P1-B thermodynamic-input and interpolation audit: complete for the 210--510 MeV band and the targeted 8--15 km opacity-sensitive region.** The remaining high-impact B.2 question is the polarization normalization of the scalar absorption rate in the optical-depth exponent. That question must be resolved from the B.6--B.10 degeneracy and detailed-balance definitions; do not insert or remove a factor of three by matching Fig. 7.

## 6. Next targeted audit

Proceed to a normalization-only derivation:
1. distinguish a rate summed over the three outgoing vector polarizations from the absorption rate of one incoming vector polarization;
2. derive detailed balance for each \(L,+,-\) mode and for the unpolarized ensemble;
3. map those definitions onto the paper's scalar \(\Gamma_{\rm abs}\) in Eq. (B.2) and the explicit factor of three in Eq. (B.7);
4. verify whether the scalar opacity in the existing code is the sum, average, or per-mode rate, without assuming which one is physically or historically correct;
5. retain the literal published scalar baseline until the normalization map is established independently of Fig. 7.

The existing mode-resolved calculation is a diagnostic input to this derivation, not a substitute for it.


## 7. Superseding status update (2026-11-10)

The normalization-only follow-up described in §6 has since been addressed by the independent P1-C audit, \`B16_P1C_POLARIZATION_NORMALIZATION_AND_GLOBAL_MODE_TRANSPORT_2026-11-10.md\`. That audit explicitly distinguishes the polarization-summed production/absorption relation in the scalar Appendix-B prescription from the per-mode rates used in the diagnostic transport calculation. No factor-of-three rescaling is authorized for the literal Fig. 7 reproduction baseline.

The separate B.1 source sensitivity to \(\mu_{\nu_\mu}\) and the \(\mu_{\nu_\tau}=0\) assumption is now completed in \`B16_P1E2_B1_NEUTRINO_CHEMICAL_POTENTIAL_SOURCE_SENSITIVITY_2026-11-10.md\`. Its broad source-only stresses change the total B.1 source by at most about \(1.17\%\), and do not explain the weak-end deficit.

The next non-duplicative source-side task is the interior lapse sensitivity in the dominant 8--15 km emission region, as specified in the updated P1-E report.
