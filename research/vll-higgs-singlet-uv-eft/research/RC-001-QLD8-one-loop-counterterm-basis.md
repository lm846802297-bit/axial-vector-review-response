# RC-001 QLD8: one-loop Green-basis and evanescent seed closure

**Date:** 2026-11-10  
**Workstream:** PR #11, strict \(O(M_E^{-4})\) Higgs-source-square sector  
**Stage:** P1.0 basis construction plus P1.1a–P1.1c, P1.2, P1.3a–P1.3b, P1.4a, and P1.4b0 QCD/evanescent setup  
**Status:** source-pair, representation, derivative, gamma-string, QCD color, momentum-routing, and formal \(d\)-dimensional direct-tensor projection checks pass locally. The higher-rank Gram obstruction is identified. No loop kernel, UV pole, or one-loop \(Z\) matrix is yet calculated.

## 1. Scope and non-negotiable boundary

The retained source is
\[
\mathcal J_H^{(4)}=\mathcal J_d+\mathcal J_u+\mathcal J_e,
\]
with
\[
\begin{aligned}
\mathcal J_d^k&=\bar d_{R\,r,a}(Y_d^\dagger)_{rp}Q_{L\,p,a}^k,\\
\mathcal J_u^k&=\epsilon_{ik}\bar Q_{L\,p,a}^{\,i}(Y_u)_{pr}u_{R\,r,a},\\
\mathcal J_e^k&=y_e^*\bar e_R L_e^k.
\end{aligned}
\]
The strict source-square sector is
\[
\mathcal O_{\rm src}^{(8)}
=\sum_{A,B=d,u,e}(D_\mu\mathcal J_A^k)^\dagger
D^\mu\mathcal J_B^k.
\]
The \(C_{5,\ell}\) axial-lepton sources are not included: their cross terms start at \(M_E^{-5}\), and their squares at \(M_E^{-6}\).

This is a four-fermion/two-derivative operator-renormalization problem. It is not a calculation of the \(hh\), \(hs\), or \(ss\) scalar two-point functions. No coefficient from this note is to be inserted into PR #69.

## 2. Freeze the source-pair sectors

All three sources transform as \((\mathbf1,\mathbf2,+1/2)\) under \(SU(3)_c\times SU(2)_L\times U(1)_Y\). The retained source fermions \(Q_L,u_R,d_R,L_e,e_R\) are neutral under \(U(1)_{L_\mu-L_\tau}\). Thus this restricted source-square block has no direct \(A'\) or \(F_X^{\mu\nu}\) gauge vertex. The Wilson coefficient can still inherit UV-model parameters; that does not create a light-field \(U(1)_X\) interaction in this block.

| Pair | Chiral seed after source expansion | 4D Fierz physical seed | Color basis | Weak contraction | Flavor tensor |
|---|---|---|---|---|---|
| \(d^\dagger d\) | \(P_R\otimes P_L\) | vector \(\otimes\) vector | \(1,8\) | singlet | \(Y_d\otimes Y_d^\dagger\) |
| \(u^\dagger u\) | \(P_L\otimes P_R\) | vector \(\otimes\) vector | \(1,8\) | singlet | \(Y_u^\dagger\otimes Y_u\) |
| \(e^\dagger e\) | \(P_R\otimes P_L\) | vector \(\otimes\) vector | \(1\) | singlet | \(|y_e|^2\) |
| \(d^\dagger u\) | \(P_R\otimes P_R\) | scalar plus tensor | \(1,8\) | \(\epsilon_{ik}\) singlet | \(Y_d\otimes Y_u\) |
| \(d^\dagger e\) | \(P_R\otimes P_L\) | vector \(\otimes\) vector | \(1\) | singlet | \(Y_d\otimes y_e^*\) |
| \(u^\dagger e\) | \(P_L\otimes P_L\) | scalar plus tensor | \(1\) | \(\epsilon_{ik}\) singlet | \(Y_u^\dagger\otimes y_e^*\) |

The six rows are three diagonal pairs and three independent cross pairs; each cross pair is accompanied by its Hermitian conjugate. Equivalently, the ordered expansion contains nine pairs. Each ordered pair has four product-rule derivative placements, hence 36 ordered placements in the full source square. These are not 36 independent Wilson coefficients.

For quark crossed-color contractions, use the fixed normalization
\[
\operatorname{tr}(T^AT^B)=\frac12\delta^{AB},\qquad
\delta_{ad}\delta_{cb}
=\frac1{N_c}\delta_{ab}\delta_{cd}
+2T^A_{ab}T^A_{cd},\qquad N_c=3.
\]
The singlet/octet basis must be retained. A crossed contraction is not to be replaced by a singlet-current product alone. Quark-lepton rows have only the quark singlet color contraction.

The weak \(\epsilon_{ik}\) in \(d^\dagger u\) and \(u^\dagger e\) is an \(SU(2)\) singlet contraction. Do not split it into independent weak components before applying the weak-index identities. Flavor tensors remain general; no diagonal-Yukawa or generation-degeneracy approximation is introduced.

## 3. Green basis first; EOM quotient later

For the loop calculation, use an off-shell Green basis. Do **not** apply the first- or second-order fermion EOM before extracting UV poles. EOM reduction is a quotient on the renormalized local operator space and can otherwise hide EOM counterterms or contaminate the off-shell projectors.

For a source pair \(A^\dagger B\), label the two derivative placements by \(r,s\in\{0,1\}\):
- \(r=0\): the derivative in the first source acts on its barred fermion; \(r=1\): it acts on its unbarred fermion;
- \(s=0\): the derivative in the second source acts on its barred fermion; \(s=1\): it acts on its unbarred fermion.

Fierz rearrangement changes the spinor pairing, not the field on which a derivative acts. Keep \((r,s)=(0,0),(0,1),(1,0),(1,1)\) distinct until the full IBP/EOM map is applied.

For four off-shell external momenta \(p_1,\ldots,p_4\), impose only
\[
p_1+p_2+p_3+p_4=0.
\]
The scalar momentum polynomials of degree two span six independent Gram invariants. One possible choice is
\[
p_1^2,\ p_2^2,\ p_3^2,\ p_4^2,\ p_1\!\cdot p_2,\ p_1\!\cdot p_3.
\]
Keep \(\slashed p_i\) and any free Lorentz-index projectors as separate Dirac/tensor structures. The four source placements are only a tree-level subspace of this off-shell polynomial space: one-loop counterterms may also contain \(p_i^2\) structures and derivative placements related by EOM or total derivatives.

The EOM-reduced physical quotient must retain, rather than discard, the following dimension-eight classes:
1. four fermions with two covariant derivatives;
2. four fermions with one covariant Higgs derivative, generated by the Yukawa part of the second-order EOM;
3. four fermions with a gauge-field strength, generated by the curvature term;
4. gauge-EOM/current representatives where a derivative acts on a field strength.

The commutator \([D_\mu,D_\nu]\) must be kept until the field-strength operators have been projected. If a gauge-field EOM is used, choose either the field-strength-derivative representative or its complete matter-current replacement, never both.

## 4. Evanescent seed tower beyond the tree-level Fierz differences

Use unit-weight antisymmetrized gamma strings
\[
\Gamma_{(n)}^{\mu_1\ldots\mu_n}
=\gamma^{[\mu_1}\cdots\gamma^{\mu_n]}.
\]
For \(g_{\mu\nu}=(+---)\), \(\epsilon^{0123}=+1\), and
\(\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3\), define
\(\eta_R=+1,\eta_L=-1\). Exact four-dimensional identities are
\[
\Gamma_{(3)}^{\mu\nu\rho}
=i\epsilon^{\mu\nu\rho\sigma}\gamma_\sigma\gamma_5,
\qquad
\Gamma_{(4)}^{\mu\nu\rho\sigma}
=-i\epsilon^{\mu\nu\rho\sigma}\gamma_5.
\]
Consequently, for direct spinor pairing,
\[
\begin{aligned}
(\Gamma_{(3)}^{\mu\nu\rho}P_X)\otimes
(\Gamma_{(3)\mu\nu\rho}P_Y)
&\xrightarrow{4D}
6\eta_X\eta_Y
(\gamma^\mu P_X)\otimes(\gamma_\mu P_Y),\\
(\Gamma_{(4)}^{\mu\nu\rho\sigma}P_X)\otimes
(\Gamma_{(4)\mu\nu\rho\sigma}P_Y)
&\xrightarrow{4D}
24\eta_X\eta_Y
P_X\otimes P_Y.
\end{aligned}
\]
The coefficients and signs have been checked with explicit Minkowski gamma matrices for all four \(XY=RR,RL,LR,LL\) choices.

This motivates the direct-pairing evanescent seeds
\[
\begin{aligned}
E_{3;XY}&=
(\bar\psi\Gamma_{(3)}^{\mu\nu\rho}P_X\chi)
(\bar\eta\Gamma_{(3)\mu\nu\rho}P_Y\xi)
-6\eta_X\eta_Y
(\bar\psi\gamma^\mu P_X\chi)
(\bar\eta\gamma_\mu P_Y\xi),\\
E_{4;XY}&=
(\bar\psi\Gamma_{(4)}^{\mu\nu\rho\sigma}P_X\chi)
(\bar\eta\Gamma_{(4)\mu\nu\rho\sigma}P_Y\xi)
-24\eta_X\eta_Y
(\bar\psi P_X\chi)(\bar\eta P_Y\xi).
\end{aligned}
\]
Each seed inherits the same color, weak, flavor, and derivative-placement labels as its parent physical operator. These definitions use no \(O(\epsilon)\) physical-operator admixture. They are direct-pairing definitions; if a crossed spinor pairing is used, the Grassmann exchange sign must be applied separately. Do not combine that sign twice with the existing \(E_{XY;V/T}^{\mu,\mu\nu}\) Fierz-difference definitions.

The one-loop gauge-exchange graphs acting on the current-current and scalar/tensor seeds can generate rank-three and rank-four antisymmetrized strings. The rank-three/rank-four seeds above are therefore required candidates. This is **not yet a proof of closure**: the actual set of \(\Gamma_{(n)}\otimes\Gamma_{(m)}\) structures, including mixed-rank structures and derivative-index correlations, must be read from the explicit one-loop numerators. The counterterm generator must fail loudly if it encounters a structure outside the declared basis; it must not project it away using four-dimensional identities.

## 5. Counterterm-matrix definition and calculation boundary

For a chosen off-shell operator vector \(\mathcal O=(\mathcal O_P,\mathcal O_E,\mathcal O_{\rm EOM})\), define
\[
\mathcal O^{\rm bare}_i=Z_{ij}\mathcal O^{\rm ren}_j,\qquad
Z_{ij}=\delta_{ij}+\frac{1}{16\pi^2\epsilon}
\left[g_s^2 Z^{(s)}_{ij}+g_2^2 Z^{(2)}_{ij}
+g'^2 Z^{(1)}_{ij}+\cdots\right]+\cdots.
\]
Yukawa-dependent entries and background-gauge mixing are separate blocks. There is no direct \(g_X\) exchange on the retained \(J_H^{(4)}\) constituent fields. The displayed equation is a matrix organization, not a computed result.

The UV pole calculation must include:
- all one-loop attachments to the four external fermion legs;
- gauge exchange between every allowed pair of legs;
- the gauge-contact vertices contained in the covariant derivatives;
- external-leg/wavefunction counterterms;
- all color and weak contractions;
- the complete set of local degree-two momentum and Dirac projectors;
- background-gauge amplitudes needed to identify \(4\psi F_{\mu\nu}\) and gauge-EOM counterterms.

Use generic nonexceptional Euclidean external momenta so the UV poles are not confused with scaleless UV/IR cancellations. The same NDR/\(\overline{\rm MS}\) and evanescent definitions must be used in the UV and EFT calculations.

## 6. Staged one-loop calculation order

1. **QCD pilot block:** start with \(d^\dagger d\), retaining the color singlet/octet and all four derivative placements. This is the cleanest test of the RL vector-current sector and the covariant-derivative contact terms.
2. **QCD same-chirality block:** add \(d^\dagger u\), which tests the RR scalar/tensor sector and the weak-\(\epsilon\) contraction.
3. **Remaining gauge blocks:** add \(u^\dagger u\), then \(d^\dagger e\), \(u^\dagger e\), and \(e^\dagger e\); include \(SU(2)_L\) and hypercharge exchange with their exact representation factors.
4. **Background-field block:** calculate one- and two-background-gauge Green functions and check the Ward identities before replacing any gauge-EOM operators by currents.
5. **Yukawa and EOM blocks:** include Higgs/Yukawa interactions and the EOM-generated \(4\psi D H\), \(4\psi F\), and gauge-current operators.
6. **EFT soft subtraction:** calculate the same external Green functions with the same IR rearrangement and scheme, then perform hard-minus-soft matching.
7. **Only after matching:** reduce to the final nonredundant physical dimension-eight basis and compare any induced scalar-sector projection separately.

The first two steps are chosen to expose both color mixing and same-chirality tensor mixing before the full SM gauge/Yukawa calculation is attempted.

## 7. Validation and claim boundary

The exact companion audit checks:
- all 64 rank-three and 256 rank-four index assignments for the four-dimensional gamma dualities;
- the contracted rank-three and rank-four projections for \(RR,RL,LR,LL\);
- the \(SU(3)\) fundamental completeness relation in all 81 color-index assignments;
- the Higgs-source hypercharges and the \(SU(2)\)-singlet epsilon contraction;
- the nine ordered source pairs and 36 derivative placements.

It does **not** evaluate a loop integral, a UV pole, \(Z_{ij}\), an anomalous dimension, or a finite Wilson coefficient. P1.0 closes the bookkeeping and exact four-dimensional projection seeds needed to start P1.1; the complete d-dimensional counterterm basis and one-loop renormalization remain open.


## 8. P1.1a: QCD color factors for the \(d^\dagger d\) pilot

The first four-quark QCD pilot is now fixed to the external-leg order
\((\bar Q,Q,\bar d,d)\). The source-pair color tensor after spinor crossing is
\[
C_X^{ij;kl}=\delta_{il}\delta_{kj}
=\frac13C_1^{ij;kl}+2C_8^{ij;kl},
\]
where \(C_1=\delta_{ij}\delta_{kl}\) and
\(C_8=T^A_{ij}T^A_{kl}\).

The six pairwise color-generator matrices are derived and checked in
[RC-001-QLD8-QCD-color-factor-block.md](RC-001-QLD8-QCD-color-factor-block.md).
Their sum satisfies the exact color-singlet identity
\[
\sum_{a<b}\mathbf T_a\cdot\mathbf T_b
=-2C_F\mathbf1=-\frac83\mathbf1.
\]
This closes the group-theory factorization of the six QCD exchange topologies
for the \(d^\dagger d\) pilot. It does not supply their Feynman-rule signs,
Dirac/momentum kernels, UV poles, or counterterms.

The exact SU(3) calculation is in
\`calculations/RC-001-QLD8-QCD-color-factor-audit.py\`, with output in
\`validation/RC-001-QLD8-QCD-color-factor-audit.txt\`. The QLD8 CI workflow
now runs both the basis/Dirac seed audit and this color-factor audit.


## 9. P1.1b: \(d^\dagger d\) QCD insertion momentum and topology routing

The first QCD pilot now has a fixed all-incoming external-momentum convention:
\[
\bar Q(p_1),\quad d(p_2),\quad \bar d(p_3),\quad Q(p_4),
\qquad \sum_i p_i=0.
\]
The two source-current momenta are \(q_A=p_1+p_2\) and
\(q_B=p_3+p_4=-q_A\). The four product-rule placements sum exactly to
\[
-q_A\cdot q_B=q_A^2.
\]

For a gluon momentum \(\ell\) flowing from the second named external leg to
the first, the six exchange topologies have been routed explicitly.
Exchanges within one original source current leave \(q_A\) unchanged;
exchanges across the two currents give \(q_A+\ell\) or \(q_A-\ell\).
Consequently their insertion factors are respectively \(q_A^2\) and
\((q_A\pm\ell)^2\). The \(\ell^2\) and \(q_A\cdot\ell\) terms must remain
in the loop numerator.

The routing derivation and exact symbolic check are in
\`research/RC-001-QLD8-QCD-one-loop-momentum-routing.md\`,
\`calculations/RC-001-QLD8-QCD-momentum-routing-audit.py\`, and
\`validation/RC-001-QLD8-QCD-momentum-routing-audit.txt\`. The updated
QLD8 workflow now runs the basis, color, and momentum-routing audits.

This closes the insertion-momentum routing algebra, not the loop calculation:
the six open-line Dirac numerators, tensor integrals, wavefunction
counterterms, UV poles, and evanescent projections remain to be evaluated.


## 10. P1.1c: direct-pairing \(RL\) tensor evanescent

A two-gamma open-line chain in the direct \(d^\dagger d\) source pairing obeys
\[
(\gamma^\mu\gamma^\nu P_R)\otimes(P_L\gamma_\nu\gamma_\mu)
=
D\,P_R\otimes P_L
+\sigma^{\mu\nu}P_R\otimes\sigma_{\mu\nu}P_L.
\]
The direct opposite-chirality tensor contraction vanishes exactly in four
dimensions by the self-duality/anti-self-duality of the two chiral tensor
representations. It is therefore a candidate direct-pairing evanescent
\[
E_{T;RL}^{\rm dir}
=(\bar Q\sigma^{\mu\nu}P_Rd)
(\bar d\sigma_{\mu\nu}P_LQ).
\]
The \(D=4-2\epsilon\) scalar coefficient \(D=4-2\epsilon\) must be retained:
the \(-2\epsilon\) term can multiply a \(1/\epsilon\) UV pole and contribute
to the finite matching term.

The exact four-dimensional tensor and gamma-chain checks have been added to
\`calculations/RC-001-QLD8-counterterm-basis-audit.py\` and its validation
output. The dedicated interpretation is in
\`research/RC-001-QLD8-RL-tensor-evanescent-seed.md\`.

The scalar–vector difference \(E_{RL;V}^{\mu,rs}\) is not the direct Fierz image of this Lorentz-scalar tensor–tensor structure. Also distinguish the direct-pairing rank-three seed \(E_{3;RL}^{\rm dir}\) from the crossed rank-three channel \(X_3^{RL}\). The formal crossed odd-rank projection is derived in the P1.2 record below. Its rank-five Gram inverse is singular at \(D=4\), so no regular finite rank-one/rank-three-only basis change is available. Keep the direct tensor, direct rank-three, and crossed odd-rank labels separate until the actual one-loop gamma-rank closure and Gram matrix are fixed. No graph coefficient or UV pole is inferred from this algebraic projection.


## 11. P1.2: formal \(d\)-dimensional Fierz projection of the direct \(RL\) tensor

The direct-pairing tensor seed
\[
\mathcal T_{RL}^{\rm dir}
=(\sigma^{\mu\nu}P_R)\otimes(\sigma_{\mu\nu}P_L)
\]
has a crossed projection onto odd-rank chiral structures
\[
X_n^{RL}
=(\Gamma^{(n)}P_R)\widetilde\otimes
(\Gamma_{(n)}P_L),\qquad n\ {\rm odd}.
\]
For unit-weight antisymmetrized gamma strings, the sandwich identity is
\[
\sigma^{\mu\nu}\Gamma^{(n)}\sigma_{\mu\nu}
=\lambda_n(D)\Gamma^{(n)},\qquad
\lambda_n(D)=D(D-1)-4n(D-n).
\]
The chiral trace norm is
\[
t_n(D)=2(-1)^{n(n-1)/2}D(D-1)\cdots(D-n+1).
\]
Projecting with the dual crossed tensor gives
\[
\boxed{
f_n(D)=
\frac{D(D-1)-4n(D-n)}
{2(-1)^{n(n-1)/2}D(D-1)\cdots(D-n+1)}.
}
\]
These are rank-channel projection coefficients; they are not a proof of finite closure in a rank-one/rank-three basis.

The first channels are
\[
f_1(D)=\frac{(D-1)(D-4)}{2D},\qquad
f_3(D)=-\frac{(D-4)(D-9)}{2D(D-1)(D-2)},
\]
\[
f_5(D)=\frac{D^2-21D+100}
{2D(D-1)(D-2)(D-3)(D-4)}.
\]
For \(D=4-2\epsilon\),
\[
f_1=-\frac34\epsilon+O(\epsilon^2),\qquad
f_3=-\frac5{24}\epsilon+O(\epsilon^2),
\]
but
\[
f_5=-\frac{1}{3\epsilon}-\frac{239}{144}+O(\epsilon).
\]
The \(f_5\) pole is not a loop UV pole: the rank-five Gram norm
\[
t_5(D)=2D(D-1)(D-2)(D-3)(D-4)
\]
vanishes at \(D=4\), and the singular coefficient comes from inverting this degenerate direction. It exposes why a rank-one/rank-three truncation cannot be used as a regular complete d-dimensional Fierz map.

At operator level, crossing the middle two Grassmann fields contributes one additional minus sign. The crossed color rearrangement is independent and retains both
\[
C_X=\frac13C_1+2C_8.
\]
The scalar–vector evanescent \(E_{RL;V}^{\mu,rs}\) is a different Lorentz sector; it must not be identified with this tensor–tensor projection. Likewise, the direct-pairing \(E_{3;RL}^{\rm dir}\) and crossed \(X_3^{RL}\) are distinct until the full Fierz map is applied.

The exact symbolic record and audit are:
- \`research/RC-001-QLD8-d-dimensional-RL-tensor-Fierz-map.md\`;
- \`calculations/RC-001-QLD8-ddim-Fierz-projection-audit.py\`;
- \`validation/RC-001-QLD8-ddim-Fierz-projection-audit.txt\`.

The explicit 4D matrix check for the \(\sigma\Gamma^{(n)}\sigma\) eigenvalues and the symbolic \(f_1,f_3,f_5\) checks pass locally. The result fixes the first crossed projections and exposes a higher-rank Gram obstruction. It does not yet select the canonical finite evanescent basis, evaluate a loop integral, extract a UV pole, or calculate any \(Z\)-matrix entry.


**Routing-sign clarification:** for each ordered pair \((a,b)\), the loop
momentum \(\ell\) flows from \(b\) to \(a\). With all external momenta
incoming at the operator insertion this gives \(r_a=p_a+\ell\) and
\(r_b=p_b-\ell\), exactly as used in the routing table. Reversing the
defined flow reverses all \(\ell\) signs and leaves the integral unchanged
after a consistent \(\ell\mapsto-\ell\) substitution.


## 12. P1.3a: align the QCD color basis with the direct spinor pairing

The \(d^\dagger d\) source is naturally in the direct spinor pairing
\[
(\bar Q_iP_Rd_i)(\bar d_jP_LQ_j).
\]
For the first QCD numerator calculation, there is no need to Fierz the
spinor indices into \((\bar Q Q)(\bar d d)\) before extracting UV poles.
Use the direct color basis
\[
C_{1,d}^{ij;kl}=\delta_{il}\delta_{kj},\qquad
C_{8,d}^{ij;kl}=T^A_{il}T^A_{kj},
\]
with tree vector \((1,0)_d\).

The direct and crossed color bases are related by
\[
\begin{pmatrix}C_{1,d}&C_{8,d}\end{pmatrix}
=
\begin{pmatrix}C_{1,x}&C_{8,x}\end{pmatrix}
\begin{pmatrix}1/3&4/9\\2&-1/3\end{pmatrix}.
\]
The six direct-basis color-exchange matrices are:
\[
\begin{array}{c|c}
(\bar Q,Q)&\begin{pmatrix}0&-2/9\\-1&-7/6\end{pmatrix}\\
(\bar Q,\bar d)&\begin{pmatrix}0&2/9\\1&-1/3\end{pmatrix}\\
(\bar Q,d)&\begin{pmatrix}-4/3&0\\0&1/6\end{pmatrix}\\
(Q,\bar d)&\begin{pmatrix}-4/3&0\\0&1/6\end{pmatrix}\\
(Q,d)&\begin{pmatrix}0&2/9\\1&-1/3\end{pmatrix}\\
(\bar d,d)&\begin{pmatrix}0&-2/9\\-1&-7/6\end{pmatrix}
\end{array}
\]
They are independently calculated from the Gell-Mann generators and
satisfy the exact similarity relation \(M_d=R^{-1}M_xR\), as well as
\[
\sum_{a<b}M_{ab}^{(d)}=-\frac83\mathbf1.
\]

This is the preferred color basis for the direct-pairing QCD numerator
calculation. The crossed basis in P1.1a remains an independent check.

On the tree vector \((1,0)_d\), the two within-source exchanges act as
\(-C_F(1,0)_d\), while the four cross-source exchanges act as
\((0,-1)_d\) for \((\bar Q,Q)\) and \((\bar d,d)\), and as
\((0,+1)_d\) for \((\bar Q,\bar d)\) and \((Q,d)\). Hence all
singlet-to-octet mixing comes from the four cross-source graphs; their
opposite color signs do not imply cancellation because their Dirac and
momentum kernels differ and must be integrated before summing.

The record and exact audit are:
- \`research/RC-001-QLD8-QCD-direct-pairing-color-basis.md\`;
- \`calculations/RC-001-QLD8-QCD-direct-color-basis-audit.py\`;
- \`validation/RC-001-QLD8-QCD-direct-color-basis-audit.txt\`.

This changes only the bookkeeping basis. No Dirac numerator, loop kernel,
UV pole, or counterterm coefficient has been evaluated.


## 13. P1.3b: six direct-pairing QCD open-line numerator chains

The \(d^\dagger d\) QCD pilot is now written without a premature spinor
Fierz crossing. For the external fields
\[
\bar Q(p_1),\quad d(p_2),\quad\bar d(p_3),\quad Q(p_4),
\]
the six Feynman-gauge exchange chains are recorded in
\`research/RC-001-QLD8-QCD-d-dagger-d-open-line-numerators.md\`.
The loop momentum convention is the corrected P1.1b convention:
for ordered pair \((a,b)\), \(\ell\) flows from \(b\) to \(a\), so
\(r_a=p_a+\ell\), \(r_b=p_b-\ell\).

The numerator table preserves the direct spinor pairing
\((\bar Q,d)\otimes(\bar d,Q)\), uses the direct color matrices of P1.3a,
and carries the insertion factors \(q_A^2\) or \((q_A\pm\ell)^2\) for the
six topologies. It records the open-line Dirac tensor only; overall graph
phases and relative Feynman-rule signs still require the complete amplitude
contraction convention. The four cross-source chains are now also decomposed explicitly into scalar, rank-two\(\otimes\)scalar, scalar\(\otimes\)rank-two, and rank-two\(\otimes\)rank-two pieces in the dedicated numerator note; the exact 4D matrix audit checks all 64 Lorentz-index assignments.

A useful exact algebraic result is that, in this direct pairing and in
Feynman gauge, each one-gluon exchange has gamma rank at most two on each
bilinear. Cross-bilinear exchanges reduce to the rank-\(0/2\) tensor-product
sector; same-bilinear exchanges use
\[
\gamma^\rho\slashed r\slashed s\gamma_\rho P_X
=D(r\cdot s)P_X+(D-4)\Gamma^{\mu\nu}r_\mu s_\nu P_X.
\] Since \(D-4=-2\epsilon\), its rank-two term is \(O(\epsilon)\) and must be retained when multiplied by a UV pole.
Thus the direct-pairing rank-two tensor and mixed rank-two\(\otimes\)scalar
structures must be retained, but no rank-three or rank-four direct string
is generated by these displayed one-gluon chains. This rank bound does not
survive a spinor Fierz crossing as a finite crossed-basis statement; P1.2
shows why the crossed odd-rank Gram tower is singular at \(D=4\).

The exact 4D matrix audit checks all four cross-chain decompositions for
64/64 Lorentz-index assignments and the same-bilinear contracted identity
for 16/16 assignments. Its output is in
\`validation/RC-001-QLD8-QCD-open-line-numerator-audit.txt\`.
The companion workflow now runs this audit.

The original \(J_d\) is a QCD color singlet, so \(D_\mu J_d=\partial_\mu J_d\)
has no independent QCD contact vertex in the original source representation.
The complete QCD four-point renormalization still requires the six exchange
graphs plus all four external-leg self-energy/wavefunction contributions.

No loop integral, UV pole, counterterm coefficient, \(Z\)-matrix entry, or
finite Wilson coefficient has been calculated. The next step is to fix all
relative graph signs, generate the complete \(D\)-dimensional tensor
integrands, and perform the nonexceptional off-shell UV extraction.


## 14. P1.4a: factorized QCD renormalization of the Yukawa-weighted source

For the retained Higgs-EOM source,
\[
J_d=\bar d_RY_d^\dagger Q_L=Y_d^\dagger S_d,\qquad
S_d=\bar d_RQ_L,
\]
the QCD renormalization of the SM Yukawa matrix and the scalar density
cancels. In the convention
\[
Y_{d,0}=Z_{Y_d}Y_d,\qquad S_{d,0}=Z_SS_d,
\]
one-loop \(\overline{\rm MS}\) gives
\[
Z_{Y_d}=Z_m
=1-\frac{3C_Fg_s^2}{16\pi^2\epsilon},\qquad
Z_S=Z_m^{-1}
=1+\frac{3C_Fg_s^2}{16\pi^2\epsilon}.
\]
Therefore
\[
\boxed{Z_{J_d}^{(s)}=Z_{Y_d}Z_S=1+O(g_s^4).}
\]
The same holds for \(J_d^\dagger\), and hence the factorized QCD
renormalization of \((D_\mu J_d^\dagger)(D^\mu J_d)\) vanishes at one loop.

Diagrammatically, the two within-source vertex corrections plus all four
external-leg self-energy/wavefunction terms reproduce the scalar-density
renormalization. The SM Yukawa counterterm then cancels it. Thus the
factorized subset must be grouped with the \(Y_d\) counterterm; it must not
be counted twice. The four cross-source exchange graphs remain and generate
the non-factorizing color/Dirac/derivative mixing.

The exact convention and derivation are in
\`research/RC-001-QLD8-QCD-Yukawa-source-renormalization-check.md\`.
This is a factorized-source identity, not the full QLD8 four-fermion
counterterm matrix or a finite Wilson coefficient.


## 15. P1.4b0: four cross-source graphs, scalar-scalar UV projection

The exact scalar projection of each cross-source open-line numerator is
\[
\frac14\operatorname{Tr}_{16}
[(P_R\otimes P_L)\mathcal N_{ab}]
=r_a\cdot r_b.
\]
This was checked for all four topologies at three independent momentum
samples (12/12 exact checks). A common auxiliary mass in the three
denominators separates the zero-momentum IR singularity; the degree-two
Taylor coefficient then gives the D-dimensional scalar UV kernel recorded
in \`research/RC-001-QLD8-cross-source-scalar-UV-pole.md\`.

After applying the direct-color tree-vector weights \((-1,+1,+1,-1)\),
the scalar-scalar projection simplifies to
\[
K_{\rm cross}^{SS}(D)
=\frac{D^2+10D-8}{48}
(p_1-p_2)\cdot(p_3-p_4).
\]
At \(D=4\), this is exactly
\[
(p_1-p_2)\cdot(p_3-p_4),
\]
the momentum polynomial of a direct-color-octet double-
\(\overleftrightarrow D\) scalar structure. This is a non-factorizing
cross-source mixing component; it is not proportional to the original
source-square polynomial \(q_A^2\).

The reproducible calculation and recorded output are:
- \`calculations/RC-001-QLD8-cross-source-scalar-UV-audit.py\`;
- \`validation/RC-001-QLD8-cross-source-scalar-UV-audit.txt\`.

**Boundary:** this is only the \(P_R\otimes P_L\) scalar projection. The
rank-two\(\otimes\)scalar, scalar\(\otimes\)rank-two, and
rank-two\(\otimes\)rank-two projections remain to be evaluated. The common
graph phase/sign must be restored in the full amplitude convention; the
auxiliary-mass rearrangement has not yet been promoted to a complete
\(R^*\) subtraction for the full operator basis. No complete QCD \(Z\)
matrix, anomalous-dimension block, EOM/IBP quotient, or finite
UV-minus-EFT Wilson coefficient is claimed.


## 15. P1.4b1: mixed rank-two/scalar cross-source UV projections

The mixed rank-two\(\otimes\)scalar and scalar\(\otimes\)rank-two projections
of the four cross-source QCD graphs have now been evaluated through the
degree-two UV Taylor coefficient. A necessary orientation clarification
was made in the numerator note: for the first two topologies the left/right
momentum pair is \((r_a,r_b)\), whereas for the last two it is
\((r_b,r_a)\). The scalar projection is insensitive to this swap, but the
rank-two projection is not.

With \(W(u,v)=\Gamma^{\mu\nu}u_\mu v_\nu\), the common auxiliary-mass
tensor integral for a topology with left/right momenta
\(x=A+s\ell\), \(y=B-s\ell\) gives
\[
T_i(D)=\frac{D-4}{12}W(A_i,B_i)
+\frac12W(q_A,A_i+B_i).
\]
The four ordered pairs are
\[
(A_i,B_i)=(p_1,p_4),(p_1,p_3),(p_2,p_4),(p_2,p_3).
\]
Combining the explicit gamma-chain signs with the direct color actions
\((-1,+1,+1,-1)\) gives
\[
K_{T\otimes S}(D)
=\frac{D+8}{12}W(q_A,p_4-p_3),
\]
\[
K_{S\otimes T}(D)
=-\frac{D+8}{6}W(p_1,p_2).
\]
Both have nonzero \(D\to4\) limits. Their \(D=4-2\epsilon\) common
prefactor is \(1-\epsilon/6\); retain this \(O(\epsilon)\) term for
finite-scheme bookkeeping.

The exact symbolic audit verifies the arbitrary-momentum wedge identities
and independent rational samples (6/6). See
\`research/RC-001-QLD8-cross-source-mixed-tensor-UV-poles.md\` and
\`validation/RC-001-QLD8-cross-source-mixed-tensor-UV-audit.txt\`.

This closes only the two mixed projections. The rank-two\(\otimes\)rank-two
projection is still required before the complete direct Dirac pole can be
assembled. The common graph phase, external-gluon completion, and
EOM/IBP reduction are also outstanding.


## 16. P1.4b2: full D-dimensional cross-source Lorentz tensor

The full degree-two UV Taylor tensor \(I_{\alpha\beta}(A,B;q_A)\) is now
derived in closed form. It contains the scalar, symmetric, and
antisymmetric Lorentz components required by the complete open-line
numerator. Two nontrivial cross-checks pass:
\[
g^{\alpha\beta}I_{\alpha\beta}
=K_{ab}^{SS}(D)
\]
using the **formal D-dimensional trace** \(g^\alpha{}_\alpha=D\), and
\[
\Gamma^{\alpha\beta}I_{\alpha\beta}
=\frac{D-4}{12}W(A,B)+\frac12W(q_A,A+B),
\]
which reproduces both mixed rank-two projections from P1.4b1.

The three radial factors have the expansions
\[
\begin{aligned}
D/4&=1-\epsilon/2+O(\epsilon^2),\\
D(D+2)/24&=1-5\epsilon/6+O(\epsilon^2),\\
D(D+2)(D+4)/192&=1-13\epsilon/12+O(\epsilon^2).
\end{aligned}
\]
The raw rank-two\(\otimes\)rank-two terms for all four topologies are now
written as explicit contractions of \(I_{\alpha\beta}^{(i)}\) with the
corresponding direct-pairing gamma tensors. The color-weighted sum is
\(-K_{TT}^{(1)}+K_{TT}^{(2)}+K_{TT}^{(3)}-K_{TT}^{(4)}\).

See
\`research/RC-001-QLD8-cross-source-rank2xrank2-UV-kernel.md\` and
\`validation/RC-001-QLD8-cross-source-tensor-integral-audit.txt\`.
The exact symbolic audit passes. The raw tensor is now available, but its
gamma/color contraction into the physical/evanescent operator basis,
complete graph phase, external-gluon gauge completion, and EOM/IBP
reduction remain open. No full \(Z\) matrix or Wilson coefficient is
claimed.


## 17. P1.5a–P1.5b: signed cross-source graphs and D-dimensional TT reduction

The common pre-loop Feynman-rule phase is fixed to +1 for the four cross-source graphs in the stated convention:
\((iC)(ig_s)^2(i)^2(-i)=+Cg_s^2\). The anti-quark representation sign is included once, through \(T_{\bar q}^A=-T^{A\,T}\) in the direct color matrices. The direct-color weights are \((-1,+1,+1,-1)\). Combining them with the exact Dirac-chain index signs gives final TT weights \((+1,+1,+1,+1)\); the four TT tensor integrals therefore add, rather than alternate.

With \(q=p_1+p_2\), \(d=p_1-p_2\), and \(R=p_3-p_4\), the exact D-dimensional sum is
\[
J_{\alpha\beta}(D)=
\frac{D}{24}(d_\alpha d_\beta+R_\alpha R_\beta)
-\frac{D+12}{24}q_\alpha q_\beta
+\frac{g_{\alpha\beta}}{48}
[D(d^2+R^2)+(D-20)q^2].
\]
It is symmetric and its \(D=4-2\epsilon\) expansion, including the full \(O(\epsilon)\) tensor, is recorded in research/RC-001-QLD8-cross-source-sign-and-TT-Dirac-reduction.md. The metric-contracted opposite-chirality tensor seed is evanescent in 4D but is retained as a D-dimensional operator. The exact symbolic and 4D matrix/index-sign checks are in calculations/RC-001-QLD8-cross-source-sign-TT-audit.py and validation/RC-001-QLD8-cross-source-sign-TT-audit.txt.

Acceptance boundary: P1.5a and the raw P1.5b TT contraction are closed locally. The merged SS+TS+ST+TT direct-pairing counterterm, external-gluon completion, physical/evanescent \(Z\) block, EOM/IBP reduction, and final anomalous dimension remain open. No CI pass is claimed.


Independent follow-up check: the coefficient multiplying \(g_{\alpha\beta}\) in the four-topology TT sum was re-derived by taking both free indices in a formal transverse direction, with all external momentum components zero. The resulting symbolic-\(D\) metric coefficient agrees exactly with the compact \(J_{\alpha\beta}(D)\) expression. This supplements the 16-component symbolic tensor identity and the explicit four-dimensional Dirac-matrix diagnostics.


## 18. P1.5c merged direct-pairing cross-source UV kernel

The four sectors are assembled in research/RC-001-QLD8-P1.5c-merged-cross-source-counterterm.md. Exact coefficients are Fss=(D^2+10D-8)/48, Fts=(D+8)/12, Fst=-(D+8)/6, and TT tensor J_ab(D). Their complete D=4-2epsilon expansions are retained. The tree-singlet cross-source subset has zero direct-singlet and nonzero direct-octet projection. Momentum conservation reduces d.R and the left mixed wedge as recorded in the P1.5c note. No Fierz, EOM or IBP quotient is taken.

The symbolic audit and output are calculations/RC-001-QLD8-P1.5c-merged-cross-source-audit.py and validation/RC-001-QLD8-P1.5c-merged-cross-source-audit.txt.

Acceptance boundary: this closes only the merged raw four-sector cross-source kernel. Nonexceptional off-shell/R* subtraction, D-dimensional operator closure, external-gluon Ward identities, EOM/IBP, full physical/evanescent/EOM Z block, same-bilinear sectors and finite UV-minus-EFT matching remain open.


## 19. P1.5c+: formal D-dimensional Dirac-rank closure

A formal arbitrary-D Clifford audit establishes that each of the four cross-source open-line chains decomposes exactly into \((0,0),(2,0),(0,2),(2,2)\) in the original direct pairing, using only \(\gamma^\mu\gamma^\nu=g^{\mu\nu}+\Gamma^{\mu\nu}\). The topology-relative TS/ST/TT signs reproduce P1.5a after applying the direct-color weights. No rank-three or rank-four string is generated by these four chains.

The two same-bilinear chains obey \(\gamma^\rho\Gamma_{(n)}\gamma_\rho=(-1)^n(D-2n)\Gamma_{(n)}\), so their direct-pairing structures are rank zero plus rank two on the affected bilinear. In particular, the tensor coefficient is \(D-4=-2\epsilon\) and must be retained for finite local terms.

This is only Dirac-rank closure for the six listed one-gluon Feynman-gauge four-fermion exchange numerators. It does not close the gauge-covariant dimension-eight operator basis or calculate the two same-bilinear loop poles, external-leg counterterms, background-gluon amplitudes, the full \(Z\) block, or matching. See research/RC-001-QLD8-P1.5c-plus-Ddim-Dirac-closure.md and its companion audit script/output.


## 19. P1.6a: same-bilinear exchange UV poles

The two within-source graphs have the same external derivative factor q_A^2. Their D-dimensional chain is D(r dot s)P_X+(D-4)Gamma^{mu nu}r_mu s_nu P_X. A nonexceptional off-shell Feynman-parameter calculation gives I_S^UV=-i D/(4(4 pi)^2 epsilon) and [I_T]_UV pole=0. The antisymmetric numerator reduces after the shift to x p1 wedge p2, while the remaining three-propagator loop integral is proportional to Gamma(1+epsilon), not Gamma(epsilon). Thus the D-4 factor does not multiply a UV pole in these graphs.

With the frozen Feynman-rule phase and direct-basis color matrix M_within=diag(-4/3,1/6), the two-graph block is -D^2 M_within/2 = diag(2D^2/3,-D^2/12), multiplying q_A^2(P_R tensor P_L) in the normalized i C g_s^2/(16 pi^2 epsilon) amplitude. On the tree-singlet source, the coefficient is C_F D^2/2 = 8 C_F - 8 C_F epsilon + 2 C_F epsilon^2, equal to 32/3 at the strict SU(3), D=4 pole residue.

The derivation and audit are in research/RC-001-QLD8-P1.6a-same-bilinear-UV-poles.md, calculations/RC-001-QLD8-P1.6a-same-bilinear-UV-audit.py, and validation/RC-001-QLD8-P1.6a-same-bilinear-UV-audit.txt. The earlier P1.5c+ wording is corrected: retain the D-4 numerator through integration, but this specific nonexceptional tensor integral is UV finite and gives no UV-pole-induced finite local term. External-leg counterterms, background-gluon completion, full operator subtraction, EOM/IBP, complete Z block and finite matching remain open.
