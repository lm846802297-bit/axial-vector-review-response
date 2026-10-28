# Finite Higgs-constraint check at two UV benchmarks

**Status:** preliminary screening only; no model-specific experimental exclusion has been established.  
**Branch:** `research/higgs-signal-strength-two-benchmarks-2026-10-28`  
**Base branch:** `research/radial-scalar-collider-recast-2026-10-28` at its 2026-10-28 research head.  
**Purpose:** assess whether a limited Higgs signal-strength and direct-search check at the two benchmarks used in the Major Point 1.3 response can close the most important experimental gap without expanding the paper into a global UV scan.

## Scope

This branch is intentionally narrower than the parent radial-scalar collider-recast study. It focuses on:

1. the 125 GeV Higgs signal strength away from the near-degenerate $m_s\simeq m_h$ region;
2. the applicability of direct searches for an additional singlet-like scalar to the two benchmark decay patterns;
3. a separate blocker for the near-degenerate region, where a fixed-self-energy diagnostic is not a physical mixing-angle calculation.

It does **not** modify the referee-facing response or claim a complete experimentally allowed scalar-mass interval.

## Frozen inputs from the current response

Both illustrative points use $M_E=20\,\mathrm{TeV}$, $\theta_{\mu L}=\theta_{\tau L}=10^{-2}$, the stated leading-seesaw Yukawa relations, and the matching condition $\lambda_{HS}^{\mathrm{EFT}}(M_E)=0$.

| Input | Benchmark A | Benchmark B |
|---|---:|---:|
| $m_{A'}$ | $10\,\mathrm{GeV}$ | $63\,\mathrm{GeV}$ |
| $g_X$ | $0.0705$ | $0.1$ |
| $v_s$ | $70.9\,\mathrm{GeV}$ | $315\,\mathrm{GeV}$ |
| $\Pi_{hs}^{\mathrm{matched}}(m_h^2)$ | $(-0.4133-0.1132i)\,\mathrm{GeV}^2$ | $(-0.09300-0.02547i)\,\mathrm{GeV}^2$ |
| $s\to A'A'$ at $m_s\simeq m_h$ | Open | Closed ($2m_{A'}=126\,\mathrm{GeV}>m_h=125.25\,\mathrm{GeV}$) |
| Scalar width used in the response at degeneracy | $3.75\,\mathrm{GeV}$ | $0.159\,\mathrm{MeV}$ |

These values are inherited from `Replies_to_Referee_3_referee_facing_2026-10-28.tex` and the parent branch's one-loop mixing record. They are not independently rederived by this branch.

## First-pass finding

Using $|\Pi_{hs}(m_h^2)|/|m_h^2-m_s^2|$ only as a **non-degenerate screening proxy**, the illustrative mixing scale for $m_s\in[65,150]\,\mathrm{GeV}$, excluding the near-degenerate region, is at most a few $10^{-4}$. In a simple isolated-pole, no-new-Higgs-decay approximation, this would make the visible Higgs signal-strength shift tiny. For Benchmark A, $h\to A'A'$ is kinematically open and must also be included; a leading small-mixing estimate still gives a sub-per-mille shift away from degeneracy, but this is not a pole-scheme result.

This screening result does **not** validate the near-degenerate region and does **not** constitute a direct-search recast. The model-specific scalar branching fractions differ from the standard singlet-scalar benchmark used by many published limits.

## Key source anchors

- ATLAS, `ATLAS-CONF-2025-006`, global Higgs signal strength $\mu=1.023^{+0.056}_{-0.053}$: https://cds.cern.ch/record/2937634/files/ATLAS-CONF-2025-006.pdf
- Generic singlet-like scalar LEP/LHC constraint discussion and its branching-ratio assumptions: https://doi.org/10.1140/epjc/s10052-023-11887-z
- GeV-scale scalar-portal production and phenomenology review: https://doi.org/10.1007/JHEP11(2019)162
- Parent branch's radial-scalar recast protocol: [`recast-protocol.md`](../radial-scalar-collider-recast-2026-10-28/recast-protocol.md)
- Parent branch's source-data audit: [`source-data-audit-2026-10-28.md`](../radial-scalar-collider-recast-2026-10-28/source-data-audit-2026-10-28.md)

## Files in this branch

- [First-pass calculation and source applicability matrix](higgs-signal-strength-first-pass.md)
- [Screening script](higgs_signal_strength_screen.py)
- [Unit tests](test_higgs_signal_strength_screen.py)

## Evidence labels

- **Analytic/proxy result:** reproducible algebra using the fixed $\Pi_{hs}(m_h^2)$ values; not a physical mixing-angle extraction.
- **Source-level constraint:** an experimental result reported under the source's own benchmark and assumptions.
- **Model-specific reinterpretation:** a source observable compared against the UV model's prediction after matching production, widths, branching fractions and lifetime.
- **Unclassified:** the necessary model-specific observable, acceptance, branching ratio or pole treatment has not been validated.

## Acceptance gates

1. Reproduce the screening calculations from the script and tests in this directory.
2. State the global signal-strength approximation and its limitations explicitly.
3. For each benchmark, audit the direct searches whose production and decay topology overlaps with the UV scalar.
4. Do not apply standard singlet limits without checking $\mathrm{BR}(s\to A'A')$, direct lepton Yukawa decays, portal-mediated decays, and lifetime.
5. Keep $m_s<m_h/2$ separate until the matched scalar potential and $h\to ss$ width are calculated consistently.
6. Keep the near-degenerate region unclassified until a width-/pole-consistent two-state calculation is performed.
7. Only promote a point to “excluded” or “passes evaluated constraints” after a reproducible comparison to a source observable. Missing information means “unclassified,” not “allowed.”

## Current decision

The limited Higgs signal-strength screen is encouraging away from degeneracy, but the direct-search question remains only partially assessed. The appropriate scientific claim at this stage is that the two selected non-degenerate benchmarks show negligible *estimated mixing-induced Higgs-rate shifts under the stated approximations*; it is not yet justified to claim a fully validated UV-allowed region.


## Validation status

- The representative numerical rows were independently cross-checked against the stated proxy formulas.
- A Python unittest suite is included, but it has **not yet been executed in a Python/CI environment** during this branch-creation pass.
- The ATLAS global signal-strength number is used as a source-level orientation point only; no official likelihood-level fit or model-specific exclusion has been performed.


## Direct-search source audit (new)

A directly relevant ATLAS search for a separate scalar decaying as \(S\to Z_dZ_d\to4\ell\) has been identified and assessed against both benchmarks. See [direct-search-source-matrix-2026-10-28.md](direct-search-source-matrix-2026-10-28.md).

- Benchmark A with \(m_{A'}=10\) GeV does not satisfy the ATLAS intermediate-mass coverage or the explicit \(m_{\ell\ell}>11.105\) GeV pair-mass selection; no limit is transferred.
- Benchmark B with \(m_{A'}=63\) GeV can be compared with the ATLAS higher-mass search for \(m_s>130\) GeV. A conservative rate screen based on the non-degenerate self-energy proxy is far below the published limit scale, but it is not a detector-level recast or a formal exclusion statement.


## Corrected ATLAS mass-grid audit

The ATLAS paper distinguishes the high-mass event-selection boundary \(m_{4\ell}>130\) GeV from its documented generated signal samples, which start at \(m_S=150\) GeV. The new source matrix therefore evaluates the fixed-self-energy screening proxy at \(m_s=150\) GeV.

At that point the screening proxy gives \(\epsilon_{\mathrm{nd}}\simeq1.415\times10^{-5}\), and a deliberately conservative 50 pb SM gluon-fusion envelope gives \(\sigma(gg\to s)\lesssim1.01\times10^{-5}\) fb before branching fractions. This is about \(5.0\times10^3\) below the smallest published observed limit value over the high-mass plane (0.05 fb). It is **not** a point-specific exclusion result.

The official [HEPData record 145171](https://www.hepdata.net/record/145171) lists Table 15 as the observed 95% CL limit in SR2. Automated retrieval of its CSV/YAML payload was blocked in this pass; the exact observed limit near \(m_{A'}=63\) GeV has not been quoted or digitized. The updated analysis records this explicitly rather than inventing a table value.

New reproducible files:
- [ATLAS direct-search screening script](atlas_direct_search_screen.py)
- [ATLAS screening unit tests](test_atlas_direct_search_screen.py)
