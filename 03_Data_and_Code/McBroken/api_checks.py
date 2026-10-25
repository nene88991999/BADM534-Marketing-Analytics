"""Preserve unknown API values instead of inventing a working machine or check time."""
import re

import pandas as pd


def status(value):
    if value is True:
        return 1
    if value is False:
        return 0
    if value is None:
        return pd.NA
    raise ValueError(f"Expected a JSON boolean or null, received {value!r}")


def check_time(snapshot_utc, text):
    match = re.fullmatch(r"Checked (\d+) minutes? ago", text or "")
    if match is None:
        return pd.NaT
    return pd.Timestamp(snapshot_utc) - pd.Timedelta(minutes=int(match.group(1)))


if __name__ == "__main__":
    # Constructed edge cases for an AI-generated parser, not observed store data.
    values = pd.Series([status(v) for v in [True, False, None]], dtype="Int64")
    assert values.iloc[0] == 1 and values.iloc[1] == 0 and pd.isna(values.iloc[2])
    assert pd.isna(check_time("2026-10-24T18:00:00Z", None))
    try:
        status("false")
    except ValueError:
        print("A string status requires schema review; an unknown status remains missing.")
    else:
        raise AssertionError("String status was silently accepted")
