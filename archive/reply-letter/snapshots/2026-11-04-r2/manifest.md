# Snapshot manifest — 2026-11-04-r2 (reference-resolution correction)

## Snapshot identity

- **Purpose:** corrected, recoverable referee-response source package after the citation/BibTeX audit.
- **Snapshot source branch HEAD before snapshot creation:** `c8e8c56e839803cb5e2293553ee84201af3828cb`.
- **Original TeX and bibliography baseline:** `d9b262798f80c0f109f328b1b0019191e99d5437`; the TeX text itself is unchanged.
- **Snapshot date:** 2026-11-04.
- **Authoritative editable TeX:** repository-root `Replies_to_Referee_3_referee_facing_2026-11-04.tex`.
- **Build support:** repository-root `JHEP.bst`, added as a byte-identical copy of the pre-existing nested style file so BibTeX can find the style from the root-level reply source.
- **Archive policy:** these `.snapshot` files are immutable archival copies, not working files.

## Files and Git blob IDs

| Original / working path | Snapshot path | Snapshot Git blob SHA-1 |
|---|---|---|
| `Replies_to_Referee_3_referee_facing_2026-11-04.tex` | `Replies_to_Referee_3_referee_facing_2026-11-04.tex.snapshot` | `a36cfa0069b578dc7796e580b54cb95a57730fef` |
| `Replies_to_Referee_3_neutrino_references.bib` | `Replies_to_Referee_3_neutrino_references.bib.snapshot` | `d5e1b6e10951c9626ff52928a24df6d3d6130b2d` |
| `overleaf-source/axial-vector-model-building-v6/references.bib` | `axial-vector-model-building-v6-references.bib.snapshot` | `6a88611b2f064093a68cf388ed2c2abd6035fc74` |
| `JHEP.bst` (root-level copy) | `JHEP.bst.snapshot` | `d39cbe846e531ed7be07eebb11be0bd72d675579` |

The root-level `JHEP.bst` copy is byte-for-byte identical to the original `overleaf-source/axial-vector-model-building-v6/JHEP.bst` (original blob SHA-1 `d39cbe846e531ed7be07eebb11be0bd72d675579`).

## Citation and bibliography audit

- 45 citation commands were found in the response TeX, representing 72 citation-key occurrences and 34 unique citation keys.
- All 34 unique keys resolve to entries in the two bibliography databases.
- No duplicate citation keys were found across the two databases.
- Both bibliography files passed a static brace-balance scan.
- Three metadata corrections were made:
  1. `NA64:2023lightDM`: added `Phys. Rev. Lett. 131 (2023) 161801` and DOI `10.1103/PhysRevLett.131.161801` (arXiv:2307.02404).
  2. `geiregat1990first`: added DOI `10.1016/0370-2693(90)90146-W`.
  3. `He:2024twoSingletHNL`: added arXiv identifier `2401.14687`.

The 2026 preprints `Fiorillo:2026wso` (arXiv:2605.24094) and `Wang:2026supernova` (arXiv:2610.35379) remain identified as preprints; no journal or DOI is invented.

## Why the root-level style copy is included

The reply TeX ends with `\bibliographystyle{JHEP}`, while the pre-existing `JHEP.bst` was stored only under `overleaf-source/axial-vector-model-building-v6/`. A local BibTeX path test confirms that the default search path does not recursively find a style file in an arbitrary project subdirectory. The root-level copy removes this path ambiguity for the root-level reply TeX.

## Compile and PDF validation record

The corrected response PDF is present at the repository root:

- **Output:** [`Replies_to_Referee_3_referee_facing_2026-11-04.pdf`](../../../../Replies_to_Referee_3_referee_facing_2026-11-04.pdf)
- **PDF Git blob SHA-1:** `63058b5679ee85f3b0780ac565e165b2a5dbb6ab`
- **File size:** 395,889 bytes.
- **PDF format / producer:** PDF 1.5; pdfTeX 1.40.25 (TeX Live 2023).
- **Build commit:** `a9edb509dc47932b872465b5d0dd1263bd1c26da`, whose parent is source commit `edce6a37a162e9fe97b5162bd2107656f50865db`.
- **Source identity:** the TeX, both bibliography databases, and root-level `JHEP.bst` at the build commit have the same Git blob SHA-1 values as the current `main` source files and this r2 snapshot:
  - TeX: `a36cfa0069b578dc7796e580b54cb95a57730fef`
  - Reply bibliography: `d5e1b6e10951c9626ff52928a24df6d3d6130b2d`
  - Model bibliography: `6a88611b2f064093a68cf388ed2c2abd6035fc74`
  - `JHEP.bst`: `d39cbe846e531ed7be07eebb11be0bd72d675579`

The recorded build sequence is:

```bash
pdflatex Replies_to_Referee_3_referee_facing_2026-11-04.tex
bibtex Replies_to_Referee_3_referee_facing_2026-11-04
pdflatex Replies_to_Referee_3_referee_facing_2026-11-04.tex
pdflatex Replies_to_Referee_3_referee_facing_2026-11-04.tex
```

The corresponding `PROJECT_STATUS.md` build record reports 34 bibliography entries, 48 PDF pages, no unresolved citation/cross-reference markers or `[?]`/ `??` placeholders, embedded fonts, and a full-page thumbnail plus targeted table/equation/reference-page visual review. No clipping, overlap, or unreadable content was reported.

One layout warning remains recorded: `Overfull \\hbox (44.0084pt too wide)` at TeX source lines 757–774, corresponding to the six-column NA64 table on PDF page 29. The table was judged visually readable; the warning is not represented as fixed. CI was not run.

The build `.log` and `.blg` files are not committed in the repository, so the validation details above are the retained build record rather than a newly re-read raw log. In the present synchronization pass, the PDF file, its Git blob SHA-1, PDF header/producer metadata, build commit ancestry, and exact source-file blob identities were rechecked. The PDF did not need to be regenerated because the current `main` sources are byte-identical to the sources used for the recorded build.
