# P1-IIIe-C: Caputo SFHo-18.8 profile mapped onto the official SFHo EOS

Date: 2026-11-11  
Repository: axial-vector-review-response  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Scope and status

This is the first local profile-to-EOS mapping at ten audited radii,
\(r=1,5,8,9,10,11,12,13,14,15\) km, for the Caputo SFHo-18.8 snapshot at
\(t_{\rm pb}=1\) s. It is deliberately a **key-radius closure diagnostic**,
not a full radial profile and not a time-integrated supernova calculation.

The primary calculation was executed locally against the authenticated
SFHo/FRDM v1.03 tables. The numerical integration is converged. The next
independent step is to add the same calculation to the EOS GitHub Actions
workflow and then extend it to the full 0.05-km Caputo composition profile.

No B.2 opacity, vector Fig. 7 benchmark, escape probability, or axial cooling
curve is changed by this calculation.

## 2. Profile inputs and the EOS coordinate

The profile combines:

- \(T(r)\) from Caputo Fig. 1 upper panel, linearly interpolated from
  T_caputo_vertices.csv;
- \(n_B(r)\) from the Caputo Fig. 1 lower-panel density normalization;
- \(Y_n(r)\), free \(Y_p(r)\), and \(Y_e(r)+Y_\mu(r)\) from the Caputo Fig. 4
  composition curves;
- \(X_{\rm cluster}=1-Y_n-Y_p\), and
  \(Y_{Q,\rm cluster}=Y_e+Y_\mu-Y_p\).

The Caputo normalization is \(n_0=0.181\ {\rm fm}^{-3}\), so
\(n_B=(n_B/n_0)n_0\).

The important coordinate choice is

\[
\boxed{Y_p^{\rm EOS}=Y_p^{\rm tot}=Y_e+Y_\mu,}
\]

not the free-proton abundance \(Y_p\). The SFHo EOS grid is indexed by the
**total** proton/charge fraction. In a charge-neutral muonic medium this is
\(Y_e+Y_\mu\); the free-proton fraction is smaller once nuclear clusters carry
positive charge. The EOS free-proton mass fraction \(X_p\) is then compared
with Caputo's free \(Y_p\).

## 3. EOS interpolation and occupation calculation

The official table files are checked by SHA-256 before use:

| Table | SHA-256 |
|---|---|
| sfho_frdm_eos_v1.03.bin | f1ea9c3e04502ca35d7fc64facce575f8553293085ea26e07732389b80d32cb4 |
| sfho_frdm_spp_v1.03.tab | 118bd3c986283d958fab88a8e81fe49b64ca3b5137ff4bcdc05f97064cc1219e |
| sfho_frdm_comp_v1.03.bin | 0dafcd272ff8b8f4b1ba4c05210ea8020dd9a92820b6b0b54165faead4871da7 |

The interpolation is trilinear in
\((\log_{10}T,\;Y_p^{\rm tot},\;\log_{10}n_B)\), using only the 308 physical
density rows. bounds_error=True is used: no radial point is extrapolated
outside the table.

At each radius the SPP table supplies \(m_N^*\), \(\Sigma_{V,N}^{\rm tot}\),
and \(\xi\), while the extended EOS supplies
\(\mu_N^{\rm nonrel}\) and the composition fractions. The Hempel mapping is

\[
U_N=m_N^*-m_N+\Sigma_{V,N}^{\rm tot},
\qquad
\mu_N^*=\mu_N^{\rm nonrel},
\]

\[
f_N(p)=
\left[
\exp\!\left(
\frac{U_N+\sqrt{p^2+m_N^{*2}}-m_N^*-\mu_N^*}{T}
\right)+1
\right]^{-1}.
\]

The density per total volume is reconstructed as

\[
n_N=\xi n_N',
\qquad
n_N'=\frac{1}{\pi^2(\hbar c)^3}\int_0^\infty dp\,p^2f_N(p),
\]

and the static degeneracy factor is

\[
F_{NN}^{\rm deg}=
\frac{\int_0^\infty dp\,p^2 f_N(p)[1-f_N(p)]}
     {\int_0^\infty dp\,p^2 f_N(p)}.
\]

The vacuum-mass comparison is made at the same \(T\), free-nucleon density,
and \(\xi\), with the ideal-gas chemical potential re-solved to reproduce that
density. It therefore isolates the effect of \(m_N^*\) on this static factor.

## 4. Composition and density closure

The interpolated SFHo table composition agrees with the Caputo free-nucleon
abundances exceptionally well:

| Closure quantity | RMS absolute difference | Maximum absolute difference |
|---|---:|---:|
| \(X_n^{\rm EOS}-Y_n^{\rm Caputo}\) | \(9.26\times10^{-6}\) | \(2.02\times10^{-5}\) |
| \(X_p^{\rm EOS}-Y_p^{\rm Caputo}\) | \(8.21\times10^{-6}\) | \(1.67\times10^{-5}\) |
| \(X_{\rm cluster}^{\rm EOS}-X_{\rm cluster}^{\rm Caputo}\) | \(1.56\times10^{-5}\) | \(2.67\times10^{-5}\) |
| Cluster charge fraction | \(8.21\times10^{-6}\) | \(1.67\times10^{-5}\) |

The SPP filling factor also agrees with the value inferred from Caputo's free
nucleon and total baryon densities:

\[
{\rm RMS}\,|\xi_{\rm SPP}-\xi_{\rm Caputo}|=8.06\times10^{-5},
\qquad
\max|\Delta\xi|=1.74\times10^{-4}.
\]

Using the interpolated EOS chemical potentials directly in the Fermi integrals
gives the following density closure against the Caputo free-nucleon targets:

| Species | RMS relative residual | Maximum absolute relative residual |
|---|---:|---:|
| neutron | 0.116% | 0.177% |
| proton | 0.349% | 0.603% |

The chemical-potential shift required to reproduce the target density exactly
is at most 0.113 MeV for neutrons and 0.176 MeV for protons. Re-solving the
chemical potential at fixed \(T,m_N^*,\xi,n_N\) changes \(F_{nn}^{\rm deg}\)
and \(F_{pp}^{\rm deg}\) by at most \(3.5\times10^{-4}\) and
\(3.6\times10^{-4}\), respectively.

The 2048-point quadrature is converged against 512 points:
the maximum relative change in density is \(1.7\times10^{-13}\), and the
maximum absolute change in \(F_{NN}^{\rm deg}\) is \(4.4\times10^{-16}\).

### Why \(Y_p^{\rm tot}\), not free \(Y_p\), is essential

A deliberate wrong-coordinate test interpolates the EOS at the free-proton
abundance \(Y_p\). At the ten radii this gives RMS absolute composition errors
of 0.0296 in \(X_n\), 0.0133 in \(X_p\), and 0.0175 in \(X_{\rm cluster}\);
the maximum errors reach 0.0602, 0.0206, and 0.0426. The total charge
fraction \(Y_e+Y_\mu\) is therefore the required EOS coordinate.

## 5. Local degeneracy factors and ideal-gas comparison

Across the ten radii,

\[
0.242\le F_{nn}^{\rm deg}\le0.731,\qquad
0.460\le F_{pp}^{\rm deg}\le0.983.
\]

The interpolated effective masses rise outward from approximately
543 MeV to 895 MeV for neutrons and 542 MeV to 893 MeV for protons.

Representative values are:

| \(r\) [km] | \(X_{\rm cluster}\) | \(F_{nn}^{\rm EOS}\) | \(F_{nn}^{m_N}\) | \(F_{pp}^{\rm EOS}\) | \(F_{pp}^{m_p}\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.00% | 0.2416 | 0.3530 | 0.4605 | 0.6277 |
| 5 | 0.00% | 0.3608 | 0.4826 | 0.6285 | 0.7544 |
| 8 | 0.00% | 0.6522 | 0.7289 | 0.8740 | 0.9109 |
| 10 | 2.20% | 0.6892 | 0.7444 | 0.9168 | 0.9363 |
| 12 | 5.68% | 0.7053 | 0.7424 | 0.9443 | 0.9536 |
| 15 | 8.85% | 0.7312 | 0.7444 | 0.9831 | 0.9842 |

Here \(F^{m_N}\) denotes the vacuum-mass ideal-gas value at the same local
temperature and free-nucleon density. Relative to this benchmark, the EOS
effective masses reduce the static factor by 31.6% to 1.8% for neutrons and
26.6% to 0.11% for protons, with the largest effect in the inner core.

This is a **static local degeneracy diagnostic**. It is not a calculation of
the full dynamic \(nn,np,pp\) response, and it must not be applied as a
single global rescaling of the semi-Compton or transport kernels.

## 6. Interpretation and limitations

1. The Caputo SFHo-18.8 composition at these key radii is highly compatible
   with the official Hempel SFHo/FRDM v1.03 table when the correct total
   charge fraction is used as the EOS coordinate.
2. The local EOS density closure is sub-percent and the quadrature error is
   negligible compared with the figure-level profile uncertainty.
3. The EOS effective-mass correction is radially dependent; a vacuum-mass
   ideal-gas approximation is most inaccurate in the inner core.
4. These are ten points from the \(t_{\rm pb}=1\) s published-figure snapshot.
   They are not raw Garching profile data and do not provide the
   space-time weighting needed to reproduce Fiorillo Table 1 global
   \(F_{NN}^{\rm deg}\) averages.
5. No opacity, luminosity, escape probability, vector Fig. 7 benchmark, or
   axial cooling curve is changed.

## 7. Next step

Extend the same mapping to the full 0.05-km Caputo composition profile, using
the archived arXiv source package to extract the full Fig. 4 abundance paths.
Then inspect \(F_{nn}^{\rm deg}(r)\), \(F_{pp}^{\rm deg}(r)\), \(m_N^*(r)\),
\(\xi(r)\), and the cluster fraction across the 8--15 km production region.
Only after that profile-level closure should the local EOS factors be supplied
to an independent dynamic-response calculation. Do not infer a global
mass-time average from the ten key radii.
