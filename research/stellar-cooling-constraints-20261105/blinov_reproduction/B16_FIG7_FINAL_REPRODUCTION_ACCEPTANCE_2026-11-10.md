# Pure-vector Fig. 7 reproduction: consolidated acceptance status

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV, pure vector, \(s18.8\)-SFHo-MUONS, \(t_{\rm pb}=1\) s  
Working profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Executive decision

**The numerical implementation of the literal published B.1--B.19 prescription is internally cross-checked, but the physical reproduction of the 10 MeV Fig. 7 curve is not passed.**

The higher-resolution current-profile result differs from the digitized Fig. 7 curve by:
- weak endpoint: \(-9.2240\%\);
- reference peak: \(+2.2315\%\);
- strong endpoint: \(+92.2600\%\).

The weak-end discrepancy is already present in the optically-thin B.1 source. The strong-end discrepancy is dominated by the B.2 escape/opacity calculation. The tested integration errors and current-profile sensitivities do not explain either residual.

No source or opacity rescaling, no fitted lapse or thermodynamic profile, no change of \(R_{\max}\), and no update of the axial-vector constraint curve is authorized by this audit.

## 2. Numerical baseline and Fig. 7 comparison

The current higher-resolution independent fixed-\(\omega\) B.1+B.2 calculation gives:

| Fig. 7 point | \(g\) | \(L_{\rm Fig.7}\) (erg/s) | \(L_{\rm calc}\) (erg/s) | Relative residual | \(P_{\rm esc}\) |
|---|---:|---:|---:|---:|---:|
| Weak | \(4.79643\times10^{-10}\) | \(1.08933\times10^{52}\) | \(9.88850\times10^{51}\) | \(-9.2240\%\) | 0.997871 |
| Peak | \(1.13411\times10^{-8}\) | \(1.91099\times10^{54}\) | \(1.95364\times10^{54}\) | \(+2.2315\%\) | 0.352625 |
| Strong | \(4.17169\times10^{-8}\) | \(1.26781\times10^{52}\) | \(2.43750\times10^{52}\) | \(+92.2600\%\) | \(3.25163\times10^{-4}\) |

The current B.1 thin source is
\[
L_{\rm thin}^{\rm B.1}/g^2
=4.3074474\times10^{70}\ {\rm erg\,s^{-1}}.
\]
At the weak endpoint, the source-only result is \(-9.0303\%\) below Fig. 7 and \(P_{\rm esc}=0.997871\). The weak residual is therefore a source-side mismatch, not a trapping effect.

At the reference peak, the optically-thin source is about 2.91 times the digitized luminosity, while \(P_{\rm esc}\simeq0.353\). The final near-agreement is a compensation between source normalization and attenuation; it is not an independent validation of both.

At the strong endpoint, the optically-thin luminosity is about \(5.93\times10^3\) times Fig. 7, and transport suppresses it by \(P_{\rm esc}\simeq3.25\times10^{-4}\). The result nevertheless remains \(92.26\%\) above the digitized curve.

## 3. Numerical implementation checks

The following numerical checks have passed at the stated scope:

1. **B.1 source integration:** independent radial/energy integration agrees with the archived source at the sub-percent level. The 200-radius/320-base-energy implementation is stable under the recorded joint refinement.
2. **Full B.1+B.2 integration:** the independent integration agrees with the archived high-order B.16 luminosity to about \(0.07\%\), \(0.08\%\), and \(0.11\%\) at the weak, peak, and strong points in the current cross-runtime comparison.
3. **B.2 chord and angular integration:** the independent analytic piecewise-linear chord integration and the full angular escape average agree with the path-quadrature implementation at the already recorded sub-percent or better level.
4. **Opacity interpolation:** direct evaluation of the local kernel from the 1687 profile vertices changes the sampled total optical depth relative to the 642-node opacity interpolation by at most \(9.07\times10^{-6}\).
5. **Local kernels and detailed balance:** the B.7--B.10 neutrino inverse-decay kernel and the B.14--B.19 reference Compton chain have independent algebraic, phase-space, and detailed-balance checks. No definite missing factor of two or three is identified in the literal scalar baseline.
6. **Fig. 7 digitization:** the visible source-PDF vertices are reproduced by the stored digitization. No visible-tail coordinate or coupling-axis swap is found.

These checks establish numerical consistency of the implemented prescription. They do not establish that the reconstructed public-figure profile is identical to the unpublished simulation input used to produce Fig. 7.

## 4. Source-side discrepancy: what has been tested

The current source profile has the following provenance status:

- \(T(r)\) and \(\mu_\mu/T\) in the main 5--20 km region agree with Bollig Figs. 1 and 4 at the \(10^{-4}\) relative level.
- Caputo's plotted muon density is internally consistent with its \(T,\mu_\mu\) Fermi reconstruction. Bollig Fig. 3 remains about 5--10% lower over parts of the muon-rich region, but B.17 fixes \(n_\mu F_{\rm deg}\) from the same distribution. The density ratio is not a justified standalone source rescaling.
- Global \(\pm30\%\) stresses of \(\mu_{\nu_\mu}\) change the total B.1 source by \(+0.555\%\) and \(-0.656\%\); setting it to zero changes the source by \(+1.174\%\). The diagnostic \(\mu_{\nu_\tau}=\mu_{\nu_\mu}\) alternative changes it by \(-1.174\%\).
- The outer 24--25 km lapse continuation changes the full strong-point B.1+B.2 luminosity by at most \(0.0262\%\).
- Matching the weak Fig. 7 source by changing the interior lapse would require a \(+4.97\%\) rescaling over 5--15 km or \(+6.03\%\) over 8--15 km. The independent public lapse visualization agrees with the current profile at the few-\(10^{-3}\) absolute read-off level; it does not support a \(0.04\)--\(0.05\) lapse shift.

The source-side tests therefore identify no evidence-based profile adjustment that accounts for the \(-9.03\%\) weak-end B.1 deficit.

## 5. Strong-end transport discrepancy: what has been tested

At \(m_V=10\) MeV:
- neutrino inverse decay supplies about \(67.93\%\) of the thin B.1 source;
- semi-Compton supplies about \(32.07\%\);
- neutrino inverse decay supplies about \(89.8\%\) of the source-weighted mean optical depth, with semi-Compton supplying about \(10.2\%\);
- the 210--510 MeV interval contains about \(9.67\%\) of the thin source but about \(69.76\%\) of the escaping luminosity.

The escape integral is controlled by the correlation among emission radius, energy, direction, and the entire chord. A source-weighted mean optical depth cannot be exponentiated in place of the full average of \(e^{-\tau}\).

The following B.2 tests do not close the discrepancy:
- direct local-kernel versus opacity-table interpolation changes total sampled \(\tau\) by at most \(9.07\times10^{-6}\);
- \(\pm10\%\) \(\mu_{\nu_\mu}\) changes the 210--510 MeV escaped band by less than \(0.03\%\);
- a \(\pm30\%\) temperature stress in 22--25 km changes the 210--510 MeV band by only about \(\pm0.39\%\);
- the path-redshift-only alternative changes the dominant 210--510 MeV band by \(-28.09\%\) and reduces the strong-end residual, but it remains a separate propagation prescription and does not reproduce Fig. 7;
- replacing B.14--B.16 by the exact moving-muon B.13 source and opacity together moves the strong-end result further above Fig. 7.

The literal fixed-\(\omega\), Euclidean-chord B.2 expression remains the reproduction baseline because that is what the paper prints. The path-redshift and mode-resolved calculations remain separately labelled diagnostics.

## 6. Boundary and gravity prescription

The adopted \(R_{\max}\simeq25\) km is supported by the literature's approximate \(T\simeq3\) MeV neutrinosphere convention. The current profile gives \(T(25\,{\rm km})\simeq3.03\) MeV.

The published B.1 source uses the lapse-squared factor and the local-energy threshold \(m_V/N(r)\). The local-energy B.1 form and its exact \(E_\infty=N(r)\omega_{\rm loc}\) change of variables have been reconciled. The printed B.2 path integral uses a fixed \(\omega\) along Euclidean chords; it does not include a proper spatial metric, geodesic bending, or an explicit path-dependent lapse conversion.

The missing spatial metric \(A(r)\) is therefore not required to reproduce the paper's printed approximation. It would be required for a separate full-GR transport extension.

### 6.1 Energy-dependent daughter-neutrino decoupling

The fixed \(R_{\max}=R_\nu\simeq25\) km prescription is retained literally, but P1-F identifies an unresolved physical limitation: the neutrinosphere is energy- and flavor-dependent, and for heavy-flavor neutrinos the transport sphere and energy sphere are distinct. The 210--510 MeV vector band produces \(\nu_\mu,\bar\nu_\mu,\nu_\tau,\bar\nu_\tau\) daughters with pair-mean energies \(105\)--\(255\) MeV. A thermal-average 25 km radius is not demonstrated to be the energy-loss boundary for this daughter population.

The P1-D conditional outward-boundary scan shows that extending the 210--510 MeV trapping region from 25 to 30 km with the vacuum-limit neutrino-decay opacity suppresses that band by \(70.94\%\). In a separate V8 cross-runtime phase-space diagnostic, the band carries \(69.76\%\) of the escaped luminosity; replacing only that band by its 30 km conditional value while holding all other energy bins fixed gives a total-luminosity proxy \(2.79\%\) below Fig. 7. This is a band-only arithmetic diagnostic, not a full re-integration or a physical prediction for \(R_{\max}=30\) km. The V8 input is not strict NumPy-grid acceptance because its generated grid hashes differ, despite the reported integral closure.

The comparison shows that an energy-dependent daughter-neutrino energy sphere could be a decisive physical uncertainty. It does **not** justify changing \(R_{\max}\): the required same-snapshot baryon density, composition, neutrino moments, and energy-dependent heavy-flavor opacities are not present in the reconstructed CSV, and the relevant Garching archive endpoints require authorization.

The physically relevant extension is an energy-weighted \(\nu\bar\nu\)-pair escape/reprocessing probability, not an arbitrary fitted sharp radius. The P1-F report documents the kinematics, the conditional band-only proxy, the required transport input, and the stopping decision.

### 6.2 Public-density transport envelope

P1-G uses Caputo et al. Fig. 1, which gives the same SFHo-18.8, \(t_{\rm pb}=1\) s baryon-density profile through 20 km, together with the published approximate \(\nu N\) mean-free-path scaling. A figure-level exponential-tail estimate gives central radial transport radii of about 22.4, 23.3, 24.6, and 26.2 km for daughter energies 100, 150, 255, and 500 MeV. The broad figure-read-off envelope gives about 22.6--27.8 km for the 255--500 MeV tail.

In the central tail model, the equal-polarization pair-energy survival proxy over the ten 210--510 MeV vector nodes ranges from 0.470 to 0.843 at 25 km, 0.898 to 0.978 at 27.5 km, and 0.986 to 0.997 at 30 km. This is a transport-only estimate, not the heavy-flavor energy sphere; the full energy-changing collision kernels are missing.

The public-density estimate therefore makes \(R_{\max}=25\) km plausible for much of the daughter-pair energy, while allowing partial reprocessing of the highest-energy tail outside 25 km. It does not support treating 30 km as a uniquely determined boundary. The P1-D 30 km result remains an extreme sharp-boundary sensitivity test, not a physical prediction. The leading boundary uncertainty is now narrowed to a smooth, energy-dependent transition around roughly 25--28 km in the figure-level transport estimate, with the actual energy sphere still unresolved. In the central-tail radial diagnostic, the smooth 25--30 km reprocessing fraction averages \(8.91\%\) across the ten vector-energy nodes (3.91%--16.05% node range), compared with the 100% reprocessing implicit in the sharp P1-D 30 km extension. This is not a full source- and angle-weighted B.2 integral, but confirms that the 30 km extension is an extreme upper bound, not a preferred correction. P1-H then inserted this smooth factor into the full 210--510 MeV B.2 ray integral. The central equal-mode tail changes the band by only \(-4.14\%\), the high-density tail by \(-10.60\%\), and the low-density tail by \(-0.33\%\); their band-only total proxies remain \(+86.87\%\), \(+78.21\%\), and \(+91.98\%\) above Fig. 7. The sharp 30 km near-match is therefore not reproduced by the smooth public-density transport model.

## 7. Remaining limitation and acceptance decision

The original Garching \(s18.8\)-SFHo-MUONS numerical profile and the authors' numerical implementation are not available in the public repository. The current 1687-row input is a reconstruction from published figures and public visualizations. Its provenance has been cross-checked, but it is not the raw simulation table.

Accordingly:

- **Numerical implementation:** internally cross-checked.
- **Public-profile provenance:** partially cross-checked; raw same-snapshot input unavailable.
- **Weak-end Fig. 7 reproduction:** not passed; \(-9.03\%\) source-side residual.
- **Peak Fig. 7 reproduction:** near agreement, but due compensation between source and escape.
- **Strong-end Fig. 7 reproduction:** not passed; \(+92.26\%\) residual.
- **Physical correction:** none established.

Keep PR #57 Draft/Open. Do not merge it as a validated reproduction, do not update the axial-vector constraint curve, and do not tune the opacity, source, lapse, coupling, or outer boundary to match Fig. 7.

If no authorized same-snapshot profile or new source-level evidence becomes available, the correct endpoint is to retain this as an explicitly documented reproduction limitation rather than to continue unmotivated parameter scans.

## 8. Main audit records

- \`B16_EQUATION_TO_CODE_RECONCILIATION_2026-11-10.md\`
- \`B16_PUBLISHED_GRAVITY_AND_ENERGY_PRESCRIPTION_RECONSTRUCTION_2026-11-09.md\`
- \`B16_P1E_NEUTRINOSPHERE_AND_PROFILE_PROVENANCE_AUDIT_2026-11-10.md\`
- \`B16_P1E2_B1_NEUTRINO_CHEMICAL_POTENTIAL_SOURCE_SENSITIVITY_2026-11-10.md\`
- \`B16_P1E3_INTERIOR_LAPSE_B1_SOURCE_SENSITIVITY_2026-11-10.md\`
- \`B16_P1C_POLARIZATION_NORMALIZATION_AND_GLOBAL_MODE_TRANSPORT_2026-11-10.md\`
- \`B16_P1B2_THERMODYNAMIC_INTERPOLATION_AND_INPUT_SENSITIVITY_2026-11-10.md\`
- \`B16_HIGH_ENERGY_CHANNEL_KERNEL_AUDIT_2026-11-10.md\`
- \`TEN_MEV_STRONG_ENDPOINT_DIAGNOSIS_2026-11-09.md\`

No manuscript, referee response, production axial-vector output, or constraint curve is modified by this acceptance report.
