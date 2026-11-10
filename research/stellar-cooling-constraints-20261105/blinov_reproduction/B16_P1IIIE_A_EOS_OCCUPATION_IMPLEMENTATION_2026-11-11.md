# P1-IIIe-A: Garching EOS nucleon occupation implementation

Date: 2026-11-11  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`

## 1. Scope

This stage implements the local nucleon occupation and static degeneracy factor consistent with the Garching SFHo EOS. It is deliberately separate from the existing vacuum-mass ideal-Fermi-gas branch.

Primary source: D. F. G. Fiorillo et al., *Axion-photon conversion in transient compact stars: Systematics, constraints, and opportunities*, JCAP 03 (2026) 053, arXiv:2509.13322v2:
- Sec. 4.2: Garching model provenance and archive availability.
- Sec. 4.3, Eqs. (41)-(42): recoil-free degeneracy factor and the two space-time weighting prescriptions.
- Appendix C.1, Eqs. (81)-(82): EOS-consistent nucleon occupation and SFHo kinetic dispersion.

The Garching simulations are stated to have evolved to 10 s post-bounce and to be available upon request. The paper does not publish the full local arrays of (m_N^*,U_N,mu_N^*) in its article text.

## 2. Implemented thermodynamics

The implementation uses the tabulated convention in which (mu_N^*) does not include the nucleon rest mass:
[
f_N(p)=left[expleft(rac{U_N+K_N(p)-mu_N^*}{T}ight)+1ight]^{-1},
qquad
K_N(p)=sqrt{p^2+m_N^{*2}}-m_N^*.
]

It defines
[

u_N=mu_N^*-U_N,
qquad
f_N(p)=operatorname{expit}!left(rac{
u_N-K_N(p)}{T}ight).
]

The number density, including the two spin states, is
[
n_N=rac{1}{pi^2(hbar c)^3}int_0^infty dp,p^2f_N(p).
]
The recoil-free static blocking factor is
[
F_{NN}^{m deg}
=rac{int_0^infty dp,p^2f_N(p)[1-f_N(p)]}
{int_0^infty dp,p^2f_N(p)}.
]
The spin factor cancels in the ratio.

The code also evaluates the independent thermodynamic identity
[
f_N(1-f_N)=Tleft(rac{partial f_N}{partial
u_N}ight)_{T,m_N^*},
qquad
F_{NN}^{m deg}
=rac{T}{n_N}
left(rac{partial n_N}{partial
u_N}ight)_{T,m_N^*}.
]
The derivative check holds (T,m_N^*,U_N) fixed; it is not a derivative along a self-consistent EOS trajectory.

For the vacuum-mass limit, the mapping is
[
m_N^*=m_N,quad U_N=0,quad mu_N^*=mu_N^{m total}-m_N.
]
With this mapping the new occupation reproduces the existing ideal relativistic Fermi-gas occupation exactly. The old code is not overwritten.

## 3. Global Table 1 targets and exact weights

Fiorillo et al. define the averages over mass coordinate and time:
[
langle Qangle_{T^3}
=rac{int dM,dt,Q(M,t)T^3(M,t)}
{int dM,dt,T^3(M,t)},
]
and
[
langle Qangle_{ho T^{5/2}}
=rac{int dM,dt,Q(M,t)ho(M,t)T^{5/2}(M,t)}
{int dM,dt,ho(M,t)T^{5/2}(M,t)}.
]
They state that these averages omit gravitational redshift/lapse effects.

For SFHo-18.8, the published targets are:
| Quantity | (T^3) weight | (ho T^{5/2}) weight |
|---|---:|---:|
| (langle F_{pp}^{m deg}angle) | 0.80 | 0.77 |
| (langle F_{nn}^{m deg}angle) | 0.48 | 0.42 |

These are global, time-integrated targets. They are not local values and cannot be reproduced from the (t_{m pb}=1) s Fig. 1/Fig. 12 snapshot alone.

The CSV reader therefore requires an explicit `dMdt_weight` column representing the cell measure (Delta M,Delta t) (or its equivalent quadrature weight). It does not silently replace the mass-time integration by an equal-weight average over rows.

## 4. Code and tests

- `audit_b16_p1iii_eos_nucleon_distribution.py`: EOS occupation, density, static degeneracy factor, profile-weighted averages, and CSV interface.
- `test_b16_p1iii_eos_nucleon_distribution.py`: unit tests for the dispersion, occupation bounds, common (U_N,mu_N^*) shift invariance, vacuum-mass limit, derivative identity, dilute limit, quadrature convergence, and the two global weighting formulas.
- `.github/workflows/b16-p1iii-eos-degeneracy.yml`: independent CI validation only; it does not commit or modify production outputs.

The CSV interface requires:
`T_MeV`, `rho_g_cm3`, `dMdt_weight`, and for each species (n,p), `mstar_N_MeV`, `U_N_MeV), and `mu_star_N_MeV). Optional free-nucleon density columns `n_n_target_fm3` and `n_p_target_fm3` provide a local density-closure test.

The implementation checks the SFHo effective-mass splitting (m_n^*-m_p^*=1.2933) MeV and reports the maximum residual. It does not impose this relation by modifying input data.

## 5. Numerical software self-test

A deterministic synthetic test fixture (not Garching profile data) was evaluated directly:
- Four local states cover neutron/proton species and two temperature scales.
- The direct (f(1-f)) integral agrees with the independent finite-difference density derivative.
- The 256- and 512-node quadratures agree.
- The vacuum-mass mapping reproduces the existing total-chemical-potential occupation.
- A dilute Boltzmann state gives (F^{m deg}	o1).
- Shifting (U_N) and (mu_N^*) by the same constant leaves the distribution unchanged.

The exact numerical residuals are archived in `outputs/p1iii_eos_kernel_self_test_2026-11-11.json`. These checks validate the implementation, not the four published Garching averages.

## 6. Validation boundary

The published global values 0.80, 0.77, 0.48, and 0.42 are **not yet claimed as reproduced**. A valid reproduction requires the Garching mass-time profiles (or equivalent cell data) for (T,ho,m_N^*,U_N,mu_N^*) with the mass-time integration measure.

The present stage does not:
- infer (m_N^*,U_N,mu_N^*) from the digitized Caputo/Fig. 12 density curves;
- tune local parameters to force agreement with Table 1;
- replace the old ideal-gas benchmark;
- implement the dynamic weak response (W_N^{mu
u}(q_0,q));
- modify B.2 opacity, the pure-vector Fig. 7 benchmark, or any axial cooling curve.

## 7. Next stage

After the Garching profile data become available, run the CSV interface and check:
1. (n_n(r,t)) and (n_p(r,t)) reconstructed from the same EOS distributions;
2. local density closure against the free-nucleon densities in the archive;
3. the effective-mass splitting and chemical-potential convention;
4. both mass-time weighted Table 1 degeneracy averages.

Only after these checks pass should P1-IIIe-B be considered complete and the EOS quasiparticle dispersion be introduced into the dynamic response in P1-IIIe-C.
