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
