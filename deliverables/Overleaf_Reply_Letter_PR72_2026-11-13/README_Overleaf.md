# Overleaf import package — extracted files

This directory is the individually extracted, verified snapshot of the Major 3 reply-letter package. It is not a ZIP archive.

## Import and compile

1. Create a new blank Overleaf project.
2. Upload all files and subdirectories from this directory, preserving the directory structure.
3. Keep main.tex at the Overleaf project root.
4. Use pdfLaTeX and run the usual bibliography sequence: pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX.
5. The package includes both bibliography databases (references.bib and Replies_to_Referee_3_stellar_references.bib), the JHEP.bst style, and the reply-figure PDF at the exact path referenced by main.tex.
6. reference_pdf/Replies_to_Referee_3_referee_facing_2026-11-04.pdf is a visual reference copy; it is not an input to compilation.

## Integrity and provenance

- SHA256SUMS.txt contains SHA-256 digests for the extracted files and the extraction-provenance record.
- ARCHIVE_ORIGINAL_SHA256SUMS.txt preserves the original archive manifest verbatim, including the original archive digest and embedded-file hashes.
- EXTRACTION_PROVENANCE.md records the source commit, original archive size and SHA-256, and verification performed.

The source snapshot is from main at commit 3a3e8bb0eeb54a627cf2b2df315edf8badfe1dc8. It is not the older 2026-11-09 branch export, which used an earlier TeX/PDF pair and omitted the current stellar-reference bibliography and included reply-figure PDF.
