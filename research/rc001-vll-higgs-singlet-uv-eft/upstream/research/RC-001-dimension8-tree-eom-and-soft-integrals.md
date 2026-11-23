# RC-001 — Tree-level EOM reduction and dimension-eight EFT soft-current loops

**Status:** analytic derivation and local exact-algebra checks completed for the restricted \(Q_{LD}^2\), \(Q_{RD}^2\), and \(Q_{LD}Q_{RD}\) sectors. This closes the corresponding EFT soft kernels only. It does not provide their UV hard partners or a dimension-eight Wilson-vector closure.

## 1. Frozen conventions and exact heavy-field elimination

For one flavor \(\ell\), take
\[
\mathcal L_{\rm UV}\supset
\bar E_\ell(i\slashed D-M_{E\ell})E_\ell
-y_\ell\bar L_\ell H E_{\ell R}
-\lambda_\ell S_\ell\bar E_{\ell L}\ell_R+\mathrm{h.c.}
\]
and define
\[
\mathcal O_{5,\ell}=(\bar L_\ell H)S_\ell\ell_R,\qquad
C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_{E\ell}},
\qquad
\mathcal L_{\rm EFT}^{(5)}\supset-C_{5,\ell}\mathcal O_{5,\ell}+\mathrm{h.c.}
\]
This explicit \(-C_5\) convention is used throughout this note. Let \(\mathscr D=i\slashed D\), with the derivative acting on the entire composite to its right.

The heavy-field sources can be written
\[
\bar J_\ell=y_\ell(\bar L_\ell H)P_R
+\lambda_\ell^*S_\ell^\dagger\bar\ell_RP_L,
\qquad
J_\ell=y_\ell^*H^\dagger L_\ell+\lambda_\ell S_\ell\ell_R.
\]
The exact classical elimination is the Schur complement
\[
\Delta\mathcal L_{\rm tree}=-\bar J_\ell
(\mathscr D-M_{E\ell})^{-1}J_\ell,
\qquad
(\mathscr D-M)^{-1}=\frac{\mathscr D+M}{\mathscr D^2-M^2}.
\]
Using the chiral projectors gives, modulo the hermitian-conjugate cross term and total derivatives,
\[
\begin{aligned}
\Delta\mathcal L_{\rm tree}={}&
-|y_\ell|^2(\bar L_\ell H)
\frac{\mathscr D}{\mathscr D^2-M_{E\ell}^2}
(H^\dagger L_\ell)\\
&-|\lambda_\ell|^2S_\ell^\dagger\bar\ell_R
\frac{\mathscr D}{\mathscr D^2-M_{E\ell}^2}
(S_\ell\ell_R)\\
&-y_\ell\lambda_\ell(\bar L_\ell H)
\frac{M_{E\ell}}{\mathscr D^2-M_{E\ell}^2}
(S_\ell\ell_R)+\mathrm{h.c.}
\end{aligned}
\]
The two same-chirality terms are hermitian up to integration by parts; the cross-chirality term is accompanied by its distinct hermitian conjugate.

Expanding the exact Schur complement gives
\[
\frac{\mathscr D}{\mathscr D^2-M_E^2}
=-\frac{\mathscr D}{M_E^2}
-\frac{\mathscr D^3}{M_E^4}+O(M_E^{-6}),
\qquad
\frac{M_E}{\mathscr D^2-M_E^2}
=-\frac1{M_E}-\frac{\mathscr D^2}{M_E^3}+O(M_E^{-5}).
\]
Consequently,
\[
\begin{aligned}
\Delta\mathcal L_{\rm tree}={}&
\frac{|y_\ell|^2}{M_{E\ell}^2}Q_{LD,\ell}
+\frac{|\lambda_\ell|^2}{M_{E\ell}^2}Q_{RD,\ell}\\
&+\frac{|y_\ell|^2}{M_{E\ell}^4}Q_{LD,\ell}^{(8)}
+\frac{|\lambda_\ell|^2}{M_{E\ell}^4}Q_{RD,\ell}^{(8)}\\
&+\frac{y_\ell\lambda_\ell}{M_{E\ell}}\mathcal O_{5,\ell}
+\frac{y_\ell\lambda_\ell}{M_{E\ell}^3}\mathcal O_{7,\ell}
+\mathrm{h.c.}+O(M_E^{-5})_{\rm cross}+O(M_E^{-6})_{\rm same},
\end{aligned}
\]
where
\[
\begin{aligned}
Q_{LD,\ell}&=(\bar L_\ell H)\mathscr D(H^\dagger L_\ell),&
Q_{RD,\ell}&=S_\ell^\dagger\bar\ell_R\mathscr D(S_\ell\ell_R),\\
Q_{LD,\ell}^{(8)}&=(\bar L_\ell H)\mathscr D^3(H^\dagger L_\ell),&
Q_{RD,\ell}^{(8)}&=S_\ell^\dagger\bar\ell_R\mathscr D^3(S_\ell\ell_R),\\
\mathcal O_{7,\ell}&=(\bar L_\ell H)\mathscr D^2(S_\ell\ell_R).
\end{aligned}
\]
Thus the coefficient of \(\mathcal O_7\) in the Lagrangian is \(+y_\ell\lambda_\ell/M_{E\ell}^3\). In the convention \(\mathcal L\supset-C_{7,\ell}\mathcal O_{7,\ell}\), this means
\[
C_{7,\ell}=\frac{C_{5,\ell}}{M_{E\ell}^2},
\qquad
-\;C_{7,\ell}\mathcal O_{7,\ell}
=+\frac{y_\ell\lambda_\ell}{M_{E\ell}^3}\mathcal O_{7,\ell}.
\]
This fixes the sign unambiguously. The earlier protocol's displayed equality \(-y_\ell\lambda_\ell\mathcal O_7/M_E^3=C_5\mathcal O_7/M_E^2\) had the wrong sign for the Lagrangian term and is superseded by this Schur-complement result.

The \(Q_{LD}^{(8)}\) and \(Q_{RD}^{(8)}\) terms are additional tree-level dimension-eight Green-basis representatives. They are not to be silently omitted from a complete \(O(M_E^{-4})\) EFT action.

## 2. Light-field EOM and dimension-six operator reduction

Write \(X=H^\dagger H\), \(Y=S_\ell^\dagger S_\ell\), and
\[
\mathcal L_{\rm EFT}\supset
\bar L_\ell i\slashed D L_\ell+
\bar\ell_R i\slashed D\ell_R
-C_{5,\ell}\mathcal O_{5,\ell}
-C_{5,\ell}^*\mathcal O_{5,\ell}^\dagger.
\]
The corresponding fermion EOM are
\[
i\slashed D L_\ell=C_{5,\ell}H S_\ell\ell_R,\qquad
i\slashed D\ell_R=C_{5,\ell}^*S_\ell^\dagger H^\dagger L_\ell,
\]
\[
i(D_\mu\bar L_\ell)\gamma^\mu
=-C_{5,\ell}^*\bar\ell_R S_\ell^\dagger H^\dagger,\qquad
i(D_\mu\bar\ell_R)\gamma^\mu
=-C_{5,\ell}\bar L_\ell H S_\ell.
\]
Define
\[
J_{L,\ell;ij}^\mu=\bar L_{\ell i}\gamma^\mu L_{\ell j},
\quad
J_{R,\ell}^\mu=\bar\ell_R\gamma^\mu\ell_R,
\]
\[
\mathcal J_{H,ij}^\mu
=i\left[H_i(D^\mu H^\dagger)_j-(D^\mu H)_iH^\dagger_j\right],
\quad
j_{S_\ell}^\mu
=i\left[S_\ell^\dagger D^\mu S_\ell-(D^\mu S_\ell)^\dagger S_\ell\right].
\]
Using the EOM and covariant integration by parts, including the non-conservation of the chiral currents induced by \(C_5\), gives
\[
Q_{LD,\ell}\doteq
\frac12\mathcal J_{H,ij}^\mu J_{L,\ell;ij,\mu}
+\frac12X\left(C_{5,\ell}\mathcal O_{5,\ell}
+C_{5,\ell}^*\mathcal O_{5,\ell}^\dagger\right),
\]
\[
Q_{RD,\ell}\doteq
\frac12j_{S_\ell}^\mu J_{R,\ell,\mu}
+\frac12Y\left(C_{5,\ell}\mathcal O_{5,\ell}
+C_{5,\ell}^*\mathcal O_{5,\ell}^\dagger\right).
\]
The source terms are essential: after multiplication by \(C_{LD}=|y|^2/M_E^2\) or \(C_{RD}=|\lambda|^2/M_E^2\), they start at \(O(M_E^{-3})\). They are not present if one uses only the free massless EOM.

## 3. Dimension-seven operator: EOM reduction through the dimension-eight order

Use
\[
(i\slashed D)^2=-D^2+\frac{i}{2}\sigma^{\mu\nu}[D_\mu,D_\nu],
\qquad \sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu].
\]
The commutator acts on the full product \(S_\ell\ell_R\):
\[
[D_\mu,D_\nu](S_\ell\ell_R)
=([D_\mu,D_\nu]S_\ell)\ell_R
+S_\ell([D_\mu,D_\nu]\ell_R).
\]
No field-strength term is dropped. An equivalent integration-by-parts form is
\[
\mathcal O_{7,\ell}\doteq
[D_\mu(\bar L_\ell H)]\gamma^\mu\gamma^\nu
D_\nu(S_\ell\ell_R).
\]
Applying the interacting light-fermion EOM and retaining terms through first order in \(C_{5,\ell}^*\) gives
\[
\begin{aligned}
\mathcal O_{7,\ell}\doteq{}&
\mathcal O_{7,\ell}^{\rm der}
+iC_{5,\ell}^*X S_\ell^\dagger(D_\mu S_\ell)J_{R,\ell}^\mu\\
&-iC_{5,\ell}^*Y\,
\bar L_\ell(D_\mu H)\gamma^\mu H^\dagger L_\ell
+O((C_{5,\ell}^*)^2),
\end{aligned}
\]
where
\[
\begin{aligned}
\mathcal O_{7,\ell}^{\rm der}
&=\bar L_\ell(D_\mu H)\gamma^\mu\gamma^\nu
(D_\nu S_\ell)\ell_R\\
&=\bar L_\ell\left[
(D_\mu H)(D^\mu S_\ell)
-i\sigma^{\mu\nu}(D_\mu H)(D_\nu S_\ell)
\right]\ell_R .
\end{aligned}
\]
The \(O(C_5^*)\) companions cannot be discarded: multiplying by the tree coefficient \(-C_{5,\ell}/M_{E\ell}^2\) makes them \(O(M_E^{-4})\). Adding the hermitian conjugate, their contribution in this EOM representative is
\[
\Delta\mathcal L_{8,\rm EOM}^{(7)}
\doteq-\frac{|C_{5,\ell}|^2}{M_{E\ell}^2}
\left[
X j_{S_\ell,\mu}J_{R,\ell}^{\mu}
+Y\mathcal J_{H,ij,\mu}J_{L,\ell;ij}^{\mu}
\right].
\]
This is an EOM-induced coefficient map, not an additional UV graph. It must be combined with the other Green-basis contributions only once. Terms \(O(C_5^{*2})\) in the operator identity enter at \(O(M_E^{-5})\) after multiplication by its tree coefficient and are beyond the present \(M_E^{-4}\) truncation.

**Boundary of this reduction:** the displayed result is the complete fermion-EOM reduction at the retained order in the declared Green basis. It does not claim that the scalar-derivative dimension-seven operator has been reduced to a unique minimal dimension-seven basis under every scalar EOM, gauge-field EOM, and integration-by-parts identity. Those transformations belong in the common-basis ledger after amplitude matching.

## 4. Soft loops from \(Q_{LD}^2\), \(Q_{RD}^2\), and \(Q_{LD}Q_{RD}\)

Set
\[
C_{LD,\ell}=\frac{|y_\ell|^2}{M_{E\ell}^2},
\qquad
C_{RD,\ell}=\frac{|\lambda_\ell|^2}{M_{E\ell}^2}.
\]
At order \(M_E^{-4}\), the two-insertion soft loops use only the current-current pieces in Sec. 2. The \(C_5\)-dependent source pieces in those EOM identities carry one additional inverse heavy mass and therefore first affect these products at \(O(M_E^{-5})\) or higher.

For one massless Weyl fermion, define the parity-even Euclidean current correlator by
\[
\Pi_{\mu\nu}^{W,E}(q)=
\frac{1}{4\pi^2}(q^2\delta_{\mu\nu}-q_\mu q_\nu)
\int_0^1 dx\,x(1-x)
\left[
\Delta_{\rm UV}-\ln\frac{x(1-x)q^2}{\mu^2}
\right],
\]
where \(\Delta_{\rm UV}=1/\epsilon-\gamma_E+\ln4\pi\), \(d=4-2\epsilon\), and \(q^2>0\) is kept nonzero as the off-shell IR scale. The exact parameter integrals are
\[
\int_0^1dx\,x(1-x)=\frac16,\qquad
\int_0^1dx\,x(1-x)\ln[x(1-x)]=-\frac5{18},
\]
hence
\[
\Pi_{\mu\nu}^{W,E}(q)=
\frac{q^2\delta_{\mu\nu}-q_\mu q_\nu}{24\pi^2}
\left[
\Delta_{\rm UV}-\ln\frac{q^2}{\mu^2}+\frac53
\right].
\]
The finite \(5/3\) is for this massless off-shell two-point function and the stated \(\overline{\rm MS}\) convention.

### 4.1 \(Q_{LD}Q_{LD}\): pure-Higgs channel

The EOM-reduced insertion is \(\frac12\mathcal J_{H,ij}^\mu J_{L,ij,\mu}\). The closed loop is one Weyl doublet; its weak-index contraction is the matrix trace, so no extra factor of two is to be appended by hand. The second-order expansion of the effective action supplies \(1/2!\), and the two EOM-reduction factors supply \(1/4\):
\[
\begin{aligned}
\Gamma_{LD^2,E}^{\rm soft}
&=\frac18\sum_{\ell=\mu,\tau}C_{LD,\ell}^2
\int_q
\operatorname{tr}_{2}\!
\left[\mathcal J_{H,\mu}(q)\mathcal J_{H,\nu}(-q)\right]
\Pi_W^{\mu\nu,E}(q)\\
&=\frac{1}{192\pi^2}\sum_\ell C_{LD,\ell}^2
\int_q\operatorname{tr}_{2}\!
\left[\mathcal J_{H,\mu}(q)\mathcal J_{H,\nu}(-q)\right]
(q^2\delta_{\mu\nu}-q_\mu q_\nu)
\left[\Delta_{\rm UV}-\ln\frac{q^2}{\mu^2}+\frac53\right],
\end{aligned}
\]
with \(\int_q=\mu^{2\epsilon}\int d^{4-2\epsilon}q/(2\pi)^{4-2\epsilon}\). This is the full one-loop soft kernel for the stated two-insertion current sector, including the weak-doublet trace.

### 4.2 \(Q_{RD}Q_{RD}\): pure-singlet channel

The insertion is \(\frac12j_{S_\ell}^\mu J_{R,\ell,\mu}\), with one right-handed Weyl fermion per flavor:
\[
\begin{aligned}
\Gamma_{RD^2,E}^{\rm soft}
&=\frac18\sum_{\ell=\mu,\tau}C_{RD,\ell}^2
\int_q j_{S_\ell,\mu}(q)j_{S_\ell,\nu}(-q)
\Pi_W^{\mu\nu,E}(q)\\
&=\frac{1}{192\pi^2}\sum_\ell C_{RD,\ell}^2
\int_q j_{S_\ell,\mu}(q)j_{S_\ell,\nu}(-q)
(q^2\delta_{\mu\nu}-q_\mu q_\nu)
\left[\Delta_{\rm UV}-\ln\frac{q^2}{\mu^2}+\frac53\right].
\end{aligned}
\]
Since \(S_\tau=S^*\), \(j_{S_\tau}=-j_{S_\mu}\); the squared-current kernel has the same sign for the two flavors. There is no cancellation between \(\mu\) and \(\tau\).

### 4.3 \(Q_{LD}Q_{RD}\): mixed channel

The candidate mixed current correlator is
\[
\Pi_{LR,\mu\nu}(q)\propto
\int_k
\frac{\operatorname{tr}
[\gamma_\mu P_L\slashed k\gamma_\nu P_R(\slashed k+\slashed q)]}
{k^2(k+q)^2}.
\]
It vanishes identically before integration. Indeed,
\[
P_R\gamma_\nu P_R=0,\qquad
P_L\slashed k=\slashed kP_R,
\]
so the numerator is zero for every \(k,q,\mu,\nu\). In the actual model \(L_\ell\) and \(\ell_R\) are independent chiral fields, and their free cross propagator is also zero. Therefore
\[
\boxed{\Gamma_{LD\,RD,E}^{\rm soft}\big|_{M_E^{-4}}=0.}
\]
A nonzero chirality-changing contribution requires additional \(C_5\) mass/source insertions; it is higher order in \(1/M_E\) and is not this two-\(Q_6\)-insertion topology.

### 4.4 Single \(Q_{LD}^{(8)}\) or \(Q_{RD}^{(8)}\) insertion: scalar two-point soft tadpole

The exact Schur complement also generates
\[
Q_{LD,\ell}^{(8)}=(\bar L_\ell H)(i\slashed D)^3(H^\dagger L_\ell),
\qquad
Q_{RD,\ell}^{(8)}=S_\ell^\dagger\bar\ell_R(i\slashed D)^3(S_\ell\ell_R),
\]
with coefficients \(|y_\ell|^2/M_{E\ell}^4\) and \(|\lambda_\ell|^2/M_{E\ell}^4\), respectively. These are genuine tree-level dimension-eight Green-basis operators. They must remain in fermionic and current/source amplitudes even when a particular scalar projection vanishes.

For the restricted unbroken-phase scalar two-point projection, close the fermion bilinear at a single \(Q_8\) insertion and keep two external scalar fields. Set gauge backgrounds to zero and take the light fermion massless. If \(p\) is the momentum carried by the external scalar composite and \(k\) the loop momentum, the parity-even numerator is proportional to
\[
\frac{\operatorname{tr}[(\slashed k+\slashed p)^3\slashed k]}{k^2}
=4\,\frac{(k+p)^2(k+p)\cdot k}{k^2}.
\]
Writing \(K=k^2\), \(a=k\cdot p\), and \(p^2=p\cdot p\), the scalar integrand reduces to
\[
K+3a+\frac{2a^2}{K}+p^2+\frac{p^2a}{K}.
\]
Symmetric integration removes the odd terms and gives
\[
\int_k\left[K+p^2+\frac{2}{K}(k\cdot p)^2\right]
=\left(1+\frac2d\right)p^2\int_k1+\int_k k^2=0
\]
in dimensional regularization: both remaining integrals are scaleless. The same conclusion holds for the right-handed singlet channel. Thus
\[
\Gamma_{\mathrm{soft}}^{(1)}[Q_{LD}^{(8)}]\big|_{\phi^\dagger\phi,\;g=0,\;m_\ell=0}=0,
\qquad
\Gamma_{\mathrm{soft}}^{(1)}[Q_{RD}^{(8)}]\big|_{S^\dagger S,\;g=0,\;m_\ell=0}=0.
\]

This is a zero for the specified one-insertion scalar tadpole, not a statement that \(Q_{LD}^{(8)}\) or \(Q_{RD}^{(8)}\) is a redundant or vanishing operator. In particular:
- their tree-level fermion–scalar matrix elements are nonzero and are part of the dimension-eight Green basis;
- the covariant derivatives generate gauge-field and field-strength contact terms; gauge-corrected fermionic/current amplitudes at \(O(g^2/M_E^4)\) have not been evaluated;
- a \(C_5\)-induced light-fermion mass/source insertion adds at least one further inverse power of \(M_E\), so it is beyond the strict \(M_E^{-4}\) scalar tadpole considered here;
- the \(Q_8\) insertion must not be counted as an extra copy of the already evaluated \(Q_6Q_6\) current bubble.

The numerator reduction and scaleless-integral classification are checked in calculations/RC-001-dimension8-Q8-soft-tadpole-audit.py; the recorded output is validation/RC-001-dimension8-Q8-soft-tadpole-audit.txt.

## 5. Local dimension-eight pole operators and matching boundary

The UV pole is local. In the Euclidean Green basis it is proportional to
\[
\mathcal O_{8,H}^{E}
=\operatorname{tr}_2\!\left[
(D_\rho\mathcal J_{H,\mu})(D_\rho\mathcal J_{H,\mu})
-(D_\mu\mathcal J_{H,\mu})(D_\nu\mathcal J_{H,\nu})
\right],
\]
\[
\mathcal O_{8,S}^{E}
=(\partial_\rho j_{S,\mu})(\partial_\rho j_{S,\mu})
-(\partial_\mu j_{S,\mu})(\partial_\nu j_{S,\nu}).
\]
The soft UV-pole coefficients are
\[
\Gamma_{\rm soft,pole}^{E}
=\frac{\Delta_{\rm UV}}{192\pi^2}
\int d^dx\left[
\sum_\ell C_{LD,\ell}^2\mathcal O_{8,H}^{E}
+\sum_\ell C_{RD,\ell}^2\mathcal O_{8,S_\ell}^{E}
\right].
\]
The EFT counterterm cancels this pole with the opposite sign in this Euclidean effective-action convention. In the UV–EFT matching, the corresponding UV hard-region IR pole must cancel the EFT soft UV pole. The displayed soft result alone is **not** the finite hard Wilson coefficient.

The logarithm is nonlocal and must be retained until the hard/soft subtraction is assembled. Setting \(q^2=0\) before the subtraction makes the massless bubble scaleless and hides the UV/IR pole separation.

For a purely real neutral radial background with gauge fields set to zero, both \(j_S^\mu\) and \(\mathcal J_H^\mu\) vanish. Thus these current-current soft sectors do not generate a constant-background \(h\)-\(s\) potential term. They are nevertheless nonzero for generic complex-scalar scattering and belong to the dimension-eight derivative-operator matching.

## 6. Census correction and no-double-counting rule

The previous census row SFT-06, which labeled \(Q_{LD}Q_{RD}\) as a one-loop mixed four-scalar graph, is incorrect in the unbroken massless EFT. Replace its status by **no connected one-loop contraction at \(O(M_E^{-4})\)**. Do not introduce an artificial \(L\)-to-\(\ell_R\) propagator. The mixed \(C_5C_5^*\) bubble is a distinct, already-counted topology at \(O(M_E^{-2})\); \(C_5^4\) is another distinct dimension-eight topology. Neither is a substitute for a nonexistent \(Q_{LD}Q_{RD}\) current bubble.

The present result closes only these EFT soft sectors:
- \(Q_{LD}^2\): evaluated in the common current Green basis;
- \(Q_{RD}^2\): evaluated in the common current Green basis;
- \(Q_{LD}Q_{RD}\): proved zero at the stated order.

Still required for a dimension-eight UV–EFT match:
1. hard-region expansion of the corresponding full-theory four-scalar UV boxes at \(y^4\), \(\lambda^4\), and any other allowed coupling structures;
2. UV counterterms, external-field normalization, and all same-order tree-EFT insertions;
3. common-basis EOM/source projection, including the dimension-seven companions above;
4. independent diagram-level validation and scale-independence checks.

No finite dimension-eight Wilson coefficient or complete dimension-eight matching is claimed here.
