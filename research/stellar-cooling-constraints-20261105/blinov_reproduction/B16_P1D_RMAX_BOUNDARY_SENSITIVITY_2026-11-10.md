# P1-D: source-frozen \(R_{\max}\) boundary sensitivity of the 10 MeV B.16 high-energy escape integral

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: pure vector, \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
Energy band: \(210\leq\omega\leq510\) MeV  
Profile: vertex-preserving public-figure reconstruction of SFHo-18.8 at \(t_{\rm pb}=1\) s  
Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`  
Profile Git blob: \`e41df78c8035540760fbcb7ef592cd830171822e\`

## 1. Motivation and physical meaning of \(R_{\max}\)

The preceding P1-C audit resolved the scalar polarization normalization. The next issue is the physical outer boundary in Eq. (B.2).

Blinov et al. identify \(R_{\max}\) with the neutrinosphere radius \(R_\nu\simeq25\) km. They state that this is the minimum radius beyond which a vector must decay for the decay products to constitute energy loss. Thus \(R_{\max}\) is not merely a numerical integration cutoff: it encodes where the neutrino daughters cease to be trapped. The paper motivates this choice from the Boltzmann-equation solution underlying Eqs. (B.1)--(B.2).

The audit therefore asks two separate questions:

1. How much does the source-frozen high-energy escape integral change if the absorbing/trapping region ends inside 25 km?
2. If neutrinos remain trapped farther out, how much additional inverse-decay optical depth would accrue outside 25 km?

The literal \(R_{\max}=25\) km calculation remains the baseline. No boundary is selected by fitting Fig. 7.

## 2. Calculation definition

The B.1 source weights are held fixed at their \(R_{\max}=25\) km values. Only the radial support of the B.2 opacity is varied. This isolates the propagation-boundary sensitivity and is not a complete redefinition of the B.1 integration domain.

For inward boundary tests, opacity is retained only where the ray lies inside \(r\leq R_{\max}\). The ray is followed forward from its emission point; if the source point lies outside the smaller sphere, only the part of the ray that actually intersects the absorbing sphere contributes. This avoids applying the interior-source chord formula outside its domain of validity.

For \(R_{\max}>25\) km, the profile is not extrapolated as an invented thermodynamic model. Instead, the extra shell is a separately labelled vacuum-limit diagnostic for the two active neutrino inverse-decay channels:
\[
\Gamma_{\nu,\mathrm{red}}^{*,\mathrm{vac}}(\omega)
=\frac{m_V^2}{4\pi\omega}
\quad\text{per }g^2.
\]
This is the sum of the two flavour contributions \(m_V^2/(8\pi\omega)\), obtained when final-state Pauli blocking vanishes. The semi-Compton opacity is set to zero in this added outer shell. This tests the additional decay optical depth if the neutrino-trapping boundary were farther out; it is not asserted to be the actual profile beyond 25 km.

The calculation uses:
- 200 B.1 source-radius nodes;
- 642 B.2 opacity-radius nodes;
- the original 842-point energy grid, selecting its 10 nodes in 210--510 MeV;
- 32 Gauss--Legendre emission-angle nodes;
- 64- and 128-point Gauss--Legendre path quadratures;
- the literal fixed-\(\omega\), scalar polarization-summed opacity;
- the same \(m_V\), \(g\), local kernels, and reconstructed profile as the archived P1-C baseline.

## 3. Baseline closure

The selected 10-node band is identical to the P1-C grid; the maximum energy-node difference is \(4.55\times10^{-13}\) MeV.

| Closure quantity | Direct calculation | Archived P1-C value |
|---|---:|---:|
| B.1 thin luminosity in 210--510 MeV | \(7.254600479852544\times10^{54}\) erg/s | \(7.254600479852540\times10^{54}\) erg/s |
| B.2 escaped luminosity at \(R_{\max}=25\) km, path order 64 | \(1.701784828846562\times10^{52}\) erg/s | \(1.701784828846571\times10^{52}\) erg/s |

The source closure is at floating-point precision. The fixed-\(\omega\) \(R_{\max}=25\) escape integral reproduces the archived P1-C scalar high-energy result to \(5.7\times10^{-15}\) relative.

Across all tested boundaries, the 64-to-128 path-order change is below \(8.7\times10^{-6}\). Thus the boundary response below is not a path-quadrature effect.

## 4. Inward boundary scan: source frozen, opacity support truncated

| \(R_{\max}\) (km) | \(L_{\rm esc}^{210-510}\) (erg/s) | Change relative to 25 km | B.1 source fraction outside \(R_{\max}\) |
|---:|---:|---:|---:|
| 15 | \(2.53894\times10^{53}\) | +1391.93% | \(9.69\times10^{-7}\) |
| 18.5 | \(9.42283\times10^{52}\) | +453.70% | \(1.73\times10^{-17}\) |
| 20 | \(6.25849\times10^{52}\) | +267.76% | \(6.65\times10^{-22}\) |
| 22 | \(3.67687\times10^{52}\) | +116.06% | \(1.25\times10^{-25}\) |
| 24 | \(2.19252\times10^{52}\) | +28.84% | \(1.94\times10^{-28}\) |
| **25 (baseline)** | **\(1.70178\times10^{52}\)** | **0** | 0 |

The high-energy B.1 source is extremely concentrated inside 15 km: even at the \(R_{\max}=15\) km stress test, less than \(10^{-6}\) of the selected band source lies outside the boundary. Therefore the large changes in this table are caused by the removed outer-path opacity, not by dropping a significant part of the source.

Reducing \(R_{\max}\) increases the escaped luminosity, as expected when less of the path is treated as a region in which vector decays rethermalize their energy. The response is strongly nonlinear because the survival factor is exponential.

## 5. Outward boundary extension: vacuum-limit neutrino opacity

At the reconstructed 25 km boundary:
\[
T(25\,{\rm km})=3.03377\ {\rm MeV},\qquad
\mu_{\nu_\mu}(25\,{\rm km})=0,\qquad
\mu_\mu(25\,{\rm km})=0.
\]
Across the 10 energy nodes, the local two-flavour reduced neutrino opacity at 25 km is already \(98.11\%\)--\(99.15\%\) of its vacuum limit. The outer extension is therefore close to the unblocked inverse-decay limit, rather than an arbitrary rescaling of the opacity.

| Extended \(R_{\max}\) (km) | \(L_{\rm esc}^{210-510}\) (erg/s) | Change relative to 25 km | Source-weighted mean extra \(\Delta\tau_\nu\) |
|---:|---:|---:|---:|
| 26 | \(1.32029\times10^{52}\) | -22.42% | 0.2896 |
| 27.5 | \(9.08069\times10^{51}\) | -46.64% | 0.7221 |
| 30 | \(4.94603\times10^{51}\) | -70.94% | 1.4389 |

These are conditional extensions: they represent the case in which neutrino daughters remain trapped over the added shell. If they already free-stream outside the 25 km neutrinosphere, this extra absorption must not be included. No raw thermodynamic profile beyond 25 km is available here, so the vacuum-limit continuation is not promoted to a new physical baseline.

## 6. Interpretation

1. **The \(R_{\max}\) choice is a high-impact physical assumption for the strong-coupling high-energy band.** Moving the trapping boundary inward by only 1 km (25 to 24 km) increases the band luminosity by 28.84%; extending it outward by 1 km with the vacuum-limit neutrino opacity decreases it by 22.42%.
2. The \(22\)--\(25\) km part of the path cannot be discarded as numerically irrelevant. Its effect is amplified by the nonlinear escape probability, even though the high-energy source itself is produced almost entirely inside 15 km.
3. The additional outer optical depth is almost entirely neutrino inverse decay. At 25 km, the muon population is negligible and the added-shell Compton opacity is set to zero.
4. The scan does **not** show that the paper's \(R_\nu\simeq25\) km choice is wrong. It shows that replacing it requires an independently justified energy-/flavour-dependent neutrinosphere or a same-snapshot transport profile.
5. This is a 210--510 MeV band calculation at the strong-endpoint coupling, not a full 25-point Fig. 7 re-integration. The band is 9.67% of the optically thin source but 69.76% of the baseline escaped luminosity.
6. The literal \(R_{\max}=25\) km result remains unchanged. No empirical rescaling, profile modification, source normalization change, coupling change, Fig. 7 curve update, or axial-vector recalculation is made.

## 7. Reproducibility

- Python reproduction script: \`audit_b16_rmax_boundary_sensitivity.py\`
- Machine-readable direct-calculation result: \`outputs/b16_rmax_boundary_sensitivity_10mev_2026-11-10.json\`
- Previous P1-C scalar baseline: \`outputs/b16_p1c_global_polarization_b14_split_10mev_2026-11-10.json\`
- Profile: \`data/sfho188_digitized.csv\`

**P1-D boundary sensitivity is complete for the 210--510 MeV band and the \(m_V=10\) MeV strong-endpoint benchmark.** The paper-faithful boundary remains 25 km. The next useful question is whether the original neutrino transport model supports an energy-dependent \(R_\nu(\omega)\) or a different effective trapping surface; without such evidence, no alternative boundary is adopted.


## References

N. Blinov, P. J. Fox, K. J. Kelly, R. Plestid, and T. Zhou, “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” arXiv:2511.09619, Appendix B, especially Eqs. (B.1)--(B.5) and the discussion of \(R_{\max}=R_\nu\simeq25\) km.


## 8. Consistency qualification for the outward extension

A follow-up check of Lai, Leung, and Lin (2024), the work cited for the \(R_{\max}=R_\nu\) prescription, makes an important qualification explicit: the production and attenuation regions must be treated consistently. If the attenuation radius is extended from \(R_\nu\) to the gain radius \(R_{\rm gain}\sim100\) km, the BSM-boson production region must be extended to the same domain. Their calculation finds that this consistent extension changes the luminosity little because the relevant particle densities fall rapidly outside the neutrinosphere.

Consequently, the 26--30 km rows above are **one-sided opacity-only diagnostics**, not self-consistent alternative luminosity predictions. They quantify the sensitivity to extra trapping optical depth, but must not be used as a correction to the paper's result. The inward scan is also source-frozen by design; in the selected 210--510 MeV band, the source fraction outside 15 km is below \(10^{-6}\), so this distinction is negligible for the inward results shown.

Reference: K.-C. Lai, C. S. J. Leung, and G.-L. Lin, Phys. Rev. D 110, 103023 (2024), arXiv:2401.16023, especially the discussion of matching the production and attenuation regions.


## 9. P1-F follow-up: energy-dependent daughter-neutrino decoupling

The follow-up is completed at the literature and kinematic level in \`B16_P1F_ENERGY_DEPENDENT_NEUTRINOSPHERE_AND_HIGH_ENERGY_DAUGHTERS_2026-11-10.md\`.

For \(m_V=10\) MeV and \(\omega=210\)--\(510\) MeV, the two daughter neutrinos have pair-mean energies \(105\)--\(255\) MeV. Supernova neutrino decoupling is energy- and flavor-dependent; for heavy-flavor states the transport sphere and energy sphere are distinct. Therefore a fixed \(R_\nu\simeq25\) km, usually understood as an effective neutrinosphere radius, is not demonstrated to be the correct energy-loss boundary for this high-energy daughter population.

A deliberately conditional band-only proxy illustrates the scale: the 25-to-30 km P1-D extension suppresses the 210--510 MeV band by \(70.94\%\). If all other energy bins are held fixed, the resulting total-luminosity proxy lies \(2.79\%\) below Fig. 7. This is **not** a full re-integration and does not justify selecting \(R_{\max}=30\) km.

The exact energy-dependent boundary cannot be computed from the current public-figure CSV: same-snapshot baryon density, composition, neutrino moments, and heavy-flavor energy-dependent opacities are missing; the relevant Garching archive endpoints require authorization. Retain \(R_{\max}=25\) km as the literal paper baseline and do not alter the production or axial-vector outputs.


## 10. P1-G public-density transport envelope

P1-G, \`B16_P1G_PUBLIC_DENSITY_NEUTRINO_TRANSPORT_ENVELOPE_2026-11-10.md\`, uses Caputo et al. Fig. 1 for the same SFHo-18.8, 1 s \(n_B(r)\) profile through 20 km and the published approximate \(\nu N\) mean-free-path scaling. Under the central exponential-tail read-off, the radial transport radii for 100, 150, 255, and 500 MeV daughters are approximately 22.4, 23.3, 24.6, and 26.2 km. The figure-read-off stress envelope gives about 22.6--27.8 km for the 255--500 MeV tail.

This is a transport-only estimate, not the heavy-flavor energy sphere. The energy-weighted daughter-pair escape proxy transitions smoothly through 25--30 km. Thus 25 km is plausible for much of the pair energy, while the highest-energy daughters can remain partially transport-thick beyond 25 km. The full 30 km sharp-boundary P1-D extension remains an extreme conditional opacity diagnostic and is not promoted to a physical prediction.

The exact energy sphere still requires same-snapshot energy-changing collision kernels and neutrino moments, which are not available in the public reconstruction. Retain the literal 25 km baseline.
