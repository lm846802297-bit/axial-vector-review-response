# P1-IIIe-C3A: full-radial degeneracy-factor derivative identity

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Purpose and scope

C3-A independently verifies the local static identity between the blocked Fermi integral and the derivative of the nucleon density with respect to the effective chemical potential. It uses all 301 radial states from C1/C2, covering \(r=0.20\)--\(15.20\) km at \(\Delta r=0.05\) km.

The background is the Caputo SFHo-18.8 published-figure snapshot at \(t_{\rm pb}=1\) s. This is not a raw time-dependent Garching simulation profile and does not provide a space-time weighted core average.

## 2. Identity and differentiation prescription

For
\[
f_N(p)=\frac{1}{\exp[(K_N(p)-\nu_N)/T]+1},
\qquad
K_N(p)=\sqrt{p^2+m_N^{*2}}-m_N^*,
\]
one has
\[
\left.\frac{\partial f_N}{\partial\nu_N}\right|_{T,m_N^*}
=\frac{1}{T}f_N(1-f_N).
\]
Consequently,
\[
\left.\frac{\partial n_N'}{\partial\nu_N}\right|_{T,m_N^*}
=\frac{1}{\pi^2(\hbar c)^3T}
\int_0^\infty dp\,p^2f_N(1-f_N),
\]
and hence
\[
F_{NN}^{\rm deg}
=\frac{\int dp\,p^2f_N(1-f_N)}{\int dp\,p^2f_N}
=\frac{T}{n_N'}\left.\frac{\partial n_N'}{\partial\nu_N}\right|_{T,m_N^*}.
\]

The numerical derivative is a central finite difference,
\[
F_{NN,\rm FD}^{\rm deg}
=\frac{T}{n_N'(\nu)}
\frac{n_N'(\nu+h)-n_N'(\nu-h)}{2h},
\qquad \frac{h}{T}=3.0\times10^{-5}.
\]
At each radius, \(T\), \(m_N^*\), \(U_N\), and \(\xi_{\rm SPP}\) are held fixed. Only \(\mu_N^{\rm nonrel}\) is shifted by \(\pm h\), so \(\nu_N=\mu_N^{\rm nonrel}-U_N\) changes by \(\pm h\). The same 2048-point Gauss-Legendre integration and \(45T\) kinetic-energy tail are used for the density integrals.

The filling factor does not alter the identity: at fixed \(\xi_{\rm SPP}\), both the total-volume density \(\xi_{\rm SPP}n_N'\) and its \(\nu_N\) derivative acquire the same multiplicative factor, which cancels in \(T n^{-1}\partial n/\partial\nu_N\).

## 3. Results over all 301 radii

| Diagnostic | Neutrons | Protons |
|---|---:|---:|
| \(F_{NN}^{\rm deg}\) range | 0.239891--0.734191 | 0.458509--0.985272 |
| RMS relative identity residual | \(7.82\times10^{-11}\) | \(8.80\times10^{-11}\) |
| Maximum absolute relative residual | \(3.20\times10^{-10}\) | \(1.98\times10^{-10}\) |
| Radius of maximum relative residual | 0.45 km | 14.40 km |
| Maximum absolute difference | \(9.09\times10^{-11}\) | \(1.93\times10^{-10}\) |

The direct integral was also recomputed and compared with the archived C2 values. The maximum absolute discrepancy is \(4.44\times10^{-16}\) for neutrons and \(6.66\times10^{-16}\) for protons, consistent with floating-point roundoff.

## 4. Acceptance

All criteria pass:
- 301 aligned radial points and the uniform 0.05-km grid;
- direct-integral versus density-derivative relative discrepancy below \(10^{-8}\) for both species;
- direct-integral reproduction of the archived C2 factors within \(5\times10^{-12}\);
- all local factors lie strictly between zero and one.

**C3-A status: PASS.**

The finite-difference step used here is a fixed, preselected numerical setting. A dedicated multi-step stability and truncation-versus-roundoff study is kept separate as C3-B.

## 5. Scope boundary and next stage

C3-A verifies the local thermodynamic identity only. It does not calculate a dynamic \(W_N^{\mu\nu}(q_0,q;r)\), a time-space weighted core average, B.2 opacity, radial transport, luminosity, the pure-vector Fig. 7 benchmark, or an axial cooling curve.

Next: C3-B, scan the finite-difference step over the full radial profile and identify a stable plateau, explicitly separating central-difference truncation error from floating-point cancellation. Only after that should C3-C investigate the radial dependence of the local static factors.
