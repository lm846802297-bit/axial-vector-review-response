# Independent explicit-spinor audit of the exact moving-muon B.13 kernel

**Date:** 2026-11-13  
**Scope:** pointwise amplitude-level validation only; no change to production rates, B.2 transport, Fig. 7 baseline, or axial-vector curves.

## Executive result

The existing exact moving-muon semi-Compton kernel already evaluates the three physical \(A'\) modes \(L,+,-\), both muon charges, exact \(2\to2\) recoil, and production/absorption statistical factors independently. This audit adds an independent pointwise check that does not use the production trace to form its reference: it constructs explicit on-shell Dirac spinors, sums the two initial/final muon spin states and two physical photon polarizations, and compares that result with the production trace.

The local independent calculation covers five moving-muon kinematic points and six current/charge combinations per point:

- pure vector, \(\mu^-\) and \(\mu^+\);
- pure axial, \(\mu^-\) and \(\mu^+\);
- mixed vector--axial, \(\mu^-\) and \(\mu^+\).

This gives 30 point/current cases and 90 mode-resolved matrix-element comparisons.

## 1. Independent amplitude construction

For the absorption orientation
\[
A'(q,h)+\mu(p)\longrightarrow \gamma(k,\lambda)+\mu(p'),
\]
the exact kinematics are
\[
p'=p+q-k,\qquad
q=(\omega,0,0,K),\qquad K=\sqrt{\omega^2-m_{A'}^2}.
\]
For a photon direction \(\hat{\mathbf n}\), the on-shell condition gives
\[
k^0=
\frac{m_{A'}^2+2p\cdot q}
{2(E_p+\omega-\mathbf p\cdot\hat{\mathbf n}-K\cos\theta_\gamma)}.
\]

The two tree diagrams are evaluated as
\[
\mathcal A_{h\lambda}=
\Gamma_{A',h}
\frac{\slashed p+\slashed q+m_\mu}{m_{A'}^2+2p\cdot q}
\slashed\epsilon_{\gamma,\lambda}
+
\slashed\epsilon_{\gamma,\lambda}
\frac{\slashed p-\slashed k+m_\mu}{-2p\cdot k}
\Gamma_{A',h}.
\]
The reference is formed from explicit positive-energy spinors normalized by
\[
\bar u(p)u(p)=2m_\mu,
\]
with the initial muon spin summed and averaged by \(1/2\), the final muon spin summed, and two orthonormal real transverse photon polarizations summed explicitly. The factor \(e^2=4\pi\alpha\) is included. No mediator-polarization average is taken: each of \(L,+,-\) is fixed separately.

The vector longitudinal mode uses the Ward-equivalent representative
\[
\widetilde\epsilon_L^\mu
=\epsilon_L^\mu-\frac{q^\mu}{m_{A'}},
\]
which is valid only for the conserved vector-current part. The axial longitudinal mode retains the physical \(\epsilon_L^\mu\). The \(\mu^+\) mixed-current amplitude reverses the relative vector--axial interference sign.

## 2. Numerical checks

The independent explicit-spinor calculation was run locally with NumPy 2.3.5 / Python 3.13.5. The acceptance thresholds are \(10^{-10}\) for amplitude/trace agreement, photon Ward residual, final-muon shell closure, and the vector longitudinal Ward shift.

| Check | Maximum / minimum result | Acceptance |
|---|---:|---:|
| Explicit spinor vs production Dirac trace, all modes | \(1.7712\times10^{-13}\) maximum relative residual | PASS |
| Explicit photon Ward contraction | \(1.4688\times10^{-13}\) maximum amplitude residual | PASS |
| Final-muon mass-shell residual | \(6.5175\times10^{-16}\) | PASS |
| Physical vs Ward-shifted vector longitudinal amplitude | \(3.5415\times10^{-14}\) maximum relative residual | PASS |
| Minimum explicit \(|\mathcal M_h|^2\) | \(7.0507\times10^{-3}\) | nonnegative |

All 90 mode-resolved explicit matrix elements are nonnegative.

As a negative control on the Ward shift, applying the same \(q^\mu/m_{A'}\) subtraction to the axial longitudinal current is not valid: the sampled axial amplitude changes by an order-one amount. The implementation must therefore continue to use the physical longitudinal polarization for the axial current.

## 3. Interpretation

This is a stronger check than comparing two quadrature implementations that share the same Dirac trace. It independently validates:

1. the \(s\)- and \(u\)-channel amplitude ordering used in the moving-muon kernel;
2. the initial/final muon spinor ordering;
3. the sum over the two physical photon polarizations;
4. the three physical mediator-polarization projections;
5. the vector-current longitudinal Ward shift;
6. the charge-conjugate sign of the mixed vector--axial term.

It is a pointwise matrix-element audit. It does **not** by itself certify the thermal phase-space integral, a uniform radial/energy quadrature error bound, or the global mode-resolved supernova transport.

## 4. Existing local-kernel validation retained

The independent check supplements, rather than replaces, the existing local-kernel tests:

- stationary-muon endpoint against the exact-recoil stationary-target kernel;
- photon Ward identity for moving muons and both charges;
- mode-by-mode production/absorption detailed balance;
- charge-conjugate cancellation of vector--axial interference at zero chemical potential;
- nonzero-chemical-potential charge-resolved interference;
- cold/dilute limit;
- unpolarized inverse-rate normalization;
- finite full local emissivity and final-muon shell closure.

The earlier high-order local quadrature audit reached a maximum \(20\times12\times12\times12\to24\times14\times14\times14\) refinement change of \(0.03016\%\) at its most demanding sampled point. That is a sampled-point screening result, not a uniform bound over the full \((r,\omega)\) domain.

## 5. P1 disposition

**Pointwise three-polarization amplitude validation: PASS.**

The exact B.13 local kernel is already implemented; this audit independently validates its pointwise matrix elements. The next unresolved P1 item is a denser, source-weighted radial/energy convergence audit of the local mode-resolved production and absorption arrays. After that, P2 must propagate the exact B.13 \(L,+,-\) rates separately and compare:

1. literal scalar polarization-summed B.2;
2. the explicitly defined equal-occupation average-opacity closure;
3. independent-mode propagation.

The existing B.13 global source-plus-opacity calculation uses the literal scalar B.2 transport prescription; it is not a global independent-mode B.13 transport result. Keep that distinction explicit. The Fig. 7 pure-vector gate remains **NOT PASSED**, and no axial-vector limit is updated.

## 6. Reproducibility

- Production local kernel: moving_muon_compton.py
- Existing thermal-rate tests: test_thermal_rates.py
- New independent reference: thermal_integrals/audit_b13_moving_muon_spinor_reference.py
- New regression tests: test_b13_moving_muon_spinor_reference.py
- Machine-readable local summary: thermal_integrals/outputs/b13_moving_muon_explicit_spinor_audit_2026-11-13.json
- Dedicated CI workflow: .github/workflows/p1-b13-exact-polarization-kernel.yml

No production collision kernel, B.2 baseline, stellar profile, luminosity, manuscript, referee response, or axial-vector output is modified.
