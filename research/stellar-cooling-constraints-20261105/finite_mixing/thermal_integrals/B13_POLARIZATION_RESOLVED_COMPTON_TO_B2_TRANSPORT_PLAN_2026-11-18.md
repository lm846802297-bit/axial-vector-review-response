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

The \(+\) and \(-\) rates agree to better than \(3\times10^{-16}\) at this anchor. All three points pass the successive-order quadrature criterion of \(10^{-3}\).

The low-order full-radial screen indicates that this polarization splitting is also radial dependent. At \(x=0.05\), its preliminary \(R_{LT}\) range is 0.77298--0.97325 across the profile, with the strongest suppression near 8.25 km and weaker suppression toward 25 km. The full-radial high-order scan is being run to replace this low-order estimate. At the 8.2482 km anchor, the low-order full-radial screen differs from the high-order \(R_{LT}\) result by 0.24--0.28% over the three tested \(x\) values, so the low-order radial envelope is a screening result rather than the final high-order profile.

## 3. Correct channel combination for B.2

For each physical polarization \(h\), the local total reduced absorption must be assembled channel by channel:

\[
\widetilde\Gamma_{\rm abs,h}^{\rm tot}(r,\omega)
=
\widetilde\Gamma_{\rm abs,h}^{\nu\bar\nu\to A'}(r,\omega)
+
\widetilde\Gamma_{\rm abs,h}^{\mu\gamma\to\mu A'}(r,\omega)
+
\widetilde\Gamma_{\rm abs,h}^{\rm other}(r,\omega).
\]

For the 10 MeV benchmark, the dimuon decay channel is kinematically closed because \(m_{A'}<2m_\mu\). The Compton term is to be taken directly from the B.13 moving-muon calculation, summed over \(\mu^-\) and \(\mu^+\) but **not** summed or equally split over \(L,+,-\).

At the source, the corresponding per-mode production is

\[
\Gamma_{\rm prod,h}^{\rm tot}
=
\Gamma_{\rm prod,h}^{\nu\bar\nu\to A'}
+
\Gamma_{\rm prod,h}^{\mu\gamma\to\mu A'}.
\]

The B.13 kernel already supplies charge-resolved production and absorption. Detailed balance is checked per charge and per mode; reduced absorption is reconstructed using

\[
\widetilde\Gamma_{\rm abs,h}
=
\left(1-e^{-\omega/T}\right)\Gamma_{\rm abs,h}.
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
