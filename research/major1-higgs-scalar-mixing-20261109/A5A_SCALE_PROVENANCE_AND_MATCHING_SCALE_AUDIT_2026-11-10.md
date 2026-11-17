# A5a — provenance and suitability of the \(20\) TeV VLL matching scale

> Scope of the scale choice: the small heavy-threshold splitting supports a common central scale for this benchmark; it does not by itself establish complete RG evolution or matching-scale independence.

**Date:** 2026-11-10  
**Scope:** the original degenerate \(S+\mathrm{VLL}\) benchmark used by PR #49 / Plan-C-lite and continued in PR #69. This note distinguishes the physical VLL mass, the EFT matching scale, and the dimensional-regularization scale.

## 1. Three quantities that must not be conflated

Use separate notation:
- \(M_E\): the vector-like Dirac mass parameter in the UV mass matrix;
- \(m_{E_\ell}^{\rm heavy}\): the heavy singular value (physical mass at tree level) after diagonalizing the charged-lepton/VLL mass matrix;
- \(\mu_M\): the scale at which the VLL is integrated out and the UV theory is matched to the EFT;
- \(\mu_R\): the \(\overline{\rm MS}\)/PV subtraction scale in loop functions.

For the present nearly degenerate benchmark, it is natural to choose
\[
\mu_M\simeq M_E,\qquad \mu_R^{\rm hard}\simeq M_E,
\]
but these are separate choices. The low-energy EFT can and generally should be evolved to a scale \(\mu_{\rm EFT}\sim m_h\) (or the relevant scalar pole scale) before evaluating the low-energy pole. One must not interpret \(\mu_M=\mu_R=m_h\) as a replacement for threshold matching at the heavy VLL scale.

## 2. Provenance of \(M_E=20\) TeV

The value is inherited from the explicit PR #49 mass-eigenstate matching benchmark and the associated Plan-C-lite calculation. It is not a value uniquely predicted by the Lagrangian or an experimental mass measurement.

The earlier model/reply setup uses a degenerate decoupling assumption
\[
M_{E_\mu}=M_{E_\tau}\equiv M_E>10~{\rm TeV},
\]
together with the small-mixing benchmark \(|\theta_{\ell L,R}|\lesssim10^{-2}\). In the leading mass-mixing relation
\[
m_\ell\simeq\theta_{\ell L}\theta_{\ell R}M_E,
\]
the tau mass implies, if both tau mixing angles are bounded by \(10^{-2}\),
\[
M_E\gtrsim
\frac{m_\tau}{10^{-2}\,10^{-2}}
=17.7686~{\rm TeV}.
\]
This is a **conditional consistency lower scale** under that mixing-angle assumption, not an experimental lower limit. The selected \(20\) TeV point lies about \(12.6\%\) above it. With \(\theta_{\tau L}=10^{-2}\),
\[
\theta_{\tau R}
=\frac{m_\tau}{M_E\theta_{\tau L}}
=8.8843\times10^{-3}<10^{-2}.
\]
For the muon, \(\theta_{\mu R}=5.2829\times10^{-4}\).

Thus 20 TeV is a convenient round benchmark consistent with both the older \(>10\) TeV decoupling condition and the stronger conditional tau-mixing requirement. It is not a uniquely preferred physical mass.

## 3. Exact mass-eigenstate threshold check

For each flavor the benchmark matrix is
\[
{\cal M}_\ell=
\begin{pmatrix}
0&M_E\theta_{\ell L}\\
m_\ell/\theta_{\ell L}&M_E
\end{pmatrix},
\]
which is the same leading-seesaw input used by the exact SVD script. Its heavy singular values are:

| Flavor | \(m_{E_\ell}^{\rm heavy}\) [GeV] | \(m_{E_\ell}^{\rm heavy}-M_E\) [GeV] | \(\ln[(m_{E_\ell}^{\rm heavy})^2/M_E^2]\) |
|---|---:|---:|---:|
| \(\mu\) | 20001.002766 | 1.002766 | \(1.00274\times10^{-4}\) |
| \(\tau\) | 20001.789149 | 1.789149 | \(1.78907\times10^{-4}\) |

The two physical heavy thresholds differ by only \(0.7864\) GeV, or \(3.93\times10^{-5}\) relative to \(M_E\). A single common matching scale is therefore fully adequate for the present degenerate benchmark. Using the more exact heavy singular values rather than the common \(20\) TeV input would make a negligible change at this order.

If the UV model is later generalized to non-degenerate \(M_{E_\mu}\) and \(M_{E_\tau}\), the preferred procedure is sequential matching at the two heavy thresholds. A common scale can still be used, but the logarithms \(\ln(m_{E_\ell}^2/\mu_M^2)\) and the RG evolution between thresholds must then be retained.

## 4. Why \(\mu_M=20\) TeV and \(\mu_R^{\rm hard}=20\) TeV are sensible central choices

The finite hard derivative coefficient in the RC-001 convention is
\[
\Pi_{RC,\rm hard}'(0)
=\frac{q}{16\pi^2}
\left[\ln\frac{M_E^2}{\mu_R^2}-\frac23\right]
+O(M_E^{-4}\ln M_E),
\qquad
q=\sum_{\ell=\mu,\tau}\frac{2m_\ell^2}{v_hv_s}.
\]
The Plan-C convention has \(\Pi_B=-\Pi_{RC}\). At \(\mu_R=M_E\), the large threshold logarithm vanishes and the remaining finite coefficient is the constant \(-2/3\) in the RC convention (or \(+2/3\) in the Plan-C convention). This is the natural scale for the hard matching calculation.

By contrast,
\[
\ln\frac{M_E^2}{m_h^2}=10.14635.
\]
Evaluating the isolated hard coefficient at \(\mu_R=m_h\) therefore introduces a large heavy-threshold logarithm. This is not a reason to avoid \(\mu_R=m_h\) in the low-energy EFT; it is a reason to evolve the matched EFT coefficients from \(\mu_M\simeq M_E\) down to \(\mu_{\rm EFT}\simeq m_h\), rather than evaluate the hard matching coefficient at a low scale without the corresponding RG organization.

## 5. Existing scale comparison: useful but not a complete RG test

The archived Plan-C-lite validation compares the selected hard-plus-soft subset at \(\mu_R=M_E\) and \(\mu_R=m_h\):

| Benchmark | \(\Pi_{\rm total}(\mu_R=M_E)\) [GeV²] | \(\Pi_{\rm total}(\mu_R=m_h)\) [GeV²] | Relative change in real part |
|---|---:|---:|---:|
| A | \(-0.413263168\) | \(-0.413850308\) | \(0.1421\%\) |
| B | \(-0.092999245\) | \(-0.093131373\) | \(0.1421\%\) |

The hard derivative piece itself changes by about \(0.3660\) GeV² (A) and \(0.08235\) GeV² (B) between these two choices; the selected soft part compensates most of this change. This is a useful internal consistency diagnostic.

However, the Plan-C-lite same-order EFT soft/counterterm set is not yet fully closed. The \(0.1421\%\) residual is therefore **not** a demonstrated all-order or complete one-loop scale-independence result, and it is not a substitute for the explicit RG evolution and matching-scale cancellation required in A5b.

## 6. Matching-scale variation is not a physical-mass scan

Two operations must be kept separate.

**Varying \(\mu_M\) at fixed physical \(M_E\):** this is a matching-scale diagnostic. The full-theory and EFT Wilson coefficients must be evolved consistently, and the final pole must be stable up to the first omitted order. A conventional first scan is
\[
\mu_M\in[M_E/2,\,2M_E]=[10,40]~{\rm TeV}.
\]
The corresponding logarithms are \(+\ln4,0,-\ln4\). These are bookkeeping variations, not different VLL masses. Do not reimpose \(\lambda_{HS}^{\rm EFT}(\mu_M)=0\) independently at every varied scale; evolve the same benchmark boundary condition.

**Varying the physical \(M_E\):** this changes the UV model benchmark. With \(\theta_{\ell L}\) fixed and the light-lepton masses held fixed,
\[
y_\ell=\frac{\sqrt2M_E\theta_{\ell L}}{v_h},
\qquad
\lambda_\ell=\frac{\sqrt2m_\ell}{\theta_{\ell L}v_s}.
\]
Consequently the leading portal threshold scales as
\[
\Delta\lambda_{HS}^{E}
=-\frac{M_E^2}{2\pi^2v_h^2v_s^2}
\sum_{\ell=\mu,\tau}m_\ell^2,
\]
within the same leading-seesaw approximation. A physical-mass scan therefore changes the Yukawa couplings and the portal threshold; it is not a renormalization-scale uncertainty.

## 7. A5a prescription and acceptance gate

For the current degenerate benchmark, adopt the following central prescription:

1. Keep \(M_E=20\) TeV as the declared physical UV benchmark parameter.
2. Use \(\mu_M=20\) TeV for integrating out the common VLL threshold.
3. Use \(\mu_R^{\rm hard}=20\) TeV for the hard VLL matching functions, so the large \(\ln(M_E^2/\mu_R^2)\) is absent.
4. Define the conditional portal boundary \(\lambda_{HS}^{\rm EFT}(\mu_M)=0\) at this central matching point. This is a chosen cancellation benchmark, not a symmetry prediction.
5. Run the complete EFT Wilson-coefficient vector and renormalized couplings down to \(\mu_{\rm EFT}\sim m_h\) before evaluating the low-energy scalar pole. Evaluate soft loops and counterterms consistently at that low scale, or keep a common scale and retain all logarithms; the two organizations must agree.
6. Once the complete beta functions, threshold counterterms, and EFT soft set are closed, vary \(\mu_M\) by a factor of two and verify that the final pole changes only by the expected uncomputed higher-order terms.

**Conclusion:** \(20\) TeV is appropriate as the central matching scale for the existing degenerate \(20\) TeV VLL benchmark. Its justification is proximity to the actual heavy singular-value thresholds, consistency with the conditional tau-mixing bound, and removal of large hard logarithms. It is not a unique prediction, an experimental lower limit, or a license to use \(20\) TeV as the renormalization scale for every low-energy EFT loop.
