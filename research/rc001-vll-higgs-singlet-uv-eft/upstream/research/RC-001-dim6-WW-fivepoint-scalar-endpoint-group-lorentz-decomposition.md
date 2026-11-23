# RC-001 — Scalar endpoint Lorentz/weak-tensor decomposition and Ward-kernel sign targets

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVg  
**Status:** the scalar-line and seagull pieces are now combined without identifying their weak tensors. The result separates the symmetric seagull tensor from the antisymmetric commutator tensor. It also fixes the distinct Lorentz-kernel sign conditions for the cross-vertex \(A\to B\) and same-vertex \(S\to F\) orientations. This is an algebraic decomposition; the common-loop-momentum Lorentz sum remains open.

## 1. Why the stripped scalar-vector formula was insufficient

For a scalar endpoint, the ordinary scalar-line graph carries one ordered matrix tensor, while the seagull carries the anticommutator:
\[
\mathcal S_X^a=\mathcal W_X^a+\widetilde{\mathcal W}_X^a.
\]
The raw-index bridges establish
\[
\mathcal W_X^a
=\frac12\mathcal S_X^a+\frac{i}{2}\mathcal G_{\rm orient}^a.
\]
Here \(\mathcal G_{\rm orient}\) is the commutator tensor with the endpoint ordering appropriate to that internal-W orientation. Thus the line and seagull contributions cannot be factored into one common weak tensor before their Lorentz numerators are combined.

## 2. A-side scalar endpoint

For the cross-vertex A endpoint, the scalar-line WTI gives
\[
q_\alpha N_{A,S}^\alpha
=\Delta_Y-\Delta_W,
\qquad
\Delta_Y=\frac1{(r_A^Y)^2},\quad
\Delta_W=\frac1{(r_A^W)^2}.
\]
With the relative phases \(P_{\rm line}/P_4=-g_2\) and \(P_{\rm sg}/P_4=+g_2\), the weak-index-weighted contribution is
\[
\mathcal C_A^\mu
=-g_2(\Delta_Y-\Delta_W)V_A^\mu\mathcal W_A^a
+g_2\Delta_Yq^\mu\mathcal S_A^a.
\]
Using
\[
\mathcal W_A^a=\frac12\mathcal S_A^a+\frac{i}{2}\mathcal G_{AB}^a,
\]
one obtains
\[
\boxed{
\mathcal C_A^\mu
=g_2\left[
\left(-\frac12(\Delta_Y-\Delta_W)V_A^\mu
+\Delta_Yq^\mu\right)\mathcal S_A^a
-\frac{i}{2}(\Delta_Y-\Delta_W)V_A^\mu\mathcal G_{AB}^a
\right].
}
\tag{2.1}
\]
The first term is the symmetric scalar/seagull tensor; the second is the antisymmetric commutator tensor.

## 3. B-side or same-vertex S-side scalar endpoint

For a B-side scalar endpoint in a cross-vertex pair, and for the S endpoint in a same-vertex pair, the scalar-line WTI has the reversed propagator difference:
\[
q_\alpha N_{B/S,S}^\alpha
=\Delta_W-\Delta_Y.
\]
After multiplying by the line phase, this gives \(+g_2(\Delta_Y-\Delta_W)\). The corresponding combined expression is
\[
\mathcal C_{B/S}^\mu
=+g_2(\Delta_Y-\Delta_W)V_{B/S}^\mu
\mathcal W_{B/S}^a
+g_2\Delta_Yq^\mu\mathcal S_{B/S}^a.
\]
With
\[
\mathcal W_{B/S}^a
=\frac12\mathcal S_{B/S}^a
+\frac{i}{2}\mathcal G_{\rm orient}^a,
\]
this becomes
\[
\boxed{
\mathcal C_{B/S}^\mu
=g_2\left[
\left(+\frac12(\Delta_Y-\Delta_W)V_{B/S}^\mu
+\Delta_Yq^\mu\right)\mathcal S_{B/S}^a
+\frac{i}{2}(\Delta_Y-\Delta_W)V_{B/S}^\mu
\mathcal G_{\rm orient}^a
\right].
}
\tag{3.1}
\]
For cross-vertex B endpoints, \(\mathcal G_{\rm orient}=\mathcal G_{AB}\). For same-vertex S endpoints, \(\mathcal G_{\rm orient}=\mathcal G_{FS}\). The exact scalar-current vector \(V_{B/S}^\mu\) is taken from the corresponding B1 routing; it must not be copied between the two topologies without checking the momentum orientation.

## 4. Distinct three-W group-phase signs and required Lorentz identities

The matter-line commutator has phase-weighted group factor
\[
-g_2(+i\mathcal G_{\rm orient})=-ig_2\mathcal G_{\rm orient}.
\]

For cross-vertex \(A\to B\),
\[
\mathcal G_{3W}=\mathcal G_{AB},
\qquad
\frac{P_{3W}}{P_4}\mathcal G_{3W}
=-ig_2\mathcal G_{AB}.
\]
The line commutator and three-W group-phase factors have the same sign. If their Lorentz kernels are denoted \(K_{\rm line}\) and \(K_{3W}\), the cancellation condition is
\[
\boxed{K_{\rm line}+K_{3W}=0\qquad(A\to B).}
\]

For same-vertex \(S\to F\),
\[
\mathcal G_{3W}=-\mathcal G_{FS},
\qquad
\frac{P_{3W}}{P_4}\mathcal G_{3W}
=+ig_2\mathcal G_{FS}.
\]
The line commutator and three-W group-phase factors have opposite signs. The corresponding Lorentz cancellation condition is
\[
\boxed{K_{\rm line}-K_{3W}=0\qquad(S\to F).}
\]
These are sign targets for the Lorentz calculation, not claims that either identity has already been verified.

The three-W Lorentz kernel in Feynman gauge remains
\[
D_F(k+q)\big[\mathcal K(k+q)-\mathcal K(k)\big]D_F(k)
=D_F(k)-D_F(k+q)+R_{\rm FG}.
\]
The nonzero \(R_{\rm FG}\) must remain explicit. The matter-line commutator comparison can only be made after all adjacent propagators, shifted heavy denominators and common loop-momentum routings are included.

## 5. Exact reproduction and boundary

The exact symbolic check is in
calculations/RC-001-dim6-WW-fivepoint-scalar-endpoint-group-lorentz-decomposition.py
with output in
validation/RC-001-dim6-WW-fivepoint-scalar-endpoint-group-lorentz-decomposition.txt.

It verifies:
- the A-side scalar line plus seagull decomposition into \(\mathcal S_A\) and \(\mathcal G_{AB}\);
- the B/S-side scalar line plus seagull decomposition into \(\mathcal S_{B/S}\) and the appropriate commutator tensor;
- the cross-vertex same-sign group-phase relation;
- the same-vertex opposite-sign group-phase relation.

It does not perform the common-\(k\) loop-integrand sum, the \(R_{\rm FG}\) gauge-fixing/ghost completion, or the UV–EFT subtraction. No five-point Wilson coefficient is extracted.

## 6. Next calculation

The next step is to construct the Lorentz-weighted integrands for the six pairs using the B1 routes and the completed raw-index ledger. For each scalar endpoint, insert (2.1) or (3.1) with its own \(V^\mu\), \(\Delta_Y\), \(\Delta_W\), and seagull propagator. Then isolate the commutator coefficient and compare it against the corresponding three-W kernel using the orientation-dependent sign targets in §4. Do not integrate until the common-\(k\) longitudinal sum closes.
