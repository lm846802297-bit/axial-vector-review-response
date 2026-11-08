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
