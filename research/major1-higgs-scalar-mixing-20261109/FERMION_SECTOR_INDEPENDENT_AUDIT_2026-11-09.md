# Independent algebraic audit of the fermion-sector matrix calculation — 2026-11-09

**PR:** #69  
**Scope:** inspect the structure of the exact-basis one-loop fermion calculation and its automated tests.  
**Status:** the basis transformations and reported internal consistency checks are algebraically coherent. The existing five tests are regression/consistency tests of one implementation; they are not an independent numerical implementation or a complete matching validation.

## 1. Mass basis and vertices

For each \(\ell=\mu,\tau\), the gauge-basis mass matrix is
\[
\mathcal M_\ell=
\begin{pmatrix}
0&y_\ell v_h/\sqrt2\\
\lambda_\ell v_s/\sqrt2&M_{E_\ell}
\end{pmatrix}.
\]
For a real parameter benchmark, an SVD
\[
U_L^T\mathcal M_\ell U_R
=\operatorname{diag}(m_{\ell_1},m_{\ell_2})
\]
is consistent with the code's use of \(U_R=V\), where NumPy returns \(V^T\) as the third SVD output. The scalar vertices transform as
\[
G_h=U_L^T\Gamma_h U_R,\qquad
G_s=U_L^T\Gamma_s U_R,
\]
with
\[
\Gamma_h=\frac1{\sqrt2}
\begin{pmatrix}0&y_\ell\\0&0\end{pmatrix},
\qquad
\Gamma_s=\frac1{\sqrt2}
\begin{pmatrix}0&0\\\lambda_\ell&0\end{pmatrix}.
\]
This correctly retains all four ordered internal mass-state pairs in the loop sum.

## 2. UV and absorptive checks

The script separates the full mass-eigenstate UV coefficients from the light-light EFT bubble coefficients. This is essential: a cancellation of the full-theory off-diagonal derivative pole does not imply that the EFT light-bubble subtraction has no derivative pole. A matching counterterm can therefore be nonzero in the difference.

The positive-semidefinite absorptive matrix is a useful optical-theorem consistency test for the explicitly included \(\mu,\tau\) cuts. The rank-one saturation follows from proportional light-state scalar couplings in this benchmark. It is not a check of the omitted channels or of the full physical width matrix.

The no-double-counting rule is essential: if the explicit \(\mu,\tau\) absorptive loops are retained in the eventual propagator, the same partial widths must be removed from any externally inserted diagonal width.

## 3. What the five tests do and do not establish

The tests establish that the current implementation:
- reproduces the archived \(hs\) absorptive and hard-momentum values;
- gives a positive-semidefinite, rank-one light-cut absorptive matrix at the stated benchmark;
- has the reported diagonal/off-diagonal UV derivative pattern;
- reproduces the recorded full-minus-light field-counterterm pole coefficients;
- gives real hard momentum differences below the heavy thresholds.

The tests do not independently establish:
- the overall sign and normalization of every \(hh,hs,ss\) Feynman rule and loop contribution;
- the full counterterm basis and its relation to the chosen scalar-potential parameters;
- cancellation of all UV poles after adding the complete EFT soft diagrams and counterterms;
- gauge-parameter independence;
- the tadpole/VEV prescription;
- full complex-momentum analytic continuation;
- complex pole positions, residues, or physical line shapes.

A second implementation or a symbolic diagram-level derivation is needed before treating the numerical matrix as independently verified.

## 4. Next calculation gate

The next task is not to add a guessed \(W\), top, Goldstone, or scalar contribution to the existing matrix. Instead:

1. Freeze the gauge, tadpole/VEV, field-renormalization, and scalar-potential counterterm conventions.
2. Derive the general Dirac-fermion two-point function for arbitrary scalar vertices \(G_a,G_b\), including its \(A_0/B_0\) coefficients and UV poles.
3. Independently reproduce the \(hh,hs,ss\) coefficients from the transformed vertices, preferably with a symbolic trace and an independent numerical integration routine.
4. Verify the EFT light-loop subtraction and counterterm signs from the same convention, rather than only testing against hard-coded outputs.
5. Map local mass-pole terms onto the renormalized scalar-potential parameters using the explicit tadpole/VEV conditions.
6. Only after the fermion-sector matching is closed, add the remaining SM/gauge/scalar sectors at a consistently defined perturbative order.

No complex poles, physical mixing angle, line shape, signal strength, or allowed/excluded scalar interval is inferred from the present subcalculation.
