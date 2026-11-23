# B.13 targeted-validation coverage of the B.16 10 MeV Fig. 7 benchmark

The B.13 high-order targeted run and the B.16 literal Fig. 7 calculation validate different parts of phase space. Here only the **published B.16 fixed-local-energy, Euclidean-chord, 10 MeV pure-vector semi-Compton source and optical-depth weight** are inspected. No B.13 rate is transplanted or interpolated. This is not a rate correction, a luminosity or bounds result, or a statement about all available B.13 calculations.

## Exact input pins

- B.16 frozen grid and prior sensitivities: [13-file weighted package at #121, commit 972f282a](https://github.com/lm846802297-bit/axial-vector-review-response/tree/972f282a2958aa39ada1c630901cc5720a451ea2/research/stellar-cooling-constraints-20261105/blinov_reproduction/fig7-10mev-weighted-sensitivity). Its parent work remains unchanged at [#121 recoil-domain commit 67ea927](https://github.com/lm846802297-bit/axial-vector-review-response/tree/67ea927f4eecf95ef27122ed29a3be32afe88f78/research/stellar-cooling-constraints-20261105/blinov_reproduction/fig7-10mev-recoil-domain). The profile is a reconstructed SFHo‑18.8 public-figure profile, not the original simulation snapshot.
- Target envelope: [local primary high-order B.13 target points at PR #133 commit 1dc11be](https://github.com/lm846802297-bit/axial-vector-review-response/blob/1dc11be3f6b3b6ac72b03fc610022fe4407fa5af/research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/results/P1B_GLOBAL06B_THRESHOLD_EDGE_FULL_RADIAL_2026-11-18/HIGH_ORDER_RERUN_2026-11-22/LOCAL_HIGH_ORDER_TARGETED_POINTS.json). Same local-energy definition $x=(\omega-m)/T(r)$, verified from the raw values at all 431 points. Raw input Git blob `050e1f3aad8cba77d499a0dbf743ad8268acc14e`, SHA-256 `f8287ce92b4a2dd241928197a28b27bd655b0e2a23895478b40f30c49f9d313e`. The 431 pairs are irregularly distributed across 39 radii and 17 $x$ values.
- B.1/B.2 physical convention: [Blinov et al., Appendix B, Eqs. (17)–(21) and (29)–(35)](https://arxiv.org/html/2511.09619v2).

## Method

The maximum sampled target energy is 11.962483967 MeV. The inclusive envelope contains all raw targets, but admits many more points: $8.45\leq r\leq 22.191894657$ km, $0\leq x\leq0.05$, and $\omega\leq11.962483967$ MeV. An energy-only cap admits every radius and is weaker still. A reported envelope weight is an **upper bound on overlap with the targeted domain as defined by these coordinates**. It is not a measure of fully validated interpolation or continuum kernel coverage.

For the B.1 source, evaluate the mask at the radius of production. The thin and escaping source weights are $J_C$ and $J_C e^{-\tau}$, where $C$ is the semi-Compton channel. For B.2, the opacity weight is $J_{\rm total}e^{-\tau}\,d\tau_C$ along the fixed-energy path. Apply the radius and local-temperature mask to each path quadrature node using the unaltered rate and geometry; never apply the emission-radius mask to path opacity. Ratios are to the corresponding unmasked total. Exact original source, opacity and energy grid hashes are required. The luminosities and source/opacity tangents at the three selected couplings close against the pinned baseline within $2.23\times10^{-16}$.

The exact source exclusion has an independent continuous check for the archived piecewise-linear profile. At each of 794 intervals spanning the target radii, bound the local production threshold gap below by $m/\max(N_0,N_1)-m-x_{\max}\max(T_0,T_1)$. The minimum bound is positive, **0.606945 MeV**. Therefore $\omega\geq m/N(r)$ for B.1 and $x\leq0.05$ are incompatible throughout this radius interval, not just at the B.16 quadrature nodes. This check uses the profile interpolation, not a continuum claim about the numerical optical-depth bounds.

## Results

All entries below are fractions, not percentages.

| B.16 semi-Compton measure | Energy-only upper bound | Full inclusive envelope upper bound |
|---|---:|---:|
| Thin B.1 source | $3.472\times10^{-6}$ | 0 |
| Escaped source, weak point | $3.438\times10^{-6}$ | 0 |
| Escaped source, published peak point | $2.066\times10^{-8}$ | 0 |
| Escaped source, last visible point | $7.362\times10^{-21}$ | 0 |
| Escape-weighted B.2 depth, weak point | $2.092\times10^{-4}$ | $6.371\times10^{-5}$ |
| Escape-weighted B.2 depth, published peak point | $1.619\times10^{-7}$ | $2.489\times10^{-8}$ |
| Escape-weighted B.2 depth, last visible point | $4.578\times10^{-21}$ | $7.410\times10^{-45}$ |

The 431-point B.13 targeted high-order check therefore does **not** validate the B.16 strong-tail source or opacity region. Its numerical success for the near-threshold targets is not in question. The extremely small last opacity fraction is a native quadrature diagnostic, not a precision claim about a continuous high-energy cross section. The less restrictive energy-only cap gives the same qualitative separation. These results do not establish whether another broader B.13 archive covers the dominant region or explain the +92.4284% strict-vs-plotted Fig. 7 residual.

## Replay

Put the exact #121 weighted package directory at `baseline/`, and the pinned #133 JSON at `pr133-target-points.json`. A portable local archive includes these inputs; a repository version can use the pinned inputs without duplicating them. Run on Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0:

```sh
(cd baseline && sha256sum -c SHA256SUMS)
sha256sum -c SHA256SUMS
OPENBLAS_NUM_THREADS=1 python -m unittest -v test_overlap
OPENBLAS_NUM_THREADS=1 python overlap.py /tmp/fig7-b13-overlap-replay.json
cmp native.json /tmp/fig7-b13-overlap-replay.json
```

The tests exercise malformed/duplicate target rows, local-temperature mask selection, the interval gap certificate, and full-mask equivalence against the reference B.2 chord routine (fixed tolerance $2\times10^{-15}$, observed maximum $9.53\times10^{-16}$ in the synthetic control). The early numerical output without a gap certificate is retained locally separately and not the native output for this packet.
