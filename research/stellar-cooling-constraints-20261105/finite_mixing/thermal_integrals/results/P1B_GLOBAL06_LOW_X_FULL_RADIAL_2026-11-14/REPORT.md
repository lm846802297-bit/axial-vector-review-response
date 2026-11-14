# P1-B Global-06: full-radial low-x B.13 screen

**Date:** 2026-11-14  
**Background:** SFHo-18.8, t_pb = 1 s, original 1687-row digitized profile.  
**Profile SHA-256:** `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`.  
**Kernel:** exact-recoil moving-muon semi-Compton B.13; m_A' = 10 MeV; pure-vector endpoint gV/gX = 1, gA/gX = 0.  
**Channels:** mu-minus and mu-plus separately; A' polarizations L,+,- separately.

## Full-radial low-order scan

All 1687 original radial vertices were directly evaluated at 17 low-energy coordinates: nine formal interpolation knots and eight independent validation midpoints. This is 28,679 direct B.13 evaluations at quadrature order (10,6,6,6). All 1686 adjacent radial intervals were ranked. The top 60 intervals received direct midpoint evaluations at all nine formal x knots, adding 540 direct B.13 points.

Energy interpolation uses PCHIP(log absorption) in sqrt(x). Production and reduced absorption are reconstructed by exact local detailed balance.

## Interpolation results

| Check | Direct checks | Maximum relative error | Result |
|---|---:|---:|---|
| Energy interpolation | 13,496 | 0.0325955% | PASS (<1%) |
| Radial midpoint interpolation | 540 | 0.0830916% | PASS (<1%) |

Energy-error median and 95th percentile are 0.0043753% and 0.0183945%. Radial-midpoint-error median and 95th percentile are 0.0345250% and 0.0714788%.

The worst energy point is r = 8.482141202 km, x = 0.0608915043, mu-plus longitudinal mode. The worst radial midpoint is 15.500–15.550 km.

The maximum adjacent-radial-node variation is 24.7592% at the extremely narrow interval 22.191893657–22.191894657 km. Its direct midpoint interpolation error is only 3.0783e-7% (relative fraction 3.0783e-9): a neighbor-change indicator is not itself an interpolation error.

## Low-x absorption variation

The maximum x=0.05 to x=0.5 absorption ratios over the 1687 radii are:
- mu-minus longitudinal: 8.4314 at r = 8.24822 km;
- mu-minus transverse: 1.9342 at r = 8.48214 km;
- mu-plus longitudinal: 8.9052 at r = 8.48214 km;
- mu-plus transverse: 1.9410 at r = 8.48214 km.

These are local absorption-rate ratios, not luminosity ratios or integrated emissivity corrections.

## Targeted high-order checks

A separate direct calculation evaluated 431 unique (r,x) points using the order ladder (10,6,6,6) -> (14,8,8,8) -> (18,10,10,10) -> (22,12,12,12) -> (26,14,14,14). The selected set comprises the top 10 radial-neighbor intervals (both endpoints and midpoint at all nine formal knots) and the 10 worst energy-interpolation points (nine knots plus validation point at each selected radius). There were 2,155 nominal ordered evaluations.

- All selected points pass the 0.1% successive-order criterion.
- Maximum successive-order change: 0.0328258%.
- Maximum high-order radial midpoint interpolation error: 0.0831044%.
- Maximum high-order energy PCHIP error: 0.0325566%.
- Maximum detailed-balance residual: 5.3245e-15.
- Maximum final-muon mass-shell residual: 2.4604e-13.
- All rates finite and nonnegative.

## Micro-consistency and provenance

Low-order global maxima: detailed-balance residual 6.8693e-15; final-muon mass-shell residual 2.0432e-13; charge-sum closure residual 0; all rates finite and nonnegative.

Low-order runtime: 366.34 s. Targeted high-order runtime: 334.35 s. Both physics calculations were run directly in the research compute container with four worker processes; CI was not used for the numerical calculation. The profile hash was checked before each run.

## Acceptance boundary

**Passed:** complete 1687-radius low-order B.13 scan for x in [0.05,0.5]; energy interpolation validation at all 1687 radii; top-60 radial midpoint screen; targeted top-10 radial and top-10 energy high-order checks; detailed balance, mass shell, charge closure, and finite/nonnegative checks.

**Not claimed:** exhaustive high-order quadrature at all 1687 x 17 points; midpoint validation of every one of the 1686 radial intervals; support for 0 <= x < 0.05; full-band B.1 source integral; B.2 path optical depth; luminosity; Fig. 7 reproduction; SN1987A update; or axial-vector limit update.

The threshold-adjacent interval 0 <= x < 0.05 must be separately tested before Global-07 can be called a complete energy integral.

Full raw data, chunk files, exact local runner scripts, source inputs, and checksums are packaged in the archive whose SHA-256 is `54b4ce938034d154b2eeb7ede87f720e21eafb24e08f9743380fb313679c05df`.
