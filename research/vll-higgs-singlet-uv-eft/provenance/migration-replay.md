# Migration checks

- PR #9: 10 exact C5 soft-bubble trace/sign/pole checks passed (SFT-01 only).
- PR #14: 3 endpoint-ordering tests passed (LD-W-03/04 subset).
- Main LD-W-06: the targeted five-test shifted-Yukawa suite gave three passes and two `IndexError: list index out of range` in the current runtime, both in the pristine upstream pin and in the staged migration. The exception is raised when arithmetic indexes the symbolic vector. This baseline copy preserves upstream source and does not attempt to repair that behavior or reclassify upstream claims.
- Inactive workflow templates are historical source evidence; they were renamed with a .txt suffix and placed outside the target's active workflow directory.
- Separately recorded original and migrated hashes distinguish exact source from narrow private-locator sanitation. This is a migration check, not a new physics result.
