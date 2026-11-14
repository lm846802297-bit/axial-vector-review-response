# B.2 polarization Boltzmann equation and state-counting audit

**Date:** 2026-11-13  
**PR:** #106  
**Benchmark context:** \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
**Scope:** analytic normalization audit; no new mass scan and no change to the literal scalar Fig. 7 reference.

## Executive conclusion

This addendum completes the missing Boltzmann-level state-counting step left open by the earlier P1-C polarization audit.

1. The mode-resolved collision equation is
   \[
   D f_h=\Gamma_{{\rm prod},h}(1+f_h)-\Gamma_{{\rm abs},h}f_h,
   \qquad h\in\{L,+,-\}.
   \]
2. Detailed balance holds mode by mode,
   \[
   \Gamma_{{\rm prod},h}=e^{-\omega/T}\Gamma_{{\rm abs},h},
   \]
   and therefore also holds after summing the three modes. The sum-to-sum relation has no additional factor of three.
3. The factor of three in Blinov et al. Eq. (B.7) converts the polarization-averaged vacuum decay width into the polarization-summed thermal production rate. It is not an extra factor to insert into Eq. (B.10).
4. If \(F=\sum_h f_h\) is the total occupation and the three modes are constrained to have equal occupation \(f_h=F/3\), the total absorption sink is governed by the arithmetic-average rate \(\sum_h\Gamma_{{\rm abs},h}/3\), not by the sum itself.
5. Without rapid polarization mixing, the exact transport problem is mode-resolved. A single scalar opacity is not a closed description when the three occupations or rates differ.
6. The literal scalar B.2 prescription is retained unchanged for equation-level Fig. 7 reproduction. Its polarization-summed exponent is not silently reinterpreted as a per-mode attenuation rate. Physical transport remains a separate mode-resolved lane.

This is a normalization and closure distinction, not a proposed empirical factor-of-three correction to the luminosity.

## 1. Mode-resolved collision integrals

For a fixed outgoing vector momentum \(k^\mu=(\omega,\mathbf k)\) and a fixed physical polarization \(h\), define the production rate for inverse neutrino decay by
\[
\begin{aligned}
\Gamma_{{\rm prod},h}(k)
={1\over 2\omega}\int d\Pi_1d\Pi_2\,
(2\pi)^4\delta^{(4)}(p_1+p_2-k)
\sum_{\rm bath\ spins}|{\cal M}_h|^2 f_1f_2,
\end{aligned}
\]
and the inverse-process absorption rate by
\[
\begin{aligned}
\Gamma_{{\rm abs},h}(k)
={1\over 2\omega}\int d\Pi_1d\Pi_2\,
(2\pi)^4\delta^{(4)}(p_1+p_2-k)
\sum_{\rm bath\ spins}|{\cal M}_h|^2
(1-f_1)(1-f_2).
\end{aligned}
\]
Here \(d\Pi_i=d^3p_i/[(2\pi)^3\,2E_i]\). The vector polarization \(h\) is fixed in each expression; the bath-fermion spins are summed. The rates include the same \(1/(2\omega)\) normalization and refer to the same local time coordinate.

The collision term for that one mode is therefore
\[
\boxed{
C_h[f_h]=\Gamma_{{\rm prod},h}(1+f_h)
-\Gamma_{{\rm abs},h}f_h.
}
\]

For neutrino and antineutrino distributions in thermal equilibrium, with chemical potentials \(\mu_\nu\) and \(-\mu_\nu\), energy conservation gives \(E_1+E_2=\omega\), and
\[
{f_1f_2\over(1-f_1)(1-f_2)}
=e^{-(E_1-\mu_\nu)/T}
 e^{-(E_2+\mu_\nu)/T}
=e^{-\omega/T}.
\]
The chemical potentials cancel. Since this relation holds pointwise in the phase-space integral,
\[
\boxed{
\Gamma_{{\rm prod},h}
=e^{-\omega/T}\Gamma_{{\rm abs},h}
}
\]
for each physical polarization separately.

Define the reduced absorption rate
\[
\Gamma_{{\rm abs},h}^{*}
=(1-e^{-\omega/T})\Gamma_{{\rm abs},h}.
\]
Then
\[
C_h[f_h]=\Gamma_{{\rm prod},h}
-\Gamma_{{\rm abs},h}^{*}f_h.
\]
This is the form that enters the attenuation exponent for a particle in mode \(h\), inside the region where the bath detailed-balance relation applies.

## 2. What happens when the three modes are summed?

Define
\[
\Gamma_{\rm prod}^{\Sigma}=\sum_h\Gamma_{{\rm prod},h},
\qquad
\Gamma_{\rm abs}^{\Sigma}=\sum_h\Gamma_{{\rm abs},h},
\qquad
F=\sum_h f_h.
\]
Summing the three exact collision equations gives
\[
D F
=\Gamma_{\rm prod}^{\Sigma}
+\sum_h\Gamma_{{\rm prod},h}f_h
-\sum_h\Gamma_{{\rm abs},h}f_h.
\]
This is the general result. It is not a closed equation for \(F\) alone unless an assumption about the mode occupations is supplied.

### Equal-occupation closure

If one imposes
\[
f_L=f_+=f_-={F\over3},
\]
then
\[
\boxed{
D F=
\Gamma_{\rm prod}^{\Sigma}\left(1+{F\over3}\right)
-{\Gamma_{\rm abs}^{\Sigma}\over3}F.
}
\]
Using summed detailed balance,
\[
\Gamma_{\rm prod}^{\Sigma}
=e^{-\omega/T}\Gamma_{\rm abs}^{\Sigma},
\]
this becomes
\[
\boxed{
D F=\Gamma_{\rm prod}^{\Sigma}
-{\Gamma_{\rm abs}^{*,\Sigma}\over3}F,
\qquad
\Gamma_{\rm abs}^{*,\Sigma}
=\sum_h\Gamma_{{\rm abs},h}^{*}.
}
\]
Thus the scalar attenuation rate for an equally populated three-state ensemble is the *average per-state opacity*,
\[
\bar\Gamma_{\rm abs}^{*}
={1\over3}\Gamma_{\rm abs}^{*,\Sigma}.
\]

This factor \(1/3\) has a precise meaning: it converts a sum over three initial vector states into the average rate acting on one member of an equally populated ensemble. It is not an extra factor in the sum-to-sum detailed-balance identity.

### Unequal mode populations

If the mode occupations are not equal, the effective absorption rate for the total population is
\[
\boxed{
\Gamma_{\rm eff}^{*}[f]
={\sum_h\Gamma_{{\rm abs},h}^{*}f_h
 \over \sum_h f_h}.
}
\]
This is occupation-weighted, not generally the arithmetic average. Since the modes can have different production and absorption rates, equal populations are not preserved by free propagation with negligible mode conversion. A scalar opacity therefore requires an explicit closure assumption; it does not follow from detailed balance alone.

## 3. Mapping to Blinov et al. Appendix B

The printed equation chain has the following state-counting structure.

| Equation / object | Polarization convention | Consequence |
|---|---|---|
| B.6 | Explicit sum over initial and final spin states | Thermal production is summed over the three final vector polarizations |
| B.7 | Uses \(3\Gamma_{V\to\bar\nu\nu}\) | Converts the vacuum width averaged over the three initial vector polarizations into the summed thermal production rate |
| B.10 | Detailed balance between the production and absorption rates | If both rates retain the B.6 spin-sum convention, the relation is sum-to-sum and has no additional factor of three |
| B.4 | \(\Gamma_{\rm abs}^{*}=(1-e^{-\omega/T})\Gamma_{\rm abs}\) | Preserves whichever polarization convention is assigned to \(\Gamma_{\rm abs}\) |
| B.2 | Inserts a scalar \(\Gamma_{\rm abs}^{*}\) into the ray exponent | Does not specify a polarization-density-matrix or equal-occupation closure |

The literal reading of B.6, B.7, and B.10 is therefore consistent with the polarization-summed local rates already implemented and tested. The existing scalar reference must not receive an ad hoc factor of three: doing so would no longer reproduce the printed equation chain.

There is, however, a separate physical interpretation issue. If the \(\Gamma_{\rm abs}\) passed from B.10 through B.4 into B.2 is indeed the summed rate, its direct use in a single-particle attenuation exponent is not the per-mode Boltzmann attenuation derived above. The paper does not spell out the intervening polarization average or mode-mixing closure. This is the precise ambiguity to retain in the audit record.

The safe disposition is:

- **Equation-level reproduction:** preserve the literal scalar B.2 implementation and its summed local opacity.
- **Physical no-mixing transport:** use \(\Gamma_{{\rm abs},h}^{*}\) in each mode's optical depth and sum the escaped mode luminosities.
- **Scalar averaged transport:** use \(\Gamma_{\rm abs}^{*,\Sigma}/3\) only when the equal-occupation closure is explicitly intended; do not claim it is exactly equivalent to mode-resolved transport when the modes have different opacities.

## 4. Propagation and the exponential nonlinearity

For a mode \(h\), the escape probability along a ray is
\[
P_h=\exp\left[-\int_{\rm ray}{ds\over v_V}
\Gamma_{{\rm abs},h}^{*}(r(s),\omega(s))\right]
=e^{-\tau_h}.
\]
The physical no-mixing luminosity is
\[
\boxed{
L_{\rm esc}^{\rm modes}
=\sum_h\int d\Pi\,\omega\,
\Gamma_{{\rm prod},h}e^{-\tau_h}.
}
\]
It is not
\[
\left(\sum_h Q_h\right)e^{-\sum_h\tau_h}.
\]
Even replacing the summed opacity by its one-third average does not in general reproduce the mode sum:
\[
\sum_h Q_he^{-\tau_h}
\ne
\left(\sum_hQ_h\right)
e^{-\frac13\sum_h\tau_h}.
\]
The latter agrees in the special case \(\tau_L=\tau_+=\tau_-\), but not for general mode-dependent rates and source weights.

This explains why the current 76.37 ratio between the mode-resolved diagnostic and literal scalar B.2 cannot be interpreted as a missing factor of three. The factor of three is a state-counting relation at the rate level; the luminosity difference is generated after exponentiation and integration over source radius, energy, and direction.

## 5. Cross-check against the current 10 MeV numerical record

The PR #106 local-rate audit reports:

| Closure check | Maximum relative residual |
|---|---:|
| Neutrino production: \(L,+,-\) sum vs scalar | \(1.67\times10^{-14}\) |
| Neutrino absorption: \(L,+,-\) sum vs scalar | \(1.60\times10^{-14}\) |
| Mode-by-mode detailed balance | \(3.42\times10^{-14}\) |
| Integrated B.1 source mode-sum closure | \(6.29\times10^{-16}\) |
| Integrated reduced-opacity mode-sum closure | \(1.10\times10^{-12}\) |

These checks show that the local mode-resolved and scalar *summed* rates are mutually consistent. They do not establish that a summed opacity is the correct attenuation rate for one propagating mode.

At the fixed 10 MeV strong endpoint, the current B.2 audit records
\[
L_{\rm scalar}=2.43964\times10^{52}\ {\rm erg\,s^{-1}},
\]
and
\[
L_{\rm modes}=1.86306\times10^{54}\ {\rm erg\,s^{-1}},
\qquad
{L_{\rm modes}\over L_{\rm scalar}}=76.37.
\]
These are retained as two different transport prescriptions. No rescaling is inferred from their ratio.

## 6. Independent literature cross-check

Das, Ghosh and Puri, arXiv:2606.23769 (22 June 2026), write a separate Boltzmann equation for each polarization and obtain
\[
L_{Z'}=L_L+2L_T.
\]
They argue that the dark-Compton conversion process
\(\mu Z'_L\leftrightarrow\mu Z'_T\) is suppressed by an additional \(g'^2\) relative to production and absorption for their stated \(g'<0.1\) regime. This supports treating the three physical modes independently as a well-motivated low-coupling transport limit. It is an independent preprint, not a substitute for reproducing the Blinov calculation; its rate approximations and stellar inputs must not be mixed into the present benchmark.

Reference: https://arxiv.org/abs/2606.23769

## 7. P0 disposition and next gate

**P0 analytic state-counting derivation: completed.**

What is settled:

- The factor of three in B.7 is the vacuum-width average to thermal-production sum conversion.
- B.10 is sum-to-sum detailed balance under the printed B.6 spin-sum convention.
- A fixed polarization mode attenuates with its own \(\Gamma_{{\rm abs},h}^{*}\).
- An equal-population scalar closure uses the average \(\Gamma_{\rm abs}^{*,\Sigma}/3\).
- The literal B.2 scalar reference remains unchanged.

What remains open:

1. Verify whether the authors intended the B.2 opacity to be a summed rate, an unpolarized average, or a shorthand for a mode-averaged transport closure.
2. Replace the B.14 no-recoil Compton mode split with a full recoil-resolved B.13 polarization kernel.
3. Compare scalar-sum, equal-population-average, and independent-mode transport with identical background, energy frame, path, and quadrature.
4. Keep the pure-vector Fig. 7 gate and all axial-vector limits unchanged until the above comparison is accepted.

The analytic identities are implemented in polarization_boltzmann_state_counting.py and tested in test_polarization_boltzmann_state_counting.py. The tests verify collision-term summation, equilibrium detailed balance, occupancy-weighted absorption, and the distinction between mode-resolved and scalar exponential attenuation.
