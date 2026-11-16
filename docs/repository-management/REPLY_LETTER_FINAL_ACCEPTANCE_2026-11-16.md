# Formal referee-response letter — final layout acceptance

- Acceptance date: 2026-11-16
- Scope: referee-facing reply-letter typesetting, source/PDF consistency, citation resolution, and visual layout only
- Status: **PASS — layout acceptance**
- Scientific acceptance: **NOT claimed**

## 1. Authoritative source and exact build

The only editable authoritative response source remains at the repository root:

- TeX: `Replies_to_Referee_3_referee_facing_2026-11-04.tex`
- PDF: `Replies_to_Referee_3_referee_facing_2026-11-04.pdf`

The final source was built by GitHub Actions run [#43767527054](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43767527054), using source commit `9a024d0684b436ac1d770a0b292b48c07d1f6685`. The workflow-generated PDF and updated audit JSON were committed in `4bdbf8e63900de43b7ef8b04e2369ba4fbe1a372`.

| Item | Final value |
|---|---|
| TeX Git blob | `d0a2b8c239cce87adf441ab8e715412ee28cb056` |
| TeX SHA-256 | `ab4cbf4f66e3ea70ac25f7d06d711e6ad9994bdf4f37674a432775ea97aa312d` |
| PDF Git blob | `4c18235a7e025872fa14a83ca7862b9c7592ac5b` |
| PDF SHA-256 | `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819` |
| PDF size | 500,973 bytes |
| Page count | 64 |
| Page format | A4, 595.276 × 841.89 pt |
| Build artifact | [reply-letter-layout-acceptance-43767527054](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43767527054) — artifact ID `14182947154` |

Build dependencies, SHA-256:

| Dependency | SHA-256 |
|---|---|
| `references.bib` | `8126a574901d557100cc22e0c0ddd9984191ce402856a19c32946e382b5beb29` |
| `Replies_to_Referee_3_stellar_references.bib` | `6dec703d2ef627d3ecb63e11389e8ef84bb17b6cccadec9b9edb30a2d2d905d4` |
| `JHEP.bst` | `32c737d743b198bd27f171a01947d44772cc12dc96bac488a60148bf41fad7cd` |
| `research/stellar-cooling-constraints-20261105/outputs/axial_stellar_constraints_reply_gev.pdf` | `2b5eb92613e02a11aaf62ff5e236e3dce217142b9755809a651f4ea77fe19909` |

## 2. Figure-caption repair and text preservation

The former 63-page build had an oversized Figure 1 caption on page 43. It overlapped the page number and was visibly clipped.

The accepted layout now:
1. Uses a short identifying figure caption.
2. Moves the complete original caption into the immediately following explanatory paragraph.
3. Adds a one-baseline page enlargement to keep the final sentence of that paragraph on page 44, avoiding a one-line continuation at the top of page 45.

The original caption is preserved exactly:
- Character count: **2,253**
- SHA-256: `3e042139e73f73b39ac42081ff494bccafe0345a1135c33eaf990cbd38d2c8c3`
- Automated exact-string comparison against the pre-layout source: PASS

No caption content, physical qualification, numerical result, reference, plot, or scientific argument was deleted or recomputed. The final page-44/45 adjustment changes pagination only.

## 3. Automated acceptance checks

The final Actions run completed successfully:

| Check | Result |
|---|---|
| latexmk + pdfLaTeX + BibTeX build | PASS |
| Unique citation keys | 47 |
| Labels | 7 |
| TeX environments balanced | PASS |
| Referee quote blocks unchanged | 27/27 |
| Major 1 scientific block unchanged | PASS |
| Major 3 through Major 4.3 scientific blocks unchanged | PASS |
| All Minor replies unchanged | PASS |
| Unresolved citations/references in final pass | 0 |
| Unresolved PDF markers | 0 |
| Embedded fonts | All |
| Overfull boxes | 0 |
| Oversized floats | 0 |
| Page-boundary audit | 0 blank pages; 0 text spans outside page |
| Page dimensions | Uniform A4 |

One pre-existing `Underfull \\hbox` warning remains at TeX lines 609–611. It is not an overfull/clipping warning and does not produce page-boundary or visual truncation; it is retained transparently rather than hidden by broad spacing changes.

## 4. Visual review

All 64 pages were rendered at 150 dpi. The build artifact contains 11 contact sheets: ten six-page sheets covering pages 1–60 and one four-page sheet covering pages 61–64. All 64 page PNGs are present. The affected region was enlarged and inspected page by page:

- Page 42: preceding text/equation page; no clipped content.
- Page 43: both panels of Figure 1, short caption, and page number are separated and fully visible.
- Page 44: full 2,253-character interpretation and its table; final sentence remains on the same page.
- Page 45: starts with a new paragraph, not an orphaned continuation line.

After the one-line pagination adjustment, a pixel comparison against the preceding 64-page build found only pages 44 and 45 changed. The other 62 page renders are identical. The final 44/45 images were inspected again. The final page-boundary JSON reports no blank pages, no text outside the page, and uniform A4 dimensions.

## 5. Overleaf package warning

`deliverables/Overleaf_Reply_Letter_PR72_2026-11-13/` is a preserved **2026-11-13 historical export snapshot**. Its `main.tex` predates the accepted caption relocation and must not be used as the final submission source. The repository-root TeX and PDF, together with the root bibliography/style files and the figure dependency listed above, are authoritative.

## 6. Acceptance boundary

This is a **typesetting and source/PDF consistency acceptance**, not a physics acceptance. No SN production rate, opacity, luminosity, cooling contour, coupling limit, or other physical result was recalculated in this task. In particular, the known vector Fig. 7 strong-absorption discrepancy and the limitations of the conditional axial ballistic-cooling benchmark remain open and are not resolved by a clean PDF build.

The formal reply-letter layout is accepted on PR #115. PR #115 remains a Draft pull request and has not been merged.

## 7. Independent artifact and source-tree follow-up (2026-11-16)

**Disposition of this acceptance report: PASS_WITH_NOTES.** The Actions run, uploaded artifact, final PDF bytes, source tree and rendered pages were independently checked.

- Run `43767527054` completed with conclusion `success`; its `build-and-inspect` job completed all 13 steps successfully. The uploaded artifact is `14182947154` (23,361,353 uncompressed bytes in the ZIP listing).
- The PDF extracted directly from the artifact ZIP has SHA-256 `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819`, Git blob `4c18235a7e025872fa14a83ca7862b9c7592ac5b`, and size 500,973 bytes. These match the report and current repository tree. It is 64 pages, A4.
- The TeX and all five build dependencies listed in the audit JSON have the same Git blob IDs at the workflow head commit `9a024d0684b436ac1d770a0b292b48c07d1f6685` and in the current maintenance tree. No post-build drift was found in the TeX, either bibliography source, the referee bibliography, `JHEP.bst`, or the axial stellar-constraint PDF dependency.
- The artifact contains 64 rendered page PNGs and 11 SVG contact sheets (ten sheets of six pages, plus one sheet of four pages). All 11 sheets were independently inspected; pages 43, 44 and 45 were also inspected individually. The Figure 1 caption no longer overlaps the page number; the complete caption interpretation is visible on page 44, and page 45 starts with a new paragraph.
- The final PDF's `page-boundary-audit.json` reports 64 pages, uniform A4 dimensions and no blank/out-of-bounds text. `pdffonts.txt` shows all fonts embedded. The final TeX `.log` has one underfull box, zero overfull boxes, and zero undefined citations/references. The earlier first-pass undefined-citation messages in `latexmk.log` occur before BibTeX; the final BibTeX and final pdfLaTeX passes resolve them.
- The artifact's `reply_audit.json` records 27/27 referee quote blocks unchanged, unchanged Major 1/Major 3–4.3/Minor science blocks, exact preservation of the 2,253-character original caption, 47 unique citation keys, seven labels, balanced environments, zero unresolved PDF markers and all fonts embedded. The PDF SHA in that JSON agrees with `pdf-sha256.txt` and the extracted artifact PDF.
- The artifact contains only the final render, not the preceding render. I therefore did not independently recompute the reported pixel-by-pixel claim that exactly pages 44 and 45 changed and the other 62 are identical; that remains a recorded workflow comparison rather than a newly reproduced comparison.

The original statement about four 4×4 contact sheets is corrected above to match the actual uploaded artifact. This follow-up is still a typesetting/source-consistency acceptance only. It does not validate any physics result or resolve the open stellar-cooling discrepancies. PR #115 remains Draft and unmerged.