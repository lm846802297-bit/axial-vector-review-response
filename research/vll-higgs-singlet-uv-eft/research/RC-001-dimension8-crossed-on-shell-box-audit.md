# RC-001 — P0.1–P0.4: crossed on-shell dimension-eight box audit

**Status (2026-11-10):** P0.1–P0.4 are analytically closed for the on-shell pure-Higgs and pure-singlet four-scalar amplitudes at \(O(p^4/M_E^4)\), per ordered cycle. The crossed external pairing, weak-index tensors, exact chiral trace, direct soft expansion of the same UV numerator, and current/action normalization have been checked. A new finite local hard polynomial is identified beyond the transverse-current projection. The off-shell Green-basis decomposition, EOM/IBP reduction, and independent FeynArts/FeynCalc diagram generation remain open. No complete nonredundant dimension-eight Wilson vector is claimed.

The calculation factors out \(|y_\ell|^4\) or \(|\lambda_\ell|^4\) and uses the same Euclidean loop-kernel sign convention as research/RC-001-dimension8-y4-lambda4-hard-box-matching.md. All expressions below are per flavor and per ordered external pairing; the flavor sums and the second pairing are added explicitly.

## 1. External states and the two inequivalent pairings

Take all external momenta incoming and massless:
\[
p_i^2=0,\qquad p_1+p_2+p_3+p_4=0,
\]
\[
s=(p_1+p_2)^2,\qquad
t=(p_1+p_3)^2,\qquad
u=(p_1+p_4)^2,\qquad s+t+u=0.
\]

For external Higgs fields \(H_i(p_1),H_j^\dagger(p_2),H_k(p_3),H_l^\dagger(p_4)\), the alternating Yukawa vertices admit two inequivalent cyclic pairings:

1. \(s\)-pairing: \((p_1,p_2)\) and \((p_3,p_4)\), with weak tensor
   \[
   \delta_{jk}\delta_{li}.
   \]
2. Crossed \(u\)-pairing: \((p_1,p_4)\) and \((p_3,p_2)\), with weak tensor
   \[
   \delta_{lk}\delta_{ji}.
   \]

The crossed contribution is obtained from the first by \(p_2\leftrightarrow p_4\), equivalently \(s\leftrightarrow u\). Reversing the reading direction of a fixed fermion loop is not an additional graph. The two terms above are the two distinct external pairings, not an extra factor of two from the SU(2) doublet.

For the singlet channel \(S(p_1),S^\dagger(p_2),S(p_3),S^\dagger(p_4)\), the same two momentum pairings occur, but there is no weak-index tensor.

## 2. Complete on-shell hard-region polynomial

Use the one-cycle numerator
\[
\mathcal N
=2\left[(a\!\cdot b)(c\!\cdot d)
-(a\!\cdot c)(b\!\cdot d)
+(a\!\cdot d)(b\!\cdot c)\right],
\]
where
\[
a=k+p_1,\qquad b=k+q,\qquad c=k-p_4,\qquad d=k,\qquad q=p_1+p_2.
\]
This is the parity-even Weyl trace. The two light denominators are \(k^2,(k+q)^2\), and the two heavy denominators are \((k+p_1)^2+M_E^2,(k-p_4)^2+M_E^2\) in the Euclidean hard-region convention.

For the on-shell projection, write
\[
a_k=k\!\cdot p_1,\qquad b_k=k\!\cdot p_4,\qquad c_k=k\!\cdot q,\qquad K=k^2.
\]
The scalar products needed in the numerator are
\[
p_1\!\cdot p_4=\frac u2,\qquad
p_1\!\cdot q=\frac s2,\qquad
p_4\!\cdot q=-\frac s2,\qquad q^2=s.
\]
The hard denominator shifts are
\[
A=2c_k+s,\qquad B=2a_k,\qquad C=-2b_k.
\]

The complete degree-four external-momentum expansion is reduced with
\[
\left\langle\prod_{r=1}^{2n}(k\!\cdot v_r)\right\rangle
=
\frac{(k^2)^n}{d(d+2)\cdots(d+2n-2)}
\sum_{\text{pairings}}\prod (v_i\!\cdot v_j).
\]
Thirteen nonzero radial tensor structures remain. Their Gamma-function integrals, including the \(O(\epsilon)\) angular coefficients multiplying hard IR poles, give
\[
\boxed{
\mathcal H_{\rm hard}(s,u)
=
\frac{1}{96\pi^2M_E^4}
\left[
(s^2+2su)(\Delta_{\rm IR}-L_E)
+\frac{11}{6}s^2+\frac{10}{3}su-\frac{3}{10}u^2
\right],
}
\]
where
\[
L_E=\ln\frac{M_E^2}{\mu_R^2},\qquad
\Delta_{\rm IR}=\frac1{\epsilon_{\rm IR}}-\gamma_E+\ln4\pi.
\]
This is the complete on-shell polynomial for the chosen ordered cycle, not merely its transverse-current projection.

## 3. Direct soft expansion of the same UV numerator

In the soft region the two heavy propagators start at \(1/M_E^4\). Combine the two massless denominators with a Feynman parameter and shift \(k=l-xq\). The \(P\!\cdot P'\) projection, with \(P\cdot q=P'\cdot q=0\), contains
\[
2x(1-x)q^2+\left(\frac4d-2\right)l^2.
\]
The \(l^2\) term is essential. Since
\[
\frac{\displaystyle\int_l l^2/(l^2+\Delta)^2}
{\displaystyle\int_l 1/(l^2+\Delta)^2}
=\frac{d}{2-d}\Delta,\qquad \Delta=x(1-x)q^2,
\]
the two terms combine exactly to \(4x(1-x)q^2\). The direct soft integral of the UV box therefore reproduces the one-Weyl transverse-current kernel, including the finite \(+5/3\):
\[
\boxed{
\mathcal H_{\rm soft}(s,u)
=
-\frac{s^2+2su}{96\pi^2M_E^4}
\left[
\Delta_{\rm UV}-\ln\frac{s}{\mu_R^2}+\frac53
\right].
}
\]
Here
\[
\Delta_{\rm UV}=\frac1{\epsilon_{\rm UV}}-\gamma_E+\ln4\pi.
\]
The hard IR and soft UV residues cancel:
\[
\operatorname{Res}_{\rm IR}\mathcal H_{\rm hard}
+\operatorname{Res}_{\rm UV}\mathcal H_{\rm soft}=0.
\]
This is a direct method-of-regions check on the same UV numerator, rather than a comparison between separately normalized formulae.

## 4. Matched on-shell result and the extra local hard term

Adding the hard and soft regions gives
\[
\boxed{
\mathcal H_{\rm matched}(s,u)
=
\frac{1}{96\pi^2M_E^4}
\left[
-(s^2+2su)\left(\ln\frac{M_E^2}{s}+\frac53\right)
+\frac{11}{6}s^2+\frac{10}{3}su-\frac{3}{10}u^2
\right].
}
\]
The arbitrary matching scale \(\mu_R\) cancels.

The transverse-current projection from the earlier calculation is
\[
P_\mu T^{\mu\nu}(q)P'_\nu
=-\frac{s^2+2su}{4},
\]
and its hard part is
\[
\mathcal H_{\rm hard}^{T}(s,u)
=
\frac{s^2+2su}{96\pi^2M_E^4}
\left[
\Delta_{\rm IR}-L_E+\frac{17}{12}
\right].
\]
The direct soft contribution is entirely this transverse-current structure. However, the complete on-shell hard box also contains the finite local remainder
\[
\boxed{
\mathcal H_{\rm hard}^{\rm local,\,rem}(s,u)
=
\frac{1}{96\pi^2M_E^4}
\left[
\frac{5}{12}s^2+\frac12 su-\frac{3}{10}u^2
\right].
}
\]
It has no pole and no nonlocal logarithm. It is not included in the previously quoted \(c_{8,H}^{\rm hard}\) or \(c_{8,S}^{\rm hard}\), which remain the coefficients of the transverse-current Green-basis projection only. The remainder must be retained when constructing the full dimension-eight local operator basis; it is not assigned to a specific nonredundant operator before the off-shell EOM/IBP reduction.

## 5. Crossed channel, weak indices, and flavor sums

The crossed \(u\)-pairing is obtained by
\[
\mathcal H(s,u)\longrightarrow\mathcal H(u,s).
\]
The complete Higgs amplitude for one flavor is therefore proportional to
\[
\delta_{jk}\delta_{li}\,\mathcal H(s,u)
+\delta_{lk}\delta_{ji}\,\mathcal H(u,s).
\]
The SU(2) contractions follow directly from
\[
\operatorname{tr}_2[\mathcal J_{H,ij}\mathcal J_{H,ji}].
\]
For a fixed neutral Higgs component, each allowed pairing has unit weak factor; there is no additional factor of two from summing over the doublet. The two terms are distinct kinematic pairings.

For the pure-Higgs channel, sum the independent flavors with weights
\[
\sum_{\ell=\mu,\tau}\frac{|y_\ell|^4}{M_{E\ell}^4}.
\]
For the pure-singlet channel, replace \(|y_\ell|^4\) by \(|\lambda_\ell|^4\) and omit the weak tensors. Since \(S_\tau=S^*\), the \(\tau\)-flavor current obeys \(j_{S_\tau}=-j_S\), but the quadratic current kernel is unchanged. There are no \(\mu\)-\(\tau\) cross terms without flavor-mixing insertions.

The summed \(s\)- and \(u\)-channel amplitudes are invariant under \(s\leftrightarrow u\).

## 6. Exact chiral trace and current normalization

The explicit chiral chain satisfies
\[
\operatorname{Tr}
\left[
P_R\slashed a P_L\slashed b P_R\slashed c P_L\slashed d P_R
\right]
=
\frac12\operatorname{Tr}
\left[
\slashed a\slashed b\slashed c\slashed d(1+\gamma_5)
\right].
\]
Its parity-even part is one half of the Dirac trace, giving the numerator used above. The \(\gamma_5\)-odd term vanishes after loop integration: only three independent external vectors \(p_1,p_4,q\) remain, and symmetric tensor integration cannot generate a fourth independent vector.

For the EFT current representation,
\[
Q_{LD}\doteq\frac12\mathcal J_H^\mu J_{L,\mu}+\cdots.
\]
The one-Weyl polarization has coefficient \(1/(24\pi^2)\). The effective-action coefficient contains
\[
\frac12\left(\frac12\right)^2\frac1{24\pi^2}
=\frac1{192\pi^2},
\]
where the first \(1/2\) is the determinant expansion and the two further factors are the EOM-current reductions. Functional differentiation of the two currents gives two assignments, while each scalar-current matrix element is \(J_H=-2P\). Thus the four-scalar amplitude coefficient is
\[
2\times 4\times\frac1{192\pi^2}
=\frac1{24\pi^2},
\]
exactly the coefficient obtained by the direct soft expansion of the UV box. This resolves the apparent factor-of-two ambiguity between the current correlator, the effective action, and the fixed-pairing four-point amplitude.

## 7. Reproducibility and acceptance boundary

The full on-shell hard/soft tensor expansion, Gamma-function integrals, crossed-channel relabeling, SU(2) contractions, exact chiral trace, and current-normalization checks are implemented in:
- calculations/RC-001-dimension8-crossed-on-shell-box-audit.py
- validation/RC-001-dimension8-crossed-on-shell-box-audit.txt

**Closed by P0.1–P0.4:** both on-shell external pairings; pure-Higgs and pure-singlet loop structures; the two SU(2) tensors and absence of an extra doublet multiplicity; the parity-even chiral trace; direct hard/soft pole cancellation; and the current/action/amplitude normalization.

**Still open:** the complete off-shell four-scalar Green-function tensor decomposition; mapping the additional finite local polynomial and the transverse-current term into a common nonredundant dimension-eight basis; scalar/gauge EOM and integration-by-parts reduction; and independent FeynArts/FeynCalc or equivalent diagram generation. No complete dimension-eight Wilson vector is claimed.
