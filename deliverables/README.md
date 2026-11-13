# Extracted deliverables

This directory contains directly usable files, not ZIP bundles. Generated delivery archives and Base64 ZIP parts are not committed to main.

## Available packages

- Major 3 Overleaf import: [Overleaf_Reply_Letter_PR72_2026-11-13/](Overleaf_Reply_Letter_PR72_2026-11-13/)
  - Upload all files and subdirectories to a blank Overleaf project, preserving paths.
  - Includes main.tex, both bibliography databases, JHEP.bst, reply-figure PDF, reference PDF, instructions, original archive manifest, and current file-level checksums.
- Higgs-portal document handoff: [higgs_portal_mixing_md_with_svg/](higgs_portal_mixing_md_with_svg/)
  - Markdown and SVG assets are extracted individually, with SHA-256 and provenance.
- Axial stellar-cooling independent-review snapshot:
  [../research/stellar-cooling-constraints-20261105/review_package_extracted/](../research/stellar-cooling-constraints-20261105/review_package_extracted/)
  - Contains the pinned review source, inputs, outputs, figures, tests, report, and extraction manifest.

## Integrity

Each package has a SHA256SUMS.txt file and extraction provenance. The original Overleaf external manifest and the stellar package's per-part metadata are preserved alongside the extracted files.

## Source-data exception

The official SFHo/FRDM v1.03 ZIP archives and split BIN source parts under research/stellar-cooling-constraints-20261105/blinov_reproduction/data/sfho-frdm-v1.03/ are original upstream EOS inputs, not generated delivery packages. They remain pinned by the source manifest and are used by the current reassembly/provenance workflow. Replacing them requires extracting the raw tables, checking per-file hashes, and migrating the reader before deleting the source containers.
