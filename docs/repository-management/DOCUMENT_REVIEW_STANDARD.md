# Axial-vector Project Document Audit Profile

**Status:** Project-specific extension to the central Research Document Review Standard.  
**Central source commit:** 142267bc803c90aa681110293b66b73947bbcaa1

The shared review dimensions, proportionality rules, review dispositions, scientific-claim integrity, migration checks, and audit-record requirements are defined by the [central Research Document Review Standard](https://github.com/lm846802297-bit/high-energy-theory-research/blob/142267bc803c90aa681110293b66b73947bbcaa1/docs/DOCUMENT_REVIEW_STANDARD.md).

## 1. Project-specific audit requirement

Every human-readable Markdown/text document in this repository must have an individual review record in the project's audit registers. A folder README or aggregate inventory does not substitute for reviewing the documents within it. This is a stricter project-level coverage requirement; it does not mean that every ordinary edit triggers a new full-repository audit. Create or update the individual record when a document is introduced, materially revised, or included in a declared review batch.

The project maintains:
- `DOCUMENT_AUDIT_REGISTER.csv` for the original 462-document baseline;
- `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv` for later-added Markdown/text files;
- dated review reports under `docs/repository-management/`.

For TeX, BibTeX, PDFs, binary assets, code, data, and workflow YAML, use the corresponding root-file, software, data, or workflow audit procedure. Do not represent a prose-document review as technical validation of those artifacts.

## 2. Register compatibility

The existing registers preserve historical review records and their original path/blob/size fingerprints. Do not rewrite historical rows merely to conform to a new status vocabulary.

The legacy registers use `HISTORICAL` as a combined disposition for some historical entries. Preserve those existing values and their provenance. For new or materially updated records, use the central separation between review disposition (`PASS`, `PASS_WITH_NOTES`, `REVISION_REQUIRED`, `BLOCKED`, `PENDING`) and document lifecycle (`current`, `historical`, `superseded`, `archival`, etc.). If a future register-schema migration is undertaken, retain the original legacy values in the historical snapshot and map them explicitly rather than silently rewriting them.

For baseline fingerprints, `blob_sha` and `size_bytes` preserve the reviewed-version identity; `current_blob_sha` and `current_size_bytes` describe the current tree. Never overwrite the historical reviewed fingerprint simply to make it match the current file.

## Coverage tracking

`DOCUMENT_AUDIT_REGISTER.csv` preserves the original 462-document Markdown/text baseline. `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv` inventories later-added Markdown/text files. At the 2026-11-23 first-batch integration checkpoint, the repository contains **877 Markdown/text files** (646 \`.md\` and 231 \`.txt\`): 462 baseline entries plus 415 supplemental entries. The baseline has 0 \`PENDING\` entries (462/462 dispositioned): 304 \`PASS_WITH_NOTES\`, 2 \`PASS\`, 156 \`HISTORICAL\`, and 0 \`REVISION_REQUIRED\`. The supplemental register has 167 \`PASS_WITH_NOTES\`, 6 \`HISTORICAL\`, 242 \`PENDING\`, and 0 \`REVISION_REQUIRED\`. The 242 pending entries are pre-existing documents that were previously absent from the supplemental inventory: 240 documents in the RC001 upstream research archive and two repository-management documents. They are now individually inventoried but have **not** been content-reviewed; their status must remain \`PENDING\` until each file is read and dispositioned.

All 877 current Markdown/text paths are registered exactly once: the baseline and supplemental registers have no missing, duplicate, overlapping or unregistered paths. Current blob SHA/size fields match the recursive Git tree. The baseline reviewed-version fingerprints are preserved separately from current-tree fingerprints: 367 \`MATCH_CURRENT\`, 94 \`CONTENT_FINGERPRINT_DIFFERS\`, and 1 \`SIZE_METADATA_DIFFERS\`. These 95 historical fingerprint differences are not missing files or current-tree metadata mismatches. The current tree contains 2,380 entries (2,218 files and 162 directories). The 26 documents added in the B.13/B.16 first-batch integration have individual \`PASS_WITH_NOTES\` records. See the [first-batch integration review](FIRST_BATCH_B13_B16_INTEGRATION_REVIEW_2026-11-23.md).

Update a row only after reading the complete file and recording a defensible outcome. In the baseline register, \`blob_sha\` and \`size_bytes\` preserve the reviewed-version fingerprint; \`current_blob_sha\` and \`current_size_bytes\` describe the live tree. \`fingerprint_status\` is \`MATCH_CURRENT\`, \`CONTENT_FINGERPRINT_DIFFERS\`, or \`SIZE_METADATA_DIFFERS\`. Do not overwrite the reviewed fingerprint merely to make the row match. When files are added, removed or renamed, refresh the supplemental inventory and retain the prior audit snapshot.

