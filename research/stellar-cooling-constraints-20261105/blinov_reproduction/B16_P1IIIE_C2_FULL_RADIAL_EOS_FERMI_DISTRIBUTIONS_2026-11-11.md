# P1-IIIe-C2: full-radial EOS-consistent nucleon Fermi distributions

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Scope and input provenance

C2 reconstructs the neutron and proton Fermi occupations at every one of the 301 radii in the committed C1 full-profile mapping. The input is the Caputo SFHo-18.8 published-figure snapshot at \(t_{\rm pb}=1\) s, on \(r=0.20\)--\(15.20\) km with \(\Delta r=0.05\) km. It is not a raw time-dependent Garching simulation profile.

Input:
- \`outputs/caputo_sfho_eos_profile_full_0p05km_2026-11-11.csv\`
- SHA-256: \`97d6a88a95d0a636ac359ae981b1b06ec33b88b0f106bfb88d203cb0f9fbbc59\`
- C1 EOS coordinate: \(Y_p^{\rm tot}=Y_e+Y_\mu\), not the free-proton fraction.
- Official SFHo/FRDM v1.03 table hashes are inherited from the C1 provenance JSON.

C2 consumes the already-validated C1 output. It does not repeat the EOS interpolation and does not refit the profile.

## 2. Chemical-potential convention

The Hempel-to-Fiorillo mapping is
\[
U_N=m_N^*-m_N+\Sigma_{V,N}^{\rm tot},
\qquad
\mu_{N,F}^*=\mu_N^{\rm nonrel}.
\]
Thus the combination entering the Fermi function is
\[
\nu_N=\mu_N^{\rm nonrel}-U_N.
\]
With
\[
K_N(p)=\sqrt{p^2+m_N^{*2}}-m_N^*,
\]
the occupation is
\[
f_N(p,r)=\frac{1}{\exp[(K_N(p)-\nu_N(r))/T(r)]+1}.
\]

Including the two spin states,
\[
n_N'(r)=\frac{1}{\pi^2(\hbar c)^3}
\int_0^\infty dp\,p^2 f_N(p,r).
\]
This is the density per available nucleon volume. The total-volume density is
\[
n_N(r)=\xi_{\rm SPP}(r)n_N'(r),
\]
and the EOS target is
\[
n_N^{\rm EOS}(r)=X_N^{\rm EOS}(r)n_B(r).
\]

The primary calculation uses the tabulated EOS chemical potentials directly. A separate density-matched \(\nu_N\) is solved only as a diagnostic; it is never substituted into the primary occupation.

## 3. Full-radial density closure

Define
\[
\delta_N(r)=\frac{\xi_{\rm SPP}(r)n_N'(r)}
{X_N^{\rm EOS}(r)n_B(r)}-1.
\]

| Quantity | Neutron | Proton |
|---|---:|---:|
| RMS relative residual | 0.1126% | 0.3010% |
| Maximum absolute relative residual | 0.2154% | 0.7630% |
| Radius of maximum residual | 15.15 km | 14.85 km |
| Maximum absolute density residual | \(4.0120\times10^{-4}\) fm\(^{-3}\) | \(1.4795\times10^{-4}\) fm\(^{-3}\) |

Both species close to better than 1% at every radial point. The largest relative proton residual occurs in the outer region where the free-proton abundance is small; at 14.85 km its absolute residual is approximately \(9.53\times10^{-6}\) fm\(^{-3}\).

The C1 composition closure and filling-factor closure remain separate checks. C2 does not identify \(n_B\) with \(n_n^{\rm free}+n_p^{\rm free}\); the cluster baryon density remains explicit.

## 4. Chemical-potential and static-factor sensitivity

The maximum shifts needed to force the local density integral to the EOS target are:

| Diagnostic | Neutron | Proton |
|---|---:|---:|
| Maximum \(|\Delta\nu_N|\) | 0.1166 MeV | 0.1832 MeV |
| Radius | 1.45 km | 8.80 km |
| Maximum \(|\Delta F_{NN}^{\rm deg}|\) | \(4.06\times10^{-4}\) | \(4.45\times10^{-4}\) |
| Radius of maximum factor change | 15.15 km | 7.70 km |

The density-matched distribution is a sensitivity diagnostic only. The primary results retain the EOS-tabulated \(\mu_N^{\rm nonrel}\), \(U_N\), and \(m_N^*\).

The direct local static factors span
\[
0.2399\le F_{nn}^{\rm deg}(r)\le0.7342,
\qquad
0.4585\le F_{pp}^{\rm deg}(r)\le0.9853.
\]
These are radial values at one snapshot, not the \(T^3\)- or \(\rho T^{5/2}\)-weighted space-time averages in Fiorillo et al. Table 1.

## 5. Numerical convergence and acceptance

Gauss-Legendre momentum integration was evaluated at 512, 1024, and 2048 nodes, with a kinetic-energy tail of \(45T\). Across all 301 radii and both species, the maximum 2048-versus-512 relative density change and absolute \(F^{\rm deg}\) change are both below \(10^{-14}\).

C2 acceptance criteria:
- all 301 physical states and the 0.05-km radial grid are present;
- local density residuals are below 1% for both species;
- density-matched chemical-potential shifts are below 0.12 MeV (neutrons) and 0.20 MeV (protons);
- the corresponding static-factor change is below \(5\times10^{-4}\);
- 2048-versus-512 quadrature differences are below \(10^{-10}\).

**Overall C2 status: PASS**, with the sub-percent interpolation closure explicitly retained in the machine-readable output.

## 6. Scope boundary and next stage

This is a local occupation and density-closure calculation. It does not calculate a dynamic \(W_N^{\mu\nu}(q_0,q)\), a mass-time weighted core average, B.2 opacity, radial transport, luminosity, the pure-vector Fig. 7 benchmark, or an axial cooling curve.

The next step is C3: independently verify
\[
F_{NN}^{\rm deg}
=\frac{\int dp\,p^2 f_N(1-f_N)}
{\int dp\,p^2 f_N}
=\frac{T}{n_N'}\left.\frac{\partial n_N'}{\partial\nu_N}\right|_{T,m_N^*},
\]
at all radial points, before moving to the dynamic response in C4.
