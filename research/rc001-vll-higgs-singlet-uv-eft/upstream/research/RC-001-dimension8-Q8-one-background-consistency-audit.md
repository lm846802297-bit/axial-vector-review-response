# RC-001 — Q8 one-background Ward consistency and corrected tensor reduction

**Status (2026-11-10):** the apparent conflict between the ordinary-line Ward contraction and its UV residue is resolved. The earlier tensor reduction omitted loop components transverse to the external \(q,r\) plane. A covariant \(d\)-dimensional angular average gives a transverse ordinary-line pole. The contact-graph angular average has also been corrected. Full R* subtraction and UV-hard matching remain open.

## 1. Exact ordinary-line contraction

Let \(a=k+r\), \(b=k+q\). The numerator is
\[
N^\mu=4a^2[b^\mu(k\cdot a)-(b\cdot k)a^\mu+(b\cdot a)k^\mu].
\]
Using \(q=b-k\),
\[
q_\mu N^\mu=4a^2[b^2(k\cdot a)-k^2(b\cdot a)].
\]
Hence
\[
\frac{q_\mu N^\mu}{k^2b^2}
=4(k+r)^2\left[\frac{k\cdot(k+r)}{k^2}
-\frac{(k+q)\cdot(k+r)}{(k+q)^2}\right].
\]
A translation-invariant shift in the second term turns the integral into a difference of massless one-propagator tadpole integrals. The complete dimensionally regulated longitudinal integral vanishes. This identity is an integrand-level check and is retained.

## 2. Source of the previous discrepancy

The earlier calculation placed \(q\) and \(r\) in a two-dimensional coordinate plane but evaluated scalar factors such as \((k+r)^2\) using only the two displayed loop components. In \(d=4-2\epsilon\), the remaining \(d-2\) transverse components contribute to \(l^2\) and to all angular averages. Omitting them corrupts the coefficients of \(L=l^2\) and \(L^2\), and produced a spurious nonzero longitudinal pole.

The old planar result is superseded. The corrected script uses invariant variables \(L=l^2\), \(u=l\cdot q\), \(v=l\cdot r\) and full \(d\)-dimensional tensor moments.

## 3. Corrected ordinary-line UV residue

The covariant reduction gives
\[
\langle N^\mu\rangle
=[A_0+A_2L+A_4L^2]q^\mu+
[B_0+B_2L+B_4L^2]r^\mu.
\]
The parameter-integrated coefficients are
\[
A_{\rm UV}=\frac43(q\cdot r)[q\cdot r-r^2],\qquad
B_{\rm UV}=-\frac43q^2[q\cdot r-r^2].
\]
Therefore
\[
\boxed{
\mathcal I_{\rm line}^{\mu}\big|_{\rm UV}
=\frac{1}{16\pi^2\epsilon}\frac43(q\cdot r-r^2)
[(q\cdot r)q^\mu-q^2r^\mu].
}
\]
It obeys
\[
q_\mu\mathcal I_{\rm line}^{\mu}\big|_{\rm UV}=0.
\]
This is the ordinary-line graph only, with \(\operatorname{tr}\mathbf1=4\) included and overall Wilson/gauge factors omitted. It is not yet the full Q8 soft pole or a matched Wilson coefficient.

Reproduction: calculations/RC-001-dimension8-Q8-one-background-line-pole-covariant.py. Recorded output: validation/RC-001-dimension8-Q8-one-background-line-pole-covariant.txt.

## 4. Corrected Q8 contact angular average

For
\[
N_{\rm ct}^\mu=4[(P'^2+P^2-P'\cdot P)k^\mu
+(k\cdot P')P^\mu+(k\cdot P)P'^\mu],
\quad P=k+r,\quad P'=k+r+q,
\]
the full \(d\)-dimensional angular average is
\[
\boxed{
\langle N_{\rm ct}^\mu\rangle
=4\,l^2\,\frac{d+2}{d}(q^\mu+2r^\mu).
}
\]
This corrects the earlier coefficient \(16l^2/d\), which came from the same incomplete planar averaging. After division by the single massless propagator, the integral is scaleless in dimensional regularization. With an auxiliary mass, its UV pole is proportional to a positive power of that auxiliary mass and vanishes as the regulator is removed. A common R* prescription is still needed to document the UV/IR split rigorously.

Reproduction: calculations/RC-001-dimension8-Q8-one-background-consistency-audit.py. Recorded output: validation/RC-001-dimension8-Q8-one-background-consistency-audit.txt.

## 4A. Auxiliary-mass IR rearrangement for the contact tadpole

As a concrete common IR regulator, replace the single massless denominator in the contact graph by \(k^2+m_{\rm IR}^2\). The covariant angular average gives
\[
\mathcal I_{\rm ct}^\mu(m_{\rm IR})
=4\frac{d+2}{d}(q^\mu+2r^\mu)
\mu^{2\epsilon}\int\frac{d^dk}{(2\pi)^d}
\frac{k^2}{k^2+m_{\rm IR}^2}.
\]
Using \(\int 1=0\) in dimensional regularization,
\[
\int\frac{d^dk}{(2\pi)^d}\frac{k^2}{k^2+m^2}
=-m^2\int\frac{d^dk}{(2\pi)^d}\frac{1}{k^2+m^2},
\]
and therefore, in the stated Euclidean convention,
\[
\left.\mathcal I_{\rm ct}^\mu(m_{\rm IR})\right|_{\rm UV}
=\frac{1}{16\pi^2\epsilon}\,
6m_{\rm IR}^4(q^\mu+2r^\mu)+O(\epsilon^0).
\]
This pole vanishes as \(m_{\rm IR}\to0\). It is an auxiliary-mass artifact proportional to the fourth power of the IR regulator, not a mass-independent dimension-eight counterterm. The same \(m_{\rm IR}\) can be used in both fermion denominators of the line graph; the mass-independent part of its UV pole is the transverse polynomial in §4E, while regulator-dependent terms carry positive powers of \(m_{\rm IR}\) and are discarded after the R* subtraction.

This explicit mass-regulated tadpole check does not replace the full R* forest subtraction if additional subdivergences or operator insertions are present. It does show that the one-propagator contact tadpole does not contribute a mass-independent UV pole in this projection.

## 4B. R* consistency: nonexceptional line bubble versus scaleless contact tadpole

The ordinary-line graph has two massless denominators \(k^2(k+q)^2\). Keeping a nonexceptional Euclidean background momentum \(q^2>0\) makes this bubble IR finite in four dimensions; its UV pole is therefore extracted directly from the \(J_0,J_1,J_2\) masters without introducing a fermion mass that would break the chiral gauge representation. The full covariant reduction is independently re-evaluated and gives
\[
A_{\rm UV}=\frac43(q\cdot r)(q\cdot r-r^2),\qquad
B_{\rm UV}=-\frac43q^2(q\cdot r-r^2),
\]
so the line pole remains transverse.

The one-propagator contact tadpole has no denominator carrying the nonexceptional external momentum. It remains scaleless and needs an R* infrared subtraction. The auxiliary-mass rearrangement in §4A is used only to expose its UV/IR content; it is **not** inserted into the chiral fermion propagators of the line graph. This distinction is deliberate: naively replacing each chiral fermion denominator by \(k^2+m_{\rm IR}^2\) while leaving the massless numerator and gauge vertex unchanged would violate the fermion Ward identity and is not an acceptable common regulator.

For the contact graph the auxiliary-mass UV residue is \(6m_{\rm IR}^4(q^\mu+2r^\mu)/(16\pi^2\epsilon)\), which vanishes in the massless limit. Thus this projection has no mass-independent contact UV pole. The line and contact pieces are treated within one R* subtraction framework, but not by imposing an identical mass deformation on both topologies.

**Scope of this conclusion:** the one-background, two-scalar projection only. The full scalar-source functional Ward identity, including the transformations of both external scalar legs and the complete \(Q_{LD}\)/\(Q_{RD}\) constituent attachments, must still be derived from the same functional determinant before the result is promoted to a complete gauge-covariant Green function.

## 4C. Functional Ward identity for the scalar two-point projection

For a complex scalar constituent \(\phi\) of charge \(Q_\phi\), background gauge invariance of the renormalized effective action implies, in momentum space and with all momenta incoming,
\[
q_\mu\Gamma^\mu_{A\phi^\dagger\phi}(p+q,p)
=gQ_\phi\left[\Gamma_{\phi^\dagger\phi}(p+q)
-\Gamma_{\phi^\dagger\phi}(p)\right],
\]
up to the overall \(i\)-convention used for the 1PI vertices. The right-hand side is the difference of the scalar two-point 1PI function at the two scalar momenta. In the massless unbroken-phase single-Q8-insertion projection, that two-point function is the scaleless one-propagator fermion tadpole and vanishes in dimensional regularization. Thus the pole-level target is
\[
q_\mu\Gamma^\mu_{A\phi^\dagger\phi}\big|_{\rm UV}=0.
\]
The corrected ordinary-line pole satisfies this identity. The contact graph has no mass-independent UV pole after its R* infrared subtraction, so it does not alter this pole-level check.

This is a Ward-identity check for the restricted scalar two-point projection and its one-background derivative. It is not a substitute for deriving the complete \(Q_{LD}\) and \(Q_{RD}\) functional identities with all constituent fields, flavor charges, and non-Abelian Slavnov–Taylor terms. Those remain part of the full Green-basis matching.

## 4D. Charge-resolved interpretation and UV-hard graph census

The transverse result in §3 is only the ordinary-line subgraph with the light-fermion gauge charge factored out. It must not be identified with the complete \(Q_{LD}\) or \(Q_{RD}\) background vertex.

For \(Q_{LD}\), the gauge charge on the light doublet line is
\[
q_{L,Y}=-\frac12,\qquad q_{L,X}=\eta_\ell Q_\ell,
\]
whereas the composite source charge is
\[
q_{\Psi_L,Y}=-1,\qquad q_{\Psi_L,X}=\eta_\ell Q_\ell.
\]
For \(Q_{RD}\),
\[
q_{\ell_R,Y}=-1,\qquad q_{\ell_R,X}=-\eta_\ell Q_\ell,
\]
while
\[
q_{\Psi_R,Y}=-1,\qquad q_{\Psi_R,X}=+\eta_\ell Q_\ell.
\]
The difference is carried by the scalar constituent: \(H^\dagger\) for QLD and \(S_\ell\) for QRD. Thus the direct Q8 contact, the ordinary light-fermion insertion, and the scalar-source transformation cannot be assigned a common charge factor. The one-loop background Ward identity is a relation among the complete set of constituent and contact terms.

### UV full-theory one-loop vertex to be matched

For the scalar-current three-point Green function with external \(\phi^\dagger(p')\), \(\phi(p)\), and background gauge field \(A_\mu(q)\), \(q=p'-p\), the full VLL theory has two 1PI fermion-loop attachment classes at order \(g_A |y_\ell|^2\) (or \(g_A|\lambda_\ell|^2\)):

1. **Gauge insertion on the light fermion:** the light propagator is split into two propagators by the background vertex; the loop also contains the heavy \(E_\ell\) propagator.
2. **Gauge insertion on the heavy VLL:** the heavy propagator is split into two propagators by the background vertex; the loop also contains the light chiral propagator.

The corresponding EFT soft expansion must reproduce the low-momentum expansion of the sum, including the ordinary light-line insertion, the ordered Q8 one-background contact, and the scalar-source/constituent charge flow. For QLD the \(SU(2)_L\) generator acts on the \(L_\ell\) line; for QRD there is no \(SU(2)_L\) contribution. The \(B_\mu\) and \(A'_\mu\) attachments must be kept separate until their representation factors are inserted.

A routing suitable for the hard-region calculation is to take the external scalar momenta \(p,p'\), set \(q=p'-p\), and choose the loop momentum so that the light-line attachment contains denominators
\[
k^2,\quad (k+q)^2,\quad (k+p)^2+M_E^2,
\]
while the heavy-line attachment contains
\[
k^2,\quad (k+p)^2+M_E^2,\quad (k+p')^2+M_E^2.
\]
The chiral numerator and momentum shifts must be derived from the actual ordered UV vertices; these denominator lists are routing guides, not yet a claimed evaluated amplitude. Expand the complete sum by regions through the \(M_E^{-4}\) term, retaining nonexceptional Euclidean external momenta. Do not infer the heavy-line numerator by replacing a charge in the light-line result.

### Matching and acceptance rule

The comparison is
\[
\Gamma^{\mu,(1)}_{\rm UV,hard}
-\Gamma^{\mu,(1)}_{\rm EFT,soft}
=\Gamma^{\mu,(1)}_{\rm local,matched}
\]
for the same three-point Green function, flavor, gauge generator, momentum routing, and \(\overline{\rm MS}\) convention. The hard-region IR poles must cancel the soft-region UV poles only after both UV attachment classes and the full EFT contact/constituent set have been summed. A transverse pole of the isolated light-line subgraph is not sufficient evidence of this cancellation.

The next concrete calculation is therefore not another scalar tadpole: derive the two UV numerator polynomials from the chiral Feynman rules, expand each by regions, and compare their soft limits against the charge-resolved EFT set. The one-background hard matching is **not yet completed**.

## 5. Remaining matching tasks

1. Fix the exact functional-determinant routing and all external scalar momenta.
2. Apply one common IR rearrangement to line and contact graphs.
3. Show explicitly that the auxiliary-regulator dependence cancels or vanishes in the massless limit.
4. Derive the full composite-source Ward identity including scalar transformations.
5. Compute the UV-hard region with the same regulator/subtraction convention.
6. Verify soft/hard pole cancellation and then perform EOM/IBP reduction.

No complete one-loop Q8 matching coefficient is claimed at this stage.
