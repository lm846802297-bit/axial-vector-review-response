# B5-2A — EFT \(C_5C_5^\ast\) matching block and quartic-EOM subblock

**Date:** 2026-11-11  
**Parent:** B5-2, EFT operator running and mixing at strict \(M_E^{-2}\).  
**Status:** the Yukawa-box \(C_5C_5^\ast\) current/4-fermion matching coefficients are numerically evaluated for A/B; the \(Q_{LD},Q_{RD}\)+quartic off-shell EOM block is also evaluated. This is a **sub-block**, not the complete EFT anomalous-dimension matrix.

## 1. Fixed EFT basis and normalization

Use the already established definitions
\[
C_{5,\ell}=-\frac{y_\ell\lambda_\ell}{M_E},\qquad
C_{LD,\ell}=\frac{|y_\ell|^2}{M_E^2},\qquad
C_{RD,\ell}=\frac{|\lambda_\ell|^2}{M_E^2},
\]
and
\[
{\cal L}_{\rm EFT}\supset
\frac{c_{\partial HS}}{M_E^2}
\partial_\mu(H^\dagger H)\partial^\mu(S^\dagger S).
\]
For flavor-resolved matching, the singlet in the dimension-five operator is
\[
S_\mu=S,\qquad S_\tau=S^\ast,\qquad
\eta_\mu=+1,\quad \eta_\tau=-1.
\]
Define \(J_{S_\ell}^\mu=S_\ell^\dagger i\overleftrightarrow D^\mu S_\ell\)
and the common-\(S\) current \(J_S^\mu=S^\dagger i\overleftrightarrow D^\mu S\).
Then
\[
J_{S_\ell}^\mu=\eta_\ell J_S^\mu.
\]
The current operators retained below are expressed in the **common-\(S\) basis**:
\[
\begin{aligned}
O_{LS}&=J_{S,\mu}(\bar L_\ell\gamma^\mu L_\ell),\\
O_{He}&=(H^\dagger i\overleftrightarrow D_\mu H)
(\bar\ell_R\gamma^\mu\ell_R),\\
O_{Se}&=J_{S,\mu}(\bar\ell_R\gamma^\mu\ell_R).
\end{aligned}
\]
Equivalently, flavor-specific \(S_\ell\)-current coefficients acquire a factor
\(\eta_\ell\) when expressed in this common basis. The four-fermion operators are
\[
O_{4f}^{S}=(\bar L_\ell\ell_R)(\bar\ell_R L_\ell),\qquad
O_{4f}^{V}=(\bar L_\ell\gamma_\mu L_\ell)
(\bar\ell_R\gamma^\mu\ell_R).
\]
All coefficients below use the same flavor-diagonal routing and Grassmann ordering as the upstream soft-loop note. They are Yukawa-box-sector coefficients only; no gauge-correction coefficients are inferred.

## 2. Exact \(C_5C_5^\ast\) hard coefficients

Define
\[
\kappa_\ell\equiv\frac{|C_{5,\ell}|^2}{16\pi^2}
=\frac{|y_\ell|^2|\lambda_\ell|^2}
{16\pi^2M_E^2}.
\]
The previously derived hard coefficients are
\[
\begin{aligned}
C_{LS,\ell}^{\rm hard,common}(\mu)
&=\eta_\ell\kappa_\ell\left(\frac{L_E}{4}-\frac38\right),\\
C_{He,\ell}^{\rm hard}(\mu)
&=-\kappa_\ell\left(\frac{L_E}{4}-\frac38\right),\\
C_{Se,\ell}^{\rm hard,common}(\mu)
&=-2\eta_\ell\kappa_\ell\left(\frac{L_E}{4}-\frac38\right),\\
C_{4f,\ell}^{S,\rm hard}(\mu)
&=\kappa_\ell(L_E-2),
\end{aligned}
\qquad L_E=\ln\frac{M_E^2}{\mu^2}.
\]
The chiral Fierz identity in this operator ordering is
\[
(\bar L_\ell\ell_R)(\bar\ell_R L_\ell)
=-\frac12(\bar L_\ell\gamma_\mu L_\ell)
(\bar\ell_R\gamma^\mu\ell_R),
\]
so
\[
C_{4f,\ell}^{V,\rm hard}(\mu)
=-\frac12 C_{4f,\ell}^{S,\rm hard}(\mu).
\]

At \(\mu=M_E\), \(L_E=0\), hence
\[
\boxed{
(C_{LS},C_{He},C_{Se},C_{4f}^{S},C_{4f}^{V})_\ell^{\rm common}
=\kappa_\ell
\left(-\eta_\ell\frac38,+\frac38,+\eta_\ell\frac34,-2,+1\right).
}
\tag{1}
\]
The scale-log derivatives of these displayed hard terms, at fixed \(\kappa_\ell\), are
\[
\frac{d}{d\ln\mu}
(C_{LS},C_{He},C_{Se},C_{4f}^{S},C_{4f}^{V})_\ell^{\rm hard}
=\kappa_\ell
\left(-\eta_\ell\frac12,+\frac12,+\eta_\ell,-2,+1\right).
\tag{2}
\]
Equation (2) is recorded as the derivative of the hard matching terms. It is not promoted to the complete EFT beta vector until the corresponding EFT counterterms, all other same-order insertions, and the common operator basis are combined.

## 3. Benchmark A/B numerical matching values

Use \(M_E=20\) TeV, \(\theta_L=10^{-2}\), \(v_h=246.22\) GeV, and the already fixed \(v_S\) values. The corrected B5-1b singlet-Yukawa RGE does not alter the boundary values at \(M_E\):
\[
y_\mu=y_\tau=1.1487397956.
\]

| Quantity | A, \(\mu\) | A, \(\tau\) | B, \(\mu\) | B, \(\tau\) |
|---|---:|---:|---:|---:|
| \(C_{5,\ell}\) [GeV\(^{-1}\)] | \(-1.21073\times10^{-5}\) | \(-2.03609\times10^{-4}\) | \(-2.72458\times10^{-6}\) | \(-4.58194\times10^{-5}\) |
| \(C_{LD,\ell}\) [GeV\(^{-2}\)] | \(3.29901\times10^{-9}\) | \(3.29901\times10^{-9}\) | \(3.29901\times10^{-9}\) | \(3.29901\times10^{-9}\) |
| \(C_{RD,\ell}\) [GeV\(^{-2}\)] | \(1.11084\times10^{-10}\) | \(3.14159\times10^{-8}\) | \(5.62544\times10^{-12}\) | \(1.59095\times10^{-9}\) |
| \(\kappa_\ell\) [GeV\(^{-2}\)] | \(9.28271\times10^{-13}\) | \(2.62527\times10^{-10}\) | \(4.70089\times10^{-14}\) | \(1.32947\times10^{-11}\) |

Summing the two flavors, the finite hard coefficients at \(\mu=M_E\) are:

| Coefficient [GeV\(^{-2}\)] | A | B |
|---|---:|---:|
| \(C_{LS}^{\rm hard,common}\) | \(+9.80994\times10^{-11}\) | \(+4.96789\times10^{-12}\) |
| \(C_{He}^{\rm hard}\) | \(+9.87956\times10^{-11}\) | \(+5.00315\times10^{-12}\) |
| \(C_{Se}^{\rm hard,common}\) | \(-1.96199\times10^{-10}\) | \(-9.93578\times10^{-12}\) |
| \(C_{4f}^{S,\rm hard}\) | \(-5.26910\times10^{-10}\) | \(-2.66834\times10^{-11}\) |
| \(C_{4f}^{V,\rm hard}\) | \(+2.63455\times10^{-10}\) | \(+1.33417\times10^{-11}\) |

These numbers are the Yukawa-box hard subset. The (O_{LS}) and (O_{Se}) sums use the common-(S) basis and include the (eta_ell) orientation factor. They are not the full Wilson coefficients after gauge matching and common-basis EOM/source reduction.

## 4. Recheck of the \(c_{\partial HS}\) inhomogeneous source

The scalar bubble/contact pole from the fixed \(C_5C_5^\ast\) sector gives
\[
\left.\beta_{c_{\partial HS}}\right|_{C_5C_5^\ast}
=-\frac{M_E^2}{16\pi^2}\sum_\ell|C_{5,\ell}|^2
=-M_E^2\sum_\ell\kappa_\ell.
\]
Numerically,
\[
\boxed{
\beta_{c_{\partial HS}}^{A}=-0.1053819882,\qquad
\beta_{c_{\partial HS}}^{B}=-0.00533668824.
}
\]
The matching identity
\[
\beta_{c_{\partial HS}}^{C_5C_5^\ast}
=\frac12\Delta\lambda_{HS}^{E}
\]
is reproduced exactly for both benchmarks. This is unchanged by the corrected \(\beta_{\lambda_\ell}\), because the boundary \(C_{5,\ell}(M_E)\) is unchanged.

## 5. \(Q_{LD},Q_{RD}\) plus scalar-quartic insertions: off-shell EOM block

The upstream hard/soft kernel for one derivative-operator insertion and one scalar-quartic vertex gives the local hard coefficient, before EOM reduction,
\[
C_{\rm EOM}^{\rm hard}(\mu)
=-\frac12\frac{C_6\lambda_{\rm vert}}{16\pi^2}
\left(L_E-\frac32\right).
\]
At \(\mu=M_E\),
\[
C_{\rm EOM}^{\rm hard}(M_E)
=+\frac34\frac{C_6\lambda_{\rm vert}}{16\pi^2},
\]
and the derivative of the hard logarithm is
\[
\frac{d C_{\rm EOM}^{\rm hard}}{d\ln\mu}
=+\frac{C_6\lambda_{\rm vert}}{16\pi^2}.
\]
Here \(\lambda_{\rm vert}\) includes the contraction multiplicity of the relevant quartic vertex.

The contractions are kept separate:
- \(Q_{LD}\) with \(\lambda_{HS}\): \(\lambda_{\rm vert}=\lambda_{HS}\), producing an \(S^\dagger S\,\bar L i\overleftrightarrow{\slashed D}L\) EOM operator.
- \(Q_{RD}\) with \(\lambda_{HS}\): \(\lambda_{\rm vert}=\lambda_{HS}\), producing an \(H^\dagger H\,\bar\ell_R i\overleftrightarrow{\slashed D}\ell_R\) EOM operator.
- \(Q_{RD}\) with \(\lambda_S\): \(\lambda_{\rm vert}=4\lambda_S\), producing an \(S^\dagger S\,\bar\ell_R i\overleftrightarrow{\slashed D}\ell_R\) EOM operator.
- \(Q_{LD}\) with \(\lambda_H\): two distinct weak-index tensors, each with \(\lambda_{\rm vert}=2\lambda_H\); they must remain separate until the singlet/triplet projection.

For \(m_s=100\) GeV, use \(\lambda_S=m_s^2/(2v_S^2)\) only as the existing leading unmixed diagnostic. The hard-log derivatives per flavor are:

| EOM structure | A, \(\mu\) | A, \(\tau\) | B, \(\mu\) | B, \(\tau\) |
|---|---:|---:|---:|---:|
| \(Q_{LD}+\lambda_{HS}\) | \(4.40311\times10^{-12}\) | \(4.40311\times10^{-12}\) | \(2.22980\times10^{-13}\) | \(2.22980\times10^{-13}\) |
| \(Q_{LD}+\lambda_H\), each weak tensor | \(2.47605\times10^{-12}\) | \(2.47605\times10^{-12}\) | \(2.47605\times10^{-12}\) | \(2.47605\times10^{-12}\) |
| \(Q_{RD}+\lambda_{HS}\) | \(1.48261\times10^{-13}\) | \(4.19302\times10^{-11}\) | \(3.80223\times10^{-16}\) | \(1.07532\times10^{-13}\) |
| \(Q_{RD}+\lambda_S\) | \(2.79985\times10^{-12}\) | \(7.91833\times10^{-10}\) | \(7.18035\times10^{-15}\) | \(2.03069\times10^{-12}\) |

These are coefficients of redundant off-shell EOM operators. In the minimal model the ordinary renormalizable \(\mu,\tau\) charged-lepton Yukawas are forbidden, so the corresponding fermion-EOM source functions \(\Xi_{L_\ell}^{(4)}\) and \(\Xi_{R_\ell}^{(4)}\) vanish. Thus this sub-block does not produce an independent on-shell scalar-pole source at this order. It must nevertheless be retained until the common off-shell counterterm and field-redefinition scheme is fixed.

## 6. What this establishes for B5-2

The direct four-scalar projection is separate from the fermionic current/EOM sector:

1. The only inhomogeneous pure-scalar derivative source explicitly established so far is the \(C_5C_5^\ast\) bubble/contact contribution to \(\beta_{c_{\partial HS}}\).
2. The \(C_5C_5^\ast\) crossed two-fermion/two-scalar and four-fermion channels generate the current and four-fermion hard coefficients in Eqs. (1)–(2).
3. A single \(Q_{LD}\) or \(Q_{RD}\) insertion plus a scalar quartic generates the displayed off-shell EOM/source structures. It does not by itself constitute a new local 1PI four-scalar coefficient.
4. Gauge-current exchange is reducible in the exchanged gauge propagator and must be kept in the current/source sector, not re-labelled as a direct \(c_{\partial HS}\) counterterm.
5. The multiplicative renormalization of \(c_{\partial HS}\), gauge corrections to \(Q_{LD},Q_{RD}\) and current operators, the full EOM/IBP projection, and mixing among the complete dimension-six basis remain open.

Therefore **B5-2 is not closed**. This note closes only the numerical \(C_5C_5^\ast\) matching sub-block and the scalar-quartic EOM kernel evaluation. The next required calculation is the gauge-corrected \(Q_{LD},Q_{RD}\) and current sector with UV/EFT pole subtraction and Ward-identity completion; only after that can the full operator-mixing matrix be assembled.

## 7. Provenance

The analytic kernels and signs are inherited from the upstream RC-001 dimension-six soft-loop note, §§2–4, and the UV–EFT subtraction ledger. The upstream note now explicitly states that the (O_{LS,ell}) and (O_{Se,ell}) formulas are first flavor-specific in (S_ell); conversion to a common-(S) basis multiplies their coefficients by (eta_ell). This clarification is recorded in high-energy-theory-research PR #11, commit `679144ecd3d3242ea5dc527884ced63e5cb8e094`. This file adds the B5-1b-consistent A/B numerical evaluation and an explicit separation of physical current coefficients, four-fermion coefficients, and redundant EOM operators. It does not claim new gauge-loop integrals or an independent diagram-generator result.
