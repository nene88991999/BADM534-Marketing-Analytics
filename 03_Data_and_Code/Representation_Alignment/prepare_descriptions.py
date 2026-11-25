"""Build a bounded, description-level sample from the public mHealth release."""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "mHealth/data/food_entries.csv.gz"
EXPECTED = "2ee04b155a93d51a02ee5acb61ff88a0dde2990b4713668c1b824ae6999ffbea"
CAPS = {"train": 6000, "validation": 1500, "test": 1500}


def normalize(text):
    return " ".join(str(text).casefold().split())


def partition(description):
    digest = hashlib.sha256(description.encode()).hexdigest()
    bucket = int(digest[:8], 16) % 10
    return ("train" if bucket < 6 else "validation" if bucket < 8 else "test"), digest


def summarize(counts):
    rows = []
    for description, categories in sorted(counts.items()):
        label = min(categories, key=lambda k: (-categories[k], k))
        split, digest = partition(description)
        rows.append(dict(description=description, category=label, split=split,
                         description_sha256=digest, source_entries=sum(categories.values()),
                         category_count=len(categories), modal_entries=categories[label]))
    return rows


def main():
    if not SOURCE.exists():
        raise FileNotFoundError("Run python3 03_Data_and_Code/mHealth/download_data.py first.")
    with SOURCE.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    if digest != EXPECTED:
        raise ValueError("The mHealth release checksum differs.")
    counts = defaultdict(Counter)
    all_rows = cohort_rows = usable_rows = 0
    columns = ["Userid", "Fancydate", "Name", "Category"]
    for chunk in pd.read_csv(SOURCE, usecols=columns, chunksize=250000,
                             dtype=str, keep_default_na=False):
        all_rows += len(chunk)
        eligible = chunk.Userid.str.slice(1, 5).map(lambda x: int(x, 16)) < 4096
        chunk = chunk.loc[eligible]
        cohort_rows += len(chunk)
        if not chunk.Fancydate.str.startswith("2016-").all():
            raise ValueError("Expected 2016 source dates.")
        description = chunk.Name.map(normalize)
        category = chunk.Category.str.strip()
        usable = description.ne("") & category.ne("") & category.ne("Unclassified")
        usable_rows += int(usable.sum())
        pairs = pd.DataFrame({"description": description[usable], "category": category[usable]})
        for (text, label), n in pairs.groupby(["description", "category"]).size().items():
            counts[text][label] += int(n)
    all_descriptions = summarize(counts)
    selected = []
    for split, cap in CAPS.items():
        candidates = [r for r in all_descriptions if r["split"] == split]
        selected.extend(sorted(candidates, key=lambda r: r["description_sha256"])[0:cap])
    target = HERE / "data/descriptions.csv"
    with target.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(selected[0]))
        writer.writeheader(); writer.writerows(selected)
    manifest = dict(source="mHealth teaching release 2026-10-23", source_sha256=digest,
                    source_rows=all_rows, cohort_rows=cohort_rows, usable_rows=usable_rows,
                    distinct_usable_descriptions=len(all_descriptions),
                    cohort_rule="First four pseudonym hex digits below 4096",
                    reference_label="Modal category among eligible 2016 rows; alphabetical tie break",
                    unit="One normalized description, equal weight", caps=CAPS,
                    split_rule="SHA256 first 8 digits modulo 10: 0-5 train, 6-7 validation, 8-9 test",
                    selection="Lowest full SHA256 within each split; independent of categories",
                    data_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                    split_counts={s: sum(r["split"] == s for r in selected) for s in CAPS},
                    split_ambiguous={s: sum(r["split"] == s and r["category_count"] > 1
                                            for r in selected) for s in CAPS})
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
