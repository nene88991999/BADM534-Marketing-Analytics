"""Retrieve publisher PDFs and OA repository copies without access-control bypass.

Read the ledger before retrying a failed host. Raw HTML/PDF remains local.
"""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import csv
import hashlib
import json
import os
import re
import subprocess
import threading
from urllib.parse import urljoin, urlparse
from collect import LIBRARY, RAW, JOURNALS, date, plain

HOST_LOCKS, BLOCKED, GUARD = {}, set(), threading.Lock()
PDFTOTEXT = os.environ.get('AGENCY_PDFTOTEXT', 'pdftotext')


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pdfs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name', '').lower() in {'citation_pdf_url', 'eprints.document_url'}:
            self.pdfs.append(attrs.get('content', ''))
        if tag == 'a':
            href = attrs.get('href', '')
            if re.search(r'\.pdf(?:\?|$)|/bitstreams/[^/]+/download', href, re.I):
                self.pdfs.append(href)


def get(url, target):
    host = urlparse(url).netloc
    with GUARD:
        lock = HOST_LOCKS.setdefault(host, threading.Lock())
    with lock:
        if host in BLOCKED:
            return 'host_access_blocked'
        result = subprocess.run(['curl', '-LsS', '--max-time', '30', '--max-filesize', '50000000',
                                 '-A', 'MarketingAnalyticsTeachingResearch/1.0', '-w', '%{http_code}',
                                 url, '-o', str(target)], capture_output=True, text=True)
        status = result.stdout.strip()
        if status in {'401', '403', '429'}:
            BLOCKED.add(host)
        return status if result.returncode == 0 else f'curl_{result.returncode}_{status}'


def filename(record):
    names = '_'.join(a.get('family', 'Unknown').replace(' ', '-') for a in record.get('author', [])) or 'Editorial'
    names = re.sub(r'[^\w\-]', '_', names, flags=re.U)[:170]
    year = (date(record, 'published-print') or date(record, 'published'))[:4]
    return f'{names}_{record["journal_code"]}{year}_{hashlib.sha256(record["DOI"].encode()).hexdigest()[:8]}.pdf'


def excluded(title):
    return bool(re.search(r'^(Editorial Board|Focus on Authors|Acknowledgments|Retraction Notice|Corrigendum|Erratum|Expression of Concern|RETRACTED:)|Service Awards|Guest Associate Editors|Ad Hoc Reviewers', title, re.I))


def download(record, work):
    doi, title, journal = record['DOI'].lower(), plain(record['title'][0]), record['journal_code']
    key = journal + '-' + hashlib.sha256(doi.encode()).hexdigest()[:8]
    ledger_path = RAW / 'access' / (key + '.json')
    if ledger_path.exists():
        return json.loads(ledger_path.read_text())
    entry = {'id': key, 'doi': doi, 'journal': journal, 'title': title,
             'online_date': date(record, 'published-online'), 'print_date': date(record, 'published-print'),
             'authors': '; '.join(' '.join([a.get('given', ''), a.get('family', '')]).strip() for a in record.get('author', [])),
             'research_screen_eligible': not excluded(title), 'abstract_available': bool(record.get('abstract') or work.get('abstract_inverted_index')),
             'download_status': 'unavailable', 'local_pdf': '', 'version': '', 'license': '',
             'oa_reported': work.get('open_access', {}).get('is_oa', False), 'attempts': []}
    locations = work.get('locations', [])
    candidates = []
    for link in record.get('link', []):
        if link.get('content-type') == 'application/pdf':
            licenses = [l['URL'] for l in record.get('license', []) if 'creativecommons.org' in l['URL']]
            candidates.append((link['URL'], 'publishedVersion', '; '.join(licenses), True))
            break
    for loc in locations:
        if loc.get('is_oa'):
            for field in ['pdf_url', 'landing_page_url']:
                if loc.get(field):
                    candidates.append((loc[field], loc.get('version', ''), loc.get('license', ''), field == 'pdf_url'))
    seen = set()
    target_dir = LIBRARY / JOURNALS[journal][0].replace(' ', '_') / 'local_papers'
    target_dir.mkdir(parents=True, exist_ok=True)
    temporary = RAW / 'access' / (key + '.part')
    (RAW / 'access').mkdir(parents=True, exist_ok=True)
    if not entry['research_screen_eligible']:
        entry['download_status'] = 'nonresearch_or_notice'
        candidates = []
    for url, version, license_, is_pdf in candidates:
        if url in seen:
            continue
        seen.add(url)
        status = get(url, temporary)
        entry['attempts'].append({'url': url, 'status': status})
        if status != '200' or not temporary.exists():
            continue
        content = temporary.read_bytes()
        if content.startswith(b'%PDF-'):
            final = target_dir / filename(record)
            temporary.replace(final)
            text_path = RAW / 'texts' / (key + '.txt')
            text_path.parent.mkdir(exist_ok=True)
            extraction = subprocess.run([PDFTOTEXT, '-layout', str(final), str(text_path)], capture_output=True, timeout=60)
            text = text_path.read_text(errors='replace') if text_path.exists() else ''
            title_words = {w for w in re.findall(r'[a-z]+', title.lower()) if len(w) > 3}
            front_words = set(re.findall(r'[a-z]+', text[:20000].lower()))
            match = len(title_words & front_words) / max(len(title_words), 1)
            if match < .75 or len(text) < 6000:
                rejected = RAW / 'rejected' / (key + '_' + hashlib.sha256(content).hexdigest()[:8] + '.pdf')
                rejected.parent.mkdir(exist_ok=True)
                final.replace(rejected)
                entry['attempts'][-1]['identity'] = 'title_or_length_check_failed'
                continue
            entry.update(download_status='downloaded_identity_pending' if match < .75 or len(text) < 6000 else 'downloaded',
                         local_pdf=str(final.relative_to(LIBRARY)), version=version, license=license_ or 'unspecified',
                         source_url=url, sha256=hashlib.sha256(content).hexdigest(),
                         text_characters=len(text), title_token_coverage=round(match, 3),
                         extracted_text=str(text_path.relative_to(LIBRARY)))
            break
        if not is_pdf:
            parser = Links()
            parser.feed(content.decode('utf-8', errors='replace'))
            for href in dict.fromkeys(parser.pdfs):
                candidates.append((urljoin(url, href), version, license_, True))
                if len(candidates) > 35:
                    break
    temporary.unlink(missing_ok=True)
    ledger_path.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + '\n')
    return entry


def main():
    records = json.loads((RAW / 'crossref_records.json').read_text())
    works = json.loads((RAW / 'openalex_records.json').read_text())
    with ThreadPoolExecutor(max_workers=6) as pool:
        entries = []
        for entry in pool.map(lambda r: download(r, works.get(r['DOI'].lower(), {})), records):
            entries.append(entry)
            if len(entries) % 50 == 0:
                print('Processed', len(entries), 'Downloaded', sum(e['download_status'].startswith('downloaded') for e in entries), flush=True)
    (LIBRARY / 'access_ledger.json').write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')
    fields = [k for k in entries[0] if k != 'attempts']
    fields += [k for k in ['source_url', 'sha256', 'text_characters', 'title_token_coverage', 'extracted_text'] if k not in fields]
    with (LIBRARY / 'access_ledger.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        writer.writerows(entries)
    from collections import Counter
    print(dict(Counter(e['download_status'] for e in entries)), flush=True)


if __name__ == '__main__':
    main()
