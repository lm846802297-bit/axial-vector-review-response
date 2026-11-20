# Croon A0: original-UV finite-mixing axial-vector transport

Date: 2026-11-20  
Status: **10 MeV A0 adaptive-radial baseline passed on 103 nodes; independent 153-node radial refinement is running after a validator-schema correction.**

## 1. Purpose and separation from C1

C1 is the pure-vector benchmark used to establish the radial transport implementation against the Croon comparison. A0 changes only the charged-muon current to the original model's finite-mixing vector--axial current. The active-neutrino current and its B.7 production/absorption rates remain unchanged.

The A0 calculation uses the same reviewed reconstructed SFHo-18.8 profile, energy map, radial integration, coupling grid, polarization order, and outer-radius convention as C1. It is a separate physical current, not a rescaling of the C1 luminosity.

## 2. Original UV coupling map

The charged-muon interaction convention is

\[
\mathcal L_{\mu A'}=
A'_\alpha\bar\mu\gamma^\alpha
(g_V^\mu+g_A^\mu\gamma^5)\mu .
\]

The mass-basis couplings are

\[
g_V^\mu=g_X\sin^2\theta_{\mu R},
\qquad
g_A^\mu=-g_X\cos^2\theta_{\mu R},
\]

with

\[
g_L^\mu=g_V^\mu-g_A^\mu=g_X,
\qquad
g_R^\mu=g_V^\mu+g_A^\mu=-g_X\cos(2\theta_{\mu R}).
\]

The benchmark uses \(\theta_{\mu R}=10^{-2}\), giving

\[
\frac{g_V^\mu}{g_X}=9.9996666711\times10^{-5},
\qquad
\frac{g_A^\mu}{g_X}=-0.999900003333.
\]

The moving-muon kernel accepts the coefficients in the
\(\gamma^\alpha(g_V+g_A\gamma^5)\) convention. The sign of \(g_A^\mu\)
is therefore passed directly; it is not replaced by its absolute value.

The active-neutrino couplings remain

\[
g_{\nu_\mu}=+g_X,\qquad g_{\nu_\tau}=-g_X,
\]

independent of \(\theta_{\mu R}\).

## 3. Goldstone and longitudinal-current relation

For the original single-VEV realization,

\[
m_{A'}=2g_Xv_s.
\]

The axial-current Ward identity fixes the diagonal Goldstone coupling to

\[
g_{G\mu\mu}
=\frac{2|g_A^\mu|m_\mu}{m_{A'}}
=\cos^2\theta_{\mu R}\frac{m_\mu}{v_s}.
\]

The A0 collision kernel uses the physical longitudinal \(A'\) polarization
for the axial part. The Goldstone-equivalence contribution is already
represented by that physical longitudinal mode; no separate
Goldstone-emission rate is added.

## 4. B.13 mixed-current kernel

The implementation reuses the module
research/stellar-cooling-constraints-20261105/finite_mixing/moving_muon_compton.py
and evaluates

\[
A'(q)+\mu^\pm(P)\leftrightarrow
\gamma(K)+\mu^\pm(P')
\]

with:

- exact two-body recoil and the final-muon on-shell condition;
- both \(\mu^-\) and \(\mu^+\) distributions, with chemical potentials
  \(+\mu_\mu\) and \(-\mu_\mu\);
- Fermi blocking and photon Bose enhancement;
- amplitude-level vector--axial interference;
- medium-rest-frame \(L,+,-\) polarization resolution;
- the physical longitudinal polarization for the axial amplitude and the
  Ward-equivalent shifted polarization for the conserved vector amplitude;
- separate production and absorption rates.

Charge conjugation reverses the relative axial contribution for the
\(\mu^+\) target before the two charge-resolved rates are summed.

The local detailed-balance identity is checked separately for each charge
and mode:

\[
\Gamma^{\rm prod}_{h,\mu^\pm}
=e^{-\omega/T}\Gamma^{\rm abs}_{h,\mu^\pm}.
\]

## 5. Radial transport

The B.7 neutrino rates are kept exactly as in C1. The B.13 rates use the
A0 current coefficients normalized to \(g_X\). Thus all local kernels are
coefficients multiplying the common overall \(g_X^2\).

For each physical mode,

\[
\Gamma_{{\rm red},h}
=\Gamma_{{\rm abs},h}-\Gamma_{{\rm prod},h}
=(1-e^{-\omega/T})\Gamma_{{\rm abs},h},
\]

and

\[
\tau_h(\omega,r)
=\int_r^{R_\nu}dr'\,
\Gamma_{{\rm red},h}(\omega,r').
\]

The escaped luminosity is evaluated with the C1 radial prescription,

\[
L_{A'}(g_X)=g_X^2
\sum_{h=L,+,-}
\int d\omega\int_0^{R_\nu}4\pi r^2dr\,
\frac{d\dot n_h}{d\omega}
e^{-g_X^2\tau_h(\omega,r)}.
\]

Two outer-radius conventions are retained: \(R_{\rm far}=R_\nu\) and
\(R_{\rm far}=100\) km. The latter includes the unchanged two-flavour B.7
vacuum-decay tail. The outer 25--100 km B.13 semi-Compton opacity remains
omitted because the validated outer muon-susceptibility profile is not
available.

The Croon Eq. (4.7) single-\(\mu^-\), pure-vector expression is retained
only as a diagnostic comparator. It is not inserted into the A0 source or
opacity.

## 6. Existing local thermal benchmark

The archived thermal_response_scan.json gives an independent local thermal
check at \(m_{A'}=10\) MeV.

At the center (\(r=0\) km), the B.13 emissivities are:

| Mode | Pure axial \(Q_A\) (MeV\(^5\)) | UV mixed \(Q_{\rm UV}\) (MeV\(^5\)) |
|---|---:|---:|
| L | 441.3345102 | 441.2462507 |
| + | 16.0646616 | 16.0620780 |
| - | 16.0646616 | 16.0608200 |
| Total | 473.4638334 | 473.3691486 |

Therefore,

\[
\frac{Q_{\rm UV}}{Q_A}=0.99980001696.
\]

The mixed-current interference fractions in the two circular modes are
approximately \(+3.916\times10^{-5}\) and \(-3.916\times10^{-5}\); the
longitudinal interference is numerically negligible at this benchmark.
At \(r=12.5\) km the total mixed-to-pure-axial ratio is \(0.99980001690\).

These are local B.13 thermal emissivities. They are not radial
luminosities, optical depths, or SN1987A limits.

## 7. Adaptive radial integration correction

The first A0 output (workflow run 44588722728) was generated before the C1 surface-centered adaptive radial method was integrated into the A0 driver. Inspection of the archived JSON and source showed that this output contained only the legacy fixed-grid Simpson luminosities. It is retained as a historical diagnostic and is not an accepted strong-coupling A0 transport result.

The A0 driver now passes the original finite-mixing current
\[
(g_V^\mu/g_X,\ g_A^\mu/g_X)
=(\sin^2\theta_{\mu R},-\cos^2\theta_{\mu R})
\]
directly into the shared transport kernel with include_adaptive_radial=True. The adaptive method interpolates the A0 mode-resolved source and reduced opacity separately and computes the optical-depth boundary layer with the same surface-centered PCHIP/QUADPACK procedure accepted for C1. The legacy Simpson fields remain in the output only to make the endpoint artifact visible.

The adaptive A0 acceptance checks include finite nonnegative luminosities, three-mode closure, QUADPACK error estimates below \(10^{-6}\), and agreement of the high-coupling result with the A0-specific surface asymptote. C1's numerical convergence does not substitute for A0's own radial and energy refinement.

## 8. First adaptive 10 MeV A0 result

Workflow [#44656918116](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44656918116) completed successfully. The output uses 103 actual radial nodes, energy order 32, 121 \(g_X\) points, and all three physical polarizations. The adaptive-radial fields are present and the legacy Simpson fields are retained only for diagnostics.

The accepted local source coefficients per \(g_X^2\) are:

| Channel | Thin source \(({\rm erg/s})/g_X^2\) |
|---|---:|
| B.7, \(\nu_\mu+\nu_\tau\) | \(4.45124477\times10^{70}\) |
| B.13, \(\mu^-\) | \(4.25564242\times10^{71}\) |
| B.13, \(\mu^+\) | \(2.92955313\times10^{69}\) |
| B.13, \(\mu^-+\mu^+\) | \(4.28493795\times10^{71}\) |
| B.7 + B.13 | \(4.73006243\times10^{71}\) |

On the same 103-node, energy-32 grid, the optically thin A0 source is 9.12381 times the C1 pure-vector source. Within A0, B.13 contributes 90.5895% of the total thin source, with B.13/B.7 = 9.62638. The mu-plus target contributes 0.68369% of the B.13 source; it is included explicitly rather than absorbed into an effective susceptibility.

The mode decomposition shows why the axial calculation cannot be obtained by rescaling the vector luminosity:

| B.13 source | Longitudinal L fraction | Transverse + fraction | Transverse - fraction |
|---|---:|---:|---:|
| A0 original-UV V-A current | 96.4692% | 1.76552% | 1.76531% |
| C1 pure-vector current | 1.61501% | 49.1925% | 49.1925% |

At fixed g_X, the A0/C1 B.13 thin-source ratios are 3491.53 in L, 2.09786 in +, and 2.09762 in -; the total B.13 ratio is 58.4525. This large longitudinal enhancement is the finite-temperature transport signature of the nonconserved axial current and its physical longitudinal-vector/Goldstone-equivalence contribution. It requires mode-resolved production and absorption in A0.

The B.7 source agrees with the accepted C1 same-grid source in the total and each polarization. The detailed-balance and shell checks are:

\[
\begin{aligned}
\epsilon_{\rm DB}^{B.7}&=3.31\times10^{-14},\\
\epsilon_{\rm DB}^{B.13}&=5.91\times10^{-14},\\
\epsilon_{\rm shell}^{\mu'}&=5.38\times10^{-13}.
\end{aligned}
\]

The maximum adaptive QUADPACK relative-error estimate is \(3.69\times10^{-8}\). At \(g_X=1\), the adaptive luminosity is
\[
L_{A0}(R_\nu)=1.4380831321\times10^{52}\ {\rm erg/s},
\]
with each mode agreeing with its A0 surface asymptote to better than \(6\times10^{-16}\).

This is an interior-profile A0 result. The outer 25--100 km semi-Compton opacity is still omitted, and the 103/153-node A0 radial convergence check has not yet been completed. It is not an SN1987A exclusion curve.

## 8.1 Preliminary adaptive 103-node comparison with C1

The accepted A0 103-node output contains both the legacy Simpson columns and the independent adaptive PCHIP/QUADPACK columns. The following comparison uses only the adaptive columns, with the same 10 MeV mass, 103 radial nodes, energy order 32, 121-point \(g_X\) grid, and three physical polarizations in A0 and C1.

| \(g_X\) (nearest scan point) | \(L_{\rm A0}/L_{\rm C1}\), \(R_{\rm far}=R_\nu\) |
|---:|---:|
| \(1.00\times10^{-11}\) | 9.1273 |
| \(1.04\times10^{-9}\) | 9.0624 |
| \(1.06\times10^{-8}\) | 4.7821 |
| \(1.08\times10^{-7}\) | 0.8630 |
| \(1.10\times10^{-6}\) | 1.0000 |
| \(9.09\times10^{-6}\) | 1.0000 |
| \(9.26\times10^{-5}\) | 1.0000 |
| \(9.44\times10^{-4}\) | 1.0000 |
| \(9.62\times10^{-3}\) | 1.0000 |
| \(9.81\times10^{-2}\) | 1.0000 |
| \(1\) | 1.0000 |

At low coupling, the UV axial charged-muon current increases the interior-profile escaped luminosity relative to the pure-vector C1 reference. At larger coupling the two curves approach the same surface-limited value. This is expected from the surface detailed-balance limit: once the escape layer is confined to the neutrinosphere boundary, the limiting luminosity depends on the common local Bose factor rather than the interior source normalization.

This comparison is a diagnostic from the 103-node baseline. The independent 153-node A0 refinement is required before quoting the radial uncertainty of the A0/C1 ratio. The outer 25--100 km semi-Compton opacity remains omitted; these values are not SN1987A limits.

## 9. Current execution and acceptance

A0 implementation and tests are committed to the PR #123 research branch.

- A0 workflow: [run 44582338538](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44582338538)
- C1 10 MeV grid convergence: [run 44577096997](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44577096997)

The A0 mapping/kernel tests and the existing C1 regression tests are rerun
before the adaptive 10 MeV transport calculation. The accepted 103-node adaptive baseline is
[workflow #44656918116](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44656918116).

The A0 baseline acceptance requires:

1. native JSON and radial CSV with 103 actual radial nodes, 32 energy
   nodes, 121 \(g_X\) points, and adaptive-radial fields enabled;
2. B.7 detailed balance, B.13 charge-mode detailed balance, and
   final-muon shell closure;
3. three-polarization source and luminosity closure;
4. exact agreement of the B.7 thin-source total and each mode with the
   same-grid accepted C1 result;
5. finite, nonnegative source and luminosity data;
6. QUADPACK error estimates below \(10^{-6}\) and high-coupling convergence to the A0 surface asymptote;
7. native-output SHA-256 manifest, artifact upload, and rebased Git archival.

After the baseline, A0 requires its own 103/153 radial and energy-order convergence scans. The 153-node radial audit script is committed as audit_croon_a0_10mev_adaptive_radial_convergence.py.
C1 grid convergence does not automatically establish A0 convergence
because the axial longitudinal source and opacity have different
kinematic weights.

Only after the A0 10 MeV convergence audit should the A0 six-mass scan be
accepted. No A0 exclusion curve is produced by this diagnostic stage.
