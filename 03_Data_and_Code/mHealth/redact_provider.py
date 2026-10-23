"""Standardize provider labels using a separately held regular-expression file."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import re


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--pattern-file", type=Path, required=True)
    args = parser.parse_args()
    pattern = re.compile(args.pattern_file.read_text().strip().encode("ascii"), re.I)
    manifest_path = args.directory / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    replacements = dict(manifest.get("provider_label_standardization", {}).get("occurrences_replaced", {}))
    for name, metadata in manifest["files"].items():
        source = args.directory / name
        assert digest(source) == metadata["sha256"]
        temporary = source.with_name(source.name + ".part")
        count = 0
        with gzip.open(source, "rb") as reader, temporary.open("wb") as output:
            with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0, compresslevel=6) as writer:
                for line in reader:
                    transformed, changes = pattern.subn(b"mHealth", line)
                    count += changes
                    writer.write(transformed)
        if count:
            temporary.replace(source)
            metadata["sha256"] = digest(source)
            metadata["compressed_bytes"] = source.stat().st_size
        else:
            temporary.unlink()
        replacements[name] = replacements.get(name, 0) + count
    manifest["provider_label_standardization"] = {"replacement": "mHealth", "occurrences_replaced": replacements, "private_pattern_published": False}
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(replacements))


if __name__ == "__main__":
    main()
