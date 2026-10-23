#!/usr/bin/env python3
"""Download openly licensed GitHub material listed in 00_Index/_data/downloads.yaml.

Usage (from 00_Index):  python3 _build/fetch_repos.py [--dry-run] [--only owner/repo,...] [--start k --count n]

For each plan item it checks the repo's license with the GitHub API, makes a shallow sparse clone in a
scratch directory outside Dropbox, keeps only the requested subpaths (plus root README/LICENSE files),
and copies the result to <folder>/repos/<owner>__<repo>/ with a SOURCE.md recording origin, commit and
license. Results are recorded in 00_Index/_data/local_copies.json, which build_catalog.py reads.
"""
import base64
import json
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

DRY = "--dry-run" in sys.argv
ONLY = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
LOCAL_MAX_MB = 60
SCRATCH = Path.home() / "_badm534_dl"
OPEN = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "Unlicense",
        "GPL-2.0", "GPL-3.0", "LGPL-3.0", "MPL-2.0", "ISC", "CC-BY-NC-4.0", "CC-BY-NC-SA-4.0", "CC-BY-NC-ND-4.0",
        "AGPL-3.0", "BSL-1.0", "0BSD"}
LICENSE_WORDS = {"CC-BY-4.0": "Attribution 4.0", "CC-BY-NC-4.0": "NonCommercial", "MIT": "MIT License",
                 "Apache-2.0": "Apache License"}


def gh(path):
    req = urllib.request.Request(f"https://api.github.com/{path}",
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "badm534-catalog"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=170)


def main():
    plan = yaml.safe_load((ROOT / "00_Index" / "_data" / "downloads.yaml").read_text())
    if "--start" in sys.argv:
        s = int(sys.argv[sys.argv.index("--start") + 1])
        n = int(sys.argv[sys.argv.index("--count") + 1]) if "--count" in sys.argv else 5
        plan = plan[s:s + n]
    out_json = ROOT / "00_Index" / "_data" / "local_copies.json"
    local = json.loads(out_json.read_text()) if out_json.exists() else {}
    SCRATCH.mkdir(exist_ok=True)
    report = []
    for item in plan:
        repo = item["repo"]
        if ONLY and repo not in ONLY:
            continue
        owner, name = repo.split("/")
        dest_rel = f"{FOLDERS[item['dest']][0]}/repos/{item.get('as') or owner + '__' + name}"
        dest = ROOT / dest_rel
        if dest.exists():
            report.append(f"HAVE {repo} -> {dest_rel}")
            for i in item.get("ids", []):
                local[i] = dest_rel
            continue
        try:
            meta = gh(f"repos/{repo}")
            lic = (meta.get("license") or {}).get("spdx_id") or "NOASSERTION"
        except Exception as ex:  # noqa: BLE001
            # API unavailable (e.g. rate limit): fall back to a license recorded in the plan from an earlier check
            if not (item.get("license_checked") and item.get("branch")):
                report.append(f"SKIP {repo}: API error {ex}")
                continue
            meta = {"default_branch": item["branch"], "clone_url": f"https://github.com/{repo}.git", "size": 0}
            lic = item["license_checked"]
        if lic not in OPEN and not item.get("license_checked"):
            trust = item.get("trust_license")
            ok = False
            if trust:
                try:
                    txt = base64.b64decode(gh(f"repos/{repo}/license")["content"]).decode("utf-8", "ignore")
                    ok = LICENSE_WORDS.get(trust, trust).lower() in txt.lower()
                except Exception:  # noqa: BLE001
                    ok = False
            if not ok:
                report.append(f"SKIP {repo}: license {lic} not confirmed open")
                continue
            lic = f"{trust} (from LICENSE file; GitHub reports {lic})"
        branch = item.get("branch") or meta["default_branch"]
        if DRY:
            report.append(f"WOULD {repo}@{branch} [{lic}, repo {meta['size'] / 1024:.0f} MB] paths={item.get('paths') or item.get('files') or 'ALL'} -> {dest_rel}")
            continue
        work = SCRATCH / dest.name
        shutil.rmtree(work, ignore_errors=True)
        sha = ""
        if item.get("files"):
            work.mkdir(parents=True)
            for fpath in item["files"]:
                url = f"https://raw.githubusercontent.com/{repo}/{branch}/{fpath}"
                target = work / fpath
                target.parent.mkdir(parents=True, exist_ok=True)
                with urllib.request.urlopen(url, timeout=60) as r:
                    target.write_bytes(r.read())
            ls = run(["git", "ls-remote", f"https://github.com/{repo}.git", branch]).stdout.split()
            sha = ls[0] if ls else "unknown"
            paths = item["files"]
        else:
            paths = item.get("paths") or []
            cmd = ["git", "clone", "--depth", "1", "--filter=blob:none", "--branch", branch]
            cmd += (["--sparse"] if paths else []) + [meta["clone_url"], str(work)]
            r = run(cmd)
            if r.returncode:
                report.append(f"FAIL {repo}: {r.stderr.strip()[-200:]}")
                continue
            if paths:
                r = run(["git", "-C", str(work), "sparse-checkout", "set", *paths])
                if r.returncode:
                    report.append(f"FAIL {repo} sparse: {r.stderr.strip()[-200:]}")
                    continue
            sha = run(["git", "-C", str(work), "rev-parse", "HEAD"]).stdout.strip()
            shutil.rmtree(work / ".git", ignore_errors=True)
            missing = [p for p in paths if not (work / p).exists()]
            if missing:
                report.append(f"WARN {repo}: paths not found {missing}")
        dropped = []
        for p in list(work.rglob("*")):
            if p.is_file() and p.stat().st_size > 40e6:
                dropped.append(str(p.relative_to(work)))
                p.unlink()
        mb = sum(p.stat().st_size for p in work.rglob("*") if p.is_file()) / 1e6
        if mb > LOCAL_MAX_MB:
            shutil.rmtree(work, ignore_errors=True)
            report.append(f"SKIP {repo}: {mb:.0f} MB after sparse checkout exceeds {LOCAL_MAX_MB} MB; link only")
            continue
        (work / "SOURCE.md").write_text(
            f"# Source\n\n- Repository: https://github.com/{repo} (branch `{branch}`)\n- Commit: `{sha}`\n"
            f"- License: {lic}\n- Downloaded: {date.today().isoformat()} for Marketing Analytics course preparation\n"
            f"- Kept: {', '.join(paths) if paths else 'entire repository'} (plus top-level README/LICENSE files)\n"
            + (f"- Omitted files over 40 MB: {', '.join(dropped)}\n" if dropped else "")
            + "\nThis is a snapshot. Check upstream for updates, and follow the upstream license when reusing or "
              "redistributing this material. Some repositories license code and prose differently; see the upstream README.\n")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(work, dest)
        shutil.rmtree(work, ignore_errors=True)
        for i in item.get("ids", []):
            local[i] = dest_rel
        report.append(f"OK   {repo} [{lic}] -> {dest_rel} ({mb:.1f} MB)")
        out_json.write_text(json.dumps(local, indent=1))
    if not DRY:
        out_json.write_text(json.dumps(local, indent=1))
    print("\n".join(report))


if __name__ == "__main__":
    main()
