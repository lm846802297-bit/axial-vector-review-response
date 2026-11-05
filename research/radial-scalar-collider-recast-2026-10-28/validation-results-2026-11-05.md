# PR #52 local validation record — 2026-11-05

**Model scope:** original paper's single-VEV \(S+\mathrm{VLL}\) model only.  
**Branch:** research/radial-scalar-original-model-belleii-20261105  
**Purpose:** record exactly what was locally tested. This is not an experimental benchmark reproduction or collider exclusion.

## 1. Exact source snapshot used

The following local files were checked against the Git blob SHA-1 values returned for the PR branch:

| File | Git blob SHA-1 | Match |
|---|---|---|
| radial_scalar_widths.py | afb583c46dc66f188e606ad39de5501c38c8945f | Yes |
| test_radial_scalar_widths.py | beaf2e10438bf9f525f27e1d1a2cea8ab9d985a1 | Yes |
| fetch_belleii_supplements.py | 935e18cff36a48e31727019b3f4327ede203d4a4 | Yes |
| test_fetch_belleii_supplements.py | 531a9b7affbdf07510dcc2b0b733b162216f3c63 | Yes |

## 2. Local test result

Environment: Python 3.13.5.

Command:
```bash
python -m unittest -v
```

Result: **14 tests passed**.

Coverage:

- fermion and vector-pair kinematic thresholds;
- mass-proportional UV Yukawa and \(v_s\) relation;
- incomplete-channel bookkeeping and the explicit completeness guard for \(c\tau\);
- Belle II normalization \(\xi=v/v_s\);
- the conditional \(\sqrt{\mathrm{BR}_{\rm benchmark}/\mathrm{BR}_{\rm UV}}\) coupling-limit rescaling;
- the \(\tau^+\tau^-\) threshold effect in the original UV model;
- suppression of the direct tau channel when \(s\to A'A'\) is open;
- deterministic SHA-256 calculation and rejection of empty, HTML, and access-block payloads by the supplement downloader.

## 3. Analytic/numerical diagnostics

Using \(m_\mu=0.1056583755\,\mathrm{GeV}\), \(m_\tau=1.77686\,\mathrm{GeV}\), and the mass-proportional UV Yukawas:

| \(m_s\) (GeV) | \(\mathrm{BR}_{\tau\tau}^{(\mu+\tau)}\) | \(\mathrm{BR}_{\mu\mu}^{(\mu+\tau)}\) |
|---:|---:|---:|
| 3.6 | 0.5372 | 0.4628 |
| 3.7 | 0.8598 | 0.1402 |
| 4.0 | 0.9649 | 0.0351 |
| 5.0 | 0.9900 | 0.0100 |
| 6.0 | 0.9933 | 0.0067 |
| 8.0 | 0.9951 | 0.0049 |
| 10.0 | 0.9957 | 0.0043 |

These are two-channel fractions with only \(\mu^+\mu^-\) and \(\tau^+\tau^-\) included and with \(s\to A'A'\) closed. They are not full UV branching fractions.

For \(m_{A'}\ll m_s\), the analytic ratio \(\Gamma(s\to A'A')/\Gamma(s\to\tau^+\tau^-)\) is approximately 251 at \(m_s=3.6\,\mathrm{GeV}\), 13.1 at 4 GeV, 5.69 at 5 GeV, and 9.70 at 10 GeV. This identifies a potentially dominant open channel; it does not constitute an experimental constraint.

## 4. What this validation does not establish

- The official APS supplemental files have **not** been downloaded into the repository.
- No raw mass grid, observed cross-section row, expected limit, or coupling-limit row has been transcribed.
- Neither Belle II scalar benchmark has been numerically reproduced.
- No detector efficiency or likelihood has been recomputed.
- No model-specific exclusion, allowed interval, or point classification has been produced.
- The downloader tests validate local payload checks only; they do not demonstrate successful access to APS.
- No GitHub Actions/CI run is claimed.

The next evidence gate is to retrieve the three official files, archive them verbatim with SHA-256 hashes, parse their schemas, and reproduce the Belle II scalar benchmark before any UV reinterpretation.
