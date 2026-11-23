# RC-001 — UV external-W five-point routing and longitudinal numerator audit

**Workstream:** RC-001-WW-UV-FF-02, Stages B1–B2 (routing and line-level contraction)  
**Status:** the six four-point seed routings and 24 direct external-W attachments have been assigned exact all-incoming momentum routes. The massless fermion, scalar, scalar-seagull, and three-W longitudinal building blocks have been checked algebraically. No five-point loop integral or complete Slavnov–Taylor sum is claimed.

## 1. Conventions and scope

Use the all-incoming five-point Green function
\[
\bar L_i(p_1),\quad H_j(p_2),\quad H_k^\dagger(p_3),\quad
L_l(p_4),\quad W_\alpha^a(q),
\qquad p_1+p_2+p_3+p_4+q=0.
\]
The internal exchanged W momentum is denoted by \(k\), and is never identified with the external momentum \(q\). Define
\[
P=p_1+p_2,\qquad h=k-P
\]
for the cross-vertex seed routing. The heavy \(E\) is an \(SU(2)_L\) singlet, so there is no \(WEE\) attachment.

The calculation is in the unbroken, massless \(SU(2)_L\) theory. The light \(L\) and \(H\) propagators are massless; the heavy propagator has mass \(M_E\). There is no broken-phase \(W\)-Goldstone mixing in this sub-block. If the calculation is moved to the broken phase, the fermion mass terms in the chiral Ward identity and the corresponding Goldstone vertices must be restored together.

The six seed classes are the already-established LD-W-01…06. Their four-point hard/soft integrals are not recomputed here. The present task is to route the additional external W and contract its momentum before any new integration.

## 2. Cross-vertex seed routing

For LD-W-01/02/05/06, orient the internal W from endpoint \(A\) (on the left Yukawa vertex) to endpoint \(B\) (on the right Yukawa vertex). The line assignment is:

| Pair | \(A\) at left vertex | \(B\) at right vertex | \(A'\) spectator at left vertex | \(B'\) spectator at right vertex |
|---|---|---|---|---|
| LD-W-01 | \(\bar L(p_1)\), fermion | \(L(p_4)\), fermion | \(H(p_2)\) | \(H^\dagger(p_3)\) |
| LD-W-02 | \(\bar L(p_1)\), fermion | \(H^\dagger(p_3)\), scalar | \(H(p_2)\) | \(L(p_4)\) |
| LD-W-05 | \(H(p_2)\), scalar | \(L(p_4)\), fermion | \(\bar L(p_1)\) | \(H^\dagger(p_3)\) |
| LD-W-06 | \(H(p_2)\), scalar | \(H^\dagger(p_3)\), scalar | \(\bar L(p_1)\) | \(L(p_4)\) |

The four-point seed momenta are
\[
r_A=k-p_A,\qquad r_B=k+p_B,\qquad h=k-p_1-p_2.
\]
At \(q=0\), the four vertex equations are
\[
p_A+r_A-k=0,\qquad p_B+k-r_B=0,
\]
\[
p_{A'}+h-r_A=0,\qquad p_{B'}+r_B-h=0.
\]
These reproduce the already-recorded generalized shifts:
\[
\begin{array}{c|cc}
\text{pair}&r_A&r_B\\ \hline
01&k-p_1&k+p_4\\
02&k-p_1&k+p_3\\
05&k-p_2&k+p_4\\
06&k-p_2&k+p_3
\end{array}
\]
and reduce to the exceptional \(p_1=p_3=0,\ p_2=P,\ p_4=-P\) routing in the existing cross-box note.

### 2.1 External W on the A matter propagator

The external W is inserted between the left Yukawa vertex and the internal-W endpoint:
\[
r_A^{Y}=k-p_A-q,\qquad r_A^{W}=k-p_A,
\]
\[
h_A=k-p_1-p_2-q,\qquad r_B=k+p_B.
\]
The external-W vertex equation is \(r_A^Y+q-r_A^W=0\). The shifted heavy momentum \(h_A\) is the same when reconstructed from either Yukawa endpoint using five-point momentum conservation.

### 2.2 External W on the B matter propagator

The insertion is between the internal-W endpoint and the right Yukawa vertex:
\[
r_B^{W}=k+p_B,\qquad r_B^{Y}=k+p_B+q,
\]
\[
h_B=k-p_1-p_2,\qquad r_A=k-p_A.
\]
The external-W vertex equation is \(r_B^W+q-r_B^Y=0\).

### 2.3 External W on the internal W propagator

The internal W is split into two propagators:
\[
k_A=k,\qquad k_B=k+q,
\]
with
\[
r_A=k-p_A,\qquad r_B=k+p_B+q,\qquad h=k-p_1-p_2.
\]
The three-W vertex obeys \(q+k_A-k_B=0\). The heavy momentum is unchanged in this routing.

### 2.4 Scalar seagulls

If endpoint \(A\) is a scalar, the two-gauge seagull replaces the ordinary scalar-W endpoint:
\[
r_A^{\rm sg}=k-p_A-q,\qquad h_A=k-p_1-p_2-q.
\]
If endpoint \(B\) is a scalar:
\[
r_B^{\rm sg}=k+p_B+q,\qquad h_B=k-p_1-p_2.
\]
These are separate five-point graphs. They are not optional additions to the scalar-line insertion: the scalar kinetic term contains both the three-point scalar-W vertex and the two-W seagull.

## 3. Same-vertex seed routing

LD-W-03 and LD-W-04 are Yukawa-vertex triangles. The heavy propagator is outside the W-loop integration. Let \(F\) denote the fermion endpoint and \(S\) the scalar endpoint; orient the internal W from \(S\) to \(F\).

| Pair | Fermion endpoint \(F\) | Scalar endpoint \(S\) | Heavy channel |
|---|---|---|---|
| LD-W-03 | \(\bar L(p_1)\) | \(H(p_2)\) | \(P_{FS}=p_1+p_2\) |
| LD-W-04 | \(L(p_4)\) | \(H^\dagger(p_3)\) | \(P_{FS}=p_3+p_4\) |

The seed momenta are
\[
r_F=k+p_F,\qquad r_S=p_S-k,\qquad
P_{FS}=r_F+r_S=p_F+p_S.
\]

For an external W on the fermion line:
\[
r_F^{F}=k+p_F,\qquad r_F^{Y}=k+p_F+q,\qquad
r_S=p_S-k,\qquad P_E=P_{FS}+q.
\]
For an external W on the scalar line:
\[
r_S^{S}=p_S-k,\qquad r_S^{Y}=p_S-k+q,\qquad
r_F=k+p_F,\qquad P_E=P_{FS}+q.
\]
For an external W on the internal W line:
\[
k_S=k,\qquad k_F=k+q,\qquad
r_F=k+p_F+q,\qquad r_S=p_S-k,\qquad P_E=P_{FS}+q.
\]
The scalar seagull at endpoint \(S\) has
\[
r_S^{\rm sg}=p_S-k+q,\qquad r_F=k+p_F,\qquad P_E=P_{FS}+q.
\]

The \(P_E\) shift is essential: the external W insertion transfers \(q\) into the heavy channel at the same Yukawa vertex. It must not be set back to \(P_{FS}\) before the propagator expansion. The existing pure-soft statement for LD-W-03/04 remains a hard-minus-EFT statement at \(O(M_E^{-2})\); it does not remove these graphs from the five-point Ward sum.

## 4. Complete direct-attachment census

The direct external-W attachments to the six one-loop subgraphs are:

| Pair | Matter-line insertions | Scalar seagulls | Three-W insertions | Total |
|---|---:|---:|---:|---:|
| LD-W-01 | 2 fermion | 0 | 1 | 3 |
| LD-W-02 | 1 fermion + 1 scalar | 1 | 1 | 4 |
| LD-W-03 | 1 fermion + 1 scalar | 1 | 1 | 4 |
| LD-W-04 | 1 fermion + 1 scalar | 1 | 1 | 4 |
| LD-W-05 | 1 scalar + 1 fermion | 1 | 1 | 4 |
| LD-W-06 | 2 scalar | 2 | 1 | 5 |
| **Total** | **12** | **6** | **6** | **24** |

Thus the 24 direct attachments consist of 12 ordinary matter-line insertions, six scalar seagulls, and six insertions on the internal W through the three-W vertex. There is no W attachment to the heavy \(E\) line.

This is a topology census for the fixed six-pair skeleton. It is not an independent FeynArts/QGRAF graph-generation or sign/multiplicity validation. Four external-leg emissions belong to the reducible/LSZ completion of the summed four-point Green function and are kept in a separate ledger; they are not counted among the 24 internal attachments. Parameter, field, and operator counterterms are also separate.

## 5. Denominator templates for the new five-point graphs

For cross-vertex classes, write \(r_A=k-p_A\), \(r_B=k+p_B\), and \(h=k-P\). The denominator families are:

- A-line insertion:
  \[
  k^2(r_A-q)^2r_A^2r_B^2[(h-q)^2-M_E^2].
  \]
- B-line insertion:
  \[
  k^2r_A^2r_B^2(r_B+q)^2(h^2-M_E^2).
  \]
- Internal-W insertion:
  \[
  k^2(k+q)^2r_A^2(r_B+q)^2(h^2-M_E^2).
  \]
- A scalar seagull:
  \[
  k^2(r_A-q)^2r_B^2[(h-q)^2-M_E^2].
  \]
- B scalar seagull:
  \[
  k^2r_A^2(r_B+q)^2(h^2-M_E^2).
  \]

For LD-W-03/04, \(P_E=P_{FS}+q\) is external to the W loop. The corresponding denominator templates are:

- Fermion-line insertion:
  \[
  k^2r_F^2(r_F+q)^2r_S^2[P_E^2-M_E^2].
  \]
- Scalar-line insertion:
  \[
  k^2r_F^2r_S^2(r_S+q)^2[P_E^2-M_E^2].
  \]
- Internal-W insertion:
  \[
  k^2(k+q)^2r_F^2r_S^2[P_E^2-M_E^2].
  \]
- Scalar seagull:
  \[
  k^2r_F^2(r_S+q)^2[P_E^2-M_E^2].
  \]

The denominators follow from the vertex momentum equations above. The numerator for each graph is obtained by inserting the corresponding vertex between the displayed adjacent propagators; the spectator factors are the remaining fermion/heavy/scalar factors of that seed topology.

## 6. B2: exact longitudinal numerator contractions

### 6.1 Massless chiral fermion line

For \(S_F(r)=\slashed r/r^2\), the line insertion numerator is
\[
N_F^\mu(r,q)=S_F(r+q)\gamma^\mu P_LS_F(r).
\]
The exact contraction is
\[
\boxed{
q_\mu N_F^\mu(r,q)
=P_LS_F(r)-S_F(r+q)P_R
=P_L\big[S_F(r)-S_F(r+q)\big].
}
\]
The chiral projectors are kept in their correct order. This is the propagator-difference identity used by the line telescope; it is not an on-shell external-fermion equation.

For a massive broken-phase fermion, the additional mass terms must be combined with the Goldstone vertex using the broken-theory Slavnov–Taylor identity. They are absent only because this sub-block is evaluated in the unbroken massless theory.

### 6.2 Complex scalar line

With \(\Delta(r)=1/r^2\),
\[
N_S^\mu(r,q)=\Delta(r+q)(2r+q)^\mu\Delta(r),
\]
and
\[
\boxed{
q_\mu N_S^\mu(r,q)=\Delta(r)-\Delta(r+q).
}
\]
The scalar insertion therefore has the same endpoint-difference structure as the fermion insertion.

### 6.3 Scalar two-gauge seagull

From \((D_\mu H)^\dagger D^\mu H\), the stripped seagull vertex with external gauge index \(a\) and internal gauge index \(b\) is
\[
V_{\rm sg}^{\mu\nu}=g_2^2\{t^a,t^b\}g^{\mu\nu}.
\]
For \(t^a=\sigma^a/2\),
\[
\{t^a,t^b\}=\frac12\delta^{ab}\mathbf1,
\qquad
q_\mu V_{\rm sg}^{\mu\nu}
=g_2^2\{t^a,t^b\}q^\nu.
\]
The seagull contraction is nonzero by itself. It must be combined with the scalar-line insertion and the gauge-endpoint terms; it is not legitimate to omit it or declare it separately transverse.

### 6.4 Internal W line and the Feynman-gauge remainder

For all incoming three-W momenta \((q,k,-k-q)\), the stripped tree vertex obeys
\[
q^\alpha\Gamma_{\alpha\mu\nu}^{abc}
=g_2f^{abc}\big[\mathcal K_{\mu\nu}(k+q)-\mathcal K_{\mu\nu}(k)\big],
\]
where
\[
\mathcal K_{\mu\nu}(k)=k^2g_{\mu\nu}-k_\mu k_\nu.
\]
With \(D_{F,\mu\nu}(k)=g_{\mu\nu}/k^2\), the contracted propagator chain is
\[
D_F(k+q)\,[\mathcal K(k+q)-\mathcal K(k)]\,D_F(k)
=D_F(k)-D_F(k+q)+R_{\rm FG}(k,q),
\]
with
\[
\boxed{
R_{{\rm FG},\mu\nu}(k,q)
=\frac{k_\mu k_\nu-(k+q)_\mu(k+q)_\nu}
{k^2(k+q)^2}.
}
\]
The remainder is nonzero at generic \(k,q\). Thus the three-W insertion is not a simple difference of Feynman-gauge propagators. The remainder must stay in the gauge-fixing/Slavnov–Taylor ledger until the complete gauge-sector identity is assembled.

## 7. Nonexceptional five-point kinematics

The existing symmetric four-point point has \(\sum_i p_i=0\). It cannot be used literally for a five-point amplitude with \(q\ne0\). The five-point calculation must instead use the same infrared scale \(\mu_{\rm IR}\), the same regulator and the same UV/EFT subtraction convention, but an extended nonexceptional five-point momentum point.

A convenient rational Euclidean diagnostic point is
\[
p_1=\mu_{\rm IR}e_1,\quad
p_2=\mu_{\rm IR}e_2,\quad
p_3=\mu_{\rm IR}e_3,\quad
q=\mu_{\rm IR}e_4,\quad
p_4=-\mu_{\rm IR}(e_1+e_2+e_3+e_4).
\]
It obeys five-point momentum conservation and
\[
(p_1^2,p_2^2,p_3^2,p_4^2,q^2)
=\mu_{\rm IR}^2(1,1,1,4,1).
\]
No external momentum or pairwise sum of distinct external momenta vanishes. This is a proposed diagnostic point, not a replacement for the four-point symmetric point. The Ward right-hand side involves four-point functions with the appropriate shifted external momenta; it must be evaluated at those shifted arguments rather than identified with one fixed symmetric-point number.

## 8. Local reproduction and evidence boundary

The exact symbolic calculation is in
calculations/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.py, with captured output in
validation/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.txt.

The local checks establish:
- six four-point seed routings satisfy momentum conservation;
- all 24 direct five-point attachment routings satisfy momentum conservation at their vertices;
- the massless chiral fermion contraction is exact in all 16 Dirac-matrix components;
- the scalar-line Ward contraction is exact;
- the scalar seagull anticommutator is exact for all nine generator pairs;
- the bare three-W contraction is exact in all 16 Lorentz components;
- the Feynman-gauge W-propagator chain decomposition, including \(R_{\rm FG}\), is exact in all 16 components.

These are local algebraic/routing checks. They do **not** establish:
1. the full graph-specific Dirac numerator after restoring every Feynman-rule phase and weak-index ordering;
2. the complete sum of scalar seagull, matter-line, and three-W weak tensors;
3. the gauge-fixing/ghost Slavnov–Taylor completion;
4. the external-leg/LSZ and field/parameter/operator counterterms;
5. any integrated UV five-point hard coefficient or transverse form factor;
6. a complete \(WW\) Wilson coefficient.

The next calculation is B2b: restore the full graph-specific numerator and weak-generator ordering for each of the 24 entries, contract before integration, and compare the endpoint terms against the four-point Ward variation and the EFT local contacts. Only after that graph-level sum closes should the hard-region integrals be evaluated.
