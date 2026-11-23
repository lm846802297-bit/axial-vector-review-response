#!/usr/bin/env python3
"""Validate research result JSON records and their local output files."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from decimal import Decimal, InvalidOperation
import sys
from pathlib import Path, PurePosixPath

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print("ERROR: install the pinned dependency with python -m pip install -r research/schemas/requirements-result-validation.txt.", file=sys.stderr)
    raise SystemExit(2)


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON numeric constant is forbidden: {value}")


def parse_finite_float(value: str) -> float:
    """Reject JSON floats that overflow or underflow during binary-float parsing."""
    try:
        exact = Decimal(value)
        numeric = float(exact)
    except (InvalidOperation, OverflowError, ValueError) as exc:
        raise ValueError(f"invalid JSON numeric value: {value}") from exc
    if not math.isfinite(numeric):
        raise ValueError(f"JSON numeric value overflows a finite float: {value}")
    if exact != 0 and numeric == 0.0:
        raise ValueError(f"JSON numeric value underflows to zero: {value}")
    return numeric


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        return json.load(
            stream,
            parse_constant=reject_nonstandard_constant,
            parse_float=parse_finite_float,
        )


def referenced_files(record: dict):
    if record.get("record_type") == "run_manifest":
        return record.get("outputs", [])
    if record.get("record_type") == "result_summary":
        return record.get("data_files", [])
    return []


def resolve_repo_path(root: Path, relative_path: str, errors: list):
    rel = Path(relative_path)
    if rel.is_absolute() or ".." in rel.parts:
        errors.append(f"{relative_path}: path must be repository-relative and cannot escape the repo")
        return None
    target = (root / rel).resolve()
    try:
        target.relative_to(root)
    except ValueError:
        errors.append(f"{relative_path}: resolved path escapes repository root")
        return None
    return target


def verify_inputs(record: dict, repo_root: Path):
    errors, warnings = [], []
    if record.get("record_type") != "run_manifest":
        return errors, warnings
    root = repo_root.resolve()
    for item in record.get("inputs", []):
        if not item.get("path"):
            continue
        target = resolve_repo_path(root, item["path"], errors)
        if target is None:
            continue
        if not target.is_file():
            if item.get("uri"):
                warnings.append(f"{item['path']}: external input not present locally; URI/version retained")
            else:
                errors.append(f"{item['path']}: referenced input file does not exist")
            continue
        if item.get("bytes") is not None and target.stat().st_size != item["bytes"]:
            errors.append(f"{item['path']}: input byte size {target.stat().st_size} != manifest {item['bytes']}")
        if item.get("sha256"):
            digest = hashlib.sha256()
            with target.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            if digest.hexdigest() != item["sha256"]:
                errors.append(f"{item['path']}: input SHA-256 mismatch")
    return errors, warnings


def verify_artifacts(record: dict, repo_root: Path):
    errors, warnings = [], []
    root = repo_root.resolve()
    for item in referenced_files(record):
        target = resolve_repo_path(root, item["path"], errors)
        if target is None:
            continue
        if not target.is_file():
            if item.get("uri"):
                warnings.append(f"{item['path']}: external artifact not present locally; URI/version retained")
            else:
                errors.append(f"{item['path']}: referenced output file does not exist")
            continue

        actual_bytes = target.stat().st_size
        if actual_bytes != item["bytes"]:
            errors.append(f"{item['path']}: byte size {actual_bytes} != manifest {item['bytes']}")

        digest = hashlib.sha256()
        with target.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        if digest.hexdigest() != item["sha256"]:
            errors.append(f"{item['path']}: SHA-256 mismatch")

        if item["format"].lower() == "csv":
            try:
                with target.open("r", encoding="utf-8-sig", newline="") as stream:
                    reader = csv.reader(stream)
                    header = next(reader, None)
                    if header is None:
                        errors.append(f"{item['path']}: CSV is empty and has no header")
                        continue
                    if len(header) != len(set(header)):
                        errors.append(f"{item['path']}: duplicate CSV column names")
                    if item.get("columns") is not None and header != item["columns"]:
                        errors.append(f"{item['path']}: CSV header differs from manifest columns")
                    unit_columns = set(item.get("units", {}))
                    missing_unit_columns = set(header) - unit_columns
                    unknown_unit_columns = unit_columns - set(header)
                    if missing_unit_columns:
                        errors.append(f"{item['path']}: unit map is missing columns {sorted(missing_unit_columns)}")
                    if unknown_unit_columns:
                        errors.append(f"{item['path']}: unit map contains unknown columns {sorted(unknown_unit_columns)}")
                    row_count = 0
                    for row in reader:
                        row_count += 1
                        if len(row) != len(header):
                            errors.append(f"{item['path']}: row {row_count + 1} has {len(row)} fields; expected {len(header)}")
                            continue
                        for col_name, cell in zip(header, row):
                            if not cell.strip():
                                continue
                            try:
                                numeric = float(cell)
                            except ValueError:
                                continue
                            if not math.isfinite(numeric):
                                errors.append(f"{item['path']}: non-finite numeric value in {col_name}, data row {row_count}")
                    if item.get("rows") is not None and row_count != item["rows"]:
                        errors.append(f"{item['path']}: CSV has {row_count} data rows; manifest says {item['rows']}")
            except (OSError, UnicodeError, csv.Error) as exc:
                errors.append(f"{item['path']}: CSV read failed: {exc}")
    return errors, warnings


def verify_manifest_checksum(record: dict, record_path: Path):
    """Check the detached checksum when a run manifest declares one."""
    if record.get("record_type") != "run_manifest":
        return []
    extension = record.get("extensions", {}).get("archive_integrity")
    if extension is None:
        return []  # Older v1 records did not have this optional extension.
    if not isinstance(extension, dict) or extension.get("manifest_checksum") != "MANIFEST.sha256":
        return ["invalid manifest checksum declaration"]
    sidecar = record_path.parent / "MANIFEST.sha256"
    try:
        contents = sidecar.read_text(encoding="ascii").strip()
        expected = hashlib.sha256(record_path.read_bytes()).hexdigest()
    except (OSError, UnicodeError) as exc:
        return [f"manifest checksum unavailable: {exc}"]
    if contents != f"{expected}  {record_path.name}":
        return ["run manifest SHA-256 mismatch or invalid checksum sidecar"]
    return []


def verify_source(record: dict, repo_root: Path):
    if record.get("record_type") != "run_manifest":
        return []
    errors = []
    source = record["source"]
    target = resolve_repo_path(repo_root.resolve(), source["script_path"], errors)
    if target is None:
        return errors
    if not target.is_file():
        return [f"{source['script_path']}: source script does not exist"]
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    if digest != source["script_sha256"]:
        errors.append(f"{source['script_path']}: source script SHA-256 mismatch")
    return errors


_FORBIDDEN_GIT_REF_CHARS = frozenset(" ~^:?*[") | {chr(92)}


def is_valid_git_ref(ref: object) -> bool:
    """Return whether ref satisfies git-check-ref-format rules for a full ref."""
    if not isinstance(ref, str) or not ref or ref == "@":
        return False
    if "/" not in ref or ref.startswith("/") or ref.endswith("/") or ref.endswith("."):
        return False
    if ".." in ref or "//" in ref or "@{" in ref:
        return False
    for char in ref:
        codepoint = ord(char)
        if codepoint <= 0x20 or codepoint == 0x7F or char in _FORBIDDEN_GIT_REF_CHARS:
            return False
    components = ref.split("/")
    if any(
        not component or component.startswith(".") or component.endswith(".lock")
        for component in components
    ):
        return False
    return True


def is_valid_git_branch_name(name: object) -> bool:
    """Validate a literal branch name, not a checkout shorthand."""
    if not isinstance(name, str) or not name or name.startswith("-"):
        return False
    return is_valid_git_ref(f"refs/heads/{name}")


def verify_source_control(record: dict) -> list[str]:
    """Validate v1.0.1 source-control provenance relationships.

    JSON Schema handles field presence, types, formats and basic value ranges.
    This function enforces relationships between fields that JSON Schema alone
    cannot safely establish.
    """
    if record.get("record_type") != "run_manifest" or record.get("schema_version") != "1.0.1":
        return []

    errors: list[str] = []
    source = record.get("source")
    execution = record.get("execution")
    if not isinstance(source, dict):
        return ["source must be an object before source-control validation"]
    if not isinstance(execution, dict):
        return ["execution must be an object before source-control validation"]
    context = execution.get("source_control")
    if not isinstance(context, dict):
        return ["v1.0.1 run_manifest is missing execution.source_control"]

    commit_sha = source.get("commit_sha")
    event = context.get("event")
    mode = context.get("checkout_mode")
    is_pr = event in {"pull_request", "pull_request_target"}
    pr_fields = (
        "pr_number", "pr_url", "pr_head_sha", "base_sha",
        "tested_merge_sha", "head_ref", "base_ref",
    )
    pr_modes = {"pull_request_merge", "pull_request_head", "pull_request_base", "unknown"}
    non_pr_modes = {"branch_commit", "detached_commit", "unknown"}

    checkout_ref = context.get("checkout_ref")
    checkout_ref_valid = checkout_ref is None or (
        isinstance(checkout_ref, str)
        and checkout_ref.startswith("refs/")
        and is_valid_git_ref(checkout_ref)
    )
    if checkout_ref is not None and not checkout_ref_valid:
        errors.append("checkout_ref must be a valid fully qualified Git ref under refs/")

    if is_pr:
        for field in ("pr_number", "pr_url", "pr_head_sha", "base_sha", "head_ref", "base_ref"):
            if context.get(field) is None:
                errors.append(f"pull-request source_control requires non-null {field}")
        for field in ("head_ref", "base_ref"):
            branch_name = context.get(field)
            if branch_name is not None and not is_valid_git_branch_name(branch_name):
                errors.append(f"{field} must be a valid Git branch name")
        if mode not in pr_modes:
            errors.append("pull-request event requires a pull-request checkout_mode")
        elif checkout_ref is not None and checkout_ref_valid:
            pr_number = context.get("pr_number")
            head_ref = context.get("head_ref")
            base_ref = context.get("base_ref")
            if mode == "pull_request_merge":
                expected_ref = f"refs/pull/{pr_number}/merge"
                if checkout_ref != expected_ref:
                    errors.append(
                        f"pull_request_merge checkout_ref must be {expected_ref} when known"
                    )
            elif mode == "pull_request_head":
                allowed_refs = {
                    f"refs/pull/{pr_number}/head",
                    f"refs/heads/{head_ref}",
                }
                if checkout_ref not in allowed_refs:
                    errors.append(
                        "pull_request_head checkout_ref must identify the PR head ref when known"
                    )
            elif mode == "pull_request_base":
                expected_ref = f"refs/heads/{base_ref}"
                if checkout_ref != expected_ref:
                    errors.append(
                        "pull_request_base checkout_ref must identify the PR base branch when known"
                    )
        tested_merge_sha = context.get("tested_merge_sha")
        if mode == "pull_request_merge":
            if tested_merge_sha is None:
                errors.append("pull_request_merge requires tested_merge_sha")
            elif tested_merge_sha != commit_sha:
                errors.append("tested_merge_sha must equal source.commit_sha for pull_request_merge")
        elif mode == "pull_request_head":
            if commit_sha != context.get("pr_head_sha"):
                errors.append("source.commit_sha must equal pr_head_sha for pull_request_head")
            if tested_merge_sha is not None:
                errors.append("tested_merge_sha must be null for pull_request_head")
        elif mode == "pull_request_base":
            if commit_sha != context.get("base_sha"):
                errors.append("source.commit_sha must equal base_sha for pull_request_base")
            if tested_merge_sha is not None:
                errors.append("tested_merge_sha must be null for pull_request_base")
        elif mode == "unknown" and tested_merge_sha is not None:
            errors.append("tested_merge_sha must be null when PR checkout_mode is unknown")
    else:
        for field in pr_fields:
            if context.get(field) is not None:
                errors.append(f"non-PR event requires {field} to be null")
        if mode not in non_pr_modes:
            errors.append("non-PR event cannot use a pull-request checkout_mode")
        if mode == "branch_commit":
            if checkout_ref is None:
                errors.append("branch_commit requires checkout_ref")
            elif checkout_ref_valid and not checkout_ref.startswith("refs/heads/"):
                errors.append("branch_commit checkout_ref must be under refs/heads/")
        elif mode == "detached_commit" and checkout_ref is not None:
            errors.append("checkout_ref must be null for detached_commit")

    workflow_run_id = context.get("workflow_run_id")
    workflow_run_attempt = context.get("workflow_run_attempt")
    legacy_workflow_run_id = source.get("workflow_run_id")
    if legacy_workflow_run_id is not None and legacy_workflow_run_id != workflow_run_id:
        errors.append("source.workflow_run_id must match execution.source_control.workflow_run_id when present")
    if (workflow_run_id is None) != (workflow_run_attempt is None):
        errors.append("workflow_run_id and workflow_run_attempt must both be null or both be present")
    if isinstance(workflow_run_id, str) and not workflow_run_id.strip():
        errors.append("workflow_run_id must not be an empty string")
    if workflow_run_attempt is not None and (
        isinstance(workflow_run_attempt, bool)
        or not isinstance(workflow_run_attempt, int)
        or workflow_run_attempt < 1
    ):
        errors.append("workflow_run_attempt must be a positive integer")

    tree_state = context.get("working_tree_state")
    dirty_paths = context.get("dirty_paths")
    if not isinstance(dirty_paths, list):
        errors.append("dirty_paths must be an array")
        dirty_paths = []
    if tree_state == "clean" and dirty_paths:
        errors.append("working_tree_state clean requires dirty_paths to be empty")
    elif tree_state == "dirty" and not dirty_paths:
        errors.append("working_tree_state dirty requires at least one dirty path")

    seen: set[str] = set()
    for path in dirty_paths:
        if not isinstance(path, str) or not path:
            errors.append("dirty_paths entries must be non-empty strings")
            continue
        if "\x00" in path:
            errors.append("dirty path must not contain NUL")
            continue
        if "\\" in path or path.startswith("/") or (len(path) >= 2 and path[1] == ":"):
            errors.append(f"dirty path must be repository-relative POSIX form: {path}")
            continue
        normalized = PurePosixPath(path)
        if normalized.is_absolute() or normalized.as_posix() == "." or ".." in normalized.parts or normalized.as_posix() != path:
            errors.append(f"dirty path must be normalized and cannot escape the repository: {path}")
            continue
        if path in seen:
            errors.append(f"dirty_paths contains duplicate path: {path}")
        seen.add(path)

    return errors


def success_message(record: dict) -> str:
    """Describe only the validation layers applicable to this record type and version."""
    record_type = record.get("record_type")
    if record_type == "run_manifest":
        if record.get("schema_version") == "1.0.1":
            return "schema, source-control provenance, and local input/output integrity"
        return "schema and local input/output integrity"
    if record_type == "result_summary":
        return "schema and local data-file integrity"
    return "schema"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="+", type=Path, help="JSON record files to validate")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="repository root for output paths")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().with_name("research-result-record-v1.0.1.schema.json"),
        help="JSON Schema Draft 2020-12 file",
    )
    args = parser.parse_args()

    try:
        schema = load_json(args.schema)
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        print(f"ERROR: invalid schema {args.schema}: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    failed = False
    for record_path in args.records:
        try:
            record = load_json(record_path)
        except Exception as exc:
            print(f"FAIL {record_path}: JSON parse error: {exc}")
            failed = True
            continue

        errors = sorted(
            validator.iter_errors(record),
            key=lambda error: (list(map(str, error.absolute_path)), error.message),
        )
        if errors:
            print(f"FAIL {record_path}: schema validation")
            for error in errors:
                location = ".".join(map(str, error.absolute_path)) or "<root>"
                print(f"  - {location}: {error.message}")
            failed = True
            continue

        input_errors, input_warnings = verify_inputs(record, args.repo_root)
        file_errors, file_warnings = verify_artifacts(record, args.repo_root)
        source_control_errors = verify_source_control(record)
        integrity_errors = (input_errors + file_errors + verify_source(record, args.repo_root)
                            + verify_manifest_checksum(record, record_path))
        if source_control_errors:
            print(f"FAIL {record_path}: source-control provenance")
            for error in source_control_errors:
                print(f"  - {error}")
            failed = True
        if integrity_errors:
            print(f"FAIL {record_path}: input/output integrity")
            for error in integrity_errors:
                print(f"  - {error}")
            failed = True
        elif not source_control_errors:
            print(f"PASS {record_path}: {success_message(record)}")
        for warning in input_warnings + file_warnings:
            print(f"WARN {record_path}: {warning}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
