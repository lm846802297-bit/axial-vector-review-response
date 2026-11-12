# Dense local B.6--B.10 and B.14--B.19 kernel audit on the full global quadrature grid (2026-11-09)

## Executive conclusion

The local production and absorption formulae used in the full independent B.1+B.2 vector calculation have now been checked on the complete set of source radius--energy quadrature nodes, rather than on the earlier 96-point diagnostic sample.

The audit covers 200 radial nodes and 320 energy nodes at each radius, for 64,000 \((r,\omega)\) points. At every radial node, the exact radius-dependent lower energy threshold is retained. Neutrino production and inverse-occupation absorption are independently reconstructed from direct two-body angular phase-space integrals. The muon density and susceptibility are independently recomputed with the transformed B.17 momentum integral, and the Compton B.14--B.19 rates are independently reconstructed.

The largest local residuals are:
- neutrino B.6 production: \(6.31\times10^{-14}\);
- neutrino B.10 absorption: \(6.00\times10^{-14}\);
- B.17 muon susceptibility: \(2.65\times10^{-13}\);
- Compton B.16 production: \(2.66\times10^{-13}\);
- total production, absorption, and reduced absorption: at most \(2.30\times10^{-13}\).

The 256-to-512 point neutrino angular quadrature change is at most \(1.20\times10^{-14}\). The \(\mu_{\nu_\mu}\to-\mu_{\nu_\mu}\) pair-production sign-invariance residual is \(3.96\times10^{-15}\).

Therefore the local B.6--B.10 and B.14--B.19 formula implementations are independently validated over the actual 64,000-point grid used by the full B.1+B.2 calculation. This closes the remaining local algebraic/numerical coverage gap for the B.16 vector baseline. It does not validate the physical no-recoil approximation against the exact moving-muon B.13 kernel.

## 1. Grid matched to the end-to-end luminosity calculation

- Mediator mass: 10 MeV.
- Profile SHA-256: \`9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c\`.
- Radial quadrature: 50 equal-width panels, four-point Gauss--Legendre per panel.
- Source radial nodes: 200.
- Energy quadrature at each radius: 80 logarithmic panels, four-point Gauss--Legendre per panel.
- Energy nodes per radius: 320.
- Total radius--energy points: 64,000.
- Energy upper limit: 2010 MeV.
- Minimum sampled energy over all source nodes: 10.87785 MeV.
- Maximum sampled energy: 1999.05050 MeV.
- Maximum \(\omega/T\): 656.4589.

The radial and energy nodes match the final 200-node full B.1+B.2 calculation. The local audit therefore tests the actual nodes used in the global luminosity calculation, not a separately chosen diagnostic grid.

## 2. Neutrino B.6 production and B.10 absorption

For each radius and energy node, the \(\nu_\mu\) and \(\nu_\tau\) pair-production rates are reconstructed independently from
\[
E_{1,2}=\frac{\omega}{2}(1\pm v_V z),
\qquad
v_V=\sqrt{1-\frac{m_V^2}{\omega^2}},
\]
with the direct angular phase-space integral over \(z\in[-1,1]\). The two flavors are evaluated separately, with \(\mu_{\nu_\mu}(r)\) and \(\mu_{\nu_\tau}=0\), respectively. The inverse-occupation factors are integrated independently for absorption.

Maximum residuals over all 64,000 radius--energy points:
- \(\nu_\mu\) B.6 direct production vs analytic expression: \(6.3052\times10^{-14}\);
- \(\nu_\tau\) B.6 direct production vs analytic expression: \(6.3052\times10^{-14}\);
- \(\nu_\mu\) B.10 detailed balance: \(5.9962\times10^{-14}\);
- \(\nu_\tau\) B.10 detailed balance: \(5.9962\times10^{-14}\);
- neutrino B.4 reduced absorption: \(5.9962\times10^{-14}\).

The direct angular integral is also repeated with 256 points at 40 evenly distributed source radii. The maximum 256-to-512 change over all energy nodes at these radii is \(1.1945\times10^{-14}\).

## 3. Muon density and B.17 susceptibility

At each of the 200 radial nodes, the one-species negative-muon density and susceptibility are independently recomputed with the transformed variable
\[
t=\sqrt{\frac{E_\mu-m_\mu}{T}},
\]
using 256-point Gauss--Legendre quadrature. The resulting density, susceptibility \(\chi_\mu=n_\mu F_{\rm deg}\), and degeneracy factor are compared with the reference implementation used in the global calculation.

Maximum residuals:
- \(n_\mu\): \(2.3248\times10^{-13}\);
- \(\chi_\mu\): \(2.6534\times10^{-13}\);
- \(F_{\rm deg}\): \(3.2641\times10^{-14}\).

The one-species B.17 convention is retained. No factor of two is added for \(\mu^+\).

## 4. Compton B.14--B.19 and B.4

Using the independently evaluated B.17 susceptibility, the Compton cross section and B.16 production rate are reconstructed directly. B.19 detailed balance, B.4 reduced absorption, and the explicit B.14--B.16 velocity cancellation are checked separately.

Maximum residuals:
- B.16 production vs reference implementation: \(2.6557\times10^{-13}\);
- B.19 detailed balance: zero at the stored floating-point precision;
- B.4 reduced absorption: \(4.4277\times10^{-16}\);
- B.14--B.16 velocity cancellation: \(7.2701\times10^{-16}\).

The total local production, absorption, and reduced absorption (neutrino plus Compton) close against the reference implementation with maximum residual \(2.2967\times10^{-13}\).

## 5. Sign of the muon-neutrino chemical potential

For the pair process \(\nu_\mu\bar\nu_\mu\to V\), the direct angular phase-space integral is invariant under
\[
\mu_{\nu_\mu}\longrightarrow-\mu_{\nu_\mu}.
\]
The sign flip exchanges the two initial-state energies under \(z\to-z\); the integration domain and measure are symmetric. The maximum residual over all 64,000 points is \(3.9617\times10^{-15}\).

This establishes that the sign of the reconstructed \(\mu_{\nu_\mu}\) branch does not affect the local pair-production or inverse-decay rate in this channel. Its magnitude profile remains relevant; this result does not justify replacing the published signed profile in other processes or observables.

## 6. Interpretation and limits

Established:
1. The B.6 \(\nu_\mu\) and \(\nu_\tau\) production formulae agree with direct angular phase-space integration over the full global quadrature grid.
2. B.10 detailed balance and B.4 reduced neutrino absorption close over the same grid.
3. The one-species B.17 density and susceptibility agree with an independent transformed momentum integral.
4. The B.14--B.19 Compton production, absorption, and reduced opacity agree with the independent susceptibility-based reconstruction.
5. The 256-to-512 angular quadrature change is negligible over the checked radial nodes.
6. The \(\mu_{\nu_\mu}\) sign convention is immaterial to this charge-conjugate pair process, although its magnitude profile is not.

Not established:
1. The physical accuracy of the B.14--B.16 no-recoil Compton approximation relative to the exact moving-muon B.13 kernel.
2. The fidelity of the reconstructed public-figure stellar profile to the raw Garching simulation data.
3. The correct conserved-energy/redshift convention and full GR ray geometry.
4. Agreement with Fig. 7. Local formula closure is not a substitute for validation of the physical background and transport prescription.

No local rate, opacity, source normalization, coupling, luminosity, vector reference curve, or production axial-vector constraint is rescaled or modified.

## 7. Reproducibility

- GitHub Actions: [Run #42565336032](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42565336032)
- Script: \`audit_b16_dense_local_kernel.py\`
- Unit tests: \`test_b16_dense_local_kernel.py\`
- Workflow: \`.github/workflows/b16-dense-local-kernel-audit.yml\`
- Machine-readable result: \`outputs/b16_dense_local_kernel_audit_10mev_2026-11-09.json\`
