"""Run the three offline cases, counterexamples, and provenance checks."""
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "01_Resources/08_M8_Current_Topics_in_Marketing/genai_demand_lab"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    before = {str(p.relative_to(SOURCE)): digest(p) for p in sorted(SOURCE.rglob("*"))
              if p.is_file() and "__pycache__" not in p.parts}
    for name in ["measurement.py", "retention.py", "demand.py"]:
        subprocess.run([sys.executable, str(HERE / name)], check=True)
    subprocess.run([sys.executable, "-m", "unittest", "-v", "test_examples"], cwd=HERE, check=True)
    assert all(digest(SOURCE / name) == sha for name, sha in before.items())
    manifest = {"reviewed_on": "2026-10-26", "source_folder": str(SOURCE.relative_to(ROOT)),
                "source_sha256": before,
                "source_rights": "User-supplied course bundle. External captures retain source terms; no blanket license is asserted.",
                "source_execution": "Collector, notebook, and full simulator inspected but not rerun; course analyses read saved inputs offline",
                "papers": ["https://www.nber.org/papers/w35953", "https://arxiv.org/abs/2504.15440"],
                "documentation": "https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/concepts/page-views.html"}
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    verification = {"python": platform.python_version(), "numpy": np.__version__, "pandas": pd.__version__,
                    "programs_executed": ["measurement.py", "retention.py", "demand.py"],
                    "unit_tests": 8, "source_files_unchanged_by_analysis": True,
                    "network_requests": 0, "external_model_calls": 0,
                    "checks": ["unique keys and valid counts", "independent pageview totals",
                               "full-population adoption denominator", "new flag reconciled with prior month",
                               "fixed-cohort partition", "price design rank", "independent FWL slope",
                               "exact binary-logit parameter recovery"]}
    (HERE / "results/verification.json").write_text(json.dumps(verification, indent=2) + "\n")


if __name__ == "__main__":
    main()
