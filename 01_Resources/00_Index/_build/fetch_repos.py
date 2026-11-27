#!/usr/bin/env python3
"""Download openly licensed GitHub material listed in a download plan (default: 00_Index/_data/downloads.yaml).

Usage (from 00_Index):
    python3 _build/fetch_repos.py [--plan _data/downloads_python_mkt.yaml] [--dry-run] [--only owner/repo,...]
                                  [--start k --count n] [--max-mb 40] [--file-mb 20]

For each plan item it makes a shallow, blob-filtered, sparse clone in a scratch directory outside Dropbox,
keeps only the requested subpaths plus top-level README/LICENSE/requirements files, reads the license from
the repository's own LICENSE file (no GitHub API needed, so no rate limit), and copies the result to
<folder>/repos/<owner>__<repo>/ with a SOURCE.md that records origin, commit and license. Repositories
without a recognisable open license are skipped (catalogue them as link-only). Results are recorded in
00_Index/_data/local_copies.json, which build_catalog.py reads.
"""
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]                       # 01_Resources
sys.path.insert(0, str(HERE))
from build_catalog import FOLDERS  # noqa: E402


def arg(name, default=None, cast=str):
    return cast(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


DRY = "--dry-run" in sys.argv
ONLY = set(arg("--only", "").split(",")) - {""} or None
PLAN = arg("--plan", "_data/downloads.yaml")
LOCAL_MAX_MB = arg("--max-mb", 60, float)
FILE_MAX_MB = arg("--file-mb", 40, float)
SCRATCH = Path.home() / "_badm534_dl"
OPEN = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "Unlicense",
        "GPL-2.0", "GPL-3.0", "LGPL-2.1", "LGPL-3.0", "MPL-2.0", "ISC", "CC-BY-NC-4.0", "CC-BY-NC-SA-4.0",
        "CC-BY-NC-ND-4.0", "AGPL-3.0", "BSL-1.0", "0BSD", "CC-BY-3.0", "CC-BY-SA-3.0"}
ROOT_FILES = ["/README*", "/readme*", "/LICENSE*", "/LICENCE*", "/License*", "/license*", "/COPYING*", "/NOTICE*",
              "/requirements*.txt", "/environment*.yml", "/environment*.yaml"]


def run(cmd, timeout=170):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def detect_license(text):
    t = re.sub(r"\s+", " ", text)
    tl = t.lower()
    head = tl[:700]                      # licence titles sit at the top; bodies cross-reference other licences

    def cc(scope):
        if "cc0" in scope or "public domain dedication" in scope or "creative commons zero" in scope:
            return "CC0-1.0"
        ver = "4.0" if "4.0" in scope else ("3.0" if "3.0" in scope else "4.0")
        nc = "noncommercial" in scope or "non-commercial" in scope
        nd = "noderivatives" in scope or "no derivatives" in scope or "noderivs" in scope
        sa = "sharealike" in scope or "share alike" in scope or "share-alike" in scope
        return "CC-BY" + ("-NC" if nc else "") + ("-ND" if nd else "") + ("-SA" if sa and not nd else "") + "-" + ver

    if "creative commons" in head or "creativecommons.org" in head:
        return cc(head)
    if "gnu affero general public license" in head:
        return "AGPL-3.0"
    if "gnu lesser general public license" in head:
        return "LGPL-3.0" if "version 3" in head else "LGPL-2.1"
    if "gnu general public license" in head:
        return "GPL-3.0" if "version 3" in head else "GPL-2.0"
    if "mozilla public license" in head:
        return "MPL-2.0"
    if "apache license" in head and "2.0" in head:
        return "Apache-2.0"
    if "mit license" in head or "permission is hereby granted, free of charge" in tl:
        return "MIT"
    if "redistribution and use in source and binary forms" in tl:
        return "BSD-3-Clause" if ("neither the name" in tl or "names of its contributors" in tl) else "BSD-2-Clause"
    if "this is free and unencumbered software" in tl:
        return "Unlicense"
    if "permission to use, copy, modify, and/or distribute this software" in tl:
        return "ISC"
    if "apache license" in tl and "version 2.0" in tl:
        return "Apache-2.0"
    if "creative commons" in tl:
        return cc(tl)
    return None


def default_branch(url):
    out = run(["git", "ls-remote", "--symref", url, "HEAD"], timeout=60).stdout
    m = re.search(r"ref: refs/heads/(\S+)\s+HEAD", out)
    return m.group(1) if m else None


def main():
    plan = yaml.safe_load((ROOT / "00_Index" / PLAN).read_text()) if not PLAN.startswith("/") else yaml.safe_load(Path(PLAN).read_text())
    if "--start" in sys.argv:
        s, n = arg("--start", 0, int), arg("--count", 5, int)
        plan = plan[s:s + n]
    out_json = ROOT / "00_Index" / "_data" / "local_copies.json"
    local = json.loads(out_json.read_text()) if out_json.exists() else {}
    SCRATCH.mkdir(exist_ok=True)
    report = []
    for item in plan:
        repo = item["repo"].replace("https://github.com/", "").strip("/")
        if ONLY and repo not in ONLY:
            continue
        if item.get("skip_reason"):
            report.append(f"SKIP {repo}: {item['skip_reason']} (catalogue link only)")
            continue
        owner, name = repo.split("/")[:2]
        dest_rel = f"{FOLDERS[item['dest']][0]}/repos/{item.get('as') or owner + '__' + name}"
        dest = ROOT / dest_rel
        if dest.exists():
            report.append(f"HAVE {repo} -> {dest_rel}")
            for i in item.get("ids", []):
                local[i] = dest_rel
            continue
        url = f"https://github.com/{repo}.git"
        branch = item.get("branch") or default_branch(url)
        if not branch:
            report.append(f"FAIL {repo}: repository not reachable")
            continue
        work = SCRATCH / dest.name
        shutil.rmtree(work, ignore_errors=True)
        paths = item.get("paths") or []
        if item.get("files"):
            work.mkdir(parents=True)
            for fpath in item["files"] + ["LICENSE"]:
                try:
                    with urllib.request.urlopen(f"https://raw.githubusercontent.com/{repo}/{branch}/{fpath}", timeout=60) as r:
                        (work / fpath).parent.mkdir(parents=True, exist_ok=True)
                        (work / fpath).write_bytes(r.read())
                except Exception:  # noqa: BLE001
                    pass
            ls = run(["git", "ls-remote", url, branch]).stdout.split()
            sha = ls[0] if ls else "unknown"
            paths = item["files"]
        else:
            r = run(["git", "clone", "--depth", "1", "--filter=blob:none", "--no-checkout", "--branch", branch, url, str(work)])
            if r.returncode:
                report.append(f"FAIL {repo}: {r.stderr.strip()[-200:]}")
                continue
            patterns = ROOT_FILES + (["/" + p.strip("/") for p in paths] if paths else ["/*"])
            run(["git", "-C", str(work), "sparse-checkout", "set", "--no-cone", *patterns])
            r = run(["git", "-C", str(work), "checkout", branch])
            if r.returncode:
                report.append(f"FAIL {repo} checkout: {r.stderr.strip()[-200:]}")
                shutil.rmtree(work, ignore_errors=True)
                continue
            sha = run(["git", "-C", str(work), "rev-parse", "HEAD"]).stdout.strip()
            shutil.rmtree(work / ".git", ignore_errors=True)
            missing = [p for p in paths if not (work / p.strip("/")).exists()]
            if missing:
                report.append(f"WARN {repo}: paths not found {missing}")
        # license from the repository's own LICENSE file
        lic_files = [p for p in work.iterdir() if p.is_file() and re.match(r"(?i)(licen[cs]e|copying)", p.name)]
        detected = None
        for lf in lic_files:
            detected = detect_license(lf.read_text(errors="ignore"))
            if detected:
                break
        declared = item.get("license_checked") or item.get("license")
        lic = detected or (declared if item.get("license_checked") else None)
        if not lic or lic not in OPEN:
            shutil.rmtree(work, ignore_errors=True)
            report.append(f"SKIP {repo}: no open license found in LICENSE file (declared: {declared}); link only")
            continue
        if declared and detected and str(declared).split()[0].upper().replace(" ", "-") not in detected.upper():
            report.append(f"NOTE {repo}: declared '{declared}' but LICENSE file reads as {detected}")
        dropped = []
        for p in list(work.rglob("*")):
            if p.is_file() and p.stat().st_size > FILE_MAX_MB * 1e6:
                dropped.append(str(p.relative_to(work)))
                p.unlink()
        mb = sum(p.stat().st_size for p in work.rglob("*") if p.is_file()) / 1e6
        if mb > LOCAL_MAX_MB:
            shutil.rmtree(work, ignore_errors=True)
            report.append(f"SKIP {repo}: {mb:.0f} MB after sparse checkout exceeds {LOCAL_MAX_MB:.0f} MB; link only")
            continue
        if DRY:
            shutil.rmtree(work, ignore_errors=True)
            report.append(f"WOULD {repo}@{branch} [{lic}] {mb:.1f} MB -> {dest_rel}")
            continue
        (work / "SOURCE.md").write_text(
            f"# Source\n\n- Repository: https://github.com/{repo} (branch `{branch}`)\n- Commit: `{sha}`\n"
            f"- License: {lic} (read from the repository's LICENSE file on {date.today().isoformat()})\n"
            f"- Downloaded: {date.today().isoformat()} for Marketing Analytics course preparation\n"
            f"- Kept: {', '.join(paths) if paths else 'entire repository'} (plus top-level README/LICENSE/requirements files)\n"
            + (f"- Omitted files over {FILE_MAX_MB:.0f} MB: {', '.join(dropped)}\n" if dropped else "")
            + "\nThis is a reference snapshot: notebooks have not been re-run here, and saved outputs are the author's. "
              "Follow the upstream license when reusing or redistributing; some repositories license code and prose differently.\n")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(work, dest)
        shutil.rmtree(work, ignore_errors=True)
        for i in item.get("ids", []):
            local[i] = dest_rel
        report.append(f"OK   {repo} [{lic}] -> {dest_rel} ({mb:.1f} MB)" + (f"; dropped {len(dropped)} large file(s)" if dropped else ""))
        out_json.write_text(json.dumps(local, indent=1))
    if not DRY:
        out_json.write_text(json.dumps(local, indent=1))
    print("\n".join(report))


if __name__ == "__main__":
    main()
