# RC-001 — Portal Boundary and B1/B3 Kernel Reconciliation Ledger

> **Record type:** Dated internal reconciliation supplement; it does not replace the frozen primary source or claim complete model-level matching.
>
> **Audit date:** 2026-10-27
>
> **Status:** The portal matching relation and a working scalar-suppressed reference boundary are explicit. The tree-level C5 coefficient has a separate derivation and exact symbolic check. All 576 real-scalar candidate-kernel integrals are evaluated conditionally, and their algebraic B1/B3 Wick signs are resolved under the declared trace convention. A separate complex-external projection now selects one oriented cycle per flavor in the unbroken zero-mixing limit: muon s channel and tau u channel. The source-aligned one-cycle hard-region audit reproduces the §248 polynomial and diagrammatic sign product. The fixed-complex 16-path mass-basis sum is now proven equal to one interaction-basis propagator trace at integrand level, and its unbroken limit reduces to the source-aligned path 0101. VEV-suppressed finite-mixing hard/soft corrections, complete EFT soft/counterterm closure beyond the fixed sector, and model-level Wilson-vector closure remain **unresolved**.

## 1. Provenance and version relationship

### 1.1 Repository baseline

- **Repository:** [`high-energy-theory-research`](https://github.com/lm846802297-bit/high-energy-theory-research)
- **Baseline `main` HEAD at audit:** [`d6143c2aa15191ac8521e062d90860ba86713f00`](https://github.com/lm846802297-bit/high-energy-theory-research/commit/d6143c2aa15191ac8521e062d90860ba86713f00)
- **RC-001 source record:** [`research/RC-001-vll-higgs-singlet-uv-eft.md`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/research/RC-001-vll-higgs-singlet-uv-eft.md)
- **Source-record blob SHA:** `4a334a2ad0ca1ebed9063b9657588c82cdf2f14b`
- **Live claim matrix:** [`research/RC-001-claim-evidence-matrix.md`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/research/RC-001-claim-evidence-matrix.md)
- **Current source-aligned two-point algebra audit:** [script](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/calculations/RC-001-uv-eft-two-point-difference.py) and [captured output](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/validation/RC-001-uv-eft-two-point-difference.txt).

### 1.2 Frozen primary working source

The RC-001 record identifies the source baseline as:

- **File:** `higgs_portal_mixing_unified_reviewer_response_and_uv_eft_UPDATED_v2(8)(20261021)(153)_matchete_mapping_version_history.md`
- **Library file ID:** `[private-library-id-withheld]`
- **Version ID:** `1`
- **Size:** `1,989,214` bytes
- **SHA-256:** `f30af8ccc62feafa3923e8356437e4b80b40e518fc9b1188646b4d763e2791f1`

Relevant source sections:

- §§272–274: portal threshold, UV pole, zero-momentum sign convention, and parameterized \(h\)–\(s\) self-energy;
- §§248–252: fixed-sector hard-minus-soft matching and off-shell completion;
- §§276–285: mass-basis self-energy, EFT soft bubble, and the old on-shell \(4/3\) finite difference;
- §§286–302: projection/EOM analysis and reconciliation of the \(4/3\) difference;
- §§76–89 and §§238–239: historical B-kernel/Wick audits and path-resolved candidate integrations.

This ledger is a dated supplement to that frozen source. It does not rewrite the source file, change the claim matrix, or alter the historical v66 archive.

## 2. Portal boundary: one explicit reference benchmark

### 2.1 Matching equation and scheme

Use the potential convention

\[
V(H,S)\supset \lambda_{HS}(H^\dagger H)(S^\dagger S),
\qquad \mathcal L\supset -V.
\]

For the VLL Yukawa sector recorded in RC-001, in dimensional regularization and \(\overline{\mathrm{MS}}\), the one-loop zero-momentum threshold is

\[
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}
\sum_{\ell=\mu,\tau}|y_\ell|^2|\lambda_\ell|^2.
\]

At a common matching scale \(\mu_M\), with both heavy states integrated out at that scale,

\[
\boxed{
\lambda_{HS}^{<}(\mu_M)
=\lambda_{HS}^{>}(\mu_M)
+\Delta\lambda_{HS}^{E}
+O(\text{two loops},\text{higher-dimensional matching}).
}
\]

Here \(>\) denotes the UV theory and \(<\) the EFT after integrating out the heavy vector-like leptons. The source calculation finds no one-loop **additive UV pole** proportional to \(|y_\ell|^2|\lambda_\ell|^2\) in this sector, but it does find the finite threshold above. Other beta-function terms and other sectors are not thereby set to zero.

### 2.2 Working boundary selected for the scalar-suppressed reference benchmark

For the next calculation, freeze the following as a **reference benchmark condition**, not as a claim about an input already specified in the original paper:

\[
\boxed{\lambda_{HS}^{<}(\mu_M)=0,\qquad \mu_M=M_E}
\]

for the degenerate reference case \(M_{E_\mu}=M_{E_\tau}=M_E\). The corresponding UV boundary at the same matching scale must be

\[
\boxed{
\lambda_{HS}^{>}(\mu_M)
=+\frac{1}{8\pi^2}
\sum_{\ell=\mu,\tau}|y_\ell|^2|\lambda_\ell|^2.
}
\]

This choice makes the *matched dimension-four EFT portal parameter* vanish at \(\mu_M\) to the displayed order. It is a boundary-condition choice that cancels the finite threshold; it is not a cancellation predicted without input and should not be described as technically automatic.

The comparison case remains:

\[
\lambda_{HS}^{>}(\mu_M)=0
\quad\Longrightarrow\quad
\lambda_{HS}^{<}(\mu_M)=\Delta\lambda_{HS}^{E}<0
\]

for nonzero Yukawa products. Thus “zero UV portal” and “zero matched EFT portal” are distinct assumptions and must not be used interchangeably.

If \(M_{E_\mu}\ne M_{E_\tau}\), do not apply the summed formula as if both thresholds were at one common mass: match sequentially at the respective heavy thresholds and run between them.

### 2.3 What is and is not fixed by this choice

The matching-scale reference condition is now explicit, but the following are not yet calculated:

1. The RG evolution from an arbitrary UV scale \(\mu_0\) to \(\mu_M\):
   \[
   \lambda_{HS}^{>}(\mu_M)
   =\lambda_{HS}^{>}(\mu_0)
   +\int_{\ln\mu_0}^{\ln\mu_M}\beta_{HS}^{>}(\mu)\,d\ln\mu.
   \]
2. The EFT evolution from \(\mu_M\) to the electroweak scale:
   \[
   \lambda_{HS}^{<}(\mu_R)
   =\lambda_{HS}^{<}(\mu_M)
   +\int_{\ln\mu_M}^{\ln\mu_R}\beta_{HS}^{<}(\mu)\,d\ln\mu.
   \]
3. Other finite thresholds, nonzero kinetic mixing, the complete broken-phase scalar pole equation, and the constraints on the resulting scalar sector.

Consequently, \(\lambda_{HS}^{<}(\mu_M)=0\) is a defined matching benchmark, not yet proof that the physical Higgs–singlet mixing is negligible at \(p^2=m_h^2\).

## 3. Zero-momentum threshold, finite momentum, and EFT soft terms

### 3.1 Sign convention and no-double-counting rule

RC-001 §274 uses

\[
\Gamma_{\mathrm{inv}}(p^2)
=p^2\mathbf 1-\mathcal M_{\mathrm{loc}}^2
+\widehat\Pi_{\mathrm{soft}}^{\mathrm{ren}}(p^2).
\]

The effective-potential threshold gives the local Hessian contribution

\[
\delta(\mathcal M_{\mathrm{loc}}^2)_{hs}
=v_hv_s\,\Delta\lambda_{HS}^{E},
\]

while the source-convention hard self-energy satisfies

\[
\boxed{\Pi_{hs}^{F,\mathrm{hard}}(0)
=-v_hv_s\,\Delta\lambda_{HS}^{E}.}
\]

These signs are consistent because the local mass matrix enters the inverse propagator with a minus sign and \(\Pi\) enters with a plus sign.

**No-double-counting rule:** choose one representation.

- **Matched-EFT representation:** absorb \(\Delta\lambda_{HS}^{E}\) into \(\lambda_{HS}^{<}\) and \(\mathcal M_{\mathrm{loc}}^2\); do not add the same \(\Pi_{hs}^{F,\mathrm{hard}}(0)\) again.
- **Explicit-hard-self-energy representation:** keep the hard constant in \(\Pi^{\mathrm{hard}}(0)\); do not also include that same threshold in the local EFT portal parameter.

The same threshold cannot be counted once as a portal coefficient and again as a hard zero-momentum self-energy.

### 3.2 Finite momentum requires a common UV–EFT subtraction

For the fixed unbroken-phase Yukawa sector, RC-001 §248 records

\[
i\Gamma_{\mathrm{hard},\mu}^{(2)}
=\frac{i|C_{5,\mu}|^2}{16\pi^2}
\left[
(-\Delta_{\mathrm{IR}}+L_\mu-2)s+\frac{t}{6}
\right],
\qquad
L_\mu=\ln\frac{M_{E_\mu}^2}{\mu_R^2},
\]

and the corresponding bare EFT soft bubble

\[
i\Gamma_{\mathrm{EFT},\mu}^{\mathrm{bare}}
=\frac{i|C_{5,\mu}|^2s}{16\pi^2}
\left[
\Delta_{\mathrm{UV}}
-\ln\frac{-s-i0}{\mu_R^2}+2
\right].
\]

After the method-of-regions pole cancellation, their sum contains the finite nonlocal logarithm and local \(t/6\) term. The UV and EFT expressions must use the same external-state, momentum, IR, and renormalization conventions. The labels \(\Delta_{\mathrm{IR}}\) and \(\Delta_{\mathrm{UV}}\) must be kept distinct until the region subtraction is performed.

In the broken-phase two-point calculation, the EFT side must include all same-order soft insertions and counterterms required by the chosen operator basis—not merely the \(C_5C_5^\ast\) bubble. The RC-001 soft-topology census explicitly keeps the full soft-insertion closure as an acceptance gate. Therefore the zero-momentum portal relation is supported within its recorded scope; it does not close the complete finite-\(p^2\) pole/mixing calculation.

### 3.3 The \(4/3\) difference is not the B1/B3 issue

The source-aligned audit distinguishes the old on-shell four-point representative from the off-shell-completed coefficient set. With

\[
a_\ell=\frac{|y_\ell\lambda_\ell|^2}{16\pi^2M_{E_\ell}^2},
\qquad L_\ell=\ln\frac{M_{E_\ell}^2}{\mu_R^2},
\]

the old representative has

\[
c_{H,\ell}^{\mathrm{old}}=c_{S,\ell}^{\mathrm{old}}
=a_\ell\left(L_\ell-\frac{13}{6}\right),
\qquad
c_{D,\ell}^{\mathrm{old}}=\frac{a_\ell}{2}(L_\ell-2).
\]

The off-shell/EOM-completed representative in source §301 is

\[
c_{H,\ell}^{\mathrm{off/EOM}}
=c_{S,\ell}^{\mathrm{off/EOM}}
=a_\ell\left(L_\ell-\frac32\right),
\qquad
c_{D,\ell}^{\mathrm{off/EOM}}
=\frac{a_\ell}{2}\left(L_\ell-\frac23\right).
\]

Each of \(c_H,c_S,c_D\) shifts by \(+2a_\ell/3\), while the EOM-reduced combination

\[
c_D-\frac12(c_H+c_S)
\]

is invariant. Source §301 records the off-shell external-leg-square terms and the required EOM completion, and the corresponding algebra audits pass. This resolves the comparison between the **old on-shell representative** and the **off-shell-completed/two-point representative** in the stated operator basis.

It does **not** settle the historical B1/B3 path-kernel issue: that candidate kernel has not been mapped term by term to the full §248/§252 amplitude, soft subtraction, and common operator basis.

## 4. B1/B3 candidate kernel: item-by-item evidence comparison

### 4.1 Historical artifacts and exact scope

The candidate kernel is confined to the immutable historical v66 archive:

| Artifact | Blob SHA | What the recorded check establishes | What it does not establish |
|---|---|---|---|
| [`audit_pathwise_wick_kernel.py`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/artifacts/higgs-portal-v66-20261019/%E8%AE%A1%E7%AE%97%E8%84%9A%E6%9C%AC/audit_pathwise_wick_kernel.py) | `2a7ac2ba589fa99e982c63cb87bcf448c64c8047` | The 32 path records satisfy the script's declared B1/B3 sign-flip and unchanged-B2 algebra | Does not determine physical signs; omits the complete labeled external-leg sum, pathwise denominator integration, and EFT subtraction |
| [`verify_numerator_to_B_kernel.py`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/artifacts/higgs-portal-v66-20261019/%E8%AE%A1%E7%AE%97%E8%84%9A%E6%9C%AC/verify_numerator_to_B_kernel.py) | `304186f8bc70821254c550a88e376615385a0afd` | Reconstructs the stated \(f_{ij},g,d_\alpha\) polynomials and confirms the **old kernel's internal algebra** | Explicitly does not verify the overall Minkowski diagram sign |
| [`audit_minkowski_wick_signs.py`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/artifacts/higgs-portal-v66-20261019/%E8%AE%A1%E7%AE%97%E8%84%9A%E6%9C%AC/audit_minkowski_wick_signs.py) | `3063ed03c6de1aacd4094c9ef7a809dff0ce9886` | Applies \(J_{M,r}^{(n)}=i(-1)^{n+r}I_{E,r}^{(n)}\) under its stated metric/denominator convention | Takes the numerator coefficients as inputs; does not derive the complete model-specific amplitude |
| [`derive_consistent_minkowski_to_euclidean_B.py`](https://github.com/lm846802297-bit/high-energy-theory-research/blob/d6143c2aa15191ac8521e062d90860ba86713f00/artifacts/higgs-portal-v66-20261019/%E8%AE%A1%E7%AE%97%E8%84%9A%E6%9C%AC/derive_consistent_minkowski_to_euclidean_B.py) | `4f17b33d648190a8386cfa98dfc20de76b2de5b2` | Derives the candidate B kernel from the numerator decomposition and Wick rules explicitly listed in that script | Does not independently derive the input numerator, complete all external-leg cycles, or perform EFT subtraction |

The historical source states that the earlier Euclidean denominator \(K_E^2+\Delta_0+\delta\Delta\) was inconsistent with the original Minkowski denominator. Under the stated routing,

\[
D_M=K_M^2-\Delta_0+\delta\Delta,
\qquad K_M^2=-K_E^2,
\]

so

\[
D_M=-(K_E^2+\Delta_0-\delta\Delta).
\]

For an \(n=4\) denominator, the corrected Euclidean expansion has a \(+4\delta\Delta/(K_E^2+\Delta_0)^5\) linear term. Thus the \(d_\alpha\) convention must be fixed before comparing the B coefficients. A sign change in the denominator shift cannot be ignored, nor can one mechanically flip the entire kernel.

### 4.2 Algebraic comparison of the two recorded B definitions

If the **same** \(d_\alpha\) convention is held fixed, the historical definitions and the kernel derived under the §84 Minkowski/Wick assumptions are

\[
\begin{aligned}
B_{1}^{\mathrm{legacy}}&=H\left(\frac23g_\alpha-2d_\alpha\right),&
B_{1}^{\mathrm{Wick}}&=H\left(-\frac23g_\alpha+2d_\alpha\right),\
B_{2}^{\mathrm{legacy}}&=\frac13F_\alpha-\frac23S\,d_\alpha,&
B_{2}^{\mathrm{Wick}}&=\frac13F_\alpha-\frac23S\,d_\alpha,\
B_{3}^{\mathrm{legacy}}&=-\frac23M\,d_\alpha,&
B_{3}^{\mathrm{Wick}}&=+\frac23M\,d_\alpha.
\end{aligned}
\]

The algebraic relation is \(B_1^{\mathrm{Wick}}=-B_1^{\mathrm{legacy}}\), \(B_2^{\mathrm{Wick}}=B_2^{\mathrm{legacy}}\), and \(B_3^{\mathrm{Wick}}=-B_3^{\mathrm{legacy}}\) **under that fixed-\(d_\alpha\) comparison**. This is what the new exact symbolic check reproduces.

It is not a physical verdict. The \(d_\alpha\) coefficients are defined by the denominator shift; they must be regenerated from the same routed Minkowski denominators and then carried through the same Wick rotation as the numerator. The §84 script assumes its displayed numerator decomposition and does not establish that the coefficients \(F_\alpha,H,S,M\) are the exact result of the complete model-specific trace and vertex mapping.

### 4.3 Comparison against the source-aligned §248/§252 matching

| Matching layer | Historical B1/B3 path calculation | Source-aligned §248/§252 calculation | Reconciliation status |
|---|---|---|---|
| External fields | Broken-phase real \(h,s\) fields; mass-eigenstate Yukawa matrices | Unbroken-phase fixed complex legs \(H,S,H^\dagger,S^\dagger\), followed by a separate off-shell/EOM completion | **Not mapped term by term.** The real-field permutations and the complex-field projection need an explicit common-basis map |
| Internal states/topology | Two vertex-type patterns with 16 internal mass paths each; later six labeled external cycles | One connected UV 1PI box for the fixed complex external legs at the stated Yukawa order, plus its EFT \(C_5C_5^\ast\) bubble | Topological equivalence and multiplicities have not been proven in a shared labeled-amplitude ledger |
| Numerator | \(H,C_{ij},M\) and \(f,g,d_\alpha\) decomposition; selected-path and fixed-rational-point trace checks exist | Explicit fixed-sector numerator \(2M_E^2\,k\cdot(k-q)\) under the stated chiral routing, with hard expansion | The full mass-basis path sum has not been analytically reduced to the §248 numerator with all phases, conjugations, and external-leg permutations |
| Denominators | Path-specific \(\Delta_{0,\rho}(x)=\sum_i x_i m_{\mathrm{edge},i}^2\); the conditional simplex integrals of all 576 candidate-kernel rows are now evaluated and reproducible | Fixed-route UV denominator \(k^2(k-q)^2[(k-p_2)^2-M_E^2][(k+p_4)^2-M_E^2]\), expanded in the hard region | No exact route-by-route identity between the path denominators and the fixed-route hard expansion is recorded |
| Wick rotation and loop prefactor | Separate sign ledgers exist, but the candidate numerator-to-kernel chain retains assumptions; historical denominator-shift conventions differ | §248 gives the hard/soft local subtraction under its declared \(i\Gamma\), PV, and \(\overline{\mathrm{MS}}\) conventions | The common loop phase, fermion-loop sign, reversed cycles, and symmetry factors have not been closed in one calculation |
| UV/IR poles | The conditional candidate-kernel simplex integrals do not perform the complete EFT subtraction or counterterm closure | §248 explicitly separates the hard IR pole from the EFT soft UV pole and cancels them by regions | Cannot compare candidate finite integrals directly with the matched coefficient |
| Finite terms | The new analytic simplex integrals are still conditional candidate-kernel diagnostics; the common loop and graph factors are not closed and these are not matched coefficients | §248 gives the conditional hard local polynomial; §252 adds off-shell external-leg-square terms and EOM completion | No common-basis, same-IR-prescription finite-term equality has been demonstrated |
| Diagram-package validation | No complete current FeynArts/FeynCalc run is recorded | The source record explicitly says the FeynArts/FeynCalc scaffold remains unrun | **Open** |

### 4.4 What the existing checks do establish

1. The geometric \(f_{ij}\), \(g_\alpha\), and \(d_\alpha\) polynomial identities can be checked algebraically for the declared routing.
2. The historical B1/B3 script verifies the sign map it was written to test; it does not derive the physical sign from the complete model amplitude.
3. The Minkowski/Wick script checks termwise signs for its declared numerator decomposition; it does not independently derive that decomposition from every model-specific path.
4. The old pathwise integration records explicitly lack the full labeled external-leg sum, loop/symmetry-factor audit, EFT subtraction, counterterms, and final operator projection.
5. The current source-aligned two-point audit reproduces 15 exact symbolic/algebraic checks, including the leading portal sign and the historical \(4/3\) difference. Source §301 reconciles that \(4/3\) difference with the off-shell/EOM completion. This does not supply the missing B1/B3-to-§248 map.

### 4.5 Decision on B1/B3

**Status: algebraic B1/B3 signs are resolved conditionally under the declared trace/Wick convention; the physical finite-mixing Wilson coefficient remains unresolved. Do not promote either real-scalar candidate kernel to the final coefficient.**

The leading unbroken fixed-Yukawa coefficient is supported by the source-aligned §248 hard-region calculation and the corresponding SFT-01 soft subtraction. The real-scalar B1/B3 ledger is a conditional kernel diagnostic, not an independent full finite-mixing Wilson coefficient. The direct trace and pathwise convention audits establish the algebraic kernel signs, while the finite-mixing complex path sum remains a d=4 diagnostic until its regions expansion and common diagrammatic multiplicity are closed. The evidence does not justify calling the historical candidate physically wrong or declaring the complete finite-mixing coefficient superseded by a term-by-term identity.

Required closure steps:

1. **Completed at the trace/convention level:** the exact source \(G_h,G_s\) matrices, signed-light-mass rephasing, chiral trace weights, and parity-odd term have been checked pathwise. The interaction-basis complex projection independently identifies the surviving orientations in the unbroken limit.
2. **Completed conditionally at the kernel level:** the generic trace/Wick derivation and route-dependent \(f_{ij},g_\alpha,d_\alpha\) now define the B1/B2/B3 kernels in one convention. The fixed complex amplitude has its own B2-only kernel; it must not be identified with the unrestricted real-scalar six-cycle sum.
3. **Still open at the physical-amplitude level:** reconcile the source-aligned hard-region result with the finite-mixing complex path sum, including the common diagrammatic \(i\)/closed-loop factor and determinant-log/graph multiplicity. The 576 real-scalar candidate integrals are diagnostics, not a single physical complex amplitude.
4. Map the complete sum to the same complex external states and momentum basis used in §248/§252, including the off-shell \(\Sigma=\sum_i p_i^2\) terms and EOM-generated potential/source companions.
5. Keep the source-aligned SFT-01 soft bubble and its pole/counterterm check as closed for the leading fixed Yukawa sector. Complete the remaining finite-mixing and model-sector EFT soft amplitudes, contact terms, and counterterms in the same IR and renormalization prescription; compare UV and IR poles and finite local terms separately.
6. Only after the analytic map and factor ledger close should the corresponding FeynArts/FeynCalc calculation be executed and archived. An algebra-only script is not a substitute for diagram-level validation.

## 5. Reproducible algebra check

The companion script is [`calculations/RC-001-portal-boundary-b1b3-reconciliation.py`](../calculations/RC-001-portal-boundary-b1b3-reconciliation.py). Its captured output is [`validation/RC-001-portal-boundary-b1b3-reconciliation.txt`](../validation/RC-001-portal-boundary-b1b3-reconciliation.txt).

The portal/B-kernel reconciliation script runs 14 exact symbolic checks covering:

- the portal matching relation and the two distinct boundary choices;
- the potential-Hessian/1PI sign relation;
- the §301 \(2a_\ell/3\) EOM completion and invariant reduced derivative combination;
- the algebraic B1/B3 sign map at fixed \(d_\alpha\), with B2 unchanged;
- the corrected Minkowski-to-Euclidean denominator shift and its \(n=4\) linear expansion;
- the fixed-sector hard/soft pole-residue and finite-log bookkeeping.

**Scope limitation:** the new simplex-integration script analytically integrates the 576 declared candidate kernels, verifies 48 equal-mass moments, compares four non-degenerate moments with direct quadrature, and passes 288 numerical reverse-cycle comparisons. Neither script independently derives the full physical numerator-to-kernel map, closes the common loop/sign/symmetry factors, completes all EFT soft insertions/counterterms, performs the full UV–EFT subtraction, or runs FeynArts/FeynCalc.


## 6. Independent trace, six-cycle, and normalization audit (2026-10-27)

### 6.1 New executable evidence

The following new audit artifacts are on this PR branch:

- [Generic trace, six-cycle routing, and normalization script](../calculations/RC-001-six-cycle-trace-normalization-audit.py)
- [Trace/normalization execution log](../validation/RC-001-six-cycle-trace-normalization-audit.txt)
- [Symbolic six-cycle O(p^2) candidate-kernel ledger script](../calculations/RC-001-six-cycle-oq2-candidate-kernel-ledger.py)
- [O(p^2) candidate-kernel execution log](../validation/RC-001-six-cycle-oq2-candidate-kernel-ledger.txt)
- [Fixed-sector hard/soft pole ledger script](../calculations/RC-001-fixed-sector-hard-soft-pole-ledger.py)
- [Fixed-sector hard/soft pole ledger output](../validation/RC-001-fixed-sector-hard-soft-pole-ledger.txt)
- [C5 C5* soft-bubble trace audit script](../calculations/RC-001-C5-soft-bubble-trace-audit.py)
- [C5 C5* soft-bubble trace audit output](../validation/RC-001-C5-soft-bubble-trace-audit.txt)

The trace audit uses the model matrices

\[
Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},
\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix},
\]

and the declared real-Yukawa vertex convention \(V_{ij}=Y_{ij}P_R+Y_{ji}P_L\). It tests all six labeled cycles and all 16 internal-state paths at exact rational routed Minkowski momenta, comparing an explicit 4-by-4 Dirac trace with the projector decomposition. The test passes for 96/96 cycle-path cases.

The second script additionally derives the generic trace identity symbolically for arbitrary \(u_i,v_i,m_i,k_i\), then constructs the model-specific \(H_\rho,C_{ij}^{(\rho)},S_\rho,M_\rho\), route-specific \(f_{ij,\alpha},g_\alpha,d_\alpha,\Delta_{0,\rho}\), and conditional \(B^{(1,2,3)}\) coefficients in the common external-invariant basis. It emits 576 rows: 6 labeled cycles × 16 internal paths × 6 invariants.

### 6.1.1 Positive-light-mass versus signed-light-mass convention

There are two displayed vertex-matrix conventions in the frozen v153 source, and they must not be mixed without the corresponding chiral rephasing.

The Eq. (13) matrices used by the six-cycle candidate kernels are

\[
Y_h=a\begin{pmatrix}c_Ls_R&c_Lc_R\\s_Ls_R&s_Lc_R\end{pmatrix},
\qquad
Y_s=b\begin{pmatrix}s_Lc_R&-s_Ls_R\\-c_Lc_R&c_Ls_R\end{pmatrix}.
\]

The real-rotation, signed-light-mass convention in v153 §276 instead gives

\[
G_h=a\begin{pmatrix}-c_Ls_R&c_Lc_R\\-s_Ls_R&s_Lc_R\end{pmatrix},
\qquad
G_s=b\begin{pmatrix}-s_Lc_R&-s_Ls_R\\c_Lc_R&c_Ls_R\end{pmatrix}.
\]

They obey the exact matrix identities

\[
G_h=Y_hD,\qquad G_s=Y_sD,\qquad D=\operatorname{diag}(-1,1).
\]

This is the right-handed light-state rephasing associated with switching between the positive-light-mass convention and the signed-light-mass convention. The new trace/normalization script checks these identities symbolically.

The six-cycle candidate ledger uses the Eq. (13) matrices and positive mass symbols in its propagator denominators. The §276 two-point formula keeps the signed light eigenmass in chirality-flip numerators. A comparison between these routes is valid only after the vertex rephasing and the sign of the mass-flip terms are transformed consistently. The matrix identity alone does not prove the full loop amplitudes equal; it removes an avoidable convention ambiguity from the next matching step.

### 6.2 Six labeled cycles and reverse-loop counting

Fixing \(h_1\) as the representative start point leaves

\[
\frac{4!}{4}=6
\]

inequivalent cyclic orderings. The three reverse pairs are already included among these six orderings. The path-level audit checks 48 reverse path pairs, and the O(p²) candidate-kernel audit checks 1,152 exact coefficient comparisons after the path map, Feynman-parameter permutation, and simplex constraint.

This supports the following bookkeeping rules:

- count each of the six labeled cycles once;
- do not sum all six cycles and then multiply by an extra factor of two for loop reversal;
- retain the 16 path-dependent mass denominators until the parameter integrations or a proven symmetry reduction justify combining them.

The reverse-kernel checks prove consistency of the generated candidate kernels under the declared mapping. They do not independently establish the physical global loop sign.

### 6.3 \(\Gamma(4)\), simplex normalization, and the fermion-loop sign

The four-propagator Feynman-parameter identity contributes

\[
\frac{\Gamma(4)}{\prod_{i=1}^4\Gamma(1)}=\Gamma(4)=6,
\]

while the standard four-parameter simplex has volume \(1/6\). Their product is one. Therefore the factor of six must be included exactly once: if the integral is written with the explicit Feynman-parameter prefactor, do not also normalize the simplex average by six a second time.

The audit also checks the five convergent Euclidean scalar-integral factors used in the candidate-kernel reduction:

\[
I_0^{(4)}=\frac{1}{6\Delta^2},\quad
I_1^{(4)}=\frac{1}{3\Delta},\quad
I_2^{(5)}=\frac{1}{4\Delta},\quad
I_1^{(5)}=\frac{1}{12\Delta^2},\quad
I_0^{(5)}=\frac{1}{12\Delta^3},
\]

each in units of \(1/(16\pi^2)\).

For the effective-action convention \(\Gamma_f=-i\,\mathrm{Tr}\ln(1+X)\), the fourth-order determinant-log coefficient is \(+i/4\). The closed-fermion-loop factor \(-1\) in diagrammatic Feynman rules is a separate bookkeeping item. The audit records both conventions but does not claim to have reconciled them with all four vertex factors, propagator factors, loop integration, and the final common Minkowski/Wick phase. The overall diagrammatic \(i\) and sign therefore remain open.

### 6.4 What has and has not been established

| Layer | Status | Evidence boundary |
|---|---|---|
| Generic chiral Dirac trace | **Verified symbolically** | Exact identity for arbitrary chiral coefficients, masses, and four independent Minkowski momenta |
| All six cycles × 16 paths | **Verified at numerator/weight level** | 96 exact rational-point direct-trace comparisons; model-specific weights are assembled symbolically |
| Routed \(O(p^2)\) real-scalar candidate coefficients | **Generated and cross-checked; kernel signs calibrated** | 576 symbolic rows and 1,152/1,152 reverse-cycle checks; B2 is source-calibrated and B1/B3 signs follow the declared Wick convention. These rows are not the fixed complex external amplitude without field-orientation projection |
| \(\Gamma(4)\), simplex volume, five Euclidean integral factors | **Verified algebraically** | Exact Gamma-function identities |
| Determinant-log \(+i/4\) and diagrammatic \(-1\) | **Partially reconciled** | The fixed-sector one-cycle box reproduces §248 after explicit vertex/propagator/closed-loop factors; determinant-log-to-diagram multiplicity and full six-cycle phase/factors remain open |
| Path-dependent simplex integrals | **Conditionally completed** | All 576 candidate B-kernel rows have analytic simplex integrals and 288 numerical reverse-cycle checks; this is not a physical Wilson coefficient because the global sign/factors and UV–EFT subtraction remain open |
| Complex external-field projection | **Verified in the unbroken zero-mixing limit** | 14 exact checks select \(H,S,S^\dagger,H^\dagger\) in the muon \(s\) channel and \(H,S^\dagger,S,H^\dagger\) in the tau \(u\) channel; the fixed-chirality trace is \(2m_1m_3 k_2\!\cdot k_4\). Finite-mixing allowed-path sums remain open |
| EFT soft diagrams and counterterms | **Partially closed by sector** | The fixed-sector C5 C5* scalar bubble has a separate 10-check trace/sign/pole audit; SFT-02/03 are classified as reducible/scaleless in the unbroken massless scheme. The full common-basis counterterm ledger, current/source sectors, and independent diagram-package validation remain open |
| Final UV–EFT Wilson coefficient | **Not established** | No final coefficient or exclusion claim is promoted |

The current O(p²) CSV generated by the optimized script has SHA-256 `01c95525e2e3c1b9998192e0347c82f4bd8bfbb85f96e2cefe09c0ec6de55f8e` and 1,632,774 bytes. It is not committed separately; the script regenerates it. The 990,656-byte CSV is from the prior source revision and is retained only as historical evidence.

### 6.5 Trace-audit provenance correction and byte-aligned rerun

The earlier trace-audit log recorded a source SHA-256 that did not match the current script content. This has now been corrected by rerunning a byte-aligned local copy of the current GitHub source:

- Script blob SHA: \`22b47f7b95d68b4e86735e8e1c0e3abb63521f43\`.
- SHA-256 of the fetched UTF-8/LF source: \`762527917e0021cca7753b27b4bb9943eb0316dc5a8d69f8baf2dd1d8335343b\`.
- Exit code: 0; 96/96 explicit trace/decomposition comparisons and 48/48 reverse path-weight/mass checks passed.
- \(\Gamma(4)=6\), simplex volume \(1/6\), the five Euclidean integral factors, and the determinant-log \(+i/4\) coefficient passed exact symbolic checks.

The refreshed [validation log](../validation/RC-001-six-cycle-trace-normalization-audit.txt) pairs this source digest with the captured stdout. A clean Git checkout was not available because the execution container could not resolve \`github.com\`; the run was instead made from a local copy whose SHA-256 matched the fetched GitHub content byte-for-byte. This is source-aligned execution evidence, but not a clean-checkout claim.

The separate [simplex-integration audit](../validation/RC-001-six-cycle-simplex-integration.txt) has also been rerun against its current source. It integrates all 576 conditional candidate kernels and passes 288/288 numerical reverse-cycle comparisons. These are conditional B-kernel results: the determinant-log coefficient and the diagrammatic closed-fermion-loop factor \(-1\) are still recorded separately, and the complete common Minkowski/Wick phase, graph/symmetry factors, EFT soft-graph/counterterm closure, and final finite UV–EFT coefficient remain unresolved.


## 7. EFT soft terms, counterterms, and UV–EFT subtraction: remaining closure gate

The repository already contains a source-aligned two-point audit ([script](../calculations/RC-001-uv-eft-two-point-difference.py), [captured result](../validation/RC-001-uv-eft-two-point-difference.txt)) with 15 exact symbolic/algebraic checks. Those checks cover the specified \(h\)-\(s\) two-point kernel, its EFT bubble/contact pole bookkeeping, the local counterterm cancellation within that kernel, and the finite \(p^2=0\) hard-minus-soft expression.

The separate soft-topology census ([script](../calculations/RC-001-eft-soft-topology-census.py), [research note](RC-001-eft-soft-topology-census.md), [captured result](../validation/RC-001-eft-soft-topology-census.txt)) explicitly says that the \(C_5C_5^\ast\) bubble has an existing soft integral but still needs an independent graph-level check. The census is a structural/power-counting audit, not a complete diagrammatic evaluation.

The new [fixed-sector hard/soft pole ledger](../calculations/RC-001-fixed-sector-hard-soft-pole-ledger.py) passes 12 exact symbolic checks. It keeps the hard-region IR pole and bare EFT soft-loop UV pole separately labeled, verifies their opposite residues in the method-of-regions sum, checks the local counterterm against the soft UV pole, and records the finite hard polynomial \((L-2)s+t/6\) in the source normalization. It also repeats the existing two-point bubble/contact and derivative-counterterm pole identities. The six-cycle candidate kernels have now been analytically integrated over the four-parameter simplex, but the complete same-order EFT soft-graph set, common-basis counterterms, and physical overall sign/factor closure remain open.

The new [C5 C5* soft-bubble trace audit](../calculations/RC-001-C5-soft-bubble-trace-audit.py) passes 10 exact symbolic checks. It independently computes the massless chiral trace, reduces the numerator to the scalar B0 bubble using scaleless-tadpole vanishing, multiplies the two vertices, two propagators, and closed-loop sign, and checks the soft UV counterterm and §248 hard/soft pole cancellation. This validates the algebra of the specified SFT-01 bubble under the recorded B0 convention; it does not independently generate the full EFT graph set or integrate the six-cycle UV candidate kernels.

### 7.1 Soft-graph coverage matrix for the target scalar 1PI amplitude

The scope must be fixed before calling the soft sector “complete.” For the target unbroken-phase four-scalar amplitude with external \(H,S,H^\dagger,S^\dagger\), at strict \(O(M_E^{-2})\) and in the fixed \(|y_\ell|^2|\lambda_\ell|^2\) sector, the source-aligned census gives this status:

| Candidate family | Target-amplitude role | Pole / finite-part evidence | Status for this matching task |
|---|---|---|---|
| SFT-01: \(C_{5,\ell}C_{5,\ell}^\ast\) light-fermion bubble | Direct four-scalar 1PI soft graph | The fixed §248 routing has a massless chiral trace; its EFT UV pole cancels the hard-region IR pole after regions identification. The fixed-routing hard local polynomial is \((L_\ell-2)s+t/6\), with the soft nonlocal logarithm retained before local matching. | **Analytically checked for the recorded routing.** Still needs flavor-resolved \(s/u\) routing and the full UV cycle-sum comparison. |
| SFT-02/03: \(Q_{LD}/Q_{RD}\) plus scalar quartic with a fermion tadpole | Scalar-line-reducible, not a local 1PI four-scalar contribution | The unbroken massless fermion tadpole is scaleless in dimensional regularization. | Excluded from this local 1PI coefficient under the stated scheme; reconsider if masses/VEVs or a different matching object are retained. |
| Pure-light scalar/gauge loops with no heavy-dependent insertion | Common UV and EFT contributions | Cancel in the hard matching difference only with identical light-field content, parameters, IR regulator, gauge convention, and external-state normalization. | Cancellation rule stated; not a substitute for checking any heavy-dependent insertion. |
| SFT-07–10: gauge-current exchanges | Reducible connected-amplitude contributions | They belong to the current/source ledger and depend on the declared gauge/kinetic-mixing inputs; they are not additional local 1PI scalar vertices. | Not added to the local scalar coefficient. Required if claiming the full connected amplitude/current vector. |
| SFT-04–06, SFT-11–13 | Dimension-eight or \(O(M_E^{-4})\) insertions | Explicit heavy-mass power counting places them beyond strict dimension six. | Excluded here; must be included in a separate dimension-eight closure. |
| SFT-14–22 | Two-fermion/two-scalar and four-fermion amplitudes | Several analytic hard/soft kernels and pole cancellations are recorded in the 41-check soft-loop audit; basis projection and/or full counterterm closure remains incomplete. | Not extra four-scalar 1PI graphs, but required for a complete dimension-six fermionic Wilson vector. |
| SFT-23–26 | \(C_5\) and gauge corrections to \(Q_{LD}/Q_{RD}\) | Gauge-covariant vertex, external-leg, contact, and counterterm sets are not fully evaluated at diagram level. | Open for full dimension-five/dimension-six closure; do not fold into the scalar-only hard coefficient without an explicit connected-amplitude matching definition. |

**Target-sector subtraction that is supported:** for the single fixed §248 channel, the hard-region IR residue is \(-s\), the bare EFT soft UV residue is \(+s\), and the local EFT counterterm cancels the EFT UV pole. After the method-of-regions identification \(\Delta_{\mathrm{IR}}=\Delta_{\mathrm{UV}}\), the region sum has no pole and leaves the finite nonlocal logarithm plus the local \(t/6\) term; the local hard polynomial is \((L_\ell-2)s+t/6\).

**What is not yet supported:** the six labeled candidate UV kernels have been integrated conditionally over their path-dependent four-parameter simplex, but their flavor-resolved \(\mu/\tau\) \(s/u\) routing has not yet been combined with the source-matched UV amplitude and the complete EFT soft/counterterm set in one common amplitude ledger. The determinant-log / diagrammatic fermion-loop sign, common Minkowski/Wick phase, graph/symmetry factors, UV/IR pole comparison for the full amplitude, and final finite local coefficient remain open. Therefore the conditional simplex integration cannot yet be promoted to a complete six-cycle UV–EFT matching result.

### 7.2 EFT soft-graph closure in the fixed mixed-Yukawa sector

The EFT soft sector can be classified more sharply when the matching object is restricted to the source-aligned unbroken-phase 1PI amplitude with external \(H,S,H^\dagger,S^\dagger\), at strict \(O(M_E^{-2})\), and in the coupling sector \(|y_\ell|^2|\lambda_\ell|^2\), with the light fields massless in dimensional regularization.

| EFT contribution | Status in this restricted sector | Reason |
|---|---|---|
| One \(C_{5,\ell}\) and one \(C_{5,\ell}^\ast\) insertion (SFT-01) | **Required and evaluated** | The two insertions supply the four external scalar legs; the massless chiral-fermion bubble is the direct 1PI soft graph. Its numerator reduces to the massless \(B_0\) bubble after scaleless tadpoles vanish. |
| Local \(\lambda_{HS}\) counterterm | **Required and pole-checked** | The EFT soft UV residue is \(+s\); the local counterterm contributes \(-s\). The hard-region IR residue is separately \(-s\), and the hard/soft region sum is finite after \(\Delta_{\rm IR}=\Delta_{\rm UV}\). |
| One \(Q_{LD}\) or \(Q_{RD}\) insertion plus a scalar quartic (SFT-02/03) | **Not an extra local 1PI coefficient** | The candidate is scalar-line reducible and contains a scaleless one-propagator fermion tadpole in the stated unbroken massless scheme. Its coupling order is also distinct from the fixed \(|y_\ell|^2|\lambda_\ell|^2\) box sector. |
| Pure-light loops with no heavy-dependent EFT insertion | **Cancel in the matching difference** | They are common to UV and EFT only when the light field content, parameters, IR regulator, gauge convention and external-state normalization are identical. |
| Gauge-current exchange and gauge corrections | **Outside this restricted coupling/topology sector** | These are separate current/source or higher-order coupling sectors; reducible gauge exchange is not an additional local scalar 1PI vertex. |
| One-loop correction to \(C_5\) inserted into the \(C_5C_5^\ast\) bubble | **Higher loop order** | It would be a two-loop contribution to this four-scalar amplitude, not part of the one-loop dimension-six matching coefficient. |

**Restricted-sector conclusion:** the EFT soft graph and its local pole counterterm are algebraically closed for the single source-aligned SFT-01 matching channel. The fixed-route hard/soft ledger therefore supports the finite local polynomial \((L_\ell-2)s+t/6\) in the declared normalization for that channel.

This is not a claim that the complete model's EFT soft sector or Wilson vector is closed. In particular, it does **not** prove that the six-cycle real-scalar candidate kernels have been mapped to the same complex external-state amplitude, with the same UV numerator, \(s/u\) routing, common \(i\)-factor, graph multiplicity, and \(d=4-2\epsilon\) tensor terms. That UV-to-source matching is the next blocking calculation.

Accordingly, the fourth requested stage is **not yet complete**. Before promoting any B1/B3 kernel to a physical Wilson coefficient, the remaining work is:

1. derive the complete set of EFT soft graphs and same-order insertions for the selected four-scalar 1PI amplitude from the operator basis, rather than relying only on a topology classification;
2. calculate each graph in the same IR prescription and renormalization scheme as the UV amplitude;
3. include the required local counterterms and keep UV and IR poles labeled separately until subtraction;
4. compare UV and EFT pole residues term by term, then compare the finite local \(O(p^2)\) coefficients in the same external-invariant and operator basis;
5. complete the loop/symmetry-factor and common \(i\)-sign reconciliation, and independently verify the result with FeynArts/FeynCalc or an equivalent diagram-level calculation.

Until those gates pass, the B1/B3 result remains a **conditional candidate-kernel result**, not the final physical matching coefficient. No manuscript result, formal response, or exclusion statement should be changed on the basis of this audit.

## 8. Archiving decision and change control

- Keep the v66 archive unchanged as historical evidence.
- Keep the B1/B3 candidate scripts in the research repository only; **do not copy them into `axial-vector-review-response`** while their physical sign and matching status remain unresolved.
- The existing [review-response PR #7](https://github.com/lm846802297-bit/axial-vector-review-response/pull/7) remains Draft and unmerged. Its evidence note is not a substitute for this calculation ledger.
- Do not change the formal response letter, manuscript PDF, v5.6 task checkboxes, or final physical conclusions on the basis of this audit.
- This ledger and its algebra check are a dated supplement on a separate research branch. They do not replace the frozen v153 baseline or assert complete model-level Wilson-vector closure.


## 9. New checked subtasks — 2026-10-27

### 9.1 Tree-level dimension-five input

The standalone record [RC-001-tree-level-C5-matching-derivation.md](RC-001-tree-level-C5-matching-derivation.md) now derives the operator coefficient from the heavy-block Schur complement and cross-checks the propagator expansion. With
\[
\mathcal O_{5,\ell}=S_\ell\bar L_\ell H\ell_R,\qquad
\mathcal L_{\rm EFT}^{(5)}\supset-C_{5,\ell}\mathcal O_{5,\ell}+\mathrm{h.c.},
\]
the mass-matrix entry gives
\[
C_{5,\ell}^{(0)}=-\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.
\]
The companion exact SymPy script passes 10 symbolic checks. This closes the tree-level coefficient and sign in that declared convention only; it does not address one-loop corrections to C5 or any B1/B3 sign.

### 9.2 Conditional pathwise simplex integration

The new script [RC-001-six-cycle-simplex-integration.py](../calculations/RC-001-six-cycle-simplex-integration.py) evaluates the candidate kernel
\[
6\int_{\sum_i x_i=1,\;x_i\ge0}d^3x\left[
\frac{B_1}{\Delta_0}
+\frac{B_2}{\Delta_0^2}
+\frac{B_3}{\Delta_0^3}
\right],\qquad
\Delta_0=\sum_i x_i m_i^2,
\]
for all six labeled external cycles, 16 internal mass paths, and six external invariants. The integration reduces each monomial to a Beta-weighted Gauss hypergeometric function. The factor \(\Gamma(4)=6\) is included exactly once.

The refreshed validation record [RC-001-six-cycle-simplex-integration.txt](../validation/RC-001-six-cycle-simplex-integration.txt) records 48/48 exact equal-mass moment checks, 4/4 comparisons against direct non-degenerate quadrature, 576 analytically integrated conditional kernels, and 288/288 numerical reverse-cycle comparisons (maximum absolute difference \(1.11487\times10^{-41}\)). The current byte-aligned run took 30.26 s. Its generated 1,724,229-byte CSV has SHA-256 \`410fc882b73d20d70f66eda588296e5e5818131c0667579cb624e8d6a594028f\`; it is reproducible and not committed. The current script source SHA-256 is \`46c71cdeb105d2b681b53752887a7528a4a032aeb6db346051cb00ec75b6b31e\`.

**Interpretation boundary:** these are analytic integrals of the current candidate B-kernel definitions, not final hard Wilson coefficients. The common \(1/(16\pi^2)\), global Minkowski/Wick phase, closed-fermion-loop sign, graph/symmetry factors, complete same-order EFT soft graphs and counterterms, and the full UV–EFT subtraction are not included. The B1/B3 physical-sign question therefore remains unresolved.

**Massless-light-state caveat:** the current simplex integration is performed in exactly \(d=4\) with the two internal masses treated as nonzero symbolic parameters. It does not by itself justify taking the light-state mass to zero in every path. Mixed heavy/light paths can develop endpoint singularities in that limit; the corresponding hard-region IR poles and EFT soft-region UV poles must be distinguished in \(d=4-2\epsilon\). The four-dimensional hypergeometric expressions are therefore conditional finite-mass integrals, not a substitute for a dimensionally regulated method-of-regions expansion. The next matching calculation must keep the light-mass/IR regulator consistent on both sides and retain the \(O(\epsilon)\) numerator and tensor terms that can multiply poles and shift finite constants.

The next blocking step is not another simplex normalization check. The fixed-sector SFT-01 soft bubble and its pole cancellation are algebraically audited, while the topology census classifies the reducible/scaleless SFT-02/03 candidates. The remaining work is to derive the physical UV numerator and denominator expansion from the same labeled diagrams, close the common sign/factor ledger, and perform the complete same-scheme UV–EFT subtraction with the required operator/counterterm projection.


### 9.3 One-cycle source-aligned numerator and B2 calibration

The new script [RC-001-one-cycle-fixed-sector-calibration.py](../calculations/RC-001-one-cycle-fixed-sector-calibration.py) independently derives the zero-mixing/unbroken limit of the labeled cycle \(h_1\to s_1\to s_2\to h_2\), exhausting all 16 internal-state paths. Only path \((0,1,0,1)\), with ordered propagator masses \((M_E,0,M_E,0)\), survives. Its exact Dirac trace is
\[
\operatorname{tr}[\cdots]
=2\,y^2\lambda^2M_E^2\,k_2\!\cdot k_4
=2\,y^2\lambda^2M_E^2\,k\!\cdot(k-q).
\]

With the external relabeling \(q_2=p_4,\ q_3=p_2,\ q=-(p_1+p_4)=p_2+p_3\), the propagator denominators become
\[
k^2(k-q)^2\big[(k-p_2)^2-M_E^2\big]
\big[(k+p_4)^2-M_E^2\big],
\]
which is the fixed-sector UV denominator recorded in §248. This establishes an integrand-level numerator/denominator match for this one path in the zero-mixing limit, not a complete six-cycle amplitude identity.

For the Feynman-parameter shift \(K=k+R\), define
\[
d=\sum_i x_i r_i^2-R^2,\qquad
\Delta_0=M_E^2(x_1+x_3),\qquad
f=R\cdot(R+q).
\]
Then the shifted denominator is \(K_M^2-\Delta_0+d\), so after Wick rotation the Euclidean denominator is \(K_E^2+\Delta_0-d\) and its fourth-power expansion has the \(+4d\) term. The numerator becomes \(2C[K_M^2+f]\) plus a term odd in \(K\), with \(C=y^2\lambda^2M_E^2\). Using
\[
I_0^{(4)}=\frac{1}{16\pi^2}\frac{1}{6\Delta_0^2},
\qquad
I_1^{(5)}=\frac{1}{16\pi^2}\frac{1}{12\Delta_0^2},
\]
the \(O(p^2)\) kernel is
\[
\frac{2Cf}{6\Delta_0^2}
-\frac{8Cd}{12\Delta_0^2}
=\frac{C(f-2d)}{3\Delta_0^2},
\]
i.e. \(B_2=(F-2Sd)/3\) with \(F=Cf\) and \(S=C\). The \(\Gamma(4)=6\) Feynman-parameter prefactor is included once; the simplex volume is \(1/6\).

The companion validation record [RC-001-one-cycle-fixed-sector-calibration.txt](../validation/RC-001-one-cycle-fixed-sector-calibration.txt) records **22 exact symbolic checks**, including the full 16-path limit, numerator, denominator routing, denominator-shift sign, B2 factor, and simplex normalization.

**Boundary:** this path has \(H=0\) and the four-mass term \(M=0\), so \(B_1=B_3=0\). It therefore validates neither historical B1/B3 sign choice. It also omits the global diagrammatic \(i\), closed-fermion-loop sign, and physical graph multiplicity. The hard-region coefficient and EFT soft subtraction are referenced from the source-aligned §248 ledger but are not independently recalculated by this script.


### 9.4 One-cycle hard-region integral and overall diagrammatic sign

The new script [RC-001-one-cycle-hard-region-match.py](../calculations/RC-001-one-cycle-hard-region-match.py) and validation record [RC-001-one-cycle-hard-region-match.txt](../validation/RC-001-one-cycle-hard-region-match.txt) independently expand the source-aligned fixed-sector box through \(O(p^2)\) in \(d=4-2\epsilon\). They start from the numerator and denominator established in §9.3, expand both light and heavy propagators in the hard region, reduce tensor integrals in \(d\) dimensions, and evaluate the three scalar masters \(J_{22},J_{13},J_{04}\) with the declared \(\overline{\mathrm{MS}}\) scale factor.

Before the closed-fermion-loop sign, the hard coefficients are
\[
\frac{i|y\lambda|^2}{16\pi^2M_E^2}
\left[
\left(\frac1\epsilon+2-L\right)s-\frac{t}{6}
\right],
\qquad L=\ln\frac{M_E^2}{\mu_R^2}.
\]
The four Yukawa vertices contribute \((-i)^4=+1\), the four fermion propagators contribute \(i^4=+1\), and the closed fermion loop contributes \(-1\). Including this factor gives
\[
\boxed{
i\Gamma_{\mathrm{hard}}^{(2)}
=\frac{i|C_5|^2}{16\pi^2}
\left[(-\Delta_{\mathrm{IR}}+L-2)s+\frac{t}{6}\right],
}
\]
where \(\Delta_{\mathrm{IR}}=1/\epsilon_{\mathrm{IR}}\) in the stated scale convention after the standard \(\overline{\mathrm{MS}}\) constants are absorbed. This reproduces the fixed-sector hard polynomial recorded in §248, including the relative \(s\)- and \(t\)-channel signs and the finite \(t/6\) coefficient.

The script passes **14 exact symbolic checks**, including the \(O(p^2)\) denominator expansion, \(d\)-dimensional tensor reduction, master-integral gamma functions, epsilon expansion, diagrammatic prefactor, and both source coefficients.

**Scope boundary:** this closes the hard-region integral and common diagrammatic prefactor for the one source-aligned box in the unbroken, on-shell massless-external-leg limit. It does not close the complete mixed-mass six-cycle sum, flavor-resolved \(\mu/\tau\) \(s/u\) routing, determinant-log-to-diagram multiplicity, or the full EFT soft/counterterm subtraction. Since \(B_1=B_3=0\) in the calibration path, the historical \(B_1/B_3\) sign discrepancy remains unresolved.


### 9.5 Algebraic resolution of the B1/B3 Wick-sign discrepancy

The new [RC-001-B1-B3-Wick-sign-check.py](../calculations/RC-001-B1-B3-Wick-sign-check.py) and [captured validation record](../validation/RC-001-B1-B3-Wick-sign-check.txt) pass **18 exact symbolic checks**. In addition to verifying the Euclidean loop-integral factors, the script checks that the ledger's \(g_\alpha\) expression is the angular-averaged \(K_M^2\) coefficient of the four-slash trace polynomial \(G\) for all six labeled cycles.

With the declared denominator shift
\[
K_M^2-\Delta_0+d
\quad\longrightarrow\quad
-\big(K_E^2+\Delta_0-d\big),
\]
the denominator expansion contributes \(+4d\). Wick rotation gives \(K_M^2\to-K_E^2\) but \(K_M^4\to K_E^4\). The \(2HG\) numerator therefore contributes
\[
-2H g_\alpha I_1^{(4)}+8H d_\alpha I_2^{(5)}
=\frac{1}{16\pi^2\Delta_0}
H\left(-\frac{2}{3}g_\alpha+2d_\alpha\right),
\]
using \(I_1^{(4)}=(16\pi^2\,3\Delta_0)^{-1}\) and \(I_2^{(5)}=(16\pi^2\,4\Delta_0)^{-1}\). The constant \(2M\) numerator contributes
\[
2M\,(4d_\alpha)I_0^{(5)}
=\frac{1}{16\pi^2\Delta_0^3}\frac{2}{3}M d_\alpha,
\]
using \(I_0^{(5)}=(16\pi^2\,12\Delta_0^3)^{-1}\). Hence the Wick-consistent kernel signs are
\[
\boxed{B_1=H\left(-\frac{2}{3}g_\alpha+2d_\alpha\right),\qquad
B_3=+\frac{2}{3}M d_\alpha,}
\]
while the independently calibrated \(B_2=(F_\alpha-2S d_\alpha)/3\) remains unchanged.

These are exactly opposite to the historical formulas \(B_1=H(2g_\alpha/3-2d_\alpha)\) and \(B_3=-2M d_\alpha/3\). Under the current trace decomposition and \(d=\sum_i x_i r_i^2-R^2\) convention, the historical signs are incompatible with the Wick rotation and loop-integral factors.

**Interpretation boundary:** this resolves the algebraic B1/B3 sign choice in the candidate kernel. It does not by itself establish the final physical Wilson coefficient: the determinant-log-to-diagram multiplicity, complete mixed-mass path sum, flavor-resolved \(s/u\) routing, and same-scheme UV–EFT subtraction remain open.

An independent second implementation, [RC-001-generic-wick-kernel-sign-derivation.py](../calculations/RC-001-generic-wick-kernel-sign-derivation.py), and its [validation log](../validation/RC-001-generic-wick-kernel-sign-derivation.txt), pass **19 exact symbolic checks**. It derives the B terms sector by sector from the generic numerator and the five Euclidean master-integral factors:
- (2H G): the angular-averaged tensor term gives (-2Hg_alpha/(3Delta_0)), while the denominator insertion gives (+2Hd_alpha/Delta_0);
- (2sum C_{ij}k_icdot k_j): the local (F_alpha) term gives (+F_alpha/(3Delta_0^2)), and the denominator insertion gives (-2Sd_alpha/(3Delta_0^2));
- the constant (2M) term gives (+2Md_alpha/(3Delta_0^3)).

This second derivation also explicitly tests the alternative denominator ((K_E^2+Delta_0+d)^{-4}). Reversing the sign of the denominator shift flips the (d_alpha)-insertion terms, but **does not** flip the (g_alpha) tensor term. Thus the historical whole-(B_1) sign flip cannot be explained by a denominator-shift sign change alone. The two scripts provide independent algebraic corroboration under the stated trace and Wick conventions; neither replaces the still-open physical six-cycle amplitude and UV–EFT matching.



### 9.6 Fixed-sector EFT soft-graph closure and amplitude-level subtraction

This subsection closes the EFT soft subtraction for the **muon-channel unbroken-phase external state**
\[
H(p_1),\quad S(p_2),\quad H^\dagger(p_3),\quad S^\dagger(p_4),
\]
at strict \(O(M_{E\mu}^{-2})\) and fixed \(O(|y_\mu|^2|\lambda_\mu|^2)\). It does not claim that every fermionic Wilson coefficient or every real-field mass-basis cycle has been matched.

| Candidate family | Decision for this target \(\mu\)-channel 1PI four-scalar amplitude | Reason / matching role |
|---|---|---|
| SFT-01: \(C_{5,\mu}C_{5,\mu}^\ast\) massless chiral-fermion bubble | **Keep; sole direct soft 1PI graph in the declared coupling sector** | The trace is \(2k\cdot(k+q)\). Using \(2k\cdot(k+q)=k^2+(k+q)^2-s\), the two tadpoles are scaleless in dimensional regularization; the remaining term is the massless \(B_0(s;0,0)\) bubble. |
| SFT-02/03: \(Q_{LD}/Q_{RD}\) plus scalar quartic and a fermion tadpole | **Do not add to the local 1PI coefficient** | The massless tadpole vanishes in dimensional regularization and the stated graph is scalar-line reducible. A broken-phase mass/VEV insertion must be power-counted anew. These are also different coupling orders from the fixed \(|y_\mu|^2|\lambda_\mu|^2\) sector. |
| Pure-light loops without a heavy-dependent insertion | Cancel in UV-minus-EFT matching | Cancellation requires identical light-field content, external-state normalization, gauge convention, IR regulator, and renormalized light parameters on both sides. |
| SFT-07–10 gauge-current exchanges | Keep in the separate connected-current/source ledger if that amplitude is matched | They are reducible through the exchanged gauge boson and are not extra local 1PI four-scalar vertices. Kinetic-mixing inputs must be the same in UV and EFT. |
| SFT-04–06 and SFT-11–13 | Exclude from strict dimension six | Their explicit heavy-mass order is \(O(M_{E\mu}^{-4})\); they belong to the dimension-eight or fixed-VEV higher-order closure. |
| SFT-14–22 | Not part of this four-scalar external state | They are required for the full dimension-six fermionic Wilson vector, but have different external amplitudes. |
| SFT-23–26 | Not an additional direct local scalar 1PI soft graph in this fixed coefficient | They concern one-loop \(C_5\) and fermionic derivative/current coefficients, with gauge/leg/contact/counterterm closure still needed for those separate claims. |

The hard-region amplitude, bare EFT soft bubble, and local EFT counterterm are

\[
i\Gamma_{\mathrm{hard},\mu}^{(2)}
=\frac{i|C_{5,\mu}|^2}{16\pi^2}
\left[(-\Delta_{\mathrm{IR}}+L_\mu-2)s+\frac{t}{6}\right],
\qquad
L_\mu=\ln\frac{M_{E\mu}^2}{\mu_R^2},
\]

\[
i\Gamma_{\mathrm{soft},\mu}^{\mathrm{bare}}
=\frac{i|C_{5,\mu}|^2s}{16\pi^2}
\left[\Delta_{\mathrm{UV}}
-\ln\frac{-s-i0}{\mu_R^2}+2\right],
\qquad
i\Gamma_{\mathrm{ct},\mu}
=-\frac{i|C_{5,\mu}|^2s}{16\pi^2}\Delta_{\mathrm{UV}}.
\]

The counterterm removes the EFT soft UV pole. Before identifying the region poles, the hard plus bare-soft sum is

\[
i\Gamma_{\mathrm{hard},\mu}^{(2)}
+i\Gamma_{\mathrm{soft},\mu}^{\mathrm{bare}}
=\frac{i|C_{5,\mu}|^2}{16\pi^2}
\left[(\Delta_{\mathrm{UV}}-\Delta_{\mathrm{IR}}+L_\mu
-\ln\tfrac{-s-i0}{\mu_R^2})s+\frac{t}{6}\right].
\]

With the method-of-regions identification \(\Delta_{\mathrm{IR}}=\Delta_{\mathrm{UV}}\), the poles cancel. The renormalized soft loop is proportional to \(s[-\ln((-s-i0)/\mu_R^2)+2]\); subtracting that soft matrix element from the renormalized full UV amplitude leaves the local hard matching polynomial

\[
\boxed{
\mathcal A_{\mathrm{match},\mu}^{\mathrm{local}}
=\frac{i|C_{5,\mu}|^2}{16\pi^2}
\left[(L_\mu-2)s+\frac{t}{6}\right].
}
\]

This is the completed amplitude-level soft subtraction for the single source-aligned \(\mu\)-channel, including the required local EFT counterterm and the UV/IR pole distinction. It agrees with the independent 10-check \(C_5C_5^\ast\) trace audit and 12-check fixed-sector pole ledger.

**Flavor boundary:** the \(\tau\) interaction contains \(S^\ast\), so its corresponding external orientation is \(H,S^\dagger,H^\dagger,S\), its bubble invariant is \(u\), and its local hard polynomial is \((L_\tau-2)u+t/6\). It is a separate oriented channel, not the same \(H,S,H^\dagger,S^\dagger\) amplitude. The source-aligned §248 ledger records that \(\tau\) subtraction separately; it must be combined with the \(\mu\) channel only after the external-state projection and flavor-resolved \(s/u\) routing are fixed.

**Boundary of this closure:** the result does not perform the full operator-basis projection of the local \(s,t\) structures; it does not prove that the 576 finite-mass simplex integrals can be taken to the massless-light-state limit without a dimensionally regulated regions expansion; and it does not yet match the full real-field six-cycle candidate sum to the complex-field amplitudes. The mixed-mass hard-region expansion, flavor-resolved \(\mu/\tau\) \(s/u\) assignment, determinant-log/diagram multiplicity, and full Wilson-vector counterterms remain open. Accordingly, PR #9 remains Draft/Open.

### 9.7 Exact mass-basis vertex rephasing and mass-matrix reconstruction

The new [mass-basis vertex/rephasing audit](../calculations/RC-001-mass-basis-vertex-rephasing-audit.py) passes **11 exact symbolic checks**, with its source-aligned output in [validation/RC-001-mass-basis-vertex-rephasing-audit.txt](../validation/RC-001-mass-basis-vertex-rephasing-audit.txt).

Using
[
U_L=egin{pmatrix}c_L&s_L\-s_L&c_Lend{pmatrix},qquad
U_R=egin{pmatrix}c_R&s_R\-s_R&c_Rend{pmatrix},
qquad D=operatorname{diag}(-1,1),
]
and the interaction-basis Yukawa matrices
[
Y_h^{(0)}=aegin{pmatrix}0&1\0&0end{pmatrix},qquad
Y_s^{(0)}=begin{pmatrix}0&0\1&0end{pmatrix},
]
the signed-light-mass convention gives (G_{h,s}=U_L^T Y_{h,s}^{(0)}U_R). The audit reproduces the source §276 matrices and verifies that (Y_{h,s}=G_{h,s}D) yields the positive-light-mass Eq. (13) matrices exactly.

The signed mass matrix reconstructs as
[
mathcal M=U_Loperatorname{diag}(-m_1,m_2)U_R^T
=egin{pmatrix}
-c_Lc_Rm_1+m_2s_Ls_R & c_Lm_1s_R+c_Rm_2s_L\
c_Lm_2s_R+c_Rm_1s_L & c_Lc_Rm_2-m_1s_Ls_R
end{pmatrix}.
]
The original triangular form requires the exact constraint
[
-c_Lc_Rm_1+m_2s_Ls_R=0.
]
This audit therefore removes the mass-basis vertex-phase ambiguity before the pathwise trace is compared with the source-aligned interaction-basis amplitude.

**Scope boundary:** the rotation/rephasing identities are now checked, but the full six-cycle amplitude is not yet proven equal to the fixed complex-field (SFT)-01 channel. The remaining comparison must still include the chiral propagator transformations, labeled external momenta, the (mu/	au) (s/u) assignment, and the complete hard/soft expansion in (d=4-2epsilon). This audit adds no new Wilson coefficient.


### 9.8 Real-field to complex-field external-state projection

The new [external-state projection audit](../calculations/RC-001-real-to-complex-external-projection-audit.py) passes four exact combinatoric checks; the captured output is in [validation/RC-001-real-to-complex-external-projection-audit.txt](../validation/RC-001-real-to-complex-external-projection-audit.txt).

For the radial components,
[
h_i=rac{H_i+H_i^dagger}{sqrt2},qquad
s_i=rac{S_i+S_i^dagger}{sqrt2}.
]
Expanding the labeled (h_1h_2s_1s_2) external state gives (2^4=16) raw complex-field assignments. Charge neutrality leaves four assignments with one (H), one (H^dagger), one (S), and one (S^dagger). Each has field-decomposition weight
[
left(rac1{sqrt2}ight)^4=rac14,
qquad
sum_{mathrm{neutral assignments}}rac14=1.
]

The six labeled real-field cycles still comprise three reverse pairs; the projection ledger records 24 orientation/cycle combinations and introduces no additional reverse-loop factor.

**Important consequence for the next matching step:** the source-aligned (H,S,H^dagger,S^dagger) amplitude is one oriented complex-field channel. It cannot be equated to the full real (h_1h_2s_1s_2) six-cycle amplitude by simply multiplying or dividing by four. The four charge-neutral assignments may route the labeled external momenta into different crossed channels, and the interaction-basis Yukawa vertices determine which orientations vanish. The next required artifact is therefore a momentum-routed projection table for all four assignments, followed by the interaction-basis flavor-flow trace for each allowed cycle. Only then can the mass-basis six-cycle sum be compared term by term to the source-aligned hard/soft result.

This is a combinatoric projection check only; it supplies no new amplitude coefficient and does not close the remaining UV–EFT matching.


### 9.9 Momentum-routed projection of the source local amplitudes onto (h_1h_2s_1s_2)

The new [momentum-routing projection script](../calculations/RC-001-real-to-complex-momentum-routing-projection.py) passes **8 exact symbolic checks**, with its source-aligned output in [validation/RC-001-real-to-complex-momentum-routing-projection.txt](../validation/RC-001-real-to-complex-momentum-routing-projection.txt).

Take all external momenta incoming and define
[
s_R=(p_{h_1}+p_{s_1})^2,qquad
u_R=(p_{h_1}+p_{s_2})^2,qquad
t_R=(p_{h_1}+p_{h_2})^2.
]
The four charge-neutral field assignments give the following flavor-channel routings:

| Assignment | (mu) channel (s_mu=(p_H+p_S)^2) | (	au) channel (u_	au=(p_H+p_{S^dagger})^2) | Field weight |
|---|---|---|---:|
| (h_1:H, h_2:H^dagger, s_1:S, s_2:S^dagger) | (s_R) | (u_R) | (1/4) |
| (h_1:H, h_2:H^dagger, s_1:S^dagger, s_2:S) | (u_R) | (s_R) | (1/4) |
| (h_1:H^dagger, h_2:H, s_1:S, s_2:S^dagger) | (u_R) | (s_R) | (1/4) |
| (h_1:H^dagger, h_2:H, s_1:S^dagger, s_2:S) | (s_R) | (u_R) | (1/4) |

The crossed (t_R) invariant is unchanged under all four assignments. Averaging the source §248 local matching polynomials over these assignments gives the projected local real-field amplitude

[
oxed{
mathcal A_{hhss,mathrm{local}}
=rac{i}{16pi^2}sum_{ell=mu,	au}|C_{5,ell}|^2
left[
rac{L_ell-2}{2}(s_R+u_R)+rac{t_R}{6}
ight],
qquad
L_ell=lnrac{M_{E_ell}^2}{mu_R^2}.
}
]

This is a new, explicit external-state projection of the **source-aligned complex local amplitudes**, not the result of integrating the mass-basis six-cycle candidate kernels. It fixes the momentum-crossing map that the next comparison must use and prevents the mistake of identifying the (h_1h_2s_1s_2) amplitude with one complex channel or multiplying one channel by an unjustified factor of four.

**Remaining matching gate:** substitute the on-shell conditions into the 576-row candidate ledger, map its invariant basis to ((s_R,t_R,u_R)), and then compare the mass-basis cycle sum to this projected local polynomial only after the dimensionally regulated mixed-mass hard/soft expansion and common graph factors are fixed. The existing finite-mass simplex integral is not by itself that comparison.


### 9.10 Chiral-flavor trace covariance: what it closes and what it does not

The new [chiral-flavor trace basis-invariance script](../calculations/RC-001-chiral-flavor-trace-basis-invariance.py) passes **22 exact symbolic checks**; the captured output is in [validation/RC-001-chiral-flavor-trace-basis-invariance.txt](../validation/RC-001-chiral-flavor-trace-basis-invariance.txt).

For each of the 16 chiral-flow patterns (a_iin{L,R}), the script verifies
[
operatorname{tr}!left[
(U_{a_1}^T X_1 U_{a_2})
(U_{a_2}^T X_2 U_{a_3})
(U_{a_3}^T X_3 U_{a_4})
(U_{a_4}^T X_4 U_{a_1})
ight]
=operatorname{tr}(X_1X_2X_3X_4),
]
using exact rational parametrizations of (U_L,U_R) for which (U_L^TU_L=U_R^TU_R=mathbf 1) holds identically. It also reproduces the signed-light-mass §276 Yukawa matrices and the right-handed rephasing to the positive-light-mass Eq. (13) matrices.

**What this establishes:** if the mass-basis calculation includes every chiral propagator block, every internal mass eigenstate, and each labeled external cycle exactly once, the ordered-loop flavor trace is invariant under the change of basis. The mass-basis sum and the interaction-basis trace are not independent physical amplitudes; they are two representations of the same amplitude.

**What remains open:** this covariance identity does not validate the candidate (B_1/B_2/B_3) momentum kernel by itself, because the kernel also depends on the explicit numerator decomposition and denominator routing. Nor does it replace the (d=4-2epsilon) hard/soft expansion: the finite-mass (d=4) simplex integrals cannot be naively taken to the massless-light-state limit when endpoint singularities are present. The source-aligned §248 calculation supplies the dimensionally regulated hard/soft subtraction for the complex channels; the remaining task is to establish the routed, common-factor mapping from the generated six-cycle candidate kernels to the projected local polynomial in §9.9.


### 9.6 Complex external-state projection and flavor-resolved s/u routing

The new [RC-001-complex-external-cycle-projection.py](../calculations/RC-001-complex-external-cycle-projection.py) and [validation record](../validation/RC-001-complex-external-cycle-projection.txt) pass **14 exact checks**. This resolves a distinction that the real-scalar six-cycle ledger alone cannot resolve: a real field \(s\) contains both \(S\) and \(S^\dagger\) orientations, whereas the EFT matching amplitude has fixed complex external legs \(H,S,H^\dagger,S^\dagger\).

For the unbroken, zero-mixing matching benchmark, the chiral complex vertices are
\[
V_H=Y_hP_R,\qquad V_{H^\dagger}=Y_h^\dagger P_L.
\]
For the muon assignment \(S_\mu=S\),
\[
V_S^{(\mu)}=Y_sP_R,\qquad V_{S^\dagger}^{(\mu)}=Y_s^\dagger P_L.
\]
For the tau assignment \(S_\tau=S^\dagger\), the \(S\) and \(S^\dagger\) assignments are interchanged. Exhausting all six labeled cycle orderings and 16 internal-state paths for each flavor gives exactly one nonzero cycle/path row per flavor in this limit:
\[
\begin{array}{c|c|c|c}
\text{flavor}&\text{oriented cycle}&\text{path}&\text{channel}\\
\mu&H\to S\to S^\dagger\to H^\dagger&(0,1,0,1)&s\\
\tau&H\to S^\dagger\to S\to H^\dagger&(0,1,0,1)&u
\end{array}
\]
Both surviving traces are
\[
\operatorname{tr}[\cdots]
=2y^2\lambda^2M_E^2\,k_2\cdot k_4.
\]
With \(q_s=-(p_H+p_S)\) and \(q_u=-(p_H+p_{S^\dagger})\), the light denominators are \(k^2(k-q_{s,u})^2\); the heavy denominators are respectively \([(k+S)^2-M_E^2][(k-S^\dagger)^2-M_E^2]\) and \([(k+S^\dagger)^2-M_E^2][(k-S)^2-M_E^2]\). The one-cycle \(s\)-channel hard-region calculation in §9.4 is therefore the source-aligned muon box; exchanging \(S\leftrightarrow S^\dagger\) gives the tau \(u\)-channel analogue.

The generic fixed-chirality trace is independently verified:
\[
\operatorname{tr}\!\left[
P_R(\slashed k_1+m_1)P_R(\slashed k_2+m_2)
P_L(\slashed k_3+m_3)P_L(\slashed k_4+m_4)
\right]
=2m_1m_3\,k_2\cdot k_4.
\]
Thus the fixed complex amplitude contains the two required mass numerators and two slash numerators only. The four-slash \(HG\) and constant four-mass \(M\) sectors that appear in the real-scalar trace decomposition vanish for this specific complex chirality sequence. Consequently, the B1/B3 sign audit remains valid for the real-scalar candidate kernels, but B1/B3 do not enter the fixed complex four-scalar matching amplitude in this unbroken benchmark.

The real-scalar projection has four nonzero cycle/path rows in the same zero-mixing limit: two reverse-order rows for the \(s\) pairing and two for the \(u\) pairing. The complex-field projection selects one oriented row for each flavor. Therefore, the 576 real-scalar candidate integrals must not be summed wholesale as a single physical complex amplitude.

**Next matching step:** retain the source-aligned complex vertices and the flavor-specific cycle, then combine the already checked hard-region polynomial with the corresponding \(C_5C_5^\ast\) EFT soft bubble, contact term, counterterm, and common-basis/EOM projection. At finite mixing, sum all allowed internal mass-eigenstate paths within the fixed complex orientation; do not reintroduce the forbidden real-scalar cycle orientations.


### 9.12 Interaction-basis orientation audit and finite-mixing complex B2 path sum — 2026-10-27

Two new calculation records extend the fixed-complex-orientation comparison.

**Interaction-basis flavor flow:** [RC-001-interaction-basis-complex-cycle-flow.py](../calculations/RC-001-interaction-basis-complex-cycle-flow.py) and its [validation record](../validation/RC-001-interaction-basis-complex-cycle-flow.txt) enumerate the four charge-neutral assignments, both flavors, and all six labeled cycles (48 cases). The interaction-basis matrices give 32 cases with no allowed flavor path, 16 cases with a unique path, and within those 16 cases eight identically zero chiral traces and eight nonzero traces. The eight nonzero contributions map to the source-aligned \(\mu\) \(s\)-channel and \(\tau\) \(u\)-channel as dictated by the external assignment. The real-field coupling normalization \(a^2b^2=y^2\lambda^2/4\) is already the \(1/4\) external-field decomposition weight; do not apply another factor of \(1/4\).

**Finite-mixing complex path sum:** [RC-001-fixed-complex-finite-mixing-B2-ledger.py](../calculations/RC-001-fixed-complex-finite-mixing-B2-ledger.py) constructs the fixed complex orientations
\[
\mu:\ H,S,S^\dagger,H^\dagger,\qquad
\tau:\ H,S^\dagger,S,H^\dagger,
\]
and retains all 16 internal mass-eigenstate paths for each flavor. Because the fixed chiral sequence is \(P_R,P_R,P_L,P_L\), its trace is
\[
\operatorname{tr}\!\left[
P_R(\slashed k_1+m_a)P_R(\slashed k_2+m_b)
P_L(\slashed k_3+m_c)P_L(\slashed k_4+m_d)
\right]
=2m_a m_c\,k_2\!\cdot k_4,
\]
so only the \(C_{13}\) mass-numerator structure and the \(B_2\)-type \(O(p^2)\) kernel occur. The analytic \(d=4\) simplex calculation produces 192 path/invariant rows (2 flavors × 16 paths × 6 invariants) and includes \(\Gamma(4)=6\) once.

In the zero-mixing limit, each fixed complex orientation has only path \((0,1,0,1)\) with coupling product \(y^2\lambda^2\). At the exact rational benchmark \(c_L=c_R=12/13\), \(s_L=s_R=5/13\), \(m_1=1\), \(m_2=144/25\), \(y=2/7\), \(\lambda=3/11\), the triangular \(M_{11}=0\) condition holds. The integrated \(\mu\) and \(\tau\) sums are related by \(S\leftrightarrow S^\dagger\), i.e. \(Q_2\leftrightarrow Q_3\) and \(Q_4\leftrightarrow Q_5\), with \(Q_1,Q_6\) unchanged; the six coefficient comparisons agree numerically at 35-digit precision.

The notebook-generated 192-row CSV is 63,259 bytes with SHA-256 3cd876b6938db7d1d86da179279d94be1554ec271c1a7de16774887be0f9dba7; it is not committed. The validation record explicitly distinguishes this expression-level notebook run from a standalone run of the checked-in script.

**Boundary:** the finite-mixing result is still a finite-mass \(d=4\) kernel sum, not the hard Wilson coefficient. The \(m_1\to0\) limit cannot be taken naively because the endpoint/IR-sensitive terms must be separated from the EFT soft contribution. The next step is the dimensionally regulated \(d=4-2\epsilon\) hard/soft expansion for the fixed complex orientation, followed by subtraction of the corresponding EFT soft bubble, contact term, and counterterm in the same scheme. Common diagrammatic normalization/multiplicity and the final common-basis/EOM projection remain open.


### 9.13 Small-mixing power counting of the finite-complex paths — 2026-10-27

Added [RC-001-fixed-complex-path-power-counting.py](../calculations/RC-001-fixed-complex-path-power-counting.py) and its [validation record](../validation/RC-001-fixed-complex-path-power-counting.txt).

For each of the 16 paths in each fixed complex orientation, the script extracts the exact powers of \(s_L,s_R\) in the four-vertex product. The \(C_{13}\) numerator also contains the two mass numerators on lines 1 and 3. Applying the triangular mass relation
\[
\frac{m_1}{m_2}=\frac{s_Ls_R}{c_Lc_R}
\]
adds one power of both mixing angles for each light mass among those two numerator factors.

The result is:
- The unique degree-zero path for both \(\mu\) and \(\tau\) is \((0,1,0,1)\).
- Its coupling product is \(y^2\lambda^2c_L^4c_R^4\), and its \(C_{13}\) mass weight is \(y^2\lambda^2c_L^4c_R^4m_2^2\).
- In the zero-mixing limit, this reduces to the source-aligned numerator \(y^2\lambda^2M_E^2\).
- All 30 other flavor/path rows have total effective mixing degree at least two after enforcing \(M_{11}=0\); the minimum non-leading degree is two.

**Interpretation:** this supports the leading unbroken dimension-six matching being controlled by the source-aligned \((0,1,0,1)\) path, whose \(d=4-2\epsilon\) hard-region and EFT-soft subtraction are already recorded in §§9.4–9.6. The remaining paths are numerator-suppressed by \(s_L^2\), \(s_R^2\), or higher powers and belong to the VEV/mixing-suppressed correction problem. This is not by itself a complete regions proof: the hard-region expansion must verify that no omitted power-enhanced infrared contribution changes the counting, and the finite-mass \(d=4\) simplex sum must not be substituted for that expansion.


### 9.14 Exact finite-mixing propagator covariance and reduction to the source box

The new [full-propagator covariance script](../calculations/RC-001-full-propagator-basis-covariance.py) passes **14 exact symbolic checks**; its byte-aligned execution record is in [validation/RC-001-full-propagator-basis-covariance.txt](../validation/RC-001-full-propagator-basis-covariance.txt).

For the fixed complex orientation, the chiral trace has the flavor structure
\[
\operatorname{tr}_{f}\!\left[
Y_h P_1Y_sD_2Y_s^T P_3Y_h^T D_4
\right],
\]
where
\[
D_i=\operatorname{diag}\!\left(
\frac1{k_i^2-m_1^2},\frac1{k_i^2-m_2^2}
\right),\qquad
P_i=\operatorname{diag}\!\left(
\frac{m_1}{k_i^2-m_1^2},\frac{m_2}{k_i^2-m_2^2}
\right).
\]
The 16 explicit internal mass-eigenstate paths are exactly the component expansion of this one matrix trace. With
\[
Y_h=U_L^T Y_h^{(I)}U_R D,\qquad
Y_s=U_L^T Y_s^{(I)}U_R D,\qquad D=\operatorname{diag}(-1,1),
\]
and the corresponding chiral propagator blocks transformed with \(U_L,U_R D\), the rotation matrices telescope around the closed trace. The script verifies the exact identity
\[
\boxed{\mathcal A_{\rm mass\ basis}^{\rm integrand}
=\mathcal A_{\rm interaction\ basis}^{\rm integrand}}
\]
for generic finite mixing, before performing the loop integral.

This gives a stronger statement than trace covariance alone: the denominators and mass numerators are included, so the 16 finite-mixing paths are **not 16 independent diagrams or 16 independent Wilson coefficients**. They are the mass-eigenstate decomposition of one ordered loop.

In the unbroken limit \(s_L=s_R=m_1=0\), only path
\[
(0,1,0,1)=(\text{light},\text{heavy},\text{light},\text{heavy})
\]
survives. Its flavor factor is
\[
\frac{y^2\lambda^2M_E^2}
{(k_1^2-M_E^2)\,k_2^2\,(k_3^2-M_E^2)\,k_4^2},
\]
and the fixed chiral Dirac trace supplies \(2k_2\cdot k_4\). This reproduces the source-aligned two-heavy/two-light box integrand used in §9.4. The \(\tau\) orientation has the same matrix structure with the external \(S\leftrightarrow S^\dagger\) routing, hence the \(u\)-channel rather than the \(\mu\) \(s\)-channel.

The normalization is also checked: four real-field vertices each carry \(1/\sqrt2\), so the real-loop coupling product has a factor \(1/4\). This is exactly the \(1/4\) weight of one charge-neutral complex external assignment. Summing the four allowed assignments gives unit projection weight; **no additional factor \(1/4\) is to be applied**.

**What this closes:** the exact finite-mixing mass-basis path sum is basis-covariant at integrand level, and the leading unbroken term reduces to the source-aligned box with the already checked global sign and hard/soft subtraction.

**What remains open:** this does not calculate the VEV-suppressed hard/soft corrections from the other paths. Their finite-mass \(d=4\) simplex integrals cannot be promoted to Wilson coefficients by taking \(m_1\to0\); each region-sensitive contribution must be separated from the corresponding EFT soft matrix element. It also does not close other operator sectors, the full counterterm vector, or the complete common-basis/EOM projection. PR #9 remains Draft/Open.


### 9.15 EFT interpretation of the power-soft finite-mixing paths — 2026-11-12

The boundary analysis in `RC-001-fixed-complex-soft-region-boundary-audit.py` identifies three power-soft paths, (0000,0001,0100), in addition to the leading logarithmic (0101) path. The new [power-soft EFT topology map](../calculations/RC-001-fixed-complex-power-soft-EFT-topology-map.py) and [validation record](../validation/RC-001-fixed-complex-power-soft-EFT-topology-map.txt) pass **10 exact symbolic coupling/factorization identities** by local SymPy expression replay. The checked-in script was not run as a standalone process; the validation record states this explicitly.

The exact triangular relation and the positive-light-mass Eq. (13) vertices give
[
m_1=M_Erac{s_Ls_R}{c_Lc_R},qquad
y_h^{m light}=yc_Ls_R,qquad
lambda_s^{m light}=lambda s_Lc_R,
]
and
[
C_{5,m eff}=rac{ylambda c_L^2c_R^2}{M_E},
qquad
oxed{y_h^{m light}lambda_s^{m light}=C_{5,m eff}m_1.}
]
This identity explains how mixing-suppressed light Yukawa vertices can coexist with nonvanishing soft-region contributions: the simplex boundary supplies inverse powers of (m_1).

The three power-soft coefficients from the boundary audit factorize as
[
mathcal S_{0000}
=-rac{|C_{5,m eff}|^2}{120}(17s+7t+u),
]
[
mathcal S_{0001}
=+rac{5|C_{5,m eff}|^2}{12}s,qquad
mathcal S_{0100}
=+rac{|C_{5,m eff}|^2}{12}(6s+t+u),
]
so
[
oxed{mathcal S_{m power}
=rac{|C_{5,m eff}|^2}{40}(31s+t+3u).}
]

Their EFT topology interpretation is:
- (0000): an all-light box with four induced light-light Yukawa vertices;
- (0001) and (0100): one-heavy/three-light soft triangles, represented in the EFT by one (C_5) insertion and two induced light-light Yukawa vertices;
- (0101): the two-heavy/two-light logarithmic region, matched to the (C_5C_5^ast) soft bubble already treated in the source-aligned hard/soft calculation.

**Crucial distinction:** the power-soft polynomial is part of the broken-phase finite-mixing amplitude. It is not an additional unbroken dimension-six Wilson coefficient. It must be reproduced by the corresponding EFT all-light box and one-heavy triangle graphs, with their (d=4-2epsilon) integrals and counterterms, before the UV soft contribution is subtracted. No empirical subtraction of (mathcal S_{m power}) is allowed. This is the next open calculation; no cancellation is claimed yet.
