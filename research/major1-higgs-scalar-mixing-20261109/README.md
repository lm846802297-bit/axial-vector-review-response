# Higgs--radial-scalar mixing and complex-pole calculation

**Scope:** independent theoretical workstream for the Higgs--radial-scalar two-point function in the original one-VEV \(S+\mathrm{VLL}\) model.  
**Baseline:** merged PR #49 and the archived calculations listed below.  
**Status:** one-loop VLL matching and selected self-energy subsets exist; complete same-order UV--EFT matching, physical complex poles/residues, and a gauge-consistent near-degenerate observable remain open.

## 1. Independence and scope lock

This PR studies only Higgs--radial-scalar mixing and the associated physical scalar poles and observables. It is independent of the Belle II collider-reinterpretation workstream and does not import or require Belle II widths, efficiencies, Crystal-Ball response functions, or collider-recast outputs.

The model is the original single-VEV construction:
\[
S=\frac{v_s+s+i a_s}{\sqrt2},\qquad
H^0=\frac{v_h+h}{\sqrt2},\qquad
m_{A'}=2g_Xv_s,\qquad
m_s^2=2\lambda_Sv_s^2.
\]
The VLL sector contains the original \(\mu,\tau\) vector-like leptons. No additional scalar VEV, RH-neutrino completion, or new field content is introduced.

The conditional portal reference boundary is
\[
\lambda_{HS}^{\mathrm{EFT}}(M_E)=0,\qquad
\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E},
\]
with
\[
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}\sum_{\ell=\mu,\tau}|y_\ell|^2|\lambda_\ell|^2.
\]
This is a chosen matching benchmark, not a symmetry prediction and not a boundary condition fixed by the original paper. The physical answer must keep the renormalized portal input explicit or show its dependence.

The PR does not modify the manuscript or formal referee response. Axial-vector supernova/stellar-cooling transport remains in its separate research PR.

## 2. Reference benchmarks

The two reference points retained from the Plan-C-lite calculation are:

| Input | Benchmark A | Benchmark B |
|---|---:|---:|
| \(M_E\) | 20 TeV | 20 TeV |
| \(v_s\) | 70.886458 GeV | 315 GeV |
| \(m_{A'}\) | 10 GeV | 63 GeV |
| \(g_X\) | 0.0705353 | 0.1000 |
| \(\theta_{\mu R}\) | \(5.283\times10^{-4}\) | \(5.283\times10^{-4}\) |
| \(\theta_{\tau R}\) | \(8.884\times10^{-3}\) | \(8.884\times10^{-3}\) |
| \(m_s^{\max}\), \(\lambda_S\leq4\pi\) | 355.4 GeV | 1579.2 GeV |

The scalar-quartic ceiling follows from
\[
\lambda_S=\frac{m_s^2}{2v_s^2}\leq4\pi
\quad\Longrightarrow\quad
m_s\leq\sqrt{8\pi}\,v_s.
\]
This is a theoretical perturbativity criterion, not an experimental exclusion. The earlier \(m_s\in[10,150]\) GeV scan is a local diagnostic and must not be represented as coverage of the full perturbative interval.

## 3. Research questions

1. Close the UV--EFT matching at one explicitly stated perturbative order, including the complete soft contribution and counterterm set at that order.
2. Establish the full diagram and counterterm census, including the gauge, Goldstone, ghost, tadpole, VEV, and field-renormalization terms required by the chosen gauge and scheme.
3. Compute the full momentum-dependent \(2\times2\) inverse propagator, not only the off-diagonal fermion-loop entry.
4. Verify matching-scale and gauge-parameter cancellation in physical pole and observable quantities to the claimed order.
5. Solve for complex pole positions and residues, with continuous pole tracking through the near-degenerate region.
6. Construct the coherent two-pole production/decay line shape and the appropriate Higgs signal-strength or direct-search observables when the poles overlap.
7. Scan the declared perturbative scalar-mass domain for Benchmarks A and B, resolving thresholds and the Higgs-pole neighbourhood.

## 4. Existing work to reuse

- **Merged PR #49:** conditional portal matching, exact charged-lepton/VLL mass-eigenstate one-loop self-energy, finite hard momentum subtraction, selected EFT soft terms, CP-even radial-scalar bubble subset, first-pass complex-pole diagnostics, and local Higgs-pole scans.
- **Exact mass-eigenstate calculation:** the archived 2026-10-27 record under the repository's referee-response research directory, together with its Python implementation and validation output.
- **Plan-C-lite matching and pole diagnostics:** the archived 2026-10-27 Plan-C-lite matching and complex-pole report.
- **P2-lite scalar-loop subset:** the archived 2026-11-05 CP-even radial-scalar bubble report.

These records are subcalculations, not a complete physical pole prediction. The CP-even bubble subset is not a gauge-complete two-loop correction; the bubble-plus-contact EFT soft contribution is not the complete same-order soft/counterterm set; and an eigenvector-composition diagnostic is not a physical mixing angle, pole residue, signal strength, or exclusion.

## 5. Execution order

### Stage A — freeze conventions and audit

1. Freeze the renormalization scheme, matching scale, gauge fixing, tadpole/VEV prescription, field normalization, and perturbative counting.
2. Inventory every existing diagram, counterterm, analytic expression, numerical script, and validation record.
3. Establish a signed diagram census and identify duplicated or omitted contributions.
4. Freeze benchmark cards A/B and the portal-boundary dependence.

### Stage B — complete matching

1. Derive the full-theory amplitudes and EFT amplitudes at the same perturbative order.
2. Include all same-order hard and soft contributions, local operators, wave-function terms, and counterterms.
3. Verify the matching-scale dependence and reproduce the zero-momentum threshold independently.
4. Do not add a Goldstone-only or CP-even-only subset to the existing fermionic result and call the sum physical.

### Stage C — full propagator and poles

1. Construct the renormalized inverse propagator
   \[
   \Gamma_{\mathrm{inv}}(p^2)=
   \begin{pmatrix}
   p^2-m_h^2+\widehat\Pi_{hh}(p^2)&\widehat\Pi_{hs}(p^2)\\
   \widehat\Pi_{sh}(p^2)&p^2-m_s^2+\widehat\Pi_{ss}(p^2)
   \end{pmatrix},
   \]
   with the precise sign convention and counterterms fixed in the calculation record.
2. Include diagonal self-energies, absorptive parts, tadpole/VEV renormalization, and the field-renormalization prescription.
3. Solve \(\det\Gamma_{\mathrm{inv}}(s_i)=0\) for the complex poles and compute residues from the derivative of the full matrix.
4. Track the two poles continuously through the near-degenerate region; do not infer physical observables from eigenvector components alone.

### Stage D — observables and scan

1. Construct the coherent two-pole amplitude for the relevant production and decay channels.
2. Compare the full line shape with isolated-pole approximations away from degeneracy.
3. Use a single-pole \(\cos^2\theta\) rate rescaling only where its validity is demonstrated.
4. Scan the declared perturbative domain up to each benchmark's \(m_s^{\max}\), with a refined grid near \(m_s=m_h\).
5. Report portal-boundary dependence and numerical/theoretical uncertainties.

## 6. Acceptance criteria

A physical mixing result is accepted only when:
- the UV and EFT pieces are matched at the same stated order;
- the diagram and counterterm census is complete for the chosen gauge/scheme;
- matching-scale and gauge-parameter dependence cancel in the claimed physical quantities to the stated order;
- the full \(2\times2\) propagator includes both diagonal and off-diagonal entries;
- complex poles and residues are computed from that propagator;
- near-degenerate observables use the coherent two-pole line shape;
- all benchmark assumptions and unassessed regions are explicit.

No full scalar-mass allowed/excluded interval is claimed until the relevant theoretical and experimental observables are independently validated.