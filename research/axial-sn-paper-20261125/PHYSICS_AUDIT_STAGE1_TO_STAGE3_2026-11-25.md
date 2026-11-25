# Axial SN physics audit: model, moving-muon charge map, and neutrino kernels

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
