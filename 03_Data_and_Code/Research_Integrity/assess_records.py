"""Read the public Study 3 artifact; report diagnostics, never a causal effect.

Run: python assess_records.py
Input: the unchanged CC BY 4.0 ResearchBox 336 workbook, described in README.md.
The archived observations contain evidence of fabrication. They are not a
validated record of insurance customers' behavior. No source workbook is edited.
"""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
from statistics import mean

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "data" / "Study3_with_fonts.xlsx"
OUTPUT = ROOT / "results"
OUTPUT.mkdir(exist_ok=True)
digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
expected = json.loads((ROOT / "source.json").read_text())["sha256"]
if digest != expected:
    raise ValueError("Source bytes changed; inspect and document the new version.")

book = load_workbook(SOURCE, read_only=True, data_only=True)
sheet = book["Data"]
cells = sheet.iter_rows()
names = [cell.value for cell in next(cells)]
records = []
for row in cells:
    record = dict(zip(names, (cell.value for cell in row)))
    record["actual_font"] = row[names.index("baseline_car1")].font.name
    records.append(record)
book.close()
if len({r["id"] for r in records}) != len(records):
    raise ValueError("Masked row identifiers are not unique.")
if any(r["font"] != r["actual_font"] for r in records):
    raise ValueError("Recorded font and workbook formatting disagree.")

def observed(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)

def write_csv(name, rows):
    with (OUTPUT / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

# Each row is a policy. Missing car slots stay missing. Differences are miles
# over varying, unknown intervals, so these values are not annual mileages.
for r in records:
    differences = [r[f"update_car{k}"] - r[f"baseline_car{k}"]
                   for k in range(1, 5)
                   if observed(r[f"baseline_car{k}"])
                   and observed(r[f"update_car{k}"])]
    if len(differences) != r["car_count"]:
        raise ValueError("Car count and paired measurements disagree.")
    if abs(mean(differences) - r["diff_average"]) > 1e-7:
        raise ValueError("Stored policy average does not reconcile.")

increments = [r["update_car1"] - r["baseline_car1"] for r in records]
histogram = []
for lower in range(0, 50000, 5000):
    count = sum(lower <= x < lower + 5000 for x in increments)
    histogram.append({"lower_miles": lower, "upper_exclusive_miles": lower + 5000,
                      "count": count, "denominator": len(increments)})
write_csv("car1_increments.csv", histogram)

rounding = []
for font in ("Calibri", "Cambria"):
    for time in ("baseline", "update"):
        # Car 1 avoids overweighting policies with more recorded cars.
        values = [r[f"{time}_car1"] for r in records if r["font"] == font]
        for multiple in (10, 100, 1000):
            count = sum(x % multiple == 0 for x in values)
            rounding.append({"font": font, "time": time, "multiple": multiple,
                             "count": count, "denominator": len(values),
                             "fraction": count / len(values)})
write_csv("rounding.csv", rounding)

# Restrict explicitly to policies with all four baseline car slots observed.
# A candidate pair must be close in every dimension, with directional offsets.
four = [r for r in records
        if all(observed(r[f"baseline_car{k}"]) for k in range(1, 5))]
left = [r for r in four if r["font"] == "Calibri"]
right = [r for r in four if r["font"] == "Cambria"]
matches = []
for a in left:
    candidates = [b for b in right
                  if all(0 <= b[f"baseline_car{k}"] - a[f"baseline_car{k}"] <= 1000
                         for k in range(1, 5))]
    matches.append(len(candidates))

groups = []
for label in ("Sign Top", "Sign Bottom"):
    rows = [r for r in records if r["condition"] == label]
    groups.append({"condition": label, "policies": len(rows),
                   "baseline_average_miles": mean(r["baseline_average"] for r in rows),
                   "increment_average_miles": mean(r["diff_average"] for r in rows)})
write_csv("condition_descriptions.csv", groups)
summary = {
    "source_sha256": digest, "policies": len(records),
    "font_counts": dict(Counter(r["font"] for r in records)),
    "car1_increment_min": min(increments), "car1_increment_max": max(increments),
    "car1_increment_below_zero": sum(x < 0 for x in increments),
    "car1_increment_at_least_50000": sum(x >= 50000 for x in increments),
    "complete_four_car_policies": len(four),
    "complete_four_car_calibri": len(left), "complete_four_car_cambria": len(right),
    "calibri_with_candidate": sum(n > 0 for n in matches),
    "calibri_with_exactly_one_candidate": sum(n == 1 for n in matches),
    "candidate_rule": "All four Cambria minus Calibri offsets in [0,1000] miles",
    "interpretation": "Descriptive properties of an archived, challenged artifact; no estimate of honesty or identification of a fabricator.",
}
(OUTPUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
