# P1-IIIe-C4A: EOS-effective-mass dynamic scalar response

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Purpose and scope

C4-A connects the validated C2/C3 local EOS occupations to a finite-\(q_0,q\) dynamic nucleon response. It deliberately begins with the scalar phase-space response, before inserting the full vector/axial weak tensor. The first validation targets are dynamic/static sum-rule closure, detailed balance, and the \(q\to0\) susceptibility limit.

The calculation uses four representative radii from the same \(t_{\rm pb}=1\) s Caputo SFHo-18.8 published-figure snapshot:
\[
r=0.20,\ 5.00,\ 10.00,\ 15.20\ {\rm km},
\]
for both neutrons and protons, and
\[
q=1,\ 3,\ 10,\ 30,\ 100,\ 200,\ 500\ {\rm MeV}.
\]
This is a local response validation, not a radial opacity or luminosity calculation.

## 2. EOS-to-dynamic-response matching

At fixed radius and species, use the C2 local quasiparticle state:
\[
E_N^*(p;r)=\sqrt{p^2+m_N^{*2}(r)},\qquad
K_N(p;r)=E_N^*(p;r)-m_N^*(r),
\]
\[
f_N(p;r)=
\left[
\exp\left(\frac{K_N(p;r)-\nu_N(r)}{T(r)}\right)+1
\right]^{-1},
\qquad
\nu_N(r)=\mu_N^{\rm nonrel}(r)-U_N(r).
\]

For elastic scattering on the same nucleon species, the local vector potential is momentum independent and cancels from the energy transfer:
\[
q_0=E_N^*(|\mathbf p+\mathbf q|;r)-E_N^*(p;r).
\]
The final-state occupation is therefore evaluated with the same \(m_N^*(r)\), \(T(r)\), and \(\nu_N(r)\) as the initial state.

With spin degeneracy two, the dynamic scalar response is
\[
S_N(q_0,q;r)=
2\int\frac{d^3p}{(2\pi)^3}
\,2\pi\delta(q_0+E_p^*-E_{p+q}^*)
f_N(p;r)[1-f_N(|\mathbf p+\mathbf q|;r)].
\]
The exact polar-angle reduction gives
\[
\boxed{
S_N(q_0,q;r)=
\frac{1}{\pi q}
\int_{p_{\min}}^\infty dp\,
p(E_p^*+q_0)f_i(1-f_f)
}
\]
for \(|q_0|<q\). Here \(p_{\min}\) is evaluated with the local effective mass \(m_N^*(r)\). The response has units of MeV\(^2\).

The constant \(U_N(r)\) is not added to \(q_0\): it cancels between the initial and final energies for the same species. It remains essential through \(\nu_N(r)\) in the Fermi occupations.

## 3. Independent validation identities

### 3.1 Dynamic/static sum rule

For every finite \(q\),
\[
\boxed{
\int_{-q}^{q}\frac{dq_0}{2\pi}S_N(q_0,q;r)
=
2\int\frac{d^3p}{(2\pi)^3}
f_N(p;r)[1-f_N(|\mathbf p+\mathbf q|;r)]
}.
\]
The left side is evaluated using a 240-node Gauss-Legendre \(q_0\) integral and a 600-node momentum integral. The right side is evaluated independently as a two-dimensional static \((p,\cos\theta)\) integral with 160 nodes in each variable.

### 3.2 Detailed balance

For the same local equilibrium state,
\[
\boxed{
S_N(-q_0,q;r)=e^{-q_0/T(r)}S_N(q_0,q;r)
}.
\]
The check samples \(q_0/T=\{0.1,0.5,1,2,4\}\), capped at \(q_0/q=0.5\) so both response directions remain numerically supported rather than testing exponentially tiny tails.

### 3.3 Static susceptibility limit

As \(q\to0\),
\[
\int\frac{dq_0}{2\pi}S_N(q_0,q;r)
\longrightarrow
\frac{1}{\pi^2}\int_0^\infty dp\,p^2f_N(1-f_N)
=n_N'(r)F_{NN}^{\rm deg}(r).
\]
The rightmost quantity is taken directly from C2. The \(q=1\) and \(3\) MeV static integrals test approach to this limit.

## 4. Numerical results

All 56 species-radius-\(q\) sum-rule checks pass.

| Diagnostic | Neutrons | Protons |
|---|---:|---:|
| Maximum dynamic/static sum-rule residual | \(2.0\times10^{-15}\) | \(2.2\times10^{-15}\) |
| Maximum detailed-balance residual | \(3.6\times10^{-15}\) | \(4.4\times10^{-15}\) |
| Maximum \(q=1\) MeV deviation from \(n'F^{\rm deg}\) | \(2.604\times10^{-5}\) | \(1.385\times10^{-5}\) |
| Maximum \(q=3\) MeV deviation from \(n'F^{\rm deg}\) | \(2.343\times10^{-4}\) | \(1.246\times10^{-4}\) |

The finite-\(q\) dynamic integral agrees with the independent static integral to near floating-point precision. The small-\(q\) static integral approaches the C2 susceptibility \(n'F^{\rm deg}\) with the expected finite-\(q\) correction.

## 5. Acceptance

C4-A acceptance:
- four radii, both species, and seven momentum transfers are included;
- 13,440 \(q_0\)-resolved response points are archived;
- all 56 dynamic/static sum-rule residuals are below \(10^{-8}\);
- detailed balance is below \(10^{-8}\);
- the \(q=1\) MeV static limit agrees with \(n'F^{\rm deg}\) within \(10^{-4}\);
- the \(q=3\) MeV static limit agrees within \(10^{-3}\);
- the direct \(q_0=0\) blocked integral reproduces the C2 value within \(5\times10^{-12}\);
- the response is nonnegative on the sampled kinematic domain.

**C4-A direct numerical status: PASS.** Independent Python CI is tracked separately.

## 6. Interpretation and scope boundary

C4-A establishes that the C2 EOS occupation can be inserted into a local finite-\(q_0,q\) scalar response without violating the dynamic/static sum rule or detailed balance. It also connects the C3 degeneracy factor to the \(q\to0\) limit of the dynamic response.

This is not yet the full weak-current tensor. In particular, it does not include the vector/axial Dirac trace, weak magnetism, finite-\(Q^2\) form factors, neutrino/antineutrino VA contraction, RPA, NN correlations, or in-medium vertex corrections. It does not calculate B.1 production, B.2 absorption, radial transport, luminosity, or an axial cooling curve.

Next: C4-B, introduce the full weak-current tensor using local quasiparticle kinematics and effective-mass spinors, while retaining vacuum nucleon form factors with their physical nucleon-mass normalization. The vector Ward identity, the \(m_N^*\to M_N\) recovery of the existing P1-IIIb kernel, and the cold/dilute Horowitz limit must all pass before any EOS-dependent opacity is considered.
