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

- The Caputo and Esseili–Kribs figure sources, captions, and shared
  SFHo-18.8 model lineage are verified.
- The Esseili–Kribs Fig. 12 temperature, neutron, and proton paths are now
  extracted from the checksum-pinned SCOAP3 copy of the published APS PDF.
- The extraction and cross-check workflow passed GitHub Actions Run
  [#42955259591](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42955259591).
- The source PDF is a published-figure source, not raw Garching simulation
  data. No byte-identical original profile snapshot has been obtained.
- No B.2 opacity, vector Fig. 7 result, escape probability, or axial cooling
  curve is modified by this figure-level audit.

## 6. Completed numerical comparison

The completed native-vector comparison is documented in
[B16_P1IIID_FIG12_VECTOR_EXTRACTION_CROSSCHECK_2026-11-11.md](B16_P1IIID_FIG12_VECTOR_EXTRACTION_CROSSCHECK_2026-11-11.md).

- \(T_{\rm EK}(r)\) vs Caputo Fig. 1: 55 common radii, RMS relative residual
  0.0707%, maximum absolute residual 0.218%.
- \(T_{\rm EK}(r)\) vs Bollig Fig. 1: 391 radii from 0.5 to 20 km, RMS
  relative residual 0.0953%, maximum absolute residual 0.277%.
- \(n_p^{\rm EK}(r)\) vs Caputo reconstructed free-proton density: ten radii
  from 1 to 15 km, RMS relative residual 0.586%.
- \(n_n^{\rm EK}(r)\) vs Caputo reconstructed free-neutron density: the same
  ten radii, RMS relative residual 0.580%.
- \(n_n^{\rm EK}+n_p^{\rm EK}\) vs Caputo free baryons
  \((1-X_{\rm cluster})n_B\): RMS relative residual 0.574%.
- The apparent deficit relative to total \(n_B\) is explained by the cluster
  baryon fraction \(X_{\rm cluster}=1-Y_n-Y_p\), which rises from zero in the
  inner comparison region to 8.85% at 15 km.

The upper two density-axis glyphs are visually ambiguous vector outlines and
are not exposed as PDF text spans. Both axis mappings are archived; equal
logarithmic spacing anchored by the lower three ticks and the Caputo
free-nucleon comparison select the calibration with upper values \(1\) and
\(10^{-1}\). This is not asserted to be a definitive typesetting error.

This is a cross-publication figure-level consistency test within a shared
Garching SFHo-18.8 model lineage, not an independent hydrodynamic simulation
validation. The sub-percent residuals are below the figure line-width
uncertainty and should not be interpreted as raw-profile precision.

## 7. Next research stage

P1-IIId is complete at the published-figure level. The next useful task is to
connect the validated free-nucleon profiles to the P1-IIIe real-EOS occupation
calculation:

1. Map \(T(r)\), \(n_n^{\rm free}(r)\), and \(n_p^{\rm free}(r)\) onto the
   authenticated SFHo EOS tables.
2. Compute local neutron/proton chemical potentials and occupation/degen-
   eracy factors on the radial profile, keeping free nucleons distinct from
   cluster-bound baryons.
3. Quantify the radial support and size of the cluster fraction in the
   8–15 km region before using a free-\(nn,np,pp\) kernel there.
4. Keep the cluster response as a separate uncertainty/contribution; do not
   rescale the free-nucleon kernel to absorb it.
5. Only after the local profile-to-EOS mapping closes should these inputs be
   used in any revised B.2 transport or axial cooling calculation.

