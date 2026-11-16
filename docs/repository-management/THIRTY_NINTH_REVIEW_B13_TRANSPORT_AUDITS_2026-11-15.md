# Individual review: B.13 global transport and local-kernel audit records

Review date: 2026-11-15. Baseline branch: `maintenance/repository-organization-audit-20261114`. Six documents from the Blinov/SFHo-18.8 B.13 workstream were reviewed. This review distinguishes archived 10 MeV convergence snapshots from the later three-mass results and does not promote sampled-point stability into a full-domain error bound.

| Document | Outcome | Findings and disposition |
|---|---|---|
| `B13_GLOBAL_STAGE_A_CONVERGENCE_STATUS_2026-11-09.md` | `HISTORICAL` | This 329-line cumulative status log records successive B.13/B.16, independent B.1/B.2, 64,000-node local-kernel, and profile/GR checks. Its final decision is explicit: the adopted fixed-\(\omega\) B.16 numerical implementation closes at sub-percent level, while the Fig. 7 strong-endpoint residual remains about +92.05%; raw same-snapshot hydro/metric inputs are unavailable, and the axial production curve remains frozen. It is a dated status ledger, not the live task queue. |
| `B13_GLOBAL_TRANSPORT_AUDIT_2026-11-09.md` | `HISTORICAL` | The 10 MeV exact moving-muon B.13 source-plus-opacity replacement is internally closed, with detailed-balance and mass-shell residuals at \(10^{-14}\)–\(10^{-13}\) and same-grid B.16 closure. The document itself says the 10 MeV point is outside the paper's main \(m_V\lesssim1\) MeV Compton regime and that the B.13 replacement worsens the strong-endpoint excess. Its initial “dedicated radial/energy scan next” wording is superseded by later convergence and three-mass audits. Preserve as the 10 MeV source/opacity diagnostic, not as the published Fig. 7 baseline. |
| `B13_GLOBAL_TRANSPORT_CONVERGENCE_AUDIT_2026-11-09.md` | `HISTORICAL` | The 10 MeV Phase-A grid scan passes its stated finest-step tests, but the companion 0.1 MeV scan explicitly fails: radial 60→80 changes total luminosity by 5.2749% and escape probability by 4.9419%. The note correctly warns that 0.1 MeV is not converged. Later work broadens the comparison to three masses and re-establishes B.16 as the published baseline. Keep the 10 MeV scan as a bounded historical result; do not infer 0.1 MeV convergence. |
| `B13_LOCAL_KERNEL_QUADRATURE_CONVERGENCE_2026-11-09.md` | `PASS_WITH_NOTES` | At three selected \((r,\omega)\) points, the \((20,12,12,12)\to(24,14,14,14)\) refinement changes the exact moving-muon B.13 rate by at most 0.03016%, passing the stated 0.1% screening target. Detailed balance and final-muon mass-shell residuals are tiny, and the recorded 10 regression tests passed. This is not a uniform bound over the continuous radius-energy domain and does not certify source-weighted global convergence. |
| `B13_NONRELATIVISTIC_MUON_APPROXIMATION_DIAGNOSTIC_2026-11-09.md` | `PASS_WITH_NOTES` | The susceptibility-weighted equilibrium muon distribution has mean speed 0.761, RMS speed 0.775, 93.2% of weight above \(v_\mu=0.5\), and 71.7% above \(p_\mu=m_\mu\). This supports the statement that the non-relativistic approximation is not parametrically obvious in the dominant core. It is not a direct B.13 rate-error calculation; the document explicitly identifies this limitation and directs the reader to the exact B.13 rate comparison. |
| `B13_THREE_MASS_SOURCE_OPACITY_AND_CONVERGENCE_AUDIT_2026-11-09.md` | `PASS_WITH_NOTES` | The consistent exact B.13 source-plus-opacity replacement is evaluated at 0.1, 1 and 10 MeV. Same-grid B.16 closure and local detailed-balance/mass-shell checks pass. The note correctly distinguishes Compton-dominated 0.1/1 MeV from the 10 MeV neutrino-inverse-decay-dominated stress test, and records that 0.1/1 MeV use the baseline (40,100,16,32) grid rather than independent full-grid convergence. Its later §8 correctly establishes that the published Fig. 7 Compton prescription is B.14–B.19, not B.13; B.13/B.16 differences are an alternative relativistic correction, not a failed reproduction of the published baseline. |

## Scientific boundaries retained

- The B.16 scalar, polarization-summed, fixed-\(\omega\) prescription remains the vector Fig. 7 reproduction baseline.
- B.13 is a distinct exact moving-muon alternative; source and reduced opacity must be changed together for a physical comparison.
- The 10 MeV B.13 convergence scan does not establish 0.1/1 MeV global convergence.
- The three sampled local-kernel points do not provide a continuous \((r,\omega)\) error bound.
- The equilibrium velocity diagnostic is not itself a collision-rate correction.
- None of these documents authorizes an empirical opacity/source rescaling or an axial-vector constraint update.
- Same-snapshot raw hydro and full GR metric inputs remain the outstanding physical-input dependency recorded in the cumulative status.

## Updated baseline register

The 462-row baseline register now records 246 individually reviewed and 216 pending documents after this batch. Exact status counts are maintained in `DOCUMENT_AUDIT_REGISTER.csv`; this report documents the six reviewed entries and their limitations.

No physics script was modified or rerun. This was a document/evidence audit; no new transport result or axial-vector curve is claimed.


## Follow-up document corrections (2026-11-15)

- Added a historical-status banner to the cumulative Stage-A file and repaired the malformed optical-depth display-equation delimiters.
- Added current scope notes to the 10-MeV global transport and global convergence records. The 10-MeV finest-grid pass is explicitly mass-specific; the 0.1-MeV companion still fails its radial 60-to-80 refinement.
- Updated the local-kernel quadrature note to point to the later three-mass/global comparison rather than describe global B.13 transport as future work. Its 10 exact moving-muon regression tests are pre-existing kernel tests; no separate local-quadrature test file is present.
- Updated the non-relativistic-muon diagnostic to point to the completed three-mass comparison and to state that the 0.1/1-MeV global curves use the baseline grid rather than independent full-grid convergence.
- Added an acceptance-boundary banner to the three-mass report: 0.1/1 MeV are baseline-grid comparisons; 10 MeV is a stress test; PR #113 contains later full-profile refinements.
- The compact three-mass summary JSONs and local-kernel/non-relativistic diagnostic JSONs were parsed. The full 10-MeV point-array blob is present by path/hash but the GitHub file reader returned no text for it, so no point-by-point reparse of that large blob is claimed.
- These are documentation and status corrections only. No B.13 kernel, source integral, opacity, transport solver, or scan was rerun.


## Independent current-tree follow-up (2026-11-16)

**Disposition: PASS_WITH_NOTES.** The six-document review table remains consistent with the current baseline register: the three global snapshots are HISTORICAL; the sampled local-kernel convergence, non-relativistic-muon diagnostic, and three-mass comparison remain PASS_WITH_NOTES. This follow-up checks the underlying source, machine-readable outputs, test logs, and later PR #113 boundary.

### 1. B.13 kinematics and local phase space

The current finite_mixing/moving_muon_compton.py source solves the exact 2-to-2 recoil kinematics at fixed local A' energy. With q=(omega,0,0,k), k=sqrt(omega^2-m_A'^2), and the photon direction n_gamma, the photon energy is obtained from the final-muon on-shell condition:

\[
E_\gamma =
\frac{m_{A'}^2+2p_\mu\cdot q}
{2\left(E_\mu+\omega-\mathbf p_\mu\cdot n_\gamma-k\cos\theta_\gamma\right)}.
\]

The final muon is reconstructed from four-momentum conservation and its mass-shell residual is checked in the kernel. The thermal integral uses x=(E_mu-m_mu)/T=t^2, the corresponding p_mu^2 dp_mu Jacobian, the muon polar angle, photon polar angle, and relative photon azimuth. It includes Fermi blocking, photon Bose enhancement, both mu-minus and mu-plus target populations, and separate L,+,- vector modes. The code and run records therefore support the description exact moving-muon/recoil kernel within this implemented local collision model; they do not establish a uniform quadrature error bound over every (r,omega).

The local convergence JSONs for 0.1, 1, and 10 MeV report maximum (20,12,12,12)->(24,14,14,14) changes of 0.02831%, 0.02880%, and 0.03016%, respectively, at the three sampled points. The 10 MeV JSON gives a maximum final-muon shell residual of 1.63e-13 and maximum mode detailed-balance residual 1.51e-15. These are local sampled-point results, not full-profile transport convergence.

### 2. B.13 source and B.2 opacity are replaced consistently

audit_b13_global_transport.py computes the B.1 source from the B.13 production rate and replaces the B.16 Compton reduced-absorption term with (1-exp(-omega/T))*Gamma_abs^B13. The neutrino inverse-decay and dimuon channels remain at their B.16 values. The code recomputes the scalar B.2 optical-depth columns and uses the same angular weights for the B.16 and B.13 cases; the same-grid B.16 closure residuals in the three mass summaries are at 10^-16 scale.

The B.2 implementation is the literal fixed-omega Appendix-B prescription: it interpolates the reduced absorption along straight Euclidean chords and integrates ds Gamma_abs*(r(s),omega)/v_A'(omega), followed by the direction-averaged exponential escape probability. This is not a lapse-redshifted path prescription, a proper-distance integral, or full GR geodesic transport. The source and opacity replacement is internally consistent within this fixed-omega, scalar mode-summed transport lane; it does not validate the alternative mode-resolved propagation prescription.

### 3. Three-mass outputs and convergence boundary

The three compact global summary JSONs reproduce the report's both-charge Fig. 7 residuals:

| m_A' | Weak endpoint | Fig. 7 peak | Strong endpoint |
|---:|---:|---:|---:|
| 0.1 MeV | -66.11% | -23.73% | +0.33% |
| 1 MeV | -64.70% | -34.79% | +138.84% |
| 10 MeV | -28.04% | -16.27% | +131.59% |

All three are baseline-grid comparisons at (N_r,N_E,N_Omega,N_s)=(40,100,16,32). The 0.1 and 1 MeV global curves are not independently grid-converged; 10 MeV is an out-of-primary-regime stress test. The separate 0.1 MeV convergence JSON explicitly has overall_passed=false: its radial 60-to-80 refinement changes total luminosity by 5.2749% and escape probability by 4.9419%. The 10 MeV convergence values meet their stated numerical tolerances, but the associated Actions runs include artifact/aggregation/validator failures detailed in the updated B13_GLOBAL_TRANSPORT_CONVERGENCE_AUDIT_2026-11-09.md; no failed workflow is relabelled as CI success.

The velocity-moment JSON independently confirms mean(v_mu)=0.76144, v_rms=0.77538, 93.16% of the susceptibility weight above v_mu=0.5, and 71.69% above p_mu=m_mu. This is an equilibrium-distribution diagnostic, not a direct B.13/B.14 rate-error estimate.

### 4. Test-count correction and artifact availability

The local-kernel report's earlier wording "10 exact moving-muon regression tests" overstated the moving-muon subset. The successful Run #42575916846 ran 10 tests total: seven moving-muon Compton tests and three dimuon tests. The source document has been corrected accordingly. There is no dedicated unit-test module for the local quadrature-convergence scan itself; its order-ladder result is provided by the separate audit driver and JSON.

The full 10 MeV global transport JSON is present in the current Git tree at research/stellar-cooling-constraints-20261105/blinov_reproduction/outputs/b13_global_transport_vertex_preserving_10mev_2026-11-09.json (1,383,603 bytes; Git blob 8cc747e69df2ffee88680ee0de528381e4290390). The text-file reader did not return its contents, so this review does not claim a point-by-point reparse of that large array. The three compact summary JSONs, three local-kernel convergence JSONs, and the non-relativistic-muon diagnostic JSON were parsed and checked against the report.

### 5. Later PR #113 work and scientific disposition

PR #113 is merged. Its 10 MeV full-profile E1 screen and selected high-order checks improve the radial/energy interpolation evidence; its B.2 follow-up covers only the 210-510 MeV band. The full B.2 energy range remains blocked by low-x support: the existing interpolation table starts at x=0.5, while the full path requires x_min approximately 0.02218. The 16-radius/5-energy low-x screen and seven-point high-order pilot are partial checks, not a full 1687-radius low-x table or full-band transport result.

**Final boundary:** B.13 is a distinct exact moving-muon alternative to the published B.14-B.16 Compton approximation. The B.16 scalar, mode-summed, fixed-omega implementation remains the vector Fig. 7 reproduction baseline. These audits do not establish full-band B.1/B.2 convergence, raw-Garching-profile fidelity, complete GR transport, a Fig. 7 reconciliation, or a new SN1987A/axial-vector exclusion. No production kernel, opacity, luminosity, constraint curve, or manuscript result was changed.
