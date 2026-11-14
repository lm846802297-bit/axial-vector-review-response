# Historical radial-scalar scan archive

This directory holds a compressed 73,728-row CSV (plus header), a summary, environment and source records, and historical test logs. The stored `SHA256SUMS.txt` names the **uncompressed** CSV, so `sha256sum -c SHA256SUMS.txt` requires extraction first. To check the CSV bytes without creating an uncompressed file:

```bash
gzip -dc original_uv_width_scan.csv.gz | sha256sum
```

On 2026-11-14 this produced `5d5f0ce306d6ac75498eef054c9c02f6897b676fe0cf6626fb5dcbdbc390dd67`, with 80,770,035 uncompressed bytes and 73,729 lines including the header. This matches `SHA256SUMS.txt`, but differs from the earlier scan record's `67ec36a5…`; the source-commit records also differ. Do not treat the historical run record and this package as the same run until reconciled.

The uncompressed CSV is not currently committed as a directly usable file. The repository's extract-before-upload policy and the provenance mismatch must be resolved before treating this archive as a complete native-file handoff. See [scan record](../../../SCAN_RUN_RECORD_2026-11-09.md) and [manifest audit](../../../../../docs/repository-management/MANIFEST_REVIEW_2026-11-14.md). Successful checksum verification does not validate the underlying physical calculation.
