# Major Point 1.3 — exact mass-eigenstate one-loop \(h\)-\(s\) mixing

**Date:** 2026-10-27  
**Status:** The one-loop charged-lepton/VLL contribution has been evaluated numerically in the full \(2\times2\) mass-eigenstate basis at two stated benchmarks. The finite hard momentum dependence agrees with the leading derivative matching result at \(6.11\times10^{-4}\) relative. The physical interpretation remains conditional on the portal boundary and the scalar pole/constraint treatment.

## 1. Meeting request and correct diagram set

The 2026-10-23 meeting transcripts, especially transcript 01 at 14:22–17:32 and 25:40–26:56, explicitly requested a quantitative one-loop estimate rather than a qualitative assertion that mixing is negligible.

The meeting mentioned possible \(W\)/top loops, but the model's leading one-loop off-diagonal \(h\)-\(s\) two-point function is the charged-lepton/VLL fermion loop in the mass-eigenstate basis. In the zero-tree-level-mixing setup, the singlet radial mode \(s\) has no tree-level \(sWW\) or \(s\bar t t\) vertex. Thus there is no direct one-loop graph with an \(hWW\) or \(h\bar t t\) vertex and a matching \(sWW\) or \(s\bar t t\) vertex. Such a vertex is absent. The direct \(W\)/top one-loop contribution to \(\Pi_{hs}\) is therefore zero under these assumptions; the relevant one-loop contribution is the full \(\mu,\tau,E_\mu,E_\tau\) fermion sector. A different portal boundary, nonzero tree-level scalar mixing, or extra field content would require a separate diagram census.

## 2. Inputs and conventions

The model mass matrix and VEV conventions are
\[
\mathcal M_\ell(h,s)=
\begin{pmatrix}
0&y_\ell(v_h+h)/\sqrt2\\
\lambda_\ell(v_s+s)/\sqrt2&M_{E_\ell}
\end{pmatrix},\qquad
H^0=(v_h+h)/\sqrt2,\quad S=(v_s+s)/\sqrt2.
\]
For \(\tau\), the original interaction contains \(S^*\); the radial real \(s\) vertex is the same for real parameters.

The gauge-basis vertices are
\[
\Gamma_h^\ell=\begin{pmatrix}0&y_\ell/\sqrt2\\0&0\end{pmatrix},\qquad
\Gamma_s^\ell=\begin{pmatrix}0&0\\\lambda_\ell/\sqrt2&0\end{pmatrix}.
\]
A numerical SVD diagonalizes the full mass matrix and constructs \(G_h=U_L^T\Gamma_hU_R\) and \(G_s=U_L^T\Gamma_sU_R\). All four internal pairs—heavy-heavy, heavy-light, light-heavy, light-light—are included for both \(\mu\) and \(\tau\).

The source convention is
\[
\Gamma_{\mathrm{inv}}(p^2)=p^2\mathbf1-\mathcal M_{\mathrm{loc}}^2+\Pi_{\mathrm{RC}}(p^2),
\]
and the Plan-B/Plan-C convention is \(\Pi_B=-\Pi_{\mathrm{RC}}\). The finite PV functions use
\[
\bar A_0(m^2)=m^2\left(1-\ln\frac{m^2}{\mu_R^2}\right),\quad
\bar B_0=-\int_0^1dx\ln\frac{xm_i^2+(1-x)m_j^2-x(1-x)p^2-i0}{\mu_R^2},
\]
with \(\mu_R=M_E=20\) TeV.

The inputs are those of the existing Plan-C-lite benchmarks: \(m_h=125.25\) GeV, \(v_h=246.22\) GeV, \(M_E=20\) TeV, \(\theta_{\mu L}=\theta_{\tau L}=10^{-2}\), and leading-seesaw Yukawa relations.
- **A, open \(A'A'\) at \(m_s=m_h\):** \(v_s=70.886458\) GeV, \(m_{A'}=10\) GeV, \(g_X=0.0705353\).
- **B, closed \(A'A'\) at \(m_s=m_h\):** \(v_s=315\) GeV, \(m_{A'}=63\) GeV, \(g_X=0.1\).

Because the Yukawas are selected from leading-seesaw relations, exact singular values differ slightly from the input physical muon/tau masses. This is recorded in the run output; it is not hidden by rounding.

## 3. One-loop formula

For \(\phi_a,\phi_b\in\{h,s\}\), define
\[
C_{ab}^{ij}=(G_a)_{ij}(G_b)_{ij}^{*}+(G_a)_{ji}^{*}(G_b)_{ji},
\quad
D_{ab}^{ij}=(G_a)_{ij}(G_b)_{ji}+(G_a)_{ji}^{*}(G_b)_{ij}^{*},
\]
\[
K_{ij}=A_0(m_i^2)+A_0(m_j^2)+(m_i^2+m_j^2-p^2)B_0(p^2;m_i^2,m_j^2).
\]
The one-loop fermion self-energy in the source convention is
\[
\Pi_{ab}^{F,\ell}(p^2)=
-\frac{1}{16\pi^2}\sum_{i,j=1}^{2}
\left[C_{ab}^{ij}K_{ij}+2m_im_jD_{ab}^{ij}B_0(p^2;m_i^2,m_j^2)\right].
\]
This is the mass-eigenstate formula recorded in the primary research source, §274.2. Unlike the earlier algebra-only check, the new script numerically evaluates the finite \(A_0/B_0\) integrals.

## 4. Exact full-loop result and EFT soft subtraction

The full-theory self-energy contains the local portal-threshold constant and is not itself the matched physical mixing input. To isolate the momentum-dependent hard term, the script computes
\[
\Delta\Pi_{\mathrm{hard}}(m_h^2)=
[\Pi_B^{\mathrm{full}}(m_h^2)-\Pi_B^{\mathrm{full}}(0)]
-[\Pi_B^{\mathrm{light,exact}}(m_h^2)-\Pi_B^{\mathrm{light,exact}}(0)],
\]
where the light-light term uses the exact light-state Yukawas from the same SVD. This avoids double counting the light-lepton cut.

| Quantity | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\Pi_{\mathrm{RC}}^{\mathrm{full}}(0)\) [GeV²] | \(3677.945520\) | \(827.671526\) |
| \(\Pi_{\mathrm{RC}}^{\mathrm{full}}(m_h^2)\) [GeV²] | \(3678.359749+0.113133310i\) | \(827.764742+0.025459110i\) |
| Full \(\Pi_B(m_h^2)-\Pi_B(0)\) [GeV²] | \(-0.414229795-0.113133310i\) | \(-0.093216771-0.025459110i\) |
| Exact light-light difference [GeV²] | \(-0.438260239-0.113133310i\) | \(-0.098624495-0.025459110i\) |
| **Exact hard momentum difference** [GeV²] | **\(+0.024030444\)** | **\(+0.005407724\)** |
| Leading derivative matching prediction [GeV²] | \(+0.024045135\) | \(+0.005411030\) |
| Relative difference | \(-6.11\times10^{-4}\) | \(-6.11\times10^{-4}\) |

At \(\mu_R=M_E\), the leading source-aligned hard derivative is
\[
\Pi_{B,\mathrm{hard}}'(0)=\frac{q}{24\pi^2},\qquad
q=\sum_{\ell=\mu,\tau}\frac{2m_\ell^2}{v_hv_s}.
\]
The exact mass-eigenstate calculation reproduces it within \(0.0611\%\) at both points. The residual is retained as a finite-mixing/leading-seesaw correction rather than rounded away.

The full mass-eigenstate sum also gives the \(p^2\) UV-pole coefficient consistent with zero, the local UV coefficient consistent with zero at numerical precision, and an absorptive part equal to the light-light cut. The hard momentum difference has no residual imaginary part below the heavy threshold.

The zero-momentum hard comparator agrees with \(-v_hv_s\Delta\lambda_{HS}^{E}\) from the leading-seesaw portal threshold to \(1.79\times10^{-4}\) relative. The residual is consistent with using leading-seesaw Yukawas alongside exact mass diagonalization. The portal threshold and the momentum-dependent derivative are separate contributions; the same constant threshold is not added twice.

## 5. Matched self-energy and mixing magnitude

The reference condition is \(\lambda_{HS}^{\mathrm{EFT}}(M_E)=0\), which requires \(\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E}\) at the displayed order. This is a benchmark input, not a symmetry prediction. Combining the exact hard momentum difference with the established low-energy EFT soft contribution gives:

| Result | Benchmark A | Benchmark B |
|---|---:|---:|
| \(\Pi_{hs}^{\mathrm{matched}}(m_h^2)\) [GeV²] | \(-0.413277859-0.113173709i\) | \(-0.093002551-0.025468201i\) |
| \(\Gamma_s(m_h)\) | \(3.746814\) GeV | \(0.158940\) MeV |
| \(\left|\Pi_{hs}/(a-b)\right|\), \(m_s=m_h\) | \(9.14\times10^{-4}\) | \(0.19685\) |
| \(2\left|\Pi_{hs}/(a-b)\right|\) diagnostic | \(1.83\times10^{-3}\) | \(0.39369\) |

Here \(a=m_h^2-i m_h\Gamma_h\) and \(b=m_s^2-i m_s\Gamma_s\). The quantity \(2|\Pi_{hs}/(a-b)|\) is a width-regulated mixing diagnostic, not a universal real mixing angle or an observable by itself.

| \(m_s\) [GeV] | A: \(2|\Pi/(a-b)|\) | B: \(2|\Pi/(a-b)|\) |
|---:|---:|---:|
| 10 | \(5.50\times10^{-5}\) | \(1.24\times10^{-5}\) |
| 50 | \(6.50\times10^{-5}\) | \(1.46\times10^{-5}\) |
| 100 | \(1.51\times10^{-4}\) | \(3.39\times10^{-5}\) |
| 124.5 | \(1.73\times10^{-3}\) | \(1.03\times10^{-3}\) |
| 125.0 | \(1.83\times10^{-3}\) | \(3.08\times10^{-3}\) |
| 125.25 | \(1.83\times10^{-3}\) | \(0.39369\) |
| 125.5 | \(1.80\times10^{-3}\) | \(3.08\times10^{-3}\) |
| 150 | \(1.25\times10^{-4}\) | \(2.83\times10^{-5}\) |

The two benchmarks have different physical behavior:
- **Open \(A'A'\):** the singlet-like scalar is broad near \(m_s=m_h\), with \(\Gamma_s\simeq3.75\) GeV. The diagnostic at exact degeneracy is about \(1.8\times10^{-3}\).
- **Closed \(A'A'\):** both poles are narrow. At exact degeneracy the diagnostic reaches about \(0.394\), so a blanket statement that mixing is negligible across the full \(m_s\) range is not justified. With the operational threshold \(2|\Pi/(a-b)|\geq0.1\), the width-regulated band is approximately \(|m_s-m_h|\lesssim7.45\) MeV for this benchmark.

This band is a theoretical diagnostic, not an experimental exclusion interval. A model-specific two-pole lineshape/signal-strength analysis and direct-search recast are still required before assigning allowed/excluded status.

## 6. Reproducibility and limits

- Script: [higgs_portal_exact_mass_eigenstate_one_loop.py](higgs_portal_exact_mass_eigenstate_one_loop.py).
- Captured output: [higgs_portal_exact_mass_eigenstate_one_loop_validation.txt](higgs_portal_exact_mass_eigenstate_one_loop_validation.txt).
- The script computes the full SVD and all four internal mass-state pairs for both \(\mu\) and \(\tau\), evaluates finite \(A_0/B_0\) functions numerically, and asserts the UV-pole structure, absorptive-part subtraction, hard derivative, and threshold scale.
- The exact committed script was compiled and executed in the local Linux environment: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. Its Git blob SHA-1 is `b5228e49f58834f6f5a2cb84dfc61e7a69749db5`, matching the branch source. `py_compile` passed, runtime exit code was 0, and all in-script assertions passed for both benchmarks.
- This is an independent numerical implementation of the mass-eigenstate formula, **not** a FeynArts/FeynCalc run. External diagram-package reproduction still requires the model-specific file and compatible Mathematica/FeynArts/FeynCalc.
- The result uses the leading-seesaw benchmark and the conditional matched-portal choice. A different renormalized portal boundary changes the local mixing term and the physical prediction.

## 7. Conclusion

The requested one-loop fermion-loop estimate is now quantitatively completed for two stated UV benchmarks, including the finite-momentum hard contribution and its combination with the EFT soft loop. The exact mass-eigenstate calculation reproduces the leading derivative matching coefficient at \(6.11\times10^{-4}\) relative and passes the recorded UV/absorptive checks.

It does **not** justify claiming that \(h\)-\(s\) mixing is negligible across the entire scalar-mass range. It is small away from degeneracy and in the open-\(A'A'\) benchmark, but it becomes non-negligible in the narrow-width near-degenerate benchmark. The portal boundary remains an independent input, and the full pole-scheme calculation and experimental recast remain open.
