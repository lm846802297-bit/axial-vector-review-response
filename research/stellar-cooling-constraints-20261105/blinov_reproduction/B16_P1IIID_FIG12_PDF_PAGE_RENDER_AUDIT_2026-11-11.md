# P1-IIId: Fig. 12 PDF-page render audit and comparison limits

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Exact published PDF page verified

The APS PDF was opened directly:
https://journals.aps.org/prd/pdf/10.1103/718s-7k7v

The relevant page is PDF page index 14, printed page 15 (Fig. 12). A page rendering was obtained at 1088 × 1536 pixels. The figure is therefore now visually available at a larger page-render resolution than the earlier 400 × 400 preview. This is a page screenshot, not the native APS image asset and not a locally archived original binary.

The figure labels are legible:
- left panel: orange curve is SFHo-18.8; green is SFHo-18.6; blue/cyan curves are LS220-20.0 and SFHo-20.0;
- right panel: \(n\), \(p\), \(e\), \(\mu\), and neutrino species;
- right-panel density is logarithmic and normalized to \(n_0=0.181\,\mathrm{fm}^{-3}\).

The caption says the right panel is the particle number-density profile in SFHo-18.8. The surrounding text states that the profiles are at 1 s after core collapse and that full profile data are at the Garching archive.

## 2. Temperature profile: comparison classification

The orange SFHo-18.8 curve has the same broad radial structure as the Caputo Fig. 1 temperature profile already extracted from the checksum-verified \`SNProfile.pdf\`:
- central plotted temperature about 19 MeV;
- maximum about 39–40 MeV around 8–9 km;
- decline to about 13 MeV around 15 km;
- a few MeV near 20 km.

This is a **qualitative visual consistency check only**. No point-by-point \(T_{\rm EK}(r)\) digitization, RMS residual, or maximum fractional residual is claimed in this record. A reproducible numerical comparison still requires pixel-level digitization of the page or acquisition of the native figure asset.

## 3. What the right panel does and does not establish

The plotted labels identify neutron and proton number-density curves, but the caption does not specify whether these are free-nucleon densities or total nucleon-equivalent densities including bound nuclei. It is therefore not justified to assume
\[
n_n^{\rm EK}+n_p^{\rm EK}=n_B^{\rm Caputo}
\]
as an identity before the particle definitions are checked.

Likewise, the Caputo Fig. 1 labels \(n_B,n_p,n_e,n_\mu\), but the figure alone does not define the exact partition of baryon number and positive charge among free protons and nuclear clusters. The outer-radius charge-closure residual found from the digitized curves is a diagnostic that this distinction matters; it is not proof of one specific nuclear-species interpretation.

## 4. Current comparison matrix

| Comparison | Current status | Permitted interpretation |
|---|---|---|
| Caputo \(T(r)\) vs Fig. 12 SFHo-18.8 \(T(r)\) | Broad shape and scale visually consistent | Qualitative agreement only |
| Caputo \(n_p(r)\) vs Fig. 12 \(p(r)\) | Both curves visible, no numerical digitization yet | No quantitative claim |
| Fig. 12 \(n_n+n_p\) vs Caputo \(n_B\) | Species convention unresolved | Diagnostic only; not an identity |
| Charge closure \(n_p-n_e-n_\mu\) in Caputo | Outer residual grows beyond about 9 km | Requires composition/species interpretation; do not rescale |

## 5. Next operation

The exact PDF page render is sufficient to guide a coarse manual digitization, but the reproducible extraction pipeline should still use a local image/PDF byte stream. The next data product must preserve:
- original source PDF or native figure image and SHA-256;
- page number and pixel dimensions;
- panel crop bounds;
- axis calibration points;
- raw pixel coordinates for each curve;
- log-scale transformation for density;
- per-point uncertainty and curve-label assignment.

Until that data product exists, do not claim numerical cross-validation and do not feed Fig. 12 digitized values into the B.2 production calculation.
