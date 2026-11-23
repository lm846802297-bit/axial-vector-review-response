# RC-001 — Tree-level matching of the dimension-five lepton operator

**Audit date:** 2026-10-27  
**Scope status:** The tree-level coefficient and its sign are derived and independently checked within the conventions below. This note does not close the one-loop matching problem.

## 1. UV interaction and EFT convention

For each \(\ell=\mu,\tau\), retain the UV interactions

\[
\mathcal L_{\rm UV}\supset
-M_{E_\ell}\bar E_{\ell L}E_{\ell R}
-y_\ell\bar L_\ell H E_{\ell R}
-\lambda_\ell S_\ell\bar E_{\ell L}\ell_R
+\mathrm{h.c.},
\]

where \(E_\ell\) is the heavy vector-like lepton and \(H,S_\ell,L_\ell,\ell_R\) are retained as light fields in the EFT. The flavor assignment is \(S_\mu=S\), \(S_\tau=S^*\).

Fix the operator convention to be

\[
\mathcal O_{5,\ell}=S_\ell\bar L_\ell H\ell_R,
\qquad
\mathcal L_{\rm EFT}^{(5)}
\supset -C_{5,\ell}\mathcal O_{5,\ell}+\mathrm{h.c.}
\]

The coefficient is not defined with an implicit sign: the minus sign in front of \(C_{5,\ell}\mathcal O_{5,\ell}\) is part of the convention.

## 2. Sign from the heavy-block Schur complement

After writing \(H^0=v_h/\sqrt2\) and \(S_\ell=w_\ell/\sqrt2\), the mass matrix in the row basis \((\ell_L,E_{\ell L})\) and column basis \((\ell_R,E_{\ell R})\) is

\[
\mathcal M_\ell=
\begin{pmatrix}
0 & y_\ell v_h/\sqrt2\\
\lambda_\ell w_\ell/\sqrt2 & M_{E_\ell}
\end{pmatrix},
\qquad
\mathcal L_{\rm mass}=-\overline{\Psi_L}\mathcal M_\ell\Psi_R+\mathrm{h.c.}
\]

At leading order in the inverse heavy mass, eliminating the heavy block gives the light mass-matrix entry

\[
\begin{aligned}
M_{\ell,\mathrm{eff}}
&=0-
\left(\frac{y_\ell v_h}{\sqrt2}\right)
\frac{1}{M_{E_\ell}}
\left(\frac{\lambda_\ell w_\ell}{\sqrt2}\right)\\
&=-\frac{y_\ell\lambda_\ell v_hw_\ell}{2M_{E_\ell}}.
\end{aligned}
\]

In the stated EFT convention, the same mass-matrix entry is \(C_{5,\ell}v_hw_\ell/2\), because the Lagrangian contains \(-C_{5,\ell}S_\ell\bar L_\ell H\ell_R\). Equating the entries therefore gives

\[
\boxed{C_{5,\ell}^{(0)}=-\frac{y_\ell\lambda_\ell}{M_{E_\ell}}.}
\]

The result applies separately to \(\mu\) and \(\tau\). For complex couplings, \(C_{5,\ell}\) is complex as written and the Hermitian-conjugate operator carries \(C_{5,\ell}^*\); replacing the product by its absolute value would change the operator coefficient.

## 3. Propagator expansion and power counting

The same result is consistent with the low-momentum heavy propagator. Suppressing its overall Feynman-rule factor \(i\),

\[
(\slashed p-M_E)^{-1}
=-\frac1{M_E}-\frac{\slashed p}{M_E^2}
-\frac{p^2}{M_E^3}
+O\!\left(\frac{p^3}{M_E^4}\right).
\]

For \(P_{R,L}=(1\pm\gamma_5)/2\), the identities \(P_R\slashed pP_R=0\) and \(P_R\slashed pP_L=\slashed pP_L\) imply

\[
P_R(\slashed p-M_E)^{-1}P_R
=-\frac{P_R}{M_E}-\frac{p^2P_R}{M_E^3}+\cdots,
\]

whereas

\[
P_R(\slashed p-M_E)^{-1}P_L
=-\frac{\slashed pP_L}{M_E^2}
+O\!\left(\frac{p^3}{M_E^4}\right).
\]

The mass-numerator component connecting the \(E_R\) and \(\bar E_L\) vertices begins at \(1/M_E\), yielding the dimension-five operator. The momentum-numerator component begins at \(1/M_E^2\) and generates derivative operators. The latter are recorded separately in the RC-001 tree-level dimension-six basis as \(Q_{LD}\) and \(Q_{RD}\); they must not be folded into \(C_5\).

The propagator expansion fixes the inverse-mass order. The Schur-complement comparison above fixes the coefficient sign in the declared Lagrangian convention, without relying on an isolated propagator sign.

## 4. Assumptions and boundaries

- The heavy mass \(M_{E_\ell}\) is nonzero and external momenta and retained light masses are small compared with it.
- \(H\) and \(S_\ell\) remain dynamical EFT fields; only \(E_\ell\) is integrated out in this step.
- This is tree-level matching at leading order \(1/M_{E_\ell}\). It does not include one-loop renormalization of \(C_{5,\ell}\), portal thresholds, or running between matching scales.
- No conclusion about the physical \(B_1/B_3\) candidate-kernel sign follows from this tree-level calculation.
- The complete one-loop dimension-six Wilson vector, the full same-order EFT soft/counterterm set, and the final UV–EFT subtraction remain separate open tasks.

## 5. Reproducibility

The companion script [RC-001-tree-level-C5-matching-check.py](../calculations/RC-001-tree-level-C5-matching-check.py) verifies the chiral-projector identities, the propagator power counting, the Schur complement, and the coefficient sign using exact SymPy algebra. Its captured output is [RC-001-tree-level-C5-matching-check.txt](../validation/RC-001-tree-level-C5-matching-check.txt).

**Conclusion:** \(C_{5,\ell}^{(0)}=-y_\ell\lambda_\ell/M_{E_\ell}\) is independently derived and checked at tree level in the stated convention. This closes that narrowly defined input coefficient, not the broader UV–EFT matching project.
