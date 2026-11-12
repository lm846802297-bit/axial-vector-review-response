"""Fetch the official Belle II scalar supplemental numerical files.

This script downloads source files verbatim. It does not digitize plots, infer
missing rows, or reinterpret the numbers. A manifest records the final URL,
content type, byte count, and SHA-256 digest for every downloaded file.

Run:
    python fetch_belleii_supplements.py --output-dir data/raw/belleii

Network access and permission to retrieve the APS-hosted supplements are
required. If APS serves an HTML challenge/error page, the script fails rather
than archiving it as numerical data.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

SOURCES = (
    (
        "belleii_4mu_scalar",
        "https://journals.aps.org/prd/supplemental/10.1103/PhysRevD.109.112015/S_supplemental.txt",
        "S_supplemental.txt",
    ),
    (
        "belleii_tautau_limits_csv",
        "https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.131.121802/limits.csv",
        "limits.csv",
    ),
    (
        "belleii_tautau_limits_txt",
        "https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.131.121802/limits.txt",
        "limits.txt",
    ),
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def validate_payload(payload: bytes, content_type: str) -> None:
    if not payload:
        raise ValueError("downloaded file is empty")
    prefix = payload[:512].lstrip().lower()
    if "text/html" in content_type.lower() or prefix.startswith(
        (b"<!doctype html", b"<html", b"<head", b"<body")
    ):
        raise ValueError("server returned HTML rather than a numerical supplement")
    if b"access denied" in prefix or b"robot check" in prefix:
        raise ValueError("server returned an access-block/challenge page")


def download_one(url: str, destination: Path) -> dict:
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; BelleIISupplementResearch/1.0)",
            "Accept": "text/plain,text/csv,application/octet-stream,*/*",
        },
    )
    with urlopen(request, timeout=45) as response:
        payload = response.read()
        content_type = response.headers.get("Content-Type", "")
        final_url = response.geturl()
    validate_payload(payload, content_type)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return {
        "filename": destination.name,
        "source_url": url,
        "final_url": final_url,
        "content_type": content_type,
        "bytes": len(payload),
        "sha256": sha256_bytes(payload),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    records = []
    for source_id, url, filename in SOURCES:
        record = download_one(url, args.output_dir / filename)
        record["source_id"] = source_id
        records.append(record)

    manifest = {
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "files": records,
        "note": (
            "Raw official supplements only. No parsing, interpolation, "
            "digitization, or recast is performed by this downloader."
        ),
    }
    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
