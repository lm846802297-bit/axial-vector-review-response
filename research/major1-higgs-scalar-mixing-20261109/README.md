# Higgs--radial-scalar mixing and complex-pole calculation

> **2026-11-14 spectral-area audit:** the archived two-pole diagnostic script integrates beyond its stated mass window when \(m_s=100\) or 150 GeV. The maximum ratio change from restricting the window is \(2.69\times10^{-8}\); historical output is preserved. See [audit and reproduction](SPECTRAL_WINDOW_AUDIT_2026-11-14.md). This does not validate a physical pole or exclusion.

**Scope:** independent theoretical workstream for the Higgs--radial-scalar two-point function in the original one-VEV \(S+\mathrm{VLL}\) model.  
**Baseline:** merged PR #49 and the archived calculations listed below.  
**Status:** the exact mass-eigenstate mu/tau+VLL fermion contribution to all three independent self-energy entries, its full-theory tadpole/potential counterterms, the leading dimension-five EFT bubble-plus-contact/dimension-eight UV structure, the Plan-C scale-running check, and the finite heavy-VLL scalar-potential matching through dimension eight are CI-validated. PR #69 adopts the signed dimension-five coefficient fixed by the UV mass-matrix Schur complement, \(C_{5,\ell}=-y_\ell\lambda_\ell/M_{E_\ell}\). The positive coefficient displayed in the archived v6 manuscript Eq. (5-d) is opposite for the printed UV Lagrangian and operator orientation; the algebraic result and gauge-field sign dictionary are recorded in [C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md](C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md). No manuscript edit is made in this PR. The leading-renormalizable light-field gauge-EOM currents for the QLD8 commutator representatives are now expanded upstream; fermion-EOM/Fierz reduction, complete mixed-background matching, the finite tadpole/VEV prescription, the full gauge-complete propagator, physical complex poles/residues, and near-degenerate observables remain open.

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
- **New 2026-11-09 fermion-sector matrix audit:** FERMION_SECTOR_MATRIX_AUDIT_2026-11-09.md, with its exact-basis script, independent validation, CI JSON output, and SHA-256 manifest.
- **New 2026-11-09 tadpole/potential/EFT UV audit:** TADPOLE_VEV_AND_EFT_DIM8_UV_AUDIT_2026-11-09.md, with full-theory gauge-invariant potential counterterms, field counterterms, the leading dimension-five EFT contact contribution, the dimension-eight operator counterterm, regression tests, CI JSON output, and hashes.
- **RC-001 cross-reconciliation:** Sec. 10 of `TADPOLE_VEV_AND_EFT_DIM8_UV_AUDIT_2026-11-09.md` records the prior RC-001 provenance of `O8`, adopts `C5_l = -y_l lambda_l/M_E` for the convention `L_EFT5 = -C5_l O5_l + h.c.`, and documents that the archived Plan-C soft function already includes the contact tadpole.
- **RC-001 derivative-operator interface:** [RC001_UPSTREAM_INTERFACE.md](RC001_UPSTREAM_INTERFACE.md) pins upstream PR #11 at `ba13cf736d0c1b1bbfef732acfb4f1785162ae88`, maps the UV fields and charges to the original axial model, and keeps QLD8 distinct from the scalar-potential `O8`. P1.5c merges the four cross-source sectors; P1.6a now evaluates both same-bilinear exchange UV poles and shows that their antisymmetric tensor integral is UV finite off shell. External-leg counterterms, gauge completion, EOM/IBP quotient, full QCD `Z` block and finite matching remain open. The upstream scripts and validation outputs remain in their source repository, and no QLD8 coefficient is imported into the `hh,hs,ss` scalar two-point calculation.
- **C5/gauge convention audit:** [C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md](C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md) derives the signed \(C_5\) coefficient from the Schur complement, identifies the opposite sign in the printed v6 Eq. (5-d), gives the explicit \(D_+=D_-\) field-redefinition map, and includes an exact-rational audit/test suite.
- **QLD8 total-current expansion:** the upstream [RC-001 current-expansion record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD-total-current-expansion.md) now writes the full leading-renormalizable (J_Y), (J_2^a), and (J_X) currents for the original one-VEV model. Fermion-EOM/Fierz reduction remains open.
- **QLD8 Higgs-source/EOM map:** the upstream [source and flavor-charge record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD-Higgs-source-EOM-model-map.md) distinguishes gauge-forbidden diagonal mu/tau Yukawas from gauge-allowed but model-set-to-zero mu-tau off-diagonal Yukawas, and records the leading fermion EOMs and source power counting. Fierz reduction remains open.
- **QLD8 source-square channel census:** the upstream [Fierz-channel record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD-source-square-Fierz-channel-census.md) enumerates the three diagonal and three cross source pairs, their chirality classes, weak/color contractions, and derivative placements. Explicit d-dimensional Fierz reduction remains open.
- **Four-dimensional chiral Fierz algebra:** the upstream [exact Fierz record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD-chiral-Fierz-identities.md) verifies the RR/LL scalar-tensor and RL/LR vector identities in 1024 exact matrix components. A working NDR/anticommuting-γ5 and minimal Fierz-evanescent convention is now fixed for the QLD8 open-line sector; the complete d-dimensional counterterm basis remains open.

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

## 7. New progress: complete fermion-sector matrix subcalculation (2026-11-09)

The exact mass-eigenstate fermion formula has been extended from the off-diagonal \(hs\) entry to all three independent entries \(hh,hs,ss\), including heavy-heavy, heavy-light, light-heavy, and light-light internal states for both \(\mu\) and \(\tau\).

The finite hard momentum differences in the Plan-B convention are:

| Entry | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\Delta\Pi_{hh,\mathrm{hard}}^B\) | \(-131.023925\) | \(-131.023925\) |
| \(\Delta\Pi_{hs,\mathrm{hard}}^B\) | \(+0.024030444\) | \(+0.005407724\) |
| \(\Delta\Pi_{ss,\mathrm{hard}}^B\) | \(-626.010390\) | \(-31.702024\) |

The off-diagonal entry reproduces the archived exact-basis calculation. The diagonal derivative UV coefficients are nonzero, while the off-diagonal coefficient cancels. The light \(\mu,\tau\) absorptive matrix is positive semidefinite and rank one to numerical precision, providing an optical-theorem cross-check.

The calculation is archived in fermion_sector_matrix_audit.py, test_fermion_sector_matrix_audit.py, fermion_sector_matrix_audit.json, and fermion_sector_matrix_tests.txt. GitHub Actions run 42564492356 passed all five tests and archived the numerical output.

This remains a fermion-sector subcalculation. The diagonal counterterms, remaining SM/gauge/scalar sectors, complete EFT soft matching, tadpole/VEV prescription, and physical complex poles are not yet complete. The explicit \(\mu,\tau\) absorptive contributions must not be double-counted through externally inserted fixed widths.


## 8. EFT light-loop UV subtraction and matching counterterms

The matrix audit now also computes the UV coefficients of the exact light-light bubble that is subtracted in the EFT comparison. This distinction matters: the full-theory off-diagonal \(p^2\) pole cancels, but the light EFT bubble has a nonzero off-diagonal \(p^2\) pole.

Define \(C_{ab}^{\rm full}=\sum_{ij}C_{ab}^{ij}\) and \(C_{ab}^{\rm light}\) from the light-light state only. In the adopted inverse-propagator convention, the counterterm coefficient for the full-minus-light bubble difference is
\[
\delta Z_{ab}^{\rm match}
=-\frac{C_{ab}^{\rm full}-C_{ab}^{\rm light}}{16\pi^2}\,\Delta_{\rm UV},
\qquad
\Delta_{\rm UV}=\frac1\epsilon-\gamma_E+\ln4\pi.
\]

The coefficients multiplying \(\Delta_{\rm UV}\) are:

| Entry | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\delta Z_{hh}^{\rm match}/\Delta_{\rm UV}\) | \(-0.0167123071\) | \(-0.0167123071\) |
| \(\delta Z_{hs}^{\rm match}/\Delta_{\rm UV}\) | \(+2.2983060\times10^{-6}\) | \(+5.1720246\times10^{-7}\) |
| \(\delta Z_{ss}^{\rm match}/\Delta_{\rm UV}\) | \(-0.0798508674\) | \(-0.00404375731\) |

Thus the EFT derivative operator requires a nonzero \(hs\) counterterm even though the full-theory \(hs\) derivative pole cancels. This is a matching statement, not a physical mixing angle.

The code also records the full-minus-light local mass-pole coefficients. They are not interpreted as physical mass shifts: they must be mapped onto the renormalized scalar-potential parameters together with the VEV/tadpole prescription. The bubble subtraction alone is not the complete EFT counterterm ledger.

The new fifth test checks these matching field-counterterm coefficients against the two benchmark values. GitHub Actions run 42564492356 passes all five tests.


## 9. Tadpole, potential, and EFT dimension-eight UV audit (2026-11-09)

The VLL determinant has now been expanded directly in gauge-invariant scalar backgrounds. Its full-theory pole maps onto \(\delta\mu_H^2,\delta\mu_S^2,\delta\lambda_H,\delta\lambda_S\), with \(\delta\lambda_{HS}=0\) at this one-loop fermion-determinant order. The potential counterterm derivatives reproduce the VLL-sector tadpole and local \(hh,hs,ss\) poles, while separate diagonal field counterterms cancel the \(p^2\) poles.

The leading dimension-five EFT mass operator,
\[
m_\ell(h,s)=\frac{C_{5,\ell}}{2}(v_h+h)(v_s+s),
\qquad C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_E}.
\]
generates the dimension-eight scalar operator
\[
O_8=(H^\dagger H)^2(S^\dagger S)^2
\]
in the one-loop light-fermion determinant. Its second derivative contains an \(hs\) contact contribution in addition to the light-light bubble. The earlier bubble-only local subtraction is therefore an intermediate result, not the complete EFT local UV structure. This refers to the archived exact-SVD light-bubble subtraction; the separate Plan-C-lite finite soft function already includes its contact tadpole, which must not be added again. The signed mass parameter follows the RC-001 Schur-complement convention; the positive mass used in the determinant is \(|m_\ell|\).

The full numerical coefficients, signs, benchmark tables, perturbative-control flag, and scope limits are in TADPOLE_VEV_AND_EFT_DIM8_UV_AUDIT_2026-11-09.md. The scalar-potential counterterm map is generated by scalar_potential_counterterm_map.py and checked by test_scalar_potential_counterterm_map.py. The current GitHub Actions validation includes 18 independent algebra, mass-matrix, tadpole, EFT-contact, exact heavy-CW matching, local-curvature, Plan-C scale-running, and potential-counterterm tests.

The finite heavy-VLL Coleman–Weinberg potential has additionally been matched through dimension eight at \(\mu=M_E\), and the Plan-C scale derivative has been checked against the leading \(O_8\) running; the retained-sector scale residual cancels to approximately \(10^{-13}\) relative precision. The complete finite EFT boundary condition, including all other hard/soft sectors and operator mixing, remains open.

This closes the VLL-sector UV-pole bookkeeping for the full-theory potential and the leading EFT5 light determinant. It does not choose the finite tadpole/VEV prescription or complete the gauge/Goldstone/ghost/scalar contributions and finite hard-plus-soft matching. In particular, Benchmark A has \(|\lambda_\tau|^2/(4\pi)\simeq1\), so its one-loop \(\lambda_S\) pole coefficient is order one and deserves extra perturbative caution.


### Plan-C scale-running check (2026-11-09)

The dimension-eight pole also fixes the leading loop-induced running
\[
\beta_{c_8}^{\rm loop}=-\frac{2}{16\pi^2}\sum_{\ell=\mu,\tau}|C_{5,\ell}|^4.
\]
At \(s=m_h^2\), the Plan-C soft-plus-hard scale derivative equals twice the leading-EFT5 mixed UV coefficient. Running \(c_8\) from \(M_E=20\) TeV to \(125.25\) GeV cancels the residual change in the Plan-C \(hs\) two-point function at both benchmarks. The relative cancellation residuals are \(1.73\times10^{-13}\) (A) and \(1.50\times10^{-13}\) (B); symmetric finite-difference checks agree with the analytic scale derivative to better than \(5.4\times10^{-8}\).

This establishes the leading-EFT5 scale-consistency check, not the complete finite matching: the finite boundary value \(c_8(M_E)\) remains undetermined. The exact numerical decomposition is recorded in scalar_potential_counterterm_map.json and summarized in TADPOLE_VEV_AND_EFT_DIM8_UV_AUDIT_2026-11-09.md.


### Finite heavy-VLL scalar-potential matching through dimension eight

The finite hard matching has now been extracted from the exact heavy singular value of the original \(\mu,\tau+\mathrm{VLL}\) mass matrix. With \(X_\ell=|y_\ell|^2H^\dagger H\) and \(Y_\ell=|\lambda_\ell|^2S^\dagger S\), the heavy eigenstate Coleman--Weinberg determinant is expanded through dimension eight. This determines the VLL-sector finite Wilson coefficients for the portal, the two mixed dimension-six operators, and all pure/mixed scalar-potential operators through dimension eight.

In particular,
\[
c_8(M_E)=-\frac{7}{2(16\pi^2)}\sum_\ell|C_{5,\ell}|^4,
\]
so the finite \(O_8=(H^\dagger H)^2(S^\dagger S)^2\) matching boundary is no longer left undetermined within this restricted VLL scalar-potential basis:
- Benchmark A: \(-3.80925598\times10^{-17}\,\mathrm{GeV}^{-4}\);
- Benchmark B: \(-9.76902113\times10^{-20}\,\mathrm{GeV}^{-4}\).

A high-precision test compares the exact heavy eigenvalue Coleman--Weinberg expression with the dimension-eight background expansion and verifies the expected fifth-order remainder. The latest test suite now contains 18 tests: 9 independent matrix/tadpole tests and 9 scalar-potential/EFT5/finite-matching/scale-running tests.

The derivative-operator basis, finite tadpole/VEV prescription, and gauge/Goldstone/ghost/scalar contributions remain outside this finite-potential matching result.


### Finite heavy-potential contribution to local \(h\)-\(s\) curvature

The finite dimension-four, dimension-six, and dimension-eight potential coefficients have been differentiated at each benchmark vacuum. After the dimension-four portal threshold is canceled, the remaining dimension-six plus dimension-eight local curvature is \(+0.656934\ \mathrm{GeV}^2\) (A) and \(+0.147834\ \mathrm{GeV}^2\) (B). The dimension-six terms dominate; the dimension-eight terms are smaller by roughly three orders of magnitude.

The additional finite portal shifts that would cancel this residual at the selected vacuum are \(-3.76387\times10^{-5}\) (A) and \(-1.90608\times10^{-6}\) (B). These are explicitly condition-dependent local-curvature diagnostics, not physical mixing angles or universal Wilson coefficients. The exact heavy-CW mixed derivative agrees with the dimension-eight-truncated expansion to relative \(2.96\times10^{-11}\) in both benchmarks.


- **QLD8 derivative-aware Fierz/IBP ledger:** the pinned upstream [ledger](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-derivative-Fierz-IBP-ledger.md) establishes the exact complete-sum relation \((D_\mu J_A^\dagger)(D^\mu J_B)\doteq-J_A^\dagger D^2J_B\), records all 36 ordered derivative placements, and tracks the derivative on each original fermion through Fierz rearrangement. This is an operator identity, not a final nonredundant basis.
- **QLD8 second-order fermion EOM:** the pinned upstream [map](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-second-order-fermion-EOM-map.md) checks the Dirac-square curvature sign and maps the endpoint Laplacians into Higgs-derivative and field-strength four-fermion structures. The scalar-pair evanescents are not closed after this EOM substitution; an enlarged basis is still required.
- **CI status:** upstream PR runs 42733380866 (Fierz) and 42733381140 (schema validation) both failed with empty job-step lists; log retrieval returned 404. The cause is unknown. Local exact algebra/bookkeeping checks passed; no CI pass is claimed.


- **EOM-generated chiral Fierz identities:** the upstream [Fierz record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md) now includes the scalar-vector and scalar-tensor projections generated by the second-order fermion EOM. Exact SymPy checks pass for 34 identities (8704/8704 components) and six chiral tensor self-duality relations.
- **Remaining scheme gate:** the four-dimensional projections are established, but the d-dimensional evanescent differences and their one-loop mixing/counterterm matrix are not yet complete. The existing scalar-pair evanescents alone are insufficient after the second-order EOM substitution.
- **CI:** latest upstream runs 42734711989 and 42734712057 failed with empty job-step lists; log retrieval returned 404. The cause is unknown. Local exact algebra passed; no CI pass is claimed.


- **Explicit EOM-generated evanescent differences:** the upstream [Fierz note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md) now writes the \(E_{XY;V}^{\mu,rs}\) scalar-vector and \(E_{XY;T}^{\mu\nu,rs}\) scalar-tensor Fierz differences explicitly, including the Grassmann sign, Levi-Civita terms, and three-component chiral tensor basis. They have no \(O(\epsilon)\) physical admixture at definition stage.
- **Remaining calculation:** the one-loop mixing of these evanescents, UV-generated higher gamma strings, same-order EFT soft insertions, and finite Wilson coefficients remain open. No PR #69 scalar two-point coefficient is changed.
- **CI:** latest upstream runs 42735130364 and 42735130363 failed with empty job-step lists; logs were unavailable. No CI pass is claimed.


## 2026-11-10 update: QLD8 P1.0 counterterm-basis seed map

The upstream PR #11 is now pinned at [`f417c7360bcc162b4da7ecb4b99bd874525234fa`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/f417c7360bcc162b4da7ecb4b99bd874525234fa). The new [QLD8 one-loop Green-basis note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-one-loop-counterterm-basis.md) separates the off-shell four-fermion/two-derivative Green basis from the later EOM-reduced physical quotient. It freezes the six independent source-pair sectors, color singlet/octet structures, weak and flavor labels, all 36 derivative placements, and the direct-pairing rank-3/rank-4 evanescent seeds.

The accompanying [exact audit](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/calculations/RC-001-QLD8-counterterm-basis-audit.py) checks 64/64 rank-3 and 256/256 rank-4 duality assignments, all four chiral projections, 81/81 SU(3) color-index assignments, the SU(2) epsilon invariant, source representations, and derivative counting. The local exact checks pass.

**Boundary:** this is a P1.0 basis/Dirac-seed audit, not a one-loop calculation. No UV pole, (Z) matrix, anomalous dimension, or finite dimension-eight Wilson coefficient has been computed. It remains a four-fermion/current-sector calculation and does not add a contribution to the PR #69 (hh,hs,ss) two-point functions.

The new [P1.0 CI workflow](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/.github/workflows/rc001-qld8-counterterm-basis-audit.yml) ran as [Run #42737785635](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42737785635) and reported failure, but GitHub returned an empty job-step list and the job-log endpoint returned 404. The cause is unknown; this is not evidence of a failed algebra assertion. No CI pass is claimed.


## 2026-11-10 update: QLD8 P1.1a QCD color block

The upstream PR #11 pin has advanced to [\`f417c7360bcc162b4da7ecb4b99bd874525234fa\`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/f417c7360bcc162b4da7ecb4b99bd874525234fa). The new [\(d^\dagger d\) QCD color-factor record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-QCD-color-factor-block.md) fixes the crossed source tensor \(C_X=C_1/3+2C_8\) and computes all six pairwise SU(3) generator matrices in the singlet/octet basis. Their sum satisfies the exact color-singlet identity \(\sum_{a<b}\mathbf T_a\cdot\mathbf T_b=-8/3\,\mathbf1\).

The [reproducible color audit](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/calculations/RC-001-QLD8-QCD-color-factor-audit.py) passes locally. These are color factors only; no QCD loop kernel or UV pole is yet computed. The four-fermion/current-sector calculation remains separate from the PR #69 scalar two-point functions.

The updated [QLD8 CI workflow](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/.github/workflows/rc001-qld8-counterterm-basis-audit.yml) includes both basis-seed and QCD color audits. Its run for the immediately preceding head failed with an empty job-step list and unavailable logs; the new run for the current head was queued at the time of this update. No CI pass is claimed.


## 2026-11-10 update: QLD8 P1.1b QCD insertion routing

The upstream [\(d^\dagger d\) QCD routing record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-QCD-one-loop-momentum-routing.md) fixes the all-incoming external-momentum convention and shows that the four product-rule derivative placements sum to the single tree insertion factor \(q_A^2\). It also fixes the loop-momentum shift for each of the six QCD exchange topologies: two within-current exchanges leave \(q_A\) unchanged, while four cross-current exchanges carry \((q_A\pm\ell)^2\).

The accompanying [exact symbolic audit](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/calculations/RC-001-QLD8-QCD-momentum-routing-audit.py) passes locally. This closes the insertion-momentum routing algebra only; no Dirac loop numerator, tensor integral, UV pole, or counterterm matrix is yet computed. The work remains a four-fermion/current-sector calculation and does not add a contribution to PR #69 \(hh,hs,ss\).

The latest upstream QLD8 workflow run on the pinned head, #42745464322, failed with an empty job-step list; log retrieval returned 404. The cause is unknown; no CI pass is claimed.


## 2026-11-10 update: QLD8 P1.1c direct \(RL\) tensor evanescent

The upstream [direct-pairing tensor note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-RL-tensor-evanescent-seed.md) identifies the candidate
\[
E_{T;RL}^{\rm dir}=(\bar Q\sigma^{\mu\nu}P_Rd)(\bar d\sigma_{\mu\nu}P_LQ),
\]
which vanishes in four dimensions because the two chiral tensor representations have opposite duality. The corresponding d-dimensional two-gamma chain contains \(D\,P_R\otimes P_L+E_{T;RL}^{\rm dir}\); its \(O(\epsilon)\) scalar coefficient must be retained in a UV-pole calculation.

The exact 4D matrix check has been added to the upstream basis audit. The direct tensor seed is not eliminated using the scalar–vector \(E_{RL;V}\) structure, which belongs to a different Lorentz sector. The direct-pairing rank-three seed and crossed rank-three channel are also distinct. No loop coefficient or UV pole is claimed. The latest upstream CI run #42745464322 failed with an empty job-step list and unavailable logs; the cause is unknown, and no CI pass is claimed.


## 2026-11-10 update: QLD8 P1.2 d-dimensional Fierz projection

The upstream [d-dimensional direct-tensor Fierz map](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-d-dimensional-RL-tensor-Fierz-map.md) derives the formal crossed odd-rank projection coefficients
\[
f_n(D)=
\frac{D(D-1)-4n(D-n)}
{2(-1)^{n(n-1)/2}D(D-1)\cdots(D-n+1)}.
\]
The first channels behave as
\[
f_1=-\frac34\epsilon+O(\epsilon^2),\qquad
f_3=-\frac5{24}\epsilon+O(\epsilon^2),
\]
while the rank-five projection has \(f_5=-1/(3\epsilon)+O(1)\). This is a Gram-projection singularity because the rank-five Gram norm vanishes at \(D=4\), not a loop UV pole. It shows that the direct tensor cannot be removed by a regular finite rank-one/rank-three-only basis change.

The scalar–vector \(E_{RL;V}^{\mu,rs}\) is a different Lorentz sector and is not the direct tensor's Fierz image. The direct-pairing \(E_{3;RL}^{\rm dir}\) is also distinct from crossed \(X_3^{RL}\). The full finite evanescent basis remains open until explicit one-loop numerators determine the gamma-rank closure.

The companion [symbolic audit](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/calculations/RC-001-QLD8-ddim-Fierz-projection-audit.py) passes locally. The latest upstream QLD8 workflow run [#42745464322](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42745464322) again failed with an empty job-step list and unavailable logs; the cause is unknown, and no CI pass is claimed.


## 2026-11-10 update: QLD8 P1.3 direct-pairing QCD basis and numerator skeleton

The upstream [direct-pairing color-basis note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-QCD-direct-pairing-color-basis.md) gives the direct singlet/octet basis
\[
C_{1,d}=\delta_{il}\delta_{kj},\qquad C_{8,d}=T^A_{il}T^A_{kj},
\]
with tree vector \((1,0)_d\). It is related to the crossed-current basis by \(B_d=B_xR\), with \(R=\begin{pmatrix}1/3&4/9\\2&-1/3\end{pmatrix}\). All six direct-basis color matrices pass exact SU(3) checks, satisfy \(M_d=R^{-1}M_xR\), and sum to \(-8/3\,\mathbf1\).

The upstream [six-topology open-line numerator note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-QCD-d-dagger-d-open-line-numerators.md) fixes the Feynman-gauge numerator skeletons in the original \((\bar Q,d)\otimes(\bar d,Q)\) spinor pairing. For each ordered pair \((a,b)\), the loop momentum \(\ell\) flows from \(b\) to \(a\), so \(r_a=p_a+\ell\), \(r_b=p_b-\ell\). The six source factors are \(q_A^2\) or \((q_A\pm\ell)^2\) as specified by the topology.

The exact 4D gamma audit passes 64/64 cross-chain Lorentz-index assignments and 16/16 same-bilinear contractions. In the direct pairing, the one-gluon Feynman-gauge chains generate gamma rank at most two on each bilinear. The direct tensor and mixed rank-two\(\otimes\)scalar structures must be retained. This is not a claim that the crossed odd-rank basis closes; the P1.2 Gram obstruction is avoided by keeping the UV calculation in the direct pairing.

The four external-leg self-energy/wavefunction contributions remain necessary. Overall graph signs, complete \(D\)-dimensional integrands, UV poles, and the \(Z\) matrix have not yet been calculated. The latest upstream QLD8 workflow run [#42745464322](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42745464322) reports failure with an empty job-step list and unavailable logs; the cause is unknown, and no CI pass is claimed.


## 2026-11-10 update: QLD8 P1.4a Yukawa-weighted source renormalization

The upstream [QCD source-renormalization check](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-QCD-Yukawa-source-renormalization-check.md) separates the Higgs-EOM source as \(J_d=Y_d^\dagger S_d\), \(S_d=\bar d_RQ_L\). In \(\overline{\rm MS}\), \(Z_{Y_d}=Z_m\) and \(Z_S=Z_m^{-1}\), so
\[
Z_{J_d}^{(s)}=Z_{Y_d}Z_S=1+O(g_s^4).
\]
Thus the two within-source scalar-current vertex corrections plus the four external-leg wavefunction terms are canceled by the \(Y_d^\dagger Y_d\) counterterm when the SM Yukawa is renormalized inside the source. This is a factorized-source identity, not the full four-fermion \(Z\) matrix.

The four cross-source exchanges remain as the non-factorizing QCD mixing problem. The latest upstream QLD8 workflow run [#42745464322](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42745464322) again has an empty job-step list and unavailable logs; its cause is unknown, and no CI pass is claimed.


## 2026-11-10 update: QLD8 P1.4b0 cross-source scalar UV projection

The upstream [cross-source scalar UV-pole note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-cross-source-scalar-UV-pole.md) now records the exact \(P_R\otimes P_L\) projection of the four cross-source QCD chains:
\[
\frac14\operatorname{Tr}_{16}[(P_R\otimes P_L)\mathcal N_{ab}]
=r_a\cdot r_b.
\]
This passed 12/12 exact gamma-matrix checks. A common auxiliary denominator mass was used to isolate the degree-two UV Taylor coefficient. After applying the direct-color weights \((-1,+1,+1,-1)\), the scalar-scalar kernel is
\[
K_{\rm cross}^{SS}(D)
=\frac{D^2+10D-8}{48}
(p_1-p_2)\cdot(p_3-p_4).
\]
At \(D=4\), this is the momentum polynomial of a direct-color-octet double-\(\overleftrightarrow D\) scalar structure, not the original \(q_A^2\) source-square polynomial.

This is only the scalar-scalar projection. The three tensor sectors, complete \(R^*\)/off-shell subtraction, common amplitude sign restoration, and full QCD counterterm matrix remain open. No finite Wilson coefficient is claimed.


## 2026-11-10 update: QLD8 P1.4b1 mixed tensor UV projections

The upstream source is pinned at [\`f417c7360bcc162b4da7ecb4b99bd874525234fa\`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/f417c7360bcc162b4da7ecb4b99bd874525234fa). The mixed rank-two\(\otimes\)scalar and scalar\(\otimes\)rank-two projections of the four cross-source QCD graphs have now been evaluated through the degree-two UV Taylor coefficient.

A topology-dependent left/right momentum ordering was clarified: the first two topologies use \((r_a,r_b)\), while the last two use \((r_b,r_a)\). With \(W(u,v)=\Gamma^{\mu\nu}u_\mu v_\nu\), the topology kernel is
\[
T_i(D)=\frac{D-4}{12}W(A_i,B_i)+\frac12W(q_A,A_i+B_i),
\]
for \((A_i,B_i)=(p_1,p_4),(p_1,p_3),(p_2,p_4),(p_2,p_3)\). The direct-color weighted sums are
\[
K_{T\otimes S}(D)=\frac{D+8}{12}W(q_A,p_4-p_3),\qquad
K_{S\otimes T}(D)=-\frac{D+8}{6}W(p_1,p_2).
\]
Both are nonzero at \(D=4\). The exact symbolic audit and six rational component checks pass.

Artifacts:
- [Mixed tensor UV derivation](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-cross-source-mixed-tensor-UV-poles.md)
- [Exact audit source](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/calculations/RC-001-QLD8-cross-source-mixed-tensor-UV-audit.py)
- [Validation output](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/validation/RC-001-QLD8-cross-source-mixed-tensor-UV-audit.txt)

The rank-two\(\otimes\)rank-two projection, complete graph phase, external-gluon completion, full QCD \(Z\) matrix, and EOM/IBP quotient remain open. The current-head candidate-schema run [#42755074288](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42755074288) and preceding-head QLD8 audit run [#42755057777](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42755057777) both report failure. Their job metadata exposes no step list or logs URL, so the cause is undiagnosed. The local symbolic mixed-tensor audit passed; no CI pass is claimed.


## 2026-11-10 update: QLD8 P1.4b2 full tensor UV kernel

The upstream source is pinned at [\`f417c7360bcc162b4da7ecb4b99bd874525234fa\`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/f417c7360bcc162b4da7ecb4b99bd874525234fa). The complete degree-two D-dimensional Lorentz tensor \(I_{\alpha\beta}(A,B;q_A)\) has been derived. Its formal D-dimensional trace reproduces the independent scalar-scalar kernel, and its antisymmetric projection reproduces the mixed rank-two/scalar kernels.

The raw rank-two\(\otimes\)rank-two contractions for all four cross-source topologies are now explicit. The radial factors retain their \(O(\epsilon)\) terms:
\[
D/4=1-\epsilon/2,\quad D(D+2)/24=1-5\epsilon/6,\quad
D(D+2)(D+4)/192=1-13\epsilon/12.
\]
Exact symbolic checks pass.

Artifacts:
- [Full tensor UV kernel](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/research/RC-001-QLD8-cross-source-rank2xrank2-UV-kernel.md)
- [Tensor integral audit source](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/calculations/RC-001-QLD8-cross-source-tensor-integral-audit.py)
- [Validation output](https://github.com/lm846802297-bit/high-energy-theory-research/blob/f417c7360bcc162b4da7ecb4b99bd874525234fa/validation/RC-001-QLD8-cross-source-tensor-integral-audit.txt)

The tensor is not yet reduced into the D-dimensional physical/evanescent operator basis. The complete graph phase, external-gluon gauge completion, EOM/IBP quotient, and full QCD \(Z\) matrix remain open.


### Latest CI metadata

On upstream head \`f417c7360bcc162b4da7ecb4b99bd874525234fa\`, the QLD8 audit [#42755580467](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42755580467), chiral-Fierz audit [#42755580434](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42755580434), and candidate-schema validation [#42755580456](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42755580456) report failure. Each job response exposes \`steps=null\` and \`logs_url=null\); the cause is unknown. Local symbolic checks passed, but CI is not reported as passing.


## 2026-11-10 upstream QLD8 interface refresh

Upstream PR #11 is now pinned at [\`f417c7360bcc162b4da7ecb4b99bd874525234fa\`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/f417c7360bcc162b4da7ecb4b99bd874525234fa). Its P1.5a–P1.5b update fixes the common cross-source graph phase and relative signs, gives the exact D-dimensional TT tensor sum, and independently checks the transverse-metric coefficient for symbolic D. This is a provenance/interface update only: it does not change the PR #69 scalar two-point diagrams or coefficients. The full direct-pairing cross-source counterterm, physical/evanescent \(Z\) block, external-gluon completion, and EOM/IBP reduction remain open upstream.


- **QLD8 P1.6a:** upstream PR #11 is pinned at `ba13cf736d0c1b1bbfef732acfb4f1785162ae88`; the two same-bilinear exchange UV poles are computed, while external-leg terms and the complete QCD renormalization remain open. No result is imported into the scalar two-point calculation.


## 2026-11-10 Major Point 1 portal/Higgs-constraint audit

The finite VLL portal threshold is not symmetry-forbidden and is numerically sizable at the two reference points: Delta lambda_HS^hard = -0.21076398 (A) and -0.01067338 (B). The negligible-portal reference condition cancels this threshold and is a conditional matching/tuning benchmark, not a prediction. The residual dimension-six/eight local mixed curvatures are +0.656934 GeV^2 (A) and +0.147834 GeV^2 (B), but the near-degenerate region requires a full complex-pole treatment. Benchmark A also has the exotic channel h_1 -> A'A' open; its width is approximately 3.744 GeV times sin^2(theta), so the simple no-exotic Higgs signal-strength mapping is not applicable there. See [MAJOR1_PORTAL_THRESHOLD_AND_HIGGS_CONSTRAINT_2026-11-10.md](MAJOR1_PORTAL_THRESHOLD_AND_HIGGS_CONSTRAINT_2026-11-10.md) and its reproducible numerical audit.


## 2026-11-10 — UV scalar-potential and diagram-census freeze

Added `UV_SCALAR_POTENTIAL_AND_DIAGRAM_CENSUS_2026-11-10.md`. The current manuscript states the portal and mixing relation but does not display the complete renormalizable scalar potential or tadpole equations. The new record supplies the unique one-Higgs-doublet/one-complex-singlet CP-conserving renormalizable potential, its tadpole conditions, CP-even mass matrix, cubic and Goldstone vertices, and the (sA'A') vertices. It also fixes the combined loop counting implied by the conditional zero-EFT-portal matching and inventories the missing gauge, Goldstone, tadpole, counterterm and two-loop sectors. This is a calculation-scope freeze, not a claim that the physical pole calculation is complete.


## 2026-11-10 — scalar-potential symbolic validation

Added `scalar_potential_symbolic_audit.py` and `scalar_potential_symbolic_audit_validation.txt`. The SymPy audit was executed locally and verifies both tadpole equations, the CP-even mass matrix, the (hhh,sss,hhs,hss) cubic derivatives, the electroweak and (U(1)_X) Goldstone cubic derivatives, and the (hhss) portal quartic. This is a tree-level algebra validation only; it does not close loop counterterms or establish physical poles.


## 2026-11-10 — direct scalar-width and complex-pole-residue audits

Added `SINGLET_SCALAR_DIRECT_WIDTH_AUDIT_2026-11-10.md` with an independently evaluated tree-level width subset for (s\to A'A',\mu^+\mu^-,\tau^+\tau^-). At the tree-level perturbativity ceiling (m_s=\sqrt{8\pi}v_s), the direct-width ratio approaches (\Gamma_s/m_s\simeq1/4) in both benchmarks, showing that the formal perturbativity endpoint is not a narrow-resonance regime. The script and numerical output are archived alongside it.

Added `PLAN_C_LITE_COMPLEX_POLE_RESIDUES_2026-11-10.md` and its numerical audit. For the inherited Plan-C-lite approximate propagator, the complex pole residue matrix is computed from the derivative of the determinant. At exact degeneracy in Benchmark B, the two Higgs-channel residues are approximately (-0.035432-0.024342i) and (1.035432+0.024342i), summing to one. These are complex residues, not probabilities or signal strengths; they demonstrate the need for a coherent two-pole amplitude. All results retain the existing fixed-width, selected-matching-kernel limitations.

The scalar-potential SymPy audit was executed locally and passed its tadpole, mass-matrix, cubic, Goldstone and quartic checks. None of these additions claims a complete gauge-independent pole or LHC likelihood.


## 2026-11-10 — exact-momentum fermion-sector hard matching and poles

Added `EXACT_MOMENTUM_FERMION_MATCHED_POLES_2026-11-10.md` and its reproducibility script/output. The full-minus-light mass-eigenstate hard momentum remainder is now evaluated from the Feynman-parameter (B_0) functions at complex (s), with the second-sheet continuation for the open (mu,	au) cuts. At (s=m_h^2), it reproduces the archived hard coefficients (0.0240304439859) GeV² (A) and (0.00540772399471) GeV² (B). The matched off-diagonal kernel uses the exact SVD light-state couplings rather than the leading mass-proportional approximation.

The approximate complex poles and residues were recomputed using this exact-momentum fermion hard remainder. The qualitative near-degenerate pattern is stable: A has a broad singlet pole from (A'A'), while B has overlapping poles with complex Higgs-channel residues. This remains a fermion-sector matched subset with fixed diagonal widths and incomplete EFT counterterm/gauge completion; no physical Higgs likelihood or exclusion is claimed.


## 2026-11-10 — coherent two-pole spectral-area diagnostic

Added `COHERENT_TWO_POLE_SPECTRAL_AREA_2026-11-10.md` with a reproducible integration of the coherent (D_{hh}) amplitude over 124.5--126.0 GeV. In the selected Plan-C-lite kernel, the integrated h-channel spectral-area ratios at exact degeneracy are 0.99934 (A) and 0.98777 (B); the corresponding non-degenerate 100 and 150 GeV checks are within about (3.1\times10^{-5}) of unity. This demonstrates that a sharp pointwise two-pole interference structure need not imply a comparably large integrated rate change. It is only a theory-level area proxy with fixed widths and constant vertices, not a detector-level signal strength or experimental likelihood.


## 2026-11-10 — Benchmark-A vector cascade and CMS search applicability

Added `BENCHMARK_A_CMS_VECTOR_CASCADE_2026-11-10.md`. Using the exact-momentum matched A benchmark pole residue, the isolated-pole estimate gives (mathcal B(h_1\to A'A')\simeq7.67\times10^{-4}), and the pure-axial (A') widths give (mathcal B(A'A'\to\mu\mu\tau\tau)\simeq0.20584). Thus ((\sigma/\sigma_{SM})\mathcal B(h_1\to A'A'\to\mu\mu\tau\tau)\simeq1.58\times10^{-4}).

This is comparable in order of magnitude to the 2026 CMS-SUS-23-005 model-independent (H\to aa\to\mu\mu\tau\tau) sensitivity envelope ((5\times10^{-5}) to (2.7\times10^{-4}) for (m_a=3.6\)--21 GeV). It is not a direct exclusion: CMS generates a pseudoscalar, whereas our (A') is a longitudinally polarized spin-1 state ((F_L\simeq0.999667) at this benchmark), and the 10 GeV point is in the (Upsilon)-background region. A vector-specific detector recast is required.


## 2026-11-10 — perturbative-order and gauge-completion map

Added `PERTURBATIVE_ORDER_AND_GAUGE_COMPLETION_2026-11-10.md`. It makes explicit that the retained negligible-EFT-portal benchmark counts the UV portal as (O(\hbar)): the exact fermion (hh,hs,ss) matrix is the leading new-physics (O(\hbar)) sector, while scalar/Goldstone/vector/ghost one-loop graphs containing a portal-induced vertex are (O(\hbar^2)) in this combined counting. It records the associated tadpole, VEV, field and mass counterterms and the no-double-counting rules.

This closes the order-classification/census step, not the loop calculation itself. The next work is to derive a common (R_\xi)-gauge-fixed Lagrangian and ghost action, machine-generate the complete vertex ledger, then calculate the complete (O(\hbar^2)) (hh,hs,ss) set and verify UV and gauge-parameter cancellation. No (h\to A'A') recast is part of this stage.


## 2026-11-10 — A1 (R_\xi) gauge-fixing derivation

Added `RXI_GAUGE_FIXING_A1_2026-11-10.md`. It fixes the charged/neutral electroweak and (U(1)_X) gauge-fixing functions, Goldstone masses, and cancellation of the gauge--Goldstone quadratic mixings. It defines the full Faddeev--Popov operator as the functional derivative of the gauge-fixing map under the nonlinear gauge transformations. The field-dependent ghost vertices are intentionally deferred to A2, rather than assigning an unverified sign/coefficient.

A1 is a Lagrangian setup step only. It does not yet provide the full ghost vertex expansion, loop integrals, or gauge-independent self-energies.


## 2026-11-10 — A2 gauge-basis scalar/ghost vertex ledger

Added `A2_SCALAR_GAUGE_GHOST_VERTEX_LEDGER_2026-11-10.md`, the SymPy audit script, and its output. The symbolic audit checks all nonzero cubic and quartic derivatives of the original (H,S) potential, the (hWW,hZZ,sA'A') and quartic gauge-boson vertices, and the radial scalar dependence of the FP operators.

A normalization error in the first A1 draft was corrected: since (m_X=2g_Xv_S), the (sar c_Xc_X) coefficient is (-\xi_Xm_X^2/v_S=-2\xi_Xm_Xg_X), not (-\xi_Xm_Xg_X). A1's scalar gauge-transformation signs were aligned with the (D_\mu=\partial_\mu+ig_AT^AA_\mu^A) convention.

A2 also corrected the earlier diagram census. In the gauge basis, (h) couples to (W,Z) and electroweak ghosts, while (s) couples to (A') and the (X) ghost. There is no common vector or ghost species, hence no one-loop (hs) vector/ghost bubble. These sectors contribute to diagonal (hh) and (ss) entries. The next-combined-order one-loop-topology (hs) subset consists of scalar/Goldstone bubbles; its pre-counterterm UV coupling combination is proportional to (\lambda_{HS}vv_S(6\lambda_H+4\lambda_S)).

The full component expansion of non-Abelian ghost-vector/off-diagonal entries, PV integration, tadpole/counterterm closure, and gauge-parameter cancellation remain open. No complete physical self-energy or pole is claimed.


## 2026-11-10 — A3a mixed scalar-bubble kernel

Added `A3A_MIXED_SCALAR_BUBBLE_KERNEL_2026-11-10.md`, its SymPy UV-pole audit script, and output. The gauge-basis one-loop-topology (hs) scalar kernel is written in terms of five (B_0) functions: internal (hh), (ss), (G^+G^-), (G^0G^0), and (aa). The CP-even (hh/ss) terms are identified as the already archived P2-lite subset; the new contribution is the three Goldstone terms with their (R_\xi)-dependent masses.

The symmetry-weighted UV pole is
[
\Pi_{hs}^{\rm scalar,UV}=
\frac{\lambda_{HS}vv_S}{16\pi^2\bar\epsilon}
(6\lambda_H+4\lambda_S),
]
which matches the scalar-potential portal counterterm contribution in the stated convention. Gauge/Yukawa pieces, higher powers of the portal, tadpole/VEV and field renormalization, and full UV--EFT matching are not included. The finite Goldstone terms are gauge dependent and are not a physical mixing prediction.


A3a was extended with an independent (O(4)\times O(2)) effective-potential check. It gives
[
[\mathrm{Tr}{\cal M}_{\rm scal}^4]_{H^2S^2}
=2\lambda_{HS}(3\lambda_H+\lambda_{HS}+2\lambda_S),
]
and the scalar-only portal counterterm includes the additional (2\lambda_{HS}^2) term. Its part linear in (lambda_{HS}) agrees with the bubble UV pole; the portal-squared term is beyond the adopted (lambda_{HS}=O(\hbar)), (O(\hbar^2)) truncation. The audit script/output were updated.


## 2026-11-10 — A3b tadpole/VEV and mixed field-counterterm matrix

Added `A3B_TADPOLE_VEV_FIELD_COUNTERTERMS_2026-11-10.md`, its SymPy audit script, and output. It derives the linearized (h,s) tadpole counterterms, parameter/VEV contributions to all three CP-even mass entries, and the general nonsymmetric (2\times2) field-renormalization contribution to (\Gamma_{hs}^{\rm inv}(p^2)). The symmetric zero-tree-portal limit is also given explicitly.

This is counterterm algebra, not a chosen renormalization scheme. The tadpole prescription, finite VEV conditions, field-renormalization convention, and actual common-scale UV/EFT counterterm coefficients remain to be fixed before the mixed self-energy can be called renormalized.


## 2026-11-10 — A3c \(R_\xi\) Goldstone-cut diagnostic

Added \`A3C_GOLDSTONE_GAUGE_PARAMETER_DIAGNOSTIC_2026-11-10.md\`, the numerical script, and output. At \(p^2=m_h^2\), the A3a Goldstone subset has gauge-dependent absorptive thresholds. In Feynman gauge, the \(aa\) Goldstone cut is open for A (\(m_X=10\) GeV) but closed for B (\(m_X=63\) GeV); at \(\xi=0.5\), the charged Goldstone cut opens in both and the B \(aa\) cut also opens. At \(\xi=40\), all these cuts close.

This is an explicit demonstration that the Goldstone-only \(\Pi_{hs}\) finite part is not physical. The physical poles require the complete \(hh,hs,ss\) matrix, including diagonal vector/Goldstone/ghost terms and the matching counterterms. The calculation does not claim the cancellation; it identifies a necessary gauge-parameter acceptance test.


## 2026-11-10 — A4a complete \(U(1)_X\) one-loop \(ss\) kernel

Added \`A4A_U1X_SS_SELF_ENERGY_2026-11-10.md\`, the SymPy/numerical audit script, and output. The general-\(R_\xi\) Euclidean integral representation includes the \(A'A'\) bubble and seagull, mixed \(A'a\) derivative bubble, Goldstone bubble and seagull, and complex \(U(1)_X\) ghost bubble. The radial \(s\)-loop bubble and quartic tadpole are added separately.

The Feynman-gauge expression reduces to \(A_E/B_E\) functions. The general-\(\xi\) longitudinal-vector/ghost tadpole cancellation and the \(p_E^2=0,\lambda_S=0\) unphysical-sector cancellation are verified algebraically. The Feynman-gauge absorptive part at \(p^2=m_s^2\) reproduces the physical \(s\to A'A'\) width exactly. At the open-channel benchmark points the relative numerical residual is below \(3\\times10^{-16}\).

The bosonic singlet-sector Feynman-gauge UV pole is recorded, including the \(p_E^2\) field-renormalization divergence. No scheme-dependent real finite part or physical pole is claimed: the common tadpole/subtraction scheme, full UV--EFT matching counterterms, general-\(\xi\) on-shell reduction, and electroweak \(hh\) sector remain open.


## 2026-11-10 — A4b explicit general-\(R_\xi\) on-shell cut cancellation

Added \`A4B_GENERAL_XI_ON_SHELL_CUT_CANCELLATION_2026-11-10.md\`, the phase-space audit script, and output. The massive-vector propagator is decomposed into transverse and longitudinal poles with their correct \(\xi_X\)-dependent residue weights. The vector-vector, mixed vector-Goldstone, Goldstone and complex-ghost two-body cuts are evaluated separately using the exact CM kinematics and projector traces.

For A at \(m_s=100,125.25,150\) GeV and B at \(m_s=150,200\) GeV, six gauge choices \(\xi_X=0.25,0.5,1,2,4,10\) were checked. The maximum relative variation of the complete on-shell absorptive coefficient is \(8.61\\times10^{-16}\). It equals the physical three-polarization \(s\\to A'A'\) width in every open case. The component cuts can vary strongly and open/close with \(\xi_X\), while their sum remains invariant.

This establishes general-\(\xi_X\) independence of the one-loop on-shell absorptive part. It does not establish gauge independence of the full complex pole; the real part, tadpole/counterterm closure, fermion matching and electroweak \(hh\) sector remain open.


## 2026-11-10 — A4c general-\(R_{\xi_X}\) \(ss\) UV pole and field renormalization

Added \`A4C_GENERAL_XI_SS_UV_AND_FIELD_RENORM_2026-11-10.md\`, the symbolic audit script, and output. The large-momentum expansion of the mixed \(A'a\) loop gives the momentum pole \((3-\xi_X)p_E^2\) and the zero-momentum local pole \(-2\xi_X^2m_X^2\). Combining the vector seagull/bubble, mixed loop and ghost bubble cancels all \(\xi_X^2m_X^2\) terms.

The complete bosonic singlet-sector UV pole is
\[
16\pi^2\Pi_{ss,E}^{\rm bos,UV}
=\frac{-g_A^2(3-\xi_X)p_E^2-9g_A^2m_X^2-\xi_X\lambda_Sm_X^2-26\lambda_S^2v_S^2}{\\bar\\epsilon}.
\]
The resulting diagonal field-counterterm coefficient is \(\delta Z_s^X=g_A^2(3-\xi_X)/(16\pi^2\\bar\\epsilon)\), matching the scalar-QED covariant-gauge coefficient. At \(\xi_X=1\), the result reduces to A4a. The local mass poles still require the common tadpole/VEV and parameter-renormalization prescription.


## 2026-11-10 — A4d tadpole-improved zero-momentum \(ss\) kernel

Added \`A4D_TADPOLE_IMPROVED_SS_KERNEL_2026-11-10.md\`, the symbolic audit script, and output. An exact \(p_E^2=0\) identity is obtained for \(\Pi_{ss,E}(0)-T_s^{(1)}/v_S\): all vector, Goldstone and radial-scalar seagulls cancel against the corresponding tadpole/VEV terms, while the longitudinal-vector, mixed \(A'a\), and ghost sector cancels identically for arbitrary \(\xi_X\).

The remaining kernel contains only the transverse-vector bubble and the Goldstone/radial scalar bubbles. Its UV pole is
\[
16\pi^2[\Pi_{ss,E}(0)-T_s^{(1)}/v_S]_{\rm UV}
=-[2(d-1)g_A^2m_X^2+20\lambda_S^2v_S^2]/\\bar\\epsilon,
\]
or \(-[6g_A^2m_X^2+20\lambda_S^2v_S^2]/\\bar\\epsilon\) in four dimensions. This is an exact zero-momentum identity, not a claim of gauge independence at nonzero momentum or of a physical pole.


A4d was extended to arbitrary external momentum. After the tadpole term is included, the local mass pole is \(\xi_X\)-independent:
\[
16\pi^2[\Pi_{ss,E}(p_E^2)-T_s^{(1)}/v_S]_{\rm UV}
=\frac{-g_A^2(3-\xi_X)p_E^2-6g_A^2m_X^2-20\lambda_S^2v_S^2}{\\bar\\epsilon}.
\]
Only the field-renormalization pole retains the \((3-\xi_X)\) dependence. In Feynman gauge the full tadpole-improved bosonic kernel reduces to two \(B_E\) functions (vector/Goldstone and radial-scalar thresholds); this is still an intermediate kernel, not a physical pole.


## 2026-11-10 — A5a provenance and suitability of the 20 TeV VLL matching scale

Added \`A5A_SCALE_PROVENANCE_AND_MATCHING_SCALE_AUDIT_2026-11-10.md\`, its numerical audit script, and output. The note distinguishes the UV mass parameter \(M_E\), physical heavy singular values, matching scale \(\mu_M\), hard-loop subtraction scale \(\mu_R^{\rm hard}\), and low-energy EFT scale \(\mu_{\rm EFT}\).

The 20 TeV value is the inherited PR #49 / Plan-C-lite benchmark, not a unique prediction. Under the conditional \(\theta_{\tau L},\theta_{\tau R}\le10^{-2}\) assumption and \(m_\tau\simeq\theta_{\tau L}\theta_{\tau R}M_E\), the lower consistency scale is 17.7686 TeV; at 20 TeV, \(\theta_{\tau R}=8.8843\times10^{-3}\). The exact SVD heavy thresholds are 20.001003 and 20.001789 TeV, with negligible logarithms relative to 20 TeV. Thus one common \(\mu_M=20\) TeV is appropriate for this degenerate benchmark.

For the hard VLL matching, \(\mu_R^{\rm hard}=M_E\) removes \(\ln(M_E^2/\mu_R^2)\). The low-energy EFT should subsequently be RG-evolved to \(\mu_{\rm EFT}\sim m_h\); 20 TeV is not to be used indiscriminately for all low-energy loops. The archived Plan-C-lite partial hard+soft comparison changes the real \(\Pi_{hs}\) by 0.1421% between \(\mu_R=M_E\) and \(m_h\), but this is not a complete RG/matching-scale closure because the same-order EFT soft/counterterm set remains open.

The A5a plan and calculation protocol now explicitly separate these scales. A factor-two matching-scale variation is deferred until the full EFT beta functions and matching counterterms are available; the portal boundary must be evolved, not reset to zero at every varied scale.


## 2026-11-10 — A5b first RGE block: \(C_5C_5^\ast\) derivative-operator running

Added A5B_RESTRICTED_EFT_RGE_AND_HARD_SOFT_SCALE_CANCELLATION_2026-11-10.md, its SymPy/numerical audit script, and the recorded output. The existing RC-001 EFT bubble-plus-contact pole gives
\[
\delta c_{\partial HS}
=-\frac{M_E^2}{32\pi^2}\sum_\ell |C_{5,\ell}|^2\Delta_{\rm UV},
\qquad
\left.\beta_{c_{\partial HS}}\right|_{C_5C_5^\ast}
=-\frac{M_E^2}{16\pi^2}\sum_\ell |C_{5,\ell}|^2.
\]
For the current normalization with \(M_*=M_E\), this equals \(\Delta\lambda_{HS}^{E}/2\). The hard logarithm and the displayed soft-bubble logarithm cancel analytically at leading \(O(M_E^{-2})\); benchmark A/B numerical checks reproduce the corresponding leading-log shifts.

The A3a scalar-only linear portal beta contribution was also translated from its pole residue:
\[
\left.\beta_{\lambda_{HS}}\right|_{\rm scalar,linear}
=\frac{\lambda_{HS}}{16\pi^2}(12\lambda_H+8\lambda_S).
\]
This is not the complete portal beta function. Gauge/Yukawa terms, the full same-order EFT soft set, the remaining Wilson-vector anomalous dimensions, and common EOM/source/tadpole closure remain open. The archived 0.1421% Plan-C-lite scale residual is not explained by this restricted leading-log identity and remains a separate diagnostic.

A branch-local GitHub Actions attempt was made, but GitHub created a failed job with runner_id=0, no steps, and no retrievable logs; this is not a script failure and not a CI pass. The temporary workflow was removed to avoid leaving a known failing check in the Draft PR. The symbolic/numeric equations were evaluated directly in the local Python/SymPy analysis environment; a clean exact-script CI rerun remains pending.


A fixed-physical-mass factor-two diagnostic was added at \(\mu=10,20,40\) TeV with \(M_E=20\) TeV held fixed. The hard and soft derivative pieces shift oppositely, while their sum is unchanged for the restricted RC-001 leading-log sector: \(4.140843561227\times10^{-5}\) (A) and \(9.318404228173\times10^{-6}\) (B). This is not the final full-model matching-scale uncertainty test. The corresponding table and the derivative-only \(m_h^2\) projections are recorded in the A5b note and output.


Added A5B_RGE_CLOSURE_MATRIX_AND_WORK_ORDER_2026-11-10.md to distinguish the UV portal beta, EFT derivative-operator running, \(C_5/Q_{LD}/Q_{RD}\) and current-operator mixing, tadpole/field renormalization, and the separate dimension-eight branch. It records the accepted intermediate result and orders the remaining work before a full \(\mu_M\) stability test.


## 2026-11-11 — B5-1 complete one-loop UV portal beta

Added B5_1_FULL_UV_PORTAL_BETA_FUNCTION_2026-11-11.md, b5_1_uv_portal_beta_audit.py, and B5_1_UV_PORTAL_BETA_AUDIT_OUTPUT_2026-11-11.txt.

For the original one-complex-singlet/two-VLL model, with \(Q_S=2\) and diagonal Abelian kinetic terms at the common threshold, the one-loop UV result is
\[
16\pi^2\beta_{\lambda_{HS}}^{UV}
=\lambda_{HS}^{UV}\left[
12\lambda_H+8\lambda_S+4\lambda_{HS}^{UV}
-\frac92g_2^2-\frac32g_Y^2-24g_X^2
+2\left(\mathcal T_H^{SM}+\sum_\ell|y_\ell|^2+\sum_\ell|\lambda_\ell|^2\right)
\right].
\]
The \(4\lambda_{HS}^2\) term is retained in the ordinary full one-loop MS expression and dropped in the strict \(\lambda_{HS}=O(\hbar)\), \(O(\hbar^2)\) combined truncation. The additive VLL \(|y_\ell|^2|\lambda_\ell|^2\) UV-pole coefficient is exactly zero from the field-dependent fermion determinant; the multiplicative VLL Yukawa wavefunction terms are nonzero. The complete chiral spectrum also gives \(\operatorname{Tr}(YX)=0\) at the common threshold.

Benchmark A/B decompositions are recorded over \(m_s=10\)–150 GeV. At the illustrative \(m_s=125.25\) GeV point, the known subtotal excluding the still-unfixed SM running remainder is \(+6.04131\times10^{-2}\) (A) and \(+5.77446\times10^{-4}\) (B), including the full one-loop portal-squared term. The numerical SM remainder is kept symbolic until \(g_2,g_Y,Y_{u,d,e}\) at \(20\) TeV are fixed in one input scheme. Benchmark A has \(\lambda_\tau=\sqrt{4\pi}\), so higher-loop running should be monitored.

B5-1 is analytically derived for \(\chi(M_E)=0\) and the common VLL threshold. This does not yet provide the EFT beta below \(M_E\), coupled UV running, or full UV–EFT scale cancellation. The closure matrix/work order was updated accordingly.


## 2026-11-11 — B5-1b SM threshold input and coupled UV RGE

Added B5_1B_SM_THRESHOLD_AND_COUPLED_UV_RGE_2026-11-11.md, b5_1b_sm_threshold_and_uv_rge.py, and B5_1B_SM_THRESHOLD_AND_UV_RGE_OUTPUT_2026-11-11.txt.

PDG-2025 central values are inserted into the NNLO weak-scale \(\overline{\rm MS}\) matching interpolants of Buttazzo et al. The SM is then run at one loop to the common VLL threshold \(M_E=20\) TeV, giving
\[
(g_Y,g_2,g_3,y_t,\lambda_H)_{M_E}
=(0.3678266,0.6232068,0.9292987,0.7674037,0.0592606).
\]
The top-dominant SM trace gives \(D_{\rm SM}(M_E)=1.5827658\). This replaces the earlier B5-1 illustrative numerical decomposition that used the tree-level weak-scale \(\lambda_H=m_h^2/(2v_h^2)\); the analytic B5-1 beta expression itself is unchanged.

The complete one-loop UV system above \(M_E\) is now implemented for \(g_Y,g_2,g_3,g_X\), \(y_t,y_{\mu,\tau}\), \(\lambda_{\mu,\tau}\), and \(\lambda_H,\lambda_S,\lambda_{HS}\). The first-pass diagnostic finds:
- Benchmark A saturates \(\lambda_\tau^2=4\pi\) at \(M_E\), and \(\beta_{\lambda_\tau}>0\); it has no upward headroom under the adopted strict perturbativity bound.
- Benchmark A has a strongly negative \(\beta_{\lambda_S}\), dominated by \(-2\lambda_\tau^4/(16\pi^2)\).
- Benchmark B remains perturbative and has positive quartics to \(2M_E\) for the \(m_s=50,100,150\) GeV diagnostic points, but \(\lambda_H\) crosses zero near \(57.9\) TeV in the one-loop upward run.

These are provisional one-loop stability/perturbativity diagnostics, not final vacuum-lifetime claims. The correct threshold rule is now explicit: use the EFT below \(M_E\) and the full UV system above \(M_E\). Independent SARAH/PyR@TE or diagrammatic RGE validation, two-loop running, and B5-2 EFT operator evolution remain open.

The B5-1 note was amended to label its old tree-level-\(\lambda_H\) numerical table as illustrative only and to direct matching-scale numerical work to B5-1b.


### B5-1b RGE coefficient correction — complex-singlet Yukawa (2026-11-11)

A follow-up check against the general complex-scalar/Weyl RG formula of Jack and Osborn, arXiv:1312.0428, Sec. 5, Eqs. (5.4), (5.8), and (5.10), identified that the first B5-1b draft had imported the Higgs-doublet \(3/2\) self coefficient into the singlet Yukawa beta. For a Yukawa coupling to the single complex scalar \(S\), the correct one-loop term is
\[
16\pi^2\beta_{\lambda_\ell}
=\lambda_\ell\left[2\lambda_\ell^2+\sum_{k=\mu,\tau}\lambda_k^2
-6g_Y^2-6g_X^2\right].
\]
The Higgs-doublet \(y_\ell\) beta retains the SM-like \(3/2\) coefficient. The B5-1 portal beta and the scalar-quartic beta functions are unchanged. The B5-1b script, note, and output have been corrected and the coupled trajectories recomputed.

The corrected values are \(\beta_{\lambda_\tau}(M_E)=0.828389\) (A) and \(0.00525178\) (B). The formal Benchmark-A \(\lambda_S\) zero for \(m_s=100\) GeV moves to \(30.98\) TeV; for Benchmark B, the \(\lambda_H\) zero remains near \(57.90\) TeV. Benchmark A remains outside the strict adopted Yukawa perturbativity bound immediately above \(M_E\), since it starts at \(\lambda_\tau=\sqrt{4\pi}\). The correction and its derivation are recorded in the B5-1b note.


## 2026-11-11 — B5-2A \(C_5C_5^\ast\) matching and quartic-EOM subblock

Added B5_2A_C5_SQUARED_AND_QUARTIC_EOM_BLOCK_2026-11-11.md, b5_2a_c5_squared_operator_block.py, and B5_2A_C5_SQUARED_AND_QUARTIC_EOM_OUTPUT_2026-11-11.txt.

The Yukawa-box \(C_5C_5^\ast\) hard matching subset is now evaluated numerically for A/B:
\[
(C_{LS},C_{He},C_{Se},C_{4f}^{S},C_{4f}^{V})_\ell
=\frac{|C_{5,\ell}|^2}{16\pi^2}
\left(-\frac38,+\frac38,+\frac34,-2,+1\right)
\quad(\mu=M_E).
\]
The scalar-to-vector four-fermion coefficient uses the declared chiral Fierz convention. Summed over flavors, the vector-current coefficient is \(2.63455\times10^{-10}\ {\rm GeV}^{-2}\) (A) and \(1.33417\times10^{-11}\ {\rm GeV}^{-2}\) (B).

The direct scalar derivative source remains
\[
\beta_{c_{\partial HS}}^{C_5C_5^\ast}
=-0.1053819882\quad(A),\qquad
=-0.00533668824\quad(B),
\]
and still satisfies \(\beta_c=\Delta\lambda_{HS}^{E}/2\) in the declared normalization.

The one-\(Q_{LD}\) or one-\(Q_{RD}\) insertion plus scalar-quartic hard/soft kernel is also evaluated as an off-shell EOM block, keeping the two \(Q_{LD}+\lambda_H\) weak-index tensors separate. In the minimal model the ordinary renormalizable muon/tau Yukawa source functions vanish, so these redundant EOM coefficients do not create an independent on-shell source at this order. They remain part of the off-shell counterterm/field-redefinition ledger.

B5-2 remains open: gauge corrections to \(Q_{LD},Q_{RD}\) and current operators, the multiplicative \(c_{\partial HS}\) anomalous dimension, complete operator mixing, and common EOM/source projection have not been calculated. The closure matrix was updated to distinguish this evaluated sub-block from full EFT-RGE closure.


## 2026-11-11 — B5-1b SM running-input sub-block

Added B5_1B_SM_RUNNING_INPUTS_20TEV_2026-11-11.md, b5_1b_sm_running_20tev.py, and B5_1B_SM_RUNNING_OUTPUT_2026-11-11.txt.

A declared one-loop \(\overline{\rm MS}\) SM-only input set was evolved to \(M_E=20\) TeV. The resulting values are \(g_Y=0.36865960\), \(g_2=0.62370335\), \(g_3=0.92908277\), \(y_t=0.77069903\), and \(\lambda_H=0.05807254\). Bottom/tau/electron Yukawas are neglected in this first diagnostic.

The top-only SM remainder is \(D_{\rm SM}=1.60947075\). Inserting it into the earlier B5-1 benchmark decomposition while holding the old scalar subtotal fixed gives diagnostic instantaneous values \(\beta_{\lambda_{HS}}^A=6.25612\times10^{-2}\) and \(\beta_{\lambda_{HS}}^B=6.86230\times10^{-4}\).

**Consistency warning:** the earlier scalar benchmark subtotal used the electroweak tree proxy \(\lambda_H=m_h^2/(2v_h^2)=0.12938\), whereas the one-loop SM-only running gives \(\lambda_H(20\,{\rm TeV})=0.05807\). These must not be mixed in a final matching-scale beta. The fully consistent value also requires the UV running of \(\lambda_S\), VLL Yukawas and \(g_X\), plus a common matching prescription. Therefore the two diagnostic beta values are not final UV matching-scale predictions.

The full coupled VLL beta functions have not yet been integrated. Derive and validate them before running Benchmark A, which starts at \(\lambda_\tau=\sqrt{4\pi}\). The VLLs must be decoupled at \(M_E\); the UV beta is not to be continued below threshold.
