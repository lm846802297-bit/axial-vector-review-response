from __future__ import annotations


def source_control(event: str = "local", mode: str = "branch_commit") -> dict:
    is_pr = event in {"pull_request", "pull_request_target"}
    return {
        "event": event,
        "checkout_mode": mode,
        "checkout_ref": "refs/pull/104/merge" if mode == "pull_request_merge" else ("refs/heads/main" if mode == "branch_commit" else None),
        "pr_number": 104 if is_pr else None,
        "pr_url": "https://github.com/example/research/pull/104" if is_pr else None,
        "pr_head_sha": "b" * 40 if is_pr else None,
        "base_sha": "c" * 40 if is_pr else None,
        "tested_merge_sha": "a" * 40 if mode == "pull_request_merge" else None,
        "head_ref": "feature/example" if is_pr else None,
        "base_ref": "main" if is_pr else None,
        "workflow_run_id": 123456 if is_pr else None,
        "workflow_run_attempt": 1 if is_pr else None,
        "working_tree_state": "clean",
        "dirty_paths": [],
    }


def minimal_manifest(version: str = "1.0.1", event: str = "local", mode: str = "branch_commit") -> dict:
    is_pr = event in {"pull_request", "pull_request_target"}
    commit_sha = "a" * 40
    if is_pr and mode == "pull_request_head":
        commit_sha = "b" * 40
    elif is_pr and mode == "pull_request_base":
        commit_sha = "c" * 40
    record = {
        "schema_version": version,
        "record_type": "run_manifest",
        "run_id": "TEST-RUN-001",
        "created_at": "2026-11-23T00:00:00Z",
        "project": {"repository": "example/research", "project_id": "validator-test"},
        "source": {
            "commit_sha": commit_sha,
            "branch": "feature/example" if is_pr else "main",
            "script_path": "run.py",
            "script_sha256": "d" * 64,
        },
        "inputs": [],
        "configuration": {"physics": {}, "numerics": {}, "conventions": {}},
        "environment": {
            "platform": "Linux",
            "runtime": {"python": "3.13.5"},
            "dependencies": {"jsonschema": "4.26.0"},
            "hardware": {"cpu": "test"},
        },
        "execution": {
            "status": "succeeded",
            "command": "python run.py",
            "started_at": "2026-11-23T00:00:00Z",
            "finished_at": "2026-11-23T00:00:01Z",
        },
        "outputs": [],
        "validation": {"status": "not_run", "checks": []},
        "archive": {"status": "local_only"},
    }
    if version == "1.0.1":
        record["execution"]["source_control"] = source_control(event, mode)
    return record


def minimal_result_summary(version: str = "1.0.0") -> dict:
    return {
        "schema_version": version,
        "record_type": "result_summary",
        "run_id": "TEST-RUN-001",
        "created_at": "2026-11-23T00:00:00Z",
        "project": {"repository": "example/research", "project_id": "validator-test"},
        "calculation": "schema compatibility fixture",
        "scope": {"included": [], "excluded": []},
        "benchmark": {},
        "observables": [],
        "data_files": [],
        "scientific_status": "diagnostic",
    }


def minimal_validation_report(version: str = "1.0.0") -> dict:
    return {
        "schema_version": version,
        "record_type": "validation_report",
        "run_id": "TEST-RUN-001",
        "created_at": "2026-11-23T00:00:00Z",
        "status": "not_run",
        "checks": [],
    }
