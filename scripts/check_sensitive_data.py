"""Check tracked notebooks and text without printing credential values."""
import json
import pathlib
import re
import subprocess

root = pathlib.Path(__file__).resolve().parents[1]
paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode("utf-8").split("\0")
errors = []
for name in filter(None, paths):
    path = root / name
    if path.suffix == ".ipynb":
        notebook = json.loads(path.read_text(encoding="utf-8"))
        for index, cell in enumerate(notebook["cells"]):
            if cell.get("outputs") or cell.get("execution_count") is not None:
                errors.append(f"{name}: cell {index} contains saved execution data")
            source = "".join(cell.get("source", []))
            pattern = r"(?i)[\"']cookie[\"']\s*:\s*[\"'][^\"']+"
            if re.search(pattern, source):
                errors.append(f"{name}: cell {index} contains a literal Cookie")
if errors:
    raise SystemExit("\n".join(errors))
print("Tracked notebook credential/output checks passed")
