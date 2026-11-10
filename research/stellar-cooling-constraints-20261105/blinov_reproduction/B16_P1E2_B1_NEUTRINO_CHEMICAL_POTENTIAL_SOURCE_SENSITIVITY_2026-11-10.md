# P1-E2: B.1 source sensitivity to neutrino chemical potentials

Date: 2026-11-10  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`  
Benchmark: \(m_V=10\) MeV, pure vector, \(s18.8\)-SFHo-MUONS, \(t_{\rm pb}=1\) s  
Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`

## 1. Question

The weak-coupling endpoint is optically thin to good accuracy, so its Fig. 7 deficit is a B.1 source-side issue. The reconstructed \(\mu_{\nu_\mu}(r)\) profile has weaker independent provenance than \(T(r)\) and \(\mu_\mu/T\). The P1-B.2 audit had already found that \(\pm10\%\) changes in \(\mu_{\nu_\mu}\) alter the 210--510 MeV escaped B.2 band by less than \(0.03\%\), but that result held the B.1 source fixed.

This audit therefore varies \(\mu_{\nu_\mu}\) inside the B.7 production kernel and recomputes the full optically-thin B.1 source. It also tests the paper's \(\mu_{\nu_\tau}=0\) assumption separately.

## 2. Method

The local one-flavour B.7 rate is evaluated as
\[
\Gamma_{\nu\bar\nu\to V}^{\rm prod}
=\frac{m_V^2}{8\pi\omega}
\frac{A(\mu_\nu;\omega,T,v)}{e^{\omega/T}-1},
\]
where \(A=1-\langle f_\nu f_{\bar\nu}\rangle\) is evaluated with the analytic Fermi-pair angular average. The two active flavours are summed as
\[
\Gamma_{\nu,{\rm total}}^{\rm prod}
\propto A(\mu_{\nu_\mu})+A(\mu_{\nu_\tau}).
\]
The B.1 source also includes the unchanged B.14--B.16 semi-Compton contribution. At \(m_V=10\) MeV, inverse dimuon decay is closed.

The higher-resolution calculation uses:
- 200 source-radius Gauss nodes over \([0,5,8,10,12,15,18,20,22,24,25]\) km;
- 320 logarithmic base energy nodes from \(m_V+10^{-5}\) to \(m_V+2000\) MeV, plus the exact \(m_V/N(r)\) threshold knots;
- piecewise-linear energy weights with the radius-dependent lower limit;
- 128-point Gauss-Legendre evaluation of \(n_\mu F_{\rm deg}\), using \(p=40t/(1-t)\).

A 100-radius/160-base-energy calculation is retained as a joint refinement check. The coupling is applied once, outside the local rates. No B.2 opacity is varied in this source-only test.

## 3. Global \(\mu_{\nu_\mu}\) sensitivity

The higher-resolution baseline has
\[
L_{\rm thin}^{\rm B.1}/g^2
=4.3074474\times10^{70}\ {\rm erg\,s^{-1}},
\]
with \(67.926\%\) from neutrino inverse decay and \(32.074\%\) from semi-Compton. The \(8\)--\(15\) km region supplies \(79.652\%\) of the total B.1 source.

| Global \(\mu_{\nu_\mu}\) variation | Change in total B.1 source |
|---|---:|
| \(\mu_{\nu_\mu}\to0.9\mu_{\nu_\mu}\) | \(+0.1985\%\) |
| \(\mu_{\nu_\mu}\to1.1\mu_{\nu_\mu}\) | \(-0.2096\%\) |
| \(\mu_{\nu_\mu}\to0.7\mu_{\nu_\mu}\) | \(+0.5554\%\) |
| \(\mu_{\nu_\mu}\to1.3\mu_{\nu_\mu}\) | \(-0.6559\%\) |
| \(\mu_{\nu_\mu}\to0\) | \(+1.1737\%\) |
| \(\mu_{\nu_\mu}\to-\mu_{\nu_\mu}\) | \(0\) |

The exact sign-flip invariance is expected: the neutrino-pair occupation product entering the isotropic B.7 kernel is even in the chemical potential. The nonzero sensitivity is to \(|\mu_{\nu_\mu}|\), not its sign.

The same calculation at lower resolution gives \(+0.1985\%/-0.2096\%\) for the \(\pm10\%\) tests and \(+0.5555\%/-0.6560\%\) for the \(\pm30\%\) tests. The source response is stable under the joint radial-and-energy refinement.

## 4. Sensitivity restricted to the dominant 8--15 km source region

Only the \(\mu_{\nu_\mu}\) values at \(8\leq r\leq15\) km are changed; all other radii and all other inputs are held fixed.

| \(8\)--\(15\) km variation | Change in total B.1 source |
|---|---:|
| \(\mu_{\nu_\mu}\to0.9\mu_{\nu_\mu}\) | \(+0.0588\%\) |
| \(\mu_{\nu_\mu}\to1.1\mu_{\nu_\mu}\) | \(-0.0646\%\) |
| \(\mu_{\nu_\mu}\to0.7\mu_{\nu_\mu}\) | \(+0.1584\%\) |
| \(\mu_{\nu_\mu}\to1.3\mu_{\nu_\mu}\) | \(-0.2109\%\) |
| \(\mu_{\nu_\mu}\to0\) | \(+0.3127\%\) |

Even a deliberately broad \(\pm30\%\) variation in the dominant source region changes the total source by only about \(0.2\%\).

## 5. Separate test of \(\mu_{\nu_\tau}=0\)

Blinov et al. state that their simulation profiles do not provide \(\mu_{\nu_\tau}\); since the tau-neutrino chemical potential can arise only from diffusion effects in this setup, they set it to zero. This is the baseline retained here.

As a diagnostic, \(\mu_{\nu_\tau}\) is set to a fraction of the reconstructed \(\mu_{\nu_\mu}\), without changing \(\mu_{\nu_\mu}\):

| Diagnostic \(\mu_{\nu_\tau}\) | Change in total B.1 source |
|---|---:|
| \(0\) (paper baseline) | \(0\) |
| \(0.25\,\mu_{\nu_\mu}\) | \(-0.0849\%\) |
| \(0.5\,\mu_{\nu_\mu}\) | \(-0.3281\%\) |
| \(\mu_{\nu_\mu}\) | \(-1.1737\%\) |
| \(-\mu_{\nu_\mu}\) | \(-1.1737\%\) |

The sign independence again follows from the evenness of the pair kernel. Taking \(\mu_{\nu_\tau}=\mu_{\nu_\mu}\) everywhere is an intentionally extreme comparison, not a proposed replacement for the paper's assumption.

## 6. Consequence for the weak-coupling Fig. 7 point

The higher-resolution optically-thin baseline gives
\[
L_{\rm thin}(g_{\rm weak})
=9.90960\times10^{51}\ {\rm erg\,s^{-1}},
\]
whereas the digitized Fig. 7 weak point is
\[
L_{\rm Fig.7}=1.08933\times10^{52}\ {\rm erg\,s^{-1}}.
\]
The source-only deficit is therefore \(-9.0303\%\). The full B.1+B.2 weak-point result has an escape fraction \(0.99787\), so transport changes this by only about \(0.21\%\).

Setting \(\mu_{\nu_\mu}=0\) globally raises the B.1 source by only \(1.1737\%\), leaving a \(-7.9626\%\) weak-point deficit. The \(\pm30\%\) global variations leave a deficit between approximately \(-8.53\%\) and \(-9.63\%\). The extreme \(\mu_{\nu_\tau}=\mu_{\nu_\mu}\) diagnostic lowers the source and makes the deficit larger.

Consequently, the reconstructed \(\mu_{\nu_\mu}\) profile and the paper's \(\mu_{\nu_\tau}=0\) assumption cannot account for the weak-end source discrepancy at the tested scale. The independent P1-B.2 result that \(\pm10\%\) \(\mu_{\nu_\mu}\) variations change the 210--510 MeV B.2 escaped band by less than \(0.03\%\) also rules out a large propagation response from this input in that band.

## 7. Decision

1. Keep the current \(\mu_{\nu_\mu}(r)\) reconstruction and \(\mu_{\nu_\tau}=0\) as the literal baseline.
2. Do not adjust the B.7 kernel, the two-flavour sum, or the B.1 source using the Fig. 7 residual.
3. The \(\mu_{\nu_\mu}\) uncertainty is not a viable explanation for the approximately \(9\%\) weak-end source deficit.
4. The \(\mu_{\nu_\tau}\) assumption is explicitly tested but remains the paper's stated approximation; the equal-to-\(\mu_{\nu_\mu}\) case is diagnostic only.
5. No source normalization, opacity, coupling, profile, Fig. 7 curve, or axial-vector result is modified.

Machine-readable results are in \`outputs/b16_numu_b1_source_sensitivity_10mev_2026-11-10.json\`. The independent V8 implementation is \`audit_b16_numu_b1_source_sensitivity.js\`.

## 8. Next source-side test

The outer 24--25 km lapse continuation is negligible, and the B.1 source response to \(\mu_{\nu_\mu}\) is below the percent level even under broad stresses. The next useful source-side test is therefore the *interior lapse normalization* over the dominant 8--15 km emission region. Vary only \(N(r)\) there, preserving \(T,\mu_\mu,\mu_{\nu_\mu}\), the exact B.1 threshold, and the radial/energy grids. Compare the required lapse shift to the available figure-level lapse cross-check. Do not change the baseline lapse or infer a correction by fitting Fig. 7.

## References

1. N. Blinov et al., *\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae*, JHEP 06 (2026) 155, Appendix B, Eqs. (B.6)--(B.10), https://doi.org/10.1007/JHEP06(2026)155.
2. A. Caputo, G. Raffelt and E. Vitagliano, *Muonic boson limits: Supernova redux*, arXiv:2109.03244v3, Fig. 1.
3. R. Bollig et al., *Muons in Supernovae: Implications for the Axion-Muon Coupling*, arXiv:2005.07141v7, Figs. 1, 3 and 4.
