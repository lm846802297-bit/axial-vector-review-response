# Higgs--radial-scalar mixing and complex-pole calculation

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
- **RC-001 derivative-operator interface:** [RC001_UPSTREAM_INTERFACE.md](RC001_UPSTREAM_INTERFACE.md) pins the upstream high-energy-theory-research PR #11 head, maps the UV fields and charges to the original axial model, distinguishes QLD8 from the scalar-potential `O8`, and records the sign/scheme checks required before transferring derivative Wilson coefficients. The upstream scripts remain in their source repository.
- **C5/gauge convention audit:** [C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md](C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md) derives the signed \(C_5\) coefficient from the Schur complement, identifies the opposite sign in the printed v6 Eq. (5-d), gives the explicit \(D_+=D_-\) field-redefinition map, and includes an exact-rational audit/test suite.
- **QLD8 total-current expansion:** the upstream [RC-001 current-expansion record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD-total-current-expansion.md) now writes the full leading-renormalizable (J_Y), (J_2^a), and (J_X) currents for the original one-VEV model. Fermion-EOM/Fierz reduction remains open.
- **QLD8 Higgs-source/EOM map:** the upstream [source and flavor-charge record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD-Higgs-source-EOM-model-map.md) distinguishes gauge-forbidden diagonal mu/tau Yukawas from gauge-allowed but model-set-to-zero mu-tau off-diagonal Yukawas, and records the leading fermion EOMs and source power counting. Fierz reduction remains open.
- **QLD8 source-square channel census:** the upstream [Fierz-channel record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD-source-square-Fierz-channel-census.md) enumerates the three diagonal and three cross source pairs, their chirality classes, weak/color contractions, and derivative placements. Explicit d-dimensional Fierz reduction remains open.
- **Four-dimensional chiral Fierz algebra:** the upstream [exact Fierz record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD-chiral-Fierz-identities.md) verifies the RR/LL scalar-tensor and RL/LR vector identities in 1024 exact matrix components. A working NDR/anticommuting-γ5 and minimal Fierz-evanescent convention is now fixed for the QLD8 open-line sector; the complete d-dimensional counterterm basis remains open.

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


- **QLD8 derivative-aware Fierz/IBP ledger:** the pinned upstream [ledger](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD8-derivative-Fierz-IBP-ledger.md) establishes the exact complete-sum relation \((D_\mu J_A^\dagger)(D^\mu J_B)\doteq-J_A^\dagger D^2J_B\), records all 36 ordered derivative placements, and tracks the derivative on each original fermion through Fierz rearrangement. This is an operator identity, not a final nonredundant basis.
- **QLD8 second-order fermion EOM:** the pinned upstream [map](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD8-second-order-fermion-EOM-map.md) checks the Dirac-square curvature sign and maps the endpoint Laplacians into Higgs-derivative and field-strength four-fermion structures. The scalar-pair evanescents are not closed after this EOM substitution; an enlarged basis is still required.
- **CI status:** upstream PR runs 42733380866 (Fierz) and 42733381140 (schema validation) both failed with empty job-step lists; log retrieval returned 404. The cause is unknown. Local exact algebra/bookkeeping checks passed; no CI pass is claimed.


- **EOM-generated chiral Fierz identities:** the upstream [Fierz record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md) now includes the scalar-vector and scalar-tensor projections generated by the second-order fermion EOM. Exact SymPy checks pass for 34 identities (8704/8704 components) and six chiral tensor self-duality relations.
- **Remaining scheme gate:** the four-dimensional projections are established, but the d-dimensional evanescent differences and their one-loop mixing/counterterm matrix are not yet complete. The existing scalar-pair evanescents alone are insufficient after the second-order EOM substitution.
- **CI:** latest upstream runs 42734711989 and 42734712057 failed with empty job-step lists; log retrieval returned 404. The cause is unknown. Local exact algebra passed; no CI pass is claimed.


- **Explicit EOM-generated evanescent differences:** the upstream [Fierz note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md) now writes the \(E_{XY;V}^{\mu,rs}\) scalar-vector and \(E_{XY;T}^{\mu\nu,rs}\) scalar-tensor Fierz differences explicitly, including the Grassmann sign, Levi-Civita terms, and three-component chiral tensor basis. They have no \(O(\epsilon)\) physical admixture at definition stage.
- **Remaining calculation:** the one-loop mixing of these evanescents, UV-generated higher gamma strings, same-order EFT soft insertions, and finite Wilson coefficients remain open. No PR #69 scalar two-point coefficient is changed.
- **CI:** latest upstream runs 42735130364 and 42735130363 failed with empty job-step lists; logs were unavailable. No CI pass is claimed.


## 2026-11-10 update: QLD8 P1.0 counterterm-basis seed map

The upstream PR #11 is now pinned at [`127ff399cfa648c7dee75dc60aff143bd001422b`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/127ff399cfa648c7dee75dc60aff143bd001422b). The new [QLD8 one-loop Green-basis note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD8-one-loop-counterterm-basis.md) separates the off-shell four-fermion/two-derivative Green basis from the later EOM-reduced physical quotient. It freezes the six independent source-pair sectors, color singlet/octet structures, weak and flavor labels, all 36 derivative placements, and the direct-pairing rank-3/rank-4 evanescent seeds.

The accompanying [exact audit](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/calculations/RC-001-QLD8-counterterm-basis-audit.py) checks 64/64 rank-3 and 256/256 rank-4 duality assignments, all four chiral projections, 81/81 SU(3) color-index assignments, the SU(2) epsilon invariant, source representations, and derivative counting. The local exact checks pass.

**Boundary:** this is a P1.0 basis/Dirac-seed audit, not a one-loop calculation. No UV pole, (Z) matrix, anomalous dimension, or finite dimension-eight Wilson coefficient has been computed. It remains a four-fermion/current-sector calculation and does not add a contribution to the PR #69 (hh,hs,ss) two-point functions.

The new [P1.0 CI workflow](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/.github/workflows/rc001-qld8-counterterm-basis-audit.yml) ran as [Run #42737785635](https://github.com/lm846802297-bit/high-energy-theory-research/actions/runs/42737785635) and reported failure, but GitHub returned an empty job-step list and the job-log endpoint returned 404. The cause is unknown; this is not evidence of a failed algebra assertion. No CI pass is claimed.


## 2026-11-10 update: QLD8 P1.1a QCD color block

The upstream PR #11 pin has advanced to [\`127ff399cfa648c7dee75dc60aff143bd001422b\`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/127ff399cfa648c7dee75dc60aff143bd001422b). The new [\(d^\dagger d\) QCD color-factor record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD8-QCD-color-factor-block.md) fixes the crossed source tensor \(C_X=C_1/3+2C_8\) and computes all six pairwise SU(3) generator matrices in the singlet/octet basis. Their sum satisfies the exact color-singlet identity \(\sum_{a<b}\mathbf T_a\cdot\mathbf T_b=-8/3\,\mathbf1\).

The [reproducible color audit](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/calculations/RC-001-QLD8-QCD-color-factor-audit.py) passes locally. These are color factors only; no QCD loop kernel or UV pole is yet computed. The four-fermion/current-sector calculation remains separate from the PR #69 scalar two-point functions.

The updated [QLD8 CI workflow](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/.github/workflows/rc001-qld8-counterterm-basis-audit.yml) includes both basis-seed and QCD color audits. Its run for the immediately preceding head failed with an empty job-step list and unavailable logs; the new run for the current head was queued at the time of this update. No CI pass is claimed.


## 2026-11-10 update: QLD8 P1.1b QCD insertion routing

The upstream [\(d^\dagger d\) QCD routing record](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/research/RC-001-QLD8-QCD-one-loop-momentum-routing.md) fixes the all-incoming external-momentum convention and shows that the four product-rule derivative placements sum to the single tree insertion factor \(q_A^2\). It also fixes the loop-momentum shift for each of the six QCD exchange topologies: two within-current exchanges leave \(q_A\) unchanged, while four cross-current exchanges carry \((q_A\pm\ell)^2\).

The accompanying [exact symbolic audit](https://github.com/lm846802297-bit/high-energy-theory-research/blob/127ff399cfa648c7dee75dc60aff143bd001422b/calculations/RC-001-QLD8-QCD-momentum-routing-audit.py) passes locally. This closes the insertion-momentum routing algebra only; no Dirac loop numerator, tensor integral, UV pole, or counterterm matrix is yet computed. The work remains a four-fermion/current-sector calculation and does not add a contribution to PR #69 \(hh,hs,ss\).

The latest upstream QLD8 workflow run on the pinned head, #42739327386, failed with an empty job-step list; log retrieval returned 404. The cause is unknown; no CI pass is claimed.
