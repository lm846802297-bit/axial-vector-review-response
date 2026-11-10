# B5-1b — SM running-input sub-block at \(M_E=20\) TeV

**Date:** 2026-11-11  
**Status:** completed as a controlled SM-only input sub-block. This is not the coupled UV evolution of the full VLL model.

## 1. Input scheme

For a reproducible first numerical pass, use central \(\overline{\rm MS}\) matching inputs of the Buttazzo et al. type:
\[
g_Y(M_Z)=0.3575,\quad g_2(M_Z)=0.65171,\quad
g_3(m_t)=1.1645,\quad y_t(m_t)=0.93587,
\]
with \(M_Z=91.1876\) GeV, \(m_t=173.15\) GeV and \(m_h=125.25\) GeV. The Higgs quartic boundary is
\[
\lambda_H(m_t)=0.12577+0.00205(m_h-125.0)-0.00004(m_t-173.15)
=0.1262825.
\]
These are an explicitly declared approximate one-loop input set, not a precision electroweak fit. The input conventions and matching formulae are documented in the Higgs-vacuum-stability literature; see Buttazzo et al., JHEP 12 (2013) 089, arXiv:1307.3536.

## 2. SM-only one-loop evolution

Run the SM subsystem from \(m_t\) to \(M_E=20\) TeV with
\[
16\pi^2\frac{dg_Y}{dt}=\frac{41}{6}g_Y^3,\quad
16\pi^2\frac{dg_2}{dt}=-\frac{19}{6}g_2^3,\quad
16\pi^2\frac{dg_3}{dt}=-7g_3^3,
\]
\[
16\pi^2\frac{dy_t}{dt}
=y_t\left(\frac92y_t^2-8g_3^2-\frac94g_2^2-\frac{17}{12}g_Y^2\right),
\]
\[
\begin{aligned}
16\pi^2\frac{d\lambda_H}{dt}={}&24\lambda_H^2
+\lambda_H(12y_t^2-9g_2^2-3g_Y^2)-6y_t^4\\
&+\frac98g_2^4+\frac34g_2^2g_Y^2+\frac38g_Y^4.
\end{aligned}
\]
Here \(t=\ln\mu\), \(g_Y\) is the non-GUT-normalized hypercharge coupling, and bottom/tau/electron Yukawas are neglected in this first numerical pass.

The resulting 20 TeV inputs are:
| Coupling | Value at 20 TeV |
|---|---:|
| \(g_Y\) | 0.36865960 |
| \(g_2\) | 0.62370335 |
| \(g_3\) | 0.92908277 |
| \(y_t\) | 0.77069903 |
| \(\lambda_H\) | 0.05807254 |

The portal-beta SM remainder, top-only, is
\[
D_{\rm SM}=2(3y_t^2)-\frac92g_2^2-\frac32g_Y^2
=1.60947075.
\]
The portal beta function therefore has the following **instantaneous values at the matching scale**, using the B5-1 benchmark decomposition (whose scalar term still uses the illustrative \(\lambda_H=m_h^2/(2v_h^2)\) input until the tree/loop matching convention is unified):
\[
\boxed{\beta_{\lambda_{HS}}^A(M_E)=6.25612\times10^{-2},\qquad
\beta_{\lambda_{HS}}^B(M_E)=6.86230\times10^{-4}.}
\]
These values add the top-only SM gauge/Yukawa remainder to the earlier known subtotal. They are not integrated low-scale predictions.

## 3. Important consistency correction before coupled running

The previous B5-1 numerical decomposition used
\(\lambda_H=m_h^2/(2v_h^2)=0.12938\), an electroweak-scale tree-level proxy. This B5-1b sub-block gives the running \(\overline{\rm MS}\) value \(\lambda_H(20\,{\rm TeV})=0.05807\). These must not be mixed in a single \(M_E\)-scale beta evaluation. Before claiming a fully numerical \(\beta_{\lambda_{HS}}(M_E)\), replace the proxy by the consistently matched/running \(\lambda_H(M_E)\), and likewise run \(\lambda_S\), the VLL Yukawas, and \(g_X\) in the full UV theory. The numbers boxed above are therefore an SM-remainder diagnostic with the earlier scalar benchmark term held fixed, not the final consistent matching-scale beta.

## 4. Why the coupled model evolution is not yet run

The SM subsystem alone does not determine the evolution of
\[
y_\mu,y_\tau,\lambda_\mu,\lambda_\tau,g_X,\lambda_S,\lambda_{HS}.
\]
Their one-loop beta functions must be derived from the exact chiral VLL representations, including all shared-fermion and scalar-wavefunction contributions. In particular, Benchmark A starts at \(\lambda_\tau=\sqrt{4\pi}\), so the full coupled system can approach or cross the perturbativity boundary rapidly. A fixed-coupling extrapolation would be misleading.

Also, the VLLs must be decoupled at \(M_E\). Below that scale the UV beta function (B5-1) is not valid; the EFT operator basis and its anomalous-dimension matrix govern the evolution. Thus no \(M_E\to m_h\) integral is reported here.

## 5. Next acceptance tests

1. Derive and independently cross-check the one-loop VLL Yukawa beta functions from the model's chiral Lagrangian.
2. Derive \(\beta_{\lambda_S}\) and \(\beta_{g_X}\), including the complete active-field content.
3. Fix a single \(M_E\)-scale \(\overline{\rm MS}\) input scheme for \(\lambda_H,\lambda_S\) and all VLL couplings.
4. Integrate the coupled UV system only over the interval where VLLs are active, and report perturbativity diagnostics.
5. Match at \(M_E\), then use the EFT anomalous-dimension system below threshold. Do not continue the UV beta below \(M_E\).

**Conclusion:** the SM running-input sub-block is numerically available, but the full B5-1b coupled evolution remains open. The key correction is to use a single consistent \(\overline{\rm MS}\) scale for every coupling; the earlier mixed-scale beta subtotal must not be advertised as a final matching-scale number.
