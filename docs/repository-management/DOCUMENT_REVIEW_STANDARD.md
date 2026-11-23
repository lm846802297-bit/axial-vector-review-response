# Axial-vector Project Document Audit Profile

**Status:** Project-specific extension to the central Research Document Review Standard.  
**Central source commit:** 142267bc803c90aa681110293b66b73947bbcaa1

The shared review dimensions, proportionality rules, review dispositions, scientific-claim integrity, migration checks, and audit-record requirements are defined by the [central Research Document Review Standard](https://github.com/lm846802297-bit/high-energy-theory-research/blob/142267bc803c90aa681110293b66b73947bbcaa1/docs/DOCUMENT_REVIEW_STANDARD.md).

## 1. Project-specific audit requirement

For a declared repository-wide document audit in this project, every in-scope human-readable Markdown/text document must receive an individual review record. A folder README or aggregate inventory does not substitute for reviewing the documents within it. This is a stricter project-level requirement; it does not require a full repository audit for every ordinary research task or minor edit.

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

`DOCUMENT_AUDIT_REGISTER.csv` preserves the original 462-document Markdown/text baseline. `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv` inventories later-added Markdown/text files. At the 2026-11-17 final integration-review checkpoint, the repository after the 2026-11-17 root relocation contains 605 such files (506 `.md` and 99 `.txt`): 462 baseline entries plus 143 supplemental entries. The baseline has 0 `PENDING` entries (462/462 individually reviewed), with 297 `PASS_WITH_NOTES`, 2 `PASS`, 156 `HISTORICAL`, and 7 `REVISION_REQUIRED`; the supplemental register has 137 `PASS_WITH_NOTES`, 6 `HISTORICAL`, 0 `PENDING`, and 0 `REVISION_REQUIRED` entries. Every supplemental document has an individual review disposition; the remaining 7 `REVISION_REQUIRED` items belong to the separate 462-document baseline. The current branch tree has 1,712 entries (1,581 files and 131 directories). Both registers have unique, non-overlapping paths with no missing or unregistered Markdown/text files; all current SHA/blob and size fields match the tree. The baseline reviewed-version fingerprints classify 389 rows as `MATCH_CURRENT`, 72 as `CONTENT_FINGERPRINT_DIFFERS`, and 1 as `SIZE_METADATA_DIFFERS`; these differences are preserved historical reviewed-version fingerprints, not unregistered files or current-tree mismatches. Update a row only after reading the complete file and recording a defensible outcome. In the baseline register, `blob_sha` and `size_bytes` preserve the reviewed-version fingerprint; `current_blob_sha` and `current_size_bytes` describe the live tree. `fingerprint_status` is `MATCH_CURRENT`, `CONTENT_FINGERPRINT_DIFFERS`, or `SIZE_METADATA_DIFFERS`. Do not overwrite the reviewed fingerprint merely to make the row match. The merged PR #115 integration report documents the seven explicitly retained baseline blockers, verified workflow run histories and full diff review: [FINAL_INTEGRATION_REVIEW_2026-11-17.md](FINAL_INTEGRATION_REVIEW_2026-11-17.md). When files are added, removed or renamed, refresh the supplemental inventory and retain the prior audit snapshot.

