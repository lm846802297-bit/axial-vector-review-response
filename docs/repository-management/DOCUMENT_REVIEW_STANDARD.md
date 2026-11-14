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
- `HISTORICAL_ONLY`: intentionally preserved and not to be used as current guidance.
- `NOT_REVIEWED`: inventory only; no content-level review claim.

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

`DOCUMENT_AUDIT_REGISTER.csv` enumerates the current Markdown/text-document set at the audited base commit. Its initial `PENDING` entries are intentional. Update each row only after reading the complete document and recording a defensible outcome. When files are added, removed or renamed, regenerate the inventory and retain the prior audit snapshot.
