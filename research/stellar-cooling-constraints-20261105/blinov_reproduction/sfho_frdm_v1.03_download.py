#!/usr/bin/env python3
"""Fetch and verify the official SFHo/FRDM v1.03 EOS archives.

The four archives and the manual are published by M. Hempel at the University of
Basel. They are not committed to this repository: the extended, single-particle
and Shen98 tables are 231 MB, 155 MB and 421 MB, and GitHub rejects files above
100 MB. The audit JSON records the SHA-256 of every archive and of every decoded
table, and outputs/p1iii_eos_sfho_realdata_fixture.csv carries the 224 audited
cells together with the closure numbers, so the tests run without the binaries.

Usage
-----
    python sfho_frdm_v1.03_download.py --dest D:\\data\\sfho
    python sfho_frdm_v1.03_download.py --dest D:\\data\\sfho --verify-only
    python sfho_frdm_v1.03_download.py --check-urls

The downloader uses only the standard library and honours HTTPS_PROXY /
HTTP_PROXY from the environment. Partial files are written to <name>.part and
renamed only after the size and SHA-256 both match.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
import urllib.request
from pathlib import Path

BASE_URL = (
    "https://astro.physik.unibas.ch/fileadmin/user_upload/astro_physik/"
    "People/Subpage_Hempel/eos/v1.0/"
)

FILES = (
    {
        "name": "sfho_frdm_bin.zip",
        "bytes": 161_092_071,
        "sha256": "45479eaf46e1aa9b1ca3502baf4aaeea60ff0021a21d621f10a75eafb8b8949c",
        "role": "extended EOS table, 18 columns",
    },
    {
        "name": "sfho_frdm_spp.zip",
        "bytes": 28_240_340,
        "sha256": "fc0a5f8ea1154880a4285d2b126d40b521af244d338fb06e4ef5a81defbd5769",
        "role": "single-particle properties, 7 columns (xi, m*_N, Sigma_V,N)",
    },
    {
        "name": "sfho_frdm_comp.zip",
        "bytes": 45_332_354,
        "sha256": "0d80c5e0355c755b61fd200b7de7b1e30d46a4931697bd1fbd05766f099ca8ca",
        "role": "nuclear composition, free neutron and proton densities",
    },
    {
        "name": "sfho_frdm_shen98format.zip",
        "bytes": 88_043_252,
        "sha256": "deed6c687457dc13026ad9e27226ef985f145683d83700b1064ee815b873a811",
        "role": "Shen98 ASCII format, cross-checks only",
    },
    {
        "name": "manual_v1.04.pdf",
        "bytes": 213_440,
        "sha256": "0994abc5073853d35dd10ed6a0313be5c701ee7c47c268f2faa77f36bb4b5478",
        "role": "EOS manual (v1.03 data, v1.04 manual)",
    },
)

CHUNK = 1 << 22


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


def describe(entry: dict) -> str:
    return f"{entry['name']} ({entry['bytes']:,} bytes, {entry['role']})"


def select(entries: tuple, only: list[str]) -> tuple:
    if not only:
        return entries
    chosen = [
        entry
        for entry in entries
        if any(needle in entry["name"] for needle in only)
    ]
    missing = [needle for needle in only if not any(needle in e["name"] for e in chosen)]
    if missing:
        raise SystemExit(f"no archive matches {missing}")
    return tuple(chosen)


def verify_only(dest: Path, entries: tuple = FILES) -> int:
    failures = 0
    for entry in entries:
        path = dest / entry["name"]
        if not path.is_file():
            print(f"MISSING  {path}")
            failures += 1
            continue
        size = path.stat().st_size
        if size != entry["bytes"]:
            print(f"SIZE     {path}: {size:,} != {entry['bytes']:,}")
            failures += 1
            continue
        actual = sha256_file(path)
        if actual != entry["sha256"]:
            print(f"SHA256   {path}: {actual} != {entry['sha256']}")
            failures += 1
            continue
        print(f"OK       {path}")
    return 1 if failures else 0


def check_urls(entries: tuple = FILES) -> int:
    failures = 0
    for entry in entries:
        url = BASE_URL + entry["name"]
        request = urllib.request.Request(url, method="HEAD")
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                length = response.headers.get("Content-Length")
                status = response.status
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"FAIL     {url}: {exc}")
            failures += 1
            continue
        matches = status == 200 and length is not None and int(length) == entry["bytes"]
        print(f"{'OK' if matches else 'LENGTH'}   {status} {length} {url}")
        failures += 0 if matches else 1
    return 1 if failures else 0


def download(dest: Path, skip_existing: bool, entries: tuple = FILES) -> int:
    dest.mkdir(parents=True, exist_ok=True)
    failures = 0
    for entry in entries:
        target = dest / entry["name"]
        if skip_existing and target.is_file():
            if target.stat().st_size == entry["bytes"] and (
                sha256_file(target) == entry["sha256"]
            ):
                print(f"PRESENT  {target}")
                continue
        url = BASE_URL + entry["name"]
        print(f"FETCH    {describe(entry)}")
        print(f"         {url}")
        partial = target.with_suffix(target.suffix + ".part")
        digest = hashlib.sha256()
        received = 0
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "sfho-frdm-fetch/1.0"})
            with urllib.request.urlopen(request, timeout=120) as response:
                with partial.open("wb") as handle:
                    while True:
                        block = response.read(CHUNK)
                        if not block:
                            break
                        handle.write(block)
                        digest.update(block)
                        received += len(block)
                        if received % (64 * CHUNK) < CHUNK:
                            share = 100.0 * received / entry["bytes"]
                            print(f"         {received:,}/{entry['bytes']:,} bytes ({share:.1f}%)")
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"FAIL     {url}: {exc}")
            if partial.exists():
                partial.unlink()
            failures += 1
            continue
        actual = digest.hexdigest()
        if received != entry["bytes"] or actual != entry["sha256"]:
            print(
                f"REJECT   {target}: got {received:,} bytes / {actual}, "
                f"expected {entry['bytes']:,} bytes / {entry['sha256']}"
            )
            partial.unlink()
            failures += 1
            continue
        os.replace(partial, target)
        print(f"VERIFIED {target}")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path.cwd() / "sfho_frdm_v1.03",
        help="directory holding the archives (default: ./sfho_frdm_v1.03)",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="only verify files already present in --dest, do not download",
    )
    parser.add_argument(
        "--check-urls",
        action="store_true",
        help="HEAD every archive URL; check HTTP 200 and Content-Length only (no remote hash)",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="SUBSTRING",
        help="fetch only archives whose name contains SUBSTRING (repeatable)",
    )
    parser.add_argument(
        "--no-skip",
        action="store_true",
        help="re-download files that are already present and valid",
    )
    args = parser.parse_args(argv)

    if shutil.which("python") is None:  # pragma: no cover - diagnostic only
        print("warning: no 'python' on PATH", file=sys.stderr)

    entries = select(FILES, args.only)
    if args.check_urls:
        return check_urls(entries)
    if args.verify_only:
        return verify_only(args.dest, entries)
    return download(args.dest, skip_existing=not args.no_skip, entries=entries)


if __name__ == "__main__":
    raise SystemExit(main())
