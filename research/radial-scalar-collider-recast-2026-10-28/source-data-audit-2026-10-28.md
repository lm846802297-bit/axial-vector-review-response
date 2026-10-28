# Source-data availability audit — 2026-10-28

## Result

The two priority Belle II analyses do publish mass-dependent numerical information. Therefore the immediate blocker is **not simply a lack of public limits**. The next step is to retrieve the numerical supplements, reproduce the experimental scalar benchmark, and only then map the results to the UV radial scalar.

## Belle II four-muon resonance search

- Paper: I. Adachi et al. (Belle II), *Search for a \(\mu^+\mu^-\) resonance in four-muon final states at Belle II*, Phys. Rev. D 109, 112015 (2024), DOI [10.1103/PhysRevD.109.112015](https://doi.org/10.1103/PhysRevD.109.112015); [arXiv:2403.02841](https://arxiv.org/abs/2403.02841).
- Official Belle II publication record: https://docs.belle2.org/pub_data/publications/4383/
- The paper explicitly says the supplemental material contains numerical observed cross sections and observed 90% CL upper limits on the cross section and scalar coupling \(g_S\) as functions of mass.
- The paper's scalar signal is generated separately from the vector benchmark. It warns that previous scalar reinterpretations can miss important efficiency differences because the scalar and vector kinematic distributions differ.
- The published analysis uses \(178\,\mathrm{fb}^{-1}\), covers \(m_S=0.212\text{--}9.0\,\mathrm{GeV}\), and analyzes \(e^+e^-\to\mu^+\mu^-S\), \(S\to\mu^+\mu^-\). Its prompt-lifetime assumption must be checked against each UV benchmark's total width.

**Implication for this study:** use the scalar-specific numerical curve, not a vector curve rescaled by coupling alone. The UV prediction must replace the benchmark branching fraction with the actual \(\mathrm{BR}(s\to\mu^+\mu^-)\), including \(s\to A'A'\) when open and any portal-mediated modes.

## Belle II tau-pair resonance search

- Paper: Belle II Collaboration, *Search for a \(\tau^+\tau^-\) resonance in \(e^+e^-\to\mu^+\mu^-\tau^+\tau^-\) events with the Belle II experiment*, Phys. Rev. Lett. 131, 121802 (2023), DOI [10.1103/PhysRevLett.131.121802](https://doi.org/10.1103/PhysRevLett.131.121802); [arXiv:2306.12294](https://arxiv.org/abs/2306.12294).
- Official Belle II publication record and PDF: https://docs.belle2.org/pub_data/documents/4407/
- The APS supplemental page publicly lists limits.csv, limits.txt, and supplemental.pdf: https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.131.121802
- The supplemental description says the text file contains numerical observed cross sections and observed 90% CL upper limits on the cross section and on the model couplings as functions of mass.
- The search uses \(62.8\,\mathrm{fb}^{-1}\) and covers \(m_X=3.6\text{--}10\,\mathrm{GeV}\). The abstract reports \(\sigma\times\mathrm{BR}(X\to\tau\tau)\) upper limits of approximately \(0.7\text{--}24\,\mathrm{fb}\), but that broad range is not a substitute for the per-mass data.

**Implication for this study:** retrieve the per-mass limits and exact scalar normalization. Compute the UV model's \(\sigma(e^+e^-\to\mu^+\mu^-s)\times\mathrm{BR}(s\to\tau^+\tau^-)\) only after the production and total-width assumptions are frozen.

## Retrieval status

- The official paper pages and the existence/content of the supplements are verified.
- Direct automated retrieval of the APS CSV/TXT files was blocked in this environment during this pass. This is a tooling/access limitation, not evidence that the files are unavailable to the public.
- Do not manually invent per-mass numbers from the abstract or read approximate values from a plot as if they were exact data. Retry via the official supplemental download or use a clearly labelled digitization with uncertainty if the numerical files cannot be obtained.

## Sources consulted

- https://docs.belle2.org/pub_data/publications/4383/
- https://docs.belle2.org/files/4383/BELLE2-PUB-PH-2023-007/1/BELLE2-PUB-PH-2023-007.pdf
- https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.131.121802
- https://docs.belle2.org/pub_data/documents/4407/
- https://arxiv.org/abs/2403.02841
- https://arxiv.org/abs/2306.12294
