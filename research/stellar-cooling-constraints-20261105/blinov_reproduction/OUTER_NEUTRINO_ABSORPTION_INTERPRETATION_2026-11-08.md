# Outer neutrino absorption in the 10 MeV B.16 benchmark

**Status:** quantitative radial attribution completed; flavor-resolved opacity audit added.  
**Scope:** pure-vector B.14--B.16 baseline, m_V=10 MeV, reconstructed SFHo-18.8 profile at 1 s. All shell-removal results are diagnostic attributions, not physical alternate supernova models.

## 1. Radial-shell luminosity removal

The shell columns were independently integrated along every chord and checked against the direct Eq. (B.2) optical-depth integral. The maximum relative closure residual is \(6.72\times10^{-16}\). The detailed-balance channel sum closes to \(5.94\times10^{-16}\).

The source-weighted mean optical depth has the following channel decomposition:

| Channel | Mean optical depth |
|---|---:|
| Neutrino inverse decay | \(8.3245\times10^{15}\) |
| Semi-Compton | \(9.4779\times10^{14}\) |
| Dimuon inverse decay | 0 |

The shells at \(r\geq15\) km contribute 56.76% of the total source-weighted mean optical depth. This does not by itself quantify the luminosity suppression, because the escape probability is exponential. We therefore also remove each shell's opacity from the exponent while keeping the B.1 source fixed.

At the calculated luminosity peak, \(g=1.1341\times10^{-8}\), removing all opacity at \(r\geq15\) km increases the luminosity by a factor 1.756. Removing only the outer neutrino opacity gives 1.756 as well, whereas removing outer Compton opacity changes the luminosity by only \(9.0\times10^{-5}\) in relative terms.

At the strong-absorption endpoint, \(g=4.1717\times10^{-8}\), removing outer opacity increases the luminosity by a factor 114.1. Removing only outer neutrino opacity gives a factor 113.9; removing outer Compton opacity gives only 1.001. These large factors are sensitivity diagnostics in a region where the baseline luminosity is exponentially suppressed.

## 2. The neutrino channel contains both muon and tau flavors

The production implementation in reference.py evaluates
\[
\Gamma_{\nu,\mathrm{prod}}
=\frac{m_V^2}{8\pi\omega}
\left[
I\!\left(\frac{\mu_{\nu_\mu}}{T},\frac{\omega}{T},v_V\right)
+
I\!\left(0,\frac{\omega}{T},v_V\right)
\right].
\]
The first term is \(\nu_\mu\bar\nu_\mu\); the second is \(\nu_\tau\bar\nu_\tau\), with \(\mu_{\nu_\tau}=0\) as in Blinov et al. The tau-flavor term does not disappear when the outer muon-neutrino chemical potential is set to zero.

This explains why zeroing the outer \(\mu_{\nu_\mu}\) branch barely changes the luminosity: it changes only one flavor's occupation factor, while the tau-flavor inverse-decay channel remains.


## 2a. Flavor-resolved numerical result

The separate flavor integration reproduces the summed neutrino rate to a maximum relative residual of (2.81\times10^{-16}), and the sum of the two flavor-resolved path columns agrees with the direct total-neutrino column to (5.45\times10^{-16}).

| Contribution | Source-weighted mean optical depth |
|---|---:|
| (
u_muar
u_mu) | (4.1264\times10^{15}) |
| (
u_	auar
u_	au) | (4.1982\times10^{15}) |
| Both flavors | (8.3245\times10^{15}) |

For (r\geq15) km, the two flavors contribute almost exactly equally:
[
\langle\tau_{\nu_\mu}^{\rm outer}\rangle_Q
=2.6304\times10^{15},\qquad
\langle\tau_{\nu_\tau}^{\rm outer}\rangle_Q
=2.6316\times10^{15}.
]
Together they account for 56.75% of the all-channel source-weighted mean optical depth.

The outer flavor equality is also visible locally. At (r=18.5) km, (mu_{
u_\mu}/T=0.079); at (r\geq20) km the reconstructed profile has (mu_{
u_\mu}=0). The muon- and tau-neutrino reduced absorption rates are therefore equal to better than 0.1% at and beyond 18.5 km for the representative energies tested.

## 2b. Flavor-specific luminosity-removal test

The following factors are (L_{\rm without\ selected\ opacity}/L_{\rm baseline}), with the B.1 source held fixed:

| Coupling point | Remove outer (
u_mu) opacity | Remove outer (
u_	au) opacity | Remove both outer neutrino flavors |
|---|---:|---:|---:|
| Luminosity peak, (g=1.1341\times10^{-8}) | 1.301 | 1.301 | 1.756 |
| Strong-absorption endpoint, (g=4.1717\times10^{-8}) | 5.329 | 5.331 | 113.90 |

Removing either flavor throughout the entire star gives factors 1.537 and 1.547 at the luminosity peak, respectively. The two flavors are therefore comparably important; the small outer (mu_{
u_\mu}) branch does not suppress the outer (
u_mu) opacity relative to the (
u_	au) opacity.

## 2c. Approach to the unblocked decay rate

For (mu_{\nu}=0), the reduced absorption divided by the per-(g^2) vacuum-decay scale (m_V^2/(8\pi\omega)) is
[
\mathcal R(\omega,r)
=\left(e^{\omega/T(r)}-1\right)
I\left(0,\omega/T(r),v_V\right).
]
It approaches unity in the Maxwell--Boltzmann/low-temperature limit. At (omega=20) MeV, the tau-flavor values are:

| Radius | (T) (MeV) | (omega/T) | (mathcal R) |
|---:|---:|---:|---:|
| 8 km | 38.74 | 0.516 | 0.128 |
| 10 km | 33.92 | 0.590 | 0.146 |
| 12 km | 25.98 | 0.770 | 0.188 |
| 15 km | 13.24 | 1.511 | 0.350 |
| 18.5 km | 5.36 | 3.730 | 0.662 |
| 20 km | 4.21 | 4.753 | 0.740 |
| 22 km | 3.55 | 5.630 | 0.788 |
| 25 km | 3.03 | 6.592 | 0.827 |

The opacity per unit length becomes progressively less Pauli-blocked outward and approaches its vacuum-decay scale. This is the physical origin of the outer-shell contribution in the fixed-(\omega) baseline.

## 3. Why cold outer layers can remain opaque

For either neutrino flavor, detailed balance gives
\[
\Gamma_{\mathrm{prod}}=e^{-\omega/T}\Gamma_{\mathrm{abs}},
\qquad
\Gamma_{\mathrm{abs}}^*=(1-e^{-\omega/T})\Gamma_{\mathrm{abs}}
=(e^{\omega/T}-1)\Gamma_{\mathrm{prod}}.
\]
In the outer layers, \(\mu_{\nu_\tau}=0\) and \(\mu_{\nu_\mu}/T\) is small. When \(\omega/T\gg1\), the production kernel is Boltzmann suppressed, \(I(0,\omega/T,v)\sim e^{-\omega/T}\), but the factor in the reduced absorption cancels that suppression. The reduced absorption approaches the time-dilated vacuum-decay scale. Equivalently, the final-state neutrino blocking becomes negligible in cold, nondegenerate outer material.

Thus low local temperature does not imply negligible vector absorption. The vector can still decay to \(\nu\bar\nu\) while traversing the outer shells.

## 4. Interpretation

The large outer optical depth is primarily a neutrino-decay opacity effect, not an outer muon-density effect and not an effect driven by a large \(\mu_{\nu_\mu}\). The flavor-resolved audit quantifies how much of this opacity is carried by \(\nu_\mu\) and \(\nu_\tau\) separately.

The next validation target is to compare the flavor-resolved shell contributions under the fixed-\(\omega\) Appendix-B prescription and the separately defined path-redshift diagnostic. No rescaling of rates or luminosity is introduced.
