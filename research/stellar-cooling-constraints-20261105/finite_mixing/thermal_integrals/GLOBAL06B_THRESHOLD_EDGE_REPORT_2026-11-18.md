# Global-06B: full-radial B.13 threshold-edge screen

**Date:** 2026-11-18  
**Benchmark:** \(m_{A'}=10\) MeV, pure-vector \(g_V/g_X=1,\ g_A/g_X=0\).  
**Profile:** SFHo-18.8, \(t_{\rm pb}=1\) s, 1687 digitized radial vertices.  
**Scope:** local moving-muon semi-Compton B.13 kernel only; \(0\le x\le0.05\).

## 1. Purpose

Global-06 covers the formal energy range beginning at \(x=0.05\). This run closes the low-\(x\) *sampling* gap at the vector threshold. It does not yet close the high-order quadrature gate or the B.1/B.2 transport calculation.

The energy coordinate is

\[
x=\frac{\omega_{\rm loc}-m_{A'}}{T(r)},\qquad
\omega_{\rm loc}=m_{A'}+xT(r).
\]

The formal knots are the five base values \(0,0.005,0.015,0.03,0.05\) plus their four midpoints in \(\sqrt{x}\). Eight additional independent validation points are inserted halfway between adjacent formal knots in \(\sqrt{x}\).

## 2. Execution and provenance

- 1687 radial vertices × 17 formal/validation coordinates = 28,679 direct local-kernel evaluations.
- Quadrature order: \((10,6,6,6)\); this is a low-order screening pass.
- 60 highest-neighbor-variation radial intervals were directly midpoint-checked at all 9 formal knots: 540 additional direct evaluations.
- Four worker processes; wall time 569.08 s.
- Runtime: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0.
- Profile SHA-256: `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.
- Source bundle: Actions run 43534587169, artifact 14089450366, ZIP SHA-256 `b27c101a063d6f5784d72ef12ad699abc2ceae000b5824cfc4aaa0d191c3474d`; source snapshot commit `5e7b60dc61b3f36909ed39f3400b06884fc77053`.
- Kernel/profile hashes are recorded in the source bundle's `MANIFEST.sha256`; the moving-muon B.13 kernel and SFHo profile were not edited.

## 3. Results

| Check | Result | Project criterion | Disposition |
|---|---:|---:|---|
| Energy interpolation: max relative error | 0.06712% | 1% | Pass |
| Radial midpoint interpolation: max relative error | 0.08310% | 1% | Pass |
| Detailed-balance residual | \(6.92\times10^{-15}\) | \(2\times10^{-10}\) | Pass |
| Final-muon mass-shell residual | \(2.04\times10^{-13}\) | \(2\times10^{-10}\) | Pass |
| Rates finite and nonnegative | all 28,679 points | all | Pass |

### Energy interpolation

PCHIP is applied to \(\log\Gamma_{\rm abs}\) in \(\sqrt{x}\). Production and reduced absorption are reconstructed from exact local detailed balance rather than independently interpolating the steep Boltzmann factor.

The maximum of 13,496 independent channel checks is 0.06712%, at \(r=8.4821412022467\) km and \(x=0.0003125\), in the \(\mu^+,L\) absorption channel.

### Radial interpolation

All 1686 adjacent intervals were ranked by their largest charge-, polarization-, field-, and formal-\(x\)-resolved neighbor change. The largest neighbor change is 24.76% across a \(10^{-6}\) km interval at \(r\simeq22.191894\) km. Direct midpoint evaluation of this same interval gives only \(3.08\times10^{-9}\) relative error; the large endpoint-to-endpoint change is therefore not an interpolation failure.

The 60 highest-ranked intervals were checked at direct radial midpoints. The largest actual midpoint interpolation error is 0.08310%, at \(r=15.525\) km and \(x=0\), in the \(\mu^+,L\) absorption channel.

### Threshold behavior: absorption is not the spectral source

At \(x=0\), \(\omega_{\rm loc}=m_{A'}\) and \(k_{A'}=0\). At \(r=8.4821412022467\) km, the archived direct kernel gives finite absorption rates per \(g_X^2\):
- \(\mu^-\): \((0.02798693,0.02790108,0.02790108)\) for \((L,+,-)\);
- \(\mu^+\): \((2.97625,2.96982,2.96982)\times10^{-4}\).

The spectral source is exactly zero at this endpoint because it contains the phase-space factor \(\omega^2 k_{A'}/(2\pi^2)\). This directly confirms that one must not set the threshold absorption rate to zero merely because the spectral source vanishes. The interpolation is therefore performed on absorption, while production and reduced absorption are reconstructed by detailed balance and the spectral source receives its explicit phase-space factor.

### Polarization splitting relevant to B.2

At \(r=8.24821831451522\) km and \(x=0.05\), the charge-summed low-order B.13 absorption is:
- longitudinal: \(\Gamma_{\rm abs,L}=0.01847052\);
- transverse average: \(\Gamma_{\rm abs,T}=0.02389514\).

The longitudinal rate is 22.70% below the transverse average. The same relative split appears in production and reduced absorption because of mode-by-mode detailed balance. This is a local low-order screen result; the targeted high-order calculation must confirm this point before it is used quantitatively in B.2. It already shows why splitting the scalar Compton opacity equally among three modes is a diagnostic closure, not an exact substitute for the B.13 mode-resolved kernel.

## 4. Interpretation

The low-\(x\) energy interpolation and the targeted radial interpolation both pass the project's 1% screening criterion over the full 1687-node profile. Detailed balance, the final-muon mass shell, and positivity also pass by large margins.

This establishes that a low-order B.13 table can be interpolated smoothly across \(0\le x\le0.05\) on the tested grid. It does **not** establish high-order quadrature convergence: the order \((10,6,6,6)\) was used for this global screen. Nor does it establish convergence of the full B.1 energy/radial integral.

## 5. Remaining gates

1. Complete targeted high-order quadrature on the worst 10 energy points and worst 10 radial intervals; require successive-order changes below \(10^{-3}\) per channel.
2. Confirm the longitudinal/transverse split at \(r=8.24821831451522\) km, \(x=0.05\), with the high-order ladder.
3. If targeted checks pass, run a full-profile high-order confirmation or an independently justified adaptive refinement.
4. Join this low-\(x\) table continuously to Global-06 at \(x=0.05\), checking the shared endpoint channel by channel.
5. Rebuild the complete B.1 source with all channels, including neutrino inverse decay; this B.13 table alone is not the full source.
6. Only after the local kernel and B.1 source converge, proceed to the three distinct B.2 lanes: literal scalar equation reproduction, equal-occupation average-opacity closure, and independent mode-resolved transport.

No B.2 luminosity, Fig. 7 curve, SN1987A limit, or axial-vector exclusion curve is updated by this run.
