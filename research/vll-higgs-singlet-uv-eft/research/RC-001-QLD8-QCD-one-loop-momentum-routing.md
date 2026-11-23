# RC-001 QLD8: \(d^\dagger d\) QCD one-loop momentum routing

**Date:** 2026-11-10  
**Stage:** P1.1b — insertion momentum and six exchange-topology routing  
**Status:** exact tree-vertex and routing identities pass. No loop integral or UV pole is evaluated.

## 1. External momenta and source grouping

Use all four external fermion momenta incoming at the local operator insertion:
\[
\bar Q(p_1),\quad d(p_2),\quad \bar d(p_3),\quad Q(p_4),
\qquad p_1+p_2+p_3+p_4=0.
\]
The two original source bilinears are
\[
J_d^\dagger:\ (\bar Q,d),\qquad J_d:\ (\bar d,Q).
\]
Define the momentum entering the first source current by
\[
q_A=p_1+p_2,\qquad q_B=p_3+p_4=-q_A.
\]

With Fourier convention \(\psi(x)=\int_p e^{-ipx}\psi(p)\), the two derivatives at the source-square insertion give
\[
(-iq_{A\mu})(-iq_B^\mu)=-q_A\cdot q_B=q_A^2.
\]
Therefore the complete tree-level four-fermion vertex from
\((D_\mu J_d^\dagger)(D^\mu J_d)\) carries the momentum polynomial \(q_A^2\), multiplying the original chiral scalar-pair spinor and color tensor.

## 2. The four derivative placements are the expansion of one vertex

Expanding each source derivative by the product rule gives
\[
\begin{aligned}
-q_A\cdot q_B=-(&p_1\cdot p_3+p_1\cdot p_4\\
&+p_2\cdot p_3+p_2\cdot p_4).
\end{aligned}
\]
Using \(p_3+p_4=-(p_1+p_2)\), this is exactly
\[
\boxed{
-(p_1+p_2)\cdot(p_3+p_4)=(p_1+p_2)^2.
}
\]
The four terms correspond to the four placements:
\[
(\bar Q,\bar d),\quad(\bar Q,Q),\quad(d,\bar d),\quad(d,Q).
\]
They are not four independent Wilson coefficients or four unrelated insertion vertices. Their sum reconstructs the total source-current momentum factor.

## 3. Loop-momentum routing for the six QCD exchanges

Let a gluon momentum \(\ell\) flow from the **second named external leg to the first**. With all external momenta incoming at the insertion, the two fermion momenta entering the operator insertion are shifted as
\[
p_a\longrightarrow p_a+\ell,\qquad
p_b\longrightarrow p_b-\ell.
\]
The momentum entering the first source current is therefore
\[
q_A^{(ab)}
=q_A+\ell\left[
\mathbf1_{a\in\{\bar Q,d\}}
-\mathbf1_{b\in\{\bar Q,d\}}
\right],
\qquad q_B^{(ab)}=-q_A^{(ab)}.
\]
The derivative factor at the insertion is
\[
V_{\rm src}^{(ab)}(\ell)
=-q_A^{(ab)}\cdot q_B^{(ab)}
=[q_A^{(ab)}]^2.
\]

| Exchanged legs \((a,b)\) | Relation to original source currents | \(q_A^{(ab)}\) | Insertion factor |
|---|---|---|---|
| \((\bar Q,Q)\) | across \(J_d^\dagger,J_d\) | \(q_A+\ell\) | \((q_A+\ell)^2\) |
| \((\bar Q,\bar d)\) | across \(J_d^\dagger,J_d\) | \(q_A+\ell\) | \((q_A+\ell)^2\) |
| \((\bar Q,d)\) | within \(J_d^\dagger\) | \(q_A\) | \(q_A^2\) |
| \((Q,\bar d)\) | within \(J_d\) | \(q_A\) | \(q_A^2\) |
| \((Q,d)\) | across \(J_d^\dagger,J_d\) | \(q_A-\ell\) | \((q_A-\ell)^2\) |
| \((\bar d,d)\) | across \(J_d^\dagger,J_d\) | \(q_A-\ell\) | \((q_A-\ell)^2\) |

This identifies an important distinction:
- the two within-current exchanges carry no loop momentum in the derivative insertion factor;
- the four cross-current exchanges carry \((q_A\pm\ell)^2=q_A^2\pm2q_A\cdot\ell+\ell^2\).

The \(\ell^2\) and \(q_A\cdot\ell\) terms must be retained in the UV numerator. They cannot be dropped by replacing the derivative factor with \(q_A^2\) before assigning the loop topology.

## 4. Relation to the singlet/octet color block

The six rows above use the same external-leg order as the exact color matrices in
[RC-001-QLD8-QCD-color-factor-block.md](RC-001-QLD8-QCD-color-factor-block.md).
For each topology, the full integrand has the schematic form
\[
\mathcal I_{ab}(\ell)
\propto
g_s^2\,
M_{ab}\,
\frac{[q_A^{(ab)}(\ell)]^2\,
\mathcal N_{ab}(\ell,p_i)}
{\ell^2\,r_a^2\,r_b^2},
\]
where \(M_{ab}\) is the corresponding singlet/octet color matrix, \(r_a,r_b\) are the routed internal fermion momenta, and \(\mathcal N_{ab}\) is the open-line Dirac numerator. The exact propagator routing and numerator signs still have to be fixed from a single consistent fermion-flow convention for each graph. This schematic expression is not an evaluated integrand or UV pole.

Because \(J_d\) is a color singlet, the composite derivative \(D_\mu J_d\) has no direct QCD gauge connection. If the product rule is expanded into constituent derivatives, the QCD connection terms cancel only after the complete two-term derivative of each source is restored. In a Fierz-rearranged octet-current basis, the adjoint-covariant derivative contact terms must be retained so that the result agrees with the original color-singlet-source representation.

## 5. Validation and boundary

The companion exact-symbolic audit checks:
1. \(q_A+q_B=0\);
2. the sum of the four derivative placements equals \(q_A^2\);
3. all six exchange routings give the stated \(q_A\) shift;
4. \(q_A^{(ab)}+q_B^{(ab)}=0\) and the insertion factor is \([q_A^{(ab)}]^2\) for every topology.

This closes the momentum-routing algebra for the \(d^\dagger d\) QCD pilot. It does not evaluate the Dirac numerators, tensor loop integrals, UV poles, wavefunction counterterms, evanescent mixing, or the \(Z\) matrix.


### Momentum-flow convention clarification

The sign convention is fixed as follows: for a listed ordered pair \((a,b)\),
\(\ell\) flows from leg \(b\) toward leg \(a\). With all external momenta
\(p_i\) incoming at the operator insertion, momentum conservation at the
two external QCD vertices then gives the insertion-side fermion momenta
\(r_a=p_a+\ell\) and \(r_b=p_b-\ell\). This is the convention used by the
routing table and the symbolic audit. If instead one chooses \(\ell\) to
flow from \(a\) to \(b\), every \(\ell\) sign in the table is reversed; the
loop integral is unchanged after \(\ell\mapsto-\ell\), provided the whole
integrand is transformed consistently.
