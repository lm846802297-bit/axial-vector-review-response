# Belle II detector-response input audit — 2026-11-09

**Purpose:** determine which published inputs are sufficient for the current narrow/prompt coupling-limit mapping and which are missing for finite-width or lifetime-dependent reinterpretations.  
**Scope:** Belle II four-muon scalar search (arXiv:2403.02841) and tau-pair scalar search (arXiv:2306.12294).  
**Conclusion:** the published scalar coupling limits are sufficient for the current narrow/prompt pointwise mapping. The papers describe Crystal-Ball signal PDFs and provide mass-resolution/efficiency information, but the public material inspected here does not supply the complete numerical response parameters or a lifetime-dependent efficiency map needed for a validated finite-width/displaced recast.

## 1. Four-muon scalar search

**Reference:** Belle II, Phys. Rev. D 109, 112015 (2024), arXiv:2403.02841.  
https://arxiv.org/abs/2403.02841

Published information relevant to the recast:
- The signal mass is reconstructed in the reduced-mass variable \(M_R=\sqrt{M_{\mu\mu}^2-4m_\mu^2}\).
- The signal PDF is constructed from a sum of two Crystal-Ball functions with a common mean.
- The mass resolution is mass dependent: approximately 2--2.5 MeV in the low-mass region, rising to about 5 MeV at intermediate masses and decreasing toward about 2.5 MeV near 9 GeV.
- Figure 10 presents separate scalar- and vector-specific full-selection efficiencies versus mass. The scalar curve is digitizable as a supporting prompt-efficiency input; the vector curve is not interchangeable because the scalar is produced through a p-wave process and has different kinematics.
- The track selection includes a transverse impact-parameter requirement at the 0.5 cm scale (and a looser longitudinal requirement). This is a track-DCA selection, not a direct cut on the scalar decay radius.
- The scan step is one mass-resolution unit and each fit spans 60 resolution units. The (J/\psi) interval 3.07--3.12 GeV is vetoed. A 7% yield correction accounts for the resolution degradation observed in the (J/\psi) control sample.
- The numerical supplementary table archived in this PR provides the mass-dependent observed/expected scalar coupling limits and cross-section results, but not the full signal-response kernel.

Not supplied in the inspected numerical material:
- the complete numerical Crystal-Ball tail parameters and relative fractions at each mass;
- a tabulated numerical representation of the scalar efficiency curve in Fig. 10 (the plotted curve can be digitized with an uncertainty);
- an event-level response kernel that can be convolved with an arbitrary finite scalar width;
- an efficiency map versus scalar proper lifetime or decay position.

The published prompt scalar coupling limit already includes the prompt scalar selection efficiency. Therefore the current narrow/prompt UV-to-limit mapping does not need a second efficiency rescaling. A finite-width convolution does need the response kernel, not merely the published upper-limit curve.

## 2. Tau-pair scalar search

**Reference:** Belle II, Phys. Rev. Lett. 131, 121802 (2023), arXiv:2306.12294.  
https://arxiv.org/abs/2306.12294

Published information relevant to the recast:
- The scalar recoil mass is reconstructed from the tagged \(\mu^+\mu^-\) system.
- The signal PDF is described by a sum of two Crystal-Ball functions sharing a common mean.
- The recoil-mass resolution is mass dependent: approximately 30 MeV near the \(\tau^+\tau^-\) threshold, 10 MeV around 6 GeV, and 1 MeV near 10 GeV.
- The paper quotes an overall signal-efficiency trend from roughly 12% near threshold to roughly 2% at 10 GeV and reports model-dependent efficiency differences of order 10--20% for alternative signal models. The trigger efficiency is also mass dependent (about 96% up to 8 GeV, 90% near 9 GeV, and 50% near 10 GeV). The published scalar-specific limit already incorporates the scalar benchmark efficiency, but the ancillary limits.csv file is a limit table rather than a mass-resolved scalar-efficiency table.
- The mass scan uses steps of half a mass-resolution unit and a fit interval of 40 resolution units.
- The track selection uses transverse and longitudinal DCA requirements of order 0.5 cm and 2 cm, respectively.
- The arXiv ancillary limits.csv file provides the mass-dependent observed and expected scalar coupling limits used in this PR.

Not supplied in the inspected numerical material:
- the complete numerical Crystal-Ball tail parameters and component fractions needed to reconstruct the recoil-mass response at each mass;
- a mass-resolved numerical scalar-efficiency table (the published scalar limit folds in the efficiency, while the quoted efficiency trend and model-dependent differences do not determine the full scalar curve);
- a two-dimensional efficiency map versus \(m_s\) and proper lifetime/decay position;
- the event-level signal template needed to refit the observed spectrum after broadening a narrow scalar resonance.

The published scalar coupling limit includes the prompt benchmark's selection and efficiency. The current narrow/prompt mapping therefore uses the published scalar limit directly and applies only the UV branching-fraction correction. The finite-width and displaced cases cannot be inferred from that limit curve alone.

## 3. What can be done without inventing detector inputs

1. Retain the current published-limit mapping for points whose full width interval is narrow relative to the experimental mass resolution and whose maximum-kinematic mean-flight interval passes the conservative prompt geometry proxy.
2. Digitize the four-muon scalar-efficiency curve in Fig. 10 as a separately labelled prompt input, with a digitization uncertainty. For the tau-pair analysis, do not infer a full scalar-efficiency curve from the quoted overall range or the 10--20% model-dependent difference. Neither input is a lifetime-dependent efficiency.
3. Use the published mass-resolution curves as resolution envelopes for sensitivity diagnostics. Do not infer Crystal-Ball tail parameters from the resolution alone.
4. Keep finite-width-sensitive points unclassified until a validated signal response kernel is available.
5. Keep lifetime-sensitive points unclassified until the selection efficiency is known as a function of decay position or proper lifetime.
6. Do not substitute the vector-mediator efficiency for the scalar efficiency, and do not convert a DCA requirement directly into a decay-radius cut.

## 4. Consequence for the current PR #68 result

The current 2,746 four-muon and zero tau-pair conditional exclusions use the published scalar-specific prompt limits. They do not require a new detector efficiency model because the reference efficiency is already folded into those limits. The classification is conditional on the narrow-width and prompt-geometry proxies.

The remaining 8,673 four-muon and 3,286 tau-pair finite-width-sensitive points, together with the lifetime-sensitive points, are not classified by this result. The response audit does not promote them to allowed or excluded.

## 5. References

- Belle II four-muon search: https://arxiv.org/abs/2403.02841
- Belle II tau-pair search: https://arxiv.org/abs/2306.12294


## 6. Fit-scan structure relevant to finite-width studies

The four-muon analysis performs unbinned maximum-likelihood fits at mass steps equal to the mass resolution, with a fit interval of \(60\sigma\). It excludes \(3.07\text{--}3.12\) GeV around the \(J/\psi\), and applies a 7% yield correction for the resolution degradation inferred from the control sample. Figure 10 gives a scalar-specific prompt-efficiency curve that can be digitized, but the numerical supplementary table supplies limits rather than the two-Crystal-Ball response parameters.

The tau-pair analysis uses mass steps of \(\sigma/2\) and a fit interval of \(40\sigma\). It quotes an overall efficiency trend and model-dependent efficiency differences, but the ancillary limits.csv file does not provide a mass-resolved scalar-efficiency curve or the two-Crystal-Ball tail parameters.

Consequently, a finite-width calculation cannot be obtained by convolving a Breit-Wigner with a Gaussian of the quoted \(\sigma\) and calling the result the published response. Such a Gaussian convolution can be used only as a labelled sensitivity diagnostic. A validated finite-width CLs reinterpretation still requires the response parameters (or a response kernel), the scalar efficiency versus mass, and the background/likelihood information needed to repeat the fit.
