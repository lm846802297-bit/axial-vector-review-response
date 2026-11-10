# A5b — EFT/portal RGE closure matrix and calculation order

**Date:** 2026-11-11 (updated after B5-1 and B5-1b)
**Purpose:** separate the beta-function entries already supported by the RC-001/A3/A4 work from the missing entries required for a full matched \(h-s\) pole calculation. This is a work ledger, not a claim that the full RGE system has been computed.

## 1. Closure matrix

| Sector / parameter | Required RGE or counterterm information | Current evidence | Status | Relevance to the current \(h-s\) calculation |
|---|---|---|---|---|
| UV \(\lambda_{HS}\): scalar loops | Linear portal pole and portal-squared term | A3a scalar/Goldstone bubble, effective-potential cross-check, and B5-1 conversion to beta | **Derived** | Full scalar one-loop contribution; portal-squared term is beyond the strict \(O(\hbar^2)\) combined truncation |
| UV \(\lambda_{HS}\): gauge loops | \(SU(2)_L\), \(U(1)_Y\), \(U(1)_X\) and kinetic-mixing dependence | B5-1 Casimir derivation; \(Q_S=2\); \(\operatorname{Tr}(YX)=0\) at the common threshold | **Derived at \(\chi=0\)** | Nonzero off-diagonal Abelian kinetic term remains a separate generalized-coupling case |
| UV \(\lambda_{HS}\): Yukawa loops | SM and VLL scalar-wavefunction terms; possible additive VLL box | B5-1 trace formula and exact \(\operatorname{Tr}[(\mathcal M^\dagger\mathcal M)^2]_{h^2s^2}=0\) check | **Derived at one loop** | Multiplicative VLL terms are nonzero; additive \(y^2\lambda^2\) pole is zero |
| UV \(\lambda_{HS}\): complete one-loop beta | Sum scalar, gauge, SM Yukawa and VLL Yukawa terms in the same \(\overline{\rm MS}\) convention | B5-1 analytic expression plus B5-1b numerical \(M_E\)-scale input and coupled UV integration | **Analytic result complete; numerical pass provisional** | Independent RGE-generator cross-check and higher-order input uncertainty remain open |
| UV coupled system: gauge/Yukawa/quartics | Coupled \(g_i,y_t,y_{\mu,\tau},\lambda_{\mu,\tau},\lambda_H,\lambda_S,\lambda_{HS}\) running above \(M_E\) | B5-1b one-loop system, exact real-scalar/Weyl Yukawa audits, B5-1d six-real-scalar quartic tensor and full gauge-spectrum audit (ten regression tests), and recomputed A/B integration | **Independent analytic tensor/group-theory audit passed; external PyR@TE/SARAH and higher-order validation open** | Do not run the UV system below \(M_E\); use the EFT there |
| EFT dimension-four \(\lambda_{HS}\) | Additive \(C_5C_5^\ast\) pole at \(M_E^{-2}\), plus ordinary EFT running | RC-001 bubble/contact pole is proportional to \(p^2\); no \(M_E^{-2}\) quartic pole in this sector | **Fixed-sector result** | Matched EFT portal remains zero in this restricted strict-dimension-six sector; not a full EFT beta statement |
| EFT \(c_{\partial HS}\): inhomogeneous term | \(C_5C_5^\ast\) soft pole and beta contribution | RC-001 counterterm ledger and A5b derivation | **Derived** | Directly controls the leading mixed-derivative self-energy and hard/soft log cancellation |
| EFT \(c_{\partial HS}\): multiplicative/mixing terms | Gauge/scalar/Yukawa anomalous dimensions and mixing with the complete dimension-six basis | RC-001 gauge attachment atlas and soft-topology census; not a complete anomalous-dimension matrix | **Open** | Required for a complete higher-order RGE and scale uncertainty |
| EFT \(C_5C_5^\ast\) current/4-fermion block | Hard coefficients for \(O_{LS},O_{He},O_{Se},O_{4f}\), matching-log derivatives and Fierz projection | B5-2A A/B evaluation with the \(S_\tau=S^\ast\) orientation factor restored in the common-\(S\) basis | **Yukawa-box sub-block evaluated; full mixing open** | Gauge corrections and complete current/4-fermion mixing remain open |
| EFT \(Q_{LD},Q_{RD}\)+quartic EOM block | Off-shell EOM/source operators from \(\lambda_H,\lambda_S,\lambda_{HS}\) insertions | RC-001 hard/soft kernel and B5-2A A/B numerical evaluation | **Kernel evaluated; EOM closure partial** | Redundant off-shell coefficients vanish as on-shell sources for minimal \(\mu,\tau\) Yukawas; common field/EOM scheme remains open |
| EFT \(C_5\) | One-loop gauge/scalar/fermion vertex and external-leg renormalization | B5-2B1 derives the diagonal-gauge parameter-induced running and independently reproduces it from the EFT fermion Casimirs; SFT-23/SFT-24 full vertex sets remain open | **Gauge-only parameter-running sub-block derived; full one-loop matching open** | The complete scalar/fermion/gauge vertex and external-leg amplitudes remain required |
| EFT \(Q_{LD},Q_{RD}\) | Gauge corrections, quartic insertions, external-leg terms, EOM/source projection | B5-2B1 derives the diagonal-gauge parameter poles and tree EOM map; B5-2B2 fixes the EFT \(B/A'\) derivative contacts and no-direct-\(W\) result | **Parameter poles, tree EOM map and EFT contacts derived; gauge-loop amplitudes open** | Needed for the complete Wilson vector; their mixing into the scalar sector must be checked at the retained order |
| EFT current operators | Gauge-current form factors, mixed \(B-A'\) terms, EOM reductions and kinetic-mixing boundary | B5-2A fixes the common-\(S\) flavor orientation; B5-2B1 fixes the tree current map; B5-2B2 fixes the EFT contact vertices | **Basis/contact conventions fixed; gauge form factors open** | Needed for complete gauge-covariant EFT and possible mixing into scalar sources |
| \(h,s\) diagonal fields and VEVs | \(\delta Z_{hh},\delta Z_{ss}\), \(\delta v,\delta v_s\), tadpole scheme and mass counterterms | A3b algebra; A4c \(U(1)_X\) \(ss\) field pole; A4d tadpole-improved \(ss\) kernel | **Partial** | Required before finite pole shifts; \(hh\) electroweak and common scheme closure remain open |
| Dimension-eight \(X^2Y^2\) | \(C_5^4\) soft pole, full hard matching, higher-dimensional tree-level insertions and EOM/source companions | RC-001 constant-pole audit and counterterm ledger | **Subset only** | Separate \(O(M_E^{-4})\) calculation; do not import into strict dimension six |

## 2. Important distinctions

### 2.1 Finite threshold versus beta-function pole

The VLL one-loop determinant has no mixed \(h^2s^2\) UV-pole coefficient:
\[
[\operatorname{Tr}({\cal M}^\dagger{\cal M})^2]_{h^2s^2}=0.
\]
Nevertheless, the finite hard threshold is
\[
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}\sum_\ell|y_\ell|^2|\lambda_\ell|^2.
\]
The absence of this additive UV pole does not set the full \(\beta_{\lambda_{HS}}\) to zero. Scalar, gauge, and multiplicative Yukawa terms remain.

### 2.2 Dimension-six derivative pole versus dimension-eight potential pole

The \(s=p^2\) pole from the \(C_5C_5^\ast\) bubble is \(O(M_E^{-2})\) and renormalizes \(c_{\partial HS}\). The constant broken-phase pole is proportional to \(q_\ell m_\ell^2\sim O(M_E^{-4})\) and belongs to the \(X^2Y^2\) dimension-eight sector. It must not be reinterpreted as a dimension-four portal beta.

### 2.3 A complete Wilson vector is not automatically required for every intermediate identity

The one-loop inhomogeneous \(C_5C_5^\ast\) contribution to \(\beta_{c_{\partial HS}}\) is a valid restricted result without pretending that the entire dimension-six Wilson vector is complete. Conversely, the restricted result cannot be used to claim a complete model-level scale uncertainty or a physical complex pole.

## 3. Ordered work plan

**B5-1 — UV portal beta closure (analytic result passed).** The full one-loop \(\overline{\rm MS}\) beta is recorded in `B5_1_FULL_UV_PORTAL_BETA_FUNCTION_2026-11-11.md`: scalar, \(SU(2)_L\), hypercharge, \(U(1)_X\), SM Yukawa, and VLL Yukawa terms are included. The additive VLL \(|y_\ell|^2|\lambda_\ell|^2\) pole is exactly zero, while the multiplicative VLL wavefunction terms are nonzero. The result assumes \(\chi(M_E)=0\) and the common VLL threshold; a numerical \(D_{\rm SM}(M_E)\) and coupled running of all UV couplings remain to be fixed.

**B5-1b — threshold input and coupled UV running (numerical pass corrected for the singlet-Yukawa and Higgs-quartic tensor coefficients).** The PDG-2025-based weak-scale inputs are matched to \(\overline{\rm MS}\), run with one-loop SM RGEs to \(M_E=20\) TeV, and then used to initialize the full one-loop UV system. The coupled UV run is only used above \(M_E\); the EFT must be used below \(M_E\). The initial singlet-Yukawa compact expression double-counted the same-flavor scalar trace; the exact two-real-scalar singlet Weyl-matrix audit fixes it to \(\beta_{\lambda_\mu}\propto\lambda_\mu(2\lambda_\mu^2+\lambda_\tau^2)\) and \(\beta_{\lambda_\tau}\propto\lambda_\tau(2\lambda_\tau^2+\lambda_\mu^2)\), and the benchmark trajectories have been recomputed. The one-loop diagnostic finds that Benchmark A saturates the adopted \(\lambda_\tau^2\le4\pi\) bound at the threshold, while Benchmark B remains perturbative to \(2M_E\) but its \(\lambda_H\) crosses zero near \(57.90\) TeV. The independent B5-1d analytic audit derives the gauge, Yukawa, and scalar-quartic coefficients and checks the full 12-component RHS; the \(\lambda_{HS}^2\) coefficient in \(\beta_{\lambda_H}\) is corrected from 2 to 1. These remain one-loop stability/perturbativity diagnostics, not final vacuum-lifetime claims. External PyR@TE/SARAH and two-loop checks remain required.


**B5-1d — independent analytic full-UV RGE audit (passed).** A separate implementation reconstructs the complete Weyl/complex-scalar gauge traces, the six-real-scalar quartic tensor, both VLL Yukawa matrix projections, external-field Casimirs, pure gauge quartic sources, and the VLL fermion determinant. Ten regression tests compare the independent 12-component beta vector and quartic decomposition against the production implementation at both benchmarks and a generic point. This audit exposes and corrects the Higgs-quartic portal coefficient to
\[
16\pi^2\beta_{\lambda_H}^{\rm scalar}
=24\lambda_H^2+\lambda_{HS}^2.
\]
The independent analytic audit is complete; an actual external PyR@TE/SARAH run or full diagrammatic calculation remains a separate acceptance gate.

**B5-2 — EFT operator running at the retained order.** B5-2A evaluates the \(C_5C_5^\ast\) hard current/4-fermion coefficients, their matching-log derivatives, and the \(Q_{LD},Q_{RD}\)+quartic off-shell EOM subblock for A/B. Its \(O_{LS}\) and \(O_{Se}\) coefficients are now corrected for \(S_\tau=S^\ast\) when expressed in the common-\(S\) basis. B5-2B1 adds the diagonal-gauge parameter-induced running of \(C_5,C_{LD},C_{RD}\) and derives the tree-level \(Q_{LD},Q_{RD}\) current/EOM map. B5-2B2 fixes the EFT derivative-contact vertices: both composites have \((Y,X)=(-1,\eta_\ell Q_\ell)\), giving \(-g_Y B_\mu+\eta_\ell Q_\ell g_X A'_\mu\) contact coefficients and no direct \(W^I\) contact. Still required are the complete gauge-loop UV/EFT amplitudes, the multiplicative \(c_{\partial HS}\) anomalous dimension, the full current/operator mixing matrix, and common EOM/source projection. Keep all sectors in one basis and exclude dimension-eight insertions from strict \(M_E^{-2}\) running.



**B5-2B2 — EFT derivative-contact vertices (analytic sub-block complete).** The composites \(H^\dagger L_\ell\) and \(S_\ell\ell_R\) are both weak singlets with \((Y,X)=(-1,\eta_\ell Q_\ell)\). Therefore the \(Q_{LD}\) and \(Q_{RD}\) EFT insertions each contain a \(B_\mu\) contact with coefficient \(-g_Y\) and an \(A'_\mu\) contact with coefficient \(+\eta_\ell Q_\ell g_X\); the latter flips sign for tau. The direct \(W^I\) contact cancels in \(D_\mu(H^\dagger L_\ell)\), although \(W\) still attaches to the individual \(L,H\) lines in \(Q_{LD}\) loops. This fixes the EFT contact set but does not evaluate the gauge-loop integrals or close the Ward identities.

**B5-3 — Common tadpole and field scheme.** Fix the VEV/tadpole prescription, \(h,s\) field-renormalization convention, and diagonal mass inputs. Combine A3b, A4c/A4d and the fermion sector without double counting tadpole or SM-width contributions.

**B5-4 — UV--EFT matching-scale cancellation.** Match the UV portal and derivative coefficients at \(\mu_M\), evolve them consistently, and verify cancellation of \(\mu_M\) dependence in the full retained \(h-s\) inverse propagator. Vary \(\mu_M\in[M_E/2,2M_E]\) only after B5-1 through B5-3 pass; use EFT evolution below \(M_E\) and UV evolution above \(M_E\).

**B5-5 — Dimension-eight branch.** Only after the strict dimension-six closure is stable, complete the \(O(M_E^{-4})\) hard/soft matching, including \(X^2Y^2\), higher-dimensional tree-level EFT insertions and their EOM/source companions.

## 4. Current acceptance decision

- The \(C_5C_5^\ast\) derivative-operator pole, its inhomogeneous beta contribution, and the restricted hard/soft leading-log cancellation are derived.
- The complete one-loop UV portal beta is analytically derived at the common-threshold \(\chi(M_E)=0\) boundary. B5-1b fixes a PDG-2025-based SM input scheme and evaluates the coupled one-loop UV system upward. B5-1d independently checks the full one-loop coefficient structure analytically and against the production RHS; external PyR@TE/SARAH execution and higher-order checks remain open.
- B5-2A has closed only the \(C_5C_5^\ast\) hard current/4-fermion matching sub-block and quartic EOM kernel, with the common-\(S\) tau orientation corrected. B5-2B1 has closed a diagonal-gauge parameter-pole sub-block and the tree-level current/EOM basis map. B5-2B2 has fixed the EFT \(B/A'\) derivative-contact vertices and the absence of a direct \(W\) contact. The complete EFT anomalous-dimension matrix, gauge-loop UV/EFT amplitudes, and multiplicative \(c_{\partial HS}\) running remain open.
- The archived \(0.1421\%\) Plan-C-lite residual remains open; the restricted leading-log cancellation does not by itself explain it.
