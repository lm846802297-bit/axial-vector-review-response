# 10 MeV high-energy B.2 fixed-energy versus path-redshift audit

Date: 2026-11-10  
PR: #57  
Branch: `research/moving-muon-thermal-rates-20261107`  
Input PR head: `8406eb809d2485f2489645bc1d05a7e42aaabb67`  
Machine-readable result: [b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-10.json](outputs/b16_high_energy_fixed_omega_vs_redshift_10mev_2026-11-10.json)

## 1. Purpose

The previous 210--510 MeV opacity and outer-temperature audits establish that the high-energy escape tail is numerically stable and weakly sensitive to a broad temperature variation in the off-frame 22--25 km shell. The remaining B.2 convention question is whether the energy in the path kernel is held fixed, as printed, or is updated according to conserved energy at infinity.

This calculation compares the two prescriptions **only for the 210--510 MeV emission-energy band**. The B.1 source distribution is identical in both cases.

## 2. Definitions

Printed-equation baseline:
[
\omega_{\rm local}(s)=\omega_{\rm source},\qquad
v(s)=\sqrt{1-m_V^2/\omega_{\rm source}^2}.
]

Path-redshift sensitivity:
[
\omega_{\rm local}(s)=\omega_{\rm source}
\frac{N(r_{\rm source})}{N(r(s))},\qquad
v(s)=\sqrt{1-m_V^2/\omega_{\rm local}(s)^2}.
]

The second prescription updates the local thermal kernel, reduced absorption, and velocity along the ray while retaining the same Euclidean straight chord. It is not a full GR ray trace and is not substituted for the printed B.2 baseline.

## 3. Numerical closure

At (m_V=10\,\mathrm{MeV}), (g=4.171689650228597\times10^{-8}), the fixed-`omega` branch reproduces the previously archived high-energy phase-space integral:

- B.1 source relative residual: `-3.331e-16`;
- fixed-`omega` escaped-integral relative residual: `0.000e+0`;
- fixed-`omega` escape probability: `2.345801e-3`.

The same B.1 source is used for the redshifted path variant.

## 4. Main result

| Quantity | Fixed `omega` | Path-redshift |
|---|---:|---:|
| B.1 source, per (g^2) | (4.16859\times10^{69}) | identical |
| Escape probability | 2.345801e-3 | 1.686751e-3 |
| Source-weighted mean (	au) | 7.7193 | 8.1169 |
| Escaped luminosity | (1.70178\times10^{52}) | (1.22367\times10^{52}) erg/s |

The path-redshift prescription lowers the 210--510 MeV escaped luminosity by **-28.09%** relative to the fixed-`omega` baseline. The source-weighted mean optical depth increases by 5.15%.

### Sub-band response

| Emission-energy bin | Fixed-`omega` escape probability | Path-redshift escape probability | Escaped-luminosity change |
|---|---:|---:|---:|
| 210-300 MeV | 1.6308e-3 | 1.1308e-3 | -30.66% |
| 300-510 MeV | 5.4424e-3 | 4.0942e-3 | -24.77% |

The lower 210--300 MeV part of the dominant tail is more sensitive than the 300--510 MeV part.

## 5. Interpretation

This establishes that the B.2 energy convention materially affects the dominant high-energy escaping component: it is not a negligible correction. It is also distinct from the outer-temperature sensitivity, which changed this same high-energy band by less than 0.4% even under a broad (pm30\%) stress of the 22--25 km temperature.

The path-redshift variant is nevertheless not the published baseline. The paper's displayed B.2 integrand keeps the same (omega) in the local rate and vector speed along the chord; the fixed-`omega` calculation remains the literal equation-level reproduction. The redshifted calculation is a sensitivity test motivated by the main-text energy-at-infinity language. It retains Euclidean chords and does not include proper spatial metric factors or ray bending.

The global 10 MeV path-redshift diagnostic previously reduced the strong-endpoint Fig. 7 residual from +92.24% to +36.74%, but did not close it. This energy-resolved result shows that the convention shift acts directly on the high-energy tail that carries most of the escaped luminosity; it does not demonstrate which convention the unpublished numerical code used.

## 6. Decision

1. Retain fixed-`omega` B.2 as the published-equation reproduction baseline.
2. Keep path-redshift as a separate physical sensitivity, not as an empirical correction.
3. Do not adjust the outer temperature, opacity normalization, energy cutoff, or coupling to force agreement.
4. The remaining order-one difference cannot be assigned to numerical integration; the key unresolved physical inputs are the exact same-snapshot stellar profile and the interpretation of B.2 in the unpublished implementation.

No production axial-vector result or constraint curve is modified.
