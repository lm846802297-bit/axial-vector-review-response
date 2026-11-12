# B5-2B4 — triplet derivative EOM and current-basis projection

**Date:** 2026-11-11  
**Parent:** B5-2B, strict dimension-six EFT gauge matching.  
**Input:** the oriented four-cross-box \(Q_{LD}\), pure-\(WW\) hard amplitude from B5-2B3.  
**Status:** the raw Pauli-triplet derivative structure has been reduced exactly to the B5-2B1 current/EOM basis. Its adjoint covariant derivative and direct \(W\)-contact term have been checked independently. This is still only the four-cross-box sub-block, not the complete \(WW\) matching coefficient or anomalous dimension.

## 1. Operator and normalization conventions

Use Pauli matrices \(\sigma^I\), not generators \(T^I=\sigma^I/2\), in the triplet currents:
\[
J_H^{(1)\mu}=H^\dagger i\overleftrightarrow D^\mu H,
\qquad
J_L^{(1)\mu}=\bar L\gamma^\mu L,
\]
\[
J_H^{(3)I\mu}=H^\dagger i\sigma^I
\overleftrightarrow D^\mu H,
\qquad
J_L^{(3)I\mu}=\bar L\sigma^I\gamma^\mu L.
\]
Define
\[
O_{HL}^{(1)}=J_H^{(1)}\cdot J_L^{(1)},
\qquad
O_{HL}^{(3)}=J_H^{(3)I}\cdot J_L^{(3)I}.
\]
The redundant fermion-EOM structures are
\[
E_L^{(1)}=(H^\dagger H)
\bar L i\overleftrightarrow{\slashed D}L,
\qquad
E_L^{(3)}=(H^\dagger\sigma^I H)
\bar L\sigma^I i\overleftrightarrow{\slashed D}L.
\]

The triplet derivative composite is
\[
C^I=H^\dagger\sigma^I L,\qquad
\bar C^I=\bar L\sigma^I H.
\]
Its symmetrized derivative form is
\[
Q_{LD}^{(3)}
\doteq
\frac{i}{2}\left[
\bar C^I\gamma^\mu D_\mu^{\rm adj}C^I
-(D_\mu^{\rm adj}\bar C^I)\gamma^\mu C^I
\right].
\]
The singlet derivative operator is
\[
Q_{LD}=(\bar L H)i\slashed D(H^\dagger L).
\]
The symbol \(\doteq\) denotes equality modulo a total derivative.

## 2. Exact Pauli reduction

The Pauli completeness identity is
\[
\sigma^I_{ij}\sigma^I_{kl}
=2\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl}.
\]
Applying it to the symmetrized derivative composite gives
\[
\boxed{
Q_{LD}^{(3)}
\doteq -O_{HL}^{(1)}+E_L^{(1)}-Q_{LD}.
}
\]

One way to see the result is to write
\[
Q_{LD}^{(3)}=2Q_{\rm cross}-Q_{LD}^{\rm sym},
\]
where the crossed contraction is
\[
Q_{\rm cross}
\doteq
-\frac12 O_{HL}^{(1)}+\frac12E_L^{(1)},
\]
and
\[
Q_{LD}^{\rm sym}
=Q_{LD}-\frac{i}{2}\partial_\mu
\left[(\bar L H)\gamma^\mu(H^\dagger L)\right].
\]
Combining these expressions gives the boxed identity.

The exact symbolic audit expands all weak indices \(i,j,k,l=1,2\) and all three Pauli matrices. The residual of the identity, including the displayed total derivative, is identically zero.

## 3. Projection into the B5-2B1 current/EOM basis

B5-2B1 established
\[
Q_{LD}\doteq
-\frac14O_{HL}^{(1)}
-\frac14O_{HL}^{(3)}
+\frac14E_L^{(1)}
+\frac14E_L^{(3)}.
\]
Substituting this into the triplet identity yields
\[
\boxed{
Q_{LD}^{(3)}
\doteq
-\frac34O_{HL}^{(1)}
+\frac14O_{HL}^{(3)}
+\frac34E_L^{(1)}
-\frac14E_L^{(3)}.
}
\]

Thus a Pauli-triplet derivative coefficient does **not** map only into \(O_{HL}^{(3)}\). It also induces a singlet-current term and two redundant EOM structures. Omitting these terms would make the operator-basis projection incomplete.

## 4. Adjoint covariant derivative and the direct \(W\) contact

With
\[
D_\mu H=(\partial_\mu-ig_2W_\mu^aT^a)H,
\qquad T^a=\frac{\sigma^a}{2},
\]
and the corresponding conjugate derivative on \(\bar L\), the two composites transform in the same real adjoint representation:
\[
\boxed{
D_\mu^{\rm adj}C^I
=\partial_\mu C^I-g_2\epsilon^{aIJ}W_\mu^aC^J,
}
\]
\[
\boxed{
D_\mu^{\rm adj}\bar C^I
=\partial_\mu\bar C^I-g_2\epsilon^{aIJ}W_\mu^a\bar C^J.
}
\]
The sign follows from
\[
[T^a,\sigma^I]=i\epsilon^{aIJ}\sigma^J.
\]

Consequently the symmetrized triplet derivative has a nonzero direct contact:
\[
\boxed{
Q_{LD}^{(3)}\big|_{W,\rm contact}
=-ig_2\epsilon^{aIJ}W_\mu^a
\bar C^I\gamma^\mu C^J.
}
\]
This differs from the singlet \(Q_{LD}\) of B5-2B2, which has no direct \(W^a\) contact at its derivative insertion.

The contact term is exactly reproduced by the gauge-field parts of the EOM/current identity. The required Pauli identity is
\[
\boxed{
-i\epsilon^{aIJ}\sigma^I_{ij}\sigma^J_{kl}
=\delta_{jk}\sigma^a_{il}
-\sigma^a_{kj}\delta_{il}.
}
\]
Indeed,
\[
\left[-O_{HL}^{(1)}+E_L^{(1)}-Q_{LD}\right]_{W,\rm contact}
=
g_2W_\mu^a\left[
(H^\dagger H)\bar L\sigma^a\gamma^\mu L
-(H^\dagger\sigma^aH)\bar L\gamma^\mu L
\right],
\]
which equals the adjoint-contact expression above after applying the Pauli identity.

Therefore the triplet contact vertex must be retained in any EFT Ward-identity check or amplitude comparison using \(Q_{LD}^{(3)}\). It must not be confused with the absence of a direct \(W\) contact for the singlet composite \(H^\dagger L\).

## 5. Wilson-coefficient contribution from the B5-2B3 box subset

B5-2B3R gives the raw hard four-box tensor coefficient
\[
A_{WW,\rm hard}^{\rm box}
=\frac{1}{M_E^2}
\left(\frac38\Delta_{\rm UV}-\frac38L+\frac{11}{16}\right),
\qquad L=\ln\frac{M_E^2}{\mu_R^2}.
\]
With \(C_{LD}=|y_\ell|^2/M_E^2\), the coefficient of the Pauli-triplet derivative structure is therefore
\[
\boxed{
C_3^{WW,\rm box}
=\left(\frac38\Delta_{\rm UV}-\frac38L+\frac{11}{16}\right)
\frac{g_2^2}{16\pi^2}C_{LD}.
}
\]
The \(O(\epsilon)\) angular terms have been retained against the UV pole. The earlier \(+3/(4M_E^2)\) result from the common-numerator diagnostic is superseded and must not be used.

Using the EOM projection in Section 3 gives the following four-box-only current-basis terms:
\[
\boxed{
\Delta C_{HL}^{(1)}\big|_{WW,\rm box}
=-\left(\frac{9}{32}\Delta_{\rm UV}
-\frac{9}{32}L+\frac{33}{64}\right)
\frac{g_2^2}{16\pi^2}C_{LD},
}
\]
\[
\boxed{
\Delta C_{HL}^{(3)}\big|_{WW,\rm box}
=+\left(\frac{3}{32}\Delta_{\rm UV}
-\frac{3}{32}L+\frac{11}{64}\right)
\frac{g_2^2}{16\pi^2}C_{LD}.
}
\]
The accompanying redundant source coefficients are
\[
\Delta C_{E_L^{(1)}}=+\frac34C_3^{WW,\rm box},
\qquad
\Delta C_{E_L^{(3)}}=-\frac14C_3^{WW,\rm box}.
\]

At the matching scale \(L=0\), after separating the displayed \(\overline{\rm MS}\) pole, the finite four-box-only pieces are
\[
\Delta C_{HL}^{(1)}\big|_{\rm finite}
=-\frac{33}{64}\frac{g_2^2}{16\pi^2}C_{LD},
\qquad
\Delta C_{HL}^{(3)}\big|_{\rm finite}
=+\frac{11}{64}\frac{g_2^2}{16\pi^2}C_{LD}
\]
in the Pauli-current normalization.

These remain the EOM/current-basis images of the four-cross-box subset only. The UV pole and matching logarithm must be combined with the EFT operator counterterm and the remaining UV/EFT amplitude organization; these are not the complete \(C_{HL}^{(1,3)}\) matching coefficients.
### Pauli versus generator normalization

If the triplet currents are instead defined with \(T^I=\sigma^I/2\), then
\[
O_{HL}^{(3)}[T]=\frac14O_{HL}^{(3)}[\sigma].
\]
The coefficient multiplying the generator-normalized operator is therefore four times the coefficient displayed above:
\[
\Delta C_{HL}^{(3)}[T]
=+\left(\frac38\Delta_{\rm UV}-\frac38L+\frac{11}{16}\right)
\frac{g_2^2}{16\pi^2}C_{LD}.
\]
This is a convention conversion, not an additional physical contribution.

## 6. Exact checks and scope boundary

The companion script and six regression tests check:
1. The full weak-index Pauli reduction, including the total-derivative term.
2. Substitution of the B5-2B1 \(Q_{LD}\) EOM map.
3. The adjoint derivative sign for both \(C^I\) and \(\bar C^I\).
4. The nonzero symmetrized triplet \(W\)-contact term.
5. Equality of that contact with the gauge-field part of the EOM/current identity.
6. The four-box-to-current coefficient factors and Pauli/generator normalization.

The exact symbolic identities pass in independent local SymPy checks. The six regression tests are wired into the research workflow. The latest GitHub Actions run (42904392663) failed before any runner step started (`runner_id=0`, empty step lists); therefore CI has not executed these tests and no CI pass is claimed.

**Still outside this sub-block:** external \(L,H\) LSZ/self-energy contributions; parameter and operator counterterms; the complete EFT insertion set; the summed weak Ward/Slavnov–Taylor identity; \(BB\), \(BA'\), and \(A'A'\) gauge sectors; and the full common-basis anomalous-dimension matrix. The displayed coefficients must not be used as final phenomenological Wilson coefficients until those pieces are combined.
