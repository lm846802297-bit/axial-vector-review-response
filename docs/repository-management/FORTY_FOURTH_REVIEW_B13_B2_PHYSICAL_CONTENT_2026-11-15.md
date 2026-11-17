# Forty-fourth review: B.2 polarization and B.13 collision physics

Review date: 2026-11-15  
Reviewed branch: \`maintenance/repository-organization-audit-20261114\`  
Scope: six pending scientific documents, the exact moving-muon B.13 implementation and tests, the polarization Boltzmann algebra, archived local/high-energy outputs, and the published Blinov et al. version of record.

Primary literature cross-check: N. Blinov, P. J. Fox, K. J. Kelly, R. Plestid and T. Zhou, *L_\mu-L_\tau gauge bosons in beam dumps and supernovae*, JHEP 06 (2026) 155, arXiv:2511.09619, [DOI:10.1007/JHEP06(2026)155](https://doi.org/10.1007/JHEP06(2026)155), especially Appendix B, Eqs. (B.1)–(B.19).

## 1. Executive result

No definite algebraic error was found in the reviewed B.7–B.10 neutrino kernel or in the local moving-muon B.13 phase-space reduction. The important unresolved issue is the polarization convention of the scalar absorption coefficient inserted into B.2. The paper sums vector polarizations in its production-rate expressions but does not explicitly state whether the scalar opacity in the ray exponent is a sum, an average over the three incident vector states, or a shorthand for a transport closure.

A second methodological limitation was found in the explicit-spinor audit: its \(\mu^+\) rows use a charge-conjugation-mapped \(u\)-spinor amplitude, not a direct \(v\)-spinor calculation. The underlying sign map is consistent with charge conjugation, but the audit must not be described as an independent antimuon-spinor validation.

The exact B.13 high-energy transport result remains restricted to the 210–510 MeV band. It is not a full-band Fig. 7 reproduction and does not support an updated SN1987A or axial-vector exclusion.

## 2. Document-by-document review

| Document | Outcome | Physics assessment |
|---|---|---|
| \`B16_NEUTRINO_B7_B10_LOCAL_KERNEL_AUDIT_2026-11-10.md\` | \`PASS_WITH_NOTES\` | The published Eq. (B.9) closed form, direct Fermi-pair angular integral, B.7 normalization, two-flavour sum, and B.10/B.4 detailed-balance reduction are mutually consistent on the stated 40-point grid. The archived V8 calculation is not the same as an executed Python/NumPy rerun; the document already records this distinction. The local check does not validate the stellar profile or full B.1/B.2 transport. |
| \`B2_POLARIZATION_BOLTZMANN_STATE_COUNTING_AUDIT_2026-11-13.md\` | \`PASS_WITH_NOTES\` | The mode-resolved collision equation, sum over modes, equal-occupation closure, and occupancy-weighted absorption rate are algebraically correct. The paper's B.2 scalar-opacity polarization convention remains unspecified. Do not assert that the paper definitely omitted a factor of three, and do not apply an empirical \(1/3\) correction to the archived scalar baseline. |
| \`B13_B16_APPROXIMATION_REGIME_AUDIT_2026-11-12.md\` | \`PASS_WITH_NOTES\` | Correctly distinguishes the full recoil-resolved B.13 thermal integral from the non-relativistic-muon/negligible-recoil B.14–B.16 approximation. The reconstructed SFHo-18.8 background has susceptibility-weighted mean muon speeds about 0.59–0.67 and RMS speeds about 0.62–0.69, so the stationary non-relativistic approximation is not parametrically controlled there. The 5% common-limit test is a broad regression check, not a precision uncertainty estimate. |
| \`B13_EXPLICIT_SPINOR_INDEPENDENT_AUDIT_2026-11-13.md\` | \`PASS_WITH_NOTES\` | Explicit \(u\)-spinor sums agree with the production trace, photon Ward contraction, and final-muon shell checks at the reported \(10^{-13}\)–\(10^{-16}\) level. However, the \(\mu^+\) cases use the charge-conjugation sign map in a positive-energy \(u\)-spinor representation; they do not independently construct \(v\) spinors. The document has been revised to state this limitation. |
| \`results/P1B_B2_EXACT_B13_2026-11-14/REPORT.md\` | \`PASS_WITH_NOTES\` | The 210–510 MeV band calculation closes against the archived B.16 band baseline and reports exact B.13 local rates, charge/mode decomposition, and three distinct transport prescriptions. The 0.22% agreement between equal-occupation average-opacity and mode-resolved results is benchmark-specific, not a general equivalence. The low-\(x\) extension is incomplete (7 of 24 pilot points); no full-band claim is allowed. |
| \`P1B_B13_LOCAL_RADIAL_ENERGY_AUDIT_PROTOCOL_2026-11-13.md\` | \`PASS_WITH_NOTES\` | The numerical protocol is consistent with the implementation after correcting the printed base-radius list to include the maximum-temperature shell \(r=8.482141202\) km. The duplicated adaptive-refinement paragraph was corrected to match the actual script: the ladder stops at \((28,16,16,16)\), and a point that still fails remains failed. |

## 3. Equation and normalization checks

### 3.1 Neutrino inverse decay, B.7–B.10

For one flavour, the vacuum width is
\[
\Gamma_{V\to\nu\bar\nu}^{(1)}
=\frac{\alpha_Vm_V}{6}
=\frac{g_X^2m_V}{24\pi}.
\]
The thermal production rate sums the three final vector polarizations, so the factor \(3\) in B.7 converts the polarization-averaged vacuum width to the polarization-summed production rate. Per \(g_X^2\), the prefactor is
\[
\frac{1}{g_X^2}\frac{m_V}{\omega}
\,3\Gamma_{V\to\nu\bar\nu}^{(1)}
=\frac{m_V^2}{8\pi\omega}.
\]
This agrees with the implementation.

For neutrino and antineutrino chemical potentials \(+\mu_\nu\) and \(-\mu_\nu\), energy conservation \(E_1+E_2=\omega\) gives
\[
\frac{f_\nu(E_1;\mu_\nu)f_{\bar\nu}(E_2;-\mu_\nu)}
{[1-f_\nu(E_1;\mu_\nu)][1-f_{\bar\nu}(E_2;-\mu_\nu)]}
=e^{-\omega/T}.
\]
The chemical potentials cancel, and the identity holds mode by mode. Therefore
\[
\Gamma_{\rm abs}^{*}
=(1-e^{-\omega/T})\Gamma_{\rm abs}
=(e^{\omega/T}-1)\Gamma_{\rm prod}.
\]
No additional factor of three belongs in this detailed-balance conversion.

The audit's maximum Eq. (B.9) versus repository residual is \(2.89\times10^{-15}\); direct angular quadrature at orders 128–1024 gives residuals of order \(3\times10^{-15}\). These are local-kernel identities, not uncertainties on the supernova profile.

### 3.2 Polarization state counting in B.2

For a fixed physical mode \(h\),
\[
C_h[f_h]=\Gamma_{{\rm prod},h}(1+f_h)
-\Gamma_{{\rm abs},h}f_h
=\Gamma_{{\rm prod},h}-\Gamma_{{\rm abs},h}^{*}f_h.
\]
Summing over \(h\) gives
\[
D F=\sum_h\Gamma_{{\rm prod},h}
-\sum_h\Gamma_{{\rm abs},h}^{*}f_h,
\qquad F=\sum_h f_h.
\]
If \(f_h=F/3\) is imposed, the scalar sink is governed by
\[
\overline{\Gamma_{\rm abs}^{*}}
=\frac13\sum_h\Gamma_{{\rm abs},h}^{*}.
\]
Without such a closure, the total equation is not closed in \(F\) alone.

The paper's B.6 and B.13 rate expressions sum the relevant spin/polarization states, B.7 explicitly accounts for the three vector polarizations, and B.10 preserves the sum-to-sum detailed-balance relation. B.2 then places a scalar \(\Gamma_{\rm abs}^{*}\) in the ray exponent without explicitly specifying its polarization average or a mode-mixing assumption. This is a genuine interpretation gap, not evidence by itself of a definite author error.

Required separate lanes:
1. literal scalar B.2 equation-level reproduction;
2. no-mixing transport with a separate \(\tau_h\) for each mode;
3. equal-occupation average-opacity closure, only with its population/mixing assumption stated.

### 3.3 Moving-muon B.13 phase-space reduction

The B.13 local kernel uses exact \(2\to2\) kinematics. For a fixed mediator \(q^\mu=(\omega,0,0,K)\), initial muon \(p^\mu\), and photon direction \(\hat n\), define
\[
D=E_p+\omega-(\mathbf p+\mathbf k)\cdot\hat n.
\]
The photon energy selected by the final-muon mass shell is
\[
k_\gamma^*=\frac{m_V^2+2p\cdot q}{2D},
\]
and the energy-delta Jacobian is \(D/E_{p'}\). Starting from the invariant three-body phase space, including the two initial muon spin states, integrating the final-muon momentum and the initial-muon azimuth gives the code prefactor
\[
\frac{1}{128\pi^4\omega}
\int dp\,\frac{p^2}{E_p}
\int d\cos\theta_p\,d\cos\theta_\gamma\,d\phi_\gamma\,
\frac{k_\gamma^*}{D}\,(\cdots).
\]
This matches the implemented \`prefactor\` and \`phase_measure\). The transformed radial variable \(x=(E_\mu-m_\mu)/T=t^2\) gives \(p^2dp=2TpE_\mu t\,dt\), matching \`radial_measure\`.

The production and absorption statistical factors are integrated separately and obey mode- and charge-resolved detailed balance. The \(-g^{\mu\nu}\) photon polarization sum is valid only because the photon Ward identity is checked; the explicit physical-photon-polarization reference supplies that cross-check. The vector longitudinal Ward shift is valid for the conserved vector current only and must not be applied to the axial current.

### 3.4 B.14 approximation regime

The published paper states that B.13 is often evaluated in the non-relativistic-muon limit with muon recoil neglected, leading to B.14. In the reconstructed SFHo-18.8 profile the thermal muons are not predominantly non-relativistic. Thus B.14–B.16 remain useful as the published approximation/reference lane, but B.13 is the appropriate local kernel for a physical moving-muon calculation on this profile.

## 4. Confirmed limitations and non-claims

1. The explicit-spinor reference does not yet provide a direct \(v\)-spinor calculation for \(\mu^+\).
2. The scalar B.2 polarization average is not specified in the paper; no factor-of-three correction is authorized without resolving that convention.
3. The P1-B global calculation covers only 210–510 MeV. It does not reproduce the full Fig. 7 energy integral.
4. The low-\(x\) domain required by the full B.2 grid reaches \(x_{\min}\simeq0.02218\), while the Global-03 table starts at \(x=0.5\). The completed low-\(x\) pilot covers only 7 of 24 planned points.
5. At \(r=15\) km and \(\omega=510\) MeV, the local B.13 Compton-to-neutrino reduced-opacity ratio is \(0.3068\%\) at \(x=38.54\), beyond the table's \(x=36\) support. This is a local comparison, not a global integrated tail bound.
6. The reconstructed profile is not the original Garching raw snapshot. No GR geodesic/path-redshift validation or updated SN1987A limit follows from these local and restricted-band results.

## 5. Repository corrections made in this review

- Corrected the P1-B protocol's base-radius list to include the \(8.482141202\) km maximum-temperature shell; the listed 10 radii now agree with the implementation and the 19-node bisected grid.
- Removed the duplicated adaptive-order statement and documented the actual maximum quadrature ladder and failure behavior.
- Qualified the B.13 explicit-spinor audit so the \(\mu^+\) charge-conjugation map is not described as an independent \(v\)-spinor check.
- Updated the approximation-regime reference to the published version of record and clarified that the 5% common-limit test is a broad regression criterion.
- Added the published-source and interpretation boundaries to the B.7–B.10 and B.2 state-counting audits.
- Added a physics-scope qualification to the restricted-band B.13 transport report.

No production collision kernel, scalar B.2 baseline, stellar profile, Fig. 7 reference, manuscript, referee response, or axial-vector exclusion output was modified.

## 6. Next physics gates

**P0**
1. Implement a direct explicit-\(v\)-spinor \(\mu^+\) amplitude reference and compare it pointwise with the charge-conjugation-mapped result for pure vector, pure axial, and mixed currents.
2. Resolve the scalar B.2 \(\Gamma_{\rm abs}^{*}\) convention. If author clarification is unavailable, preserve the three transport prescriptions as distinct and do not label one as the uniquely physical result.

**P1**
1. Complete the low-\(x\) B.13 interpolation extension over the full radial profile.
2. Establish a high-order full-band local B.13 source/absorption table and an integrated energy-tail bound.
3. Propagate the full band using identical background, energy convention, paths, and quadrature for the scalar-sum, equal-occupation-average, and independent-mode lanes.

**P2**
1. Resolve fixed local \(\omega\) versus energy-at-infinity propagation with a same-snapshot lapse/metric.
2. Obtain authorized same-snapshot Garching hydrodynamic data before claiming a raw-profile reproduction.

The pure-vector Fig. 7 gate remains unpassed. Production axial-vector limits remain frozen.


## Current-tree and subsequent-review reconciliation (2026-11-16)

The six scientific source documents in §2 were individually fetched from the current maintenance branch. Their live Git blob IDs match the baseline register's current-blob fields, and all six retain `PASS_WITH_NOTES` with `MATCH_CURRENT` fingerprints. The B.13 local-kernel and high-energy transport JSON was also read directly rather than relying only on the prose report.

The machine-readable B.13 summary confirms: 42/42 fixed-radius/fixed-energy local points pass the 0.1% successive-order criterion; maximum detailed-balance and final-muon shell residuals are \(1.0985\times10^{-14}\) and \(1.7108\times10^{-13}\), respectively. In the 210–510 MeV band, the literal scalar-sum, equal-occupation-average, and independent-mode prescriptions give \(2.1001262\times10^{52}\), \(6.07138768\times10^{53}\), and \(6.05812455\times10^{53}\) erg/s. The mode-resolved/equal-average difference is 0.22% for this benchmark only, while mode-resolved/scalar-sum is 28.8465. These are distinct attenuation prescriptions, not a normalization correction. The B.16 band baseline closes to \(1.01\times10^{-7}\) relative against the archived P1-C result.

The low-\(x\) extension remains incomplete: only 7 of 24 pilot points were completed; the required full-band minimum is \(x\simeq0.02218\), below the current table's \(x=0.5\) floor. The full-profile high-order B.13 scan, full-band Fig. 7 reproduction, GR energy convention, and updated SN1987A/axial limits therefore remain unaccepted. The Global-04 report's 950 selected high-order nodes and 240 stratified nodes pass their stated local quadrature screens, but it explicitly does not claim exhaustive full-grid high-order convergence or B.1/B.2 transport.

The explicit-spinor output remains a pointwise check: direct positive-energy \(u\)-spinors validate the \(\mu^-\) amplitudes; the \(\mu^+\) entries use the charge-conjugated (u)-spinor mapping and are not an independent \(v\)-spinor calculation. The later sixty-first review independently retains this limitation. Its separate correction to the thermal-integral design's initial-muon spin-degeneracy convention concerns a different document and does not alter the six-file findings here.

No production collision kernel, scalar B.2 convention, stellar profile, Fig. 7 reference, luminosity, SN1987A limit, manuscript, referee response, or axial-vector constraint output was modified by this review.
