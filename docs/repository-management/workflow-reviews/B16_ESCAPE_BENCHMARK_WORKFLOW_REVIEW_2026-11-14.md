# GitHub Actions workflow review — B.16 escape and vector benchmark batch (2026-11-14)

## Scope

Reviewed five complete workflow YAML definitions. This was a static review of triggers, checkout identity, permissions, numerical settings, assertions, output destinations and archival behavior. No workflow or calculation was executed or changed.

## Individual outcomes

| Workflow | Outcome | Findings |
|---|---|---|
| `b16-emission-radius-escape.yml` | REVIEWED_WITH_NOTES | Runs a 10 MeV source-radius/escape-probability audit after shell and opacity-matrix tests. It uses a 40×100×16×32 grid, checks production-output isolation and commits a JSON result. The workflow itself does not assert a profile SHA; confirm the script/output records the exact input profile fingerprint. |
| `b16-escape-phase-space.yml` | REVIEWED_WITH_NOTES | High-order 10 MeV phase-space decomposition (200 radial, 640 opacity, 200 energy, 32 angular and 64 path orders). It validates luminosity/escape closure, direction normalization, regional/joint-bin normalization and reconstruction of one-dimensional marginals. The checks are unusually thorough; nevertheless this is a B.16 vector benchmark diagnostic, not an axial-current exclusion. |
| `b16-flavour-fixed-vs-redshift.yml` | REVIEWED_WITH_NOTES | Compares flavor-resolved fixed-ω and path-redshift conventions at 10 MeV, with tests and production-output isolation. It commits the result. Keep the energy convention, flavor definition and profile provenance explicit in the JSON; no profile SHA assertion is visible in the workflow. |
| `b16-global-fig7-vertex-preserving.yml` | REVIEWED_WITH_NOTES | Recomputes the 10 MeV B.16 Fig. 7 vector benchmark on the vertex-preserving profile, checks a pinned SHA-256 and protects production axial outputs. It commits a JSON result. It is a vector baseline/control and cannot be promoted to axial-current acceptance. |
| `b16-global-redshift-audit.yml` | REVIEWED_WITH_NOTES | Computes the global vector luminosity/redshift audit at 0.1, 1 and 10 MeV, with regression tests and production-output isolation. It commits the result. It does not explicitly pin a profile hash in the YAML, so compare the actual output fingerprint and energy convention before combining it with the vertex-preserving 10 MeV result. |

## Cross-cutting findings

1. B.16 workflows contain distinct evidence layers: source-radius weighting, directional escape, phase-space decomposition, flavor/energy convention, and global luminosity. Their outputs should not be merged into one undifferentiated “transport passed” status.
2. The phase-space workflow has strong internal normalization checks, including reconstruction of marginals from the joint radius-energy-direction table. These establish bookkeeping closure for the generated object, not agreement with the external Fig. 7 benchmark by themselves.
3. Profile fingerprints are explicit in the vertex-preserving global Fig. 7 workflow but not in the emission-radius, flavor-comparison and generic global-redshift YAML. The corresponding scripts may still record hashes; inspect outputs before declaring provenance complete.
4. All five workflows use `contents: write` to commit JSON outputs. Reassess least-privilege needs if archival is moved to artifacts.
5. The vector-current baseline remains a prerequisite for axial-current work. No workflow in this batch authorizes updating axial curves.

## Disposition

All five entries were marked `REVIEWED_WITH_NOTES`. No scientific source, calculation, numerical output, trigger, runner permission or workflow was changed.
