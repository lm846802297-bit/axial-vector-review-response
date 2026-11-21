"""Extract and verify the archived 73,728-row PR52 width-scan CSV.

By default the 80.8 MB CSV is materialized only in a temporary directory.
Pass --output PATH when a persistent, directly usable CSV is needed.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_ARCHIVE = HERE / "original_uv_width_scan.csv.gz"
DEFAULT_MANIFEST = HERE / "SHA256SUMS.txt"
DEFAULT_VERSION = HERE / "scan_version_comparison_2026-11-14.json"
DEFAULT_SOURCE_COMMIT = HERE / "source-commit.txt"
DEFAULT_SOURCE_HASHES = HERE / "source-sha256.txt"


def sha256_file(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return digest.hexdigest(), size


def manifest_hash(path: Path, filename: str) -> str:
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        parts = line.strip().split()
        if len(parts) >= 2 and parts[-1].lstrip("*") == filename:
            return parts[0]
    raise ValueError(f"{filename} not found in {path}")


def inspect_csv(path: Path):
    header = None
    row_count = 0
    bad_width_rows = []
    with Path(path).open("r", encoding="utf-8", newline="") as stream:
        reader = csv.reader(stream)
        header = next(reader)
        for line_number, row in enumerate(reader, start=2):
            row_count += 1
            if len(row) != len(header):
                if len(bad_width_rows) < 10:
                    bad_width_rows.append({"line": line_number, "fields": len(row)})
    return {
        "header": header,
        "row_count": row_count,
        "column_count": len(header),
        "bad_width_rows": bad_width_rows,
    }


def verify_archive(archive=DEFAULT_ARCHIVE, manifest=DEFAULT_MANIFEST,
                   version_path=DEFAULT_VERSION, output=None):
    archive, manifest, version_path = Path(archive), Path(manifest), Path(version_path)
    version = json.loads(version_path.read_text(encoding="utf-8"))
    expected_gzip = version["current_archive"]["gzip"]
    expected_csv = version["current_archive"]["csv"]
    expected_manifest_hash = manifest_hash(manifest, "original_uv_width_scan.csv")
    if expected_manifest_hash != expected_csv["sha256"]:
        raise AssertionError("SHA256SUMS.txt and version-comparison CSV hash disagree")

    archive_sha, archive_bytes = sha256_file(archive)
    if archive_sha != expected_gzip["sha256"] or archive_bytes != expected_gzip["bytes"]:
        raise AssertionError(
            f"Compressed archive mismatch: sha256={archive_sha}, bytes={archive_bytes}"
        )

    temp_context = None
    if output is None:
        temp_context = tempfile.TemporaryDirectory(prefix="scan-pr52-extract-")
        csv_path = Path(temp_context.name) / "original_uv_width_scan.csv"
    else:
        csv_path = Path(output)
        csv_path.parent.mkdir(parents=True, exist_ok=True)

    digest = hashlib.sha256()
    byte_count = 0
    with gzip.open(archive, "rb") as source, csv_path.open("wb") as target:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            target.write(chunk)
            digest.update(chunk)
            byte_count += len(chunk)
    csv_sha = digest.hexdigest()
    if csv_sha != expected_csv["sha256"] or byte_count != expected_csv["bytes"]:
        raise AssertionError(
            f"Decompressed CSV mismatch: sha256={csv_sha}, bytes={byte_count}"
        )

    csv_info = inspect_csv(csv_path)
    if csv_info["row_count"] != version["rows"]:
        raise AssertionError(f"CSV row count {csv_info['row_count']} != {version['rows']}")
    if csv_info["column_count"] != version["column_count"]:
        raise AssertionError(
            f"CSV column count {csv_info['column_count']} != {version['column_count']}"
        )
    if csv_info["bad_width_rows"]:
        raise AssertionError(f"CSV contains inconsistent row widths: {csv_info['bad_width_rows']}")

    report = {
        "title": "PR52 current width-scan archive extraction and integrity audit",
        "date": "2026-11-17",
        "status": "PASS",
        "archive": {
            "path": archive.name,
            "sha256": archive_sha,
            "bytes": archive_bytes,
            "expected_sha256": expected_gzip["sha256"],
            "expected_bytes": expected_gzip["bytes"],
        },
        "decompressed_csv": {
            "path": csv_path.name if output is not None else "temporary extraction (not committed)",
            "sha256": csv_sha,
            "bytes": byte_count,
            "expected_sha256": expected_csv["sha256"],
            "expected_bytes": expected_csv["bytes"],
            "row_count": csv_info["row_count"],
            "column_count": csv_info["column_count"],
            "header": csv_info["header"],
            "bad_width_rows": csv_info["bad_width_rows"],
        },
        "manifest": {
            "path": manifest.name,
            "uncompressed_csv_sha256": expected_manifest_hash,
        },
        "source": {
            "commit": DEFAULT_SOURCE_COMMIT.read_text(encoding="utf-8").strip(),
            "sha256_manifest": DEFAULT_SOURCE_HASHES.read_text(encoding="utf-8").splitlines(),
        },
        "old_vs_current": {
            "old_archive": version["old_archive"],
            "current_archive": version["current_archive"],
            "changed_rows": version["different_rows"],
            "changed_columns": version["changed_columns"],
            "old_lower_greater_count": version["old_lower_greater_count"],
            "current_lower_greater_count": version["current_lower_greater_count"],
            "exact_swapped_pairs": version["exact_swapped_pairs"],
            "swapped_within_1e_minus_12": version["swapped_within_1e_minus_12"],
            "max_relative_difference_from_swap": version["max_relative_difference_from_swap"],
            "nonfinite_bound_rows": version["nonfinite_bound_rows"],
        },
        "repository_policy": {
            "uncompressed_csv_committed": False,
            "reason": "The 80,770,035-byte extracted CSV duplicates the 20,156,701-byte gzip archive; keep the canonical compressed archive and a verified on-demand extractor rather than adding an 80.8 MB duplicate to Git history.",
            "persistent_extraction": "python extract_and_verify_scan_archive.py --output /path/to/original_uv_width_scan.csv",
        },
    }
    if temp_context is not None:
        temp_context.cleanup()
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--version", type=Path, default=DEFAULT_VERSION)
    parser.add_argument("--output", type=Path, default=None,
                        help="optional persistent path for the decompressed CSV")
    parser.add_argument("--report", type=Path, default=HERE / "scan_archive_integrity_2026-11-17.json")
    args = parser.parse_args()
    report = verify_archive(args.archive, args.manifest, args.version, args.output)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
