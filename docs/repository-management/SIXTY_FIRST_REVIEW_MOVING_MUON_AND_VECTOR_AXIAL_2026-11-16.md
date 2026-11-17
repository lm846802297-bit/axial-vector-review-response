# Sixty-first review — moving-muon semi-Compton and vector-to-axial response

**Date:** 2026-11-16  
**Reviewed base:** `503fe7a3492ee03bb4e1b43403b10118ed45ce69`  
**Scope:** the next six `PENDING` entries in `docs/repository-management/DOCUMENT_AUDIT_REGISTER.csv` after the sixtieth review.  
**Disposition:** 2 `PASS_WITH_NOTES`, 3 `REVISION_REQUIRED`, 1 `HISTORICAL`.

This review checked the six documents against their equations, source code, machine-readable outputs, test files, and successful workflow records. It does not change any production collision kernel, local rate output, B.2 opacity, luminosity, Fig. 7 digitization, SN1987A limit, or axial-vector constraint.

## 1. Result summary

| Document | Result | Main finding |
|---|---|---|
| `B13_B14_LOW_MASS_SCAN_2026-11-08.md` | `PASS_WITH_NOTES` | The dated profile-A scan is reproduced by the 2026-11-12 profile-B scan to about \(10^{-9}\) relative precision. The newer output, not the old profile-A JSON, is the current reference. |
| `MOVING_MUON_SEMI_COMPTON_DERIVATION_2026-11-07.md` | `REVISION_REQUIRED` | The phase-space reduction and normalization agree with both implementations, but its header still says the production implementation is not validated. Pointwise explicit-spinor and local-rate validation has since been completed, with a specific \(\mu^+\) caveat. |
| `MOVING_MUON_THERMAL_INTEGRAL_DESIGN_2026-11-07.md` | `REVISION_REQUIRED` | Its invariant collision-integral formula does not state the factor of two for the initial-muon spin degeneracy, nor define whether the overline already contains that spin average. The later derivation and code do include the factor. |
| `MOVING_MUON_THERMAL_RATE_AUDIT_2026-11-07.md` | `PASS_WITH_NOTES` | Local production/absorption, mode-by-mode detailed balance, the dimuon integral, and explicit-spinor checks are supported. The \(\sum_{\pm,s}\) notation in the opening collision term needs a definition to remove a possible spin-counting ambiguity. |
| `VECTOR_ENDPOINT_GATE_2026-11-07.md` | `HISTORICAL` | This is the initial 2026-11-07 gate snapshot. It is superseded by the 2026-11-09 B.16 acceptance gate and Fig. 7 reevaluation, with a later 2026-11-15 review addendum. The pure-vector gate remains blocked. |
| `VECTOR_TO_AXIAL_RESPONSE_MAPPING_2026-11-07.md` | `REVISION_REQUIRED` | Its header says the numerical scan is the next task, but the 2026-11-12 response scan and successful workflow now exist. The document must report those local results and retain the no-universal-rescaling conclusion. |

## 2. Individual findings

### 2.1 Low-mass B.13 versus B.14--B.16 scan — PASS_WITH_NOTES

The original report is a valid dated snapshot:
- workflow [#42435752134](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42435752134) succeeded with 40 tests;
- the original output used profile A, SHA `08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9`;
- the scan covered \(m_V=0.1,0.3,1,3\) MeV at \(r=0\) and \(12.5\) km, with the 10 MeV reference reused.

The current rerun is [workflow #43206544350](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544350), which succeeded on profile B, SHA `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`. It recomputed the four low-mass cases and archived `research/stellar-cooling-constraints-20261105/finite_mixing/outputs/b13_b16_low_mass_scan_2026-11-12.json`. The 10 MeV reference row is explicitly marked `recomputed=false`; it is reused from the profile-B 10 MeV comparison output.

Comparing the archived profile-A and profile-B low-mass JSONs at all eight new mass/radius points gives:
- maximum relative change in \(Q_{\rm B13}\): \(1.04\times10^{-9}\);
- maximum relative change in \(Q_{\rm B16}\): \(1.09\times10^{-9}\);
- maximum absolute change in \(Q_{\rm B13}/Q_{\rm B16}-1\): \(2.39\times10^{-11}\).

Representative profile-B results are:
- at \(r=0\), \(Q_{\rm B13}/Q_{\rm B16}-1=-51.8569\%\) at 0.1 MeV and \(-51.8612\%\) at 3 MeV;
- at \(r=12.5\) km, the corresponding values are \(-56.9891\%\) and \(-56.9931\%\);
- the explicit B.14 parenthesis correction is only \(3.40\times10^{-6}\) at 0.1 MeV and \(2.67\times10^{-3}\) at 3 MeV at the center.

Thus the large B.13/B.16 difference is not caused by the explicit \(m_V^2/(2\omega^2)\) term. The B.17-weighted muons are not parametrically nonrelativistic: the reported RMS velocities are about 0.617 and 0.690 at the two radii, and only 2.26% of the susceptibility weight at 12.5 km has \(p/m_\mu<0.3\). The paper's \(m_V\lesssim\mathrm{MeV}\) statement does not by itself justify either a nonrelativistic muon gas or negligible recoil.

The comparison remains a local emissivity audit. It is not a radial luminosity, opacity, escape-probability, or SN1987A calculation. Preserve the profile-A report as a dated record, but link the 2026-11-12 profile-B output when citing current numbers.

### 2.2 Moving-muon B.13 derivation — REVISION_REQUIRED

The phase-space reduction is internally consistent.

With
\[
D=E_p+\omega-\mathbf p\cdot\hat{\mathbf q}-k_A\cos\theta_q,
\qquad
q_\star=\frac{m_{A'}^2+2P\cdot K}{2D},
\]
the energy-delta Jacobian is \(E_{p'}/D\). It cancels the final-muon \(1/(2E_{p'})\) factor after the photon radial integral, leaving \(q_\star/D\). The change of variable \(x=(E_p-m_\mu)/T\) gives
\[
\frac{p^2}{E_p}\,dp=T p\,dx.
\]

The spin convention is also correct in this derivation: the trace averages the initial muon spin and sums the final muon spin and two physical photon polarizations; the phase-space rate then carries the physical initial-muon degeneracy two. Including the integrated initial-muon azimuth gives
\[
\frac{2}{16\omega(2\pi)^4}
=\frac{1}{128\pi^4\omega}.
\]
The legacy implementation uses \(1/(128\pi^4\omega)\); the newer `research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/moving_compton.py` implementation uses the algebraically identical \(2/[16\omega(2\pi)^4]\). No additional photon factor is to be inserted into the mode-resolved B.13 rate.

The document's header, however, still says “production implementation is not yet validated.” That is stale:
- workflow [#43534265182](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43534265182) passed;
- its direct explicit-spinor audit found maximum \(\mu^-\) spinor/trace residual \(1.4820\times10^{-13}\), photon-Ward amplitude residual \(6.8864\times10^{-13}\), final-muon shell residual \(6.52\times10^{-16}\), and vector-longitudinal Ward-shift residual \(4.77\times10^{-14}\);
- 5 explicit-spinor tests, 11 existing thermal-rate tests, 7 GR-ray tests, 7 polarization-state-counting tests, and 8 P1-B local-kernel tests passed.

The qualification must remain explicit: the \(\mu^-\) amplitudes are checked with direct positive-energy \(u\) spinors; the \(\mu^+\) rows use the charge-conjugated \(u\)-spinor mapping and are **not** an independent explicit \(v\)-spinor calculation. The updated status should say that pointwise matrix-element validation passed, while the antimuon \(v\)-spinor cross-check and global transport acceptance remain open.

### 2.3 Moving-muon thermal-integral design — REVISION_REQUIRED

The design document's first invariant collision integral is written as
\[
\Gamma^{\rm prod}_{\mu\gamma,h}
=\frac{1}{2\omega}\sum_{Q=\mu^-,\mu^+}
\int d\Pi_p\,d\Pi_q\,d\Pi_{p'}\,
(2\pi)^4\delta^{(4)}(\cdots)\,
\overline{|\mathcal M_{Q,h}|^2}\,F_{\rm prod}.
\]

Unlike the later derivation, this equation does not display the factor two for the initial-muon spin degeneracy and does not define whether \(\overline{|\mathcal M|^2}\) is averaged over the initial muon spin. Under the convention used by the derivation and both implementations—initial-spin-averaged trace, final-muon spin sum, physical photon-polarization sum—the design equation is missing that factor unless it is supplied implicitly by a different, explicitly stated definition of the matrix element.

Required repair: write either \(2/(2\omega)\) multiplying the initial-spin-averaged trace, or write the fully unaveraged spin sum with no extra degeneracy factor. State the convention once and use it consistently for production and absorption. This is a documentation/normalization-specification defect; the later derivation and current code contain the factor two.

### 2.4 Moving-muon thermal-rate audit — PASS_WITH_NOTES

The 2026-11-12 moving-muon thermal workflow [#43206544350](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544350) completed successfully. Its log confirms 81 tests passed, and it regenerated:
- the profile-B local thermal response scan;
- the 0.1/0.3/1/3 MeV B.13 versus B.14--B.16 comparison;
- the current validation manifest;
- the fixed-energy moving-muon validation and vector polarization audit.

The archived fixed-energy validation for the newer `research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/moving_compton.py` implementation gives a maximum coarse/fine thermal quadrature difference \(2.52\times10^{-4}\), detailed-balance residual \(4.35\times10^{-15}\), and unpolarized Eq. (5.12) residual \(3.11\times10^{-15}\). These are local fixed-\(\omega\) checks, not a full radial transport result.

One notation point remains: the opening rate equations use \(\sum_{\pm,s}\), but do not define \(s\). The later text says that the trace averages the initial muon spin and that a physical spin degeneracy of two is included. Define whether \(s\) denotes the final-muon spin sum or another index; if it denotes an initial-spin sum, the displayed average and the later factor two would double count. The reduced integral and implemented prefactor are consistent, so this is retained as a note rather than evidence of a numerical factor error.

The explicit-spinor boundary from §2 applies here too. The local rate audit does not include the active-neutrino channel, radial optical depth, escape probability, redshifted luminosity, or a validated Fig. 7 curve.

### 2.5 Pure-vector endpoint gate — HISTORICAL

The 2026-11-07 gate is an initial decision record. Its substantive conclusion—do not promote a mixed-current curve before the pure-vector Fig. 7 benchmark passes—remains correct, but its detailed numbers and branch status are superseded by:
- `research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_VECTOR_BENCHMARK_ACCEPTANCE_GATE_2026-11-09.md`;
- `research/stellar-cooling-constraints-20261105/blinov_reproduction/FIG7_VECTOR_BENCHMARK_REEVALUATION_2026-11-09.md`, including its 2026-11-15 review qualification.

The current fixed-\(\omega\), scalar B.2 B.16 benchmark still fails the 10 MeV strong endpoint (the later acceptance gate records \(+92.2406\%\)). The separate path-redshift and global B.13 alternatives are not substitutes for the literal published benchmark. Keep this 2026-11-07 document as a historical snapshot; do not use its old PR #56 Draft status or old endpoint table as the current sign-off.

### 2.6 Vector-to-axial response mapping — REVISION_REQUIRED

The document says the numerical response scan is the next local-kernel task. That is stale. Workflow [#43206544724](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544724) succeeded, ran the 81-test finite-mixing suite, and archived `research/stellar-cooling-constraints-20261105/finite_mixing/outputs/vector_axial_response_scan.json` with 25 differential Compton points, 25 angle-integrated Compton points, 25 finite-mixing points, and 9 dimuon points.

Across the angle-integrated Compton grid:
- transverse \(A/V\) ratios range from 1.2124 to 2.9890;
- longitudinal \(A/V\) ratios range from 1.4200 to \(3.9669\times10^4\);
- the polarization-summed ratio ranges from 1.4188 to 200.5173.

The local response is strongly dependent on mass, \(\omega/m_{A'}\), angle, and polarization. It cannot be represented by one universal factor. The UV active-neutrino couplings remain unchanged as \(\theta_{\mu R}\) varies, so even a constant muon-channel ratio would not justify rescaling the total stellar luminosity.

The dimuon data also need two scopes distinguished. The 9-point `research/stellar-cooling-constraints-20261105/finite_mixing/outputs/vector_axial_response_scan.json` is a fixed-energy local-rate comparison at \(\omega=1.25m_{A'}\); its thermal \(A/V\) ratios differ from the vacuum-width ratio by up to 0.992%. The separate full mediator-momentum thermal integral in `research/stellar-cooling-constraints-20261105/finite_mixing/outputs/thermal_response_scan.json` agrees with the analytic vacuum-width ratio to \(1.11\times10^{-15}\). These are not contradictory: one is a fixed-energy response, the other is the fully integrated emissivity.

Update the mapping document to record the completed local scan, its limited fixed-energy/local scope, the full thermal dimuon result, and the still-open global transport step. Do not infer a luminosity rescaling from these local ratios.

## 3. Cross-implementation audit gap

Two fixed-energy moving-muon implementations are present:
- `research/stellar-cooling-constraints-20261105/finite_mixing/moving_muon_compton.py`, used by the local thermal-response/mass scans and the explicit-spinor audit;
- `research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/moving_compton.py`, with its own matrix-element, covariance, phase-space, and thermal-rate tests.

Both use the same reduced invariant integral and the same spin-degeneracy normalization, but the reviewed tests do not directly compare their numerical \(\Gamma^{\rm prod/abs}_{Q,h}\) values at identical nontrivial \((m_{A'},\omega,T,\mu_\mu,g_V,g_A)\) points. Their separate test success is not a cross-implementation closure test.

Recommended next regression: evaluate both implementations at shared points for \(\mu^-\), \(\mu^+\), pure vector, pure axial, and mixed currents; compare all three modes, production, absorption, shell closure, and convergence under independent quadrature refinement. This should be a focused local-rate comparison, not another broad mass scan.

## 4. Register reconciliation

Before this review: 360 reviewed, 102 pending:
- 244 PASS_WITH_NOTES
- 2 PASS
- 14 REVISION_REQUIRED
- 100 HISTORICAL
- 102 PENDING

After this review: 366 reviewed, 96 pending:
- 246 PASS_WITH_NOTES
- 2 PASS
- 17 REVISION_REQUIRED
- 101 HISTORICAL
- 96 PENDING

## 5. Required next work

1. Make the initial-muon spin degeneracy convention explicit in the thermal-integral design and rate-audit equations; preserve the verified factor-two implementation.
2. Update the B.13 derivation status with the explicit-spinor result and the direct-\(v\)-spinor limitation for \(\mu^+\).
3. Update the vector-to-axial mapping document with the completed local scan, fixed-energy versus full thermal dimuon distinction, and the continuing no-universal-rescale result.
4. Add a paired numerical regression between the two moving-muon fixed-energy implementations.
5. Keep the pure-vector Fig. 7 gate blocked; do not rescale source, opacity, coupling, profile, luminosity, or any axial-vector constraint.

**Scientific disposition:** the moving-muon B.13 local matrix element and local thermal-rate machinery have substantial independent checks, but they are not a global transport acceptance. The pure-vector Fig. 7 benchmark remains unpassed, and no axial-vector cooling curve is promoted.

## 6. Post-review current-tree reconciliation (2026-11-16)

The reviewed-base snapshot classified three documents as `REVISION_REQUIRED`. A current-tree recheck confirms that all three repairs have since landed, with their updated contents and dispositions reflected in the baseline audit register:

- `MOVING_MUON_SEMI_COMPTON_DERIVATION_2026-11-07.md`: header now states pointwise `mu-` spinor/trace and local implementation validation passed under workflow #43534265182 (38 targeted tests), while explicitly retaining the independent `mu+` (v)-spinor and global-transport limitations. The explicit-spinor JSON is blob `bf0e4ea17fa0aa6af69146be1520481229780ad8`; maximum trace/spinor residual is (1.77\times10^{-13}).
- `MOVING_MUON_THERMAL_INTEGRAL_DESIGN_2026-11-07.md`: status now records the initial-muon spin degeneracy factor two and defines the matrix-element convention as initial-spin average, final-spin sum and two physical photon-polarization sum. The same convention is applied to absorption. This resolves the omitted-factor ambiguity in the design equation.
- `VECTOR_TO_AXIAL_RESPONSE_MAPPING_2026-11-07.md`: status now records workflow #43206544724 and the local response scan (25 differential Compton, 25 angle-integrated Compton, 25 finite-mixing and 9 dimuon points). It distinguishes fixed-energy dimuon response from the full thermal dimuon integral and retains the no-universal-rescaling conclusion.

The profile-B low-mass rerun JSON (blob `1ff3273ef498567d32edb5cfcd2996cbe9124039`) was compared point-by-point with the profile-A JSON (blob `998cbf994c1aae92d93c72f5fdeb1282a7b10a41`) at all eight new mass/radius points. The maxima reproduce the report: (1.0385\times10^{-9}) for (Q_{\rm B13}), (1.0881\times10^{-9}) for (Q_{\rm B16}), and (2.3861\times10^{-11}) absolute change in the B.13/B.16 ratio. Workflow #43206544350 succeeded; workflow #43206544724 succeeded; workflow #43534265182 succeeded. The original profile-A scan remains a historical snapshot, not the current reference.

Thus the three former revision findings are resolved at the document level and are now `PASS_WITH_NOTES` in the baseline register. The direct `mu+` (v)-spinor proof, cross-implementation pointwise regression, and global transport acceptance remain open. The pure-vector Fig. 7 gate and all cooling constraints remain unchanged.
