"""Assess the public digital-usage release and join Census areas by identifier."""
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
RAW_HASH = "23c3c6f719114ba08366fe4fca246c2bdb1e1b49cd7237c3027b1d2c6fd6b96f"


def zip_strings(values):
    values = values.astype("string")
    if not values.str.fullmatch(r"\d{4,5}").fillna(False).all():
        raise ValueError("Expected four- or five-digit postal identifiers")
    return values.str.zfill(5)


def nonnegative(values):
    values = pd.to_numeric(values, errors="coerce")
    return values.where(values >= 0)


def ratio(numerator, denominator):
    result = numerator / denominator.where(denominator > 0)
    return result.where(result.between(0, 1))


def main():
    path = ROOT / "data/published_indices.csv"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == RAW_HASH
    raw = pd.read_csv(path, dtype={"ZIP_CODE": "string"})
    assert list(raw.columns) == ["ZIP_CODE", "STATE",
        "MEDIA AND INFORMATION INDEX", "CONTENT CREATION AND COMPUTATIONAL INDEX"]
    data = raw.rename(columns={"ZIP_CODE": "zip", "STATE": "state",
        "MEDIA AND INFORMATION INDEX": "mci",
        "CONTENT CREATION AND COMPUTATIONAL INDEX": "cci"})
    data["zip"] = zip_strings(data["zip"])
    assert data["zip"].is_unique and len(data) == 28561
    assert data.notna().all().all()
    assert np.isfinite(data[["mci", "cci"]].to_numpy()).all()
    census = pd.read_csv(ROOT / "data/acs2021_zcta.csv", dtype="string")
    assert census["zcta"].is_unique
    for field in census.columns.drop("zcta"):
        census[field] = nonnegative(census[field])
    # Boundary codes denote open-ended median categories, not dollar values.
    census["income_boundary"] = census["B19013_E001"].isin([2499, 250001])
    census["income_10k"] = census["B19013_E001"].where(
        ~census["income_boundary"]) / 10000
    census["college_share"] = ratio(census[
        [f"B15003_E{n:03d}" for n in [22, 23, 24, 25]]].sum(axis=1, min_count=4),
        census["B15003_E001"])
    census["broadband_share"] = ratio(census["B28002_E004"], census["B28002_E001"])
    data = data.merge(census, left_on="zip", right_on="zcta", how="left",
                      validate="one_to_one", indicator="census_match")
    geography = pd.read_csv(ROOT / "data/zcta_coordinates.csv",
                            dtype={"zcta": "string"})
    data = data.merge(geography, left_on="zip", right_on="zcta", how="left",
                      validate="one_to_one", suffixes=("", "_coordinate"))
    assert len(data) == len(raw)
    data["regression_eligible"] = data[
        ["income_10k", "college_share", "broadband_share"]].notna().all(axis=1)
    # Every released ZIP remains in this table, including unmatched records.
    RESULTS.mkdir(exist_ok=True)
    data.to_csv(RESULTS / "joined_areas.csv", index=False, lineterminator="\n")
    il = data.loc[data.state.eq("IL")].copy()
    # Each point is a Census internal point matched by identifier, not a person.
    for index in ["mci", "cci"]:
        il[index + "_z"] = (il[index] - il[index].mean()) / il[index].std(ddof=0)
    il[["zip", "latitude", "longitude", "mci", "cci", "mci_z", "cci_z"]].to_csv(
        RESULTS / "illinois_map.csv", index=False, lineterminator="\n")
    summary = {"released_rows": len(data), "states_and_dc": data.state.nunique(),
        "four_digit_codes_restored": int(raw.ZIP_CODE.str.len().eq(4).sum()),
        "census_matches": int(data.census_match.eq("both").sum()),
        "regression_eligible": int(data.regression_eligible.sum()),
        "income_boundary_codes": int(data.income_boundary.sum()),
        "illinois_rows": len(il), "illinois_mapped": int(il.latitude.notna().sum()),
        "index_correlation_equal_zip_weights": float(data.mci.corr(data.cci)),
        "illinois_regression_eligible": int(il.regression_eligible.sum())}
    data.groupby("state", observed=True).agg(released=("zip", "size"),
        eligible=("regression_eligible", "sum")).to_csv(RESULTS / "state_coverage.csv")
    (RESULTS / "assessment.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
