# RC-001 — Same-Yukawa-vertex pure-WW subgraphs in nonexceptional matching

**Status:** the two same-vertex attachment classes LD-W-03 and LD-W-04 are shown to be pure-soft at \(O(M_E^{-2})\). Their light-loop form factors are reproduced by the tree \(Q_{LD}\) insertion; their hard-region loop integrals are scaleless. No finite hard Wilson coefficient arises from these two subgraphs at this order. The complete six-pair \(WW\) amplitude and Ward/counterterm sum remain open.

## 1. External ordering and momentum routing

Use the ordered Green function
\[
\bar L(p_1),\quad H(p_2),\quad H^\dagger(p_3),\quad L(p_4),
\qquad p_1+p_2+p_3+p_4=0,
\]
with all momenta incoming. Define
\[
P=p_1+p_2=-(p_3+p_4).
\]

For LD-W-03, the W joins \(\bar L\) and \(H\) attached to the same left Yukawa vertex. Choose W momentum \(k\). The light denominators are
\[
D_{03}=k^2(k+p_1)^2(k-p_2)^2.
\]
A stripped numerator chain is
\[
N_{03}=
\gamma_\mu(\slashed k+\slashed p_1)(2p_2-k)^\mu.
\]
The common overall Feynman-rule phase, gauge coupling, Yukawa factors and the weak generator are kept outside this stripped expression.

For LD-W-04, the W joins \(L\) and \(H^\dagger\) at the conjugate right Yukawa vertex. The corresponding light denominators and a consistent conjugate ordering are
\[
D_{04}=k^2(k+p_4)^2(k-p_3)^2,
\qquad
N_{04}=(2p_3-k)_\mu(\slashed k+\slashed p_4)\gamma^\mu.
\]

In both cases, the heavy propagator carries only the external channel momentum \(P\) (or \(-P\) at the conjugate vertex). It does not carry the W-loop momentum \(k\).

## 2. Chiral heavy propagator and tree EFT insertion

The Yukawa vertices select the chirality-preserving heavy propagator:
\[
P_R\frac{\slashed P+M_E}{P^2-M_E^2}P_L
=\frac{\slashed P P_L}{P^2-M_E^2}.
\]
The mass numerator vanishes because \(P_RP_L=0\). For \(|P^2|\ll M_E^2\),
\[
P_R\frac{\slashed P+M_E}{P^2-M_E^2}P_L
=-\frac{\slashed P P_L}{M_E^2}
+O(M_E^{-4}).
\]

The tree-level derivative operator has
\[
Q_{LD}=(\bar L H)i\slashed D(H^\dagger L),
\qquad
q_D=p_3+p_4=-P.
\]
Its insertion therefore supplies
\[
\frac{\slashed q_D P_L}{M_E^2}
=-\frac{\slashed P P_L}{M_E^2},
\]
with the same tree matching sign convention \(C_{LD}=|y_\ell|^2/M_E^2\) used in the master ledger.

Consequently the full-theory same-vertex subgraph at leading order in \(1/M_E^2\) is exactly the same light-loop form factor as the EFT \(Q_{LD}\) insertion:
\[
\mathcal M^{\rm UV}_{03,04}
\big|_{M_E^{-2}}
=
\mathcal M^{\rm EFT}_{03,04},
\]
provided the same external-field, gauge-fixing and loop-momentum conventions are used. This is an integrand-level factorization identity; it does not require evaluating the finite massless triangle.

## 3. UV numerator and the common light-loop pole

At large \(k\), the two stripped numerator chains obey
\[
N_{03}=-k^2\mathbf 1+O(kp,p^2),
\qquad
N_{04}=-k^2\mathbf 1+O(kp,p^2),
\]
using \(\gamma_\mu\slashed k k^\mu=\slashed k\slashed k=k^2\). Thus each nonexceptional light triangle has the expected logarithmic UV behavior:
\[
\frac{N_{03,04}}{D_{03,04}}
\sim-\frac{\mathbf 1}{(k^2)^2}.
\]
In the stripped Euclidean normalization the leading scalar UV residue is \(-1/(16\pi^2\epsilon_{\rm UV})\), before restoring the common Feynman-rule phase and couplings. The exact overall amplitude sign must be fixed together with the full graph convention; it is not inferred from this stripped numerator alone.

The weak-generator contraction is separately fixed by
\[
LD\text{-}W\text{-}03:\ -\frac34T_0,\qquad
LD\text{-}W\text{-}04:\ -\frac34T_0,
\]
as recorded in research/RC-001-dim6-SU2-attachment-projection.md. These are singlet-tensor contributions, unlike the triplet cross-box classes LD-W-01/02/05/06.

## 4. Hard-region conclusion

There is no \(M_E\)-dependent propagator in either W-loop denominator. The only heavy-scale dependence is the external heavy propagator already expanded as \(-\slashed P/M_E^2\). Therefore the hard-region expansion of the loop integral contains only massless propagators and polynomial external momenta. Its integrals are scaleless in dimensional regularization.

A scaleless hard integral must not be interpreted as having separately vanishing UV and IR poles. The common nonexceptional external momenta regulate the soft amplitude; in a hard-region/R* bookkeeping, retain the UV/IR labels until the full UV-minus-EFT difference is assembled. Since the same light-loop integrand occurs on the EFT side, the soft form factors and their poles cancel in matching.

Hence
\[
\boxed{
\Delta C_{LD}^{WW,\mathrm{same\ vertex}}(M_E^{-2})=0
}
\]
for LD-W-03 and LD-W-04. This is a statement about the hard matching contribution, not about the physical amplitude: both graphs remain necessary in the EFT soft sum, the \(Q_{LD}\) operator renormalization, and the complete Ward identity.

## 5. Reproducibility and boundary

The explicit 4D Clifford/numerator and chiral-projector checks are in:
- calculations/RC-001-dim6-WW-same-vertex-soft-identity.py;
- validation/RC-001-dim6-WW-same-vertex-soft-identity.txt.

The check verifies the leading \(-k^2\mathbf 1\) numerator, the vanishing heavy mass numerator, and \(q_D=-P\). It is an algebraic factorization check, not a full finite triangle integration or a diagram-package run.

Still open:
1. Restore and cross-check the complete Feynman-rule phases and exact multiplicities for the six \(WW\) attachment classes.
2. Include the external-leg, heavy-line, parameter and operator counterterms in one common convention.
3. Evaluate the external-\(W\) five-point form factor, including the EFT triplet-derivative contact.
4. Complete the Slavnov–Taylor sum and common nonredundant operator-basis projection.

The four cross-vertex classes LD-W-01/02/05/06 have their nonexceptional hard/soft pole closure and finite local hard polynomial recorded in research/RC-001-dim6-nonexceptional-matching-kinematics.md §§3.1–3.4. The two same-vertex results here complement that sub-block but do not close the full \(WW\) matching.
