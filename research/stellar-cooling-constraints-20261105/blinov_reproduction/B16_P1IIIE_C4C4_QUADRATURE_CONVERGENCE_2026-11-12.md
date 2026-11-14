# P1-IIIe-C4-C4-Aq: energy-dependent combined quadrature convergence

Date: 2026-11-12  
Branch: `research/c4c4-energy-dependence-20261112`  
Status: completed; 80-case combined-order comparison archived; physical validation not claimed.

## 1. Why this stage is required

C4-C4-A has produced 80 new local rates at five energies using the C4-C2 base orders (8,48,36,12). The C4-C2 100-MeV baseline has its own earlier energy, angle, and kernel-order checks, but those checks do not establish convergence at the new incident energies.

Before extending C4-C4 to all 301 radial points, the five new energy slices must be checked against a higher-order calculation.

## 2. Comparison

For each of the 80 new cases (five energies × four radii × neutron/proton × neutrino/antineutrino), compare:
- base: (N_cos,N_E',N_p,N_phi)=(8,48,36,12);
- high: (N_cos,N_E',N_p,N_phi)=(12,72,48,16).

All four quadrature dimensions are increased simultaneously. The exact outgoing-energy support is recomputed with the same 10,001-point root scan and 45T momentum-tail cutoff. The base value is read from the byte-pinned C4-C4-A archive; it is not recomputed.

The relative difference is
\[
\delta_{\rm quad}=\left|\frac{\Gamma_{\rm high}}{\Gamma_{\rm base}}-1\right|.
\]
The working acceptance threshold is 1% for every case.

## 3. Interpretation of outcomes

- If all 80 cases satisfy the 1% threshold, the C4-C4-A rates are stable under the combined order increase.
- If any case exceeds 1%, all high-order diagnostic results are still archived. The responsible quadrature dimensions must then be isolated (outgoing energy, angle, initial momentum, azimuth) before changing the production settings.
- A combined-order pass does not separately quantify the error of each quadrature dimension.

The result is a numerical convergence diagnostic, not a physical transport or literature-reproduction acceptance.

## 4. Data and source provenance

The base C4-C4-A CSV is pinned by Git blob SHA:
`8be3757cf28011132a82b5c2373aa3c1fa59d342`.

C4-B2, C4-C1, C4-C2 source files and the C1/C2 EOS inputs are reused unchanged. No 100-MeV baseline, C4-C3 301-radius archive, transport result, or axial cooling limit is overwritten.

## 5. Next stage

Only after this combined quadrature check passes should C4-C4-B extend the energy scan to all 301 radial points. If it fails, isolate the quadrature dimension(s) responsible and repeat the affected cases with a justified refined order.


## Execution update — 2026-11-13

The archived 80-row comparison has been independently inspected.

- All 80 expected energy/radius/target/sign combinations are present.
- Every base and high-order rate is finite and positive.
- The maximum support-root relative residual is \(5.06778\times10^{-13}\).
- The maximum combined-order relative difference is \(8.30690\times10^{-5}\) (0.00831%), below the 1% working threshold.
- The largest per-energy difference occurs at 20 MeV; the per-energy maxima are preserved in the machine-readable summary.

This is a combined quadrature-order stability check at four anchor radii. It is not a pointwise convergence proof over all 301 radii and is not a physical transport or literature-reproduction acceptance.
