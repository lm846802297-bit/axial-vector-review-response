# Major Point 1 — radiative Higgs-portal threshold, mixing diagnostics, and Higgs constraints

**Date:** 2026-11-10  
**Scope:** original one-VEV \(S+\mathrm{VLL}\) model, Benchmarks A/B, \(M_E=20\) TeV.  
**Status:** the finite VLL portal threshold and its benchmark consequences are quantified. The portal is not symmetry-forbidden. The negligible-portal point is a conditional matching/tuning benchmark, not a prediction. A tree-level/local-curvature diagnostic identifies the resonance windows, but a complete gauge-independent complex-pole and experimental recast is still outstanding.

## 1. Portal operator is allowed

The gauge-invariant renormalizable operator
\[
V\supset\lambda_{HS}(H^\dagger H)(S^\dagger S)
\]
is allowed by \(U(1)_{L_\mu-L_\tau}\). Therefore no symmetry enforces \(\lambda_{HS}=0\). The charged-lepton/VLL interactions radiatively generate a finite threshold.

For
\[
{\cal M}_\ell(\phi_h,\phi_s)=
\begin{pmatrix}0&y_\ell\phi_h/\sqrt2\\
\lambda_\ell\phi_s/\sqrt2&M_E\end{pmatrix},
\]
the one-loop VLL determinant has no mixed \(\phi_h^2\phi_s^2\) term in its UV pole:
\[
\partial_{\phi_h}\partial_{\phi_s}
\operatorname{Tr}[({\cal M}^\dagger{\cal M})^2]=0.
\]
Thus the VLL-sector divergent renormalizable portal counterterm vanishes at this one-loop order. This does **not** imply a zero finite threshold.

The finite heavy-eigenstate Coleman–Weinberg matching at \(\mu=M_E\) gives
\[
\Delta\lambda_{HS}^{\rm hard}
=-\frac{1}{8\pi^2}\sum_{\ell=\mu,\tau}|y_\ell|^2|\lambda_\ell|^2,
\]
with the benchmark values:
\[
\Delta\lambda_{HS}^{\rm hard}=
\begin{cases}
-0.21076398 & (A),\\
-0.01067338 & (B).
\end{cases}
\]
The corresponding local off-diagonal curvature before compensation is
\[
\Delta M_{hs,H}^2=\Delta\lambda_{HS}^{\rm hard}v_hv_s
=\begin{cases}
-3.67860356\times10^3\ {\rm GeV}^2 &(A),\\
-8.27819609\times10^2\ {\rm GeV}^2 &(B).
\end{cases}
\]

## 2. Meaning of the negligible-portal reference point

The adopted conditional boundary is
\[
\lambda_{HS}^{\rm EFT}(M_E)=0,\qquad
\lambda_{HS}^{\rm UV}(M_E)=-\Delta\lambda_{HS}^{\rm hard}.
\]
This cancels the finite dimension-four threshold at the matching scale. It is a legitimate renormalization/matching benchmark, but it is not symmetry-protected or predicted by the original model. It represents a chosen cancellation between the independent UV portal parameter and the VLL threshold. A generic UV boundary, including \(\lambda_{HS}^{\rm UV}=0\), does not give negligible mixing.

After this dimension-four cancellation, the finite heavy-potential dimension-six plus dimension-eight operators leave the local mixed curvature
\[
\delta_{\rm loc}\equiv\Delta M_{hs}^{2,(6+8)}
=\begin{cases}
+0.656933835\ {\rm GeV}^2 &(A),\\
+0.147834009\ {\rm GeV}^2 &(B).
\end{cases}
\]
These are local potential curvatures in the specified VLL/\(\overline{\rm MS}\) matching subset, not complete momentum-dependent physical self-energies.

## 3. Tree-level mixing diagnostics

For a real symmetric two-state mass matrix with off-diagonal entry \(\delta\),
\[
\tan2\theta=\frac{2\delta}{m_h^2-m_s^2},\qquad
|\theta|=\frac12\arctan\frac{2|\delta|}{|m_h^2-m_s^2|}.
\]
This formula is used only as an away-from-resonance diagnostic. At degeneracy it is not a physical pole prescription; widths, momentum-dependent self-energies and diagonal mass shifts require the full complex \(2\times2\) propagator.

If the finite portal threshold is **not** compensated, the above formula using \(\delta=\Delta\lambda_{HS}^{\rm hard}v_hv_s\) gives the following illustrative angles and doublet-component signal-strength factors \(\cos^2\theta\), with \(m_h=125.25\) GeV:

| \(m_s\) [GeV] | A: \(|\theta|\) [rad] | A: \(\cos^2\theta\) | B: \(|\theta|\) [rad] | B: \(\cos^2\theta\) |
|---:|---:|---:|---:|---:|
| 10 | 0.22050 | 0.95216 | 0.05291 | 0.99720 |
| 100 | 0.45635 | 0.80581 | 0.14164 | 0.98007 |
| 150 | 0.41191 | 0.83971 | 0.11920 | 0.98586 |
| 200 | 0.14693 | 0.97857 | 0.03400 | 0.99884 |
| 355.4 (A cap) / 1579.2 (B cap) | 0.03321 | 0.99890 | 0.000334 | 0.9999999 |

The A and B perturbative upper limits are \(m_s^{max}=\sqrt{8\pi}v_s=355.4\) and \(1579.2\) GeV, respectively. The 10 GeV lower endpoint in this table is the reference scan endpoint, not a universal experimental lower bound.

## 4. Illustrative Higgs signal-strength constraint

The ATLAS 2026 combination reports an inclusive Higgs event rate
\[
\mu_{\rm incl}=0.990^{+0.053}_{-0.051}.
\]
For an isolated singlet-mixed Higgs-like pole, assuming no nonstandard decays and universal doublet-coupling rescaling, \(\mu\simeq\cos^2\theta\). A one-sided Gaussian 95% lower estimate is \(\mu_{\min}\simeq0.906\), giving the illustrative condition
\[
\sin^2\theta\lesssim0.094,\qquad |\theta|\lesssim0.311\ {\rm rad}.
\]
This is not a model-specific likelihood fit. It does not apply unchanged when the two poles overlap, when the second scalar contributes within the experimental mass resolution, or when exotic decays are open.

Under this simplified no-exotic single-pole criterion, the **uncompensated finite-threshold diagnostic** is outside the rate bound approximately for
\[
73.8\lesssim m_s\lesssim161.0\ {\rm GeV}\quad(A),
\]
and
\[
115.7\lesssim m_s\lesssim134.1\ {\rm GeV}\quad(B).
\]
These are conditional diagnostic intervals, not exclusions: the renormalized portal is an independent input, and the actual model has additional decay channels in part of the parameter space.

## 5. Near-degenerate windows after dimension-four portal cancellation

Using only the residual local curvatures \(\delta_{\rm loc}\), the approximate half-width in mass around \(m_h\) at which a target mixing angle is reached is
\[
|m_s-m_h|\simeq
\frac{|\delta_{\rm loc}|}{m_h\tan(2|\theta|)}.
\]
For \(m_h=125.25\) GeV:
- \(|\theta_{\rm loc}|\ge0.1\): about \(25.9\) MeV (A), \(5.82\) MeV (B);
- \(|\theta_{\rm loc}|\ge0.01\): about \(262\) MeV (A), \(59.0\) MeV (B);
- \(|\theta_{\rm loc}|\ge0.311\): about \(7.30\) MeV (A), \(1.64\) MeV (B).

The last line compares with the illustrative isolated-pole signal-strength angle above, but is not an exclusion window. The previous Plan-C local scan already found a sizeable eigenvector-composition diagnostic in a narrow Benchmark-B near-degenerate interval. That diagnostic is not a pole residue or a physical mixing angle. It nevertheless independently flags the need for a full complex-pole treatment.

## 6. Additional model-specific decay: \(h_{\rm SM-like}\to A'A'\)

This channel is essential for Benchmark A and is absent kinematically for Benchmark B.

From \(|D_\mu S|^2\), using \(m_{A'}=2g_Xv_s\), the radial scalar has
\[
{\cal L}\supset \frac{m_{A'}^2}{v_s}s A'_\mu A'^\mu.
\]
If the 125-GeV-like state has singlet component \(\sin\theta\), then
\[
\Gamma(h_1\to A'A')=
\frac{m_{h_1}^3}{32\pi v_s^2}\sin^2\theta
(1-4x+12x^2)\sqrt{1-4x},\quad
x=\frac{m_{A'}^2}{m_{h_1}^2}.
\]
For Benchmark A, \(m_{A'}=10\) GeV and \(v_s=70.886458\) GeV, so the channel is open and
\[
\Gamma(h_1\to A'A')\simeq
3.744\ {\rm GeV}\times\sin^2\theta.
\]
Compared with the SM Higgs width of about 4.1 MeV, this is approximately \(9.2\times10^2\sin^2\theta\) times the SM width. Thus even a small singlet admixture can produce a significant exotic width. For illustration only, requiring this partial width to be below 10% of the SM width would imply \(\sin^2\theta\lesssim1.1\times10^{-4}\); this is not itself an experimental limit.

For Benchmark B, \(2m_{A'}=126\) GeV exceeds \(m_h=125.25\) GeV, so this two-body channel is closed. Other exotic channels, including \(h_1\to ss\) when kinematically open, require their own coupling and width calculation.

ATLAS has searched for Higgs decays to light dark photons with prompt collimated electron/muon pairs and sets mass- and signal-dependent 95% CL branching-fraction limits ranging from 0.001% to 5%. These limits cannot be copied directly onto this \(L_\mu-L_\tau\) model: the \(A'\) branching fractions and final-state composition differ, so a dedicated recast is needed.

## 7. Referee-response conclusion and acceptance boundary

The technically correct response is not that loop-induced portal mixing is absent or automatically negligible. It is:
1. the portal is allowed and receives a finite VLL threshold;
2. the negligible-portal point is a conditional matching choice that cancels that threshold, not a symmetry prediction;
3. after this choice, the retained heavy-potential dimension-six/eight local curvature is small away from \(m_s\simeq m_h\);
4. near degeneracy the small-mixing expansion fails, and the two-state complex propagator/line shape must be used;
5. for Benchmark A, \(h\to A'A'\) is open and may make Higgs exotic-decay searches more important than the inclusive \(\cos^2\theta\) estimate;
6. a complete allowed/excluded region is not claimed until the full gauge-complete propagator, tadpole/VEV prescription, scalar widths, and model-specific Higgs-search recast are completed.

The original paper's low-energy EFT treatment may therefore be defended only as a stated non-degenerate, negligible-renormalized-portal benchmark. It must not be presented as a generic decoupling theorem or as valid throughout the full perturbative \(m_s\) interval.


## 8. External experimental references and applicability

- ATLAS Collaboration, [Combination of Higgs boson measurements at sqrt(s) = 13 TeV and their interpretations by the ATLAS experiment, arXiv:2608.07332](https://arxiv.org/abs/2608.07332) (2026). The paper reports the inclusive Higgs event rate \(\mu_{\rm incl}=0.990^{+0.053}_{-0.051}\), using up to 140 fb\(^{-1}\) at 13 TeV. The one-sided Gaussian lower estimate used above is an illustrative translation of this measured rate, not an ATLAS-provided model-independent mixing-angle limit.
- ATLAS Collaboration, [Search for light neutral particles decaying promptly into collimated pairs of electrons or muons, arXiv:2407.09168](https://arxiv.org/abs/2407.09168), published in *European Physical Journal C* (2025), [doi:10.1140/epjc/s10052-025-13916-5](https://doi.org/10.1140/epjc/s10052-025-13916-5). The 95% CL branching-fraction range 0.001%–5% is mass- and signal-model-dependent and comes from the specified 13 TeV, 140 fb\(^{-1}\), prompt-collimated e/mu search. It is not a model-independent bound on this model's \(h\to A'A'\) rate.

The references support the experimental inputs only. They do not replace a model-specific recast with the actual \(A'\) branching fractions, lifetime, collimation/acceptance and final-state composition.
