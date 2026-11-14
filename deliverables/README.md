# Extracted deliverables

This directory contains directly usable files, not ZIP bundles. Generated delivery archives and Base64 ZIP parts are not committed to main.

## Available packages

- Major 3 Overleaf import: [Overleaf_Reply_Letter_PR72_2026-11-13/](Overleaf_Reply_Letter_PR72_2026-11-13/)
  - Upload all files and subdirectories to a blank Overleaf project, preserving paths.
  - Includes main.tex, both bibliography databases, JHEP.bst, reply-figure PDF, reference PDF, instructions, original archive manifest, and current file-level checksums.
- Higgs-portal document handoff: [higgs_portal_mixing_md_with_svg/](higgs_portal_mixing_md_with_svg/)
  - Markdown and SVG assets are extracted individually, with SHA-256 and provenance.
  - The included unified work document is a **historical 2026-10-18 working snapshot**, not the current Major 1 calculation authority or referee-facing response. Current Major 1 work is maintained under [the Major 1 research README](../research/major1-higgs-scalar-mixing-20261109/README.md); repository/PR status is maintained in [PROJECT_STATUS.md](../PROJECT_STATUS.md).
- Axial stellar-cooling collaborator archive: [archive guide](../research/stellar-cooling-collaborator-archive-20261113/README.md) and [source/provenance index](../research/stellar-cooling-constraints-20261105/REVIEW_PACKAGE_INDEX_2026-11-13.md).
  - The former `review_package_extracted/` duplicate directory was retired. Canonical inputs and results remain in their research directories; original package metadata is preserved in the collaborator archive's `provenance/` directory.

## Integrity

The extracted Overleaf and Higgs-portal packages include file-level SHA-256 records and extraction provenance. The stellar archive uses the source/provenance index and retained original package metadata; consult its guide for the current packaging and checksums.

## Source-data exception

The official SFHo/FRDM v1.03 ZIP archives and split BIN source parts under research/stellar-cooling-constraints-20261105/blinov_reproduction/data/sfho-frdm-v1.03/ are original upstream EOS inputs, not generated delivery packages. They remain pinned by the source manifest and are used by the current reassembly/provenance workflow. Replacing them requires extracting the raw tables, checking per-file hashes, and migrating the reader before deleting the source containers.
