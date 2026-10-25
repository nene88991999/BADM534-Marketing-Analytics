"""Run the offline teaching examples; source preparation is a separate command."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
for script in ["test_examples.py", "api_checks.py", "coverage.py", "policy.py", "predict.py"]:
    subprocess.run([sys.executable, str(root / script)], cwd=root, check=True)
