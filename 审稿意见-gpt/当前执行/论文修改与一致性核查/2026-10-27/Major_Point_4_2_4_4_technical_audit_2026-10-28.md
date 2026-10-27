# Major Point 4.2–4.4: technical audit (2026-10-28)

**Scope.** This note records the benchmark-level calculations and literature applicability checks used to revise the existing response letter in PR #27. It does not claim a complete finite-mixing collider recast or a full axial-current supernova transport calculation. The manuscript source itself was not changed.

## 1. Model inputs used

The current model source gives the light-muon interaction
\[
\mathcal L\supset A'_\alpha\bar\mu\gamma^\alpha
\left[g_X\sin^2\theta_{\mu R}-g_X\cos^2\theta_{\mu R}\gamma_5\right]\mu
\]
and states that the tau sector follows with reversed \(U_A(1)_{L_\mu-L_\tau}\) charges. Thus
\[
g_V^\mu=g_X\sin^2\theta_{\mu R},\quad
g_A^\mu=-g_X\cos^2\theta_{\mu R},\qquad
g_V^\tau=-g_X\sin^2\theta_{\tau R},\quad
g_A^\tau=+g_X\cos^2\theta_{\tau R}.
\]
The left-handed neutrino couplings remain \(g_{\nu_\mu}=+g_X\) and \(g_{\nu_\tau}=-g_X\), as in the conventional \(L_\mu-L_\tau\) model. These statements are grounded in the current source file *overleaf-source/axial-vector-model-building-v6/main-v6.tex*, especially the mass-basis interaction and effective-current convention.

The benchmark used for the numerical examples below is
\[
\theta_{\mu R}=\theta_{\tau R}=10^{-2},\quad
M_{E_\mu}=M_{E_\tau},\quad
\chi_{\rm UV}=0
\]
at the stated matching scale, with no additional bare low-energy kinetic mixing. Results are conditional on these choices.

## 2. Major Point 4.2: momentum-dependent kinetic mixing

For equal right-handed mixing angles, the light charged-lepton vector charges are equal and opposite:
\[
g_V^\mu=-g_V^\tau=g_X\sin^2\theta_R.
\]
The irreducible one-loop photon--\(A'\) polarization is therefore
\[
\epsilon_{\gamma A'}(q^2)=
-\frac{e\,g_X\sin^2\theta_R}{2\pi^2}
\int_0^1dx\,x(1-x)
\log\!\left[
\frac{m_\tau^2-x(1-x)q^2-i0}
{m_\mu^2-x(1-x)q^2-i0}
\right].
\]
This is the momentum-dependent \(L_\mu-L_\tau\) loop expression of Kamada and Yu, arXiv:1504.00711, with the coupling replaced by the small vector admixture \(g_X\sin^2\theta_R\). The same integral and the behavior near \(m_{A'}=2m_\mu\) are discussed in the recent supernova study arXiv:2610.35379.

At zero momentum,
\[
|\epsilon_{\gamma A'}(0)|=
\frac{e|g_X|\sin^2\theta_R}{12\pi^2}
\ln\frac{m_\tau^2}{m_\mu^2}
\simeq1.4433\times10^{-6}|g_X|
\quad(\theta_R=10^{-2}).
\]
For an on-shell \(A'\), set \(q^2=m_{A'}^2\). The integral becomes complex above charged-lepton thresholds; the numerical table below gives the modulus, not only the real part.

| \(m_{A'}\) | \(|\epsilon_{\gamma A'}(m_{A'}^2)|/|g_X|\) | Relative to \(|\epsilon(0)|\) |
|---:|---:|---:|
| 10 MeV | \(1.44\times10^{-6}\) | 1.00 |
| 100 MeV | \(1.49\times10^{-6}\) | 1.04 |
| 200 MeV | \(1.82\times10^{-6}\) | 1.26 |
| 212 MeV | \(2.12\times10^{-6}\) | 1.47 |
| 500 MeV | \(1.40\times10^{-6}\) | 0.97 |
| 1 GeV | \(1.08\times10^{-6}\) | 0.75 |
| 3 GeV | \(8.06\times10^{-7}\) | 0.56 |
| 10 GeV | \(5.47\times10^{-8}\) | \(3.79\times10^{-2}\) |
| 100 GeV | \(4.84\times10^{-10}\) | \(3.35\times10^{-4}\) |

Numerical method: integrate the real logarithm of the absolute ratio piecewise, splitting the Feynman-parameter interval at the roots of \(m_\ell^2-q^2x(1-x)=0\); integrate the absorptive part from the corresponding branch-cut intervals. The physical masses used were \(m_\mu=105.6583755\) MeV and \(m_\tau=1.77686\) GeV, with \(e=\sqrt{4\pi/137.035999084}\). At \(m_{A'}\simeq2m_\mu\), the modulus is about 1.47 times its zero-momentum value, consistent with arXiv:2610.35379.

For unequal \(\theta_{\mu R}\) and \(\theta_{\tau R}\), the cancellation of scale-dependent terms does not follow from the individual upper bounds \(|\theta_{\ell R}|\le10^{-2}\). One must consistently match the renormalized kinetic-mixing counterterm, heavy thresholds, and electroweak-scale contributions. For spacelike virtual exchange, the same integral must be evaluated at the process-specific spacelike \(q^2\); the on-shell table is not a universal replacement for every observable.

## 3. Major Point 4.3: finite vector component versus axial benchmark

For \(|\theta_{\ell R}|\le10^{-2}\),
\[
\left|\frac{g_V^\ell}{g_A^\ell}\right|
=\tan^2\theta_{\ell R}\le1.0001\times10^{-4}.
\]
At the scan endpoint \(g_X=0.1\), this gives \(|g_V^\ell|\le10^{-5}\). This coupling ratio is useful but is not, by itself, an experimental exclusion comparison.

### 3.1 Neutrino trident

In the current manuscript, the pure-axial mediator shifts the axial coefficient \(C_A\); the finite vector component instead induces a shift in \(C_V\). At the same momentum transfer,
\[
\left|\frac{\delta C_V}{\delta C_A}\right|
\simeq\tan^2\theta_{\mu R}\lesssim1.01\times10^{-4}.
\]
Using \(C_V=1/2+2s_W^2\simeq0.96\) and \(C_A=1/2\), the ratio of the leading SM-interference terms is parametrically
\[
\left|\frac{C_V\delta C_V}{C_A\delta C_A}\right|
\sim\frac{C_V}{C_A}\tan^2\theta_{\mu R}
\lesssim2.0\times10^{-4}.
\]
This estimate compares the coupling-level interference terms. It does not include the distinct finite-\(m_\mu\) response functions and is not a substitute for a full finite-mixing integration of the trident cross section.

### 3.2 Muon anomalous magnetic moment

The manuscript uses
\[
\Delta a_\mu^{A'}=\frac{m_\mu^2}{4\pi^2m_{A'}^2}
\left[(g_\mu^V)^2F_V(r)-(g_\mu^A)^2F_A(r)\right],
\]
with \(F_V\) and \(F_A\) defined in its equation for the vector and axial loop functions. Therefore
\[
\left|\frac{\Delta a_\mu^V}{\Delta a_\mu^A}\right|
=\tan^4\theta_{\mu R}\frac{F_V(r)}{F_A(r)}.
\]
Numerical evaluation over \(1\) MeV \(\le m_{A'}\le100\) GeV gives \(F_V/F_A\le0.20\), with the heavy-mediator limit approaching \(1/5\). At \(\theta_{\mu R}=10^{-2}\), the vector-to-axial contribution ratio is at most about \(2.1\times10^{-9}\). For the stated benchmark, the finite vector term is negligible in the \((g-2)_\mu\) calculation.

### 3.3 Visible dimuon width and threshold caveat

Writing \(r_\mu=m_\mu^2/m_{A'}^2\), the vector and axial parts scale as
\[
\Gamma_V\propto(g_V^\mu)^2(1+2r_\mu)\sqrt{1-4r_\mu},\qquad
\Gamma_A\propto(g_A^\mu)^2(1-4r_\mu)^{3/2}.
\]
Away from the immediate dimuon threshold, the vector-squared piece is suppressed by \(\tan^4\theta_{\mu R}\), up to the displayed phase-space factor. Since the axial width has an additional \(1-4r_\mu\) suppression, the vector contribution can become relevant in an extremely narrow threshold neighborhood. A threshold-sensitive branching-fraction or lifetime recast must retain both terms.

### 3.4 What is and is not established

These estimates support a quantitative statement for the benchmark: the vector contribution to \((g-2)_\mu\) is negligible, and the vector part of the leading trident interference is parametrically below the axial part. They do **not** prove that vector constraints are always weaker for every observable. The full finite-mixing recast still needs the process-dependent response functions, widths and branching fractions, the momentum-dependent kinetic mixing, and (where relevant) experimental acceptance. The Fig. 2 contours remain pure-axial effective-current constraints rather than a complete finite-mixing classification of the UV model.

## 4. Major Point 4.4: supernova and stellar constraints

### 4.1 Literature and benchmark mapping

The referee's cited work, Blinov, Fox, Kelly, Plestid and Zhou, is now published as JHEP 06 (2026) 155, arXiv:2511.09619. It discusses SN1987A cooling, diffusive transport, high-energy neutrinos, and energy deposition in low-energy supernova progenitors.

A newer preprint by Wang and Zhang, arXiv:2610.35379 (submitted 26 October 2026), updates the conventional vector \(L_\mu-L_\tau\) supernova limits. For the representative SFHo-18.8 profile, its stated reach extends to \(m_{Z'}\sim300\) MeV for SN1987A cooling, with coupling sensitivity of order \(10^{-10}\), and to \(m_{Z'}\sim600\) MeV for low-energy-supernova constraints, with coupling sensitivity down to \(6.4\times10^{-12}\). These are important reference limits, but they are not taken as direct exclusions of the axial model.

### 4.2 Contributions that transfer

The axial UV model has the same tree-level neutrino couplings as the conventional \(L_\mu-L_\tau\) model:
\[
g_{\nu_\mu}=+g_X,\qquad g_{\nu_\tau}=-g_X.
\]
Consequently, at fixed \((m_{A'},g_X)\), the matrix element for neutrino coalescence \(\nu_\alpha\bar\nu_\alpha\to A'\), the partial width \(\Gamma(A'\to\nu_\alpha\bar\nu_\alpha)\), and the neutrino-coalescence production integrand are unchanged. Below the dimuon threshold, where the \(A'\) decays almost entirely to neutrinos and the kinetic-mixing-induced electron channel is highly suppressed, the neutrino production/decay part of the supernova analysis is directly applicable.

The final high-energy-neutrino flux is not automatically identical above the dimuon threshold: it depends on the total width and \(\mathrm{BR}(A'\to\nu\bar\nu)\), which change when the axial \(\mu^+\mu^-\) channel opens.

### 4.3 Contributions requiring an axial-current recast

The total vector-model exclusion curve also includes muon semi-Compton production \(\mu\gamma\to\mu A'\), its inverse absorption, and visible decays in the progenitor. Those amplitudes and the polarization-resolved optical depth depend on the charged-muon current. They must be recalculated for \(g_A^\mu\simeq-g_X\) rather than the vector coupling \(g_V^\mu=g_X\). In arXiv:2610.35379, semi-Compton production dominates for \(m_{A'}\lesssim10\) MeV, while neutrino coalescence dominates the production luminosity at larger masses in the displayed benchmark. Thus the neutrino-coalescence component is directly reusable, but the dominance of that component does not prove that the total exclusion contour is unchanged.

For \(m_{A'}>2m_\mu\), low-energy-supernova heating depends on the probability of \(A'\to\mu^+\mu^-\) inside the progenitor, the branching ratio, and the energy carried away by muon-decay neutrinos. The axial width has a \(\beta^3\) threshold dependence rather than the vector width's \(\beta(1+2r_\mu)\) dependence. These effects require a model-specific lifetime, branching-ratio and transport calculation.

The kinetic-mixing-induced electron/proton coupling is also parametrically different. At low momentum, the equal-mixing axial benchmark gives \(|\epsilon_{\gamma A'}|/|g_X|\simeq1.4\times10^{-6}\), while the conventional vector \(L_\mu-L_\tau\) estimate is \(|\epsilon_{\mu\tau}|/|g_{\mu\tau}|\simeq1/70\). At the same gauge coupling, the mixing-induced amplitude is therefore smaller by about \(10^{-4}\) and its rate by about \(10^{-8}\). This suppresses the mixing-induced electron/proton channels, but does not remove direct neutrino or muon production.

### 4.4 Current conclusion

The correct status is **partial transfer established; total axial supernova recast open**:

- Directly transferable at fixed \((m_{A'},g_X)\): neutrino-coalescence production and the partial widths into neutrinos.
- Must be recalculated: axial muon semi-Compton production/absorption, total widths and branching fractions above threshold, optical depths/trapping, high-energy-neutrino flux when visible channels open, and low-energy-supernova energy deposition.
- Not claimed: that all SN1987A or low-energy-supernova constraints are subdominant or inapplicable.

This note covers the supernova probes raised by the referee. Other stellar environments and mass ranges still require a separate production/transport applicability check.

## 5. Sources consulted

1. Kamada and Yu, arXiv:1504.00711: https://arxiv.org/abs/1504.00711
2. Blinov, Fox, Kelly, Plestid and Zhou, “\(L_\mu-L_\tau\) gauge bosons in beam dumps and supernovae,” arXiv:2511.09619; JHEP 06 (2026) 155: https://arxiv.org/abs/2511.09619
3. Wang and Zhang, “Revisiting supernova constraints on dark gauge bosons,” arXiv:2610.35379 (submitted 26 October 2026): https://arxiv.org/abs/2610.35379
4. Das, Ghosh and Puri, “SN1987A Constraints of Light \(Z'\) with Non-Mixing Polarisations,” arXiv:2606.23769: https://arxiv.org/abs/2606.23769
5. Current UV model source: overleaf-source/axial-vector-model-building-v6/main-v6.tex in this repository.
