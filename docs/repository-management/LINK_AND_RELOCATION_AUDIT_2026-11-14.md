# Local path and workflow-review relocation audit — 2026-11-14

> **Later update:** The 63-page PDF described below is historical. A matched 64-page layout-fixed build is documented in [the PDF audit](ROOT_PDF_EXTRACTION_AUDIT_2026-11-14.md).

> **Later checkpoint:** the [manifest review](MANIFEST_REVIEW_2026-11-14.md) and [legacy-log review](LEGACY_LOG_REVIEW_2026-11-14.md) examined additional baseline entries; 357 remain pending. Counts below record the earlier checkpoint.

## Changes

Seven Markdown workflow review records were moved from `.github/workflows/` to `docs/repository-management/workflow-reviews/`. The original and destination blob IDs, SHA-256 hashes and sizes are recorded in the [relocation manifest](workflow-reviews/RELOCATION_MANIFEST_2026-11-14.json). All seven contents are byte-identical before/after. The workflow index links were updated; no YAML file, workflow trigger, Python source, physics equation or numerical output was moved by this migration.

Historical bare file URLs to the old review paths will not redirect automatically. The manifest maps each old path to the replacement, and links pinned to old commits continue to identify the original file. No claim is made that external sites or private copies were updated.

## Local Markdown links

Pandoc's GFM parser was applied to each tracked Markdown file in the post-move working tree. Before the six repairs, 394 files produced zero parser errors and six local target candidates:

1. The deliverables index pointed to `review_package_extracted/`, a retired duplicate directory; it now points to the actual collaborator archive and source/provenance index.
2. A stellar-cooling plan used an incorrect parent directory for the archived profile-sensitivity JSON; the relative path is corrected.
3. One of three links to the 2026-11-08 Table II manuscript checklist omitted `../`; it is corrected.
4. Three historical Higgs-portal v64/v65/v66 documents referenced a missing SVG. They now reference the existing file in `deliverables/higgs_portal_mixing_md_with_svg/`, whose archive provenance and checksum are recorded there. Their section 187 wording matches the SVG handoff document. The image is an illustrative topology and does not validate its physics.

After the repairs and staging of the newly added indexes/reports, 400 Markdown files parsed without errors and the local path check returned zero missing or outside-repository targets. This checks only destinations returned as Markdown links/images by Pandoc; it does **not** validate section anchors, HTML-only links, file paths in prose, generated files, external URLs, or document claims. It is not a document-by-document scientific review.

## Code, workflow and register checks

- The seven relocated files are Markdown, and no Python or YAML workflow path was moved.
- Python `ast.parse` accepted all 398 tracked `.py` files. This is syntax-only: it neither imports dependencies nor executes tests.
- PyYAML parsed all 109 tracked workflow YAML files. This does not validate GitHub Actions schema, permissions, triggers or execution.
- A limited scan found 168 literal `python ... .py` commands beginning a workflow shell line; all resolved in the current checkout under the declared/default working directory. Three dynamic candidates were skipped. Heredocs, `cd`, shell variables, module calls, other commands, branch-specific files and GitHub expression evaluation require separate checks.
- The baseline document register retains 462 data rows. Ten rows had an extra empty seventh CSV field; those empty fields were removed, leaving six fields on every row. The baseline blob/size columns still identify the original inventory, not necessarily the current edited files. No outcome was changed by this CSV repair.
- The two individually read attachments are marked historical with specific scope notes; the register contains 67 non-pending and 395 pending baseline entries. New management documents are outside this baseline and are not counted as reviewed by it.

## Scientific preservation and remaining work

The change does not edit the referee-facing TeX, manuscript source, equations, physical results or numerical output. The historical attachment warning banners do not delete arguments or conclusions. The three historical portal files received link and asset-location prose edits only; the manuscript synchronization checklist received one link correction. In accordance with `审稿意见-gpt/写作规范/审稿回复写作原则.md` §§3.1, 6 and 7, the deletion/merge ledger is **none** for substantive scientific arguments; see the diff for the exact editorial replacements.

The 395 pending baseline documents, 59 pending workflows and further review of 16 historical-candidate workflows remain open. The static checks above do not prove all Python imports, TeX inputs, workflow behavior, external handoffs, or the scientific contents of every document. The current reply PDF still requires a same-source build and page-by-page review; the local build attempt failed because `pdflatex.fmt` is missing, as recorded in the [PDF audit](ROOT_PDF_EXTRACTION_AUDIT_2026-11-14.md).
