# Fifty-fourth review: P1-IIIb/P1-IIIc moving-nucleon kernels and P1-I literature/finite-Q domain

Review date: 2026-11-15  
Repository: lm846802297-bit/axial-vector-review-response  
Reviewed commit: f5235b94fc9c02813716be04b8357515f2013cf5  
Scope: six baseline documents, their calculation scripts and JSON outputs, the Horowitz baseline implementation, and primary-literature equation/validity statements.

## 1. Executive result

Six documents were individually reviewed. All six are PASS_WITH_NOTES. The stationary weak-current trace and moving-nucleon kernel are algebraically consistent with the stated conventions and the cold/dilute Horowitz limit. The P1-IIIc energy grid correctly distinguishes total opacity from transport, momentum-transfer, and signed net energy-loss moments. The P1-I literature hierarchy is supported by the cited primary sources, with one subsection citation corrected. One machine-readable metadata error was fixed: the P1-Ic 400/800-node convergence value is an absolute difference, not a relative difference.

Several archived output/source pairs are not schema-identical. These are recorded as reproducibility caveats rather than interpreted as numerical failures. None of the six local-kernel audits is a radial B.2 calculation; the new Caputo/SFHo radial profile artifacts have not yet been inserted into the moving-nucleon kernel.

No B.2 opacity, production source, pure-vector Fig. 7 curve, luminosity, SN1987A limit, or axial-vector constraint was modified.

## 2. Individual document outcomes

| Document | Outcome | Review finding |
|---|---|---|
| B16_P1III_B_MOVING_FERMI_GAS_COLLISION_KERNEL_2026-11-10.md | PASS_WITH_NOTES | The \(p_{\min}\) delta-function reduction, exact \(q_0,q\) kinematics, azimuthal average, initial-spin average, and spin-degeneracy normalization are consistent. Cold/dilute recovery is within \(8.1\times10^{-6}\) in four channels. Current Python driver emits "definition" and omits the archived JSON's "high_density_convergence"; the archived JSON is not an exact output of the current script. No dedicated tests/workflow. |
| B16_P1III_B_MOVING_TRANSPORT_MOMENTS_2026-11-10.md | PASS_WITH_NOTES | The transformed-angle Jacobian and the four moment weights are correct. The 8/16 angular comparison closes at \(8.6\times10^{-5}\) or better for the selected benchmark. It is one ideal-gas point, not a global energy/density convergence bound. |
| B16_P1III_B_STATIONARY_DIRAC_TRACE_VALIDATION_2026-11-10.md | PASS_WITH_NOTES | The tensor conventions, neutrino/antineutrino trace swap, weak form factors, VV/AA/VA decomposition, Ward identity, and Hermiticity checks are consistent. The current script emits 180 pointwise and 20 integrated rows; the archived JSON is a compact four-row summary and is not schema-identical. No dedicated tests/workflow. |
| B16_P1III_C_MOVING_TRANSPORT_ENERGY_GRID_2026-11-10.md | PASS_WITH_NOTES | Five energies and four channels are covered. The net energy-loss ratio rises from about 0.67 at 50 MeV to 0.98 at 500 MeV, while total-scattering ratios remain near unity. Higher-order and energy-window checks are spot checks, not uniform all-grid convergence. |
| B16_P1I_A_LITERATURE_KERNEL_VALIDITY_AND_HIGH_ENERGY_LIMITS_2026-11-10.md | PASS_WITH_NOTES | H&R Eqs. (3) and (7) are correctly distinguished; the Keil omission is in §3.2, not §3.2.1. Caputo density/composition paths and the SFHo-mapped profile now exist as separate artifacts; the canonical sfho188_digitized.csv remains unchanged and lacks \(n_B,n_p\). |
| B16_P1I_C_FINITE_Q_RESPONSE_DOMAIN_2026-11-10.md | PASS_WITH_NOTES | Reddy/Horowitz/Bedaque response domains and the finite-\(q\) kinematic fractions are correctly bounded. Corrected the JSON/script key from max_relative_difference_400_vs_800_nodes to max_absolute_difference_400_vs_800_nodes; the value is unchanged. |

## 3. P1-IIIb weak-current and moving-nucleon chain

The stationary-target trace uses \(g^{\mu\nu}=(+---)\), \(q=p'-p=k-k'\), \(Q^2=-q^2\), and \(H^{\mu\nu}=\tfrac12\mathrm{Tr}[(\slashed p'+M)\Gamma^\mu(\slashed p+M)\bar\Gamma^\nu]\). Its duplicated Horowitz form-factor implementation was compared term by term with the repository's audit_b16_p1i_horowitz_transport_moments.py: nucleon masses, \(\sin^2\theta_W\), \(g_A\), anomalous moments, dipole/axial form factors, and proton/neutron weak combinations agree.

The reported maxima are:
- pointwise differential cross section and Horowitz bracket: \(3.11\times10^{-15}\);
- vector Ward identity: \(1.77\times10^{-14}\);
- hadronic-tensor Hermiticity: \(3.66\times10^{-17}\);
- VV+AA+VA decomposition: \(1.72\times10^{-15}\);
- separate VV/AA/VA bracket components: \(1.11\times10^{-12}\);
- integrated-moment quadrature: \(1.67\times10^{-14}\).

The moving kernel analytically integrates the energy delta over the initial nucleon polar angle. Its \(p_{\min}\) boundary follows from the on-shell condition \(E_{p'}=E_p+q_0\), and the initial nucleon azimuth is averaged relative to the scattering plane. With \(f_i\) defined per spin state and the hadronic trace averaged over the initial spin, the explicit spin degeneracy is included once. The cold/dilute ratios are 1.00000562--1.00000804 across \(\nu n,\bar\nu n,\nu p,\bar\nu p\).

At the illustrative \(T=3.03\) MeV, \(Y_p=0.10\), \(n_B/n_0=10^{-3}\), \(E_\nu=100\) MeV point, the total rate shifts by about 1.7--2.2%, while the signed net energy-loss moment can shift more. At \(n_B=0.1n_0\), the \(\nu n\) blocking factor is 0.695748; this is a deliberately ideal-gas stress point, not an SFHo radial opacity.

## 4. Integrated moments and energy grid

The transformed angle \(s=\sqrt{(1-\cos\theta)/2}\) has \(|d\cos\theta|=4s\,ds\). The moment definitions distinguish:
\[
\sigma_{\rm tot},\quad
\sigma_{\rm tr}\propto1-\cos\theta,\quad
\sigma_{\rm mom}\propto1-(E'/E)\cos\theta,\quad
\sigma_{\rm loss}\propto1-E'/E.
\]
The last is signed and includes upscattering. At 100 MeV the integrated ideal-gas benchmark gives ratios 1.000006 (total), 1.017761 (angular transport), 1.021881 (momentum transfer), and 0.851563 (net energy loss).

P1-IIIc extends this to 50, 100, 150, 255, and 500 MeV for all four neutron/proton neutrino/antineutrino channels. The total-scattering ratios remain 1.00006--1.01640. The net energy-loss ratio is 0.6656--0.6813 at 50 MeV, 0.8517--0.8616 at 100 MeV, and 0.9802--0.9812 at 500 MeV. This is an energy-transfer correction, not a 30% opacity correction.

The baseline uses \((N_s,N_{E'},N_p,N_\phi)=(8,24,20,6)\) and a \(7q\sqrt{T/M_N}\) outgoing-energy half-window. The reported higher-order and 5/9-window checks reach \(2.49\times10^{-4}\) and \(1.45\times10^{-4}\), respectively, but cover selected channel/energy points rather than every point at the highest order.

## 5. P1-I literature and response-domain conclusions

Hannestad--Raffelt Eq. (3) compares inelastic \(NN\) energy transfer with pair bremsstrahlung: a leading factor 20, with order-unity corrections reducing the estimate to about 10. Eq. (7) instead compares inelastic scattering with recoil:
\[
\frac{\Delta Q_{\rm inelastic}}{\Delta Q_{\rm recoil}}
\simeq1.21\eta_*^{3/2},
\]
with the authors suggesting roughly \(0.5\eta_*^{3/2}\) after vector-current and pion-mass corrections. For \(\eta_*=2\)--4 this is about 1.4--4.0, not a universal factor of ten. Their assumptions of \(nn\)-only interactions, nonrelativistic nucleons, OPE Born approximation, no \(np\) channel, no explicit \(NN\) correlations, and surface-layer applicability are accurately recorded. Keil--Raffelt--Janka §3.2 omits inelastic \(NN\) scattering because it was unimportant relative to recoil in their tested models; this is model-specific, not a universal hierarchy. Müller--Janka Eq. (A31) is an effective recoil-opacity prescription, not a differential collision kernel.

Reddy et al. provide finite-\((q_0,q)\) density/spin structure functions and an RPA construction, but their momentum-independent particle-hole interaction is motivated by thermal PNS momentum transfers of a few tens of MeV. Horowitz's virial response and Bedaque et al.'s virial scaling are low-\(q\) benchmarks. They are not universal response corrections at \(q\sim100\)--500 MeV.

The P1-Ia daughter support calculation uses the elastic \(E'=E\) limit, so it is deliberately generous for small-\(Q\) phase space; an inelastic event has \(Q_{\min}=|E-E'|\). Its \(m_\pi,m_\pi/2,m_\pi/4\) cuts are illustrative scales, not formal validity boundaries. P1-Ic uses stationary-target Horowitz recoil/weak-magnetism form factors and shows that low-\(q\) regions can contribute to total scattering while contributing much less to angular transport and energy loss. These are kinematic support fractions, not collision probabilities or multiplicative corrections.

## 6. Updated profile/kernel dependency

The 301-point Caputo figure-derived density/composition profile and the 301-point SFHo-EOS-mapped profile now exist separately. The canonical data/sfho188_digitized.csv remains a thermodynamic/lapse file and has not been silently rewritten. The moving-nucleon kernel and five-energy grid still use one illustrative ideal-gas thermodynamic point; they have not yet been evaluated on the co-located radial EOS profile.

The next physical gate is to evaluate the moving kernel with the EOS-derived \(n_B(r),Y_p(r),T(r),m_N^*(r)\), and vector mean fields, then add a controlled in-medium response where its momentum-transfer domain is supported. Only after local rates and their angular/energy redistribution are validated should radial B.2 propagation begin.

## 7. Reproducibility and CI limitations

- The P1-IIIb moving-kernel JSON uses rate_definition and includes high_density_convergence; the current driver emits definition and omits that block. Exact producer/invocation provenance is incomplete.
- The P1-IIIb stationary-trace JSON is a compact summary (integrated_moments_selected, four rows); the current script emits pointwise_rows (180) and integrated_moments (20). Do not describe the compact JSON as containing all rows.
- P1-IIIb moving, P1-IIIb moments, P1-IIIb stationary trace, P1-IIIc grid, P1-Ia and P1-Ic have no dedicated CI workflow in the current tree. Their numerical self-checks are not GitHub Actions acceptance.
- The P1-Ic convergence key was corrected to identify an absolute, not relative, difference. The numerical result is unchanged.

## 8. Final disposition

All six documents are PASS_WITH_NOTES. The stationary trace, moving-nucleon kernel, integrated moments, and energy grid are valid local ideal-gas diagnostics within their stated scope. The low-\(q\) literature remains a controlled-domain benchmark, not a high-energy daughter opacity correction. The EOS-mapped radial profile is available but not yet fed into the moving kernel.

No B.2 opacity, pure-vector Fig. 7 benchmark, luminosity, SN1987A limit, or axial-vector cooling constraint is changed.
