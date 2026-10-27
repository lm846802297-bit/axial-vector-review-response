# Major Point 1 — scalar \(S\) response status

**Date:** 2026-10-27  
**Purpose:** Internal evidence and follow-up record for the ordered response to Major Point 1 and subpoints 1.1–1.3. This file is not part of the formal letter to the referee.

## Current workflow status

These five labels describe the state of the response workflow; they do **not** mean that the scalar phenomenology has been fully solved.

| Workstream | Status | Meaning |
| --- | --- | --- |
| Response-letter text draft | **Complete** | The draft response to Major Point 1 and subpoints 1.1–1.3 has been written in the referee's original order. |
| Response–Diff consistency review | **Complete at claim/scope level** | The response wording has been checked against the four meeting transcripts, meeting summary, and the corresponding Diff sections; the crosswalk is recorded in Diff v2.4, §2E. |
| Manuscript and Diff synchronization | **Pending** | The Diff proposal is cross-checked against the response, but these scalar-response edits have not been applied to the manuscript. The TeX/BibTeX source is now archived under `overleaf-source/axial-vector-model-building-v6/`; citation checks, source edits, and compilation remain pending. |
| Quantitative scalar-phenomenology validation | **One-loop fermion mixing benchmark completed; full phenomenology remains open** | Exact mass-eigenstate \(h\)-\(s\) fermion self-energy has been numerically evaluated at two stated benchmarks and matched to the EFT soft contribution; full pole-scheme closure, scalar-search recasts, and near-degenerate experimental classification remain open. |
| Formal acceptance of the full response letter | **Pending** | The full letter still requires cross-section consistency checks, completion of other response items, and final LaTeX compilation and review. |

## Response–Diff consistency review (2026-10-27)

Before this review, all four original meeting transcripts (01–04) and `会议观点总结_2026-10-23.md` were read, then compared with the current response draft, Diff v2.4, and the v5.6 execution-state snapshot.

- **Aligned:** transcript 01 is the primary meeting record for Major Point 1. Retain \(S\) in the UV model; keep the paper's main line focused on \(A'\); reproduce the selected low-mass scalar constraints in the response instead of sending the referee back to Table II; cite existing singlet-scalar/Higgs-portal and scalar-search literature; distinguish perturbativity, plotting range, applied experimental exclusions, and unassessed regions; do not add particles. The transcript itself flags the spoken coefficient in Eq. (34) as uncertain, so the potential convention and exact submitted manuscript—not the ASR formula alone—must determine the final coefficient.
- **Specific response refinements:** the reply explains that perturbativity constrains \(m_s/v_s\) with \(v_s=m_{A'}/(2g_X)\) derived point by point, reproduces the selected low-mass scalar constraints with source-key citations, distinguishes the two Belle II spin-0 interpretations, and cites singlet-Higgs, GeV scalar-portal, B-factory, and prospective high-energy collider literature. It explicitly distinguishes a future muon-collider sensitivity study in a different leptophilic benchmark from a reach prediction for this UV radial scalar.
- **Quantitative follow-up completed (2026-10-27):** the exact mass-eigenstate one-loop calculation evaluates all light/heavy \(\mu,\tau\) internal-state pairs at two Plan-C-lite benchmarks, separates the EFT soft contribution, checks the hard momentum derivative against the RC-001 leading coefficient (relative difference \(6.11\times10^{-4}\)), and checks the zero-momentum threshold scale (relative residual \(1.79\times10^{-4}\)). A 1 MeV scan over \(m_s\in[10,150]\) GeV finds no \(2|\Pi_{hs}/(a-b)|\geq0.1\) interval in the open-channel benchmark; for the closed-channel benchmark it finds \([125.242553544,125.257446018]\) GeV, a half-width of \(7.446237\) MeV around \(m_h\). The exact-degeneracy diagnostic reaches \(2|\Pi_{hs}/(a-b)|\simeq0.394\) in that narrow-width case. Thus the original fermion-loop estimate is quantitatively addressed; it does **not** establish negligible mixing over the whole mass range. Full pole-scheme closure and model-specific experimental recasts remain open.
- **Manuscript application remains pending:** the TeX/BibTeX source is archived in [`overleaf-source/axial-vector-model-building-v6/`](../../../../overleaf-source/axial-vector-model-building-v6/). The response-letter citations now resolve against the archived bibliography, including the new Robens--Stefaniak (2015), Robens--Stefaniak--Wittbrodt (2020), and Boiarska et al. (2019) entries. The scalar edits still need to be applied to the manuscript, then equation numbers and the synchronized manuscript/reply must be checked and compiled.

### Cross-check findings: response letter vs. Diff v2.4

| Referee item | Response-letter text | Diff anchor | Consistency result |
|---|---|---|---|
| Overall Major Point 1 | States the scalar mass/self-coupling relation under the chosen small-portal benchmark; reproduces the five selected low-mass scalar-coupling rows; distinguishes scalar limits from the (A') effective-current constraints; avoids claiming a complete scalar exclusion map. | Diff 4A and 4D; task T-03/T-09 | **Aligned at claim/scope level.** The copied table is labelled selected/non-exhaustive and its source assumptions are stated. |
| Major Point 1.1 | Retains (S) as a UV degree of freedom, keeps the paper focused on (A'), cites singlet-Higgs and GeV scalar-portal literature, existing BaBar/Belle/Belle II searches, and prospective high-energy collider sensitivity in a different leptophilic benchmark; distinguishes the two Belle II spin-0 interpretations. No model-specific exclusion or discovery reach is claimed. | Diff 2F and 4B | **Aligned at claim/scope level.** The cited bibliography keys resolve in the archived `references.bib`; manuscript application and compilation remain pending. |
| Major Point 1.2 | Gives the conditional perturbativity bound through (v_s=m_{A'}/(2g_X)), but does not claim a universal phenomenologically allowed (m_s) interval. Theoretical consistency, applied exclusions, and unassessed regions are separated. | Diff 4A and 4D; task T-03/T-09 | **Aligned at claim/scope level.** The model-specific scalar search recast remains open, so the physical allowed set is not yet fully classified. |
| Major Point 1.3 | Gives the conditional zero-momentum portal threshold, the matched finite-momentum one-loop fermion self-energy at two benchmarks, and the width-regulated degeneracy diagnostic; does not claim a global scalar classification. | Diff 2C and 2D; new exact mass-eigenstate calculation record | **Quantitative fermion-loop benchmark addressed.** The narrow-width near-degenerate case is demonstrably non-negligible in one stated benchmark; full pole-scheme closure and experimental recasts remain open. |

### Quantitative one-loop calculation added (2026-10-27)

- Research report: Higgs_portal_exact_mass_eigenstate_one_loop_2026-10-27.md.
- Reproducible script: higgs_portal_exact_mass_eigenstate_one_loop.py.
- Captured validation output: higgs_portal_exact_mass_eigenstate_one_loop_validation.txt.
- The script uses the full mass-eigenstate \(G_h,G_s\) matrices and all four internal-state pairings, numerically evaluates the finite PV functions, checks the \(p^2\) UV cancellation and absorptive part, and compares the exact hard momentum difference with the leading derivative matching result.
- The formal reply draft now includes the two matched benchmark self-energies and the distinct open-/closed-\(A'A'\) near-degenerate diagnostics.
- **Not completed:** a full pole-scheme calculation with all diagonal self-energies/tadpole/input counterterms and a model-specific Higgs lineshape/direct-search recast. The near-degenerate narrow-width region remains **not assessed** experimentally.

### Meeting-decision audit

- **Principle 1 — do not send the referee back to the paper:** followed for the selected low-mass scalar limits; the response reproduces the table entries rather than merely pointing to Table II.
- **Principle 2 — cite established scalar-portal literature instead of duplicating a generic review:** followed in the response draft and represented in Diff 2F. The bibliography must still be synchronized against the actual manuscript source.
- **Principle 3 — do not rely only on argument where a calculation was requested:** the benchmark-level one-loop fermion calculation is now recorded in Higgs_portal_exact_mass_eigenstate_one_loop_2026-10-27.md, with a reproducible script and captured output. The full physical pole/lineshape and experimental classification are still open; the numerical result is not promoted to a global UV-model conclusion.
- **Principle 4 — do not expand the model merely to answer the referee:** followed; no new particles are introduced.

### Scope of this completed review

The **response–Diff claim/scope consistency review is complete** for Major Point 1 and subpoints 1.1–1.3. This does not mean the scalar phenomenology is fully solved, nor that the manuscript has been edited. The manuscript TeX/BibTeX source is now archived in `overleaf-source/axial-vector-model-building-v6/`. The scalar Diff remains a proposed patch: source-level application, citation-key verification, equation/section cross-checks, and compilation remain pending.

## Decision basis

The response follows the 2026-10-23 meeting summary and transcripts:

1. Retain \(S\) as a genuine degree of freedom in the UV construction; do not claim that it is absent or arbitrarily decoupled.
2. Keep the paper's main phenomenological emphasis on the axial-vector \(A'\). Use existing singlet-scalar/Higgs-portal literature as context rather than attempting to reproduce a generic scalar-portal review.
3. Reproduce the relevant low-mass scalar-coupling constraints in the response, while making clear that they constrain the stated \(y_{s\mu\mu}\) benchmark and inherit the assumptions of the cited analyses.
4. Distinguish the theoretical perturbativity relation from a model-specific experimentally allowed scalar-mass interval.
5. Under the adopted Route B, retain the zero-momentum portal-threshold result and its explicit matching-boundary interpretation. Do not use it as if it were a full finite-momentum mixing-angle calculation.
6. Do not enlarge the particle content to address this comment.

## Changes made to the response-letter draft

File: `Replies_to_Referee_3_revised_working_2026-10-27.tex`

- Completed the overall Major Point 1 response so that it states the evidence boundary instead of leaving a scalar-classification placeholder.
- Completed Major Point 1.1: separates generic published search coverage from a model-specific exclusion/discovery claim.
- Completed Major Point 1.2: distinguishes the scan window, theoretical perturbativity condition, and phenomenological classification.
- Strengthened Major Point 1.3 with the newly evaluated matched finite-momentum one-loop fermion self-energies at two benchmarks and the open-/closed-channel width-regulated diagnostics. The near-degenerate experimental recast and full pole-scheme closure remain incomplete.
- Preserved the referee's quoted wording and the existing order of the response.

## Evidence boundary — claims that may be made now

- The scalar mass/VEV/self-coupling relations can be stated for the manuscript's specified potential convention.
- The reproduced low-mass bounds can be described as approximate bounds on \(y_{s\mu\mu}\), with their source assumptions; they are not direct model-independent bounds on \(g_X\).
- The zero-momentum VLL threshold relation and the two illustrative benchmark evaluations may be presented only with their stated matching condition and benchmark inputs.
- The \(A'\) contours are conditional constraints on the specified small-portal, pure-axial effective-current benchmark, not a global viability classification of the full UV model.
- Generic singlet-scalar literature and published search mass coverage do not, without a model-specific recast, establish exclusion or viability of this model's scalar.

## Open work — do not mark as completed

1. **Manuscript alignment:** apply and cross-check the corresponding scope and matching-boundary clarifications in Sec. II.C and verify equation/section references against the actual manuscript source.
2. **Constraint provenance:** check the cited astrophysical entries and their assumptions against the original sources before final submission.
3. **Collider applicability:** determine which published scalar searches can be recast using the model's actual production rates, decay channels (including \(s\to A'A'\) when open), branching fractions, widths, and lifetime. Until then, do not assign a model-specific allowed/excluded label to the unassessed domain.
4. **Portal/mixing:** the exact mass-eigenstate fermion-loop benchmark calculation and finite-momentum hard/EFT-soft comparison are now recorded. The full pole scheme, all diagonal self-energies/tadpole/input counterterms, external diagram-package reproduction, and model-specific Higgs/lineshape recast remain outstanding. In particular, the narrow-width near-degenerate region remains **not assessed** experimentally.
5. **Final synchronization:** after the relevant manuscript changes and evidence checks are complete, synchronize the formal response, manuscript Diff, constraint tables, and task ledger.

## Status

**Integration PR:** [#22 — quantify one-loop Higgs-singlet mixing for Major Point 1.3](https://github.com/lm846802297-bit/axial-vector-review-response/pull/22) consolidates `research/major-point-1-exact-hs-mixing-2026-10-27` and its `-v2` successor. The v2 result retains the original calculation, adds the dense mass scan, and preserves the Major Point 2 response already on `main`. The integration includes both branch histories; consult the PR for its live merge status. No GitHub check runs or commit statuses were configured for the reviewed head, so validation is documented as local execution, not CI.

**Integration validation:** the unchanged script (Git blob `a2128e5ed9fe0065fc01e61972fdbfbe3f4859fb`) was syntax-compiled and rerun with Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. Both benchmark assertion sets passed; the reported matched self-energies and dense-scan interval were reproduced. The separate `work/hs-mixing-one-loop-20261027` development branch is outside this integration.

This branch adds a reproducible benchmark-level one-loop fermion mixing calculation and updates the response, Diff, and status record. It does **not** claim that the main manuscript has been edited, that the full pole scheme is closed, or that the scalar collider recast is complete. Repository integration does not constitute final scientific acceptance or readiness to submit the response letter.
