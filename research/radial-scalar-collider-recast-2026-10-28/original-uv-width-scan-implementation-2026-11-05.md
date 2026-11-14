# Original one-VEV UV radial-scalar width scan: implementation note

> Historical design stage: the later bounded double-virtual calculation and updated scan are documented in [the width audit](original-uv-width-scan-and-belleii-width-audit-2026-11-05.md) and [bounded recast](BOUNDED_WIDTH_RECAST_2026-11-09.md). Statements below that the four-body term is not yet included describe this earlier stage.

**Date:** 2026-11-05  
**Scope:** original paper's single-VEV \(S+\mathrm{VLL}\) model only.  
**Benchmark assumptions:** negligible Higgs portal; decoupled VLLs; \(\theta_{\mu R}=\theta_{\tau R}=10^{-2}\) for the \(A'\) decay/cascade module; no electron Yukawa, extra scalar, extra VEV, or right-handed neutrino.

## 1. Width formula audit

Using
\[
m_{A'}=2g_Xv_s,\qquad m_s^2=2\lambda_Sv_s^2,\qquad
y_{s\ell\ell}=m_\ell/v_s,
\]
the tree-level charged-lepton widths are
\[
\Gamma_{\ell\ell}=\frac{m_\ell^2m_s}{8\pi v_s^2}
\left(1-\frac{4m_\ell^2}{m_s^2}\right)^{3/2},
\quad \ell=\mu,\tau.
\]

The original canonical radial-mode interaction is
\[
\mathcal L\supset \frac{m_{A'}^2}{v_s}sA'_\mu A'^\mu.
\]
With the identical-vector symmetry factor and the longitudinal-polarization contribution, this gives
\[
\Gamma_{A'A'}=\frac{m_s^3}{32\pi v_s^2}
\sqrt{1-4r_A}(1-4r_A+12r_A^2),
\quad r_A=m_{A'}^2/m_s^2,
\]
for \(m_s>2m_{A'}\). This is the normalization already implemented in radial_scalar_widths.py and its threshold test.

The leading \(\gamma\gamma\) contribution from muon and tau loops is also retained in the two-body width sum. The electron direct Yukawa is absent in the original \(U(1)_{L_\mu-L_\tau}\) model. Heavy-VLL loop terms are omitted only under the declared decoupling benchmark.

## 2. Existing and new implementation

Existing modules reused:

- radial_scalar_widths.py: \(\mu\mu,\tau\tau,A'A'\), and leading \(\gamma\gamma\) widths; computes \(v_s,\lambda_S\), partial-width fractions, and included-width lifetime diagnostics.
- off_shell_cascades.py: \(s\to A'A'^*\to A' f\bar f\) in the region \(m_s/2\leq m_{A'}<m_s\), with \(f=\nu_\mu,\nu_\tau,\mu,\tau\), using the original axial-dominant charged-lepton couplings and running \(A'\) width.

New files:

- scan_original_uv_widths.py: logarithmic scan over \(m_s,m_{A'},g_X\); records every partial width, \(\Gamma_s/m_s\), included-width \(c\tau\), \(\lambda_S\), \(A'\) decay branching fractions, and explicit completeness flags.
- test_scan_original_uv_widths.py: tests the on-shell, one-on-shell/one-virtual, and two-virtual regimes, the benchmark width ratio, and the absence of an electron Yukawa.

Default scan window follows the already established phenomenology window:
\[
m_s\in[0.212,10]\ {\rm GeV},\quad
m_{A'}\in[10^{-3},10^2]\ {\rm GeV},\quad
g_X\in[10^{-6},10^{-1}].
\]
The default grid is \(48\times48\times32\). It is a diagnostic scan, not a claim that every point is experimentally or theoretically viable.

## 3. Crucial completeness partition

| Region | Scalar decay treatment | Status |
|---|---|---|
| \(m_{A'}<m_s/2\) | On-shell \(s\to A'A'\), followed by on-shell \(A'\) decays | Included at declared tree level |
| \(m_s/2\leq m_{A'}<m_s\) | One on-shell and one virtual \(A'\): three-body \(s\to A'f\bar f\) | Included by off_shell_cascades.py |
| \(m_{A'}\geq m_s\) | Both \(A'\) legs virtual: four-body final states | Not yet included; branching fractions flagged incomplete |

In addition, the declared benchmark neglects Higgs-portal-induced widths and non-decoupled VLL effects. These are assumptions, not symmetry protections. Consequently, the script never marks the last region as complete and never converts an incomplete partial-width sum into a physical lifetime or complete branching fractions.

The script's default \(\Gamma_s/m_s<10^{-2}\) label is only a configurable diagnostic. It is not asserted to be Belle II's detector-resolution criterion. A proper Belle II narrow-resonance check must compare the natural width and lifetime against the experiment's mass resolution and prompt-selection assumptions.

## 4. Hand-checked benchmark points

The following values were evaluated independently from the analytic two-body formulas, including the leading muon/tau-loop \(\gamma\gamma\) width. They are diagnostic examples, not results of the full logarithmic grid scan.

| \(m_s\) (GeV) | \(m_{A'}\) (GeV) | \(g_X\) | \(v_s\) (GeV) | \(\lambda_S\) | \(\Gamma_s/m_s\) | \(BR(A'A')\) |
|---:|---:|---:|---:|---:|---:|---:|
| 4.0 | 0.5 | 0.1 | 2.5 | 1.28 | \(2.5202\times10^{-2}\) | 0.9201 |
| 4.0 | 1.9 | 0.1 | 9.5 | 0.08864 | \(5.2959\times10^{-4}\) | 0.7366 |
| 4.0 | 2.1 | 0.1 | 10.5 | 0.07256 | \(1.1421\times10^{-4}\) | 0 |
| 4.0 | 10.0 | 0.1 | 50.0 | 0.00320 | \(5.0368\times10^{-6}\) | 0 |

For \(m_{A'}=0.5\) GeV, the on-shell \(A'A'\) channel accounts for about 92% of the included scalar width. This demonstrates why a two-lepton-only branching-ratio translation can fail badly when \(s\to A'A'\) is open.

For the second point, \(m_{A'}=1.9\) GeV is just below \(m_s/2=2\) GeV. The two-body \(A'A'\) channel is open but phase-space suppressed; its branching fraction remains about 74%. For \(m_{A'}=2.1\) GeV, the two-body channel is closed and the one-on-shell/one-virtual three-body region applies. The quoted row's \(\Gamma_s/m_s\) is the analytic two-body sum only and must not be mistaken for the complete three-body-inclusive scan result.

At fixed \(m_s,m_{A'}\), all these leading widths scale as \(g_X^2\) through \(1/v_s^2\); the branching fractions are therefore independent of \(g_X\) in this restricted benchmark, while \(\Gamma_s/m_s\) and the inverse lifetime scale as \(g_X^2\). The three-body cascade also has its own propagator dependence and is evaluated separately by the numerical integration module.

## 5. What remains before a physical Belle II reinterpretation

1. Execute the new full grid scan and inspect convergence of the three-body quadrature.
2. Add and validate the two-virtual-\(A'\) four-body widths for \(m_{A'}\geq m_s\), or retain those points as unclassified.
3. Compare \(\Gamma_s\) and \(c\tau_s\) with Belle II's actual mass resolution and prompt/displaced selection assumptions; do not substitute a generic \(\Gamma/m_s\) threshold.
4. Assess portal-induced scalar widths under the already adopted portal benchmark and the near-degenerate \(h\)-\(s\) caveat.
5. Assess whether finite VLL effects alter the loop-induced \(\gamma\gamma\) width for the chosen \(M_E\) benchmark.
6. Only then perform the separate four-muon and tau-pair limit translations.

No formal referee-response text is changed by this implementation note.
