# Organization change: author-side diff review — 2026-11-14

Review baseline: maintenance branch `e4dd7ec4df4c83f70c5ab53bc7b91bea4f1eede9`, after synchronizing `main`. This is an author-side review, not an independent reviewer or physical recalculation.

## Preservation audit

The review applies [writing rules §3.1, §6 and §7](../../审稿意见-gpt/写作规范/审稿回复写作原则.md) because it touches supporting historical notes and the internal manuscript checklist.

| Before | After | Scientific preservation |
|---|---|---|
| Seven workflow-review Markdown reports next to workflow YAML | Same seven byte-identical reports under `workflow-reviews/`; the workflow index links to them | Git blob and SHA-256 mapping is recorded in the relocation manifest; no YAML change. |
| Historical portal v64/v65/v66 embed a missing SVG | Image links point to the documented extracted asset and the asset-location note is updated | No equations, vertices, calculations, numbers or arguments removed. The asset's §187 caption and explanatory text match the packaged document. |
| Two historical attachments contain old unqualified claims | Added scope warnings and links; original body retained | No substantive argument, applicability condition or historical result deleted or merged. |
| One internal Table II link and one historical plan link use wrong relative paths | Correct targets | No manuscript or referee-facing TeX text changed. |
| Deliverables index points to retired duplicate package | Points to canonical archive guide and provenance index | No payload removed; distinguishes current canonical sources from historical extraction metadata. |
| Root PDF review recorded incomplete metadata-scan annotation counts | New pypdf extraction audit and explicit correction | No binary edited. Extracted text equality is not a visual comparison. |

**Substantive scientific deletion/merge ledger:** none. The seven report path moves and their updated links are documented separately in the relocation manifest. Ten empty extra CSV columns were removed without altering their meaningful fields. Repository statuses, file hash information, and historical assumptions are not evidence of physical validation.

## Verification and unresolved items

`LINK_AND_RELOCATION_AUDIT_2026-11-14.md` records the syntax/path checks and their limitations. The current response PDF could not be rebuilt locally because `pdflatex.fmt` was absent; its page-by-page visual verification remains open. At the original diff-review checkpoint the register contained 395 pending baseline documents; the later manifest review reduced this to 374, while three additional provenance issues remain revision-required. Workflow classification still contains pending/historical candidates. This review does not approve the PR as a complete repository-wide scientific audit.


## Follow-up manifest review

The follow-up adds warnings to three existing research notes and current checksum sidecars while preserving the original manifests, archived source files, outputs and reported historical values. The radial-scalar scan's two sets of source and CSV hashes are now traced to separate runs; the comparison and bound-column correction are recorded. The current uncompressed CSV remains unavailable as a directly committed file. No scientific argument or result is deleted or merged. This remains an author-side review under writing rules §§3.1, 6 and 7, not a full physical re-derivation.
