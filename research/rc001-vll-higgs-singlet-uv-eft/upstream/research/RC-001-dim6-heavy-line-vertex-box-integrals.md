# RC-001 — Heavy-line self-energy, Yukawa-vertex, and crossed-box master integrals

**Status:** the scalar master integrals and the heavy-line self-energy subgraph are analytically evaluated. The complete gauge-corrected \(Q_{LD}\) and \(Q_{RD}\) amplitudes are **not** claimed: the relative signs, all crossed routings, Dirac/Fierz projections, and complete UV–EFT sums must still be assembled before a Wilson coefficient can be quoted.

## 1. Conventions

Use Feynman gauge for this sub-block, \(d=4-2\epsilon\), and
\[
\Delta_\epsilon=\frac1\epsilon-\gamma_E+\ln4\pi,\qquad
L_\ell=\ln\frac{M_{E_\ell}^2}{\mu_R^2}.
\]
Normalize scalar loop integrals by
\[
\int_k \equiv (4\pi)^\epsilon\mu_R^{2\epsilon}\int\frac{d^dk}{i\pi^{d/2}},
\]
with the usual \(+i0\) prescriptions understood. The explicit \((4\pi)^\epsilon\) factor is part of the stated loop normalization and makes the pole convention \(\Delta_\epsilon=1/\epsilon-\gamma_E+\ln4\pi\) consistent with the displayed scalar master integrals. The displayed \(\Delta_{\rm UV}\) and \(\Delta_{\rm IR}\) symbols are kept distinct; a scaleless integral is never treated as evidence that its UV and IR poles separately vanish.

## 2. Heavy-\(E_\ell\) self-energy at low momentum

Define the 1PI self-energy sign by
\[
S_E^{-1}(p)=\slashed p-M_E-\Sigma_E(\slashed p),\qquad
\Sigma_E(\slashed p)=
\frac{g_A^2 C_E^A}{16\pi^2}
\left[\Sigma_V(p^2)\slashed p+\Sigma_S(p^2)M_E\right].
\]
For a massless gauge boson in Feynman gauge, Feynman parametrization gives
\[
\begin{aligned}
\Sigma_V(p^2)&=(2-d)\int_0^1 dx\,(1-x)
\left[
\Delta_\epsilon-\ln\frac{x(M_E^2-(1-x)p^2)-i0}{\mu_R^2}
\right],\\
\Sigma_S(p^2)&=d\int_0^1 dx
\left[
\Delta_\epsilon-\ln\frac{x(M_E^2-(1-x)p^2)-i0}{\mu_R^2}
\right].
\end{aligned}
\]
At \(p^2=0\), the exact parameter integrals needed through \(O(\epsilon^0)\) are
\[
\int_0^1 dx\,(1-x)(\Delta_\epsilon-L_\ell-\ln x)
=\frac12(\Delta_\epsilon-L_\ell)+\frac34,
\]
\[
\int_0^1 dx\,(\Delta_\epsilon-L_\ell-\ln x)
=\Delta_\epsilon-L_\ell+1.
\]
Keeping the \(O(\epsilon)\) pieces of \(2-d=-2+2\epsilon\) and \(d=4-2\epsilon\), because they multiply the UV pole, yields
\[
\boxed{\Sigma_V(0)=-\Delta_\epsilon+L_\ell-\frac12},\qquad
\boxed{\Sigma_S(0)=4\Delta_\epsilon-4L_\ell+2}.
\]

The chirality-preserving heavy propagator has
\[
P_R S_E^{(0)}(p)P_L
=-\frac{i\slashed p P_L}{M_E^2}+O(p^3/M_E^4).
\]
Inserting the 1PI self-energy and expanding to first order in \(g_A^2\), its relative correction is
\[
\left.\frac{\delta(P_R S_E P_L)}{P_R S_E^{(0)}P_L}\right|_{\Sigma_E^{\rm 1PI}}
=\frac{g_A^2 C_E^A}{16\pi^2}
\left[-\Sigma_V(0)-2\Sigma_S(0)\right]
\]
and hence
\[
\boxed{
\left.\frac{\delta(P_R S_E P_L)}{P_R S_E^{(0)}P_L}\right|_{\Sigma_E^{\rm 1PI}}
=\frac{g_A^2 C_E^A}{16\pi^2}
\left[-7\Delta_\epsilon+7L_\ell-\frac72\right].
}
\]
The same scalar coefficient applies to the opposite chirality-preserving projection \(P_L S_E P_R\). This is a gauge-dependent subgraph, not a gauge-invariant Wilson coefficient.

For diagonal gauge exchange,
\[
C_E^B=Y_E^2=1,\qquad C_E^W=0,\qquad
C_E^X=x_E^2Q_\ell^2=Q_\ell^2.
\]
Thus the heavy-line subgraph exists for \(B\) and \(A'\), but not for \(W^I\), because \(E_\ell\) is an \(SU(2)_L\) singlet. If a mixed propagator is present, define \(\kappa_{BX}\) as its off-diagonal transverse propagator relative to the diagonal propagator. At first order in \(\kappa_{BX}\), the same kernel is multiplied by
\[
2\kappa_{BX}g_Yg_X\,Y_E(x_EQ_\ell)
=-2\kappa_{BX}g_Yg_X\,\eta_\ell Q_\ell,
\]
where the factor of two is the sum of the two orientations of the symmetric off-diagonal propagator. This term is conditional on the declared kinetic-matrix convention.

The UV pole in the bare self-energy insertion must be combined with heavy-field and mass counterterms exactly once. With the standard Feynman-gauge pole terms \(\delta Z_E=-g_A^2C_E^A\Delta_\epsilon/(16\pi^2)\) and \(\delta M_E/M_E=-3g_A^2C_E^A\Delta_\epsilon/(16\pi^2)\), the corresponding propagator-counterterm contribution is \(+7g_A^2C_E^A\Delta_\epsilon/(16\pi^2)\). After this subgraph-level cancellation, its finite remainder is \(g_A^2C_E^A(7L_\ell-7/2)/(16\pi^2)\). Do not add this counterterm contribution a second time through a separate tree-coefficient parameter-counterterm row.

## 3. Yukawa-vertex scalar kernel

At vanishing external momenta, the heavy-light-fermion and heavy-scalar vertex topologies reduce to the same two-propagator scalar master after their numerator algebra. Define
\[
B_0(0;0,M_E^2)=
\int_k\frac{1}{(k^2+i0)(k^2-M_E^2+i0)}.
\]
Then
\[
\boxed{B_0(0;0,M_E^2)=\Delta_\epsilon+1-L_\ell.}
\]
For the heavy–light fermion numerator, retain \(d=4-2\epsilon\) through the pole multiplication:
\[
\boxed{d\,B_0(0;0,M_E^2)=4\Delta_\epsilon+2-4L_\ell+O(\epsilon).}
\]
The finite \(+2\) rather than \(+4\) is due to \((-2\epsilon)(1/\epsilon)=-2\). Dropping the \(O(\epsilon)\) part of \(d\) before multiplying the UV pole would therefore corrupt the finite hard term. This remains a numerator kernel before the graph's overall signs and group factors.
For the heavy-light-fermion vertex, the representative numerator contraction
\[
\gamma^\mu\slashed k P_{R,L}\slashed k\gamma_\mu
=d\,k^2 P_{R,L}
\]
(up to the chirality relabeling fixed by the vertex orientation) reduces the loop kernel to \(d\,B_0\). For the heavy-scalar vertex, the scalar-gauge vertex supplies one internal momentum \(k_\mu\) when the external scalar momentum is set to zero; after symmetric integration the term proportional to \(M_E\slashed k\) vanishes and the numerator reduces to \(k^2\), giving \(B_0\). The sign depends on the consistently assigned scalar-flow orientation and is not fixed by this scalar-kernel statement. These are numerator-reduction kernels before the overall Feynman-rule signs, representation generators, and orientation-dependent charge factors are applied.

The light-fermion–scalar exchange at a Yukawa vertex contains no heavy propagator. At zero external momenta its loop integral is scaleless and belongs to the common soft sector; it cannot be assigned a hard finite coefficient independently of the matched EFT subtraction.

## 4. Crossed-box master and explicit UV–EFT split

A common leading box numerator reduces the scalar kernel
\[
J(M_E)=\int_k
\frac{1}{(k^2+i0)^2(k^2-M_E^2+i0)}.
\]
Partial fractions give
\[
\frac{1}{(k^2)^2(k^2-M_E^2)}
=-\frac{1}{M_E^4k^2}
-\frac{1}{M_E^2(k^2)^2}
+\frac{1}{M_E^4(k^2-M_E^2)}.
\]
Using \(A_0(M_E^2)=M_E^2(\Delta_\epsilon+1-L_\ell)\) and retaining the separate UV/IR poles of the scaleless massless bubble, the full zero-momentum integral is
\[
\boxed{
J_{\rm full}(M_E)=\frac1{M_E^2}
\left(\Delta_{\rm IR}+1-L_\ell\right).
}
\]
The soft-region expansion of the heavy propagator is \(-1/M_E^2\), so
\[
\boxed{
J_{\rm soft}(M_E)=\frac1{M_E^2}
\left(-\Delta_{\rm UV}+\Delta_{\rm IR}\right).
}
\]
The hard part, equivalently the full UV integral minus the EFT soft integral, is therefore
\[
\boxed{
J_{\rm hard}(M_E)=J_{\rm full}-J_{\rm soft}
=\frac1{M_E^2}\left(\Delta_{\rm UV}+1-L_\ell\right).
}
\]
This explicitly demonstrates why setting a scaleless EFT integral to zero before separating its UV and IR poles would lose the UV pole of the local matching coefficient. In the actual amplitudes, use the common nonexceptional external momenta or shared IR regulator from the subtraction ledger; the zero-momentum expression above is a master-integral expansion, not a substitute for summing all graphs.

## 5. Charge mapping and current status

For the tree exchange of either \(Q_{LD}\) or \(Q_{RD}\), the heavy-line self-energy charge factors are identical:
- \(BB:\;Y_E^2=1\);
- \(WW:\;0\);
- \(A'A':\;x_E^2Q_\ell^2=Q_\ell^2\);
- \(BA'\): conditional on the off-diagonal propagator; with the \(\kappa_{BX}\) convention above, the heavy-line factor is \(-2\kappa_{BX}g_Yg_X\eta_\ell Q_\ell\).

The evaluated kernels in this file do not yet determine the full vertex or crossed-box coefficients. The following remain open for each LD/RD gauge sector: all crossed momentum routings and multiplicities; overall signs and group-generator ordering; the complete Dirac/Fierz and weak-tensor projections; external-field and parameter counterterms in one consistent organization; EFT contact graphs; and the summed Ward-identity check. No complete finite \(O(g^2/M_E^2)\) Wilson coefficient is claimed.
