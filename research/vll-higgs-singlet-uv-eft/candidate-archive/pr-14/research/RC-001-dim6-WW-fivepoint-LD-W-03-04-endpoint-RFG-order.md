# RC-001 — LD-W-03/04 same-vertex WTI endpoint and \(R_{\rm FG}\) ordering

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVn-h/08  
**Baseline:** PR #11 merge commit \`6909feccb58b9e4b79da72f3a6af96a47edb3e10\`  
**Status:** local exact Dirac-algebra audit completed for the two same-vertex orientations. The WTI endpoint chains reduce to explicit, distinct chiral matrix orders; their Dirac-Hermitian relation is checked. The pair-specific two-W \(R_{\rm FG}\) numerators remain separate. This is not a cancellation or a complete longitudinal identity.

## 1. Fixed routing and conventions

Use \(\kappa=k+q\), \(r_F^W=k+p_F\), \(r_F^Y=k+p_F+q\), and
\[
V_S=2p_S-\kappa,\qquad h_E=p_F+p_S+q.
\]
The metric is \((+---)\), \(P_{L,R}=(1\mp\gamma_5)/2\), and the Dirac representation and \(\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3\) are explicit in the source. The \(h_E\) propagator is a \(k\)-independent spectator and is not folded into the loop-side \(R_{\rm FG}\) kernel.

## 2. Actual WTI endpoint reductions

For LD-W-03 the open-line WTI is
\[
S_F(r_F^W)\slashed qP_LS_F(r_F^Y)
=S_F(r_F^W)P_R-P_LS_F(r_F^Y).
\]
After contracting the internal W index with the scalar current and retaining the seed order \(\gamma_\mu(\cdots)V_S^\mu\), the two numerator endpoints reduce to
\[
\boxed{\mathcal E_{03,W}=\slashed V_S\slashed r_F^W P_R,\qquad
\mathcal E_{03,Y}=-\slashed V_S\slashed r_F^Y P_R.}
\]

For the Dirac-Hermitian-conjugate LD-W-04 orientation,
\[
S_F(r_F^Y)\slashed qP_LS_F(r_F^W)
=P_LS_F(r_F^W)-S_F(r_F^Y)P_R.
\]
The ordered contraction \(V_S^\mu(\cdots)\gamma_\mu\) gives
\[
\boxed{\mathcal E_{04,W}=\slashed r_F^W\slashed V_S P_L,\qquad
\mathcal E_{04,Y}=-\slashed r_F^Y\slashed V_S P_L.}
\]
The two formula pairs obey \(\overline{\mathcal E_{03,W}}=\mathcal E_{04,W}\) and \(\overline{\mathcal E_{03,Y}}=\mathcal E_{04,Y}\). The opposite chiral projector and reversed gamma order are retained; replacing both orientations by one common chain would be incorrect.

## 3. Pair-specific two-W remainder

The \(R_{\rm FG}\) numerators from the actual same-vertex currents are
\[
\mathcal N_{03}^{\rm FG}
=(V_S\!\cdot k)\slashed k\slashed r_F^Y
-(V_S\!\cdot\kappa)\slashed\kappa\slashed r_F^Y,
\]
\[
\mathcal N_{04}^{\rm FG}
=(V_S\!\cdot k)\slashed r_F^Y\slashed k
-(V_S\!\cdot\kappa)\slashed r_F^Y\slashed\kappa.
\]
The exact symbolic and rational-point checks show that neither single-W endpoint is equal to the pair-specific two-W remainder. They must enter the complete common-\(k\) sum with their own propagator denominators, scalar-line/seagull terms, weak tensors, and orientation phases.

## 4. Exact rational-point diagnostic

At
\[
\begin{aligned}
k&=(4,1,2,1),&q&=(1,2,0,1),\\
p_1&=(1,0,1,0),&p_2&=(0,1,0,2),\\
p_3&=(2,1,1,1),&p_4&=(-4,-4,-2,-4),
\end{aligned}
\]
with \(M_E^2=400\), the nonzero denominator factors are
\[
\begin{array}{c|ccccc}
 &k^2&\kappa^2&(r_F^Y)^2&r_S^2&h_E^2-M_E^2\\\hline
03&10&8&14&11&-415\\
04&10&8&-4&3&-405
\end{array}
\]
The numbers of nonzero entries in the \(4\times4\) endpoint matrices \((\mathcal E_W,\mathcal E_Y,\mathcal N^{\rm FG})\) are \(16,16,16\) for LD-W-03 and \(8,8,16\) for LD-W-04. All three matrices are pairwise distinct in each orientation. The exact source also checks all 32 derivatives \(\partial h_E^\mu/\partial k^\nu=0\).

## 5. Reproduction and evidence boundary

- Source: \`calculations/RC-001-dim6-WW-fivepoint-LD-W-03-04-endpoint-RFG-order.py\`
- Test: \`calculations/test_RC001_dim6_WW_fivepoint_LD_W_03_04_endpoint_RFG_order.py\`
- Output: \`validation/RC-001-dim6-WW-fivepoint-LD-W-03-04-endpoint-RFG-order.txt\`

Execution provenance: Python 3.13.5 and SymPy 1.14.0 were used in the current analysis runtime to independently transcribe and evaluate the six symbolic endpoint/conjugation identities, the rational-point matrices, denominator values, and spectator derivatives. The committed calculation entry point and standalone unittest file have not yet been executed from their repository paths. No GitHub Actions or independent diagram-package pass is claimed.

This does not combine the WTI endpoints with scalar-line/seagull kernels, the three-W phase-weighted term, reducible LSZ factors, gauge-fixing/ghost contributions, or counterterms. No loop integration, UV–EFT subtraction, transverse form factor, or Wilson coefficient is claimed.
