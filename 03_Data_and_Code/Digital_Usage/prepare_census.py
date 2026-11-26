"""Extract archived Census ZCTA tables from downloaded official source files.

Usage: python prepare_census.py --source-dir PATH
Download URLs and SHA256 hashes are in manifest.json. No network calls occur.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
FIELDS = {"b19013": [1], "b15003": [1, 22, 23, 24, 25],
          "b28002": [1, 4]}


def prepare(source):
    rows, sources = {}, []
    for table, numbers in FIELDS.items():
        path = source / f"{table}.dat"
        fields = [f"{table.upper()}_{kind}{n:03d}"
                  for n in numbers for kind in ["E", "M"]]
        seen = set()
        with path.open() as stream:
            for row in csv.DictReader(stream, delimiter="|"):
                geo = row["GEO_ID"]
                if not geo.startswith("860Z200US"):
                    continue
                code = geo[-5:]
                if code in seen:
                    raise ValueError(f"Duplicate ZCTA in {table}: {code}")
                seen.add(code)
                rows.setdefault(code, {"zcta": code}).update(
                    {field: row[field] for field in fields})
        sources.append({"file": path.name, "zctas": len(seen),
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    columns = ["zcta"] + [f"{t.upper()}_{k}{n:03d}" for t, ns in
                         FIELDS.items() for n in ns for k in ["E", "M"]]
    with (ROOT / "data/acs2021_zcta.csv").open("w", newline="") as out:
        writer = csv.DictWriter(out, columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows[c] for c in sorted(rows))
    path = source / "gazetteer2021.zip"
    with zipfile.ZipFile(path) as archive:
        raw = archive.read("2021_Gaz_zcta_national.txt").decode()
    reader = csv.DictReader(io.StringIO(raw), delimiter="\t")
    reader.fieldnames = [x.strip() for x in reader.fieldnames]
    with (ROOT / "data/zcta_coordinates.csv").open("w", newline="") as out:
        writer = csv.writer(out, lineterminator="\n")
        writer.writerow(["zcta", "latitude", "longitude"])
        for row in reader:
            writer.writerow([row["GEOID"], row["INTPTLAT"].strip(),
                             row["INTPTLONG"].strip()])
    sources.append({"file": path.name,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    (ROOT / "results/census_extraction.json").write_text(
        json.dumps(sources, indent=2) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    prepare(parser.parse_args().source_dir)
