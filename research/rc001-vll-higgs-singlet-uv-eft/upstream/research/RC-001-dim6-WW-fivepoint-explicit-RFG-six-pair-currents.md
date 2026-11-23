# RC-001 — Explicit six-pair Feynman-gauge remainder with graph-specific currents

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVl  
**Status:** the generic \(R_{\rm FG}\) current projection has now been populated with the oriented endpoint numerators for LD-W-01…06. The four cross-vertex chains retain the \(X_A\slashed h X_B^Y\) order; the two same-vertex chains retain the distinct Dirac-Hermitian orientations \(\gamma\slashed r_F V_S\) and \(V_S\slashed r_F\gamma\). Direct tensor contractions and their factorized forms agree exactly at two nonsingular rational momentum points for all six pairs. The same-vertex heavy channel is displayed explicitly as a spectator factor. This is not the complete gauge-fixed five-point amplitude.

## 1. Conventions and the matrix-valued projection

Set
\[
\kappa=k+q,\qquad
R_{\rm FG}^{\mu\nu}(k,q)
=\frac{k^\mu k^\nu-\kappa^\mu\kappa^\nu}{k^2\kappa^2}.
\]
For endpoint currents \(J_A^\mu,J_B^\nu\) and an ordered open Dirac chain \(\mathcal X\), the contraction is
\[
\mathcal R[J_A,\mathcal X,J_B]
=J_{A\mu}\,\mathcal X\,J_{B\nu}R_{\rm FG}^{\mu\nu}
=\frac{(J_A\!\cdot k)\mathcal X(J_B\!\cdot k)
-(J_A\!\cdot\kappa)\mathcal X(J_B\!\cdot\kappa)}
{k^2\kappa^2}.
\tag{1.1}
\]
For fermion endpoints, \(J_F^\mu=\gamma^\mu\), so \(J_F\cdot k=\slashed k\). For scalar endpoints the contraction is the ordinary scalar product with the scalar-current vector. Equation (1.1) is used without commuting any Dirac factors through \(\mathcal X\).

The numerator-only object below is denoted \(\mathcal N_{\rm FG}\); the factor \(1/(k^2\kappa^2)\) is supplied by \(R_{\rm FG}\). This convention prevents double-counting the two internal-W propagators.

## 2. Cross-vertex pairs LD-W-01/02/05/06

Use the all-incoming momenta
\[
p_4=-p_1-p_2-p_3-q,\qquad h=k-p_1-p_2,
\]
\[
r_A=k-p_A,\qquad r_B^Y=k+p_B+q.
\]
The endpoint data inherited from the oriented numerator ledger are
\[
X_A=\begin{cases}-\slashed r_A&A=\bar L,\\1&A=H,\end{cases}
\qquad
X_B^Y=\begin{cases}\slashed r_B^Y&B=L,\\1&B=H^\dagger,\end{cases}
\]
\[
J_A^\mu=\begin{cases}\gamma^\mu&A=\bar L,\\
V_A^\mu=2p_A^\mu-k^\mu&A=H,\end{cases}
\]
\[
J_B^\nu=\begin{cases}\gamma^\nu&B=L,\\
V_B^\nu=-2p_B^\nu-\kappa^\nu&B=H^\dagger.\end{cases}
\]
The common ordered chain is \(X_A\slashed h X_B^Y\). Thus
\[
\boxed{
\mathcal N_{\rm FG}^{AB}
=(J_A\!\cdot k)X_A\slashed h X_B^Y(J_B\!\cdot k)
-(J_A\!\cdot\kappa)X_A\slashed h X_B^Y(J_B\!\cdot\kappa).
}
\tag{2.1}
\]

The four explicit cases are:

### LD-W-01: F–F

\[
p_A=p_1,\quad p_B=p_4,\quad
X_A=-\slashed r_A,\quad X_B^Y=\slashed r_B^Y.
\]
\[
\boxed{
\mathcal N_{01}
=\slashed k(-\slashed r_A)\slashed h\slashed r_B^Y\slashed k
-\slashed\kappa(-\slashed r_A)\slashed h\slashed r_B^Y\slashed\kappa.
}
\]

### LD-W-02: F–S

\[
p_A=p_1,\quad p_B=p_3,\quad
X_A=-\slashed r_A,\quad V_B=-2p_3-\kappa.
\]
\[
\boxed{
\mathcal N_{02}
=\slashed k(-\slashed r_A)\slashed h(V_B\!\cdot k)
-\slashed\kappa(-\slashed r_A)\slashed h(V_B\!\cdot\kappa).
}
\]

### LD-W-05: S–F

\[
p_A=p_2,\quad p_B=p_4,\quad
V_A=2p_2-k,\quad X_B^Y=\slashed r_B^Y.
\]
\[
\boxed{
\mathcal N_{05}
=(V_A\!\cdot k)\slashed h\slashed r_B^Y\slashed k
-(V_A\!\cdot\kappa)\slashed h\slashed r_B^Y\slashed\kappa.
}
\]

### LD-W-06: S–S

\[
p_A=p_2,\quad p_B=p_3,\quad
V_A=2p_2-k,\quad V_B=-2p_3-\kappa.
\]
\[
\boxed{
\mathcal N_{06}
=(V_A\!\cdot k)\slashed h(V_B\!\cdot k)
-(V_A\!\cdot\kappa)\slashed h(V_B\!\cdot\kappa).
}
\]

For each cross pair, the full denominator accompanying \(\mathcal N_{\rm FG}/(k^2\kappa^2)\) is
\[
\mathcal D_{AB}
=(r_A^2)(r_B^{Y\,2})(h^2-M_E^2).
\tag{2.2}
\]
The two W propagators are already displayed in \(R_{\rm FG}\). The cross-pair heavy numerator \(\slashed h\) is retained inside (2.1), not absorbed into a scalar prefactor.

## 3. Same-vertex pairs LD-W-03/04

For the same-vertex triangles the internal W flows \(S\to F\). Define
\[
r_F^Y=k+p_F+q,\qquad r_S=p_S-k,\qquad
V_S=2p_S-k,\qquad h_E=p_F+p_S+q.
\]
The heavy line is an external-channel spectator to the loop-side RFG contraction. Its propagator is
\[
S_E(h_E)=\frac{i\,\slashed h_E P_L}{h_E^2-M_E^2}
\]
in the left-vertex orientation, with the Dirac-Hermitian-conjugate ordering for the right-vertex orientation. It is not commuted through the loop numerator.

### LD-W-03: \(\gamma\slashed r_F V_S\)

The seed numerator is \(N_{03}=\gamma_\mu\slashed r_F V_S^\mu\). The shifted fermion momentum in the three-W attachment is \(r_F^Y\). Therefore
\[
\boxed{
\mathcal N_{03}
=(V_S\!\cdot k)\slashed k\slashed r_F^Y
-(V_S\!\cdot\kappa)\slashed\kappa\slashed r_F^Y.
}
\tag{3.1}
\]
The loop-side RFG factor is \(\mathcal N_{03}/(k^2\kappa^2)\), followed by the heavy spectator in the original seed orientation.

### LD-W-04: \(V_S\slashed r_F\gamma\)

The conjugate seed numerator is \(N_{04}=V_S^\mu\slashed r_F\gamma_\mu\). Its ordering must not be replaced by the LD-W-03 ordering:
\[
\boxed{
\mathcal N_{04}
=(V_S\!\cdot k)\slashed r_F^Y\slashed k
-(V_S\!\cdot\kappa)\slashed r_F^Y\slashed\kappa.
}
\tag{3.2}
\]
The heavy spectator is placed with the conjugate seed orientation. In both cases the remaining denominator is
\[
\mathcal D_{FS}
=(r_F^{Y\,2})(r_S^2)(h_E^2-M_E^2).
\tag{3.3}
\]
Equations (3.1) and (3.2) differ by the order of the two slash factors. They are not interchangeable before the chiral projectors and the heavy spectator are restored.

## 4. Scalar seagulls: explicit longitudinal contact factors, kept separate

The six scalar seagulls are not part of \(R_{\rm FG}\). Their external-W contraction is \(q_\alpha g^{\alpha\mu}=q^\mu\), followed by the single internal-W propagator and the opposite endpoint current. The common-\(k\) shifts fixed in IVj give the following factors:

| Pair | Seagull endpoint | Internal-W momentum | Opposite-current factor after \(q_\alpha\) contraction |
|---|---|---|---|
| LD-W-02 | B scalar | \(k\) | \((J_A\cdot q)X_A\slashed h/k^2\), with \(J_A\cdot q=\slashed q\) |
| LD-W-03 | S scalar | \(\kappa\) | \(\slashed q\slashed r_F^Y/\kappa^2\) |
| LD-W-04 | S scalar | \(\kappa\) | \(\slashed r_F^Y\slashed q/\kappa^2\) |
| LD-W-05 | A scalar | \(\kappa\) | \(\slashed h\slashed r_B^Y\slashed q/\kappa^2\) |
| LD-W-06 | A scalar | \(\kappa\) | \(\slashed h(V_B\cdot q)/\kappa^2\) |
| LD-W-06 | B scalar | \(k\) | \((V_A\cdot q)\slashed h/k^2\) |

Each row multiplies its own scalar propagator, opposite-endpoint propagator, heavy factor, phase, and anticommutator weak tensor \(\mathcal S_X^a\). The two LD-W-06 seagulls are distinct graphs and carry \(\mathcal S_A^a\) and \(\mathcal S_B^a\), respectively. The anticommutator tensor must not be replaced by the ordered scalar-line tensor.

For use in the scalar-line-plus-seagull decomposition, the explicit scalar-current and propagator assignments are:
- cross A scalar (LD-W-05/06), after \(k_{\rm old}=k+q\):
  \[
  V_A=2p_A-\kappa,\quad
  r_A^Y=k-p_A,\quad r_A^W=\kappa-p_A;
  \]
- cross B scalar (LD-W-02/06), without a shift:
  \[
  V_B=-2p_B-k,\quad
  r_B^Y=k+p_B+q,\quad r_B^W=k+p_B;
  \]
- same-vertex S scalar (LD-W-03/04), after \(k_{\rm old}=k+q\):
  \[
  V_S=2p_S-\kappa,\quad
  r_S^Y=p_S-k,\quad r_S^W=p_S-k-q.
  \]
These are the inputs to the already-derived A-side and B/S-side weak-tensor decompositions in B2c-IVg. They do not yet constitute their full common-\(k\) integral sum.

## 5. Exact rational-point audit

The source
\[
\texttt{calculations/RC-001-dim6-WW-fivepoint-explicit-RFG-six-pair-currents.py}
\]
constructs the four-dimensional Dirac matrices and compares:
1. the direct component sum \(J_{A\mu}\mathcal XJ_{B\nu}(k^\mu k^\nu-\kappa^\mu\kappa^\nu)\);
2. the factorized current expression (1.1), with the open-chain matrix order unchanged.

It does this for all six pair classes at two independent nonsingular rational momentum points. At each point, every W, light-matter, and heavy-channel denominator is checked to be nonzero, and every pair's RFG numerator is checked to be nonzero.

The test points use \(M_E^2=400\) only as a nonsingular diagnostic value; this is not a physical benchmark or a mass scan. The exact checks establish algebraic agreement at those points, not an integrated or on-shell observable.

Reproduction:
- source: \`calculations/RC-001-dim6-WW-fivepoint-explicit-RFG-six-pair-currents.py\`
- tests: \`calculations/test_RC001_dim6_WW_fivepoint_explicit_RFG_six_pair_currents.py\`
- output: \`validation/RC-001-dim6-WW-fivepoint-explicit-RFG-six-pair-currents.txt\`

## 6. What this establishes—and what it does not

**Established in this stage**
- the actual F/S endpoint currents have been inserted into \(R_{\rm FG}\) for all six pair classes;
- the A-side minus sign \(X_A=-\slashed r_A\), B-side \(+\slashed r_B^Y\), and the scalar derivative-current signs are retained;
- LD-W-03 and LD-W-04 keep their distinct Dirac-Hermitian numerator order;
- the cross-pair heavy numerator \(\slashed h\) is inside the chain, while the same-vertex heavy channel is retained as a spectator with momentum \(h_E\);
- all six direct tensor contractions agree with their factorized forms at two exact rational points.

**Not established**
- cancellation of the six pairwise RFG terms after weak-index, phase, external-field, and counterterm sums;
- cancellation by ghost/gauge-fixing Slavnov–Taylor terms;
- a full scalar-line plus seagull common-\(k\) identity;
- a nonexceptional loop integration, UV–EFT soft subtraction, or transverse form factor;
- any Wilson coefficient.

The next calculation is to assemble the scalar-line/seagull terms in the same common-\(k\) convention, with the weak tensors \(\mathcal S_A,\mathcal S_B,\mathcal S_S\) and \(\mathcal G_{AB},\mathcal G_{FS}\) kept distinct. Only after this ordinary-matter sector is explicit should the BRST/ghost STI completion be added. Do not set \(R_{\rm FG}\) to zero and do not identify it with a ghost graph by itself.
