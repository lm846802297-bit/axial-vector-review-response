# Individual review: portal threshold, gauge completion and upstream interface records

Review date: 2026-11-15. This batch covers the next six pending Major 1 documents in register order. The review checks model-scope consistency, perturbative counting, gauge-basis vertices, external experimental provenance and the lifecycle of cross-repository pins.

| Document | Outcome | Findings |
|---|---|---|
| `research/major1-higgs-scalar-mixing-20261109/MAJOR1_PORTAL_THRESHOLD_AND_HIGGS_CONSTRAINT_2026-11-10.md` | `PASS_WITH_NOTES` | The finite VLL threshold, conditional portal cancellation, residual local-curvature caveat, away-from-degeneracy mixing diagnostic and h-to-A-prime-A-prime width are consistently labelled as benchmarks/diagnostics rather than physical pole results or exclusions. Recomputed the one-sided Gaussian translation from the ATLAS inclusive rate: mu_min = 0.9061 and theta_max = 0.3116 rad. Independently recomputed the Benchmark-A h-to-A-prime-A-prime coefficient as 3.7437 GeV and the 10%-of-SM-width illustrative sin-squared-theta threshold as 1.10e-4. Added direct sources for ATLAS arXiv:2608.07332 and arXiv:2407.09168/DOI 10.1140/epjc/s10052-025-13916-5, with the analysis-specific applicability caveat. |
| `research/major1-higgs-scalar-mixing-20261109/PERTURBATIVE_ORDER_AND_GAUGE_COMPLETION_2026-11-10.md` | `PASS_WITH_NOTES` | The combined counting lambda_HS = O(hbar) and the distinction between leading fermion O(hbar) and portal-induced O(hbar^2) are correct. The old W/Z and A-prime vector rows implied mixed gauge-basis hs bubbles from mixing-induced vertices, contradicting the later A2 correction and the A1 gauge-basis vertex list. Corrected the main table and explanatory bullet: W/Z/electroweak-ghost loops are diagonal hh; A-prime/U(1)_X-ghost loops are diagonal ss; no one-loop gauge-basis hs vector/ghost bubble is claimed. Fixed one unclosed inline-code span in the A2 correction. |
| `research/major1-higgs-scalar-mixing-20261109/RC001_UPSTREAM_INTERFACE.md` | `HISTORICAL` | This is a cross-repository provenance/interface snapshot pinned to the upstream PR #11 head inspected on 2026-11-10. Its table accurately records the state at inspection, but later paragraphs incorrectly continued to say PR #11 remained Open/Draft. Upstream PR #13 explicitly describes work after PR #11 merged; PR #14 is a later follow-up record. Added a top-level historical-pin notice and replaced the stale live-status wording. The many artifact URLs remain intentionally pinned to their recorded commits; this file is not a live upstream dashboard and does not import QCD/QLD8 coefficients into the axial-vector scalar two-point result. |
| `research/major1-higgs-scalar-mixing-20261109/RXI_GAUGE_FIXING_A1_2026-11-10.md` | `PASS_WITH_NOTES` | The gauge-fixing signs are consistent with the declared D_mu = partial_mu + i g T A_mu and delta A = +partial alpha convention. The U(1)_X Goldstone shift gives m_X = 2 g_X v_s, and the FP operator yields the displayed s cbar_X c_X coefficient -xi_X m_X^2/v_s = -2 xi_X m_X g_X. The note correctly limits its claim: the complete nonlinear electroweak ghost matrix and full O(hbar^2) graph set are not yet expanded. |
| `research/major1-higgs-scalar-mixing-20261109/TADPOLE_VEV_AND_EFT_DIM8_UV_AUDIT_2026-11-09.md` | `HISTORICAL` | The VLL determinant has no mixed phi_h^2 phi_s^2 UV pole, while its finite heavy-eigenstate threshold is nonzero; the note keeps these distinct. The EFT5 bubble-plus-contact/O8 running is explicitly restricted and not presented as complete model-level matching. The append-only file has repeated section numbers (§7/§8/§10); added a snapshot/navigation warning rather than renumbering historical cross-references. No fresh CI or physics calculation was claimed. |
| `research/major1-higgs-scalar-mixing-20261109/UV_SCALAR_POTENTIAL_AND_DIAGRAM_CENSUS_2026-11-10.md` | `PASS_WITH_NOTES` | The potential, tadpole conditions, cubic vertices and combined loop counting are internally consistent. The W/Z, A-prime and SM-fermion rows in the diagram census incorrectly allowed mixing-induced gauge-basis hs vertices. Corrected them to direct gauge-basis vertices, added electroweak and U(1)_X ghost rows, and added an explicit no-double-counting rule for use of the full two-state propagator. |

## External-source checks

- ATLAS inclusive Higgs rate: arXiv:2608.07332 reports mu_incl = 0.990 (+0.053/-0.051), matching the value used in the threshold note. The note's one-sided Gaussian angle is explicitly illustrative, not an ATLAS mixing-angle limit. [Source](https://arxiv.org/abs/2608.07332).
- ATLAS prompt collimated e/mu dark-photon search: arXiv:2407.09168 reports model- and mass-dependent 95% CL branching-ratio limits between 0.001% and 5%, matching the note. The paper's signal assumptions are not a model-specific recast for this L_mu-L_tau model. [Source](https://arxiv.org/abs/2407.09168).

## Register after this batch

- `PASS`: 2
- `PASS_WITH_NOTES`: 142
- `HISTORICAL`: 68
- `REVISION_REQUIRED`: 8
- `PENDING`: 242
- Individually reviewed: 220 / 462

No physics scripts, numerical production outputs, manuscript files or referee-response files were modified or rerun in this batch. The independent checks were limited to the stated scalar-width/angle arithmetic and the gauge-fixing/vertex consistency review. The full gauge-complete propagator, complex poles, residues, UV–EFT Wilson-vector closure and model-specific Higgs recast remain open.
