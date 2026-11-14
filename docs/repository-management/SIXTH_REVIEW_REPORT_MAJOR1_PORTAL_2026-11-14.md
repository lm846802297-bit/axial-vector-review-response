# Sixth document review batch — Major 1 portal reference documents (2026-11-14)

## Scope

Reviewed two complete Major 1 portal documents: the 2026-10-26 merged working guide and the 2026-10-19 independent loop-review report. The review checked stated model conventions, claim boundaries, historical revisions, relation to current A2–A5 records and Markdown/math readability. No loop integrals or physical poles were recalculated.

## Individual outcomes

| Document | Outcome | Findings and action |
|---|---|---|
| `higgs_portal_mixing_merged_guide-gemini.md` | HISTORICAL | The guide is unusually explicit about the conditional status of the low-energy lepton soft loop, the separate zero-momentum heavy-VLL portal threshold, and the still-open full UV–EFT matching, complex-pole, (h\to ss), and LHC recast work. It also preserves withdrawn static/on-shell estimates and a historical English response draft. Added a top-level warning that the old response/manuscript text is not copy-ready and that current A2–A5 research files supersede its progress record. Keep as provenance and historical derivation route. |
| `单圈混合推导独立复核报告-协调更新版-20261019.md` | REVISION_REQUIRED | The scientific scope warning is sound: the report checks a conditional low-energy lepton bubble, not the full UV model. It explicitly identifies the unresolved (12\Delta\to6\Delta) coefficient transition, missing matching/counterterms, and invalid inference from nonzero widths to a safe degenerate region. However, the Markdown contains extensive Pandoc conversion artifacts such as `{=tex}`, mixed math/code fences and malformed inline notation. Added a top-level warning and links to current A2/A3a/A3b records. If this report remains a collaborator-facing document, restore the equations from its original source and revalidate the math rendering. |

## Cross-document consistency

1. The merged guide and independent report agree that the low-energy soft-loop integral is conditional and cannot be promoted to the complete UV prediction.
2. The guide explicitly distinguishes the heavy-VLL zero-momentum portal threshold from the light-lepton EFT bubble; these must not be added or substituted without common-scheme matching.
3. Both documents correctly keep the near-degenerate complex-pole analysis and the complete (h\to ss)/LHC recast open.
4. The current A2/A3a/A3b notes provide a newer and more structured gauge-basis, scalar-bubble and counterterm framework. The old documents remain useful for provenance but should not be treated as current status sources.
5. Historical response drafts in the merged guide must not be copied into the formal response letter without a fresh comparison against current decisions and accepted evidence.

## Edits made

- Added a historical-working-guide banner to the merged portal guide.
- Added a formatting/scope warning to the independent report and linked the current A2/A3a/A3b documents.
- No physics formula, parameter, numerical result or scientific conclusion was changed.
