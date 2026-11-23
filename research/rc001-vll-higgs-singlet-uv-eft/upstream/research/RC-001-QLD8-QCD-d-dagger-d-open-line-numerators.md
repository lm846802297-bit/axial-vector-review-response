# RC-001 QLD8: \(d^\dagger d\) QCD open-line numerator map

**Date:** 2026-11-10  
**Stage:** P1.3b — six Feynman-gauge exchange numerator skeletons  
**Status:** the six topology chains and their momentum/source factors are fixed in the direct spinor pairing. Exact 4D matrix checks verify the rank-0/rank-2 Clifford decompositions. Overall graph phases, \(D\)-dimensional tensor integrals, and UV poles are not yet calculated.

## 1. Operator and conventions

Keep the source in its original direct spinor pairing:
\[
\mathcal O_{d^\dagger d}^{(8)}
=(D_\mu J_d^\dagger)(D^\mu J_d),\qquad
J_d=\bar d_RY_d^\dagger Q_L,
\]
so the four-fermion spinor tensor is
\[
(P_R)_{\alpha\beta}(P_L)_{\gamma\delta},
\]
with bilinears \((\bar Q,d)\) and \((\bar d,Q)\).

Use all external momenta incoming at the insertion:
\[
\bar Q(p_1),\quad d(p_2),\quad\bar d(p_3),\quad Q(p_4),
\qquad \sum_i p_i=0.
\]
Define source groups \(A=(\bar Q,d)\), \(B=(\bar d,Q)\), and
\[
q_A=p_1+p_2,\qquad q_B=p_3+p_4=-q_A.
\]

For an ordered exchange pair \((a,b)\), let \(\ell\) flow from the second named leg \(b\) to the first named leg \(a\). The insertion-side momenta are
\[
r_a=p_a+\ell,\qquad r_b=p_b-\ell.
\]
The two internal massless fermion propagators and the Feynman-gauge gluon propagator give the denominator
\[
\ell^2 r_a^2r_b^2.
\]
The derivative insertion contributes \([q_A^{(ab)}]^2\), with \(q_A^{(ab)}\) from the P1.1b routing table.

Use
\[
S_F(r)=\frac{i\slashed r}{r^2+i0},\qquad
V^\rho_{q q g}=ig_s\gamma^\rho T^A,\qquad
D_{\rho\sigma}^{AB}(\ell)=
\frac{-i\delta^{AB}g_{\rho\sigma}}{\ell^2+i0}.
\]
The table below records the open-line Dirac numerator tensor only. Overall \(i\)-factors and graph signs from the complete contraction/fermion-flow convention are not included in these numerator definitions and must be fixed before UV extraction.

## 2. Six exchange topologies

Write \(\mathcal N_{ab}\) as a tensor product in the original bilinear order \((\bar Q,d)\otimes(\bar d,Q)\). The color factor is the corresponding direct-basis matrix \(M_{ab}^{(d)}\) from the P1.3a record.

| Ordered pair \((a,b)\) | \(r_a\) | \(r_b\) | \(q_A^{(ab)}\) | Open-line numerator \(\mathcal N_{ab}\) |
|---|---|---|---|---|
| \((\bar Q,Q)\) | \(r_1=p_1+\ell\) | \(r_4=p_4-\ell\) | \(q_A+\ell\) | \((\gamma^\rho\slashed r_1P_R)\otimes(P_L\slashed r_4\gamma_\rho)\) |
| \((\bar Q,\bar d)\) | \(r_1=p_1+\ell\) | \(r_3=p_3-\ell\) | \(q_A+\ell\) | \((\gamma^\rho\slashed r_1P_R)\otimes(\gamma_\rho\slashed r_3P_L)\) |
| \((\bar Q,d)\) | \(r_1=p_1+\ell\) | \(r_2=p_2-\ell\) | \(q_A\) | \((\gamma^\rho\slashed r_1P_R\slashed r_2\gamma_\rho)\otimes P_L\) |
| \((Q,\bar d)\) | \(r_4=p_4+\ell\) | \(r_3=p_3-\ell\) | \(q_A\) | \(P_R\otimes(\gamma^\rho\slashed r_3P_L\slashed r_4\gamma_\rho)\) |
| \((Q,d)\) | \(r_4=p_4+\ell\) | \(r_2=p_2-\ell\) | \(q_A-\ell\) | \((P_R\slashed r_2\gamma^\rho)\otimes(P_L\slashed r_4\gamma_\rho)\) |
| \((\bar d,d)\) | \(r_3=p_3+\ell\) | \(r_2=p_2-\ell\) | \(q_A-\ell\) | \((P_R\slashed r_2\gamma^\rho)\otimes(\gamma_\rho\slashed r_3P_L)\) |

The schematic integrand for a topology is therefore
\[
\mathcal I_{ab}(\ell)
\propto
g_s^2\,
M_{ab}^{(d)}
\frac{[q_A^{(ab)}]^2\,\mathcal N_{ab}(\ell,p_i)}
{\ell^2r_a^2r_b^2}.
\]
This is a numerator/routing organization, not an evaluated signed amplitude.

## 3. Direct-pairing gamma-rank closure for one gluon exchange

Define the unit-weight rank-two string
\[
\Gamma^{\mu\nu}=\gamma^{[\mu}\gamma^{\nu]}
=\frac12[\gamma^\mu,\gamma^\nu],
\qquad
\gamma^\mu\gamma^\nu=g^{\mu\nu}+\Gamma^{\mu\nu}.
\]
Every cross-bilinear exchange in the table has two gamma matrices on each original bilinear. Expanding each two-gamma product shows that the direct-pairing structures have rank at most two on each bilinear:
\[
P_R\otimes P_L,\qquad
\Gamma^{\mu\nu}P_R\otimes P_L,\qquad
P_R\otimes\Gamma^{\mu\nu}P_L,\qquad
\Gamma^{\mu\nu}P_R\otimes\Gamma^{\rho\sigma}P_L,
\]
with the Lorentz indices contracted against the external/loop momenta and the gluon metric as fixed by each topology. Mixed rank-two \(\otimes\) scalar structures must not be dropped before the tensor integration.

For the two exchanges within a single source bilinear, the contracted chain reduces exactly in \(D\) dimensions:
\[
\boxed{
\gamma^\rho\slashed r\slashed s\gamma_\rho P_X
=
D(r\!\cdot\!s)P_X
+(D-4)\Gamma^{\mu\nu}r_\mu s_\nu P_X.
}
\]
Thus these same-bilinear vertex corrections also generate only rank zero and rank two on that bilinear. Since \(D-4=-2\epsilon\), the rank-two term is \(O(\epsilon)\) near four dimensions. It must be retained: when multiplied by a \(1/\epsilon\) UV pole it contributes to the finite local operator coefficient.

This is a useful finite rank bound for the **direct-pairing, one-gluon, Feynman-gauge \(d^\dagger d\) pilot**. It does not assert closure after a spinor Fierz crossing: the crossed representation has the odd-rank tower and the Gram degeneracy described in P1.2. The clean choice is to extract UV poles in the direct pairing and avoid a premature d-dimensional spinor Fierz transformation.

## 4. Contact terms and external-leg counterterms

The composite \(J_d=\bar d_RY_d^\dagger Q_L\) is a color singlet. Therefore \(D_\mu J_d=\partial_\mu J_d\) has no independent QCD gauge connection at the source insertion. If the derivative is expanded onto the two constituent fields, the two constituent QCD connection terms cancel in the complete source derivative.

Accordingly, in the original direct-source representation, the QCD one-loop four-point calculation consists of:
- the six pairwise exchange topologies in the table;
- the four external-leg quark self-energy contributions/wavefunction counterterms.

If the operator is rewritten in the crossed color-octet current basis, adjoint-covariant derivative contact terms must be restored. They are not extra independent interactions in the original color-singlet-source representation; they are required to make the Fierz-rearranged representation equivalent.

## 5. UV extraction still required

The four cross-source exchanges \((\bar Q,Q)\), \((\bar Q,\bar d)\), \((Q,d)\), and \((\bar d,d)\) carry \((q_A\pm\ell)^2\), which contains \(\ell^2\) and \(q_A\cdot\ell\) terms. Combined with the two fermion numerators, these four unexpanded integrands have superficial degree \(+2\). By contrast, the two within-source exchanges \((\bar Q,d)\) and \((Q,\bar d)\) carry the external factor \(q_A^2\) and are logarithmically divergent by power counting.

For the four cross-source graphs, the dimension-eight logarithmic counterterm must be isolated from the power-like pieces by an IR-safe off-shell UV expansion through external-momentum degree two (or a consistent \(R^*\) implementation). Do not discard the loop-momentum terms before UV/IR separation; the degree-two logarithmic local polynomial and any power-like lower-dimensional pieces must be distinguished.

Next steps:
1. Fix the complete relative Feynman-rule signs and fermion-flow conventions for all six graphs.
2. Generate the exact \(D\)-dimensional tensor numerators, including the rank-two \(\otimes\) scalar and scalar \(\otimes\) rank-two terms.
3. Add the four external-leg self-energy counterterms.
4. Perform nonexceptional off-shell tensor integrals (or a consistent \(R^*\) implementation) and extract the local \(1/\epsilon\) polynomial.
5. Verify the complete pole in the direct color basis and only then reduce by IBP/EOM.

The exact 4D matrix checks for the four cross-chain decompositions and the same-bilinear contracted identity are in
\`calculations/RC-001-QLD8-QCD-open-line-numerator-audit.py\`,
with output in
\`validation/RC-001-QLD8-QCD-open-line-numerator-audit.txt\`.
No loop integral, UV pole, \(Z\) matrix, or Wilson coefficient is claimed here.


## 6. Explicit rank-zero/rank-two decomposition of the four cross-source chains

For clarity, write
\[
\Gamma^{\mu\nu}=\gamma^{[\mu}\gamma^{\nu]}
=\frac12[\gamma^\mu,\gamma^\nu],
\qquad
\gamma^\mu\gamma^\nu=g^{\mu\nu}+\Gamma^{\mu\nu}.
\]
The four cross-source numerator chains, after factoring out the left- and right-bilinear momentum components \(x_\alpha y_\beta\), obey the following exact
Clifford decompositions. For the first two topologies \(x=r_a\), \(y=r_b\); for the last two topologies \(x=r_b\), \(y=r_a\). This orientation matters for the rank-two projections even though it does not affect the scalar projection \(r_a\cdot r_b\). \(P_R\) and \(P_L\) commute with each rank-two
string.

For \((\bar Q,Q)\):
\[
\begin{aligned}
(\gamma^\rho\gamma^\alpha P_R)
\otimes(P_L\gamma^\beta\gamma_\rho)
={}&g^{\alpha\beta}P_R\otimes P_L
+P_R\otimes\Gamma^{\beta\alpha}P_L\\
&+\Gamma^{\beta\alpha}P_R\otimes P_L
+\Gamma^{\rho\alpha}P_R
 \otimes\Gamma^\beta{}_\rho P_L.
\end{aligned}
\]

For \((\bar Q,\bar d)\):
\[
\begin{aligned}
(\gamma^\rho\gamma^\alpha P_R)
\otimes(\gamma_\rho\gamma^\beta P_L)
={}&g^{\alpha\beta}P_R\otimes P_L
+P_R\otimes\Gamma^{\alpha\beta}P_L\\
&+\Gamma^{\beta\alpha}P_R\otimes P_L
+\Gamma^{\rho\alpha}P_R
 \otimes\Gamma_\rho{}^\beta P_L.
\end{aligned}
\]

For \((Q,d)\):
\[
\begin{aligned}
(P_R\gamma^\alpha\gamma^\rho)
\otimes(P_L\gamma^\beta\gamma_\rho)
={}&g^{\alpha\beta}P_R\otimes P_L
+P_R\otimes\Gamma^{\beta\alpha}P_L\\
&+\Gamma^{\alpha\beta}P_R\otimes P_L
+\Gamma^{\alpha\rho}P_R
 \otimes\Gamma^\beta{}_\rho P_L.
\end{aligned}
\]

For \((\bar d,d)\):
\[
\begin{aligned}
(P_R\gamma^\alpha\gamma^\rho)
\otimes(\gamma_\rho\gamma^\beta P_L)
={}&g^{\alpha\beta}P_R\otimes P_L
+P_R\otimes\Gamma^{\alpha\beta}P_L\\
&+\Gamma^{\alpha\beta}P_R\otimes P_L
+\Gamma^{\alpha\rho}P_R
 \otimes\Gamma_\rho{}^\beta P_L.
\end{aligned}
\]

These formulas make explicit that the mixed rank-two\(\otimes\)scalar
terms are present and generally have different signs/index order in the
four topologies. They cannot be replaced by a single scalar\(\otimes\)scalar
plus tensor\(\otimes\)tensor expression before the loop tensor integrals.
The companion 4D exact-matrix audit checks all four identities for all
\(4\times4=16\) choices of \((\alpha,\beta)\), i.e. 64/64 assignments.
