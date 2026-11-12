# P1-IIIe-C4B2: EOS-effective-mass moving-nucleon weak collision kernel

Date: 2026-11-11  
PR: #57  
Branch: \`research/moving-muon-thermal-rates-20261107\`

## 1. Purpose and scope

C4-B2 integrates the C4-B1 effective-mass weak tensor over the local initial nucleon Fermi sea. It is the first EOS-dependent moving-nucleon neutral-current collision-kernel calculation on the Caputo SFHo-18.8 snapshot.

The local benchmark contains 16 cases:
- radii \(r=0.20,\ 5.00,\ 10.00,\ 15.20\) km;
- neutron and proton targets;
- neutrino and antineutrino;
- incident neutrino energy \(E_\nu=100\) MeV;
- fixed outgoing-angle cosine \(\cos\theta=-0.5\);
- outgoing-energy integration centered on the stationary-quasiparticle recoil energy with half-window \(60\) MeV.

This is a local differential-in-angle kernel slice. It is **not** the total neutrino scattering rate, total cross section, B.2 radial opacity, transport solution, or luminosity.

## 2. Matched EOS and weak-current conventions

For each species and radius, use
\[
E_N^*(p;r)=\sqrt{p^2+m_N^{*2}(r)},\qquad
K_N(p;r)=E_N^*(p;r)-m_N^*(r),
\]
\[
f_N(p;r)=
\left[\exp\left(\frac{K_N(p;r)-\nu_N(r)}{T(r)}\right)+1\right]^{-1},
\qquad
\nu_N(r)=\mu_N^{\rm nonrel}(r)-U_N(r).
\]

The initial and final nucleon quasiparticle spinors and their on-shell energies use the same local \(m_N^*(r)\). For same-species neutral-current scattering, the momentum-independent vector potential cancels from
\[
q_0=E_N^*(|\mathbf p+\mathbf q|;r)-E_N^*(p;r).
\]
The EOS chemical potential remains in both Fermi factors.

The minimal weak vertex is
\[
\Gamma_N^\mu(q)=
F_1^N(Q^2)\gamma^\mu
+i\frac{F_2^N(Q^2)}{2M_N}\sigma^{\mu\alpha}q_\alpha
-G_A^N(Q^2)\gamma^\mu\gamma^5.
\]
The mass conventions are deliberately split:
- \(m_N^*(r)\) is used in quasiparticle spinors, on-shell energies, and \(p_{\min}\);
- the physical vacuum \(M_N\) is retained in the vacuum form-factor parameterization and weak-magnetism denominator.

The spin-averaged hadronic tensor is
\[
H_N^{\mu\nu}=\frac12\operatorname{Tr}\left[
(\slashed p'^*+m_N^*)\Gamma_N^\mu
(\slashed p^*+m_N^*)\overline\Gamma_N^\nu
\right].
\]
The trace averages over the initial nucleon spin. The occupation integral is normalized with the EOS available-volume density \(n_N'\); no extra spin factor is inserted into the already spin-averaged trace.

## 3. Moving-nucleon collision kernel

For an incoming neutrino \(k^\mu=(E_\nu,\mathbf k)\) and outgoing neutrino \(k'^\mu=(E_\nu',\mathbf k')\), define
\[
q^\mu=k^\mu-k'^\mu=(q_0,\mathbf q),\qquad
q_0=E_\nu-E_\nu',\qquad q=|\mathbf q|.
\]
The nucleon on-shell condition fixes the angle between \(\mathbf p\) and \(\mathbf q\). The initial momentum integral is restricted by the exact local \(p_{\min}(q_0,q;m_N^*)\), and the final-state Pauli factor is evaluated using the same EOS state:
\[
f_i(1-f_f)=
f_N(p;r)\left[1-f_N(|\mathbf p+\mathbf q|;r)\right].
\]

The implemented differential kernel has the structure
\[
\frac{d\Gamma_N}{dE_\nu'\,d\Omega'}
=
\frac{G_F^2 E_\nu'}{256\pi^4 E_\nu q}
\int_{p_{\min}}^{p_{\max}}dp\,
\frac{p}{E_p^*}\,
f_i(1-f_f)\,
\left\langle L_{\mu\nu}H_N^{\mu\nu}\right\rangle_\phi .
\]
The azimuthal average is performed explicitly. The finite-temperature integration over \(E_\nu'\) is then carried out over the stated \(60\) MeV half-window.

The result \(\Gamma_N^{\rm avail}\) is proportional to the free-nucleon density per available volume. Therefore
\[
\frac{d\sigma_N}{d\Omega'}\bigg|_{\rm window}
=\frac{\Gamma_N^{\rm avail}}{n_N'}
\]
is the per-target, finite-\(E_\nu'\)-window differential-in-angle quantity. The total-volume local rate carries the available-volume fraction:
\[
\Gamma_N^{\rm total\ volume}=\xi_{\rm SPP}\Gamma_N^{\rm avail}.
\]
The factor \(\xi_{\rm SPP}\) must not be included in the per-target normalization and is restored only when converting to the total-volume rate.

## 4. Required limiting checks

### 4.1 Vacuum-mass recovery of P1-IIIb

Set \(m_N^*=M_N\) and \(\nu_N=\mu_N-M_N\). The EOS kernel must reproduce the existing P1-IIIb moving-nucleon implementation, including the same Fermi occupation, recoil kinematics, weak vertex, and phase-space normalization.

### 4.2 Cold/dilute Horowitz limit

At \(n_B/n_0=10^{-10}\), \(T=10^{-3}\) MeV, and \(m_N^*=M_N\), the per-target result must approach the stationary Horowitz differential cross section. The finite-temperature and finite-density corrections are negligible in this benchmark.

### 4.3 Local detailed balance

For the initial/final Fermi factors,
\[
\frac{f_i(1-f_f)}{f_f(1-f_i)}=e^{q_0/T}.
\]
This identity is tested for both signs of \(q_0\) and several kinetic energies in every local EOS case.

### 4.4 Quadrature convergence

At the inner-core neutron benchmark, compare
\[
(n_{E'},n_p,n_\phi)=(24,24,8),\ (36,36,12),\ (48,48,16).
\]
The high-order result must differ from both lower-order results by less than one percent.

## 5. Numerical results

The final independent GitHub Actions reconstruction gives:

| Diagnostic | Maximum residual | Acceptance |
|---|---:|---:|
| \(m_N^*=M_N\) recovery of P1-IIIb | \(2.89\times10^{-15}\) | \(<10^{-10}\) |
| Cold/dilute Horowitz limit | \(8.04\times10^{-6}\) | \(<10^{-3}\) |
| Local Fermi-factor detailed balance | \(2.76\times10^{-13}\) | \(<10^{-10}\) |
| Inner-core quadrature convergence | \(9.28\times10^{-4}\) | \(<10^{-2}\) |

All 16 local EOS cases have nonnegative rates and per-target differential quantities. The \(m_N^*=M_N\) recovery is at floating-point precision; the cold/dilute result is within \(8.1\) parts per million of Horowitz; the selected core integral is converged to better than \(0.1\%\) under the tested quadrature refinement.

## 6. Independent CI and archived outputs

**C4-B2 status: PASS.**

GitHub Actions Run #7:
https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43006872370

- 6/6 unit tests passed, including strict JSON serialization of all summary diagnostics.
- The complete local EOS kernel was independently recomputed.
- The workflow revalidated all acceptance criteria.
- Output artifact: \`c4b2-eos-effective-mass-collision-kernel\`, artifact ID \`13849740173\` (90-day retention).

The artifact contains the summary JSON and the 16-case local EOS CSV, together with the P1-IIIb recovery and cold-Horowitz comparison tables.

## 7. Interpretation and scope boundary

C4-B2 establishes a consistent minimal quasiparticle embedding of the EOS effective mass into the moving-nucleon neutral-current kernel:
1. the C2 EOS chemical potentials and temperatures are used in both initial and final Fermi factors;
2. the SFHo effective mass is used in on-shell kinematics and spinors;
3. vacuum weak form factors and the physical weak-magnetism mass normalization are retained;
4. the available-volume density and \(\xi_{\rm SPP}\) are kept distinct;
5. the vacuum-mass, cold/dilute, detailed-balance, and quadrature limits pass.

Two limitations remain before interpreting this as a physical local opacity. First, the current result is differential in the outgoing angle and uses a finite \\(E_\\nu'\\) window; it is not integrated over the full outgoing phase space. Second, the minimal quasiparticle treatment does not include RPA, NN correlations, or in-medium vertex corrections.

The subsequent C4-C1 full-support audit quantifies the first limitation: the legacy \\(\\pm60\\) MeV window captures only 75.05%--99.30% of the full outgoing-energy integral in the selected local cases, with the largest deficit in the 10 km neutron-neutrino benchmark. Accordingly, the C4-B2 numbers are retained as finite-window kernel diagnostics only; the full-support C4-C1 values supersede them for this benchmark. They are not used as total rates or radial opacities.

## 8. Next stage: C4-C

C4-C should first establish outgoing-phase-space completeness:
- determine the exact kinematically allowed \(E_\nu'\) support from \(p_{\min}\le p_{\max}\), rather than assuming a fixed half-window;
- demonstrate convergence of the \(E_\nu'\) integral and its tails;
- integrate over the full outgoing-angle range with an independently converged angular grid;
- recover the cold/dilute total Horowitz cross section after integrating the differential kernel;
- only then generate the 301-radius EOS local total scattering rate and construct a radial optical-depth diagnostic.

No B.2 production opacity, radial transport, luminosity, or axial cooling curve is updated at this stage.
