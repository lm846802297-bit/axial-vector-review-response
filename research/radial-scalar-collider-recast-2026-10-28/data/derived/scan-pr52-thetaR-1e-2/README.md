# Historical radial-scalar scan archive

This directory holds a compressed 73,728-row CSV (plus header), a summary, environment and source records, and historical test logs. The stored `SHA256SUMS.txt` names the **uncompressed** CSV, so `sha256sum -c SHA256SUMS.txt` requires extraction first. To check the CSV bytes without creating an uncompressed file:

```bash
gzip -dc original_uv_width_scan.csv.gz | sha256sum
```

On 2026-11-14 this produced `5d5f0ce306d6ac75498eef054c9c02f6897b676fe0cf6626fb5dcbdbc390dd67`, with 80,770,035 uncompressed bytes and 73,729 lines including the header. This matches `SHA256SUMS.txt`, but differs from the earlier scan record's `67ec36a5…`; the source-commit records also differ. Git history identifies these as distinct archived runs: commit `9ae7955…` contains the earlier CSV with the run record’s `67ec36a5…` hash and 58-test log. Their row-level relationship and source-code change are recorded in the [comparison output](scan_version_comparison_2026-11-14.json) and manifest audit.

The uncompressed CSV is not currently committed as a directly usable file. The repository's extract-before-upload policy and the original run’s results and the current run must remain distinguished before treating this archive as a complete native-file handoff. See [scan record](../../../SCAN_RUN_RECORD_2026-11-09.md) and [manifest audit](../../../../../docs/repository-management/MANIFEST_REVIEW_2026-11-14.md). Successful checksum verification does not validate the underlying physical calculation.

 
 ## 2026-11-17 exact extraction verification
 
 The current compressed archive was actually decompressed and checked in
 [scan_archive_integrity_2026-11-17.json](scan_archive_integrity_2026-11-17.json)
 by GitHub Actions run
 [#44033029862](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/44033029862).
 The verifier confirms:
 
 - gzip SHA-256 `f8dde6825e3c658cb841f06e1ac2aa9de36519e805e589d86fc07e37079429ff`, 20,156,701 bytes;
 - decompressed CSV SHA-256 `5d5f0ce306d6ac75498eef054c9c02f6897b676fe0cf6626fb5dcbdbc390dd67`, 80,770,035 bytes;
 - 73,728 data rows, 77 columns, no malformed row widths;
 - decompressed hash matches `SHA256SUMS.txt` and the version-comparison record.
 
 The uncompressed CSV is intentionally not committed: it duplicates an
 80.8 MB file alongside the 20.2 MB compressed archive and would add that
 duplicate to every future Git checkout. The exact extraction is reproducible
 on demand:
 
 ```bash
 python extract_and_verify_scan_archive.py --output /path/to/original_uv_width_scan.csv
 ```
 
 The default invocation verifies in a temporary directory and records the
 integrity report without leaving a large extracted file in the repository.
