# RC-001 QLD8 — P1.5c merged direct-pairing cross-source UV pole

**Status (2026-11-10):** SS, TS, ST and TT are assembled into one raw local momentum-space pole kernel. Exact D dependence and O(epsilon) terms are retained. No d-dimensional Fierz, EOM or IBP quotient is taken.

Use all-incoming momenta p1+p2+p3+p4=0, q=p1+p2, d=p1-p2, R=p3-p4, and W(u,v)=Gamma^{mu nu}u_mu v_nu. The direct spinor pairing remains (bar Q,d) tensor (bar d,Q); color basis is (1_d,8_d).

## 1. Unified four-sector kernel

\[
\begin{aligned}
{\cal K}_{cross}(D)={}&
\frac{D^2+10D-8}{48}(d\cdot R)(P_R\otimes P_L)\\
&+\frac{D+8}{12}[\Gamma^{\mu\nu}q_\mu(p_4-p_3)_\nu P_R]\otimes P_L\\
&-\frac{D+8}{6}P_R\otimes[\Gamma^{\mu\nu}(p_1)_\mu(p_2)_\nu P_L]\\
&+J_{\alpha\beta}(D)(\Gamma^{\alpha\rho}P_R)\otimes(\Gamma^\beta{}_{\rho}P_L),
\end{aligned}
\]
where
\[
J_{\alpha\beta}(D)=\frac{D}{24}(d_\alpha d_\beta+R_\alpha R_\beta)-\frac{D+12}{24}q_\alpha q_\beta+
\frac{g_{\alpha\beta}}{48}[D(d^2+R^2)+(D-20)q^2].
\]
In the frozen phase convention, M_div^(1)=i C g_s^2/(16 pi^2 epsilon) K_cross|pole, with the overall direct-octet color tensor understood. The counterterm insertion has the opposite sign. The pole residue uses D->4; O(epsilon) numerator terms are retained for finite scheme bookkeeping.

## 2. D=4-2epsilon coefficients

F_SS=1-3 epsilon/4+epsilon^2/12; F_TS=1-epsilon/6; F_ST=-2+epsilon/3. The TT tensor is J=J^(0)+epsilon J^(1)+O(epsilon^2), with
\[
\begin{aligned}
J^{(0)}_{\alpha\beta}={}&\frac16(d_\alpha d_\beta+R_\alpha R_\beta)-\frac23q_\alpha q_\beta+
\frac{g_{\alpha\beta}}{12}(d^2+R^2-4q^2),\\
J^{(1)}_{\alpha\beta}={}&-\frac1{12}(d_\alpha d_\beta+R_\alpha R_\beta)+\frac1{12}q_\alpha q_\beta-
\frac{g_{\alpha\beta}}{24}(d^2+R^2+q^2).
\end{aligned}
\]
The complete linear-epsilon kernel is -3/4(d.R) SS -1/6 TS +1/3 ST + J^(1). The scalar coefficient also has its exact epsilon^2/12 term.

## 3. Momentum and color checks

Momentum conservation gives d.R=p1^2-p2^2+2 p1.p3-2 p2.p3 and W(q,p4-p3)=-2[W(p1,p3)+W(p2,p3)]. The two mixed wedge structures W(q,p4-p3) and W(p1,p2) are linearly independent for generic off-shell momenta. J_ab is symmetric and retained unreduced.

Color weights (-1,+1,+1,-1), combined with the Dirac-chain signs, give SS (-,+,+,-), TS (+,-,+,-), ST (+,+,-,-), TT (+,+,+,+). The tree-singlet cross-source subset has zero direct-singlet projection and a direct-octet projection. This is not the full QCD mixing matrix.

The metric-contracted opposite-chirality tensor seed is four-dimensionally evanescent in the explicit diagnostic, but remains in the D-dimensional subtraction basis. No four-dimensional Fierz, EOM or IBP identity is used.

## 4. Boundary

Closed locally: unified SS+TS+ST+TT raw kernel, exact D coefficients, O(epsilon) terms, direct-octet projection, momentum-conservation reductions and retention of the evanescent seed.

Open: nonexceptional off-shell/R* UV-IR subtraction; complete D-dimensional physical/evanescent closure; external-background-gluon amplitudes and Ward identities; EOM/IBP after off-shell subtraction; full physical/evanescent/EOM Z block and anomalous dimension; same-bilinear and other source-pair sectors; finite UV-minus-EFT matching in a specified evanescent scheme.

This is the merged raw four-sector cross-source kernel, not yet a complete gauge-covariant counterterm basis or final Wilson coefficient.
