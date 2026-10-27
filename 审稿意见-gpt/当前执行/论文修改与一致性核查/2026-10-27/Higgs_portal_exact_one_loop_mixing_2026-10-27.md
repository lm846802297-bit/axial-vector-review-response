# Exact one-loop \(h\)-\(s\) mixing audit

**Date:** 2026-10-27  
**Scope:** Complete the meeting-requested one-loop induced \(h\)-\(s\) mixing estimate for the specified axial-vector UV model, including a finite-momentum fermion-loop calculation and a conditional near-degenerate pole diagnostic.  
**Script:** [\`higgs_portal_exact_fermion_loop_audit.py\`](higgs_portal_exact_fermion_loop_audit.py)  
**Related baseline:** [Plan C-lite matching and complex-pole record](Higgs_portal_planC_lite_matching_and_complex_poles_2026-10-27.md).

## 1. Source and meeting decisions reviewed first

Before performing this calculation, I reviewed all four original 2026-10-23 meeting transcripts (01–04) and \`会议观点总结_2026-10-23.md\`. The decisive instructions are:

- Transcript 01, 14:22–17:32 and 25:03–26:56: do not answer only with the formal expression for \(\theta_{hs}\); calculate the one-loop induced term and estimate its size.
- The summary's Principles 3 and issue families C/D: a quantitative calculation is needed rather than argument alone; do not expand the particle content.
- Transcript 03, 00:00: the expected suppression by small mixing angles was suggested as a useful comparison, but the calculation must determine whether that expectation is actually valid.
- The adopted Route B remains unchanged: retain the axial-vector phenomenology, narrow the claims, and add no particles.

I also checked the current exported manuscript source \`main.tex\` in the Library, especially \`eq:mu-2by2-mass\`, \`eq:exact-masses-2by2\`, \`eq:mixing-angles-2by2\`, \`eq:gauge-basis-scalar-yukawa\`, \`eq:light-scalar-yukawa\`, and the benchmark paragraph below Eq. (34). The relevant model content is the \(\mu\) and \(\tau\) charged-lepton/VLL blocks, with the \(\tau\) interaction using \(S^*\); for the real CP-even component \(s\), the diagonal \(\mu\) and \(\tau\) couplings have the same sign.

## 2. Diagram selection: why not a direct top or \(W\) loop?

In the stated renormalizable model, \(S\) is an electroweak singlet and has no direct tree-level \(s\bar t t\) or \(sW^+W^-\) vertex. With the portal treated as a loop-order matching input, **there is no direct one-loop top or \(W\) diagram for the off-diagonal \(h\)-\(s\) two-point function at the order calculated here**. A diagram using an \(sWW\) or \(s\bar t t\) vertex would require portal-induced scalar mixing; that is not an independent tree-level coupling of the model and is beyond the leading fermion-loop order evaluated here.

The nonzero leading diagrams are the complete charged-lepton/VLL fermion loops. For each \(\ell=\mu,\tau\), both mass eigenstates \(f_\ell,E_\ell\) are retained. The calculation sums the four ordered internal-state pairs \((f,f),(f,E),(E,f),(E,E)\), rather than keeping only the light-lepton bubble. This is essential for checking the UV structure and the hard matching term.

## 3. One-loop formula and UV consistency check

Use the manuscript's real Yukawa matrices \(Y_h,Y_s\) in the mass basis, with the 1PI insertion convention \(-i\Pi_{hs}\). For each ordered internal-state pair \(i,j\), define
\[
C_{ij}=Y^h_{ij}Y^s_{ij}+Y^h_{ji}Y^s_{ji},\qquad
D_{ij}=Y^h_{ij}Y^s_{ji}+Y^h_{ji}Y^s_{ij}.
\]
The finite \(\overline{\mathrm{MS}}\) contribution is
\[
\Pi_{hs}^{ij}(p^2)=\frac{1}{16\pi^2}\left\{
C_{ij}\left[A_0(m_i^2)+A_0(m_j^2)
+(m_i^2+m_j^2-p^2)B_0(p^2;m_i^2,m_j^2)\right]
+2m_im_jD_{ij}B_0(p^2;m_i^2,m_j^2)
\right\}.
\]
Here the finite functions are
\[
A_0(m^2)=m^2\left(1-\ln\frac{m^2}{\mu_R^2}\right),\quad
B_0(p^2;m_i^2,m_j^2)=-\int_0^1dx\,
\ln\frac{xm_i^2+(1-x)m_j^2-x(1-x)p^2-i0}{\mu_R^2},
\]
with the above expressions denoting the \(\overline{\mathrm{MS}}\)-subtracted parts. The full fermion result is the sum over \(i,j\) and both flavors.

The source's gauge-basis Yukawa matrices occupy orthogonal entries: \(h\) couples \(\bar L E_R\), whereas \(s\) couples \(\bar E_L\ell_R\). Consequently,
\[
\sum_{i,j}C_{ij}=2\,\mathrm{Re\,Tr}(Y_hY_s^\dagger)=0.
\]
The script verifies this cancellation numerically for both flavor blocks. It is the expected cancellation of the \(p^2\)-proportional UV divergence in the complete mass-eigenstate sum; the light-diagonal subset alone does not pass this test.

## 4. Matching convention and benchmark inputs

The finite-momentum result is quoted under the explicit Plan C-lite reference condition
\[
\lambda_{HS}^{\mathrm{EFT}}(M_E)=0,\qquad M_E=\mu_R=20~\mathrm{TeV}.
\]
This is a chosen benchmark, not a symmetry prediction. The one-loop zero-momentum threshold is
\[
\Delta\lambda_{HS}^{E}=-\frac{1}{8\pi^2}
\sum_{\ell=\mu,\tau}|y_\ell|^2|\lambda_\ell|^2,
\qquad
\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E}.
\]
The exact full-loop \(\Pi_{hs}^{\mathrm{UV}}(0)/(v_hv_s)\) agrees with the leading-seesaw threshold above to a relative difference \(1.79\times10^{-4}\) at both reference points. This residual is consistent with comparing the exact diagonalization of the benchmark mass matrix against the leading-seesaw coupling approximation used to define the threshold input.

| Input | Benchmark A: \(A'A'\) open near \(m_h\) | Benchmark B: \(A'A'\) closed near \(m_h\) |
|---|---:|---:|
| \(M_E\) | \(20~\mathrm{TeV}\) | \(20~\mathrm{TeV}\) |
| \(\theta_{\mu L}=\theta_{\tau L}\) input | \(10^{-2}\) | \(10^{-2}\) |
| \(v_s\) | \(70.886458~\mathrm{GeV}\) | \(315~\mathrm{GeV}\) |
| \(m_{A'}\) | \(10~\mathrm{GeV}\) | \(63~\mathrm{GeV}\) |
| \(g_X=m_{A'}/(2v_s)\) | \(0.0705353\) | \(0.1000\) |
| \(\Delta\lambda_{HS}^{E}\) | \(-0.21076398\) | \(-0.01067338\) |
| \(\lambda_{HS}^{\mathrm{UV}}\) for \(\lambda_{HS}^{\mathrm{EFT}}=0\) | \(+0.21076398\) | \(+0.01067338\) |
| Perturbative scalar-mass interval used in the scan | \(10\le m_s\le355.372~\mathrm{GeV}\) | \(10\le m_s\le1579.176~\mathrm{GeV}\) |

The last row uses \(m_s\ge10~\mathrm{GeV}\) and \(\lambda_S\le4\pi\), hence \(m_s\le\sqrt{8\pi}v_s\). It is a theoretical benchmark interval, not an experimentally allowed region.

## 5. Exact finite-momentum hard-minus-light result

The hard momentum-dependent part is computed from the full UV mass-eigenstate loop and the low-energy light-diagonal bubble:
\[
\Delta\Pi_{\mathrm{hard}}(m_h^2)=
\left[\Pi_{\mathrm{UV}}(m_h^2)-\Pi_{\mathrm{UV}}(0)\right]
-\sum_{\ell=\mu,\tau}\left[
\Pi_{\ell\ell}(m_h^2)-\Pi_{\ell\ell}(0)\right].
\]
The constant hard threshold is absorbed into the chosen matching condition. The remaining result is then added to the Plan C-lite EFT soft bubble and dimension-five contact tadpole. This avoids double-counting the zero-momentum portal threshold.

| Quantity | Benchmark A | Benchmark B |
|---|---:|---:|
| Exact \(\Delta\Pi_{\mathrm{hard}}(m_h^2)\) | \(+0.02403044~\mathrm{GeV}^2\) | \(+0.005407724~\mathrm{GeV}^2\) |
| Source-aligned leading derivative estimate | \(+0.02404513~\mathrm{GeV}^2\) | \(+0.005411030~\mathrm{GeV}^2\) |
| Relative difference | \(6.11\times10^{-4}\) | \(6.11\times10^{-4}\) |
| EFT soft bubble + contact | \(-0.43730830-0.11317371i~\mathrm{GeV}^2\) | \(-0.09841028-0.02546820i~\mathrm{GeV}^2\) |
| Matched \(\Pi_{hs}(m_h^2)\) | \(-0.41327786-0.11317371i~\mathrm{GeV}^2\) | \(-0.09300255-0.02546820i~\mathrm{GeV}^2\) |

The \(\tau\)-block contribution dominates the hard momentum dependence; the \(\mu\)-block contribution is \(8.47\times10^{-5}~\mathrm{GeV}^2\) for A and \(1.91\times10^{-5}~\mathrm{GeV}^2\) for B. The full mass-eigenstate sum is therefore an independent diagram-level check of the source-aligned derivative coefficient at \(p^2=m_h^2\), not just a reuse of that coefficient.

## 6. Mixing size over the conditional scalar-mass interval

Away from degeneracy, the small-mixing diagnostic is
\[
|\theta_{hs}|\simeq\frac{|\Pi_{hs}(m_h^2)|}{|m_h^2-m_s^2|}.
\]
At \(m_s=10~\mathrm{GeV}\), it gives \(2.75\times10^{-5}\) for A and \(6.19\times10^{-6}\) for B. At \(m_s=100~\mathrm{GeV}\), the corresponding \(2|\theta_{hs}|\) diagnostics are \(1.51\times10^{-4}\) and \(3.39\times10^{-5}\). These values support a small-mixing approximation away from the Higgs-degenerate region for these benchmark inputs.

Near degeneracy, the mass-difference formula is not used. Instead the diagnostic
\[
R_{\mathrm{mix}}=\frac{2|\Pi_{hs}(m_h^2)|}{|a-b|},\qquad
a=m_h^2-i m_h\Gamma_h,\quad b=m_s^2-i m_s\Gamma_s,
\]
and the two roots of the complex \(2\times2\) inverse propagator are evaluated. The pole calculation keeps the momentum dependence of the EFT soft loop and uses the exact hard difference at \(p^2=m_h^2\) as the leading analytic hard continuation. Diagonal real self-energies are absorbed into the input masses and diagonal widths are fixed near each pole; this remains a first-pass pole diagnostic, not a full pole-scheme calculation.

| Near-degenerate result at \(m_s=m_h=125.25~\mathrm{GeV}\) | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\Gamma_s(m_h)\) | \(3.746814~\mathrm{GeV}\) | \(0.000158940~\mathrm{GeV}=0.158940~\mathrm{MeV}\) |
| \(R_{\mathrm{mix}}\) | \(0.00182813\) | \(0.39369054\) |
| Higgs-like pole \((m_{\rm pole},\Gamma)\) | \((125.2500008~\mathrm{GeV},4.072691~\mathrm{MeV})\) | \((125.2499586~\mathrm{GeV},3.936814~\mathrm{MeV})\) |
| Higgs-like pole \(|s/h|\) diagnostic | \(9.14\times10^{-4}\) | \(0.203736\) |
| Other pole \((m_{\rm pole},\Gamma)\) | \((125.2640059~\mathrm{GeV},3746.392489~\mathrm{MeV})\) | \((125.2500414~\mathrm{GeV},0.292123~\mathrm{MeV})\) |
| Other pole \(|s/h|\) diagnostic | \(1.09\times10^3\) | \(4.90832\) |
| Region with \(R_{\mathrm{mix}}\ge0.1\) | None in the scanned interval | approximately \(|m_s-m_h|\lesssim7.446~\mathrm{MeV}\) |

The full scan uses \(10~\mathrm{GeV}\le m_s\le\sqrt{8\pi}v_s\) for each benchmark, with a dense scan around \(m_s=m_h\). Benchmark A remains width-regulated and its maximum \(R_{\mathrm{mix}}\) is about \(1.83\times10^{-3}\). Benchmark B has a narrow scalar near \(m_h\); the mixing diagnostic reaches \(0.394\) at degeneracy and the two poles exhibit width redistribution. Thus the meeting's proposed universal conclusion that the loop-induced mixing is always tiny is **not** supported across the full scalar-mass interval.

## 7. What is now complete, and what is not

**Completed for the requested one-loop task:**
1. Reconstructed the actual model's mass-eigenstate \(h\) and \(s\) Yukawa matrices from the manuscript source.
2. Evaluated the complete one-loop \(\mu/\tau\)+VLL fermion contribution, including light-heavy and heavy-heavy internal states.
3. Verified cancellation of the \(p^2\)-proportional divergence in the complete sum and checked the zero-momentum portal threshold against the effective-potential relation.
4. Independently evaluated the finite-momentum hard-minus-light term and reproduced the source-aligned derivative estimate to \(0.0611\%\).
5. Combined the result with the declared Plan C-lite EFT soft/contact benchmark and computed conditional near-degenerate complex-pole diagnostics for two reference points.

**Still outside the completed one-loop task:**
- A fully closed same-order EFT contact/renormalization ledger and complete pole-scheme calculation, including all diagonal self-energies, tadpole/VEV counterterms and residues.
- A model-specific Higgs signal-strength/lineshape and direct-search recast. Therefore the near-degenerate region is **not classified as allowed or excluded**.
- A global scan over the full independent UV parameter set. The two benchmark points are examples, not a global UV viability statement.
- The calculation assumes the stated matching condition \(\lambda_{HS}^{\mathrm{EFT}}(M_E)=0\); the corresponding UV portal is nonzero and must not be presented as symmetry-protected.

**Conclusion for the referee response:** the requested one-loop mixing estimate is now available under explicit matching assumptions. It supports small mixing away from degeneracy in the illustrated benchmarks, but it does not support claiming negligible mixing for every \(m_s\). The narrow-width near-degenerate benchmark must remain **not assessed** until a dedicated two-pole Higgs lineshape and constraint recast is completed.
