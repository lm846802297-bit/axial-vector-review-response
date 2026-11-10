# P1-IIIe-B: SFHo/FRDM v1.03 real-table decoding and local density closure

Date: 2026-11-11  
PR: #57  
Branch: research/moving-muon-thermal-rates-20261107

## 1. Scope

This stage closes the gap recorded in [P1-IIIe-A](B16_P1IIIE_A_EOS_OCCUPATION_IMPLEMENTATION_2026-11-11.md) §6, where the official
Hempel SFHo binary archives "could not be downloaded in the current execution
environment". The four archives listed on the University of Basel EOS page have
now been fetched, byte-verified, decoded, and audited, and the local
density-closure criterion

\[
\xi\,n'_N \;=\; X_N\,n_B
\]

has been tested cell by cell on the published grid. This is a data and
verification stage: it produces no cooling curves, no opacity change, and no
claim on the published Table 1 averages.

Sources:
- University of Basel, M. Hempel, *Equations of state* page and EOS table
  manual v1.04.
- M. Hempel, Phys. Rev. C 91, 055807 (2015), [arXiv:1410.6337](https://arxiv.org/abs/1410.6337),
  Eqs. (91)-(99) and (107).
- D. F. G. Fiorillo et al., JCAP 03 (2026) 053,
  [arXiv:2509.13322v2](https://arxiv.org/abs/2509.13322), Sec. 4.2-4.3 and
  Appendix C.1.

## 2. Provenance and version reconciliation

| Archive | Bytes | SHA-256 |
|---|---:|---|
| `sfho_frdm_bin.zip` | 161 092 071 | `45479eaf…b8949c` |
| `sfho_frdm_spp.zip` | 28 240 340 | `fc0a5f8e…bdf5769` |
| `sfho_frdm_comp.zip` | 45 332 354 | `0d80c5e0…f099ca8ca` |
| `sfho_frdm_shen98format.zip` | 88 043 252 | `deed6c68…eb873a811` |
| `manual_v1.04.pdf` | 213 440 | `0994abc5…bb4b5478` |

The full hashes and the per-file hashes of the extracted tables are written into
`outputs/p1iii_eos_sfho_realdata_closure_2026-11-11.json` (`provenance`).

The archive name (`v1.0` directory) and the table names (`v1.03`) differ from the
manual version (`v1.04`); this is not a version mismatch. The official version
history states that v1.03 (2012-07-09) uploaded the SFHo and SFHx tables, and
v1.04 (2012-12-19) only added the IUFSU table and updated the manual figure. The
SFHo/FRDM data are therefore v1.03 data, and the v1.04 manual is their manual.
The single-particle table was posted later (2014-10-23) but is also labelled
v1.03.

Grid (manual Eqs. 2-4): 81 temperatures \(T=0.1\cdot10^{0.04(i-1)}\) MeV
(0.1-158.489), 61 proton fractions \(Y_{p}=0.01j\), \(j=0..60\) (the
single-particle table has 60 values, no \(Y_p=0\)), and 326 baryon densities
\(n_B=10^{-12}\cdot10^{0.04(k-1)}\) fm\(^{-3}\). For SFHo the interaction has no
solution at Fortran \(k\ge309\): the density rows with array index 308-325 are
exactly zero, so only 308 of the 326 density entries are physical, and the last
physical density is \(n_B=1.9055\) fm\(^{-3}\) (\(\rho_B=3.16\times10^{15}\)
g cm\(^{-3}\)). Every whole-table statistic below is restricted to those 308 rows;
`sfho_eos_tables.NB_PHYSICAL` carries the count so the mask cannot drift.

## 3. Decoded formats

All three binary tables are Intel-Fortran unformatted sequential files with one
record; the file size reconstructs exactly as \(8+8N\), which is the independent
check used in the reader.

- **Extended EOS** `sfho_frdm_eos_v1.03.bin` (231 950 312 B):
  `(81, 61, 326, 18)` in `order="F"`. Columns: 1 \(n_B\), 2 \(Y_p^{\rm tot}\),
  3 \(E_{\rm tot}\) [MeV] (rest mass included), 4 \(p_{\rm tot}\)
  [MeV fm\(^{-3}\)], 5 \(S_{\rm tot}\) [\(k_B\)], 6
  \(\mu_n^{\rm nonrel}=\mu_n-m_n\), 7 \(\mu_p^{\rm nonrel}=\mu_p-m_p\),
  8 \(\mu_e^{\rm nonrel}\) (kinetic only), 9 \(F_{\rm tot}\), 10-16 the mass
  fractions \(X_n,X_p,X_d,X_t,X_h,X_\alpha,X_A\), 17-18 mean \(A\) and \(Z\).
- **Single-particle properties** `sfho_frdm_spp_v1.03.tab` (155 283 075 B,
  ASCII, manual Sec. IX): per temperature block, 60 \(Y_p\) sub-blocks of 326
  rows of 7 columns: \(n_B\) [fm\(^{-3}\)], \(Y_p^{\rm tot}\),
  \(\Sigma_{V,n}^{\rm tot}\), \(\Sigma_{V,p}^{\rm tot}\) [MeV], the filling
  factor \(\xi\), and the Dirac masses \(m_n^*,m_p^*\) [MeV]. 81 blocks and
  1 589 463 lines are verified.
- **Composition** `sfho_frdm_comp_v1.03.bin` (103 284 392 B): one record
  `read(10) az, mass, bind, comp` with \(8140\times2\) int32 nuclide ids,
  8140 nuclear masses and binding energies (MeV), and `comp(81,61,326,8)`.
  Layer 0 is \(\mu_n^{\rm nonrel}\), layer 2 approximately but not exactly
  \(\xi\), layer 3 is the Coulomb-type term of the module, layer 4 is the
  "no nuclei" flag (\(\approx1.0\)), layer 5 is \(n_e=Y_p^{\rm tot}n_B\)
  [MeV\(^3\)], and layers 6-7 are the free neutron and proton densities
  [MeV\(^3\)]. Layer 1 is a proton-side chemical potential whose precise
  definition remains open; it is not used here.

## 4. Whole-table audit (restricted to the 308 physical density rows)

| Check | Result |
|---|---|
| stored \(n_B\) vs nominal grid | \(\max|{\rm rel}|=9.99\times10^{-9}\) |
| stored \(Y_p\) vs nominal \(Y_e\) | \(\max=8.87\times10^{-9}\) |
| mass-fraction closure \(\sum X\) | \(\max=7.46\times10^{-12}\), mean \(1.25\times10^{-14}\) |
| \(F-(E-TS)\) | \(\max|{\rm rel}|=6.80\times10^{-15}\) |
| zero rows at \(k\ge309\) | 1.000000 |
| minimum entropy | \(1.35\times10^{-3}\,k_B\) |
| minimum pressure | \(3.18\times10^{-12}\) MeV fm\(^{-3}\) |
| composition \(n_n\) vs \(X_n n_B(\hbar c)^3\) | \(\max|{\rm rel}|=4.44\times10^{-16}\) |
| cells containing nuclei | 0.75139 |
| nuclide table | 8140 nuclides, \(2\le A\le339\) |
| SPP \(T\) and \(n_B\) vs extended table | \(\max|{\rm rel}|=3.61\times10^{-7}\) (ASCII rounding) |
| SPP ranges | \(\xi\in[0.5206,1]\), \(m_n^*\in[165.72,939.565]\), \(m_p^*\in[164.43,938.272]\), \(\Sigma_{V,n}^{\rm tot}\in[-2.4\times10^{-8},2517.714]\), \(\Sigma_{V,p}^{\rm tot}\in[-5.08,2517.714]\) MeV |

The composition-table free-nucleon densities reproduce the extended-table mass
fractions to machine precision, so the two archives are mutually consistent and
\(n_N=X_N n_B\) is a safe input for the closure test, as required in
P1-IIIe-A §4.

## 5. The filling factor is the excluded-volume closure

For the HS excluded-volume model the filling factor satisfies

\[
\xi = 1-\frac{n_B-n_n-n_p}{n_0},
\qquad n_0=0.15824150805\ {\rm fm}^{-3},
\]

with \(n_N=X_Nn_B\). Using only table columns, the right-hand side reproduces
the tabulated single-particle \(\xi\) for all 224 audited cells with
\(\max|\Delta\xi|=7.57\times10^{-8}\) and median \(5.6\times10^{-12}\). The
single-particle \(\xi\) is therefore the excluded-volume closure itself, not an
independent fit parameter. Per the author's rule the closure test still takes
\(\xi\) from the single-particle table and never from this relation; the
identity is used only as a cross-check.

Twelve cells originally rounded to \(\xi=1+4\times10^{-16}\) and made the
inference raise. That is a printing artifact of a cell with no bound baryons, so
`infer_filling_factor_from_global_densities` now clamps
\(1<\xi\le1+10^{-12}\) to unity and still rejects a genuine violation
(\(n_n+n_p>n_B\) beyond \(10^{-10}\)). The existing unit test for the rejection
path is unchanged and passes.

## 6. Local density closure on the published grid

The audited grid is \(T\in\{0.1,0.251,0.631,1.585,3.981,10,25.119,63.096\}\)
MeV, \(Y_p\in\{0.1,0.2,0.3,0.4\}\), and
\(n_B\in\{1.10\times10^{-12},10^{-10},10^{-8},10^{-6},10^{-4},10^{-2},1\}\)
fm\(^{-3}\), i.e. 224 cells. For each cell the tables supply
\(m_N^*\), \(\Sigma_{V,N}^{\rm tot}\), \(\mu_N^{\rm nonrel}\) and \(\xi\); the
occupation integral of P1-IIIe-A is evaluated with 512-node quadrature and
compared with \(X_N n_B\).

**Validity domain.** All cells with

\[
T\le25.2\ {\rm MeV}\quad\text{or}\quad n_B\ge9.9\times10^{-5}\ {\rm fm}^{-3}
\]

(208 of 224) satisfy the closure:

| Species | cells | median | max |
|---|---:|---:|---:|
| neutron | 208 | \(8.75\times10^{-6}\) | \(6.13\times10^{-4}\) |
| proton (\(X_p\ge10^{-6}\)) | 145 | \(2.98\times10^{-6}\) | \(8.86\times10^{-5}\) |

The proton restriction avoids ratios of denormal densities
(\(X_p\sim10^{-81}\) in the most dilute cold cells, where both sides of the
identity are meaningless but numerically still agree).

**The 16 excluded cells** are all at \(T=63.096\) MeV with
\(n_B\le10^{-4}\) fm\(^{-3}\), and they are not a cluster effect: \(X_n=0.8\),
\(X_p=0.2\), so \(X_{\rm free}=1\). There the single-particle state saturates:

| \(n_B\) [fm\(^{-3}\)] | \(\nu_n/T\) | reconstructed \(n'_n\) | \(X_n n_B\) | ratio |
|---:|---:|---:|---:|---:|
| \(1.10\times10^{-12}\) | \(-14.891\) | \(9.19\times10^{-8}\) | \(8.8\times10^{-13}\) | \(1.05\times10^{5}\) |
| \(10^{-10}\) | \(-14.891\) | \(9.20\times10^{-8}\) | \(8.0\times10^{-11}\) | \(1.15\times10^{3}\) |
| \(10^{-8}\) | \(-14.85\) | \(9.60\times10^{-8}\) | \(8.0\times10^{-9}\) | \(1.20\times10^{1}\) |
| \(10^{-6}\) | \(-12.71\) | \(8.10\times10^{-7}\) | \(8.0\times10^{-7}\) | \(1.01\) |

The reconstructed density is constant to \(4.9\times10^{-4}\) across two decades
of \(n_B\) while the target density falls by \(10^{2}\). In other words the
tabulated \(\mu_N^{\rm nonrel}\) at this temperature stops responding below
\(n_B\sim10^{-8}\) fm\(^{-3}\); the table carries no resolution there rather
than a wrong normalization. Those cells are also physically remote: at
\(T=63\) MeV and \(n_B=10^{-6}\) fm\(^{-3}\) the dilution is
\(n_B/T^3\approx4\times10^{-10}\). The test suite asserts this frozen-density
behaviour and the large residual explicitly, so the excluded corner cannot
silently change.

## 7. Code and tests

- **`sfho_eos_tables.py`** — standalone readers for the three formats plus
  `sha256_file`, the nominal grids, `NB_PHYSICAL`, and the column names. No
  SciPy dependency.
- **`audit_b16_p1iii_eos_sfho_realdata_closure.py`** — loads the archives,
  reproduces the whole-table audit of Sec. 4, runs the closure grid of Sec. 6,
  and writes both the JSON record and a 224-row profile-format fixture.
- **`test_b16_p1iii_eos_sfho_realdata.py`** — 10 tests. Seven run from the
  committed fixture alone (grid coverage, \(\xi\) identity, domain closure,
  frozen-density corner, \(F^{\rm deg}\in(0,1]\), and an end-to-end pass through
  `load_profile_csv` + `aggregate_profile_rows`); three whole-table tests run
  only when `SFHO_TABLES_DIR` points at an extracted copy, otherwise the class
  is skipped. CI therefore exercises the fixture path and does not need the
  400 MB binaries.
- **`outputs/p1iii_eos_sfho_realdata_fixture.csv`** — 224 rows of real
  table values in the P1-IIIe-A Hempel column layout
  (`mstar_N`, `SigmaV_N`, `mu_nonrel_N`, `xi`, `X_N`, targets, and the audited
  `nprime`, `ratio`, `Fdeg` columns).
- **`.github/workflows/b16-p1iii-eos-degeneracy.yml`** — now also triggers on
  the three new files and runs the new test module.

Reproduction:

```
set SFHO_TABLES_DIR=<...>\eos-sfho-frdm-v1.0\extracted
python audit_b16_p1iii_eos_sfho_realdata_closure.py --tables-dir %SFHO_TABLES_DIR% \
    --fixture outputs/p1iii_eos_sfho_realdata_fixture.csv
python -m unittest test_b16_p1iii_eos_sfho_realdata -v
```

## 8. Repairs made in this stage

1. **Corrupted newlines in the P1-IIIe-A module and workflow.** The file
   `audit_b16_p1iii_eos_nucleon_distribution.py` contained literal backslash-`n`
   character pairs instead of real line breaks at three places, and the workflow
   at three more. The module therefore failed to import at all
   (`SyntaxError: unexpected character after line continuation character`), so
   every test that imports it failed at collection. Both files are repaired and
   the 15 P1-IIIe-A tests now pass locally. The workflow was likewise invalid
   YAML at that line. Both defects are real, but they are **not** the cause of the
   observed 3-second failure runs, whose job API reports no steps: the check-run
   annotation on the first run of this commit reads "The job was not started
   because recent account payments have failed or your spending limit needs to be
   increased", and no runner is ever assigned. That is an account-level billing
   condition, independent of these files and not repairable inside the
   repository. No CI result is claimed for this commit; the local evidence above
   stands on its own.
2. **Density-row masking off by one.** Whole-table statistics previously ranged
   over all 326 rows, so the zero rows at \(k\ge309\) produced spurious maxima
   (relative density deviation 1.0, \(\sum X\) residual 1.0, minimum entropy 0).
   They are now masked with `NB_PHYSICAL`, and the reported maxima are the ones
   in Sec. 4.
3. **\(\xi\) rounding clamp** described in Sec. 5.

## 9. Validation boundary

- No Garching profile data are used or fabricated. The fixture carries real EOS
  values but uniform weights, so the aggregate averages it produces are a code
  path exercise, not a physical result, and are not quoted.
- The published Table 1 values 0.80, 0.77, 0.48, 0.42 remain **not
  reproduced**.
- `sfho_frdm_shen98format.zip` was downloaded and hash-verified but is not used
  here: its effective mass is the density-weighted average
  \((n_nm_n^*+n_pm_p^*)/(n_n+n_p)\), which cannot be separated into species.
- The composition module's \(n_A\) formula was re-implemented and validated
  against the tables elsewhere: it reproduces the peak nuclide and
  \(\langle A\rangle,\langle Z\rangle\) exactly, and overproduces the total bound
  baryon density by up to a factor 2 in cluster-dominated cells. This does not
  affect the present chain, which uses the free-nucleon densities stored directly
  in composition layers 6-7, but it must be settled before any cluster-based
  response is built.
- Composition layer 1 (a proton-side chemical potential that is neither
  \(\mu_p\) nor \(\mu_p-\mu_e\)) and layer 3 remain unidentified; neither is used.
- The quadrature is a fixed-node Gauss-Legendre rule with a \(45T\) kinetic
  tail; the P1-IIIe-A convergence test bounds its error at the \(10^{-10}\) level
  for the states used here.

## 10. Next stage

P1-IIIe-B is complete as a data and closure stage. The remaining work toward the
dynamic response (P1-IIIe-C) is:

1. assemble a local \(T\), \(n_B\), \(Y_p^{\rm tot}\) profile (Garching, or an
   explicitly labelled reconstruction) and interpolate these tables onto it;
2. produce local \(F_{pp}^{\rm deg}\), \(F_{nn}^{\rm deg}\) through the CSV
   interface, with the mass-time weighting supplied by the profile rather than
   uniform weights;
3. check the density closure cell by cell on that profile, respecting the
   \(T\le25.2\) MeV or \(n_B\ge9.9\times10^{-5}\) fm\(^{-3}\) domain of Sec. 6 and
   recording any sampled cell that falls outside it;
4. only then insert the EOS quasiparticle dispersion into the dynamic weak
   response, keeping the single filling factor \(\xi\) as the volume
   normalization.
