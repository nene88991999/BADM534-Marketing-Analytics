"""Reconcile the journal census, full-text availability, and review denominators."""
from pathlib import Path
import json
import pandas as pd

HERE = Path(__file__).resolve().parent
LIBRARY = HERE.parents[1] / "01_Resources/13_Consumer_Agency_and_Recent_Research"


def main():
    data = pd.DataFrame(json.loads((LIBRARY / "catalog.json").read_text())["resources"])
    assert data.doi.is_unique and data.id.is_unique
    eligible = data.research_screen_eligible.eq(True)
    downloaded = data.download_status.eq("downloaded")
    reviewed = data.review_status.ne("not_reviewed")
    assert not (downloaded & ~eligible).any()
    assert not (downloaded & ~reviewed).any()
    table = data.assign(eligible=eligible.astype(int), downloaded=downloaded.astype(int),
                        reviewed=reviewed.astype(int)).groupby("journal").agg(
        doi_records=("doi", "size"), eligible=("eligible", "sum"),
        downloaded=("downloaded", "sum"), reviewed=("reviewed", "sum"))
    table["access_gaps"] = table.eligible - table.downloaded
    table["download_share_of_eligible"] = table.downloaded / table.eligible
    assert table.doi_records.sum() == len(data)
    assert table.access_gaps.sum() == sum(eligible & ~downloaded)
    # Worst-case bounds use the same eligible-record denominator at both ends.
    # They concern the eventual coding label, not the prevalence of actual harm.
    feature = "social_cues"
    known_positive = int(pd.to_numeric(data.loc[eligible & reviewed, feature]).sum())
    unknown = int(sum(eligible & ~reviewed))
    denominator = int(eligible.sum())
    bounds = {"feature": feature, "eligible": denominator, "reviewed_positive": known_positive,
              "unreviewed": unknown, "lower_bound": known_positive / denominator,
              "upper_bound": (known_positive + unknown) / denominator}
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    table.to_csv(output / "coverage_by_journal.csv")
    (output / "missing_evidence_bounds.json").write_text(json.dumps(bounds, indent=2) + "\n")
    print(table.to_string())
    print(json.dumps(bounds, indent=2))


if __name__ == "__main__":
    main()
