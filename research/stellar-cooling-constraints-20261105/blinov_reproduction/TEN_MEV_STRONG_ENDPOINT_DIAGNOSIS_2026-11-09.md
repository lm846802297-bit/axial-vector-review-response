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


## 9. Reconciliation with the completed high-order baseline and existing phase-space audit

The current vertex-preserving profile has SHA-256
\`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.
The high-order independent-grid result at the strong endpoint is
\[
L_{\rm B.16}=2.43963596\times10^{52}\ {\rm erg\,s^{-1}},
\qquad
P_{\rm esc}=3.2517740\times10^{-4},
\]
with a \(+92.4284\%\) difference from Fig. 7. The corresponding effective-log ratio is
\[
\ln(L_{\rm B.16}/L_{\rm Fig.7})=0.65455.
\]

The vertex-preserving emission-radius/direction/path audit was run at the lower configuration
\[
(N_r,N_E,N_\theta,N_s)=(40,100,32,256)
\]
with analytic piecewise-linear chord integration. It is not the same high-order grid, but its integrated escape probability agrees with the high-order result at the sub-percent level:
\[
P_{\rm esc}^{\rm directional}=3.2393538\times10^{-4},
\qquad
P_{\rm esc}^{\rm high\ order}=3.2517740\times10^{-4}.
\]
The relative difference is about \(0.38\%\). Thus the phase-space interpretation below is already cross-checked against the high-order *integrated* luminosity, although the individual bins have not yet been recomputed on the 200/640/200/32/64 grid.

### 9.1 Where the escaping luminosity comes from

For all emission radii, the B.1 source-weighted escape probability is \(3.23935\times10^{-4}\). The directional distribution of the escaped luminosity is:

| \(\cos\theta\) | Fraction of escaped luminosity |
|---|---:|
| \([-1,-0.5]\) | 0.806% |
| \([-0.5,0]\) | 2.975% |
| \([0,0.5]\) | 20.203% |
| \([0.5,1]\) | 76.016% |

The escaping population is therefore strongly biased toward outward directions. Backward-emitted vectors traverse more of the dense inner core and are exponentially suppressed.

The emission-shell decomposition is:

| Emission shell | Fraction of total thin B.1 source | Fraction of escaped luminosity |
|---|---:|---:|
| 5--8 km | 17.508% | 9.723% |
| 8--10 km | 39.812% | 49.405% |
| 10--12 km | 26.081% | 30.598% |
| 12--15 km | 13.718% | 6.833% |
| 22--25 km | 0.0728% | 3.357% |

The 8--15 km region supplies 79.611% of the thin source and 86.836% of the escaped luminosity. Within that region, the escaped-luminosity direction fractions are 0.556%, 2.786%, 19.979%, and 76.679% in the four direction bins above.

This is a more informative description than the source-weighted mean optical depth alone: the escaping luminosity is dominated by a restricted subset of source radii and outward trajectories.

### 9.2 Which path shells matter

The leave-one-shell-out tests are nonlinear counterfactuals, not additive optical-depth contributions. Their ranking depends on the emission region.

For all emission radii:
- removing all opacity in 22--25 km increases the luminosity by a factor 4.073;
- removing all opacity in 12--15 km increases it by a factor 2.926.

For the dominant 8--15 km emission region:
- removing all opacity in 12--15 km increases the luminosity by a factor 3.047;
- removing all opacity in 22--25 km increases it by a factor 2.627.

The outer shell is important, but it is not the unique controlling region. The 12--15 km path shell is at least as influential for the dominant core-emission population. The neutrino inverse-decay channels dominate the source-weighted mean optical depth (about 89.8%); Compton contributes about 10.2%.

**Interpretation:** the existing C-stage calculation already establishes that the high-coupling escaping population is selected jointly by emission radius, direction, and the entire inner-plus-outer path. It does not support attributing the 92% discrepancy to the 22--25 km shell alone.

## 10. One-parameter numerical convergence checks already available

The following tests use the current vertex-preserving profile. They are isolated one-parameter comparisons, not a single combined error estimate.

| Numerical dimension | Comparison | Change at 10 MeV strong endpoint |
|---|---|---:|
| Energy quadrature | \(N_E=150\to200\) | 0.1121% |
| Opacity interpolation grid | \(N_{\rm opacity}=480\to640\) | 0.001525% |
| Path quadrature | \(N_s=48\to64\) | 0.001075% |
| B.1 source radial grid | \(N_r=160\to200\), with opacity grid fixed at 640 | 0.0609% |

The energy and path comparisons keep their other grid identities fixed. The radial comparison explicitly keeps the 642-node opacity grid and 742-node energy grid fixed. The opacity comparison uses its own fixed source/energy configuration. These checks are not all performed at the final high-order configuration, but they show that the tested one-dimensional numerical refinements are far below the 92.4% discrepancy.

The earlier 0.1 and 1 MeV points are not being expanded in this stage.

## 11. High-order phase-space binning: execution status

A dedicated post-processing script has been added:
\`audit_b16_escape_phase_space.py\`.
It reconstructs the exact 10 MeV high-order source and opacity grids, checks their SHA-256 identities against the archived 200/640/200/32/64 baseline, and bins the same \(S_{\rm B.1}e^{-g^2\tau}\) weights by emission radius, energy, and direction. It introduces no new physical approximation.

The corresponding workflow is
\`.github/workflows/b16-escape-phase-space.yml\`.
The first run and subsequent retries ended before any workflow step was executed; the Actions job returned no step records. Therefore **no high-order phase-space-bin result is accepted yet**. The script is staged for execution when a runner is allocated. The already completed lower-order phase-space audit remains the only source of the numerical bin fractions in §9.1.

## 12. Updated decision and next action

The combined evidence now supports the following:

1. The \(+92.4\%\) strong-end discrepancy is not explained by the tested energy, opacity-grid, path, or source-radial quadrature errors.
2. The outer 22--25 km shell matters, but the 12--15 km path shell and the inner 8--22 km trajectory are also important.
3. Escaped luminosity is strongly outward-direction biased; the full angular average is dominated by a small subset of rays.
4. The current profile remains a public-figure reconstruction, not the raw Garching simulation profile. This is still a systematic limitation, not a numerical error estimate.

The next calculation remains the high-order energy-resolved escape decomposition. It should establish which energy bins, in combination with the already identified outward directions and emission shells, dominate the residual. Only after that should we decide whether a new physical input or a different propagation prescription is required.

No opacity rescaling is applied, no \(R_{\max}=25\) km change is made, and no axial-vector production result or constraint curve is updated.
