"""Refresh the browser's reference cases and visible complete Python source."""
import html
import importlib.util
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / "03_Data_and_Code/Learning_Design/bill_identity.py"
spec = importlib.util.spec_from_file_location("bill_identity", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
cases = module.comparisons()
(HERE / "reference_data.js").write_text(
    "/* Generated from the existing synthetic bill table. */\nwindow.BILL_REFERENCE = "
    + json.dumps(cases, indent=2) + ";\n")
page = HERE / "index.html"
page.write_text(re.sub(r'<code id="python-source">.*?</code>',
                      lambda _: '<code id="python-source">' + html.escape(SOURCE.read_text()) + '</code>',
                      page.read_text(), flags=re.S))
print("Refreshed three reference cases and the complete Python listing.")
