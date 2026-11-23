from pathlib import Path
import hashlib

root = Path(__file__).resolve().parents[1]
work = root / "work"
candidate = work / "v57_reconstructed_1007.md"

structure_path = work / "structure_v57.py"
structure = structure_path.read_text(encoding="utf-8")
old_target = "target=ROOT/'审稿意见-gpt'/'审稿意见分析v5.7-物理校核与专题连续阅读版.md'"
new_target = "target=ROOT/'work'/'v57_reconstructed_1007.md'"
assert structure.count(old_target) == 1
structure = structure.replace(old_target, new_target)
exec(compile(structure, str(structure_path), "exec"), {"__file__": str(structure_path), "__name__": "__main__"})

polish_path = work / "polish_v57.py"
polish = polish_path.read_text(encoding="utf-8")
old_input = "p=next((ROOT/'审稿意见-gpt').glob('审稿意见分析v5.7*.md'))"
new_input = "p=ROOT/'work'/'v57_reconstructed_1007.md'"
assert polish.count(old_input) == 1
polish = polish.replace(old_input, new_input)
exec(compile(polish, str(polish_path), "exec"), {"__file__": str(polish_path), "__name__": "__main__"})

raw = candidate.read_bytes()
print({"candidate": str(candidate), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
