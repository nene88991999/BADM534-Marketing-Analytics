#!/usr/bin/env python3
"""Public signals of demand for generative-AI services (companion to Egan, Russel, Shi and Yao, NBER w35953).

The paper measures *paid* adoption, plan tiers, multihoming, retention and switching from card
transactions of 174 million consumers. No public source has that. What is public, documented and
free is a set of *proxies* for the same objects, each one request away:

    Apple App Store top charts      adoption / rank of each assistant app, daily, by country   (no key)
    Wikipedia pageviews             attention to each service, daily since 2015               (no key)
    OpenRouter models API           API-side prices per million tokens, hundreds of models    (no key)
    Wayback Machine CDX API         history of each provider's consumer pricing page          (no key)
    Epoch AI notable models (CSV)   model release dates, for "switching around releases"      (CC BY)
    Cloudflare Radar                popularity ranking of generative-AI services by traffic   (free token)

Usage
-----
    python collect_genai_signals.py --all --out data
    python collect_genai_signals.py --apple --wikipedia --since 2024-01-01
    python collect_genai_signals.py --wayback-list https://claude.com/pricing --since 2024-01-01
    python collect_genai_signals.py --cloudflare --cf-token $CF_API_TOKEN

Every collector is a plain function returning a pandas DataFrame, so the notebook can import them.
Each one sends an honest User-Agent, sets a timeout, checks the status code, and is wrapped in
try/except at the CLI level, so one blocked host does not stop the others. Requests are small:
one call per source per run. Do not loop these in a tight loop; daily is plenty.
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import sys
from pathlib import Path

import pandas as pd
import requests

UA = "BADM534-genai-demand-lab/1.0 (University of Illinois course use; contact instructor)"
TIMEOUT = 30
HERE = Path(__file__).resolve().parent

# App Store ids verified from the live top-free feed on 2026-10-26 (see data/ai_apps_appstore.csv).
AI_APPS = {
    6448311069: ("ChatGPT", "OpenAI"),
    6473753684: ("Claude", "Anthropic"),
    6477489729: ("Google Gemini", "Google"),
    6670324846: ("Grok AI", "xAI"),
    6794501026: ("Grok Bot", "xAI"),
    541164041: ("Microsoft Copilot", "Microsoft"),
    1668000334: ("Perplexity", "Perplexity"),
}
WIKI_ARTICLES = {           # English Wikipedia article titles (as of 2026-10); check if a page is renamed
    "ChatGPT": "OpenAI",
    "Claude_(language_model)": "Anthropic",
    "Gemini_(chatbot)": "Google",
    "Microsoft_Copilot": "Microsoft",
    "Perplexity_AI": "Perplexity",
    "Grok_(chatbot)": "xAI",
}
PRICING_PAGES = {            # consumer pricing pages for the Wayback exercise
    "OpenAI": "https://chatgpt.com/pricing",
    "OpenAI (old)": "https://openai.com/chatgpt/pricing",
    "Anthropic": "https://claude.com/pricing",
    "Anthropic (old)": "https://www.anthropic.com/pricing",
    "Google": "https://one.google.com/about/google-ai-plans/",
    "Google (old)": "https://one.google.com/about/ai-premium/",
    "Perplexity": "https://www.perplexity.ai/pro",
    "xAI": "https://x.ai/grok",
}
PROVIDERS_OF_INTEREST = ["OpenAI", "Anthropic", "Google", "Google DeepMind", "xAI", "Microsoft", "Meta AI", "Meta", "Perplexity", "DeepSeek", "Mistral AI"]


def _get(url: str, params: dict | None = None, headers: dict | None = None) -> requests.Response:
    h = {"User-Agent": UA, "Accept": "application/json, text/csv, */*"}
    if headers:
        h.update(headers)
    r = requests.get(url, params=params, headers=h, timeout=TIMEOUT)
    r.raise_for_status()
    return r


# --------------------------------------------------------------------------- 1. Apple App Store top charts

def apple_top_chart(country: str = "us", chart: str = "top-free", limit: int = 100) -> pd.DataFrame:
    """Apple's RSS feed generator (https://rss.marketingtools.apple.com). ``chart`` is 'top-free' or 'top-paid';
    there is no top-grossing feed in this API. Returns every app with its rank, flagging the AI assistants."""
    url = f"https://rss.marketingtools.apple.com/api/v2/{country}/apps/{chart}/{limit}/apps.json"
    return parse_apple_feed(_get(url).json()["feed"], country, chart)


def parse_apple_feed(feed: dict, country: str = "us", chart: str = "top-free") -> pd.DataFrame:
    rows = []
    for rank, a in enumerate(feed["results"], start=1):
        app_id = int(a["id"])
        rows.append({"captured_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                     "feed_updated": feed.get("updated"), "country": country, "chart": chart, "rank": rank,
                     "app_id": app_id, "name": a["name"], "developer": a.get("artistName"),
                     "release_date": a.get("releaseDate"), "ai_assistant": app_id in AI_APPS,
                     "provider": AI_APPS.get(app_id, (None, None))[1]})
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- 2. Wikipedia pageviews

def wikipedia_resolve(titles: list, project: str = "en.wikipedia") -> dict:
    """Map each title to the article it currently redirects to (MediaWiki Action API, action=query&redirects=1).
    Articles get renamed: 'Claude (language model)' became 'Claude (AI)' and 'Gemini (chatbot)' became
    'Google Gemini' in 2026. Pageviews are counted per title, so a renamed article's series collapses to
    near zero on the old title and starts on the new one. Query both and add them."""
    r = _get(f"https://{project}.org/w/api.php", params={"action": "query", "titles": "|".join(titles), "redirects": 1, "format": "json"}).json()
    q = r.get("query", {})
    norm = {x["from"]: x["to"] for x in q.get("normalized", [])}
    redir = {x["from"]: x["to"] for x in q.get("redirects", [])}
    out = {}
    for t in titles:
        cur = norm.get(t, t.replace("_", " "))
        cur = redir.get(cur, cur)
        out[t] = cur.replace(" ", "_")
    return out


def wikipedia_pageviews(articles: dict | list = WIKI_ARTICLES, start: str = "2022-11-01", end: str | None = None,
                        project: str = "en.wikipedia", granularity: str = "daily", follow_redirects: bool = True) -> pd.DataFrame:
    """Wikimedia REST API (https://wikimedia.org/api/rest_v1/#/Pageviews%20data). Agent 'user' excludes spiders;
    days with zero views are omitted by the API. Wikimedia asks for a descriptive User-Agent."""
    end = end or dt.date.today().isoformat()
    s, e = start.replace("-", ""), end.replace("-", "")
    arts = articles if isinstance(articles, dict) else {a: None for a in articles}
    targets = wikipedia_resolve(list(arts), project) if follow_redirects else {a: a for a in arts}
    frames = []
    for title, provider in arts.items():
        for t in dict.fromkeys([title, targets.get(title, title)]):       # old title first, then its current target
            url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/all-access/user/"
                   f"{requests.utils.quote(t, safe='')}/{granularity}/{s}/{e}")
            try:
                items = _get(url).json().get("items", [])
            except requests.HTTPError as err:                              # 404 = no views recorded for that title
                if err.response is not None and err.response.status_code == 404:
                    continue
                raise
            f = pd.DataFrame(items)
            if f.empty:
                continue
            f["date"] = pd.to_datetime(f["timestamp"].str[:8])
            f["provider"] = provider
            f["requested_title"] = title
            frames.append(f[["date", "article", "requested_title", "provider", "views"]])
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=["date", "article", "requested_title", "provider", "views"])


# --------------------------------------------------------------------------- 3. OpenRouter model prices

def openrouter_models() -> pd.DataFrame:
    """https://openrouter.ai/api/v1/models (no key). Prices are USD per token as strings; converted to USD per
    million tokens. This is the API side of the market, the one Fradkin (2025) studies with OpenRouter data."""
    data = _get("https://openrouter.ai/api/v1/models").json()["data"]
    rows = []
    for m in data:
        p = m.get("pricing", {}) or {}
        def per_m(x):
            try:
                v = float(x)
                return None if v < 0 else v * 1e6
            except (TypeError, ValueError):
                return None
        mid = str(m.get("id", ""))
        rows.append({"captured_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                     "model_id": mid, "name": m.get("name"), "provider": mid.lstrip("~").split("/")[0],
                     "variant": mid.split(":")[1] if ":" in mid else "standard",
                     "created": pd.to_datetime(m.get("created"), unit="s", utc=True).date() if m.get("created") else None,
                     "context_length": m.get("context_length"),
                     "usd_per_m_input": per_m(p.get("prompt")), "usd_per_m_output": per_m(p.get("completion"))})
    return pd.DataFrame(rows)


def release_events_from_openrouter(models: pd.DataFrame, providers: tuple = ("openai", "anthropic", "google", "x-ai")) -> pd.DataFrame:
    """A cheap, dated list of model launches: the day each standard (non-batch, non-free) model of the big
    consumer providers was listed on OpenRouter. Listing usually lags the public launch by hours, not weeks
    (Claude Haiku 5.5: announced 7 Oct 2026, listed 7 Oct 2026). Use Epoch AI's table when you need the
    official dates."""
    m = models[(models["variant"] == "standard") & models["provider"].isin(providers) & ~models["model_id"].str.startswith("~")]
    m = m[~m["model_id"].str.contains("image|audio|lyria|codex|oss|guard|safeguard|chat-latest|build", case=False)]
    return m[["created", "provider", "model_id", "usd_per_m_input", "usd_per_m_output"]].sort_values("created").reset_index(drop=True)


# --------------------------------------------------------------------------- 4. Wayback Machine (pricing-page history)

def wayback_snapshots(url: str, start: str = "2023-01-01", end: str | None = None, collapse: str = "timestamp:8") -> pd.DataFrame:
    """List archived captures of ``url`` via the CDX API (docs: github.com/internetarchive/wayback, wayback-cdx-server).
    ``collapse='timestamp:8'`` keeps one capture per day. Each row's ``archive_url`` serves the archived page."""
    end = end or dt.date.today().isoformat()
    params = {"url": url, "output": "json", "from": start.replace("-", ""), "to": end.replace("-", ""),
              "filter": "statuscode:200", "collapse": collapse, "fl": "timestamp,original,statuscode,digest"}
    rows = _get("https://web.archive.org/cdx/search/cdx", params=params).json()
    if not rows:
        return pd.DataFrame(columns=["timestamp", "original", "statuscode", "digest", "captured", "archive_url"])
    f = pd.DataFrame(rows[1:], columns=rows[0])
    f["captured"] = pd.to_datetime(f["timestamp"], format="%Y%m%d%H%M%S")
    f["archive_url"] = "https://web.archive.org/web/" + f["timestamp"] + "id_/" + f["original"]
    return f


def wayback_fetch_text(timestamp: str, url: str) -> str:
    """Return the archived page's visible text (tags stripped) so prices can be read or regex-searched.
    'id_' asks for the original bytes without the Wayback toolbar."""
    import re
    html = _get(f"https://web.archive.org/web/{timestamp}id_/{url}", headers={"Accept": "text/html"}).text
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text)


# --------------------------------------------------------------------------- 5. Epoch AI model releases

def epoch_notable_models(providers: list = PROVIDERS_OF_INTEREST, since: str = "2022-11-01") -> pd.DataFrame:
    """Epoch AI's 'Notable AI models' table, CC BY 4.0 (https://epoch.ai/data/notable-ai-models). Used here as the
    event list for 'switching rises around major model releases'."""
    csv = _get("https://epoch.ai/data/notable_ai_models.csv", headers={"Accept": "text/csv"}).text
    f = pd.read_csv(io.StringIO(csv))
    f = f.rename(columns={"Model": "model", "Organization": "organization", "Publication date": "release_date"})
    f["release_date"] = pd.to_datetime(f["release_date"], errors="coerce")
    keep = f["organization"].fillna("").apply(lambda s: any(p.lower() in s.lower() for p in providers))
    cols = [c for c in ["model", "organization", "release_date", "Domain", "Model accessibility", "Frontier model", "Link"] if c in f.columns]
    return f.loc[keep & (f["release_date"] >= since), cols].sort_values("release_date").reset_index(drop=True)


# --------------------------------------------------------------------------- 6. Cloudflare Radar

def cloudflare_internet_services(token: str, service_category: str | None = "Generative AI", limit: int = 20,
                                 date: str | None = None) -> pd.DataFrame:
    """Radar's ranking of Internet services by traffic (https://developers.cloudflare.com/api/resources/radar/).
    Needs a free API token with 'User Details Read'. Call the categories endpoint first to confirm the exact
    category label; it is 'Generative AI' in Radar's public reports."""
    base = "https://api.cloudflare.com/client/v4/radar/ranking/internet_services"
    h = {"Authorization": f"Bearer {token}"}
    cats = _get(f"{base}/categories", headers=h).json()
    params = {"limit": limit}
    if service_category:
        params["serviceCategory"] = service_category
    if date:
        params["date"] = date
    res = _get(f"{base}/top", params=params, headers=h).json()["result"]
    f = pd.DataFrame(res["top_0"])
    f["date"] = res["meta"].get("top_0", {}).get("date") or date
    f["service_category"] = service_category
    f.attrs["categories"] = cats
    return f


# --------------------------------------------------------------------------- CLI

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apple", action="store_true")
    ap.add_argument("--wikipedia", action="store_true")
    ap.add_argument("--openrouter", action="store_true")
    ap.add_argument("--epoch", action="store_true")
    ap.add_argument("--wayback-list", metavar="URL", help="list archived captures of a pricing page")
    ap.add_argument("--cloudflare", action="store_true")
    ap.add_argument("--cf-token", default=None)
    ap.add_argument("--country", default="us")
    ap.add_argument("--since", default="2022-11-01")
    ap.add_argument("--out", default="data")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    stamp = dt.date.today().isoformat()

    jobs = []
    if a.all or a.apple:
        jobs.append(("apple_top_free", lambda: apple_top_chart(a.country, "top-free", 100), f"apple_top_free_{a.country}_{stamp}.csv"))
        jobs.append(("apple_top_paid", lambda: apple_top_chart(a.country, "top-paid", 100), f"apple_top_paid_{a.country}_{stamp}.csv"))
    if a.all or a.wikipedia:
        jobs.append(("wikipedia_pageviews", lambda: wikipedia_pageviews(start=a.since), f"wikipedia_pageviews_{stamp}.csv"))
    if a.all or a.openrouter:
        jobs.append(("openrouter_models", openrouter_models, f"openrouter_models_{stamp}.csv"))
        jobs.append(("openrouter_release_events", lambda: release_events_from_openrouter(pd.read_csv(out / f"openrouter_models_{stamp}.csv")), f"model_releases_openrouter_{stamp}.csv"))
    if a.all or a.epoch:
        jobs.append(("epoch_releases", lambda: epoch_notable_models(since=a.since), f"model_releases_epoch_{stamp}.csv"))
    if a.wayback_list:
        jobs.append(("wayback", lambda: wayback_snapshots(a.wayback_list, a.since), f"wayback_{stamp}.csv"))
    if a.all or a.cloudflare:
        if a.cf_token:
            jobs.append(("cloudflare_genai", lambda: cloudflare_internet_services(a.cf_token), f"cloudflare_genai_ranking_{stamp}.csv"))
        else:
            print("[skip] cloudflare: pass --cf-token (free token from dash.cloudflare.com)", file=sys.stderr)
    for name, fn, fname in jobs:
        try:
            df = fn()
            df.to_csv(out / fname, index=False)
            print(f"OK   {name}: {len(df):,} rows -> {out / fname}")
        except Exception as e:  # noqa: BLE001
            print(f"FAIL {name}: {type(e).__name__}: {str(e)[:160]}", file=sys.stderr)


if __name__ == "__main__":
    main()
