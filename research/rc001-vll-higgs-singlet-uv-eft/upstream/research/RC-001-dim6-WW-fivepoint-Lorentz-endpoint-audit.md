# RC-001 — UV five-point Lorentz endpoint audit: fermion lines, scalar seagulls, and the three-W chain

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVc  
**Status:** the Lorentz contractions of both oriented fermion-line insertions and both scalar-line insertions, the scalar seagull metric contraction, the bare three-W vertex, and the Feynman-gauge propagator chain have been checked exactly. The scalar-line and seagull Lorentz factors are kept separate: their weak tensors differ, as shown by the subsequent raw-index bridge. This is an exact **Lorentz endpoint audit**, not the full weak-index/phase-weighted 24-graph sum. No cancellation of the matter-line terms against the three-W graph is claimed.

## 1. Fixed routing variables and scope

Retain the external-W routing used in the Stage-B2c numerator templates:
\[
r_A^W=r_A,\qquad r_A^Y=r_A-q,
\]
\[
r_B^W=r_B,\qquad r_B^Y=r_B+q.
\]
Define
\[
\Delta(r)=\frac1{r^2},\qquad
G_F(r)=\frac{\slashed r}{r^2}.
\]
The labels \(W,Y\) refer to the two segments adjacent to the internal-W and Yukawa ends, respectively. The A and B line orientations are opposite.

The present audit factors out the common four-point skeleton and checks the Lorentz endpoint functions. It does not independently regenerate every weak-index matrix product, every external momentum-conservation equation, or every heavy propagator denominator in the five-point diagrams. Those remain separate inputs to the complete graph sum.

## 2. Fermion-line longitudinal contractions

For the A orientation, the stripped numerator is
\[
N_{A,F}^\alpha
=(-\slashed r_A^W)\gamma^\alpha(-\slashed r_A^Y).
\]
Using \(r_A^W-r_A^Y=q\),
\[
\frac{q_\alpha N_{A,F}^\alpha}
{(r_A^W)^2(r_A^Y)^2}
=
\frac{\slashed r_A^Y}{(r_A^Y)^2}
-\frac{\slashed r_A^W}{(r_A^W)^2}.
\]
Thus
\[
\boxed{
\mathcal W_{A,F}
=G_F(r_A^Y)-G_F(r_A^W).
}
\tag{2.1}
\]

For the B orientation,
\[
N_{B,F}^\alpha
=\slashed r_B^Y\gamma^\alpha\slashed r_B^W,
\]
and \(r_B^Y-r_B^W=q\) gives
\[
\boxed{
\mathcal W_{B,F}
=G_F(r_B^W)-G_F(r_B^Y).
}
\tag{2.2}
\]
Both identities are exact off shell. The numerator/denominator identities are checked as \(4\times4\) Dirac-matrix identities for generic symbolic \(r,q\), not only at the exceptional local projection.

When restoring the chiral projectors, use the oriented propagator WTIs from Stage B2c-I/II. Equations (2.1)–(2.2) display the reduced numerator functions after the common chiral chain has been factored out.

## 3. Scalar-line WTI and the separate seagull Lorentz factor

For the scalar-line numerators used in the fixed routing,
\[
q\cdot(r_A^W+r_A^Y)
=(r_A^W)^2-(r_A^Y)^2,
\]
\[
q\cdot(r_B^W+r_B^Y)
=(r_B^Y)^2-(r_B^W)^2.
\]
Therefore the ordinary scalar-line insertions reduce to
\[
\boxed{
q_\alpha N_{A,S}^{\alpha}
\longrightarrow
\Delta(r_A^Y)-\Delta(r_A^W),
}
\tag{3.1}
\]
\[
\boxed{
q_\alpha N_{B,S}^{\alpha}
\longrightarrow
\Delta(r_B^W)-\Delta(r_B^Y).
}
\tag{3.2}
\]
These are stripped propagator-difference identities. The phase-weighted scalar-line graphs still carry their own ordered weak tensors, \(\mathcal W_A^a\) or \(\mathcal W_B^a\).

The two-gauge scalar seagull has Lorentz vertex proportional to \(g^{\alpha\mu}\), where \(\alpha\) is the external-W index and \(\mu\) is the internal-W index. Its longitudinal contraction is
\[
q_\alpha g^{\alpha\mu}=q^\mu.
\]
It therefore supplies a separate \(q^\mu\Delta(r_{\rm sg})\) numerator, with the scalar propagator and spectator factors fixed by the B1 routing. The seagull weak tensor is an anticommutator, not the same ordered tensor as the ordinary scalar-line graph. The exact raw-index result is recorded in
research/RC-001-dim6-WW-cross-vertex-raw-weak-index-bridge.md:
\[
\mathcal S_A^a=\mathcal W_A^a+\widetilde{\mathcal W}_A^a,
\qquad
\mathcal S_B^a=\mathcal W_B^a+\widetilde{\mathcal W}_B^a.
\]
Consequently the scalar-line and seagull pieces must not be combined into one stripped Lorentz vector with a common weak tensor. The full weak-index-weighted combination remains part of the B2c-IV integrand sum.

## 4. Three-W contraction and the Feynman-gauge remainder

For all incoming momenta \((q,k,-k-q)\), define
\[
\Gamma_{\alpha\mu\nu}
=g_{\alpha\mu}(q-k)_\nu
+g_{\mu\nu}(2k+q)_\alpha
+g_{\nu\alpha}(-k-2q)_\mu.
\]
Then
\[
\boxed{
q^\alpha\Gamma_{\alpha\mu\nu}
=\mathcal K_{\mu\nu}(k+q)-\mathcal K_{\mu\nu}(k),
}
\tag{4.1}
\]
where
\[
\mathcal K_{\mu\nu}(k)=k^2g_{\mu\nu}-k_\mu k_\nu.
\]

For clarity, the index positions in the Feynman-gauge chain are
\[
D^{\mu\alpha}(k+q)
\left[\mathcal K_{\alpha\beta}(k+q)-\mathcal K_{\alpha\beta}(k)\right]
D^{\beta\nu}(k),
\qquad
D^{\mu\nu}(k)=\frac{g^{\mu\nu}}{k^2}.
\]
The exact decomposition is
\[
\boxed{
D^{\mu\alpha}(k+q)\Delta\mathcal K_{\alpha\beta}D^{\beta\nu}(k)
=
D^{\mu\nu}(k)-D^{\mu\nu}(k+q)
+R_{\rm FG}^{\mu\nu},
}
\tag{4.2}
\]
with
\[
\boxed{
R_{\rm FG}^{\mu\nu}
=\frac{k^\mu k^\nu-(k+q)^\mu(k+q)^\nu}
{k^2(k+q)^2}.
}
\tag{4.3}
\]
The remainder is generically nonzero. For example, with metric signature \(+---\), \(k=(3,2,0,0)\) and \(q=(1,0,1,0)\),
\[
R_{\rm FG}^{\mu\nu}
=\frac1{55}
\begin{pmatrix}
-7&-2&-4&0\\
-2&0&-2&0\\
-4&-2&-1&0\\
0&0&0&0
\end{pmatrix}.
\]
This numerical point is only a non-vanishing diagnostic; the symbolic matrix identity (4.2) is the actual check.

Do not drop \(R_{\rm FG}\), and do not identify it by itself with a ghost-loop contribution. It is the remainder generated when the transverse Yang–Mills inverse kernel is sandwiched between ordinary Feynman-gauge propagators. Its role must be settled in the full gauge-fixing/Slavnov–Taylor bookkeeping.

## 5. Six-pair Lorentz endpoint census

The attachment classes map to the following line types:

| Pair | A endpoint | B endpoint | Matter-line insertions | Scalar seagulls | Three-W |
|---|---|---|---:|---:|---:|
| LD-W-01 | F | F | 2 | 0 | 1 |
| LD-W-02 | F | S | 2 | 1 (B) | 1 |
| LD-W-03 | F | S | 2 | 1 (B) | 1 |
| LD-W-04 | S | F | 2 | 1 (A) | 1 |
| LD-W-05 | S | F | 2 | 1 (A) | 1 |
| LD-W-06 | S | S | 2 | 2 (A and B) | 1 |
| **Total** |  |  | **12** | **6** | **6** |

Here F denotes a fermion endpoint and S a scalar endpoint. The table reproduces the 24 internal attachment topologies in the existing census:
\[
12\text{ matter-line insertions}
+6\text{ scalar seagulls}
+6\text{ three-W insertions}=24.
\]
This is a topology count, not a FeynArts/QGRAF-generated diagram count.

For a cross-vertex pair, the Lorentz endpoint factors (2.1)–(3.4) multiply the appropriate heavy-line numerator and the opposite endpoint current. The three-W term multiplies the two internal-W propagators and the shifted matter current at the second W endpoint. For LD-W-03/04, the heavy propagator is a spectator external-channel propagator in the four-point seed; its momentum in each five-point attachment must be fixed by the actual all-incoming momentum conservation at the corresponding Yukawa vertex.

## 6. Same-vertex momentum routing is already checked in B1

For LD-W-03/04, the four-point seed has
\[
r_F=k+p_F,\qquad r_S=p_S-k,\qquad
P_{FS}=p_F+p_S.
\]
The original B1 routing audit explicitly assigns the external-W insertions on the fermion line, scalar line, internal-W line, and scalar seagull. In each case the momentum entering the Yukawa vertex is shifted so that
\[
\boxed{P_E=P_{FS}+q.}
\]
The vertex momentum-conservation equations for these four attachment types are included in
calculations/RC-001-dim6-WW-UV-fivepoint-routing-Ward-numerators.py
and were checked together with the cross-vertex routes (24/24).

Thus the same-vertex heavy-channel shift is **not an unresolved momentum-routing gate**. The present Lorentz endpoint script does not independently rederive those equations, but the B1 route record already validates them. The remaining same-vertex issue is the raw weak-index matrix order for the \(S\to F\) internal-W orientation, not the heavy denominator assignment.

## 7. Reproduction and evidence boundary

The exact local audit is in
calculations/RC-001-dim6-WW-fivepoint-Lorentz-endpoint-audit.py
with captured output in
validation/RC-001-dim6-WW-fivepoint-Lorentz-endpoint-audit.txt.

It checks:
- A/B fermion numerator differences: 16/16 Dirac components each;
- A/B scalar propagator differences: 2/2;
- A/B scalar-line propagator-difference identities: 2/2;
- scalar seagull metric contraction (q_alpha g^{\alpha\mu}=q^\mu): 4/4 Lorentz components;
- three-W contraction: 16/16 Lorentz components;
- Feynman-gauge propagator chain including \(R_{\rm FG}\): 16/16 components;
- non-vanishing of \(R_{\rm FG}\) at a generic rational diagnostic point;
- six-pair topology census: 12+6+6=24.

This does **not** establish:
1. the Lorentz-weighted sum of the matter-line commutator pieces with the three-W graph;
2. cancellation of \(D(k)-D(k+q)\) against the shifted matter endpoint terms after a common loop-momentum routing;
3. the complete scalar-line/seagull/three-W sum for each pair;
4. the gauge-fixing/ghost Slavnov–Taylor completion;
5. external-leg/LSZ and counterterm completion;
6. any integrated five-point hard coefficient or transverse form factor.

The raw weak-index ordering and relative phase factors for all 24 direct attachments are recorded in the cross-vertex and same-vertex bridge notes. The common-\(k\) transverse-kernel cancellation has now been checked for all six pair classes, and the B1 momentum shifts have been explicitly matched for all 12 Yukawa endpoints and six scalar seagulls. See \`research/RC-001-dim6-WW-fivepoint-common-k-lorentz-kernel.md\` and \`research/RC-001-dim6-WW-fivepoint-common-k-shift-maps.md\`. The remaining task is to insert the explicit pair-dependent current numerators and heavy propagators, combine the scalar seagulls with their distinct weak tensors, and complete the external-leg/LSZ and ghost/gauge-fixing Slavnov–Taylor terms. Keep the nonzero \(R_{\rm FG}\) explicit. Only after the complete UV–EFT integrand identity closes should the five-point hard/soft subtraction be evaluated.