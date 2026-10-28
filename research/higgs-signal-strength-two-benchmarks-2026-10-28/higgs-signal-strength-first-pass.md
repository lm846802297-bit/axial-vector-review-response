# First-pass Higgs signal-strength check at two benchmarks

**Date:** 2026-10-28  
**Status:** analytic screening calculation; not an official fit, not a pole-scheme mixing angle, and not a direct-search recast.

## 1. Question and scope

The referee asks whether the loop-induced $h$-$s$ mixing could lead to strong constraints from the measured 125 GeV Higgs signal strengths, especially as $m_s\to m_h$. This note performs a deliberately limited check at the two benchmarks already used in the response. It does not replace the full collider recast tracked in the parent research branch.

The first-pass domain is $m_s\ge m_h/2=62.625\,\mathrm{GeV}$, so the exotic decay $h\to ss$ is kinematically closed. The region $m_s<m_h/2$ is kept unclassified until the matched scalar potential, the $hss$ trilinear and $\Gamma(h\to ss)$ are calculated consistently.

## 2. Inputs inherited from the one-loop response

Use $m_h=125.25\,\mathrm{GeV}$ and the response's matched self-energies at $p^2=m_h^2$:

$$
\Pi_A=(-0.4133-0.1132i)\,\mathrm{GeV}^2,
\qquad |\Pi_A|=0.428522\,\mathrm{GeV}^2,
$$

$$
\Pi_B=(-0.09300-0.02547i)\,\mathrm{GeV}^2,
\qquad |\Pi_B|=0.096425\,\mathrm{GeV}^2.
$$

| Input | A | B |
|---|---:|---:|
| $m_{A'}$ | $10\,\mathrm{GeV}$ | $63\,\mathrm{GeV}$ |
| $g_X$ | $0.0705$ | $0.1$ |
| $v_s$ | $70.9\,\mathrm{GeV}$ | $315\,\mathrm{GeV}$ |
| $\Gamma_s$ used at degeneracy in the response | $3.75\,\mathrm{GeV}$ | $0.159\,\mathrm{MeV}$ |
| $s\to A'A'$ at $m_s=m_h$ | open | closed |

The matching condition is $\lambda_{HS}^{\mathrm{EFT}}(M_E)=0$ at $M_E=20\,\mathrm{TeV}$, with $\theta_{\mu L}=\theta_{\tau L}=10^{-2}$. This is a conditional benchmark, not a symmetry prediction.

## 3. Non-degenerate screening proxy

Away from pole overlap, use only as a screening estimate

$$
\epsilon_{\rm nd}(m_s)
=\frac{|\Pi_{hs}(m_h^2)|}{|m_h^2-m_s^2|}.
$$

For sufficiently small mixing and well-separated poles, this is of the order of the mixing parameter. It is **not** a physical mixing angle: the numerator is a complex self-energy evaluated at $p^2=m_h^2$, held fixed while $m_s$ varies. A self-consistent result requires the momentum-dependent inverse propagator matrix, counterterms/renormalization prescription, and both complex poles.

For the SM-like Higgs visible rates, absent any extra Higgs decay, the simple isolated-state approximation is

$$
\mu_{\rm vis}\simeq\cos^2\theta
\simeq1-\epsilon_{\rm nd}^2.
$$

Benchmark A has an additional open channel $h_{\rm like}\to A'A'$ induced by the singlet admixture. A leading small-mixing estimate includes it as

$$
\mu_{\rm vis}^{(A)}
\simeq
\frac{\cos^4\theta}
{\cos^2\theta+\sin^2\theta\,r_A},
\qquad
r_A=\frac{\Gamma_{s_0\to A'A'}(m_h)}{\Gamma_h^{\rm SM}}.
$$

Using the response's $\Gamma_{s_0\to A'A'}(m_h)\simeq3.75\,\mathrm{GeV}$ and $\Gamma_h^{\rm SM}\simeq4.07\,\mathrm{MeV}$, $r_A\simeq9.21\times10^2$. This formula assumes the same small-angle rotation rescales all SM-like production and partial widths, and that the new $A'A'$ mode is the only extra width considered. It is still an estimate, not a pole-scheme prediction or an analysis of the final states from the $A'$ decays.

## 4. Reproducible screening values

The script named **higgs_signal_strength_screen.py** calculates the proxy at selected masses. The table below lists representative points. The mask $|m_s-m_h|<1\,\mathrm{GeV}$ is a conservative **calculation mask only**, not a physical exclusion interval. The exact near-degenerate band identified by the response is much narrower (about $7.5\,\mathrm{MeV}$ on either side under its fixed-self-energy diagnostic), but the full region requires a pole-consistent treatment.

| $m_s$ (GeV) | $\epsilon_{\rm nd}$, A | $1-\mu_{\rm vis}^{(A)}$ | $\epsilon_{\rm nd}$, B | $1-\mu_{\rm vis}^{(B)}$ |
|---:|---:|---:|---:|---:|
| 65 | $3.74\times10^{-5}$ | $1.29\times10^{-6}$ | $8.41\times10^{-6}$ | $7.08\times10^{-11}$ |
| 80 | $4.61\times10^{-5}$ | $1.96\times10^{-6}$ | $1.04\times10^{-5}$ | $1.08\times10^{-10}$ |
| 100 | $7.53\times10^{-5}$ | $5.24\times10^{-6}$ | $1.70\times10^{-5}$ | $2.87\times10^{-10}$ |
| 120 | $3.33\times10^{-4}$ | $1.02\times10^{-4}$ | $7.49\times10^{-5}$ | $5.61\times10^{-9}$ |
| 130 | $3.53\times10^{-4}$ | $1.15\times10^{-4}$ | $7.95\times10^{-5}$ | $6.32\times10^{-9}$ |
| 150 | $6.29\times10^{-5}$ | $3.65\times10^{-6}$ | $1.42\times10^{-5}$ | $2.00\times10^{-10}$ |

The largest estimated visible-rate shift among these selected non-degenerate points is about $1.2\times10^{-4}$ for A and $6.4\times10^{-9}$ for B. These are much smaller than current inclusive Higgs signal-strength uncertainties. This supports a narrow statement: **under the fixed matching condition and non-degenerate proxy, the two illustrative points do not show a sizeable mixing-induced Higgs-rate shift in this mass slice.** It does not establish a global bound.

## 5. Comparison with the measured Higgs signal strength

ATLAS-CONF-2025-006 reports a global signal strength

$$
\mu=1.023^{+0.056}_{-0.053}.
$$

For orientation only, a one-sided Gaussian approximation using the lower uncertainty gives

$$
\mu_{\min}^{95\%}\approx1.023-1.645(0.053)=0.936,
$$

$$
\sin^2\theta\lesssim1-\mu_{\min}^{95\%}\approx0.064,
\qquad |\sin\theta|\lesssim0.253,
$$

if the only effect is universal mixing rescaling and there are no extra Higgs decays. This is **not** an official 95% CL limit: a proper bound requires the experiment's likelihood/correlations and the actual model predictions. In Benchmark A, $h\to A'A'$ is open and the extra width must be included; in the near-degenerate region, the one-state mapping $\mu=\cos^2\theta$ is not valid without resolving the overlapping poles.

## 6. Direct-search applicability matrix

| Search class | What is available at source level | Benchmark A | Benchmark B | Current status |
|---|---|---|---|---|
| 125 GeV Higgs signal strength | ATLAS global $\mu$; generic Higgs coupling fit | Include mixing-induced $h\to A'A'$ width | No $h\to A'A'$ threshold at 125.25 GeV | Non-degenerate screening only; no official model fit |
| LEP $e^+e^-\to Zs$ / Higgs-like scalar searches below about 115 GeV | Generic singlet studies quote limits on mixing under specified SM-like decay assumptions | $s\to A'A'$ opens for $m_s>20\,\mathrm{GeV}$, so standard visible branching assumptions fail | $s\to A'A'$ closed for $m_s<126\,\mathrm{GeV}$, but direct lepton Yukawas alter the decay pattern | Need observable-by-observable branching/acceptance audit; no UV exclusion assigned |
| LHC direct searches for extra scalars around 100–150 GeV | Limits depend on production mode and final state | Cascade $s\to A'A'$ changes the signature | $A'A'$ opens only above $126\,\mathrm{GeV}$ | No matching analysis has yet been recast in this branch |
| Belle II $4\mu$ and $\tau\tau$ resonances | Published mass domains $0.212$–$9.0\,\mathrm{GeV}$ and $3.6$–$10\,\mathrm{GeV}$ | No overlap with the present $m_s\ge62.625\,\mathrm{GeV}$ first-pass slice | Same | Refer to the parent recast branch for lower masses; not applicable to this slice |

A recent singlet-scalar review reports LEP mixing constraints of order $|\sin\xi|\lesssim0.2$ or below for $m_s<100\,\mathrm{GeV}$, but those results assume particular scalar decay patterns, often SM-like decays. They are context, not direct limits for the present model. Even where the non-degenerate proxy is far below that mixing scale, this does not constrain production channels driven by direct leptonic Yukawa interactions or the $A'A'$ cascade.

## 7. Near-degenerate region: separate unresolved task

The current response reports, at exact $m_s=m_h$, the fixed-self-energy diagnostic

- A, $s\to A'A'$ open: $|\Pi_{hs}/(a-b)|\simeq9.1\times10^{-4}$;
- B, $s\to A'A'$ closed: $|\Pi_{hs}/(a-b)|\simeq0.197$, with the doubled diagnostic about $0.394$.

These values should not be converted into $\sin\theta$, signal strength, or an experimental exclusion. The scan holds $\Pi_{hs}(m_h^2)$ fixed while varying $m_s$ and the singlet width. The required follow-up is to build and solve the width-/pole-consistent $2\times2$ inverse propagator, determine both complex poles and residues, then derive the Higgs-like rates and extra-scalar search observables.

Until then, the near-degenerate points are **unclassified**.

## 8. Current conclusion and next actions

1. The non-degenerate Higgs signal-strength screen is numerically negligible for the two illustrative benchmarks under the declared approximations.
2. Generic LEP/LHC singlet limits cannot simply be copied over because the scalar branching pattern is model-dependent.
3. No model-specific direct-search exclusion has been established by this note.
4. Do not claim a complete experimentally allowed $m_s$ interval.
5. Next: extract applicable published direct-search curves; compute exact branching fractions and $A'$ cascade final states; audit acceptance/lifetime; and treat the near-degenerate pole problem separately.

## Sources

- ATLAS Collaboration, *Measurement of Higgs boson production and decay rates in $pp$ collisions at $\sqrt{s}=13\,\mathrm{TeV}$*, ATLAS-CONF-2025-006, PDF: https://cds.cern.ch/record/2937634/files/ATLAS-CONF-2025-006.pdf
- *Electroweak baryogenesis: The scalar singlet strikes back*, Eur. Phys. J. C (2023), DOI: https://doi.org/10.1140/epjc/s10052-023-11887-z
- Boiarska et al., *Phenomenology of GeV-scale scalar portal*, JHEP 11 (2019) 162, DOI: https://doi.org/10.1007/JHEP11(2019)162
- Parent branch's detailed recast ledger and protocol: research/radial-scalar-collider-recast-2026-10-28/
