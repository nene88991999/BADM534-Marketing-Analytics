"""Verify released files without printing participant records."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=Path(__file__).parent / "data")
    parser.add_argument("--manifest", type=Path, default=Path(__file__).parent / "manifest.json")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    if not manifest["complete_sources"]:
        raise AssertionError("Incomplete export.")
    forbidden = {"Birthday", "Image", "Currenteer", "Bmi", "Age"}
    daily = pd.read_csv(args.directory / "daily_records.csv.gz", dtype={"Userid": str})
    keys = ["Userid", "Fancydate"]
    assert not daily.duplicated(keys).any()
    daily = daily.set_index(keys)
    counts = {}
    missing_matches = 0
    matched_rows = 0
    currentweight_mismatches = 0
    age_mismatches = 0
    invalid_bmi = 0
    for name, metadata in manifest["files"].items():
        path = args.directory / name
        assert path.stat().st_size == metadata["compressed_bytes"]
        assert sha256(path) == metadata["sha256"]
        rows = 0
        users = set()
        missing_age_rows = 0
        with gzip.open(path, "rt") as stream:
            for chunk in pd.read_csv(stream, chunksize=100000, dtype={"Userid": str}):
                assert not (forbidden & set(chunk.columns))
                assert chunk.columns.tolist() == metadata["columns"]
                assert chunk.Userid.str.fullmatch(r"L[0-9a-f]{24}").all()
                rows += len(chunk)
                users.update(chunk.Userid.unique())
                missing_age_rows += int(chunk.Age_at_2016_01_01.isna().sum())
                if name == "food_entries.csv.gz":
                    lookup = daily.reindex(pd.MultiIndex.from_frame(chunk[keys]))
                    match = lookup.Currentweight.notna().to_numpy()
                    missing_matches += int((~match).sum())
                    matched_rows += int(match.sum())
                    currentweight_mismatches += int((~np.isclose(chunk.Currentweight.to_numpy()[match], lookup.Currentweight.to_numpy()[match], atol=1e-8, rtol=0, equal_nan=True)).sum())
                    age_mismatches += int((~np.isclose(chunk.Age_at_2016_01_01.to_numpy()[match], lookup.Age_at_2016_01_01.to_numpy()[match], atol=0, rtol=0, equal_nan=True)).sum())
                    expected = (703 * chunk.Currentweight / chunk.Heightinches**2).where((chunk.Currentweight > 0) & (chunk.Heightinches > 0)).round(3)
                    invalid_bmi += int((~np.isclose(expected, chunk.Bmi_from_noisy_weight, atol=1e-8, rtol=0, equal_nan=True)).sum())
        assert rows == metadata["rows"]
        assert len(users) == metadata["users"]
        counts[name] = {"rows": rows, "users": len(users), "missing_age_rows": missing_age_rows, "sha256_verified": True, "excluded_columns_absent": True, "id_format_verified": True}
    assert invalid_bmi == 0
    assert age_mismatches == 0
    report = {"files": counts, "daily_key_unique": True, "food_rows_with_daily_match": matched_rows, "food_rows_without_daily_match": missing_matches, "matched_rows_with_different_currentweight": currentweight_mismatches, "matched_rows_with_different_fixed_age": age_mismatches, "incorrect_bmi_rows": invalid_bmi}
    args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
