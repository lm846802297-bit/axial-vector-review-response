# RC-001 — Oriented UV external-W five-point numerators and Feynman-rule phases

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-I/II  
**Status:** the all-incoming routing is now tied to the actual fermion-arrow orientation on the two sides of each cross-vertex box. The A- and B-oriented fermion WTI, the oppositely oriented scalar WTI, the scalar seagull group factor, the bare three-W contraction, the Feynman-gauge propagator-chain remainder, the conjugate same-vertex numerator relation, and the relative Feynman-rule phases are checked exactly. This fixes the graph-level numerator templates and phase bookkeeping, but the 24 amplitudes have not yet been summed into a complete Slavnov–Taylor identity.

## 1. Frozen action and Feynman-rule convention

Use
\[
D_\mu=\partial_\mu-i g_2 t^a W_\mu^a,\qquad t^a=\frac{\sigma^a}{2},
\]
\[
W_{\mu\nu}^a
=\partial_\mu W_\nu^a-\partial_\nu W_\mu^a
+g_2\epsilon^{abc}W_\mu^bW_\nu^c,
\]
and
\[
\mathcal L_{\rm int}\supset
-y_\ell\bar L_\ell H E_{\ell R}
-y_\ell^\ast\bar E_{\ell R}H^\dagger L_\ell.
\]
The Fourier convention is \(\phi(x)=\int_p e^{-ipx}\phi(p)\), and all external momenta are incoming.

The stripped Feynman rules are:

| Interaction | Rule |
|---|---|
| Yukawa \(\bar LHE_R\) | \(-iy_\ell P_R\) |
| Conjugate Yukawa \(\bar E_RH^\dagger L\) | \(-iy_\ell^\ast P_L\) |
| \(W\bar L L\) | \(+ig_2\gamma^\mu t^aP_L\) |
| \(WHH^\dagger\) | \(+ig_2t^a(p_H-p_{H^\dagger})^\mu\) |
| \(W^a_\alpha W^b_\mu H^\dagger H\) | \(+ig_2^2\{t^a,t^b\}g^{\alpha\mu}\) |
| \(W^a_\alpha(q)W^b_\mu(k)W^c_\nu(-k-q)\) | \(+g_2\epsilon^{abc}\Gamma_{\alpha\mu\nu}(q,k,-k-q)\) |

The three-W sign follows from the displayed \(W_{\mu\nu}\) convention. With
\[
\Gamma_{\alpha\mu\nu}
=g_{\alpha\mu}(q-k)_\nu
+g_{\mu\nu}(2k+q)_\alpha
+g_{\nu\alpha}(-k-2q)_\mu,
\]
one has
\[
q^\alpha\Gamma_{\alpha\mu\nu}
=\mathcal K_{\mu\nu}(k+q)-\mathcal K_{\mu\nu}(k),
\qquad
\mathcal K_{\mu\nu}(k)=k^2g_{\mu\nu}-k_\mu k_\nu.
\]
The Feynman rule is \(+g_2\epsilon^{abc}\Gamma\), not \(-g_2\epsilon^{abc}\Gamma\), for this action convention.

The heavy propagator is projected as
\[
P_R\frac{i(\slashed h+M_E)}{h^2-M_E^2}P_L
=\frac{i\slashed hP_L}{h^2-M_E^2}.
\]
The mass numerator vanishes in the chirality-preserving channel.

## 2. Common four-point skeleton and exact numerator templates

For the four cross-vertex pairs LD-W-01/02/05/06, define
\[
P=p_1+p_2,\qquad h=k-P,
\]
\[
r_A=k-p_A,\qquad r_B=k+p_B.
\]
The internal W momentum \(k\) flows from the left Yukawa endpoint \(A\) to the right endpoint \(B\). The physical fermion/scalar propagator momentum on the A side is \(-r_A\), while on the B side it is \(+r_B\). This is the arrow-orientation information that the routing-only audit did not encode.

The scalar endpoint vectors fixed by the \(WHH^\dagger\) rule are
\[
V_A^\mu=2p_A^\mu-k^\mu
\quad(A=H),
\qquad
V_B^\nu=-2p_B^\nu-k^\nu
\quad(B=H^\dagger).
\]
The stripped matter numerators are
\[
X_A=
\begin{cases}
-\slashed r_A,&A=\bar L,\\
1,&A=H,
\end{cases}
\qquad
X_B=
\begin{cases}
+\slashed r_B,&B=L,\\
1,&B=H^\dagger.
\end{cases}
\]
The four-point numerator, before the common Feynman-rule phase and with the final chiral projector understood, is
\[
\mathcal N_{AB}
=\begin{cases}
\gamma^\mu X_A\slashed h X_B\gamma_\mu P_L,&A,B\text{ fermionic},\\
\gamma^\mu X_A\slashed h V_{B,\mu}P_L,&A\text{ fermionic},\ B\text{ scalar},\\
V_A^\mu\slashed h X_B\gamma_\mu P_L,&A\text{ scalar},\ B\text{ fermionic},\\
V_A^\mu V_{B,\mu}\slashed hP_L,&A,B\text{ scalar}.
\end{cases}
\]
At the exceptional point \(p_1=p_3=0,\ p_2=P,\ p_4=-P\), this reproduces the four previously recorded numerator chains:
\[
\begin{aligned}
N_{01}&=\gamma^\mu(-\slashed k)\slashed{(k-P)}
\slashed{(k-P)}\gamma_\mu,\\
N_{02}&=\gamma^\mu(-\slashed k)\slashed{(k-P)}(-k_\mu),\\
N_{05}&=(2P-k)_\mu\slashed{(k-P)}
\slashed{(k-P)}\gamma^\mu,\\
N_{06}&=-(2P-k)\cdot k\,\slashed{(k-P)}.
\end{aligned}
\]
The numerator factors \(-\slashed r_A\) and \(+\slashed r_B\) are not interchangeable: they follow from the fermion-arrow orientation on the left and right sides of the box.

## 3. Cross-vertex five-point routes and graph-specific numerators

For an external \(W^a(q)\), keep
\[
r_A^W=r_A,\quad r_A^Y=r_A-q,\qquad
r_B^W=r_B,\quad r_B^Y=r_B+q.
\]
An insertion on the A-side line transfers \(q\) into the left Yukawa channel, so
\[
h_A=h-q.
\]
An insertion on the B-side line leaves \(h\) unchanged. An insertion on the internal W line has momenta \(k\) and \(k+q\), leaves \(h\) unchanged, and shifts the B-side matter momentum to \(r_B+q\).

The graph numerators are generated from the following replacements in the common skeleton. All expressions below have the same final \(P_L\) as the four-point skeleton.

### 3.1 External W on an A-side fermion line

For \(A=\bar L\),
\[
\boxed{
X_A\longrightarrow
(-\slashed r_A^W)\gamma^\alpha(-\slashed r_A^Y),
\qquad h\longrightarrow h-q.
}
\]
Thus, for LD-W-01 and LD-W-02,
\[
\mathcal N_{A,F}^\alpha
=\gamma^\mu(-\slashed r_A^W)\gamma^\alpha
(-\slashed r_A^Y)\slashed{(h-q)}X_BJ_{B,\mu},
\]
where \(J_B^\nu=\gamma^\nu\) for \(B=L\) and \(J_B^\nu=V_B^\nu\) for \(B=H^\dagger\).

The denominator is
\[
k^2(r_A^W)^2(r_A^Y)^2(r_B^W)^2
[(h-q)^2-M_E^2].
\]

### 3.2 External W on an A-side scalar line

For \(A=H\),
\[
\boxed{
X_A\longrightarrow (r_A^W+r_A^Y)^\alpha,
\qquad h\longrightarrow h-q.
}
\]
The numerator is
\[
\mathcal N_{A,S}^\alpha
=V_A^\mu(r_A^W+r_A^Y)^\alpha
\slashed{(h-q)}X_BJ_{B,\mu}.
\]
The denominator is the same A-insertion denominator as in §3.1. The scalar-line WTI has the A-side endpoint order shown in §5.2.

### 3.3 External W on a B-side fermion line

For \(B=L\),
\[
\boxed{
X_B\longrightarrow
\slashed r_B^Y\gamma^\alpha\slashed r_B^W,
\qquad h\longrightarrow h.
}
\]
Thus, for LD-W-01 and LD-W-05,
\[
\mathcal N_{B,F}^\alpha
=J_A^\mu X_A\slashed h
\slashed r_B^Y\gamma^\alpha\slashed r_B^W
\gamma_\mu,
\]
where \(J_A^\mu=\gamma^\mu\) for \(A=\bar L\) and \(J_A^\mu=V_A^\mu\) for \(A=H\).

The denominator is
\[
k^2(r_A^W)^2(r_B^W)^2(r_B^Y)^2(h^2-M_E^2).
\]

### 3.4 External W on a B-side scalar line

For \(B=H^\dagger\),
\[
\boxed{
X_B\longrightarrow (r_B^W+r_B^Y)^\alpha,
\qquad h\longrightarrow h.
}
\]
The numerator is
\[
\mathcal N_{B,S}^\alpha
=J_A^\mu X_A\slashed h
(r_B^W+r_B^Y)^\alpha V_{B,\mu}.
\]
The denominator is the same B-insertion denominator as in §3.3. Its longitudinal endpoint order is opposite to the A-side scalar identity.

### 3.5 Scalar seagulls

If \(A=H\), the A-side scalar three-point vertex is replaced by the two-gauge seagull:
\[
\boxed{
J_A^\mu X_A\longrightarrow
g^{\alpha\mu}\{t^a,t^b\},
\qquad r_A\longrightarrow r_A^Y,\quad h\longrightarrow h-q.
}
\]
If \(B=H^\dagger\),
\[
\boxed{
X_BJ_B^\nu\longrightarrow
g^{\alpha\nu}\{t^a,t^b\},
\qquad r_B\longrightarrow r_B^Y,\quad h\longrightarrow h.
}
\]
These are separate graphs, not replacements for the ordinary scalar-line insertion. For \(t^a=\sigma^a/2\),
\[
\{t^a,t^b\}=\frac12\delta^{ab}\mathbf1.
\]
The seagull's longitudinal contraction is nonzero and must be combined with the corresponding scalar-line insertion before an endpoint identity is claimed.

### 3.6 External W on the internal W line

Replace the single W propagator by propagators with momenta \(k\) and \(k+q\), and insert
\[
\Gamma_{\alpha\mu\nu}(q,k,-k-q).
\]
The B-side matter endpoint is shifted:
\[
r_B\longrightarrow r_B+q,\qquad
V_B^\nu(k)\longrightarrow V_B^\nu(k+q)
=-2p_B^\nu-(k+q)^\nu
\]
when \(B=H^\dagger\). The numerator is
\[
\boxed{
\mathcal N_{3W}^\alpha
=J_A^\mu X_A\slashed h\,X_B^YJ_B^\nu
\Gamma^\alpha{}_{\mu\nu}(q,k,-k-q),
}
\]
where \(X_B^Y=\slashed{(r_B+q)}\) for \(B=L\), and \(J_B^\nu=V_B^\nu(k+q)\) for \(B=H^\dagger\). Its denominator is
\[
k^2(k+q)^2(r_A^W)^2(r_B^Y)^2(h^2-M_E^2).
\]
The Feynman-gauge contraction of the two W propagators is not a pure propagator difference; the nonzero \(R_{\rm FG}\) term in Stage A remains.

## 4. Same-vertex triangles LD-W-03/04

For LD-W-03, the fixed loop routing is
\[
r_F=k+p_1,\qquad r_S=p_2-k,\qquad
P_{FS}=p_1+p_2.
\]
Its stripped numerator is
\[
N_{03}=\gamma_\mu\slashed r_F(2p_2-k)^\mu.
\]
The conjugate right-vertex orientation is fixed by Dirac-Hermitian conjugation:
\[
N_{04}=\left(N_{03}\right)^{\dagger_D}
=(2p_3-k)_\mu\slashed{(k+p_4)}\gamma^\mu
\]
after the corresponding external-momentum relabeling. The relation is checked as a 16-component matrix identity. This is the correct way to fix the conjugate numerator orientation; it must not be regenerated by copying the left-vertex scalar momentum factor without conjugating the full fermion/scalar ordering.

For either same-vertex triangle, the external W insertion transfers \(q\) into the heavy channel:
\[
P_{FS}\longrightarrow P_{FS}+q.
\]
The four attachment classes are:
1. external W on the internal fermion segment, splitting its propagator into the two adjacent momenta;
2. external W on the internal scalar segment, with the scalar three-point vertex \(p_H-p_{H^\dagger}\) evaluated from its actual field orientation;
3. the scalar two-gauge seagull at the scalar endpoint;
4. the three-W insertion on the internal W line, with the fermion-side momentum shifted by \(q\).

Their denominators are the same four topology templates recorded in the Stage-B1 routing note, with the heavy denominator \([(P_{FS}+q)^2-M_E^2]\) in every case. The LD-W-03/04 hard-minus-EFT contribution remains zero at \(O(M_E^{-2})\); this does not remove these four attachments per pair from the Ward sum.

## 5. Oriented longitudinal line identities

The generic line WTI used in Stage A must be written in the orientation of the actual box line. The A and B sides have opposite physical propagator momenta.

### 5.1 Fermion lines

On the A side, \(r_A^W=r_A^Y+q\) and the physical propagator momenta are \(-r_A^W,-r_A^Y\):
\[
\boxed{
S_F(-r_A^W)\slashed q P_L S_F(-r_A^Y)
=S_F(-r_A^W)P_R-P_LS_F(-r_A^Y).
}
\]
On the B side, \(r_B^Y=r_B^W+q\):
\[
\boxed{
S_F(r_B^Y)\slashed q P_L S_F(r_B^W)
=P_LS_F(r_B^W)-S_F(r_B^Y)P_R.
}
\]
Both are exact off-shell identities. Their opposite endpoint ordering is essential when the internal W generator and external W generator are restored.

### 5.2 Scalar lines

For \(\Delta(r)=1/r^2\), the external scalar-W vertex on the A side gives
\[
\boxed{
\Delta(r_A^W)\,
q\cdot(r_A^W+r_A^Y)\,
\Delta(r_A^Y)
=\Delta(r_A^Y)-\Delta(r_A^W).
}
\]
On the B side,
\[
\boxed{
\Delta(r_B^Y)\,
q\cdot(r_B^W+r_B^Y)\,
\Delta(r_B^W)
=\Delta(r_B^W)-\Delta(r_B^Y).
}
\]
The signs are opposite because the physical scalar momentum flows oppositely on the two sides of the internal W exchange.

### 5.3 Seagull and three-W completion

The scalar seagull is
\[
V_{\rm sg}^{a b,\alpha\mu}
=ig_2^2\{t^a,t^b\}g^{\alpha\mu},
\qquad
q_\alpha V_{\rm sg}^{a b,\alpha\mu}
=ig_2^2\{t^a,t^b\}q^\mu.
\]
It is nonzero by itself. It completes the scalar Compton/Ward identity together with the scalar-line insertion.

The three-W identity is
\[
q^\alpha\Gamma_{\alpha\mu\nu}
=\mathcal K_{\mu\nu}(k+q)-\mathcal K_{\mu\nu}(k).
\]
In Feynman gauge,
\[
D_F(k+q)[\mathcal K(k+q)-\mathcal K(k)]D_F(k)
=D_F(k)-D_F(k+q)+R_{\rm FG},
\]
\[
R_{{\rm FG},\mu\nu}
=\frac{k_\mu k_\nu-(k+q)_\mu(k+q)_\nu}
{k^2(k+q)^2}.
\]
The \(R_{\rm FG}\) term remains in the gauge-fixing/Slavnov–Taylor ledger. The ordinary Feynman-gauge propagator cannot be substituted for the transverse kernel before this term is treated.

## 6. Relative Feynman-rule phases

For any of the six four-point seed skeletons, the product of the two Yukawa vertices, two gauge endpoints, three matter propagators (heavy plus two light), and one internal-W propagator is
\[
P_4=(-i)^2(i)^2(i)^3(-i)
=-g_2^2|y_\ell|^2
\]
after restoring the couplings. Relative to this common four-point phase:

| Five-point topology | Additional/replaced Feynman rules | Relative phase |
|---|---|---:|
| Ordinary fermion-line insertion | one \(+ig_2\) vertex and one additional \(i\) propagator | \(-g_2\) |
| Ordinary scalar-line insertion | one \(+ig_2\) vertex and one additional \(i\) propagator | \(-g_2\) |
| Scalar seagull | replace \(+ig_2t^bV^\mu\) by \(+ig_2^2\{t^a,t^b\}g^{\alpha\mu}\) | \(+g_2\), with the anticommutator retained |
| Internal-W insertion | replace \(-iD_F\) by two \(-iD_F\)'s and \(+g_2f^{abc}\Gamma\) | \(-ig_2\) |

These phase ratios are common to the cross-vertex and same-vertex skeletons. The momentum signs in \(X_A,X_B,V_A,V_B\), the weak-generator ordering, and the seagull anticommutator remain separate factors. In particular, the weak commutator identity from the B2b audit cannot by itself determine a graph cancellation until it is multiplied by these oriented phases and the actual numerator order.

## 7. External legs and counterterms remain separate

The 24 internal attachments are not the entire five-point Green function. Keep the four external-leg emissions in a separate reducible/LSZ ledger, with the shifted four-point amplitude on the right-hand side of the Ward identity. The renormalized identity also requires the \(W\)-field/gauge-coupling counterterms, \(L,H\) field terms, \(y_\ell,M_E\) parameter terms, the EFT \(C_{LD}\) and operator counterterms, and the gauge-fixing/ghost sector.

In the unbroken phase there are no electroweak Goldstone modes associated with a broken \(SU(2)_L\) generator. Ghosts are still present in the covariant-gauge Slavnov–Taylor identity. In a broken-phase extension, Goldstone vertices and fermion mass terms must be restored together.

## 8. Exact local reproduction and evidence boundary

The SymPy audit is in
calculations/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.py
with output in
validation/RC-001-dim6-WW-fivepoint-oriented-numerators-phases.txt.

It checks:
- A-oriented fermion WTI: 16/16 Dirac components;
- B-oriented fermion WTI: 16/16 Dirac components;
- A/B scalar WTI: 2/2 identities;
- scalar seagull anticommutator: 9/9 generator pairs;
- three-W contraction: 16/16 Lorentz components;
- Feynman-gauge W-chain decomposition including \(R_{\rm FG}\): 16/16 components;
- LD-W-03/04 Dirac-Hermitian conjugate numerator relation: 16/16 components;
- the relative Feynman-rule phase ratios in §6.

These are exact line-level and phase-bookkeeping checks. They do **not** establish:
1. the full weak/Lorentz sum of all 24 graph amplitudes;
2. the cancellation of the matter-line commutator against the three-W contribution;
3. the scalar-line/seagull endpoint sum for every weak-index ordering;
4. the ghost/gauge-fixing Slavnov–Taylor completion;
5. the external-leg and counterterm sum;
6. any integrated five-point hard coefficient or transverse form factor.

The next task is B2c-III/IV: assemble the explicit numerator and phase of every graph with its weak tensor, contract \(q_\alpha\) before integration, and compare the sum to the shifted four-point UV Ward variation plus the EFT contact. Only after that sum is closed should the five-point hard-region integrals begin.
