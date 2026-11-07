# Moving-muon Compton and full dimuon thermal integrals

Date: 2026-11-07  
Status: implementation specification; no production code or cooling curve changed.

## Scope and decision

The next calculation converts the already-tested local kernels into thermal emissivities and inverse absorption rates. It is deliberately limited to the fixed reconstructed SFHo-18.8 background already used by this project. It does not request Garching raw simulation data, modify the referee response or manuscript, or start a new constraint scan.

Two calculations must remain distinct:

1. **Blinov comparison lane:** reproduce the published Appendix-B approximations literally, including the B.14--B.19 nonrelativistic-muon/no-recoil semi-Compton prescription and its stated domain of applicability.
2. **Moving-muon physical lane:** evaluate the full thermal collision integral with moving initial and final muons. This is a separate improvement, not a correction to be tuned until it matches Fig. 7.

The fixed-muon-at-rest exact-recoil kernel in `rates.py` is an intermediate diagnostic only. It is neither the B.14 no-recoil limit nor the full moving-muon thermal integral.

## 1. Semi-Compton: invariant collision integral

For each mediator polarization (h=L,+,-), evaluate the differential production rate at fixed on-shell mediator momentum (k^mu=(\omega,\mathbf k)):

\[
\Gamma^{\rm prod}_{\mu\gamma,h}(k)=
\frac{1}{2\omega}\sum_{Q=\mu^-,\mu^+}
\int d\Pi_p\,d\Pi_q\,d\Pi_{p'}
(2\pi)^4\delta^{(4)}(p+q-p'-k)
\overline{|\mathcal M_{Q,h}|^2}
f_Q(E_p)f_\gamma(q)
[1-f_Q(E_{p'})],
\]

where (d\Pi_a=d^3p_a/[(2\pi)^3 2E_a]). The inverse absorption rate uses the same matrix element and phase space with statistical factor

\[
f_Q(E_{p'})[1-f_Q(E_p)][1+f_\gamma(q)].
\]

The amplitude must retain the full vector--axial combination at the mediator vertex,

\[
\mathcal M_h=g_V^\mu\mathcal M_{V,h}
+g_A^\mu\mathcal M_{A,h},
\qquad
|\mathcal M_h|^2=|\mathcal M_h|^2_{\rm full},
\]

including interference. The code-basis sign convention remains the one documented in `model.py`: the positive axial basis in `rates.py` is \(\gamma^\alpha(-\gamma^5)\), so its coefficient is (-g_A^\mu).

### Numerical reduction

Use the energy-momentum delta function to eliminate the final-muon momentum and one remaining scalar integration variable. The implementation must document the Jacobian, physical integration limits, and treatment of multiple kinematic roots. Do not replace the moving-muon distribution by an effective density multiplying a rest-target cross section.

For numerical stability:

- use dimensionless momenta scaled by local (T(r));
- evaluate Fermi/Bose factors with overflow-safe functions;
- split the integration at kinematic endpoints and any angular turning points;
- compare adaptive integration with an independently refined tensor-product quadrature at representative points;
- sum the two charge states explicitly, with chemical potentials (+\mu_\mu) and (-\mu_\mu);
- compute production and absorption independently before testing detailed balance.

At zero chemical potential, the two charge contributions must be equal. At nonzero chemical potential, they need not be equal individually; their sum must obey the equilibrium relation.

### Mandatory checks

1. Photon Ward identity for arbitrary sampled moving initial-muon momenta.
2. Pure-vector and pure-axial limits reproduce the corresponding amplitude kernels.
3. Mixed-current result equals the coherent amplitude square, not an incoherent sum.
4. Pointwise thermal detailed balance:
   \[
   \Gamma^{\rm abs}_h(k)=e^{\omega/T}\Gamma^{\rm prod}_h(k)
   \]
   for the charge-neutral reaction when all distributions share the same temperature and the chemical potentials are assigned consistently.
5. Nonrelativistic/dilute-muon limit approaches the existing stationary-target result within its stated approximation.
6. Separately, the B.14--B.19 implementation reproduces the published no-recoil normalization; it must not be used as a surrogate for check 5.

## 2. Dimuon inverse decay: full mediator-momentum integral

The existing `charged_muon_decay_rates` and `charged_muon_decay_rates_mixed` functions already provide exact free-fermion kinematics, Fermi blocking, polarization resolution, and mode-by-mode detailed balance at fixed mediator energy. Reuse them; do not duplicate the decay trace.

For a local thermodynamic point, compute the energy-differential emissivity

\[
Q_{\mu\mu}(r)=
\sum_h\int\frac{d^3k}{(2\pi)^3}
\,\omega\,\Gamma^{\rm prod}_{\mu\mu,h}
(\omega,r).
\]

For an isotropic medium this becomes

\[
Q_{\mu\mu}(r)=
\frac{1}{2\pi^2}
\sum_h\int_{m_{A'}}^\infty dk\,
k^2\omega\,\Gamma^{\rm prod}_{\mu\mu,h}
(\omega,r),\qquad
\omega=\sqrt{k^2+m_{A'}^2}.
\]

The inverse absorption rate is integrated over the same mediator momentum grid independently. The local reduced opacity is assembled only after the per-mode rates are validated:

\[
\Gamma^{\rm red}_{h}=
\sum_i\left(1-e^{-\omega/T}\right)
\Gamma^{\rm abs}_{i,h}.
\]

The threshold is exact: this on-shell channel is identically zero for (m_{A'}\leq2m_\mu). Near threshold, use a variable that resolves the small outgoing-muon velocity β and compare against the analytic vacuum-width scaling Γ_A/Γ_V.

## 3. Thermal emissivity and transport are separate stages

First archive local differential production and absorption tables as functions of ((r,\omega,m_{A'},h)). Only after local rates pass should the code construct radial optical depths and escape probabilities.

Do not interchange

\[
\sum_h Q_h e^{-\tau_h}
\quad\hbox{and}\quad
\left(\sum_h Q_h\right)e^{-\tau_{\rm scalar}}.
\]

Keep the two documented transport lanes separate:

- Lane A: literal published polarization-summed prescription for the Blinov comparison.
- Lane B: mode-resolved production, absorption, optical depth, and escaped luminosity.

A Lane-B physical result is not required to equal Lane A by assumption. Any difference must be traced to the transport prescription and quantified.

## 4. UV channel bookkeeping

At fixed (g_X,m_{A'}), use

\[
g_V^\mu=g_X\sin^2\theta_{\mu R},\qquad
g_A^\mu=-g_X\cos^2\theta_{\mu R},
\]

while retaining the active-neutrino couplings

\[
g_{\nu_\mu}=+g_X,\qquad
g_{\nu_\tau}=-g_X
\]

independently of θμR. Therefore the total included emissivity is a channel sum, not a rescaled muon-current result:

\[
Q_{\rm included}=Q_{\nu_\mu}+Q_{\nu_\tau}
+Q_{\mu\gamma}(g_V^\mu,g_A^\mu)
+Q_{\mu\mu}(g_V^\mu,g_A^\mu).
\]

The neutrino channel must be reused from the independently validated implementation. No neutrino coupling is changed when scanning the charged-muon mixing angle.

## 5. Execution order and acceptance

### P0-A — full dimuon momentum integral

- Reuse the existing fixed-ω mode-resolved rates.
- Integrate over mediator momentum with a mapped semi-infinite interval and adaptive/reference quadrature.
- Save (Q_h(r)), integrated absorption, and convergence diagnostics.
- Test threshold closure, dilute limit, detailed balance, pure-current endpoints, and mixed interference.
- Do not run stellar transport until these tests pass.

### P0-B — moving-muon semi-Compton collision integral

- Derive and record the reduced phase-space integral and Jacobian before coding.
- Implement vector, axial, and coherent mixed amplitudes using the same gamma-matrix conventions as `rates.py`.
- Integrate both muon charge states and both forward/reverse statistical factors.
- Validate Ward identities and detailed balance pointwise.
- Compare against the stationary-target limit and the separately implemented B.14 limit.

### P1 — local profile tables

Evaluate both channels at a small set of representative radii and mediator energies on the existing reconstructed profile. Include at least a core point, an intermediate-radius point, and an outer production-region point. Record the exact profile interpolation and units.

### P2 — transport integration

Only after P0 and P1 pass, feed the local rates into the existing transport implementation. Keep Lane A and Lane B separate, and do not run a finite-mixing exclusion scan until the pure-vector literature gate and transport prescription are explicitly resolved.

## 6. Output and preservation policy

New code, tests, and machine-readable outputs belong in a dedicated subdirectory under `finite_mixing/thermal_integrals/`. Existing `rates.py`, saved response scans, axial figures, manuscript source, and referee-response TeX/PDF remain unchanged until the new implementation passes its own review. No fitted rescaling, opacity multiplier, or post-hoc contour adjustment is allowed.

The exact numerical tolerances are to be set from independent quadrature convergence and floating-point error after the reduced integrals are derived; do not invent tolerances before the integration variables and endpoint behavior are established.
