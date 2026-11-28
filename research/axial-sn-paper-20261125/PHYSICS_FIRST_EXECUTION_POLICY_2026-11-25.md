# Physics-first execution policy for the axial SN paper

Date: 2026-11-25  
Repository: `lm846802297-bit/axial-vector-review-response`  
Branch: `research/axial-sn-paper-20261125`  
Authority: this note supersedes the sequencing and dependency statements in the initial research plan wherever they make the unresolved Blinov 10 MeV reproduction discrepancy a prerequisite for current axial-model physics work.

## Decision

The current research priority is **physical correctness of the axial-vector calculation**, not completion of the numerical reproduction of the published Blinov vector benchmark.

The approximately (+92.4284\%\) discrepancy in the 10 MeV strong-absorption tail is retained as an unresolved historical reproduction issue. It will be reopened when the original numerical inputs and sufficiently complete source data for the relevant benchmark are obtained. Until then:

- Do not tune normalization, profiles, or transport parameters to remove the discrepancy.
- Do not describe the old vector or axial contours as fully validated final exclusions.
- Do not make the discrepancy a blocking dependency for analytic derivations, local collision-kernel checks, Goldstone-limit checks, or internal consistency tests of the axial model.
- Do not rerun already archived calculations unless a specific physical or implementation issue requires it.
- Keep paper-reported values, existing archived calculations, and new independent calculations explicitly separate.

## Current main line: physics verification

Proceed in this order.

### P1. Model and current conventions

Acceptance:
- Fix the original one-VEV UV model and the mass-basis convention:
  [
  g_V^\mu=g_X\sin^2\theta_{\mu R},\qquad
  g_A^\mu=-g_X\cos^2\theta_{\mu R}.
  ]
- Preserve (g_{\nu_\mu}=+g_X) and (g_{\nu_\tau}=-g_X).
- Verify signs, chiral couplings, charge-conjugate muon conventions, and the mapping (m_{A'}=2g_Xv_s).
- Keep the finite-mixing benchmark and pure-axial limit distinct.
- Do not introduce additional neutrino states, a second scalar VEV, or a physical-scalar cooling channel into this first study.

### P2. Exact local amplitudes and polarization structure

Acceptance:
- Verify the complete (s)- and (u)-channel amplitudes for (mu^\pm\gamma\leftrightarrow\mu^\pm A'), including the photon Ward identity.
- Verify the axial-current Ward identity and the physical longitudinal polarization normalization.
- Check the (L,+,-) polarization basis, mode sums, positivity, kinematic thresholds, and finite-(m_{A'}) behavior.
- Retain amplitude-level vector/axial interference at finite (	heta_{\mu R}).
- Treat the Goldstone-equivalence relation as a limiting cross-check. The physical longitudinal (A') mode already contains this contribution; never add a separate Goldstone production rate.
- Independently check selected phase-space points with a separately organized implementation or analytic trace.

### P3. Thermal production, inverse processes, and decays

Acceptance:
- Construct the thermal moving-muon production and absorption kernels for both muon charges, with Fermi blocking and photon Bose enhancement.
- Check detailed balance mode by mode and charge by charge using the mediator energy and the stated chemical-potential conventions.
- Verify neutrino inverse decay and absorption with both active flavors and their correct normalization.
- Include the axial dimuon width above threshold when the mass range is extended beyond (2m_\mu); do not use the vector width in its place.
- Check all open channels and branching fractions consistently.
- Separate local emissivity from escaping luminosity.

### P4. Transport equations and controlled numerical studies

Acceptance:
- Verify the optical-depth and escape-probability equations, velocity factors, angular averages, decay terms, and any lapse/redshift factors used.
- Check that mode-resolved opacities are propagated with the corresponding mode-resolved source rates.
- Test limiting regimes: optically thin, optically thick/trapping, low-mass Goldstone limit, and threshold behavior.
- Use the currently archived reconstructed profile for controlled code/physics diagnostics where useful, while labeling all outputs as conditional on that reconstructed profile.
- Quantify radial, energy, angular, and coupling-grid convergence for new calculations.
- Do not require agreement with the published Blinov Fig. 7 high-coupling tail as an entry condition for these physics checks.

### P5. Physical cross-checks and interpretation

Acceptance:
- Compare the low-mass longitudinal kernel with the derivative-coupled muonic-pseudoscalar limit using exactly matched coupling normalization and kinematic assumptions.
- Compare the neutrino-only sector with the flavor-matched conventional (L_\mu-L_\tau) vector control under identical medium conditions.
- Compare pure-vector and axial/mixed-current kernels at identical kinematics and medium inputs; this is a theory-level comparison, not a claim of reproducing a published astrophysical contour.
- Verify energy accounting and detailed balance independently.
- State which conclusions are analytic, which are local-kernel results, and which depend on the reconstructed stellar profile.

## Deferred line: original-input reproduction

The Blinov 10 MeV strong-absorption-tail discrepancy remains recorded as:

- Historical reported discrepancy: approximately (+92.4284\%) relative to the digitized Fig. 7 target in the archived strict phase-space comparison.
- Status: **DEFERRED — awaiting original benchmark inputs / sufficiently complete source data**.
- Current action: preserve the archived source, outputs, hashes, and diagnostics unchanged.
- Reopen trigger: original inputs become available, or a specific newly identified physical inconsistency directly implicates the present calculation.
- Reopen scope: reproduce the reference calculation with its original inputs and conventions, identify the source of the discrepancy, and independently verify the correction. Do not use fitted normalization to force agreement.

This deferred reproduction task is not a gate for P1–P5. It remains relevant before making a final quantitative claim that the new axial exclusion contour is benchmark-validated against the published Blinov result.

## Publication claims and status discipline

Until the relevant gates are passed:

- A verified Ward identity is a verified analytic identity, not a validated supernova bound.
- A converged local kernel is a verified local rate, not a validated global luminosity.
- A converged transport integral on a reconstructed profile is a conditional profile result, not automatically a validated SN1987A exclusion.
- A vector-model reproduction discrepancy does not by itself invalidate a separately checked axial matrix element or thermal kernel.
- Conversely, passing local axial checks does not resolve the deferred vector benchmark discrepancy.

## Immediate next actions

1. Audit the existing original-UV axial amplitudes, Ward-identity tests, moving-muon B.13 kernels, and finite-mixing conventions; reuse passing evidence by exact source SHA.
2. Complete the full-text comparison with existing axial-supernova literature, especially Gori et al. and the polarization-resolved 2026 work, and define the precise novelty claim.
3. Perform targeted independent checks of the local axial kernels and detailed balance; do not launch a broad parameter scan before these pass.
4. Validate the transport equations and limiting regimes on existing profile inputs, clearly labeling the profile dependence.
5. Resume the Blinov 10 MeV reproduction only after the original inputs are obtained, unless a concrete physics error requires earlier investigation.
