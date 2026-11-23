# RC-001 — Nonexceptional kinematics and local-projector prescription for dimension-six gauge matching

**Status:** the fixed-routing, unit-multiplicity pure-WW cross-box triplet sub-block now has a nonexceptional EFT-soft UV residue, a d-dimensional hard-region expansion, and a finite local hard polynomial. This is not the complete gauge-corrected Wilson coefficient.

## 1. Why the existing zero-momentum routing is not the final subtraction prescription

The fixed-routing WW cross-box calculation uses an exceptional local projection with two external momenta set to zero. It is useful for deriving the hard local numerator and for an expansion-by-regions diagnostic, but massless UV and EFT subgraphs can then contain overlapping UV/IR poles. The formal cancellation of the labeled \(\Delta_{\rm UV}\) terms in the scalar-master split is not, by itself, a complete \(R^*\) subtraction or a proof that every IR pole has been identified.

The UV and EFT amplitudes must ultimately be evaluated with identical nonexceptional external momenta, gauge fixing, regulator, field normalization, and tensor projectors. The same local operator coefficient is then extracted from their difference.

## 2. Symmetric nonexceptional four-point Euclidean point

Take all four external momenta incoming, with
\[
p_1+p_2+p_3+p_4=0,
\]
where the ordering is \(\bar L(p_1),H(p_2),H^\dagger(p_3),L(p_4)\). Choose the symmetric Euclidean point
\[
p_i^2=\mu_{\rm IR}^2,\qquad
p_i\cdot p_j=-\frac{\mu_{\rm IR}^2}{3}\quad(i\ne j).
\]
It follows that every two-particle channel is nonexceptional:
\[
(p_i+p_j)^2=\frac{4\mu_{\rm IR}^2}{3}\quad(i\ne j).
\]
The \(4\times4\) Gram matrix has one zero eigenvalue corresponding to momentum conservation and three positive eigenvalues \((4/3,4/3,1/3)\mu_{\rm IR}^2\). Thus no external leg or two-particle channel carries zero momentum. Analytic continuation to Minkowski signature is made only after the Euclidean tensor projection is defined.

Keep \(\mu_{\rm IR}^2\ll M_E^2\), expand the UV amplitude in \(\mu_{\rm IR}^2/M_E^2\), and retain the dimension-six local terms. The EFT is evaluated at the same point without changing the IR prescription.

## 3. Weak and Lorentz tensor projection

Keep the weak tensors separate:
\[
T_0=\delta_{ij}\delta_{kl},\qquad
T_3=2\delta_{il}\delta_{kj}-\delta_{ij}\delta_{kl}.
\]
Do not project onto a single Warsaw-basis current before the complete UV-minus-EFT amplitude is assembled.

For the local UV-pole polynomial, choose three independent momenta, e.g. \(p_1,p_2,p_3\), and retain
\[
\mathcal M_T^{\rm local}=
\bar u(p_1)\left[
F_{1,T}\slashed p_1+
F_{2,T}\slashed p_2+
F_{3,T}\slashed p_3
\right]P_Lu(p_4),
\qquad T=T_0,T_3.
\]
No external Dirac equation is imposed at the projection stage. The \(3\times3\) Gram matrix
\[
G_{ab}=p_a\cdot p_b,\qquad a,b=1,2,3,
\]
is invertible at the symmetric point, with
\[
\det G=\frac{16}{27}\mu_{\rm IR}^6.
\]
Thus the three local momentum structures can be projected independently. The actual Dirac trace projectors must be constructed with the same \(d\)-dimensional gamma algebra and chiral convention in the UV and EFT calculations.

For the **full off-shell amplitude**, do not assume that these three structures exhaust the tensor basis. The fixed-routing four-cross-box soft calculation below contains a finite rank-three antisymmetric gamma structure. In four dimensions it is dual to a pseudovector
\[
p_\perp^\mu=\epsilon^{\mu\nu\rho\sigma}
p_{1\nu}p_{2\rho}p_{3\sigma},
\qquad p_\perp\cdot p_i=0,
\]
so the chiral amplitude can contain an additional \(\slashed p_\perp P_L\) form factor. In a genuinely \(d\)-dimensional subtraction, retain \(\gamma^{[\mu\nu\rho]}\) as an independent antisymmetric-gamma structure and postpone four-dimensional epsilon duality until after UV–EFT subtraction. The local UV pole found below has no such rank-three component; the nonzero term is finite and nonlocal.

### 3.1 Generalized routing and nonexceptional soft triangles

For the four cross-vertex classes, the general heavy momentum is
\[
q_E=k-p_1-p_2,
\]
not merely \(k-p_2\). The latter is recovered only in the old exceptional projection \(p_1=0\). With all momenta incoming, the two light-line shifts and the third triangle invariant are:

| Pair | \(a,b\) in \(k^2(k+a)^2(k+b)^2\) | \((a-b)^2\) at the symmetric point |
|---|---|---:|
| LD-W-01 | \(-p_1,\ p_4\) | \(4\mu_{\rm IR}^2/3\) |
| LD-W-02 | \(-p_1,\ p_3\) | \(4\mu_{\rm IR}^2/3\) |
| LD-W-05 | \(-p_2,\ p_4\) | \(4\mu_{\rm IR}^2/3\) |
| LD-W-06 | \(-p_2,\ p_3\) | \(4\mu_{\rm IR}^2/3\) |

All four soft denominators therefore reduce to the same massless triangle family, with
\[
a^2=b^2=\mu_{\rm IR}^2,\qquad
(a-b)^2=\frac43\mu_{\rm IR}^2.
\]
The scalar triangle master is
\[
I_3=\frac{1}{16\pi^2\mu_{\rm IR}^2}\,T\!\left(\frac43\right),
\qquad
T(r)=\int_0^1dt\,
\frac{-\ln[r\,t(1-t)]}{1-r\,t(1-t)},
\]
and
\[
T(4/3)=2.124033948003819155075451589888473217478\ldots.
\]

### 3.2 Nonexceptional EFT-soft UV pole

Expanding the heavy denominator in the soft region gives
\[
\frac{1}{(k-p_1-p_2)^2-M_E^2}
=-\frac1{M_E^2}+O(M_E^{-4}).
\] The EFT insertion \(Q_{LD}=(\bar L H)i\slashed D(H^\dagger L)\) differentiates the composite \(H^\dagger L\), whose momentum in these loop routings is
\[
q_D=p_3+p_4+k=k-p_1-p_2=q_E.
\]
The \(SU(2)_L\)-singlet composite has no direct one-\(W\) derivative contact. Constructing the four EFT numerators from this derivative momentum and the ordinary fermion/scalar \(W\) vertices reproduces the soft-expanded UV numerator **pair by pair**, with zero symbolic residual for LD-W-01/02/05/06. This is an integrand-level UV-soft/EFT identity for this cross-box subset, not yet the full amplitude or Ward sum.
The four numerator chains were reconstructed with the general shifts above. Feynman parametrization and the \(d\to4\) UV tensor residue give the following stripped coefficients of \(1/(16\pi^2\epsilon_{\rm UV})\), before the common heavy factor \(-1/M_E^2\), in the ordered basis \((\slashed p_1,\slashed p_2,\slashed p_3)P_L\):
\[
\begin{array}{c|rrr}
\text{pair}&p_1&p_2&p_3\\ \hline
01&-1&0&-1\\
02&0&-1&3/2\\
05&0&3/2&1/2\\
06&-1&-1&0
\end{array}
\]
Applying the weak-triplet weights \((-1,+1,+1,-1)/4\) gives
\[
\boxed{
R_{T_3}^{\rm soft}
=\frac12\slashed p_1+
\frac38\slashed p_2+
\frac34\slashed p_3.
}
\]
Thus, with the leading heavy propagator included,
\[
\left.\mathcal M_{T_3}^{\rm EFT,soft}\right|_{\rm UV}
=-\frac{g_2^2|y_\ell|^2}{16\pi^2M_E^2}
\frac{1}{\epsilon_{\rm UV}}\,
\bar u(p_1)R_{T_3}^{\rm soft}P_Lu(p_4),
\]
up to the common overall Feynman-rule phase. The exceptional limit \(p_1=p_3=0,\ p_2=P\) gives \(R_{T_3}^{\rm soft}=3\slashed P/8\), exactly reproducing the pole coefficient in the previous scalar-master calculation. At nonexceptional momenta there is no separate \(\Delta_{\rm IR}\) pole: it is replaced by finite functions of the nonzero external invariants. The UV residue is unchanged.

### 3.3 Finite rank-three/pseudovector soft form factor

The four-dimensional chiral projection of the finite scalar-triangle part has a nonzero component orthogonal to the span of \(p_1,p_2,p_3\). Its parameter-space numerator is
\[
c_\perp(y,z)=\frac{\sqrt3}{9}(y+3z-2).
\]
Since the symmetric-point denominator is invariant under \(y\leftrightarrow z\), its symmetric part is
\[
c_\perp^{\rm sym}(y,z)
=-\frac{2\sqrt3}{9}(1-y-z).
\]
Define
\[
I_\epsilon(r)=\int_0^1dt\left[
\frac{1}{1-a(t)}
+\frac{a(t)\ln a(t)}{[1-a(t)]^2}
\right],
\qquad a(t)=r\,t(1-t).
\]
At \(r=4/3\),
\[
I_\epsilon(4/3)=0.7467700413397904843482771519674888779972\ldots.
\]
With \(p_\perp^2=\det G=16\mu_{\rm IR}^6/27\), the stripped coefficient of \(\slashed p_\perp P_L\) is
\[
F_\perp^{\rm soft,stripped}
=-\frac{I_\epsilon(4/3)}{32\pi^2\mu_{\rm IR}^2}.
\]
The leading heavy factor \(-1/M_E^2\) reverses this sign. The \(1/\mu_{\rm IR}^2\) dependence makes this a nonlocal soft form factor, not a local Wilson coefficient. For this fixed cross-box subset, the soft-expanded UV integrand and the EFT \(Q_{LD}\) insertion have the same three light denominators and the same numerator after using \(p_1+p_2+p_3+p_4=0\). Consequently this rank-three nonlocal term, together with the other soft form factors, cancels in the UV-minus-EFT difference for this subset. This is the expected expansion-by-regions identity, not a cancellation between unrelated diagrams; the other routing and Ward-completing graphs remain open.

The exact residue and parameter-polynomial checks are in calculations/RC-001-dim6-WW-nonexceptional-soft-pole.py; the nine regression cases are in calculations/test_RC001_dim6_WW_nonexceptional_soft_pole.py. The scalar triangle and epsilon-moment numerical values are recorded in validation/RC-001-dim6-WW-nonexceptional-soft-pole.txt. The UV-soft/EFT numerator equality is an algebraic routing identity using the derivative momentum, not an independent diagram-generator validation. The checked-in unittest file is a regression artifact and is not represented as a GitHub Actions pass.

### 3.4 Nonexceptional hard-region expansion and local matching polynomial

The hard region keeps the full heavy propagator and expands the two shifted light propagators and the heavy momentum to first order in the external momenta. With
\[
J=\int\frac{d^dk}{(2\pi)^d}\frac{1}{(k^2)^2(k^2-M_E^2)},\qquad
K=\int\frac{d^dk}{(2\pi)^d}\frac{1}{k^2(k^2-M_E^2)^2},
\]
the d-dimensional numerator and tensor reduction give:

| Pair | coefficient of \(J\) | coefficient of \(K\) |
|---|---|---|
| LD-W-01 | \(\frac{(d-2)^2}{d}(p_2+p_4)\) | \(\frac{2(d-2)}d(p_1+p_2)\) |
| LD-W-02 | \(-p_2+2(1-\frac1d)p_3\) | \(\frac2d(p_1+p_2)\) |
| LD-W-05 | \(2(1-\frac1d)p_2+(1-\frac2d)p_3\) | \(-\frac2d(p_1+p_2)\) |
| LD-W-06 | \(-(p_1+p_2)\) | \(\frac2d(p_1+p_2)\) |

The LD-W-01 chain uses
\[
\gamma_\mu\slashed a\slashed b\slashed c\gamma^\mu
=-2\slashed c\slashed b\slashed a+(4-d)\slashed a\slashed b\slashed c,
\]
and the loop tensors use
\[
\langle k_\mu k_\nu\rangle=\frac{k^2}{d}g_{\mu\nu},\qquad
\langle k_\mu k_\nu k_\rho k_\sigma\rangle
=\frac{k^4}{d(d+2)}
(g_{\mu\nu}g_{\rho\sigma}+g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}).
\]
No four-dimensional epsilon duality is needed for this local hard polynomial.

Applying the same triplet weights \((-1,+1,+1,-1)/4\) and then imposing momentum conservation gives
\[
R_J(d)=
\frac{d^2-3d+4}{4d}p_1+
\frac{d-1}{2d}p_2+
\frac{d-1}{4}p_3,
\qquad
R_K(d)=-\frac{d-1}{2d}(p_1+p_2).
\]
The exceptional limit \(p_1=p_3=0,\ p_2=P,\ p_4=-P\) reproduces the previous four pair kernels exactly and yields
\[
R_J= \frac{d-1}{2d}P,\qquad
R_K=-\frac{d-1}{2d}P,
\]
i.e. \((d-1)(J-K)/(2d)\).

Using the checked hard masters
\[
J_{\rm hard}=\frac{\Delta_{\rm UV}+1-L}{M_E^2},\qquad
K_{\rm hard}=-\frac1{M_E^2},\qquad
L=\ln\frac{M_E^2}{\mu_R^2},
\]
and expanding \(d=4-2\epsilon\), one finds
\[
R_J=
\left(\frac12-\frac{3\epsilon}{8}\right)p_1+
\left(\frac38-\frac{\epsilon}{16}\right)p_2+
\left(\frac34-\frac{\epsilon}{2}\right)p_3,
\]
\[
R_K=\left(-\frac38+\frac{\epsilon}{16}\right)(p_1+p_2).
\]
The hard-region pole is
\[
\left.\mathcal M_{T_3}^{\rm hard}\right|_{\rm pole}
=\frac{g_2^2|y_\ell|^2}{16\pi^2M_E^2\epsilon_{\rm UV}}\,
\bar u(p_1)\left(
\frac12\slashed p_1+\frac38\slashed p_2+\frac34\slashed p_3
\right)P_Lu(p_4),
\]
which cancels the EFT-soft UV pole in §3.2 with the opposite sign. This is an explicit nonexceptional pole closure for the four cross-vertex classes at fixed routing and unit multiplicity.

After \(\overline{\rm MS}\) subtraction, the finite local hard polynomial is
\[
\boxed{
C_{\rm hard}^{\rm fin}=
\left(\frac12-\frac L2\right)\slashed p_1+
\left(\frac{11}{16}-\frac{3L}{8}\right)\slashed p_2+
\left(\frac14-\frac{3L}{4}\right)\slashed p_3.
}
\]
At \(\mu_R=M_E\), its coefficients are \((1/2,11/16,1/4)\). The \(p_2\) coefficient reduces to the previously obtained \(11/16\) in the exceptional projection. The \(O(\epsilon)\) terms in \(R_J\) are essential: in particular, \(-\epsilon/16\) multiplying the pole gives the familiar \(-1/16\) finite shift.

The analytic kernels and expansion are in calculations/RC-001-dim6-WW-nonexceptional-hard-expansion.py; eight regression tests are in calculations/test_RC001_dim6_WW_nonexceptional_hard_expansion.py; captured coefficients are in validation/RC-001-dim6-WW-nonexceptional-hard-expansion.txt. A separate explicit 4D Dirac-matrix implementation reproduces all four d=4 pair kernels; its source/output are calculations/RC-001-dim6-WW-hard-explicit-4d-crosscheck.py and validation/RC-001-dim6-WW-hard-explicit-4d-crosscheck.txt. These are analytic numerator/tensor reductions for a fixed sub-block, not a generated complete diagram set or a full basis-matched Wilson coefficient.

### 3.5 Six-pair internal-\(W\) hard-matching summary

The two same-Yukawa-vertex classes LD-W-03/04 are pure-soft at \(O(M_E^{-2})\), as shown in research/RC-001-dim6-WW-same-vertex-soft-matching.md. Their W-loop denominators contain only light propagators, the heavy propagator carries only the external channel momentum \(P=p_1+p_2\), and the chiral heavy numerator reduces to \(-\slashed P/M_E^2\). The EFT derivative momentum is \(q_D=p_3+p_4=-P\), so the light-loop form factor is reproduced exactly. Their hard-region loop integrals are scaleless and the hard-minus-EFT contribution is zero.

Combining these two singlet-tensor pure-soft classes with the four cross-vertex triplet classes gives the following fixed-ordering internal-\(W\) result:
\[
\boxed{
C_{\rm hard}^{WW,\rm internal}=
\left(\frac12-\frac L2\right)\slashed p_1+
\left(\frac{11}{16}-\frac{3L}{8}\right)\slashed p_2+
\left(\frac14-\frac{3L}{4}\right)\slashed p_3,
\qquad
L=\ln\frac{M_E^2}{\mu_R^2}.
}
\]
Only the cross-vertex classes contribute to this hard polynomial; the same-vertex singlet contribution is zero. At \(\mu_R=M_E\), the coefficient vector is \((1/2,11/16,1/4)\). The assembly script and output are calculations/RC-001-dim6-WW-six-pair-hard-summary.py and validation/RC-001-dim6-WW-six-pair-hard-summary.txt.

This closes the hard/soft analysis of the six internal-\(W\) line-pair classes for one fixed ordered tree exchange and unit multiplicity. It does **not** close the full renormalized \(WW\) four-point amplitude: external-field and parameter/operator counterterms, the external-\(W\) five-point form factor, the complete Slavnov–Taylor sum, and the common EOM/IBP operator-basis projection remain open. No complete \(Q_{LD}\) Wilson coefficient is claimed.

### 3.6 Off-shell momentum-basis decomposition of the hard polynomial

The finite hard polynomial can be decomposed into three independent momentum vectors without yet assigning all of them to named operators. Define
\[
v_D=p_3+p_4=-(p_1+p_2),\qquad
v_-=p_2-p_3,\qquad
v_+=p_2+p_3.
\]
Then
\[
C_{\rm hard}^{\rm fin}=a\,v_D+b\,v_-+c\,v_+,
\]
with
\[
\boxed{
a=-\frac12+\frac L2,\qquad
b=-\frac1{32}+\frac{7L}{16},\qquad
c=\frac7{32}-\frac{5L}{16}.
}
\]
At \(\mu_R=M_E\), \((a,b,c)=(-1/2,-1/32,7/32)\). The \(v_D\) direction is the derivative momentum of the triplet \(Q_{LD}^{(3)}\) representative. The other two are retained as independent off-shell form-factor directions; they are not assigned to Warsaw-basis operators before the weak-index, total-derivative, EOM/source, and full-amplitude reductions are performed. The exact linear-algebra check is in calculations/RC-001-dim6-WW-offshell-formfactor-decomposition.py with output validation/RC-001-dim6-WW-offshell-formfactor-decomposition.txt.

### 3.7 Matching-scale logarithm and pole consistency

For the hard polynomial in §3.4, the coefficient of \(L=\ln(M_E^2/\mu_R^2)\) is
\[
-\left(\frac12p_1+\frac38p_2+\frac34p_3\right)=-R_{\rm pole}.
\]
Since \(dL/d\ln\mu_R=-2\),
\[
\frac{d C_{\rm hard}^{\rm fin}}{d\ln\mu_R}
=2R_{\rm pole}
=p_1+\frac34p_2+\frac32p_3.
\]
Thus the matching logarithm is fixed by the same nonexceptional pole residue that cancels the EFT-soft UV pole. The exceptional projection again gives \(11/16-3L/8\). The exact symbolic check is in calculations/RC-001-dim6-WW-hard-scale-dependence.py with output validation/RC-001-dim6-WW-hard-scale-dependence.txt. This is a sub-block pole/log consistency relation, not the full EFT RG cancellation; the latter requires the complete operator-mixing and counterterm matrix.

## 4. UV–EFT and \(R^*\) bookkeeping

For each attachment class, record before simplification:
1. the UV integrand and its weak/Dirac numerator;
2. the EFT insertion graph, including the covariant-derivative contact term where present;
3. the UV and IR pole labels separately;
4. the UV parameter, field, and operator counterterms;
5. the projected finite local polynomial at the symmetric point.

If an auxiliary-mass or infrared-rearrangement version is used to simplify a UV pole, apply the same rearrangement to the UV and EFT graphs and include the required IR counterterm forests. A scaleless integral is never set to zero before its UV and IR parts have been separated. The nonexceptional point is the primary common-regulator check; \(R^*\) is an independent UV-pole extraction route, not a replacement for the full finite UV–EFT difference.

## 5. Immediate calculation order

1. Reproduce the fixed-routing Feynman-gauge WW box numerator with the nonexceptional momentum assignment before expanding in external momenta.
2. Construct and test the three Lorentz projectors and the \(T_0/T_3\) weak projectors independently.
3. Generate the matching EFT \(Q_{LD}\) insertion graphs; for the \(T_3\) derivative representative include the adjoint-covariant one-\(W\) contact already recorded in the current-form-factor atlas.
4. Compare UV and EFT pole residues at the same \(\mu_{\rm IR}\), before adding counterterms.
5. Add the parameter/operator counterterms once, then extract the local hard coefficient.
6. Only after the four-point subtraction closes, calculate the independent external-\(W\) five-point form factor and test the full Slavnov–Taylor identity.

## 6. Evidence boundary

This file fixes a reproducible kinematic and projection prescription. It does not claim that the nonexceptional loop integrals, EFT contact graphs, \(R^*\) forests, or one-\(W\) form factors have been evaluated. The fixed-routing \(11/16\) result remains a hard sub-block under its stated exceptional projection and is not promoted to a complete Wilson coefficient.
