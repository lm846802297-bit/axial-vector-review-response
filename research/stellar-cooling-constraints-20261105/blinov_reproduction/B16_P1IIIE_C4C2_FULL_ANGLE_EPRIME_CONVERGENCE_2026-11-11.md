# P1-IIIe-C4C2: full-angle outgoing-energy quadrature convergence

Date: 2026-11-11  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`

## 1. Purpose

This supplementary audit closes the one remaining numerical-validation gap identified after the C4-C2 full-angle total-scattering workflow passed. C4-C1 had already checked the outgoing-energy quadrature at a fixed scattering angle; this calculation checks the same energy-order convergence **inside the full outgoing-angle integral**.

The existing C4-B2 collision kernel, C4-C1 exact outgoing-energy support, C4-C2 angular integral, C1 SFHo profile, and C2 occupation table are reused. No new collision kernel or weak tensor is introduced.

## 2. Definition

For each local state, the full-angle rate is
[
\Gamma_N(E)=2\pi\int_{-1}^{1}d\cos\theta
\int_{E'_{\min}(\theta)}^{E'_{\max}(\theta)}
dE'\,\frac{d\Gamma_N}{dE' d\Omega'}.
]

At each outgoing-angle node, the exact support roots are solved from
[
p_{\min}(E',\cos\theta;m_N^*)=p_{\max}(m_N^*,\nu_N,T),
]
using the existing 45T momentum-tail cutoff. The same support interval is then used for both (E') quadrature orders, 48 and 72. This isolates the energy-quadrature error from any change in kinematic support.

The comparison uses:
- (E_\nu=100) MeV;
- 8 Gauss-Legendre outgoing-angle nodes;
- 36 initial-momentum nodes;
- 12 azimuthal nodes;
- 48 versus 72 outgoing-energy nodes;
- 10,001 points in the support-root scan.

## 3. Benchmark coverage

All 16 combinations are evaluated:
- (r=0.20, 5.00, 10.00, 15.20) km;
- neutron and proton targets;
- neutrino and antineutrino.

## 4. Results

| Radius [km] | Maximum relative difference, 48 vs 72 |
|---:|---:|
| 0.20 | (3.16\times10^{-6}) |
| 5.00 | (2.09\times10^{-5}) |
| 10.00 | (3.29\times10^{-6}) |
| 15.20 | (5.31\times10^{-8}) |

The maximum over all 16 cases is
[
\boxed{\max\delta_{E'}=2.08975\times10^{-5}},
]
well below the (10^{-2}) acceptance threshold. The maximum support-root residual is
[
1.03173\times10^{-13}.
]

All 48- and 72-point full-angle rates are positive. The local computation took 503.86 s.

## 5. Acceptance

- 16/16 radius/species/sign cases present;
- all full-angle rates positive;
- full-angle (E') order-48 versus order-72 difference below 1%;
- support-root residual below (10^{-7}).

**Overall result: PASS.** Together with the C4-C2 cold-Horowitz, angular, initial-momentum, and azimuthal checks, this closes the stated C4-C2 numerical acceptance gate.

## 6. Reproducibility

- Driver: `audit_b16_p1iii_eos_c4c2_full_angle_eprime_convergence.py`
- Tests: `test_b16_p1iii_eos_c4c2_full_angle_eprime_convergence.py`
- Per-case CSV: `outputs/p1iiie_c4c2_full_angle_eprime_convergence_2026-11-11.csv`
- Acceptance JSON: `outputs/p1iiie_c4c2_full_angle_eprime_convergence_2026-11-11.json`
- Local source/input snapshot: commit `780e0c0bfd745ec41cb7b840c7ba4f8226bb723d`
- C1 profile Git blob: `9ff7818b0679992c0a9ba402330ec7f0d1f3041b`
- C2 occupation Git blob: `c472040a4551e68ffadbf7addf9402663f99e7e3`

The input C1/C2 files and the existing C4 collision-kernel implementation are unchanged. No B.2 opacity, radial transport, luminosity, PR #56 baseline, manuscript, referee response, or axial cooling curve is modified.

## 7. Next stage

C4-C2 is now complete. The next calculation is C4-C3: recompute the validated full-angle local total scattering rate at all 301 radial points, then form the fixed-local-energy, flat-space radial scattering optical-depth diagnostic. The ξ factor is restored exactly once because the C4-C2 Γ value already contains the available-volume nucleon occupation integral.
