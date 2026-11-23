# RC-001 — Common-loop-momentum Lorentz-kernel comparison for the six \(WW\) pair classes

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVh  
**Status:** the transverse inverse-kernel part of the matter-line/three-W longitudinal sum is now checked at common loop momentum for all six pair classes. The two internal-W orientations have different line-kernel signs and different three-W group phases; with both distinctions retained, the \(D(k)-D(k+q)\) pieces cancel pairwise. In conventional Feynman gauge the nonzero \(R_{\rm FG}\) remainder remains. This is a universal Lorentz-kernel result with arbitrary endpoint currents, not yet the complete graph-specific 24-attachment amplitude or the full Slavnov–Taylor identity.

## 1. Fixed routing and orientation data

The B1 routing audit and the two raw-index bridges are used as fixed inputs; no momentum route or weak-index census is repeated here.

For the cross-vertex pairs LD-W-01/02/05/06,
\[
k_A=k,\qquad k_B=k+q,
\]
and the matter-line momenta obey
\[
r_A^Y=r_A^W-q,\qquad r_B^Y=r_B^W+q.
\]
The A- and B-side fermion/scalar WTIs therefore have opposite endpoint orientations. After grouping the internal-W endpoint terms in the common-\(k\) commutator channel, their Lorentz kernel is
\[
\boxed{\mathcal L_{A\to B}^{\mu\nu}=D^{\mu\nu}(k+q)-D^{\mu\nu}(k).}
\tag{1.1}
\]

For the same-vertex pairs LD-W-03/04,
\[
k_S=k,\qquad k_F=k+q,
\]
and both matter-line routes have
\[
r_F^Y=r_F^W+q,\qquad r_S^Y=r_S^W+q.
\]
The internal W flows \(S\to F\). Reversing the endpoint order reverses the line kernel:
\[
\boxed{\mathcal L_{S\to F}^{\mu\nu}=D^{\mu\nu}(k)-D^{\mu\nu}(k+q).}
\tag{1.2}
\]
The exact oriented fermion and scalar WTI identities are rechecked in the calculation script for every endpoint type appearing in the six pairs.

## 2. Three-W contraction and both propagator orientations

Use
\[
D^{\mu\nu}(k)=\frac{g^{\mu\nu}}{k^2},\qquad
\mathcal K_{\mu\nu}(k)=k^2g_{\mu\nu}-k_\mu k_\nu.
\]
For the all-incoming three-W vertex \((q,k,-k-q)\),
\[
q^\alpha\Gamma_{\alpha\mu\nu}
=\mathcal K_{\mu\nu}(k+q)-\mathcal K_{\mu\nu}(k).
\tag{2.1}
\]

The cross-vertex propagator chain is
\[
\mathcal C_{A\to B}^{\mu\nu}
=D^{\mu\alpha}(k+q)
[\mathcal K_{\alpha\beta}(k+q)-\mathcal K_{\alpha\beta}(k)]
D^{\beta\nu}(k).
\tag{2.2}
\]
For the reversed \(S\to F\) endpoint ordering it is
\[
\mathcal C_{S\to F}^{\mu\nu}
=D^{\mu\alpha}(k)
[\mathcal K_{\alpha\beta}(k+q)-\mathcal K_{\alpha\beta}(k)]
D^{\beta\nu}(k+q).
\tag{2.3}
\]
Because the Feynman-gauge propagator is proportional to the metric and the inverse-kernel difference is symmetric, the two chains are equal. Exact matrix multiplication gives
\[
\boxed{
\mathcal C_{A\to B}^{\mu\nu}
=\mathcal C_{S\to F}^{\mu\nu}
=D^{\mu\nu}(k)-D^{\mu\nu}(k+q)+R_{\rm FG}^{\mu\nu},
}
\tag{2.4}
\]
where
\[
\boxed{
R_{\rm FG}^{\mu\nu}
=\frac{k^\mu k^\nu-(k+q)^\mu(k+q)^\nu}
{k^2(k+q)^2}.
}
\tag{2.5}
\]
The identity is exact; no expansion in the external momentum \(q\) is used.

## 3. Group-phase-weighted cancellation

The raw-index bridges fix the phase-weighted group factors.

### 3.1 Cross-vertex \(A\to B\)

The line commutator and three-W graph both carry
\[
P_{\rm line}\mathcal G_{AB}
=P_{3W}\mathcal G_{3W}
=-ig_2\mathcal G_{AB}.
\]
Combining (1.1) and (2.4), the transverse-kernel part cancels:
\[
\begin{aligned}
\mathcal L_{A\to B}+\mathcal C_{A\to B}
&=D(k+q)-D(k)+D(k)-D(k+q)+R_{\rm FG}\\
&=R_{\rm FG}.
\end{aligned}
\]
For arbitrary endpoint currents \(J_A^\mu(k)\) and \(J_B^\nu(k+q)\),
\[
\boxed{
\mathcal M_{A\to B}^{\rm long}
=-ig_2\mathcal G_{AB}\,
J_A^\mu(k)R_{{\rm FG},\mu\nu}J_B^\nu(k+q).
}
\tag{3.1}
\]

### 3.2 Same-vertex \(S\to F\)

Here the matter-line commutator has phase-weighted group factor \(-ig_2\mathcal G_{FS}\), whereas the three-W tensor has the reversed endpoint orientation and contributes \(+ig_2\mathcal G_{FS}\). Therefore
\[
\begin{aligned}
-\mathcal L_{S\to F}+\mathcal C_{S\to F}
&\quad\text{with the corresponding group phases}\\
&\propto
-[D(k)-D(k+q)]
+[D(k)-D(k+q)+R_{\rm FG}]\\
&=R_{\rm FG}.
\end{aligned}
\]
Equivalently,
\[
\boxed{
\mathcal M_{S\to F}^{\rm long}
=+ig_2\mathcal G_{FS}\,
J_S^\mu(k)R_{{\rm FG},\mu\nu}J_F^\nu(k+q).
}
\tag{3.2}
\]
The opposite group-phase sign is essential. It is not permissible to copy the cross-vertex three-W group tensor into LD-W-03/04.

## 4. Six-pair application

The Lorentz identity is tensorial and does not depend on whether an endpoint current is a fermionic Dirac matrix or a scalar derivative current. The script inserts independent symbolic four-currents for each pair and checks the group-phase-weighted identity component by component.

| Pair | Endpoint types | Internal-W orientation | Result |
|---|---|---|---|
| LD-W-01 | F–F | \(A\to B\) | \(D\)-difference cancels |
| LD-W-02 | F–S | \(A\to B\) | \(D\)-difference cancels |
| LD-W-03 | F–S | \(S\to F\) | \(D\)-difference cancels |
| LD-W-04 | S–F | \(S\to F\) | \(D\)-difference cancels |
| LD-W-05 | S–F | \(A\to B\) | \(D\)-difference cancels |
| LD-W-06 | S–S | \(A\to B\) | \(D\)-difference cancels |

The exact audit checks:
- six pair-specific endpoint-WTI assignments: six fermion matrix identities (16 Dirac components each) and six scalar identities;
- the three-W contraction: 16/16 Lorentz components;
- both oriented W-propagator chains: 32/32 matrix components;
- arbitrary-current contraction for all six pair classes: 96/96 Lorentz components.

This establishes the common-k transverse-kernel cancellation for all six pair classes. It does not replace insertion of the explicit pair-dependent current numerators and heavy propagators into the complete loop integrand.

## 5. Scalar seagull tensors remain separate

The scalar endpoint decomposition is rechecked together with the common-kernel result. For an A-side scalar endpoint,
\[
\mathcal W_A^a=\frac12\mathcal S_A^a+\frac{i}{2}\mathcal G_{AB}^a,
\]
so the line plus seagull contribution has the form
\[
\boxed{
\mathcal C_A^\mu
=g_2\left[
\left(-\frac12(\Delta_Y-\Delta_W)V_A^\mu
+\Delta_Yq^\mu\right)\mathcal S_A^a
-\frac{i}{2}(\Delta_Y-\Delta_W)V_A^\mu\mathcal G_{AB}^a
\right].
}
\tag{5.1}
\]
For a B-side scalar endpoint,
\[
\boxed{
\mathcal C_B^\mu
=g_2\left[
\left(+\frac12(\Delta_Y-\Delta_W)V_B^\mu
+\Delta_Yq^\mu\right)\mathcal S_B^a
+\frac{i}{2}(\Delta_Y-\Delta_W)V_B^\mu\mathcal G_{AB}^a
\right].
}
\tag{5.2}
\]
For the same-vertex S endpoint, the last term uses \(\mathcal G_{FS}^a\), not \(\mathcal G_{AB}^a\).

The symmetric seagull tensor and the antisymmetric commutator tensor must remain distinct. Equations (5.1)–(5.2) are exact algebraic decompositions, not a claim that the full scalar-line/seagull contribution has canceled. The explicit scalar currents \(V^\mu\), shifted scalar denominators, and all spectator factors still have to be inserted into the complete pair integrand.

## 6. The Feynman-gauge remainder is genuinely nonzero

At the rational diagnostic point
\[
k=(3,2,0,0),\qquad q=(1,0,1,0),
\]
one has
\[
k^2=5,\qquad (k+q)^2=11,
\]
and
\[
R_{\rm FG}^{\mu\nu}
=\frac1{55}
\begin{pmatrix}
-7&-2&-4&0\\
-2&0&-2&0\\
-4&-2&-1&0\\
0&0&0&0
\end{pmatrix}.
\]
Thus \(R_{\rm FG}\) is not an algebraic zero. It is retained in (3.1) and (3.2). This calculation does not identify it with a ghost contribution or establish its cancellation by the full gauge-fixing/ghost Slavnov–Taylor sector.

## 7. Reproduction and next calculation

- Exact source: calculations/RC-001-dim6-WW-fivepoint-common-k-lorentz-kernel.py
- Captured output: validation/RC-001-dim6-WW-fivepoint-common-k-lorentz-kernel.txt
- Raw weak-index inputs: the cross-vertex and same-vertex bridge notes cited in the consolidated 24-graph ledger.

**Closed in this stage:** the common-k \(D(k)-D(k+q)\) transverse-kernel cancellation, including the orientation-dependent weak phases, for arbitrary endpoint Lorentz currents in all six pair classes.

**Still open:**
1. insert the explicit fermion/scalar current numerators and heavy propagators for each pair into one common routed loop integrand;
2. combine the symmetric scalar seagull terms with the appropriate Yukawa/external endpoint terms;
3. assemble external-leg/LSZ and the gauge-fixing/ghost Slavnov–Taylor completion of \(R_{\rm FG}\);
4. include the already-fixed EFT one-\(W\) contact and perform the common UV–EFT soft subtraction;
5. only then assess the complete longitudinal identity and any local matching coefficient.

No integrated UV five-point form factor, independent transverse form factor, or Wilson coefficient is claimed here.


## 8. 2026-11-11 scope refinement from IVn-e: momentum-dependent scalar currents

The arbitrary-current test in the source represents \(J_A\) and \(J_B\) by independent symbolic four-vectors. It therefore verifies the propagator tensor identity for fixed current values. It does not, by itself, verify that the actual scalar derivative currents in the line-insertion and three-W graphs have the same momentum arguments after the common-\(k\) shifts.

The graph-specific IVl and IVm sources use
\[
V_A^{(3W)}=2p_A-k,\qquad V_A^{(\rm line)}=2p_A-(k+q),
\]
\[
V_B^{(3W)}=-2p_B-(k+q),\qquad V_B^{(\rm line)}=-2p_B-k,
\]
\[
V_S^{(3W)}=2p_S-k,\qquad V_S^{(\rm line)}=2p_S-(k+q).
\]
Each pair differs by \(q\). The exact six-endpoint rational-point audit is recorded in
\`research/RC-001-dim6-WW-fivepoint-momentum-dependent-scalar-current-audit.md\`.

Accordingly, the statement in §§3–4 that the transverse \(D(k)-D(k+q)\) pieces cancel for all six pair classes is established at the **abstract fixed-current kernel level**. Its use as a graph-specific cancellation for LD-W-02/03/04/05/06 still requires an explicit loop-variable/routing bridge that carries the scalar currents, all light/heavy denominators, weak tensors, phases, and ordered Dirac chains together. This is not evidence of a physical failure of the Ward identity; it is an unclosed step in applying the abstract identity to the actual scalar-containing graphs.

LD-W-01, whose two endpoint currents are fermionic and momentum independent, is not affected by this particular scalar-current shift issue. \(R_{\rm FG}\) remains explicit throughout. No graph is removed and no ghost/ST cancellation is inferred.
