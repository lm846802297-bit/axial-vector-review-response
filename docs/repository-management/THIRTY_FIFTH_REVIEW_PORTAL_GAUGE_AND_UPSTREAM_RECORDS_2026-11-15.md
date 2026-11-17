# Individual review: portal threshold, gauge completion and upstream interface records

Review date: 2026-11-15. This batch covers the next six pending Major 1 documents in register order. The review checks model-scope consistency, perturbative counting, gauge-basis vertices, external experimental provenance and the lifecycle of cross-repository pins.

| Document | Outcome | Findings |
|---|---|---|
| `research/major1-higgs-scalar-mixing-20261109/MAJOR1_PORTAL_THRESHOLD_AND_HIGGS_CONSTRAINT_2026-11-10.md` | `PASS_WITH_NOTES` | The finite VLL threshold, conditional portal cancellation, residual local-curvature caveat, away-from-degeneracy mixing diagnostic and h-to-A-prime-A-prime width are consistently labelled as benchmarks/diagnostics rather than physical pole results or exclusions. Recomputed the one-sided Gaussian translation from the ATLAS inclusive rate: mu_min = 0.906105 and theta_max = 0.311433 rad (0.3114 rad to four decimal places). Independently recomputed the Benchmark-A h-to-A-prime-A-prime coefficient as 3.7437 GeV and the 10%-of-SM-width illustrative sin-squared-theta threshold as 1.10e-4. Added direct sources for ATLAS arXiv:2608.07332 and arXiv:2407.09168/DOI 10.1140/epjc/s10052-025-13916-5, with the analysis-specific applicability caveat. |
| `research/major1-higgs-scalar-mixing-20261109/PERTURBATIVE_ORDER_AND_GAUGE_COMPLETION_2026-11-10.md` | `PASS_WITH_NOTES` | The combined counting lambda_HS = O(hbar) and the distinction between leading fermion O(hbar) and portal-induced O(hbar^2) are correct. The old W/Z and A-prime vector rows implied mixed gauge-basis hs bubbles from mixing-induced vertices, contradicting the later A2 correction and the A1 gauge-basis vertex list. Corrected the main table and explanatory bullet: W/Z/electroweak-ghost loops are diagonal hh; A-prime/U(1)_X-ghost loops are diagonal ss; no one-loop gauge-basis hs vector/ghost bubble is claimed. Fixed one unclosed inline-code span in the A2 correction and normalized its inline mathematics and the A4 residual/decay/2x2 TeX escapes. |
| `research/major1-higgs-scalar-mixing-20261109/RC001_UPSTREAM_INTERFACE.md` | `HISTORICAL` | This is a cross-repository provenance/interface snapshot pinned to the upstream PR #11 head inspected on 2026-11-10. Its table accurately records the state at inspection, but later paragraphs incorrectly continued to say PR #11 remained Open/Draft. Upstream PR #13 explicitly describes work after PR #11 merged; PR #14 is a later follow-up record. Added a top-level historical-pin notice and replaced the stale live-status wording. The final P1.6a update block is duplicated at the end; it repeats the same pinned result and is not a second calculation, so both copies remain visibly part of the historical record. The many artifact URLs remain intentionally pinned to their recorded commits; this file is not a live upstream dashboard and does not import QCD/QLD8 coefficients into the axial-vector scalar two-point result. |
| `research/major1-higgs-scalar-mixing-20261109/RXI_GAUGE_FIXING_A1_2026-11-10.md` | `PASS_WITH_NOTES` | The gauge-fixing signs are consistent with the declared D_mu = partial_mu + i g T A_mu and delta A = +partial alpha convention. The U(1)_X Goldstone shift gives m_X = 2 g_X v_s, and the FP operator yields the displayed s cbar_X c_X coefficient -xi_X m_X^2/v_s = -2 xi_X m_X g_X. The note correctly limits its claim: the complete nonlinear electroweak ghost matrix and full O(hbar^2) graph set are not yet expanded. The final paragraph was updated to point to the now-existing A2 ledger and to distinguish its completed scalar-dependent entries from the still-open A2b/A3 work. |
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


## Post-review consistency fixes

- Updated the A1 closing paragraph to point to the existing A2 vertex ledger and to separate its completed scalar-dependent FP entries from the remaining non-Abelian ghost-vector/A2b work.
- Repaired the A2 correction paragraph's inline-math rendering in the perturbative-order note and normalized the residual/decay/inverse-propagator TeX escapes.
- Reconciled the portal-threshold register metadata with the current file blob: the external-reference addition changed the file, so its byte count and blob SHA are now refreshed.
- The duplicated final P1.6a block in the RC-001 interface is recorded as a repeated archival entry, not independent evidence.


## Independent current-tree follow-up (2026-11-16)

**Disposition of this six-document batch: PASS_WITH_NOTES.** The six records, their current local links, the associated portal audit script/validation output, and the upstream PR states were rechecked. The original PASS_WITH_NOTES/HISTORICAL dispositions remain appropriate, with the order-classification correction below.

### 1. Portal/Higgs arithmetic and external inputs

The audit script uses \(\mu_{95}=0.990-1.645(0.051)=0.906105\) and \(\theta_{95}=\arcsin\sqrt{1-\mu_{95}}=0.3114329\) rad. The review report's earlier 0.3116 transcription was too high; it is corrected to 0.311433 rad, and the source note now gives 0.3114 rad. Independently evaluating the vector-boson phase-space expression gives
\[
\Gamma(h_1\to A'A')=3.7436757\ {\rm GeV}\,\sin^2\theta
\]
for Benchmark A, and the illustrative 10%-of-SM-width threshold is \(\sin^2\theta=1.09518\times10^{-4}\). Benchmark B remains kinematically closed because \(2m_{A'}=126\) GeV exceeds \(m_h=125.25\) GeV.

The external inputs are correctly attributed: ATLAS arXiv:2608.07332 gives the inclusive rate \(0.990^{+0.053}_{-0.051}\); ATLAS arXiv:2407.09168 gives mass- and signal-dependent 95% CL branching-ratio limits from 0.001% to 5% for its prompt collimated e/mu search. Neither source supplies a model-specific mixing-angle limit or a direct recast for this \(L_\mu-L_\tau\) model.

### 2. Remaining perturbative-order classification correction

The earlier gauge-basis correction in PERTURBATIVE_ORDER_AND_GAUGE_COMPLETION_2026-11-10.md correctly removed mixed \(hs\) vector/ghost bubbles, but the diagonal \(W/Z\) and \(A'\) vector/ghost rows still sat inside the section headed “portal-induced \(O(\hbar^2)\) completion”. Those are ordinary diagonal one-loop \(O(\hbar)\) terms, not portal-induced \(O(\hbar^2)\) terms. The broad scalar/vector/Goldstone/ghost row also mixed these orders.

The note has now been corrected at the order-bookkeeping level:

- The leading \(O(\hbar)\) section explicitly distinguishes the exact fermion matrix from the full diagonal entries: SM/electroweak contributions in \(hh\), and radial-scalar plus \(U(1)_X\) vector/Goldstone/ghost contributions in \(ss\). The A4 work is a partial subcalculation of the latter.
- The \(O(\hbar^2)\) table now contains portal-induced \(hs\) scalar/Goldstone bubbles, portal-suppressed diagonal \(hh/ss\) scalar/Goldstone bubbles, and portal-dependent tadpole/VEV/parameter/field-counterterm insertions.
- The ordinary \(W,Z\)/electroweak-ghost and \(A',a\)/\(U(1)_X\)-ghost loops are explicitly kept in the leading diagonal order, with no gauge-basis \(hs\) vector/ghost bubble.

This is a perturbative bookkeeping/documentation correction. It does not add a loop integral, numerical self-energy, Wilson coefficient, or physical pole.

### 3. Gauge-fixing and upstream-interface checks

The A1 convention remains internally consistent: with \(D_\mu=\partial_\mu+igT A_\mu\), \(\delta A_\mu=+\partial_\mu\alpha\), and \(m_X=2g_Xv_S\), the scalar-dependent \(U(1)_X\) FP coefficient is \(-\xi_Xm_X^2/v_S=-2\xi_Xm_Xg_X\). The A2 ledger has the same coefficient and no direct gauge-basis \(hA'A'\), \(sWW/sZZ\), or mixed \(hs\) ghost vertex. The full nonlinear electroweak ghost expansion and gauge-parameter cancellation remain open.

Upstream status was checked directly: PR #11 merged on 2026-11-12; PR #13 merged on 2026-11-12; PR #14 remains Open/Draft. The two P1.6a paragraphs in RC001_UPSTREAM_INTERFACE.md are near-duplicate archival descriptions of the same pinned calculation, not two independent calculations. They remain retained as history. The RC-001 four-fermion/current-sector results are not imported into the axial scalar two-point function.

The tadpole/VEV/EFT-DIM8 note still distinguishes the vanishing mixed renormalizable UV pole from the nonzero finite VLL threshold and limits the EFT5 bubble/contact and \(O_8\) running statements to their stated subset. Its repeated section numbers are documented as an append-only navigation issue. The scalar-potential census correctly gives the gauge-basis vertices and the no-double-counting rule for the full two-state propagator.

**Scientific boundary:** the complete gauge-complete \(2\times2\) propagator, complex poles/residues, full UV–EFT Wilson-vector closure, scalar widths and model-specific Higgs-search recast remain open. No physical scalar exclusion, full Major 1 closure, or gauge-independent pole is claimed. No production calculation or manuscript/referee-response file was changed.
