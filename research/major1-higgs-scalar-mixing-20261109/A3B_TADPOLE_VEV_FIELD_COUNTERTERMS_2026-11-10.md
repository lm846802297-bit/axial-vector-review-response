# Major Point 1 — A3b tadpole, VEV, portal and field-counterterm matrix

**Purpose:** fix the counterterm algebra needed to combine the A3a scalar bubbles with the already computed fermion matching. This note derives the parameter/field counterterm structure but does not choose numerical finite renormalization conditions.

## 1. Tree potential and tadpoles

For
\[
V=-\mu_H^2H^\dagger H-\mu_S^2S^\dagger S
+\lambda_H(H^\dagger H)^2+\lambda_S(S^\dagger S)^2
+\lambda_{HS}(H^\dagger H)(S^\dagger S),
\]
the tree tadpoles at \(H^0=v/\sqrt2\), \(S=v_S/\sqrt2\) are
\[
T_h=-\mu_H^2v+\lambda_Hv^3+\frac12\lambda_{HS}vv_S^2,
\]
\[
T_s=-\mu_S^2v_S+\lambda_Sv_S^3+\frac12\lambda_{HS}v^2v_S.
\]
The tree stationarity conditions are
\[
\mu_H^2=\lambda_Hv^2+\frac12\lambda_{HS}v_S^2,\qquad
\mu_S^2=\lambda_Sv_S^2+\frac12\lambda_{HS}v^2.
\]

Let
\[
v_0=v+\delta v,\quad v_{S0}=v_S+\delta v_S,\quad
\lambda_{i,0}=\lambda_i+\delta\lambda_i,\quad
\mu_{i,0}^2=\mu_i^2+\delta\mu_i^2.
\]
Linearizing the tadpoles and using the tree stationarity conditions gives
\[
\boxed{\begin{aligned}
\delta T_h={}&-v\,\delta\mu_H^2+v^3\delta\lambda_H
+\frac12vv_S^2\delta\lambda_{HS}
+2\lambda_Hv^2\delta v
+\lambda_{HS}vv_S\delta v_S,\\
\delta T_s={}&-v_S\delta\mu_S^2+v_S^3\delta\lambda_S
+\frac12v^2v_S\delta\lambda_{HS}
+2\lambda_Sv_S^2\delta v_S
+\lambda_{HS}vv_S\delta v.
\end{aligned}}
\]
The renormalized tadpole conditions are \(T_h^{\rm loop}+\delta T_h=0\) and \(T_s^{\rm loop}+\delta T_s=0\). Equivalently, one may use an explicit tadpole-counterterm prescription; the same choice must then be used in the two-point functions. Do not independently shift \(v,v_S\) and also add a second copy of the same tadpole insertion.

## 2. Parameter counterterms for the CP-even mass matrix

At tree level,
\[
{\cal M}_0^2=
\begin{pmatrix}
2\lambda_Hv^2&\lambda_{HS}vv_S\\
\lambda_{HS}vv_S&2\lambda_Sv_S^2
\end{pmatrix}.
\]
The parameter/VEV counterterms are
\[
\boxed{\begin{aligned}
\delta M_{hh,\rm par}^2&=2v^2\delta\lambda_H+4\lambda_Hv\delta v,\\
\delta M_{ss,\rm par}^2&=2v_S^2\delta\lambda_S+4\lambda_Sv_S\delta v_S,\\
\delta M_{hs,\rm par}^2&=vv_S\delta\lambda_{HS}
+\lambda_{HS}(v_S\delta v+v\delta v_S).
\end{aligned}}
\]
These formulas are obtained after eliminating \(\mu_H^2,\mu_S^2\) with the tadpole conditions. They show explicitly why VEV renormalization contributes to the mixed mass whenever the UV portal is nonzero.

## 3. Field-renormalization matrix

Use the general, not-yet-assumed-symmetric field renormalization
\[
\begin{pmatrix}h_0\\s_0\end{pmatrix}
=
\left[
I+\frac12
\begin{pmatrix}
\delta Z_{hh}&\delta Z_{hs}\\
\delta Z_{sh}&\delta Z_{ss}
\end{pmatrix}
\right]
\begin{pmatrix}h\\s\end{pmatrix}.
\]
For the inverse-propagator convention
\[
\Gamma_{\rm inv}(p^2)=p^2I-{\cal M}_0^2+\Pi(p^2),
\]
the field counterterm contributions are
\[
\delta\Gamma_{\rm kin}(p^2)
=\frac12(\delta Z+\delta Z^T)p^2,
\qquad
\delta{\cal M}_{Z}^2
=\frac12(\delta Z^T{\cal M}_0^2+{\cal M}_0^2\delta Z).
\]
Thus
\[
\boxed{\begin{aligned}
\delta\Gamma_{hs}^{\rm ct}(p^2)={}&
\frac12(\delta Z_{hs}+\delta Z_{sh})p^2\\
&-\frac12\left[
\delta Z_{hh}M_{hs}^2+\delta Z_{sh}M_{ss}^2
+M_{hh}^2\delta Z_{hs}+M_{hs}^2\delta Z_{ss}
\right]\\
&-\delta M_{hs,\rm par}^2
+\delta\Gamma_{hs}^{\rm tad,scheme}.
\end{aligned}}
\]
Here \(\delta\Gamma_{hs}^{\rm tad,scheme}\) denotes any explicit tadpole-counterterm contribution not already absorbed into \(\delta v,\delta v_S,\delta\mu_H^2,\delta\mu_S^2\). It must be included exactly once.

At a zero tree-portal point, \(M_{hs}^2=0\), and for a symmetric field-renormalization convention \(\delta Z_{hs}=\delta Z_{sh}\), this reduces to
\[
\boxed{
\delta\Gamma_{hs}^{\rm ct}(p^2)
=\delta Z_{hs}\left[p^2-\frac12(m_h^2+m_s^2)\right]
-vv_S\delta\lambda_{HS}
+\delta\Gamma_{hs}^{\rm tad,scheme}.
}
\]
This makes the distinction between a local portal mass counterterm and a derivative/mixed-field counterterm explicit.

## 4. Combined-order assignment

At the conditional matching point,
\[
\lambda_{HS}^{\rm EFT}(M_E)=0,\qquad
\lambda_{HS}^{\rm UV}(M_E)=-\Delta\lambda_{HS}^{\rm hard}=O(\hbar).
\]
Therefore, at the next combined order:
- \(vv_S\delta\lambda_{HS}^{\rm scalar}\), with \(\delta\lambda_{HS}^{\rm scalar}\propto\lambda_{HS}\lambda_{H,S}/(16\pi^2\bar\epsilon)\), is \(O(\hbar^2)\);
- \(\lambda_{HS}(v_S\delta v+v\delta v_S)\) is \(O(\hbar^2)\) when the VEV shifts are one-loop;
- \(\lambda_{HS}\delta Z_{hh,ss}\) contributions to the mixed mass are \(O(\hbar^2)\);
- off-diagonal \(\delta Z_{hs,sh}\) terms multiply the leading diagonal masses and must be retained at the order at which they arise;
- the two-loop VLL/gauge/Yukawa portal matching and the complete EFT soft-counterterm set are also required for a closed result.

The scalar-only A3a pole is one contribution to \(\delta\lambda_{HS}\). The full portal counterterm also contains gauge, Yukawa and VLL-sector terms. It is not permissible to use the scalar-only coefficient as the complete portal beta function.

## 5. Relation to the existing fermion matching

The existing exact fermion-sector work already distinguishes the full-theory derivative pole from the EFT light-loop derivative pole. Their difference requires an EFT mixed-field counterterm even when the full-theory off-diagonal derivative divergence cancels. That matching field counterterm must be inserted into the same \(\delta Z_{hs,sh}\) matrix above; it is not an additional independent physical mixing angle.

The existing fermion-sector finite \(\Pi_{hs}\), the A3a scalar bubbles, the portal threshold insertion, and the field/tadpole counterterms must be assembled in one common scheme. In particular, do not add the VLL hard portal threshold again after imposing the matching boundary condition.

## 6. Symbolic validation and remaining input

The accompanying SymPy audit verifies:
1. the linearized \(h,s\) tadpole counterterms;
2. the three parameter/VEV mass-counterterm formulas;
3. the general field-renormalization contribution to the off-diagonal inverse propagator;
4. the symmetric zero-portal limit.

The algebra is fixed, but the calculation still needs a declared tadpole/VEV prescription, a choice of symmetric or nonsymmetric \(\delta Z\) convention, and the actual UV/EFT counterterm coefficients at the common matching scale. No finite physical mixed self-energy is inferred from this identity map.
