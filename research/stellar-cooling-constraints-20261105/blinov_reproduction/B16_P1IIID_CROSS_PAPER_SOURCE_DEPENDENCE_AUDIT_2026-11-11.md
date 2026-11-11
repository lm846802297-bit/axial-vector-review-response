# P1-IIId: Cross-paper source-dependence audit — Caputo vs Esseili–Kribs

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Key correction: this is not an independent simulation cross-check

The two papers are:

1. A. Caputo, G. Raffelt, E. Vitagliano, *Muonic Boson Limits: Supernova Redux*, arXiv:2109.03244v3 (post-publication note dated 13 March 2026).
2. H. Esseili, G. D. Kribs, *Hiding a Light Vector Boson from Terrestrial Experiments: A Chargephobic Dark Photon*, arXiv:2512.10916v3; Phys. Rev. D 114, 016023 (2026).

Caputo explicitly identifies Fig. 1 as the Garching muonic SN model SFHo-18.8 at 1 s postbounce and calls it the cold reference model.

Esseili–Kribs explicitly states that its supernova calculation uses Garching simulations, considers SFHo-18.6, SFHo-18.8, SFHo-20.0, and LS220-20.0, and plots the temperature and normalized particle number densities at 1 s after core collapse. Its Fig. 12 right panel is the SFHo-18.8 density profile.

Therefore, the two papers are not two independent hydrodynamical simulations. The appropriate description is **cross-publication / figure-level consistency audit of a shared Garching model family**, not independent simulation validation. It is not yet proven that both papers use byte-identical profile snapshots, identical post-processing, or identical species conventions.

## 2. Exact source evidence

### Caputo et al.

- arXiv PDF: https://arxiv.org/pdf/2109.03244
- Lines around the introduction identify SFHo-18.8 at 1 s postbounce as the cold reference model.
- Fig. 1 lower panel labels \(n_B,n_p,n_\mu,n_e\), normalized to \(n_0=0.181\,\mathrm{fm}^{-3}\).

### Esseili–Kribs

- arXiv HTML v3: https://arxiv.org/html/2512.10916v3
- APS PDF: https://journals.aps.org/prd/pdf/10.1103/718s-7k7v
- Section V.2.1 states that the four models are SFHo-18.6, SFHo-18.8, SFHo-20.0, and LS220-20.0, and that Fig. 12 shows temperature and normalized particle number densities at 1 s after collapse.
- Fig. 12 caption identifies the right panel as the SFHo-18.8 particle number-density profile normalized to \(n_0=0.181\,\mathrm{fm}^{-3}\).
- Footnote 12 directs full profile data to the Garching Core Collapse Supernova Archive.

## 3. Consequence for the planned comparison

The comparison remains valuable, but its purpose changes:

- \(T_{\rm Caputo}(r)\) vs \(T_{\rm EK}(r)\): test figure extraction, model labeling, radial calibration, and whether the two papers used the same snapshot/version.
- \(n_p^{\rm Caputo}(r)\) vs \(p_{\rm EK}(r)\): test proton-density convention and figure consistency.
- \(n_B^{\rm Caputo}(r)\) vs \(n_n^{\rm EK}(r)+n_p^{\rm EK}(r)\): test whether the plotted n,p curves represent all baryons or only free nucleons. Do not assume equality before checking the EOS species convention.
- \(n_e+n_\mu\) vs positive charge: use charge neutrality as a consistency diagnostic, including the possible positive charge of nuclei/clusters. Do not impose closure by rescaling digitized curves.

If the profiles agree, this is a useful independent publication-level reproduction check, but not an independent simulation uncertainty estimate. If they disagree, investigate snapshot version, model implementation, species definition, normalization, radial coordinate, and digitization before attributing the difference to physics.

## 4. Implication for the Caputo charge-closure residual

The residual
\[
\Delta_Q(r)=\frac{n_p(r)-n_e(r)-n_\mu(r)}{n_0}
\]
from the Caputo figure is not by itself proof of a missing nuclear-cluster component. It is evidence that the meaning of the plotted \(n_p\) and the treatment of positive charge must be clarified. The cross-publication Fig. 12 comparison can help, but only after the curves are digitized and their species conventions are known.

## 5. Status and restrictions

- Source pages and captions are verified.
- The APS PDF page 15 render is available for visual inspection.
- No numerical Fig. 12 density digitization or pointwise residual is claimed yet.
- No raw Garching profile data have been obtained.
- No B.2 opacity, vector Fig. 7 result, or axial cooling curve is modified.

## 6. Next steps

1. Digitize Fig. 12 \(T,n_n,n_p\) from the published PDF with explicit pixel uncertainty.
2. Compare its SFHo-18.8 temperature curve against the existing Caputo \(T(r)\) vertices.
3. Compare the two proton curves and determine whether their figure-level normalizations agree.
4. Compare \(n_n+n_p\) with Caputo \(n_B\) only as a diagnostic of the free/bound baryon partition.
5. Seek the archive variable definitions or original Garching data documentation to identify the exact species conventions.
6. Keep the free-nucleon collision kernel restricted to radii/compositions where its input densities are physically defined.



## 7. Follow-up status: Fig. 12 numerical extraction completed

The planned Fig. 12 extraction and pointwise comparison in §§5–6 are completed
in [B16_P1IIID_FIG12_VECTOR_EXTRACTION_CROSSCHECK_2026-11-11.md](B16_P1IIID_FIG12_VECTOR_EXTRACTION_CROSSCHECK_2026-11-11.md).
The extracted curves are native PDF vector paths. The temperature curve agrees
with the Caputo profile and Bollig Fig. 1 at sub-percent figure-reading
precision; the right-panel n,p curves agree with Caputo reconstructed
free-neutron and free-proton densities at the ten common radii from 1 to 15 km,
provided the right-panel density-axis top-two labels are interpreted as a
one-decade printing inconsistency. This remains a cross-publication figure
check of the same Garching SFHo-18.8 lineage, not an independent simulation
validation.
