# Forty-fifth review: weak-current tensor, SFHo EOS occupations, and recoil moments

Review date: 2026-11-15  
Reviewed branch: `maintenance/repository-organization-audit-20261114`  
Scope: four P1-I/P1-IIIb/P1-IIIe scientific documents, the stationary-target weak-current implementation, the C4-B1 effective-mass tensor implementation/tests, and the published Horowitz and Fiorillo references.

Primary references:
- C. J. Horowitz, *Phys. Rev. D* 65, 043001 (2002), [DOI:10.1103/PhysRevD.65.043001](https://doi.org/10.1103/PhysRevD.65.043001).
- D. F. G. Fiorillo et al., *JCAP* 03 (2026) 053, [DOI:10.1088/1475-7516/2026/03/053](https://doi.org/10.1088/1475-7516/2026/03/053), Appendix C.1.

## 1. Executive result

No definite algebraic error was found in the stationary-target Horowitz cross section, the P1-IIIb weak-current tensor normalization specification, the C4-B1 equal-effective-mass tensor algebra, or the SFHo nucleon occupation convention. Two important qualifications were made explicit:

1. The additional recoil moment \(\sigma_{\rm mom}\) is a **longitudinal** momentum-transfer moment, not the magnitude of the three-momentum transfer.
2. Müller–Janka Eq. (A31) is a heuristic small-recoil effective-opacity estimate, not an exact cross section. Its comparison at \(E_\nu/M_N\simeq0.53\) is outside a controlled first-order recoil regime.

The use of vacuum \(M_N\) in the C4-B1 Pauli denominator while the external quasiparticle spinors use \(m_N^*\) is a declared minimal model prescription. The vector Ward identity does not select this denominator and does not validate a unique in-medium weak vertex.

## 2. Document-by-document outcomes

| Document | Outcome | Physics assessment |
|---|---|---|
| `B16_P1I_B_EXACT_ONE_NUCLEON_RECOIL_WEAK_MAGNETISM_2026-11-10.md` | `PASS_WITH_NOTES` | The Horowitz exact stationary-target recoil/weak-magnetism formula and single-nucleon form factors match the published expressions. The new \(\sigma_{\rm mom}\) definition is algebraically useful but represents longitudinal momentum transfer \(q_\parallel/E_\nu\), not \(|\mathbf q|/E_\nu\). The Müller–Janka A31 comparison is now qualified as a small-recoil heuristic stress test. |
| `B16_P1III_B_WEAK_CURRENT_TENSOR_SPEC_2026-11-10.md` | `PASS_WITH_NOTES` | The invariant response and moving-nucleon rate prefactors follow from the spin-averaged hadronic tensor plus explicit two-state nucleon degeneracy. The \(1/(4\pi q)\) response prefactor and \(G_F^2E'/(256\pi^4Eq)\) local-rate prefactor are consistent. This remains a specification/validation contract, not evidence that a full EOS-integrated transport kernel is complete. |
| `B16_P1IIIE_GARCHING_EOS_NUCLEON_DISTRIBUTIONS_2026-11-11.md` | `PASS_WITH_NOTES` | The Fiorillo Appendix C.1 occupation \(f_N=[\exp((U_N+K_N-\mu_N^*)/T)+1]^{-1}\), with \(K_N=\sqrt{p^2+m_N^{*2}}-m_N^*\), is correctly represented. The distinction between nucleon chemical potentials excluding rest mass and relativistic muon chemical potentials including mass is essential. The weighted degeneracy factors are global time/core averages, not \(t_{\rm pb}=1\) s local values. |
| `B16_P1IIIE_C4B1_EFFECTIVE_MASS_WEAK_TENSOR_2026-11-11.md` | `PASS_WITH_NOTES` | The equal-\(m_N^*\) quasiparticle spinors, on-shell kinematics, trace, vector Ward identity, hermiticity, vacuum-mass recovery, and neutrino/antineutrino VA sign structure are internally consistent. The vacuum \(M_N\) in the Pauli denominator is a model choice, not a consequence of the Ward identity; the calculation is not a full in-medium vertex or RPA response. |

## 3. Independent equation checks

### 3.1 Horowitz stationary-target kernel

The code's kinematic recoil factor
\[
\eta=\frac{E'_\nu}{E_\nu}
=\frac{1}{1+(E_\nu/M_N)(1-\cos\theta)}
\]
matches Horowitz's exact two-body stationary-target relation. The code's form-factor definitions reproduce Horowitz Appendix B:
\[
F_1^p=\frac{[1+\tau(1+\lambda_p)]G_D}{1+\tau},\quad
F_2^p=\frac{\lambda_pG_D}{1+\tau},
\]
\[
F_1^n=\frac{\tau\lambda_n(1-\eta_n)G_D}{1+\tau},\quad
F_2^n=\frac{\lambda_n(1+\tau\eta_n)G_D}{1+\tau},
\]
with \(\tau=Q^2/(4M_N^2)\), \(\eta_n=(1+5.6\tau)^{-1}\), and \(G_D=(1+4.97\tau)^{-2}\). The neutral-current proton/neutron weak combinations and the \(G_A\) dipole form are consistent with Horowitz's Appendix B and Table I.

The exact energy and angular moments satisfy the implementation identity
\[
\frac{\sigma_E}{\sigma_{\rm mom}}=\frac{E_\nu}{M_N+E_\nu}.
\]
Here
\[
1-\eta\cos\theta
=\frac{E_\nu-E'_\nu\cos\theta}{E_\nu}
=\frac{q_\parallel}{E_\nu}.
\]
Thus \(\sigma_{\rm mom}\) is the incident-direction longitudinal momentum-transfer moment. It is distinct from Horowitz's conventional \(\sigma_{\rm ang}=\int(1-\cos\theta)d\sigma\), and from a magnitude-weighted moment involving \(|\mathbf q|\).

Horowitz explicitly notes that the usual angular transport moment is strictly motivated in the \(E'_\nu\simeq E_\nu\) limit; the exact longitudinal moment retains recoil kinematics.

### 3.2 Müller–Janka A31 interpretation

Müller & Janka introduce
\[
\kappa_{a,\nu N}
=\frac{|E_\nu-3T|}{m_nc^2}\,\kappa_{s,\nu N}
\]
as an effective absorption opacity to approximate the small recoil energy transfer in their FMT scheme. It is not an exact differential cross section or an all-orders identity. The \(3T\) term represents thermal-motion effects. At \(E_\nu=100\) MeV, \(E_\nu/M_N\simeq0.106\); at 500 MeV, \(E_\nu/M_N\simeq0.53\), where a first-order recoil estimate is not controlled. The high-energy ratio against the stationary-target exact moment is therefore a stress test of the approximation's extrapolation, not evidence that A31 is wrong in its intended regime.

### 3.3 P1-IIIb weak-current tensor normalization

With
\[
H_N^{\mu\nu}
=\frac12\operatorname{Tr}[(\slashed p'+M_N)\Gamma^\mu
(\slashed p+M_N)\bar\Gamma^\nu],
\]
the trace averages the initial nucleon spin. The medium response includes the two occupied spin states explicitly:
\[
W_N^{\mu\nu}
=2\pi\int\frac{d^3p}{(2\pi)^3}
\frac{f_N(1-f_N')}{4E_pE_{p'}}
\delta(q_0+E_p-E_{p'})\,2H_N^{\mu\nu}.
\]
Using the energy delta to integrate the polar angle gives \(1/(4\pi q)\), not \(1/(8\pi q)\). The separate local rate formula similarly yields \(G_F^2E'/(256\pi^4Eq)\) after the polar-angle integration. These factors follow from the stated spin-averaged trace convention; multiplying either expression by another factor of two would double-count the nucleon spin degeneracy.

### 3.4 SFHo EOS chemical-potential convention

Fiorillo Appendix C.1 states that the Garching nucleon distribution is
\[
f_N(p)=\left[\exp\left(\frac{U_N+K_N(p)-\mu_N^*}{T}\right)+1\right]^{-1},
\]
where \(\mu_N^*\) excludes the rest mass, while relativistic chemical potentials for muons include their mass. For the Hempel/SFHo mapping,
\[
\mu_N^{\rm nonrel}=\mu_N^{\rm total}-M_N,\qquad
U_N=m_N^*-M_N+\Sigma_{V,N}^{\rm total}.
\]
Therefore the kinetic Fermi parameter is \(\nu_N=\mu_N^{\rm nonrel}-U_N\). The vector potential must not be subtracted a second time before inserting \(\mu_N^{\rm nonrel}\) into the displayed Fiorillo formula.

The common \(U_N\) cancels from the same-species elastic energy-conservation difference, but remains in the initial and final occupations. The published \(F_{NN}^{\rm deg}\) values are static occupation/Pauli-blocking checks; they do not replace the dynamic \(W_N^{\mu\nu}(q_0,q)\).

### 3.5 C4-B1 effective-mass weak tensor

For the stated local quasiparticle prescription, both legs have the same \(m_N^*(r)\). The vector contraction is
\[
q_\mu\Gamma_V^\mu
=F_1\slashed q,
\]
because \(q_\mu\sigma^{\mu\alpha}q_\alpha=0\), and the on-shell spinors imply \(\bar u(p'^*)\slashed q\,u(p^*)=0\). This remains true for \(m_N^*\ne M_N\), provided the two legs share the same local effective mass.

However, the Ward identity does not constrain the denominator in the Pauli term because the antisymmetric contraction vanishes independently of that denominator. The use of \(2M_N\) with \(m_N^*\) spinors is a declared vacuum-normalized minimal vertex, not a uniquely derived in-medium form factor prescription. The existing 288 Ward cases and 40 vacuum-mass recovery cases validate algebraic consistency only.

## 4. Scope boundaries

- The P1-IIIb note is a specification and normalization contract; it does not itself establish a completed full EOS-dependent collision kernel.
- The C4-B1 result is a local tensor algebra check, not a density-integrated opacity or RPA response.
- The EOS degeneracy factors are time/core-weighted aggregate quantities, not a local \(t_{\rm pb}=1\) s snapshot.
- The stationary-target Horowitz result does not include thermal nucleon motion, Pauli blocking, or in-medium correlations.
- No B.2 opacity, Fig. 7 curve, or axial-vector constraint is updated by this review.

## 5. Repository corrections made

- Clarified \(\sigma_{\rm mom}\) as a longitudinal momentum-transfer moment and distinguished it from \(|\mathbf q|\).
- Reclassified the Müller–Janka A31 comparison as a small-recoil heuristic stress test, with the \(E_\nu/M_N\) regime stated.
- Added the published Horowitz source and clarified the P1-IIIb spin-degeneracy normalization.
- Added the exact Fiorillo/Hempel chemical-potential mapping and the warning against subtracting the vector potential twice.
- Clarified that the C4-B1 Pauli denominator is a model prescription not selected by the vector Ward identity.

No production rates, B.2 opacity, stellar profile, or axial-vector outputs were changed.

## 6. Next physics gates

1. Complete the EOS-dependent moving-nucleon collision kernel using co-located \(m_N^*,U_N,\mu_N^*,T\) and species fractions from one consistent SFHo snapshot.
2. Reproduce the published static \(F_{pp}^{\rm deg}\) and \(F_{nn}^{\rm deg}\) targets before using the dynamic tensor response.
3. Compare the declared vacuum-normalized Pauli vertex with any available EOS-consistent/in-medium weak-current prescription; do not infer the answer from the Ward identity alone.
4. Keep stationary-target, moving ideal-gas, and EOS-quasiparticle results as separate lanes until the cold/dilute and finite-density limits all pass.

The B.2 and axial-vector production gates remain unchanged.


## Current-tree reconciliation (2026-11-16)

The four source documents in §2 remain present and their live blob IDs and baseline-register outcomes match the reviewed entries (all four PASS_WITH_NOTES). The Horowitz moment summary JSON retains the stated identity residual (3.33\times10^{-16}), pointlike-form-factor residual (1.38\times10^{-13}), and 64-to-1024-node quadrature difference (1.1\times10^{-14}). The C4-B1 summary retains 288 Ward cases, 40 vacuum-mass recovery cases, eight VA sign cases and `overall_pass=true`; its cited workflow #43001802164 is completed successfully. The P1-IIIb note remains a normalization/specification contract, and C4-B1 remains a local tensor-algebra check only. No EOS-integrated collision kernel, B.2 opacity, stellar transport or SN limit is accepted by this review.



## Independent code/output spot-check (2026-11-16)

The four §2 source documents were fetched from the current tree; each live blob ID matches its baseline-register \`current_blob_sha\`, and each remains \`PASS_WITH_NOTES\` / \`MATCH_CURRENT\`.

The Horowitz implementation \`audit_b16_p1i_horowitz_transport_moments.py\` and its JSON were inspected directly. The JSON contains the five incident-energy points 50, 100, 150, 255 and 500 MeV for neutron/proton and neutrino/antineutrino channels. Its archived checks are: pointlike Horowitz \(R_T\) versus Eqs. (37)–(42), \(1.38\times10^{-13}\); \(\sigma_E/\sigma_{\rm mom}=E/(M_N+E)\), \(3.33\times10^{-16}\); and 64-to-1024-node quadrature difference, \(1.1\times10^{-14}\). At 500 MeV the A31/exact energy-loss ratios are about 2.43 for \(\nu n\) and 4.24 for \(\bar\nu n\); this is an extrapolation stress test at \(E/M_N\simeq0.53\), not a validation/refutation of A31 in its intended small-recoil regime.

The C4-B1 output JSON and test module were checked against workflow #43001802164, which the Actions API reports as completed successfully. The output records 288 effective-mass Ward configurations, 40 vacuum-mass recovery cases, and eight neutrino/antineutrino VA-sign cases. The maxima are \(3.0095\times10^{-15}\) (vector Ward), \(2.4158\times10^{-16}\) (tensor hermiticity), \(6.6142\times10^{-16}\) (vacuum-mass recovery), and \(2.6095\times10^{-16}\) (VA sign). All five unit tests and all serialized acceptance flags are consistent with \`overall_pass=true\`. This validates the stated minimal quasiparticle tensor algebra, not a unique in-medium weak vertex.

The EOS occupation implementation was also checked directly: it uses \(K_N=\sqrt{p^2+m_N^{*2}}-m_N^*\), maps \(\mu_N^{\rm nonrel}=\mu_N^{\rm total}-M_N\), and evaluates the occupation with the explicit \(U_N-\mu_N^*\) term. The test module includes the density, degeneracy, common-shift, HS-to-Fiorillo mapping, and quadrature identities. The published time/core-weighted degeneracy targets remain aggregate benchmarks, not local \(t_{\rm pb}=1\) s values.

No new evidence in these checks upgrades the P1-IIIb specification to a completed EOS-integrated collision kernel, the C4-B1 tensor to an RPA/in-medium response, or any of these local calculations to B.2 opacity or SN transport.
