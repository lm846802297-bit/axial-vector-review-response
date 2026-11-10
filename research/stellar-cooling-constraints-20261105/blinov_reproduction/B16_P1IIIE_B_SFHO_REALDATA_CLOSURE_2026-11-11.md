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

**Reproducible acquisition.** The archives are not committed (323 MB in total,
GitHub rejects files above 100 MB). `sfho_frdm_v1.03_download.py` fetches them
from the published URLs with the standard library only, verifies the size and the
SHA-256 of every file, and renames `<name>.part` only after both match;
`sfho_frdm_v1.03_manifest.sha256` is the same list in `sha256sum -c` form. The
verification that this work actually relies on was run on 2026-11-11 against the
local copies: `--verify-only` reports `OK` for all five files, and `--check-urls`
reports HTTP 200 with a `Content-Length` equal to the recorded byte count for all
five URLs, this verifies endpoint reachability and advertised size, not the remote content hash. A real
fetch of the smallest file (`--only manual`) was also exercised end to end. An
offline test (`ArchiveManifestTests`) keeps the manifest and the downloader's
`FILES` table in agreement, because a truncated hash is otherwise silent.

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

| nuclide table | 8140 nuclides, \(2\le A\le339\) |
| SPP \(T\) and \(n_B\) vs extended table | \(\max|{\rm rel}|=3.61\times10^{-7}\) (ASCII rounding) |
| SPP ranges | \(\xi\in[0.5206,1]\), \(m_n^*\in[165.72,939.565]\), \(m_p^*\in[164.43,938.272]\), \(\Sigma_{V,n}^{\rm tot}\in[-2.4\times10^{-8},2517.714]\), \(\Sigma_{V,p}^{\rm tot}\in[-5.08,2517.714]\) MeV |

The nuclei-containing-cell fraction is now computed with the 308-row physical mask in the audit code. Its updated whole-table numerical value is not claimed here because the raw composition archive was not re-read during this follow-up.

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

The Hempel-to-Fiorillo occupation mapping is written explicitly to avoid
overloading the symbol \(\mu_N^*\). Fiorillo's kinetic-energy convention is

\[
f_N(p)=\left[
\exp\left(\frac{U_N+K_N(p)-\mu_{N,F}^*}{T}\right)+1
\right]^{-1},
\qquad K_N(p)=\sqrt{p^2+m_N^{*2}}-m_N^*.
\]

The Hempel single-particle table supplies

\[
U_N=m_N^*-m_N+\Sigma_{V,N}^{\rm tot},
\qquad \mu_{N,F}^*=\mu_N^{\rm nonrel}.
\]

Consequently,

\[
\nu_N=\mu_{N,F}^*-U_N
=\mu_N^{\rm nonrel}+m_N-m_N^*-\Sigma_{V,N}^{\rm tot}.
\]

In the equivalent relativistic-dispersion convention,

\[
f_N(p)=\left[
\exp\left(\frac{\sqrt{p^2+m_N^{*2}}-\widetilde\mu_N}{T}\right)+1
\right]^{-1},
\qquad
\widetilde\mu_N=\mu_N^{\rm nonrel}+m_N-\Sigma_{V,N}^{\rm tot}.
\]

Thus \(\widetilde\mu_N\) is not Fiorillo's \(\mu_{N,F}^*\), and the
quantity approaching the low-density floor is \(\nu_N/T\), not
\(\mu_N^{\rm nonrel}/T\).

## 6. Local density closure on the published grid

The audited grid is \(T\in\{0.1,0.251,0.631,1.585,3.981,10,25.119,63.096\}\)
MeV, \(Y_p\in\{0.1,0.2,0.3,0.4\}\), and
\(n_B\in\{1.10\times10^{-12},10^{-10},10^{-8},10^{-6},10^{-4},10^{-2},1\}\)
fm\(^{-3}\), i.e. 224 cells. The following validity classification applies
only to these sampled cells; it is not a continuous-domain guarantee. For each
cell the tables supply
\(m_N^*\), \(\Sigma_{V,N}^{\rm tot}\), \(\mu_N^{\rm nonrel}\) and \(\xi\); the
occupation integral of P1-IIIe-A is evaluated with 1024-node quadrature and
compared with \(X_N n_B\).

**Validated subset of this sampled grid.** All cells with

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

**The 16 cells outside the sampled acceptance domain** are all at
\(T=63.096\) MeV, with four \(Y_p\) values at each of
\(n_B=1.10\times10^{-12},10^{-10},10^{-8},10^{-6}\) fm\(^{-3}\).
They are all nucleon-only in composition,
\(X_n+X_p=1\), with \(X_n\simeq1-Y_p\) and \(X_p\simeq Y_p\);
they are not all the fixed \((X_n,X_p)=(0.8,0.2)\) case.

| \(n_B\) [fm\(^{-3}\)] | behaviour | neutron ratio range | proton ratio range |
|---:|---|---:|---:|
| \(1.10\times10^{-12}\) | clear density plateau | \(9.31\times10^4\)--\(1.40\times10^5\) | \(2.13\times10^5\)--\(8.54\times10^5\) |
| \(10^{-10}\) | clear density plateau | \(1.02\times10^3\)--\(1.53\times10^3\) | \(2.34\times10^3\)--\(9.36\times10^3\) |
| \(10^{-8}\) | transition region | \(10.72\)--\(15.83\) | \(23.91\)--\(94.14\) |
| \(10^{-6}\) | closer to closure, still outside \(10^{-3}\) | \(1.010\)--\(1.023\) | \(1.052\)--\(1.562\) |

Only the eight lowest-density cells show the clear chemical-potential floor:
for neutrons \(\nu_n/T\simeq-14.891\), with
\(n'_n\simeq9.19\times10^{-8}\) fm\(^{-3}\). The four
\(10^{-8}\) cells are transitional, and the four \(10^{-6}\) cells
already respond appreciably to density. The neutron ratio reaches
\(1.40\times10^5\); the proton ratio reaches
\(8.54\times10^5\). Thus the old description of all 16 cells as frozen at
\(\nu_N/T=-14.891\) was too broad.

For context, the dimensionless natural-unit dilution is
\[
\frac{n_B}{T^3}\bigg|_{\rm natural}
=\frac{n_B(\hbar c)^3}{T^3}.
\]
At \(T=63.096\) MeV and \(n_B=10^{-6}\) fm\(^{-3}\), this is
\(3.06\times10^{-5}\), not \(4\times10^{-10}\). The corner is baryon-dilute,
but that statement is not used to remove any of the 16 cells from the audit.

## 7. Code and tests

- **`sfho_eos_tables.py`** — standalone readers for the three formats plus
  `sha256_file`, the nominal grids, `NB_PHYSICAL`, and the column names. No
  SciPy dependency.
- **`audit_b16_p1iii_eos_sfho_realdata_closure.py`** — loads the archives,
  reproduces the whole-table audit of Sec. 4, runs the closure grid of Sec. 6,
  and writes both the JSON record and a 224-row profile-format fixture.
- **`test_b16_p1iii_eos_sfho_realdata.py`** — 17 tests: 10 fixture-only tests, four official-table tests and three offline
  archive-manifest tests. The fixture-only tests cover grid membership, the
  excluded-volume identity, closure-domain classification, the low-density
  regimes, 1024/2048 quadrature convergence, effective-mass splitting and the
  end-to-end profile-kernel path. The four official-table tests require
  SFHO_TABLES_DIR and are skipped when the raw archives are absent. The workflow
  is configured to exercise the fixture path without the 400 MB binaries, but
  no CI pass is claimed for this commit because the Actions job is blocked before
  runner allocation by the repository account billing/limit condition.
- **`sfho_frdm_v1.03_download.py`** and **`sfho_frdm_v1.03_manifest.sha256`** —
  the reproducible, checksum-verified fetch path for the five published files
  (Sec. 2); `--dest`, `--verify-only`, `--check-urls`, `--only`, `--no-skip`.
- **`outputs/p1iii_eos_sfho_realdata_fixture.csv`** — 224 rows of real
  table values in the P1-IIIe-A Hempel column layout
  (`mstar_N`, `SigmaV_N`, `mu_nonrel_N`, `xi`, `X_N`, targets, and the audited
  `nprime`, `ratio`, `Fdeg` columns).
- **`.github/workflows/b16-p1iii-eos-degeneracy.yml`** — now also triggers on
  the three new files plus the downloader and its manifest, and runs the new test
  module.

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
   the pre-follow-up e68eae8 tree had 15 P1-IIIe-A local tests passing. The
   follow-up changes the quadrature and adds regression tests, so this historical
   result does not certify the current tree. The workflow was likewise invalid
   YAML at that line. Both defects are real, but they are **not** the cause of the
   observed 3-second failure runs, whose job API reports no steps: the check-run
   annotation on the first run of this commit reads "The job was not started
   because recent account payments have failed or your spending limit needs to be
   increased", and no runner is ever assigned. That is an account-level billing
   condition, independent of these files and not repairable inside the
   repository. No CI result is claimed for the current follow-up; the earlier local
   evidence applies only to the pre-follow-up e68eae8 tree.
2. **Density-row masking off by one.** Whole-table statistics previously ranged
   over all 326 rows, so the zero rows at \(k\ge309\) produced spurious maxima
   (relative density deviation 1.0, \(\sum X\) residual 1.0, minimum entropy 0).
   They are now masked with `NB_PHYSICAL`, and the reported maxima are the ones
   in Sec. 4.
3. **\(\xi\) rounding clamp** described in Sec. 5.
4. **Truncated archive hash in the provenance record.** The SHA-256 of
   `sfho_frdm_bin.zip` was hand-transcribed 62 characters long, so the recorded
   value was internally invalid rather than merely wrong; the audit script and its
   JSON were regenerated with the value computed from the archive itself, and
   `sfho_frdm_v1.03_download.py --verify-only` now reproduces all five hashes.
   `ArchiveManifestTests` checks full SHA-256 length, downloader/manifest/audit
   agreement, and exact filename-set equality offline, so truncated hashes and
   missing manifest entries are caught by tests rather than manual inspection.
5. **Line endings.** The generated fixture is written with `lineterminator="\n"`
   so it is byte-identical on Windows and in CI; without it the CSV module emits
   CRLF and every row of a committed fixture shows up as rewritten.

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
  tail; the P1-IIIe-A synthetic-state convergence test is not a real-EOS convergence
  guarantee. Real EOS states are now checked at 1024 against 2048 nodes in Sec. 6.

## 10. Next stage

P1-IIIe-B now has a reproducible real-table data and sampled-grid closure implementation. The post-follow-up Python suite and the four raw-table checks still require execution.
The remaining work toward the dynamic response (P1-IIIe-C) is:

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


## 11. Follow-up numerical and provenance corrections

The 224-row fixture and audit JSON are regenerated at 1024-node quadrature.
Across all 448 species-states, the 1024-to-2048 comparison gives a maximum
absolute Fdeg difference of 4.72e-8 and a maximum relative density difference
of 1.02e-8. The previous 512-node rule differed by up to 2.73% in Fdeg for a
cold, dense neutron state.

The five-object archive manifest, downloader table and audit provenance now
have exactly the same filename set, including manual_v1.04.pdf. The Release
tag sfho-frdm-v1.03-data points to commit e68eae8; its five GitHub asset
SHA-256 digests match the manifest.

The two hbar-c values are retained with distinct roles: 197.3269631 MeV fm
is the Hempel EOS-internal conversion used for the composition-table MeV^3
cross-check, whereas 197.3269804 MeV fm is the phase-space kernel's physical
unit conversion. The raw-table test now checks the actual SPP Yp and density
columns against the corresponding Extended EOS entries. Those two tests
require SFHO_TABLES_DIR and are not inferred from the 224-row fixture.


## 12. Independent post-patch fixture cross-check (2026-11-11)

After aligning the raw-table regression test with the 1024-node fixture, the
committed CSV and JSON were independently parsed and checked in a separate
JavaScript implementation of the same phase-space integral. This is an
independent numerical cross-check, **not** execution of the Python unittest
suite and not a substitute for re-reading the binary tables.

Twelve check groups passed: ten fixture-side checks, one combined
manifest/downloader/audit-provenance check, and one source-consistency check.
The numerical results are:

- 224 fixture rows cover the stated (8\times4\times7) grid.
- The maximum filling-factor identity residual is
  (7.57\times10^{-8}), below the (10^{-6}) test tolerance.
- The sampled acceptance domain contains 208/224 cells. The maximum neutron
  residual is (6.1345\times10^{-4}); for protons with
  (X_p\ge10^{-6}), it is (8.8578\times10^{-5}).
- The eight lowest-density cells have a reconstructed neutron-density spread
  (4.8615\times10^{-4}); the three higher-density groups retain the
  distinct transitional/near-closure behaviour documented above.
- Across 448 species-states, 1024-vs-2048 gives
  (max|\Delta F^{\rm deg}|=4.7117\times10^{-8}) and maximum relative
  density difference (1.0115\times10^{-8}).
- Recomputing all 448 states at 1024 nodes against the committed fixture gives
  maximum absolute (F^{\rm deg}) difference (4.995\times10^{-11}) and
  maximum relative density difference (4.680\times10^{-10}).
- The maximum effective-mass-splitting residual is
  (6.70\times10^{-5}\) MeV, below the (10^{-4}\) MeV regression threshold.
- The five-entry manifest, downloader table and JSON provenance agree on names
  and digests; total archive size is 322,921,457 bytes.

The raw-table regression test now calls `closure_cell(..., order=1024)`,
matching the fixture-generation and audit defaults.

**Remaining execution boundary.** The current execution environment can inspect
the authenticated GitHub release metadata and asset SHA-256 digests, but cannot
retrieve the 322.9 MB binary release attachments into the numerical runtime.
Therefore the four `SFHO_TABLES_DIR`-dependent tests and the post-follow-up
Python unittest suite remain unexecuted. No Python test pass or CI pass is
claimed. The raw-table checks require the extracted EOS, SPP and composition
files; once these are available to the runtime, run the complete 17-test suite
and the whole-table audit before treating P1-IIIe-B as fully accepted.
