"""Retrieve explicitly identified author/repository copies after the indexed pass."""
import json
from collect import RAW, LIBRARY
from download import download

SOURCES = {
    28: ('https://nposner12.github.io/website/reeck2023.pdf', 'author_manuscript'),
    142: ('https://osuva.uwasa.fi/server/api/core/bitstreams/c12e2452-2f88-4703-ad5d-0d0b16f4e580/content', 'publishedVersion'),
    639: ('https://robdonnelly.me/files/personalized_rankings.pdf', 'publishedVersion'),
    725: ('https://spinup-000d1a-wp-offload-media.s3.amazonaws.com/faculty/wp-content/uploads/sites/32/2024/06/Targeted_Advertising_as_Recommendation__Jiwoong_.pdf', 'author_manuscript'),
}


def main():
    records = json.loads((RAW / 'crossref_records.json').read_text())
    ledger = json.loads((LIBRARY / 'access_ledger.json').read_text())
    entries = {r['doi']: r for r in ledger}
    for i, (url, version) in SOURCES.items():
        record = dict(records[i])
        old = entries[record['DOI'].lower()]
        if old['download_status'] == 'downloaded':
            continue
        path = RAW / 'access' / (old['id'] + '.json')
        backup = RAW / 'access' / (old['id'] + '.indexed.json')
        if not backup.exists():
            path.replace(backup)
        else:
            path.unlink(missing_ok=True)
        record['link'] = [{'URL': url, 'content-type': 'application/pdf'}]
        new = download(record, {})
        new['attempts'] = old['attempts'] + new['attempts']
        new['version'] = version if new['download_status'] == 'downloaded' else ''
        if new['download_status'] == 'downloaded':
            new['license'] = 'unspecified; local research copy'
        path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
        entries[new['doi']] = new
        print(i, new['download_status'], flush=True)
    (LIBRARY / 'access_ledger.json').write_text(json.dumps(list(entries.values()), ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
