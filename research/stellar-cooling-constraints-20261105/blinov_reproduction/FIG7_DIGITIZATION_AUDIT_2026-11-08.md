# Fig. 7 source-PDF digitization audit (2026-11-08)

**Status:** passed. The 10 MeV high-coupling tail is reproduced directly from the pinned vector path in the original arXiv source PDF. No change to the archived reference vertices is warranted.

## 1. Pinned source and coordinate frame

- Source archive: https://arxiv.org/src/2511.09619v2
- Archive member: \`luminosity_snapshot_t=1.pdf\`
- PDF SHA-256: \`4d7d1d10bfe2b52992af94df98749fa3adac887c009cbf98515fa12e6c48fdb5\`
- One PDF page, 56 vector drawing paths.
- The six luminosity curves are the six colored paths at drawing indices 39--44; the 10 MeV curve is drawing index 43.

The four plot-frame boundaries are read from the PDF's own vector axis paths:

\[
x_{\rm left}=54.82951355,\quad x_{\rm right}=397.99951172,
\]
\[
y_{\rm bottom}=195.54043579,\quad y_{\rm top}=20.90443420.
\]

The horizontal labels embedded in the PDF are
\[
10^{-22},10^{-20},\ldots,10^{-6},
\]
and the vertical labels are
\[
10^{52},10^{53},10^{54},10^{55}\ {\rm erg\,s^{-1}}.
\]

The extracted tick-label centers agree with the pinned log-coordinate transform to a maximum of 0.494 PDF points (the offset is the text glyph bounding-box center relative to the tick line). The horizontal tick centers agree to about 0.0021 points. The transform used in the existing digitization is therefore consistent with the labels actually embedded in the source PDF.

## 2. 10 MeV path geometry

The 10 MeV path has 27 line segments and 28 ordered vertices. The audit finds:

- strictly increasing PDF \(x\) coordinate along the path;
- zero duplicate-\(x\) segments;
- zero backwards-\(x\) segments;
- sorting by \(x\) preserves the original path order;
- no vertex is lost by the historical sort/unique operation;
- 25 vertices lie inside the displayed luminosity interval \(10^{52}\)--\(10^{55}\ {\rm erg\,s^{-1}}\);
- three vertices lie outside the displayed luminosity interval.

The archived 25 points reconstruct from the pinned PDF path with zero relative residual in both \(g\) and luminosity. Thus the current 25-point 10 MeV reference array is not affected by an accidental curve swap, path-order error, duplicate-\(x\) collapse, or coordinate-rounding mismatch.

## 3. Original high-coupling tail

The last visible source-PDF vertices are:

| \(g_{\mu\tau}\) | \(L_V\) [erg/s] |
|---:|---:|
| \(1.98189\times10^{-8}\) | \(9.49423\times10^{53}\) |
| \(2.38719\times10^{-8}\) | \(5.07668\times10^{53}\) |
| \(2.87538\times10^{-8}\) | \(2.08560\times10^{53}\) |
| \(3.46341\times10^{-8}\) | \(6.20256\times10^{52}\) |
| \(4.17169\times10^{-8}\) | \(1.26781\times10^{52}\) |

The final visible point is followed by one additional vector-path vertex:
\[
g_{\mu\tau}=5.00410\times10^{-8},\qquad
L_V=1.68951\times10^{51}\ {\rm erg\,s^{-1}}.
\]
This point is below the plotted lower luminosity boundary \(10^{52}\ {\rm erg\,s^{-1}}\), so its exclusion from the 25-point comparison is correct. It is not a missing visible point.

The last visible luminosity falls to 20.44% of the preceding visible point. The sharp drop is present in the original vector path itself, not introduced by digitization.

## 4. All six curves

All six pinned luminosity paths have monotonic coupling coordinates, no duplicate-\(x\) segments, and no backwards-\(x\) segments. Their archived visible vertices reconstruct from the source PDF to floating-point precision; the largest residual is \(1.64\times10^{-14}\) in luminosity for the \(10^{-6}\) MeV path.

This check validates the curve identification and coordinate extraction. It does not make the coarse vector plot equivalent to the authors' underlying numerical table; the plotted line width and PDF rounding remain the digitization uncertainty.

## 5. Decision

**Do not alter the 10 MeV Fig. 7 reference vertices or the high-coupling comparison grid.** The high-coupling residual in the literal reproduction is not explained by a curve-recognition or visible-tail digitization error.

The next investigation therefore remains on the calculation side: compare the radial source distribution, emission-radius-dependent escape probability, and the accumulated path opacity for particles produced at different radii. In particular, distinguish the fact that most particles are produced in the inner core from the fact that a large fraction of their optical depth accumulates in outer shells.

## Reproducibility

- Script: \`audit_fig7_digitization_geometry.py\`
- Tests: \`test_fig7_digitization_geometry.py\` (6 tests pass)
- Machine-readable result: \`../outputs/fig7_digitization_geometry_2026-11-08.json\`
- GitHub Actions: https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42447481306
