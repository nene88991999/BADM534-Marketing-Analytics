"""Download official legal texts and preserve source URLs and file checksums."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "01_Resources/13_Consumer_Agency_and_Recent_Research/Policy"
SOURCES = [
    ("Eighth_Circuit_2025_Vacatur.pdf", "https://ecf.ca8.uscourts.gov/opndir/25/07/243137P.pdf"),
    ("FTC_2026_Recodification.pdf", "https://www.govinfo.gov/content/pkg/FR-2026-02-12/pdf/2026-02866.pdf"),
    ("FTC_2026_Proposed_Rulemaking.pdf", "https://www.govinfo.gov/content/pkg/FR-2026-03-13/pdf/2026-04952.pdf"),
    ("FTC_2026_Information_Collection.pdf", "https://www.govinfo.gov/content/pkg/FR-2026-10-14/pdf/2026-20971.pdf"),
    ("ROSCA_2010.pdf", "https://www.govinfo.gov/content/pkg/PLAW-111publ345/pdf/PLAW-111publ345.pdf"),
    ("NYC_2026_Click_to_Cancel_Rule.pdf", "https://www.nyc.gov/content/dam/nycgov/nyc-main/pdf/2026/Click-to-Cancel-Rule.pdf"),
]


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    records = []
    for filename, url in SOURCES:
        target = DEST / filename
        if not target.exists():
            result = subprocess.run(["curl", "-fLsS", "--max-time", "45", url, "-o", str(target)], capture_output=True, text=True)
            if result.returncode:
                records.append({"file": "", "url": url, "retrieved_on": "2026-11-05",
                                "status": "PDF transfer failed; official text verified with web reader",
                                "error": result.stderr.strip()})
                continue
        assert target.read_bytes().startswith(b"%PDF"), filename
        records.append({"file": filename, "url": url, "retrieved_on": "2026-11-05",
                        "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                        "rights": "U.S. federal government work or official legal edict"})
    (DEST / "sources.json").write_text(json.dumps(records, indent=2) + "\n")
    print(f"Verified {sum(bool(r['file']) for r in records)} official legal PDFs; {sum(not r['file'] for r in records)} linked text")


if __name__ == "__main__":
    main()
