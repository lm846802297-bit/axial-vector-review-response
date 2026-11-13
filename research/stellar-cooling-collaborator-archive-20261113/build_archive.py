"""Build a deduplicated collaborator ZIP from the tracked research tree.

Large SFHo-FRDM ZIP payloads remain in the documented GitHub Release.
All other tracked stellar-cooling source, reports, tests, and results are
included once by SHA-256. Byte-identical model-variant aliases are recorded
in the file catalog rather than copied a second time.
"""
from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PACKAGE_NAME = "Stellar_Cooling_Research_Archive_2026-11-13"
SOURCE_ROOTS = [
    ("research/stellar-cooling-constraints-20261105/",
     "01_axial_benchmark_and_transport/"),
    ("research/stellar-cooling-shared-20261105/",
     "02_model_variants/stellar-cooling-shared-20261105/"),
    ("research/stellar-cooling-original-uv-model-20261105/",
     "02_model_variants/stellar-cooling-original-uv-model-20261105/"),
    ("research/stellar-cooling-two-vev-20261105/",
     "02_model_variants/stellar-cooling-two-vev-20261105/"),
    ("research/stellar-cooling-eft-literature-20261105/",
     "02_model_variants/stellar-cooling-eft-literature-20261105/"),
]
WORKFLOW_RE = re.compile("(stellar|cooling|b13|b16|sfho|eos|vector)", re.I)
EOS_RELEASE = (
    "https://github.com/lm846802297-bit/axial-vector-review-response/"
    "releases/tag/sfho-frdm-v1.03-data"
)


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=REPO, text=True).strip()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def describe(path: str, data: bytes) -> str:
    suffix = PurePosixPath(path).suffix.lower()
    name = PurePosixPath(path).name
    if suffix in {".md", ".rst"}:
        text = data.decode("utf-8", errors="replace")
        lines = [line.strip() for line in text.splitlines()]
        title = next((line.lstrip("#").strip() for line in lines
                      if line.startswith("#")), "")
        paragraph = next((line for line in lines
                          if line and not line.startswith("#")
                          and not line.startswith("|")
                          and not line.startswith(chr(96) * 3)
                          and not line.startswith("---")), "")
        summary = (paragraph or title or name).replace("|", " ")
        return f"Research note/report: {title or name}. {summary[:180]}"
    if suffix == ".py":
        text = data.decode("utf-8", errors="replace")
        try:
            doc = ast.get_docstring(ast.parse(text))
        except (SyntaxError, ValueError):
            doc = None
        if doc:
            return "Python source: " + " ".join(doc.split())[:220]
        return f"Python source / driver / test: {name}"
    if suffix == ".json":
        try:
            obj = json.loads(data)
            summary = obj.get("description") or obj.get("title") or obj.get("stage")
            if summary:
                return f"Machine-readable result: {str(summary)[:220]}"
        except (ValueError, UnicodeDecodeError, AttributeError):
            pass
        return f"Machine-readable audit or calculation output: {name}"
    if suffix == ".csv":
        first = data.decode("utf-8", errors="replace").splitlines()
        header = first[0][:180] if first else ""
        return f"Tabular numerical data; first-row fields: {header}"
    if suffix == ".pdf":
        return f"PDF figure, source document, or manual; inspect visually: {name}"
    if suffix in {".yml", ".yaml"}:
        return f"GitHub Actions workflow for stellar-cooling research: {name}"
    if suffix in {".txt", ".sha256"}:
        first = data.decode("utf-8", errors="replace").splitlines()
        return f"Text provenance / dependency / checksum record: {(first[0] if first else name)[:180]}"
    return f"Research source or supporting asset: {name}"


def git_blob_map():
    output = subprocess.check_output(
        ["git", "ls-tree", "-r", "HEAD"], cwd=REPO, text=True
    )
    result = {}
    for line in output.splitlines():
        try:
            meta, path = line.split(chr(9), 1)
            result[path] = meta.split()[2]
        except (ValueError, IndexError):
            continue
    return result


def eos_manifest_hashes():
    manifest = (
        REPO / "research/stellar-cooling-constraints-20261105/"
        "blinov_reproduction/data/sfho-frdm-v1.03/MANIFEST.sha256"
    )
    result = {}
    if not manifest.exists():
        return result
    for line in manifest.read_text(encoding="utf-8", errors="replace").splitlines():
        fields = line.split()
        if len(fields) >= 2 and len(fields[0]) == 64:
            result[PurePosixPath(fields[-1].lstrip("*")).name] = fields[0].lower()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=REPO / "dist" /
                        "Stellar_Cooling_Research_Archive_2026-11-13.zip")
    parser.add_argument("--generated-figures", type=Path, default=None)
    args = parser.parse_args()

    output = args.output if args.output.is_absolute() else REPO / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = output.parent / (PACKAGE_NAME + "_staging")
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    package = stage / PACKAGE_NAME
    package.mkdir()

    source_commit = run_git("rev-parse", "HEAD")
    try:
        source_branch = os.environ.get("GITHUB_REF_NAME") or run_git("branch", "--show-current")
    except subprocess.CalledProcessError:
        source_branch = "detached"
    blobs = git_blob_map()
    eos_hashes = eos_manifest_hashes()
    seen = {}
    rows = []
    included_count = 0
    duplicate_count = 0
    external_count = 0

    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=REPO
    ).decode("utf-8", errors="surrogateescape").split(chr(0))
    tracked = [p for p in tracked if p]

    def record_external(path: str, target: Path):
        nonlocal external_count
        size = target.stat().st_size
        digest = eos_hashes.get(target.name, "")
        rows.append({
            "source_path": path, "package_path": "",
            "status": "external_release_not_bundled",
            "sha256": digest, "git_blob_sha": blobs.get(path, ""),
            "size_bytes": size,
            "description": (
                "Large official SFHo-FRDM EOS ZIP payload; intentionally not "
                "duplicated in the collaborator ZIP. Retrieve from " + EOS_RELEASE
            ),
        })
        external_count += 1

    for source_prefix, package_prefix in SOURCE_ROOTS:
        for path in tracked:
            if not path.startswith(source_prefix):
                continue
            if "/review_package_extracted/" in path:
                continue
            source = REPO / path
            if not source.is_file():
                continue
            rel = path[len(source_prefix):]
            is_large_eos = (
                "data/sfho-frdm-v1.03/" in rel
                and (rel.endswith(".zip") or ".zip.part-" in rel)
            )
            if is_large_eos:
                record_external(path, source)
                continue
            data = source.read_bytes()
            digest = sha256_bytes(data)
            package_path = package_prefix + rel
            if digest in seen:
                canonical = seen[digest]
                rows.append({
                    "source_path": path, "package_path": canonical,
                    "status": "deduplicated_alias",
                    "sha256": digest, "git_blob_sha": blobs.get(path, ""),
                    "size_bytes": len(data),
                    "description": (
                        f"Byte-identical to {canonical}; stored once to avoid "
                        "duplicating a shared source file."
                    ),
                })
                duplicate_count += 1
                continue
            seen[digest] = package_path
            dest = package / package_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            rows.append({
                "source_path": path, "package_path": package_path,
                "status": "included",
                "sha256": digest, "git_blob_sha": blobs.get(path, ""),
                "size_bytes": len(data), "description": describe(path, data),
            })
            included_count += 1

    for path in tracked:
        if not path.startswith(".github/workflows/"):
            continue
        if not WORKFLOW_RE.search(PurePosixPath(path).name):
            continue
        source = REPO / path
        data = source.read_bytes()
        digest = sha256_bytes(data)
        package_path = "06_reproduction_workflows/" + PurePosixPath(path).name
        if digest in seen:
            rows.append({
                "source_path": path, "package_path": seen[digest],
                "status": "deduplicated_alias", "sha256": digest,
                "git_blob_sha": blobs.get(path, ""), "size_bytes": len(data),
                "description": "Byte-identical workflow/source already stored once.",
            })
            duplicate_count += 1
            continue
        seen[digest] = package_path
        dest = package / package_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        rows.append({
            "source_path": path, "package_path": package_path,
            "status": "included", "sha256": digest,
            "git_blob_sha": blobs.get(path, ""), "size_bytes": len(data),
            "description": describe(path, data),
        })
        included_count += 1

    start = package / "00_START_HERE"
    start.mkdir(parents=True, exist_ok=True)
    docs = ["README.md", "STATUS_MATRIX.md", "FIGURE_AUDIT.md",
            "REVIEW_CHECKLIST.md", "requirements-review.txt"]
    for name in docs:
        data = (HERE / name).read_bytes()
        dest = start / name
        dest.write_bytes(data)
        rows.append({
            "source_path": str((HERE / name).relative_to(REPO)).replace(chr(92), "/"),
            "package_path": f"00_START_HERE/{name}",
            "status": "archive_document", "sha256": sha256_bytes(data),
            "git_blob_sha": blobs.get(
                str((HERE / name).relative_to(REPO)).replace(chr(92), "/"), ""),
            "size_bytes": len(data), "description": describe(name, data),
        })

    tool_dest = start / "tools"
    tool_dest.mkdir(exist_ok=True)
    builder_data = Path(__file__).read_bytes()
    (tool_dest / "build_archive.py").write_bytes(builder_data)
    rows.append({
        "source_path": str(Path(__file__).relative_to(REPO)).replace(chr(92), "/"),
        "package_path": "00_START_HERE/tools/build_archive.py",
        "status": "archive_tool", "sha256": sha256_bytes(builder_data),
        "git_blob_sha": blobs.get(
            str(Path(__file__).relative_to(REPO)).replace(chr(92), "/"), ""),
        "size_bytes": len(builder_data),
        "description": "Standard-library builder for the deduplicated collaborator ZIP; run from a repository checkout.",
    })

    generated = []
    if args.generated_figures and args.generated_figures.exists():
        for source in sorted(args.generated_figures.iterdir()):
            if not source.is_file():
                continue
            data = source.read_bytes()
            digest = sha256_bytes(data)
            package_path = "01_axial_benchmark_and_transport/outputs/reviewed_loglog/" + source.name
            if digest in seen:
                rows.append({
                    "source_path": str(source), "package_path": seen[digest],
                    "status": "deduplicated_alias", "sha256": digest,
                    "git_blob_sha": "", "size_bytes": len(data),
                    "description": "Generated review output is byte-identical to an existing package file.",
                })
                duplicate_count += 1
                continue
            seen[digest] = package_path
            dest = package / package_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            rows.append({
                "source_path": str(source), "package_path": package_path,
                "status": "generated_in_archive", "sha256": digest,
                "git_blob_sha": "", "size_bytes": len(data),
                "description": describe(source.name, data),
            })
            generated.append(package_path)

    provenance = {
        "archive_name": PACKAGE_NAME + ".zip",
        "snapshot_date": "2026-11-13",
        "build_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_repository": "lm846802297-bit/axial-vector-review-response",
        "source_branch": source_branch,
        "source_commit": source_commit,
        "source_roots": [p for p, _ in SOURCE_ROOTS],
        "included_unique_source_files": included_count,
        "deduplicated_alias_count": duplicate_count,
        "large_eos_payloads_not_bundled": external_count,
        "generated_review_outputs": generated,
        "eos_release": EOS_RELEASE,
        "garching_raw_profile_included": False,
        "scientific_status": (
            "Conditional fixed-profile axial-EFT ballistic benchmark; not a "
            "final SN1987A exclusion. Pure-vector Fig. 7 end-to-end acceptance "
            "and several physical transport gates remain open."
        ),
    }
    provenance_data = (json.dumps(provenance, indent=2) + chr(10)).encode("utf-8")
    (start / "ARCHIVE_PROVENANCE.json").write_bytes(provenance_data)
    rows.append({
        "source_path": "", "package_path": "00_START_HERE/ARCHIVE_PROVENANCE.json",
        "status": "archive_provenance", "sha256": sha256_bytes(provenance_data),
        "git_blob_sha": "", "size_bytes": len(provenance_data),
        "description": "Pinned repository commit, build metadata, file counts, EOS release link, and scientific status.",
    })

    catalog_path = start / "SOURCE_FILE_CATALOG.csv"
    rows.extend([
        {
            "source_path": "", "package_path": "00_START_HERE/SOURCE_FILE_CATALOG.csv",
            "status": "catalog_index", "sha256": "", "git_blob_sha": "",
            "size_bytes": "",
            "description": "This index describes every source, generated output, external payload, and alias in the archive; its own checksum is in SHA256SUMS.txt.",
        },
        {
            "source_path": "", "package_path": "00_START_HERE/SHA256SUMS.txt",
            "status": "integrity_manifest", "sha256": "", "git_blob_sha": "",
            "size_bytes": "",
            "description": "SHA-256 manifest for every packaged file except this manifest itself.",
        },
    ])
    fieldnames = ["source_path", "package_path", "status", "size_bytes",
                  "sha256", "git_blob_sha", "description"]
    with catalog_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: (
            row["source_path"], row["status"])))

    checksum_path = start / "SHA256SUMS.txt"
    checksum_lines = []
    for path in sorted(p for p in package.rglob("*") if p.is_file()
                       and p != checksum_path):
        rel = path.relative_to(package).as_posix()
        checksum_lines.append(f"{sha256_bytes(path.read_bytes())}  {rel}")
    checksum_path.write_text(chr(10).join(checksum_lines) + chr(10),
                             encoding="utf-8")

    # Fail closed if two packaged files have identical bytes.
    hashes = {}
    for path in package.rglob("*"):
        if not path.is_file():
            continue
        digest = sha256_bytes(path.read_bytes())
        if digest in hashes:
            raise RuntimeError(
                f"Duplicate packaged content: {path} == {hashes[digest]}"
            )
        hashes[digest] = path

    # Validate the checksum manifest before creating the ZIP.
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        if sha256_bytes((package / rel).read_bytes()) != digest:
            raise RuntimeError(f"Checksum validation failed: {rel}")

    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=6) as archive:
        for path in sorted(package.rglob("*")):
            if path.is_file():
                archive.write(path, (Path(PACKAGE_NAME) /
                                     path.relative_to(package)).as_posix())
    with zipfile.ZipFile(output, "r") as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"Corrupt ZIP member: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise RuntimeError("Duplicate ZIP member names")
    print(json.dumps({
        "output": str(output),
        "bytes": output.stat().st_size,
        "included_unique_source_files": included_count,
        "deduplicated_alias_count": duplicate_count,
        "external_large_eos_payloads": external_count,
        "catalog_rows": len(rows),
        "package_files": len(hashes),
        "generated_review_outputs": generated,
        "source_commit": source_commit,
    }, indent=2))


if __name__ == "__main__":
    main()
