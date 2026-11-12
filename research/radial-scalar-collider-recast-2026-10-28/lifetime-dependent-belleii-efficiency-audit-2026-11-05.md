# Belle II lifetime-dependent selection: evidence audit and required simulation

**Date:** 2026-11-05  
**Scope:** original one-VEV \(S+\mathrm{VLL}\) radial scalar. No new field content and no referee-response change.

## 1. What the publications actually establish

### Four-muon search

The Belle II four-muon paper (arXiv:2403.02841, Phys. Rev. D 109, 112015) states that, for the couplings explored in its muonphilic-scalar and vector benchmarks, the lifetime of \(X\) is negligible compared with the experimental resolution. It generates prompt scalar signal samples with MadGraph5_aMC@NLO including ISR, and describes detector simulation with Geant4 and the Belle II software framework.

The analysis requires the transverse and longitudinal track DCA projections to satisfy
\[
|d_0|<0.5\ {\rm cm},\qquad |z_0|<2.0\ {\rm cm}.
\]
The publication does not provide a lifetime-dependent efficiency curve for a displaced scalar or a public table of signal efficiency versus proper lifetime.

### Tau-pair search

The Belle II tau-pair paper (arXiv:2306.12294, Phys. Rev. Lett. 131, 121802) uses signal simulation with MadGraph5_aMC@NLO including ISR, followed by detector simulation with Geant4 and the Belle II framework. It applies the same quoted track-DCA requirements:
\[
|d_0|<0.5\ {\rm cm},\qquad |z_0|<2.0\ {\rm cm}.
\]
The paper reports scalar-specific selection efficiency and its difference from the vector benchmark, but does not publish a lifetime scan, a displaced-scalar efficiency curve, or an efficiency map versus decay radius.

The absence of a lifetime curve is not evidence that displaced points pass the prompt selection.

## 2. Existing UV geometry diagnostic

The width scan computes
\[
L_{\rm mean}^{\rm max}
=(\beta\gamma)_{\rm max}\,c\tau_s,
\]
where \((\beta\gamma)_{\rm max}\) is a conservative kinematic maximum for \(e^+e^-\to\mu^+\mu^-s\), with the dimuon recoil at threshold and the SuperKEKB lab boost applied.

This is only a parent flight-length scale. It is not a track DCA, nor a reconstruction efficiency. The daughter directions, scalar decay position, detector geometry, tracking, particle identification, trigger, and MLP selection all enter the actual acceptance.

For the currently evaluated width-complete narrow/prompt subset:

- The 1,852 conditional four-muon excluded points have maximum \(L_{\rm mean}^{\rm max}=0.209\) mm, substantially below the 5 mm transverse DCA scale. Their prompt-benchmark assumption is therefore geometrically well motivated, though still not a substitute for a displaced-vertex detector study.
- The four-muon table separately marks 946 points as lifetime-sensitive under the 5 mm mean-flight screen.
- The tau-pair table marks 15 points as lifetime-sensitive under the same screen. No tau-pair point is excluded in the evaluated narrow/prompt subset.

These counts inherit the archived scan's limitation: all rows whose branching-fraction sum is incomplete remain unclassified.

## 3. What is required for a real lifetime-dependent efficiency

A validated efficiency map requires, separately for the two analyses:

1. Generate the original-UV scalar in \(e^+e^-\to\mu^+\mu^-s\) with the correct spin-0 FSR matrix element and ISR treatment.
2. Sample the proper decay time from the UV total width at each \((m_s,m_{A'},g_X)\) point and boost the decay vertex into the Belle II laboratory frame.
3. Propagate the \(\mu\mu\) or \(\tau\tau\) daughters through the detector geometry and material with the relevant detector simulation.
4. Reconstruct tracks and apply the published trigger, track-quality, DCA, particle-identification, and MLP selections.
5. Measure the selected/generated ratio as a function of \(m_s\), \(c\tau_s\), and the relevant production kinematics. For the tau analysis, retain the one-prong tau-decay restrictions and the tagging-muon requirements.
6. Validate the zero-lifetime limit by reproducing the collaboration's prompt scalar efficiency before trusting any displaced result.

The public papers do not provide the full MLP model weights, event-level selection implementation, or lifetime-dependent efficiency samples needed to do this exactly outside the Belle II analysis framework. A detector-level lifetime recast is therefore blocked on the required experiment software/selection inputs or collaboration-provided efficiency maps.

## 4. Current conclusion

The published prompt scalar coupling limits can be used conditionally for points whose UV decay lengths are much smaller than the relevant DCA scales. The current 5 mm screen is a transparent geometry diagnostic, not a hard lifetime cut. Points flagged lifetime-sensitive remain unclassified for detector-level acceptance.

No efficiency is invented, no DCA cut is treated as a decay-radius cut, and no displaced-point exclusion is claimed. The 1,852 four-muon exclusions remain conditional on the prompt benchmark, while the tau search has no exclusions in its evaluated narrow/prompt subset.
