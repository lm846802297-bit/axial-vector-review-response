# RC-001 — Momentum-dependent scalar-current routing audit between IVl and IVm

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-e  
**Status:** an exact comparison of the actual scalar derivative currents in the IVl three-W \(R_{\rm FG}\) projection and the IVm scalar-line/seagull routes finds a nontrivial momentum-routing difference at every scalar endpoint. The difference is exactly \(q^\mu\), and substituting one current for the other changes the corresponding \(R_{\rm FG}\) numerator at a nonsingular rational diagnostic point. This does **not** prove that the physical diagrams fail to cancel: an explicit change-of-variable identity or an endpoint-adapted three-W routing may reconcile the terms. It does show that the IVh arbitrary-current tensor identity is not, by itself, a graph-specific cancellation proof for momentum-dependent scalar currents.

## 1. Why this audit is necessary

The IVh calculation proves a valid tensor identity for arbitrary symbolic endpoint currents \(J_A,J_B\):
\[
D(\kappa)[K(\kappa)-K(k)]D(k)
=D(k)-D(\kappa)+R_{\rm FG}.
\]
Its test represents \(J_A,J_B\) by independent four-component symbols. Such a test does not test how a scalar derivative current changes when the loop momentum is shifted.

The graph-specific IVl projection uses the following currents:
\[
V_A^{(3W)}=2p_A-k,\qquad
V_B^{(3W)}=-2p_B-\kappa,\qquad
V_S^{(3W)}=2p_S-k.
\]
The common-\(k\) IVm scalar-line/seagull kernels instead use
\[
V_A^{(\rm line)}=2p_A-\kappa,\qquad
V_B^{(\rm line)}=-2p_B-k,\qquad
V_S^{(\rm line)}=2p_S-\kappa.
\]
These are the actual expressions in the two source files, not a new choice of convention.

## 2. Exact current shifts

With \(\kappa=k+q\),
\[
\boxed{
V_A^{(3W)}-V_A^{(\rm line)}=q,
\qquad
V_B^{(\rm line)}-V_B^{(3W)}=q,
\qquad
V_S^{(3W)}-V_S^{(\rm line)}=q.
}
\tag{2.1}
\]
All 12 vector components are checked exactly for independent symbolic \(p_A,p_B,p_S,k,q\).

The six affected scalar endpoints are:

| Pair | IVm scalar endpoint current | IVl three-W current | Exact difference |
|---|---|---|---|
| LD-W-02(B) | \(V_B(k)\) | \(V_B(\kappa)\) | \(+q\) |
| LD-W-03(S) | \(V_S(\kappa)\) | \(V_S(k)\) | \(+q\) |
| LD-W-04(S) | \(V_S(\kappa)\) | \(V_S(k)\) | \(+q\) |
| LD-W-05(A) | \(V_A(\kappa)\) | \(V_A(k)\) | \(+q\) |
| LD-W-06(A) | \(V_A(\kappa)\) | \(V_A(k)\) | \(+q\) |
| LD-W-06(B) | \(V_B(k)\) | \(V_B(\kappa)\) | \(+q\) |

For LD-W-06 the opposite scalar current also matters:
- the A-line/seagull route uses \((V_A(\kappa),V_B(\kappa))\);
- the B-line/seagull route uses \((V_A(k),V_B(k))\);
- the IVl three-W projection uses the mixed pair \((V_A(k),V_B(\kappa))\).

Thus the two scalar endpoints cannot be collapsed into one common scalar-current factor.

## 3. Exact denominator-route factors

The current shifts occur together with nontrivial changes in the propagator products. This is why a current-only substitution is not the full graph comparison.

For a cross-vertex pair define
\[
r_A=k-p_A,\quad r_B=k+p_B,\quad h=k-P,\quad \kappa=k+q.
\]
The three-W denominator is
\[
\mathscr D_{3W}^{AB}
=k^2\kappa^2\,r_A^2(r_B+q)^2(h^2-M_E^2).
\]
After the common shift of the A-line graph, its denominator and the A seagull denominator are
\[
\mathscr D_{A\text{-line}}
=\kappa^2r_A^2(r_A+q)^2(r_B+q)^2(h^2-M_E^2),
\]
\[
\mathscr D_{A\text{-sg}}
=\kappa^2r_A^2(r_B+q)^2(h^2-M_E^2).
\]
Thus
\[
\boxed{
\mathscr D_{A\text{-line}}\;k^2
=\mathscr D_{3W}^{AB}(r_A+q)^2,\qquad
\mathscr D_{A\text{-sg}}\;k^2=\mathscr D_{3W}^{AB}.
}
\tag{3.1}
\]
For the B-line and B-seagull routes,
\[
\mathscr D_{B\text{-line}}
=k^2r_A^2r_B^2(r_B+q)^2(h^2-M_E^2),
\]
\[
\mathscr D_{B\text{-sg}}
=k^2r_A^2(r_B+q)^2(h^2-M_E^2),
\]
so
\[
\boxed{
\mathscr D_{B\text{-line}}\;\kappa^2
=\mathscr D_{3W}^{AB}r_B^2,\qquad
\mathscr D_{B\text{-sg}}\;\kappa^2=\mathscr D_{3W}^{AB}.
}
\tag{3.2}
\]

For the same-vertex \(S\to F\) pairs, define
\[
r_F=k+p_F,\quad r_F^Y=\kappa+p_F,\quad
r_S=p_S-k,\quad r_S^W=p_S-\kappa,\quad
h_E=p_F+p_S+q.
\]
The three-W denominator is
\[
\mathscr D_{3W}^{FS}
=k^2\kappa^2(r_F^Y)^2r_S^2(h_E^2-M_E^2).
\]
The fermion-line, scalar-line and scalar-seagull denominators obey
\[
\boxed{
\mathscr D_{F\text{-line}}\;\kappa^2
=\mathscr D_{3W}^{FS}r_F^2,
\qquad
\mathscr D_{S\text{-line}}\;k^2
=\mathscr D_{3W}^{FS}(r_S^W)^2,
\qquad
\mathscr D_{S\text{-sg}}\;k^2
=\mathscr D_{3W}^{FS}.
}
\tag{3.3}
\]
All seven cross/same-vertex factor identities are checked exactly with independent symbolic momenta and \(M_E^2\).

These relations show that the matter-line graphs do not differ from the three-W graph only by replacing a scalar current: an adjacent scalar or fermion propagator takes the place of the missing second W propagator. The WTI numerator, seagull contact, shifted scalar current, and full propagator product must therefore be combined before comparing with the \(R_{\rm FG}\) projection. This is the precise reason the IVh fixed-current identity cannot be promoted directly to a graph-specific cancellation.

## 4. Direct \(R_{\rm FG}\)-numerator substitution test

For a fixed ordered Dirac chain \(\mathcal X\), define the IVl numerator projection
\[
\mathcal N_{\rm FG}[J_A,\mathcal X,J_B]
=(J_A\cdot k)\mathcal X(J_B\cdot k)
-(J_A\cdot\kappa)\mathcal X(J_B\cdot\kappa).
\]
The audit replaces only the scalar current, leaving the other endpoint current and the ordered Dirac chain fixed. This isolates the effect of the \(k\leftrightarrow\kappa\) scalar-current difference; it does not assume a physical cancellation or alter a graph's Feynman-rule phase.

The nonsingular rational diagnostic is
\[
\begin{aligned}
k&=(4,1,2,1),&q&=(1,2,0,1),\\
p_1&=(1,0,1,0),&p_2&=(0,1,0,2),\\
p_3&=(2,0,1,1),&
p_4&=(-4,-3,-2,-4),
\end{aligned}
\]
with metric \(\operatorname{diag}(1,-1,-1,-1)\) and diagnostic \(M_E^2=400\). It gives \(k^2=10\), \(\kappa^2=8\). All scalar, light-fermion, heavy-channel and W denominators listed in the source are nonzero.

The exact 4-by-4 Dirac-matrix differences are:

| Scalar endpoint substitution | Nonzero matrix entries | Trace |
|---|---:|---:|
| LD-W-02(B) | 16/16 | 0 |
| LD-W-03(S) | 16/16 | \(-184\) |
| LD-W-04(S) | 16/16 | \(-132\) |
| LD-W-05(A) | 16/16 | 0 |
| LD-W-06(A current) | 12/16 | 0 |
| LD-W-06(B current) | 12/16 | 0 |

The nonzero entries show that replacing the IVm current by the IVl current changes the explicit \(R_{\rm FG}\) numerator. The zero traces for several rows do not mean the matrices vanish; their individual entries are nonzero.

## 5. Interpretation: what is and is not established

**Established**
1. The IVh arbitrary-current propagator identity is exact.
2. The actual scalar currents in IVl and IVm differ by the exact external momentum \(q\).
3. At a nonsingular rational point, the corresponding \(R_{\rm FG}\) current projections change under that substitution for all six scalar endpoints.
4. LD-W-06 requires two separate endpoint routings.

**Not established**
1. A physical failure of the Slavnov–Taylor identity.
2. A nonzero uncanceled contribution to the integrated five-point amplitude.
3. That the IVl or IVm current convention is individually wrong.
4. That \(R_{\rm FG}\) survives the complete BRST/ghost and external-field sum.

The two current sets may be related by a loop-momentum change of variables, by exchanging the two internal-W legs of the three-W graph with the associated Lorentz/group orientation change, or by combining the scalar seagull \(q^\mu\) contact with the endpoint terms. Each option must be derived explicitly with the heavy and light propagator denominators retained. One cannot replace \(V_A(\kappa)\) by \(V_A(k)\), or \(V_B(k)\) by \(V_B(\kappa)\), by inspection.

## 6. Exact three-W internal-leg exchange identity

The three-W graph admits an exact internal-leg exchange at the vertex level. For \(\kappa=k+q\),
\[
\boxed{
\Gamma_{\alpha\nu\mu}(q,-\kappa,k)
=-\Gamma_{\alpha\mu\nu}(q,k,-\kappa).
}
\tag{5.1}
\]
At the same time,
\[
\epsilon^{acb}=-\epsilon^{abc}.
\]
The Lorentz vertex and the antisymmetric weak tensor each change sign, so their product is invariant:
\[
\boxed{
\epsilon^{acb}\Gamma_{\alpha\nu\mu}(q,-\kappa,k)
=\epsilon^{abc}\Gamma_{\alpha\mu\nu}(q,k,-\kappa).
}
\tag{5.2}
\]
The updated exact source checks 64/64 Lorentz components, 27/27 weak-index permutations, and 1728/1728 combined Lorentz/group components.

This establishes the antisymmetry/relabeling identity of the three-W vertex and its weak tensor. It is **not** a physical exchange of the A/B matter endpoints: once the two W legs are attached to distinct matter subgraphs, each endpoint current remains tied to its own momentum-conservation equation. In particular, (5.2) does not by itself turn (V_A(k)) into (V_A(\kappa)), or (V_B(\kappa)) into (V_B(k)). The scalar endpoint momenta, scalar propagators, heavy-channel momentum, Dirac ordering, and physical W-flow signs must all be transformed together before claiming a common routing. Equation (5.2) is only the vertex-level starting identity, not the completed common-routing bridge.

## 7. Correct next calculation

The next task is a **graph-specific common-routing bridge**, not another arbitrary-current tensor proof:

1. For each scalar-containing pair, write the complete q-contracted scalar-line plus seagull term with its actual shifted scalar propagators, internal-W propagator, opposite-endpoint current, weak tensor and heavy numerator.
2. Write the same pair's three-W graph in both allowed internal-leg routings, including the exchange of Lorentz indices, momenta, group tensor and Feynman-rule phase.
3. Derive the loop-variable transformation between the two routings at the level of the full denominator and ordered Dirac numerator, not just the W propagator.
4. For LD-W-06, keep the A and B scalar-line terms separate until the common representation of the single three-W graph is established.
5. Only then combine the scalar commutator pieces with the three-W term and the symmetric seagull pieces with the Yukawa-endpoint WTI terms.
6. Revisit the fermion-only LD-W-01 separately as a control case; its endpoint currents are momentum independent, so it is not affected by this particular scalar-current issue.

The ordinary-matter longitudinal integrand is not yet assembled. Keep \(R_{\rm FG}\) explicit. Do not infer a ghost cancellation from the inverse-kernel algebra identity, and do not begin UV–EFT integration or Wilson-coefficient extraction until this graph-specific routing bridge closes.

## 8. Reproduction

- Source: \`calculations/RC-001-dim6-WW-fivepoint-momentum-dependent-scalar-current-audit.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_momentum_dependent_scalar_current_audit.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-momentum-dependent-scalar-current-audit.txt\`

The checks are exact local SymPy symbolic/rational calculations. They are not a GitHub Actions run, a loop integration, or a physical benchmark scan.
