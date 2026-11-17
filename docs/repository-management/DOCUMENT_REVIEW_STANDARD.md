# Document-by-document review standard

## Purpose

Every human-readable document in this repository must receive an individual review record. A folder README or a bulk inventory does not substitute for reviewing the documents inside it.

## Required checks for each document

1. **Identity and role** — title, purpose, intended audience, workstream and document type.
2. **Authority and lifecycle** — current authority, historical snapshot, working draft, superseded note or deliverable. Identify the canonical replacement when one exists.
3. **Scientific content** — equations, definitions, conventions, dimensions, units, approximations, parameter values and limiting cases. Check against the stated model and the cited derivation; do not infer correctness from polished prose.
4. **Evidence and citations** — references resolve, support the attached claim, and are sufficiently specific. Separate literature statements, author assumptions, numerical observations and conclusions.
5. **Consistency** — compare model content, benchmarks, numerical values and status statements with current decisions and authoritative workstream records.
6. **Reproducibility** — source commit, input data, configuration, exact command, software environment, output location, checksums and validation criteria where applicable.
7. **Links and assets** — validate relative Markdown links, images, PDFs, data paths and cross-document anchors.
8. **Language and structure** — clear title, summary, scope, definitions, results, limitations and next steps; remove contradictory or stale instructions without erasing historical facts.
9. **Disposition** — retain, revise, mark historical, merge into a canonical document, or propose archival/removal. Deletion requires provenance and inbound-reference checks.

## Review outcomes

- `PASS`: all applicable checks completed with no blocking issue.
- `PASS_WITH_NOTES`: usable, with non-blocking caveats recorded.
- `REVISION_REQUIRED`: at least one actionable issue.
- `BLOCKED`: cannot validate because source, data, cited paper, or required context is unavailable.
- `HISTORICAL`: intentionally preserved for provenance and not to be used as current guidance.
- `PENDING`: inventory only; no content-level review claim.

These are the canonical register values used in `DOCUMENT_AUDIT_REGISTER.csv` and `README.md`; do not substitute `HISTORICAL_ONLY` or `NOT_REVIEWED`.

## Scientific claim discipline

A document must distinguish:
- analytic derivation from numerical implementation;
- pointwise tests from global convergence;
- local rate validation from transport validation;
- code/CI success from physical acceptance;
- conditional benchmark from a final exclusion;
- original one-VEV model from any two-VEV extension.

Do not silently change a result, uncertainty, benchmark, model assumption or physical conclusion during editorial cleanup. Flag scientific discrepancies for a separate author decision.

## Audit record format

For each file record: path, title, role, workstream, lifecycle/authority, outcome, findings, required action, reviewed commit SHA, reviewer/date. For code/data artifacts, use the corresponding software/data validation checklist rather than pretending they are prose documents.

## Coverage tracking

`DOCUMENT_AUDIT_REGISTER.csv` preserves the original 462-document Markdown/text baseline. `SUPPLEMENTAL_DOCUMENT_AUDIT_REGISTER.csv` inventories later-added Markdown/text files. At the 2026-11-17 tree checkpoint after the eighty-eighth review, the repository contains 593 such files (494 `.md` and 99 `.txt`): 462 baseline entries plus 131 supplemental entries. The baseline has 0 `PENDING` entries (462/462 individually reviewed), with 296 `PASS_WITH_NOTES`, 2 `PASS`, 156 `HISTORICAL`, and 8 `REVISION_REQUIRED`; the supplemental register has 125 `PASS_WITH_NOTES`, 6 `HISTORICAL`, 0 `PENDING`, and 0 `REVISION_REQUIRED` entries. Every supplemental document has an individual review disposition; the remaining 8 `REVISION_REQUIRED` items belong to the separate 462-document baseline. The current recursive Git tree has 1,690 entries (1,567 files and 123 directories). Both registers have unique, non-overlapping paths with no missing or unregistered Markdown/text files; all current SHA/blob and size fields match the tree. The baseline reviewed-version fingerprints classify 389 rows as `MATCH_CURRENT`, 72 as `CONTENT_FINGERPRINT_DIFFERS`, and 1 as `SIZE_METADATA_DIFFERS`; these differences are reconciliation flags, not automatic review-outcome changes. Update a row only after reading the complete file and recording a defensible outcome. In the baseline register, `blob_sha` and `size_bytes` preserve the reviewed-version fingerprint; `current_blob_sha` and `current_size_bytes` describe the live tree. `fingerprint_status` is `MATCH_CURRENT`, `CONTENT_FINGERPRINT_DIFFERS`, or `SIZE_METADATA_DIFFERS`. Do not overwrite the reviewed fingerprint merely to make the row match. When files are added, removed or renamed, refresh the supplemental inventory and retain the prior audit snapshot.
