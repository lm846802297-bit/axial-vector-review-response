# P1-E: neutrinosphere boundary and joint profile provenance audit

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Working profile: vertex-preserving public-figure reconstruction of SFHo-18.8 at \(t_{\rm pb}=1\) s  
Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`  
Profile Git blob: \`e41df78c8035540760fbcb7ef592cd830171822e\`

## 1. Objective

Consolidate the provenance status of the three background inputs relevant to the B.1/B.2 calculation:
- temperature \(T(r)\);
- muon and muon-neutrino chemical potentials \(\mu_\mu(r)\), \(\mu_{\nu_\mu}(r)\);
- gravitational lapse \(N(r)\).

Then test whether the adopted \(R_{\max}=25\) km boundary has an independent physical anchor, rather than treating it as an arbitrary numerical cutoff.

This is a source/provenance adjudication. It does not change the working profile, B.1 source, B.2 opacity, \(R_{\max}\), Fig. 7 curve, or axial-vector result.

## 2. Joint provenance matrix

| Input | Current source | Independent check | Status |
|---|---|---|---|
| \(T(r)\), 0--20 km | Caputo et al., arXiv:2109.03244v3, Fig. 1 vector path | Bollig et al., arXiv:2005.07141v7, Fig. 1; Ferreira et al. Fig. 1 | Strong figure-level cross-check |
| \(T(r)\), 20--25 km | Caputo PDF off-frame vector path | No independent Bollig Fig. 1 comparison beyond its plotted range | Encoded public-source continuation; not raw data |
| \(\mu_\mu/T\), 0--20 km | Caputo Fig. 1 \(\mu_\mu\) and \(T\) paths | Original Bollig Fig. 4 | Strong figure-level cross-check; Caputo selected over Ferreira |
| \(\mu_\mu(r)\), 20--22.19 km | Caputo off-frame vector path | No independent Bollig Fig. 4 check in this interval | Encoded public-source continuation |
| \(\mu_{\nu_\mu}(r)\) | Caputo Fig. 1 negative/positive branches | Original Bollig Fig. 3 is a density plot, not a direct \(\mu_{\nu_\mu}\) validation | Sign/support and local-rate sensitivities checked; exact profile provenance incomplete |
| \(N(r)\), 0--20 km | Ferreira et al., arXiv:2510.14469v1, Fig. 1 lapse path | Zuowei Liu presentation, 2026-10-31, slide 65, attributed to the SFHo-18.8/Bollig model | Independent visual corroboration only |
| \(N(r)\), 20--24 km | Ferreira Fig. 1 lapse path | No independent numerical table identified | Public-figure reconstruction only |
| \(N(r)\), 24--25 km | Matched Schwarzschild exterior continuation from the 24 km endpoint | No same-snapshot mass/lapse table | Explicit model continuation, not a digitized simulation output |

The exact source-PDF hashes, drawing-path indices, axis maps, and retained profile vertices are recorded in \`data/profile_provenance.json\` and \`extract_profile.py\`.

## 3. Temperature and charged-muon degeneracy

The Caputo \(T(r)\) and \(\mu_\mu/T\) curves are independently compared with the original Bollig figures. The comparisons are especially precise in the regions carrying most of the B.1 source and B.2 opacity:
- 12--15 km: Caputo \(T\) and \(\mu_\mu/T\) agree with Bollig Figs. 1 and 4 at the \(10^{-4}\) relative scale;
- 15--20 km: mean absolute relative differences are \(0.00431\%\) for \(T\) and \(0.00468\%\) for \(\mu_\mu/T\), with maxima \(0.01628\%\) and \(0.01547\%\), respectively;
- the Caputo--Ferreira \(\mu_\mu\) discrepancy is not a free baseline ambiguity: the direct original Bollig Fig. 4 comparison selects Caputo for the SFHo-18.8, 1 s benchmark.

The absolute muon-density comparison in Bollig Fig. 3 remains inconsistent with the density reconstructed from the published \(T,\mu_\mu/T\) curves in parts of the outer region. This is a separate source-level tension. It does not justify a standalone rescaling of \(n_\mu F_{\rm deg}\), because the B.17 susceptibility is defined from the same distribution. The density tension must remain documented rather than folded into an invented uncertainty band.

The 20--22 km Caputo \(T,\mu_\mu\) segments are encoded in off-frame PDF vector paths. They are not invented extrapolations, but they are outside the visible plotting frame and lack an independent Bollig Fig. 1/Fig. 4 comparison. The 22--25 km temperature path is likewise encoded in the Caputo PDF; the muon chemical potential falls below the plotted 1 MeV floor near 22.19 km and is set to zero thereafter under the existing reconstruction convention.

## 4. Muon-neutrino chemical potential

The reconstructed \(\mu_{\nu_\mu}(r)\) includes a negative branch ending at 13.10993 km, a zero interval, and a positive branch from 16.58818 to 18.42300 km. The exact branch endpoints are retained from the PDF drawing paths with near-step support knots.

For the high-energy 10 MeV inverse-decay kernel:
- the pair integral is even in \(\mu_{\nu_\mu}\), so a sign flip does not change the local kernel;
- direct B.7--B.10 angular integration and the independent closed form agree;
- source-frozen global tests show that \(\pm10\%\) changes in \(\mu_{\nu_\mu}\) change the 210--510 MeV escaped luminosity by less than \(0.03\%\).

There is no comparably precise independent original-Bollig plot that validates the full \(\mu_{\nu_\mu}(r)\) curve. The result is therefore a sensitivity statement, not a claim that the reconstructed chemical-potential profile is known exactly.

## 5. Lapse provenance and the 24--25 km continuation

The lapse path is digitized from the Ferreira SFHo-18.8 curve through \(r=23.9998\) km. Its values agree visually with an independent public presentation of the same SFHo-18.8 core profile over 0--20 km. That presentation is rasterized, so it supports the radial trend and normalization at the few-\(10^{-3}\) level, not a precision residual.

At selected radii, the current profile gives:
| \(r\) (km) | \(N(r)\) |
|---:|---:|
| 0 | 0.73633 |
| 5 | 0.75868 |
| 10 | 0.81136 |
| 15 | 0.86350 |
| 20 | 0.89889 |
| 22 | 0.90850 |
| 24 | 0.91642 |
| 25 | 0.91991 |

The 24--25 km segment is not a measured or digitized lapse curve. It is a Schwarzschild exterior matched continuously to \(N(24\,{\rm km})\), with
\[
r_s=24\,{\rm km}\,[1-N(24\,{\rm km})^2]
=3.8440\,{\rm km}.
\]
This corresponds to an effective exterior mass parameter of about \(1.30\,M_\odot\). It is a continuation convention, not an independently verified enclosed-mass profile. No spatial metric \(A(r)\) is inferred from \(N(r)\).

### Current-profile B.1+B.2 lapse-variant calculation

The earlier 501-row diagnostic is superseded by a current-profile calculation using the active 1687-row profile, SHA-256 \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`. The calculation evaluates the complete fixed-\(\omega\) B.1+B.2 luminosity at the weak, peak, and strong 10 MeV Fig. 7 coupling points. The B.2 opacity is held fixed across the lapse variants, as required by the printed fixed-\(\omega\) prescription; only the B.1 \(N^2\) radial measure and exact lower threshold \(\omega_{\min}=m_V/N(r)\) change.

The higher-resolution run uses 200 source-radius Gauss nodes, 541 global energy nodes (320 logarithmic base nodes plus the threshold union for all variants), 202 opacity-radius nodes, 16 angular nodes, and 32 chord nodes. The muon susceptibility is evaluated with a 96-point Gauss-Legendre integral after the transformation \(p=40t/(1-t)\). A 100-radius/271-energy run provides a joint coarse-to-fine stability check.

The matched Schwarzschild baseline has \(N(23)=0.91265839\), \(N(24)=0.91642363\), and \(N(25)=0.91991249\). Its high-resolution results are:

| Fig. 7 point | \(g\) | \(L_{\rm calc}\) (erg/s) | Relative to Fig. 7 |
|---|---:|---:|---:|
| Weak | \(4.79643\times10^{-10}\) | \(9.88850\times10^{51}\) | \(-9.2240\%\) |
| Peak | \(1.13411\times10^{-8}\) | \(1.95364\times10^{54}\) | \(+2.2315\%\) |
| Strong | \(4.17169\times10^{-8}\) | \(2.43750\times10^{52}\) | \(+92.2600\%\) |

The current-profile lapse variants give the following relative changes in the *full escaped luminosity* compared with the matched Schwarzschild baseline:

| Diagnostic lapse continuation | Thin B.1 source | Weak \(L\) | Peak \(L\) | Strong \(L\) |
|---|---:|---:|---:|---:|
| Freeze \(N(r>24\,{\rm km})=N(24\,{\rm km})\) | \(-1.1607\times10^{-6}\) | \(-1.1522\times10^{-6}\) | \(-1.1503\times10^{-6}\) | \(-2.6199\times10^{-4}\) |
| Linear continuation of the 23--24 km slope | \(+7.3906\times10^{-8}\) | \(+7.3363\times10^{-8}\) | \(+7.5952\times10^{-8}\) | \(+1.9358\times10^{-5}\) |

Thus the largest tested change in the strong-point luminosity is \(2.62\times10^{-4}\), or \(0.0262\%\). The corresponding strong-endpoint residual remains \(+92.26\%\). The 24--25 km lapse continuation is therefore quantitatively excluded as an explanation of the order-one Fig. 7 mismatch.

The high-resolution baseline differs from the archived independent 200-source-node B.1+B.2 result by \(0.0737\%\), \(0.0777\%\), and \(0.1072\%\) at the weak, peak, and strong points, respectively. The joint coarse-to-fine refinement changes the baseline luminosities by \(-0.1551\%\), \(-0.1455\%\), and \(-0.0892\%\), respectively. The variant-to-baseline shifts are stable between the two resolutions: the strong-point freeze shift is \(-2.6181\times10^{-4}\) at lower resolution and \(-2.6199\times10^{-4}\) at higher resolution; the linear-continuation shift is \(+1.9341\times10^{-5}\) and \(+1.9358\times10^{-5}\).

The independent implementation is archived in \`audit_b16_lapse_boundary_current_profile.js\`, with machine-readable results in \`outputs/b16_lapse_boundary_sensitivity_current_profile_10mev_2026-11-10.json\`. This is a cross-runtime V8 calculation, not a bitwise-identical NumPy-grid acceptance run. The freeze and linear profiles are diagnostic brackets, not physical replacements for the matched Schwarzschild continuation.

## 6. Physical anchor for \(R_{\max}\simeq25\) km

There is an independent literature-level anchor for the approximate 25 km radius.

Croon et al., *Supernova Muons: New Constraints on \(Z'\) Bosons, Axions, and ALPs*, arXiv:2006.13942, Sec. 3.2, state that for their \(t_{\rm pb}=1\) s benchmark they take \(R_\nu\simeq25\) km and define it as the radius where the stellar temperature has fallen to \(3\) MeV, approximately consistent with neutrino free streaming.

The current Caputo-derived profile gives:
\[
T(24\,{\rm km})=3.21643~{\rm MeV},\qquad
T(25\,{\rm km})=3.03377~{\rm MeV}.
\]
A local linear extrapolation of the 24--25 km slope would reach \(T=3\) MeV at \(r\simeq25.19\) km. This last number is only a short extrapolation diagnostic; the profile ends at 25 km and it is not a new measured neutrinosphere radius. The direct statement supported by the data is that the 25 km endpoint lies very close to the 3 MeV criterion.

Blinov et al., arXiv:2511.09619, Appendix B, explicitly set \(R_{\max}=R_\nu\simeq25\) km, identifying it as the radius beyond which a vector must decay for its energy loss to affect the neutrino signal. Lai, Leung and Lin, arXiv:2401.16023, explain that production and attenuation domains must be treated consistently: if the attenuation region is extended from the neutrinosphere to the gain radius, the production region must be extended as well; their calculation finds little change because relevant particle densities fall rapidly outside the neutrinosphere.

These statements support the *approximate fixed 25 km convention* used in the reproduction. They do not establish a unique sharp neutrinosphere for all neutrino flavours and energies. In a detailed transport solution, neutrinosphere radii depend on energy and opacity; a single \(R_\nu\) is an effective model boundary.

## 7. Consequence for the Fig. 7 discrepancy

The provenance and current-profile sensitivity audits support the following differentiated conclusions:

1. \(T(r)\) and \(\mu_\mu/T\) in the principal 5--20 km region are strongly anchored to the original Bollig figures. Their measured figure-level differences are too small to explain the strong-endpoint mismatch through ordinary interpolation or digitization errors.
2. The 24--25 km lapse continuation has now been tested in the complete B.1+B.2 luminosity on the current 1687-row profile. The largest tested change is \(0.0262\%\) at the strong point, compared with the \(+92.26\%\) baseline residual. This input is not a viable explanation.
3. \(\mu_{\nu_\mu}(r)\) has weaker independent provenance, but its tested influence on the 210--510 MeV escaped luminosity is below \(0.03\%\) for \(\pm10\%\) changes.
4. The absolute muon-density tension and the outer 20--25 km profile limitations remain real source-level limitations. They are not evidence for an arbitrary opacity correction.
5. The \(R_{\max}=25\) km convention is physically motivated and consistent with the \(T\simeq3\) MeV criterion, but remains an effective, energy-averaged boundary rather than an exact energy-/flavour-resolved neutrinosphere.
6. The 25 km choice is not selected by fitting Fig. 7. Its sensitivity is quantified separately in P1-D; no alternative boundary is adopted.

The pure-vector Fig. 7 physical reproduction therefore remains **not passed**. The current-profile lapse ambiguity has been tested and is far too small to account for the remaining strong-endpoint discrepancy.

## 8. Next action

The current-profile source/provenance sequence P1-E1--P1-E3 is complete:
- P1-E1 tested the 24--25 km lapse continuation in full B.1+B.2;
- P1-E2 tested \(\mu_{\nu_\mu}(r)\) and the \(\mu_{\nu_\tau}=0\) assumption in B.1;
- P1-E3 tested the interior lapse normalization in the dominant 8--15 km and 5--15 km source regions.

None identifies a supported profile adjustment that explains the weak-end source deficit. The interior lapse would need a \(+4.97\%\) to \(+6.03\%\) shift, while the independent public lapse visualization differs from the current profile only at the few-\(10^{-3}\) absolute read-off level. The neutrino chemical-potential tests change the total B.1 source by at most about \(1.17\%\).

Do not continue broad profile stress scans or fit any input to Fig. 7. Without the original same-snapshot Garching table, further profile variation would be arbitrary.

The remaining work belongs to the pure-vector reproduction status rather than the P1-E profile audit:
1. preserve the literal fixed-\(\omega\) B.2 prescription as the published-equation baseline;
2. keep the path-redshift alternative as a separate sensitivity result;
3. consolidate the residuals and all completed numerical/provenance checks into a final Fig. 7 acceptance report;
4. do not update the axial-vector constraint curve or merge the research PR as a validated reproduction while the \(+92.26\%\) strong-endpoint residual remains.

No production code, source normalization, opacity, coupling, profile, Fig. 7 curve, or axial-vector result is modified by P1-E1--P1-E3.

## References

1. N. Blinov et al., *\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae*, arXiv:2511.09619, Appendix B, especially Eqs. (B.1)--(B.5).
2. K.-C. Lai, C. S. J. Leung, and G.-L. Lin, *SN1987A constraints to BSM models with extra neutral bosons near the trapping regime*, arXiv:2401.16023, especially the discussion of consistent production and attenuation domains.
3. D. Croon, G. Elor, R. K. Leane, and S. D. McDermott, *Supernova Muons: New Constraints on \(Z'\) Bosons, Axions, and ALPs*, arXiv:2006.13942, Sec. 3.2.
4. R. Bollig et al., *Muons in Supernovae: Implications for the Axion-Muon Coupling*, arXiv:2005.07141v7, Figs. 1, 3, and 4.
5. A. Caputo et al., *Muonic boson limits: Supernova redux*, arXiv:2109.03244v3, Fig. 1.
6. R. Z. Ferreira, M. C. D. Marsh, and E. Ravensburg, arXiv:2510.14469v1, Fig. 1.
7. Z. Liu, *Supernova constraints on millicharged particles and lepton-flavor-violating axions*, 7th Joint Workshop on the Standard Model and Beyond, 2026-10-31, slide 65.
