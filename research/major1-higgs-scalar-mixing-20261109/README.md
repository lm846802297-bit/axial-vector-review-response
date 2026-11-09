# Higgs--radial-scalar mixing and complex-pole calculation

**Scope:** independent theoretical workstream for the Higgs--radial-scalar two-point function in the original one-VEV \(S+\mathrm{VLL}\) model.  
**Baseline:** merged PR #49 and the archived calculations listed below.  
**Status:** the exact mass-eigenstate mu/tau+VLL fermion contribution to all three independent self-energy entries, its full-theory tadpole/potential counterterms, the leading dimension-five EFT bubble-plus-contact/dimension-eight UV structure, the Plan-C scale-running check, and the finite heavy-VLL scalar-potential matching through dimension eight are CI-validated. PR #69 adopts the signed dimension-five coefficient convention used by RC-001; its comparison with the sign displayed in the archived v6 manuscript Eq. (5-d) is tracked as an explicit open audit item in [RC001_UPSTREAM_INTERFACE.md](RC001_UPSTREAM_INTERFACE.md). Complete same-order UV--EFT matching, the finite tadpole/VEV prescription, the full gauge-complete propagator, physical complex poles/residues, and near-degenerate observables remain open.

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
