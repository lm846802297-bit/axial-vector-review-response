"""Validate the 2026-10-20 relocation without rerunning physics calculations."""
from pathlib import Path
import hashlib
import json
import re

here = Path(__file__).resolve().parent
base = here.parent
workspace = base.parent
manifest_path = here / "relocation_manifest_20261020.json"
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))

# Only these two evidence files intentionally change for the new link locations.
audit = base / "审计结果" / "DeepSeek66"
report = audit / "DeepSeek第66版独立审计-20261020.md"
evidence = audit / "audit_evidence.json"
intentional = {report.resolve(), evidence.resolve()}
unchanged = 0
for item in manifest["files"]:
    target = Path(item["new_path"])
    assert target.is_file(), target
    assert not Path(item["old_path"]).exists(), item["old_path"]
    actual = sha(target)
    if target.resolve() not in intentional:
        assert actual == item["sha256_before"], target
        unchanged += 1
    item["sha256_after"] = actual
    item["bytes_unchanged"] = actual == item["sha256_before"]

for item in manifest["main_documents"]:
    actual = sha(Path(item["path"]))
    assert actual == item["sha256_before"], item["path"]
    item["sha256_after"] = actual
    item["bytes_unchanged"] = True

data = json.loads(evidence.read_text(encoding="utf-8-sig"))
assert data["review_report_sha256"] == sha(report)
assert data["independent_script_sha256"] == sha(audit / "independent_review.wl")
assert data["independent_log_sha256"] == sha(audit / "independent_review_checks.txt")

link_count = 0
external_links = []
for doc in [base / "README.md", report]:
    content = doc.read_text(encoding="utf-8-sig")
    targets = []
    for match in re.finditer(r"\]\(", content):
        start = match.end()
        depth = 1
        end = start
        while depth and end < len(content):
            if content[end] == "(":
                depth += 1
            elif content[end] == ")":
                depth -= 1
            end += 1
        assert depth == 0, (doc, start)
        targets.append(content[start:end - 1])
    for target in targets:
        if target.startswith(("https://", "http://")):
            continue
        path = Path(re.sub(r":\d+$", "", target))
        if not path.is_absolute():
            path = doc.parent / path
        if not path.resolve().is_relative_to(workspace.resolve()):
            external_links.append({"target": target, "exists": path.exists()})
            continue
        assert path.exists(), (doc, target)
        link_count += 1

assert not (workspace / "计算输出").exists()
assert not (workspace / "审计结果").exists()
manifest["verification"] = {
    "moved_files": len(manifest["files"]),
    "unmodified_evidence_files": unchanged,
    "intentional_path_metadata_edits": 2,
    "unchanged_main_documents": len(manifest["main_documents"]),
    "local_links_checked": link_count,
    "external_reference_links": external_links,
    "physics_calculations_rerun": False,
}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(manifest["verification"], ensure_ascii=False, indent=2))
