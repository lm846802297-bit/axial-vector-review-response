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
- The paper presents scalar-specific signal-efficiency information as a function of mass. The scalar efficiency must be used; the vector-mediator efficiency is not interchangeable because the production kinematics differ.
- The track selection includes a transverse impact-parameter requirement at the 0.5 cm scale (and a looser longitudinal requirement). This is a track-DCA selection, not a direct cut on the scalar decay radius.
- The numerical supplementary table archived in this PR provides the mass-dependent observed/expected scalar coupling limits and associated numerical fit results.

Not supplied in the inspected numerical material:
- the complete numerical Crystal-Ball tail parameters and relative fractions at each mass;
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
- The paper quotes a signal efficiency that decreases from roughly 12% near threshold to roughly 2% at 10 GeV. Trigger efficiency is also mass dependent.
- The track selection uses transverse and longitudinal DCA requirements of order 0.5 cm and 2 cm, respectively.
- The arXiv ancillary limits.csv file provides the mass-dependent observed and expected scalar coupling limits used in this PR.

Not supplied in the inspected numerical material:
- the complete numerical Crystal-Ball tail parameters and component fractions needed to reconstruct the recoil-mass response at each mass;
- a two-dimensional efficiency map versus \(m_s\) and proper lifetime/decay position;
- the event-level signal template needed to refit the observed spectrum after broadening a narrow scalar resonance.

The published scalar coupling limit includes the prompt benchmark's selection and efficiency. The current narrow/prompt mapping therefore uses the published scalar limit directly and applies only the UV branching-fraction correction. The finite-width and displaced cases cannot be inferred from that limit curve alone.

## 3. What can be done without inventing detector inputs

1. Retain the current published-limit mapping for points whose full width interval is narrow relative to the experimental mass resolution and whose maximum-kinematic mean-flight interval passes the conservative prompt geometry proxy.
2. Digitize the published prompt scalar-efficiency curves as a separately labelled numerical input, with a digitization uncertainty. Do not treat them as lifetime-dependent efficiencies.
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
