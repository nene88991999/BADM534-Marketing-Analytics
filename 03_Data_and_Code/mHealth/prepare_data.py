"""Prepare the course copy from separately held source CSVs.

Requires pandas and numpy. The private random key must remain outside Git.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import gzip
import hashlib
import hmac
import io
import json
from pathlib import Path
import secrets

import numpy as np
import pandas as pd

WEIGHTS = ["Currentweight", "Startweight", "Minweight", "Maxweight", "Goalweight"]
REMOVE = {"Birthday", "Image", "Currenteer", "Age", "Bmi"}
AGE_REFERENCE = pd.Timestamp("2016-01-01")


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


class Transformer:
    def __init__(self, key):
        self.key = key
        self.ages = {}
        self.users = set()
        self.max_weight_change = 0.0
        self.weight_values_changed = Counter()
        self.weight_values_positive = Counter()
        self.weight_values_below_two = Counter()

    def digest(self, purpose, *values):
        message = json.dumps([purpose, *values], separators=(",", ":")).encode()
        return hmac.new(self.key, message, hashlib.sha256).digest()

    @lru_cache(maxsize=100000)
    def user_id(self, uid):
        return "L" + self.digest("course-user-v1", uid).hex()[:24]

    @lru_cache(maxsize=100000)
    def user_offset(self, uid):
        return int.from_bytes(self.digest("user-weight-offset-v1", uid)[:8], "big") / 2**64 - 0.5

    @lru_cache(maxsize=200000)
    def day_offset(self, uid, date):
        jitter = int.from_bytes(self.digest("day-weight-offset-v1", uid, date)[:8], "big") / 2**64 - 0.5
        return self.user_offset(uid) + jitter

    def transform(self, raw, food):
        uid = raw.Userid.astype(str)
        date = raw.Fancydate.astype(str)
        self.users.update(uid.unique())
        if food:
            birth = pd.to_datetime(raw.Birthday, errors="coerce")
            age = AGE_REFERENCE.year - birth.dt.year - ((birth.dt.month > 1) | ((birth.dt.month == 1) & (birth.dt.day > 1))).astype(int)
            age = age.where(age.between(0, 120)).astype("Int64")
            pairs = pd.DataFrame({"uid": uid, "age": age}).drop_duplicates()
            for ident, years in pairs.itertuples(index=False, name=None):
                value = None if pd.isna(years) else int(years)
                if ident in self.ages and self.ages[ident] != value:
                    raise ValueError("Inconsistent fixed age within a source user; review privately.")
                self.ages[ident] = value
        result = raw.drop(columns=list(REMOVE & set(raw.columns))).copy()
        result["Userid"] = uid.map(self.user_id)
        result["Age_at_2016_01_01"] = uid.map(self.ages).astype("Int64")
        offset = np.fromiter((self.day_offset(u, d) for u, d in zip(uid, date)), float, count=len(raw))
        for column in WEIGHTS:
            if column not in result:
                continue
            original = pd.to_numeric(raw[column], errors="raise")
            positive = original > 0
            changed = original.copy()
            regular = original >= 2
            small = positive & ~regular
            changed.loc[regular] = (original[regular] + offset[regular]).round(3)
            changed.loc[small] = original[small] * (1 + offset[small] / 2)
            self.weight_values_below_two[column] += int(small.sum())
            if (changed[positive] <= 0).any():
                raise ValueError("Weight perturbation produced a nonpositive weight.")
            result[column] = changed
            error = (changed[positive] - original[positive]).abs()
            self.max_weight_change = max(self.max_weight_change, float(error.max()) if len(error) else 0)
            self.weight_values_positive[column] += int(positive.sum())
            self.weight_values_changed[column] += int((error > 0).sum())
        if food:
            height = pd.to_numeric(result.Heightinches, errors="raise")
            valid = (height > 0) & (result.Currentweight > 0)
            result["Bmi_from_noisy_weight"] = (703 * result.Currentweight / height**2).where(valid).round(3)
        if any(column in result for column in ["Birthday", "Image", "Currenteer", "Bmi", "Age"]):
            raise AssertionError("An excluded source field survived transformation.")
        if not result.Userid.str.fullmatch(r"L[0-9a-f]{24}").all():
            raise AssertionError("Invalid replacement ID.")
        return result


def process(source, output, transformer, food, limit=None):
    counts = {"rows": 0, "users": set(), "date_min": None, "date_max": None}
    original_digest = hashlib.sha256()
    # Hashing reader avoids another cloud read while retaining source provenance.
    class Reader(io.RawIOBase):
        def __init__(self, stream):
            self.stream = stream
        def readable(self):
            return True
        def readinto(self, buffer):
            data = self.stream.read(len(buffer))
            original_digest.update(data)
            buffer[:len(data)] = data
            return len(data)
    with source.open("rb") as source_handle, output.open("wb") as destination:
        reader = io.BufferedReader(Reader(source_handle), buffer_size=1024 * 1024)
        with gzip.GzipFile(filename="", mode="wb", fileobj=destination, compresslevel=6, mtime=0) as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8", newline="") as text:
                for raw in pd.read_csv(reader, chunksize=100000, nrows=limit, dtype={"Userid": str}, low_memory=False):
                    transformed = transformer.transform(raw, food)
                    transformed.to_csv(text, index=False, header=counts["rows"] == 0, lineterminator="\n")
                    counts["rows"] += len(raw)
                    counts["users"].update(transformed.Userid.unique())
                    low, high = raw.Fancydate.min(), raw.Fancydate.max()
                    counts["date_min"] = low if counts["date_min"] is None else min(low, counts["date_min"])
                    counts["date_max"] = high if counts["date_max"] is None else max(high, counts["date_max"])
                    counts["columns"] = transformed.columns.tolist()
                    if counts["rows"] % 500000 == 0:
                        print(f'{source.name}: {counts["rows"]:,} rows processed', flush=True)
    counts["users"] = len(counts["users"])
    counts["compressed_bytes"] = output.stat().st_size
    counts["sha256"] = sha256(output)
    counts["source_sha256"] = original_digest.hexdigest() if limit is None else None
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--private-key", type=Path, required=True)
    parser.add_argument("--limit", type=int, help="Development inspection only; never a complete release.")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    args.private_key.parent.mkdir(parents=True, exist_ok=True)
    if not args.private_key.exists():
        args.private_key.write_bytes(secrets.token_bytes(32))
        args.private_key.chmod(0o600)
    key = args.private_key.read_bytes()
    if len(key) != 32:
        raise ValueError("The private key must contain 32 random bytes.")
    transformer = Transformer(key)
    manifest = {"version": "2026-10-23", "complete_sources": args.limit is None, "age_reference": "2016-01-01", "weight_unit": "pound, inferred from source BMI/height relationship", "weight_noise": {"user_offset": "Uniform(-0.5, 0.5)", "day_offset": "Uniform(-0.5, 0.5)", "same_offset_across_weight_fields_and_files": True, "rounding_decimals": 3, "private_key_published": False}, "files": {}}
    for stem, food in [("data_final_25", True), ("data_everyday", False)]:
        target = "food_entries.csv.gz" if food else "daily_records.csv.gz"
        manifest["files"][target] = process(args.source / f"{stem}.csv", args.output / target, transformer, food, args.limit)
        print(f'Completed {target}', flush=True)
    manifest["weight_noise"]["small_positive_weights"] = "For 0 < w < 2, use w * (1 + offset/2) without rounding, preserving positivity."
    manifest["validation"] = {"maximum_absolute_weight_change": transformer.max_weight_change, "positive_weight_values": dict(transformer.weight_values_positive), "changed_weight_values": dict(transformer.weight_values_changed), "positive_weight_values_below_two": dict(transformer.weight_values_below_two), "private_user_key_count": len(transformer.users), "missing_fixed_age_users": sum(v is None for v in transformer.ages.values())}
    assert transformer.max_weight_change <= 1.000500001
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"complete_sources": manifest["complete_sources"], "files": {n: {k: v for k, v in f.items() if k in ["rows", "users", "compressed_bytes"]} for n, f in manifest["files"].items()}}, indent=2), flush=True)


if __name__ == "__main__":
    main()
