"""Run from any working directory after downloading and verifying the data."""

from pathlib import Path
import platform
import subprocess
import sys
from importlib.metadata import version
from common import save_result

root = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(root.parent / "download_data.py")], check=True)
scripts = ["common.py", "audit.py", "nutrition.py", "test_logic.py"] + [
    f"m{module:02}.py" for module in range(1, 9)
]
for script in scripts:
    subprocess.run([sys.executable, str(root / script)], check=True, cwd=root)
packages = ["numpy", "pandas", "pyarrow", "scipy", "scikit-learn", "statsmodels"]
save_result(
    "environment",
    {
        "python": platform.python_version(),
        "packages": {name: version(name) for name in packages},
    },
)
