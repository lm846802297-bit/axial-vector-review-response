# RC-001 — Portal Boundary and B1/B3 Kernel Reconciliation Ledger

> **Record type:** Dated internal reconciliation supplement; it does not replace the frozen primary source or claim complete model-level matching.
>
> **Audit date:** 2026-10-27
>
> **Status:** The portal matching relation and a working scalar-suppressed reference boundary are explicit. The tree-level C5 coefficient has a separate derivation and exact symbolic check. All 576 six-cycle candidate-kernel simplex integrals are now evaluated conditionally on the current B1/B2/B3 definitions. The physical B1/B3 sign, common loop factors, complete UV–EFT subtraction, and model-level Wilson-vector closure remain **unresolved**.

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

**Status: unresolved; do not promote either candidate kernel to the final Wilson coefficient.**

The working dimension-six result should continue to be quoted only with the scope and caveats of the source-aligned §248/§252 ledger and the live CL-001 claim. The historical B1/B3 calculation is a diagnostic branch, not an accepted independent derivation of that coefficient. The evidence does not yet justify calling it physically wrong, nor does it justify declaring it superseded by a proven term-by-term identity.

Required closure steps:

1. Independently derive the full mass-basis Dirac trace from the actual \(G_h,G_s\) vertices, including conjugation and the parity-odd trace contribution; the existing generic trace identity and path-weight construction do not by themselves prove the complete physical numerator.
2. Derive the numerator-to-kernel map in one Minkowski convention, including the denominator shift and all \(F_\alpha,H,S,M,d_\alpha\) terms, rather than taking the B-kernel formula as a physical input.
3. The six labeled cycles and 16 internal paths have been generated, and their conditional simplex integrals are now evaluated. Still close the physical fermion-loop sign, common Minkowski/Wick phase, and graph/symmetry factors; numerical reverse-cycle agreement is a consistency check, not the physical-amplitude sign determination.
4. Map the complete sum to the same complex external states and momentum basis used in §248/§252, including the off-shell \(\Sigma=\sum_i p_i^2\) terms and EOM-generated potential/source companions.
5. Enumerate and evaluate the complete same-order EFT soft amplitudes, contact terms, and counterterms in the same IR and renormalization prescription; compare UV and IR poles and finite local terms separately.
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
| Routed \(O(p^2)\) candidate coefficients | **Generated and cross-checked** | 576 symbolic rows; reverse-cycle coefficient map passes 1,152/1,152 checks |
| \(\Gamma(4)\), simplex volume, five Euclidean integral factors | **Verified algebraically** | Exact Gamma-function identities |
| Determinant-log \(+i/4\) and diagrammatic \(-1\) | **Recorded separately** | Their complete Feynman-rule/Wick reconciliation is still open |
| Path-dependent simplex integrals | **Conditionally completed** | All 576 candidate B-kernel rows have analytic simplex integrals and 288 numerical reverse-cycle checks; this is not a physical Wilson coefficient because the global sign/factors and UV–EFT subtraction remain open |
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
