# Croon A0: original-UV finite-mixing axial-vector transport

Date: 2026-11-20  
Status: **10 MeV full radial transport running; A0 regression tests passed. This is not yet a converged A0 luminosity result.**

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

## 7. Current execution and acceptance

A0 implementation and tests are committed to the PR #123 research branch.

- A0 workflow: [run 44582338538](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44582338538)
- C1 10 MeV grid convergence: [run 44577096997](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44577096997)

The A0 mapping/kernel tests and the existing C1 regression tests passed
before the 10 MeV transport calculation started.

The A0 baseline acceptance requires:

1. native JSON and radial CSV with 103 actual radial nodes, 32 energy
   nodes, and 121 \(g_X\) points;
2. B.7 detailed balance, B.13 charge-mode detailed balance, and
   final-muon shell closure;
3. three-polarization source and luminosity closure;
4. exact agreement of the B.7 thin-source total and each mode with the
   same-grid accepted C1 result;
5. finite, nonnegative source and luminosity data;
6. native-output SHA-256 manifest, artifact upload, and rebased Git archival.

After the baseline, A0 requires its own radial/energy convergence scan.
C1 grid convergence does not automatically establish A0 convergence
because the axial longitudinal source and opacity have different
kinematic weights.

Only after the A0 10 MeV convergence audit should the A0 six-mass scan be
accepted. No A0 exclusion curve is produced by this diagnostic stage.
