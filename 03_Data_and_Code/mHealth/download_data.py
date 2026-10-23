"""Download the two release assets and verify their recorded SHA-256 hashes."""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=Path(__file__).parent / "data")
    args = parser.parse_args()
    manifest = json.loads((Path(__file__).parent / "manifest.json").read_text())
    if not manifest["complete_sources"]:
        raise ValueError("The manifest describes an incomplete preparation run.")
    args.directory.mkdir(parents=True, exist_ok=True)
    for name, entry in manifest["files"].items():
        destination = args.directory / name
        if destination.exists():
            if digest(destination) == entry["sha256"]:
                print(f"Verified existing {name}")
                continue
            raise ValueError(f"Existing {name} differs from this release; choose an empty directory.")
        temporary = destination.with_name(destination.name + ".part")
        request = urllib.request.Request(entry["download_url"], headers={"User-Agent": "BADM534-course-data"})
        with urllib.request.urlopen(request, timeout=120) as response, temporary.open("wb") as handle:
            for block in iter(lambda: response.read(1024 * 1024), b""):
                handle.write(block)
        if digest(temporary) != entry["sha256"]:
            temporary.unlink()
            raise ValueError(f"Checksum mismatch for {name}; incomplete download discarded.")
        temporary.replace(destination)
        print(f"Downloaded and verified {name}")


if __name__ == "__main__":
    main()
