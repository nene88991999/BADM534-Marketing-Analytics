"""Build the public index and original review cards from the local acquisition ledger."""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
from collect import LIBRARY, RAW, JOURNALS, date, plain
from download import excluded

HERE = Path(__file__).resolve().parent
FEATURES = ['attention_salience', 'framing_reference', 'social_cues', 'emotion_identity',
            'opacity_disclosure', 'personalization', 'privacy_control', 'defaults_order',
            'exit_search_friction', 'habits_rewards', 'financial_commitment', 'delegation_control']


def csv_file(path, rows, fields=None):
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields or list(rows[0]), extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    records = json.loads((RAW / 'crossref_records.json').read_text())
    ledger = {r['doi']: r for r in json.loads((LIBRARY / 'access_ledger.json').read_text())}
    reviews = json.loads((HERE / 'reviewed_summaries.json').read_text())
    evidence = json.loads((HERE / 'review_evidence.json').read_text())
    resources, coded = [], []
    for i, record in enumerate(records):
        doi = record['DOI'].lower()
        access = ledger[doi]
        if i == 741:
            access['version'] = '2021 dissertation chapter; earlier related version, not version of record'
        access['research_screen_eligible'] = not excluded(plain(record['title'][0]))
        row = {k: access.get(k, '') for k in ['id', 'doi', 'journal', 'title', 'authors',
               'online_date', 'print_date', 'download_status', 'version', 'license', 'source_url',
               'local_pdf', 'abstract_available', 'research_screen_eligible']}
        row.update(census_index=i, url='https://doi.org/' + doi, review_status='not_reviewed',
                   managerial_implications='', agency_assessment='', evidence_basis='', review_card='')
        for feature in FEATURES:
            row[feature] = ''
        if str(i) in reviews:
            summary, status, features, assessment = reviews[str(i)]
            assert set(features) <= set(FEATURES)
            basis = 'Publisher abstract deposited in Crossref; preliminary interpretation'
            if record['journal_code'] == 'MS' and access['download_status'] == 'downloaded':
                basis = 'Abstract in the retrieved full-text version; methods and results not exhaustively assessed'
            if i in [549, 639, 698, 725]:
                basis = 'Publisher or author abstract verified on the primary source page; preliminary interpretation'
            if i in [602, 788, 876, 877, 883]:
                basis = 'Full abstract in Crossref or OpenAlex metadata; preliminary interpretation'
            basis = evidence.get(str(i), basis)
            row.update(review_status=status, managerial_implications=summary,
                       agency_assessment=assessment, evidence_basis=basis)
            for feature in FEATURES:
                row[feature] = int(feature in features)
            card = Path(JOURNALS[record['journal_code']][0].replace(' ', '_')) / 'summaries' / (access['id'] + '.md')
            row['review_card'] = str(card)
            path = LIBRARY / card
            path.parent.mkdir(parents=True, exist_ok=True)
            body = f'# {row["title"]}\n\n{row["authors"]}. {JOURNALS[row["journal"]][0]}. [DOI]({row["url"]}).\n\n'
            body += f'Online publication: {row["online_date"] or "not recorded"}. Issue publication: {row["print_date"] or "not recorded"}.\n\n'
            body += f'## Managerial Implications\n\n{summary}\n\n## Consumer Agency\n\n{assessment}\n\n'
            body += f'Assessment: {status.replace("_", " ")}. Mechanism features: {", ".join(features) or "none coded"}. '
            body += 'A potential misuse is an analytical inference, not a claim about the authors\' intentions or proof of harm.\n\n'
            body += f'## Evidence and Access\n\n{basis}. Access status: {row["download_status"].replace("_", " ")}. '
            if row['download_status'] == 'downloaded':
                body += f'Retrieved version: {row["version"]}. The local research-copy path is recorded in the access ledger. '
            body += 'Original article and version details are available through the DOI and the [access ledger](../../access_ledger.csv).\n'
            path.write_text(body)
            coded.append(row)
        if row['download_status'] == 'downloaded':
            assert row['review_status'] != 'not_reviewed', (i, row['title'])
        resources.append(row)
    (LIBRARY / 'access_ledger.json').write_text(json.dumps(list(ledger.values()), ensure_ascii=False, indent=2) + '\n')
    (LIBRARY / 'catalog.json').write_text(json.dumps({'resources': resources}, ensure_ascii=False, indent=2) + '\n')
    csv_file(LIBRARY / 'catalog.csv', resources)
    csv_file(HERE / 'coded_papers.csv', coded)
    csv_file(LIBRARY / 'access_ledger.csv', list(ledger.values()), [
        'id','doi','journal','title','online_date','print_date','download_status','source_url',
        'version','license','local_pdf','sha256','text_characters','title_token_coverage'])
    gaps = [r for r in resources if r['research_screen_eligible'] and r['download_status'] != 'downloaded']
    csv_file(LIBRARY / 'access_gaps.csv', gaps)
    overview = ['# Journal Article Index', '', 'Coverage: issue publication or online publication in 2023 through November 5, 2026. Each DOI appears once. The inclusion of a record does not establish full-text access or review.', '']
    for code, (name, _, _) in JOURNALS.items():
        subset = [r for r in resources if r['journal'] == code]
        overview += [f'## {name}', '', '| Paper | Online / Issue Date | Access | Review |', '| --- | --- | --- | --- |']
        for r in subset:
            title = r['title'].replace('|', '\\|')
            review = f'[Summary]({r["review_card"]})' if r['review_card'] else 'Not reviewed'
            overview.append(f'| [{title}]({r["url"]}) | {r["online_date"]} / {r["print_date"]} | {r["download_status"].replace("_", " ")} | {review} |')
        overview.append('')
        folder = LIBRARY / name.replace(' ', '_')
        folder.mkdir(exist_ok=True)
        (folder / 'README.md').write_text(f'# {name}\n\n{len(subset)} DOI records. '
            f'{sum(r["download_status"] == "downloaded" for r in subset)} retrieved research copies. '
            f'{sum(bool(r["review_card"]) for r in subset)} original managerial and agency summaries.\n\n'
            'See the [article index](../CATALOG.md), [access ledger](../access_ledger.csv), and [review protocol](../README.md). '
            'Full texts with unverified redistribution rights remain in the Dropbox-only `local_papers/` directory.\n')
    (LIBRARY / 'CATALOG.md').write_text('\n'.join(overview))
    counts = {'doi_records': len(resources), 'screen_eligible': sum(r['research_screen_eligible'] for r in resources),
              'downloaded': sum(r['download_status'] == 'downloaded' for r in resources), 'access_gaps': len(gaps),
              'reviewed': len(coded), 'review_statuses': dict(Counter(r['review_status'] for r in coded)),
              'journals': {c: dict(Counter(r['download_status'] for r in resources if r['journal'] == c)) for c in JOURNALS}}
    (LIBRARY / 'coverage.json').write_text(json.dumps(counts, indent=2) + '\n')
    print(json.dumps(counts, indent=2))


if __name__ == '__main__':
    main()
