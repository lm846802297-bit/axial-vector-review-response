# Moving-muon semi-Compton collision integral

Date: 2026-11-07  
Status: phase-space reduction and normalization specification; production implementation is not yet validated.

## 1. Scope

This is the next microscopic calculation after the dimuon thermal-emissivity integral passed its first numerical gate. It evaluates the full in-medium \(2\leftrightarrow2\) process
\[
\mu^Q(p)+\gamma(q)\rightleftarrows \mu^Q(p')+A'(k),
\qquad Q=\mu^-,\mu^+,
\]
for fixed on-shell mediator momentum \(k^\mu=(\omega,0,0,K)\), \(K=\sqrt{\omega^2-m_{A'}^2}\).

The implementation must:
- integrate over the thermal momentum of the initial muon rather than replacing it by a stationary target times an effective density;
- retain the exact two-body recoil kinematics;
- sum both charge species explicitly, with chemical potentials \(+\mu_\mu\) and \(-\mu_\mu\);
- keep the three physical \(A'\) polarizations separate;
- sum the two physical photon polarizations;
- retain vector--axial interference at amplitude level;
- calculate production and inverse absorption independently.

This is a local microscopic-rate calculation only. It does not run stellar transport, alter the published-vector comparison lane, or generate an axial cooling curve.

## 2. Collision terms before phase-space reduction

Use \(d\Pi_a=d^3p_a/[(2\pi)^3 2E_a]\). For a fixed mediator polarization \(h\), the absorption rate is
\[
\Gamma^{\rm abs}_{h}(k)=
\frac{2}{2\omega}\sum_{Q=\pm}
\int d\Pi_p\,d\Pi_q\,d\Pi_{p'}
(2\pi)^4\delta^{(4)}(p+k-q-p')
\overline{|\mathcal M^{Q}_{h}|^2}
f_Q(E_p)[1-f_Q(E_{p'})][1+f_B(q)].
\]
The factor 2 is the initial-muon spin degeneracy; the matrix element is averaged over the initial muon spin and summed over the final muon spin and the two physical photon polarizations. There is no average over the fixed mediator polarization \(h\).

The production rate is evaluated independently:
\[
\Gamma^{\rm prod}_{h}(k)=
\frac{2}{2\omega}\sum_{Q=\pm}
\int d\Pi_p\,d\Pi_q\,d\Pi_{p'}
(2\pi)^4\delta^{(4)}(p+k-q-p')
\overline{|\mathcal M^{Q}_{h}|^2}
f_Q(E_{p'})f_B(q)[1-f_Q(E_p)].
\]
Here \(f_Q(E)=[e^{(E-\mu_Q)/T}+1]^{-1}\), with
\[
\mu_{\mu^-}=+\mu_\mu,\qquad
\mu_{\mu^+}=-\mu_\mu,\qquad
f_B(q)=\frac{1}{e^{q/T}-1}.
\]
Energy conservation \(E_p+\omega=E_{p'}+q\) gives, pointwise in phase space and separately for each charge and polarization,
\[
\frac{F_{\rm abs}}{F_{\rm prod}}=e^{\omega/T},
\qquad
\Gamma^{\rm abs}_{h}(k)=e^{\omega/T}\Gamma^{\rm prod}_{h}(k).
\]
The numerical implementation must nevertheless integrate both statistical factors independently; it must not construct one rate from the other by multiplying by a Boltzmann factor.

## 3. Exact reduction of the final-state delta function

Choose the mediator momentum along \(+z\). Let the initial muon momentum be
\[
p^\mu=(E_p,\mathbf p),\qquad E_p=\sqrt{p^2+m_\mu^2},
\]
and write the outgoing photon as \(q^\mu=(q,q\hat{\mathbf n})\). Momentum conservation fixes
\[
p'^\mu=p^\mu+k^\mu-q^\mu.
\]
Define
\[
A=E_p+\omega,\qquad
\mathbf P=\mathbf p+\mathbf k,\qquad
D=A-\mathbf P\cdot\hat{\mathbf n}.
\]
The on-shell condition \(p'^2=m_\mu^2\) gives one positive photon-energy root,
\[
q_\star=
\frac{A^2-|\mathbf P|^2-m_\mu^2}{2D}
=
\frac{m_{A'}^2+2(E_p\omega-\mathbf p\cdot\mathbf k)}{2D}.
\]
For future-directed on-shell \(p,k\), \(D>0\) and the physical root obeys \(0<q_\star<A\). The final muon energy is \(E_{p'}=A-q_\star\).

The energy-delta Jacobian is
\[
\left|\frac{\partial(E_p+\omega-q-E_{p'})}{\partial q}\right|_{q_\star}
=\frac{D}{E_{p'}}.
\]
It cancels the final-state \(1/(2E_{p'})\) factor down to \(q_\star/D\) after the photon radial integral.

Rotational invariance about \(\mathbf k\) allows the initial-muon azimuth to be fixed to zero and contributes a factor \(2\pi\). Let \(c_p=\cos\theta_p\), \(c_q=\cos\theta_q\), and let \(\phi\) be the photon azimuth relative to the plane containing \(\mathbf p\) and \(\mathbf k\). Then
\[
\boxed{
\Gamma^{\rm abs/prod}_{h}(\omega)=
\frac{2}{8\omega(2\pi)^4}
\sum_{Q=\pm}
\int_0^\infty dp\,\frac{p^2}{E_p}
\int_{-1}^{1}dc_p
\int_{-1}^{1}dc_q
\int_0^{2\pi}d\phi\,
\frac{q_\star}{D}
\overline{|\mathcal M^{Q}_{h}|^2}
F^{\rm abs/prod}_{Q}
}
\]
where \(F_Q^{\rm abs}=f_Q(E_p)[1-f_Q(E_{p'})][1+f_B(q_\star)]\) and \(F_Q^{\rm prod}=f_Q(E_{p'})f_B(q_\star)[1-f_Q(E_p)]\). The leading factor 2 is the muon spin degeneracy. This normalization must be retained exactly; no additional spin or photon factor is inserted.

## 4. Matrix element and current conventions

For absorption, the two tree diagrams are
\[
\mathcal M^{Q}_{h\lambda}=
\bar u(p')
\left[
\Gamma^{Q}_{A,h}\,
\frac{\slashed p+\slashed k+m_\mu}{m_{A'}^2+2p\cdot k}\,
\slashed\epsilon_{\gamma,\lambda}
+
\slashed\epsilon_{\gamma,\lambda}\,
\frac{\slashed p-\slashed q+m_\mu}{-2p\cdot q}\,
\Gamma^{Q}_{A,h}
\right]u(p)
\]
for the muon-particle line. The physical mediator polarization basis is \(L,+,-\); the photon basis is any two orthonormal transverse vectors to \(\hat{\mathbf n}\). The spin-averaged trace sums over the two photon polarizations and final muon spin.

The UV convention is
\[
\mathcal L_{\mu A'}=
A'_\alpha\bar\mu\gamma^\alpha
(g_V^\mu+g_A^\mu\gamma^5)\mu,
\qquad
g_V^\mu=g_X\sin^2\theta_{\mu R},
\qquad
g_A^\mu=-g_X\cos^2\theta_{\mu R}.
\]
The existing rates.py pure-axial basis is \(\gamma^\alpha(-\gamma^5)\), so for a \(\mu^-\) target the mixed amplitude is
\[
\mathcal M_{\mu^-}=g_V^\mu\mathcal M_V-g_A^\mu\mathcal M_{A,\,-\gamma^5}.
\]

### Charge-conjugate sign

The \(\mu^+\) contribution must not be obtained by simply copying the \(\mu^-\) mixed-current rate. Charge conjugation gives
\[
C^{-1}(\gamma^\alpha)^T C=-\gamma^\alpha,
\qquad
C^{-1}(\gamma^\alpha\gamma^5)^T C=
+\gamma^\alpha\gamma^5.
\]
The photon vertex is vector. Consequently, after dropping an overall unobservable sign, the relative vector--axial interference changes sign for an antimuon target:
\[
|\mathcal M_{\mu^+}(g_V^\mu,g_A^\mu)|^2
=
|\mathcal M_{\mu^-}(g_V^\mu,-g_A^\mu)|^2
\]
at matched kinematics. Pure-vector and pure-axial terms are unchanged. This relation is to be encoded and independently regression-tested; the two charge distributions remain distinct through \(\mu_Q=\pm\mu_\mu\).

For the vector longitudinal amplitude, the Ward-equivalent polarization shift already used in rates.py may be applied to avoid cancellation at \(m_{A'}/\omega\ll1\). The axial longitudinal amplitude must retain the physical polarization. The photon Ward identity is tested by replacing \(\epsilon_\gamma\) with \(q\).

## 5. Independent stationary-target normalization check

In the limit \(\mathbf p\to0\),
\[
q_\star=
\frac{m_{A'}^2+2m_\mu\omega}
{2(m_\mu+\omega-Kc_q)},
\]
which is exactly the recoil photon energy in the existing stationary-muon kernel. The reduced phase-space prefactor then gives
\[
\frac{q_\star}{64\pi^2m_\mu\omega(m_\mu+\omega-Kc_q)}
\,d\Omega_q\,\overline{|\mathcal M_h|^2},
\]
the same differential \(v_{\rm rel}\sigma\) normalization as rates.compton_kernels for one target muon. This is a mandatory pointwise endpoint test, not an adjustable normalization.

In the dilute, nonrelativistic thermal limit, the integrated moving-muon absorption rate divided by the explicit two-charge, two-spin target density must approach the stationary-target compton_absorption result. The positive-muon fraction is retained in the new calculation; the literal Blinov Eq. (33) single-negative-muon prescription remains a separate literature-comparison convention.

## 6. Numerical integration plan

- Integrate the initial-muon radial momentum with a composite Gauss--Legendre rule. In a degenerate gas, split around \(p_F=\sqrt{\mu_Q^2-m_\mu^2}\) to resolve the Fermi surface; in a nondegenerate gas, use a scale set by \(\sqrt{m_\mu T}\).
- Integrate \(c_p,c_q\) with Gauss--Legendre nodes and \(\phi\) with a periodic trapezoidal rule.
- Vectorize the Dirac traces in bounded chunks; do not materialize an unbounded 4D tensor.
- Use overflow-safe Fermi and Bose functions. The factor \(q_\star[1+f_B(q_\star)]\) must be evaluated stably as \(q_\star/[1-e^{-q_\star/T}]\) where appropriate.
- Integrate the forward and reverse statistical factors independently on identical kinematic nodes.
- Record radial, angular, azimuthal, and chunking orders, profile-independent input parameters, and SHA-256 fingerprints in each output.

## 7. Required tests before using the rates

1. The \(p=0\) moving-matrix-element endpoint agrees with the existing pure-vector and pure-axial rates.compton_matrix_elements for all three mediator polarizations and photon-angle points.
2. The photon Ward identity holds for arbitrary moving-muon kinematics, each mediator polarization, and both charge-conjugate signs.
3. The vector longitudinal Ward shift agrees with the physical polarization result in the conserved-current limit.
4. The \(\mu^+\) mixed-current trace equals the \(\mu^-\) trace with \(g_A\to-g_A\); pure endpoints are unchanged.
5. At \(\mu_\mu=0\), the charge-summed vector--axial interference cancels; at nonzero \(\mu_\mu\), the charge-weighted interference is retained.
6. Production and absorption independently satisfy mode-resolved detailed balance to the numerical integration tolerance.
7. The dilute/nonrelativistic limit approaches the existing stationary-target kernel with the explicit spin and charge multiplicities.
8. Radial and angular quadrature convergence is demonstrated at representative core and outer-profile thermodynamic points.
9. The pure-vector local thermal rate is compared with the literal Blinov B.13/B.14 conventions; the positive-muon and charge-conjugate corrections are reported separately rather than silently absorbed into a normalization.

Only after these tests pass may the local rates be tabulated over the reconstructed SFHo-18.8 profile. The pure-vector full Fig. 7 reproduction gate remains separate and mandatory before any final astrophysical exclusion claim.
