# Eighth review batch — current navigation, workflow catalog and reply archive (2026-11-14)

## Scope

Reviewed five high-traffic entry documents and checked their local Markdown links against the current branch tree:
- `research/README.md`
- `审稿意见-gpt/当前执行/README.md`
- `审稿意见-gpt/写作规范/审稿回复写作原则.md`
- `.github/workflows/README.md`
- `archive/reply-letter/README.md`

The link scan found all local links valid except one self-link in the writing-principles document. The archive README had stale current-build metadata and an outdated claim about the current TeX having no figure dependency.

## Individual findings and actions

| Document | Outcome | Findings and action |
|---|---|---|
| `research/README.md` | PASS_WITH_NOTES | The 12 local links resolve. The directory map keeps Major 1, stellar cooling, collaborator archive and the original one-VEV/two-VEV boundary separate. Its statement that local checks alone do not authorize a final axial-limit update is consistent with the current research status. No content edit was required. |
| `审稿意见-gpt/当前执行/README.md` | PASS_WITH_NOTES | All 7 local links resolve. It correctly directs live status to `PROJECT_STATUS.md`, research acceptance to the research index, and model scope to the decision ledger. It separates optional Major 3/4.1 neutrino completion from the original model. No content edit was required. |
| `审稿意见-gpt/写作规范/审稿回复写作原则.md` | PASS_WITH_NOTES | The mandatory writing standard is coherent and consistent with the current response workflow. One self-link used the literal destination `本文件`, which did not resolve; changed it to the actual sibling filename `审稿回复写作原则.md`. |
| `.github/workflows/README.md` | PASS_WITH_NOTES | All 111 local links resolve. The top still said 25 individually reviewed workflows, while the current register has 34 reviewed, 16 historical candidates and 59 pending; a lower paragraph still said only the first 10 had review notes. Updated both statements and linked all six current review batches plus the earlier batch-2 summary. The 109-workflow topic grouping remains provisional and filename-based. |
| `archive/reply-letter/README.md` | PASS_WITH_NOTES | All 4 local links resolve. Its “current build” still reported the 2026-11-06 65-page PDF, old size/hash, and a historical figure path; its 2026-11-05 section also described PR #49/#50 as current. Updated the top to the 2026-11-12 merge commit and current root PDF hash/size, explicitly marked the 65-page build as historical, and documented the current TeX's figure/BibTeX dependencies. Clarified that the no-figure-dependency statement applies only to the archived r2 snapshot. |

## Cross-document consistency

1. All live navigation now points to `PROJECT_STATUS.md` for PR/repository state and to the dated research index for scientific acceptance boundaries.
2. The original one-VEV model remains distinct from optional Major 3/4.1 neutrino completion; no navigation page promotes the extension into the original non-neutrino model.
3. The workflow catalog reports the same 34/16/59 split as the workflow register.
4. The reply archive now distinguishes the 2026-11-06 65-page build from the current root PDF committed on 2026-11-12. The current PDF still requires a same-source rebuild and page-by-page render audit.
5. No scientific source, numerical output, model assumption, or physical conclusion was changed.

## Edits

- Fixed one broken self-link in the writing-principles document.
- Refreshed workflow review counts and linked review batches.
- Reconciled archive README with the current TeX/PDF hashes, commit, and build dependencies.
- Updated four Markdown/text register outcomes to `PASS_WITH_NOTES`; no document was marked fully `PASS`.
