# P1-IIId: Public SFHo-18.8 snapshot and nucleon-composition provenance audit

Date: 2026-11-10  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Why this audit is required

P1-IIIc has completed local free-nucleon transport moments for an illustrative point \(T=3.03\) MeV, \(Y_p=0.10\), \(n_B/n_0=10^{-3}\). This point is not a radial SFHo-18.8 input.

Before evaluating the collision kernel along the star, we need co-located and internally consistent
\[
T(r),\quad n_B(r),\quad n_n^{\rm free}(r),\quad n_p^{\rm free}(r),
\]
and, where relevant, the abundance of nuclei or other baryonic species. It is not generally valid to infer \(n_n=n_B-n_p\) unless \(n_p\) and \(n_B\) use compatible species definitions and no additional baryonic components are present.

## 2. Primary source: Caputo et al. Fig. 1

A. Caputo, G. Raffelt, and E. Vitagliano, *Muonic boson limits: Supernova redux*, Phys. Rev. D 105, 035022 (2022), arXiv:2109.03244v3, Fig. 1.

The paper explicitly identifies Fig. 1 as the Garching muonic SN model SFHo-18.8 at \(t_{\rm pb}=1\) s. Its upper panel shows chemical potentials, temperature, plasma frequency, and screening scale; the lower panel shows number densities normalized to \(n_0=0.181\ {\rm fm}^{-3}\).

The current repository reconstruction is based on the vector drawing paths of the same public PDF:
- \(T(r)\): path 0;
- \(\mu_\mu(r)\): path 1;
- \(\mu_{\nu_\mu}(r)\) branches: paths 6 and 7;
- \(n_\mu(r)/n_0\): path 161.

**Important gap:** the existing extraction script and profile provenance record do not yet digitize the \(n_B(r)\), \(n_p(r)\), or \(n_e(r)\) paths from the lower panel. Those curves must not be reconstructed from visual guesses or inferred from \(n_\mu\).

The immediate task is to identify the exact vector-path indices for \(n_B,n_p,n_e\) from the source PDF, record their axis calibration and source vertices, and add them to the provenance record. The existing source-PDF SHA-256 must remain unchanged.

## 3. Independent public density plot: Esseili and Kribs Fig. 12

H. Esseili and G. D. Kribs, *Hiding a light vector boson from terrestrial experiments: A chargephobic dark photon*, Phys. Rev. D 114, 016023 (2026), Fig. 12.

The paper states that it uses four representative models, including SFHo-18.8, and shows temperature profiles and normalized particle number densities at 1 s after core collapse. The right panel includes neutron and proton number-density curves, along with leptonic species. The figure uses the same normalization \(n_0=0.181\ {\rm fm}^{-3}\). The paper directs readers to the Garching Core-Collapse Supernova Archive for the full profile data and cites Bollig et al. for the model family.

This is a valuable independent public source for \(n_n(r)\) and \(n_p(r)\). However, the shared label “SFHo-18.8” and time “1 s” are not, by themselves, enough to justify merging its curves with the Caputo reconstruction. Before using it as the same snapshot, we require a point-by-point figure-level compatibility test:
1. digitize the SFHo-18.8 temperature curve in Fig. 12;
2. compare it with the Caputo \(T(r)\) reconstruction over the common radial interval;
3. digitize the \(n_n,n_p\) curves and compare the proton curve with Caputo's \(n_p\) curve;
4. test whether \(n_n+n_p\) is consistent with Caputo's \(n_B\), allowing for clearly identified non-free baryonic components and differences in species definitions.

Until these tests pass, Fig. 12 is a cross-check candidate, not an input to be spliced into the Caputo profile.

The paper's full-profile link points to the Garching archive. The direct hydro-profile endpoint is access-controlled in the present access path; no private/raw data are assumed or redistributed.

## 4. Separate EOS-composition diagnostic: SFHoY

The dissertation *Phenomenology of Light Particles on Earth and in the Sky*, Fig. 8.1, shows \(Y_n,Y_p,Y_\Lambda\) for an 18.8-\(M_\odot\) model about 1 s after bounce. Its text states that:
- the temperature profile is based on the supernova simulation input;
- the composition is calculated with CompOSE using the SFHoY equation of state;
- the input includes baryonic energy density, temperature, and total lepton fraction \(Y_\ell=Y_e+Y_\mu\);
- SFHoY includes hyperons;
- deuterium and tritium nuclei, which compensate part of the apparent charge imbalance, are not plotted.

This is useful as an **alternative EOS-composition reconstruction** from related simulation input. It is not the original SFHo composition: SFHoY adds hyperons and has an explicit cluster-content issue. It must therefore remain a separate sensitivity scenario, not be silently merged into the Caputo SFHo baseline.

In particular, the plotted \(Y_n+Y_p\) need not equal unity because \(Y_\Lambda\) and unshown nuclear clusters carry baryon number.

## 5. Consequence for the P1-IIIb kernel

The P1-IIIb kernel currently describes scattering on free neutrons and free protons. It does not describe coherent/inelastic scattering on deuterium, tritium, alpha particles, or heavy nuclei.

Therefore:
- do not set \(n_n^{\rm free}=n_B-n_p^{\rm free}\) without a verified composition closure;
- do not interpret \(Y_p=0.10\) from P1-IIIc as a stellar-profile measurement;
- do not extend the free-nucleon kernel through a cluster-rich layer while silently assigning all baryon density to free nucleons;
- where clusters are relevant, either add the corresponding nuclear response or restrict the free-nucleon-only calculation to a validated nucleon-dominated radial domain and quantify the omitted layer separately.

The distinction is especially important for the 15–20 km region, where the public composition study explicitly notes unplotted D/T nuclei. The 8–15 km region should be checked separately rather than assumed to be compositionally identical.

## 6. P1-IIId execution order

1. Extend the Caputo vector-PDF extraction to \(n_B,n_p,n_e\), retaining all original PDF vertices and recording the exact path indices.
2. Independently digitize the SFHo-18.8 \(n_n,n_p,T\) curves in Esseili–Kribs Fig. 12.
3. Compare the two public reconstructions over their common radius range and adjudicate whether they represent the same numerical profile and species conventions.
4. Digitize the SFHoY \(Y_n,Y_p,Y_\Lambda\) composition as a separate EOS-variant diagnostic; do not merge it with the baseline.
5. Establish a radial free-nucleon validity mask and quantify the cluster/hyperon baryon fraction where the information permits.
6. Only then build the radial \(n_n^{\rm free}(r),n_p^{\rm free}(r)\) inputs and integrate the P1-IIIb collision kernel.

No B.2 opacity, transport sphere, escape probability, pure-vector Fig. 7 result, or axial cooling curve is changed in this source audit.
