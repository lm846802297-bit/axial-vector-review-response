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

**Reproducible acquisition.** The two small archives and the manual are committed
under `data/sfho-frdm-v1.03/`, and the 161 092 071-byte extended table is
committed as three ordered pieces of at most 60 MiB, because GitHub rejects
single files above 100 MB; `reassemble_sfho_frdm_archives.py` rebuilds it and
checks the whole-archive digest, and `data/sfho-frdm-v1.03/README.md` records
the layout. `sfho_frdm_shen98format.zip` (88 043 252 bytes) remains
Release-only, since it is a cross-validation format the analysis does not read. `sfho_frdm_v1.03_download.py` fetches them
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
  \(\xi\), and layer 3 is the Coulomb-type term of the module. Layer 4 is a
  nuclear-suppression switch: it equals 1 when no nuclei are present and is
  fractional in the transition region. Layer 5 is the electron-density input
  passed to the Fortran routine sub_coulomb(ne) [MeV\(^3\)]; it is not
  globally equal to \(Y_p^{\rm tot}n_B\), and is zero when the no-nuclei switch
  equals 1. Layers 6-7 are the free neutron and proton densities [MeV\(^3\)].
  Layer 1 is a proton-side chemical potential whose precise definition remains
  open; it is not used here.

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

The raw composition archive was re-read. Over the 1,521,828 physical composition cells, 1,121,375 (73.6861%) are nuclei-containing under the module's layer-4 switch; 400,453 (26.3139%) have the no-nuclei switch set to 1.

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
- **`test_b16_p1iii_eos_sfho_realdata.py`** — 19 tests: 10 fixture-only tests, five official-table tests and four offline
  archive-manifest tests; the fourth locks the vendored split layout
  (three pieces, sizes summing to 161 092 071 bytes, seven manifest entries). The fixture-only tests cover grid membership, the
  excluded-volume identity, closure-domain classification, the low-density
  regimes, 1024/2048 quadrature convergence, effective-mass splitting and the
  end-to-end profile-kernel path. The five official-table tests require
  SFHO_TABLES_DIR and are skipped when the raw archives are absent. The workflow
  exercises the fixture path without the 400 MB binaries. It has a verified pass:
  run 42922595906 on head `5dd24ac` concluded `success` in 23 s, running this
  module as `Ran 14 tests ... OK (skipped=1)` (the official-table test class is
  skipped as one unit without `SFHO_TABLES_DIR`) and the deterministic self-test assertion block.
  Locally, with the unpacked v1.03 tables, the same module reports
  `Ran 19 tests ... OK`.
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
   repository. No CI result was claimed for the current follow-up at the time of writing; the
   earlier local evidence applies only to the pre-follow-up e68eae8 tree. The
   condition cleared later the same day and the workflow then passed on head
   `5dd24ac` (run 42922595906); the failures at `edb0f2e`, `d7adb11` and
   `b1393ef` were the same startup failure, with no runner assigned and no steps
   executed.
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
6. **The data were carried by reference only.** The archives lived in a private
   Release, so a reader could not reproduce a run from a clone. The two small
   archives and the manual are now committed as published, and the extended
   table is committed as three ordered pieces with a `sha256sum`-compatible
   manifest and a reassembly tool that takes its sizes and hashes from the
   downloader's `FILES` table instead of a second hand-maintained copy. A round
   trip was verified: the rebuilt archive is byte-identical to the published one
   (sha256 `45479eaf...b8949c`) and `--verify-only` then accepts it.

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

- 224 fixture rows cover the stated \(8\times4\times7\) grid.
- The maximum filling-factor identity residual is
  \(7.57\times10^{-8}\), below the \(10^{-6}\) test tolerance.
- The sampled acceptance domain contains 208/224 cells. The maximum neutron
  residual is \(6.1345\times10^{-4}\); for protons with
  \(X_p\ge10^{-6}\), it is \(8.8578\times10^{-5}\).
- The eight lowest-density cells have a reconstructed neutron-density spread
  \(4.8615\times10^{-4}\); the three higher-density groups retain the
  distinct transitional/near-closure behaviour documented above.
- Across 448 species-states, 1024-vs-2048 gives
  \(\max|\Delta F^{\rm deg}|=4.7117\times10^{-8}\) and maximum relative
  density difference \(1.0115\times10^{-8}\).
- Recomputing all 448 states at 1024 nodes against the committed fixture gives
  maximum absolute \(F^{\rm deg}\) difference \(4.995\times10^{-11}\) and
  maximum relative density difference \(4.680\times10^{-10}\).
- The maximum effective-mass-splitting residual is
  \(6.70\times10^{-5}\) MeV, below the \(10^{-4}\) MeV regression threshold.
- The five-entry manifest, downloader table and JSON provenance agree on names
  and digests; total archive size is 322,921,457 bytes.

The raw-table regression test now calls closure_cell with order=1024,
matching the fixture-generation and audit defaults.

**Remaining execution boundary.** The current execution environment can inspect
the authenticated GitHub release metadata and asset SHA-256 digests, but cannot
retrieve the 322.9 MB binary release attachments into the numerical runtime.
Therefore the four SFHO_TABLES_DIR-dependent tests and the post-follow-up
Python unittest suite remain unexecuted. No Python test pass or CI pass is
claimed. The raw-table checks require the extracted EOS, SPP and composition
files; once these are available to the runtime, run the complete 19-test suite
and the whole-table audit before treating P1-IIIe-B as fully accepted.

**Update after the vendored-archive commit (2026-11-11, later the same day).** The
execution boundary above no longer binds this checkout: the published archives are
committed to the repository, the unpacked v1.03 tables are available to the local
runtime, and both suites have been run at `5dd24ac` with `SFHO_TABLES_DIR` set -
P1-IIIe-A `Ran 15 tests ... OK` and P1-IIIe-B `Ran 19 tests ... OK`. CI run
42922595906 on the same head concluded `success`, executing the fixture path as
`Ran 14 tests ... OK (skipped=1)` plus the self-test assertions. What remains open
is the physical input rather than the execution path: no Garching
stellar-evolution profile has been obtained, so the global degeneracy averages are
still exercised on synthetic weights only.


## 13. Independent raw-table execution acceptance (2026-11-11)

The three original archives were downloaded from the public Release into the
numerical runtime through a short-lived Actions artifact. The archive SHA-256
values were recomputed locally and match the five-entry repository manifest
for each transferred object:

| Archive | Bytes | SHA-256 |
|---|---:|---|
| \`sfho_frdm_bin.zip\` | 161,092,071 | \`45479eaf46e1aa9b1ca3502baf4aaeea60ff0021a21d621f10a75eafb8b8949c\` |
| \`sfho_frdm_spp.zip\` | 28,240,340 | \`fc0a5f8ea1154880a4285d2b126d40b521af244d338fb06e4ef5a81defbd5769\` |
| \`sfho_frdm_comp.zip\` | 45,332,354 | \`0d80c5e0355c755b61fd200b7de7b1e30d46a4931697bd1fbd05766f099ca8ca\` |

The extracted table hashes are:

| Table | Bytes | SHA-256 |
|---|---:|---|
| \`sfho_frdm_eos_v1.03.bin\` | 231,950,312 | \`f1ea9c3e04502ca35d7fc64facce575f8553293085ea26e07732389b80d32cb4\` |
| \`sfho_frdm_spp_v1.03.tab\` | 155,283,075 | \`118bd3c986283d958fab88a8e81fe49b64ca3b5137ff4bcdc05f97064cc1219e\` |
| \`sfho_frdm_comp_v1.03.bin\` | 103,284,392 | \`0dafcd272ff8b8f4b1ba4c05210ea8020dd9a92820b6b0b54165faead4871da7\` |

Both binary files are single-record little-endian Fortran sequential files.
The extended-table record markers are 231,950,304 bytes and the composition
record markers are 103,284,384 bytes; in both files the leading marker, trailing
marker, and actual payload length agree exactly. The SPP parser reads 81
temperature blocks, each containing 60 proton-fraction blocks by 326 density
rows, with seven numeric columns; the source file has 1,589,463 text lines.

The three decoded shapes are exactly:

- extended EOS: \`(81, 61, 326, 18)\`;
- SPP: \`(81, 60, 326, 7)\`;
- composition: \`(81, 61, 326, 8)\`.

The physical density mask is 308 rows. Thus the physical cell counts are
1,521,828 for the extended and composition tables and 1,496,880 for the SPP
table. The extended and composition payloads are exactly zero for Fortran
\(k\ge309\); the nominal SPP coordinate columns continue beyond that boundary
and are not interpreted as physical solutions.

The full-table checks were rerun from the extracted archives:

| Check | Recomputed result |
|---|---:|
| Extended \(n_B\) vs nominal grid, maximum relative deviation | \(9.99999\times10^{-9}\) |
| Extended \(Y_p^{\rm tot}\) vs nominal \(Y_e\), maximum absolute deviation | \(8.87047\times10^{-9}\) |
| Mass-fraction closure \(\sum_i X_i=1\), maximum absolute residual | \(7.45537\times10^{-12}\) |
| \(F-(E-TS)\), maximum relative residual | \(6.79532\times10^{-15}\) |
| Composition free-neutron density vs \(X_n n_B\), maximum relative deviation | \(4.44\times10^{-16}\) |
| Composition free-proton density vs \(X_p n_B\), maximum relative deviation | \(4.44\times10^{-16}\) |
| SPP \(n_B\) vs extended \(n_B\), maximum relative deviation | \(3.71499\times10^{-7}\) |
| SPP \(Y_p^{\rm tot}\) vs extended \(Y_p^{\rm tot}\), maximum absolute deviation | \(8.87047\times10^{-9}\) |

The SPP-to-extended density difference is consistent with the printed ASCII
precision. The full physical-grid filling-factor identity was also evaluated
independently on all 1,496,880 SPP cells:
\[
\xi_{\rm SPP}\stackrel{?}{=}
1-\frac{n_B-X_n n_B-X_p n_B}{n_0}.
\]
Its maximum absolute residual is \(7.97497\times10^{-8}\), with median
\(2.31581\times10^{-11}\). This is a full-grid identity check, distinct from
the 224-cell phase-space closure sample.

### Correction: the composition neutron-side NSE input is not a global chemical-potential column

The Fortran composition module uses \\texttt{comp(i,j,k,1)} as the neutron-side
chemical-potential input in the nuclear-abundance exponent. This is Python
layer \\texttt{comp[...,0]}. The same Fortran routine skips the nuclear-abundance
calculation when layer 4 (the nuclear-suppression switch) equals 1. In those
400,453 no-nuclei cells, layer 0 is exactly zero and must not be read as a
physical \\(\\mu_n^{\\rm nonrel}\\). In the 1,121,375 nuclei-containing cells it
usually tracks the Extended EOS neutron chemical potential, but the difference
has median \\(2.37\\times10^{-9}\\) MeV and reaches \\(6.56\\) MeV. It is therefore
not an interchangeable copy of the thermodynamic chemical-potential column
and is not used in the Fiorillo occupation mapping. The parser documentation
and a raw-table regression test now encode this conditional meaning.

### Correction: the composition electron-density input is not global \(Y_p n_B\)

The raw-table read exposed a semantic issue that was not visible in the earlier
free-neutron/free-proton checks. In the official Fortran module,
\(\texttt{comp(i,j,k,6)}\) is passed to \(\texttt{sub_coulomb(ne)}\), whose
argument is documented as the electron number density used by the Coulomb
correction. This is Python array layer \(\texttt{comp[...,5]}\). It must not be
identified indiscriminately with the volume-averaged charge density
\(Y_p^{\rm tot}n_B\).

Over the 1,521,828 physical composition cells:

- the nuclear-suppression switch \(\texttt{comp[...,4]}\) equals 1 in
  400,453 cells, and the Coulomb input \(\texttt{comp[...,5]}\) is exactly zero
  in all of them;
- the remaining 1,121,375 cells have a positive Coulomb input;
- in those nuclei-containing cells,
  \(n_e^{\rm Coulomb}/(Y_p^{\rm tot}n_B)\) ranges from 0.691831 to
  1.00000001; 8,331 cells differ from the global charge-density value by more
  than \(10^{-4}\), with the affected Fortran density indices \(k=266\ldots280\);
- \(n_e^{\rm Coulomb}/Y_e\) lies on a nominal density-grid point to within
  \(10^{-7}\) dex for 99.5769% of nuclei-containing cells. The inferred density
  index never exceeds the current table index and is at most four bins lower.

This pattern is consistent with a phase/coexistence-specific Coulomb background
rather than a globally averaged electron-density column, but the exact physical
mapping is not inferred from this numerical identity alone. The parser and
report therefore label this field as the **Coulomb electron-density input**.
The global charge density remains \(Y_p^{\rm tot}n_B\), derived from the
extended EOS charge-neutrality convention. The free-neutron and free-proton
layers remain the independently validated composition inputs used in the
occupation closure.

### Execution and acceptance boundary

The local run of the complete P1-IIIe-A and P1-IIIe-B test modules passes
**35/35 tests**: 15 distribution-kernel tests, 10 fixture tests, six
official-table tests (including the conditional NSE-neutron-input and
Coulomb-input semantic regressions), and four offline archive-manifest tests.
No raw-table test was skipped.

The same 35-test suite is now reproducible in GitHub Actions. Run
[#42953524476](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42953524476)
downloaded the three original Release ZIPs, verified all three SHA-256 entries,
extracted the EOS/SPP/composition files, and completed 15/15 distribution-kernel
tests plus 20/20 real-table/fixture/archive tests. No table-dependent test was
skipped in this CI run.


The 224-cell phase-space audit was regenerated from the extracted tables.
The 1024-to-2048-node checks over its 448 species states pass; the committed
fixture and this runtime's regenerated fixture differ only at the small
quadrature-rounding level (maximum relative difference below \(5\times10^{-8}\)
for the density/ratio columns and maximum absolute \(F^{\rm deg}\) difference
below \(1.2\times10^{-10}\)).

This acceptance establishes the binary/ASCII parsing, table dimensions,
grid alignment, thermodynamic identities, composition free-\(n,p\) closure,
and the sampled occupation-kernel closure. It does **not** establish the
Fiorillo Table 1 weighted averages \(F_{pp}^{\rm deg}=(0.80,0.77)\) and
\(F_{nn}^{\rm deg}=(0.48,0.42)\): those require the Garching profile and the
same mass/time weights, which are not contained in these EOS tables. It also
does not claim a phase-space closure proof over every one of the 1.5 million
physical EOS cells. No B.2 transport, pure-vector Fig. 7, or axial-vector
constraint curve is changed by this validation.
