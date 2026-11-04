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

## Compile and PDF validation boundary

The source-level audit is complete, but the corrected PDF has **not** been rebuilt or visually inspected in this task. The required classic BibTeX sequence is:

```bash
pdflatex Replies_to_Referee_3_referee_facing_2026-11-04.tex
bibtex Replies_to_Referee_3_referee_facing_2026-11-04
pdflatex Replies_to_Referee_3_referee_facing_2026-11-04.tex
pdflatex Replies_to_Referee_3_referee_facing_2026-11-04.tex
```

After compilation, inspect the `.blg` for missing entries/style errors and verify that the PDF has no `[?]` citations and that every cited work appears in the bibliography. No PDF is claimed to be fixed until that check is performed.
