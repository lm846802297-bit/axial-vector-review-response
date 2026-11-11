# P1-IIIe-C4B1: effective-mass quasiparticle weak tensor

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Purpose

C4-B1 specifies and tests the weak-current tensor algebra when the local SFHo quasiparticle dispersion uses \(m_N^*(r)\), while the weak form factors retain their vacuum nucleon normalization. This is the algebraic bridge between C4-A's EOS-consistent scalar response and the full moving-nucleon collision kernel.

This is a minimal local quasiparticle embedding. It is not a full in-medium weak vertex, RPA response, or NN-correlated response.

## 2. Kinematic and vertex conventions

At fixed radius and species, define
\[
p^{*\mu}=(E_p^*,\mathbf p),\qquad
E_p^*=\sqrt{p^2+m_N^{*2}(r)},
\]
\[
p'^{*\mu}=(E_{p'}^*,\mathbf p+\mathbf q),\qquad
E_{p'}^*=\sqrt{|\mathbf p+\mathbf q|^2+m_N^{*2}(r)},
\]
\[
q^\mu=p'^{*\mu}-p^{*\mu}=(q_0,\mathbf q),\qquad Q^2=|\mathbf q|^2-q_0^2.
\]
Both quasiparticle legs use the same local \(m_N^*(r)\). The momentum-independent vector potential cancels from \(q_0\), while \(\nu_N(r)=\mu_N^{\rm nonrel}(r)-U_N(r)\) remains in the initial and final Fermi factors.

The minimal vertex is
\[
\Gamma_N^\mu(q)=
F_1^N(Q^2)\gamma^\mu
+i\frac{F_2^N(Q^2)}{2M_N}\sigma^{\mu\alpha}q_\alpha
-G_A^N(Q^2)\gamma^\mu\gamma^5.
\]
The distinction is deliberate:
- quasiparticle spinors and on-shell energies use \(m_N^*(r)\);
- vacuum form-factor arguments, dipole scales, and the weak-magnetism denominator use the physical vacuum mass \(M_N\).

The spin-averaged tensor is
\[
H_N^{\mu\nu}=
\frac12\operatorname{Tr}\left[
(\slashed p'^*+m_N^*)\Gamma_N^\mu
(\slashed p^*+m_N^*)\overline\Gamma_N^\nu
\right].
\]
The factor \(1/2\) averages the initial nucleon spin. The medium phase-space integral separately accounts for the two occupied spin states; no extra spin factor is to be inserted into this trace.

## 3. Why the vector Ward identity remains valid

For the vector vertex
\[
\Gamma_V^\mu=F_1\gamma^\mu+
i\frac{F_2}{2M_N}\sigma^{\mu\alpha}q_\alpha,
\]
one has
\[
q_\mu\Gamma_V^\mu=F_1\slashed q,
\]
because \(q_\mu\sigma^{\mu\alpha}q_\alpha=0\). Between equal-mass on-shell quasiparticle spinors,
\[
\overline u(p'^*)\slashed q\,u(p^*)
=\overline u(p'^*)(\slashed p'^*-\slashed p^*)u(p^*)=0.
\]
Thus the local vector Ward identity is compatible with \(m_N^*\ne M_N\), provided both legs use the same local effective mass and the vertex uses the stated vacuum form factors.

This does not imply that all in-medium vertex corrections vanish. It only establishes the Ward identity for the minimal local quasiparticle prescription being tested.

## 4. Numerical checks

The algebra audit covers:
- 288 on-shell quasiparticle configurations from four selected radii, two species, four momentum transfers, three initial momenta, and three initial momentum directions;
- the \(m_N^*=M_N\) limit against the existing P1-IIIb stationary Dirac tensor at 40 species/energy/angle points;
- eight neutrino/antineutrino contractions checking that VV and AA pieces are unchanged while the VA interference reverses sign.

Required checks:
1. \(q_\mu H_{VV}^{\mu\nu}=0\);
2. \(q_\mu H_{VA}^{\mu\nu}=0\) and \(H_{AV}^{\mu\nu}q_\nu=0\), with the vector current on the contracted index;
3. Hermiticity of \(H_{VV}\), \(H_{AA}\), and the full tensor;
4. exact recovery of the existing P1-IIIb tensor when \(m_N^*=M_N\);
5. the expected neutrino/antineutrino VA sign structure.

### 4.1 Numerical results and independent CI

The effective-mass Ward scan contains 288 on-shell configurations; the vacuum-mass recovery contains 40 stationary-target cases; the neutrino/antineutrino interference check contains eight EOS-state cases.

| Diagnostic | Maximum residual |
|---|---:|
| Vector Ward identity | (3.01	imes10^{-15}) |
| Tensor hermiticity | (2.42	imes10^{-16}) |
| (m_N^*=M_N) recovery of P1-IIIb | (6.61	imes10^{-16}) |
| Neutrino/antineutrino VA sign structure | (2.61	imes10^{-16}) |

All are far below their acceptance thresholds. In particular, the vacuum-mass limit reproduces the existing P1-IIIb tensor component by component, while the mixed-mass quasiparticle tensor preserves the vector Ward identity.

**C4-B1 status: PASS.** Independent GitHub Actions workflow run #5:
https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43001802164

- 5/5 unit tests passed.
- 288 effective-mass Ward cases passed.
- 40 vacuum-mass recovery cases passed.
- Eight VA sign-structure cases passed.
- The numerical CSV outputs are retained in the workflow artifact `c4b1-effective-mass-weak-tensor` (artifact ID 13846825852); the summary JSON is also committed under `outputs/`.

## 5. Scope boundary and next stage

C4-B1 does not yet integrate over the initial Fermi sea, compute \(d\Gamma/(dE'd\Omega')\), or produce a cross section/opacity. It does not modify the existing P1-IIIb code or the production B.2 calculation.

After the algebraic gate passes, C4-B2 will implement the EOS-dependent moving-nucleon collision kernel:
- \(m_N^*(r)\) in the on-shell kinematics, spinors, and exact \(p_{\min}\);
- \(\nu_N(r)\), \(T(r)\) in both initial and final Fermi factors;
- physical \(M_N\) in vacuum form factors and weak-magnetism normalization;
- \(n_N'(r)\) for per-target normalization, with \(\xi_{\rm SPP}(r)\) restored only when converting to a total-volume opacity.

The mandatory C4-B2 limits are \(m_N^*\to M_N\) recovery of P1-IIIb, the cold/dilute Horowitz limit, and local detailed balance. No B.2 or luminosity calculation is allowed before those gates pass.
