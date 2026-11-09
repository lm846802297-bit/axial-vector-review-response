# Independent B.1 optically-thin source integration audit (10 MeV, 2026-11-09)

## Executive conclusion

An independent numerical evaluation of the B.1 optically-thin source has been completed and archived. The implementation does not call the existing \`eq_b1_source_measure\`, \`energy_weights\`, or \`radial_rule\`. It evaluates the local production kernels at new quadrature nodes and uses:

- composite Gauss--Legendre quadrature on equal-width radial panels;
- composite Gauss--Legendre quadrature in \(x=\ln(\omega-m_V)\), with the exact radius-dependent threshold \(\omega_{\min}=m_V/N(r)\) inserted at every radial node;
- separate neutrino inverse-decay, dimuon inverse-decay, and muon-Compton source integrals;
- explicit energy-cutoff, energy-resolution, and radial-resolution convergence checks.

For \(m_V=10\) MeV, the high-resolution independent optically-thin source is
\[
L_{\rm thin}^{\rm independent}
=4.30436817\times10^{70}\ {\rm erg\,s^{-1}}\quad\text{per }g_{\mu\tau}^2.
\]
The archived B.16 source measure gives
\[
L_{\rm thin}^{\rm archived}
=4.32352241\times10^{70}\ {\rm erg\,s^{-1}}\quad\text{per }g_{\mu\tau}^2.
\]
The independent result is lower by \(0.4430\%\). This small residual is resolved further below: at the same 40 radial nodes used by the archived calculation, direct energy integration is lower by \(0.5755\%\); refining the radial integral from 40 to 400 nodes then raises the source by \(0.1332\%\), leaving the net \(-0.4430\%\) difference.

The independent radial and energy integrations are converged well below the project's 1% source-stability target. This sub-percent B.1 numerical difference cannot explain the \(+92.25\%\) strong-coupling discrepancy in the Fig. 7 luminosity curve. The result validates the optically-thin source quadrature for the adopted profile and shared local kernels; it does not yet validate the full \(L_V\), because this audit sets \(\mathcal O=1\).

## 1. Published B.1 expression and the isolated quantity

Blinov et al., JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B, Eq. (B.1), write
\[
L_V=\int_0^{R_{\max}}dr\,4\pi r^2N(r)^2
\int_{m_V/N(r)}^\infty d\omega\,
\frac{k\omega^2}{2\pi^2}
\Gamma_{\rm prod}(r,\omega)\mathcal O(r,\omega),
\qquad
k=\sqrt{\omega^2-m_V^2}.
\]

The present audit first sets \(\mathcal O(r,\omega)=1\) and computes
\[
L_{\rm thin}=\int_0^{R_{\max}}dr\,4\pi r^2N(r)^2
\int_{m_V/N(r)}^{\omega_{\max}}d\omega\,
\frac{\sqrt{\omega^2-m_V^2}\,\omega^2}{2\pi^2}
\Gamma_{\rm prod}(r,\omega).
\]
This isolates the source normalization and its radial/energy quadrature from the escape-probability calculation. It is not the full trapped luminosity.

At \(m_V=10\) MeV, the dimuon inverse-decay channel is kinematically closed. The source therefore contains neutrino inverse decay and muon-Compton production.

## 2. Independent integration method

### 2.1 Radial integration

The profile is read directly from the archived CSV and linearly interpolated in radius. The radial integral uses equal-width panels on \([0,25]\) km, with four-point Gauss--Legendre quadrature on each panel.

The convergence sequence is:
- 25 panels of width 1 km: 100 radial nodes;
- 50 panels of width 0.5 km: 200 radial nodes;
- 100 panels of width 0.25 km: 400 radial nodes.

This is a different partition from the archived 40-node rule, which uses the fixed interfaces \(0,5,8,10,12,15,18,20,22,24,25\) km.

### 2.2 Energy integration

At each radial quadrature node, the exact lower limit is
\[
\omega_{\min}(r)=\frac{m_V}{N(r)}.
\]
Define
\[
x=\ln\left(\frac{\omega-m_V}{1\ {\rm MeV}}\right),
\qquad
d\omega=(\omega-m_V)dx.
\]
The energy integral is evaluated with composite Gauss--Legendre quadrature in \(x\). The lower limit is inserted exactly for each radius; the old global energy grid and the old \`energy_weights\` routine are not used.

The production kernels are evaluated directly at the new energy quadrature nodes. The neutrino inverse-decay and Compton contributions are integrated separately before summing them.

### 2.3 Shared physics and independence boundary

The following are intentionally shared with the Appendix-B reference implementation:
- the reconstructed SFHo-18.8 profile;
- the local neutrino inverse-decay production kernel;
- the local muon-Compton production kernel;
- the negative-muon density and susceptibility convention used in Eq. (B.17).

The following are independently implemented:
- CSV profile reading and interpolation at the new radial nodes;
- radial quadrature nodes and weights;
- the logarithmic energy transformation and quadrature;
- exact insertion of the radius-dependent lower energy limit;
- source-channel integration and radial shell accumulation.

The script does not import or call \`eq_b1_source_measure\`, \`energy_weights\`, \`radial_rule\`, \`load_profile\`, or any B.2 path integrator.

## 3. Frozen inputs

- Mediator mass: 10 MeV.
- Outer radius: 25 km.
- Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.
- Profile rows: 1687.
- Final radial quadrature: 400 nodes.
- Final energy quadrature: 240 logarithmic panels, four Gauss nodes per panel (960 energy nodes per radial node).
- Final energy upper limit: \(\omega_{\max}=2010\) MeV.
- Coupling convention: rates are reported per \(g_{\mu\tau}^2\).

## 4. Radial convergence

The radial convergence scan uses 160 logarithmic energy panels, four energy Gauss nodes per panel, and \(\omega_{\max}=1010\) MeV.

| Equal-width radial panels | Radial nodes | \(L_{\rm thin}\) [erg/s per \(g^2\)] | Relative shift vs 400 nodes |
|---:|---:|---:|---:|
| 25 | 100 | \(4.30137121\times10^{70}\) | \(-0.06963\%\) |
| 50 | 200 | \(4.30427599\times10^{70}\) | \(-0.002141\%\) |
| 100 | 400 | \(4.30436816\times10^{70}\) | 0 |

At 200 versus 400 nodes, the channel-specific relative changes are:
- neutrino inverse decay: \(-0.000579\%\);
- muon-Compton: \(-0.005451\%\).

The radial integral is therefore stable at the sub-\(0.01\%\) level for the two source channels at the last refinement.

## 5. Energy convergence

At fixed 200 radial nodes, four-point Gauss--Legendre integration is performed with 80, 120, 180, and 240 logarithmic panels. The total source is \(4.304275994987931\times10^{70}\) erg/s per \(g^2\) at all four resolutions to the precision retained in the output. The neutrino and Compton fractions are also stable to the displayed precision.

The energy quadrature is therefore numerically converged well before the final 240-panel resolution.

## 6. High-energy cutoff convergence

At fixed 200 radial nodes and 240 energy panels:

| \(\omega_{\max}-m_V\) [MeV] | \(L_{\rm thin}\) [erg/s per \(g^2\)] | Relative shift vs 4000 MeV offset |
|---:|---:|---:|
| 500 | \(4.30333350\times10^{70}\) | \(-0.02190\%\) |
| 1000 | \(4.30427599\times10^{70}\) | \(-2.575\times10^{-7}\%\) |
| 2000 | \(4.30427601\times10^{70}\) | 0 |
| 4000 | \(4.30427601\times10^{70}\) | 0 |

The original 1000 MeV energy offset already captures the high-energy tail to better than \(3\times10^{-9}\) relative in the integrated source. The 500 MeV offset is not sufficient for the same precision.

## 7. Matched 40-node comparison: isolate the old energy quadrature

To distinguish energy-integration and radial-integration effects, the archived 40-node radial quadrature is reconstructed independently using the same interval boundaries and four-point Gauss rule. The energy integral is then replaced by the new direct logarithmic-energy quadrature with 240 panels and \(\omega_{\max}=2010\) MeV.

At these matched 40 radial nodes:
\[
L_{\rm thin}^{40r,\mathrm{direct}\ E}
=4.29864077\times10^{70}\ {\rm erg\,s^{-1}}\quad\text{per }g^2.
\]
Relative to the archived B.16 source measure, this is lower by \(0.575495\%\).

The channel-specific matched-node differences are:
- neutrino inverse decay: \(-0.575690\%\);
- muon-Compton: \(-0.575081\%\).

Because the radial nodes and weights are held fixed in this comparison, the residual isolates the archived energy-grid integration/interpolation relative to direct evaluation of the production kernels at independent quadrature nodes.

## 8. Independent 400-node source and comparison with the archived B.1 measure

The final independent source is
\[
L_{\rm thin}^{400r,\mathrm{direct}\ E}
=4.30436817\times10^{70}\ {\rm erg\,s^{-1}}\quad\text{per }g^2.
\]

| Channel | Independent source [erg/s per \(g^2\)] | Archived source [erg/s per \(g^2\)] | Relative difference |
|---|---:|---:|---:|
| Neutrino inverse decay | \(2.92401428\times10^{70}\) | \(2.93977934\times10^{70}\) | \(-0.53627\%\) |
| Muon-Compton | \(1.38035389\times10^{70}\) | \(1.38374308\times10^{70}\) | \(-0.24493\%\) |
| Dimuon inverse decay | 0 | 0 | 0 |
| **Total** | **\(4.30436817\times10^{70}\)** | **\(4.32352241\times10^{70}\)** | **\(-0.44302\%\)** |

The final independent source fractions are:
- neutrino inverse decay: 67.9313%;
- muon-Compton: 32.0687%;
- dimuon inverse decay: 0%.

The archived fractions are 67.9950% neutrino inverse decay and 32.0050% Compton. The channel decomposition is therefore also stable at the sub-percent level.

The radial refinement from the matched 40-node direct-energy result to the 400-node direct-energy result raises the total source by \(0.13324\%\). This partially offsets the \(-0.57550\%\) energy-integration residual at matched radial nodes, giving the final \(-0.44302\%\) difference against the archived source.

## 9. Radial source distribution

The independent 400-node result gives the following fractions of the total optically-thin source:

| Radial shell | Fraction |
|---|---:|
| 0--5 km | 0.9080% |
| 5--8 km | 17.4770% |
| 8--10 km | 39.9038% |
| 10--12 km | 26.0453% |
| 12--15 km | 13.6984% |
| 15--18 km | 1.6437% |
| 18--20 km | 0.1769% |
| 20--22 km | 0.0744% |
| 22--25 km | 0.0726% |

Approximately 97.1% of the optically-thin source is produced inside 15 km. This is a source distribution, not an opacity or escape-probability distribution; the outer shells can still have a disproportionate effect on B.2 optical depth.

## 10. Interpretation

Established:
1. The independent B.1 optically-thin source integral is implemented with a different radial and energy quadrature.
2. The exact radius-dependent lower limit \(m_V/N(r)\) is respected at every radial node.
3. Radial convergence is better than \(0.01\%\) between the last two resolutions.
4. Energy resolution is stable from 80 to 240 logarithmic panels at the displayed precision.
5. The 1000 MeV energy offset captures the high-energy tail to better than \(3\times10^{-9}\) relative.
6. The independent total source differs from the archived source by only \(-0.4430\%\).
7. The matched 40-node comparison isolates a \(-0.5755\%\) difference from the archived energy-grid integration, partly offset by a \(+0.1332\%\) radial refinement correction.

Not established:
1. The escape factor \(\mathcal O(r,\omega)\) is not included in this audit. The full B.1 luminosity is not yet independently recomputed.
2. The local production kernels are shared and are not re-derived here.
3. The reconstructed profile is not the original Garching s18.8-SFHo-MUONS simulation table.
4. The negative-muon species convention and the source-energy interpretation are retained as in the archived Appendix-B reference; this audit does not revisit those physical choices.

The sub-percent B.1 source-quadrature difference is much too small to account for the order-one strong-coupling Fig. 7 luminosity mismatch. The next step is to combine this independently integrated source with the independently validated analytic B.2 escape factor on the same radial and energy quadrature nodes, and compare the complete luminosity curve against both the archived B.16 result and the digitized Fig. 7 vertices. No empirical rescaling is justified.

## 11. Reproducibility

- GitHub Actions: [Run #42563868176](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42563868176)
- Script: \`audit_b16_b1_independent.py\`
- Unit tests: \`test_b16_b1_independent.py\`
- Workflow: \`.github/workflows/b16-b1-independent-source.yml\`
- Machine-readable result: \`outputs/b16_b1_independent_thin_source_10mev_2026-11-09.json\`
- The workflow checks that the production axial-vector outputs remain unchanged.
