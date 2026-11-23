# RC-001 — Same-vertex fermion-line WTI for LD-W-03/04

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-a  
**Status:** the previously implicit fermion-line Ward contractions in the two same-vertex triangles are now derived from their actual \(N_{03}\) and \(N_{04}\) Dirac-Hermitian orientations. The two open-line WTIs, the q-contracted insertion conjugation, the seed conjugation, the common-\(k\) momentum shift, and the \(k\)-independence of the heavy spectator are checked exactly. This closes the same-vertex fermion-line WTI input; it does not close the full same-vertex graph sum.

## 1. Fixed same-vertex routing

For either LD-W-03 or LD-W-04, write
\[
r_F^W=k+p_F,\qquad r_F^Y=k+p_F+q,
\qquad r_F^Y-r_F^W=q.
\]
The heavy channel is
\[
h_E=p_F+p_S+q,
\]
which is independent of the loop momentum \(k\). The heavy propagator remains an external-channel spectator and is not absorbed into the loop-side WTI.

The seed numerator orientations are
\[
N_{03}=\gamma_\mu\slashed r_F^W V_S^\mu,
\qquad
N_{04}=V_S^\mu\slashed r_F^W\gamma_\mu,
\]
where \(V_S^\mu\) is the scalar current with the actual \(H\) or \(H^\dagger\) field orientation. The second expression is the Dirac-Hermitian conjugate orientation of the first.

## 2. LD-W-03: left-vertex orientation

The external-W insertion lies between the internal-W endpoint and the Yukawa-side fermion propagator. Its contracted open-line chain is
\[
S_F(r_F^W)\slashed q P_L S_F(r_F^Y).
\]
Since \(r_F^Y=r_F^W+q\), the exact off-shell identity is
\[
\boxed{
S_F(r_F^W)\slashed q P_L S_F(r_F^Y)
=S_F(r_F^W)P_R-P_LS_F(r_F^Y).
}
\tag{2.1}
\]
Here \(S_F(r)=\slashed r/r^2\). No on-shell equation is used.

The corresponding full chain retains the seed ordering:
\[
\gamma_\mu
\left[S_F(r_F^W)P_R-P_LS_F(r_F^Y)\right]
V_S^\mu,
\]
with the heavy spectator \(S_E(h_E)\) attached on the same side as in the original left-vertex amplitude.

## 3. LD-W-04: Dirac-Hermitian-conjugate orientation

The conjugate open-line order is reversed:
\[
S_F(r_F^Y)\slashed q P_L S_F(r_F^W).
\]
Its exact identity is
\[
\boxed{
S_F(r_F^Y)\slashed q P_L S_F(r_F^W)
=P_LS_F(r_F^W)-S_F(r_F^Y)P_R.
}
\tag{3.1}
\]
The full chain is therefore
\[
V_S^\mu
\left[P_LS_F(r_F^W)-S_F(r_F^Y)P_R\right]
\gamma_\mu,
\]
with the heavy spectator in the conjugate seed orientation. Equations (2.1) and (3.1) must not be interchanged: the location of \(P_L/P_R\) and the order of the propagators are different.

## 4. Conjugation and common-\(k\) checks

The q-contracted insertion numerators are
\[
N_{03,q}=\gamma_\mu\slashed r_F^W\slashed q P_L
\slashed r_F^Y V_S^\mu,
\]
\[
N_{04,q}=V_S^\mu\slashed r_F^Y\slashed q P_L
\slashed r_F^W\gamma_\mu.
\]
The exact Dirac-Hermitian relation is
\[
\boxed{\overline{N_{03,q}}=N_{04,q}.}
\]
The same relation holds for the q-independent seed numerators.

The common-\(k\) shift-map input is unchanged:
\[
r_F^Y=r_F^W+q,\qquad h_E=p_F+p_S+q,\qquad
\frac{\partial h_E}{\partial k^\mu}=0.
\]
Thus the fermion WTI is now fixed without changing the already validated same-vertex heavy-channel routing.

## 5. Reproduction and evidence boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-same-vertex-fermion-WTI.py\`
- Tests: \`calculations/test_RC001_dim6_WW_fivepoint_same_vertex_fermion_WTI.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-same-vertex-fermion-WTI.txt\`

The local exact SymPy audit checks:
- LD-W-03 and LD-W-04 open-line WTIs: 32/32 Dirac components;
- q-contracted insertion and seed Dirac-Hermitian conjugation: 32/32 components;
- common-\(k\) fermion momentum relation: 4/4 vector components;
- heavy-channel spectator \(k\)-independence: 16/16 derivatives.

This is not a GitHub Actions result or a FeynArts/FeynCalc run.

## 6. What remains

This closes the missing same-vertex fermion-line WTI input. It does not yet combine:
1. the two endpoint terms in (2.1)/(3.1) with the local Yukawa-singlet gauge variations;
2. the scalar-line/seagull kernels from B2c-IVm;
3. the same-vertex three-W contribution with its reversed \(S\to F\) group phase and \(R_{\rm FG}\);
4. the external-leg/LSZ, ghost/gauge-fixing, and counterterm sectors.

The next step is to assemble the ordinary-matter common-\(k\) longitudinal integrand for each of the six pair classes, preserving these same-vertex WTI orientations and the spectator heavy propagator. No loop integration or Wilson coefficient should be attempted until that assembly is explicit.
