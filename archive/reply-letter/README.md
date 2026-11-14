# Referee-response letter archive

This directory preserves recoverable, immutable source snapshots of the referee-response letter. It is an archive, not a second working copy.

## Current root response status (2026-11-14)

On the maintenance branch the root TeX and PDF include a layout-only repair of the oversized Figure 1 caption. The corresponding 64-page PDF has SHA-256 `095daf18a7202d11f9bf9f48077ab2ab82c1f10386059da9bf9633ae4d9ea679`. The 63-page PR #56 PDF (`e0a2114e…`) and the older 65-page build remain historical records. The build dependencies are `references.bib`, `Replies_to_Referee_3_stellar_references.bib`, `JHEP.bst`, and `research/stellar-cooling-constraints-20261105/outputs/axial_stellar_constraints_reply_gev.pdf`.

The older source snapshots remain immutable. Statements below about two bibliographies, no figure dependency, or an outdated root PDF describe the 2026-11-04/05 snapshots and are superseded for the current build by this note. No new immutable snapshot is declared accepted by this PR.

## Source-of-truth rule

The only editable, authoritative response letter remains at the repository root:

- `Replies_to_Referee_3_referee_facing_2026-11-04.tex`

The two bibliography databases remain at their working paths, and the root-level `JHEP.bst` is the BibTeX style used by the root-level reply source. All files under `snapshots/` are archival copies. Do not edit them in place or compile from them as the working version. For a new revision, edit the root source and working bibliography files, then create a new dated snapshot after the revision is accepted.

## Snapshots preserved

- [2026-11-04 baseline snapshot manifest](snapshots/2026-11-04/manifest.md): original TeX plus the two bibliography databases; this is the historical source backup created before the citation audit.
- `snapshots/2026-11-04-r1/manifest.md` is referenced by an older archive note but is not present in the current Git tree; treat this snapshot as an unresolved historical reference until its source commit or manifest is recovered. Do not infer that the file exists.
- [2026-11-04-r2 corrected reference snapshot manifest](snapshots/2026-11-04-r2/manifest.md): latest source package, including the root-level `JHEP.bst` and the completed NA64, CHARM-II, and HNL bibliographic metadata.

The `2026-11-04-r2` snapshot is the reference-complete recovery point for the 2026-11-04 source state. It does not include the subsequent referee-response TeX edits in PR #49 or PR #50; use the repository-root TeX on the current branch/main as the editable source. The older snapshots remain unchanged for history.

## Citation audit result

The 2026-11-04-r2 response TeX snapshot contained 45 citation commands, representing 72 citation-key occurrences and 34 unique citation keys. All 34 keys resolved in the two bibliography databases; no duplicate keys were found, and both databases passed a static brace-balance scan. This is a historical snapshot audit, not a count for the post-PR #49/#50 source.

The likely source-level issue behind widespread `[?]` markers is the BibTeX style lookup: the root-level response TeX uses `\bibliographystyle{JHEP}`, while the original `JHEP.bst` was stored only in the nested model-source directory. A default local BibTeX search does not recursively discover arbitrary project subdirectories. A byte-identical copy is therefore now present at repository root. The 2026-11-04-r2 PDF was compiled and visually reviewed; see the build record in [the r2 manifest](snapshots/2026-11-04-r2/manifest.md). That PDF predates the TeX changes in PR #49 and PR #50 and is not a current build of the root-level response source.

## Historical source/PDF status snapshot (2026-11-05; superseded by the 2026-11-12 merge)

This paragraph records only the state as of 2026-11-05: PR #49 had merged, PR #50 was a later referee-response-only update, and the root PDF was still the 2026-11-04-r2 build. It is superseded by the 2026-11-12 PR #56 merge and the current root-file status above. Do not use the 2026-11-04-r2 PDF as the current compiled response.

## Restore procedure for the 2026-11-04-r2 historical snapshot

1. Check out or download the source commit recorded in the selected snapshot manifest.
2. For the latest corrected package, restore the TeX snapshot to the repository root and remove the `.snapshot` suffix.
3. Restore the two bibliography snapshots to their original working paths, removing `.snapshot`:
   - `Replies_to_Referee_3_neutrino_references.bib` at the repository root;
   - `overleaf-source/axial-vector-model-building-v6/references.bib`.
4. Restore `JHEP.bst.snapshot` to repository-root `JHEP.bst`.
5. Verify the restored files against the blob SHA-1 values in the selected manifest before editing or compiling.

For the original full repository state at the baseline source commit, use GitHub's commit-addressed ZIP archive:

[Download repository snapshot at d9b262798f80c0f109f328b1b0019191e99d5437](https://github.com/lm846802297-bit/axial-vector-review-response/archive/d9b262798f80c0f109f328b1b0019191e99d5437.zip)

GitHub generates this archive on request; it is not a separately uploaded binary asset.

## Git tag

A tag is a repository reference, not a file that can be committed as part of a pull-request diff. After this PR is merged, create the annotated tag:

`reply-letter-2026-11-04`

pointing to the fixed baseline source commit `d9b262798f80c0f109f328b1b0019191e99d5437`. The tag has not been created. The newer reference-complete package is independently pinned by the PR commits and the `2026-11-04-r2` manifest.

After merge, create and push the baseline tag from a local clone:

```bash
git tag -a reply-letter-2026-11-04 d9b262798f80c0f109f328b1b0019191e99d5437 -m "Archive referee-response letter source and bibliography state as of 2026-11-04"
git push origin reply-letter-2026-11-04
```

## Historical 2026-11-04-r2 snapshot build boundary

For the archived 2026-11-04-r2 source snapshot only, the response TeX had no `\input`, `\include`, or `\includegraphics` file dependencies. **This statement does not apply to the current root TeX**, which includes one figure dependency: `research/stellar-cooling-constraints-20261105/outputs/axial_stellar_constraints_reply_gev.pdf`. The current source also uses the two root BibTeX databases and root `JHEP.bst`. LaTeX packages such as `amsmath`, `slashed`, `graphicx`, `multirow`, `needspace`, `placeins`, `microtype`, `url`, `xcolor`, and `hyperref` remain TeX-environment dependencies.

The historical 2026-11-04-r2 PDF was built from the reference-complete r2 source package. Its build commit and source blob IDs are recorded in the r2 manifest. That snapshot build record reports one remaining overfull-box warning in the NA64 table; the table was visually judged readable. Raw `.log` and `.blg` files were not retained in the repository. This historical check does not validate the current 2026-11-12 root PDF.
