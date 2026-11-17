# Root PDF extraction and annotation audit — 2026-11-14

## Scope

Read-only inspection of the four root PDF blobs in maintenance commit `e4dd7ec4df4c83f70c5ab53bc7b91bea4f1eede9` using Python 3.12.14 and pypdf 6.21.4. SHA-256 applies to file bytes. Text extraction does not establish visual equality, source-PDF equivalence or correctness of the scientific arguments.

| File | Pages | Bytes | SHA-256 | Extracted characters |
|---|---:|---:|---|---:|
| `axial_vector_model_building-v6.pdf` | 33 | 2,759,986 | `6da901c2cea57bde8e557aff03c16198934c4f2e987147046c8031f2e8ad75f4` | 64,993 |
| `dw13678_report_1_a.pdf` | 4 | 161,829 | `752226d16c3aa57c1dffad338860976c88f5f6c82426b69a6b1c8ce2886bfba6` | 12,496 |
| `（原件）dw13678_report_1_a.pdf` | 4 | 158,794 | `ac7357aa2e9d29a9de3198f31f03e72c5c97f7c15b2a12875d73ff7d826c7d5e` | 12,496 |
| `Replies_to_Referee_3_referee_facing_2026-11-04.pdf` | 63 | 500,497 | `e0a2114e5e932d02794a1cdf074c9214ed201f71ff37fc25a72314af05ed4051` | 121,917 |

The two referee PDFs produce identical concatenated pypdf-extracted text, including page order. Their annotation objects are different: the first has 18 `/Highlight`, 20 `/Popup` and 2 `/Underline` objects; the original-named variant has 15, 17 and 2 respectively. This supersedes the earlier metadata-scan finding of one versus four highlights. Both files remain preserved; text equality does not imply equal annotations or visual presentation.

The 63-page current response PDF is distinct from the 65-page 2026-11-06 historical build. Its stored source/PDF pair has not yet been independently rebuilt and visually compared.

## Reproduction

Use `pypdf.PdfReader` to enumerate pages, concatenate `page.extract_text() or ''`, and count `a.get_object().get('/Subtype')` for each entry in each page's `/Annots`; calculate byte hashes with `hashlib.sha256`. Do not rely on annotation count alone to infer source provenance.

An attempted `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/axial_repo_response_build Replies_to_Referee_3_referee_facing_2026-11-04.tex` did **not** build: the environment could not locate `pdflatex.fmt`. No page-render or successful compilation claim is made. Install or select a complete TeX distribution, rerun from the exact source/dependency revision, and visually inspect the output before accepting the PDF.

## Subsequent build and clipping finding

The initial format-file failure above was subsequently resolved with a temporary local TeX format and font map. Rebuilding the unchanged source produced a 63-page PDF. Visual comparison found that page 43 in both the tracked PDF and the same-source rebuild has an oversized Figure 1 caption that overlaps the page number and extends below the page: the end of the caption is not visibly rendered. The LaTeX log reported `Float too large for page by 255.35114pt`. This is a presentation defect and should be corrected before the PDF is submitted.

A local candidate moved the original caption text, unchanged, into a paragraph immediately after the figure and used a short caption. That candidate compiled to 64 pages; the affected pages 42–44 were visually inspected and the original scientific text was retained. The candidate is **not committed to this branch** and the tracked PDF remains unchanged; full-page visual inspection and publication of a matched TeX/PDF pair remain outstanding. The temporary build artifacts are no longer available. No conclusion about the physical validity of the cooling curve follows from this layout test.

## Layout repair accepted for this maintenance branch

The 64-page PDF (501,004 bytes, SHA-256 `095daf18a7202d11f9bf9f48077ab2ab82c1f10386059da9bf9633ae4d9ea679`) was built from the corresponding root TeX and the existing two BibTeX inputs, JHEP style and unchanged figure. Original caption text (2,253 characters; SHA-256 `3e042139e73f73b39ac42081ff494bccafe0345a1135c33eaf990cbd38d2c8c3`) is retained exactly as body text immediately after the figure. A short caption and clear page separate the figure and explanation. A reconstruction test restores the pre-edit TeX byte-for-byte by reversing these insertions and relocation. No scientific claim, parameter, formula, result or graphic was removed or recomputed.

`latexmk` completed with BibTeX, no undefined reference or oversized float warnings; one pre-existing underfull box at lines 609–611 remains. All pages were rendered and inspected as 4-by-4 contact sheets; pages 42–44 also received enlarged inspection. A PyMuPDF text-boundary scan found no lines outside the page. All fonts were embedded. Contact sheets and boundary checks are not a substitute for independent physics or high-resolution equation verification. The environment used a temporary locally generated TeX format and font map. The earlier 63-page PDF and historical Overleaf package are preserved in Git history.


## Final CI build and visual acceptance — 2026-11-16

The earlier statements above that the caption-repaired candidate was not yet committed, and that the current PDF was still the 501,004-byte local candidate, describe an intermediate checkpoint only. They are superseded by the final CI acceptance in [REPLY_LETTER_FINAL_ACCEPTANCE_2026-11-16.md](REPLY_LETTER_FINAL_ACCEPTANCE_2026-11-16.md).

The final root PDF is 64 pages / 500,973 bytes, SHA-256 `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819`, built in [Actions run #43767527054](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43767527054). The 2,253-character original Figure 1 caption is preserved exactly. All 64 pages were rendered and visually reviewed; the final page-44/45 widow adjustment was independently rebuilt and re-inspected. The build has no unresolved references, no overfull boxes or oversized floats, all fonts embedded, and no blank/out-of-bounds text. One non-clipping underfull box warning at lines 609–611 remains documented.

This remains a layout-only acceptance. It does not validate the physical cooling calculation or close the outstanding scientific questions.

## Independent current-tree follow-up — 2026-11-16

**Disposition of this extraction/layout report: PASS_WITH_NOTES.** The final CI PDF and the unchanged non-reply root PDFs were checked against the earlier extraction snapshot.

- The final 64-page PDF was extracted directly from Actions artifact `14182947154`. Its 500,973-byte payload has SHA-256 `f5f7f5c24bc04b3901f26d261d18b64ec876a2680dee23c7b3b1964abf3e1819` and Git blob `4c18235a7e025872fa14a83ca7862b9c7592ac5b`; both match the current root PDF and the final acceptance report. The earlier 63-page/500,497-byte PDF and the 64-page/501,004-byte local candidate remain historical checkpoints.
- The final CI artifact contains 64 page PNGs and 11 contact sheets (ten six-page sheets and one four-page sheet). All 11 sheets were inspected; pages 43–45 were also inspected individually. The page-boundary audit reports no blank/out-of-bounds text; all fonts are embedded; the final TeX log has one non-clipping underfull box, zero overfull boxes, and zero unresolved citations/references.
- The other three root PDFs are byte-identical to the files in the original extraction snapshot: `axial_vector_model_building-v6.pdf` (2,759,986 bytes), `dw13678_report_1_a.pdf` (161,829 bytes), and `（原件）dw13678_report_1_a.pdf` (158,794 bytes). Their earlier extraction/annotation findings therefore remain applicable.
- The two four-page referee PDFs still have identical extracted text but different annotation objects (18/20/2 versus 15/17/2 for highlights/popups/underlines). They remain blocked for visual/source equivalence; text equality is not visual equality. The 33-page manuscript PDF remains blocked because this follow-up did not render or visually inspect it.

This follow-up closes the final referee-response PDF layout/extraction task only. It does not validate the manuscript PDF's visual fidelity, establish the source provenance of the two referee-report PDFs, or validate any physical calculation.