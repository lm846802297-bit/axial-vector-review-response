from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCHEMA_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCHEMA_DIR))
from validate_result_records import success_message, verify_source_control  # noqa: E402
from rcrps_v1_0_1_fixtures import minimal_manifest  # noqa: E402


class SourceControlSemanticTests(unittest.TestCase):
    def errors(self, record: dict) -> list[str]:
        return verify_source_control(record)

    def test_valid_pr_merge_checkout(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_merge")
        self.assertEqual(self.errors(record), [])

    def test_merge_checkout_sha_must_equal_source_commit(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_merge")
        record["execution"]["source_control"]["tested_merge_sha"] = "e" * 40
        self.assertTrue(any("tested_merge_sha" in error for error in self.errors(record)))

    def test_valid_pr_head_checkout(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_head")
        self.assertEqual(self.errors(record), [])

    def test_head_checkout_sha_must_equal_pr_head(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_head")
        record["source"]["commit_sha"] = "e" * 40
        self.assertTrue(any("pr_head_sha" in error for error in self.errors(record)))

    def test_head_checkout_rejects_tested_merge_sha(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_head")
        record["execution"]["source_control"]["tested_merge_sha"] = "e" * 40
        self.assertTrue(any("tested_merge_sha" in error for error in self.errors(record)))

    def test_valid_pr_base_checkout(self):
        record = minimal_manifest(event="pull_request_target", mode="pull_request_base")
        self.assertEqual(self.errors(record), [])

    def test_pr_base_checkout_requires_base_sha(self):
        record = minimal_manifest(event="pull_request_target", mode="pull_request_base")
        record["source"]["commit_sha"] = "e" * 40
        self.assertTrue(any("base_sha" in error for error in self.errors(record)))

    def test_valid_unknown_pr_checkout(self):
        record = minimal_manifest(event="pull_request", mode="unknown")
        self.assertEqual(self.errors(record), [])

    def test_unknown_pr_checkout_rejects_tested_merge_sha(self):
        record = minimal_manifest(event="pull_request", mode="unknown")
        record["execution"]["source_control"]["tested_merge_sha"] = "e" * 40
        self.assertTrue(any("tested_merge_sha" in error for error in self.errors(record)))

    def test_checkout_ref_must_be_valid_fully_qualified_git_ref(self):
        invalid_refs = (
            "main",
            "refs/heads/foo bar",
            "refs/heads/main..evil",
            "refs/heads/foo.lock",
            "refs/heads/foo.",
            "refs/heads/foo@{bar}",
            "refs/heads/foo//bar",
            "refs/heads/.hidden",
            "refs/heads/foo^bar",
        )
        for checkout_ref in invalid_refs:
            with self.subTest(checkout_ref=checkout_ref):
                record = minimal_manifest(event="push", mode="branch_commit")
                record["execution"]["source_control"]["checkout_ref"] = checkout_ref
                self.assertTrue(
                    any("checkout_ref" in error for error in self.errors(record)),
                    checkout_ref,
                )

    def test_pr_branch_names_must_follow_git_branch_rules(self):
        invalid_names = ("feature branch", "main..evil", "foo.lock", ".hidden", "-leading-dash", "foo@{bar}")
        for field in ("head_ref", "base_ref"):
            for branch_name in invalid_names:
                with self.subTest(field=field, branch_name=branch_name):
                    record = minimal_manifest(event="pull_request", mode="pull_request_merge")
                    record["execution"]["source_control"][field] = branch_name
                    self.assertTrue(
                        any(field in error for error in self.errors(record)),
                        f"{field}={branch_name!r}",
                    )

    def test_pr_merge_checkout_ref_matches_pr_number_and_mode(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_merge")
        self.assertEqual(self.errors(record), [])
        for checkout_ref in ("refs/pull/104/head", "refs/pull/105/merge", "refs/heads/main"):
            with self.subTest(checkout_ref=checkout_ref):
                broken = minimal_manifest(event="pull_request", mode="pull_request_merge")
                broken["execution"]["source_control"]["checkout_ref"] = checkout_ref
                self.assertTrue(
                    any("checkout_ref" in error for error in self.errors(broken)),
                    checkout_ref,
                )

    def test_pr_head_checkout_ref_matches_head_branch_or_pull_ref(self):
        for checkout_ref in ("refs/pull/104/head", "refs/heads/feature/example"):
            with self.subTest(valid_checkout_ref=checkout_ref):
                record = minimal_manifest(event="pull_request", mode="pull_request_head")
                record["execution"]["source_control"]["checkout_ref"] = checkout_ref
                self.assertEqual(self.errors(record), [])
        for checkout_ref in ("refs/pull/104/merge", "refs/heads/main"):
            with self.subTest(invalid_checkout_ref=checkout_ref):
                record = minimal_manifest(event="pull_request", mode="pull_request_head")
                record["execution"]["source_control"]["checkout_ref"] = checkout_ref
                self.assertTrue(
                    any("checkout_ref" in error for error in self.errors(record)),
                    checkout_ref,
                )

    def test_pr_base_checkout_ref_matches_base_branch(self):
        record = minimal_manifest(event="pull_request_target", mode="pull_request_base")
        record["execution"]["source_control"]["checkout_ref"] = "refs/heads/main"
        self.assertEqual(self.errors(record), [])
        for checkout_ref in ("refs/pull/104/merge", "refs/pull/104/head", "refs/heads/feature/example"):
            with self.subTest(checkout_ref=checkout_ref):
                broken = minimal_manifest(event="pull_request_target", mode="pull_request_base")
                broken["execution"]["source_control"]["checkout_ref"] = checkout_ref
                self.assertTrue(
                    any("checkout_ref" in error for error in self.errors(broken)),
                    checkout_ref,
                )

    def test_non_pr_branch_commit_requires_heads_ref(self):
        record = minimal_manifest(event="push", mode="branch_commit")
        record["execution"]["source_control"]["checkout_ref"] = "refs/heads/main"
        self.assertEqual(self.errors(record), [])
        record["execution"]["source_control"]["checkout_ref"] = "refs/tags/v1.0.1"
        self.assertTrue(any("checkout_ref" in error for error in self.errors(record)))

    def test_non_pr_events_accept_explicit_null_pr_fields(self):
        for event in ("local", "push", "workflow_dispatch", "schedule", "workflow_run"):
            with self.subTest(event=event):
                record = minimal_manifest(event=event, mode="branch_commit")
                self.assertEqual(self.errors(record), [])

    def test_non_pr_rejects_non_null_pr_fields(self):
        values = {
            "pr_number": 104,
            "pr_url": "https://github.com/example/research/pull/104",
            "pr_head_sha": "b" * 40,
            "base_sha": "c" * 40,
            "tested_merge_sha": "a" * 40,
            "head_ref": "feature/example",
            "base_ref": "main",
        }
        for field, value in values.items():
            with self.subTest(field=field):
                record = minimal_manifest()
                record["execution"]["source_control"][field] = value
                self.assertTrue(self.errors(record), field)

    def test_pr_checkout_mode_rejected_for_non_pr(self):
        record = minimal_manifest()
        record["execution"]["source_control"]["checkout_mode"] = "pull_request_head"
        self.assertTrue(any("checkout_mode" in error for error in self.errors(record)))

    def test_non_pr_checkout_mode_rejected_for_pr(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_merge")
        record["execution"]["source_control"]["checkout_mode"] = "branch_commit"
        self.assertTrue(any("checkout_mode" in error for error in self.errors(record)))

    def test_branch_commit_requires_checkout_ref(self):
        record = minimal_manifest(event="push", mode="branch_commit")
        record["execution"]["source_control"]["checkout_ref"] = None
        self.assertTrue(any("checkout_ref" in error for error in self.errors(record)))

    def test_detached_commit_requires_null_checkout_ref(self):
        record = minimal_manifest(event="local", mode="detached_commit")
        record["execution"]["source_control"]["checkout_ref"] = "refs/heads/main"
        self.assertTrue(any("checkout_ref" in error for error in self.errors(record)))

    def test_legacy_source_workflow_run_id_must_match_source_control(self):
        record = minimal_manifest(event="push", mode="branch_commit")
        record["source"]["workflow_run_id"] = 123456
        record["execution"]["source_control"]["workflow_run_id"] = 123456
        record["execution"]["source_control"]["workflow_run_attempt"] = 1
        self.assertEqual(self.errors(record), [])
        record["source"]["workflow_run_id"] = 654321
        self.assertTrue(any("source.workflow_run_id" in error for error in self.errors(record)))

    def test_workflow_run_id_and_attempt_must_be_paired(self):
        record = minimal_manifest()
        record["execution"]["source_control"]["workflow_run_id"] = 123
        self.assertTrue(any("workflow_run_id" in error for error in self.errors(record)))
        record = minimal_manifest()
        record["execution"]["source_control"]["workflow_run_attempt"] = 1
        self.assertTrue(any("workflow_run_attempt" in error for error in self.errors(record)))
        record = minimal_manifest()
        record["execution"]["source_control"]["workflow_run_id"] = ""
        record["execution"]["source_control"]["workflow_run_attempt"] = 1
        self.assertTrue(any("workflow_run_id" in error for error in self.errors(record)))

    def test_clean_tree_requires_empty_dirty_paths(self):
        record = minimal_manifest()
        record["execution"]["source_control"]["dirty_paths"] = ["src/model.py"]
        self.assertTrue(any("clean" in error for error in self.errors(record)))

    def test_dirty_tree_requires_paths(self):
        record = minimal_manifest()
        record["execution"]["source_control"]["working_tree_state"] = "dirty"
        self.assertTrue(any("dirty" in error for error in self.errors(record)))

    def test_dirty_paths_must_be_safe_and_unique(self):
        for paths in (["/etc/passwd"], ["../escape.py"], ["src\\model.py"], ["./src/model.py"], ["src//model.py"], ["."], ["src/\x00model.py"], ["src/model.py", "src/model.py"]):
            with self.subTest(paths=paths):
                record = minimal_manifest()
                record["execution"]["source_control"]["working_tree_state"] = "dirty"
                record["execution"]["source_control"]["dirty_paths"] = list(paths)
                self.assertTrue(self.errors(record))

    def test_v100_manifest_bypasses_source_control_semantics(self):
        record = minimal_manifest(version="1.0.0")
        record["execution"].pop("source_control", None)
        self.assertEqual(self.errors(record), [])

    def test_source_branch_is_not_misread_as_checkout_ref(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_merge")
        record["source"]["branch"] = "104/merge"
        self.assertEqual(self.errors(record), [])



class ValidatorSuccessMessageTests(unittest.TestCase):
    def test_success_message_reports_only_applicable_validation_layers(self):
        cases = (
            (
                {"record_type": "run_manifest", "schema_version": "1.0.1"},
                "schema, source-control provenance, and local input/output integrity",
            ),
            (
                {"record_type": "run_manifest", "schema_version": "1.0.0"},
                "schema and local input/output integrity",
            ),
            (
                {"record_type": "result_summary", "schema_version": "1.0.1"},
                "schema and local data-file integrity",
            ),
            (
                {"record_type": "validation_report", "schema_version": "1.0.1"},
                "schema",
            ),
        )
        for record, expected in cases:
            with self.subTest(record_type=record["record_type"], version=record["schema_version"]):
                self.assertEqual(success_message(record), expected)


class ValidatorCliSchemaSelectionTests(unittest.TestCase):
    def run_cli(self, record: dict, schema_path: Path | None = None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / "run.py"
            script.write_text("print('rcrps fixture')\n", encoding="utf-8")
            record = json.loads(json.dumps(record))
            record["source"]["script_path"] = "run.py"
            record["source"]["script_sha256"] = hashlib.sha256(script.read_bytes()).hexdigest()
            record_path = root / "run_manifest.json"
            record_path.write_text(json.dumps(record), encoding="utf-8")
            command = [sys.executable, str(SCHEMA_DIR / "validate_result_records.py"), "--repo-root", str(root)]
            if schema_path is not None:
                command.extend(["--schema", str(schema_path)])
            command.append(str(record_path))
            return subprocess.run(command, capture_output=True, text=True, check=False)

    def test_default_cli_accepts_v100_records(self):
        result = self.run_cli(minimal_manifest(version="1.0.0"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("source-control provenance", result.stdout)

    def test_default_cli_accepts_v101_local_records(self):
        result = self.run_cli(minimal_manifest(version="1.0.1", event="local", mode="branch_commit"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("source-control provenance", result.stdout)

    def test_default_cli_accepts_v101_pr_records(self):
        result = self.run_cli(minimal_manifest(version="1.0.1", event="pull_request", mode="pull_request_merge"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_default_cli_rejects_v101_manifest_with_invalid_checkout_sha(self):
        record = minimal_manifest(version="1.0.1", event="pull_request", mode="pull_request_merge")
        record["execution"]["source_control"]["tested_merge_sha"] = "e" * 40
        result = self.run_cli(record)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("source-control provenance", result.stdout)
        self.assertNotIn("PASS", result.stdout)

    def test_default_cli_rejects_v101_manifest_without_source_control(self):
        record = minimal_manifest(version="1.0.1")
        record["execution"].pop("source_control")
        result = self.run_cli(record)
        self.assertNotEqual(result.returncode, 0)

    def test_explicit_v100_schema_still_accepts_legacy_records(self):
        result = self.run_cli(
            minimal_manifest(version="1.0.0"),
            SCHEMA_DIR / "research-result-record-v1.0.0.schema.json",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
