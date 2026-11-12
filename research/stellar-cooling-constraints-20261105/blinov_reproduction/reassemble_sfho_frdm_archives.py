"""Reassemble the vendored SFHo/FRDM v1.03 archives from `data/sfho-frdm-v1.03`.

GitHub rejects a single file above 100 MB, so ``sfho_frdm_bin.zip`` is stored as
ordered ``.part-NN`` pieces.  This script verifies every piece against
``data/sfho-frdm-v1.03/MANIFEST.sha256``, concatenates them in order, and checks
the result against the SHA-256 and byte count of the published archive (the same
table ``sfho_frdm_v1.03_download.py`` uses).  The output is byte-identical to the
file on the Basel server, so the split is a transport detail, not a fork.

Usage::

    python reassemble_sfho_frdm_archives.py                     # -> ./sfho_frdm_v1.03
    python reassemble_sfho_frdm_archives.py --dest /tmp/tables   # explicit target
    python reassemble_sfho_frdm_archives.py --verify-only        # only check pieces
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data" / "sfho-frdm-v1.03"

SPLIT = ("sfho_frdm_bin.zip",)
PLAIN = ("sfho_frdm_spp.zip", "sfho_frdm_comp.zip")
EXTRA = ("manual_v1.04.pdf",)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 22), b""):
            digest.update(block)
    return digest.hexdigest()


def load_expected() -> dict[str, tuple[int, str]]:
    """Size and hash of every published file, from the downloader's table."""

    spec = importlib.util.spec_from_file_location(
        "_sfho_dl", HERE / "sfho_frdm_v1.03_download.py"
    )
    if spec is None or spec.loader is None:  # pragma: no cover - broken checkout
        raise SystemExit("cannot load sfho_frdm_v1.03_download.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {entry["name"]: (int(entry["bytes"]), entry["sha256"]) for entry in module.FILES}


def read_manifest(data_dir: Path) -> dict[str, str]:
    manifest: dict[str, str] = {}
    for line in (data_dir / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split(None, 1)
        manifest[name.strip()] = digest
    return manifest


def parts_of(data_dir: Path, name: str) -> list[Path]:
    return sorted(data_dir.glob(f"{name}.part-*"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR)
    parser.add_argument("--dest", type=Path, default=Path.cwd() / "sfho_frdm_v1.03")
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="verify the pieces in place instead of writing the archives",
    )
    args = parser.parse_args(argv)

    if not (args.data_dir / "MANIFEST.sha256").is_file():
        print(f"missing manifest in {args.data_dir}", file=sys.stderr)
        return 2

    expected = load_expected()
    manifest = read_manifest(args.data_dir)
    failures = 0
    joined: dict[str, Path] = {}

    for name in SPLIT:
        pieces = parts_of(args.data_dir, name)
        if not pieces:
            print(f"MISSING  {name}.part-*")
            failures += 1
            continue
        written = 0
        for piece in pieces:
            actual = sha256_file(piece)
            recorded = manifest.get(piece.name)
            if recorded != actual:
                print(f"SHA256   {piece.name}: {actual} != {recorded}")
                failures += 1
                continue
            written += piece.stat().st_size
            print(f"OK       {piece.name} ({piece.stat().st_size:,} B)")
        size, digest = expected[name]
        if written != size:
            print(f"SIZE     {name}: pieces total {written:,} != {size:,}")
            failures += 1
            continue
        if args.verify_only:
            continue
        args.dest.mkdir(parents=True, exist_ok=True)
        target = args.dest / name
        partial = target.with_suffix(target.suffix + ".part")
        with partial.open("wb") as out:
            for piece in pieces:
                with piece.open("rb") as handle:
                    shutil.copyfileobj(handle, out)
        actual = sha256_file(partial)
        if actual != digest:
            print(f"SHA256   {target}: joined {actual} != {digest}")
            partial.unlink()
            failures += 1
            continue
        partial.replace(target)
        joined[name] = target
        print(f"REBUILT  {target} ({size:,} B, sha256 {digest})")

    for name in PLAIN + EXTRA:
        source = args.data_dir / name
        size, digest = expected[name]
        actual = sha256_file(source)
        if source.stat().st_size != size or actual != digest:
            print(f"SHA256   {name}: {actual} != {digest}")
            failures += 1
            continue
        print(f"OK       {name} ({size:,} B)")
        if not args.verify_only:
            args.dest.mkdir(parents=True, exist_ok=True)
            target = args.dest / name
            if not target.is_file() or sha256_file(target) != digest:
                shutil.copyfile(source, target)
                joined[name] = target

    if failures:
        print(f"\n{failures} problem(s) found", file=sys.stderr)
        return 1
    print("\nall archives verified" + ("" if args.verify_only else f" in {args.dest}"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
