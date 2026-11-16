# Forty-seventh review: EOS moving-nucleon response and scattering opacity

Review date: 2026-11-15  
Reviewed branch: \`maintenance/repository-organization-audit-20261114\`  
Scope: C4-A scalar dynamic response; C4-B2 EOS-effective-mass moving-nucleon weak kernel; C4-C1 finite-temperature outgoing-energy support; C4-C2 full-angle integration and quadrature; C4-C3 301-radius local-rate and radial-\(\tau\) archive; associated Python implementations, tests, JSON/CSV outputs, and provenance records.

Primary physics references:
- C. J. Horowitz, *Phys. Rev. D* 65, 043001 (2002), [DOI:10.1103/PhysRevD.65.043001](https://doi.org/10.1103/PhysRevD.65.043001).
- D. F. G. Fiorillo et al., *JCAP* 03 (2026) 053, [DOI:10.1088/1475-7516/2026/03/053](https://doi.org/10.1088/1475-7516/2026/03/053), Appendix C.1.
- The P1-IIIb weak-current tensor normalization specification and the repository's C2 SFHo/Hempel occupation mapping.

## 1. Executive result

No definite algebraic error was found in the C4-A scalar response, the C4-B2 local moving-nucleon weak collision kernel, or the C4-C1/C4-C2 phase-space reductions. The EOS mapping, same-species cancellation of the local vector potential, final-state nucleon Pauli factor, \(\xi_{\rm SPP}\) volume conversion, and cold/dilute Horowitz normalization checks are internally consistent with the declared minimal quasiparticle model.

The main outstanding issue is **validation coverage, not a demonstrated wrong formula**:

1. C4-C2's \(E_\nu'\) quadrature convergence is checked for all 16 selected radius/species/sign cases, but its angular \(8\)-versus-\(12\) comparison is checked only at the innermost radius \(r=0.20\) km.
2. C4-C3 then applies \(N_{\cos\theta}=8\) to all 301 radii without a radial angular-convergence scan. The 301-rate table reproduces the archived table to \(5.55\times10^{-16}\), but this is code/result reproducibility, not an independent bound on the angular-integration error.
3. C4-C1's finite \(E_\nu'\) interval is exact only conditional on the declared \(45T\) initial-momentum cutoff. The untruncated Fermi-Dirac distribution has a nonzero tail at arbitrarily large momentum. The archived work does not yet compare \(40T/45T/50T\) cutoffs.

Accordingly, the C4-C3 output remains a useful **fixed-local-energy, flat-space radial scattering diagnostic**, but it must not yet be promoted to a uniformly angular-converged physical opacity or transport solution.

## 2. Document-by-document outcomes

| Document | Outcome | Physics assessment |
|---|---|---|
| \`B16_P1IIIE_C4A_EOS_DYNAMIC_SCALAR_RESPONSE_2026-11-11.md\` | \`PASS_WITH_NOTES\` | The spin-summed scalar response normalization \(1/(\pi q)\), dynamic/static sum rule, detailed balance, and \(q\to0\) susceptibility relation are consistent. Four radii/two species are representative local states only. The 45T cutoff is common to both sides of the sum-rule check, so its tiny residual does not independently bound the omitted momentum tail. |
| \`B16_P1IIIE_C4B2_EOS_EFFECTIVE_MASS_COLLISION_KERNEL_2026-11-11.md\` | \`PASS_WITH_NOTES\` | The exact moving-nucleon shell kinematics, \(p_{\min}\), Dirac trace, final-state nucleon blocking, cold/dilute Horowitz limit, and \(m_N^*=M_N\) recovery are consistent. The \(\pm60\) MeV outgoing-energy window is only a finite-window diagnostic and misses 0.70%–24.95% of the 45T-truncated full-support result in the selected cases. |
| \`B16_P1IIIE_C4C1_EXACT_OUTGOING_ENERGY_SUPPORT_2026-11-11.md\` | \`PASS_WITH_NOTES\` | The two support roots are accurately solved for the \(45T\)-truncated initial-momentum domain. The term “exact support” needed qualification: it is not the support of the untruncated thermal distribution. The 48-versus-72 \(E_\nu'\) comparison does not test the separate 45T tail truncation. |
| \`B16_P1IIIE_C4C2_FULL_ANGLE_EPRIME_CONVERGENCE_2026-11-11.md\` | \`PASS_WITH_NOTES\` | The full-angle \(E_\nu'\) order-48 versus order-72 comparison passes for all 16 selected cases, with maximum difference \(2.08975\times10^{-5}\). This uses eight angle nodes at both orders; it is not an angular-order convergence test. |
| \`C4C2_C4C3_STATUS_AND_LOCAL_RATE_AUDIT_2026-11-11.md\` | \`PASS_WITH_NOTES\` | The \(\xi_{\rm SPP}\) convention and C4-C3 status are correctly separated from transport. The report now explicitly records the radial angular-convergence and 45T tail limitations. |
| \`C4C3_DIRECT_LOCAL_RECOMPUTATION_2026-11-11.md\` | \`PASS_WITH_NOTES\` | The 1204 local rates and radial optical-depth archive are faithfully reproduced. The machine-precision agreement with the archive does not independently validate the shared eight-node angular quadrature at all 301 radii. |
| \`c4c3_direct_local_recomputation_2026-11-11/README.md\` | \`PASS_WITH_NOTES\` | Provenance and archive structure are consistent; the README now carries the same angular/tail qualification as the main report. |

## 3. C4-A: EOS dynamic scalar response

For a local quasiparticle state,
\[
E_N^*(p)=\sqrt{p^2+m_N^{*2}},\qquad
K_N(p)=E_N^*(p)-m_N^*,
\]
\[
f_N(p)=\left[\exp\left(\frac{K_N(p)-\nu_N}{T}\right)+1\right]^{-1},
\qquad \nu_N=\mu_N^{\rm nonrel}-U_N.
\]
For same-species elastic scattering, the momentum-independent \(U_N\) cancels from the energy transfer \(q_0=E_N^*(|\mathbf p+\mathbf q|)-E_N^*(p)\), but remains in the occupation through \(\nu_N\).

With spin degeneracy two and the stated \(2\pi\delta\)-function convention,
\[
S_N(q_0,q)=\frac{1}{\pi q}\int_{p_{\min}}^{p_{\max}}dp\,
p(E_N^*+q_0)f_i(1-f_f).
\]
The factor \(1/(\pi q)\) is consistent with the angular reduction. The dynamic/static sum rule integrates the response over \(q_0\) and matches the independent three-dimensional static integral; detailed balance follows from the Fermi factors; and the \(q\to0\) limit matches \(n_N'F_{NN}^{\rm deg}\).

The reported maximum residuals are:
- dynamic/static sum rule: \(2.0\)–\(2.2\times10^{-15}\);
- detailed balance: \(3.6\)–\(4.4\times10^{-15}\);
- \(q=1\) MeV susceptibility deviation: \(1.4\)–\(2.6\times10^{-5}\);
- \(q=3\) MeV susceptibility deviation: \(1.2\)–\(2.3\times10^{-4}\).

These checks validate the local scalar response within the shared \(45T\) momentum cutoff. They do not validate the full weak tensor, RPA, NN correlations, in-medium vertices, or radial opacity.

## 4. C4-B2: EOS-effective-mass moving-nucleon kernel

The code uses \(m_N^*\) in both quasiparticle spinors and on-shell energies, the same local \(\nu_N,T\) in initial and final Fermi factors, and the exact momentum transfer \(q^\mu=k^\mu-k'^\mu\). The fixed-shell relation gives
\[
\cos\theta_{pq}
=\frac{2E_p^*q_0+q_0^2-q^2}{2pq},
\]
and the initial momentum integral begins at the exact \(p_{\min}(q_0,q;m_N^*)\). The final nucleon blocking factor is \(1-f_N(|\mathbf p+\mathbf q|)\).

The C4-B2 local kernel recovers the P1-IIIb free-mass implementation at \(m_N^*=M_N\), and the cold/dilute limit recovers the stationary Horowitz differential cross section. The split convention \(m_N^*\) for the quasiparticle kinematics and \(M_N\) for the vacuum weak-magnetism normalization remains a declared minimal in-medium model prescription; the vector Ward identity does not uniquely determine that choice.

The available-volume normalization is consistent:
\[
\sigma_N^{\rm window}=\frac{\Gamma_N^{\rm avail}}{n_N'},
\qquad
\kappa_N=\xi_{\rm SPP}\Gamma_N^{\rm avail}.
\]
The filling factor is restored exactly once in the total-volume opacity. The old \(\pm60\) MeV \(E_\nu'\) window, however, is not complete; C4-C1 supersedes those finite-window numbers for the same benchmark.

## 5. C4-C1: outgoing-energy support and the 45T tail

The support solver finds the roots of
\[
p_{\min}(E_\nu',\cos\theta;m_N^*)=p_{\max},
\quad
E_{\max}^*=m_N^*+\max(\nu_N,0)+45T.
\]
The root residual \(3.85\times10^{-13}\) verifies the numerical root solve. The \(\pm60\) MeV window captures 75.05%–99.30% of the integrated result over the selected local cases; its largest deficit is the 10 km neutron-neutrino case.

A Fermi-Dirac occupation is never identically zero at finite momentum. Thus \(p_{\max}\) creates a numerical truncation, and the resulting finite outgoing-energy interval is exact only within that truncated domain. The 45T cutoff is highly conservative, but a tail-convergence test at 40T, 45T, and 50T is still needed to attach a quantitative omitted-tail error.

## 6. C4-C2/C4-C3: full-angle rates and radial optical depth

C4-C2 evaluates
\[
\Gamma_N(E)=2\pi\int_{-1}^{1}d\cos\theta
\int_{E'_{\min}(\theta)}^{E'_{\max}(\theta)}dE'\,
\frac{d\Gamma_N}{dE'd\Omega'}.
\]
The cold/dilute total Horowitz residual is \(5.37\times10^{-6}\), the outgoing-energy order-48/72 difference is \(2.09\times10^{-5}\), and the initial-momentum/azimuth order comparison is \(7.23\times10^{-6}\) for the tested core cases.

The angular-order comparison is narrower than those numbers may first suggest. In the C4-C2 driver, the 8-versus-12 comparison is guarded by the first selected profile index and therefore tests only \(r=0.20\) km for the four target/sign combinations. The three other selected radii are evaluated at eight angle nodes, but are not compared with twelve. The separate \(E_\nu'\) convergence script evaluates all four radii with eight angle nodes at both energy orders; it does not add an angular-order comparison.

C4-C3 computes 301 radii and 1204 target/sign cases with \(N_{\cos\theta}=8\), \(N_{E'}=48\), \(N_p=36\), and \(N_\phi=12\). It reproduces the archived table at \(5.55\times10^{-16}\), has density-closure residuals below 0.763%, and passes its radial-grid checks. Those results verify the implementation and radial integration against the archived setup. They do not bound the angular error at the other 300 radii. The reported neutrino opacity peak is at \(r=7.35\) km, which was not included in the angular-order comparison.

The archived optical depths at \(r=0.20\) km are \(\tau_\nu=28603.0\) and \(\tau_{\bar\nu}=17568.6\), but they remain fixed-local-energy, flat-space radial scattering diagnostics. They are not redshifted transport optical depths, escape probabilities, or a solution of the neutrino Boltzmann equation. Neutrino final-state blocking is also outside this calculation.

## 7. Corrections made in this review

- Added independent physics-review qualifications to the C4-A and C4-B2 notes.
- Renamed/qualified C4-C1's “exact support” as support within the 45T momentum cutoff and documented the untruncated Fermi-tail distinction.
- Clarified that C4-C2's 48-versus-72 result is an outgoing-energy convergence check, while the 8-versus-12 angular check covers only the innermost radius.
- Added the missing radial angular-convergence caveat to the C4-C2/C4-C3 status note, the C4-C3 direct recomputation report, and the archived C4-C3 README.
- Preserved all numerical source code, EOS tables, local rates, optical depths, and archived outputs unchanged.

## 8. Next physical gates

**P0 — angular convergence**
1. Compare \(N_{\cos\theta}=8\) and 12 at all 301 radii using the same \(E_\nu'=48\), \(N_p=36\), and \(N_\phi=12\) settings, or at a dense predeclared radial subset that includes the opacity peak at 7.35 km.
2. Escalate any radius/species/sign case exceeding a declared tolerance to 16 or more angle nodes.
3. Rebuild \(\kappa(r)\) and \(\tau(r)\) only after the angular-order check passes.

**P1 — thermal-tail convergence**
1. Repeat the most demanding inner/intermediate cases at 40T, 45T, and 50T momentum cutoffs.
2. Require stability of both the local total rate and the integrated outgoing-energy rate; keep this separate from the \(E_\nu'\) quadrature-order test.

**P2 — physical transport completeness**
1. Add neutrino final-state blocking where the intended transport observable requires it.
2. Treat local-energy redshift and path geometry separately; the present radial diagnostic is not full GR.
3. Keep the effective-mass/weak-magnetism vertex prescription distinct from any future RPA or in-medium vertex calculation.

No B.2 vector production opacity, Blinov Fig. 7 result, SN1987A bound, manuscript, referee response, or axial-vector exclusion is updated by this review.


## Current-tree and CI execution reconciliation (2026-11-16)

The seven C4-A/C4-B2/C4-C1/C4-C2/C4-C3 documents listed in §2 remain present in the current tree and retain their recorded `PASS_WITH_NOTES` baseline dispositions. The C4-A sum-rule CSV has 56 data rows (four radii, two species, seven momentum-transfer values); the serialized acceptance JSON has all seven acceptance flags true. The C4-C2 \(E_\nu'\) output records all 16 selected radius/species/sign cases, maximum 48-to-72 difference \(2.08975\times10^{-5}\), and support-root residual \(1.03173\times10^{-13}\). The C4-C3 local summary records 301 radial points and 1204 species/sign cases, with its archived-table and radial-grid acceptance flags true. These outputs do not change the angular/tail limitations in §1.

The four earlier numerical CI workflows were independently fetched and are completed successfully: C4-A #42999848393, C4-B2 #43006872370, C4-C1 #43009019757, and C4-C2 #43011762069. By contrast, C4-C3 Actions run #43039883023 is completed with failure before Python setup: the checkout step received a literal backslash-prefixed commit SHA because the workflow escaped GitHub expression markers. The unit-test, 20-shard, and merge jobs were consequently skipped; this failure is not a numerical test failure and does not validate or invalidate the archived local calculation.

A second latent C4-C3 workflow defect was found during repair: the shard command wrote a literal escaped shell variable in its output filename, while the artifact upload expected a matrix-indexed filename. The maintenance-branch workflow was corrected by removing the escape before GitHub expressions and the shell variable, and making the shard write/upload paths agree. The workflow repair is recorded in commits `cd355d23a9d2f9682077c159d82cd148637d49ee` and `f352c117c2a1108812db48fadc8f7310d607f744`; current workflow blob is `6598dc67af10d07704694b25c4c404857ac2db93`. The corrected workflow has not yet been rerun. The C4-C3 301-radius archive remains a direct local computation, not a successful Actions run. The execution-status document was updated accordingly; its original reviewed blob/size were preserved while the live blob/size were refreshed, and its baseline fingerprint is now correctly marked CONTENT_FINGERPRINT_DIFFERS.

The physical disposition is unchanged: C4-C3 is a reproducible fixed-local-energy, flat-space radial diagnostic, not a uniformly angular-converged opacity or transport solution. P0 remains the radial angular-order scan (especially near the 7.35 km opacity peak); P1 remains the independent 40T/45T/50T momentum-tail test. No production weak kernel, EOS table, local-rate CSV, optical-depth archive, B.2 vector opacity, SN1987A bound, manuscript, referee response, or axial-vector constraint output was modified.
