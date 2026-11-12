# P1-F: Energy-dependent neutrino decoupling and high-energy vector-decay daughters

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: pure vector, \(m_V=10\) MeV, \(g=4.171689650228597\times10^{-8}\)  
Energy interval: \(210\leq\omega\leq510\) MeV  
Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Question and motivation

The numerical B.2 path integral, angular average, opacity interpolation, channel decomposition, and scalar polarization normalization have been independently checked. P1-D then showed that the 210--510 MeV escaped band is highly sensitive to the outer trapping boundary.

The physical interpretation of \(R_{\max}=R_\nu\simeq25\) km is therefore the remaining important issue. In Blinov et al., \(R_{\max}\) is not merely a numerical cutoff: it is the radius beyond which a vector decay is assumed to constitute energy loss because the daughter neutrinos escape. The paper adopts one fixed effective neutrinosphere radius.

This audit asks whether a single thermal-average radius is demonstrably appropriate for the highly energetic \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) daughters produced by the strongly boosted 10 MeV vector bosons in the 210--510 MeV band.

## 2. What the cited prescription establishes

Blinov et al. state that \(R_{\max}\) is the same as the minimum radius beyond which \(V\) must decay to count as energy loss, and identify it with \(R_\nu\simeq25\) km. This is the literal baseline retained by the project.

Lai, Leung, and Lin (2024), the work cited for this choice, emphasize that the production and attenuation regions must be treated consistently. If the attenuation region is extended from the neutrinosphere to the gain radius, the production region must also be extended. Their calculation finds only a small change for that consistent extension because the relevant particle densities fall rapidly outside the neutrinosphere.

Neither statement demonstrates that 25 km is the energy-dependent energy-decoupling radius of 100--250 MeV heavy-flavor neutrinos in the exact SFHo-18.8, \(t_{\rm pb}=1\) s snapshot.

## 3. Daughter-neutrino kinematics

For a vector of local energy \(\omega\), mass \(m_V\), and speed
\[
\beta=\sqrt{1-\frac{m_V^2}{\omega^2}},
\]
the two massless daughters have energies
\[
E_{1,2}=\frac{\omega}{2}(1\pm\beta z),\qquad z=\cos\theta_*.
\]
Thus
\[
E_{\min,\max}=\frac{\omega}{2}(1\mp\beta),
\qquad
\frac{E_1+E_2}{2}=\frac{\omega}{2}
\]
for every decay event.

At \(m_V=10\) MeV:

| Vector energy \(\omega\) | \(E_{\min}\) | \(E_{\max}\) | Pair-mean daughter energy |
|---:|---:|---:|---:|
| 210 MeV | 0.119 MeV | 209.881 MeV | 105 MeV |
| 300 MeV | 0.083 MeV | 299.917 MeV | 150 MeV |
| 510 MeV | 0.049 MeV | 509.951 MeV | 255 MeV |

The energy distribution is broad: one daughter can be soft while its partner carries almost the entire vector energy. A number-averaged daughter energy or a single representative neutrino energy is therefore not enough; the relevant quantity is the fraction of the *pair energy* that escapes.

For the polarization weights used in the P1-C two-body kinematics,
\[
W_L(z)=\frac34(1-z^2),\qquad
W_\pm(z)=\frac38(1\pm z)^2,
\]
each mode integrates to one and \(W_L+W_++W_-=3/2\). The equal-polarization average is useful as a reference, but the actual production polarization density matrix is channel- and phase-space-dependent. The archived scalar B.16 result does not contain the full daughter-neutrino transport distribution.

For an equal-polarization kinematic reference, the energy fractions carried by daughters above a threshold are:

| \(\omega\) | \(E_\nu>20\) MeV | \(E_\nu>50\) MeV | \(E_\nu>100\) MeV |
|---:|---:|---:|---:|
| 210 MeV | 99.08% | 94.31% | 77.36% |
| 300 MeV | 99.57% | 97.28% | 88.97% |
| 510 MeV | 99.85% | 99.02% | 96.09% |

These are energy fractions, not number fractions. Mode-resolved values are archived in the JSON output. The polarization dependence is modest for the 20--50 MeV cuts and more visible for higher cuts; it does not remove the high-energy character of the daughter population.

## 4. Why a fixed 25 km radius is not automatically an energy-resolved boundary

A neutrinosphere is conventionally defined through an optical-depth condition, schematically
\[
\tau_\nu(E,r)=\int_r^\infty\frac{dr'}{\lambda_\nu(E,r')}\simeq\frac23.
\]
The radius depends on neutrino energy and flavor. Weak scattering opacities on nucleons grow approximately as \(E_\nu^2\), so high-energy neutrinos generally decouple farther out than lower-energy neutrinos.

For heavy-flavor neutrinos, there is an additional distinction between:
- the **transport sphere**, associated with the last scattering that changes the propagation direction;
- the **energy sphere**, associated with the last energy-changing interaction.

The latter distinction matters here. A vector decay transfers energy to a \(\nu\bar\nu\) pair. If the daughters scatter or exchange energy with the medium before escaping, some or all of the vector energy is reprocessed. A transport radius alone is not automatically the correct energy-loss boundary.

The 2025 review by Raffelt, Janka, and Fiorillo describes the neutrino decoupling region as energy- and flavor-dependent, extending over tens of kilometres, and explicitly distinguishes the heavy-flavor transport and energy spheres. Müller (2019) discusses the outward shift of high-energy neutrino decoupling due to the energy dependence of weak opacities.

This literature supports treating \(R_\nu\simeq25\) km as an effective fixed-radius approximation, not as a demonstrated energy-independent boundary for the high-energy daughter neutrinos in this benchmark.

## 5. Quantitative connection to the existing P1-D boundary scan

The high-order phase-space result gives:
- \(9.6696\%\) of the optically thin B.1 source in the 210--510 MeV band;
- \(69.7557\%\) of the escaped luminosity in the same band;
- a total fixed-\(\omega\) luminosity \(2.43964\times10^{52}\) erg/s;
- a digitized Fig. 7 reference \(1.26781\times10^{52}\) erg/s;
- a baseline residual \(+92.4284\%\).

The P1-D calculation holds the B.1 source fixed and adds the two-flavour vacuum-limit neutrino inverse-decay opacity outside 25 km, conditional on the daughter neutrinos remaining trapped there. It gives the following 210--510 MeV band response:

| Conditional outer boundary | Band change relative to 25 km | Band-only total-luminosity proxy residual |
|---:|---:|---:|
| 25 km | 0 | +92.43% |
| 26 km | -22.42% | +62.34% |
| 27.5 km | -46.64% | +29.82% |
| 30 km | -70.94% | -2.79% |

The last column is deliberately only an arithmetic diagnostic: it replaces the 210--510 MeV band by the P1-D value and holds every other energy bin fixed. It is **not** a full luminosity re-integration, and it is not a physical prediction for \(R_{\max}=30\) km.

Nevertheless, the comparison is important. If the high-energy band alone were suppressed by \(68.86\%\), the full luminosity would reach the digitized Fig. 7 value with all other bins held fixed. The conditional 25-to-30 km band extension suppresses it by \(70.94\%\). Thus the outer-boundary sensitivity is large enough to be of the same order as the remaining strong-endpoint discrepancy.

This does not justify choosing 30 km. It identifies the energy-dependent neutrino energy-decoupling surface as a potentially decisive missing physical input.

## 6. Consistency with the production-region requirement

Lai et al. require the production and attenuation domains to be extended consistently. The P1-D outward rows are one-sided opacity-only diagnostics and do not satisfy that requirement as complete alternative models.

There is, however, a useful benchmark-specific observation: in the reconstructed profile, less than \(10^{-6}\) of the 210--510 MeV B.1 source lies outside 15 km. Therefore the source in the selected band is already extremely concentrated well inside 25 km. Extending the high-energy-band production domain beyond 25 km may consequently add very little source, but this cannot be proved without the raw profile beyond 25 km.

The 26--30 km rows must therefore remain conditional sensitivity tests. They must not be promoted to corrected Fig. 7 predictions.

## 7. The physically relevant generalization

A sharp \(R_\nu\) approximates the daughter-pair energy escape fraction by a step function: zero inside the neutrinosphere and unity outside. For a boosted vector decay, the more physical object is the energy-weighted pair escape fraction
\[
P_{\nu\bar\nu}^{E}(\omega,r)=
\frac{1}{\omega}
\sum_{h,\alpha} w_{h\alpha}(\omega,r)
\int_{-1}^{1}dz\,W_{h\alpha}(z)
\left[
E_1P_{\nu_\alpha}^{\rm esc}(E_1,r)
+
E_2P_{\bar\nu_\alpha}^{\rm esc}(E_2,r)
\right],
\]
where \(\alpha=\mu,\tau\), \(h\) labels vector polarization, and the weights \(w_{h\alpha}\) must be derived from the production density matrix and normalized consistently.

The part of the vector-decay energy that is reprocessed is then proportional to
\[
1-P_{\nu\bar\nu}^{E}(\omega,r).
\]
A transport extension would therefore replace the sharp neutrino-decay loss/absorption boundary by a daughter-energy-dependent reprocessing probability. The semi-Compton channel, which transfers energy directly to the muon-photon medium, must remain separately treated.

This is a proposed physical extension, not a change to the literal published B.2 equation. It requires neutrino transport information that is not present in the current reconstructed profile.

## 8. Missing inputs and stopping decision

The current public-figure CSV contains \(r,T,\mu_\mu,\mu_{\nu_\mu}\), and the lapse. Caputo et al. Fig. 1 additionally gives a figure-level \(n_B(r)\) read-off for the same SFHo-18.8, 1 s snapshot, but only through 20 km. P1-G uses that plot to construct an explicitly approximate exponential outer tail; it is not a raw density table.

The inputs still missing for a genuine energy-sphere calculation are:
- the raw same-snapshot baryon-density profile and composition beyond 20 km;
- energy- and flavor-dependent \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) collision opacities;
- neutrino angular moments and distribution functions needed to distinguish transport from energy decoupling;
- the energy-changing pair-process opacity that determines the heavy-flavor energy sphere.

The official Garching archive lists radial neutrino moments/spectra and hydro profiles, but the relevant endpoints return HTTP 401 without authorization. No access control is bypassed and no substitute snapshot is spliced into the benchmark.

**Decision:**
1. Retain \(R_{\max}=25\) km as the literal Blinov equation-level baseline.
2. Do not adopt 26, 27.5, or 30 km by fitting Fig. 7.
3. Record energy-dependent daughter-neutrino decoupling as the leading unresolved physical boundary issue for the strong 10 MeV endpoint.
4. Do not change the scalar B.2 opacity normalization, the source, the profile, or the axial-vector curve.
5. If authorized same-snapshot neutrino transport data become available, compute \(P_{\nu\bar\nu}^{E}(\omega,r)\) before revisiting the boundary. Otherwise classify the strong-endpoint difference as unresolved by the public data.

## 9. Reproducibility

- Analytic kinematics and boundary-proxy script: \`audit_b16_energy_dependent_neutrinosphere_daughters.js\`
- Machine-readable result: \`outputs/b16_energy_dependent_neutrinosphere_daughters_10mev_2026-11-10.json\`
- Boundary input: \`outputs/b16_rmax_boundary_sensitivity_10mev_2026-11-10.json\`
- High-order phase-space input: \`outputs/b16_escape_phase_space_10mev_2026-11-10_v8_crosscheck.json\`

The phase-space input is a direct V8 cross-runtime check. Its node counts and integral closures match the high-order baseline, but its NumPy-generated grid hashes are not bitwise identical; it is not strict NumPy-grid acceptance. The P1-D boundary calculation remains independently closed against the archived P1-C band result.

## References

1. N. Blinov, P. J. Fox, K. J. Kelly, R. Plestid, and T. Zhou, “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” JHEP 06 (2026) 155, arXiv:2511.09619, Appendix B.
2. K.-C. Lai, C. S. J. Leung, and G.-L. Lin, “SN1987A constraints to BSM models with extra neutral bosons near the trapping regime,” Phys. Rev. D 110, 103023 (2024), arXiv:2401.16023.
3. G. G. Raffelt, H.-T. Janka, and D. F. G. Fiorillo, “Neutrinos from core-collapse supernovae,” 2025 review manuscript, Sec. 2.2.
4. B. Müller, “Neutrino Emission as Diagnostics of Core-Collapse Supernovae,” Annu. Rev. Nucl. Part. Sci. 69, 253--278 (2019), DOI: 10.1146/annurev-nucl-101918-023434.


## 10. Public-density follow-up

P1-G, \`B16_P1G_PUBLIC_DENSITY_NEUTRINO_TRANSPORT_ENVELOPE_2026-11-10.md\`, uses Caputo et al. Fig. 1 for the same SFHo-18.8, 1 s baryon-density profile through 20 km. A figure-level exponential-tail estimate gives a central radial transport radius of about 22.4 km at 100 MeV, 24.6 km at 255 MeV, and 26.2 km at 500 MeV. The broad figure-read-off envelope spans roughly 22.6--27.8 km for the 255--500 MeV high-energy tail.

The transport-only pair-energy escape proxy rises smoothly across 25--30 km. This makes \(R_{\max}=25\) km plausible for much of the pair energy, while allowing the high-energy tail to remain partially transport-thick outside 25 km. It does not establish the energy sphere; the full energy-changing collision terms remain unavailable. The P1-D sharp 30 km extension is therefore an extreme conditional bound, not a preferred boundary.

P1-G narrows the boundary uncertainty but does not select a new \(R_{\max}\) or alter the literal B.2 baseline.
