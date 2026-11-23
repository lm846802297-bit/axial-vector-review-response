# Croon A0: original-UV finite-mixing axial-vector transport

Date: 2026-11-20  
Status: **10 MeV A0 153-node / 32-to-48 energy-order convergence passed as an Actions-based independent verification. No local primary run is archived. Reduced-grid six-mass pilots are diagnostic only; the full six-mass transport scan remains pending.**

## 1. Purpose and separation from C1

C1 is the pure-vector benchmark used to establish the radial transport implementation against the Croon comparison. A0 changes only the charged-muon current to the original model's finite-mixing vector--axial current. The active-neutrino current and its B.7 production/absorption rates remain unchanged.

The A0 calculation uses the same reviewed reconstructed SFHo-18.8 profile, energy map, radial integration, coupling grid, polarization order, and outer-radius convention as C1. It is a separate physical current, not a rescaling of the C1 luminosity.

## 2. Original UV coupling map

The charged-muon interaction convention is

$$
\mathcal L_{\mu A'}=
A'_\alpha\bar\mu\gamma^\alpha
(g_V^\mu+g_A^\mu\gamma^5)\mu .
$$

The mass-basis couplings are

$$
g_V^\mu=g_X\sin^2\theta_{\mu R},
\qquad
g_A^\mu=-g_X\cos^2\theta_{\mu R},
$$

with

$$
g_L^\mu=g_V^\mu-g_A^\mu=g_X,
\qquad
g_R^\mu=g_V^\mu+g_A^\mu=-g_X\cos(2\theta_{\mu R}).
$$

The benchmark uses $\theta_{\mu R}=10^{-2}$, giving

$$
\frac{g_V^\mu}{g_X}=9.9996666711\times10^{-5},
\qquad
\frac{g_A^\mu}{g_X}=-0.999900003333.
$$

The moving-muon kernel accepts the coefficients in the
$\gamma^\alpha(g_V+g_A\gamma^5)$ convention. The sign of $g_A^\mu$
is therefore passed directly; it is not replaced by its absolute value.

The active-neutrino couplings remain

$$
g_{\nu_\mu}=+g_X,\qquad g_{\nu_\tau}=-g_X,
$$

independent of $\theta_{\mu R}$.

## 3. Goldstone and longitudinal-current relation

For the original single-VEV realization,

$$
m_{A'}=2g_Xv_s.
$$

The axial-current Ward identity fixes the diagonal Goldstone coupling to

$$
g_{G\mu\mu}
=\frac{2|g_A^\mu|m_\mu}{m_{A'}}
=\cos^2\theta_{\mu R}\frac{m_\mu}{v_s}.
$$

The A0 collision kernel uses the physical longitudinal $A'$ polarization
for the axial part. The Goldstone-equivalence contribution is already
represented by that physical longitudinal mode; no separate
Goldstone-emission rate is added.

## 4. B.13 mixed-current kernel

The implementation reuses the module
research/stellar-cooling-constraints-20261105/finite_mixing/moving_muon_compton.py
and evaluates

$$
A'(q)+\mu^\pm(P)\leftrightarrow
\gamma(K)+\mu^\pm(P')
$$

with:

- exact two-body recoil and the final-muon on-shell condition;
- both $\mu^-$ and $\mu^+$ distributions, with chemical potentials
  $+\mu_\mu$ and $-\mu_\mu$;
- Fermi blocking and photon Bose enhancement;
- amplitude-level vector--axial interference;
- medium-rest-frame $L,+,-$ polarization resolution;
- the physical longitudinal polarization for the axial amplitude and the
  Ward-equivalent shifted polarization for the conserved vector amplitude;
- separate production and absorption rates.

Charge conjugation reverses the relative axial contribution for the
$\mu^+$ target before the two charge-resolved rates are summed.

The local detailed-balance identity is checked separately for each charge
and mode:

$$
\Gamma^{\rm prod}_{h,\mu^\pm}
=e^{-\omega/T}\Gamma^{\rm abs}_{h,\mu^\pm}.
$$

## 5. Radial transport

The B.7 neutrino rates are kept exactly as in C1. The B.13 rates use the
A0 current coefficients normalized to $g_X$. Thus all local kernels are
coefficients multiplying the common overall $g_X^2$.

For each physical mode,

$$
\Gamma_{{\rm red},h}
=\Gamma_{{\rm abs},h}-\Gamma_{{\rm prod},h}
=(1-e^{-\omega/T})\Gamma_{{\rm abs},h},
$$

and

$$
\tau_h(\omega,r)
=\int_r^{R_\nu}dr'\,
\Gamma_{{\rm red},h}(\omega,r').
$$

The escaped luminosity is evaluated with the C1 radial prescription,

$$
L_{A'}(g_X)=g_X^2
\sum_{h=L,+,-}
\int d\omega\int_0^{R_\nu}4\pi r^2dr\,
\frac{d\dot n_h}{d\omega}
e^{-g_X^2\tau_h(\omega,r)}.
$$

Two outer-radius conventions are retained: $R_{\rm far}=R_\nu$ and
$R_{\rm far}=100$ km. The latter includes the unchanged two-flavour B.7
vacuum-decay tail. The outer 25--100 km B.13 semi-Compton opacity remains
omitted because the validated outer muon-susceptibility profile is not
available.

The Croon Eq. (4.7) single-$\mu^-$, pure-vector expression is retained
only as a diagnostic comparator. It is not inserted into the A0 source or
opacity.

## 6. Existing local thermal benchmark

The archived thermal_response_scan.json gives an independent local thermal
check at $m_{A'}=10$ MeV.

At the center ($r=0$ km), the B.13 emissivities are:

| Mode | Pure axial $Q_A$ (MeV$^5$) | UV mixed $Q_{\rm UV}$ (MeV$^5$) |
|---|---:|---:|
| L | 441.3345102 | 441.2462507 |
| + | 16.0646616 | 16.0620780 |
| - | 16.0646616 | 16.0608200 |
| Total | 473.4638334 | 473.3691486 |

Therefore,

$$
\frac{Q_{\rm UV}}{Q_A}=0.99980001696.
$$

The mixed-current interference fractions in the two circular modes are
approximately $+3.916\times10^{-5}$ and $-3.916\times10^{-5}$; the
longitudinal interference is numerically negligible at this benchmark.
At $r=12.5$ km the total mixed-to-pure-axial ratio is $0.99980001690$.

These are local B.13 thermal emissivities. They are not radial
luminosities, optical depths, or SN1987A limits.

## 7. Adaptive radial integration correction

The first A0 output (workflow run 44588722728) was generated before the C1 surface-centered adaptive radial method was integrated into the A0 driver. Inspection of the archived JSON and source showed that this output contained only the legacy fixed-grid Simpson luminosities. It is retained as a historical diagnostic and is not an accepted strong-coupling A0 transport result.

The A0 driver now passes the original finite-mixing current
$$
(g_V^\mu/g_X,\ g_A^\mu/g_X)
=(\sin^2\theta_{\mu R},-\cos^2\theta_{\mu R})
$$
directly into the shared transport kernel with include_adaptive_radial=True. The adaptive method interpolates the A0 mode-resolved source and reduced opacity separately and computes the optical-depth boundary layer with the same surface-centered PCHIP/QUADPACK procedure accepted for C1. The legacy Simpson fields remain in the output only to make the endpoint artifact visible.

The adaptive A0 acceptance checks include finite nonnegative luminosities, three-mode closure, QUADPACK error estimates below $10^{-6}$, and agreement of the high-coupling result with the A0-specific surface asymptote. C1's numerical convergence does not substitute for A0's own radial and energy refinement.

## 8. First adaptive 10 MeV A0 result

Workflow [#44656918116](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44656918116) completed successfully. The output uses 103 actual radial nodes, energy order 32, 121 $g_X$ points, and all three physical polarizations. The adaptive-radial fields are present and the legacy Simpson fields are retained only for diagnostics.

The accepted local source coefficients per $g_X^2$ are:

| Channel | Thin source $({\rm erg/s})/g_X^2$ |
|---|---:|
| B.7, $\nu_\mu+\nu_\tau$ | $4.45124477\times10^{70}$ |
| B.13, $\mu^-$ | $4.25564242\times10^{71}$ |
| B.13, $\mu^+$ | $2.92955313\times10^{69}$ |
| B.13, $\mu^-+\mu^+$ | $4.28493795\times10^{71}$ |
| B.7 + B.13 | $4.73006243\times10^{71}$ |

On the same 103-node, energy-32 grid, the optically thin A0 source is 9.12381 times the C1 pure-vector source. Within A0, B.13 contributes 90.5895% of the total thin source, with B.13/B.7 = 9.62638. The mu-plus target contributes 0.68369% of the B.13 source; it is included explicitly rather than absorbed into an effective susceptibility.

The mode decomposition shows why the axial calculation cannot be obtained by rescaling the vector luminosity:

| B.13 source | Longitudinal L fraction | Transverse + fraction | Transverse - fraction |
|---|---:|---:|---:|
| A0 original-UV V-A current | 96.4692% | 1.76552% | 1.76531% |
| C1 pure-vector current | 1.61501% | 49.1925% | 49.1925% |

At fixed g_X, the A0/C1 B.13 thin-source ratios are 3491.53 in L, 2.09786 in +, and 2.09762 in -; the total B.13 ratio is 58.4525. This large longitudinal enhancement is the finite-temperature transport signature of the nonconserved axial current and its physical longitudinal-vector/Goldstone-equivalence contribution. It requires mode-resolved production and absorption in A0.

The B.7 source agrees with the accepted C1 same-grid source in the total and each polarization. The detailed-balance and shell checks are:

$$
\begin{aligned}
\epsilon_{\rm DB}^{B.7}&=3.31\times10^{-14},\\
\epsilon_{\rm DB}^{B.13}&=5.91\times10^{-14},\\
\epsilon_{\rm shell}^{\mu'}&=5.38\times10^{-13}.
\end{aligned}
$$

The maximum adaptive QUADPACK relative-error estimate is $3.69\times10^{-8}$. At $g_X=1$, the adaptive luminosity is
$$
L_{A0}(R_\nu)=1.4380831321\times10^{52}\ {\rm erg/s},
$$
with each mode agreeing with its A0 surface asymptote to better than $6\times10^{-16}$.

This is an interior-profile A0 result. The outer 25--100 km semi-Compton opacity is still omitted, and the 103/153-node A0 radial convergence check has not yet been completed. It is not an SN1987A exclusion curve.

## 8.1 Preliminary adaptive 103-node comparison with C1

The accepted A0 103-node output contains both the legacy Simpson columns and the independent adaptive PCHIP/QUADPACK columns. The following comparison uses only the adaptive columns, with the same 10 MeV mass, 103 radial nodes, energy order 32, 121-point $g_X$ grid, and three physical polarizations in A0 and C1.

| $g_X$ (nearest scan point) | $L_{\rm A0}/L_{\rm C1}$, $R_{\rm far}=R_\nu$ |
|---:|---:|
| $1.00\times10^{-11}$ | 9.1273 |
| $1.04\times10^{-9}$ | 9.0624 |
| $1.06\times10^{-8}$ | 4.7821 |
| $1.08\times10^{-7}$ | 0.8630 |
| $1.10\times10^{-6}$ | 1.0000 |
| $9.09\times10^{-6}$ | 1.0000 |
| $9.26\times10^{-5}$ | 1.0000 |
| $9.44\times10^{-4}$ | 1.0000 |
| $9.62\times10^{-3}$ | 1.0000 |
| $9.81\times10^{-2}$ | 1.0000 |
| $1$ | 1.0000 |

At low coupling, the UV axial charged-muon current increases the interior-profile escaped luminosity relative to the pure-vector C1 reference. At larger coupling the two curves approach the same surface-limited value. This is expected from the surface detailed-balance limit: once the escape layer is confined to the neutrinosphere boundary, the limiting luminosity depends on the common local Bose factor rather than the interior source normalization.

A full 121-point comparison of the 103-node adaptive curves gives
$$
\max_{g_X}\frac{L_{\rm A0}}{L_{\rm C1}}=9.12732
\quad(g_X=10^{-11}),
\qquad
\min_{g_X}\frac{L_{\rm A0}}{L_{\rm C1}}=0.739287
\quad(g_X=8.7431\times10^{-8}).
$$
The first crossing below unity occurs between
$g_X=3.0432\times10^{-8}$ and
$3.7584\times10^{-8}$. The longitudinal ratio is the dominant source of the low-coupling enhancement; the two transverse ratios remain near 1.2 at the weakest coupling. These are 103-node diagnostics and will be recomputed from the accepted 153-node A0 result.

This comparison is a diagnostic from the 103-node baseline. The independent 153-node A0 refinement is required before quoting the radial uncertainty of the A0/C1 ratio. The outer 25--100 km semi-Compton opacity remains omitted; these values are not SN1987A limits.

## 8.2 Accepted 153-node A0/C1 comparison

The independent A0 153-node, energy-32 refinement has now passed. On the same 153-node/energy-32 grid, the thin-source ratios are:

| Channel | A0/C1 source ratio |
|---|---:|
| B.7, nu_mu + nu_tau | 1.00000 |
| B.13, mu-minus | 58.4603 |
| B.13, mu-plus | 58.1062 |
| B.13, both charges | 58.4578 |
| B.7 + B.13 total | 9.12764 |

The B.13 mode ratios are 3492.32 in L, 2.09779 in +, and 2.09754 in -. The B.7 source agrees exactly with C1 in the total and all three modes. Thus the large A0 enhancement is localized in the charged-muon B.13 current, particularly its longitudinal mode; it is not a neutrino normalization change.

For the neutrinosphere boundary R_far=R_nu, the 121-point escaped-luminosity ratio has maximum 9.12551 at g_X=10^-11 and minimum 0.739221 at g_X=8.7431e-8. It returns to unity in the surface-limited high-coupling regime. The first crossing below unity lies between g_X=3.0432e-8 and 3.7584e-8. These values are based on the accepted 153-node A0 result and the matching C1 153-node/energy-32 output.

The A0 radial-grid acceptance report gives a maximum normalized change metric of 0.00402177 against a 0.01 target. The largest relevant pointwise curve difference is 0.40218% (longitudinal mode, R_far=100 km); the total-luminosity differences are 0.09852% for R_far=R_nu and 0.11666% for R_far=100 km. Thin-source changes from 103 to 153 nodes are 0.06177% for B.13 (both charges), 0.00850% for B.7, and 0.05676% for B.7+B.13.

The numerical checks also pass: maximum QUADPACK relative-error estimate 3.5721e-7; three-mode closure 2.19e-16; B.7 detailed-balance residual 3.46e-14; B.13 charge/mode detailed-balance residual 5.78e-14; final-muon shell residual 5.38e-13; and high-coupling surface-asymptote residual below 5.6e-16. The native JSON, CSV, convergence report, and SHA-256 manifest are committed in the PR branch.

## 9. Current execution and acceptance

A0 implementation and tests are committed to the PR #123 research branch.

- A0 workflow: [run 44582338538](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44582338538)
- C1 10 MeV grid convergence: [run 44577096997](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44577096997)

The A0 mapping/kernel tests and the existing C1 regression tests are rerun
before the adaptive 10 MeV transport calculation. The accepted 103-node adaptive baseline is
[workflow #44656918116](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44656918116).

The A0 baseline acceptance requires:

1. native JSON and radial CSV with 103 actual radial nodes, 32 energy
   nodes, 121 $g_X$ points, and adaptive-radial fields enabled;
2. B.7 detailed balance, B.13 charge-mode detailed balance, and
   final-muon shell closure;
3. three-polarization source and luminosity closure;
4. exact agreement of the B.7 thin-source total and each mode with the
   same-grid accepted C1 result;
5. finite, nonnegative source and luminosity data;
6. QUADPACK error estimates below $10^{-6}$ and high-coupling convergence to the A0 surface asymptote;
7. native-output SHA-256 manifest, artifact upload, and rebased Git archival.

The A0 10 MeV 103/153 radial comparison and 32/48 energy-order comparison have now passed as Actions-based independent verification. The 153-node radial audit script is committed as audit_croon_a0_10mev_adaptive_radial_convergence.py. This does not replace a local primary calculation record.
C1 grid convergence does not automatically establish A0 convergence because the axial longitudinal source and opacity have different kinematic weights.

The A0 10 MeV numerical verification is complete, but the full six-mass transport scan remains pending. No A0 exclusion curve is produced by this diagnostic stage.

## 9.1 Independent explicit-spinor and Ward audit

The separate B.13 explicit-spinor audit covers five kinematic points and six current/charge cases (vector, axial, and mixed currents for both mu-minus and mu-plus). Its archived results are:

| Audit quantity | Maximum residual |
|---|---:|
| Explicit-spinor sum vs Dirac trace | 1.77e-13 |
| Photon Ward amplitude | 1.47e-13 |
| Vector longitudinal Ward shift | 3.54e-14 |
| Final-muon mass shell | 6.52e-16 |

All mode matrix elements are nonnegative. This is an amplitude-level independent validation; it does not replace the A0 thermal phase-space, radial, or energy convergence checks.

Source: finite_mixing/thermal_integrals/outputs/b13_moving_muon_explicit_spinor_audit_2026-11-13.json.

## 10. Independent A0 radial and energy convergence

The first A0 153-node radial attempt, [workflow #44661771748](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44661771748), completed the numerical integration but failed its post-processing validator because the independently generated 121-point coupling grids were compared bit-for-bit. The grids are numerically identical to floating-point precision; the validator was corrected to require a maximum relative difference below 1e-13.

The corrected 153-node radial refinement passed in [workflow #44671688630](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44671688630). Its native JSON, CSV, convergence report, and SHA-256 manifest are committed to the research branch. The accepted numerical results and tolerances are recorded in Sec. 8.2 above.

The A0 energy-order audit is implemented in audit_croon_a0_10mev_adaptive_energy_convergence.py. Its first attempt, [workflow #44671693423](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44671693423), stopped at the input gate because the A0 153-node reference had not yet been committed; no energy-order-48 computation was performed. The gate was changed to defer cleanly rather than mark a not-yet-runnable calculation as a failure. The deferral checks [#44672658393](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44672658393) and [#44673027259](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44673027259) completed successfully with the numerical stage skipped.

The energy-audit coupling-grid validator was changed from bitwise equality to a 1e-13 maximum relative tolerance. The workflow records SHA-256 fingerprints of the A0 153-node/energy-32 and C1 153-node/energy-48 reference outputs. The A0 48-order computation completed successfully in [workflow #44673753335](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44673753335). The archived comparison reports a maximum over all energy-order metrics of $8.160358994668485\times10^{-8}$ against a $10^{-4}$ target; the maximum QUADPACK estimate is $4.890950852625319\times10^{-8}$, the maximum three-mode closure residual is $1.9232393730565026\times10^{-16}$, and the B.7 source agrees with C1 on the identical 153-node / energy-48 grid to $1.3770218205966729\times10^{-16}$. B.7 detailed balance, B.13 charge/mode detailed balance and final-muon shell residuals are $3.295430550940328\times10^{-14}$, $6.876085485811427\times10^{-14}$ and $5.380211888635872\times10^{-13}$, respectively. These are Actions-based independent-verification results; no local primary run record is archived.

A minimal source/profile/reference bundle was exported in [workflow #44674462571](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44674462571). This is a packaging run, not a local numerical result. The repository currently contains no independently recorded local primary A0 10 MeV run manifest; the Actions result above is retained only as an independent verification.

The energy comparison holds fixed the 153-node radial grid, 121-point
$g_X$ grid, $\theta_{\mu R}=10^{-2}$, neutrino angular order 128,
susceptibility order 192, and inner quadrature orders $(12,8,8,8)$.
Only the energy order changes from 32 to 48. The audit compares:

1. both $R_{\rm far}=R_\nu$ and $R_{\rm far}=100$ km luminosity curves;
2. total luminosity and each $L,+,-$ polarization separately;
3. B.7 and B.13 thin-source channel integrals and their mode decomposition;
4. the A0 surface asymptotes and high-coupling residuals;
5. the B.7 source against C1 on the identical 153-node/energy-48 grid;
6. QUADPACK estimates, three-mode closure, detailed balance, and final-muon
   on-shell closure.

The numerical acceptance target is a maximum reported normalized/physical
relative change below $10^{-4}$, with QUADPACK relative-error estimates
below $10^{-6}$, three-mode closure below $10^{-12}$, B.7 cross-check
below $10^{-12}$, and the existing detailed-balance/on-shell tolerances.
The generated JSON, CSV, report, and SHA-256 manifest are committed only
after these checks pass.

The A0 energy audit is a distinct calculation. C1's energy convergence does
not establish A0 energy convergence because the axial current changes the
longitudinal production and absorption kernels.

## 11. Goldstone-Yukawa perturbativity mask for the six-mass scan

Before accepting the A0 six-mass scan, the UV longitudinal sector needs a coupling-domain mask. The finite-mixing model gives
$$
g_A^\mu=-g_X\cos^2\theta_{\mu R},\qquad m_{A'}=2g_Xv_s,
$$
and the Goldstone-equivalence relation is
$$
y_{G\mu\mu}=\frac{2|g_A^\mu|m_\mu}{m_{A'}}
=\frac{2g_X\cos^2\theta_{\mu R}m_\mu}{m_{A'}}
=\frac{\cos^2\theta_{\mu R}m_\mu}{v_s}.
$$

Using the conservative Yukawa perturbativity criterion
$$
\alpha_G\equiv\frac{y_{G\mu\mu}^2}{4\pi}\leq1,
$$
the maximum perturbative gauge coupling at fixed mediator mass is
$$
\boxed{g_X^{\rm pert}(m_{A'})=
\frac{\sqrt{4\pi}\,m_{A'}}{2m_\mu\cos^2\theta_{\mu R}}.}
$$
This is a theory-validity mask, not an additional supernova exclusion. The full transport curve can be retained for numerical diagnostics, while the physically interpreted A0 parameter region is restricted to the points below this line.

For the existing 121-point scan, $g_X\in[10^{-11},1]$, and $\theta_{\mu R}=10^{-2}$, the local calculation gives:

| $m_{A'}$ | $g_X^{\rm pert}$ | Perturbative scan points |
|---:|---:|---:|
| 0.1 eV | $1.6777\times10^{-9}$ | 25/121 |
| 1 eV | $1.6777\times10^{-8}$ | 36/121 |
| 10 eV | $1.6777\times10^{-7}$ | 47/121 |
| 0.1 MeV | $1.6777\times10^{-3}$ | 90/121 |
| 10 MeV | $1.6777\times10^{-1}$ | 112/121 |
| 200 MeV | 3.3554 | 121/121 |

At 10 MeV, for example, the endpoint $g_X=1$ gives $y_{G\mu\mu}=21.13$ and $\alpha_G=35.53$, outside this conservative perturbative criterion. The accepted 10 MeV radial-convergence result remains a valid numerical transport diagnostic; its nonperturbative high-$g_X$ points must not be used as perturbative model bounds. At 200 MeV the entire scanned interval satisfies the criterion.

The reproducible calculation is in audit_a0_goldstone_perturbativity.py, with its JSON and CSV outputs in outputs/A0_GOLDSTONE_PERTURBATIVITY_WINDOW_2026-11-20.{json,csv}. This mask will be carried into the six-mass scan and its final plots.


## 11. Low-mass longitudinal stability: explicit spinor and physical-photon sum

The six-mass preparation exposed a numerical failure that is absent at the 10 MeV benchmark. For
$$
m_{A'}=10^{-7}\ \mathrm{MeV},\qquad
\omega=5.3329616310\times10^{-4}\ \mathrm{MeV},
$$
at the central reconstructed-profile point, the former covariant photon sum using
$-g_{\mu\nu}$ returned a negative longitudinal matrix element,
$$
|\mathcal M_L|^2=-4.670\times10^3,
$$
while the physical rate must be nonnegative. The failure occurs because
$\epsilon_L^\mu\simeq q^\mu/m_{A'}$ and the covariant photon sum subtracts large unphysical components. This is a numerical cancellation in the trace representation, not a negative physical rate.

The production kernel now evaluates the positive sum directly:
$$
\overline{|\mathcal M_h|^2}
=\frac{e^2}{2}
\sum_{s_i,s_f}\sum_{\lambda_\gamma=1}^{2}
\left|
\bar u_{s_f}(p_f)\,
\mathcal A_{h,\lambda_\gamma}\,
u_{s_i}(p_i)
\right|^2,
$$
using two orthonormal physical photon polarizations. The covariant $-g_{\mu\nu}$ trace is retained as a separate moderate-mass diagnostic, not used for the low-mass production rates.

### 11.1 Independent checks

- The vectorized explicit-spinor point kernel agrees with the independently written explicit-spinor reference for all six vector, axial, mixed-current and charge cases at the 0.1 eV benchmark point. The largest relative residual is $4.62\times10^{-9}$; the photon-Ward residuals are below $10^{-8}$.
- The complete low-mass thermal kernel gives finite, strictly positive production and absorption in all three modes and both muon-charge sectors. Its mode/charge detailed-balance residual is below $5\times10^{-14}$.
- The 10 MeV A0 calculation was repeated with the explicit-spinor implementation in [workflow #44681748661](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44681748661). Relative to the former covariant-trace baseline on the identical 103-node/energy-32 grid, the B.13 thin-source totals and mode components change by at most $4.45\times10^{-16}$; the adaptive $R_{\rm far}=R_\nu$ luminosity curve changes by at most $4.26\times10^{-16}$, and the 100 km curve by at most $6.18\times10^{-15}$. The unchanged B.7 source is identical.

The low-mass pilot completed for all six benchmark masses with reduced diagnostic grids. These pilot values establish that the explicit-spinor kernel is numerically operational across the mass range; they are not accepted full transport results. The 10 MeV 153-node / 32-to-48 energy-order independent verification is complete, and the Goldstone perturbativity mask has been computed. The full six-mass transport scan remains pending.

### 11.2 Regression coverage

The new regression coverage includes:

1. explicit-spinor comparison at 0.1 eV for all six current/charge cases;
2. positivity of the longitudinal and transverse matrix elements;
3. photon-Ward identity and final-muon mass-shell closure;
4. ultralight thermal production/absorption detailed balance;
5. stationary-muon vector and axial endpoint recovery;
6. unchanged A0 and C1 mapping/transport regressions.

The local finite-mixing test run passed all A0-relevant and moving-muon tests. The full package discovery also encountered one unrelated test import requiring the separate literature reference module; that test is outside this A0 bundle's source scope. The dedicated GitHub workflow [#44682747697](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44682747697) runs the targeted regression set independently.
