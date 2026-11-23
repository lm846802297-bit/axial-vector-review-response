# Global-06B: full-radial threshold-edge and targeted high-order audit

**Date:** 2026-11-18  
**Benchmark:** \(m_{A'}=10\) MeV, pure-vector \(g_V/g_X=1,\ g_A/g_X=0\).  
**Profile:** SFHo-18.8, \(t_{\rm pb}=1\) s, 1687 digitized radial vertices.  
**Scope:** B.13 moving-muon semi-Compton local kernel. This is not a full B.1 source or B.2 transport result.

## 1. Low-x coordinate and full-profile screen

The threshold coordinate is

\[
x=\frac{\omega_{\rm loc}-m_{A'}}{T(r)},\qquad
\omega_{\rm loc}=m_{A'}+xT(r).
\]

The low-x screen covers \(0\le x\le0.05\), with nine formal knots uniformly refined in \(\sqrt{x}\) from the five base knots \(0,0.005,0.015,0.03,0.05\), plus eight independent validation points. The full low-order screen evaluates all 1687 radial vertices and 28,679 direct radial-energy points. Sixty radial intervals with the largest channel-resolved neighbor changes are checked at direct midpoints (540 additional evaluations).

Low-order full-profile results:
- energy PCHIP maximum relative error: 0.067119%;
- top-60 radial midpoint maximum relative error: 0.083104%;
- detailed-balance maximum residual: \(6.92\times10^{-15}\);
- final-muon mass-shell maximum residual: \(2.04\times10^{-13}\);
- all rates finite and nonnegative.

The interpolation is applied to absorption, with production and reduced absorption reconstructed using local detailed balance. The spectral source retains its explicit \(\omega^2 k_{A'}/(2\pi^2)\) phase-space factor.

## 2. Targeted high-order quadrature

The worst ten energy-interpolation points and ten highest-neighbor-change radial intervals were frozen in `results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_TARGETS_INPUT.json`. The source profile SHA-256 is `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.

The targeted calculation contains 431 unique \((r,x)\) positions and 2155 ordered kernel evaluations. Four workers completed the run in 591.37 s. The actual order ladder at all evaluated positions stopped at

\[
(10,6,6,6)\to(14,8,8,8)\to(18,10,10,10)
\to(22,12,12,12)\to(26,14,14,14),
\]

because the final successive-order change was already below \(10^{-3}\). The optional extension \((30,16,16,16)\) was not needed for this targeted set.

| High-order check | Maximum relative error/residual | Criterion | Result |
|---|---:|---:|---|
| Final successive-order change | 0.032922% | 0.1% | Pass |
| Energy PCHIP, high-order truth | 0.067166% | 1% | Pass |
| Radial midpoint, high-order truth | 0.083111% | 1% | Pass |
| Detailed balance | \(5.03\times10^{-15}\) | \(2\times10^{-10}\) | Pass |
| Final-muon mass shell | \(2.04\times10^{-13}\) | \(2\times10^{-10}\) | Pass |
| Positivity/finiteness | all targeted rates | all | Pass |

The worst high-order energy interpolation point is \(r=8.4821412022467\) km, \(x=0.0003125\), in the \(\mu^+,L\) absorption channel. The largest high-order radial midpoint interpolation error is 0.083111%, at \(r=15.525\) km, \(x=0\), in the \(\mu^+,L\) absorption channel.

### The apparent 24.76% radial jump

The largest endpoint-to-endpoint neighbor change is 24.759% across the very short interval

\[
22.1918936570\text{ km}\le r\le22.1918946570\text{ km}.
\]

The high-order direct midpoint interpolation error in this interval is only \(3.08\times10^{-9}\). The profile provenance resolves the origin of this feature: the reconstructed Caputo muon-chemical-potential curve ends at \(r_{\max}=22.191893657048542\) km, and the profile builder records a support-boundary offset of \(10^{-6}\) km. The next profile vertex is exactly \(r_{\max}+10^{-6}\) km, where the unsupported \(\mu_\mu\) input is set to zero.

- last source-supported node: \(\mu_\mu=0.999999834\) MeV;
- first support-boundary node: \(\mu_\mu=0\) MeV.

This is therefore a **profile-support truncation edge**, not evidence of a physical discontinuity in the supernova muon chemical potential. The supporting input-domain and support-offset metadata are recorded in the [profile provenance](../../data/profile_provenance.json). The direct midpoint test shows that the interpolant reproduces the chosen linear transition at that midpoint, but the support convention itself must remain explicit in any outer-shell opacity/path integration; it must not be mistaken for a resolved physical muonosphere boundary.

## 3. High-order polarization anchor

Because the B.13 kernel itself resolves the three vector polarizations, we directly checked the mode-resolved absorption at

\[
r=8.24821831451522\text{ km},\quad
T=39.1873531264\text{ MeV},\quad N=0.791831563,
\]

using the same order ladder through \((26,14,14,14)\). Charge-resolved \(\mu^-\), \(\mu^+\) contributions and all three modes \((L,+,-)\) are retained.

| \(x\) | \(\omega_{\rm loc}\) (MeV) | \(\Gamma_{\rm abs,L}/\Gamma_{\rm abs,T,av}\) | Longitudinal suppression |
|---:|---:|---:|---:|
| 0 | 10.0000 | 1.000159 | effectively 0% |
| 0.015 | 10.5878 | 0.921539 | 7.846% |
| 0.05 | 11.9594 | 0.771126 | 22.887% |

Here \(\Gamma_{\rm abs,T,av}=(\Gamma_{+}+\Gamma_{-})/2\). The \(+\) and \(-\) rates agree to relative precision better than \(3\times10^{-16}\), as expected for this pure-vector, parity-symmetric local kernel. The final order changes at the three points are 0.03213%, 0.03212%, and 0.03207%, respectively.

This establishes an energy-dependent longitudinal/transverse difference in the **local B.13 semi-Compton opacity**. It rules out treating the three B.13 modes as having identical Compton opacity at all energies. It does not yet give the total B.2 opacity: neutrino inverse decay and dimuon channels must be included, and each mode must be propagated through the full ray integral.

For a quantitative comparison, define the equal-split proxy \(\bar\Gamma=(\Gamma_L+\Gamma_++\Gamma_-)/3\). At \(x=0.015\), assigning \(\bar\Gamma\) to each mode would overestimate the true longitudinal absorption by 5.68% and underestimate each transverse absorption by 2.62%. At \(x=0.05\), those errors grow to +19.79% for \(L\) and -7.63% for each transverse mode. These are local B.13-only errors at the stated radius; they are not yet errors on the total B.2 optical depth or escaped luminosity.

## 4. Acceptance boundary

The targeted high-order checks pass. The following gates remain open:

1. **Full-profile high-order confirmation:** the 431-point set is targeted, not a high-order evaluation of every radial vertex and every formal energy knot. Therefore `full_global_high_order_acceptance=false`.
2. **Complete B.1 source:** this run is B.13 semi-Compton only; it does not include the full neutrino inverse-decay and dimuon source sum or the converged production integral.
3. **B.2 mode-resolved transport:** the new polarization anchor demonstrates that the equal split of Compton opacity among \(L,+,-\) is only a diagnostic closure. Replace it with the actual mode-resolved B.13 rates, combine with mode-resolved neutrino inverse decay and dimuon opacity, then perform the angular/radial path integration.
4. **Thermodynamic edge:** retain the sharp \(\mu_\mu\) transition near 22.191894 km in the profile interpolation and ray-opacity audit.

No B.2 escaped luminosity, Fig. 7 curve, SN1987A limit, or axial-vector exclusion curve is updated by this report.

## 5. Reproduction and files

- Frozen target set: [`HIGH_ORDER_TARGETS_INPUT.json`](results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_TARGETS_INPUT.json).
- High-order driver: [`run_p1b_global06b_threshold_edge_high_order_targets.py`](run_p1b_global06b_threshold_edge_high_order_targets.py).
- Polarization-anchor driver: [`run_p1b_global06b_polarization_anchor_high_order.py`](run_p1b_global06b_polarization_anchor_high_order.py).
- Machine-readable targeted result: [`HIGH_ORDER_ACCEPTANCE_SUMMARY.json`](results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_ACCEPTANCE_SUMMARY.json).
- Machine-readable polarization result: [`POLARIZATION_ANCHOR_SUMMARY.json`](results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/POLARIZATION_ANCHOR_SUMMARY.json).
- Calculation provenance: [`HIGH_ORDER_PROVENANCE.json`](results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_PROVENANCE.json).

Run from the repository's thermal-integrals directory:

```bash
python run_p1b_global06b_threshold_edge_high_order_targets.py
python run_p1b_global06b_polarization_anchor_high_order.py
```

The raw local output archive is retained separately; the committed JSON files are compact acceptance records. The scripts verify the SFHo profile hash before calculating.
