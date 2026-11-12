# B5-1 — Full one-loop UV beta function of the Higgs–singlet portal

**Date:** 2026-11-11  
**Model:** original \(U(1)_{L_\mu-L_\tau}\) one-complex-singlet plus two-VLL model; no neutrino-sector extension.  
**Matching reference:** \(M_E=20\) TeV, \(\lambda_{HS}^{\rm EFT}(M_E)=0\), \(\lambda_{HS}^{\rm UV}(M_E)=-\Delta\lambda_{HS}^{E}\).  
**Status:** the complete one-loop UV \(\overline{\rm MS}\) beta function for \(\lambda_{HS}\) is derived for the common-threshold, diagonal-gauge-kinetic boundary \(\chi(M_E)=0\). The exact symbolic checks and benchmark decomposition are recorded below. This does not close the EFT beta functions or the full UV–EFT pole calculation.

## 1. Fixed Lagrangian and charge normalization

The scalar potential is
\[
V=-\mu_H^2H^\dagger H-\mu_S^2S^\dagger S
+\lambda_H(H^\dagger H)^2+\lambda_S(S^\dagger S)^2
+\lambda_{HS}(H^\dagger H)(S^\dagger S).
\]

The relevant gauge charges are
\[
H:\quad (SU(2)_L,\ Y,\ X)=(\mathbf 2,\tfrac12,0),
\qquad
S:\quad (SU(2)_L,\ Y,\ X)=(\mathbf 1,0,+2).
\]
The convention is \(m_X=2g_Xv_S\). Thus the physical \(U(1)_X\) charge-coupling of \(S\) is \(2g_X\), not \(g_X\).

The VLL Yukawa terms are
\[
-\mathcal L_Y^{\rm VLL}\supset
\sum_{\ell=\mu,\tau}
\left[
y_\ell\bar L_\ell H E_{\ell R}
+\lambda_\ell S_\ell\bar E_{\ell L}\ell_R
\right]+\mathrm{h.c.},
\qquad S_\mu=S,\quad S_\tau=S^\ast.
\]
The \(U(1)_X\) charges of \(L_\mu,\mu_R,E_\mu\) are \(+1,-1,+1\), respectively; the tau-sector charges have the opposite signs. The direct SM muon and tau Yukawa couplings are forbidden. The electron and quark SM Yukawa matrices remain allowed.

The gauge kinetic mixing is taken diagonal at the common matching scale. The full chiral spectrum has \(\operatorname{Tr}(YX)=0\), as checked explicitly in §4. Therefore no one-loop additive \(B-X\) kinetic-mixing pole is generated in the mass-independent full-theory scheme at this boundary. A finite threshold can still arise if the two heavy VLL masses are split; that is not the common-\(M_E\) benchmark considered here.

## 2. Complete one-loop beta function

Define
\[
\mathcal T_H^{\rm SM}
=3\,\operatorname{Tr}(Y_u^\dagger Y_u)
+3\,\operatorname{Tr}(Y_d^\dagger Y_d)
+\operatorname{Tr}(Y_e^\dagger Y_e),
\]
where \(Y_e\) contains only the allowed direct charged-lepton Yukawa entries, and
\[
\mathcal T_H^{\rm VLL}=|y_\mu|^2+|y_\tau|^2,
\qquad
\mathcal T_S^{\rm VLL}=|\lambda_\mu|^2+|\lambda_\tau|^2.
\]

The full one-loop UV result is
\[
\boxed{\begin{aligned}
16\pi^2\beta_{\lambda_{HS}}^{\rm UV}
={}&\lambda_{HS}^{\rm UV}\bigg[
12\lambda_H+8\lambda_S+4\lambda_{HS}^{\rm UV}\\
&-\frac92g_2^2-\frac32g_Y^2-24g_X^2\\
&+2\Big(
\mathcal T_H^{\rm SM}
+\mathcal T_H^{\rm VLL}
+\mathcal T_S^{\rm VLL}
\Big)
\bigg].
\end{aligned}}
\tag{1}
\]

Equivalently, the VLL contribution to the Yukawa trace is
\[
\boxed{
\Delta_{\rm VLL}\!\left(
16\pi^2\frac{\beta_{\lambda_{HS}}}{\lambda_{HS}}
\right)
=
2\sum_{\ell=\mu,\tau}
\left(|y_\ell|^2+|\lambda_\ell|^2\right).
}
\tag{2}
\]

There is **no additive one-loop term** proportional to
\(|y_\ell|^2|\lambda_\ell|^2\) in \(\beta_{\lambda_{HS}}\) for this chiral VLL mass/Yukawa structure. This absence is not an assumption: it follows from the explicit fermion determinant check in §3.

### 2.1 Scalar contribution

The A3a scalar/Goldstone pole gives, including the portal-squared term from the independent effective-potential cross-check,
\[
\delta\lambda_{HS}^{\rm scalar}
=\frac{\lambda_{HS}}{16\pi^2\bar\epsilon}
(6\lambda_H+2\lambda_{HS}+4\lambda_S).
\]
For \(d=4-2\epsilon\), the one-loop beta contribution is twice the pole residue:
\[
16\pi^2\beta_{\lambda_{HS}}^{\rm scalar}
=\lambda_{HS}(12\lambda_H+4\lambda_{HS}+8\lambda_S).
\]
This reproduces the A3a linear-in-portal result and restores the \(4\lambda_{HS}^2\) term when the portal is treated as an ordinary independent tree-level coupling.

### 2.2 Gauge contribution

For a quartic with external fields \(H,H^\dagger,S,S^\dagger\), the one-loop gauge contribution from external-leg/gauge-vertex renormalization is
\[
-3g_a^2\sum_{\rm four\ external\ legs}C_a(\phi_i)\,\lambda_{HS}
=-6\lambda_{HS}\sum_{a}
\big[C_a(H)+C_a(S)\big]g_a^2.
\]
Using
\[
C_2(H)=\frac34,\qquad Y_H^2=\frac14,\qquad X_S^2=4,
\]
and the absence of a common gauge generator for \(H\) and \(S\), gives
\[
16\pi^2\beta_{\lambda_{HS}}^{\rm gauge}
=-\lambda_{HS}
\left(\frac92g_2^2+\frac32g_Y^2+24g_X^2\right).
\]
There is no additive \(g^4\) portal source at \(\chi=0\): \(H\) is charged only under \(SU(2)_L\times U(1)_Y\), while \(S\) is charged only under \(U(1)_X\). A nonzero off-diagonal Abelian kinetic term would require a separate generalized-coupling calculation.

### 2.3 Yukawa contribution

The scalar anomalous dimensions from Yukawa interactions are
\[
16\pi^2\gamma_H^{Y}
=\mathcal T_H^{\rm SM}+\sum_\ell|y_\ell|^2,
\qquad
16\pi^2\gamma_S^{Y}
=\sum_\ell|\lambda_\ell|^2.
\]
The portal contains two \(H\) legs and two \(S\) legs, so the Yukawa wavefunction contribution is
\[
16\pi^2\beta_{\lambda_{HS}}^{Y}
=2\lambda_{HS}(\gamma_H^Y+\gamma_S^Y)\,16\pi^2,
\]
which gives the \(+2(\mathcal T_H^{\rm SM}+\mathcal T_H^{\rm VLL}+\mathcal T_S^{\rm VLL})\) term in Eq. (1).

The possible additive four-Yukawa box is checked separately. It vanishes for the present chiral mass matrix and must not be inserted by analogy with a model in which the same fermions couple to both scalars through a different chirality structure.

## 3. Exact VLL determinant check: no additive mixed-quartic UV pole

For one flavor, in a neutral scalar background, use
\[
\mathcal M_\ell(h,s)=
\begin{pmatrix}
0&y_\ell h/\sqrt2\\
\lambda_\ell s/\sqrt2&M_{E_\ell}
\end{pmatrix}.
\]
For real couplings (the result depends only on absolute squares for complex couplings),
\[
\operatorname{Tr}\big[(\mathcal M_\ell^\dagger\mathcal M_\ell)^2\big]
=
M_{E_\ell}^4
+M_{E_\ell}^2|y_\ell|^2h^2
+M_{E_\ell}^2|\lambda_\ell|^2s^2
+\frac14|y_\ell|^4h^4
+\frac14|\lambda_\ell|^4s^4.
\]
In particular,
\[
\boxed{
\left[
\operatorname{Tr}(\mathcal M_\ell^\dagger\mathcal M_\ell)^2
\right]_{h^2s^2}=0.
}
\]
The one-loop fermion determinant therefore has no additive
\(|y_\ell|^2|\lambda_\ell|^2/\bar\epsilon\) divergence in the renormalizable portal. This is consistent with the existing RC-001 result:
\[
\Delta\lambda_{HS}^{E}
=-\frac{1}{8\pi^2}\sum_\ell|y_\ell|^2|\lambda_\ell|^2
\]
is a **finite hard threshold**, not a pole residue and not an additive term in the one-loop UV beta function.

The determinant check does not remove the multiplicative VLL Yukawa terms in Eq. (2): those arise from the \(H\) and \(S\) scalar wavefunction renormalizations.

## 4. Abelian kinetic-mixing trace

Using left-handed Weyl fields and including the two \(SU(2)_L\) components of each lepton doublet:
\[
\begin{array}{c|r|r|r}
\text{Weyl multiplet}&d_{\rm mult}&Y&X\\ \hline
L_\mu&2&-1/2&+1\\
\mu_R^c&1&+1&+1\\
L_\tau&2&-1/2&-1\\
\tau_R^c&1&+1&-1\\
E_{\mu L}&1&-1&+1\\
E_{\mu R}^c&1&+1&-1\\
E_{\tau L}&1&-1&-1\\
E_{\tau R}^c&1&+1&+1
\end{array}
\]
The light \(\mu\) and \(\tau\) chiral sectors each give zero separately. The two heavy Dirac VLLs give \(-2\) and \(+2\), respectively. Hence
\[
\boxed{\operatorname{Tr}_{\rm Weyl}(YX)=0.}
\]
The scalars also give zero because \(X_H=0\) and \(Y_S=0\). Therefore \(\beta_\chi^{(1)}=0\) at \(\chi=0\) for the complete common-threshold spectrum. If \(M_{E_\mu}\ne M_{E_\tau}\), sequential decoupling can leave a finite threshold and an intermediate EFT running interval; that case is outside the equal-\(M_E\) benchmark.

## 5. Combined perturbative counting

At the selected matching point,
\[
\lambda_{HS}^{\rm UV}(M_E)
=-\Delta\lambda_{HS}^{E}>0,
\qquad
\lambda_{HS}^{\rm EFT}(M_E)=0,
\]
with
\[
\lambda_{HS}^{\rm UV}(A)=0.2107639764,\qquad
\lambda_{HS}^{\rm UV}(B)=0.01067337649.
\]

Since the reference assignment counts \(\lambda_{HS}^{\rm UV}=O(\hbar)\), the terms linear in \(\lambda_{HS}\) in Eq. (1) are \(O(\hbar^2)\) in the combined expansion. The \(4(\lambda_{HS}^{\rm UV})^2\) term is \(O(\hbar^3)\) and is dropped if strictly truncating at \(O(\hbar^2)\). It is retained in Eq. (1) so that the ordinary full one-loop \(\overline{\rm MS}\) beta function is also available.

Do not use Eq. (1) below \(M_E\). The EFT beta function has a different field/operator content and must be derived from the EFT counterterm basis.

## 6. Benchmark evaluation

Use the A5b benchmark relations
\[
y_\mu=y_\tau=\frac{\sqrt2M_E\theta_L}{v_h},
\qquad
\lambda_\ell=\frac{\sqrt2m_\ell}{\theta_Lv_S},
\qquad
g_X=\frac{m_X}{2v_S},
\]
with \(\theta_L=10^{-2}\). These give
\[
y_\mu=y_\tau=1.14873980.
\]

| Input | Benchmark A | Benchmark B |
|---|---:|---:|
| \(v_S\) [GeV] | 70.886458 | 315 |
| \(m_X\) [GeV] | 10 | 63 |
| \(g_X\) | 0.0705353 | 0.100000 |
| \(\lambda_{HS}^{\rm UV}(M_E)\) | 0.21076398 | 0.01067338 |
| \(\lambda_\mu\) | 0.2107927 | 0.0474360 |
| \(\lambda_\tau\) | 3.5449077 | 0.7977332 |
| \(\mathcal T_H^{\rm VLL}\) | 2.6392062 | 2.6392062 |
| \(\mathcal T_S^{\rm VLL}\) | 12.6108042 | 0.6386284 |
| \(2(\mathcal T_H^{\rm VLL}+\mathcal T_S^{\rm VLL})\) | 30.5000209 | 6.5556693 |
| \(24g_X^2\) | 0.1194056 | 0.2400000 |

At the illustrative \(m_s=125.25\) GeV point, with
\(\lambda_H=m_h^2/(2v_h^2)\) and the leading unmixed relation
\(\lambda_S=m_s^2/(2v_S^2)\), the known pieces of the beta function are:

| Contribution to \(\beta_{\lambda_{HS}}\) | A | B |
|---|---:|---:|
| Scalar linear \(+\lambda_{HS}(12\lambda_H+8\lambda_S)/(16\pi^2)\) | \(+1.87395\times10^{-2}\) | \(+1.47684\times10^{-4}\) |
| VLL Yukawa \(+2\lambda_{HS}(\mathcal T_H^{VLL}+\mathcal T_S^{VLL})/(16\pi^2)\) | \(+4.07077\times10^{-2}\) | \(+4.43097\times10^{-4}\) |
| \(U(1)_X\) gauge \(-24g_X^2\lambda_{HS}/(16\pi^2)\) | \(-1.59368\times10^{-4}\) | \(-1.62216\times10^{-5}\) |
| Portal-squared \(+4\lambda_{HS}^2/(16\pi^2)\) | \(+1.12521\times10^{-3}\) | \(+2.88565\times10^{-6}\) |
| **Known subtotal, excluding SM gauge/Yukawa terms** | **\(+6.04131\times10^{-2}\)** | **\(+5.77446\times10^{-4}\)** |

The remaining SM contribution is kept explicit:
\[
D_{\rm SM}\equiv
2\mathcal T_H^{\rm SM}
-\frac92g_2^2-\frac32g_Y^2,
\]
so at \(m_s=125.25\) GeV
\[
\begin{aligned}
\beta_{\lambda_{HS}}^{A}
&=0.0604131+1.3346785\times10^{-3}D_{\rm SM},\\
\beta_{\lambda_{HS}}^{B}
&=5.7744579\times10^{-4}
+6.7589946\times10^{-5}D_{\rm SM}.
\end{aligned}
\]
No numerical \(D_{\rm SM}\) is inserted because the running SM gauge/Yukawa inputs at \(20\) TeV have not yet been fixed in the repository. This avoids silently mixing electroweak-scale and matching-scale couplings.

Across the current \(m_s=10\)–150 GeV diagnostic interval, the known subtotal (including the full one-loop portal-squared term but excluding \(D_{\rm SM}\)) ranges from
\[
A:\quad 0.0438520\ \text{to}\ 0.0676510,
\qquad
B:\quad 5.34974\times10^{-4}\ \text{to}\ 5.96008\times10^{-4}.
\]
The scalar-mass dependence enters through \(\lambda_S\). The relation
\(\lambda_S=m_s^2/(2v_S^2)\) is a leading unmixed radial-mass parametrization, not a full mass-eigenstate inversion. Near the Higgs–singlet degeneracy the full \(2\times2\) scalar mass matrix is required.

### Perturbativity observation

Benchmark A has
\[
\lambda_\tau=3.5449077=\sqrt{4\pi},
\qquad
\frac{\lambda_\tau^2}{16\pi^2}=0.0795775.
\]
It sits at the adopted Yukawa perturbativity boundary. Benchmark B has
\[
\lambda_\tau=0.7977332,\qquad
\frac{\lambda_\tau^2}{16\pi^2}=0.00402991.
\]
The VLL Yukawa term dominates the known beta subtotal, especially in A. This is a reason to integrate the coupled running and monitor higher-loop sensitivity; it is not a reason to extrapolate the one-loop coefficient with fixed couplings over a large logarithm.

## 7. Independent literature cross-check

For a complex scalar singlet with the same quartic normalization, Cheng and Bian, *Phys. Rev. D* **98**, 023524 (2018), Appendix A, Eq. (A3), give the common scalar/SM part of the portal beta function. Rewriting their expression in the present convention reproduces
\[
12\lambda_H+8\lambda_S+4\lambda_{HS}
-\frac92g_2^2-\frac32g_Y^2+6y_t^2.
\]
Our expression extends this common part by the gauged-singlet term \(-24g_X^2\) and the two VLL Yukawa traces. The paper is a cross-check of the common complex-singlet/SM terms, not a source for the model-specific \(U(1)_X\) or VLL additions. DOI: 10.1103/PhysRevD.98.023524.

## 8. B5-1 acceptance and remaining work

**B5-1 passed for the one-loop UV portal beta at \(\chi(M_E)=0\):**
1. Scalar coefficient, including the portal-squared term, matches A3a and the effective-potential cross-check.
2. Gauge coefficient follows from the actual representations and \(Q_S=2\).
3. SM and VLL Yukawa multiplicative terms are included with the correct scalar-leg multiplicities.
4. The additive VLL \(|y|^2|\lambda|^2\) pole is explicitly zero from the field-dependent mass determinant.
5. The one-loop \(\operatorname{Tr}(YX)\) kinetic-mixing source vanishes for the complete common-threshold spectrum.
6. Both benchmarks are evaluated without inventing the still-unfixed running SM inputs at \(20\) TeV.

**B5-1b update (2026-11-11):** the numerical benchmark table in §6 is an algebraic illustration using the tree-level weak-scale value \(\lambda_H=m_h^2/(2v_h^2)\) and \(m_s=125.25\) GeV. It is **not** the correctly RG-matched \(20\) TeV numerical beta evaluation. The matched SM inputs and the one-loop running to \(M_E\), together with the corrected numerical \(\beta_{\lambda_{HS}}(M_E)\), are recorded in `B5_1B_SM_THRESHOLD_AND_COUPLED_UV_RGE_2026-11-11.md`. Use B5-1b for numerical work at the matching scale. Also, the full UV RGE is used only above \(M_E\); below \(M_E\), the EFT RGE must be used.

**Still open:**
- Independently validate the model-specific gauge, VLL Yukawa, and scalar-quartic beta functions with SARAH/PyR@TE or a diagrammatic calculation.
- Upgrade the SM running below \(M_E\) to a consistent two-loop cross-check and propagate the top-mass/matching-input uncertainty.
- Derive the EFT beta below \(M_E\) in the common operator basis; Eq. (1) is UV-only.
- Complete B5-2 Wilson-operator mixing and B5-3 tadpole/field closure before the full \(\mu_M\) stability test.
- Keep the \(0.1421\%\) Plan-C-lite residual as a separate exact-mass hard/soft diagnostic; Eq. (1) does not explain it.

**Conclusion:** the complete one-loop UV portal beta is analytically explicit. B5-1b provides a first-pass \(20\) TeV input and coupled UV-running evaluation. The next step is to validate the full RGE system independently and derive the EFT running below \(M_E\) before attempting the full UV–EFT matching-scale cancellation.
