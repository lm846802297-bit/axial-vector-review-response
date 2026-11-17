# Individual review: stellar-cooling baseline and Stage-1 audits

Review date: 2026-11-15. Baseline branch: maintenance/repository-organization-audit-20261114. This batch reviews the next six pending files in register order. It is a document/evidence audit; no production scan or physics-rate script was rerun.

| Document | Outcome | Findings and disposition |
|---|---|---|
| research/stellar-cooling-constraints-20261105/AXIAL_STELLAR_CONSTRAINTS_CALCULATION_AND_REVIEW_2026-11-13.md | HISTORICAL | The document is a useful 2026-11-13 snapshot of the 75-row baseline axial scan plus five endpoint masses, with explicit reconstructed-profile assumptions, mode-resolved transport, saved source fractions, and open physics gates. It correctly records the pure-vector Fig. 7 10-MeV residual (+92.24% in the fixed-\(\omega\) lane; +35.97% in the \(E_\infty\) diagnostic), the stationary-muon approximation, and the B.2 opacity ambiguity. Because the current validation order defers axial constraint updates until the vector baseline passes, added a top-level warning that this saved contour is exploratory/provenance only, not an adopted SN1987A axial exclusion. Added direct arXiv links for Caputo, Ferreira and Blinov source inputs. |
| research/stellar-cooling-constraints-20261105/DIRECT_COLLISION_INTEGRAL_AUDIT_2026-11-07.md | PASS_WITH_NOTES | The audit's independent adaptive reference and archived JSON agree on 60 neutrino and 60 B.14 Compton points. The recorded maxima are \(3.91\times10^{-15}\) (neutrino production), \(3.96\times10^{-15}\) (neutrino absorption), \(1.07\times10^{-15}\) (neutrino detailed balance), \(2.38\times10^{-16}\) (Compton detailed balance), and \(3.94\times10^{-16}\) (B.14/B.16 spin sum). The script, test module and JSON output exist. Repaired the malformed Section 5 in which literal backslash-n sequences had collapsed the entire numerical-results section into one physical line. The 82-test Actions result is retained as a dated run, not claimed as a fresh run. B.13 moving-muon thermal integration, B.17 charge-conjugate source convention, B.2 mode-opacity interpretation and full Fig. 7 transport remain open. |
| research/stellar-cooling-constraints-20261105/MUON_CHEMICAL_POTENTIAL_ORIGIN_AND_DEFINITION_2026-11-08.md | PASS_WITH_NOTES | The full-versus-kinetic chemical-potential distinction, Fermi factors for \(\mu^\mp\), weak-equilibrium relation \(\mu_\mu-\mu_e=\mu_{\nu_\mu}-\mu_{\nu_e}\), and explanation of muonization are internally consistent. The Caputo curve is retained because its \(\mu_\mu\) reconstruction is consistent with the separately plotted muon density; the Ferreira curve remains a separate diagnostic, not an averaged substitute. The note correctly says this does not prove which raw simulation profile is authoritative. References are supplied; raw Garching data remain inaccessible in this record. |
| research/stellar-cooling-constraints-20261105/ORIGINAL_SFHO188_PROFILE_ACCESS_2026-11-07.md | HISTORICAL | The archive listing and access restrictions are documented with appropriate privacy/non-redistribution safeguards. The email is a draft and the file does not establish that it was sent or that access was granted. Its old statement that raw-profile acquisition is an active P0 prerequisite is superseded by the later literature-reconstruction route. Updated the status and final decision to make access an optional independent validation opportunity, not a blocker. |
| research/stellar-cooling-constraints-20261105/PLAN.md | HISTORICAL | This is a cumulative 2026-11-06–08 plan. Its earlier statements that PR #56 remained Open/Draft and that restricted Garching profile access was the next P0 task are no longer live. Added a historical banner recording PR #56's 2026-11-12 merge and pointing to the later axial benchmark summary and current project status. The historical sequence and old run records are preserved. |
| research/stellar-cooling-constraints-20261105/POLARIZATION_DETAILED_BALANCE_AUDIT_2026-11-07.md | HISTORICAL | The mode weights are individually normalized, their sum gives the expected three-polarization factor, and the B.19 detailed-balance ratio uses the mediator energy \(\omega\). The B.14/B.16 factor-of-three and photon-spin factor-of-two bookkeeping is stated consistently. The note correctly keeps the B.2 scalar-opacity convention ambiguous and distinguishes its exact-recoil fixed-target integrand test from a full moving-muon B.13 thermal integral. Added a historical-stage banner and corrected the stale PR #56 Draft status; the direct collision-integral note is the later scoped numerical cross-check. |

## Scope and acceptance boundaries

- The axial scan remains a saved exploratory calculation on a reconstructed SFHo-18.8 profile. It is not an accepted constraint update while the pure-vector Fig. 7 benchmark remains unpassed.
- The direct collision audit validates the stated neutrino and no-recoil B.14 local integrals on its test grid; it does not validate the moving-muon B.13 thermal kernel or the full transport.
- The Caputo-versus-Ferreira mu_mu(r) discrepancy remains unresolved at the raw-simulation level. The Caputo profile is a documented baseline choice, not proof of exact raw-profile identity.
- Original Garching profile access is no longer treated as a blocker for the literature-driven route. Any future access must comply with the archive's permission and non-redistribution terms.
- PR #56 merged on 2026-11-12. The dated Stage-1 notes remain as provenance; their old PR-state text is explicitly superseded.

## Updated baseline register

The register remains 462 documents. After this batch:

- PASS: 2
- PASS_WITH_NOTES: 145
- HISTORICAL: 79
- REVISION_REQUIRED: 8
- PENDING: 228
- Individually reviewed: 234 / 462

No production rate, axial/vector scan, transport result, figure, manuscript, or referee-response source was modified or rerun. The changes are limited to document warnings, source links, historical status, and repair of the malformed direct-audit section.
