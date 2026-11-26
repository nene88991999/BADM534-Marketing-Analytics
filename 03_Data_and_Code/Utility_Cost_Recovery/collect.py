"""Retrieve a fixed public-source list; retain documents locally and export counts."""
import argparse
import hashlib
import io
import json
import re
import time
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
PATTERNS = {
    "investment": r"\b(invest\w*|infrastructure|construction|capital|generation)\b",
    "recovery": r"\b(recover\w*|rate base|revenue requirement|tracker\w*|rider\w*)\b",
    "household": r"\b(residential|household\w*)\b",
    "bill": r"\b(bill\w*|rate\w*|charge\w*)\b",
    "large_load": r"\b(data cent(?:er|re)s?|large load\w*|hyperscaler\w*)\b",
    "protection": r"\b(protect\w*|minimum bill\w*|take.or.pay|collateral|offset\w*)\b",
}


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {"head", "script", "style", "noscript"}:
            self.hidden += 1
        if tag in {"p", "div", "br", "tr", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"head", "script", "style", "noscript"}:
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, text):
        if not self.hidden:
            self.parts.append(text)


def extract(raw, spec):
    if spec["format"] == "pdf":
        if not raw.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        from pypdf import PdfReader
        pages = [p.extract_text() or "" for p in PdfReader(io.BytesIO(raw)).pages]
        # Remove exact repeated page furniture. Keep page numbers as locators.
        repeated = Counter(line.strip() for p in pages for line in set(p.splitlines()))
        pages = ["\n".join(x for x in p.splitlines()
                  if repeated[x.strip()] < 3 and not x.strip().isdigit()) for p in pages]
    else:
        parser = VisibleText()
        parser.feed(raw.decode("utf-8", errors="replace"))
        text = " ".join("".join(parser.parts).split())
        start = text.index(spec["start_marker"])
        stop = text.index(spec["end_marker"], start) if spec.get("end_marker") else len(text)
        pages = [text[start:stop]]
    pages = [" ".join(p.split()) for p in pages]
    combined = " ".join(pages)
    if any(marker.lower() not in combined.lower() for marker in spec["identity_markers"]):
        raise ValueError("Document identity or expected content did not match")
    if len(combined) < 400:
        raise ValueError("Empty or truncated document")
    return pages


def retrieve(spec, cache, download):
    path = cache / (spec["id"] + "." + spec["format"])
    receipt = cache / (spec["id"] + ".receipt.json")
    if path.exists() and receipt.exists():
        raw = path.read_bytes()
        record = json.loads(receipt.read_text())
        if hashlib.sha256(raw).hexdigest() != record["sha256"]:
            raise ValueError("Cached source checksum differs")
        return raw, record
    if not download:
        raise FileNotFoundError("No local source; use --download for the fixed URL list")
    request = Request(spec["url"], headers={"User-Agent": "MarketingAnalyticsCourse/1.0 (educational source review)"})
    time.sleep(2)  # Sequential requests, no authentication or access-control bypass.
    with urlopen(request, timeout=40) as response:
        raw = response.read(15_000_001)
        if len(raw) > 15_000_000:
            raise ValueError("Document exceeds 15 MB limit")
        record = {"source_id": spec["id"], "url": spec["url"],
                  "final_url": response.geturl(), "http_status": response.status,
                  "retrieved_at": datetime.now(timezone.utc).isoformat(),
                  "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
    extract(raw, spec)  # Never cache an error page as a successful document.
    path.write_bytes(raw)
    receipt.write_text(json.dumps(record, indent=2) + "\n")
    return raw, record


def features(pages):
    text = " ".join(pages)
    values = {key: len(re.findall(pattern, text, re.I)) for key, pattern in PATTERNS.items()}
    values["words"] = len(re.findall(r"\b[\w'-]+\b", text))
    return values


def candidates(pages):
    found = []
    for page, text in enumerate(pages, 1):
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text)
        for i, sentence in enumerate(sentences):
            context = " ".join(sentences[max(0, i - 1):i + 2])
            tags = [k for k, p in PATTERNS.items() if re.search(p, context, re.I)]
            if "bill" in tags and ("recovery" in tags or "investment" in tags):
                found.append({"page": page, "sentence": i + 1, "tags": tags,
                              "context": context})
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--output", type=Path, default=HERE / ".cache/retrieval.json")
    args = parser.parse_args()
    cache = HERE / ".cache"
    cache.mkdir(exist_ok=True)
    records = []
    for spec in json.loads((HERE / "sources.json").read_text()):
        try:
            raw, receipt = retrieve(spec, cache, args.download)
            pages = extract(raw, spec)
            matches = candidates(pages)
            (cache / (spec["id"] + ".review.json")).write_text(json.dumps(matches, indent=2) + "\n")
            (cache / (spec["id"] + ".pages.json")).write_text(json.dumps(pages, indent=2) + "\n")
            records.append({**receipt, "status": "ok", "pages": len(pages),
                            "candidate_windows": len(matches), **features(pages)})
        except (HTTPError, OSError, ValueError) as error:
            records.append({"source_id": spec["id"], "url": spec["url"],
                            "status": "unavailable", "reason": str(error)})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, indent=2) + "\n")
    print(json.dumps({r["source_id"]: r["status"] for r in records}, indent=2))


if __name__ == "__main__":
    main()
