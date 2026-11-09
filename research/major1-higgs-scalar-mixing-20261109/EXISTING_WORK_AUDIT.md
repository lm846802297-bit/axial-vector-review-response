# Existing-work audit — Higgs--radial-scalar mixing

**Baseline:** main commit d3b234efbce270cd92b7ea55e31e02680114fc3a.  
**Purpose:** separate completed subcalculations from the missing ingredients needed for a physical, gauge-consistent pole and observable prediction.

## 1. Executive assessment

The merged PR #49 contains substantial one-loop and selected higher-order work. It does not yet close the complete same-order UV--EFT matching or produce a complete physical \(h\)-\(s\) pole/residue/lineshape prediction. The near-degenerate region therefore remains unclassified by the present calculation.

No new physical result is claimed by this audit.

## 2. Evidence ledger

| Existing record | Established result | Remaining limitation |
|---|---|---|
| Exact mass-eigenstate one-loop calculation | Full \(\mu,\tau,E_\mu,E_\tau\) fermion loop in the mass-eigenstate basis, including all four internal mass-state pairings and finite hard momentum subtraction | Complete same-order EFT soft/counterterm set and physical pole treatment |
| Plan-C-lite matching and complex-pole diagnostics | Conditional \(\overline{\mathrm{MS}}\) zero-momentum portal threshold, candidate derivative matching coefficient, first-pass complex-pole diagnostics and local Higgs-pole scan | Full-momentum hard analytic continuation in the pole solver, full diagonal self-energies, residues, tadpole/VEV completion, and complete observable |
| P2-lite scalar-loop calculation | CP-even radial-scalar bubble subset with analytic expressions and Simpson-integration cross-check | Gauge/Goldstone/ghost/tadpole completion, mixed VLL--scalar matching terms, and complete same-order EFT counterterms |

## 3. Quantitative results already recorded

The retained full-theory fermionic self-energies at \(p^2=m_h^2\) are
\[
\Pi_{hs}^{\mathrm{ret}}(m_h^2)=
\begin{cases}
-0.413277859-0.113173709\,i~\mathrm{GeV}^2,&\text{Benchmark A},\\
-0.093002551-0.025468201\,i~\mathrm{GeV}^2,&\text{Benchmark B}.
\end{cases}
\]

The exact hard momentum difference agrees with the leading derivative matching result at \(6.11\times10^{-4}\) relative. The zero-momentum hard comparator agrees with the leading portal-threshold estimate at \(1.79\times10^{-4}\) relative.

These are checks of the hard fermionic subcalculation. The retained combined \(\Pi_{hs}^{\mathrm{ret}}\) includes only the bubble-plus-contact EFT soft subset, not the complete same-order soft/counterterm set.

The CP-even radial-scalar bubble formulas agree with the recorded 8,000-interval Simpson integration at relative differences below \(10^{-14}\) for the listed test points. This verifies the selected integral formulas and their numerical implementation, not a gauge-complete physical two-loop correction.

## 4. Existing local pole diagnostic

The Plan-C-lite record includes a local scan around the Higgs pole, \(m_s\in[125.20,125.30]\) GeV with 0.1 MeV steps. The reported eigenvector-composition diagnostic reaches approximately \(9.15\times10^{-4}\) in Benchmark A and 0.20391 in Benchmark B. In Benchmark B, the sampled points with \(|s/h|\geq0.1\) occupy approximately 125.2467--125.2532 GeV.

These values are not physical mixing angles, pole residues, signal strengths, or experimental exclusions. The current pole solver uses approximate diagonal inverse kernels, fixed diagonal widths in the local scan, and a derivative hard-matching approximation. It does not yet solve the complete renormalized \(2\times2\) propagator with all diagonal and off-diagonal contributions.

## 5. Missing calculation ledger

| Missing ingredient | Why it matters | Acceptance evidence |
|---|---|---|
| Complete same-order EFT soft diagrams and counterterms | The current retained self-energy is a selected subset | Diagram-by-diagram UV/EFT matching ledger and independent checks |
| Full diagonal \(\Pi_{hh}\) and \(\Pi_{ss}\) | Diagonal terms move poles and affect residues and widths | Renormalized momentum-dependent diagonal kernels |
| Tadpole and VEV counterterms | Needed for a consistent expansion around the chosen vacuum | Explicit renormalization conditions and counterterm derivation |
| Gauge/Goldstone/ghost completion | A selected scalar subset is not a physical gauge-independent correction | Complete gauge-fixed diagram census and gauge-parameter checks |
| Full complex-momentum continuation | Real-axis derivative matching is not the complete complex-pole input | Analytic continuation and numerical stability checks |
| Pole residues and continuous pole tracking | Eigenvector composition alone is not an observable | Complex poles, residues, and stable tracking through degeneracy |
| Coherent two-pole line shape | A single-angle rescaling fails when poles overlap | Full production/decay amplitude and line-shape comparison |
| Portal-boundary dependence | The matching boundary is conditional, not symmetry-fixed | Scan or analytic dependence on the renormalized portal input |

## 6. Recommended next actions

1. Freeze scheme, gauge, tadpole/VEV, matching-scale, and field-normalization conventions.
2. Produce a complete diagram and counterterm census at one perturbative order.
3. Complete the UV--EFT matching, including the missing soft and counterterm terms.
4. Independently validate the full diagonal and off-diagonal self-energies.
5. Build the full \(2\times2\) renormalized inverse propagator.
6. Compute complex poles and residues, then construct the coherent two-pole observable near degeneracy.
7. Extend the scan over the declared perturbative \(m_s\) domain for Benchmarks A and B.

The Belle II collider reinterpretation is explicitly outside this workstream and is tracked independently in PR #68.