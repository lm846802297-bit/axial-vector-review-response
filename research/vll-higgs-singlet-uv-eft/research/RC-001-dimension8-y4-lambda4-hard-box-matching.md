# RC-001 — Dimension-eight \(|y|^4\) and \(|\lambda|^4\) UV hard boxes

**Status (2026-11-10):** the transverse current-current projection and the full on-shell crossed four-scalar amplitude of the one-ordered-cycle heavy/light fermion box have been evaluated by a \(d\)-dimensional hard-region expansion. The direct soft expansion of the same UV numerator reproduces the one-Weyl EFT kernel, and the hard IR / soft UV poles cancel. P0.1–P0.4 are closed at the on-shell amplitude level, including the crossed pairing, weak-index tensors, exact chiral trace, and current/action normalization. The full on-shell hard result also contains a finite local polynomial beyond the transverse-current projection; it is recorded in §5 and must be retained. The off-shell Green-basis tensor decomposition, remaining same-order EFT insertions, final EOM/source reduction, and independent diagram-package validation remain open. No complete dimension-eight Wilson vector is claimed.

## 1. Scope, conventions, and external projection

Use \(d=4-2\epsilon\), dimensional regularization, and the same \(\overline{\mathrm{MS}}\) convention as the soft calculation. Define
\[
L_E=\ln\frac{M_E^2}{\mu_R^2},\qquad
\Delta_{\mathrm{IR,UV}}=\frac1{\epsilon_{\mathrm{IR,UV}}}-\gamma_E+\ln4\pi.
\]
For one flavor, the tree-level coefficients are
\[
C_{LD,\ell}=\frac{|y_\ell|^2}{M_{E\ell}^2},\qquad
C_{RD,\ell}=\frac{|\lambda_\ell|^2}{M_{E\ell}^2}.
\]

The target is the parity-even transverse scalar-current projection. For the Higgs channel choose the complex external fields
\[
H(p_1),\quad H^\dagger(p_2),\quad H(p_3),\quad H^\dagger(p_4),
\]
with
\[
p_1=P+\frac q2,\quad p_2=-P+\frac q2,\quad
p_3=P'-\frac q2,\quad p_4=-P'-\frac q2,
\qquad P\cdot q=P'\cdot q=0.
\]
The scalar currents have matrix elements \(\mathcal J_H=-2P\) and \(\mathcal J'_H=-2P'\) in the all-incoming convention. The transverse projector is
\[
T_{\mu\nu}(q)=q^2\delta_{\mu\nu}-q_\mu q_\nu.
\]
The projection isolates \(P_\mu T^{\mu\nu}P'_\nu=q^2P\cdot P'\). The singlet \(S\) channel is identical with \(P,P'\) interpreted as the corresponding scalar-current momenta.

The ordered full-theory box has two massless chiral propagators and two heavy VLL propagators:
\[
\mathcal I_{\mathrm{UV}}^{\mathrm{ord}}=
\int_k
\frac{\mathcal N(k;p_i)}
{k^2(k+q)^2[(k+p_1)^2+M_E^2][(k-p_4)^2+M_E^2]},
\]
where \(\int_k=\mu_R^{2\epsilon}\int d^dk/(2\pi)^d\), with the Euclidean continuation understood. The parity-even Weyl numerator in NDR is
\[
\mathcal N
=\frac12\operatorname{tr}
\left[
(\slashed k+\slashed p_1)
(\slashed k+\slashed q)
(\slashed k-\slashed p_4)
\slashed k
\right].
\]
The \(\gamma_5\)-odd trace vanishes for this four-scalar projection because momentum conservation leaves at most three independent external four-vectors.

The one-cycle integral is evaluated first. The effective action has the usual \(1/2\) from the second-order current-source expansion; converting the current matrix elements from \(P,P'\) to \(\mathcal J_H,\mathcal J'_H\) supplies a further factor \(1/4\). Thus the effective-action coefficient is the one-cycle projected amplitude coefficient divided by eight. This convention is the same as the \(1/8\) factor in the previously derived EFT soft current kernel.

## 2. Hard-region expansion

In the hard region \(k\sim M_E\), expand the three shifted denominators in the external momenta through total degree four, retaining the coefficient of \(P P' q^2\). The required angular averages are
\[
\left\langle k_1^{2m}k_4^{2n}\right\rangle
=(k^2)^{m+n}
\frac{(\frac12)_m(\frac12)_n}{(\frac d2)_{m+n}},
\]
with odd powers vanishing. The remaining radial integrals reduce to
\[
I_{a b n}=
\int_k\frac{(k^2)^{n-a}}{(k^2+M_E^2)^b}
=
\frac{(M_E^2)^{d/2+n-a-b}}{(4\pi)^{d/2}}
\frac{\Gamma(d/2+n-a)\Gamma(b-d/2-n+a)}
{\Gamma(d/2)\Gamma(b)}.
\]

The exact sum of the radial terms for this transverse projection is
\[
\mathcal I_{\mathrm{hard}}^{\mathrm{ord}}\big|_{P T P'}
=
-\frac{P_\mu T^{\mu\nu}(q)P'_\nu}{24\pi^2M_E^4}
\left[
\Delta_{\mathrm{IR}}-L_E+\frac{17}{12}
\right].
\]
The \(-\Delta_{\mathrm{IR}}\) residue is an infrared pole of the hard region. It is not a UV divergence of the full renormalizable UV box.

After the determinant \(1/2\) and current normalization are included, the hard contribution to the Euclidean effective action is
\[
\boxed{
\begin{aligned}
\Gamma_{\mathrm{hard},H}^{(8),E}
={}&-\frac{1}{192\pi^2}
\sum_{\ell=\mu,\tau}\frac{|y_\ell|^4}{M_{E\ell}^4}
\int_q
\operatorname{tr}_2\!\left[
\mathcal J_{H,\mu}(q)\mathcal J_{H,\nu}(-q)
\right]T^{\mu\nu}(q)
\\[-2pt]
&\hspace{35mm}\times
\left[
\Delta_{\mathrm{IR}}-L_{E\ell}+\frac{17}{12}
\right].
\end{aligned}
}
\]
For the right-handed singlet channel,
\[
\boxed{
\begin{aligned}
\Gamma_{\mathrm{hard},S}^{(8),E}
={}&-\frac{1}{192\pi^2}
\sum_{\ell=\mu,\tau}\frac{|\lambda_\ell|^4}{M_{E\ell}^4}
\int_q
j_{S_\ell,\mu}(q)j_{S_\ell,\nu}(-q)T^{\mu\nu}(q)
\\[-2pt]
&\hspace{35mm}\times
\left[
\Delta_{\mathrm{IR}}-L_{E\ell}+\frac{17}{12}
\right].
\end{aligned}
}
\]
The left-handed result is a weak-index trace, not an extra multiplicity of two appended to a fixed external component. The right-handed loop has one Weyl singlet and no weak multiplicity. Since \(S_\tau=S^*\), \(j_{S_\tau}=-j_{S_\mu}\), but the quadratic current kernel has the same sign for both flavors.

## 3. Soft region and pole cancellation

The soft region expands the two heavy propagators in \(1/M_E\). The remaining massless Weyl current bubble is the kernel already evaluated in the tree/EFT soft audit:
\[
\Pi_{\mu\nu}^{W,E}(q)
=\frac{T_{\mu\nu}(q)}{24\pi^2}
\left[
\Delta_{\mathrm{UV}}-\ln\frac{q^2}{\mu_R^2}+\frac53
\right].
\]
The \(+5/3\) follows from
\[
\int_0^1dx\,x(1-x)=\frac16,\qquad
\int_0^1dx\,x(1-x)\ln[x(1-x)]=-\frac5{18}.
\]
With the same determinant and current normalization,
\[
\begin{aligned}
\Gamma_{\mathrm{soft},H}^{(8),E}
={}&+\frac{1}{192\pi^2}
\sum_\ell\frac{|y_\ell|^4}{M_{E\ell}^4}
\int_q\operatorname{tr}_2[
\mathcal J_{H,\mu}(q)\mathcal J_{H,\nu}(-q)]T^{\mu\nu}(q)
\\[-2pt]
&\hspace{35mm}\times
\left[
\Delta_{\mathrm{UV}}-\ln\frac{q^2}{\mu_R^2}+\frac53
\right],
\end{aligned}
\]
and
\[
\begin{aligned}
\Gamma_{\mathrm{soft},S}^{(8),E}
={}&+\frac{1}{192\pi^2}
\sum_\ell\frac{|\lambda_\ell|^4}{M_{E\ell}^4}
\int_q j_{S_\ell,\mu}(q)j_{S_\ell,\nu}(-q)T^{\mu\nu}(q)
\\[-2pt]
&\hspace{35mm}\times
\left[
\Delta_{\mathrm{UV}}-\ln\frac{q^2}{\mu_R^2}+\frac53
\right].
\end{aligned}
\]

Thus, in each flavor channel,
\[
\boxed{\operatorname{Res}_{\mathrm{IR}}\Gamma_{\mathrm{hard}}
+\operatorname{Res}_{\mathrm{UV}}\Gamma_{\mathrm{soft}}=0.}
\]
The poles are kept distinct until the method-of-regions sum is formed. The EFT local counterterm has the opposite sign to the soft UV pole; the hard-region IR pole cancels that soft pole in the full-theory expansion.

## 4. Finite hard coefficients and matched kernels

The renormalized local hard coefficients in this current Green basis are
\[
\boxed{
c_{8,H}^{\mathrm{hard}}(\mu_R)
=\frac{1}{192\pi^2}
\sum_{\ell=\mu,\tau}\frac{|y_\ell|^4}{M_{E\ell}^4}
\left[
\ln\frac{M_{E\ell}^2}{\mu_R^2}-\frac{17}{12}
\right],
}
\]
\[
\boxed{
c_{8,S}^{\mathrm{hard}}(\mu_R)
=\frac{1}{192\pi^2}
\sum_{\ell=\mu,\tau}\frac{|\lambda_\ell|^4}{M_{E\ell}^4}
\left[
\ln\frac{M_{E\ell}^2}{\mu_R^2}-\frac{17}{12}
\right].
}
\]
These multiply the momentum-space local structures \(\mathcal J_H T\mathcal J_H\) and \(j_S Tj_S\), respectively. They are finite hard matching coefficients for the transverse current projection, not yet coefficients in a fully minimized scalar-operator basis.

Adding the soft terms gives the scale-independent matched kernels
\[
\boxed{
\Gamma_{\mathrm{matched},H}^{(8),E}
=\frac{1}{192\pi^2}
\sum_\ell\frac{|y_\ell|^4}{M_{E\ell}^4}
\int_q\operatorname{tr}_2[
\mathcal J_{H,\mu}(q)\mathcal J_{H,\nu}(-q)]T^{\mu\nu}(q)
\left[\ln\frac{M_{E\ell}^2}{q^2}+\frac14\right],
}
\]
\[
\boxed{
\Gamma_{\mathrm{matched},S}^{(8),E}
=\frac{1}{192\pi^2}
\sum_\ell\frac{|\lambda_\ell|^4}{M_{E\ell}^4}
\int_q j_{S_\ell,\mu}(q)j_{S_\ell,\nu}(-q)T^{\mu\nu}(q)
\left[\ln\frac{M_{E\ell}^2}{q^2}+\frac14\right].
}
\]
The constant \(+1/4\) is the difference \(5/3-17/12\). The arbitrary matching scale cancels between the hard logarithm and the soft logarithm.

## 5. P0.1–P0.4: crossed on-shell amplitude and normalization audit

The full on-shell four-scalar expansion and the crossed pairing are now recorded in research/RC-001-dimension8-crossed-on-shell-box-audit.md. This extends the transverse projection above without changing its result.

For one ordered cycle, the complete on-shell hard polynomial is
\[
\mathcal H_{\rm hard}(s,u)
=
\frac{1}{96\pi^2M_E^4}
\left[
(s^2+2su)(\Delta_{\rm IR}-L_E)
+\frac{11}{6}s^2+\frac{10}{3}su-\frac{3}{10}u^2
\right].
\]
The direct soft expansion of the same UV numerator is
\[
\mathcal H_{\rm soft}(s,u)
=
-\frac{s^2+2su}{96\pi^2M_E^4}
\left[
\Delta_{\rm UV}-\ln\frac{s}{\mu_R^2}+\frac53
\right].
\]
The hard IR and soft UV poles cancel. The matched result is independent of \(\mu_R\).

Importantly, the full on-shell hard polynomial contains a finite local remainder beyond the transverse-current projection:
\[
\mathcal H_{\rm hard}^{\rm local,rem}
=
\frac{1}{96\pi^2M_E^4}
\left[
\frac5{12}s^2+\frac12su-\frac3{10}u^2
\right].
\]
Therefore the previously quoted \(c_{8,H}^{\rm hard}\) and \(c_{8,S}^{\rm hard}\) are **transverse-current Green-basis coefficients only**; they are not the complete on-shell dimension-eight hard matching coefficients. The additional polynomial is retained for the later common-basis EOM/IBP reduction.

The crossed external pairing is obtained by \(s\leftrightarrow u\). For the Higgs doublet the two pairings carry \(\delta_{jk}\delta_{li}\) and \(\delta_{lk}\delta_{ji}\), respectively; there is no additional SU(2) multiplicity. The pure-singlet channel has the same scalar kernels without weak tensors. The \(\tau\) conjugation \(S_\tau=S^*\) reverses the current but leaves the quadratic current kernel unchanged.

The direct soft expansion also resolves the current normalization: the full numerator contains both \(2x(1-x)q^2\) and \((4/d-2)l^2\); after tensor integration these combine to \(4x(1-x)q^2\), recovering the \(+5/3\) one-Weyl kernel. The action coefficient \(1/(192\pi^2)\), after the two current assignments and \(J_H=-2P\) matrix elements, gives the fixed-pairing amplitude coefficient \(1/(24\pi^2)\), exactly as in the direct UV soft limit.

This closes P0.1–P0.4 at the **on-shell four-scalar amplitude** level. The off-shell Green-basis tensor decomposition, final EOM/IBP basis, and independent diagram-package validation remain open; no complete dimension-eight Wilson vector is claimed.

## 6. Reproducibility and acceptance boundary

The exact d-dimensional expansion, angular averages, radial Gamma integrals, soft Feynman-parameter expansion, and pole/finite-term identities are implemented in:
- calculations/RC-001-dimension8-y4-lambda4-hard-box.py
- validation/RC-001-dimension8-y4-lambda4-hard-box.txt

The six local exact checks pass. They verify the displayed stripped transverse projection and its hard/soft pole and finite-term reconciliation. They do not replace an independent diagram-generation package.

**Closed in this note:** the transverse-current hard kernels; the full on-shell hard polynomial for one ordered cycle; the crossed (s/u) pairing; the two Higgs weak-index tensors; the direct soft limit of the same UV numerator; the hard-IR/soft-UV pole cancellation; and the scale-independent matched on-shell amplitude.

**Still open:**
1. the complete off-shell four-scalar Green-function tensor decomposition and its matching to the same-order EFT soft/contact graphs;
2. the additional \(O(M_E^{-4})\) soft insertions from \(Q_{LD}^{(8)},Q_{RD}^{(8)}\), \(C_5C_7^*\), VEV/wavefunction insertions, and source/current companions;
3. the common scalar/gauge EOM and integration-by-parts reduction of the transverse-current term and finite local remainder to a nonredundant dimension-eight basis;
4. UV parameter, field, and operator counterterms in the complete off-shell amplitude set;
5. independent FeynArts/FeynCalc or equivalent diagram-level validation.

No complete dimension-eight Wilson vector is claimed by this partial hard/soft closure.
