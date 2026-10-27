# Major Point 2 — effective-theory parameter range response status

**Date:** 2026-10-27  
**Purpose:** Internal status and evidence record for the ordered reply to Major Point 2, “Motivating the range of effective theory parameters.” This file is not part of the formal letter.

## Meeting sources reviewed before drafting

The draft was prepared only after reading the four original meeting transcripts from 2026-10-23 (01–04) and \`会议观点总结_2026-10-23.md\`, then comparing them with the current response draft, Diff v2.4, and the v5.6 execution-state snapshot.

Relevant meeting decisions:

- Explain that the displayed \(m_{A'}\) and \(g_X\) ranges are a chosen plotting window, not a universal physical boundary.
- Give the physical motivation in one place: the lower-mass region is relevant to low-energy/astrophysical constraints (including white-dwarf bounds and the \((g-2)_\mu\) discussion), while the higher-mass region reaches the terrestrial collider coverage considered in the paper.
- State that the scan could be extended lower or higher; the selected window is for the scope and coverage of this analysis, not because all outside points are forbidden.
- Distinguish theoretical perturbativity from experimental exclusions, and do not claim a single constraint is strongest over the entire plane without a point-by-point comparison.
- Keep Route B: retain the axial-vector phenomenology, narrow the claims, and do not add particles.

## Current response draft

The response letter now states:

\[
10^{-3}\,\mathrm{GeV}\leq m_{A'}\leq10^2\,\mathrm{GeV},\qquad
10^{-6}\leq g_X\leq10^{-1}.
\]

It includes a compact table defining the plotting window and derived UV quantities, and explains that:

- \(v_s=m_{A'}/(2g_X)\) is derived at each scan point;
- \(\lambda_S=m_s^2/(2v_s^2)=2g_X^2m_s^2/m_{A'}^2\) in the stated negligible-mixing benchmark;
- \(\lambda_S\leq4\pi\) gives \(m_s\leq\sqrt{8\pi}\,v_s\) under the current manuscript normalization;
- for the illustrative \(m_s\geq10\,\mathrm{GeV}\) benchmark, \(v_s\geq10/\sqrt{8\pi}\,\mathrm{GeV}\simeq1.995\,\mathrm{GeV}\), equivalently \(m_{A'}\gtrsim(3.99\,\mathrm{GeV})g_X\);
- this is a benchmark-dependent theoretical consistency condition, not an experimental exclusion line or a universal exclusion of all UV realizations.

The reply also clarifies that the \(g_X\) plotting range lies below the usual perturbativity criterion \(g_X\lesssim\sqrt{4\pi}\), so the scalar self-coupling condition—not the gauge-coupling criterion—is the relevant point-dependent theoretical check for the selected scalar benchmark.

## Response–Diff cross-check

- **Diff 5:** the unified parameter table records the scan window, derived \(v_s\), scalar benchmark, and \(\lambda_S\) relation. A rationale paragraph now links the displayed window to the low-energy/astrophysical/precision constraints and terrestrial collider coverage, while explicitly denying that it is a universal physical boundary.
- **Diff 6:** the Fig. 2 caption distinguishes the axis window from global physical boundaries and labels the dashed \(v_s=2\,\mathrm{GeV}\) line as a rounded reference for the selected \(m_s=10\,\mathrm{GeV}\), \(\lambda_S^{\max}=4\pi\) benchmark—not an experimental exclusion or a Yukawa nonperturbativity limit.
- **Diff 12:** the Major Point 2 row now explicitly requires the response, parameter table, and Fig. 2 discussion to distinguish plotting range, theoretical consistency, applied experimental exclusions, and unassessed regions.

## Workflow status

| Workstream | Status | Meaning |
|---|---|---|
| Response-letter text draft for Major Point 2 | **Draft complete** | The placeholder in this response section has been replaced with the motivated plotting window, parameter table, and perturbativity relation. |
| Meeting-decision review | **Complete** | All four transcripts and the meeting summary were read before drafting. |
| Response–Diff consistency review | **Complete at claim/scope level** | The response and Diff 5/6/12 now use the same distinction between plotting window, theory condition, and experimental classification. |
| Manuscript application | **Pending** | The actual manuscript TeX/BibTeX source is not in the repository; no claim is made that the main paper has been edited or compiled. |
| Full UV feasibility and Fig. 2 robustness | **Pending** | T-13/T-14 and relevant scalar, VLL, kinetic-mixing, and constraint checks remain open. |
| Formal acceptance of the full response letter | **Pending** | Other referee points, global consistency, final source compilation, and final review remain outstanding. |

## Evidence limits and open work

1. The plotting window itself is not a complete allowed-region classification. Do not label points outside the axes as excluded or all points inside them as viable.
2. The theoretical \(m_s\) condition depends on the selected scalar benchmark. A point failing the \(m_s\geq10\,\mathrm{GeV}\) benchmark condition is not automatically excluded for every other scalar mass or UV parameter choice.
3. The statement about white-dwarf/astrophysical and \((g-2)_\mu\) constraints motivates the low-mass display range; it does not claim either constraint is globally strongest across the full plane. The exact source assumptions and the applicability of each plotted contour still need to be checked in the final constraint audit.
4. The final UV interpretation requires a consistent same-point check of portal assumptions, finite VLL effects, kinetic mixing, EFT truncation, and the relevant experimental constraints. Diff 5/6 are proposed manuscript edits, not proof that those checks have been completed.
5. Once the manuscript source is obtained, apply the corresponding Diff, verify the actual Fig. 2 axes and dashed-line convention, reconcile bibliography keys, compile, and then update the response and task ledger from the resulting evidence.

**Status summary:** Major Point 2 has a response draft and a claim-level Diff cross-check. Manuscript application, full UV feasibility classification, and formal acceptance remain pending.
