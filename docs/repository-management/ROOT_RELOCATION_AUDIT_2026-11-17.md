# Root-file relocation and directory-entry audit — 2026-11-17

## Scope

This follow-up implements root-file archival (PR A) and directory entry points (PR B), based on `main` commit `ce9cf1628efc16c55d64aa59f93b7d745f8ef23e`, on branch `chore/root-archive-and-directory-index-20261117`.

Twelve root-level files are moved into lifecycle-appropriate directories. The authoritative 2026-11-04 response TeX/PDF and its working BibTeX/style dependencies remain at root. No scientific source code, production output, equation, model assumption, numerical result, constraint curve, or formal-response content is edited. No files are deleted; all moves reuse the original Git blob SHA and size. The root goes from 24 files to 12.

## Path mapping

| Previous path | New path |
|---|---|
| `Replies_to_Referee_3_referee_facing_2026-10-28.tex` | `archive/reply-letter/versions/Replies_to_Referee_3_referee_facing_2026-10-28.tex` |
| `Replies_to_Referee_3_referee_facing_2026-11-03.tex` | `archive/reply-letter/versions/Replies_to_Referee_3_referee_facing_2026-11-03.tex` |
| `higgs_portal_mixing_merged_guide-gemini.md` | `archive/research/major1-higgs-scalar-mixing/2026-10/higgs_portal_mixing_merged_guide-gemini.md` |
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(65).md` | `archive/research/major1-higgs-scalar-mixing/2026-10/higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(65).md` |
| `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(66).md` | `archive/research/major1-higgs-scalar-mixing/2026-10/higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261019)(66).md` |
| `单圈混合推导独立复核报告-协调更新版-20261019.md` | `archive/research/major1-higgs-scalar-mixing/2026-10/单圈混合推导独立复核报告-协调更新版-20261019.md` |
| `中微子扇区电荷分析-hy4-统一更新版-20261019.md` | `archive/referee-analysis/2026-10/中微子扇区电荷分析-hy4-统一更新版-20261019.md` |
| `审稿意见逐条对照表-统一更新版-20261019.md` | `archive/referee-analysis/2026-10/审稿意见逐条对照表-统一更新版-20261019.md` |
| `axial_vector_model_building-v6.pdf` | `archive/manuscript-baselines/axial_vector_model_building-v6.pdf` |
| `dw13678_report_1_a.md` | `审稿意见-gpt/原始审稿材料/dw13678_report_1_a.md` |
| `dw13678_report_1_a.pdf` | `审稿意见-gpt/原始审稿材料/dw13678_report_1_a.pdf` |
| `（原件）dw13678_report_1_a.pdf` | `审稿意见-gpt/原始审稿材料/（原件）dw13678_report_1_a.pdf` |

Exact byte-preservation records are in [`ROOT_RELOCATION_MANIFEST_2026-11-17.csv`](ROOT_RELOCATION_MANIFEST_2026-11-17.csv). The two referee-PDF SHA-256 values are recorded from the previous PDF audit; for other files this manifest records Git blob SHA and size.

## Directory entry points

Added [`archive/README.md`](../../archive/README.md), [`overleaf-source/README.md`](../../overleaf-source/README.md), [`审稿意见-gpt/README.md`](../../审稿意见-gpt/README.md), and [`审稿意见-gpt/原始审稿材料/README.md`](../../审稿意见-gpt/原始审稿材料/README.md). Updated the existing [reply-letter archive README](../../archive/reply-letter/README.md) to link historical TeX versions.

## Preservation and authority

- v65 and v66 are sequential snapshots, not duplicates; v66 adds §262.
- The early single-loop review remains historical, including its math-conversion residue.
- The neutrino analysis does not change the original single-VEV `S+VLL` model; `sigma+3N_R` remains response-only discussion for Major 3/4.1.
- The two referee PDFs have identical extracted text/page count but distinct bytes and annotations; both remain preserved, with no visual-equivalence claim.
- The current Major 1 authority remains `research/major1-higgs-scalar-mixing-20261109/README.md`.

## Register and validation

Seven baseline-register paths are updated without overwriting reviewed-version fingerprints. Five new Markdown documents are added to the supplemental register as `PASS_WITH_NOTES`; the existing reply-letter README fingerprint is refreshed. The text inventory becomes 601 files (502 Markdown, 99 TXT): 462 baseline plus 139 supplemental (133 `PASS_WITH_NOTES`, 6 `HISTORICAL`). Seven baseline `REVISION_REQUIRED` items remain open.

The root reply TeX, PDF, both bibliography databases, `JHEP.bst` and figure dependency remain at their original paths. No Python/Mathematica/FORM source, workflow YAML, production data, or active Major 2/3/4.2 script is moved. No LaTeX build, test suite, workflow, or physics calculation is run because source/build inputs and computation code are unchanged. Link checks cover the principal entry points and changed navigation, not every prose path, historical URL, HTML link or anchor across the entire repository. PR #116 is the integration vehicle for this change; this audit records the file/path validation and does not itself attest to merge status. See [PR #116](https://github.com/lm846802297-bit/axial-vector-review-response/pull/116) for the current integration state.
