# Vendored SFHo/FRDM v1.03 EOS archives

The three archives that the P1-IIIe-B audit reads, plus the v1.04 manual, copied
into the repository byte for byte from the University of Basel EOS page (see
`../../B16_P1IIIE_B_SFHO_REALDATA_CLOSURE_2026-11-11.md`, Sec. 2, and
`../sfho_frdm_v1.03_manifest.sha256`).

| File | Bytes | SHA-256 |
|---|---:|---|
| `sfho_frdm_spp.zip` | 28 240 340 | `fc0a5f8ea1154880a4285d2b126d40b521af244d338fb06e4ef5a81defbd5769` |
| `sfho_frdm_comp.zip` | 45 332 354 | `0d80c5e0355c755b61fd200b7de7b1e30d46a4931697bd1fbd05766f099ca8ca` |
| `sfho_frdm_bin.zip.part-00/01/02` | 62 914 560 / 62 914 560 / 35 262 951 | see `MANIFEST.sha256` |
| `sfho_frdm_bin.zip` (after reassembly) | 161 092 071 | `45479eaf46e1aa9b1ca3502baf4aaeea60ff0021a21d621f10a75eafb8b8949c` |
| `manual_v1.04.pdf` | 213 440 | `0994abc5073853d35dd10ed6a0313be5c701ee7c47c268f2faa77f36bb4b5478` |

## Why one archive is split

GitHub rejects any file above 100 MB, and `sfho_frdm_bin.zip` is 161 092 071 B.
It is therefore stored as three ordered 60 MiB pieces. Concatenating
`part-00`, `part-01`, `part-02` in that order reproduces the published archive
exactly; the split carries no transformation.

## Getting the archives back

```bash
cd research/stellar-cooling-constraints-20261105/blinov_reproduction
python reassemble_sfho_frdm_archives.py --dest /path/to/sfho_frdm_v1.03
```

The script verifies every piece against `MANIFEST.sha256`, joins them, and checks
the result against the byte count and SHA-256 of the published file. To check the
pieces in place without writing anything, add `--verify-only`. Every file can also
be checked with plain `sha256sum -c MANIFEST.sha256` from this directory.

`sfho_frdm_shen98format.zip` (88 043 252 B) is **not** vendored: the audit only
uses it for cross-checks, and it lives in the GitHub release
`sfho-frdm-v1.03-data` together with all five objects; fetch it with
`sfho_frdm_v1.03_download.py` or `gh release download` if a check needs it.

## Version note

The directory on the server is `v1.0`, the table files are labelled `v1.03`, and
the manual is `v1.04`. This is not a mismatch: v1.03 (2012-07-09) uploaded the
SFHo and SFHx tables, v1.04 (2012-12-19) only added the IUFSU table and updated
the manual figure, and the single-particle table was posted later (2014-10-23)
under the same v1.03 label.

## Usage boundary

Published EOS tables by M. Hempel, redistributed unmodified for reproducibility.
Cite Hempel (2015), arXiv:1410.6337, and the University of Basel EOS page.
