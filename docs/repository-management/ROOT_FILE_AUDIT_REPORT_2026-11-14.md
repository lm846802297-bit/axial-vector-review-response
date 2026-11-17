# Root-file audit report — 2026-11-14

> **2026-11-17 relocation follow-up:** this report remains the historical audit of the original 24 root files. Twelve historical/source files have since been moved byte-identically; the root now has 12 files. The authoritative 2026-11-04 reply TeX/PDF and its BibTeX/style dependencies remain at root. See [the relocation audit](ROOT_RELOCATION_AUDIT_2026-11-17.md) and [the path/blob manifest](ROOT_RELOCATION_MANIFEST_2026-11-17.csv).


> **Later update:** The 63-page PDF described below is historical. A matched 64-page layout-fixed build is documented in [the PDF audit](ROOT_PDF_EXTRACTION_AUDIT_2026-11-14.md).

> **Later PDF check (2026-11-14):** This historical review predates local PDF extraction. A later [audit](ROOT_PDF_EXTRACTION_AUDIT_2026-11-14.md) found the two four-page referee PDFs have identical extracted text; their `/Highlight` counts are 18 and 15, not the earlier metadata-scan counts 1 and 4. Bytes and annotations differ. At the 2026-11-14 extraction snapshot, the tracked response PDF was 63 pages and had not yet been rebuilt from the exact current TeX. This is superseded by the 64-page CI-accepted PDF documented in the final acceptance report; the 65-page 2026-11-06 build remains a separate historical artifact.

## Scope and method

Reviewed all **24 files directly in the repository root**. This is a file-role, navigation, source/build-dependency, provenance and consistency review. It is separate from the 462-row Markdown/text register and the workflow register (109 rows at this review snapshot; 115 in the current tree).

For the current formal reply TeX, performed static source checks over the complete current 1,842-line file (the earlier 1,839-line count was the 2026-11-14 snapshot):
- 82 citation occurrences / 47 unique citation keys; all keys resolve across the two declared BibTeX databases.
- 168 entries in `references.bib` and 5 entries in `Replies_to_Referee_3_stellar_references.bib`; no duplicate keys between them.
- 7 labels and 6 reference-command occurrences across 4 distinct targets; all resolve.
- The single `includegraphics` path exists in the branch tree.
- No TODO/FIXME/TBD/placeholder markers; no `input` or `include` dependency.
- The current response source explicitly separates the original one-VEV `S+VLL` model from the optional `sigma+3N_R` completion confined to Major 3/4.1. It treats the Major 1.3 near-degenerate scan as a diagnostic, not an allowed/excluded interval or physical mixing angle; it labels the axial-EFT cooling curve as conditional, not a complete SN1987A transport/exclusion result.

No loop integral, numerical scan, LaTeX build, PDF page rendering or scientific re-derivation was performed in this root-file audit. A static TeX pass is not a substitute for those checks.

## File-by-file classification

| Root file | Review outcome | Role and findings | Action |
|---|---|---|---|
| `.gitignore` | PASS_WITH_NOTES | 12-line ignore file covers Python caches, notebooks and common LaTeX build products. No currently identified root-level generated artifact requires a new rule. | Keep at root; extend only when a concrete generated-file pattern appears. |
| `AGENTS.md` | PASS_WITH_NOTES | Mandatory task preflight, task-specific reading routes, scientific result provenance, and merge-policy links are internally coherent. It correctly distinguishes CI from scientific acceptance. | Keep at root; normative instructions. |
| `GIT_MERGE_POLICY.md` | PASS | Clear Merge Commit default for substantive research; limited Squash/Rebase exceptions and post-merge verification. | Keep at root. |
| `JHEP.bst` | PASS_WITH_NOTES | 1,102-line BibTeX style dependency. The current formal response uses `\\bibliographystyle{JHEP}`; file must remain available to the root build. | Keep at root unless TeX build root and bibliography lookup are migrated together. |
| `PROJECT_STATUS.md` | PASS_WITH_NOTES | Long append-only live/historical status ledger. The top section needed reconciliation: PR #56 had merged on 2026-11-12, and a separate documentation-only Draft PR #115 is open. Older PR #56 Open/Draft entries are historical snapshots. The current root PDF differs from the earlier 2026-11-06 validation artifact. | Keep at root as current status source; latest live section is authoritative. |
| `README-先读这里.md` | PASS_WITH_NOTES | Chinese quick-start. Found a literal escaped-newline rendering defect and stale PR #56 Open/Draft/PDF status. Corrected those and linked the root-file audit. | Keep at root; navigation only, defer current status to PROJECT_STATUS. |
| `README.md` | PASS_WITH_NOTES | English/Chinese project entry page links to governance, review registers, workflow catalog and scientific indexes. | Keep at root; short landing page. |
| `Replies_to_Referee_3_referee_facing_2026-10-28.tex` | HISTORICAL | Earlier formal-response source; uses the old external manuscript citation/build arrangement. Not the current response source. | Preserve for version provenance; do not edit as current source. |
| `Replies_to_Referee_3_referee_facing_2026-11-03.tex` | HISTORICAL | Intermediate response source, superseded by the 2026-11-04 root TeX. | Preserve for version provenance; do not build or submit as current source. |
| `Replies_to_Referee_3_referee_facing_2026-11-04.tex` | PASS_WITH_NOTES | Current root referee-facing source. Static citation, label, cross-reference and figure-path checks passed. Its two BibTeX databases and JHEP style are explicit build dependencies. Scientific claims were checked for scope against the decision ledger, not independently re-derived. | Keep at root as the editable authoritative response source. |
| `Replies_to_Referee_3_referee_facing_2026-11-04.pdf` | PASS_WITH_NOTES | Final tracked PDF is 500,973 bytes; SHA-256 `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819`; Git blob `4c18235a7e025872fa14a83ca7862b9c7592ac5b`. It is a 64-page A4 build from the exact root TeX and declared dependencies, accepted by Actions run #43767527054. The earlier 63-page file (500,497 bytes; SHA `e0a2114e…`) and the 65-page 2026-11-06 artifact are historical. Layout acceptance only; no scientific acceptance. | Keep at root as the authoritative referee-facing PDF paired with the root TeX. |
| `Replies_to_Referee_3_stellar_references.bib` | PASS_WITH_NOTES | Five stellar-response references; none duplicates a key in `references.bib`. They are explicitly included by the current TeX bibliography command. | Keep at root as a separate declared BibTeX input; do not merge without updating TeX and build records. |
| `axial_vector_model_building-v6.pdf` | BLOCKED | Manuscript baseline PDF (2,759,986 bytes; Git blob `be8f472a…`). The binary PDF was not text-extracted or visually rendered in this review. | Preserve as read-only manuscript baseline; validate against the pinned Overleaf source archive in a dedicated PDF/source audit. |
| `dw13678_report_1_a.md` | PASS_WITH_NOTES | Readable transcription of the referee report, preserving Major/Minor structure and source wording. The paired PDFs were not text-extracted page by page in this audit. | Keep as searchable transcription; use the source PDF when wording/layout is disputed. |
| `dw13678_report_1_a.pdf` | BLOCKED | Distinct annotated PDF variant, 161,829 bytes; SHA-256 `752226d16c3aa57c1dffad338860976c88f5f6c82426b69a6b1c8ce2886bfba6`. Binary content/page equivalence was not verified. | Preserve; do not silently designate as the only pristine original. |
| `（原件）dw13678_report_1_a.pdf` | BLOCKED | Separate annotated PDF variant, 158,794 bytes; SHA-256 `ac7357aa2e9d29a9de3198f31f03e72c5c97f7c15b2a12875d73ff7d826c7d5e`. It is not byte-identical to the other report PDF; extracted text is identical, but annotation objects differ: 15 highlights, 17 popups and 2 underlines, versus 18/20/2 in `dw13678_report_1_a.pdf`. Visual/source equivalence remains unverified. | Preserve both variants; not a duplicate candidate. |
| `higgs_portal_mixing_merged_guide-gemini.md` | HISTORICAL | Historical guide with conditional low-energy lepton soft-loop analysis, separate heavy-VLL threshold, withdrawn estimates and old response draft. A top-level warning now directs readers to current A2–A5 work. | Keep as provenance; do not treat its progress summary or English response draft as current. |
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(65).md` | HISTORICAL | Large cumulative portal snapshot v65; ends at §261.12. | Keep as historical provenance; not current status authority. |
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(66).md` | HISTORICAL | Later cumulative snapshot v66; adds §262 light-fermion two-point/pole-kernel work. It is sequentially newer, not a duplicate of v65. | Keep as historical provenance; validate any reused numerical claim against current A2–A5 work. |
| `references.bib` | PASS_WITH_NOTES | Main response/manuscript bibliography database, 168 BibTeX entries. Together with the five-entry stellar supplement, it resolves all 47 unique citation keys in the current response TeX. | Keep at root as declared build input; do not merge/split without updating all consumers. |
| `中微子扇区电荷分析-hy4-统一更新版-20261019.md` | HISTORICAL | Early charge/no-go analysis with later appended corrections. Its warning correctly says the original paper remains one-VEV `S+VLL`; `sigma+3N_R` is only an optional Major 3/4.1 response completion, not an adopted manuscript extension or completed PMNS fit. | Keep as historical analysis; follow the decision ledger and current reply source. |
| `仓库分类索引.md` | PASS_WITH_NOTES | Older topical index contained a stale v5.6 §0.1 live-status pointer and an overly terse neutrino-route description. Updated to point live status to PROJECT_STATUS and distinguish original model from optional response-only completion. | Keep as stable root navigation alias; current status must not be duplicated here. |
| `单圈混合推导独立复核报告-协调更新版-20261019.md` | REVISION_REQUIRED | Historical conditional low-energy lepton-bubble review, not complete UV–EFT matching. Markdown has widespread Pandoc conversion residue such as `{=tex}`, mixed math/code fences and malformed inline notation. A top-level warning now points to A2/A3a/A3b. | Restore equations from original source if it remains a collaborator-facing document; retain as historical evidence until then. |
| `审稿意见逐条对照表-统一更新版-20261019.md` | HISTORICAL | Its 38-item coverage statistics describe the 2026-10-19 v3 analysis only, not current reply coverage. A top-level warning now points to current status and decision sources. | Keep for provenance; do not use as current checklist. |

## Cross-file/build findings

1. The current reply TeX is the only root editable response source. The 10-28 and 11-03 TeX files are historical snapshots.
2. The current TeX declares `references.bib`, `Replies_to_Referee_3_stellar_references.bib`, and `JHEP.bst`; all must remain available at the root unless the complete build configuration is moved together.
3. The current TeX has one figure dependency, `research/stellar-cooling-constraints-20261105/outputs/axial_stellar_constraints_reply_gev.pdf`; that exact path exists.
4. The current TeX's neutrino discussion is explicitly isolated to Major 3/4.1. Non-neutrino claims retain the original one-VEV model. The Major 1.3 near-degenerate diagnostics are not presented as a physical allowed/excluded interval.
5. The current TeX describes the axial-EFT cooling curve as conditional and explicitly not a complete SN1987A transport/exclusion result. The pure-vector Fig. 7 10 MeV reproduction gate remains not passed in the research status.
6. The two referee PDFs and the v65/v66 portal documents are not byte-identical duplicates. Their distinct provenance/versioning is a reason to preserve them, not deduplicate them.

## Safe migration decision

No root file is moved or deleted in this batch. The current remote code-search result did not provide a complete inbound-reference inventory, and the TeX/BibTeX dependencies plus PDF provenance need to remain stable. Before any move, perform a repository-wide local search for Markdown links, code paths, workflow references, TeX inputs/graphics, bibliography lookup and external handoff paths, then migrate with a relocation manifest and post-move build checks.

## Current-tree follow-up — 2026-11-16

- The root still contains exactly 24 files. The current TeX has 1,842 lines, 82 citation occurrences / 47 unique keys, 7 labels and 6 reference commands across 4 distinct targets; all resolve. The two BibTeX databases contain 168 and 5 entries with no cross-database duplicate keys. The single graphics path exists; there are no TODO/FIXME/TBD/placeholder markers or TeX input/include dependencies.
- `JHEP.bst` is 1,102 lines in the current tree, not 161; it remains a required root build dependency.
- The final root PDF is 64 pages / 500,973 bytes, SHA-256 `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819`, Git blob `4c18235a7e025872fa14a83ca7862b9c7592ac5b`. The PDF extracted from Actions artifact `14182947154` matches both its SHA-256 and Git blob exactly. The TeX and all declared build dependency Git blobs are unchanged between the workflow head and the current branch.
- The final build has 64 A4 pages, all fonts embedded, no blank/out-of-bounds text, no overfull boxes or undefined citations/references, and one documented non-clipping underfull box. The artifact has 64 page PNGs and 11 contact sheets (ten six-page sheets and one four-page sheet), all inspected. The final PDF is accepted for layout/source consistency only.
- The two four-page referee-report PDFs remain separate, non-byte-identical variants with identical extracted text and different annotation counts (18/20/2 versus 15/17/2 for highlights/popups/underlines). They remain blocked pending visual/source provenance review. The 33-page manuscript baseline PDF remains unrendered/unverified and blocked.
- The current workflow register has 115 rows; the original 109-row count above is retained as the historical 2026-11-14 snapshot. **At the time of this 2026-11-14 audit, no root files had yet been moved or deleted.** That migration decision was superseded by the 2026-11-17 byte-preserving relocation of 12 historical/source files; see [ROOT_RELOCATION_AUDIT_2026-11-17.md](ROOT_RELOCATION_AUDIT_2026-11-17.md).

The final response PDF acceptance supersedes the earlier BLOCKED status of the 63-page intermediate PDF. This is not a scientific acceptance and does not close the outstanding supernova-transport or UV–EFT questions.