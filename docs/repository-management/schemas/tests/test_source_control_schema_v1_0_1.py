from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from rcrps_v1_0_1_fixtures import (
    minimal_manifest,
    minimal_result_summary,
    minimal_validation_report,
    source_control,
)

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "research-result-record-v1.0.1.schema.json"


class SourceControlSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with SCHEMA_PATH.open("r", encoding="utf-8") as stream:
            cls.schema = json.load(stream)
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema, format_checker=FormatChecker())

    def errors(self, record: dict):
        return list(self.validator.iter_errors(record))

    def test_schema_is_valid_draft_2020_12(self):
        Draft202012Validator.check_schema(self.schema)

    def test_v100_run_manifest_is_accepted(self):
        self.assertEqual(self.errors(minimal_manifest("1.0.0")), [])

    def test_v100_result_summary_is_accepted(self):
        self.assertEqual(self.errors(minimal_result_summary("1.0.0")), [])

    def test_v100_validation_report_is_accepted(self):
        self.assertEqual(self.errors(minimal_validation_report("1.0.0")), [])

    def test_v100_run_manifest_rejects_v101_source_control_extension(self):
        record = minimal_manifest("1.0.0")
        record["execution"]["source_control"] = source_control()
        self.assertTrue(self.errors(record))

    def test_checkout_ref_must_be_fully_qualified(self):
        record = minimal_manifest()
        record["execution"]["source_control"]["checkout_ref"] = "main"
        self.assertTrue(self.errors(record))

    def test_checkout_ref_cannot_be_empty(self):
        record = minimal_manifest()
        record["execution"]["source_control"]["checkout_ref"] = ""
        self.assertTrue(self.errors(record))

    def test_v101_run_manifest_requires_source_control(self):
        record = minimal_manifest()
        record["execution"].pop("source_control")
        self.assertTrue(self.errors(record))

    def test_source_control_requires_all_fourteen_fields(self):
        record = minimal_manifest()
        for field in source_control():
            broken = json.loads(json.dumps(record))
            broken["execution"]["source_control"].pop(field)
            self.assertTrue(self.errors(broken), field)

    def test_pr_event_requires_non_null_pr_metadata(self):
        record = minimal_manifest(event="pull_request", mode="pull_request_merge")
        for field in ("pr_number", "pr_url", "pr_head_sha", "base_sha", "head_ref", "base_ref"):
            broken = json.loads(json.dumps(record))
            broken["execution"]["source_control"][field] = None
            self.assertTrue(self.errors(broken), field)

    def test_non_pr_requires_explicit_null_pr_fields(self):
        record = minimal_manifest()
        for field in ("pr_number", "pr_url", "pr_head_sha", "base_sha", "tested_merge_sha", "head_ref", "base_ref"):
            broken = json.loads(json.dumps(record))
            broken["execution"]["source_control"].pop(field)
            self.assertTrue(self.errors(broken), field)

    def test_pr_and_non_pr_checkout_mode_sets_are_enforced(self):
        pr_record = minimal_manifest(event="pull_request", mode="pull_request_merge")
        pr_record["execution"]["source_control"]["checkout_mode"] = "branch_commit"
        self.assertTrue(self.errors(pr_record))
        non_pr_record = minimal_manifest()
        non_pr_record["execution"]["source_control"]["checkout_mode"] = "pull_request_merge"
        self.assertTrue(self.errors(non_pr_record))

    def test_invalid_pr_sha_url_number_and_empty_refs_are_rejected(self):
        mutations = (
            ("pr_head_sha", "not-a-sha"),
            ("base_sha", "not-a-sha"),
            ("pr_url", "not-a-uri"),
            ("pr_number", 0),
            ("head_ref", ""),
            ("base_ref", ""),
        )
        for field, value in mutations:
            with self.subTest(field=field):
                record = minimal_manifest(event="pull_request", mode="pull_request_merge")
                record["execution"]["source_control"][field] = value
                self.assertTrue(self.errors(record), field)

    def test_workflow_run_id_and_attempt_must_be_paired(self):
        record = minimal_manifest()
        record["execution"]["source_control"]["workflow_run_id"] = 123
        self.assertTrue(self.errors(record))
        record = minimal_manifest()
        record["execution"]["source_control"]["workflow_run_attempt"] = 1
        self.assertTrue(self.errors(record))

    def test_pr_base_and_unknown_checkout_modes_are_schema_valid(self):
        base_record = minimal_manifest(event="pull_request_target", mode="pull_request_base")
        self.assertEqual(self.errors(base_record), [])
        unknown_record = minimal_manifest(event="pull_request", mode="unknown")
        self.assertEqual(self.errors(unknown_record), [])

    def test_working_tree_state_and_dirty_paths_schema(self):
        record = minimal_manifest()
        record["execution"]["source_control"]["working_tree_state"] = "dirty"
        record["execution"]["source_control"]["dirty_paths"] = ["src/model.py"]
        self.assertEqual(self.errors(record), [])
        record["execution"]["source_control"]["dirty_paths"] = ["src/model.py", "src/model.py"]
        self.assertTrue(self.errors(record))


if __name__ == "__main__":
    unittest.main()
