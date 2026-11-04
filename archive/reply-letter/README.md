# Referee-response letter archive

This directory preserves recoverable, immutable source snapshots of the referee-response letter. It is an archive, not a second working copy.

## Source-of-truth rule

The only editable, authoritative response letter remains at the repository root:

- `Replies_to_Referee_3_referee_facing_2026-11-04.tex`

The two bibliography databases remain at their working paths, and the root-level `JHEP.bst` is the BibTeX style used by the root-level reply source. All files under `snapshots/` are archival copies. Do not edit them in place or compile from them as the working version. For a new revision, edit the root source and working bibliography files, then create a new dated snapshot after the revision is accepted.

## Snapshots preserved

- [2026-11-04 baseline snapshot manifest](snapshots/2026-11-04/manifest.md): original TeX plus the two bibliography databases; this is the historical source backup created before the citation audit.
- [2026-11-04-r1 manifest](snapshots/2026-11-04-r1/manifest.md): adds a root-level copy of the pre-existing nested `JHEP.bst`.
- [2026-11-04-r2 corrected reference snapshot manifest](snapshots/2026-11-04-r2/manifest.md): latest source package, including the root-level `JHEP.bst` and the completed NA64, CHARM-II, and HNL bibliographic metadata.

The `2026-11-04-r2` snapshot is the current recommended recovery point for the reference-complete source package. The older snapshots remain unchanged for history.

## Citation audit result

The current response TeX contains 45 citation commands, representing 72 citation-key occurrences and 34 unique citation keys. All 34 keys resolve in the two bibliography databases; no duplicate keys were found, and both databases passed a static brace-balance scan.

The likely source-level issue behind widespread `[?]` markers is the BibTeX style lookup: the root-level response TeX uses `\bibliographystyle{JHEP}`, while the original `JHEP.bst` was stored only in the nested model-source directory. A default local BibTeX search does not recursively discover arbitrary project subdirectories. A byte-identical copy is therefore now present at repository root. The corrected PDF still requires a complete BibTeX build and visual check; no PDF is claimed to be fixed yet.

## Restore procedure

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

## Scope and validation boundary

The response TeX has no `\input`, `\include`, or `\includegraphics` file dependencies. Its two bibliography databases and the `JHEP.bst` style are repository files. LaTeX packages such as `amsmath`, `slashed`, `graphicx`, `multirow`, `needspace`, `placeins`, `microtype`, `url`, `xcolor`, and `hyperref` remain TeX-environment dependencies.

No PDF was rebuilt or visually inspected in this task. The existing PDF must not be represented as matching the corrected reference source until the full compile sequence and visual check are complete.
