# RC-001 QLD8: formal \(d\)-dimensional Fierz projections of the direct \(RL\) tensor

**Date:** 2026-11-10  
**Stage:** P1.2 — direct/crossed pairing map for the \(d^\dagger d\) tensor seed  
**Scheme:** NDR, anticommuting \(\gamma_5\) on open fermion lines, \(D=4-2\epsilon\)  
**Status:** the rank-\(n\) crossed-channel projection coefficients are derived analytically and checked symbolically; the first higher-rank Gram degeneracy is exposed. This is not a finite closed Fierz basis and is not a loop calculation.

## 1. What is being transformed

The direct-pairing tensor seed is
\[
\mathcal T_{RL}^{\rm dir}
=(\sigma^{\mu\nu}P_R)\otimes(\sigma_{\mu\nu}P_L),
\qquad
\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu].
\]
The direct pairing has spinor indices \((\alpha\beta)(\gamma\delta)\). The crossed pairing is
\[
(A\widetilde\otimes B)_{\alpha\beta\gamma\delta}
=A_{\alpha\delta}B_{\gamma\beta}.
\]

Define normalized antisymmetrized gamma strings
\[
\Gamma^{(n)}_{\mu_1\ldots\mu_n}
=\gamma_{[\mu_1}\cdots\gamma_{\mu_n]},
\]
and the crossed chiral structures
\[
X_n^{RL}
=(\Gamma^{(n)}P_R)\widetilde\otimes
(\Gamma_{(n)}P_L).
\]
Because \(\Gamma^{(n)}\) commutes with \(\gamma_5\) for even \(n\) and anticommutes for odd \(n\), the crossed \(RL\) projection is nonzero only for odd \(n\).

## 2. Projection formula

Project \(\mathcal T_{RL}^{\rm dir}\) onto \(X_n^{RL}\) with the dual crossed tensor
\[
(\Gamma_{(n)}P_L)_{\delta\alpha}
(\Gamma^{(n)}P_R)_{\beta\gamma}.
\]
For odd \(n\), the numerator reduces to
\[
\begin{aligned}
N_n
&=\operatorname{tr}\!\left[
\sigma^{\mu\nu}P_R\Gamma_{(n)}P_L
\sigma_{\mu\nu}P_L\Gamma^{(n)}P_R
\right]\\
&=\lambda_n(D)\,t_n(D),
\end{aligned}
\]
where
\[
\sigma^{\mu\nu}\Gamma^{(n)}\sigma_{\mu\nu}
=\lambda_n(D)\Gamma^{(n)},
\qquad
\lambda_n(D)=D(D-1)-4n(D-n),
\]
and
\[
t_n(D)
=\operatorname{tr}\!\left[
\Gamma^{(n)}P_R\Gamma_{(n)}P_L
\right]
=2(-1)^{n(n-1)/2}\prod_{j=0}^{n-1}(D-j).
\]
The crossed-basis Gram denominator is \(t_n(D)^2\). Thus the rank-\(n\) projection coefficient is
\[
\boxed{
f_n(D)=
\frac{D(D-1)-4n(D-n)}
{2(-1)^{n(n-1)/2}D(D-1)\cdots(D-n+1)}
\quad(n\ {\rm odd}).
}
\]

This is a projection coefficient for a specified gamma-rank channel. It is not by itself a claim that the direct tensor has a finite expansion involving only \(n=1\) and \(n=3\). A complete formal crossed representation requires the higher odd-rank gamma-string tower and a non-degenerate treatment of its Gram matrix.

## 3. First crossed projections near four dimensions

For the first three odd ranks:
\[
f_1(D)=\frac{(D-1)(D-4)}{2D},
\]
\[
f_3(D)=
-\frac{(D-4)(D-9)}
{2D(D-1)(D-2)},
\]
\[
f_5(D)=
\frac{D^2-21D+100}
{2D(D-1)(D-2)(D-3)(D-4)}.
\]

With \(D=4-2\epsilon\),
\[
\boxed{
f_1=-\frac34\epsilon+O(\epsilon^2),\qquad
f_3=-\frac5{24}\epsilon+O(\epsilon^2),
}
\]
whereas
\[
\boxed{
f_5=-\frac{1}{3\epsilon}-\frac{239}{144}
+O(\epsilon).
}
\]

The \(f_5\) pole is **not a loop UV pole**. It arises because the rank-five crossed-channel Gram norm contains
\[
t_5(D)=2D(D-1)(D-2)(D-3)(D-4),
\]
which vanishes at \(D=4\). Inverting this degenerate Gram direction produces a singular projection coefficient. The rank-five gamma string is itself evanescent at four dimensions.

Consequently, the direct tensor cannot be eliminated by a regular finite change of basis using only the rank-one and rank-three crossed structures. The \(n=1,3\) projections are \(O(\epsilon)\), while the first omitted higher-rank channel already has a singular Gram inverse. Higher odd ranks must be treated consistently if one insists on a complete crossed representation.

## 4. Operator-level sign and color are separate

The c-number matrix identity uses \(\widetilde\otimes\). For anticommuting four-fermion fields, crossing the middle two fields adds an overall minus sign:
\[
\left[
(\bar\psi\sigma^{\mu\nu}P_R\chi)
(\bar\eta\sigma_{\mu\nu}P_L\xi)
\right]_{n}
=
-f_n(D)
(\bar\psi\Gamma^{(n)}P_R\xi)
(\bar\eta\Gamma_{(n)}P_L\chi).
\]
This sign is separate from the color rearrangement.

For the \(d^\dagger d\) source, the crossed color tensor is
\[
C_X^{ij;kl}=\delta_{il}\delta_{kj}
=\frac13C_1^{ij;kl}+2C_8^{ij;kl}.
\]
Thus the crossed current basis must retain both color singlet and octet channels. The spinor projection coefficient \(f_n(D)\) does not replace or modify this independent color decomposition.

## 5. Important correction to the earlier evanescent bookkeeping

The scalar–vector difference \(E_{RL;V}^{\mu,rs}\) is a distinct Lorentz structure: it starts from scalar \(\times\) vector with one open Lorentz index. It is **not** the direct Fierz image of the Lorentz-scalar tensor \(\sigma^{\mu\nu}P_R\otimes\sigma_{\mu\nu}P_L\).

The relevant crossed channels for the direct tensor are contracted odd-rank products:
- rank one: vector \(\times\) vector;
- rank three: rank-three \(\times\) rank-three;
- rank five and higher odd ranks in the formal \(D\)-dimensional tower.

Therefore the earlier shorthand that grouped \(E_{T;RL}^{\rm dir}\) with \(E_{RL;V}\) was too broad. \(E_{RL;V}\) remains in the separate scalar–vector EOM sector. The direct tensor must be tracked against the contracted odd-rank crossed tower, including the rank-three seed and higher-rank evanescents.

## 6. Consequence for the canonical basis

For the one-loop \(d^\dagger d\) pilot, use the following conservative bookkeeping:

1. Keep \(E_{T;RL}^{\rm dir}\) as an explicit direct-pairing evanescent seed.
2. Keep the rank-three crossed gamma-string structure as a separate numerator/counterterm label.
3. Do not identify the direct tensor with \(E_{RL;V}\).
4. Do not eliminate \(E_{T;RL}^{\rm dir}\) using only \(f_1\) and \(f_3\).
5. When explicit one-loop numerators are available, determine the maximum gamma rank actually generated and construct the corresponding finite counterterm basis before projecting to four dimensions.
6. Check the rank and Gram matrix of that finite set at generic \(D\), then define the evanescent subtraction convention and any \(O(\epsilon)\) physical admixtures.

This settles the first projection coefficients and exposes the higher-rank obstruction; it does **not** yet determine the final independent evanescent basis for the complete one-loop problem.

## 7. Reproducible audit and boundary

The companion script
\`calculations/RC-001-QLD8-ddim-Fierz-projection-audit.py\`
checks:
- the \(\sigma^{\mu\nu}\Gamma^{(n)}\sigma_{\mu\nu}\) eigenvalue in an explicit \(4\times4\) Minkowski representation for \(n=0,\ldots,4\);
- the analytic \(D\)-dependent projection coefficients \(f_1,f_3,f_5\);
- the \(D=4-2\epsilon\) limits shown above;
- the vanishing rank-five Gram norm at \(D=4\).

The recorded output is
\`validation/RC-001-QLD8-ddim-Fierz-projection-audit.txt\`.

No loop momentum integral, UV pole, physical/evanescent \(Z\) matrix, anomalous dimension, finite matching coefficient, or contribution to the PR #69 \(hh,hs,ss\) two-point functions is calculated here.


## 8. Practical resolution: keep the QCD UV calculation in the direct pairing

The rank-five Gram obstruction is a warning against forcing the direct tensor
through a finite crossed odd-rank basis. It does **not** obstruct the QCD
renormalization itself.

The six one-gluon Feynman-gauge \(d^\dagger d\) numerator chains have now
been written in the original direct spinor pairing
\[
(\bar Q,d)\otimes(\bar d,Q).
\]
Their exact Clifford decomposition has gamma rank at most two on each
original bilinear. The same-bilinear chain reduces as
\[
\gamma^\rho\slashed r\slashed s\gamma_\rho P_X
=D(r\cdot s)P_X+(D-4)\Gamma^{\mu\nu}r_\mu s_\nu P_X,
\]
and the cross-bilinear chains contain only rank-zero/rank-two factors on
each side. The direct rank-two tensor and mixed rank-two\(\otimes\)scalar
structures must be retained; no rank-three/five direct string is generated
by these one-gluon chains.

Therefore the preferred P1.3 calculation basis is:
- direct spinor pairing, with no d-dimensional spinor Fierz crossing before
  UV subtraction;
- direct singlet/octet color basis \(C_{1,d},C_{8,d}\);
- direct scalar, rank-two, and derivative-correlated tensor structures;
- the direct \(E_{T;RL}^{\rm dir}\) seed with its \(O(\epsilon)\) coefficients
  retained.

The crossed \(f_n(D)\) projection remains a diagnostic for translating
results into a crossed-current basis. It is not needed to compute the
direct-pairing UV poles. The exact numerator record is
\`research/RC-001-QLD8-QCD-d-dagger-d-open-line-numerators.md\`, and the
direct color basis is in
\`research/RC-001-QLD8-QCD-direct-pairing-color-basis.md\`.

This resolves the immediate basis-choice problem for the first QCD pilot,
but not the full counterterm closure: derivative-index structures, EOM
representatives, external-leg terms, and the UV/EFT subtraction still need
to be calculated.
