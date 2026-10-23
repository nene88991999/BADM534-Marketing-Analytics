"""Verify that Python source blocks in the lecture notes match runnable files."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
pattern = re.compile(r"Python source: \[[^\]]+\]\(([^)]+)\).*?\n```python\n(.*?)\n```", re.S)
checked = 0
for module in sorted((root / "06_Lecture_Notes/modules").glob("M*.md")):
    for relative, code in pattern.findall(module.read_text()):
        source = (module.parent / relative).resolve()
        assert source.is_file(), source
        assert code.strip() == source.read_text().strip(), f"Stale code in {module.name}: {source.name}"
        compile(code, str(source), "exec")
        checked += 1
assert checked >= 20, checked
print(f"Verified {checked} matching, syntactically valid Python source blocks.")
