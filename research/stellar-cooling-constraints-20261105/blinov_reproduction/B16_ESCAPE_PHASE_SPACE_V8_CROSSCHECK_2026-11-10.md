# B.16 10 MeV escape phase-space: direct V8 cross-check

Date: 2026-11-10  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`  
Input HEAD: `531c58a6564169fee5bc9e8bd5a2f21cb81f3848`  
Result JSON: [`b16_escape_phase_space_10mev_2026-11-10_v8_crosscheck.json`](outputs/b16_escape_phase_space_10mev_2026-11-10_v8_crosscheck.json)

## Scope

This is a direct double-precision execution of a V8/JavaScript port of the formulas in the existing `audit_b16_escape_phase_space.py` and `reference.py`. It uses the exact PR profile and Fig. 7 digitization, the 10 MeV strongest Fig. 7 coupling, the fixed-`omega` Eq. (B.2) chord prescription, and the requested quadrature orders:

- source radius: 200 nodes;
- opacity radius: 642 nodes (order 640 plus endpoints);
- energy: 842 nodes (order 200 plus lapse-threshold nodes);
- direction: 32 nodes;
- path: 64 nodes.

The profile SHA-256 and Fig. 7 SHA-256 match the archived B.16 baseline. All node counts, the coupling, and the integrated luminosity/source closure are checked against the archived result.

## Integrated closure

At (g=4.17168965e-8):

- calculated luminosity: (L=2.43963596e+52\,\mathrm{erg\,s^{-1}});
- archived B.16 luminosity: (L_0=2.43963596e+52\,\mathrm{erg\,s^{-1}});
- relative luminosity closure residual: `-9.2293e-13`;
- relative optically-thin source closure residual: `-8.7375e-14`;
- absolute escape-probability residual: `-2.7176e-16`;
- maximum source/escaped marginal and joint partition residual: `9.2104e-13`;
- direction weights sum to `1.0000000000000002`.

The result is (+92.428%) relative to the digitized Fig. 7 strong-end luminosity.

## Source and escape selection

- (8	ext{--}15\,\mathrm{km}) contributes `79.652%` of the optically-thin B.1 source.
- The neutrino inverse-decay and Compton production fractions are `67.926%` and `32.074%`, respectively.
- The 8--15 km region carries `86.855%` of the escaping luminosity.
- The global escape probability is `3.251774e-4`.

### Largest global joint cells

| Emission shell | Energy bin | Direction bin | B.1 source fraction | Escaping-luminosity fraction |
|---|---|---|---:|---:|
| 8-10 km | 210-510 MeV | 0.5-1 cos(theta) | 1.563% | 30.591% |
| 10-12 km | 210-510 MeV | 0.5-1 cos(theta) | 0.434% | 15.436% |
| 10-12 km | 110-210 MeV | 0.5-1 cos(theta) | 2.295% | 8.688% |
| 8-10 km | 210-510 MeV | 0-0.5 cos(theta) | 1.357% | 7.421% |
| 8-10 km | 110-210 MeV | 0.5-1 cos(theta) | 4.316% | 7.364% |
| 5-8 km | 210-510 MeV | 0.5-1 cos(theta) | 0.555% | 5.549% |
| 10-12 km | 210-510 MeV | 0-0.5 cos(theta) | 0.377% | 3.841% |
| 12-15 km | 110-210 MeV | 0.5-1 cos(theta) | 0.537% | 3.535% |
| 12-15 km | 210-510 MeV | 0.5-1 cos(theta) | 0.032% | 1.785% |
| 5-8 km | 210-510 MeV | 0-0.5 cos(theta) | 0.482% | 1.494% |
| 10-12 km | 110-210 MeV | 0-0.5 cos(theta) | 1.993% | 1.363% |
| 5-8 km | 110-210 MeV | 0.5-1 cos(theta) | 1.796% | 1.282% |


## Energy and direction selection: main finding

The marginal distributions show that the escaping luminosity is not representative of the B.1 source spectrum:

| Energy interval | B.1 source fraction | Escaping-luminosity fraction |
|---|---:|---:|
| 60-110 MeV | 35.925% | 0.963% |
| 110-210 MeV | 33.611% | 24.674% |
| 210-510 MeV | 9.670% | 69.756% |
| 510-1010.0000000010101 MeV | 0.021% | 1.170% |

The (E=210	ext{--}510\,\mathrm{MeV}) bin contains only `9.670%` of the optically-thin source but carries `69.756%` of the escaping luminosity. Combining all (E>210\,\mathrm{MeV}) bins gives `9.691%` of the source and `70.926%` of the escaped luminosity.

| Initial direction (cos\theta) | B.1 source fraction | Escaping-luminosity fraction |
|---|---:|---:|
| -1--0.5 cos(theta) | 26.758% | 0.883% |
| -0.5-0 cos(theta) | 23.242% | 2.875% |
| 0-0.5 cos(theta) | 23.242% | 17.592% |
| 0.5-1 cos(theta) | 26.758% | 78.650% |

Thus outward directions ((cos\theta>0)) account for `96.242%` of the escaped luminosity, while inward directions account for only `3.758%`. The most important joint cell is (r=8	ext{--}10\,\mathrm{km}), (E=210	ext{--}510\,\mathrm{MeV}), (cos\theta=0.5	ext{--}1): it contains `1.563%` of the B.1 source and `30.591%` of the total escaping luminosity. The top five joint cells together carry `69.500%` of the escaped luminosity.

The (8	ext{--}15\,\mathrm{km}) emission region contributes `79.652%` of the B.1 source and `86.855%` of the escaping luminosity. The dominant escaping component is therefore selected jointly by high energy, outward initial direction, and emission in the inner (8	ext{--}15\,\mathrm{km}) region.

This identifies the next targeted physics check: inspect the high-energy source and absorption kernels in the (E=110	ext{--}510\,\mathrm{MeV}) range, especially their separate neutrino-inverse-decay and semi-Compton contributions. Do not change the energy cutoff, opacity, or source normalization on the basis of this diagnostic alone.

## Important acceptance qualification

This is a cross-runtime numerical cross-check, **not** the strict Python runbook acceptance. The source/opacity/energy node counts and physical quadrature prescription match, and the integral closures are at the (10^{-12}) level; however, the bitwise SHA-256 hashes of the grids generated by V8 Newton roots differ from the archived NumPy `leggauss/geomspace` grid hashes. The JSON records this explicitly. It must not be relabeled as a bitwise-identical NumPy run.

No opacity, stellar profile, source kernel, vector baseline, or axial-vector output is changed. No empirical rescaling is applied. The canonical Python script and runbook remain the strict reproduction path.
