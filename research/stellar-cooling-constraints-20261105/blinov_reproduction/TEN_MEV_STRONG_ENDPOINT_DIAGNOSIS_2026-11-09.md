# 10 MeV strong-absorption endpoint: targeted diagnosis

Date: 2026-11-09  
Branch: research/moving-muon-thermal-rates-20261107  
Scope: pure-vector B.16 Fig. 7 reproduction only. No axial-vector production files or constraint curves are changed.

## 1. Problem definition

At the strongest digitized Fig. 7 coupling for \(m_V=10\) MeV,
\[
g=4.171689650228597\times10^{-8},
\]
the high-order fixed-\(\omega\) B.16 result is
\[
L_{\rm B16}=2.4396\times10^{52}\ {\rm erg\,s^{-1}},
\qquad
L_{\rm Fig.7}=1.2678\times10^{52}\ {\rm erg\,s^{-1}},
\]
or \(+92.43\%\).

The corresponding optically thin luminosity is \(7.5025\times10^{55}\,\mathrm{erg\,s^{-1}}\), and the escape fraction is \(3.2518\times10^{-4}\). The discrepancy is therefore an escape/opacity issue at this endpoint, not simply a normalization difference in the optically thin source.

The reference is the digitized published Fig. 7 curve from the formal JHEP article, not an analytic fit.

## 2. What is already numerically under control

The high-order B.16 calculation uses:
- B.1 source radial order 200;
- independent B.2 opacity grid with 642 nodes (opacity order 640);
- energy order 200, with 842 final energy nodes after lapse-threshold nodes are inserted;
- angular order 32;
- path order 64.

Independent B.1 source-radial tests at 10 MeV passed the 1% adjacent-grid screen through orders 80, 100, 120, 160, and 200. The high-order directional/path diagnostic at lower radial and energy order found:
- angular-order changes at the strong endpoint below \(2.1\times10^{-6}\) between 32 and 64;
- direction-bin quadrature changes below \(1.1\times10^{-6}\) between per-bin orders 16 and 32;
- analytic radial-shell integration versus global path quadrature maximum residual \(1.19\times10^{-4}\), with source-weighted L1 residual \(2.09\times10^{-6}\).

These checks make angular averaging and the basic chord/path quadrature unlikely explanations for a 92% luminosity excess. They do not replace a dedicated high-order energy-order and opacity-grid convergence test at 10 MeV.

## 3. Opacity and source anatomy at 10 MeV

The high-order B.16 output gives the following source fractions:
- inverse-neutrino-decay source: 67.93%;
- Compton source: 32.07%;
- dimuon source: zero below threshold.

The fixed-\(\omega\) source-weighted mean optical-depth decomposition gives:
- neutrino inverse-decay opacity: 89.78%;
- Compton opacity: 10.22%;
- \(r\geq15\) km: 56.71% of the source-weighted mean optical depth;
- \(20\)--\(22\) km: 11.57%;
- \(22\)--\(25\) km: 17.37%.

The B.1 emission is concentrated much deeper:
- mean emission radius: 9.83 km;
- median: 9.51 km;
- 90th percentile: 12.73 km;
- 79.61% of the thin source is emitted in 8--15 km.

Thus the strong-end escape probability is particularly sensitive to the outer \(15\)--\(25\) km inverse-decay opacity crossed by particles emitted in the inner core.

## 4. Existing sensitivity tests that do not explain the excess

### 4.1 Inner and outer neutrino chemical-potential branches

The 8--12 km \(\mu_{\nu_\mu}\) sign/scale tests change the strong-end luminosity by much less than 1%. The 20--22 km and 22--25 km \(\mu_{\nu_\mu}\) continuation tests are also negligible at the tested perturbations. These branches are not the leading explanation.

### 4.2 Outer temperature

The 22--25 km temperature stress tests show that a broad \(\pm30\%\) temperature variation can move the strong-end luminosity appreciably (the low-temperature case shifts it down by about 7%; the high-temperature case shifts it up by about 24%). This confirms that the outer profile matters, but the tested temperature changes do not by themselves account for the full 92% discrepancy. These are stress tests, not a statistical uncertainty band.

### 4.3 Polarization-resolved outer-shell diagnostic

The existing 22--25 km-only polarization-resolved diagnostic finds a strong-end escape factor of 0.468 for its mode-resolved prescription versus 0.150 for the literal scalar-summed opacity, a ratio of 3.11. This diagnostic:
- attenuates only the 22--25 km segment;
- uses an equal-third split of the scalar Compton source/opacity as an explicit assumption;
- does not propagate the modes through the inner path.

It therefore cannot be used as a correction to the published scalar B.2 baseline. Its direction is also opposite to what is needed: it increases escape and would worsen an already-too-large luminosity. A full mode-resolved treatment remains a separate physics question, not the present Fig. 7 discrepancy fix.

### 4.4 Path-energy redshift diagnostic

The high-order path-redshift-only diagnostic changes the strong-end luminosity by \(-28.85\%\), reducing the Fig. 7 residual from \(+92.43\%\) to \(+36.91\%\). It evaluates
\[
\omega_{\rm loc}(s)=\omega_{\rm source}\frac{N(r_{\rm source})}{N(r(s))}
\]
and updates the local rate and \(v_V(s)\), while retaining the same Euclidean chord.

This is retained as a gravitational-energy sensitivity diagnostic, not substituted for the published Eq. (B.2) fixed-\(\omega\) implementation. The paper's Eq. (B.2) uses the same \(\omega\) argument along the chord and follows the Caputo--Raffelt--Vitagliano optical-depth prescription [28]. The B.1 gravitational factors and escape threshold are separately implemented. The path-redshift result must not be used to claim that the published Fig. 7 has been reproduced.

## 5. Quantitative scale of the remaining discrepancy

At the strong endpoint, the redshift-only result is
\[
L_{\rm redshift}=1.7358\times10^{52}\ {\rm erg\,s^{-1}},
\]
still \(36.91\%\) above Fig. 7.

The corresponding escape fraction is \(2.3136\times10^{-4}\), compared with the Fig. 7-implied value
\[
P_{\rm esc}^{\rm Fig.7}
=\frac{L_{\rm Fig.7}}{L_{\rm thin}}
\simeq1.69\times10^{-4}.
\]
The residual corresponds to an additional effective optical depth of only
\[
\Delta\tau_{\rm eff}
=\ln\!\left(\frac{L_{\rm redshift}}{L_{\rm Fig.7}}\right)
\simeq0.314.
\]
This is a useful scale estimate, not a proposed opacity rescaling. It shows that a modest systematic change in the escaping part of the optical-depth distribution can produce a large luminosity shift in the strong-absorption tail.

## 6. Next calculations: 10 MeV only

Do not increase the grid for 0.1 or 1 MeV. Keep the physics and profile fixed, and isolate the remaining numerical dimensions at 10 MeV:

1. **Energy quadrature convergence:** compare energy orders 160, 200, 240, and 320 with source radial order 200, opacity order 640, angular order 32, and path order 64 fixed. Record both \(L_{\rm thin}\) and the strong-end escaped luminosity. Also report the energy-resolved contributions to the escaping luminosity, not just the total.
2. **Opacity-grid convergence:** compare opacity orders 640, 960, and 1280 while holding the B.1 source grid and energy order fixed. Verify the interpolation error in the outer \(15\)--\(25\) km shells separately.
3. **Source/opacity decoupling:** vary only the source radial order while holding the opacity and energy grids fixed, then vary only the opacity grid while holding the source nodes fixed. This avoids conflating B.1 and B.2 errors.
4. **Escaping-bin diagnosis:** at the strong endpoint, identify the emission-radius, energy, and direction bins that dominate \(L_{\rm esc}\). Compare their shell-by-shell \(\tau\) contributions. The source-weighted mean \(\tau\) alone is not an adequate statistic in the exponentially suppressed regime.
5. **Profile reconstruction audit:** prioritize the opacity profile in \(15\)--\(25\) km, especially \(T(r)\), lapse \(N(r)\), and \(\mu_{\nu_\mu}(r)\). The archived profile is a public-figure reconstruction, not the original Garching table. Do not infer a physical profile correction from the luminosity residual.

Acceptance criteria for each isolated refinement:
- \(L_{\rm thin}\) changes by less than 1%;
- strong-end \(L_{\rm esc}\) changes by less than 2%;
- the opacity-grid identity and source-grid identity are recorded independently;
- the B.16 baseline closure and detailed-balance checks pass.

## 7. CI status

The targeted full-path polarization diagnostic was added as a separate workflow, but the first run and its retry failed before runner allocation: GitHub reported runner_id=0, no runner name, and zero executed steps. This is an infrastructure/runner-allocation failure, not a numerical failure. No numerical result from that workflow is accepted.

The B.13 convergence matrix and the independent B.16 quadrature matrix show the same no-runner pattern. Do not interpret these runs as failed physics calculations. Resume the targeted 10 MeV scans when a GitHub-hosted runner is available.

## 8. Decision

The 10 MeV strong-end excess is not resolved. The evidence points to the outer-shell neutrino inverse-decay opacity and its energy/radial integration as the first places to isolate. The already-tested angular/path quadratures, inner \(\mu_{\nu_\mu}\) branch, and outer \(\mu_{\nu_\mu}\) continuation are not leading explanations.

No empirical rescaling is applied. No axial-vector production output or formal constraint curve is changed.
