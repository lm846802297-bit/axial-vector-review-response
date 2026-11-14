# P1-IIId: APS Fig. 12 source-access record

> Historical access record: later work reports local PDF vector extraction; consult [the subsequent extraction audit](B16_P1IIID_FIG12_VECTOR_EXTRACTION_CROSSCHECK_2026-11-11.md) for its scope and status.

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Primary figure resource located

The APS published article page exposes Fig. 12 as a separate figure-deliverable resource:

https://journals.aps.org/prd/article/10.1103/718s-7k7v/deliverable/53a3ed45-c49f-4d41-8efb-a0a38db4c508

The linked resource was opened and visually confirmed to contain the correct two-panel Fig. 12:
- left: temperature profiles for SFHo-18.6, SFHo-18.8, SFHo-20.0, and LS220-20.0;
- right: normalized particle densities for SFHo-18.8.

The published APS PDF is also directly accessible:
https://journals.aps.org/prd/pdf/10.1103/718s-7k7v

The relevant caption is on printed page 15 (PDF page index 14), and explicitly states that the right panel is the SFHo-18.8 particle number-density profile normalized to \(n_0=0.181\,\mathrm{fm}^{-3}\). The article text states that the four model profiles correspond to 1 s after core collapse and that full profile data are in the Garching archive.

## 2. Important correction to the previous execution status

The previous report described the high-resolution figure as not yet obtained. This should now be refined:

- **The exact APS figure resource has been located and visually verified.**
- The web rendering currently available to this execution is a 400-by-400 preview. This does not establish the native resolution of the underlying APS asset.
- Attempts to retrieve the binary image/PDF into the local numerical environment did not succeed in this session. Therefore, no machine-readable pixel array has yet been produced from the APS resource.
- No new \(T(r)\), \(n_n(r)\), or \(n_p(r)\) digitization is claimed in this addendum.

This distinction matters: source discovery is complete, but local image acquisition and numerical digitization are not.

## 3. Figure calibration to use once the image bytes are locally available

The two panels have independent axes and must be calibrated separately.

For the left temperature panel:
- horizontal axis: radius \(r\) in km, visibly spanning 0–20 km;
- vertical axis: temperature \(T\) in MeV, visibly spanning 0–60 MeV.

For the right density panel:
- horizontal axis: radius \(r\) in km, visibly spanning 0–20 km;
- vertical axis: \(n_i/n_0\), logarithmic, with labeled decade ticks.

Do not reuse a linear y calibration for the right panel. Preserve the individual curve labels and digitization uncertainties. The plotted species include neutron, proton, electron, muon, and neutrino curves.

## 4. Current scientific status

1. The source figure identity and caption are verified against the APS publication.
2. The broad temperature-profile consistency with Caputo remains qualitative; no pointwise residual is reported.
3. The independent neutron/proton density digitization remains pending.
4. The Caputo charge-closure residual remains a diagnostic of possible species-definition/composition effects, not proof that a specific cluster component has been omitted.
5. No Caputo curves are rescaled, and no free-neutron density is inferred as \(n_B-n_p\).
6. No B.2 opacity, Fig. 7 vector benchmark, or axial cooling result is changed.

## 5. Required next operation

Acquire the APS deliverable image bytes or the published PDF locally, verify the file checksum and native pixel dimensions, then digitize all three Fig. 12 curves \(T_{\rm SFHo-18.8}(r)\), \(n_n(r)\), and \(n_p(r)\). Store:
- the unmodified source image/PDF;
- source URL and checksum;
- axis calibration points;
- raw pixel coordinates;
- transformed radius and physical ordinate;
- curve masks and digitization uncertainty;
- reproducible extraction code.

Only after those records exist should pointwise Caputo comparisons be computed.
