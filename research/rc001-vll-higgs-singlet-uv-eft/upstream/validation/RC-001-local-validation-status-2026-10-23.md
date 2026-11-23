# RC-001 local validation status — 2026-10-23

**CI disposition:** explicitly skipped by project decision because GitHub Actions repeatedly failed before starting a runner. This is not a CI pass and is not treated as a physics result.

## Local checks performed

| Check | Result | What it establishes | What it does not establish |
|---|---|---|---|
| Charge-aware \(Q_{LD}/Q_{RD}\) attachment census | PASS | Counts of allowed unordered gauge line-pair classes for \(\mu,\tau\); signed \(B-A'\) charge-factor cancellations | Individual Feynman-diagram multiplicities, loop numerators, or coefficients |
| \(Q_{LD}\) \(SU(2)_L\) generator contractions | PASS | Exact tensor decomposition of all six \(WW\) line-pair classes into singlet/triplet tensors | Loop integrals, graph signs beyond the generator contraction, or finite Wilson coefficients |
| Diagonal-gauge input-parameter counterterm algebra | PASS | Exact rational combination \(2\delta y/y-2\delta M_E/M_E\) and \(2\delta\lambda/\lambda-2\delta M_E/M_E\) for the stated standard MS pole formulas | Independent derivation of the general counterterm formulas, mixed kinetic-mixing terms, EFT operator counterterms, or full UV–EFT matching |
| Light-only external-leg factor cancellation | ANALYTIC IDENTITY | With matched tree amplitudes and identical light-field conventions, common light-leg gauge factors multiply the same tree amplitude and cancel in the UV–EFT difference at \(O(M_E^{-2})\) | Heavy-line corrections, finite field decoupling, external gauge-field thresholds, or the complete Ward-identity sum |
| Heavy-\(E\) self-energy and scalar master integrals | PASS (local algebra only) | Exact Feynman-parameter integrals at \(p^2=0\), \(dB_0=4\Delta_\epsilon+2-4L_E\), crossed-box partial fractions, and the displayed UV/IR split; see the local reproduction log | Full vertex/box graph signs, multiplicities, and Wilson coefficients |
| Additive \(B-A'\) kinetic mixing | PASS (charge-trace algebra only) | \(\operatorname{Tr}(YX)=0\) for the stated light sector and across the \(\mu,\tau\) heavy pair; finite heavy threshold \(\propto\ln(M_{E_\mu}^2/M_{E_\tau}^2)\) | Independent \(\chi\) boundary, full kinetic-matrix scheme, and mixed-propagator four-point amplitudes |
| Conjugate Yukawa-vertex charge factors | PASS (exact rational algebra) | Hypercharge and \(X\)-charge conservation plus all signed \(F_B,F_X,F_{BX}\) pair factors for the four Yukawa vertices and both flavors | Overall Feynman-rule signs, loop integrals, and full vertex amplitudes |
| Light-only Yukawa-vertex hard cancellation | ANALYTIC IDENTITY | Tree propagator expansion and common light-loop factor cancel at \(O(M_E^{-2})\) when the full gauge-covariant EFT insertion/contact set is included | Full contact/vertex set has not been independently generated; final summed Ward identity remains open |
| Conditional mixed input-parameter counterterms | PASS (charge algebra only) | First-order signed \(B-A'\) parameter-only pole combinations for \(C_{LD}\) and \(C_{RD}\) under \(\rho_{BX}=-\chi+O(\chi^2)\) | Full kinetic-matrix renormalization, mixed vertex/box amplitudes, EFT operator counterterms, and Ward sum |
| Heavy-containing Yukawa-vertex hard sub-block | PASS (symbolic algebra only) | FF/FS numerator kernels, oriented charge factors, the finite \(dB_0\) term, six one-vertex pole/log/finite expressions, and conjugate-vertex doubling | No diagram-package reproduction; crossed boxes, full EFT contacts, common counterterm organization, Ward sum, and final Wilson coefficients remain open |

## Open physics evidence

- No FeynArts/FeynCalc, QGRAF, FORM, Cadabra, Sage, or equivalent diagram-level package was available in the probed runtime.
- The heavy-line self-energy, selected scalar master integrals, and heavy-containing FF/FS Yukawa-vertex sub-blocks are evaluated. The complete vertex/box amplitudes have not been combined; the LD/RD amplitude ledger rows remain open.
- The new \(O(g^2/M_E^2)\) UV loop integrals and corresponding EFT soft integrals have not been evaluated as a complete set.
- No finite gauge-correction Wilson coefficient is claimed.
- The shared UV/EFT pole tables, counterterm matrix, Ward-identity completion, kinetic-mixing terms, and full EOM/source/current projection remain open.
- PR #4 was merged as a research-continuity checkpoint. The merge does not close the physics gates above; CI remains skipped by explicit project decision and is not claimed to pass.
