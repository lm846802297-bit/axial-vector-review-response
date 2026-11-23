# RC-001 QLD8 — P1.6a same-bilinear exchange UV poles

**Date:** 2026-11-10  
**Scope:** Feynman-gauge same-bilinear graphs (\bar Q,d) and (Q,\bar d), original direct spinor pairing and direct singlet/octet color basis.  
**Result:** both graphs have an exact D-dimensional scalar UV pole. The rank-two numerator proportional to D-4 has a UV-finite tensor integral under nonexceptional off-shell subtraction; it does not produce a (D-4) times 1/epsilon finite local UV term in these graphs.

## 1. Numerators and routing

Left graph:
\[
r_1=p_1+\ell,\quad r_2=p_2-\ell,\quad
N_L=\gamma^\rho\slashed r_1P_R\slashed r_2\gamma_\rho\otimes P_L.
\]
Right graph:
\[
r_3=p_3-\ell,\quad r_4=p_4+\ell,\quad
N_R=P_R\otimes\gamma^\rho\slashed r_3P_L\slashed r_4\gamma_\rho.
\]
Both have denominator ell^2 r_a^2 r_b^2 and external derivative factor q_A^2=(p_1+p_2)^2=(p_3+p_4)^2. Neither has (q_A plus/minus ell)^2.

Use the exact D-dimensional identity:
\[
\gamma^\rho\slashed r\slashed s\gamma_\rho P_X
=D(r\cdot s)P_X+(D-4)\Gamma^{\mu\nu}r_\mu s_\nu P_X.
\]

## 2. Scalar integral

For the left graph:
\[
I_S=\mu^{2\epsilon}\int\frac{d^D\ell}{(2\pi)^D}
\frac{r_1\cdot r_2}{\ell^2r_1^2r_2^2}.
\]
Feynman-parametrize with x+y+z=1 and shift
\[
L=\ell+yp_1-zp_2,\quad
A=(1-y)p_1+zp_2,\quad B=yp_1+(1-z)p_2.
\]
Then r_1=L+A, r_2=-L+B, and
\[
r_1\cdot r_2=-L^2+L\cdot(B-A)+A\cdot B.
\]
The odd term vanishes. A dot B multiplies a UV-finite three-propagator integral. Only -L^2 produces the UV pole:
\[
\int\frac{d^DL}{(2\pi)^D}
\frac{L^2}{(L^2-\Delta+i0)^3}
=\frac{i}{(4\pi)^{D/2}}\frac D4
\Gamma(\epsilon)\Delta^{-\epsilon}.
\]
The simplex volume is 1/2 and the Feynman-parameter prefactor is 2, so their product is one. Therefore
\[
\boxed{I_S^{UV}=-\frac{i}{(4\pi)^{D/2}}\frac D4
\mu^{2\epsilon}\Gamma(\epsilon)
=-\frac{i}{16\pi^2}\frac{D}{4\epsilon}+\text{finite}.}
\]
Take generic nonexceptional Euclidean off-shell invariants, e.g. p_1^2,p_2^2,(p_1-p_2)^2 nonzero, so no IR pole is confused with the UV pole.

## 3. Antisymmetric tensor integral

After the same shift,
\[
\Gamma^{\mu\nu}r_{1\mu}r_{2\nu}
=-\Gamma^{\mu\nu}L_\mu L_\nu
+\Gamma^{\mu\nu}L_\mu B_\nu
-\Gamma^{\mu\nu}A_\mu L_\nu
+\Gamma^{\mu\nu}A_\mu B_\nu.
\]
The first term vanishes by antisymmetry; the linear terms integrate to zero. Also
\[
A\wedge B=[(1-y)(1-z)-yz]p_1\wedge p_2
=(1-y-z)p_1\wedge p_2=x\,p_1\wedge p_2.
\]
Thus the remaining tensor term is proportional to
\[
\Gamma^{\mu\nu}p_{1\mu}p_{2\nu}
\int_{\rm simplex}dx\,dy\,dz\,x
\int\frac{d^DL}{(2\pi)^D}\frac1{(L^2-\Delta+i0)^3}.
\]
The loop integral is proportional to Gamma(3-D/2)=Gamma(1+epsilon), which is UV finite:
\[
\boxed{[I_T]_{\rm UV\ pole}=0.}
\]
Hence (D-4)I_T=-2epsilon I_T vanishes as epsilon tends to zero for this nonexceptional off-shell graph. The tensor numerator was retained until after integration; no four-dimensional identity was used.

## 4. Signed amplitude and color block

The frozen Feynman-rule phase product is
\[
(iC)(ig_s)^2(i)^2(-i)=+Cg_s^2.
\]
Together with the scalar loop pole, the normalized 1PI coefficient for each graph is -D^2/4 times its direct-basis color matrix, multiplying q_A^2(P_R tensor P_L).

The exact direct-basis matrices are identical:
\[
M_{\bar Q,d}^{(d)}=M_{Q,\bar d}^{(d)}
=\begin{pmatrix}-4/3&0\\0&1/6\end{pmatrix}.
\]
The two-graph result is
\[
\boxed{
\mathcal M_{\rm same,div}^{(1)}
=iC\frac{g_s^2}{16\pi^2\epsilon}
q_A^2(P_R\otimes P_L)
\left[-\frac{D^2}{2}
\begin{pmatrix}-4/3&0\\0&1/6\end{pmatrix}\right].
}
\]
Thus the combined SU(3) color block is
\[
\boxed{\begin{pmatrix}2D^2/3&0\\0&-D^2/12\end{pmatrix}.}
\]
For the tree-singlet vector (1,0), only the singlet column contributes:
\[
\boxed{
\mathcal K_{\rm same}^{tree}
=\frac{C_FD^2}{2}q_A^2(P_R\otimes P_L)
=(8C_F-8C_F\epsilon+2C_F\epsilon^2)q_A^2(P_R\otimes P_L).
}
\]
At D=4 this is 8C_F=32/3 for SU(3). These graphs do not mix the tree singlet into the direct octet.

## 5. Coefficient expansions

Per graph:
\[
-\frac{D^2}{4}M_{\rm within}
=\begin{pmatrix}D^2/3&0\\0&-D^2/24\end{pmatrix}.
\]
For both:
\[
-\frac{D^2}{2}M_{\rm within}
=\begin{pmatrix}
32/3-32\epsilon/3+8\epsilon^2/3&0\\
0&-4/3+4\epsilon/3-\epsilon^2/3
\end{pmatrix}.
\]
The O(epsilon) numerator terms are retained for scheme bookkeeping; they are not a complete finite matching coefficient without the finite loop parts and a declared subtraction/evanescent scheme.

## 6. Correction to P1.5c+

The earlier statement that the same-bilinear (D-4) tensor term can automatically multiply a UV pole was too broad. The actual antisymmetric tensor integral is UV finite for these nonexceptional off-shell three-propagator graphs. Correct procedure: retain the D-dimensional numerator, integrate it, and only then classify its UV pole. Here the tensor UV pole is zero.

## 7. Boundary

Completed: both same-bilinear scalar UV poles, exact D dependence, O(epsilon) coefficients, tensor UV-finiteness proof, Feynman-rule phase and direct-color block.

Open: four external-quark wave-function counterterms; complete six-exchange Green function; external-background-gluon Ward identities; full off-shell/R* operator subtraction; EOM/IBP; physical/evanescent/EOM Z block; finite UV-minus-EFT matching. No anomalous dimension or final Wilson coefficient is claimed.
