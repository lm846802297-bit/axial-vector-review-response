# B.13 polarization-resolved Compton kernel: physical interpretation and B.2 handoff

**Date:** 2026-11-18  
**Benchmark:** \(m_{A'}=10\) MeV, \(g_V/g_X=1\), \(g_A/g_X=0\), SFHo-18.8 at \(t_{\rm pb}=1\) s.  
**Status:** local B.13 polarization calculation is validated at targeted high order; full radial three-anchor scan is in progress. No B.2 transport or luminosity is updated here.

## 1. What is being resolved

In the local medium rest frame, take the outgoing vector momentum along \(+z\),

\[
q^\mu=(\omega,0,0,k),\qquad k=\sqrt{\omega^2-m_{A'}^2}.
\]

The exact-recoil moving-muon Compton kernel returns three physical final-vector polarization rates, ordered as

\[
h=L,+,-,
\]

where \(L\) is the longitudinal mode and \(+,-\) are circular transverse modes. The kernel retains both target charges \(\mu^-\) and \(\mu^+\), Fermi blocking, photon Bose enhancement, and the exact final-muon mass shell. Rates are per \(g_X^2\) and per final-vector polarization.

For the pure-vector benchmark, the two transverse rates are equal to numerical precision. The longitudinal rate need not equal the transverse rate: the thermal medium selects a rest-frame four-velocity \(u^\mu\), so the current correlator has independent longitudinal and transverse projections relative to the spatial direction \(\mathbf q\). Equality of all three modes is recovered at the threshold \(k\to0\), where the momentum direction ceases to distinguish a longitudinal axis.

Define

\[
\overline\Gamma_T=\frac{\Gamma_++\Gamma_-}{2},\qquad
R_{LT}=\frac{\Gamma_L}{\overline\Gamma_T}.
\]

This ratio is a local polarization diagnostic; it is not itself the total opacity or an escape probability.

## 2. Current numerical evidence

The full low-order Global-06B screen covers 1687 profile radii and nine formal \(x\)-knots in \(0\le x\le0.05\), with eight independent energy-validation points per radius. Its maximum energy interpolation error is 0.06712%, and its top-60 radial midpoint error is 0.08311%. This is a low-order global screen, not a full high-order acceptance.

At the high-order anchor \(r=8.2482183145\) km, \(T=39.1873531264\) MeV, the direct B.13 result is:

| \(x=(\omega-m)/T\) | \(\omega\) (MeV) | \(R_{LT}\) | \(1-R_{LT}\) |
|---:|---:|---:|---:|
| 0 | 10.0000 | 1.000159 | -0.0159% |
| 0.015 | 10.5878 | 0.921539 | 7.846% |
| 0.05 | 11.9594 | 0.771126 | 22.887% |

The \(+\) and \(-\) rates agree to better than \(3\times10^{-16}\) at this anchor. All three points pass the successive-order quadrature criterion of \(10^{-3}\). **These quoted ratios are for the charge-summed \(\mu^-+\mu^+\) kernel output.** The like-for-like \(\mu^-\)-only ratios are retained separately in the charge-resolved data and must be used for comparison with the single-species B.17 reference.

The low-order full-radial screen indicates that this polarization splitting is also radial dependent. At \(x=0.05\), its preliminary \(R_{LT}\) range is 0.77298--0.97325 across the profile, with the strongest suppression near 8.25 km and weaker suppression toward 25 km. The full-radial high-order scan is being run to replace this low-order estimate. At the 8.2482 km anchor, the low-order full-radial screen differs from the high-order \(R_{LT}\) result by 0.24--0.28% over the three tested \(x\) values, so the low-order radial envelope is a screening result rather than the final high-order profile.

## 3. Correct channel combination for B.2

For each physical polarization \(h\) and each separately retained charge convention \(Q\), the local total reduced absorption is assembled channel by channel:

\[
\widetilde\Gamma_{\rm abs,h}^{\rm tot,Q}(r,\omega)
=
\widetilde\Gamma_{\rm abs,h}^{\nu\bar\nu\to A'}(r,\omega)
+
\widetilde\Gamma_{\rm abs,h}^{\mu\gamma,Q}(r,\omega)
+
\widetilde\Gamma_{\rm abs,h}^{\rm other}(r,\omega).
\]

For the 10 MeV benchmark, the dimuon decay channel is kinematically closed because \(m_{A'}<2m_\mu\). The primary like-for-like B.13 lane takes the \(\mu^-\) component only, matching the one-species B.17 convention. The \(\mu^-+\mu^+\) charge sum is a separate thermal-gas extension. In both lanes the Compton contribution is retained separately for \(L,+,-\); it is never divided equally among the three modes.

At the source, the corresponding per-mode production is

\[
\Gamma_{\rm prod,h}^{\rm tot,Q}
=
\Gamma_{\rm prod,h}^{\nu\bar\nu\to A'}
+
\Gamma_{\rm prod,h}^{\mu\gamma,Q}.
\]

The B.13 kernel supplies charge-resolved production and absorption. Detailed balance is checked per charge and per mode before the charge convention is selected. Reduced absorption is reconstructed using

\[
\widetilde\Gamma_{\rm abs,h}^{Q}
=
\left(1-e^{-\omega/T}\right)\Gamma_{\rm abs,h}^{Q}.
\]

This avoids an inconsistent shortcut in which a polarization-summed Compton rate is divided by three. The old equal-thirds transport result remains a diagnostic comparison only.

## 4. Energy and radial interpolation requirements

The local kernel is tabulated in

\[
x=\frac{\omega_{\rm loc}-m_{A'}}{T(r)},
\]

not in a radius-independent energy variable. For a fixed-energy or redshifted ray, first compute the appropriate local \(\omega(r)\), then map to \(x(r)\), and interpolate each charge/mode absorption channel consistently. Do not reuse a single \(x\) at all radii.

The low-x screen is restricted to \(0\le x\le0.05\). It cannot by itself supply the full B.1 source or the full B.2 optical depth over the complete energy domain. High-energy B.13 coverage and the exact energy convention of the transport path must be retained.

## 5. Required gates before updating any luminosity

1. Finish the 1687-radius high-order B.13 scan at \(x=0,0.015,0.05\), with per-charge and per-mode outputs.
2. Confirm the threshold isotropy check \(R_{LT}\to1\), transverse equality, detailed balance, mass shell, positivity, and quadrature convergence.
3. Construct the complete mode-resolved B.13 opacity over the energy domain needed by the B.2 ray integral, not only the low-x band.
4. Combine it with the already mode-resolved neutrino inverse-decay opacity, preserving the same redshift/fixed-\(\omega\) convention and radial interpolation.
5. Integrate the mode-resolved optical depths and source contributions; compare with the literal scalar B.2 baseline and the previous equal-thirds/B.14 diagnostics.
6. Only after the vector benchmark passes should any axial-vector stellar-cooling curve be reconsidered.

Until these gates pass, do not update Fig. 7, the escaped luminosity, the SN1987A bound, or the axial-vector exclusion.


## 6. Exact software interface and state-counting contract

The implementation must combine two independent mode-resolved local kernels. For the same local \((r,\omega)\) and the same mode ordering \((L,+,-)\):

- The function `moving_muon_compton_rates(..., g_vector=1, g_axial=0)` supplies exact-recoil B.13 production and absorption arrays separately for \(\mu^-\) and \(\mu^+\), as well as their sum. Its `charge_resolved` member must be retained. The **primary like-for-like lane** uses the \(\mu^-\) component alone, matching the single negative-muon distribution in the printed B.17 prescription. The \(\mu^-+\mu^+\) result is a separately labeled charge-summed thermal-gas extension; it must never be silently substituted for the one-species reference.
- The function `rates.neutrino_rates(m,\omega,T,\mu_{\nu_\mu})` supplies the \(\nu_\mu+\nu_\tau\) inverse-decay production and absorption arrays. It already returns the three physical polarization modes.

The no-mixing physical lane is assembled directly as

\[
\Gamma_{\mathrm{prod},h}^{\mathrm{tot},Q}
=\Gamma_{\mathrm{prod},h}^{\nu\bar\nu}
+\Gamma_{\mathrm{prod},h}^{\mu\gamma,Q},\qquad
Q\in\{\mu^-,\;\mu^-+\mu^+\},
\]

\[
\boxed{
\widetilde\Gamma_{\mathrm{abs},h}^{\mathrm{tot},Q}
=(1-e^{-\omega/T})
\left[
\Gamma_{\mathrm{abs},h}^{\nu\bar\nu}
+\Gamma_{\mathrm{abs},h}^{\mu\gamma,Q}
\right].
}
\]

The local B.13 rates are per \(g_X^2\); the coupling factor is applied once in the ray exponent and once in the luminosity normalization. Do not multiply the local rates by \(g_X^2\) and then multiply by \(g_X^2\) again downstream.

For each mode, the ray optical depth is

\[
\tau_h^Q(r,\omega,\mu)
=\frac{g_X^2}{v_{A'}}
\int_{\mathrm{ray}(r,\mu)} ds\,
\widetilde\Gamma_{\mathrm{abs},h}^{\mathrm{tot}}
\bigl(r(s),\omega_{\mathrm{loc}}(s)\bigr),
\]

with the existing unit conversion and the already-selected fixed-\(\omega\) or redshifted-energy prescription applied consistently. The escaped no-mixing luminosity is the sum of the three separately propagated mode sources,

\[
L_\infty^{\mathrm{no\ mix},Q}
=g_X^2\sum_{h=L,+,-}
\int d\mathcal P\,
\Gamma_{\mathrm{prod},h}^{\mathrm{tot},Q}
\,e^{-\tau_h}.
\]

Here \(d\mathcal P\) denotes the same B.1 radial, energy, phase-space, and lapse measure used by the scalar reference. This is a transport prescription, not a claim that the three modes have equal populations.

**Do not construct the B.13 mode opacity by subtracting the neutrino sum from the scalar B.16 result and dividing the remainder by three.** That operation recovers the old polarization-summed B.14--B.16 Compton approximation, not the exact B.13 mode rates. It remains valid only inside the old equal-thirds diagnostic lane.

Keep the following four outputs distinct:

| Lane | Compton input | Attenuation |
|---|---|---|
| Literal published scalar reference | Original B.14--B.16 scalar rate | Unmodified scalar B.2 exponent |
| Exact B.13, \(\mu^-\)-only, no mixing | Direct \(\mu^-\) B.13 \(L,+,-\) rates | Three independent \(e^{-\tau_h}\) factors |
| Exact B.13, \(\mu^-+\mu^+\), no mixing | Charge-summed B.13 \(L,+,-\) rates | Separate charge-summed extension with three independent \(e^{-\tau_h}\) factors |
| Equal-occupation closure | Direct B.13 mode rates summed over modes | \(\sum_h\widetilde\Gamma_h^*/3\), only if an explicit rapid-mixing/equal-occupation assumption is adopted |

The scalar reference is never overwritten by either alternative lane. The B.13 no-mixing result is not required to reproduce the B.14--B.16 Fig. 7 curve because it changes the local Compton physics as well as the polarization transport prescription.

## 7. Acceptance tests for the B.13-to-B.2 adapter

Before any global luminosity run, the adapter must pass all of the following at identical \((r,\omega)\) points:

1. **Mode ordering:** both kernels use exactly \((L,+,-)\); no hidden permutation.
2. **Charge closure:** \(\Gamma^{\mu\gamma}_{h}=\Gamma^{\mu^-\gamma}_{h}+\Gamma^{\mu^+\gamma}_{h}\) for each mode and for production and absorption. Retain the \(\mu^-\)-only and \(\mu^-+\mu^+\) transport lanes separately.
3. **Neutrino closure:** sum of the three mode rates agrees with the independently retained polarization-summed neutrino rate to numerical precision.
4. **Detailed balance:** test production/absorption separately for each channel, charge, and polarization before combining channels.
5. **Reduced-opacity identity:** reconstruct \((1-e^{-\omega/T})\Gamma_{\rm abs,h}\) independently and compare with the sum of channel-wise reduced opacities.
6. **Positivity and finiteness:** all per-charge and per-mode production, absorption, and reduced-absorption rates are finite and nonnegative.
7. **Threshold symmetry:** \(\Gamma_L/[(\Gamma_++\Gamma_-)/2]\to1\) as \(k\to0\); transverse equality is checked separately.
8. **Interpolation:** interpolate each positive charge/mode channel in the audited thermal coordinate \(x\), then reconstruct production and reduced absorption using exact detailed balance. Never interpolate a polarization ratio alone.
9. **Transport convention:** the same local-energy convention is used in source evaluation and along every opacity ray; the current fixed-\(\omega\) baseline and the redshifted diagnostic remain separate.
10. **State counting:** no-mixing attenuation has no factor \(1/3\); the factor \(1/3\) appears only in the explicitly separate equal-occupation closure.

Only after these tests pass over the complete energy domain and the radial path should the B.13 no-mixing B.2 calculation be run. The present three-anchor scan is a local-kernel polarization study and does not satisfy this global transport gate.
