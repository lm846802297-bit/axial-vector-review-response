# Major Point 1 — direct singlet-like scalar widths and narrow-width audit

**Scope:** tree-level \(s\to A'A'\), \(s\to\mu^+\mu^-\), \(s\to\tau^+\tau^-\) in the original one-singlet model, using the two existing benchmarks. This is a direct-width subset; it is not the complete total width of the mixed scalar system.

From \(|D_\mu S|^2\), \(m_{A'}=2g_Xv_s\), and the scalar Yukawa matrices in the alignment/decoupling limit:
\[
\Gamma(s\to A'A')=
\frac{m_s^3}{32\pi v_s^2}
(1-4x+12x^2)\sqrt{1-4x},\quad x=\frac{m_{A'}^2}{m_s^2},
\]
when \(m_s>2m_{A'}\), and
\[
\Gamma(s\to\ell^+\ell^-)=
\frac{m_\ell^2m_s}{8\pi v_s^2}
\left(1-\frac{4m_\ell^2}{m_s^2}\right)^{3/2}
\]
when \(m_s>2m_\ell\).

## Numerical results

| \(m_s\) [GeV] | A: \(\Gamma_{A'A'}\) [GeV] | A: \(\Gamma_{\mu\mu+\tau\tau}\) [GeV] | B: \(\Gamma_{A'A'}\) [GeV] | B: \(\Gamma_{\mu\mu+\tau\tau}\) [GeV] |
|---:|---:|---:|---:|---:|
| 10 | 0 | \(2.051\times10^{-4}\) | 0 | \(1.038\times10^{-5}\) |
| 100 | 1.86433 | \(2.504\times10^{-3}\) | 0 | \(1.268\times10^{-4}\) |
| 125.25 | 3.74368 | \(3.1386\times10^{-3}\) | 0 | \(1.5894\times10^{-4}\) |
| 150 | 6.50529 | \(3.7601\times10^{-3}\) | 0.122594 | \(1.9042\times10^{-4}\) |
| 200 | 15.6009 | \(5.0153\times10^{-3}\) | 0.449208 | \(2.5398\times10^{-4}\) |
| \(m_s^{\max}\) | 88.4219 | \(8.9144\times10^{-3}\) | 391.0419 | \(2.0063\times10^{-3}\) |

Here \(m_s^{\max}=\sqrt{8\pi}v_s\), corresponding to the adopted tree-level perturbativity criterion \(\lambda_S=4\pi\).

At the perturbativity ceiling,
\[
\frac{\Gamma(s\to A'A')}{m_s}
\longrightarrow \frac{m_s^2}{32\pi v_s^2}
=\frac14
\quad (m_s\gg m_{A'}),
\]
up to the small vector-mass phase-space correction. Numerically the total direct-width ratios are 0.24884 (A) and 0.24763 (B). Thus the perturbativity upper endpoint is not a narrow-resonance regime. A narrow-width treatment should not be extrapolated to the entire formal mass interval.

At the Higgs pole, \(2m_{A'}<m_h\) for A, while \(2m_{A'}>m_h\) for B. Hence the singlet component of a Higgs-like pole can feed \(A'A'\) in A but not in B. The coefficient at \(m_h\) is
\[
\Gamma(h_{\rm pole}\to A'A')\simeq
3.74368~{\rm GeV}\times |\text{singlet amplitude}|^2
\]
in the small-admixture approximation for A. This must be evaluated with the properly normalized pole residue and physical vertex in a complete calculation; the eigenvector ratio alone is only a diagnostic.

## Important no-double-counting and matching caveat

The UV portal parameter is chosen \(O(\hbar)\) to cancel the finite hard threshold in the reference matching. Therefore one must not insert the uncancelled UV cubic \(g_{hss}=\lambda_{HS}^{UV}v_h\) as a physical low-energy \(h\to ss\) amplitude without adding the corresponding hard VLL vertex correction and matching terms. The same warning applies to portal-induced \(h\to A'A'\) mixing. Physical amplitudes must be computed in either the full UV theory or the matched EFT, not by mixing vertices from the two descriptions.

The table includes only the direct singlet-like tree-level channels above. It omits mixing-induced \(WW,ZZ,hh\), off-shell multi-body channels, scalar-loop corrections, and higher-order corrections. It is therefore a lower-level width audit, not a complete \(\Gamma_s\) prediction.
