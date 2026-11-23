# RC-001 upstream archive migration

**Status:** archive transfer and byte-integrity verification complete; PR #135 remains Draft pending reference/workflow review.  
**Source repository:** https://github.com/lm846802297-bit/high-energy-theory-research  
**Frozen source main:** `b2dd8f7e4427d0292bc299d273c780c05021fdab`  
**Target branch:** `migration/rc001-rehome-20261123`

## Canonical archive

The complete frozen source tree is mirrored under:

`research/rc001-vll-higgs-singlet-uv-eft/upstream/<original-source-path>`

This preserves the source-relative paths and original directory hierarchy. The target repository's existing Major 1 workstream is not overwritten. The source `research/README.md` remains within the mirrored `upstream/research/` directory.

## Archive-integrity acceptance

| Check | Result |
|---|---:|
| Source files in frozen inventory | 480 |
| Target mapped paths present | 480 |
| Git blob SHA matches | 480 |
| Byte sizes match | 480 |
| Missing paths | 0 |
| SHA/size mismatches | 0 |

The comparison was made against the remote source Git tree and the remote target branch tree. This establishes byte-for-byte archive identity at the Git blob level; it does not revalidate physical claims or recalculate any result.

## Workflow disposition

The three RC-001 workflow files are retained under the mirrored source snapshot at `upstream/.github/workflows/` as historical source artifacts. They are not active workflows in the target repository because GitHub Actions only discovers workflows in the repository-root `.github/workflows/` directory. The target project's existing tests and workflow policy remain authoritative. If any of these checks are still required operationally, they must be deliberately adapted into the target repository's active workflow layout and reviewed separately; do not simply copy the historical YAML to the root.

## Unmerged source work

Source PR #9 and PR #14 are not part of the frozen source `main` snapshot. Their proposed changes remain separate and must not be represented as merged research results.

## Remaining acceptance gates

1. Complete the target reference/link and script-dependency review.
2. Confirm the archived workflow disposition above and identify any genuinely reusable active checks.
3. Run the relevant target repository checks against the exact PR head.
4. Review and merge PR #135.
5. Only after merge and remote read-back verification, open a separate cleanup PR in the source infrastructure repository.

No physical calculation is rerun or modified by this archive migration. Software and archive checks are not physical validation.
