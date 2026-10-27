# Major Point 2 — effective-theory parameter range response status

**Date:** 2026-10-27  
**Purpose:** Internal status and evidence record for the ordered reply to Major Point 2, “Motivating the range of effective theory parameters.” This file is not part of the formal letter.

## Meeting sources reviewed before drafting

Before editing the response, the four original meeting transcripts (01–04) from 2026-10-23 and \`会议观点总结_2026-10-23.md\` were read. The directly relevant discussion is transcript 01 at 27:57–32:07 and the summary's “意见族 E：Figure 2 参数空间范围缺乏物理动机.” The current v5.6 execution manual and Diff v2.4 were also checked.

The meeting decision is to acknowledge that the plotted window could be extended in either direction, then explain the chosen scope:
- The upper end is motivated by the combination of perturbativity and the mass reach of terrestrial searches considered in the paper.
- The lower end is motivated by the low-energy precision/astrophysical context discussed in the paper; the meeting specifically mentioned the low-energy \((g-2)_\mu\) comparison and white-dwarf bounds.
- Do not claim that points outside the plotted window are forbidden, or that one constraint is strongest throughout the entire plane.
- Preserve Route B: retain the axial-vector phenomenology, narrow the claims, and add no particles.

**Important distinction added during the review:** the white-dwarf/stellar limits in Table II constrain the scalar coupling \(y_{s\mu\mu}\) under their source assumptions. They are not direct bounds on the \(A'\) effective-current coupling \(g_X\). The response therefore mentions them only as part of the broader model context and explicitly keeps scalar-sector constraints separate from the \(A'\) contours.

## Current response draft

The response letter states the plotting window
\[
10^{-3}\,\mathrm{GeV}\leq m_{A'}\leq10^2\,\mathrm{GeV},\qquad
10^{-6}\leq g_X\leq10^{-1}.
\]

It includes a compact table defining the plotting window and derived UV quantities:
- \(v_s=m_{A'}/(2g_X)\) is derived at each scan point.
- \(\lambda_S=m_s^2/(2v_s^2)=2g_X^2m_s^2/m_{A'}^2\) in the stated small-portal benchmark.
- \(\lambda_S\leq4\pi\) gives \(m_s\leq\sqrt{8\pi}\,v_s\) under the current manuscript normalization.
- For the illustrative \(m_s\geq10\,\mathrm{GeV}\) benchmark, \(v_s\geq10/\sqrt{8\pi}\,\mathrm{GeV}\simeq1.995\,\mathrm{GeV}\), equivalently \(m_{A'}\gtrsim(3.99\,\mathrm{GeV})g_X\).
- The \(g_X\) plotting range is well below \(g_X\lesssim\sqrt{4\pi}\), so gauge-coupling perturbativity is not the limiting condition within the displayed range. The scalar self-coupling condition remains a point-dependent check once \(m_s\) is specified.

These relations are conditional theoretical-consistency statements. They do not establish that every point inside the plotting window is viable, or that points outside it are excluded.

## Response–Diff cross-check

- **Diff 5:** retains the unified parameter table and now includes a range-motivation paragraph consistent with the response.
- **Diff 6:** already distinguishes the Fig. 2 axis window from physical boundaries and identifies the \(v_s=2\,\mathrm{GeV}\) line as a rounded reference for the \(m_s=10\,\mathrm{GeV}\), \(\lambda_S^{\max}=4\pi\) benchmark, not an experimental exclusion line.
- **Diff 12:** the Major Point 2 row now requires the response and manuscript to distinguish plotting range, theoretical consistency, applied experimental exclusions, and unassessed regions, while checking UV–EFT validity and the same-point model interpretation.
- The response's perturbativity relation and the Diff's corresponding benchmark relation use the same current manuscript normalization. The actual manuscript source is still needed to verify equation numbering and apply the edits.

## Workflow status

| Workstream | Status | Meaning |
|---|---|---|
| Response-letter text draft for Major Point 2 | **Complete as a draft** | The former parameter-range placeholder has been replaced with the plotting window, its motivation, a parameter table, and the conditional perturbativity relation. |
| Meeting-decision review | **Complete** | All four transcripts and the meeting summary were reviewed before drafting. |
| Response–Diff consistency review | **Complete at claim/scope level** | The response and Diff 5/6/12 distinguish the plotting window from physical boundaries and theoretical conditions. |
| Manuscript application | **Pending** | The actual manuscript TeX/BibTeX source is not in the repository; no claim is made that the main paper has been edited or compiled. |
| Full UV feasibility and Fig. 2 robustness | **Pending** | T-09/T-13/T-14 and relevant scalar, VLL, kinetic-mixing, EFT-truncation, and constraint checks remain open. |
| Formal acceptance of the full response letter | **Pending** | Other referee points, global consistency, final source compilation, and final review remain outstanding. |

## Evidence limits and open work

1. The plotting window is not a complete allowed-region classification. Do not label points outside the axes as excluded or all points inside them as viable.
2. The theoretical \(m_s\) condition depends on the selected scalar benchmark. A point failing the \(m_s\geq10\,\mathrm{GeV}\) benchmark condition is not automatically excluded for every other scalar mass or UV parameter choice.
3. The white-dwarf/stellar constraints in Table II act on the scalar coupling \(y_{s\mu\mu}\) under their stated assumptions; they are not directly interchangeable with the \(A'\) effective-current constraints on \(g_X\).
4. The response does not claim that \((g-2)_\mu\) is explained by the axial benchmark or that it is globally the strongest constraint. The exact source assumptions and the applicability of each plotted contour still require final constraint audit.
5. The final UV interpretation requires a consistent same-point check of portal assumptions, finite VLL effects, kinetic mixing, EFT truncation, and relevant experimental constraints. Diff 5/6 are proposed manuscript edits, not proof that these checks have been completed.
6. Once the manuscript source is available, apply the corresponding Diff, verify the actual Fig. 2 axes and dashed-line convention, reconcile bibliography keys, compile, and update the response and task ledger from the resulting evidence.

**Status summary:** Major Point 2 now has a response draft and a claim-level Diff cross-check. Manuscript application, full UV feasibility classification, and formal acceptance remain pending.
