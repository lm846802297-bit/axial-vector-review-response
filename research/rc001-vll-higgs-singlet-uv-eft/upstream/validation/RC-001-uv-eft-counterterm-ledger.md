# RC-001 UV–EFT h–s local counterterm ledger

**Scope.** This ledger is derived from the frozen v153 source §§274.2–274.4, 276–278, 283.1–283.5, 284.1–284.4 and 285.1–285.4. It covers the explicitly stated EFT light-state Yukawa bubble plus the tree-generated \(hs\bar\ell\ell\) contact tadpole. It does not claim that all same-order EFT soft insertions have been calculated.

## Conventions

\[
\Gamma_{\rm inv}(s)=s\mathbf 1-\mathcal M_{\rm loc}^2+\Pi(s),\qquad
\Pi_{\rm loop}^{\ell}(s)
=-\frac{q_\ell}{16\pi^2}\left[4A_0(x)+(4x-s)B_0(s;x,x)\right],
\]
where \(x=m_\ell^2\), \(q_\ell=2g_{h\ell}g_{s\ell}\), \(s=p^2\), and
\[
A_0(x)|_{\rm pole}=x\Delta_{\rm UV},\qquad
B_0(s;x,x)|_{\rm pole}=\Delta_{\rm UV}.
\]
The bubble and contact terms are separately
\[
\Pi_{\rm bub}^{\ell}(s)
=-\frac{q_\ell}{16\pi^2}\left[2A_0(x)+(4x-s)B_0(s;x,x)\right],
\qquad
\Pi_{\rm ct}^{\ell}
=-\frac{q_\ell}{16\pi^2}2A_0(x).
\]
The contact tadpole has no \(s\)-dependence.

## Pole cancellation

The total EFT-loop pole is
\[
\boxed{\Pi_{\rm EFT,loop}^{\ell}(s)|_{\rm pole}
=-\frac{q_\ell}{16\pi^2}(8x-s)\Delta_{\rm UV}.}
\]
The local contribution to the inverse propagator must therefore be
\[
\boxed{\Pi_{\rm local\,CT}^{\ell}(s)|_{\rm pole}
=+\frac{q_\ell}{16\pi^2}(8x-s)\Delta_{\rm UV}.}
\]
The bare UV-minus-EFT difference carries this same local pole because the complete mass-basis UV self-energy has zero UV pole under
\[
q_\ell(m_1^2+m_2^2)+2r_\ell m_1m_2=0.
\]

| Projection | Counterterm contribution to \(\Gamma_{\rm inv}\) | Interpretation | Status |
|---|---|---|---|
| \(s^0\) | \(+8q_\ell x\Delta_{\rm UV}/(16\pi^2)\) | In seesaw counting, \(q_\ell=O(M_E^{-2})\) and \(x=O(M_E^{-2})\), so this is \(O(M_E^{-4})\). It must not be misidentified as the leading dimension-four portal counterterm. A gauge-invariant assignment requires a frozen higher-dimensional scalar-potential basis and EOM conventions. | Pole identified; operator assignment open |
| \(s^1\) | \(-q_\ell s\Delta_{\rm UV}/(16\pi^2)\) | For \(\mathcal L_{\rm EFT}\supset(c_{\partial HS}/M_*^2)\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S)\), the quadratic term contributes \(c_{\partial HS}v_hv_s s/M_*^2\). Thus \(\displaystyle\delta c_{\partial HS}=-\frac{M_*^2q_\ell}{16\pi^2v_hv_s}\Delta_{\rm UV}\). | Pole cancellation verified algebraically for this EFT subset |

## Finite terms and unresolved matching

The leading finite \(s^0\) hard term satisfies the source sign check
\[
\Delta\Pi_{\rm hard}^{\ell}(0)
\simeq+\frac{|y_\ell|^2|\lambda_\ell|^2v_hv_s}{8\pi^2}
=-v_hv_s\Delta\lambda_{HS}^{E,\ell},
\quad
\Delta\lambda_{HS}^{E,\ell}
=-\frac{|y_\ell|^2|\lambda_\ell|^2}{8\pi^2}.
\]
This leading dimension-four portal threshold is finite. The \(O(q_\ell x)\) pole in the broken-phase EFT subset is a higher-order term and does not by itself determine the renormalized \(\lambda_{HS}\) boundary condition.

For the derivative projection, subtracting the stated renormalized-Yukawa bubble/contact subset gives
\[
\Delta\Pi_{\rm hard}^{(2{\rm pt})\,\prime}(0)
=\frac{q_\ell}{16\pi^2}\left(L_E-\frac23\right)+\cdots,
\]
while the older on-shell four-point representative gives
\[
\Delta\Pi_{\rm hard}^{(4{\rm pt}),\,\rm old\,rep\,\prime}(0)
=\frac{q_\ell}{16\pi^2}(L_E-2)+\cdots.
\]
Their difference \(4q_\ell/[3(16\pi^2)]\) is a difference between these representatives, not a remaining same-basis mismatch. The cumulative master source v153 §301.1–§301.4 includes the off-shell external-leg terms and EOM completion by \(T_H,T_S\), shifting \(c_H,c_S,c_D\) by \(+2a_\ell/3\) and aligning the specified Yukawa-box derivative coefficients. The contact tadpole itself still has zero momentum derivative.

Open items are the complete model-level Wilson vector, remaining higher-dimensional EFT soft/source sectors, the complete dimension-eight hard matching, and independent diagram-level validation.

## 5. \(C_5^2\) soft-potential counterterm at dimension eight (subset only)

The restricted bubble-plus-contact subset has the constant inverse-kernel pole
\[
+\frac{8q_\ell x_\ell}{16\pi^2}\Delta_{\rm UV}
\simeq+\frac{|y_\ell|^4|\lambda_\ell|^4v_h^3v_s^3}{16\pi^2M_{E_\ell}^4}\Delta_{\rm UV}.
\]
The cumulative master source §§262.5 and 264.4 gives the same \(C_5^2\) light-fermion determinant pole in the gauge-invariant pure-potential representative
\[
\delta\mathcal L_{\rm pot,8}
=+\frac{|y_\ell|^4|\lambda_\ell|^4}{16\pi^2M_{E_\ell}^4}
\Delta_{\rm UV}\,X^2Y^2,\qquad X=H^\dagger H,\quad Y=S^\dagger S.
\]
Its mixed Hessian is \(v_h^3v_s^3\), so it cancels the subset-level constant pole with the source inverse-kernel convention. The equivalent potential counterterm has the opposite sign.

The four-check audit at `calculations/RC-001-dimension8-constant-pole-candidate.py` verifies the leading-seesaw scaling, the \(X^2Y^2\) Hessian, the counterterm sign, and the \(M_E^{-4}\) order; captured output is `validation/RC-001-dimension8-constant-pole-candidate.txt`.

This does **not** complete the dimension-eight hard matching or all \(O(M_E^{-4})\) predictions. Higher-dimensional tree-level EFT vertices and their soft insertions remain outstanding. At a strict \(O(M_E^{-2})\) truncation, this entire constant-pole sector must be dropped consistently.

## 6. PR #69 Benchmark A/B cross-check and Plan-C contact bookkeeping (2026-11-09)

The leading \(O_8=(H^\dagger H)^2(S^\dagger S)^2\) soft-potential pole in Sec. 5 is prior RC-001 work, not a new discovery in [PR #69](https://github.com/lm846802297-bit/axial-vector-review-response/pull/69). PR #69 independently reconstructs it at Benchmarks A/B, explicitly separates the \(hs\) bubble and dimension-five contact pieces, and checks the Plan-C scale derivative against the corresponding running.

The coefficient convention is the one used throughout this ledger:
\[
\mathcal L_{\mathrm{EFT5}}\supset-C_{5,\ell}\mathcal O_{5,\ell}+\mathrm{h.c.},
\qquad
C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.
\]
The signed EFT mass parameter follows the Schur complement; the positive mass used in the light-fermion determinant is its magnitude. The \(O_8\) pole and running depend on \(|C_5|^4\), so the benchmark coefficients are insensitive to the sign once the operator convention is used consistently.

For \(F=\sum_\ell |m_\ell|^4\), the mixed Hessian is
\[
F_{hs}=\frac{16F}{v_hv_s}
=\underbrace{\frac{12F}{v_hv_s}}_{\mathrm{bubble}}
+\underbrace{\frac{4F}{v_hv_s}}_{\mathrm{dimension\!-\!five\ contact}}.
\]
Thus the RC-convention EFT loop pole is
\[
\Pi_{hs,\mathrm{EFT5},\mathrm{loop}}^{\mathrm{UV}}
=-\frac{16F}{16\pi^2v_hv_s}\Delta_{\mathrm{UV}},
\]
with the opposite Plan-B sign used in the archived Plan-C self-energy. This is the same \(12+4=16\) structure already represented by the bubble-plus-contact counterterm in Sec. 5.

**No double counting:** the statement that the archived exact-SVD light-light subtraction is bubble-only applies only to that subtraction. The separate Plan-C-lite finite soft function already includes its contact tadpole: the archived higgs_portal_planC_lite.py function pi_soft_planb returns the sum of explicit bubble and contact terms (source blob SHA df139e099853246501d2fbf9957dbba890014d14). The PR #69 scale-check routine independently retains bubble + contact + hard. The contact must not be appended again to the Plan-C finite soft self-energy.

At \(s=m_h^2\), PR #69 finds in Plan-B convention
\[
\frac{d\Pi_{hs,B}^{\mathrm{soft+hard}}}{d\ln\mu}
=2\Pi_{hs,\mathrm{EFT5},B}^{\mathrm{loop,UV}},
\qquad
\beta_{c_8}^{\mathrm{loop}}
=-\frac{2}{16\pi^2}\sum_\ell|C_{5,\ell}|^4.
\]
The \(O_8\) running cancels the retained scale variation. The residual after running is \(1.73\times10^{-13}\) relative (A) and \(1.50\times10^{-13}\) (B); the symmetric finite-difference derivative agrees with the analytic result to better than \(5.4\times10^{-8}\).

PR #69 also evaluates the finite heavy-eigenstate Coleman--Weinberg contribution in the restricted VLL scalar-potential/\(\overline{\mathrm{MS}}\) basis:
\[
c_8^{\mathrm{VLL,CW}}(M_E)
=-\frac{7}{2(16\pi^2)}\sum_\ell|C_{5,\ell}|^4,
\]
giving \(-3.80925598\times10^{-17}\,\mathrm{GeV}^{-4}\) (A) and \(-9.76902113\times10^{-20}\,\mathrm{GeV}^{-4}\) (B). This is the finite heavy-VLL scalar-potential contribution, not the complete dimension-eight hard/soft Wilson vector. The independent high-precision heavy-eigenvalue expansion check agrees at relative \(2.96\times10^{-11}\); the associated PR #69 GitHub Actions run [42582889232](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42582889232) passes 18 tests.

The new cross-check refines the status of the \(O_8\) scalar-potential subsector only. Higher-dimensional EFT soft/source insertions, derivative-operator/EOM completion, remaining gauge/scalar sectors, diagram-level validation, and full model-level Wilson-vector closure remain open.

## Reproducibility boundary

The SymPy script at calculations/RC-001-uv-eft-two-point-difference.py checks the stated algebraic identities and the counterterm pole cancellation. Its output is in validation/RC-001-uv-eft-two-point-difference.txt. No numerical loop integration, FeynArts/FeynCalc run, complete higher-dimensional EFT soft-insertion sum, or final finite dimension-six Wilson coefficient is claimed.
