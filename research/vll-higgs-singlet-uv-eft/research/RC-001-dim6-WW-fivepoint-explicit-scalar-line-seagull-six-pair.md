# RC-001 — Explicit scalar-line plus seagull kernels for all scalar WW endpoints

**Workstream:** RC-001-WW-UV-FF-02, Stage B2c-IVm  
**Status:** the scalar-line insertion and scalar seagull have been combined with their distinct ordered/anticommutator weak tensors, then contracted with the actual opposite endpoint current in the common-\(k\) routing. This gives six explicit scalar endpoint kernels: LD-W-02(B), LD-W-03(S), LD-W-04(S), LD-W-05(A), and both LD-W-06 endpoints. The three oriented scalar WTIs and all three raw-to-decomposed vector identities are checked exactly. The kernels are nonzero at two nonsingular rational points. This is not the complete matter-plus-gauge Slavnov–Taylor sum.

## 1. Weak tensors and the endpoint decomposition

For a scalar endpoint \(X\) and its opposite endpoint \(Y\), the ordered scalar-line tensor and the seagull anticommutator tensor obey
\[
\mathcal W_X^a
=\frac12\mathcal S_X^a+\frac{i}{2}\mathcal G_{\rm orient}^a,
\qquad
\mathcal S_X^a=\mathcal W_X^a+\widetilde{\mathcal W}_X^a.
\]
The explicit raw-index bridges fix
\[
\mathcal S_A^a=\frac12R_B^aT_0,\qquad
\mathcal S_B^a=\frac12R_A^aT_0,\qquad
\mathcal S_S^a=\frac12R_F^aT_0.
\]
For cross-vertex endpoints \(\mathcal G_{\rm orient}=\mathcal G_{AB}\); for the same-vertex \(S\to F\) endpoints it is \(\mathcal G_{FS}\). These tensors are not identified with one another.

Define
\[
\delta_X=\Delta_Y-\Delta_W,\qquad
\Delta_{Y,W}=\frac1{(r_{Y,W})^2}.
\]
The phase-weighted A-side scalar line plus seagull is
\[
\boxed{
\mathcal C_A^\mu
=g_2\left[
\left(-\frac12\delta_A V_A^\mu+\Delta_Yq^\mu\right)
\mathcal S_A^a
-\frac{i}{2}\delta_A V_A^\mu\mathcal G_{AB}^a
\right].
}
\tag{1.1}
\]
For a B-side or same-vertex S-side scalar endpoint,
\[
\boxed{
\mathcal C_{B/S}^\mu
=g_2\left[
\left(+\frac12\delta_{B/S}V_{B/S}^\mu+\Delta_Yq^\mu\right)
\mathcal S_{B/S}^a
+\frac{i}{2}\delta_{B/S}V_{B/S}^\mu
\mathcal G_{\rm orient}^a
\right].
}
\tag{1.2}
\]
These expressions retain the symmetric seagull tensor and antisymmetric commutator tensor separately. The \(\Delta_Yq^\mu\) term is the actual seagull contact; it is not part of \(R_{\rm FG}\).

## 2. Common-\(k\) momentum assignments

Let \(\kappa=k+q\). The common routing from B2c-IVj fixes:

| Endpoint | Pair(s) | \(V_X^\mu\) | \(r_Y\) | \(r_W\) | Internal-W propagator |
|---|---|---|---|---|---|
| A scalar | LD-W-05/06 | \(2p_A^\mu-\kappa^\mu\) | \(k-p_A\) | \(\kappa-p_A\) | \(D(\kappa)\) |
| B scalar | LD-W-02/06 | \(-2p_B^\mu-k^\mu\) | \(\kappa+p_B\) | \(k+p_B\) | \(D(k)\) |
| S scalar | LD-W-03/04 | \(2p_S^\mu-\kappa^\mu\) | \(p_S-k\) | \(p_S-\kappa\) | \(D(\kappa)\) |

For A endpoints, \(r_W-r_Y=q\), and
\[
\frac{q\cdot(r_W+r_Y)}{r_W^2r_Y^2}
=\Delta_Y-\Delta_W.
\]
For B/S endpoints, \(r_Y-r_W=q\), and
\[
\frac{q\cdot(r_W+r_Y)}{r_W^2r_Y^2}
=\Delta_W-\Delta_Y.
\]
The different signs are retained in (1.1) and (1.2).

## 3. Actual contracted kernels

Write \(\slashed{\mathcal C}_X=\gamma_\mu\mathcal C_X^\mu\). The internal-W propagator is included in each expression below; the remaining opposite-endpoint and heavy denominators are listed after the kernels.

### LD-W-02: B-side scalar \(H^\dagger\)

Here \(p_A=p_1\), \(p_B=p_3\), \(X_A=-\slashed r_A\), and the opposite endpoint is fermionic. The B-side scalar current contracts with the A-side gamma current:
\[
\boxed{
\mathcal K_{02,B}
=\frac{\slashed{\mathcal C}_B\,(-\slashed r_A)\slashed h}{k^2},
\quad
r_A=k-p_1,\quad h=k-p_1-p_2.
}
\tag{3.1}
\]
The remaining denominator is \(r_A^2(h^2-M_E^2)\); \(\Delta_Y,\Delta_W\) are already inside \(\mathcal C_B\).

### LD-W-05: A-side scalar \(H\)

Here \(p_A=p_2\), \(p_B=p_4\), and the opposite endpoint is the B-side fermion:
\[
\boxed{
\mathcal K_{05,A}
=\frac{\slashed h\slashed r_B^Y\slashed{\mathcal C}_A}{\kappa^2},
\qquad r_B^Y=\kappa+p_4.
}
\tag{3.2}
\]
The remaining denominator is \((r_B^Y)^2(h^2-M_E^2)\).

### LD-W-06: two distinct scalar endpoints

The A-side and B-side seagulls are separate graphs with different weak tensors and different W momenta:
\[
\boxed{
\mathcal K_{06,A}
=\frac{\slashed h\,(V_B\cdot\mathcal C_A)}{\kappa^2},
\qquad V_B=-2p_3-\kappa,
}
\tag{3.3}
\]
\[
\boxed{
\mathcal K_{06,B}
=\frac{(V_A\cdot\mathcal C_B)\slashed h}{k^2},
\qquad V_A=2p_2-k.
}
\tag{3.4}
\]
The first carries \(\mathcal S_A,\mathcal G_{AB}\); the second carries \(\mathcal S_B,\mathcal G_{AB}\). They must not be combined by replacing both with one common scalar tensor.

### LD-W-03: same-vertex S-side scalar

The seed ordering is \(\gamma_\mu\slashed r_F V_S^\mu\). Therefore the scalar endpoint current contracts to the left of the shifted fermion numerator:
\[
\boxed{
\mathcal K_{03,S}
=\frac{\slashed{\mathcal C}_S\slashed r_F^Y}{\kappa^2},
\qquad r_F^Y=k+p_1+q.
}
\tag{3.5}
\]

### LD-W-04: conjugate same-vertex S-side scalar

The conjugate seed ordering is \(V_S^\mu\slashed r_F\gamma_\mu\), so
\[
\boxed{
\mathcal K_{04,S}
=\frac{\slashed r_F^Y\slashed{\mathcal C}_S}{\kappa^2},
\qquad r_F^Y=k+p_4+q.
}
\tag{3.6}
\]
The order in (3.5) and (3.6) is fixed by the corresponding Dirac-Hermitian seed orientation. The same-vertex heavy factor \(S_E(h_E)\), \(h_E=p_F+p_S+q\), remains a spectator on the appropriate side of the loop form factor; it is not included in \(\mathcal K_{03,S}\) or \(\mathcal K_{04,S}\).

There is no scalar endpoint in LD-W-01.

## 4. Exact checks and reproduction

The exact source
\[
\texttt{calculations/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.py}
\]
performs three checks:
1. compares the raw ordered scalar-line plus seagull expressions against the decomposed \(\mathcal S_X/\mathcal G_{\rm orient}\) expressions: 12/12 Lorentz-component identities;
2. checks the A, B, and same-vertex S scalar propagator WTIs with their correct opposite orientations: 3/3;
3. contracts all six actual scalar endpoints with the opposite F/S current at two exact rational momentum points, checking every scalar/W/heavy denominator is nonsingular and every resulting Dirac kernel is nonzero.

The test points use \(M_E^2=400\) only as a nonsingular diagnostic input, not as a physical benchmark. Reproduction:
- source: \`calculations/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.py\`
- tests: \`calculations/test_RC001_dim6_WW_fivepoint_explicit_scalar_line_seagull_six_pair.py\`
- output: \`validation/RC-001-dim6-WW-fivepoint-explicit-scalar-line-seagull-six-pair.txt\`

These are exact local SymPy rational/symbolic checks, not a GitHub Actions result.

## 5. Interpretation and remaining boundary

This stage closes the **explicit ordinary scalar endpoint kernels**. It does not show that their sum vanishes. In particular:
- the \(\mathcal S_X\) symmetric terms must be combined with the relevant Yukawa-endpoint and external-field Ward terms;
- the \(\mathcal G_{AB}\) and \(\mathcal G_{FS}\) terms must be combined with the corresponding three-W group phases and the already-derived \(R_{\rm FG}\) current kernels;
- the gauge-fixing/ghost Slavnov–Taylor completion remains separate;
- external-leg/LSZ and parameter/operator counterterms are not included;
- no loop integration, UV–EFT soft subtraction, or Wilson coefficient is extracted.

The next step is a single common-\(k\) assembly ledger containing (i) the four fermion-line endpoint WTI terms, (ii) these six scalar-line/seagull kernels, (iii) the six three-W terms with \(D(k)-D(\kappa)+R_{\rm FG}\), and (iv) the correct weak tensors/phases. Only after this ordinary-matter integrand is assembled should the BRST/ghost STI terms be added.
