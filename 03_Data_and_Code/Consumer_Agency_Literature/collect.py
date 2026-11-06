"""Collect a reproducible Crossref census and lawful open-access locations.

Run with Python 3.10+ and curl. Raw responses and full texts stay in Dropbox.
This program downloads data only; it never executes downloaded content.
"""
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
import subprocess
import time
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[2]
LIBRARY = ROOT / '01_Resources/13_Consumer_Agency_and_Recent_Research'
RAW = LIBRARY / 'local_sources'
START, END = '2023-01-01', '2026-11-05'
JOURNALS = {
    'JM': ('Journal of Marketing', '0022-2429', '1547-7185'),
    'JMR': ('Journal of Marketing Research', '0022-2437', '1547-7193'),
    'MS': ('Marketing Science', '0732-2399', '1526-548X'),
}


def fetch(url, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return json.loads(path.read_text())
    temporary = path.with_suffix('.part')
    subprocess.run(['curl', '-fLsS', '--retry', '2', '--max-time', '90',
                    '-A', 'MarketingAnalyticsTeachingResearch/1.0',
                    url, '-o', str(temporary)], check=True)
    data = json.loads(temporary.read_text())
    temporary.replace(path)
    time.sleep(0.3)
    return data


def plain(text):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', text or ''))).strip()


def date(record, key):
    parts = record.get(key, {}).get('date-parts', [[]])[0]
    return '-'.join(f'{p:04d}' if i == 0 else f'{p:02d}' for i, p in enumerate(parts))


def census():
    records, requests = {}, []
    for code, (name, print_issn, electronic_issn) in JOURNALS.items():
        journal = fetch(f'https://api.crossref.org/journals/{print_issn}', RAW / f'{code}_journal.json')['message']
        assert journal['title'].casefold() == name.casefold(), journal['title']
        assert {print_issn, electronic_issn} <= set(journal['ISSN'])
        for field in ['pub', 'print-pub']:
            cursor, count, page = '*', 0, 0
            while True:
                query = urlencode({'filter': f'from-{field}-date:{START},until-{field}-date:{END}',
                                   'rows': 1000, 'cursor': cursor})
                url = f'https://api.crossref.org/journals/{print_issn}/works?{query}'
                response = fetch(url, RAW / f'{code}_{field}_{page}.json')['message']
                items = response['items']
                for item in items:
                    item['journal_code'] = code
                    records[item['DOI'].lower()] = item
                count += len(items)
                if count >= response['total-results'] or not items:
                    requests.append({'journal': code, 'date_filter': field, 'returned': count,
                                     'total_results': response['total-results'], 'url': url})
                    break
                cursor, page = response['next-cursor'], page + 1
            print(code, field, count, flush=True)
    records = sorted(records.values(), key=lambda r: (r['journal_code'], date(r, 'published'), r['DOI']))
    (RAW / 'crossref_records.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
    (LIBRARY / 'retrieval_manifest.json').write_text(json.dumps({
        'retrieved_on': END, 'start': START, 'end': END, 'requests': requests,
        'inclusion': 'Union of Crossref publication-date and print-publication-date queries; DOI deduplicated.',
        'unique_records': len(records),
    }, indent=2) + '\n')
    print('Unique DOI records:', len(records), 'With abstract:', sum(bool(r.get('abstract')) for r in records))


def openalex():
    records = json.loads((RAW / 'crossref_records.json').read_text())
    enriched = {}
    for start in range(0, len(records), 40):
        dois = '|'.join('https://doi.org/' + r['DOI'] for r in records[start:start + 40])
        query = urlencode({'filter': 'doi:' + dois, 'per_page': 100})
        result = fetch('https://api.openalex.org/works?' + query, RAW / f'openalex_{start:04d}.json')
        for work in result['results']:
            enriched[work['doi'].removeprefix('https://doi.org/').lower()] = work
        print('OpenAlex', start, len(result['results']), flush=True)
    (RAW / 'openalex_records.json').write_text(json.dumps(enriched, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('step', choices=['census', 'openalex'])
    args = parser.parse_args()
    {'census': census, 'openalex': openalex}[args.step]()
