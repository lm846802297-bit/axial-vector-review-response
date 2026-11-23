# RC-001 — Exact endpoint-current projection of the Feynman-gauge remainder

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVk  
**Status:** the nonzero Feynman-gauge remainder left by the common-\(k\) matter-line/three-W transverse-kernel cancellation has been reduced to scalar contractions of the two endpoint currents. This makes the condition for its vanishing explicit. No transversality condition is assumed for the off-shell UV five-point currents.

## 1. Starting point

The B2c-IVh result leaves
\[
R_{\rm FG}^{\mu\nu}(k,q)
=\frac{k^\mu k^\nu-(k+q)^\mu(k+q)^\nu}
{k^2(k+q)^2}.
\]
For arbitrary left and right endpoint currents \(J_L^\mu\) and \(J_R^\nu\),
\[
\mathcal R[J_L,J_R]
=J_{L\mu}R_{\rm FG}^{\mu\nu}J_{R\nu}.
\]
Define the four scalar contractions
\[
X=J_L\cdot k,\qquad U=J_L\cdot q,\qquad
Y=J_R\cdot k,\qquad V=J_R\cdot q.
\]
Since \(J_R\cdot(k+q)=Y+V\) and \(J_L\cdot(k+q)=X+U\), the exact result is
\[
\boxed{
\mathcal R[J_L,J_R]
=\frac{XY-(X+U)(Y+V)}{k^2(k+q)^2}
=-\frac{XV+UY+UV}{k^2(k+q)^2}.
}
\tag{1.1}
\]
This identity is valid for vector currents and, componentwise, for matrix-valued Dirac currents, provided their order is retained.

## 2. What would make the remainder vanish?

A sufficient condition is
\[
J_L\cdot k=0,\qquad J_R\cdot(k+q)=0.
\]
Then both terms in the first numerator of (1.1) vanish. This is a sufficient condition, not a necessary one; accidental cancellations between \(X,V,U,Y\) are also possible.

Crucially, this condition is **not** established for the off-shell matter currents in the present matching problem. The internal W endpoints are attached to Yukawa-connected fermion/scalar lines, not to separately conserved on-shell external currents. One cannot set \(R_{\rm FG}\) to zero by invoking current conservation without deriving the relevant off-shell Slavnov–Taylor identity and including its inverse-propagator, ghost and gauge-fixing terms.

## 3. Rational nonzero diagnostic

At
\[
k=(3,2,0,0),\quad q=(1,0,1,0),\quad
J_L=(1,0,0,0),\quad J_R=(0,1,0,0),
\]
using the mostly-minus metric,
\[
k^2=5,\qquad(k+q)^2=11,
\]
\[
J_L\cdot k=3,\quad J_R\cdot k=-2,\quad
J_L\cdot(k+q)=4,\quad J_R\cdot(k+q)=-2.
\]
Consequently,
\[
\boxed{\mathcal R[J_L,J_R]=\frac{(-6)-(-8)}{55}
=\frac2{55}\ne0.}
\]
This confirms that the remainder is not annihilated by a generic pair of endpoint currents.

## 4. Reproduction

- Exact source: calculations/RC-001-dim6-WW-fivepoint-RFG-current-projection.py
- Captured output: validation/RC-001-dim6-WW-fivepoint-RFG-current-projection.txt

The exact SymPy audit checks the algebraic reduction (1.1), the sufficient transversality condition, and the nonzero rational diagnostic. It is a local symbolic calculation, not a GitHub Actions result or a FeynArts/FeynCalc run.

## 5. Consequence for the six-pair calculation

The B2c-IVh universal current result should now be read as
\[
\mathcal M_{\rm line+3W}^{\rm long}
=\begin{cases}
-ig_2\mathcal G_{AB}^a\,
J_A^\mu R_{{\rm FG},\mu\nu}J_B^\nu,
& A\to B,\\[2mm]
+ig_2\mathcal G_{FS}^a\,
J_S^\mu R_{{\rm FG},\mu\nu}J_F^\nu,
& S\to F.
\end{cases}
\]
The transverse inverse-kernel difference has canceled, but the displayed current projection remains. It must be combined with the complete gauge-fixing/ghost Slavnov–Taylor sector and the off-shell external-leg terms. It is not an independently physical residual interaction and must not be used as a matching coefficient.

The next calculation is to insert the actual pair-dependent endpoint currents and spectator/heavy factors for LD-W-01…06 into (1.1), preserving the matrix order for the F–F and F–S cases and the derivative-current signs for the S endpoints. The scalar seagull anticommutator terms remain a separate contribution. Only after these explicit currents and the complete STI terms are assembled can one decide whether the conventional Feynman-gauge remainder cancels in the full Green function.
