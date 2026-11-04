# Snapshot manifest — 2026-11-04

## Snapshot identity

- **Purpose:** immutable source backup of the referee-response letter and its bibliography inputs.
- **Source commit:** \`d9b262798f80c0f109f328b1b0019191e99d5437\`
- **Source commit URL:** https://github.com/lm846802297-bit/axial-vector-review-response/commit/d9b262798f80c0f109f328b1b0019191e99d5437
- **Snapshot date:** 2026-11-04
- **Authoritative working file:** repository-root \`Replies_to_Referee_3_referee_facing_2026-11-04.tex\`
- **Policy:** files ending in \`.snapshot\` are archival copies, not editable working sources.

## Files and Git blob IDs

| Original path at source commit | Snapshot path | Original Git blob SHA-1 |
|---|---|---|
| \`Replies_to_Referee_3_referee_facing_2026-11-04.tex\` | \`Replies_to_Referee_3_referee_facing_2026-11-04.tex.snapshot\` | \`a36cfa0069b578dc7796e580b54cb95a57730fef\` |
| \`Replies_to_Referee_3_neutrino_references.bib\` | \`Replies_to_Referee_3_neutrino_references.bib.snapshot\` | \`8d71083e53c4e04a850e67184d333b06cf4e4622\` |
| \`overleaf-source/axial-vector-model-building-v6/references.bib\` | \`axial-vector-model-building-v6-references.bib.snapshot\` | \`bb38a532a32b70b60d5709e30817cbb3d8f43d24\` |

Git blob IDs are content-addressed identifiers. Since each snapshot preserves the original file content exactly, the snapshot file's Git blob ID should equal the original blob ID even though its repository path differs.

## Dependency inventory

The response TeX references these two bibliography databases:

1. \`overleaf-source/axial-vector-model-building-v6/references.bib\`
2. \`Replies_to_Referee_3_neutrino_references.bib\`

The TeX preamble uses the following LaTeX packages:

- \`amsmath\`, \`amssymb\`, \`slashed\`
- \`graphicx\`, \`epsfig\`, \`epstopdf\`
- \`multirow\`, \`array\`, \`needspace\`, \`placeins\`
- \`microtype\`, \`url\`, \`xcolor\`, \`hyperref\`

The bibliography command uses \`\bibliographystyle{JHEP}\`. A repository-local \`JHEP.bst\` was not found in the checked source tree; it must be available in the TeX/BibTeX environment used for compilation.

Static source scan found no \`\\input{...}\`, \`\\include{...}\`, or \`\\includegraphics{...}\` file dependencies in the response TeX. No PDF is part of this source snapshot.

## Restore and verify

Restore the files to the original paths listed above, removing the \`.snapshot\` suffix. Then verify each restored file using the Git blob SHA-1 shown in the table. Do not replace the current root working source merely by copying an older snapshot; first compare the snapshot against the desired target version.

A full repository archive can be downloaded at the immutable source commit:

https://github.com/lm846802297-bit/axial-vector-review-response/archive/d9b262798f80c0f109f328b1b0019191e99d5437.zip

## Tagging

Recommended annotated tag after this PR is merged:

- Tag: \`reply-letter-2026-11-04\`
- Target commit: \`d9b262798f80c0f109f328b1b0019191e99d5437\`
- Message: \`Archive referee-response letter source and bibliography state as of 2026-11-04\`

The tag is not created by this PR because Git tags are repository refs rather than tracked files. Do not retarget or overwrite this tag once created.

After merge, create and push it from a local clone:

```bash
git tag -a reply-letter-2026-11-04 d9b262798f80c0f109f328b1b0019191e99d5437 -m "Archive referee-response letter source and bibliography state as of 2026-11-04"
git push origin reply-letter-2026-11-04
```
