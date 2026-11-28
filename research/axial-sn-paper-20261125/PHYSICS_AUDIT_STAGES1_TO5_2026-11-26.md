# Axial SN physics audit: model, thermal rates, transport and limiting cases

Date: 2026-11-25  
Repository: `lm846802297-bit/axial-vector-review-response`  
Branch: `research/axial-sn-paper-20261125`  
Source baseline: `main@6986463487ddade80ad72e67087b376e34969835`  
Status: **Step 1 PASS_WITH_NOTES; Step 2 pointwise charge-conjugation check PASS; Step 3 neutrino-kernel analytic/independent checks PASS. Step 4 remains open.**

## 1. Model and convention audit

The first-paper model remains the original one-VEV UV completion:
[
m_{A'}=2|g_X|v_s,qquad
g_{
u_mu}=+g_X,qquad g_{
u_	au}=-g_X.
]

Two equivalent charged-muon conventions occur in the repository and must not be mixed:

- The original UV matrix-element module writes
  [
  A'_alphaarmugamma^alpha(g_V-g_A^{(-)}gamma^5)mu,
  qquad g_A^{(-)}=+g_Xcos^2	heta_{mu R}.
  ]
- The finite-mixing thermal kernel writes
  [
  A'_alphaarmugamma^alpha(g_V+g_A^{(+)}gamma^5)mu,
  qquad g_A^{(+)}=-g_Xcos^2	heta_{mu R}.
  ]

Thus (g_A^{(-)}=-g_A^{(+)}). The physical quantities are convention independent:
[
|g_A^mu|=|g_X|cos^2	heta_{mu R},qquad
left|g_V^mu/g_A^muight|=	an^2	heta_{mu R}.
]
At (	heta_{mu R}=10^{-2}), (g_V/g_X=9.9996666711\times10^{-5}) and (g_A^{(+)}/g_X=-0.999900003333).

The original one-VEV Goldstone relation is
[
c_mu=rac{|g_A^mu|}{m_{A'}},qquad
|y_{Gmumu}|=2m_mu c_mu
=cos^2	heta_{mu R}rac{m_mu}{v_s}.
]
An independent exact (2\times2) singular-value diagonalization checked the phase-of-(S) coupling (m_R|s_Lc_R|/v_s) against this Ward-identity expression for three representative mass matrices. The maximum relative discrepancy was (3.9\times10^{-14}).

## 2. Goldstone Ward identity and physical polarizations

The tree-level open-muon-line identity is
[
q_alphaar u(p')gamma^alphagamma^5u(p)
=2im_muar u(p')gamma^5u(p),
]
with the corresponding two-diagram identity for (mugamma\leftrightarrowmu A'). The independent implementation used both (s)- and (u)-channel diagrams and checked the complete amplitude, not a single diagram.

Five non-collinear rest-frame kinematic points were tested. Results:

| Check | Maximum residual |
|---|---:|
| Final-muon on-shell condition | (1.79\times10^{-15}) |
| Axial Ward identity vs. pseudoscalar amplitude | (8.97\times10^{-13}) |
| Physical polarization norm | (1.97\times10^{-14}) |
| Polarization orthogonality | (5.99\times10^{-16}) |
| Completeness (sum_h\epsilon_h^\mu\epsilon_h^{*\nu}=-g^{\mu\nu}+q^\mu q^\nu/m_{A'}^2) | (1.42\times10^{-14}) |
| Photon Ward identity, relative amplitude | (1.05\times10^{-9}) |
| Vector-current longitudinal Ward shift | (2.32\times10^{-9}) |

The three physical modes are (L,+,-). The longitudinal mode is
[
\epsilon_L^\mu=(|\mathbf q|,E_{A'}\hat{\mathbf q})/m_{A'}.
]
For the conserved vector part only, (epsilon_L-q/m_{A'}) is an equivalent, numerically stable representative. The axial part must retain the physical (epsilon_L). The mixed-current implementation follows this separation at amplitude level.

The Goldstone-equivalence comparison was checked as a high-energy limit, not used as a finite-mass replacement. For spin/polarization-summed amplitudes at (E_{A'}/m_{A'}=84.1,345.7,913.5), the relative differences between the physical longitudinal amplitude and the (q^mu/m_{A'}) contraction were (2.03\times10^{-4}), (4.93\times10^{-5}), and (2.06\times10^{-5}), respectively.

### Quantum anomaly scope

The identity above is the tree-level open-muon-line Ward identity. The muon-only axial current has an electromagnetic anomaly at loop level. In the full UV model the (U(1)_X-U(1)_{\rm EM}^2) anomaly cancels between the oppositely charged muon and tau sectors (the SM-vectorlike heavy-lepton pairs cancel within each pair). Therefore a muon-only EFT calculation of (G\gamma\gamma) must retain the threshold-matching contribution of the integrated-out charged states. This does not modify the tree-level semi-Compton Ward identity, but it must be addressed before deciding whether loop-induced Primakoff or two-photon channels are negligible.

## 3. Independent moving-muon positron check

The existing moving-muon kernel evaluates both (mu^-) and (mu^+) targets by reversing the relative axial coefficient for the positive-muon target:
[
g_A\longrightarrow -g_A,
]
while retaining the vector coefficient. This is required because the vector and axial currents have opposite charge-conjugation parity.

A new independent implementation used explicit (v)-spinors and the reversed fermion-flow amplitude for
[
gamma+mu^+\tomu^++A'.
]
It compared the direct (v)-spinor result against the (u)-spinor charge-conjugation map with (g_A\to-g_A), mode by mode. Five moving-muon kinematic points were tested, including the (m_{A'}=10^{-7}) MeV ultralight point used by the existing thermal-kernel regression. The comparison covered pure-vector, pure-axial, and finite-mixing currents and all (L,+,-) modes.

- Maximum relative discrepancy: (2.72\times10^{-9}).
- Maximum final-muon shell error: (2.18\times10^{-14}).
- The direct (v)-spinors satisfy ((\not p+m)v=0) to (1.14\times10^{-13}) in the moving-spinor normalization check.

This closes the explicit-(v)-spinor charge-conjugation gap for the sampled local amplitudes. It is a pointwise amplitude check, not a replacement for the full thermal phase-space integral.

### 3.1 Moving-muon thermal phase-space normalization

The thermal kernel follows the invariant absorption integral
[
\Gamma_{\rm abs,h}(q)=\frac{1}{2\omega_{A'}}
\int d\Pi_p\,d\Pi_{p'}\,d\Pi_k\,
(2\pi)^4\delta^{(4)}(p+q-p'-k)
\overline{|\mathcal M_h|^2}
f_\mu(E_p)[1-f_\mu(E_{p'})][1+f_\gamma(\omega_\gamma)].
]
The initial muon spin is averaged in the matrix element; the prefactor restores the two initial spin states. The initial muon azimuth is integrated by rotational symmetry, while the photon azimuth is integrated explicitly. With
[
t=\sqrt{(E_\mu-m_\mu)/T},\qquad
\frac{p^2dp}{E_\mu}=2Tpt\,dt,
]
and the final-muon on-shell delta function, the photon-energy Jacobian is (\omega_\gamma/C), where
[
C=E_\mu+\omega_{A'}-\mathbf p_\mu\cdot\hat{\mathbf k}
-|\mathbf q|\cos\theta_\gamma,qquad
\omega_\gamma=\frac{m_{A'}^2+2p_\mu\cdot q}{2C}.
]
This gives the repository prefactor (1/(128\pi^4\omega_{A'})) with its stated spin and azimuth conventions. The rate sums the two physical photon polarizations (no initial-photon average) and computes one (A') mode at a time.

The source implementation includes exact two-body recoil, both muon charges with (\mu_{\mu^\pm}=\pm\mu_\mu), Fermi blocking, photon Bose enhancement, and amplitude-level V--A interference. The independent moving-(v)-spinor comparison in §3 checks the positive-muon charge map. The existing `test_thermal_rates.py` contains cold-dilute, stationary-muon, Eq. (5.12) normalization, photon-Ward, and mode-by-mode detailed-balance regressions. Those archived tests were inspected; the complete high-dimensional thermal quadrature has not yet been rerun as a new local primary calculation.

## 4. Neutrino inverse-decay, blocking, and detailed balance

For each active flavor, the vacuum width is
[
\Gamma(A'\to\nu_i\bar\nu_i)=rac{g_X^2m_{A'}}{24\pi}.
]
The two-flavor total is therefore
[
\Gamma_{\nu\bar\nu}^{\rm vac}=rac{g_X^2m_{A'}}{12\pi}.
]

The mode-resolved angular weights used by the repository are normalized:
[
W_L(z)=rac{3}{4}(1-z^2),qquad
W_\pm(z)=rac{3}{8}(1\pm z)^2.
]
The daughter energies are (E_{1,2}=(\omega\pm k z)/2), and the statistical factors are
[
f_{\nu_i}(E_1)f_{\bar\nu_i}(E_2),qquad
[1-f_{\nu_i}(E_1)][1-f_{\bar\nu_i}(E_2)].
]
With (mu_{\bar\nu_i}=-mu_{\nu_i}), their ratio is exactly (e^{-\omega/T}), independently of the chemical potential.

An independent Gauss-Legendre implementation checked:
- the two-flavor vacuum normalization at (m=10) MeV and (omega=10,30) MeV, with maximum relative discrepancy (4.0\times10^{-15});
- mode-by-mode detailed balance at (T=30) MeV and (mu_{\nu_\mu}=\pm45,0) MeV, with maximum relative discrepancy (7.1\times10^{-16});
- the expected (+leftrightarrow-) circular-mode exchange under (mu_{\nu_\mu}\to-\mu_{\nu_\mu}), with discrepancy (4.7\times10^{-16});
- equality of the two flavor contributions at zero chemical potential.

The repository's existing `test_rates.py` independently checks the vacuum limit, scalar phase-space integral, detailed balance, circular-mode asymmetry, and sign reversal. Those repository test modules were inspected but were **not rerun** in this local audit; the numerical values above come from the separately written local implementations.

## 5. Source identities and local run provenance

Pinned source revision:
`main@6986463487ddade80ad72e67087b376e34969835`.

| Source | Git blob SHA |
|---|---|
| Original UV semi-Compton matrix element | `188747498b105159aca525651d16448cdc3f592c` |
| Original Goldstone Ward regression | `8819a1257555078c5aeb9b8dd5f9ac0f6f225f1f` |
| Single-VEV axial mapping | `bd31ad4f5896b98612e07dcabee69b278ec33b46` |
| Moving-muon semi-Compton kernel | `2cf8f8f4c3929c1d07f6800a8293f44185dec986` |
| Finite-mixing model convention | `8c4a8301134fd745bbd40e07eb7550c761ac7e86` |
| Moving-muon thermal regressions | `115174656f92a4f30e89df46d37709caeb5ad651` |
| Neutrino and decay rates | `dd4d1accfd58a574e704f477f611299f15943465` |

Independent local environment:
- Python 3.13.5, NumPy 2.3.5; calculations used CPU double precision.
- Linux x86_64, AMD EPYC 9V74, 5 visible CPU cores, 5.8 GiB RAM; no GPU used.
- No external profile data were used in these local algebraic and pointwise tests. All kinematic inputs are embedded in the independent scripts.

Independent source/result SHA-256:
- Stage-1 model/Ward/polarization script: `b6f23d9939ebdc01030edfe71db7f68391773069c9b99c63450b98a75d18149f`.
- Stage-1 stdout: `4198a99a96279b6689370ea443140f2b79fd613066b7f609830223656c091f02`.
- Moving-muon direct-(v)-spinor script: `adb028c89998b2b853fdd8d304d846a5e73e126fe31f9aa655cf2207585e2bbd`.
- Moving-muon stdout: `ad10c414415c903e557fae021d9c38e28052f1e23d8919f28c7f927b22b62308`.
- Independent neutrino-rate script: `6d2ba55b1bb6cf649d5a0fcf377a1857bb0ec149673d7da4dcd4dcb9388aaaa1`.
- Neutrino-rate stdout: `4894768f475e2a8a4fa9ea62860ec68154d97934c665f5a0b16fbd3966b653f8`.

## 6. Current gate status and next work

| Ordered task | Status | Remaining acceptance item |
|---|---|---|
| 1. Axial current, Goldstone Ward identity, three polarizations | **PASS_WITH_NOTES** | Loop-level anomaly matching is separate from the tree-level result. |
| 2. Moving-muon semi-Compton production/absorption matrix elements | **Pointwise PASS** | Next verify the full thermal quadrature and its convergence locally against the archived thermal-kernel regressions. |
| 3. Neutrino inverse decay, Pauli blocking, detailed balance | **PASS** | Include in the combined local channel/transport audit. |
| 4. Decay widths, optical depth, escape probability | **IN PROGRESS** | Resolve the energy-frame convention in the old lapse-weighted fixed-profile transport before using it for a new scan. |
| 5. Low-mass pseudoscalar and vector limits | **PARTIAL** | Complete independent comparisons of the local kernels and their normalizations. |
| 6. Axial parameter scan | **NOT STARTED** | Do not start until Steps 1–5 are accepted. |

### Specific transport issue found

The old fixed-profile axial scan uses an (N^2) luminosity weight and lower energy limit (m_{A'}/N(r)), while the local thermal rates are called with the same numerical energy grid and local (T(r),mu(r)). The path opacity also uses a fixed numerical energy and a fixed (v=\sqrt{1-m^2/\omega^2}). This is a documented leading-gravity prescription, but the local-energy versus conserved-(E_\infty) mapping is not fully derived in one consistent convention. It must be resolved before that old contour is used as a physical prediction.

For the first clean transport control, retain the C1/A0 flat-space local-energy convention (no lapse/redshift) as a separately labeled approximation, then derive the conserved-(E_\infty) GR treatment as a distinct calculation. Do not mix the two conventions in a single rate or opacity integral.

The 10 MeV Blinov high-absorption reproduction discrepancy remains deferred until original reference inputs are obtained. It is not a blocker for the local physics checks above.


## 7. Decay widths and local attenuation

For the original model, only the two active-flavor neutrino channels are open below the dimuon threshold:
\[
\Gamma_{\nu_i\bar\nu_i}^{\rm vac}
=\frac{g_X^2m_{A'}}{24\pi},
\qquad
\Gamma_{\nu\bar\nu}^{\rm vac}
=\frac{g_X^2m_{A'}}{12\pi}.
\]
The electron-flavor channel is absent at tree level. The opposite signs of the \(\nu_\mu\) and \(\nu_\tau\) charges do not interfere in the inclusive width.

Above threshold, with \(r_\mu=m_\mu^2/m_{A'}^2\) and \(\beta_\mu=\sqrt{1-4r_\mu}\),
\[
\Gamma_V(A'\to\mu^+\mu^-)
=\frac{g_V^2m_{A'}}{12\pi}\beta_\mu(1+2r_\mu),
\]
\[
\Gamma_A(A'\to\mu^+\mu^-)
=\frac{g_A^2m_{A'}}{12\pi}\beta_\mu^3.
\]
For the finite-mixing current, the integrated vacuum V--A interference vanishes:
\[
\Gamma_{\mu\mu}^{\rm vac}
=\frac{g_X^2m_{A'}}{12\pi}\beta_\mu
\left[
\sin^4\theta_{\mu R}(1+2r_\mu)
+\cos^4\theta_{\mu R}(1-4r_\mu)
\right].
\]
The thermal angular distributions can still retain charge- and mode-dependent interference in a medium with nonzero muon chemical potential. The archived width implementation gives the axial dimuon-to-total-neutrino width ratios 0.02152, 0.35756 and 0.81967 at \(m_{A'}=220,300,600\) MeV, respectively.

For a mode in local thermal equilibrium,
\[
C_h[f_h]=\Gamma_{{\rm prod},h}(1+f_h)
-\Gamma_{{\rm abs},h}f_h.
\]
Detailed balance gives
\[
\Gamma_{{\rm prod},h}
=e^{-\omega_{\rm loc}/T}\Gamma_{{\rm abs},h},
\qquad
\Gamma_{{\rm red},h}
=(1-e^{-\omega_{\rm loc}/T})\Gamma_{{\rm abs},h}.
\]
The local attenuation length is \(v_h/\Gamma_{{\rm red},h}\), and for a prescribed path
\[
P_h=\exp\left[
-\int_{\rm path}\frac{ds}{v_h}
\Gamma_{{\rm red},h}(\omega_{\rm loc},r)
\right].
\]

A conservative local bound can be obtained from the \(\nu_\tau\bar\nu_\tau\) channel alone. With \(\mu_{\nu_\tau}=0\), each Fermi blocking factor satisfies \(1-f\ge1/2\), so
\[
\Gamma_{{\rm red},\nu_\tau}
\ge
(1-e^{-\omega/T})\frac{\Gamma_{\nu_\tau\bar\nu_\tau}^{\rm vac}}{4}
=
(1-e^{-\omega/T})\frac{\Gamma_{\nu\bar\nu}^{\rm vac}}{8}.
\]
At \(m_{A'}=100\) MeV, \(g_X=4.99\times10^{-5}\), \(\omega=200\) MeV and the central-profile \(T=19.265221\) MeV,
\[
\Gamma_{\nu\bar\nu}^{\rm vac}=6.60496\times10^{-9}\ {\rm MeV},
\quad
\tau_{\rm vac}=9.96542\times10^{-14}\ {\rm s},
\]
\[
\ell_{\rm vac}=\beta\gamma\,c\tau_{\rm vac}
=5.17460\times10^{-5}\ {\rm m}.
\]
Here \(\omega/T=10.3814\) and \(1-e^{-\omega/T}=0.999969\). The \(\nu_\tau\)-only blocking bound therefore gives
\[
\ell_{\rm red}\le 8.00025\,\ell_{\rm vac}
=4.13981\times10^{-4}\ {\rm m}.
\]
This is a conservative local inverse-decay attenuation bound at the stated point; it is not a scattering mean free path or a complete stellar transport result. Other open absorption channels only increase the total opacity.

## 8. Optical depth, escape probability, and polarization state counting

The physically mode-resolved no-mixing transport equation is
\[
D f_h=\Gamma_{{\rm prod},h}
-\Gamma_{{\rm red},h}f_h,
\qquad h=L,+,-.
\]
Consequently,
\[
\tau_h(r,\omega,\Omega)
=\int_{\rm ray}\frac{ds}{v_h}
\Gamma_{{\rm red},h}(r(s),\omega(s)),
\qquad
P_h=e^{-\tau_h},
\]
and the escaped luminosity is formed as
\[
L_{\rm esc}^{\rm modes}
=\sum_{h=L,+,-}\int d\Pi\,\omega\,
\Gamma_{{\rm prod},h}\,
\left\langle e^{-\tau_h}\right\rangle_\Omega.
\]
The sum is taken after the mode-dependent attenuation. It is not equivalent to applying one summed opacity to all three modes.

The existing B2 polarization-state-counting audit settles the factor-of-three issue:

- The mode-resolved detailed-balance identity is sum-to-sum and has no extra factor of three.
- A fixed polarization mode attenuates with its own \(\Gamma_{{\rm red},h}\).
- An equal-occupation scalar closure uses \(\sum_h\Gamma_{{\rm red},h}/3\).
- The literal scalar B.2 prescription is retained as an equation-level reproduction lane; it is not silently reinterpreted as the physical no-mixing opacity.

The old transport kernel in research/stellar-cooling-constraints-20261105/transport.py already carries mode-resolved source and opacity arrays, the \(1/v_h\) path factor, and the angular average. Its current semi-Compton input, however, is the earlier stationary-muon/effective-density approximation. It has not yet been connected to the validated exact moving-muon thermal kernel. The 10 MeV vector B2 state-counting comparison also shows that scalar-summed and mode-resolved luminosities can differ substantially after exponentiation; that numerical ratio is not transferred to the axial model.

The gravitational-energy convention is reused from the existing B16 audit, not reopened here: B.1 uses the local production energy with the \(N(r)^2\) source weight and lower limit \(m_{A'}/N(r)\); the literal B.2 path opacity holds the same \(\omega\) along the Euclidean chord. The separate path-redshift-only calculation remains a sensitivity diagnostic, not the published baseline or a full-GR ray calculation.

Evidence reused:
- B2_POLARIZATION_BOLTZMANN_STATE_COUNTING_AUDIT_2026-11-13.md, Git blob 8697c92cc6648ac1e647c38ed51c360879ae8485.
- B16_ENERGY_VARIABLE_AND_PATH_REDSHIFT_CONVENTION_AUDIT_2026-11-09.md, Git blob eb0794aafe7e4096b65aacf8c9c96c0b402120d0.
- B16_OUTER_PROFILE_NEUTRINO_OPACITY_DIRECTION_AUDIT_2026-11-08.md, Git blob 85dba39b06339af1a34e39b4f770be5d714222cf.

## 9. Moving-muon thermal rates and neutrino inverse decay

The exact moving-muon semi-Compton thermal integral is already implemented and independently validated in the existing repository. The archived validation covers both \(\mu^-\) and \(\mu^+\), exact two-body recoil, all \(L,+,-\) modes, Fermi blocking, photon Bose enhancement, and coherent V--A interference.

The existing moving-Compton validation gives:
- stationary-target endpoint residual: zero for pure vector and pure axial currents;
- maximum photon-Ward amplitude residual: \(7.71\times10^{-13}\);
- maximum conserved-vector mediator-Ward residual: \(1.02\times10^{-12}\);
- zero-chemical-potential charge-conjugation/interference cancellation residual: \(2.91\times10^{-15}\);
- core-like degenerate-gas coarse-to-fine thermal absorption difference: \(2.51565\times10^{-4}\);
- mode-by-mode detailed-balance residual: \(4.35\times10^{-15}\);
- unpolarized Eq. (5.12) normalization residual: \(3.11\times10^{-15}\).

The full dimuon thermal momentum integral is also archived separately. Its 64/128/192-point energy-quadrature differences are at most \(8.73\times10^{-14}\), its maximum detailed-balance residual is \(5.62\times10^{-14}\), and the threshold axial/vector width-ratio check agrees to \(1.11\times10^{-15}\). The dimuon channel remains exactly closed for \(m_{A'}\le2m_\mu\).

The neutrino inverse-decay kernel is common to the original axial model and the vector \(L_\mu-L_\tau\) control because the two active-flavor coupling magnitudes are both \(g_X\). The signs \(g_{\nu_\mu}=+g_X\) and \(g_{\nu_\tau}=-g_X\) do not alter the separate inclusive rates. Two distinct archived B16 checks are reused and their profile versions are kept separate:

1. The B.7--B.10 closed-form audit covers 40 points: four radii \((8,10,12.5,15)\) km, five energies \((60,110,210,510,1010)\) MeV, and both active flavors. It uses the current vertex-preserving profile SHA-256 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. The Eq. (B.9) closed form versus the repository pair average has maximum relative residual \(2.89\times10^{-15}\); direct angular orders 128, 256, 512 and 1024 give maxima \(2.89,3.11,2.66,3.11\times10^{-15}\). The B.7 two-flavor normalization and B.10/B.4 detailed-balance identity agree algebraically. This specific V8 result is not described as a Python rerun: its accompanying Python reproduction script was added but not executed in that V8 session.
2. The separate direct mode-resolved inverse-decay audit uses a historical 501-node profile SHA-256 08d7afce8252bce18dcd69035b9b5cd76ee2a848b3e755b84bb8ede72f6e65b9. It covers ten radii and seven energies with a 512-point direct angular integral. The 48-point code versus direct production/absorption residuals are \(4.01\times10^{-12}\); analytic \(I\) versus direct angular integration is \(4.19\times10^{-15}\); the B.4 reduced-opacity residual is \(6.81\times10^{-15}\); the B.10 detailed-balance residual is \(6.82\times10^{-15}\); and the 256/512-point difference is \(5.55\times10^{-15}\). This historical-profile output is not merged numerically with the current-profile scan.

The separate local independent check in this branch gives a maximum detailed-balance residual \(7.08\times10^{-16}\) for \(\mu_{\nu_\mu}=\pm45\) MeV, \(T=30\) MeV and \(\omega=40\) MeV, and verifies the circular-mode exchange under \(\mu_{\nu_\mu}\to-\mu_{\nu_\mu}\).

The thermal response scan and the two-point profile data remain local-emissivity results, not a full radial luminosity. The reconstructed SFHo-18.8 profile SHA-256 is 9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c. The original Garching hydro snapshot has not been substituted or inferred.

## 10. Independent low-mass pseudoscalar and conserved-vector limits

The original one-VEV UV relations give
\[
m_{A'}=2g_Xv_s,\qquad
g_A^\mu=-g_X\cos^2\theta_{\mu R},
\]
and hence the Goldstone-equivalent pseudoscalar Yukawa magnitude
\[
y_{G\mu\mu}
=\frac{2|g_A^\mu|m_\mu}{m_{A'}}
=\cos^2\theta_{\mu R}\frac{m_\mu}{v_s}.
\]
The physical longitudinal \(A'\) mode already contains this contribution; a separate Goldstone production channel must not be added to the \(L\) mode.

A new independent explicit-Dirac-spinor calculation was run for \(\gamma\mu\to\mu A'\), with exact recoil and the two Compton diagrams. It compares the physical longitudinal axial amplitude to the pseudoscalar amplitude weighted by \(y_G=2m_\mu/m_{A'}\), and separately tests the conserved-vector longitudinal mode. The grid uses \(E_\gamma=(0.05,0.1,0.5,1)\) MeV and \(m_{A'}/E_\gamma=(0.1,0.01,0.001)\), with 160-point angular integration.

Results:
- maximum physical-\(L\) versus Goldstone-pseudoscalar cross-section difference: \(7.42\times10^{-5}\) over the full grid; for \(m_{A'}/E_\gamma\le10^{-2}\), it is at most \(4.84\times10^{-7}\);
- maximum axial Ward residual in the mode-summed comparison: \(7.60\times10^{-7}\);
- final-muon mass-shell residual: \(3.26\times10^{-16}\);
- conserved-vector \(q_\mu\mathcal M^\mu\) relative to the transverse rate: at most \(9.18\times10^{-20}\);
- \(\sigma_L/\sigma_T\), divided by \((m_{A'}/E_\gamma)^2\), lies between 0.50024 and 0.50469, approaching the expected \(1/2\) low-energy coefficient;
- changing the angular order 80 to 240 changes the small-mass vector coefficient by less than \(4.8\times10^{-11}\).

The independent source and native result are archived at:
- verification/stage5_pseudoscalar_vector_limit_audit.py, SHA-256 6263b808cada52991d95a41fc40a31ddb306a705c11343a5e0f2cbac903520d7;
- verification/outputs/stage5_pseudoscalar_vector_limit_audit.json, SHA-256 1224735e0f7e08db97aa08f5bf1e94b8e080f80dfb2ebb27a9aa21e1e32acdbd.

The existing moving-muon thermal scan independently shows the low-mass axial scaling:
\[
Q_L/g_X^2\propto m_{A'}^{-2},
\qquad
m_{A'}^2Q_L/g_X^2
= (4.5169\times10^4)\ {\rm MeV}^7
\]
to a relative spread of \(2.63\times10^{-4}\) between \(m_{A'}=0.01\) and 1 MeV. At \(m_{A'}=0.01\) MeV, \(Q_L/Q_T=1.305\times10^7\). This is the expected Goldstone-equivalent longitudinal enhancement, not a new independent pseudoscalar channel.

The scaling must be interpreted along the UV trajectory. At fixed \(g_X\), the per-\(g_X^2\) longitudinal response grows as \(m_{A'}^{-2}\). At fixed \(v_s\), \(g_X=m_{A'}/(2v_s)\), so the physical \(g_X^2Q_L/g_X^2\) remains finite and is controlled by \(y_{G\mu\mu}^2\). The Goldstone perturbativity criterion used in the archived A0 scan is
\[
\frac{y_{G\mu\mu}^2}{4\pi}\le1,
\qquad
g_X\le
\frac{\sqrt{4\pi}\,m_{A'}}{2m_\mu\cos^2\theta_{\mu R}}.
\]
For \(\theta_{\mu R}=0.01\), the corresponding \(g_X\) ceilings are \(1.68\times10^{-9}\) at \(m_{A'}=0.1\) eV, \(1.68\times10^{-3}\) at 0.1 MeV, and 0.1678 at 10 MeV.

The archived fixed-profile cooling scan gives \(g_{X,\rm lower}\propto m_{A'}\) over 0.01--1 MeV, with \(g_{X,\rm lower}/m_{A'}\simeq3.8462\times10^{-11}\ {\rm MeV}^{-1}\). This is a conditional fixed-profile scaling diagnostic, not a final exclusion: that scan has not been recomputed with the exact moving-muon kernel in full radial, mode-resolved transport. No standalone pseudoscalar thermal kernel has been independently integrated in this stage; the current acceptance is the amplitude-level Goldstone equivalence plus the archived axial thermal scaling.

## 11. Reproducibility and source identities

The independent Stage-5 run used:
- Python 3.13.5, NumPy 2.3.5;
- Linux x86_64, AMD EPYC 9V74, five visible CPU cores, 5.8 GiB RAM;
- CPU double precision; no GPU and no external profile input;
- muon mass \(m_\mu=105.6583755\) MeV;
- exact two-body kinematics and 160-point Gauss-Legendre angular quadrature, with an 80/160/240 convergence check.

The existing moving-muon thermal validation manifest records Python 3.12.16, NumPy 2.5.4, SciPy 1.18.1, the source hashes and the executed validation commands. The thermal response scan separately records hashes for rates.py, moving_muon_compton.py, thermal_dimuon.py and the scan driver. These archived calculations are reused rather than rerun.

## 12. Updated ordered gate status

| Ordered task | Status | Remaining acceptance item |
|---|---|---|
| 1. Original axial current, Goldstone Ward identity, three polarizations | **PASS_WITH_NOTES** | The tree-level open-muon-line identity is established; loop-level anomaly matching remains a separate EFT issue. |
| 2. Moving-muon semi-Compton production/absorption matrix elements | **PASS** | Local thermal kernels and convergence checks pass; full radial mode-resolved transport is separate. |
| 3. Neutrino inverse decay, Pauli blocking, detailed balance | **PASS** | The local kernel is validated and ready to be combined with the moving-muon opacity. |
| 4. Decay widths, optical depth and escape probability | **PARTIAL** | Widths, reduced-opacity identity and mode-resolved escape formula pass; connect the exact moving-muon rates to the radial transport kernel and complete source-weighted radial/energy convergence. |
| 5. Low-mass pseudoscalar and conserved-vector limits | **PASS_WITH_NOTES** | Direct amplitude and thermal-scaling checks pass; a standalone pseudoscalar thermal-rate integration is not claimed. |
| 6. Axial parameter scan | **NOT STARTED** | Start only after the mode-resolved moving-muon transport in Step 4 passes. |

### Immediate next calculation

Build the radial-energy tables for \(\Gamma_{{\rm prod},h}(r,\omega)\) and \(\Gamma_{{\rm abs},h}(r,\omega)\) from the validated exact moving-muon kernel, combine them with the already validated \(\nu_\mu,\nu_\tau\) inverse-decay rates, and feed the three modes separately into the existing transport kernel. Use the accepted B.1 local-energy source convention and the fixed-\(\omega\) B.2 Euclidean-chord comparison convention consistently. Validate radial, energy, angular and interpolation convergence before extracting any axial free-streaming or trapping boundary. Do not run a new parameter scan until this gate is passed.
