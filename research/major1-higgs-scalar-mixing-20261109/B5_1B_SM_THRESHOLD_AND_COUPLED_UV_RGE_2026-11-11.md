# B5-1b — SM-to-threshold input matching and coupled one-loop UV running

**Date:** 2026-11-11  
**Model:** original \(U(1)_{L_\mu-L_\tau}\) model with one complex \(S\) and two VLL Dirac fermions; no neutrino-sector extension.  
**Common threshold:** \(M_E=20\) TeV.  
**Status:** a reproducible one-loop leading-log numerical pass is complete. The result is provisional pending an independent automated RGE-generator cross-check and a higher-order uncertainty study.

## 1. Threshold logic: UV and EFT must be run on opposite sides

The VLLs are integrated out at the common threshold \(M_E\). Therefore the full UV beta functions are used only for \(\mu>M_E\), while the EFT beta functions are used for \(\mu<M_E\).

The correct sequence is:

1. Start from weak-scale \(\overline{\rm MS}\) SM inputs.
2. Run the low-energy EFT to \(M_E\). At the renormalizable dimension-four level used here, the matched EFT portal is set to zero at \(M_E\); hence the leading SM running of \(g_Y,g_2,g_3,y_t,\lambda_H\) is the appropriate first-pass boundary evolution.
3. Match the VLL Yukawas and \(U(1)_X\) coupling at \(M_E\).
4. Run the full UV theory upward from \(M_E\), using the coupled one-loop system below.
5. For a matching-scale choice below \(M_E\), use the EFT RGE; for a matching-scale choice above \(M_E\), use the UV RGE. Do not evolve the full UV theory down to \(m_h\).

This corrects the tempting but incorrect procedure of integrating the VLL-containing UV beta functions over the entire interval \(M_E\to m_h\).

## 2. Weak-scale input scheme

Use the PDG 2025 central values:
\[
M_t=172.56\ {\rm GeV},\quad
M_H=125.20\ {\rm GeV},\quad
M_W=80.369\ {\rm GeV},\quad
\alpha_s^{(5)}(M_Z)=0.1180.
\]
The top mass is the direct/MC mass average; its interpretation as a pole mass has an additional theory ambiguity. This first-pass run uses the central value and does not yet propagate that ambiguity.

The NNLO matching interpolants of Buttazzo et al. (arXiv:1307.3536), with the updated PDG central values inserted, are
\[
\begin{aligned}
\lambda_H(M_t)&=0.12604
+0.00206(M_H-125.15)
-0.00004(M_t-173.34),\\
y_t(M_t)&=0.93690
+0.00556(M_t-173.34)
-0.00042\frac{\alpha_s(M_Z)-0.1184}{0.0007},\\
g_2(M_t)&=0.64779
+0.00004(M_t-173.34)
+0.00011\frac{M_W-80.384}{0.014},\\
g_Y(M_t)&=0.35830
+0.00011(M_t-173.34)
+0.00020\frac{M_W-80.384}{0.014},\\
g_3(M_t)&=1.1666
+0.00314\frac{\alpha_s(M_Z)-0.1184}{0.0007}
-0.00046(M_t-173.34),
\end{aligned}
\]
where all masses in the interpolation formulae are in GeV and \(g_Y\) is in the non-GUT hypercharge convention \(Q=T_3+Y\).

This gives
\[
\begin{aligned}
\lambda_H(M_t)&=0.1261742,\\
y_t(M_t)&=0.9328032,\\
g_2(M_t)&=0.6476409,\\
g_Y(M_t)&=0.3579999,\\
g_3(M_t)&=1.1651645.
\end{aligned}
\]

## 3. SM running below the VLL threshold

For the first pass, retain the top Yukawa and use one-loop SM RGEs:
\[
16\pi^2\beta_{g_Y}=\frac{41}{6}g_Y^3,\quad
16\pi^2\beta_{g_2}=-\frac{19}{6}g_2^3,\quad
16\pi^2\beta_{g_3}=-7g_3^3,
\]
\[
16\pi^2\beta_{y_t}
=y_t\left(\frac92y_t^2-\frac{17}{12}g_Y^2
-\frac94g_2^2-8g_3^2\right),
\]
and
\[
\begin{aligned}
16\pi^2\beta_{\lambda_H}^{\rm SM}
={}&24\lambda_H^2
+\lambda_H(12y_t^2-9g_2^2-3g_Y^2)
-6y_t^4\\
&+\frac98g_2^4+\frac34g_2^2g_Y^2+\frac38g_Y^4.
\end{aligned}
\]

The numerical integration from \(M_t\) to \(M_E=20\) TeV gives
\[
\boxed{
\begin{array}{c|r}
\text{coupling at }20\text{ TeV}&\text{value}\\\hline
g_Y&0.3678265854\\
g_2&0.6232068405\\
g_3&0.9292986928\\
y_t&0.7674037247\\
\lambda_H&0.0592605784
\end{array}}
\]

For the top-dominant SM trace,
\[
\mathcal T_H^{\rm SM}\simeq3y_t^2=1.7667254302,
\]
and therefore
\[
D_{\rm SM}\equiv
2\mathcal T_H^{\rm SM}-\frac92g_2^2-\frac32g_Y^2
=1.5827658176.
\]
Bottom and direct electron Yukawa effects are neglected in this first-pass numerical input; they are small for this particular trace.

## 4. Matching of the scalar quartics at \(\mu=M_E\)

The VLL determinant also contains pure \(H^4\) and \(S^4\) terms. They generate the additive Yukawa-box pieces in the UV beta functions for \(\lambda_H\) and \(\lambda_S\). They must not be confused with finite threshold corrections.

For a single background direction, the heavy eigenvalue is \(M_E^2+x\), with \(x=|y|^2H^\dagger H\) or \(x=|\lambda|^2S^\dagger S\). The Coleman–Weinberg function is
\[
f(z)=z^2\left(\ln\frac{z}{\mu^2}-\frac32\right).
\]
The pure-quartic finite matching coefficient is proportional to
\[
\frac12f''(M_E^2)
=\ln\frac{M_E^2}{\mu^2},
\]
which vanishes at \(\mu=M_E\). The mixed \(H^\dagger HS^\dagger S\) coefficient instead involves
\[
-\frac{f'(M_E^2)}{M_E^2}+f''(M_E^2)=2
\quad(\mu=M_E),
\]
and gives the already established nonzero portal threshold.

Thus, in the common-mass \(\overline{\rm MS}\) matching convention at \(\mu=M_E\), the one-loop pure-quartic finite VLL thresholds vanish in this restricted determinant sector, while the portal finite threshold does not:
\[
\lambda_H^{\rm UV}(M_E)=\lambda_H^{\rm EFT}(M_E),\qquad
\lambda_S^{\rm UV}(M_E)=\lambda_S^{\rm EFT}(M_E),
\]
\[
\lambda_{HS}^{\rm UV}(M_E)=-\Delta\lambda_{HS}^{E},
\qquad \lambda_{HS}^{\rm EFT}(M_E)=0.
\]
This statement identifies \(M_E\) with the common running mass at the matching point. A pole-to-\(\overline{\rm MS}\) conversion for the heavy mass and a complete tadpole/VEV matching remain outside this first pass.

## 5. Full one-loop UV RGE system above \(M_E\)

The following equations use the non-GUT \(g_Y\) convention, diagonal Abelian kinetic terms at \(M_E\), and the common VLL threshold. The one-loop mixed trace is zero, \(\operatorname{Tr}(YX)=0\).

### 5.1 Gauge couplings

The two charged VLL Dirac singlets shift the hypercharge coefficient by \(2(4/3)\), while the \(U(1)_X\) spectrum has ten charged Weyl components and one complex scalar of charge \(Q_S=2\). Hence
\[
\boxed{
\begin{aligned}
16\pi^2\beta_{g_Y}&=\frac{19}{2}g_Y^3,\\
16\pi^2\beta_{g_2}&=-\frac{19}{6}g_2^3,\\
16\pi^2\beta_{g_3}&=-7g_3^3,\\
16\pi^2\beta_{g_X}&=8g_X^3.
\end{aligned}}
\]

### 5.2 Yukawa couplings

Define
\[
T_H=3y_t^2+y_\mu^2+y_\tau^2,\qquad
T_S=\lambda_\mu^2+\lambda_\tau^2.
\]
Then
\[
\begin{aligned}
16\pi^2\beta_{y_t}
&=y_t\left[
\frac92y_t^2+y_\mu^2+y_\tau^2
-\frac{17}{12}g_Y^2-\frac94g_2^2-8g_3^2
\right],\\
16\pi^2\beta_{y_\ell}
&=y_\ell\left[
\frac32y_\ell^2+T_H
-\frac{15}{4}g_Y^2-\frac94g_2^2-6g_X^2
\right],\\
16\pi^2\beta_{\lambda_\ell}
&=\lambda_\ell\left[
\frac32\lambda_\ell^2+T_S
-6g_Y^2-6g_X^2
\right],
\qquad \ell=\mu,\tau.
\end{aligned}
\]
The \(y_\ell\) and \(\lambda_\ell\) sectors connect different chiral VLL components. The mass-independent one-loop beta functions therefore have no \(y_\ell\lambda_\ell\) cross term. The scalar-wavefunction traces do couple the two flavors within each of the \(H\) and \(S\) sectors.

### 5.3 Scalar quartics

With \(V\supset\lambda_H(H^\dagger H)^2+\lambda_S(S^\dagger S)^2+\lambda_{HS}(H^\dagger H)(S^\dagger S)\),
\[
\begin{aligned}
16\pi^2\beta_{\lambda_H}
={}&24\lambda_H^2+2\lambda_{HS}^2\\
&+\lambda_H\left[12y_t^2+4(y_\mu^2+y_\tau^2)
-9g_2^2-3g_Y^2\right]\\
&-6y_t^4-2(y_\mu^4+y_\tau^4)\\
&+\frac98g_2^4+\frac34g_2^2g_Y^2+\frac38g_Y^4,
\\[2mm]
16\pi^2\beta_{\lambda_S}
={}&20\lambda_S^2+2\lambda_{HS}^2
-48g_X^2\lambda_S+96g_X^4\\
&+4\lambda_S(\lambda_\mu^2+\lambda_\tau^2)
-2(\lambda_\mu^4+\lambda_\tau^4),
\\[2mm]
16\pi^2\beta_{\lambda_{HS}}
={}&\lambda_{HS}\bigg[
12\lambda_H+8\lambda_S+4\lambda_{HS}
-\frac92g_2^2-\frac32g_Y^2-24g_X^2\\
&\hspace{27mm}
+2\left(3y_t^2+y_\mu^2+y_\tau^2
+\lambda_\mu^2+\lambda_\tau^2\right)
\bigg].
\end{aligned}
\]
The \(\lambda_H\) and \(\lambda_S\) equations are important additions to B5-1: the VLL Yukawa boxes that vanish in the *mixed* \(H^\dagger HS^\dagger S\) determinant coefficient do not vanish in the *pure* \(H^4\) and \(S^4\) coefficients.

The scalar mass relation used for the diagnostic scan is
\[
\lambda_S(M_E)=\frac{m_s^2}{2v_S^2}.
\]
This is the leading unmixed radial-mass relation, not a pole-mass inversion. It must not be used to classify the near-degenerate Higgs–singlet region or to replace the common tadpole/mass matching in B5-3.

## 6. Numerical beta functions at \(M_E=20\) TeV

The matching relations are
\[
y_\mu=y_\tau=\frac{\sqrt2M_E\theta_L}{v_h},\quad
\lambda_\ell=\frac{\sqrt2m_\ell}{\theta_Lv_S},\quad
g_X=\frac{m_X}{2v_S},
\quad \theta_L=10^{-2}.
\]
They give \(y_\mu=y_\tau=1.1487397956\).

The table below uses the same \(m_s\) diagnostic grid for both benchmarks. The beta functions are derivatives with respect to \(\ln\mu\), including the factor \(1/(16\pi^2)\).

| \(m_s\) [GeV] | Benchmark | \(\lambda_S(M_E)\) | \(\beta_{\lambda_S}(M_E)\) | \(\beta_{\lambda_H}(M_E)\) | \(\beta_{\lambda_{HS}}(M_E)\) |
|---:|:---:|---:|---:|---:|---:|
| 10 | A | 0.0099505 | -1.99627 | -0.0496727 | +0.0448414 |
| 50 | A | 0.248762 | -1.91252 | -0.0496727 | +0.0473913 |
| 100 | A | 0.995047 | -1.55770 | -0.0496727 | +0.0553597 |
| 150 | A | 2.23886 | -0.652827 | -0.0496727 | +0.0686404 |
| 10 | B | 0.00050391 | -0.00506027 | -0.0502338 | +0.000585078 |
| 50 | B | 0.0125976 | -0.00488133 | -0.0502338 | +0.000591617 |
| 100 | B | 0.0503905 | -0.00408335 | -0.0502338 | +0.000612053 |
| 150 | B | 0.113379 | -0.00194940 | -0.0502338 | +0.000646112 |

At \(m_s=100\) GeV, the decomposition of \(\beta_{\lambda_H}\) is
\[
\begin{array}{c|rr}
\text{contribution}&A&B\\\hline
\text{scalar}&+1.09634\times10^{-3}&+5.35175\times10^{-4}\\
\text{Yukawa wavefunction}&+6.61369\times10^{-3}&+6.61369\times10^{-3}\\
\text{Yukawa boxes}&-5.72863\times10^{-2}&-5.72863\times10^{-2}\\
\text{gauge linear}&-1.46407\times10^{-3}&-1.46407\times10^{-3}\\
\text{gauge quartic}&+1.36768\times10^{-3}&+1.36768\times10^{-3}
\end{array}
\]
The SM-only one-loop value at \(M_E\) is
\[
\beta_{\lambda_H}^{\rm SM}(M_E)=-1.00880\times10^{-2}.
\]
The new VLL Yukawa boxes therefore make the Higgs quartic run substantially more negative immediately above the threshold.

## 7. Coupled UV running: perturbativity and quartic-stability diagnostics

The full coupled system was integrated upward from \(M_E\). The following are formal one-loop diagnostics, not a final vacuum-lifetime calculation.

### 7.1 Benchmark A

At the matching point,
\[
\lambda_\tau=3.5449077=\sqrt{4\pi},
\qquad
\frac{\lambda_\tau^2}{16\pi^2}=0.0795775.
\]
Thus Benchmark A already saturates the adopted Yukawa perturbativity condition \(\lambda_\tau^2\le4\pi\). Moreover,
\[
\beta_{\lambda_\tau}(M_E)=+0.68734,
\]
so the coupling grows immediately above \(M_E\). At \(1.05M_E\), the one-loop trajectory already gives \(\lambda_\tau\simeq3.58\), above the adopted bound. Consequently, no finite upward UV interval is perturbative under the strict \(\lambda_\tau^2\le4\pi\) criterion.

The formal one-loop \(\lambda_S\) zero-crossing scales are:
\[
\begin{array}{c|rrrr}
m_s\,[{\rm GeV}]&10&50&100&150\\\hline
\mu(\lambda_S=0)\,[{\rm TeV}]
&20.10&22.57&31.49&52.39
\end{array}
\]
Because the Yukawa perturbativity boundary is saturated at \(M_E\), these later zero crossings are diagnostic only and must not be interpreted as controlled predictions.

### 7.2 Benchmark B

Benchmark B has
\[
\lambda_\tau(M_E)=0.7977332,\qquad
\beta_{\lambda_\tau}(M_E)=+0.00364439.
\]
Its \(\lambda_S\) remains positive throughout the upward scan to \(70\) TeV for \(m_s=50,100,150\) GeV. For the very low \(m_s=10\) GeV point, the small initial \(\lambda_S\) is driven through zero at approximately \(22.09\) TeV.

However, the Higgs quartic crosses zero at
\[
\mu(\lambda_H=0)\simeq57.90\ {\rm TeV}.
\]
The corresponding Benchmark-A formal crossing is approximately \(58.6\) TeV, but is outside the strict perturbative domain already at the threshold.

At \(2M_E=40\) TeV, Benchmark B with \(m_s=100\) GeV gives
\[
\lambda_H\simeq0.02200,\quad
\lambda_S\simeq0.04751,\quad
\lambda_{HS}\simeq0.01110,\quad
\lambda_\tau\simeq0.80026.
\]
Thus B remains perturbative and has positive quartics over this factor-two upward interval in the present one-loop diagnostic.

### 7.3 Physical interpretation

The quartic potential requires \(\lambda_H\ge0\), \(\lambda_S\ge0\), and the usual copositivity condition involving \(\lambda_{HS}\). Since the portal benchmarks are positive, a negative \(\lambda_H\) or \(\lambda_S\) signals loss of absolute quartic boundedness along the corresponding field direction.

This does **not** by itself prove that the electroweak vacuum is excluded: metastability, the effective potential, two-loop running, scalar threshold matching, and the exact scalar mass/tadpole scheme must be treated before making a physical vacuum-lifetime statement.

The robust first-pass observations are:
- Benchmark A has no upward perturbative headroom under the adopted \(\lambda_\tau^2\le4\pi\) criterion.
- Benchmark A's \(\lambda_S\) beta is strongly negative because the \(-2\lambda_\tau^4/(16\pi^2)\) box term is about \(-2\) at the threshold.
- Benchmark B is substantially better controlled in the singlet/Yukawa sector, but its large \(y_\mu=y_\tau\simeq1.15\) drives \(\lambda_H\) down rapidly above \(M_E\).
- A complete high-scale stability claim is premature until two-loop and matching uncertainties are included.

## 8. Symbolic and numerical checks

The companion script checks:
1. NNLO weak-scale matching interpolants and the one-loop SM evolution to \(M_E\).
2. The one-loop gauge coefficients \(b_Y=19/2\) and \(b_X=8\).
3. The zero one-loop Abelian kinetic-mixing trace \(\operatorname{Tr}(YX)=0\).
4. The Coleman–Weinberg pure-quartic finite threshold \(f''(M_E^2)/2=0\) at \(\mu=M_E\).
5. The mixed finite portal coefficient \(-f'(M_E^2)/M_E^2+f''(M_E^2)=2\).
6. The coupled UV evolution and the tabulated zero crossings.

The equations are derived from the stated chiral spectrum and standard one-loop gauge/Yukawa/scalar renormalization formulae. An independent SARAH/PyR@TE or diagrammatic cross-check of the *complete model-specific* RGE system has not yet been run. This is a required acceptance gate before promoting the running to a final model-level conclusion.

## 9. B5-1b acceptance and next work

**B5-1b first-pass numerical calculation is complete; final RGE acceptance remains provisional.**

Completed:
- PDG 2025 central inputs fixed.
- NNLO weak-scale matching values obtained.
- SM-only one-loop running to \(M_E\) performed.
- Full one-loop UV beta system for gauge, top/VLL Yukawas, and all three quartics implemented.
- Benchmark A/B beta decompositions and upward running diagnostics generated.
- The threshold-side logic has been corrected: UV running above \(M_E\), EFT running below \(M_E\).

Still required:
1. Independent RGE-generator/diagrammatic validation of the model-specific VLL Yukawa and scalar-quartic beta functions.
2. A two-loop SM running cross-check below \(M_E\), and a quantified top-mass/matching-input uncertainty.
3. B5-2: derive the EFT running below \(M_E\), including the complete retained operator basis and mixing.
4. B5-3: close the common tadpole, VEV, and \(h,s\) field-renormalization scheme.
5. B5-4: only then perform the factor-two matching-scale comparison, using EFT running for \(M_E/2\) and UV running for \(2M_E\).

**Decision:** Benchmark B is the better-controlled reference for the next matching-scale study. Benchmark A should remain in the comparison as a perturbativity-boundary diagnostic, not be silently treated as an equally controlled UV trajectory.
