# Major Point 1 — scalar \(S\) response status

**Date:** 2026-10-27  
**Purpose:** Internal evidence and follow-up record for the ordered response to Major Point 1 and subpoints 1.1–1.3. This file is not part of the formal letter to the referee.

## Current workflow status

These four labels describe the state of the response workflow; they do **not** mean that the scalar phenomenology has been fully solved.

| Workstream | Status | Meaning |
| --- | --- | --- |
| Response-letter text draft | **Complete** | The draft response to Major Point 1 and subpoints 1.1–1.3 has been written in the referee's original order. |
| Response–Diff consistency review | **Complete at claim/scope level** | The response wording has been checked against the four meeting transcripts, meeting summary, and the corresponding Diff sections; the crosswalk is recorded in Diff v2.4, §2E. |\n| Manuscript and Diff synchronization | **Pending** | The Diff proposal is cross-checked against the response, but the actual manuscript edits have not been applied; the manuscript TeX/BibTeX source is not present in this repository. |
| Quantitative scalar-phenomenology validation | **Partially complete; open issues remain** | Existing threshold/benchmark evidence is retained within its stated scope; model-specific scalar-search recasts, complete finite-momentum mixing validation, and the near-degenerate two-pole assessment remain open. |
| Formal acceptance of the full response letter | **Pending** | The full letter still requires cross-section consistency checks, completion of other response items, and final LaTeX compilation and review. |

## Response–Diff consistency review (2026-10-27)

Before this review, all four original meeting transcripts (01–04) and \`会议观点总结_2026-10-23.md\` were read, then compared with the current response draft, Diff v2.4, and the v5.6 execution-state snapshot.

- **Aligned:** retain \(S\) in the UV model; keep the paper's main line focused on \(A'\); reproduce the selected low-mass scalar constraints in the response instead of sending the referee back to Table II; cite existing singlet-scalar/Higgs-portal and scalar-search literature; distinguish perturbativity, plotting range, applied experimental exclusions, and unassessed regions; do not add particles.
- **Specific response refinements:** the reply now explains that the perturbativity condition constrains \(m_s/v_s\) with \(v_s=m_{A'}/(2g_X)\) derived point by point, and gives the approximate mass ranges and distinct spin-0 interpretations of the two Belle II analyses cited in Diff 4B.
- **Important reconciliation:** the 2026-10-23 meeting initially proposed calculating a loop-induced \(h\)--\(s\) mixing estimate and using it to argue that the effect is small. The later-adopted Route B and the present evidence ledger do not support claiming that this finite-momentum calculation and the near-degenerate pole analysis are complete. The current reply therefore does **not** claim that mixing is negligible; it retains the verified zero-momentum matching-boundary result and marks the near-degenerate region **not assessed**. This is a deliberate narrowing of the claim, not a claim that the original quantitative request has been fully answered.
- **Manuscript application remains pending:** the repository does not contain the actual manuscript TeX/BibTeX source. The Diff gives section/equation anchors and proposed text, but the source must be obtained before applying changes, checking citation keys, or verifying equation numbers.

## Decision basis

The response follows the 2026-10-23 meeting summary and transcripts:

1. Retain \(S\) as a genuine degree of freedom in the UV construction; do not claim that it is absent or arbitrarily decoupled.
2. Keep the paper's main phenomenological emphasis on the axial-vector \(A'\). Use existing singlet-scalar/Higgs-portal literature as context rather than attempting to reproduce a generic scalar-portal review.
3. Reproduce the relevant low-mass scalar-coupling constraints in the response, while making clear that they constrain the stated \(y_{s\mu\mu}\) benchmark and inherit the assumptions of the cited analyses.
4. Distinguish the theoretical perturbativity relation from a model-specific experimentally allowed scalar-mass interval.
5. Under the adopted Route B, retain the zero-momentum portal-threshold result and its explicit matching-boundary interpretation. Do not use it as if it were a full finite-momentum mixing-angle calculation.
6. Do not enlarge the particle content to address this comment.

## Changes made to the response-letter draft

File: \`Replies_to_Referee_3_revised_working_2026-10-27.tex\`

- Completed the overall Major Point 1 response so that it states the evidence boundary instead of leaving a scalar-classification placeholder.
- Completed Major Point 1.1: separates generic published search coverage from a model-specific exclusion/discovery claim.
- Completed Major Point 1.2: distinguishes the scan window, theoretical perturbativity condition, and phenomenological classification.
- Strengthened Major Point 1.3 to acknowledge possible \(\mu\), \(\tau\), and vector-like-lepton loop contributions and to state explicitly that the finite-momentum mixing calculation and near-degenerate recast remain incomplete.
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
4. **Portal/mixing:** the zero-momentum threshold does not determine the complete \(\Pi_{hs}(p^2)\), physical mixing angle, or pole structure. A closed same-order UV–EFT calculation, independent diagram-level validation, and model-specific Higgs/lineshape recast remain outstanding. In particular, the near-degenerate \(m_S\simeq m_h\) region remains **not assessed**.
5. **Final synchronization:** after the relevant manuscript changes and evidence checks are complete, synchronize the formal response, manuscript Diff, constraint tables, and task ledger.

## Status

This branch updates the response-letter draft and adds this internal status record only. It does **not** claim that the main manuscript has been edited, that the scalar collider recast is complete, or that the full finite-momentum portal/mixing problem has been solved. No merge is performed by this change.
