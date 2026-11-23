"""Verify the archived relocation and link integrity without rerunning physics calculations."""
from pathlib import Path
import hashlib
import json
import re

here = Path(__file__).resolve().parent
calculation_root = here.parent
workspace = calculation_root.parent
manifest_path = here / "relocation_manifest_20261020.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()

assert manifest["path_convention"]["bundle_root"] == "."
checked = 0
unchanged = 0
for item in manifest["files"]:
    old_rel = Path(item["old_path"])
    new_rel = Path(item["new_path"])
    assert not old_rel.is_absolute() and not re.match(r"^[A-Za-z]:[\\/]", item["old_path"]), item["old_path"]
    assert not new_rel.is_absolute() and not re.match(r"^[A-Za-z]:[\\/]", item["new_path"]), item["new_path"]
    assert "\\" not in item["old_path"] and "\\" not in item["new_path"]
    target = workspace / new_rel
    assert target.is_file(), target
    assert not (workspace / old_rel).exists(), item["old_path"]
    actual = sha(target)
    assert actual == item["sha256_after"], (target, item["sha256_after"], actual)
    assert item["bytes_unchanged"] == (actual == item["sha256_before"]), target
    checked += 1
    unchanged += actual == item["sha256_before"]

verified_main_documents = 0
not_bundled_main_documents = 0
for item in manifest["main_documents"]:
    path = Path(item["path"])
    assert not path.is_absolute() and not re.match(r"^[A-Za-z]:[\\/]", item["path"]), item["path"]
    if not item.get("included_in_bundle", False):
        not_bundled_main_documents += 1
        continue
    target = workspace / path
    assert target.is_file(), target
    actual = sha(target)
    assert actual == item["sha256_after"], (target, item["sha256_after"], actual)
    verified_main_documents += 1

audit = calculation_root / "审计结果" / "DeepSeek66"
report = audit / "DeepSeek第66版独立审计-20261020.md"
evidence = audit / "audit_evidence.json"
data = json.loads(evidence.read_text(encoding="utf-8-sig"))
assert data["review_report_sha256"] == sha(report)
assert data["independent_script_sha256"] == sha(audit / "independent_review.wl")
assert data["independent_log_sha256"] == sha(audit / "independent_review_checks.txt")

link_count = 0
external_links = []
for doc in [calculation_root / "README.md", report]:
    content = doc.read_text(encoding="utf-8-sig")
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
        target_text = content[start:end - 1]
        if target_text.startswith(("https://", "http://")):
            continue
        if re.match(r"^[A-Za-z]:[\\/]", target_text):
            external_links.append({"target": target_text, "status": "historical machine-specific reference; not checked in bundle"})
            continue
        target_path = Path(re.sub(r":\d+$", "", target_text))
        if not target_path.is_absolute():
            target_path = doc.parent / target_path
        if not target_path.resolve().is_relative_to(workspace.resolve()):
            external_links.append({"target": target_text, "status": "external relative reference; not checked in bundle"})
            continue
        assert target_path.exists(), (doc, target_text)
        link_count += 1

assert not (workspace / "计算输出").exists()
assert not (workspace / "审计结果").exists()
summary = {
    "relocation_manifest_entries": checked,
    "sha256_after_values_verified": checked,
    "sha256_mismatches": 0,
    "unchanged_bytes_vs_source": unchanged,
    "changed_bytes_vs_source": checked - unchanged,
    "included_main_documents_verified": verified_main_documents,
    "main_documents_recorded_but_not_bundled": not_bundled_main_documents,
    "local_links_checked": link_count,
    "external_references_not_checked": external_links,
    "physics_calculations_rerun": False,
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
